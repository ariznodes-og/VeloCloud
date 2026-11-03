#!/usr/bin/env bash
# ArizNodes network repair — lets LXD containers reach the internet.
# Fixes the usual blockers: IP forwarding off, Docker's FORWARD DROP policy, ufw / firewalld, LXD NAT, broken DNS.
# Usage: netfix.sh [--no-test | --test-only]
export PATH=$PATH:/snap/bin:/usr/sbin:/sbin
MODE="$1"; SYSCTL_DIR="${ARIZ_SYSCTL_DIR:-/etc/sysctl.d}"
say() { echo "  • $*"; }
command -v lxc >/dev/null 2>&1 || { echo "  ✘ lxc not found — install LXD first (snap install lxd && lxd init --auto)"; exit 2; }
BR="$(lxc network list --format csv 2>/dev/null | awk -F, '$2=="bridge" && $3=="YES" {print $1; exit}')"; BR="${BR:-lxdbr0}"

if [ "$MODE" != "--test-only" ]; then
  say "Bridge: $BR"
  sysctl -w net.ipv4.ip_forward=1 >/dev/null 2>&1 && say "IP forwarding enabled"
  mkdir -p "$SYSCTL_DIR" 2>/dev/null && echo 'net.ipv4.ip_forward=1' > "$SYSCTL_DIR/99-ariznodes.conf" 2>/dev/null
  lxc network set "$BR" ipv4.nat true >/dev/null 2>&1 && say "LXD NAT on $BR enabled"
  if command -v iptables >/dev/null 2>&1; then
    ensure() { iptables -C "$@" 2>/dev/null || iptables -I "$@" 2>/dev/null; }
    if iptables -nL DOCKER-USER >/dev/null 2>&1; then
      ensure DOCKER-USER -i "$BR" -j ACCEPT; ensure DOCKER-USER -o "$BR" -j ACCEPT; say "Docker detected — added DOCKER-USER rules for $BR"
    fi
    ensure FORWARD -i "$BR" -j ACCEPT; ensure FORWARD -o "$BR" -j ACCEPT
    ensure INPUT -i "$BR" -p udp --dport 53 -j ACCEPT; ensure INPUT -i "$BR" -p tcp --dport 53 -j ACCEPT; ensure INPUT -i "$BR" -p udp --dport 67 -j ACCEPT
    say "Firewall FORWARD/DNS/DHCP rules ensured for $BR"
  fi
  if command -v ufw >/dev/null 2>&1 && ufw status 2>/dev/null | grep -q "Status: active"; then
    ufw allow in on "$BR" >/dev/null 2>&1; ufw route allow in on "$BR" >/dev/null 2>&1; ufw route allow out on "$BR" >/dev/null 2>&1; say "ufw is active — allowed traffic on $BR"
  fi
  if command -v firewall-cmd >/dev/null 2>&1 && systemctl is-active --quiet firewalld 2>/dev/null; then
    firewall-cmd --permanent --zone=trusted --add-interface="$BR" >/dev/null 2>&1; firewall-cmd --reload >/dev/null 2>&1; say "firewalld is active — $BR added to the trusted zone"
  fi
fi

[ "$MODE" = "--no-test" ] && { echo "  ✔ repair finished (no test run)"; exit 0; }
T="ariz-nettest-$$"
if ! lxc launch images:alpine/edge "$T" >/dev/null 2>&1 && ! lxc launch images:debian/12 "$T" >/dev/null 2>&1; then echo "  ⚠ could not start a test container — run the check manually: lxc launch images:debian/12 t1 && lxc exec t1 -- ping -c1 1.1.1.1"; exit 3; fi
sleep 7
check() { lxc exec "$T" -- sh -c '
  TCP=no; DNS=no; X=""; command -v timeout >/dev/null 2>&1 && X="timeout 6"
  if command -v bash >/dev/null 2>&1; then $X bash -c "exec 3<>/dev/tcp/1.1.1.1/443" >/dev/null 2>&1 && TCP=yes
  elif command -v wget >/dev/null 2>&1; then $X wget -q -T5 -O /dev/null http://deb.debian.org/ >/dev/null 2>&1 && TCP=yes; fi
  ($X getent hosts deb.debian.org || $X nslookup deb.debian.org) >/dev/null 2>&1 && DNS=yes
  echo "TCP=$TCP DNS=$DNS"' 2>/dev/null; }
R="$(check)"
if echo "$R" | grep -q "TCP=yes" && echo "$R" | grep -q "DNS=no"; then
  lxc network set "$BR" raw.dnsmasq "$(printf 'server=1.1.1.1\nserver=8.8.8.8')" >/dev/null 2>&1 && say "DNS was broken — set public resolvers on $BR"; sleep 3; R="$(check)"
fi
lxc delete -f "$T" >/dev/null 2>&1
if echo "$R" | grep -q "TCP=yes" && echo "$R" | grep -q "DNS=yes"; then echo "  ✔ containers have internet (TCP + DNS ok)"; exit 0; fi
echo "  ✘ containers still have NO internet ($R)."
echo "    Check:  iptables -S FORWARD | head ;  ufw status ;  lxc network show $BR ;  sysctl net.ipv4.ip_forward"
exit 1
