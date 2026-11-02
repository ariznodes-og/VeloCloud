#!/usr/bin/env bash
# ArizNodesLabs • VPS Deployer Bot v4 — by Vasplayz90
#   bash ariznodes-vps-bundle-v4.sh              guided install (or upgrade if already installed)
#   bash ariznodes-vps-bundle-v4.sh --install    fresh install        --upgrade   keep data, update code
#   bash ariznodes-vps-bundle-v4.sh --doctor     health check         --fix-network   repair container internet
#   bash ariznodes-vps-bundle-v4.sh --files-only write files + .env only (no system changes)
set -o pipefail
VERSION="4.0"; DIR="$(pwd)"; LOGF=/tmp/ariznodes-install.log; : > "$LOGF"; export PATH=$PATH:/snap/bin
MODE="${1:-auto}"
if [ -t 1 ]; then O=$'\e[38;5;208m'; G=$'\e[32m'; R=$'\e[31m'; Y=$'\e[33m'; C=$'\e[36m'; D=$'\e[2m'; B=$'\e[1m'; N=$'\e[0m'; TTY=1; else O=; G=; R=; Y=; C=; D=; B=; N=; TTY=0; fi

banner() {
  printf '%s\n' "$O"
  cat <<'ART'
    _           _       _   _             _            
   / \    _ __ (_) ____| \ | |  ___    __| |  ___  ___ 
  / _ \  | '__|| ||_  /|  \| | / _ \  / _` | / _ \/ __|
 / ___ \ | |   | | / / | |\  || (_) || (_| ||  __/\__ \
/_/   \_\|_|   |_|/___||_| \_| \___/  \__,_| \___||___/
ART
  printf '%s   VPS Cloud  •  LXC + Pinggy + sshx + Discord website  •  v%s%s\n' "$B" "$VERSION" "$N"
  printf '%s   by Vasplayz90  •  ArizNodesLabs%s\n\n' "$D" "$N"
}
ok()   { printf '  %s✔%s %s\n' "$G" "$N" "$*"; }
warn() { printf '  %s!%s %s\n' "$Y" "$N" "$*"; }
bad()  { printf '  %s✘%s %s\n' "$R" "$N" "$*"; }
info() { printf '  %s•%s %s\n' "$C" "$N" "$*"; }
step() { printf '\n%s%s[%s/%s]%s %s%s%s\n' "$O" "$B" "$1" "$2" "$N" "$B" "$3" "$N"; }
spin() {
  local pid=$1 msg=$2 i=0 f='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
  if [ "$TTY" = 1 ]; then while kill -0 "$pid" 2>/dev/null; do printf '\r  %s%s%s %s' "$C" "${f:i++%${#f}:1}" "$N" "$msg"; sleep 0.1; done; else printf '  … %s\n' "$msg"; fi
  wait "$pid"
}
run() {  # run "message" command args…   (output goes to the log; shows a spinner)
  local msg=$1; shift; ( "$@" >>"$LOGF" 2>&1 ) & local pid=$!
  if spin "$pid" "$msg"; then [ "$TTY" = 1 ] && printf '\r\033[K'; ok "$msg"; return 0
  else [ "$TTY" = 1 ] && printf '\r\033[K'; bad "$msg"; printf '%s    last log lines (%s):%s\n' "$D" "$LOGF" "$N"; tail -n 12 "$LOGF" | sed 's/^/      /'; return 1; fi
}
die() { bad "$*"; exit 1; }
ask() {  # ask VAR "Prompt" "default"      (env var ARIZ_<VAR> or non-interactive mode skips the question)
  local __v=$1 __p=$2 __d=$3 __in="" __pre="ARIZ_$1"
  if [ -n "${!__pre}" ]; then printf -v "$__v" '%s' "${!__pre}"; return; fi
  if [ "$ARIZ_NONINTERACTIVE" = 1 ] || ! [ -r /dev/tty ]; then printf -v "$__v" '%s' "$__d"; return; fi
  read -r -p "  ${B}?${N} ${__p}" __in </dev/tty; printf -v "$__v" '%s' "${__in:-$__d}"
}
ask_secret() {
  local __v=$1 __p=$2 __in="" __pre="ARIZ_$1"
  if [ -n "${!__pre}" ]; then printf -v "$__v" '%s' "${!__pre}"; return; fi
  if [ "$ARIZ_NONINTERACTIVE" = 1 ] || ! [ -r /dev/tty ]; then printf -v "$__v" '%s' ""; return; fi
  read -r -s -p "  ${B}?${N} ${__p}" __in </dev/tty; echo; printf -v "$__v" '%s' "$__in"
}
rand() { tr -dc 'A-Za-z0-9' </dev/urandom 2>/dev/null | head -c "${1:-20}"; }

# ───────────────────────── files ─────────────────────────
write_files() {
  cat > bot.py <<'ARIZ_BOT_PY'
# ╔══════════════════════════════════════════════════════════════╗
# ║  ArizNodesLabs • VPS Deployer Bot v4  —  by Vasplayz90       ║
# ║  LXC containers + Pinggy SSH tunnels + sshx web terminals    ║
# ╚══════════════════════════════════════════════════════════════╝
import os, re, io, sys, json, shutil, subprocess, time, ast, random, string, base64, hashlib, secrets, asyncio, sqlite3, uuid as uuidlib, operator as op, datetime as dt
from asyncio.subprocess import PIPE, STDOUT, DEVNULL
import aiohttp, discord, psutil
from aiohttp import web
from urllib.parse import urlencode
from discord.ext import commands
from dotenv import load_dotenv
try: import pyfiglet
except Exception: pyfiglet = None

load_dotenv()
def env(k, d=""): return os.getenv(k, d).strip()
TOKEN = env("DISCORD_TOKEN"); PREFIX = env("PREFIX", "!")
OWNERS = {int(x) for x in re.findall(r"\d+", env("OWNER_IDS"))}
MAX_VPS = int(env("MAX_VPS_PER_USER", "3")); MAX_RAM = int(env("MAX_RAM_MB", "8192"))
MAX_CPU = int(env("MAX_CPU", "4")); MAX_DISK = int(env("MAX_DISK_GB", "50"))
PINGGY_TOKEN = env("PINGGY_TOKEN"); LXC = env("LXC_BIN", "lxc")
DASH_PASS = env("DASH_PASSWORD"); DASH_HOST = env("DASH_HOST", "127.0.0.1"); DASH_PORT = int(env("DASH_PORT", "8787"))
DISCORD_CLIENT_ID = env("DISCORD_CLIENT_ID"); DISCORD_SECRET = env("DISCORD_CLIENT_SECRET"); DASH_URL = env("DASH_URL").rstrip("/")
TRUST_PROXY = env("DASH_TRUST_PROXY", "1" if DASH_HOST in ("127.0.0.1", "localhost") else "0") == "1"
BOT_DIR = os.path.dirname(os.path.abspath(globals().get("__file__", ".")))
DEFAULT_DAYS = int(env("DEFAULT_DAYS", "0")); GRACE_DAYS = int(env("GRACE_DAYS", "3")); RENEW_DAYS = int(env("RENEW_DAYS") or DEFAULT_DAYS or 30)
COOLDOWN = int(env("DEPLOY_COOLDOWN", "60")); MAX_PARALLEL = int(env("MAX_PARALLEL_DEPLOYS", "2")); MAX_BACKUPS = int(env("MAX_BACKUPS", "2")); TUN_RENEW_MIN = 52
FIRE, RED = 0xFF4500, 0xE74C3C
VERSION = "4.0"; BRAND = "🔥 ArizNodesLabs • Vasplayz90 • v4"; START = time.time()

IMAGES = {  # key: (label, lxc image alias, emoji)  — edit freely
 "debian11": ("Debian 11 (Bullseye)", "images:debian/11", "🌀"),
 "debian12": ("Debian 12 (Bookworm)", "images:debian/12", "🌀"),
 "debian13": ("Debian 13 (Trixie)", "images:debian/13", "🌀"),
 "ubuntu2404": ("Ubuntu 24.04.5 LTS", "ubuntu:24.04", "🟠"),
 "ubuntu2204": ("Ubuntu 22.04.5 LTS", "ubuntu:22.04", "🟠"),
 "ubuntu2004": ("Ubuntu 20.04 LTS", "ubuntu:20.04", "🟠"),
 "alma9": ("AlmaLinux 9", "images:almalinux/9", "🦬"),
 "alma8": ("AlmaLinux 8", "images:almalinux/8", "🦬"),
 "rocky9": ("Rocky Linux 9", "images:rockylinux/9", "⛰️"),
 "centos9": ("CentOS 9 Stream", "images:centos/9-Stream", "💠"),
 "fedora": ("Fedora 42", "images:fedora/42", "🎩"),
 "alpine": ("Alpine Edge", "images:alpine/edge", "🏔️"),
 "arch": ("Arch Linux", "images:archlinux", "🏹"),
 "kali": ("Kali Linux", "images:kali", "🐉"),
 "opensuse": ("openSUSE Tumbleweed", "images:opensuse/tumbleweed", "🦎"),
}
_P = {"starter": (1024, 1, 10), "basic": (2048, 1, 20), "standard": (4096, 2, 30), "pro": (8192, 4, 50)}
PLANS = {k: v for k, v in _P.items() if v[0] <= MAX_RAM and v[1] <= MAX_CPU and v[2] <= MAX_DISK} or {"starter": _P["starter"]}
DEF_PLAN = next(iter(PLANS))

# ───────────────────────── database ─────────────────────────
db = sqlite3.connect("vps.db", check_same_thread=False); db.row_factory = sqlite3.Row
db.executescript("""
CREATE TABLE IF NOT EXISTS vps(name TEXT PRIMARY KEY, owner INTEGER, os TEXT, ram INTEGER, cpu INTEGER, disk INTEGER,
  created INTEGER, suspended INTEGER DEFAULT 0, ssh TEXT DEFAULT '', sshx TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, banned INTEGER DEFAULT 0, max_vps INTEGER);
CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY);
CREATE TABLE IF NOT EXISTS warns(id INTEGER PRIMARY KEY AUTOINCREMENT, guild INTEGER, uid INTEGER, reason TEXT, ts INTEGER);
CREATE TABLE IF NOT EXISTS audit(id INTEGER PRIMARY KEY AUTOINCREMENT, ts INTEGER, uid INTEGER, action TEXT, detail TEXT);
CREATE TABLE IF NOT EXISTS settings(k TEXT PRIMARY KEY, v TEXT);
""")
for _col in ("expires INTEGER DEFAULT 0", "autossh INTEGER DEFAULT 0", "http TEXT DEFAULT ''", "note TEXT DEFAULT ''", "notified INTEGER DEFAULT 0"):
    try: db.execute("ALTER TABLE vps ADD COLUMN " + _col)
    except sqlite3.OperationalError: pass
db.commit()
def q(sql, a=(), one=False):
    cur = db.execute(sql, a); r = cur.fetchone() if one else cur.fetchall(); db.commit(); return r
def gset(k, d=""): r = q("SELECT v FROM settings WHERE k=?", (k,), True); return r["v"] if r else d
def sset(k, v): q("INSERT OR REPLACE INTO settings VALUES(?,?)", (k, str(v)))
def urow(uid): q("INSERT OR IGNORE INTO users(id) VALUES(?)", (uid,)); return q("SELECT * FROM users WHERE id=?", (uid,), True)
def is_admin(uid): return uid in OWNERS or bool(q("SELECT 1 FROM admins WHERE id=?", (uid,), True))
def ulimit(uid): m = urow(uid)["max_vps"]; return m if m is not None else MAX_VPS

# ───────────────────────── helpers ─────────────────────────
THEMES = {"fire": (0xFF4500, "🔥", "Fire"), "ocean": (0x1E90FF, "🌊", "Ocean"), "neon": (0x39FF14, "⚡", "Neon"), "royal": (0x8A2BE2, "👑", "Royal"),
 "rose": (0xFF3B8B, "🌸", "Rose"), "gold": (0xFFC400, "✨", "Gold"), "ice": (0x00E5FF, "❄️", "Ice")}
def theme(): return THEMES.get(gset("theme", "fire"), THEMES["fire"])
def emb(title=None, desc=None, color=None):
    t = theme(); e = discord.Embed(title=title, description=desc, color=t[0] if color is None else color, timestamp=dt.datetime.now(dt.timezone.utc))
    e.set_author(name=f"{t[1]} ArizNodesLabs  ·  VPS Cloud"); e.set_footer(text=BRAND); return e
def err(m): return emb("❌ Error", m, RED)
def trim(s, n=1800): s = s or ""; return s if len(s) <= n else s[:n] + "\n…"

def errtail(o, n=700):
    o = re.sub(r"(Retrieving image|Unpacking image)[^%]*?\d+% \([^)]*\)\s*", "", o or ""); i = o.rfind("Error:")
    o = o[i:] if i >= 0 else o
    return o if len(o) <= n else "…" + o[-n:]
def clean(s): return re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]|\x1b[()][A-Z0-9]|\x1b\][^\x07]*\x07|\r", "", s or "")
def bar(p, n=12): f = int(max(0, min(100, p)) / 100 * n); return "█" * f + "░" * (n - f) + f" {p:.0f}%"
def rpass(n=14): a = string.ascii_letters + string.digits; return "".join(secrets.choice(a) for _ in range(n))
def upt(s): d, r = divmod(int(s), 86400); h, r = divmod(r, 3600); m, s = divmod(r, 60); return f"{d}d {h}h {m}m {s}s"
def art(t, font="small"):
    try: return pyfiglet.figlet_format(t, font=font).rstrip()
    except Exception: return t
def audit(uid, action, detail=""):
    q("INSERT INTO audit(ts,uid,action,detail) VALUES(?,?,?,?)", (int(time.time()), uid, action, detail[:300]))
    ch = gset("logch")
    if ch:
        async def _s():
            c = bot.get_channel(int(ch))
            if c: await c.send(embed=emb("📜 Audit Log", f"<@{uid}> • **{action}**\n{detail[:300]}"))
        try: asyncio.get_running_loop().create_task(_s())
        except RuntimeError: pass

async def sh(*a, timeout=120):
    try:
        p = await asyncio.create_subprocess_exec(*a, stdout=PIPE, stderr=STDOUT, stdin=DEVNULL)
        out, _ = await asyncio.wait_for(p.communicate(), timeout)
        return p.returncode, clean(out.decode(errors="ignore")).strip()
    except asyncio.TimeoutError:
        try: p.kill()
        except Exception: pass
        return 124, "Timed out"
    except FileNotFoundError: return 127, f"`{a[0]}` not found on host"
async def lx(*a, timeout=120): return await sh(LXC, *a, timeout=timeout)
async def inside(c, script, timeout=300, envs=None):
    a = ["exec", c]
    for k, v in {"DEBIAN_FRONTEND": "noninteractive", **(envs or {})}.items(): a += ["--env", f"{k}={v}"]
    return await lx(*a, "--", "sh", "-c", script, timeout=timeout)
async def lxstate(c):
    rc, o = await lx("list", f"^{c}$", "-c", "s", "--format", "csv")
    return o.splitlines()[0].upper() if rc == 0 and o.strip() else "MISSING"
async def lxip(c):
    rc, o = await lx("list", f"^{c}$", "-c", "4", "--format", "csv")
    m = re.search(r"\d+\.\d+\.\d+\.\d+", o); return m.group(0) if m else None
def pm(pk):
    return ("if command -v apt-get >/dev/null 2>&1; then apt-get update -y && apt-get install -y {p}; "
            "elif command -v dnf >/dev/null 2>&1; then dnf install -y {p}; elif command -v apk >/dev/null 2>&1; then apk add --no-cache {p}; "
            "elif command -v pacman >/dev/null 2>&1; then pacman -Sy --noconfirm {p}; "
            "elif command -v zypper >/dev/null 2>&1; then zypper -n install {p}; fi").format(p=pk)
SETUP = r'''
export DEBIAN_FRONTEND=noninteractive LC_ALL=C
LOG=/root/ariz-setup.log; : > "$LOG"; exec >>"$LOG" 2>&1
echo "== ArizNodes SSH setup =="
command -v cloud-init >/dev/null 2>&1 && cloud-init status --wait >/dev/null 2>&1
if ! getent hosts deb.debian.org >/dev/null 2>&1 && ! getent hosts github.com >/dev/null 2>&1; then
  echo "DNS looks broken - switching to public resolvers"; rm -f /etc/resolv.conf; printf 'nameserver 1.1.1.1\nnameserver 8.8.8.8\n' > /etc/resolv.conf
fi
retry() { n=0; until "$@"; do n=$((n+1)); [ "$n" -ge 3 ] && return 1; echo "retry $n: $*"; sleep 5; done; return 0; }
if command -v apt-get >/dev/null 2>&1; then
  retry apt-get -o DPkg::Lock::Timeout=240 update && retry apt-get -o DPkg::Lock::Timeout=240 install -y --no-install-recommends openssh-server curl ca-certificates sudo nano
elif command -v dnf >/dev/null 2>&1; then retry dnf install -y openssh-server curl ca-certificates sudo nano
elif command -v apk >/dev/null 2>&1; then retry apk add --no-cache openssh curl ca-certificates sudo nano bash
elif command -v pacman >/dev/null 2>&1; then (pacman-key --init; pacman-key --populate archlinux); retry pacman -Sy --noconfirm openssh curl sudo nano
elif command -v zypper >/dev/null 2>&1; then retry zypper -n --gpg-auto-import-keys install openssh curl sudo nano
fi
SSHD=$(command -v sshd 2>/dev/null); if [ -z "$SSHD" ]; then for p in /usr/sbin/sshd /usr/bin/sshd /sbin/sshd; do [ -x "$p" ] && SSHD=$p && break; done; fi
if [ -z "$SSHD" ]; then echo "FATAL: sshd was not installed - the package manager failed (usually the VPS has no internet)"; exit 1; fi
mkdir -p /run/sshd /var/run/sshd /etc/ssh/sshd_config.d; ssh-keygen -A
touch /etc/ssh/sshd_config
sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/;s/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
grep -q '^PermitRootLogin' /etc/ssh/sshd_config || echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
grep -q '^PasswordAuthentication' /etc/ssh/sshd_config || echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
printf 'PermitRootLogin yes\nPasswordAuthentication yes\n' > /etc/ssh/sshd_config.d/00-ariz.conf
(systemctl enable ssh || systemctl enable sshd || rc-update add sshd default) >/dev/null 2>&1
(systemctl restart ssh.socket; systemctl restart ssh || systemctl restart sshd || rc-service sshd restart) >/dev/null 2>&1
sleep 2
LISTEN='grep -qiE ":0016 [0-9A-F:]+ 0A" /proc/net/tcp /proc/net/tcp6'
sh -c "$LISTEN" 2>/dev/null || { "$SSHD"; sleep 2; }
echo "root:$PW" | chpasswd || { echo "FATAL: could not set the root password"; exit 1; }
sh -c "$LISTEN" 2>/dev/null || { echo "FATAL: sshd is installed but not listening on port 22"; exit 1; }
echo "== SSH ready =="
'''
NETCHECK = r'''
X=""; command -v timeout >/dev/null 2>&1 && X="timeout 6"
TCP=no; DNS=no
if command -v bash >/dev/null 2>&1; then $X bash -c 'exec 3<>/dev/tcp/1.1.1.1/443' >/dev/null 2>&1 && TCP=yes
elif command -v wget >/dev/null 2>&1; then $X wget -q -T5 -O /dev/null http://deb.debian.org/ >/dev/null 2>&1 && TCP=yes
elif command -v curl >/dev/null 2>&1; then $X curl -fsS -m5 -o /dev/null http://deb.debian.org/ >/dev/null 2>&1 && TCP=yes; fi
($X getent hosts deb.debian.org || $X nslookup deb.debian.org) >/dev/null 2>&1 && DNS=yes
echo "TCP=$TCP DNS=$DNS"
'''
NETFIX_AT = {"t": 0}
NO_NET_HOST = "The new VPS has **no internet access**, so SSH / sshx can't be installed. This is a host firewall / NAT problem (very common when Docker or ufw runs on the same server).\nThe bot already tried an automatic repair, but it did not help. As owner run `!netfix`, or on the server: `ariznodes netfix`, then deploy again."
NO_NET_VPS = "This VPS has **no internet access**, so sshd / sshx can't be installed.\nOwner: run `!netfix` (or *Repair network* in the website settings), then try again."
async def inet_state(c):
    rc, o = await inside(c, NETCHECK, 45); return ("TCP=yes" in o), ("DNS=yes" in o)
async def host_netfix():
    if time.time() - NETFIX_AT["t"] < 90: return "(network repair already ran a moment ago)"
    NETFIX_AT["t"] = time.time(); path = os.path.join(BOT_DIR, "netfix.sh")
    if not os.path.exists(path): return "netfix.sh was not found next to bot.py — re-run the installer."
    rc, o = await sh("bash", path, "--no-test", timeout=120); return o
def pg_key():
    p = os.path.join(BOT_DIR, ".pinggy_key")
    if not os.path.exists(p):
        try: subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", p], check=True, capture_output=True, timeout=20)
        except Exception: return None
    return p

# ───────────────────────── tunnels (Pinggy + sshx) ─────────────────────────
TUN = {}
SSHD_CHECK = r'grep -qiE ":0016 [0-9A-F:]+ 0A" /proc/net/tcp /proc/net/tcp6 2>/dev/null'
def pg_host(): return env("PINGGY_SERVER") or ("pro.pinggy.io" if PINGGY_TOKEN else "a.pinggy.io")
async def pg_reachable(host):
    try: _, w = await asyncio.wait_for(asyncio.open_connection(host, 443), 8); w.close(); return True
    except Exception: return False
