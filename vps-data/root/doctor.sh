#!/usr/bin/env bash
# ArizNodes doctor — checks everything the bot needs.   Usage: doctor.sh [--quick]
export PATH=$PATH:/snap/bin:/usr/sbin:/sbin
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -t 1 ]; then G=$'\e[32m'; R=$'\e[31m'; Y=$'\e[33m'; D=$'\e[2m'; N=$'\e[0m'; B=$'\e[1m'; else G=; R=; Y=; D=; N=; B=; fi
BAD=0; WARN=0
ok()   { echo "  ${G}✔${N} $*"; }
bad()  { echo "  ${R}✘${N} $*"; BAD=$((BAD+1)); }
warn() { echo "  ${Y}!${N} $*"; WARN=$((WARN+1)); }
envv() { grep -E "^$1=" "$DIR/.env" 2>/dev/null | head -1 | cut -d= -f2- | sed "s/^['\"]//; s/['\"]\$//"; }
echo; echo "${B}ArizNodes doctor${N}  ${D}($DIR)${N}"; echo
echo "${B}Bot${N}"
if systemctl is-active --quiet ariznodes-vpsbot 2>/dev/null; then ok "service ariznodes-vpsbot is running"; else bad "service is NOT running → ariznodes logs"; fi
[ -f "$DIR/.env" ] && ok ".env found" || bad ".env missing"
T="$(envv DISCORD_TOKEN)"; if [ -z "$T" ] || [ "$T" = "YOUR_BOT_TOKEN_HERE" ]; then bad "DISCORD_TOKEN is not set → ariznodes env"; else ok "bot token is set"; fi
O="$(envv OWNER_IDS)"; case "$O" in ""|*123456789012345678*) bad "OWNER_IDS is not set → ariznodes env";; *) ok "owner id(s): $O";; esac
journalctl -u ariznodes-vpsbot -n 60 --no-pager 2>/dev/null | grep -q "Logged in as" && ok "connected to Discord" || warn "no 'Logged in' line in the recent log"
echo; echo "${B}Website${N}"
P="$(envv DASH_PORT)"; P="${P:-8787}"; DS="$(envv DISCORD_CLIENT_SECRET)"; DP="$(envv DASH_PASSWORD)"
if [ -z "$DS$DP" ]; then warn "website is OFF (set DISCORD_CLIENT_SECRET and/or DASH_PASSWORD)"; else
  [ -n "$DS" ] && ok "Discord login configured" || warn "Discord login not configured (admin password only)"
  [ -n "$DP" ] && ok "admin password configured" || warn "no admin password (Discord login only)"
  if (exec 3<>/dev/tcp/127.0.0.1/$P) 2>/dev/null; then ok "listening on 127.0.0.1:$P"; else bad "nothing is listening on port $P → ariznodes logs"; fi
  [ -n "$(envv DASH_URL)" ] && ok "public URL: $(envv DASH_URL)" || warn "DASH_URL not set (needed for Discord login behind a domain/Cloudflare)"
fi
echo; echo "${B}Host${N}"
command -v ssh >/dev/null 2>&1 && ok "ssh client installed" || bad "ssh client missing → apt install -y openssh-client"
code=$(curl -s -m 8 -o /dev/null -w '%{http_code}' https://discord.com/api/v10/gateway 2>/dev/null); [ "$code" = 200 ] && ok "host can reach Discord" || bad "host cannot reach Discord (http $code)"
(exec 3<>/dev/tcp/a.pinggy.io/443) 2>/dev/null && ok "host can reach Pinggy (a.pinggy.io:443)" || bad "host cannot reach a.pinggy.io:443 (firewall?)"
AV=$(df -BG --output=avail /var 2>/dev/null | tail -1 | tr -dc 0-9); [ -n "$AV" ] && { [ "$AV" -ge 10 ] && ok "disk space: ${AV}G free on /var" || warn "low disk space: only ${AV}G free on /var"; }
echo; echo "${B}LXD${N}"
if ! command -v lxc >/dev/null 2>&1; then bad "lxc not found → snap install lxd && lxd init --auto"; else
  lxc list >/dev/null 2>&1 && ok "LXD is responding" || bad "LXD is not responding → snap restart lxd"
  PR="$(lxc profile show default 2>/dev/null)"
  echo "$PR" | grep -q 'root:' && ok "default profile has a root disk" || bad "default profile has NO root disk → lxc storage create default dir && lxc profile device add default root disk path=/ pool=default"
  echo "$PR" | grep -q 'eth0:' && ok "default profile has a network" || bad "default profile has NO network → lxc network create lxdbr0; lxc profile device add default eth0 nic network=lxdbr0 name=eth0"
  lxc remote list 2>/dev/null | grep -q ubuntu && ok "'ubuntu:' image remote present" || warn "'ubuntu:' remote missing (Ubuntu VPS need it)"
  echo "  ${D}VPS on this host: $(lxc list -c n --format csv 2>/dev/null | grep -c '^ariz-')${N}"
  if [ "$1" != "--quick" ]; then
    echo; echo "${B}Container internet${N} ${D}(launches a tiny test container, ~20s)${N}"
    if bash "$DIR/netfix.sh" --test-only >/tmp/ariz-doc-net.log 2>&1; then ok "containers have internet (TCP + DNS)"; else bad "containers have NO internet → run: ariznodes netfix"; sed 's/^/      /' /tmp/ariz-doc-net.log | tail -4; fi
  fi
fi
echo
if [ $BAD -eq 0 ] && [ $WARN -eq 0 ]; then echo "${G}${B}All good — everything checks out.${N}"
elif [ $BAD -eq 0 ]; then echo "${Y}${B}Working, with $WARN note(s) above.${N}"
else echo "${R}${B}$BAD problem(s) found${N} — fix the ✘ lines above (each shows the command)."; fi
exit $BAD