async def pinggy_open(target, port, mode="tcp"):
    """Open a Pinggy tunnel to target:port. mode 'tcp' -> 'host:port', 'http' -> 'https://…'. Returns (proc, result, error)."""
    if not shutil.which("ssh"): return None, None, "`ssh` client missing on the host — run: `apt install -y openssh-client`"
    host = pg_host()
    user = (f"{PINGGY_TOKEN}+tcp" if PINGGY_TOKEN else "tcp") if mode == "tcp" else PINGGY_TOKEN
    dest = f"{user}@{host}" if user else host
    if not await pg_reachable(host): return None, None, f"This server cannot reach `{host}:443` — check the firewall / outbound network."
    tail = []
    for tty in ("-T", "-tt"):  # attempt 1: plain-text output, attempt 2: forced pty (some Pinggy versions only print the link on a tty)
        try:
            p = await asyncio.create_subprocess_exec("ssh", "-p", "443", tty, *(["-i", pg_key(), "-o", "IdentitiesOnly=yes"] if pg_key() else []), "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", "-o", "ServerAliveInterval=30",
                "-o", "ServerAliveCountMax=3", "-o", "ExitOnForwardFailure=yes", "-o", "ConnectTimeout=15", "-R", f"0:{target}:{port}", dest, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        except Exception as ex: return None, None, f"Could not start ssh: {ex}"
        buf = ""
        async def wait():
            nonlocal buf
            while True:
                d = await p.stdout.read(4096)
                if not d: return None
                buf += clean(d.decode(errors="ignore"))
                if mode == "tcp":
                    m = re.search(r"tcp://([\w.\-]+):(\d+)", buf) or re.search(r"\b([\w\-]+(?:\.[\w\-]+)*\.pinggy\.\w+):(\d{2,5})\b", buf)
                    if m: return f"{m.group(1)}:{m.group(2)}"
                else:
                    for u in re.findall(r"https://[\w.\-]+", buf):
                        if "pinggy" in u and not re.match(r"https://(dashboard|www|pinggy)\.", u): return u
        try: res = await asyncio.wait_for(wait(), 30)
        except asyncio.TimeoutError: res = None
        if res: return p, res, None
        tail.append(buf.strip()[-300:])
        try: p.kill()
        except ProcessLookupError: pass
    return None, None, "Pinggy did not return a link.\n```" + trim(" | ".join(t for t in tail if t) or "(no output from pinggy)", 450) + "```"
async def stop_tunnel(c):
    t = TUN.pop(c, None)
    if t:
        try: t["proc"].kill()
        except Exception: pass
    q("UPDATE vps SET ssh='' WHERE name=?", (c,))
async def ensure_ssh(c):
    """Make sure sshd is installed and listening on :22 inside the VPS. Returns (ok, new_password_or_None, message)."""
    rc, _ = await inside(c, SSHD_CHECK, 20)
    if rc == 0: return True, None, ""
    rc, _ = await inside(c, "mkdir -p /run/sshd; (systemctl restart ssh.socket; systemctl restart ssh || systemctl restart sshd || rc-service sshd restart || /usr/sbin/sshd) >/dev/null 2>&1; sleep 2; " + SSHD_CHECK, 40)
    if rc == 0: return True, None, ""
    tcp, dns = await inet_state(c)
    if not tcp: return False, None, NO_NET_VPS
    pw = rpass(); rc, o = await inside(c, SETUP, 900, {"PW": pw}); rc2, _ = await inside(c, "sleep 1; " + SSHD_CHECK, 20)
    if rc2 == 0: return True, pw, "SSH was missing and has been reinstalled."
    rc3, log = await inside(c, "tail -n 12 /root/ariz-setup.log 2>/dev/null", 20)
    return False, None, "sshd could not be installed:\n```" + trim(log or o, 600) + "```"
async def start_tunnel(c):
    await stop_tunnel(c)
    if await lxstate(c) != "RUNNING": return None, "The VPS is not running — start it first."
    ok, pw, msg = await ensure_ssh(c)
    if not ok: return None, msg
    r = find(c)
    if pw and r: await notify(r["owner"], emb("🔐 SSH was reinstalled", f"`{c}` has a new root password: `{pw}`", 0xF1C40F))
    ip = await lxip(c)
    if not ip: return None, "The VPS has no IPv4 yet — wait a few seconds and try again."
    p, addr, e = await pinggy_open(ip, 22, "tcp")
    if e: return None, e
    async def drain():
        try:
            while await p.stdout.read(4096): pass
        finally:
            if TUN.get(c, {}).get("proc") is p: TUN.pop(c, None); q("UPDATE vps SET ssh='' WHERE name=?", (c,))
    TUN[c] = {"proc": p, "addr": addr, "task": asyncio.create_task(drain()), "started": time.time()}
    q("UPDATE vps SET ssh=? WHERE name=?", (addr, c)); return addr, None
SSHX_SCRIPT = r'''
pkill -x sshx 2>/dev/null; rm -f /root/.sshx.log /tmp/sshx.err
if ! command -v curl >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1; then apt-get update -y >/dev/null 2>&1; apt-get install -y curl ca-certificates >/dev/null 2>&1;
  elif command -v dnf >/dev/null 2>&1; then dnf install -y curl ca-certificates >/dev/null 2>&1;
  elif command -v apk >/dev/null 2>&1; then apk add --no-cache curl ca-certificates >/dev/null 2>&1;
  elif command -v pacman >/dev/null 2>&1; then pacman -Sy --noconfirm curl >/dev/null 2>&1;
  elif command -v zypper >/dev/null 2>&1; then zypper -n install curl >/dev/null 2>&1; fi
fi
BIN=$(command -v sshx 2>/dev/null)
if [ -z "$BIN" ]; then
  case "$(uname -m)" in x86_64|amd64) A=x86_64;; aarch64|arm64) A=aarch64;; arm*) A=arm;; *) A=$(uname -m);; esac
  if curl -fsSL "https://s3.amazonaws.com/sshx/sshx-$A-unknown-linux-musl.tar.gz" -o /tmp/sshx.tgz 2>/tmp/sshx.err && tar -xzf /tmp/sshx.tgz -C /usr/local/bin sshx 2>>/tmp/sshx.err; then
    chmod +x /usr/local/bin/sshx; BIN=/usr/local/bin/sshx
  fi
fi
if [ -n "$BIN" ]; then ( setsid nohup "$BIN" > /root/.sshx.log 2>&1 < /dev/null & )
else ( setsid nohup sh -c 'curl -sSf https://sshx.io/get | sh -s run' > /root/.sshx.log 2>&1 < /dev/null & ); fi
for i in $(seq 1 35); do grep -q 'sshx.io/s/' /root/.sshx.log 2>/dev/null && break; sleep 1; done
cat /root/.sshx.log 2>/dev/null; cat /tmp/sshx.err 2>/dev/null
'''
async def start_sshx(c):
    if await lxstate(c) != "RUNNING": return None, "The VPS is not running — start it first."
    rc, o = await inside(c, SSHX_SCRIPT, 150)
    m = re.search(r"https://sshx\.io/s/[\w\-/#.]+", o)
    if not m:
        tcp, dns = await inet_state(c)
        if not tcp: return None, NO_NET_VPS
        return None, "sshx did not return a link.\n```" + trim(o or "(no output)", 450) + "```"
    q("UPDATE vps SET sshx=? WHERE name=?", (m.group(0), c)); return m.group(0), None
async def stop_sshx(c):
    await inside(c, "pkill -x sshx 2>/dev/null; true", 20); q("UPDATE vps SET sshx='' WHERE name=?", (c,))

# ───────────────────────── VPS core ─────────────────────────
def find(ref):
    ref = (ref or "").lower().strip()
    for n in (ref, "ariz-" + ref):
        r = q("SELECT * FROM vps WHERE name=?", (n,), True)
        if r: return r
def guard(r, uid, active=True):
    if r["owner"] != uid and not is_admin(uid): return "That VPS is not yours."
    if active and r["suspended"] and not is_admin(uid): return "⛔ This VPS is suspended. Contact an admin."
async def do_act(act, r):
    c = r["name"]
    if act in ("start", "resume"): rc, o = await lx("start", c)
    elif act == "stop":
        await stop_tunnel(c); await stop_http(c); rc, o = await lx("stop", c, "--timeout", "30")
        if rc != 0: rc, o = await lx("stop", c, "--force")
    elif act == "kill": await stop_tunnel(c); await stop_http(c); rc, o = await lx("stop", c, "--force")
    elif act == "restart": await stop_tunnel(c); await stop_http(c); rc, o = await lx("restart", c, "--timeout", "30")
    elif act == "pause": rc, o = await lx("pause", c)
    elif act == "delete":
        await stop_tunnel(c); await stop_http(c); rc, o = await lx("delete", c, "--force", timeout=180)
        if rc == 0 or "not found" in o.lower(): q("DELETE FROM vps WHERE name=?", (c,)); rc = 0
    else: return False, "unknown action"
    if act in ("stop", "kill", "restart", "pause", "delete"): q("UPDATE vps SET sshx='' WHERE name=?", (c,)); CONS.pop(c, None)
    audit(r["owner"], act, c); return rc == 0, o or "Done."
async def provision(c, alias, ram, cpu, disk, say=None):
    async def S(n, t):
        if say: await say(n, t)
    await S(1, "Creating LXC container")
    base = ["launch", alias, c, "-c", f"limits.memory={ram}MiB", "-c", f"limits.cpu={cpu}", "-c", "security.nesting=true"]
    rc, o = await lx(*base, "-d", f"root,size={disk}GiB", timeout=900)
    if rc != 0: await lx("delete", "-f", c); rc, o = await lx(*base, timeout=900)
    if rc != 0: await lx("delete", "-f", c); return None, "LXC launch failed:\n" + errtail(o)
    await S(2, "Waiting for network & internet")
    for _ in range(30):
        if await lxip(c): break
        await asyncio.sleep(2)
    await asyncio.sleep(2); tcp, dns = await inet_state(c)
    if not tcp: await asyncio.sleep(5); tcp, dns = await inet_state(c)
    if not tcp:
        fixlog = await host_netfix(); await asyncio.sleep(5); tcp, dns = await inet_state(c)
        if not tcp: await lx("delete", "-f", c); return None, NO_NET_HOST + "\n```" + trim(fixlog, 450) + "```"
    await S(3, "Installing & configuring SSH")
    pw = rpass(); rc, o = await inside(c, SETUP, 900, {"PW": pw})
    if rc != 0:
        rc2, log = await inside(c, "tail -n 14 /root/ariz-setup.log 2>/dev/null", 20); await lx("delete", "-f", c)
        return None, "SSH setup failed:\n```" + trim(log or o, 700) + "```"
    return pw, None
async def deploy_vps(uid, osk, plan, prog=None, force=False):
    if osk not in IMAGES: return None, "Unknown OS. See `%simages`." % PREFIX
    if plan not in PLANS: return None, "Unknown plan. See `%splans`." % PREFIX
    if urow(uid)["banned"] and not force: return None, "You are banned."
    if gset("maint") == "1" and not is_admin(uid) and not force: return None, "🛠️ Maintenance mode is on."
    n = q("SELECT COUNT(*) c FROM vps WHERE owner=?", (uid,), True)["c"]
    if n >= ulimit(uid) and not is_admin(uid) and not force: return None, f"VPS limit reached ({n}/{ulimit(uid)})."
    global SEM
    wait = int(COOLDOWN - (time.time() - LAST.get(uid, 0)))
    if wait > 0 and not is_admin(uid) and not force: return None, f"⏳ Cooldown — try again in {wait}s."
    LAST[uid] = time.time(); SEM = SEM or asyncio.Semaphore(MAX_PARALLEL)
    ram, cpu, disk = PLANS[plan]; c = "ariz-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    if prog: await prog(0, "Queued (waiting for a free slot)")
    async with SEM: pw, e = await provision(c, IMAGES[osk][1], ram, cpu, disk, prog)
    if e: LAST[uid] = 0; return None, e
    exp = int(time.time() + DEFAULT_DAYS * 86400) if DEFAULT_DAYS else 0
    q("INSERT INTO vps(name,owner,os,ram,cpu,disk,created,expires) VALUES(?,?,?,?,?,?,?,?)", (c, uid, osk, ram, cpu, disk, int(time.time()), exp))
    if prog: await prog(4, "Opening Pinggy SSH tunnel")
    addr, te = await start_tunnel(c)
    if prog: await prog(5, "Finalizing")
    audit(uid, "deploy", f"{c} {osk} {plan}")
    return {"name": c, "os": osk, "pw": pw, "ssh": addr, "tunnel_err": te, "ram": ram, "cpu": cpu, "disk": disk, "expires": exp}, None
def progress_embed(n, t):
    return emb("🚀 Deploying your VPS", f"`{'█' * n}{'░' * (5 - n)}` **{n}/5**\n⚙️ {t}…\n\n*This can take 1–3 minutes.*")
def ssh_line(addr): h, p = addr.rsplit(":", 1); return f"ssh root@{h} -p {p}"
def cred_embed(res):
    e = emb("🔥 VPS Credentials", f"**{IMAGES[res['os']][0]}** • `{res['name']}`", 0x2ECC71)
    e.add_field(name="🔑 Username / Password", value=f"`root` / `{res['pw']}`", inline=False)
    e.add_field(name="🔌 SSH (Pinggy IPv4)", value=f"```{ssh_line(res['ssh'])}```" if res["ssh"] else f"⚠️ {res['tunnel_err']}\nUse **New SSH** in `{PREFIX}manage`.", inline=False)
    e.add_field(name="📦 Resources", value=f"{res['ram']}MB RAM • {res['cpu']} vCPU • {res['disk']}GB disk"); e.add_field(name="⏳ Note", value=f"Free Pinggy links last ~60 min. Turn on **Auto-SSH** (`{PREFIX}autossh on`) and v2 renews them for you.")
    if res.get("expires"): e.add_field(name="⌛ Expires", value=f"<t:{res['expires']}:R> — renew with `{PREFIX}renew`")
    return e
async def vps_embed(r):
    c = r["name"]; st = await lxstate(c); ip = await lxip(c) if st == "RUNNING" else None
    col = {"RUNNING": 0x2ECC71, "STOPPED": 0xE74C3C, "FROZEN": 0x3498DB}.get(st, 0x95A5A6)
    badge = {"RUNNING": "🟢 Online", "STOPPED": "🔴 Offline", "FROZEN": "🧊 Paused"}.get(st, "⚪ " + st); sus = {1: "  ·  ⛔ Suspended", 2: "  ·  ⌛ Expired"}.get(r["suspended"], "")
    e = emb(f"🖥️  {c}", f"### {badge}{sus}\n{IMAGES.get(r['os'], (r['os'],))[0]}  ·  **{r['ram']}MB** RAM  ·  **{r['cpu']}** vCPU  ·  **{r['disk']}GB** disk" + (f"\n📝 *{r['note']}*" if r["note"] else ""), col)
    e.add_field(name="🌐 Internal IP", value=f"`{ip or 'n/a'}`"); e.add_field(name="👤 Owner", value=f"<@{r['owner']}>"); e.add_field(name="⏳ Expires", value=f"<t:{r['expires']}:R>" if r["expires"] else "never")
    if st == "RUNNING":
        u = await usage(c, r, 0)
        if u: e.add_field(name="📊 Usage", value=f"💾 RAM `{bar(u['memp'])}`\n💽 Disk `{bar(u['diskp'])}`", inline=False)
    e.add_field(name="🔌 Pinggy SSH", value=f"`{ssh_line(r['ssh'])}`" if r["ssh"] else "not active", inline=False)
    e.add_field(name="🌍 sshx", value=r["sshx"] or "not active"); e.add_field(name="🌐 Web", value=r["http"] or "not active"); e.add_field(name="🔁 Auto-SSH", value="ON" if r["autossh"] else "off")
    e.set_footer(text=f"{BRAND}  ·  created {time.strftime('%Y-%m-%d', time.gmtime(r['created']))}"); return e
def deploy_intro():
    return emb("🚀 Deploy a VPS", "Pick an **OS** and a **plan**, then hit **Deploy**.\n\n" + "\n".join(f"{'**%s**' % k}: {v[0]}MB • {v[1]}vCPU • {v[2]}GB" for k, v in PLANS.items()))
def manage_embed(uid):
    n = q("SELECT COUNT(*) c FROM vps WHERE owner=?", (uid,), True)["c"]
    return emb("🎛️ VPS Manager", f"You own **{n}/{ulimit(uid)}** VPS.\nSelect one below to start / stop / restart, open SSH (Pinggy), sshx, snapshots and more.")

# ───────────────────────── UI ─────────────────────────
class OV(discord.ui.View):
    def __init__(s, uid, timeout=900): super().__init__(timeout=timeout); s.uid = uid
    async def interaction_check(s, i):
        if i.user.id == s.uid or is_admin(i.user.id): return True
        await i.response.send_message("🔒 This panel isn't yours — run it yourself.", ephemeral=True); return False

class ConfirmView(OV):
    def __init__(s, uid, fn, label="Confirm"): super().__init__(uid, 120); s.fn = fn; s.b_ok.label = label
    @discord.ui.button(label="Confirm", emoji="✅", style=discord.ButtonStyle.danger)
    async def b_ok(s, i, b):
        await i.response.edit_message(embed=emb("⏳ Working…"), view=None); ok, m = await s.fn()
        await i.edit_original_response(embed=emb("✅ Done" if ok else "❌ Failed", f"```{trim(m, 800)}```" if m else None, 0x2ECC71 if ok else RED))
    @discord.ui.button(label="Cancel", emoji="✖️", style=discord.ButtonStyle.secondary)
    async def b_no(s, i, b): await i.response.edit_message(embed=emb("Cancelled"), view=None)

class DeployView(OV):
    def __init__(s, uid):
        super().__init__(uid); s.os = "debian12"; s.plan = DEF_PLAN
        a = discord.ui.Select(placeholder="🐧 Choose operating system", options=[discord.SelectOption(label=v[0], value=k, emoji=v[2], default=(k == "debian12")) for k, v in IMAGES.items()])
        b = discord.ui.Select(placeholder="📦 Choose plan", row=1, options=[discord.SelectOption(label=k.title(), value=k, description=f"{v[0]}MB • {v[1]}vCPU • {v[2]}GB", default=(k == DEF_PLAN)) for k, v in PLANS.items()])
        async def ca(i): s.os = a.values[0]; await i.response.defer()
        async def cb(i): s.plan = b.values[0]; await i.response.defer()
        a.callback, b.callback = ca, cb; s.add_item(a); s.add_item(b)
    @discord.ui.button(label="Deploy", emoji="🚀", style=discord.ButtonStyle.success, row=2)
    async def go(s, i, b):
        await i.response.edit_message(embed=progress_embed(0, "Starting"), view=None)
        async def prog(n, t): await i.edit_original_response(embed=progress_embed(n, t))
        res, e = await deploy_vps(s.uid, s.os, s.plan, prog)
        if e: return await i.edit_original_response(embed=err(e))
        await i.edit_original_response(embed=emb("✅ VPS Deployed", f"`{res['name']}` is online!\nCredentials are in the private message below (and your DMs).\nControl it with `{PREFIX}manage`.", 0x2ECC71))
        ce = cred_embed(res); await i.followup.send(embed=ce, ephemeral=True)
        try: await i.user.send(embed=ce)
        except Exception: pass

class ManageView(OV):
    def __init__(s, uid):
        super().__init__(uid)
        rows = q("SELECT name,os FROM vps WHERE owner=? ORDER BY created DESC LIMIT 25", (uid,))
        if rows:
            sel = discord.ui.Select(placeholder="🖥️ Select a VPS to manage", options=[discord.SelectOption(label=r["name"], description=IMAGES.get(r["os"], (r["os"],))[0][:90], emoji="🖥️") for r in rows])
            async def cb(i):
                r = find(sel.values[0])
                if not r: return await i.response.send_message(embed=err("VPS not found."), ephemeral=True)
                await i.response.edit_message(embed=await vps_embed(r), view=VPSPanel(s.uid, r["name"]))
            sel.callback = cb; s.add_item(sel)
    @discord.ui.button(label="Deploy New VPS", emoji="🚀", style=discord.ButtonStyle.success, row=1)
    async def b_new(s, i, b): await i.response.edit_message(embed=deploy_intro(), view=DeployView(s.uid))

class VPSPanel(OV):
    def __init__(s, uid, c): super().__init__(uid); s.c = c
    async def pre(s, i, defer=True, active=True):
        r = find(s.c); g = guard(r, i.user.id, active) if r else "VPS no longer exists."
        if g: await i.response.send_message(embed=err(g), ephemeral=True); return None
        if defer: await i.response.defer()
        return r
    async def refresh(s, i):
        r = find(s.c)
        if r: await i.edit_original_response(embed=await vps_embed(r), view=s)
    async def act(s, i, act, label):
        r = await s.pre(i)
        if not r: return
        ok, o = await do_act(act, r)
        await i.followup.send(embed=emb(("✅ " if ok else "❌ ") + label, f"```{trim(o, 500)}```", 0x2ECC71 if ok else RED), ephemeral=True); await s.refresh(i)
    @discord.ui.button(label="Start", emoji="▶️", style=discord.ButtonStyle.success, row=0)
    async def b1(s, i, b): await s.act(i, "start", "Start")
    @discord.ui.button(label="Stop", emoji="⏹️", style=discord.ButtonStyle.danger, row=0)
    async def b2(s, i, b): await s.act(i, "stop", "Stop")
    @discord.ui.button(label="Restart", emoji="🔄", style=discord.ButtonStyle.primary, row=0)
    async def b3(s, i, b): await s.act(i, "restart", "Restart")
    @discord.ui.button(label="Refresh", emoji="♻️", style=discord.ButtonStyle.secondary, row=0)
    async def b4(s, i, b):
        if await s.pre(i): await s.refresh(i)
    @discord.ui.button(label="Console", emoji="⌨️", style=discord.ButtonStyle.success, row=0)
    async def b4c(s, i, b):
        r = await s.pre(i, False)
        if not r: return
        if await lxstate(r["name"]) != "RUNNING": return await i.response.send_message(embed=err("Start the VPS first — the console needs it running."), ephemeral=True)
        await i.response.edit_message(embed=console_embed(r), view=ConsoleView(s.uid, r["name"]))
    @discord.ui.button(label="New SSH (Pinggy)", emoji="🔌", style=discord.ButtonStyle.primary, row=1)
    async def b5(s, i, b):
        r = await s.pre(i)
        if not r: return
        addr, e = await start_tunnel(r["name"])
        await i.followup.send(embed=err(e) if e else emb("🔌 Pinggy SSH Ready", f"```{ssh_line(addr)}```\nLogin: `root` + your password (use **Reset Pass** if lost).", 0x2ECC71), ephemeral=True); await s.refresh(i)
    @discord.ui.button(label="sshx Terminal", emoji="🌍", style=discord.ButtonStyle.primary, row=1)
    async def b6(s, i, b):
        r = await s.pre(i)
        if not r: return
        await i.followup.send(embed=emb("🌍 Starting sshx…", "Takes ~15 seconds."), ephemeral=True)
        url, e = await start_sshx(r["name"])
        await i.followup.send(embed=err(e) if e else emb("🌍 sshx Web Terminal", url, 0x2ECC71), ephemeral=True); await s.refresh(i)
    @discord.ui.button(label="Stop Tunnels", emoji="🛑", style=discord.ButtonStyle.secondary, row=1)
    async def b7(s, i, b):
        r = await s.pre(i)
        if not r: return
        await stop_tunnel(r["name"]); await stop_sshx(r["name"]); await s.refresh(i)
    @discord.ui.button(label="Snapshot", emoji="📸", style=discord.ButtonStyle.secondary, row=2)
    async def b8(s, i, b):
        r = await s.pre(i)
        if not r: return
        n = "snap-" + time.strftime("%m%d-%H%M%S"); rc, o = await lx("snapshot", r["name"], n, timeout=300)
        await i.followup.send(embed=emb("📸 Snapshot", f"`{n}` created" if rc == 0 else o, 0x2ECC71 if rc == 0 else RED), ephemeral=True)
    @discord.ui.button(label="Stats", emoji="📈", style=discord.ButtonStyle.secondary, row=2)
    async def b9(s, i, b):
        r = await s.pre(i)
        if not r: return
        u = await usage(r["name"], r, 2); await i.followup.send(embed=usage_embed(r, u) if u else err("VPS must be running."), ephemeral=True)
    @discord.ui.button(label="Reset Pass", emoji="🔐", style=discord.ButtonStyle.secondary, row=2)
    async def b10(s, i, b):
        r = await s.pre(i)
        if not r: return
        pw = rpass(); rc, o = await inside(r["name"], 'echo "root:$PW" | chpasswd', 30, {"PW": pw})
        await i.followup.send(embed=emb("🔐 New root password", f"`{pw}`", 0x2ECC71) if rc == 0 else err(o), ephemeral=True)
    @discord.ui.button(label="Delete", emoji="🗑️", style=discord.ButtonStyle.danger, row=3)
    async def b11(s, i, b):
        r = await s.pre(i, False)
        if not r: return
        async def fn(): return await do_act("delete", r)
        await i.response.send_message(embed=emb("⚠️ Delete VPS?", f"`{r['name']}` and all its data will be destroyed.", RED), view=ConfirmView(i.user.id, fn, "Delete forever"), ephemeral=True)
    @discord.ui.button(label="Back", emoji="⬅️", style=discord.ButtonStyle.secondary, row=3)
    async def b12(s, i, b): await i.response.edit_message(embed=manage_embed(s.uid), view=ManageView(s.uid))
    @discord.ui.button(label="Backup", emoji="💾", style=discord.ButtonStyle.secondary, row=4)
    async def b13(s, i, b):
        r = await s.pre(i)
        if not r: return
        await i.followup.send(embed=emb("💾 Backup started", "This can take a few minutes…"), ephemeral=True); ok, m = await do_backup(r)
        await i.followup.send(embed=emb("💾 Backup", m, 0x2ECC71 if ok else RED), ephemeral=True)
    @discord.ui.button(label="Auto-SSH", emoji="🔁", style=discord.ButtonStyle.secondary, row=4)
    async def b14(s, i, b):
        r = await s.pre(i)
        if not r: return
        q("UPDATE vps SET autossh=? WHERE name=?", (0 if r["autossh"] else 1, r["name"])); await s.refresh(i)
    @discord.ui.button(label="Renew", emoji="⏳", style=discord.ButtonStyle.success, row=4)
    async def b15(s, i, b):
        r = await s.pre(i, True, False)
        if not r: return
        ok, m = await do_renew(r); await i.followup.send(embed=emb("⏳ Renew", m, 0x2ECC71 if ok else RED), ephemeral=True); await s.refresh(i)
    @discord.ui.button(label="Web Port", emoji="🌐", style=discord.ButtonStyle.secondary, row=4)
    async def b16(s, i, b):
        r = await s.pre(i, False)
        if r: await i.response.send_modal(PortModal(r["name"]))
    @discord.ui.button(label="Logs", emoji="🧾", style=discord.ButtonStyle.secondary, row=3)
    async def b17(s, i, b):
        r = await s.pre(i)
        if not r: return
        rc, o = await inside(r["name"], LOGCMD, 30); await i.followup.send(embed=emb("🧾 Logs", f"```\n{trim(o, 1700) or 'empty'}\n```"), ephemeral=True)

class PortModal(discord.ui.Modal, title="Expose a web port"):
    port = discord.ui.TextInput(label="Port inside the VPS (e.g. 80, 3000, 8080)", max_length=5)
    def __init__(s, c): super().__init__(); s.c = c
    async def on_submit(s, i):
        r = find(s.c); g = guard(r, i.user.id) if r else "VPS not found."
        if g: return await i.response.send_message(embed=err(g), ephemeral=True)
        if not str(s.port).isdigit() or not 1 <= int(str(s.port)) <= 65535: return await i.response.send_message(embed=err("Invalid port."), ephemeral=True)
        await i.response.defer(ephemeral=True); url, e = await start_http(r["name"], int(str(s.port)))
        await i.followup.send(embed=err(e) if e else emb("🌐 Web link ready", f"{url}\n→ port `{s.port}` of `{r['name']}`", 0x2ECC71), ephemeral=True)

async def dash_embed():
    vm, du = psutil.virtual_memory(), psutil.disk_usage("/")
    rc, o = await lx("list", "-c", "ns", "--format", "csv"); live = dict(l.split(",", 1) for l in o.splitlines() if "," in l) if rc == 0 else {}
    rows = q("SELECT name,suspended FROM vps"); run = sum(1 for r in rows if live.get(r["name"], "").upper() == "RUNNING")
    e = emb("📊 ArizNodes Dashboard", f"Maintenance: **{'ON 🛠️' if gset('maint') == '1' else 'OFF'}**  •  Uptime `{upt(time.time() - START)}`")
    e.add_field(name="🧠 CPU", value=f"`{bar(psutil.cpu_percent())}`", inline=False); e.add_field(name="💾 RAM", value=f"`{bar(vm.percent)}`", inline=False)
    e.add_field(name="💽 Disk", value=f"`{bar(du.percent)}`", inline=False)
    e.add_field(name="🖥️ VPS", value=f"{len(rows)} total\n{run} running"); e.add_field(name="⛔ Suspended", value=str(sum(1 for r in rows if r['suspended'])))
    e.add_field(name="🔌 Tunnels", value=str(len(TUN))); e.add_field(name="👥 Users", value=str(q("SELECT COUNT(DISTINCT owner) c FROM vps", one=True)["c"]))
    e.add_field(name="🏓 Latency", value=f"{bot.latency * 1000:.0f}ms"); return e
class BroadcastModal(discord.ui.Modal, title="Broadcast to all VPS owners"):
    msg = discord.ui.TextInput(label="Message", style=discord.TextStyle.paragraph, max_length=1500)
    async def on_submit(s, i):
        owners = [r["owner"] for r in q("SELECT DISTINCT owner FROM vps")]
        await i.response.send_message(embed=emb("📢 Broadcasting…", f"Sending to **{len(owners)}** users in the background."), ephemeral=True)
        async def go():
            for o in owners: await notify(o, emb("📢 Announcement", str(s.msg.value))); await asyncio.sleep(1)
        asyncio.create_task(go())
class DashView(OV):
    def __init__(s, uid):
        super().__init__(uid)
        rows = q("SELECT name,owner,suspended FROM vps ORDER BY created DESC LIMIT 25")
        if rows:
            sel = discord.ui.Select(placeholder="🖥️ Open any VPS (admin control)", options=[discord.SelectOption(label=r["name"], description=f"owner {r['owner']}" + (" • suspended" if r["suspended"] else ""), emoji="🖥️") for r in rows])
            async def cb(i):
                r = find(sel.values[0])
                if r: await i.response.send_message(embed=await vps_embed(r), view=VPSPanel(i.user.id, r["name"]), ephemeral=True)
            sel.callback = cb; s.add_item(sel)
        th = discord.ui.Select(placeholder="🎨 Bot theme", row=1, options=[discord.SelectOption(label=v[2], value=k, emoji=v[1], default=(k == gset("theme", "fire"))) for k, v in THEMES.items()])
        async def tcb(i): sset("theme", th.values[0]); await i.response.edit_message(embed=await dash_embed(), view=DashView(s.uid))
        th.callback = tcb; s.add_item(th)
    @discord.ui.button(label="Refresh", emoji="♻️", style=discord.ButtonStyle.primary, row=2)
    async def d1(s, i, b): await i.response.edit_message(embed=await dash_embed(), view=DashView(s.uid))
    @discord.ui.button(label="Maintenance", emoji="🛠️", style=discord.ButtonStyle.secondary, row=2)
    async def d3(s, i, b): sset("maint", "0" if gset("maint") == "1" else "1"); await i.response.edit_message(embed=await dash_embed(), view=DashView(s.uid))
    @discord.ui.button(label="Kill Tunnels", emoji="🛑", style=discord.ButtonStyle.danger, row=2)
    async def d4(s, i, b):
        for c in list(TUN): await stop_tunnel(c)
        await i.response.edit_message(embed=await dash_embed(), view=DashView(s.uid))
    @discord.ui.button(label="Users", emoji="👥", style=discord.ButtonStyle.secondary, row=3)
    async def d5(s, i, b):
        rows = q("SELECT owner,COUNT(*) c FROM vps GROUP BY owner ORDER BY c DESC LIMIT 15"); await i.response.send_message(embed=emb("👥 Top VPS owners", "\n".join(f"<@{r['owner']}> — **{r['c']}** VPS" for r in rows) or "none"), ephemeral=True)
    @discord.ui.button(label="Broadcast", emoji="📢", style=discord.ButtonStyle.secondary, row=3)
    async def d6(s, i, b): await i.response.send_modal(BroadcastModal())
    @discord.ui.button(label="Web Panel", emoji="🌐", style=discord.ButtonStyle.primary, row=3)
    async def d7(s, i, b):
        if not (DASH_PASS or DISCORD_SECRET): return await i.response.send_message(embed=err("The website is disabled. Set `DISCORD_CLIENT_SECRET` and/or `DASH_PASSWORD` in `.env` and restart the bot."), ephemeral=True)
        await i.response.send_message(embed=web_info_embed(), ephemeral=True)
    @discord.ui.button(label="Audit", emoji="📜", style=discord.ButtonStyle.secondary, row=3)
    async def d8(s, i, b):
        rows = q("SELECT * FROM audit ORDER BY id DESC LIMIT 12"); await i.response.send_message(embed=emb("📜 Recent activity", "\n".join(f"<t:{r['ts']}:t> <@{r['uid']}> **{r['action']}** {r['detail']}" for r in rows) or "empty"), ephemeral=True)

TITLES = {"vps": "🖥️ VPS", "admin": "🛡️ Admin & Dashboard", "util": "🧰 Utility & Fun", "pro": "⚡ Pro"}; CAT = {}
def help_home():
    e = emb("🔥 ArizNodesLabs VPS Deployer", f"Prefix `{PREFIX}` • **{len(CAT)} commands**\nPick a category below, or use `{PREFIX}help <command>`.\n\n```\n{art('ArizNodes')}\n```")
    for k, t in TITLES.items(): e.add_field(name=t, value=f"{sum(1 for c in CAT.values() if c == k)} commands")
    return e
def help_cat(k):
    names = sorted(n for n, c in CAT.items() if c == k); return emb(f"{TITLES[k]} — {len(names)} commands", " ".join(f"`{PREFIX}{n}`" for n in names))
class HelpView(OV):
    def __init__(s, uid):
        super().__init__(uid); sel = discord.ui.Select(placeholder="📚 Choose a category", options=[discord.SelectOption(label="Home", value="home", emoji="🏠")] + [discord.SelectOption(label=t[2:].strip(), value=k, emoji=t[0]) for k, t in TITLES.items()])
        async def cb(i): v = sel.values[0]; await i.response.edit_message(embed=help_home() if v == "home" else help_cat(v), view=s)
        sel.callback = cb; s.add_item(sel)
class PanelView(discord.ui.View):
    def __init__(s): super().__init__(timeout=None)
    @discord.ui.button(label="Deploy VPS", emoji="🚀", style=discord.ButtonStyle.success, custom_id="ariz:deploy")
    async def p1(s, i, b): await i.response.send_message(embed=deploy_intro(), view=DeployView(i.user.id), ephemeral=True)
    @discord.ui.button(label="My VPS", emoji="🖥️", style=discord.ButtonStyle.primary, custom_id="ariz:manage")
    async def p2(s, i, b): await i.response.send_message(embed=manage_embed(i.user.id), view=ManageView(i.user.id), ephemeral=True)
    @discord.ui.button(label="Dashboard", emoji="📊", style=discord.ButtonStyle.secondary, custom_id="ariz:dash")
    async def p3(s, i, b):
        if not is_admin(i.user.id): return await i.response.send_message(embed=err("Admins only."), ephemeral=True)
        await i.response.send_message(embed=await dash_embed(), view=DashView(i.user.id), ephemeral=True)
    @discord.ui.button(label="Help", emoji="❓", style=discord.ButtonStyle.secondary, custom_id="ariz:help")
    async def p4(s, i, b): await i.response.send_message(embed=help_home(), view=HelpView(i.user.id), ephemeral=True)

# ───────────────────────── bot + command registry ─────────────────────────
intents = discord.Intents.default(); intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents, help_command=None, case_insensitive=True)
def chk_admin(ctx):
    if is_admin(ctx.author.id): return True
    raise commands.CheckFailure("🔒 Admins only.")
def chk_owner(ctx):
    if ctx.author.id in OWNERS: return True
    raise commands.CheckFailure("🔒 Bot owner only.")
def cmd(cat, brief="", level=0, name=None, **kw):
    def deco(f):
        c = commands.Command(f, name=name or f.__name__.rstrip("_"), brief=brief, **kw)
        if level == 1: c.add_check(chk_admin)
        if level == 2: c.add_check(chk_owner)
        bot.add_command(c); CAT[c.name] = cat; return f
    return deco
@bot.check
async def gate(ctx):
    if is_admin(ctx.author.id): return True
    if urow(ctx.author.id)["banned"]: raise commands.CheckFailure("🚫 You are banned from this bot.")
    if gset("maint") == "1" and CAT.get(ctx.command.name) in ("vps", "pro"): raise commands.CheckFailure("🛠️ Maintenance mode — VPS commands are temporarily disabled.")
    return True
@bot.event
async def on_command_error(ctx, e):
    e = getattr(e, "original", e)
    if isinstance(e, commands.CommandNotFound): return
    if isinstance(e, commands.CheckFailure): m = str(e) or "You can't use that."
    elif isinstance(e, commands.MissingRequiredArgument): m = f"Missing `{e.param.name}`.\nUsage: `{PREFIX}{ctx.command.name} {ctx.command.signature}`"
    elif isinstance(e, (commands.BadArgument, commands.BadUnionArgument)): m = f"Bad argument. Usage: `{PREFIX}{ctx.command.name} {ctx.command.signature}`"
    elif isinstance(e, discord.Forbidden): m = "I lack permission to do that."
    else: m = f"{type(e).__name__}: {e}"; print("ERR", ctx.command, repr(e))
    await ctx.send(embed=err(m))
async def mine(ctx, ref=None, active=True):
    if ref is None:
        rows = q("SELECT * FROM vps WHERE owner=?", (ctx.author.id,))
        if len(rows) != 1: await ctx.send(embed=err(f"Specify a VPS name — see `{PREFIX}myvps`.")); return None
        r = rows[0]
    else: r = find(ref)
    if not r: await ctx.send(embed=err(f"VPS not found. See `{PREFIX}myvps`.")); return None
    g = guard(r, ctx.author.id, active)
    if g: await ctx.send(embed=err(g)); return None
    return r
async def dm_or_here(ctx, e):
    try: await ctx.author.send(embed=e); return "📬 Details sent to your DMs."
    except discord.Forbidden: await ctx.send(embed=e, delete_after=120); return "⚠️ DMs closed — shown above for 2 min."

# ═════════════════════ CATEGORY 1 — VPS (50) ═════════════════════
@cmd("vps", "Deploy a VPS: !deploy [os] [plan]")
async def deploy(ctx, osk: str = None, plan: str = None):
    if not osk: return await ctx.send(embed=deploy_intro(), view=DeployView(ctx.author.id))
    m = await ctx.send(embed=progress_embed(0, "Starting"))
    async def prog(n, t): await m.edit(embed=progress_embed(n, t))
    res, e = await deploy_vps(ctx.author.id, osk.lower(), (plan or DEF_PLAN).lower(), prog)
    if e: return await m.edit(embed=err(e))
    note = await dm_or_here(ctx, cred_embed(res)); await m.edit(embed=emb("✅ VPS Deployed", f"`{res['name']}` is online!\n{note}\nControl it with `{PREFIX}manage`.", 0x2ECC71))
@cmd("vps", "Open the premium VPS manager")
async def manage(ctx): await ctx.send(embed=manage_embed(ctx.author.id), view=ManageView(ctx.author.id))
@cmd("vps", "List your VPS")
async def myvps(ctx):
    rows = q("SELECT * FROM vps WHERE owner=?", (ctx.author.id,)); lines = []
    for r in rows: lines.append(f"{'🟢' if await lxstate(r['name']) == 'RUNNING' else '🔴'} `{r['name']}` • {IMAGES.get(r['os'], (r['os'],))[0]} • {r['ram']}MB/{r['cpu']}c/{r['disk']}G")
    await ctx.send(embed=emb(f"🖥️ Your VPS ({len(rows)}/{ulimit(ctx.author.id)})", "\n".join(lines) or f"None yet — `{PREFIX}deploy`"))
@cmd("vps", "Detailed VPS info")
async def vpsinfo(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if r: await ctx.send(embed=await vps_embed(r))
def mk_act(act, brief):
    async def f(ctx, name: str = None):
        r = await mine(ctx, name)
        if not r: return
        ok, o = await do_act(act, r); await ctx.send(embed=emb(("✅ " if ok else "❌ ") + act.title(), f"`{r['name']}` — {trim(o, 400)}", 0x2ECC71 if ok else RED))
    f.__name__ = act; cmd("vps", brief)(f)
for _a, _b in [("start", "Start a VPS"), ("stop", "Stop a VPS"), ("restart", "Restart a VPS"), ("kill", "Force-stop a VPS"), ("pause", "Freeze a VPS"), ("resume", "Unfreeze a VPS")]: mk_act(_a, _b)
@cmd("vps", "Delete a VPS (confirm)")
async def delete(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if not r: return
    async def fn(): return await do_act("delete", r)
    await ctx.send(embed=emb("⚠️ Delete VPS?", f"`{r['name']}` will be destroyed forever.", RED), view=ConfirmView(ctx.author.id, fn, "Delete forever"))
@cmd("vps", "Open a new Pinggy SSH link")
async def ssh(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    m = await ctx.send(embed=emb("🔌 Opening Pinggy tunnel…")); addr, e = await start_tunnel(r["name"])
    if e: return await m.edit(embed=err(e))
    note = await dm_or_here(ctx, emb("🔌 Pinggy SSH Ready", f"`{r['name']}`\n```{ssh_line(addr)}```Login: `root` + password (`{PREFIX}resetpass` if lost).", 0x2ECC71)); await m.edit(embed=emb("✅ Tunnel ready", note, 0x2ECC71))
@cmd("vps", "Close the Pinggy tunnel")
async def sshstop(ctx, name: str = None):
    r = await mine(ctx, name)
    if r: await stop_tunnel(r["name"]); await ctx.send(embed=emb("🛑 Tunnel closed", r["name"]))
@cmd("vps", "Start an sshx web terminal link")
async def sshx(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    m = await ctx.send(embed=emb("🌍 Starting sshx…", "~15 seconds")); url, e = await start_sshx(r["name"])
    if e: return await m.edit(embed=err(e))
    note = await dm_or_here(ctx, emb("🌍 sshx Terminal", url, 0x2ECC71)); await m.edit(embed=emb("✅ sshx ready", note, 0x2ECC71))
@cmd("vps", "Stop the sshx session")
async def sshxstop(ctx, name: str = None):
    r = await mine(ctx, name)
    if r: await stop_sshx(r["name"]); await ctx.send(embed=emb("🛑 sshx stopped", r["name"]))
@cmd("vps", "Reset the root password")
async def resetpass(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    pw = rpass(); rc, o = await inside(r["name"], 'echo "root:$PW" | chpasswd', 30, {"PW": pw})
    await ctx.send(embed=err(o)) if rc else await ctx.send(embed=emb("🔐 Password reset", await dm_or_here(ctx, emb("🔐 New root password", f"`{r['name']}`: `{pw}`", 0x2ECC71)), 0x2ECC71))
@cmd("vps", "Rename a VPS: !rename old new")
async def rename(ctx, name: str, new: str):
    r = await mine(ctx, name)
    if not r: return
    new = "ariz-" + re.sub(r"[^a-z0-9-]", "", new.lower().removeprefix("ariz-"))[:20]
    if len(new) < 8 or find(new): return await ctx.send(embed=err("Invalid or taken name (3+ chars, a-z 0-9 -)."))
    await do_act("stop", r); rc, o = await lx("rename", r["name"], new)
    if rc: return await ctx.send(embed=err(o))
    q("UPDATE vps SET name=? WHERE name=?", (new, r["name"])); await lx("start", new); await ctx.send(embed=emb("✏️ Renamed", f"`{r['name']}` → `{new}`", 0x2ECC71))
@cmd("vps", "Create a snapshot: !snapshot [name] [label]")
async def snapshot(ctx, name: str = None, label: str = None):
    r = await mine(ctx, name)
    if not r: return
    label = re.sub(r"[^\w-]", "", label or "snap-" + time.strftime("%m%d-%H%M%S")); rc, o = await lx("snapshot", r["name"], label, timeout=300)
    await ctx.send(embed=emb("📸 Snapshot", f"`{label}` created" if rc == 0 else o, 0x2ECC71 if rc == 0 else RED))
async def snaps(c):
    rc, o = await lx("query", f"/1.0/instances/{c}/snapshots")
    try: import json; return [p.split("/")[-1] for p in json.loads(o)]
    except Exception: return []
@cmd("vps", "List snapshots")
async def snapshots(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if r: s = await snaps(r["name"]); await ctx.send(embed=emb(f"📸 Snapshots • {r['name']}", "\n".join(f"`{x}`" for x in s) or "none"))
@cmd("vps", "Restore a snapshot: !restore name snap")
async def restore(ctx, name: str, snap: str):
    r = await mine(ctx, name)
    if r: rc, o = await lx("restore", r["name"], snap, timeout=300); await ctx.send(embed=emb("↩️ Restore", f"`{snap}` restored" if rc == 0 else o, 0x2ECC71 if rc == 0 else RED))
@cmd("vps", "Delete a snapshot: !delsnapshot name snap")
async def delsnapshot(ctx, name: str, snap: str):
    r = await mine(ctx, name)
    if r: rc, o = await lx("delete", f"{r['name']}/{snap}"); await ctx.send(embed=emb("🗑️ Snapshot", "deleted" if rc == 0 else o, 0x2ECC71 if rc == 0 else RED))
async def resize(ctx, name, val, lo, hi, key, unit):
    r = await mine(ctx, name)
    if not r: return
    if not lo <= val <= hi: return await ctx.send(embed=err(f"Allowed range: {lo}–{hi}{unit}."))
    if key == "disk":
        rc, o = await lx("config", "device", "set", r["name"], "root", f"size={val}GiB")
        if rc: rc, o = await lx("config", "device", "override", r["name"], "root", f"size={val}GiB")
    else: rc, o = await lx("config", "set", r["name"], "limits.memory" if key == "ram" else "limits.cpu", f"{val}MiB" if key == "ram" else str(val))
    if rc: return await ctx.send(embed=err(o))
    q(f"UPDATE vps SET {key}=? WHERE name=?", (val, r["name"])); await ctx.send(embed=emb("⚙️ Resized", f"`{r['name']}` {key.upper()} → **{val}{unit}**", 0x2ECC71))
@cmd("vps", "Set RAM (MB): !setram name mb")
async def setram(ctx, name: str, mb: int): await resize(ctx, name, mb, 256, MAX_RAM, "ram", "MB")
@cmd("vps", "Set vCPU: !setcpu name n")
async def setcpu(ctx, name: str, n: int): await resize(ctx, name, n, 1, MAX_CPU, "cpu", " vCPU")
@cmd("vps", "Set disk (GB): !setdisk name gb")
async def setdisk(ctx, name: str, gb: int): await resize(ctx, name, gb, 1, MAX_DISK, "disk", "GB")
@cmd("vps", "Reinstall with another OS: !reinstall name [os]")
async def reinstall(ctx, name: str, osk: str = None):
    r = await mine(ctx, name)
    if not r: return
    osk = (osk or r["os"]).lower()
    if osk not in IMAGES: return await ctx.send(embed=err("Unknown OS."))
    async def fn():
        await stop_tunnel(r["name"]); await lx("delete", "-f", r["name"], timeout=180)
        pw, e = await provision(r["name"], IMAGES[osk][1], r["ram"], r["cpu"], r["disk"])
        if e: q("DELETE FROM vps WHERE name=?", (r["name"],)); return False, e
        q("UPDATE vps SET os=?, ssh='', sshx='' WHERE name=?", (osk, r["name"])); await dm_or_here(ctx, emb("♻️ Reinstalled", f"`{r['name']}` root password: `{pw}`", 0x2ECC71)); return True, "Reinstalled. New password sent."
    await ctx.send(embed=emb("⚠️ Reinstall?", f"All data on `{r['name']}` will be wiped.", RED), view=ConfirmView(ctx.author.id, fn, "Reinstall"))
@cmd("vps", "List available operating systems")
async def images(ctx): await ctx.send(embed=emb("💿 Operating Systems", "\n".join(f"{v[2]} `{k}` — {v[0]}" for k, v in IMAGES.items()) + f"\n\nUse `{PREFIX}deploy <key> [plan]`"))
@cmd("vps", "List plans")
async def plans(ctx): await ctx.send(embed=emb("📦 Plans", "\n".join(f"**{k}** — {v[0]}MB RAM • {v[1]} vCPU • {v[2]}GB disk" for k, v in PLANS.items())))
@cmd("vps", "Run a command inside your VPS: !exec name <cmd>")
async def exec_(ctx, name: str, *, command: str):
    r = await mine(ctx, name)
    if not r: return
    if await lxstate(r["name"]) != "RUNNING": return await ctx.send(embed=err("VPS must be running."))
    rc, o = await inside(r["name"], command, 120); await ctx.send(embed=emb(f"💻 {r['name']} (exit {rc})", f"```\n{trim(o, 1800) or 'no output'}\n```"))
@cmd("vps", "Live resource stats")
async def stats(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if r: rc, o = await lx("info", r["name"]); await ctx.send(embed=emb(f"📈 {r['name']}", f"```\n{trim(o, 1800)}\n```"))
def mk_quick(n, brief, script, to=60):
    async def f(ctx, name: str = None):
        r = await mine(ctx, name)
        if not r: return
        if await lxstate(r["name"]) != "RUNNING": return await ctx.send(embed=err("VPS must be running."))
        m = await ctx.send(embed=emb(f"⏳ {n}", "Running…")); rc, o = await inside(r["name"], script, to)
        await m.edit(embed=emb(f"{'✅' if rc == 0 else '⚠️'} {n} • {r['name']}", f"```\n{trim(o, 1800) or 'no output'}\n```"))
    f.__name__ = n; cmd("vps", brief)(f)
for _n, _b, _s, _t in [
 ("vuptime", "VPS uptime", "uptime -p 2>/dev/null || uptime", 30), ("vprocs", "Top processes by memory", "(ps aux --sort=-%mem 2>/dev/null || ps aux) | head -12", 30),
 ("vdisk", "Disk usage", "df -h /", 30), ("vmem", "Memory usage", "free -h", 30), ("vcpu", "CPU info", '(lscpu 2>/dev/null || (nproc; grep -m1 "model name" /proc/cpuinfo)) | head -15', 30),
 ("vos", "OS release", "head -6 /etc/os-release", 30), ("vkernel", "Kernel", "uname -a", 30), ("vnet", "Network interfaces", "ip -br a 2>/dev/null || ifconfig", 30),
 ("vports", "Listening ports", "ss -tulpn 2>/dev/null || netstat -tulpn", 30), ("vusers", "System users", "cut -d: -f1 /etc/passwd | tr '\\n' ' '", 30),
 ("vdate", "Date/time", "date", 30), ("vhost", "Hostname", "hostname", 30), ("vload", "Load average", "cat /proc/loadavg", 30), ("vtop", "top snapshot", "top -bn1 | head -15", 30),
 ("vupdate", "Refresh package lists", "if command -v apt-get >/dev/null; then apt-get update -y; elif command -v dnf >/dev/null; then dnf makecache; elif command -v apk >/dev/null; then apk update; elif command -v pacman >/dev/null; then pacman -Sy --noconfirm; fi", 300),
 ("vdocker", "Install Docker", "curl -fsSL https://get.docker.com | sh && docker --version", 900), ("vnode", "Install Node.js", pm("nodejs npm") + "; node -v", 600),
 ("vpython", "Install Python 3 + pip", pm("python3 python3-pip") + "; python3 --version", 600), ("vgit", "Install Git", pm("git") + "; git --version", 600),
 ("vtools", "Install curl/wget/git/nano/htop", pm("curl wget git nano htop"), 600), ("vneofetch", "System summary", "neofetch --stdout 2>/dev/null || cat /etc/os-release", 30)]: mk_quick(_n, _b, _s, _t)

# ═════════════════════ CATEGORY 2 — ADMIN & DASHBOARD (50) ═════════════════════
@cmd("admin", "Open the admin dashboard", 1)
async def dashboard(ctx): await ctx.send(embed=await dash_embed(), view=DashView(ctx.author.id))
def panel_embed():
    return emb(f"{theme()[1]} ArizNodesLabs — VPS Cloud", f"```\n{art('ArizNodes')}\n```\n### Premium VPS, one tap away\n🚀 **Deploy** in seconds  ·  🖥️ **Manage** every VPS  ·  ⌨️ **Console**\n🔌 **Pinggy SSH**  ·  🌍 **sshx terminal**  ·  🌐 **Web links**  ·  💾 **Backups**\n\n*Press a button below to get started.*")
@cmd("admin", "Post the public deploy panel", 1)
async def panel(ctx): await ctx.send(embed=panel_embed(), view=PanelView())
@cmd("admin", "Host CPU/RAM/disk stats", 1)
async def hoststats(ctx):
    vm, du = psutil.virtual_memory(), psutil.disk_usage("/"); await ctx.send(embed=emb("🖥️ Host Stats", f"CPU `{bar(psutil.cpu_percent(1))}`\nRAM `{bar(vm.percent)}` {vm.used >> 20}/{vm.total >> 20}MB\nDisk `{bar(du.percent)}` {du.used >> 30}/{du.total >> 30}GB\nLoad `{os.getloadavg()}`"))
@cmd("admin", "List all VPS: !allvps [page]", 1)
async def allvps(ctx, page: int = 1):
    rows = q("SELECT * FROM vps ORDER BY created DESC LIMIT 15 OFFSET ?", ((max(page, 1) - 1) * 15,)); await ctx.send(embed=emb(f"📋 All VPS • page {page}", "\n".join(f"`{r['name']}` <@{r['owner']}> {r['ram']}MB {'⛔' if r['suspended'] else ''}" for r in rows) or "empty"))
@cmd("admin", "A user's VPS", 1)
async def uservps(ctx, user: discord.User):
    rows = q("SELECT * FROM vps WHERE owner=?", (user.id,)); await ctx.send(embed=emb(f"🖥️ {user}", "\n".join(f"`{r['name']}` {IMAGES.get(r['os'], (r['os'],))[0]}" for r in rows) or "none"))
@cmd("admin", "A user's profile", 1)
async def userstats(ctx, user: discord.User):
    u = urow(user.id); n = q("SELECT COUNT(*) c FROM vps WHERE owner=?", (user.id,), True)["c"]; w = q("SELECT COUNT(*) c FROM warns WHERE uid=?", (user.id,), True)["c"]
    await ctx.send(embed=emb(f"👤 {user}", f"VPS: **{n}/{ulimit(user.id)}**\nBanned: **{bool(u['banned'])}**\nWarnings: **{w}**\nAdmin: **{is_admin(user.id)}**"))
def mk_susp(n, v):
    async def f(ctx, name: str):
        r = find(name)
        if not r: return await ctx.send(embed=err("VPS not found."))
        q("UPDATE vps SET suspended=? WHERE name=?", (v, r["name"]))
        if v: await do_act("stop", r)
        audit(ctx.author.id, n, r["name"]); await ctx.send(embed=emb(f"✅ {n.title()}", f"`{r['name']}`", 0x2ECC71))
    f.__name__ = n; cmd("admin", f"{n.title()} a VPS", 1)(f)
mk_susp("suspend", 1); mk_susp("unsuspend", 0)
def mk_ban(n, v):
    async def f(ctx, user: discord.User):
        urow(user.id); q("UPDATE users SET banned=? WHERE id=?", (v, user.id)); audit(ctx.author.id, n, str(user.id)); await ctx.send(embed=emb(f"✅ {n.title()}ned" if v else "✅ Unbanned", f"{user.mention}", 0x2ECC71))
    f.__name__ = n; cmd("admin", f"{n.title()} a user from the bot", 1)(f)
mk_ban("ban", 1); mk_ban("unban", 0)
@cmd("admin", "Bot-banned users", 1)
async def banlist(ctx): await ctx.send(embed=emb("🚫 Banned", "\n".join(f"<@{r['id']}>" for r in q("SELECT id FROM users WHERE banned=1")) or "none"))
@cmd("admin", "Set a user's VPS limit", 1)
async def setlimit(ctx, user: discord.User, n: int): urow(user.id); q("UPDATE users SET max_vps=? WHERE id=?", (n, user.id)); await ctx.send(embed=emb("✅ Limit set", f"{user.mention} → **{n}**", 0x2ECC71))
@cmd("admin", "Add a bot admin", 2)
async def addadmin(ctx, user: discord.User): q("INSERT OR IGNORE INTO admins VALUES(?)", (user.id,)); await ctx.send(embed=emb("✅ Admin added", user.mention, 0x2ECC71))
@cmd("admin", "Remove a bot admin", 2)
async def removeadmin(ctx, user: discord.User): q("DELETE FROM admins WHERE id=?", (user.id,)); await ctx.send(embed=emb("✅ Admin removed", user.mention, 0x2ECC71))
@cmd("admin", "List bot admins", 1)
async def admins(ctx): await ctx.send(embed=emb("👑 Admins", "\n".join(f"<@{i}>" for i in OWNERS | {r['id'] for r in q("SELECT id FROM admins")})))
def mk_force(act):
    async def f(ctx, name: str):
        r = find(name)
        if not r: return await ctx.send(embed=err("VPS not found."))
        ok, o = await do_act(act, r); await ctx.send(embed=emb(("✅ " if ok else "❌ ") + "Force " + act, f"`{r['name']}` {trim(o, 300)}", 0x2ECC71 if ok else RED))
    n = "force" + {"stop": "stop", "start": "start", "delete": "delete"}[act]; f.__name__ = n; cmd("admin", f"Admin: {act} any VPS", 1)(f)
for _a in ("delete", "stop", "start"): mk_force(_a)
@cmd("admin", "DM every VPS owner", 1)
async def broadcast(ctx, *, msg: str):
    n = 0
    for r in q("SELECT DISTINCT owner FROM vps"):
        try: u = await bot.fetch_user(r["owner"]); await u.send(embed=emb("📢 Announcement", msg)); n += 1; await asyncio.sleep(1)
        except Exception: pass
    await ctx.send(embed=emb("📢 Broadcast sent", f"Delivered to **{n}** users.", 0x2ECC71))
@cmd("admin", "Announce in a channel", 1)
async def announce(ctx, ch: discord.TextChannel, *, msg: str): await ch.send(embed=emb("📢 Announcement", msg)); await ctx.message.add_reaction("✅")
@cmd("admin", "Set audit-log channel", 1)
async def setlog(ctx, ch: discord.TextChannel): sset("logch", ch.id); await ctx.send(embed=emb("✅ Log channel set", ch.mention, 0x2ECC71))
@cmd("admin", "Maintenance mode: !maintenance on|off", 1)
async def maintenance(ctx, mode: str = None):
    sset("maint", "1" if (mode or ("off" if gset("maint") == "1" else "on")).lower() == "on" else "0"); await ctx.send(embed=emb("🛠️ Maintenance", "ON" if gset("maint") == "1" else "OFF"))
@cmd("admin", "Reload .env limits", 2)
async def reloadcfg(ctx):
    global OWNERS, MAX_VPS
    load_dotenv(override=True); OWNERS = {int(x) for x in re.findall(r"\d+", env("OWNER_IDS"))}; MAX_VPS = int(env("MAX_VPS_PER_USER", "3")); await ctx.send(embed=emb("♻️ Config reloaded", None, 0x2ECC71))
@cmd("admin", "Restart the bot", 2)
async def restartbot(ctx): await ctx.send(embed=emb("🔄 Restarting…")); os.execv(sys.executable, [sys.executable] + sys.argv)
@cmd("admin", "Shut the bot down", 2)
async def shutdown(ctx): await ctx.send(embed=emb("🛑 Shutting down…")); await bot.close()
@cmd("admin", "Run a shell command on the HOST", 2)
async def hostexec(ctx, *, command: str): rc, o = await sh("bash", "-c", command, timeout=120); await ctx.send(embed=emb(f"🖥️ host (exit {rc})", f"```\n{trim(o, 1800) or 'no output'}\n```"))
@cmd("admin", "Delete messages", 1)
async def purge(ctx, n: int): d = await ctx.channel.purge(limit=max(1, min(n, 200)) + 1); await ctx.send(embed=emb("🧹 Purged", f"{len(d) - 1} messages"), delete_after=5)
@cmd("admin", "Kick a member", 1)
async def kick(ctx, m: discord.Member, *, reason: str = "-"): await m.kick(reason=reason); await ctx.send(embed=emb("👢 Kicked", f"{m} — {reason}"))
@cmd("admin", "Timeout a member: !timeout @u minutes", 1)
async def timeout(ctx, m: discord.Member, minutes: int = 10): await m.timeout(dt.timedelta(minutes=minutes)); await ctx.send(embed=emb("⏳ Timed out", f"{m.mention} for {minutes}m"))
def mk_lock(n, v):
    async def f(ctx):
        ow = ctx.channel.overwrites_for(ctx.guild.default_role); ow.send_messages = v; await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=ow); await ctx.send(embed=emb("🔒 Channel locked" if v is False else "🔓 Channel unlocked"))
    f.__name__ = n; cmd("admin", f"{n.title()} this channel", 1)(f)
mk_lock("lock", False); mk_lock("unlock", None)
@cmd("admin", "Set slowmode seconds", 1)
async def slowmode(ctx, s: int = 0): await ctx.channel.edit(slowmode_delay=max(0, min(s, 21600))); await ctx.send(embed=emb("🐌 Slowmode", f"{s}s"))
@cmd("admin", "Change a member nickname", 1)
async def nick(ctx, m: discord.Member, *, nick: str = None): await m.edit(nick=nick); await ctx.send(embed=emb("✏️ Nickname", nick or "reset"))
@cmd("admin", "Give a role", 1)
async def addrole(ctx, m: discord.Member, role: discord.Role): await m.add_roles(role); await ctx.send(embed=emb("✅ Role added", f"{role.mention} → {m.mention}"))
@cmd("admin", "Remove a role", 1)
async def removerole(ctx, m: discord.Member, role: discord.Role): await m.remove_roles(role); await ctx.send(embed=emb("✅ Role removed", f"{role.mention} ← {m.mention}"))
@cmd("admin", "Warn a user", 1)
async def warn(ctx, m: discord.Member, *, reason: str = "-"): q("INSERT INTO warns(guild,uid,reason,ts) VALUES(?,?,?,?)", (ctx.guild.id, m.id, reason, int(time.time()))); await ctx.send(embed=emb("⚠️ Warned", f"{m.mention}: {reason}"))
@cmd("admin", "Show warnings", 1)
async def warnings(ctx, m: discord.Member): await ctx.send(embed=emb(f"⚠️ Warnings • {m}", "\n".join(f"<t:{r['ts']}:d> {r['reason']}" for r in q("SELECT * FROM warns WHERE uid=? AND guild=?", (m.id, ctx.guild.id))) or "none"))
@cmd("admin", "Clear warnings", 1)
async def clearwarns(ctx, m: discord.Member): q("DELETE FROM warns WHERE uid=? AND guild=?", (m.id, ctx.guild.id)); await ctx.send(embed=emb("✅ Cleared", m.mention, 0x2ECC71))
@cmd("admin", "Close every Pinggy tunnel", 1)
async def stopalltunnels(ctx):
    n = len(TUN)
    for c in list(TUN): await stop_tunnel(c)
    await ctx.send(embed=emb("🛑 Tunnels closed", str(n)))
@cmd("admin", "Remove DB rows of missing containers", 1)
async def cleanup(ctx):
    n = 0
    for r in q("SELECT name FROM vps"):
        if await lxstate(r["name"]) == "MISSING": q("DELETE FROM vps WHERE name=?", (r["name"],)); n += 1
    await ctx.send(embed=emb("🧹 Cleanup", f"Removed **{n}** orphan records.", 0x2ECC71))
@cmd("admin", "Send DB backup to your DMs", 2)
async def backupdb(ctx): await ctx.author.send(file=discord.File("vps.db")); await ctx.send(embed=emb("💾 Backup sent to DMs"))
@cmd("admin", "Database statistics", 1)
async def dbstats(ctx): await ctx.send(embed=emb("🗄️ Database", "\n".join(f"**{t}**: {q(f'SELECT COUNT(*) c FROM {t}', one=True)['c']}" for t in ("vps", "users", "admins", "warns", "audit"))))
@cmd("admin", "Transfer VPS: !transfer name @user", 1)
async def transfer(ctx, name: str, user: discord.User):
    r = find(name)
    if not r: return await ctx.send(embed=err("VPS not found."))
    q("UPDATE vps SET owner=? WHERE name=?", (user.id, r["name"])); await ctx.send(embed=emb("🔁 Transferred", f"`{r['name']}` → {user.mention}", 0x2ECC71))
@cmd("admin", "Local LXC image cache", 1)
async def hostimages(ctx): rc, o = await lx("image", "list", "-c", "lfd"); await ctx.send(embed=emb("🗃️ Cached images", f"```\n{trim(o, 1800)}\n```"))
@cmd("admin", "Raw `lxc list`", 1)
async def hostcontainers(ctx): rc, o = await lx("list", "-c", "ns4mc"); await ctx.send(embed=emb("📦 Containers", f"```\n{trim(o, 1800)}\n```"))
@cmd("admin", "LXC version", 1)
async def lxcversion(ctx): rc, o = await lx("version"); await ctx.send(embed=emb("ℹ️ LXC", f"```{o}```"))
@cmd("admin", "Change bot status text", 1)
async def setstatus(ctx, *, text: str): await bot.change_presence(activity=discord.Game(text)); await ctx.send(embed=emb("✅ Status set", text))
@cmd("admin", "Recent audit log", 1)
async def auditlog(ctx): await ctx.send(embed=emb("📜 Audit", "\n".join(f"<t:{r['ts']}:t> <@{r['uid']}> **{r['action']}** {r['detail']}" for r in q("SELECT * FROM audit ORDER BY id DESC LIMIT 15")) or "empty"))
@cmd("admin", "Count users & VPS", 1)
async def usercount(ctx): await ctx.send(embed=emb("👥 Users", f"Known: **{q('SELECT COUNT(*) c FROM users', one=True)['c']}**\nWith VPS: **{q('SELECT COUNT(DISTINCT owner) c FROM vps', one=True)['c']}**"))
@cmd("admin", "Top VPS owners", 1)
async def topusers(ctx): await ctx.send(embed=emb("🏆 Top owners", "\n".join(f"<@{r['owner']}> — {r['c']}" for r in q("SELECT owner,COUNT(*) c FROM vps GROUP BY owner ORDER BY c DESC LIMIT 10")) or "none"))

# ═════════════════════ CATEGORY 3 — UTILITY & FUN (50) ═════════════════════
@cmd("util", "Show commands")
async def help_(ctx, *, query: str = None):
    if query:
        c = bot.get_command(query.lower().lstrip(PREFIX))
        if not c: return await ctx.send(embed=err("Unknown command."))
        return await ctx.send(embed=emb(f"📖 {PREFIX}{c.name}", f"{c.brief or '-'}\n**Usage:** `{PREFIX}{c.name} {c.signature}`\n**Category:** {TITLES.get(CAT.get(c.name), '-')}"))
    await ctx.send(embed=help_home(), view=HelpView(ctx.author.id))
@cmd("util", "Latency")
async def ping(ctx): await ctx.send(embed=emb("🏓 Pong!", f"`{bot.latency * 1000:.0f} ms`"))
@cmd("util", "Bot uptime")
async def uptime(ctx): await ctx.send(embed=emb("⏱️ Uptime", f"`{upt(time.time() - START)}`"))
@cmd("util", "Bot information")
async def botinfo(ctx):
    e = emb("🤖 Bot Info", f"Servers **{len(bot.guilds)}** • Commands **{len(CAT)}** • VPS **{q('SELECT COUNT(*) c FROM vps', one=True)['c']}**\ndiscord.py `{discord.__version__}` • Python `{sys.version.split()[0]}`"); await ctx.send(embed=e)
@cmd("util", "Invite link")
async def invite(ctx): await ctx.send(embed=emb("🔗 Invite", f"https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands"))
@cmd("util", "About the project")
async def about(ctx): await ctx.send(embed=emb("🔥 About", f"```\n{art('ArizNodesLabs')}\n{art('Vasplayz90')}\n```LXC VPS deployer with Pinggy SSH + sshx."))
@cmd("util", "Credits")
async def credits(ctx): await ctx.send(embed=emb("💎 Credits", "Made by **Vasplayz90**\nPowered by **ArizNodesLabs**\nLXC • Pinggy • sshx • discord.py"))
@cmd("util", "Server info")
async def serverinfo(ctx):
    g = ctx.guild; await ctx.send(embed=emb(f"🏰 {g.name}", f"Members **{g.member_count}** • Channels **{len(g.channels)}** • Roles **{len(g.roles)}**\nOwner <@{g.owner_id}> • Created <t:{int(g.created_at.timestamp())}:R>"))
@cmd("util", "User info")
async def whois(ctx, m: discord.Member = None):
    m = m or ctx.author; e = emb(f"👤 {m}", f"ID `{m.id}`\nCreated <t:{int(m.created_at.timestamp())}:R>\nJoined <t:{int(m.joined_at.timestamp())}:R>"); e.set_thumbnail(url=m.display_avatar.url); await ctx.send(embed=e)
@cmd("util", "Avatar")
async def avatar(ctx, u: discord.User = None): u = u or ctx.author; e = emb(f"🖼️ {u}"); e.set_image(url=u.display_avatar.url); await ctx.send(embed=e)
@cmd("util", "Make the bot say something")
async def say(ctx, *, text: str):
    try: await ctx.message.delete()
    except Exception: pass
    await ctx.send(text, allowed_mentions=discord.AllowedMentions.none())
@cmd("util", "Custom embed: !embed title | text")
async def embed(ctx, *, text: str): t, _, d = text.partition("|"); await ctx.send(embed=emb(t.strip(), d.strip() or None))
@cmd("util", "Poll: !poll Q | a | b | c")
async def poll(ctx, *, text: str):
    p = [x.strip() for x in text.split("|")]
    if len(p) < 3: return await ctx.send(embed=err("Usage: `poll Question | a | b`"))
    m = await ctx.send(embed=emb("📊 " + p[0], "\n".join(f"{i + 1}\ufe0f\u20e3 {o}" for i, o in enumerate(p[1:10]))))
    for i in range(len(p[1:10])): await m.add_reaction(f"{i + 1}\ufe0f\u20e3")
@cmd("util", "Flip a coin")
async def coinflip(ctx): await ctx.send(embed=emb("🪙 Coin", random.choice(["Heads", "Tails"])))
@cmd("util", "Roll a d6")
async def dice(ctx): await ctx.send(embed=emb("🎲 Dice", str(random.randint(1, 6))))
@cmd("util", "Magic 8-ball", name="8ball")
async def eightball(ctx, *, q_: str = "?"): await ctx.send(embed=emb("🎱 8-Ball", random.choice(["Yes.", "No.", "Maybe.", "Definitely!", "Ask later.", "Doubtful.", "Without a doubt.", "Very unlikely.", "Signs point to yes.", "Cannot predict now."])))
@cmd("util", "Random joke")
async def joke(ctx): await ctx.send(embed=emb("😂 Joke", random.choice(["Why do programmers prefer dark mode? Light attracts bugs.", "There are 10 kinds of people: those who know binary and those who don't.", "A SQL query walks into a bar, sees two tables and asks: 'Can I join you?'", "!false — it's funny because it's true.", "I'd tell you a UDP joke, but you might not get it."])))
@cmd("util", "Choose: !choose a | b | c")
async def choose(ctx, *, opts: str): await ctx.send(embed=emb("🤔 I choose", random.choice([o.strip() for o in opts.split("|") if o.strip()] or ["nothing"])))
@cmd("util", "Roll NdM: !roll 2d20")
async def roll(ctx, spec: str = "1d20"):
    m = re.fullmatch(r"(\d{1,2})d(\d{1,4})", spec)
    if not m: return await ctx.send(embed=err("Use NdM, e.g. 2d20"))
    r = [random.randint(1, int(m.group(2))) for _ in range(int(m.group(1)))]; await ctx.send(embed=emb("🎲 Roll", f"{r} = **{sum(r)}**"))
_O = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.Pow: op.pow, ast.Mod: op.mod, ast.FloorDiv: op.floordiv}
def _ev(n):
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)): return n.value
    if isinstance(n, ast.BinOp) and type(n.op) in _O:
        a, b = _ev(n.left), _ev(n.right)
        if isinstance(n.op, ast.Pow) and abs(b) > 100: raise ValueError("exponent too large")
        return _O[type(n.op)](a, b)
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub): return -_ev(n.operand)
    raise ValueError("unsupported expression")
@cmd("util", "Safe calculator")
async def calc(ctx, *, expr: str):
    try: await ctx.send(embed=emb("🧮 Result", f"`{expr}` = **{_ev(ast.parse(expr, mode='eval').body)}**"))
    except Exception as e: await ctx.send(embed=err(str(e)))
@cmd("util", "Discord timestamp")
async def timestamp(ctx): t = int(time.time()); await ctx.send(embed=emb("🕒 Timestamp", f"<t:{t}:F>\n`<t:{t}:F>`"))
def mk_text(n, brief, fn):
    async def f(ctx, *, text: str):
        try: await ctx.send(embed=emb(f"✨ {n}", f"```{trim(str(fn(text)), 1800)}```"))
        except Exception as e: await ctx.send(embed=err(str(e)))
    f.__name__ = n; cmd("util", brief)(f)
for _n, _b, _f in [("b64e", "Base64 encode", lambda s: base64.b64encode(s.encode()).decode()), ("b64d", "Base64 decode", lambda s: base64.b64decode(s.encode()).decode()),
 ("reverse", "Reverse text", lambda s: s[::-1]), ("upper", "UPPERCASE", lambda s: s.upper()), ("lower", "lowercase", lambda s: s.lower()), ("count", "Count characters", lambda s: f"{len(s)} characters"),
 ("binary", "Text to binary", lambda s: " ".join(f"{ord(c):08b}" for c in s[:100])), ("mock", "mOcKiNg text", lambda s: "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(s))),
 ("wordcount", "Count words", lambda s: f"{len(s.split())} words")]: mk_text(_n, _b, _f)
@cmd("util", "Hash text (sha256)", name="hash")
async def hash_(ctx, *, text: str): await ctx.send(embed=emb("🔏 SHA-256", f"```{hashlib.sha256(text.encode()).hexdigest()}```"))
@cmd("util", "Generate a password")
async def genpass(ctx, n: int = 16):
    try: await ctx.author.send(embed=emb("🔑 Password", f"`{''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%^&*') for _ in range(max(8, min(n, 64))))}`")); await ctx.message.add_reaction("📬")
    except discord.Forbidden: await ctx.send(embed=err("Open your DMs first."))
@cmd("util", "Random UUID")
async def uuid(ctx): await ctx.send(embed=emb("🆔 UUID", f"`{uuidlib.uuid4()}`"))
@cmd("util", "Preview a hex color")
async def color(ctx, hexcode: str):
    h = hexcode.lstrip("#")
    try: v = int(h, 16); assert len(h) == 6
    except Exception: return await ctx.send(embed=err("Use 6-digit hex, e.g. `ff4500`"))
    await ctx.send(embed=emb(f"🎨 #{h}", f"RGB `{(v >> 16, (v >> 8) & 255, v & 255)}`", v))
@cmd("util", "Rock paper scissors")
async def rps(ctx, pick: str):
    pick = pick.lower(); b = random.choice(["rock", "paper", "scissors"])
    if pick not in ("rock", "paper", "scissors"): return await ctx.send(embed=err("rock / paper / scissors"))
    await ctx.send(embed=emb("✂️ RPS", f"You: **{pick}** • Me: **{b}**\n" + ("Draw!" if pick == b else "You win! 🎉" if (pick, b) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")] else "I win 😎")))
def mk_act2(n, verb):
    async def f(ctx, m: discord.Member = None): await ctx.send(embed=emb(f"{verb}", f"{ctx.author.mention} {n}s {(m or ctx.author).mention}!"))
    f.__name__ = n; cmd("util", f"{n.title()} someone")(f)
for _n, _v in [("slap", "👋 Slap!"), ("hug", "🤗 Hug!"), ("pat", "🐾 Pat!")]: mk_act2(_n, _v)
@cmd("util", "Reminder: !remind 10m text")
async def remind(ctx, when: str, *, text: str = "⏰"):
    m = re.fullmatch(r"(\d+)([smhd])", when)
    if not m: return await ctx.send(embed=err("Use e.g. 30s, 10m, 2h, 1d"))
    s = int(m.group(1)) * {"s": 1, "m": 60, "h": 3600, "d": 86400}[m.group(2)]
    if s > 604800: return await ctx.send(embed=err("Max 7 days."))
    await ctx.send(embed=emb("⏰ Reminder set", f"in {when}"))
    async def _r(): await asyncio.sleep(s); await ctx.send(f"{ctx.author.mention}", embed=emb("⏰ Reminder", text))
    asyncio.create_task(_r())
@cmd("util", "Member count")
async def membercount(ctx): await ctx.send(embed=emb("👥 Members", str(ctx.guild.member_count)))
@cmd("util", "List roles")
async def roles(ctx): await ctx.send(embed=emb("🎭 Roles", trim(" ".join(r.mention for r in ctx.guild.roles[1:]), 3000) or "none"))
@cmd("util", "Channel info")
async def channelinfo(ctx, ch: discord.TextChannel = None): ch = ch or ctx.channel; await ctx.send(embed=emb(f"#{ch.name}", f"ID `{ch.id}`\nCreated <t:{int(ch.created_at.timestamp())}:R>\nSlowmode {ch.slowmode_delay}s"))
@cmd("util", "Role info")
async def roleinfo(ctx, role: discord.Role): await ctx.send(embed=emb(f"🎭 {role.name}", f"ID `{role.id}` • Members **{len(role.members)}** • Color `{role.color}`", role.color.value or FIRE))
@cmd("util", "Snowflake → date")
async def snowflake(ctx, sid: int): await ctx.send(embed=emb("❄️ Snowflake", f"<t:{int(discord.utils.snowflake_time(sid).timestamp())}:F>"))
@cmd("util", "Big ASCII text")
async def bigtext(ctx, *, text: str): await ctx.send(f"```\n{trim(art(text[:14], 'big'), 1900)}\n```")
@cmd("util", "Rate anything")
async def rate(ctx, *, thing: str): await ctx.send(embed=emb("⭐ Rating", f"**{thing}** → `{random.Random(thing.lower()).randint(0, 10)}/10`"))
@cmd("util", "Ship two names")
async def ship(ctx, a: str, b: str): p = int(hashlib.md5("".join(sorted([a.lower(), b.lower()])).encode()).hexdigest(), 16) % 101; await ctx.send(embed=emb("💘 Ship", f"{a} × {b}\n`{bar(p)}`"))
@cmd("util", "Current UTC time")
async def utc(ctx): await ctx.send(embed=emb("🌐 UTC", dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")))
@cmd("util", "Random tech fact")
async def fact(ctx): await ctx.send(embed=emb("🧠 Fact", random.choice(["LXC shares the host kernel, so containers boot in seconds.", "The first computer bug was a real moth, found in 1947.", "Linux powers the vast majority of the world's servers.", "SSH replaced telnet in 1995 to encrypt remote logins.", "The first domain ever registered was symbolics.com."])))
@cmd("util", "Inspirational quote")
async def quote(ctx): await ctx.send(embed=emb("💬 Quote", random.choice(["Talk is cheap. Show me the code. — Linus Torvalds", "Premature optimization is the root of all evil. — Donald Knuth", "Simplicity is prerequisite for reliability. — Edsger Dijkstra", "Make it work, make it right, make it fast. — Kent Beck"])))

# ═════════════════════ CATEGORY 4 — v2 PRO (21) ═════════════════════
HTTP = {}; LAST = {}; FAIL = {}; SEM = None
LOGCMD = "(journalctl -n 40 --no-pager 2>/dev/null || dmesg 2>/dev/null | tail -40 || tail -40 /var/log/messages 2>/dev/null)"
BK = "backups"
def hb(n):
    n = float(n)
    for u in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or u == "TB": return f"{n:.1f}{u}"
        n /= 1024
async def _state(c):
    rc, o = await lx("query", f"/1.0/instances/{c}/state", timeout=20)
    try: return json.loads(o)
    except Exception: return None
async def usage(c, r, wait=2):
    a = await _state(c)
    if not a: return None
    cpu0 = (a.get("cpu") or {}).get("usage", 0); t0 = time.time(); b = a
    if wait: await asyncio.sleep(wait); b = await _state(c) or a
    span = max(time.time() - t0, 0.001)
    cpu_p = ((b.get("cpu") or {}).get("usage", 0) - cpu0) / 1e9 / span / max(r["cpu"], 1) * 100 if wait else 0
    mem = (b.get("memory") or {}).get("usage", 0); disk = ((b.get("disk") or {}).get("root") or {}).get("usage", 0); rx = tx = 0
    for k, v in (b.get("network") or {}).items():
        if k != "lo": cn = v.get("counters", {}); rx += cn.get("bytes_received", 0); tx += cn.get("bytes_sent", 0)
    return dict(cpup=max(0, min(100, cpu_p)), mem=mem, memp=mem / (r["ram"] * 1048576) * 100, disk=disk, diskp=disk / (max(r["disk"], 1) * 1073741824) * 100, rx=rx, tx=tx, procs=b.get("processes", 0))
def usage_embed(r, u, title=None):
    e = emb(title or f"📊 Usage • {r['name']}")
    e.add_field(name="🧠 CPU", value=f"`{bar(u['cpup'])}`", inline=False); e.add_field(name="💾 RAM", value=f"`{bar(u['memp'])}` {hb(u['mem'])}/{r['ram']}MB", inline=False)
    e.add_field(name="💽 Disk", value=f"`{bar(u['diskp'])}` {hb(u['disk'])}/{r['disk']}GB", inline=False)
    e.add_field(name="🌐 Network", value=f"⬇️ {hb(u['rx'])}  ⬆️ {hb(u['tx'])}"); e.add_field(name="⚙️ Processes", value=str(u["procs"])); return e
async def stop_http(c):
    t = HTTP.pop(c, None)
    if t:
        try: t["proc"].kill()
        except Exception: pass
    q("UPDATE vps SET http='' WHERE name=?", (c,))
async def start_http(c, port):
    await stop_http(c)
    if await lxstate(c) != "RUNNING": return None, "The VPS is not running."
    ip = await lxip(c)
    if not ip: return None, "The VPS has no IPv4 yet."
    p, url, e = await pinggy_open(ip, port, "http")
    if e: return None, e
    async def drain():
        try:
            while await p.stdout.read(4096): pass
        finally:
            if HTTP.get(c, {}).get("proc") is p: HTTP.pop(c, None); q("UPDATE vps SET http='' WHERE name=?", (c,))
    HTTP[c] = {"proc": p, "url": url, "task": asyncio.create_task(drain())}; q("UPDATE vps SET http=? WHERE name=?", (url, c)); return url, None
async def do_renew(r):
    if not DEFAULT_DAYS: return False, "Expiry is disabled on this host — your VPS never expires."
    now = int(time.time()); new = min(max(now, r["expires"]) + RENEW_DAYS * 86400, now + 90 * 86400)
    if new <= r["expires"]: return False, "Already at the 90-day maximum."
    was = r["suspended"] == 2; q("UPDATE vps SET expires=?, notified=0, suspended=CASE WHEN suspended=2 THEN 0 ELSE suspended END WHERE name=?", (new, r["name"]))
    if was: await lx("start", r["name"])
    return True, f"`{r['name']}` renewed — new expiry <t:{new}:F> (<t:{new}:R>)"
def bk_files(c):
    os.makedirs(BK, exist_ok=True); return sorted(f for f in os.listdir(BK) if re.fullmatch(re.escape(c) + r"-\d{8}-\d{6}\.tar\.gz", f))
async def do_backup(r):
    if len(bk_files(r["name"])) >= MAX_BACKUPS: return False, f"Backup limit reached ({MAX_BACKUPS}). Delete one with `{PREFIX}delbackup`."
    f = f"{BK}/{r['name']}-{time.strftime('%Y%m%d-%H%M%S')}.tar.gz"; rc, o = await lx("export", r["name"], f, timeout=1800)
    return (True, f"Saved `{os.path.basename(f)}` ({hb(os.path.getsize(f))})") if rc == 0 else (False, trim(o, 500))
async def notify(uid, e):
    try: u = await bot.fetch_user(uid); await u.send(embed=e)
    except Exception: pass
async def watchdog():
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            now = int(time.time())
            for c, t in list(TUN.items()):  # renew expiring free tunnels
                r = find(c)
                if r and r["autossh"] and time.time() - t["started"] > TUN_RENEW_MIN * 60 and await lxstate(c) == "RUNNING":
                    addr, e = await start_tunnel(c)
                    if addr: await notify(r["owner"], emb("🔁 Auto-SSH renewed", f"`{c}`\n```{ssh_line(addr)}```", 0x2ECC71))
            for r in q("SELECT * FROM vps WHERE autossh=1 AND suspended=0"):  # (re)open missing tunnels, e.g. after a bot restart
                c = r["name"]
                if c not in TUN and now - FAIL.get(c, 0) > 300 and await lxstate(c) == "RUNNING":
                    addr, e = await start_tunnel(c)
                    if addr: await notify(r["owner"], emb("🔁 Auto-SSH online", f"`{c}`\n```{ssh_line(addr)}```", 0x2ECC71))
                    else: FAIL[c] = now
            for r in q("SELECT * FROM vps WHERE expires>0"):  # expiry lifecycle
                left = r["expires"] - now; c = r["name"]
                if left <= -GRACE_DAYS * 86400: await do_act("delete", r); await notify(r["owner"], emb("🗑️ VPS deleted", f"`{c}` expired and the grace period ended.", RED))
                elif left <= 0 and r["suspended"] == 0:
                    q("UPDATE vps SET suspended=2 WHERE name=?", (c,)); await do_act("stop", r)
                    await notify(r["owner"], emb("⌛ VPS expired", f"`{c}` was stopped. Run `{PREFIX}renew {c}` within **{GRACE_DAYS} days** or it will be deleted.", RED))
                elif 0 < left < 86400 and not r["notified"]:
                    q("UPDATE vps SET notified=1 WHERE name=?", (c,)); await notify(r["owner"], emb("⏳ VPS expires soon", f"`{c}` expires <t:{r['expires']}:R>. Use `{PREFIX}renew {c}`."))
        except Exception as ex: print("watchdog:", repr(ex))
        await asyncio.sleep(60)

@cmd("pro", "Auto-renew Pinggy SSH: !autossh [name] on|off")
async def autossh(ctx, name: str = None, mode: str = None):
    if name and name.lower() in ("on", "off") and mode is None: name, mode = None, name
    r = await mine(ctx, name)
    if not r: return
    v = 0 if (mode or ("off" if r["autossh"] else "on")).lower() == "off" else 1; q("UPDATE vps SET autossh=? WHERE name=?", (v, r["name"]))
    await ctx.send(embed=emb("🔁 Auto-SSH", f"`{r['name']}` → **{'ON' if v else 'OFF'}**\nPinggy links are renewed automatically and DM'd to you.", 0x2ECC71))
@cmd("pro", "Extend your VPS expiry")
async def renew(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if r: ok, m = await do_renew(r); await ctx.send(embed=emb("⏳ Renew", m, 0x2ECC71 if ok else RED))
@cmd("pro", "Show expiry of your VPS")
async def expires(ctx):
    rows = q("SELECT * FROM vps WHERE owner=?", (ctx.author.id,)); await ctx.send(embed=emb("⌛ Expiry", "\n".join(f"`{r['name']}` — " + (f"<t:{r['expires']}:R>" if r["expires"] else "never") for r in rows) or "No VPS."))
@cmd("pro", "Set expiry in days (0 = never)", 1)
async def setexpiry(ctx, name: str, days: int):
    r = find(name)
    if not r: return await ctx.send(embed=err("VPS not found."))
    q("UPDATE vps SET expires=?, notified=0, suspended=CASE WHEN suspended=2 THEN 0 ELSE suspended END WHERE name=?", (int(time.time() + days * 86400) if days > 0 else 0, r["name"]))
    await ctx.send(embed=emb("✅ Expiry set", f"`{r['name']}` → {days} days" if days > 0 else f"`{r['name']}` never expires", 0x2ECC71))
@cmd("pro", "Expose a web port: !http name port")
async def http(ctx, name: str, port: int):
    r = await mine(ctx, name)
    if not r: return
    m = await ctx.send(embed=emb("🌐 Opening Pinggy web tunnel…")); url, e = await start_http(r["name"], port)
    await m.edit(embed=err(e) if e else emb("🌐 Web link ready", f"{url}\n→ port `{port}` of `{r['name']}`", 0x2ECC71))
@cmd("pro", "Close the web tunnel")
async def httpstop(ctx, name: str = None):
    r = await mine(ctx, name)
    if r: await stop_http(r["name"]); await ctx.send(embed=emb("🛑 Web tunnel closed", r["name"]))
@cmd("pro", "CPU / RAM / disk / network usage")
async def usage_(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if not r: return
    u = await usage(r["name"], r, 2); await ctx.send(embed=usage_embed(r, u) if u else err("VPS must be running."))
@cmd("pro", "Live auto-updating monitor (~1 min)")
async def monitor(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if not r: return
    m = await ctx.send(embed=emb("📡 Starting monitor…"))
    for _ in range(15):
        u = await usage(r["name"], r, 3) if await lxstate(r["name"]) == "RUNNING" else None
        if not u: return await m.edit(embed=err("VPS is not running."))
        await m.edit(embed=usage_embed(r, u, f"📡 Live Monitor • {r['name']}"))
    await m.edit(embed=emb("📡 Monitor ended", f"Run `{PREFIX}monitor` again for another minute."))
@cmd("pro", "Create a backup (export)")
async def backup(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    m = await ctx.send(embed=emb("💾 Backing up…", "This can take a few minutes.")); ok, t = await do_backup(r); await m.edit(embed=emb("💾 Backup", t, 0x2ECC71 if ok else RED))
@cmd("pro", "List backups")
async def backups(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if r: await ctx.send(embed=emb(f"💾 Backups • {r['name']}", "\n".join(f"`{f}` {hb(os.path.getsize(f'{BK}/{f}'))}" for f in bk_files(r["name"])) or "none"))
@cmd("pro", "Delete a backup: !delbackup name file")
async def delbackup(ctx, name: str, file: str):
    r = await mine(ctx, name)
    if not r: return
    if file not in bk_files(r["name"]): return await ctx.send(embed=err("Backup not found — see `%sbackups`." % PREFIX))
    os.remove(f"{BK}/{file}"); await ctx.send(embed=emb("🗑️ Backup deleted", file, 0x2ECC71))
@cmd("pro", "Restore a backup: !restorebackup name file")
async def restorebackup(ctx, name: str, file: str):
    r = await mine(ctx, name)
    if not r: return
    if file not in bk_files(r["name"]): return await ctx.send(embed=err("Backup not found — see `%sbackups`." % PREFIX))
    async def fn():
        c = r["name"]; await stop_tunnel(c); await stop_http(c); await lx("delete", "-f", c, timeout=180)
        rc, o = await lx("import", f"{BK}/{file}", c, timeout=1800)
        if rc: return False, o
        await lx("start", c); return True, "Backup restored and VPS started."
    await ctx.send(embed=emb("⚠️ Restore backup?", f"`{r['name']}` will be replaced by `{file}`.", RED), view=ConfirmView(ctx.author.id, fn, "Restore"))
@cmd("pro", "Pull latest code from git & restart", 2)
async def update(ctx):
    m = await ctx.send(embed=emb("⬇️ Updating…")); rc, o = await sh("git", "pull", "--ff-only", timeout=120)
    if rc: return await m.edit(embed=err(f"git pull failed (is this a git clone?):\n```{trim(o, 600)}```"))
    await sh(sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q", timeout=300)
    await m.edit(embed=emb("✅ Updated — restarting…", f"```{trim(o, 500)}```", 0x2ECC71)); os.execv(sys.executable, [sys.executable] + sys.argv)
@cmd("pro", "Bot version")
async def version(ctx): rc, o = await lx("version"); await ctx.send(embed=emb(f"⚡ ArizNodes VPS Bot v{VERSION}", f"Python `{sys.version.split()[0]}` • discord.py `{discord.__version__}`\n```{o}```"))
@cmd("pro", "What's new in v4")
async def changelog(ctx):
    await ctx.send(embed=emb("📜 v4 Changelog", "🌐 **Website for everyone** — Discord login, members manage their own VPS, admins control everything\n🛠️ **Internet auto-repair** — detects containers with no internet (Docker/ufw/NAT) and fixes the firewall\n🔐 **SSH setup rewritten** — verifies sshd really runs, shows the real error, retries package installs\n🔌 Pinggy uses a dedicated key + clearer failures • 🌍 sshx hints when the VPS is offline\n🩺 `diag` checks container internet • `!netfix` repair command\n⌨️ Console • 🎨 Themes • 🔁 Auto-SSH • 💾 Backups"))
@cmd("pro", "Host health check", 1)
async def health(ctx):
    rc, v = await lx("version"); rc2, o = await sh("curl", "-sS", "-m", "8", "-o", "/dev/null", "-w", "%{http_code}", "https://pinggy.io", timeout=15); du = psutil.disk_usage("/")
    await ctx.send(embed=emb("🩺 Health", f"{'✅' if rc == 0 else '❌'} LXC: `{v.replace(chr(10), ' | ')[:90]}`\n{'✅' if shutil.which('ssh') else '❌'} ssh client\n{'✅' if rc2 == 0 else '❌'} Pinggy reachable ({o[:40]})\n{'✅' if du.percent < 90 else '⚠️'} Disk {du.percent:.0f}% used\n{'✅' if gset('maint') != '1' else '🛠️'} Maintenance {'off' if gset('maint') != '1' else 'ON'}"))
@cmd("pro", "All active tunnels on the host", 1)
async def tunnels(ctx):
    L = [f"🔌 `{c}` {t['addr']}" for c, t in TUN.items()] + [f"🌐 `{c}` {t['url']}" for c, t in HTTP.items()]
    await ctx.send(embed=emb(f"🔌 Active tunnels ({len(L)})", "\n".join(L) or "none"))
@cmd("pro", "Show your SSH / sshx / HTTP links")
async def sshinfo(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if not r: return
    note = await dm_or_here(ctx, emb(f"🔗 Links • {r['name']}", f"**SSH:** `{ssh_line(r['ssh']) if r['ssh'] else 'not active'}`\n**sshx:** {r['sshx'] or 'not active'}\n**HTTP:** {r['http'] or 'not active'}"))
    await ctx.send(embed=emb("🔗 Links", note))
@cmd("pro", "Kernel / service logs of your VPS")
async def vlogs(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    rc, o = await inside(r["name"], LOGCMD, 30); await ctx.send(embed=emb(f"🧾 Logs • {r['name']}", f"```\n{trim(o, 1800) or 'empty'}\n```"))
@cmd("pro", "Clone a VPS (counts toward your limit)")
async def clone(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    n = q("SELECT COUNT(*) c FROM vps WHERE owner=?", (ctx.author.id,), True)["c"]
    if n >= ulimit(ctx.author.id) and not is_admin(ctx.author.id): return await ctx.send(embed=err(f"VPS limit reached ({n}/{ulimit(ctx.author.id)})."))
    new = "ariz-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=6)); m = await ctx.send(embed=emb("🧬 Cloning…", "This can take a minute."))
    rc, o = await lx("copy", r["name"], new, timeout=900)
    if rc: return await m.edit(embed=err(trim(o, 500)))
    await lx("start", new); q("INSERT INTO vps(name,owner,os,ram,cpu,disk,created,expires) VALUES(?,?,?,?,?,?,?,?)", (new, ctx.author.id, r["os"], r["ram"], r["cpu"], r["disk"], int(time.time()), int(time.time() + DEFAULT_DAYS * 86400) if DEFAULT_DAYS else 0))
    await m.edit(embed=emb("🧬 Cloned", f"`{r['name']}` → `{new}`\nSame root password as the original — run `{PREFIX}resetpass {new}` and `{PREFIX}ssh {new}`.", 0x2ECC71))
@cmd("pro", "Add a note to a VPS: !note name text")
async def note(ctx, name: str, *, text: str):
    r = await mine(ctx, name, False)
    if r: q("UPDATE vps SET note=? WHERE name=?", (text[:100], r["name"])); await ctx.send(embed=emb("📝 Note saved", text[:100], 0x2ECC71))

@bot.tree.command(name="panel", description="Post the VPS control panel (admin)")
async def s_panel(i: discord.Interaction):
    if not is_admin(i.user.id): return await i.response.send_message(embed=err("Admins only."), ephemeral=True)
    await i.response.send_message(embed=panel_embed(), view=PanelView())
@bot.tree.command(name="deploy", description="Deploy a new VPS")
async def s_deploy(i: discord.Interaction):
    if urow(i.user.id)["banned"]: return await i.response.send_message(embed=err("You are banned."), ephemeral=True)
    await i.response.send_message(embed=deploy_intro(), view=DeployView(i.user.id), ephemeral=True)
@bot.tree.command(name="manage", description="Manage your VPS")
async def s_manage(i: discord.Interaction):
    if urow(i.user.id)["banned"]: return await i.response.send_message(embed=err("You are banned."), ephemeral=True)
    await i.response.send_message(embed=manage_embed(i.user.id), view=ManageView(i.user.id), ephemeral=True)
@bot.tree.command(name="dashboard", description="Open the admin dashboard")
async def s_dash(i: discord.Interaction):
    if not is_admin(i.user.id): return await i.response.send_message(embed=err("Admins only."), ephemeral=True)
    await i.response.send_message(embed=await dash_embed(), view=DashView(i.user.id), ephemeral=True)


# ═════════════════════ v3: THEMES • CONSOLE • WEB DASHBOARD • DIAGNOSTICS ═════════════════════
def web_info_embed():
    local = DASH_HOST in ("127.0.0.1", "localhost"); h = "127.0.0.1" if local else DASH_HOST; pub = DASH_URL or f"http://{h}:{DASH_PORT}"
    e = emb("🌐 Website", f"**Address:** `{pub}`\n**Discord login:** {'✅ on' if DISCORD_SECRET else '❌ off — set `DISCORD_CLIENT_SECRET` in `.env`'}\n**Admin password login:** {'✅ on' if DASH_PASS else '❌ off'}")
    e.add_field(name="🔑 Discord login redirect URL", value=f"Add this in the Developer Portal → OAuth2 → Redirects:\n`{(DASH_URL or 'https://YOUR-DOMAIN')}/auth/callback`", inline=False)
    if local: e.add_field(name="🔐 Open it from your PC", value=f"```ssh -L {DASH_PORT}:127.0.0.1:{DASH_PORT} root@YOUR_SERVER_IP```then browse to `http://127.0.0.1:{DASH_PORT}`", inline=False)
    e.add_field(name="🌍 Temporary public link", value=f"The owner can run `{PREFIX}webdash public` for a Pinggy link.", inline=False); return e

# ───────── interactive console ─────────
CONS = {}; CTHREADS = {}
QUICK_CMDS = [("📊 System overview", "uname -a; echo; uptime; echo; free -h; echo; df -h /", 60), ("🧠 Top processes", "top -bn1 | head -20", 60),
 ("🌐 Network & ports", "ip -br a; echo; (ss -tulpn 2>/dev/null || netstat -tulpn 2>/dev/null)", 60), ("💽 Disk usage", "df -h; echo; du -sh /root /var /home 2>/dev/null", 90),
 ("📦 Update packages", "if command -v apt-get >/dev/null; then apt-get update -y && apt-get upgrade -y; elif command -v dnf >/dev/null; then dnf upgrade -y; elif command -v apk >/dev/null; then apk update && apk upgrade; elif command -v pacman >/dev/null; then pacman -Syu --noconfirm; fi", 900),
 ("🔧 Install tools (curl wget git nano htop)", pm("curl wget git nano htop"), 600), ("🐍 Install Python 3 + pip", pm("python3 python3-pip") + "; python3 --version", 600),
 ("🟢 Install Node.js", pm("nodejs npm") + "; node -v", 600), ("🐳 Install Docker", "curl -fsSL https://get.docker.com | sh; docker --version", 900),
 ("👥 Logged-in users", "w; echo; last -n 5 2>/dev/null", 30), ("🔥 Listening on port 22?", "ss -tlnp 2>/dev/null | grep ':22 ' || echo 'ss not available — sshd check: ' && " + SSHD_CHECK + " && echo yes || echo no", 30),
 ("🧹 Clean package caches", "apt-get clean 2>/dev/null; dnf clean all 2>/dev/null; apk cache clean 2>/dev/null; echo done", 60)]
def cons(c): return CONS.setdefault(c, {"cwd": "/root", "hist": [], "bash": None})
def safe(t): return (t or "").replace("```", "'''")
async def console_run(c, cmdline, timeout=120):
    s = cons(c)
    if s["bash"] is None: rc, _ = await lx("exec", c, "--", "sh", "-c", "command -v bash"); s["bash"] = (rc == 0)
    script = 'cd "$ARIZ_CWD" 2>/dev/null || cd /root 2>/dev/null || cd /\n' + cmdline + '\n__r=$?\n' + r'printf "\n@@ARIZ@@%s@@%s" "$__r" "$(pwd)"'
    rc, o = await lx("exec", c, "--env", f"ARIZ_CWD={s['cwd']}", "--env", "HOME=/root", "--env", "TERM=dumb", "--env", "DEBIAN_FRONTEND=noninteractive", "--",
                     "bash" if s["bash"] else "sh", "-c", script, timeout=timeout)
    m = re.search(r"\n?@@ARIZ@@(\d+)@@(.*)\Z", o, re.S)
    if m: out, rc, s["cwd"] = o[:m.start()], int(m.group(1)), (m.group(2).strip() or s["cwd"])
    else: out = f"⏱️ Timed out after {timeout}s — the command was stopped." if rc == 124 else o
    return rc, out.strip("\n"), s["cwd"]
def console_embed(r, note=None):
    s = cons(r["name"]); body = ""
    for h in s["hist"][-3:]:
        body += f"**`root@{r['name']}:{h['cwd']}# {trim(h['cmd'], 70)}`** · exit `{h['rc']}`\n```\n{trim(safe(h['out']), 650) or '(no output)'}\n```\n"
    e = emb(f"⌨️ Console • {r['name']}", (body or "*No commands yet.* Press **Run Command**, pick a **quick command**, or open a **Live Thread** for a real terminal feel.") + (f"\n{note}" if note else ""), 0x5865F2)
    e.add_field(name="📂 Directory", value=f"`{s['cwd']}`"); e.add_field(name="🧾 History", value=str(len(s["hist"]))); return e
class CmdModal(discord.ui.Modal, title="Run a command"):
    command = discord.ui.TextInput(label="Command (runs as root)", style=discord.TextStyle.paragraph, max_length=1500, placeholder="apt update && apt install -y htop")
    def __init__(s, view): super().__init__(); s.view = view
    async def on_submit(s, i): await s.view.run(i, str(s.command.value))
class ConsoleView(OV):
    def __init__(s, uid, c):
        super().__init__(uid, 1800); s.c = c
        sel = discord.ui.Select(placeholder="⚡ Quick commands", row=1, options=[discord.SelectOption(label=l[:100], value=str(n)) for n, (l, _, _) in enumerate(QUICK_CMDS)])
        async def cb(i): _, cmdline, to = QUICK_CMDS[int(sel.values[0])]; await s.run(i, cmdline, to)
        sel.callback = cb; s.add_item(sel)
    async def run(s, i, cmdline, timeout=120):
        r = find(s.c); g = guard(r, i.user.id) if r else "VPS no longer exists."
        if g: return await i.response.send_message(embed=err(g), ephemeral=True)
        if await lxstate(s.c) != "RUNNING": return await i.response.send_message(embed=err("The VPS is not running."), ephemeral=True)
        await i.response.defer(); rc, out, cwd = await console_run(s.c, cmdline, timeout); st = cons(s.c)
        st["hist"].append({"cmd": cmdline, "out": clean(out), "rc": rc, "cwd": cwd}); st["hist"] = st["hist"][-20:]
        await i.edit_original_response(embed=console_embed(r), view=s)
        if len(out) > 650: await i.followup.send(content="📎 Full output:", file=discord.File(io.BytesIO(clean(out).encode()), "output.txt"), ephemeral=True)
    @discord.ui.button(label="Run Command", emoji="▶️", style=discord.ButtonStyle.success, row=0)
    async def b_run(s, i, b): await i.response.send_modal(CmdModal(s))
    @discord.ui.button(label="Live Thread", emoji="🧵", style=discord.ButtonStyle.primary, row=0)
    async def b_thread(s, i, b):
        r = find(s.c)
        if not r or guard(r, i.user.id): return await i.response.send_message(embed=err("Not allowed."), ephemeral=True)
        th, e = await open_thread(i, r)
        await i.response.send_message(embed=err(e) if e else emb("🧵 Live console ready", f"Open {th.mention} and just type commands like in a terminal.", 0x2ECC71), ephemeral=True)
    @discord.ui.button(label="Clear", emoji="🧹", style=discord.ButtonStyle.secondary, row=0)
    async def b_clear(s, i, b): cons(s.c)["hist"].clear(); await i.response.edit_message(embed=console_embed(find(s.c)), view=s)
    @discord.ui.button(label="Back", emoji="⬅️", style=discord.ButtonStyle.secondary, row=0)
    async def b_back(s, i, b):
        r = find(s.c); await i.response.edit_message(embed=await vps_embed(r) if r else manage_embed(s.uid), view=VPSPanel(s.uid, s.c) if r else ManageView(s.uid))
def save_threads(): sset("cthreads", json.dumps({str(k): list(v) for k, v in CTHREADS.items()}))
async def open_thread(i, r):
    if not isinstance(i.channel, discord.TextChannel): return None, "Live threads can only be opened from a normal server text channel."
    try:
        th = await i.channel.create_thread(name=f"console-{r['name']}", type=discord.ChannelType.private_thread, invitable=False, auto_archive_duration=1440)
        await th.add_user(i.user)
    except discord.Forbidden: return None, "I need the **Create Private Threads** and **Send Messages in Threads** permissions in this channel."
    except Exception as ex: return None, f"Could not create the thread: {ex}"
    CTHREADS[th.id] = (r["name"], i.user.id); save_threads()
    await th.send(embed=emb(f"🧵 Live console • {r['name']}", "Type any command as a normal message — it runs as **root** inside the VPS.\n`cd` is remembered. Type `exit` to close.\n*Interactive programs (vim, top without -bn1) are not supported.*", 0x5865F2))
    return th, None
async def thread_exec(m, c):
    txt = m.content.strip()
    if not txt: return
    if txt.lower() in ("exit", "logout", "quit"):
        CTHREADS.pop(m.channel.id, None); save_threads(); await m.channel.send("👋 Console closed.")
        try: await m.channel.edit(archived=True, locked=True)
        except Exception: pass
        return
    r = find(c); g = guard(r, m.author.id) if r else "This VPS no longer exists."
    if g: return await m.channel.send(f"❌ {g}")
    if await lxstate(c) != "RUNNING": return await m.channel.send("❌ The VPS is not running.")
    async with m.channel.typing(): rc, out, cwd = await console_run(c, txt, 180)
    head = f"`root@{c}:{cwd}#` exit `{rc}`"; out = clean(out); mentions = discord.AllowedMentions.none()
    if len(out) <= 1800: await m.channel.send(f"{head}\n```\n{safe(out) or '(no output)'}\n```", allowed_mentions=mentions)
    else: await m.channel.send(head, file=discord.File(io.BytesIO(out.encode()), "output.txt"), allowed_mentions=mentions)
@bot.event
async def on_message(m):
    if m.author.bot: return
    t = CTHREADS.get(m.channel.id)
    if t:
        if (m.author.id == t[1] or is_admin(m.author.id)) and not urow(m.author.id)["banned"]: await thread_exec(m, t[0])
        return
    await bot.process_commands(m)

@cmd("vps", "Open the interactive console: !console [name]")
async def console(ctx, name: str = None):
    r = await mine(ctx, name)
    if not r: return
    if await lxstate(r["name"]) != "RUNNING": return await ctx.send(embed=err("Start the VPS first — the console needs it running."))
    await ctx.send(embed=console_embed(r), view=ConsoleView(ctx.author.id, r["name"]))
@cmd("vps", "Diagnose Pinggy / SSH / sshx problems")
async def diag(ctx, name: str = None):
    r = await mine(ctx, name, False)
    if not r: return
    c = r["name"]; m = await ctx.send(embed=emb("🩺 Running diagnostics…")); st = await lxstate(c); host = pg_host(); L = [f"{'✅' if st == 'RUNNING' else '❌'} VPS state: **{st}**"]
    L.append(f"{'✅' if shutil.which('ssh') else '❌'} `ssh` client installed on the host"); L.append(f"{'✅' if await pg_reachable(host) else '❌'} Host can reach `{host}:443`")
    if st == "RUNNING":
        rc, _ = await inside(c, SSHD_CHECK, 20); L.append(f"{'✅' if rc == 0 else '❌'} sshd is listening on port 22 inside the VPS")
        tcp, dns = await inet_state(c); L.append(f"{'✅' if tcp else '❌'} The VPS has internet access (TCP)"); L.append(f"{'✅' if dns else '❌'} The VPS can resolve DNS names")
        if not tcp: L.append(f"⚠️ **No internet inside the VPS** — SSH install and sshx cannot work. Owner: run `{PREFIX}netfix`.")
    L.append(f"{'✅' if c in TUN else '➖'} Pinggy tunnel: " + (f"`{TUN[c]['addr']}`" if c in TUN else "not active")); L.append(f"{'✅' if r['sshx'] else '➖'} sshx: " + ("active" if r["sshx"] else "not active"))
    await m.edit(embed=emb(f"🩺 Diagnostics • {c}", "\n".join(L) + f"\n\n🔌 `{PREFIX}ssh {c}` · 🌍 `{PREFIX}sshx {c}` · ⌨️ `{PREFIX}console {c}`"))

# ───────── themes ─────────
class ThemeView(OV):
    def __init__(s, uid):
        super().__init__(uid, 300); sel = discord.ui.Select(placeholder="🎨 Pick a theme", options=[discord.SelectOption(label=v[2], value=k, emoji=v[1], default=(k == gset("theme", "fire"))) for k, v in THEMES.items()])
        async def cb(i): sset("theme", sel.values[0]); await i.response.edit_message(embed=emb(f"{theme()[1]} Theme: {theme()[2]}", "Applied everywhere — Discord embeds and the web dashboard."), view=ThemeView(s.uid))
        sel.callback = cb; s.add_item(sel)
@cmd("admin", "Change the bot theme: !theme [name]", 1)
async def theme_(ctx, name: str = None):
    if name and name.lower() in THEMES: sset("theme", name.lower()); return await ctx.send(embed=emb(f"{theme()[1]} Theme: {theme()[2]}", "Applied everywhere — Discord embeds and the web dashboard."))
    await ctx.send(embed=emb("🎨 Themes", " ".join(f"{v[1]} `{k}`" for k, v in THEMES.items()) + f"\nCurrent: **{theme()[2]}**"), view=ThemeView(ctx.author.id))

# ───────── web dashboard v4 (Discord login • members + admins) ─────────
DASH_HTML = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ArizNodes Cloud</title>
<style>
:root{--bg:#090b10;--p1:#10131a;--p2:#171b25;--ln:#242a3a;--tx:#e8ebf4;--mt:#8a92a8;--ac:#ff4500;--ok:#2ecc71;--bad:#e74c3c;--wn:#f1c40f;--bl:#3498db}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:radial-gradient(1100px 520px at 85% -10%,color-mix(in srgb,var(--ac) 20%,transparent),transparent),radial-gradient(800px 400px at -10% 110%,color-mix(in srgb,var(--ac) 10%,transparent),transparent),var(--bg);color:var(--tx);font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
button,input,select,textarea{font:inherit;color:inherit}
.app{display:flex;min-height:100%}
.side{width:224px;background:var(--p1);border-right:1px solid var(--ln);padding:18px 12px;position:sticky;top:0;height:100vh;display:flex;flex-direction:column;gap:4px}
.brand{font-weight:800;font-size:17px;padding:4px 10px 16px;letter-spacing:.3px}.brand b{color:var(--ac)}
#nav{display:flex;flex-direction:column;gap:4px;flex:1}
.nav{padding:10px 12px;border-radius:10px;cursor:pointer;color:var(--mt);border:0;background:none;text-align:left;width:100%}
.nav:hover{background:var(--p2);color:var(--tx)}
.nav.on{background:color-mix(in srgb,var(--ac) 16%,transparent);color:var(--tx);box-shadow:inset 3px 0 var(--ac)}
.who{display:flex;gap:10px;align-items:center;padding:10px;border-top:1px solid var(--ln);margin-top:auto}.who img{width:34px;height:34px;border-radius:50%}
.main{flex:1;padding:26px;max-width:1280px;margin:0 auto;width:100%}
h1{margin:0 0 4px;font-size:22px}.sub{color:var(--mt);margin-bottom:16px}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(215px,1fr))}
.card{background:var(--p1);border:1px solid var(--ln);border-radius:14px;padding:16px}
.vc{cursor:pointer;transition:.15s}.vc:hover{border-color:var(--ac);transform:translateY(-2px)}
.card h3{margin:0 0 8px;font-size:12px;color:var(--mt);text-transform:uppercase;letter-spacing:.8px;font-weight:600}
.big{font-size:28px;font-weight:800}
.bar{height:8px;background:var(--p2);border-radius:99px;overflow:hidden;margin:6px 0 10px}
.bar i{display:block;height:100%;background:linear-gradient(90deg,var(--ac),color-mix(in srgb,var(--ac) 45%,#fff));border-radius:99px;transition:width .4s}
table{width:100%;border-collapse:collapse}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--ln);vertical-align:middle}
th{color:var(--mt);font-size:12px;text-transform:uppercase;letter-spacing:.6px;font-weight:600}
tr:hover td{background:rgba(255,255,255,.025)}
.badge{padding:2px 9px;border-radius:99px;font-size:12px;font-weight:600;display:inline-block}
.RUNNING{background:#2ecc7126;color:var(--ok)}.STOPPED{background:#e74c3c26;color:var(--bad)}.FROZEN{background:#3498db26;color:var(--bl)}.MISSING{background:#8a92a826;color:var(--mt)}
.btn{background:var(--p2);border:1px solid var(--ln);padding:8px 13px;border-radius:9px;cursor:pointer}
.btn:hover{border-color:var(--ac)}.btn:disabled{opacity:.5;cursor:wait}
.btn.pri{background:var(--ac);border-color:var(--ac);color:#fff;font-weight:600}
.btn.dc{background:#5865F2;border-color:#5865F2;color:#fff;font-weight:700;padding:12px 18px;font-size:15px}
.btn.bad{color:var(--bad)}.btn.ok{color:var(--ok)}.btn.sm{padding:4px 10px;font-size:12px}
input,select,textarea{background:var(--p2);border:1px solid var(--ln);border-radius:9px;padding:9px 11px;width:100%;outline:none}
input:focus,select:focus,textarea:focus{border-color:var(--ac)}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.grow{flex:1 1 200px}
.drawer{position:fixed;top:0;right:0;width:min(660px,100%);height:100%;background:var(--p1);border-left:1px solid var(--ln);transform:translateX(105%);transition:.25s;overflow:auto;padding:22px;z-index:20}
.drawer.on{transform:none}
.scrim{position:fixed;inset:0;background:#000a;display:none;z-index:15}.scrim.on{display:block}
.term{background:#05070a;border:1px solid var(--ln);border-radius:10px;padding:10px;height:260px;overflow:auto;font:12.5px/1.45 ui-monospace,Consolas,monospace;white-space:pre-wrap;word-break:break-all}
.term .p{color:var(--ok)}.term .e{color:var(--bad)}
.toast{position:fixed;bottom:18px;right:18px;background:var(--p2);border:1px solid var(--ln);border-left:4px solid var(--ok);padding:12px 16px;border-radius:10px;z-index:80;max-width:430px;display:none;word-break:break-word}
.toast.bad{border-left-color:var(--bad)}
.login{position:fixed;inset:0;background:radial-gradient(900px 500px at 50% -10%,color-mix(in srgb,var(--ac) 25%,transparent),transparent),var(--bg);display:none;overflow:auto;z-index:60}.login.on{display:block}
.hero{max-width:900px;margin:0 auto;padding:64px 20px;text-align:center}
.hero h1{font-size:44px;line-height:1.1;margin:10px 0 12px}.hero p{color:var(--mt);font-size:16px;max-width:560px;margin:0 auto 26px}
.feat{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));margin-top:38px;text-align:left}
.sw{display:flex;gap:10px;flex-wrap:wrap}.dot{width:34px;height:34px;border-radius:50%;cursor:pointer;border:3px solid transparent}.dot.on{border-color:#fff}
code{background:var(--p2);padding:2px 6px;border-radius:6px;font:12.5px ui-monospace,Consolas,monospace;word-break:break-all}
.av{width:72px;height:72px;border-radius:50%}
@media(max-width:800px){.side{position:fixed;bottom:0;top:auto;height:auto;width:100%;flex-direction:row;overflow:auto;z-index:10;border-top:1px solid var(--ln);border-right:0;padding:8px}.brand,.who{display:none}#nav{flex-direction:row}.nav{white-space:nowrap}.main{padding:14px 12px 90px}.hero h1{font-size:32px}}
</style></head><body>
<div class="login" id="login"></div>
<div class="app"><nav class="side"><div class="brand">🔥 Ariz<b>Nodes</b>Cloud</div><div id="nav"></div></nav>
<main class="main"><section id="t-overview" hidden></section><section id="t-vps" hidden></section><section id="t-deploy" hidden></section><section id="t-users" hidden></section><section id="t-audit" hidden></section><section id="t-settings" hidden></section><section id="t-account" hidden></section></main></div>
<div id="scrim" class="scrim" onclick="closeDrawer()"></div><div id="drawer" class="drawer"><div id="dr"></div></div><div id="toast" class="toast"></div>
<script>
const $=s=>document.querySelector(s);
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let CFG={},ME=null,OV={},VPS=[],CUR=null,TAB='',TERMS={};
const isAdmin=()=>!!(ME&&ME.admin), VB=()=>isAdmin()?'vps/':'my/vps/';
async function api(p,m,b){
  const r=await fetch('/api/'+p,{method:m||'GET',headers:{'Content-Type':'application/json','X-Requested-With':'ariz'},body:b?JSON.stringify(b):undefined});
  if(r.status===401){showLogin();throw new Error('Not signed in')}
  const j=await r.json().catch(()=>({}));if(!r.ok)throw new Error(j.error||r.statusText);return j}
function toast(t,bad){const e=$('#toast');e.textContent=t;e.className='toast'+(bad?' bad':'');e.style.display='block';clearTimeout(toast.t);toast.t=setTimeout(()=>{e.style.display='none'},bad?9000:5500)}
const ERR={state:'Login expired — please try again.',token:'Discord login failed — check the Client Secret / redirect URL in the bot settings.',banned:'This account is banned.',discord_off:'Discord login is not configured on this server.'};
function showLogin(){
  const c=CFG||{};$('#login').classList.add('on');
  $('#login').innerHTML='<div class="hero"><div class="brand" style="font-size:20px">🔥 Ariz<b>Nodes</b>Cloud</div><h1>Your own server,<br>one click away.</h1><p>Deploy, manage and control your VPS from anywhere — web terminal, SSH links and live stats included.</p>'
  +(c.discord?'<a href="/auth/login" style="text-decoration:none"><button class="btn dc">Continue with Discord</button></a>':'<div class="sub">Discord login is not enabled yet.</div>')
  +(c.password?'<div style="max-width:320px;margin:26px auto 0"><div class="sub" style="margin-bottom:6px">Administrator password</div><div class="row" style="flex-wrap:nowrap"><input id="pw" type="password" placeholder="Admin password" onkeydown="if(event.key===\'Enter\')doLogin()"><button class="btn pri" onclick="doLogin()">Sign in</button></div></div>':'')
  +'<div class="feat"><div class="card"><b>⌨️ Web terminal</b><div class="sub" style="margin:4px 0 0">Run commands right in your browser.</div></div><div class="card"><b>🔌 SSH & sshx</b><div class="sub" style="margin:4px 0 0">One-click SSH link or browser shell.</div></div><div class="card"><b>🚀 Instant deploy</b><div class="sub" style="margin:4px 0 0">Debian, Ubuntu, Alma, Rocky & more.</div></div><div class="card"><b>📊 Live stats</b><div class="sub" style="margin:4px 0 0">CPU, RAM, disk and network usage.</div></div></div></div>'}
async function doLogin(){try{await api('login','POST',{password:$('#pw').value});boot()}catch(e){toast(e.message,1)}}
async function logout(){await api('logout','POST',{}).catch(()=>{});ME=null;location.href='/'}
const bar=p=>'<div class="bar"><i style="width:'+Math.min(100,Math.max(0,p||0))+'%"></i></div>';
const fmtUp=s=>Math.floor(s/86400)+'d '+Math.floor(s%86400/3600)+'h '+Math.floor(s%3600/60)+'m';
const NAV_USER=[['vps','🖥️ My VPS'],['deploy','🚀 Deploy'],['account','👤 Account']];
const NAV_ADMIN=[['overview','📊 Overview'],['vps','🖥️ All VPS'],['deploy','🚀 Deploy'],['users','👥 Users'],['audit','📜 Audit'],['settings','⚙️ Settings'],['account','👤 Account']];
function buildNav(){
  $('#nav').innerHTML=(isAdmin()?NAV_ADMIN:NAV_USER).map(x=>'<button class="nav" data-t="'+x[0]+'" onclick="show(\''+x[0]+'\')">'+x[1]+'</button>').join('')
  +'<div class="who">'+(ME.avatar?'<img src="'+esc(ME.avatar)+'" alt="">':'')+'<div><b>'+esc(ME.name)+'</b><div class="sub" style="margin:0;font-size:12px">'+(isAdmin()?'Administrator':'Member')+'</div></div></div>'}
async function loadOverview(){
  OV=await api('overview');document.documentElement.style.setProperty('--ac',OV.themes[OV.theme]||'#ff4500');
  $('#t-overview').innerHTML='<h1>Overview</h1><div class="sub">'+esc(OV.bot)+' · v'+esc(OV.version)+' · up '+fmtUp(OV.uptime)+' · '+OV.latency+'ms · '+OV.guilds+' server(s)</div><div class="grid">'
  +'<div class="card"><h3>CPU</h3><div class="big">'+OV.cpu.toFixed(0)+'%</div>'+bar(OV.cpu)+'</div>'
  +'<div class="card"><h3>Memory</h3><div class="big">'+OV.ram.toFixed(0)+'%</div><div class="sub" style="margin:0">'+OV.ram_used+' / '+OV.ram_total+' MB</div>'+bar(OV.ram)+'</div>'
  +'<div class="card"><h3>Disk</h3><div class="big">'+OV.disk.toFixed(0)+'%</div><div class="sub" style="margin:0">'+OV.disk_used+' / '+OV.disk_total+' GB</div>'+bar(OV.disk)+'</div>'
  +'<div class="card"><h3>VPS</h3><div class="big">'+OV.running+'<span style="color:var(--mt);font-size:16px"> / '+OV.vps+' running</span></div><div class="sub" style="margin:0">'+OV.suspended+' suspended</div></div>'
  +'<div class="card"><h3>Users</h3><div class="big">'+OV.users+'</div><div class="sub" style="margin:0">'+OV.tunnels+' active tunnels</div></div>'
  +'<div class="card"><h3>Mode</h3><div class="big" style="font-size:20px">'+(OV.maintenance?'🛠️ Maintenance':'✅ Live')+'</div><div class="sub" style="margin:0">load '+OV.load.map(x=>x.toFixed(2)).join(' ')+'</div></div></div>'}
function initVps(){
  const a=isAdmin();
  $('#t-vps').innerHTML='<h1>'+(a?'All VPS':'My VPS')+'</h1><div class="sub" id="vcount"></div>'
  +(a?'<div class="row" style="margin-bottom:12px"><input id="vf" class="grow" placeholder="Search name / owner / OS…" oninput="drawVps()"><button class="btn" onclick="loadVps()">↻ Refresh</button></div><div class="card" style="padding:0;overflow:auto"><table><thead><tr><th>Name</th><th>State</th><th>Owner</th><th>Specs</th><th>Expires</th><th></th></tr></thead><tbody id="vb"></tbody></table></div>'
  :'<div class="row" style="margin-bottom:12px"><button class="btn" onclick="loadVps()">↻ Refresh</button><button class="btn pri" onclick="show(\'deploy\')">🚀 New VPS</button></div><div class="grid" id="vgrid"></div>')}
async function loadVps(){VPS=await api(isAdmin()?'vps':'my/vps');drawVps();if(CUR)drawDrawer()}
function drawVps(){
  $('#vcount').textContent=VPS.length+(isAdmin()?' total':' server(s)');
  if(!isAdmin()){
    $('#vgrid').innerHTML=VPS.length?VPS.map(v=>'<div class="card vc" onclick="openVps(\''+esc(v.name)+'\')"><div class="row" style="justify-content:space-between"><b>'+esc(v.name)+'</b><span class="badge '+esc(v.state)+'">'+esc(v.state)+'</span></div>'
      +'<div class="sub" style="margin:4px 0 8px">'+esc(v.os_label)+(v.note?' · '+esc(v.note):'')+'</div><div class="row"><code>'+v.ram+' MB</code><code>'+v.cpu+' vCPU</code><code>'+v.disk+' GB</code></div>'
      +(v.suspended==2?'<div class="sub" style="margin:8px 0 0;color:var(--bad)">⌛ expired — open to renew</div>':v.suspended?'<div class="sub" style="margin:8px 0 0;color:var(--bad)">⛔ suspended</div>':v.expires?'<div class="sub" style="margin:8px 0 0">⏳ expires '+new Date(v.expires*1000).toLocaleDateString()+'</div>':'')+'</div>').join('')
      :'<div class="card"><b>No VPS yet</b><div class="sub" style="margin:6px 0 12px">Deploy your first server in under two minutes.</div><button class="btn pri" onclick="show(\'deploy\')">🚀 Deploy now</button></div>';return}
  const f=($('#vf')?$('#vf').value:'').toLowerCase();
  const rows=VPS.filter(v=>!f||(v.name+' '+v.owner+' '+(v.owner_name||'')+' '+v.os_label).toLowerCase().includes(f)).map(v=>
   '<tr><td><b>'+esc(v.name)+'</b><div class="sub" style="margin:0;font-size:12px">'+esc(v.note||v.os_label)+'</div></td><td><span class="badge '+esc(v.state)+'">'+esc(v.state)+'</span>'
   +(v.suspended?' <span class="badge STOPPED">'+(v.suspended==2?'expired':'suspended')+'</span>':'')+'</td><td>'+esc(v.owner_name||v.owner)+'</td><td>'+v.ram+'MB · '+v.cpu+'c · '+v.disk+'G</td>'
   +'<td>'+(v.expires?new Date(v.expires*1000).toLocaleDateString():'—')+'</td><td style="text-align:right"><button class="btn sm pri" onclick="openVps(\''+esc(v.name)+'\')">Manage</button></td></tr>').join('');
  $('#vb').innerHTML=rows||'<tr><td colspan="6" style="text-align:center;color:var(--mt)">No VPS found</td></tr>'}
async function openVps(n){CUR=n;$('#drawer').classList.add('on');$('#scrim').classList.add('on');drawDrawer()}
function closeDrawer(){CUR=null;$('#drawer').classList.remove('on');$('#scrim').classList.remove('on')}
function drawDrawer(){
  const v=VPS.find(x=>x.name===CUR);if(!v)return;
  const L=(l,x)=>x?'<div style="margin:6px 0"><div class="sub" style="margin:0;font-size:12px">'+l+'</div><code>'+esc(x)+'</code></div>':'';
  const ssh=v.ssh?'ssh root@'+v.ssh.split(':')[0]+' -p '+v.ssh.split(':')[1]:'';
  const B=(a,l,c)=>'<button class="btn sm '+(c||'')+'" onclick="act(\''+a+'\')">'+l+'</button>', a=isAdmin();
  $('#dr').innerHTML='<div class="row" style="justify-content:space-between"><h1 style="margin:0">'+esc(v.name)+'</h1><button class="btn sm" onclick="closeDrawer()">✕</button></div>'
  +'<div class="sub"><span class="badge '+esc(v.state)+'">'+esc(v.state)+'</span> · '+esc(v.os_label)+' · '+v.ram+'MB · '+v.cpu+' vCPU · '+v.disk+'GB'+(a?' · owner '+esc(v.owner_name||v.owner):'')+'</div>'
  +(v.suspended==2?'<div class="card" style="border-color:var(--bad);margin-bottom:12px">⌛ This VPS expired. Renew it to start it again. '+B('renew','⏳ Renew now','pri')+'</div>':'')
  +'<div class="row" style="margin-bottom:10px">'+B('start','▶ start','ok')+B('stop','⏹ stop')+B('restart','🔄 restart')+B('kill','☠ kill','bad')+(a?B('pause','⏸ pause')+B('resume','⏯ resume'):'')+'</div>'
  +'<div class="row" style="margin-bottom:12px">'+B('ssh','🔌 Pinggy SSH','pri')+B('sshstop','stop SSH')+B('sshx','🌍 sshx','pri')+B('sshxstop','stop sshx')+B('http','🌐 web port')+B('httpstop','stop web')+B('autossh','🔁 auto-SSH')
  +B('snapshot','📸 snapshot')+B('resetpass','🔐 reset pass')+B('renew','⏳ renew')+(a?B(v.suspended?'unsuspend':'suspend',v.suspended?'✅ unsuspend':'⛔ suspend'):'')
  +'<button class="btn sm bad" onclick="if(confirm(\'Delete \'+CUR+\' permanently? This cannot be undone.\'))act(\'delete\')">🗑 delete</button></div>'
  +'<div class="card" style="margin-bottom:12px"><h3>Access</h3>'+L('Pinggy SSH',ssh)+L('sshx web terminal',v.sshx)+L('Web link',v.http)+((!ssh&&!v.sshx&&!v.http)?'<span class="sub">No active links — open one above.</span>':'')+'</div>'
  +'<div class="card" style="margin-bottom:12px"><h3>Live usage <button class="btn sm" onclick="usage()">↻ measure</button></h3><div id="us" class="sub">Press measure.</div></div>'
  +'<div class="card"><h3>Console</h3><div class="term" id="term"></div><div class="row" style="margin-top:8px;flex-wrap:nowrap"><input id="cmd" class="grow" placeholder="type a command and press Enter" onkeydown="if(event.key===\'Enter\')runCmd()"><button class="btn pri" onclick="runCmd()">Run</button></div></div>';
  const t=$('#term');t.innerHTML=TERMS[CUR]||'<span class="sub">root@'+esc(v.name)+' — commands run as root, cd is remembered.</span>';t.scrollTop=t.scrollHeight}
async function act(a){
  try{let body={};if(a==='http'){const p=prompt('Port inside the VPS to expose (e.g. 80, 3000):','80');if(!p)return;body={port:parseInt(p,10)}}
   toast('⏳ '+a+'… (SSH / sshx can take up to a minute)');const r=await api(VB()+CUR+'/'+a,'POST',body);
   let m=r.msg||'Done';if(r.cmd)m='SSH ready: '+r.cmd;if(r.url)m='Link: '+r.url;if(r.pw)m='New root password: '+r.pw;toast(m);
   if(a==='delete')closeDrawer();await loadVps()}catch(e){toast(e.message,1)}}
async function runCmd(){
  const i=$('#cmd'),c=i.value.trim();if(!c)return;i.value='';const n=CUR;
  TERMS[n]=(TERMS[n]||'')+'<span class="p">$ '+esc(c)+'</span>\n';$('#term').innerHTML=TERMS[n];
  try{const r=await api(VB()+n+'/exec','POST',{cmd:c});TERMS[n]+=esc(r.out||'')+(r.out?'\n':'')+'<span class="'+(r.rc?'e':'p')+'">[exit '+r.rc+'] '+esc(r.cwd)+'</span>\n'}
  catch(e){TERMS[n]+='<span class="e">'+esc(e.message)+'</span>\n'}
  if(CUR===n){const t=$('#term');t.innerHTML=TERMS[n];t.scrollTop=t.scrollHeight}}
async function usage(){
  try{$('#us').textContent='Measuring…';const u=await api(VB()+CUR+'/usage','POST',{});
   $('#us').innerHTML='CPU '+u.cpup.toFixed(0)+'%'+bar(u.cpup)+'RAM '+u.memp.toFixed(0)+'% ('+(u.mem/1048576).toFixed(0)+' MB)'+bar(u.memp)+'Disk '+u.diskp.toFixed(0)+'%'+bar(u.diskp)
   +'<div>⬇ '+(u.rx/1048576).toFixed(1)+' MB · ⬆ '+(u.tx/1048576).toFixed(1)+' MB · '+u.procs+' processes</div>'}catch(e){$('#us').textContent=e.message}}
function initDeploy(){
  const a=isAdmin(),opts=Object.entries(ME.images).map(x=>'<option value="'+esc(x[0])+'">'+esc(x[1])+'</option>').join(''),pl=Object.entries(ME.plans).map(x=>'<option value="'+esc(x[0])+'">'+esc(x[0])+' — '+x[1][0]+'MB · '+x[1][1]+' vCPU · '+x[1][2]+'GB</option>').join('');
  $('#t-deploy').innerHTML='<h1>Deploy</h1><div class="sub">'+(a?'Create a VPS for any user — ignores limits, cooldown and maintenance mode.':'You are using <b>'+ME.count+' of '+ME.limit+'</b> servers.'+(ME.default_days?' Servers last '+ME.default_days+' days and can be renewed.':''))+'</div>'
  +(ME.maintenance&&!a?'<div class="card" style="border-color:var(--wn);margin-bottom:12px;max-width:560px">🛠️ Maintenance mode is on — new deployments are paused.</div>':'')
  +'<div class="card" style="max-width:560px"><div style="display:grid;gap:10px">'+(a?'<input id="d_u" placeholder="Discord user ID (e.g. 123456789012345678)">':'')
  +'<select id="d_os">'+opts+'</select><select id="d_pl">'+pl+'</select><button class="btn pri" id="d_go" onclick="deploy()">🚀 Deploy</button><div id="d_out"></div></div></div>'}
async function deploy(){
  const b=$('#d_go');b.disabled=true;b.textContent='Deploying… (1–3 min, keep this page open)';
  try{const body={os:$('#d_os').value,plan:$('#d_pl').value};if(isAdmin())body.user_id=$('#d_u').value.trim();
   const r=await api(isAdmin()?'deploy':'my/deploy','POST',body);
   $('#d_out').innerHTML='<div class="card"><b>✅ '+esc(r.name)+' is ready</b><br>root password: <code>'+esc(r.pw)+'</code><br>'+(r.ssh?'<code>'+esc(r.ssh)+'</code>':'⚠️ '+esc(r.tunnel_err||'no tunnel yet — open one from the VPS page'))+'<div class="sub" style="margin:6px 0 0">Credentials were also sent by Discord DM. Save the password now.</div></div>';
   if(!isAdmin()){ME=await api('me')}}
  catch(e){toast(e.message,1)}b.disabled=false;b.textContent='🚀 Deploy'}
async function loadUsers(){
  const U=await api('users');
  $('#t-users').innerHTML='<h1>Users</h1><div class="sub">'+U.length+' known</div><div class="card" style="padding:0;overflow:auto"><table><thead><tr><th>User</th><th>VPS</th><th>Limit</th><th>Status</th><th></th></tr></thead><tbody>'
  +U.map(u=>'<tr><td><b>'+esc(u.name||u.id)+'</b><div class="sub" style="margin:0;font-size:12px">'+esc(u.id)+'</div></td><td>'+u.vps+'</td><td>'+u.limit+'</td><td>'+(u.admin?'<span class="badge RUNNING">admin</span> ':'')+(u.banned?'<span class="badge STOPPED">banned</span>':'')+'</td>'
  +'<td style="text-align:right">'+(u.banned?'<button class="btn sm ok" onclick="uact(\''+esc(u.id)+'\',\'unban\')">unban</button>':'<button class="btn sm bad" onclick="uact(\''+esc(u.id)+'\',\'ban\')">ban</button>')
  +' <button class="btn sm" onclick="setLimit(\''+esc(u.id)+'\','+u.limit+')">limit</button> <button class="btn sm" onclick="uact(\''+esc(u.id)+'\',\''+(u.admin?'unadmin':'admin')+'\')">'+(u.admin?'− admin':'+ admin')+'</button></td></tr>').join('')+'</tbody></table></div>'}
async function uact(id,a,v){try{await api('users/'+id+'/'+a,'POST',{value:v});toast('✅ '+a+' done');loadUsers()}catch(e){toast(e.message,1)}}
function setLimit(id,cur){const v=prompt('New VPS limit for this user:',cur);if(v!==null&&v!=='')uact(id,'limit',parseInt(v,10))}
async function loadAudit(){
  const A=await api('audit');
  $('#t-audit').innerHTML='<h1>Audit log</h1><div class="sub">Latest 150 actions</div><div class="card" style="padding:0;overflow:auto"><table><thead><tr><th>Time</th><th>User</th><th>Action</th><th>Detail</th></tr></thead><tbody>'
  +A.map(a=>'<tr><td>'+new Date(a.ts*1000).toLocaleString()+'</td><td>'+(a.uid==='0'?'🌐 web admin':esc(a.uid))+'</td><td><b>'+esc(a.action)+'</b></td><td>'+esc(a.detail)+'</td></tr>').join('')+'</tbody></table></div>'}
async function loadSettings(){
  await loadOverview();
  $('#t-settings').innerHTML='<h1>Settings</h1><div class="sub">Changes apply instantly to the bot.</div><div class="grid">'
  +'<div class="card"><h3>Maintenance mode</h3><p class="sub">Blocks deploys and VPS commands for non-admins.</p><button class="btn '+(OV.maintenance?'bad':'ok')+'" onclick="setS(\'maintenance\','+(!OV.maintenance)+')">'+(OV.maintenance?'Turn OFF':'Turn ON')+'</button></div>'
  +'<div class="card"><h3>Theme (Discord + website)</h3><div class="sw">'+Object.entries(OV.themes).map(x=>'<div class="dot '+(x[0]===OV.theme?'on':'')+'" style="background:'+esc(x[1])+'" title="'+esc(x[0])+'" onclick="setS(\'theme\',\''+esc(x[0])+'\')"></div>').join('')+'</div></div>'
  +'<div class="card"><h3>Container network</h3><p class="sub">If new VPS have no internet (SSH / sshx fail), repair the host firewall &amp; NAT.</p><button class="btn pri" id="nfb" onclick="netfix()">🛠 Repair network</button><pre id="nfo" class="term" style="display:none;height:auto;max-height:220px;margin-top:10px"></pre></div>'
  +'<div class="card" style="grid-column:1/-1"><h3>Broadcast to all VPS owners (DM)</h3><textarea id="bc" rows="3" placeholder="Message…"></textarea><div style="height:8px"></div><button class="btn pri" onclick="broadcast()">📢 Send</button></div></div>'}
async function netfix(){const b=$('#nfb');b.disabled=true;b.textContent='Repairing… (up to 2 min)';try{const r=await api('netfix','POST',{});const o=$('#nfo');o.style.display='block';o.textContent=r.out||'done'}catch(e){toast(e.message,1)}b.disabled=false;b.textContent='🛠 Repair network'}
async function setS(k,v){try{await api('settings','POST',{key:k,value:v});toast('✅ Saved');loadSettings()}catch(e){toast(e.message,1)}}
async function broadcast(){const m=$('#bc').value.trim();if(!m)return;try{const r=await api('broadcast','POST',{message:m});toast('📢 Sending to '+r.count+' users');$('#bc').value=''}catch(e){toast(e.message,1)}}
function loadAccount(){
  const pct=ME.limit?Math.min(100,ME.count/ME.limit*100):0;
  $('#t-account').innerHTML='<h1>Account</h1><div class="sub">Signed in with '+(ME.uid==='0'?'the admin password':'Discord')+'</div><div class="card" style="max-width:520px"><div class="row" style="flex-wrap:nowrap;gap:16px">'+(ME.avatar?'<img class="av" src="'+esc(ME.avatar)+'" alt="">':'')
  +'<div><div class="big" style="font-size:22px">'+esc(ME.name)+'</div><div class="sub" style="margin:0">'+(ME.uid==='0'?'Web administrator':'Discord ID '+esc(ME.uid))+'</div><div style="margin-top:6px"><span class="badge '+(isAdmin()?'RUNNING':'FROZEN')+'">'+(isAdmin()?'Administrator':'Member')+'</span></div></div></div>'
  +'<div style="margin-top:16px"><div class="sub" style="margin:0">Servers: '+ME.count+' / '+ME.limit+'</div>'+bar(pct)+'</div><button class="btn bad" onclick="logout()">Log out</button></div>'}
async function load(t){
  try{if(t==='overview')await loadOverview();else if(t==='vps'){initVps();await loadVps()}else if(t==='deploy')initDeploy();else if(t==='users')await loadUsers();else if(t==='audit')await loadAudit();else if(t==='settings')await loadSettings();else if(t==='account')loadAccount()}
  catch(e){if(e.message!=='Not signed in')toast(e.message,1)}}
function show(t){TAB=t;document.querySelectorAll('.nav').forEach(b=>b.classList.toggle('on',b.dataset.t===t));document.querySelectorAll('main section').forEach(s=>{s.hidden=s.id!=='t-'+t});load(t)}
async function boot(){
  try{CFG=await api('config')}catch(e){CFG={}}
  const m=location.search.match(/err=(\w+)/);if(m){toast(ERR[m[1]]||'Login failed','1');history.replaceState(null,'','/')}
  try{ME=await api('me')}catch(e){showLogin();return}
  $('#login').classList.remove('on');buildNav();show(isAdmin()?'overview':'vps')}
setInterval(()=>{if(!ME||CUR)return;if(TAB==='overview'&&isAdmin())loadOverview().catch(()=>{});else if(TAB==='vps')loadVps().catch(()=>{})},8000);
boot();
</script></body></html>
'''
SESS = {}; LOGIN_FAILS = {}; DASHTUN = {}
USER_ACTS = {"start", "stop", "restart", "kill", "ssh", "sshstop", "sshx", "sshxstop", "http", "httpstop", "autossh", "snapshot", "resetpass", "renew", "exec", "usage", "delete", "note"}
async def live_states():
    rc, o = await lx("list", "-c", "ns", "--format", "csv"); return dict((l.split(",", 1)[0], l.split(",", 1)[1].upper()) for l in o.splitlines() if "," in l) if rc == 0 else {}
def client_ip(req):
    if TRUST_PROXY: return req.headers.get("CF-Connecting-IP") or req.headers.get("X-Forwarded-For", "").split(",")[0].strip() or req.remote or "?"
    return req.remote or "?"
def base_url(req):
    if DASH_URL: return DASH_URL
    proto = (req.headers.get("X-Forwarded-Proto") if TRUST_PROXY else None) or ("https" if req.secure else "http")
    return f"{proto}://{req.host}"
def sess_of(req):
    t = req.cookies.get("ariz_s"); s = SESS.get(t) if t else None
    return s if s and s["exp"] > time.time() else None
def set_session(resp, req, s):
    tok = secrets.token_urlsafe(32); SESS[tok] = {**s, "exp": time.time() + 7 * 86400}
    resp.set_cookie("ariz_s", tok, max_age=7 * 86400, httponly=True, samesite="Lax", secure=base_url(req).startswith("https")); return tok
def jr(data, status=200): return web.json_response(data, status=status)
@web.middleware
async def dash_mw(req, handler):
    p = req.path; s = sess_of(req); req["sess"] = s
    if p.startswith("/api/") and p not in ("/api/config", "/api/login", "/api/logout"):
        if not s: return jr({"error": "Not signed in"}, 401)
        s["admin"] = True if s["uid"] == 0 else is_admin(s["uid"])
        if s["uid"] and not s["admin"] and urow(s["uid"])["banned"]: return jr({"error": "This account is banned."}, 403)
        if not s["admin"] and not (p == "/api/me" or p.startswith("/api/my/")): return jr({"error": "Administrators only."}, 403)
        if req.method != "GET" and req.headers.get("X-Requested-With") != "ariz": return jr({"error": "Bad request"}, 403)
    try: resp = await handler(req)
    except web.HTTPException: raise
    except Exception as ex: print("dashboard error:", repr(ex)); return jr({"error": f"{type(ex).__name__}: {ex}"}, 500)
    resp.headers["Cache-Control"] = "no-store"; resp.headers["X-Frame-Options"] = "DENY"; resp.headers["X-Content-Type-Options"] = "nosniff"; return resp
async def dash_index(req): return web.Response(text=DASH_HTML, content_type="text/html")
async def api_config(req):
    return jr({"name": str(bot.user), "discord": bool(DISCORD_SECRET), "password": bool(DASH_PASS), "theme": "#%06x" % theme()[0]})
async def api_login(req):  # administrator password login
    ip = client_ip(req); n, ts = LOGIN_FAILS.get(ip, (0, 0))
    if n >= 5 and time.time() - ts < 300: return jr({"error": "Too many attempts — wait 5 minutes"}, 429)
    try: d = await req.json()
    except Exception: d = {}
    if not DASH_PASS or not secrets.compare_digest(str(d.get("password", "")).encode(), DASH_PASS.encode()):
        LOGIN_FAILS[ip] = (n + 1, time.time()); return jr({"error": "Wrong password"}, 403)
    LOGIN_FAILS.pop(ip, None); audit(0, "web:login", ip); r = jr({"ok": True}); set_session(r, req, {"uid": 0, "name": "Administrator", "avatar": "", "admin": True}); return r
async def api_logout(req):
    SESS.pop(req.cookies.get("ariz_s", ""), None); r = jr({"ok": True}); r.del_cookie("ariz_s"); return r
async def auth_login(req):
    if not DISCORD_SECRET: raise web.HTTPFound("/?err=discord_off")
    st = secrets.token_urlsafe(24)
    url = "https://discord.com/oauth2/authorize?" + urlencode({"client_id": DISCORD_CLIENT_ID or str(bot.user.id), "redirect_uri": base_url(req) + "/auth/callback", "response_type": "code", "scope": "identify", "state": st})
    r = web.HTTPFound(url); r.set_cookie("ariz_state", st, max_age=600, httponly=True, samesite="Lax", secure=base_url(req).startswith("https")); raise r
async def auth_callback(req):
    code, st = req.query.get("code"), req.query.get("state")
    if not code or not st or st != req.cookies.get("ariz_state"): raise web.HTTPFound("/?err=state")
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as cs:
            async with cs.post("https://discord.com/api/v10/oauth2/token", data={"client_id": DISCORD_CLIENT_ID or str(bot.user.id), "client_secret": DISCORD_SECRET, "grant_type": "authorization_code",
                    "code": code, "redirect_uri": base_url(req) + "/auth/callback"}) as r:
                tk = await r.json()
                if r.status != 200 or "access_token" not in tk: print("discord token error:", tk); raise web.HTTPFound("/?err=token")
            async with cs.get("https://discord.com/api/v10/users/@me", headers={"Authorization": "Bearer " + tk["access_token"]}) as r:
                me = await r.json()
        uid = int(me["id"])
    except web.HTTPException: raise
    except Exception as ex: print("discord login error:", repr(ex)); raise web.HTTPFound("/?err=token")
    if urow(uid)["banned"] and not is_admin(uid): raise web.HTTPFound("/?err=banned")
    av = f"https://cdn.discordapp.com/avatars/{uid}/{me['avatar']}.png?size=128" if me.get("avatar") else f"https://cdn.discordapp.com/embed/avatars/{(uid >> 22) % 6}.png"
    resp = web.HTTPFound("/"); set_session(resp, req, {"uid": uid, "name": me.get("global_name") or me.get("username") or str(uid), "avatar": av, "admin": is_admin(uid)}); resp.del_cookie("ariz_state")
    audit(uid, "web:login", client_ip(req)); raise resp
async def api_me(req):
    s = req["sess"]; uid = s["uid"]; n = q("SELECT COUNT(*) c FROM vps WHERE owner=?", (uid,), True)["c"] if uid else 0
    return jr({"uid": str(uid), "name": s["name"], "avatar": s.get("avatar", ""), "admin": s["admin"], "count": n, "limit": ulimit(uid) if uid else 999, "maintenance": gset("maint") == "1", "default_days": DEFAULT_DAYS,
        "cooldown": COOLDOWN, "images": {k: v[0] for k, v in IMAGES.items()}, "plans": {k: list(v) for k, v in PLANS.items()}})
def vps_dict(r, live):
    d = dict(r); d["owner"] = str(r["owner"]); u = bot.get_user(r["owner"]); d["owner_name"] = str(u) if u else None
    d["state"] = live.get(r["name"], "MISSING"); d["os_label"] = IMAGES.get(r["os"], (r["os"],))[0]; return d
async def vps_action(r, act, d, admin):
    c = r["name"]
    if act in ("start", "stop", "restart", "kill", "pause", "resume", "delete"):
        ok, o = await do_act(act, r); return ({"ok": True, "msg": f"{act} done"}, 200) if ok else ({"error": o}, 400)
    if act == "ssh": addr, e = await start_tunnel(c); return ({"error": e}, 400) if e else ({"ok": True, "addr": addr, "cmd": ssh_line(addr)}, 200)
    if act == "sshstop": await stop_tunnel(c); return {"ok": True, "msg": "Pinggy tunnel closed"}, 200
    if act == "sshx": url, e = await start_sshx(c); return ({"error": e}, 400) if e else ({"ok": True, "url": url}, 200)
    if act == "sshxstop": await stop_sshx(c); return {"ok": True, "msg": "sshx stopped"}, 200
    if act == "http":
        try: port = int(d.get("port"))
        except (TypeError, ValueError): return {"error": "Enter a valid port (1-65535)"}, 400
        if not 1 <= port <= 65535: return {"error": "Enter a valid port (1-65535)"}, 400
        url, e = await start_http(c, port); return ({"error": e}, 400) if e else ({"ok": True, "url": url}, 200)
    if act == "httpstop": await stop_http(c); return {"ok": True, "msg": "Web tunnel closed"}, 200
    if act == "autossh": v = 0 if r["autossh"] else 1; q("UPDATE vps SET autossh=? WHERE name=?", (v, c)); return {"ok": True, "msg": "Auto-SSH " + ("ON" if v else "OFF")}, 200
    if act == "note": q("UPDATE vps SET note=? WHERE name=?", (str(d.get("note", ""))[:100], c)); return {"ok": True, "msg": "Note saved"}, 200
    if act in ("suspend", "unsuspend"):
        if not admin: return {"error": "Administrators only."}, 403
        q("UPDATE vps SET suspended=? WHERE name=?", (1 if act == "suspend" else 0, c))
        if act == "suspend": await do_act("stop", r)
        return {"ok": True, "msg": act + " done"}, 200
    if act == "resetpass":
        pw = rpass(); rc, o = await inside(c, 'echo "root:$PW" | chpasswd', 30, {"PW": pw}); return ({"error": o or "Could not reset — is the VPS running?"}, 400) if rc else ({"ok": True, "pw": pw}, 200)
    if act == "snapshot":
        n = "snap-" + time.strftime("%m%d-%H%M%S"); rc, o = await lx("snapshot", c, n, timeout=300); return ({"error": o}, 400) if rc else ({"ok": True, "msg": "Snapshot " + n}, 200)
    if act == "renew":
        ok, m = await do_renew(r); m = re.sub(r" \(<t:\d+:R>\)", "", m); m = re.sub(r"<t:(\d+):[A-Za-z]>", lambda x: time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(int(x.group(1)))), m).replace("`", ""); return ({"ok": True, "msg": m}, 200) if ok else ({"error": m}, 400)
    if act == "usage":
        u = await usage(c, r, 2) if await lxstate(c) == "RUNNING" else None; return (u, 200) if u else ({"error": "VPS is not running"}, 400)
    if act == "exec":
        if await lxstate(c) != "RUNNING": return {"error": "VPS is not running"}, 400
        rc, out, cwd = await console_run(c, str(d.get("cmd", ""))[:4000], 120); return {"out": out[-8000:], "rc": rc, "cwd": cwd}, 200
    return {"error": "unknown action"}, 400
async def body_of(req):
    try: return await req.json()
    except Exception: return {}
# ── member endpoints ──
async def api_my_vps(req):
    live = await live_states(); return jr([vps_dict(r, live) for r in q("SELECT * FROM vps WHERE owner=? ORDER BY created DESC", (req["sess"]["uid"],))])
async def api_my_action(req):
    s = req["sess"]; r = find(req.match_info["name"]); act = req.match_info["act"]
    if not r or r["owner"] != s["uid"]: return jr({"error": "VPS not found"}, 404)
    if act not in USER_ACTS: return jr({"error": "Not allowed"}, 403)
    if r["suspended"] == 1: return jr({"error": "⛔ This VPS was suspended by an administrator."}, 403)
    if r["suspended"] == 2 and act not in ("renew", "delete"): return jr({"error": "⌛ This VPS expired — renew it first."}, 403)
    if act not in ("usage", "exec"): audit(s["uid"], "web:" + act, r["name"])
    data, st = await vps_action(r, act, await body_of(req), False); return jr(data, st)
async def api_my_deploy(req):
    s = req["sess"]; uid = s["uid"]
    if not uid: return jr({"error": "Sign in with Discord to deploy servers for yourself."}, 400)
    d = await body_of(req); task = asyncio.create_task(deploy_vps(uid, d.get("os"), d.get("plan"), None)); res, e = await asyncio.shield(task)
    if e: return jr({"error": e}, 400)
    asyncio.create_task(notify(uid, cred_embed(res))); audit(uid, "web:deploy", res["name"])
    return jr({"ok": True, "name": res["name"], "pw": res["pw"], "ssh": ssh_line(res["ssh"]) if res["ssh"] else None, "tunnel_err": res["tunnel_err"]})
# ── admin endpoints ──
async def api_overview(req):
    vm, du = psutil.virtual_memory(), psutil.disk_usage("/"); rows = q("SELECT * FROM vps"); live = await live_states()
    return jr({"cpu": psutil.cpu_percent(), "ram": vm.percent, "ram_used": vm.used >> 20, "ram_total": vm.total >> 20, "disk": du.percent, "disk_used": du.used >> 30, "disk_total": du.total >> 30,
        "vps": len(rows), "running": sum(1 for r in rows if live.get(r["name"]) == "RUNNING"), "suspended": sum(1 for r in rows if r["suspended"]), "users": q("SELECT COUNT(DISTINCT owner) c FROM vps", one=True)["c"],
        "tunnels": len(TUN) + len(HTTP), "maintenance": gset("maint") == "1", "theme": gset("theme", "fire"), "uptime": int(time.time() - START), "latency": round((bot.latency or 0) * 1000),
        "guilds": len(bot.guilds), "version": VERSION, "bot": str(bot.user), "load": list(os.getloadavg()), "themes": {k: "#%06x" % v[0] for k, v in THEMES.items()}})
async def api_vps(req):
    live = await live_states(); return jr([vps_dict(r, live) for r in q("SELECT * FROM vps ORDER BY created DESC")])
async def api_action(req):
    r = find(req.match_info["name"]); act = req.match_info["act"]
    if not r: return jr({"error": "VPS not found"}, 404)
    if act not in ("usage", "exec"): audit(req["sess"]["uid"], "web:" + act, r["name"])
    d = await body_of(req)
    if act == "exec": audit(req["sess"]["uid"], "web:exec", f"{r['name']}: {str(d.get('cmd', ''))[:120]}")
    data, st = await vps_action(r, act, d, True); return jr(data, st)
async def api_users(req):
    ids = {r["id"] for r in q("SELECT id FROM users")} | {r["owner"] for r in q("SELECT DISTINCT owner FROM vps")} | {r["id"] for r in q("SELECT id FROM admins")} | set(OWNERS); out = []
    for uid in sorted(ids):
        u = urow(uid); du = bot.get_user(uid)
        out.append({"id": str(uid), "name": str(du) if du else None, "vps": q("SELECT COUNT(*) c FROM vps WHERE owner=?", (uid,), True)["c"], "limit": ulimit(uid), "banned": bool(u["banned"]), "admin": is_admin(uid)})
    return jr(out)
async def api_user_act(req):
    try: uid = int(req.match_info["uid"])
    except ValueError: return jr({"error": "bad id"}, 400)
    act = req.match_info["act"]; d = await body_of(req); urow(uid)
    if act == "ban":
        if uid in OWNERS: return jr({"error": "Owners cannot be banned"}, 400)
        q("UPDATE users SET banned=1 WHERE id=?", (uid,))
        for t in [k for k, v in SESS.items() if v["uid"] == uid]: SESS.pop(t, None)
    elif act == "unban": q("UPDATE users SET banned=0 WHERE id=?", (uid,))
    elif act == "limit": q("UPDATE users SET max_vps=? WHERE id=?", (max(0, int(d.get("value", 0))), uid))
    elif act == "admin": q("INSERT OR IGNORE INTO admins VALUES(?)", (uid,))
    elif act == "unadmin":
        if uid in OWNERS: return jr({"error": "Owners are always admins"}, 400)
        q("DELETE FROM admins WHERE id=?", (uid,))
    else: return jr({"error": "unknown action"}, 400)
    audit(req["sess"]["uid"], "web:" + act, str(uid)); return jr({"ok": True})
async def api_audit(req): return jr([{"ts": r["ts"], "uid": str(r["uid"]), "action": r["action"], "detail": r["detail"]} for r in q("SELECT * FROM audit ORDER BY id DESC LIMIT 150")])
async def api_settings(req):
    d = await body_of(req); k, v = d.get("key"), d.get("value")
    if k == "maintenance": sset("maint", "1" if v else "0")
    elif k == "theme" and v in THEMES: sset("theme", v)
    else: return jr({"error": "bad setting"}, 400)
    audit(req["sess"]["uid"], "web:setting", f"{k}={v}"); return jr({"ok": True})
async def api_broadcast(req):
    msg = str((await body_of(req)).get("message", "")).strip()[:1500]
    if not msg: return jr({"error": "empty message"}, 400)
    owners = [r["owner"] for r in q("SELECT DISTINCT owner FROM vps")]
    async def go():
        for o in owners: await notify(o, emb("📢 Announcement", msg)); await asyncio.sleep(1)
    asyncio.create_task(go()); audit(req["sess"]["uid"], "web:broadcast", msg[:100]); return jr({"ok": True, "count": len(owners)})
async def api_deploy(req):
    d = await body_of(req)
    try: uid = int(str(d.get("user_id", "")).strip())
    except ValueError: return jr({"error": "Enter a valid Discord user ID"}, 400)
    task = asyncio.create_task(deploy_vps(uid, d.get("os"), d.get("plan"), None, force=True)); res, e = await asyncio.shield(task)
    if e: return jr({"error": e}, 400)
    asyncio.create_task(notify(uid, cred_embed(res))); audit(req["sess"]["uid"], "web:deploy", f"{res['name']} for {uid}")
    return jr({"ok": True, "name": res["name"], "pw": res["pw"], "ssh": ssh_line(res["ssh"]) if res["ssh"] else None, "tunnel_err": res["tunnel_err"]})
async def api_netfix(req): audit(req["sess"]["uid"], "web:netfix", ""); NETFIX_AT["t"] = 0; return jr({"ok": True, "out": await host_netfix()})
async def start_dashboard():
    if not (DASH_PASS or DISCORD_SECRET): print("ℹ️  Website is OFF — set DISCORD_CLIENT_SECRET (Discord login) and/or DASH_PASSWORD in .env to enable it"); return
    app = web.Application(middlewares=[dash_mw])
    app.add_routes([web.get("/", dash_index), web.get("/auth/login", auth_login), web.get("/auth/callback", auth_callback), web.get("/api/config", api_config), web.post("/api/login", api_login), web.post("/api/logout", api_logout),
        web.get("/api/me", api_me), web.get("/api/my/vps", api_my_vps), web.post("/api/my/vps/{name}/{act}", api_my_action), web.post("/api/my/deploy", api_my_deploy),
        web.get("/api/overview", api_overview), web.get("/api/vps", api_vps), web.post("/api/vps/{name}/{act}", api_action), web.get("/api/users", api_users), web.post("/api/users/{uid}/{act}", api_user_act),
        web.get("/api/audit", api_audit), web.post("/api/settings", api_settings), web.post("/api/broadcast", api_broadcast), web.post("/api/deploy", api_deploy), web.post("/api/netfix", api_netfix)])
    try:
        runner = web.AppRunner(app); await runner.setup(); await web.TCPSite(runner, DASH_HOST, DASH_PORT).start(); print(f"🌐 Website: http://{DASH_HOST}:{DASH_PORT}  (Discord login: {'ON' if DISCORD_SECRET else 'off'}, admin password: {'ON' if DASH_PASS else 'off'})")
    except OSError as ex: print(f"❌ Website could not start on {DASH_HOST}:{DASH_PORT} — {ex}")

@cmd("admin", "Repair container internet (firewall / NAT): !netfix", 2)
async def netfix(ctx):
    m = await ctx.send(embed=emb("🛠️ Repairing container network…", "Checking Docker / ufw / firewalld / NAT. Up to 2 minutes.")); NETFIX_AT["t"] = 0; o = await host_netfix()
    await m.edit(embed=emb("🛠️ Network repair", f"```\n{trim(o, 1500)}\n```\nNow run `{PREFIX}diag <vps>` or deploy again.", 0x2ECC71))
@cmd("admin", "Web dashboard info: !webdash [public]", 2)
async def webdash(ctx, mode: str = None):
    if not (DASH_PASS or DISCORD_SECRET): return await ctx.send(embed=err("The website is disabled. Set `DISCORD_CLIENT_SECRET` and/or `DASH_PASSWORD` in `.env` and restart the bot."))
    e = web_info_embed()
    if mode and mode.lower() == "public":
        m = await ctx.send(embed=emb("🌐 Opening a public Pinggy link…")); old = DASHTUN.pop("t", None)
        if old:
            try: old.kill()
            except Exception: pass
        p, url, er = await pinggy_open("127.0.0.1" if DASH_HOST in ("0.0.0.0", "::", "localhost") else DASH_HOST, DASH_PORT, "http")
        if er: return await m.edit(embed=err(er))
        DASHTUN["t"] = p
        async def drain():
            while await p.stdout.read(4096): pass
        asyncio.create_task(drain()); e.add_field(name="🌍 Public link (temporary, ~60 min)", value=url, inline=False); await m.delete()
    await ctx.send(embed=emb("🌐 Web dashboard", await dm_or_here(ctx, e), 0x2ECC71))


# ───────────────────────── startup ─────────────────────────
async def _hook():
    bot.add_view(PanelView())
    try: await bot.tree.sync()
    except Exception as ex: print("slash sync failed:", ex)
    try:
        for k, v in json.loads(gset("cthreads", "{}")).items(): CTHREADS[int(k)] = tuple(v)
    except Exception: pass
    asyncio.get_event_loop().create_task(watchdog()); asyncio.get_event_loop().create_task(start_dashboard())
bot.setup_hook = _hook
@bot.event
async def on_ready():
    q("UPDATE vps SET ssh='', http=''"); await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{PREFIX}help • ArizNodesLabs"))
    print(f"\n✅ Logged in as {bot.user} • {len(bot.commands)} commands • {len(bot.guilds)} servers")
def banner():
    print("\033[38;5;208m")
    for t in ("ArizNodesLabs", "Vasplayz90"): print(art(t, "big"))
    print("\033[0m  🔥 VPS Deployer Bot v3 • LXC + Pinggy + sshx + Web Panel\n")
if __name__ == "__main__":
    banner(); cnt = {k: sum(1 for c in CAT.values() if c == k) for k in TITLES}; print("Commands:", cnt, "total", len(CAT))
    if not TOKEN or "YOUR_BOT_TOKEN" in TOKEN: sys.exit("❌ Set DISCORD_TOKEN in .env")
    bot.run(TOKEN, log_handler=None)
ARIZ_BOT_PY
  cat > requirements.txt <<'ARIZ_REQ'
discord.py>=2.4.0
python-dotenv>=1.0.0
psutil>=5.9.0
pyfiglet>=1.0.2
aiohttp>=3.9.0
ARIZ_REQ
  cat > netfix.sh <<'ARIZ_NETFIX'
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
ARIZ_NETFIX
  cat > doctor.sh <<'ARIZ_DOCTOR'
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
ARIZ_DOCTOR
  cat > ariznodes-cli <<'ARIZ_CLI'
#!/usr/bin/env bash
# ariznodes — control the ArizNodes VPS bot
DIR="__DIR__"; SVC=ariznodes-vpsbot; export PATH=$PATH:/snap/bin
if [ -t 1 ]; then O=$'\e[38;5;208m'; D=$'\e[2m'; N=$'\e[0m'; B=$'\e[1m'; else O=; D=; N=; B=; fi
envv() { grep -E "^$1=" "$DIR/.env" 2>/dev/null | head -1 | cut -d= -f2- | sed "s/^['\"]//; s/['\"]\$//"; }
need_root() { [ "$(id -u)" = 0 ] || { echo "Run as root:  sudo ariznodes $1"; exit 1; }; }
case "$1" in
  status)  systemctl status $SVC --no-pager -l 2>&1 | head -14 ;;
  start|stop|restart) need_root "$1"; systemctl "$1" $SVC && echo "${O}✔${N} $1 ok" ;;
  logs)    journalctl -u $SVC -n "${2:-60}" --no-pager ;;
  follow)  journalctl -fu $SVC ;;
  env)     need_root env; ${EDITOR:-nano} "$DIR/.env" && echo "Saved. Apply with:  ariznodes restart" ;;
  doctor)  bash "$DIR/doctor.sh" "$2" ;;
  netfix)  need_root netfix; echo "${B}Repairing container networking…${N}"; bash "$DIR/netfix.sh" ;;
  web)     P="$(envv DASH_PORT)"; P="${P:-8787}"; U="$(envv DASH_URL)"
           echo "${B}Website${N}"; echo "  local   : http://127.0.0.1:$P"; [ -n "$U" ] && echo "  public  : $U"
           echo "  Discord login redirect URL → ${U:-https://YOUR-DOMAIN}/auth/callback"
           echo "  Cloudflare Tunnel service URL → http://localhost:$P  (type HTTP)"
           echo "  from your PC:  ssh -L $P:127.0.0.1:$P root@YOUR_SERVER_IP" ;;
  update)  need_root update; [ -f "$2" ] || { echo "Usage: ariznodes update /path/to/ariznodes-vps-bundle-v4.sh"; exit 1; }; cd "$DIR" && bash "$2" --upgrade ;;
  uninstall) need_root uninstall; read -r -p "Remove the service and CLI? VPS and data stay. [y/N] " a; [ "$a" = y ] || exit 0
           systemctl disable --now $SVC ariznodes-netfix 2>/dev/null; rm -f /etc/systemd/system/$SVC.service /etc/systemd/system/ariznodes-netfix.service /usr/local/bin/ariznodes; systemctl daemon-reload; echo "Removed. Files remain in $DIR" ;;
  *) cat <<HELP
${O}${B}ariznodes${N} — ArizNodes VPS bot control
  ${B}status${N}            service status
  ${B}start|stop|restart${N}  control the bot
  ${B}logs [n]${N}          last n log lines     ${D}(follow = live)${N}
  ${B}env${N}               edit settings (.env)
  ${B}doctor [--quick]${N}  full health check
  ${B}netfix${N}            repair container internet (Docker/ufw/NAT)
  ${B}web${N}               website address & Cloudflare/Discord hints
  ${B}update <bundle>${N}   upgrade from a new bundle file
  ${B}uninstall${N}         remove service (keeps your VPS)
HELP
  ;;
esac
ARIZ_CLI
  sed -i "s|__DIR__|$DIR|g" ariznodes-cli; chmod +x netfix.sh doctor.sh ariznodes-cli; mkdir -p backups
}

# ───────────────────────── settings ─────────────────────────
verify_token() {  # sets BOT_NAME / BOT_ID. return 0 ok, 1 invalid, 2 could not reach Discord
  local code; code=$(curl -s -m 12 -o /tmp/ariz_me.json -w '%{http_code}' -H "Authorization: Bot $1" https://discord.com/api/v10/users/@me 2>/dev/null)
  case "$code" in 200) BOT_NAME=$(sed -n 's/.*"username": *"\([^"]*\)".*/\1/p' /tmp/ariz_me.json | head -1); BOT_ID=$(sed -n 's/.*"id": *"\([0-9]*\)".*/\1/p' /tmp/ariz_me.json | head -1); return 0;; 401) return 1;; *) return 2;; esac
}
configure() {
  printf '\n%s%s Let'"'"'s set up your bot %s\n' "$O" "$B" "$N"; printf '%s  (press Enter to accept [defaults]; everything is saved in .env)%s\n\n' "$D" "$N"
  TOKEN=""; local tries=0
  while [ $tries -lt 3 ]; do
    ask_secret TOKEN "Discord bot token (Developer Portal → Bot → Reset Token): "
    [ -z "$TOKEN" ] && { warn "No token entered — you can add it later with: ariznodes env"; break; }
    verify_token "$TOKEN"; case $? in 0) ok "Token is valid — bot is ${B}${BOT_NAME}${N}"; break;; 2) warn "Could not reach Discord to verify the token (offline?). Continuing."; break;; *) bad "Discord says this token is invalid."; TOKEN=""; tries=$((tries+1)); [ -n "$ARIZ_TOKEN" ] && break;; esac
  done
  OWNERS=""; ask OWNERS "Your Discord user ID (Settings → Advanced → Developer Mode → right-click your name → Copy ID): " ""
  OWNERS=$(echo "$OWNERS" | tr -cd '0-9,' ); [ -z "$OWNERS" ] && warn "No owner ID — add it later with: ariznodes env"
  WEB=""; ask WEB "Enable the website (Discord login + admin panel)? [Y/n]: " "Y"
  DASHPASS=""; CSECRET=""; DURL=""; DPORT=8787
  case "$WEB" in n|N|no|NO) info "Website disabled (enable anytime in .env)";; *)
    ask CSECRET "Discord OAuth2 Client Secret (Developer Portal → OAuth2 → Client Secret) [skip = password login only]: " ""
    ask DURL "Public website URL, e.g. https://panel.example.com  [Enter = local only]: " ""; DURL="${DURL%/}"
    ask DPORT "Website port [8787]: " "8787"; DPORT=$(echo "$DPORT" | tr -cd '0-9'); DPORT="${DPORT:-8787}"
    ask DASHPASS "Admin password for the website [Enter = generate a strong one]: " ""
    if [ -z "$DASHPASS" ]; then DASHPASS="$(rand 20)"; GENPASS=1; fi
    DASHPASS=$(printf '%s' "$DASHPASS" | tr -d "'\\\\ ") ;;
  esac
}
write_env() {
  [ -f .env ] && cp .env ".env.bak-$(date +%s)"
  { echo "# ── ArizNodesLabs VPS Deployer v$VERSION — edit with:  ariznodes env  (then: ariznodes restart) ──"
    echo "DISCORD_TOKEN=${TOKEN:-YOUR_BOT_TOKEN_HERE}"; echo "OWNER_IDS=${OWNERS:-123456789012345678}"
    echo "PREFIX=!"; echo "MAX_VPS_PER_USER=3"; echo "MAX_RAM_MB=8192"; echo "MAX_CPU=4"; echo "MAX_DISK_GB=50"; echo "LXC_BIN=lxc"
    echo "PINGGY_TOKEN="; echo "PINGGY_SERVER="
    echo; echo "# website: members log in with Discord, admins control everything"
    echo "DISCORD_CLIENT_SECRET='${CSECRET}'"; echo "DASH_PASSWORD='${DASHPASS}'"; echo "DASH_URL=${DURL}"; echo "DASH_HOST=127.0.0.1"; echo "DASH_PORT=${DPORT}"
    echo; echo "# server rules"; echo "DEFAULT_DAYS=0"; echo "GRACE_DAYS=3"; echo "RENEW_DAYS="; echo "DEPLOY_COOLDOWN=60"; echo "MAX_PARALLEL_DEPLOYS=2"; echo "MAX_BACKUPS=2"; } > .env
  chmod 600 .env
}
add_env() { grep -q "^$1=" .env 2>/dev/null || { printf '\n%s\n%s=%s\n' "$2" "$1" "$3" >> .env; info "added $1 to .env"; }; }
upgrade_env() {
  add_env DEFAULT_DAYS "# days a VPS lives before it auto-stops (0 = never)" 0; add_env GRACE_DAYS "# days after expiry before deletion" 3; add_env RENEW_DAYS "# days added per renew (blank = same as DEFAULT_DAYS)" ""
  add_env DEPLOY_COOLDOWN "# seconds between deploys per user" 60; add_env MAX_PARALLEL_DEPLOYS "# simultaneous builds" 2; add_env MAX_BACKUPS "# backups kept per VPS" 2
  add_env DASH_PASSWORD "# website admin password (empty = password login off)" "''"; add_env DISCORD_CLIENT_SECRET "# Discord OAuth2 client secret (website login)" "''"
  add_env DASH_URL "# public website URL, e.g. https://panel.example.com" ""; add_env DASH_HOST "# 127.0.0.1 = local only (use a tunnel/proxy)" 127.0.0.1; add_env DASH_PORT "# website port" 8787
  add_env PINGGY_SERVER "# optional Pinggy server override" ""; chmod 600 .env
}

# ───────────────────────── system steps ─────────────────────────
install_packages() { export DEBIAN_FRONTEND=noninteractive; apt-get update -y && apt-get install -y python3 python3-venv python3-pip openssh-client curl git ca-certificates iptables snapd; }
install_lxd() {
  command -v lxc >/dev/null 2>&1 || [ -x /snap/bin/lxc ] && return 0
  systemctl enable --now snapd.socket; ln -s /var/lib/snapd/snap /snap 2>/dev/null; sleep 3
  for i in 1 2 3; do snap install core && break; sleep 5; done
  snap install lxd && /snap/bin/lxd waitready --timeout 90 && /snap/bin/lxd init --auto
}
fix_lxd_profile() {
  export PATH=$PATH:/snap/bin; local P; P="$(lxc profile show default 2>/dev/null)"
  echo "$P" | grep -q 'root:' || { lxc storage list --format csv 2>/dev/null | grep -q '^default,' || lxc storage create default dir; lxc profile device add default root disk path=/ pool=default; }
  P="$(lxc profile show default 2>/dev/null)"
  echo "$P" | grep -q 'eth0:' || { lxc network list --format csv 2>/dev/null | grep -q '^lxdbr0,' || lxc network create lxdbr0; lxc profile device add default eth0 nic network=lxdbr0 name=eth0; }
  lxc remote list 2>/dev/null | grep -q ubuntu || lxc remote add ubuntu https://cloud-images.ubuntu.com/releases --protocol=simplestreams --public
  return 0
}
install_python() { [ -d venv ] || python3 -m venv venv; ./venv/bin/pip install -q --upgrade pip && ./venv/bin/pip install -q -r requirements.txt; }
install_services() {
  cat > /etc/systemd/system/ariznodes-netfix.service <<UNIT
[Unit]
Description=ArizNodes - let LXD containers reach the internet
After=network-online.target docker.service snap.lxd.daemon.service
Wants=network-online.target
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStartPre=-/snap/bin/lxd waitready --timeout 60
ExecStart=/bin/bash $DIR/netfix.sh --no-test
[Install]
WantedBy=multi-user.target
UNIT
  cat > /etc/systemd/system/ariznodes-vpsbot.service <<UNIT
[Unit]
Description=ArizNodesLabs VPS Deployer Bot v$VERSION
After=network-online.target snap.lxd.daemon.service ariznodes-netfix.service
Wants=network-online.target
[Service]
User=root
WorkingDirectory=$DIR
Environment=PATH=/snap/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=$DIR/venv/bin/python bot.py
Restart=on-failure
RestartSec=5
[Install]
WantedBy=multi-user.target
UNIT
  cp "$DIR/ariznodes-cli" /usr/local/bin/ariznodes && chmod +x /usr/local/bin/ariznodes
  systemctl daemon-reload && systemctl enable ariznodes-netfix ariznodes-vpsbot
}
start_bot() { systemctl restart ariznodes-vpsbot; for i in $(seq 1 25); do sleep 1; journalctl -u ariznodes-vpsbot -n 40 --no-pager 2>/dev/null | grep -q "Logged in as" && return 0; done; return 1; }
net_repair() { bash "$DIR/netfix.sh" >>"$LOGF" 2>&1; }

summary() {
  local P URL W=74 line; P=$(grep -E '^DASH_PORT=' .env | cut -d= -f2); P="${P:-8787}"; URL=$(grep -E '^DASH_URL=' .env | cut -d= -f2-); line=$(printf '─%.0s' $(seq 1 $W))
  row() { local plain pad; plain=$(printf '%s' "$1" | sed 's/\x1b\[[0-9;]*m//g'); pad=$((W-2-${#plain})); [ $pad -lt 0 ] && pad=0; printf '%s│%s %s%*s %s│%s\n' "$O" "$N" "$1" "$pad" "" "$O" "$N"; }
  printf '\n%s╭%s╮%s\n' "$O" "$line" "$N"
  row "${B}ArizNodes v$VERSION is installed${N}   $( [ "$BOT_ONLINE" = 1 ] && echo "${G}● ONLINE${N}" || echo "${Y}○ not running yet${N}" )"
  printf '%s├%s┤%s\n' "$O" "$line" "$N"
  row "Control it with:  ariznodes status | logs | restart | doctor"
  row "Edit settings  :  ariznodes env      (then: ariznodes restart)"
  row "No VPS internet:  ariznodes netfix   (Docker / ufw / NAT repair)"
  if grep -qE "^(DISCORD_CLIENT_SECRET|DASH_PASSWORD)='.+'" .env; then
    printf '%s├%s┤%s\n' "$O" "$line" "$N"; row "${B}Website${N}   http://127.0.0.1:$P  ${D}(this server)${N}"
    [ -n "$URL" ] && row "Public URL  $URL"
    row "Discord → OAuth2 → Redirects → add:"; row "   ${URL:-https://YOUR-DOMAIN}/auth/callback"
    row "Cloudflare Tunnel → service URL:  http://localhost:$P  (type HTTP)"
    [ "$GENPASS" = 1 ] && row "${Y}Admin password:${N} ${B}$DASHPASS${N}   ${D}(also saved in .env)${N}"
  fi
  printf '%s╰%s╯%s\n\n' "$O" "$line" "$N"
  [ -z "$TOKEN" ] && warn "Bot token missing — run  ariznodes env  then  ariznodes restart"
  printf '  %sInvite the bot:%s https://discord.com/oauth2/authorize?client_id=%s&permissions=8&scope=bot%%20applications.commands\n' "$B" "$N" "${BOT_ID:-YOUR_APP_ID}"
  printf '  %sThen in Discord:%s  !help → !panel → !deploy   %s(turn on "Message Content Intent" in Developer Portal → Bot)%s\n\n' "$B" "$N" "$D" "$N"
}

# ───────────────────────── main ─────────────────────────
[ "$MODE" = "--help" ] && { sed -n '2,7p' "$0"; exit 0; }
banner
case "$MODE" in
  --doctor) write_files >/dev/null 2>&1; bash doctor.sh; exit $? ;;
  --fix-network) [ "$(id -u)" = 0 ] || die "Run as root"; write_files >/dev/null 2>&1; bash netfix.sh; exit $? ;;
  --files-only) step 1 2 "Writing files"; write_files; ok "bot.py, requirements.txt, netfix.sh, doctor.sh written"; step 2 2 "Settings"; configure; write_env; ok ".env written (permissions 600)"; summary; exit 0 ;;
  auto) if [ -f .env ] && [ -f bot.py ]; then MODE=--upgrade; else MODE=--install; fi ;;
esac
[ "$(id -u)" = 0 ] || die "Please run as root:  sudo bash $0"
command -v apt-get >/dev/null 2>&1 || die "This installer supports Debian/Ubuntu servers (apt)."
VIRT="$(systemd-detect-virt 2>/dev/null)"; case "$VIRT" in openvz|lxc) warn "This server is a '$VIRT' container — LXD usually cannot run inside it. A KVM VPS or dedicated server is required.";; esac
command -v docker >/dev/null 2>&1 && info "Docker detected — the network repair step will make LXD and Docker coexist."

if [ "$MODE" = "--install" ]; then
  T=8; step 1 $T "Writing bot files"; write_files; ok "files written to $DIR"
  step 2 $T "Your settings"; configure; write_env; ok ".env saved (permissions 600)"
  step 3 $T "System packages"; run "Installing Python, git, ssh client, iptables, snapd" install_packages || exit 1
  step 4 $T "LXD container engine"; run "Installing & initialising LXD (this can take a few minutes)" install_lxd || exit 1; run "Checking LXD storage, network & image remotes" fix_lxd_profile || warn "LXD profile needs attention — run: ariznodes doctor"
  step 5 $T "Container internet"; if run "Repairing firewall/NAT and testing a container" net_repair; then :; else warn "Containers still have no internet — see: ariznodes netfix"; fi
  step 6 $T "Python environment"; run "Creating venv & installing discord.py, aiohttp, psutil" install_python || exit 1
  step 7 $T "Services"; run "Registering systemd services & the 'ariznodes' command" install_services || exit 1
  step 8 $T "Starting"
  if [ -n "$TOKEN" ]; then if run "Starting the bot and waiting for Discord" start_bot; then BOT_ONLINE=1; else bad "Bot did not come online — last log lines:"; journalctl -u ariznodes-vpsbot -n 8 --no-pager | sed 's/^/      /'; fi; else info "Skipped — no token yet"; fi
  summary
elif [ "$MODE" = "--upgrade" ]; then
  T=5; step 1 $T "Updating files"; [ -f bot.py ] && cp bot.py "bot.py.bak-$(date +%s)" && info "old bot.py backed up"; write_files; ok "new files written"
  step 2 $T "Settings"; upgrade_env; ok ".env kept — new options added"
  step 3 $T "Python environment"; run "Updating dependencies" install_python || exit 1
  step 4 $T "Services & network"; run "Updating systemd units & CLI" install_services || exit 1; run "Repairing firewall/NAT for containers" net_repair || warn "Containers may still lack internet — run: ariznodes netfix"
  step 5 $T "Restarting"; if run "Restarting the bot" start_bot; then BOT_ONLINE=1; else bad "Bot did not come online — run: ariznodes logs"; fi
  TOKEN="x"; summary
else die "Unknown option $MODE (try --help)"; fi
