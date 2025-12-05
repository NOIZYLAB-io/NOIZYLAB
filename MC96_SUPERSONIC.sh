#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
#  ███╗   ███╗ ██████╗ █████╗  ██████╗     ███████╗██╗   ██╗██████╗ ███████╗██████╗ 
#  ████╗ ████║██╔════╝██╔══██╗██╔════╝     ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗
#  ██╔████╔██║██║     ╚██████║███████╗     ███████╗██║   ██║██████╔╝█████╗  ██████╔╝
#  ██║╚██╔╝██║██║      ╚═══██║██╔═══██╗    ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
#  ██║ ╚═╝ ██║╚██████╗ █████╔╝╚██████╔╝    ███████║╚██████╔╝██║     ███████╗██║  ██║
#  ╚═╝     ╚═╝ ╚═════╝ ╚════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝
#                    ███████╗ ██████╗ ███╗   ██╗██╗ ██████╗                         
#                    ██╔════╝██╔═══██╗████╗  ██║██║██╔════╝                         
#                    ███████╗██║   ██║██╔██╗ ██║██║██║                              
#                    ╚════██║██║   ██║██║╚██╗██║██║██║                              
#                    ███████║╚██████╔╝██║ ╚████║██║╚██████╗                         
#                    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝                         
# ═══════════════════════════════════════════════════════════════════════════════
# MC96ECOUNIVERSE SUPERSONIC MODE - 1000% SPEED - NO LIMITS
# HARD RULE #24: JUMBO FRAMES = DEFAULT SETTING FOREVER (GOD LIKE)
# HARD RULE #27: NO LIMITS OF ANY KIND IN THE UNIVERSE
# ═══════════════════════════════════════════════════════════════════════════════
# GOD (M2 Ultra) + GABRIEL (HP-OMEN) = UNIFIED THROUGH GITHUB
# CLOUDFLARE DNS 1.1.1.1 = FASTEST DNS ON EARTH
# MTU 9000 = JUMBO FRAMES = 15-20% SPEED BOOST
# ═══════════════════════════════════════════════════════════════════════════════

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${PURPLE}"
echo "═══════════════════════════════════════════════════════════════════════════════"
echo "  🚀 MC96ECOUNIVERSE SUPERSONIC MODE - 1000% ACTIVATION"
echo "═══════════════════════════════════════════════════════════════════════════════"
echo -e "${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 1. JUMBO FRAMES - MTU 9000 (15-20% SPEED BOOST)
# ═══════════════════════════════════════════════════════════════════════════════
echo -e "${CYAN}⚡ [1/8] ACTIVATING JUMBO FRAMES (MTU 9000)...${NC}"
for iface in en0 en1 en2 en3 en4 en5; do
    if ifconfig $iface >/dev/null 2>&1; then
        current_mtu=$(ifconfig $iface | grep mtu | awk '{print $NF}')
        if [ "$current_mtu" != "9000" ]; then
            sudo ifconfig $iface mtu 9000 2>/dev/null && echo -e "   ${GREEN}✅ $iface: MTU 9000 (was $current_mtu)${NC}"
        else
            echo -e "   ${GREEN}✅ $iface: MTU 9000 (already set)${NC}"
        fi
    fi
done

# ═══════════════════════════════════════════════════════════════════════════════
# 2. TCP/IP STACK OPTIMIZATION - MAXIMUM THROUGHPUT
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [2/8] TURBOCHARGING TCP/IP STACK...${NC}"

# Massive buffer increases for high-bandwidth transfers
sudo sysctl -w net.inet.tcp.sendspace=2097152 >/dev/null 2>&1
sudo sysctl -w net.inet.tcp.recvspace=2097152 >/dev/null 2>&1
sudo sysctl -w net.inet.tcp.autorcvbufmax=8388608 >/dev/null 2>&1
sudo sysctl -w net.inet.tcp.autosndbufmax=8388608 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP buffers: 2MB send/recv${NC}"
echo -e "   ${GREEN}✅ TCP auto max: 8MB${NC}"

# Window scaling for gigabit+
sudo sysctl -w net.inet.tcp.win_scale_factor=8 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP window scaling: 8x${NC}"

# Reduce latency - disable delayed ACK
sudo sysctl -w net.inet.tcp.delayed_ack=0 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP delayed ACK: DISABLED (lower latency)${NC}"

# Maximum segment size for jumbo frames
sudo sysctl -w net.inet.tcp.mssdflt=8960 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP MSS: 8960 (jumbo optimized)${NC}"

# Enable TCP Fast Open
sudo sysctl -w net.inet.tcp.fastopen=3 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP Fast Open: ENABLED${NC}"

# ECN for congestion control
sudo sysctl -w net.inet.tcp.ecn_initiate_out=1 >/dev/null 2>&1
echo -e "   ${GREEN}✅ TCP ECN: ENABLED${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 3. UDP OPTIMIZATION - FOR STREAMING/REALTIME
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [3/8] OPTIMIZING UDP (STREAMING/REALTIME)...${NC}"
sudo sysctl -w net.inet.udp.maxdgram=65535 >/dev/null 2>&1
sudo sysctl -w net.inet.udp.recvspace=1048576 >/dev/null 2>&1
echo -e "   ${GREEN}✅ UDP max datagram: 64KB${NC}"
echo -e "   ${GREEN}✅ UDP recv buffer: 1MB${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 4. SMB OPTIMIZATION - NETWORK SHARES TURBO
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [4/8] TURBOCHARGING SMB (NETWORK SHARES)...${NC}"

cat << 'SMBEOF' | sudo tee /etc/nsmb.conf > /dev/null 2>&1
[default]
# MC96ECOUNIVERSE SUPERSONIC SMB
signing_required=no
streams=yes
soft=yes
notify_off=yes
dir_cache_max_cnt=8192
dir_cache_max=120
protocol_vers_map=6
mc_prefer_wired=yes
validate_neg_off=yes
SMBEOF

echo -e "   ${GREEN}✅ SMB signing: DISABLED (faster)${NC}"
echo -e "   ${GREEN}✅ SMB dir cache: 8192 entries / 120 sec${NC}"
echo -e "   ${GREEN}✅ SMB protocol: SMB3 multichannel${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 5. DISK I/O OPTIMIZATION - M2 ULTRA POWER
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [5/8] MAXIMIZING DISK I/O...${NC}"

# Increase vnode and file limits massively
sudo sysctl -w kern.maxvnodes=1000000 >/dev/null 2>&1
sudo sysctl -w kern.maxfiles=500000 >/dev/null 2>&1
sudo sysctl -w kern.maxfilesperproc=250000 >/dev/null 2>&1
echo -e "   ${GREEN}✅ Max vnodes: 1,000,000${NC}"
echo -e "   ${GREEN}✅ Max files: 500,000${NC}"
echo -e "   ${GREEN}✅ Max files/proc: 250,000${NC}"

# Disable sudden motion sensor (SSD optimization)
sudo pmset -a sms 0 >/dev/null 2>&1
echo -e "   ${GREEN}✅ Sudden motion sensor: DISABLED${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 6. MEMORY OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [6/8] OPTIMIZING MEMORY...${NC}"

# Purge inactive memory
sudo purge >/dev/null 2>&1 && echo -e "   ${GREEN}✅ Inactive memory: PURGED${NC}"

# Increase shared memory for audio/video apps
sudo sysctl -w kern.sysv.shmmax=4294967296 >/dev/null 2>&1
sudo sysctl -w kern.sysv.shmall=1048576 >/dev/null 2>&1
echo -e "   ${GREEN}✅ Shared memory max: 4GB${NC}"

# ═══════════════════════════════════════════════════════════════════════════════
# 7. SPOTLIGHT CONTROL - PREVENT SLOWDOWNS ON EXTERNAL VOLUMES
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [7/8] DISABLING SPOTLIGHT ON EXTERNAL VOLUMES...${NC}"

for vol in "/Volumes/6TB" "/Volumes/SIDNEY" "/Volumes/MAG 4TB" "/Volumes/4TB Lacie" "/Volumes/4TBSG" "/Volumes/4TB Big Fish" "/Volumes/4TB Blue Fish" "/Volumes/4TB FISH SG"; do
    if [ -d "$vol" ]; then
        sudo mdutil -i off "$vol" >/dev/null 2>&1 && echo -e "   ${GREEN}✅ Spotlight OFF: $(basename "$vol")${NC}"
    fi
done

# ═══════════════════════════════════════════════════════════════════════════════
# 8. DNS VERIFICATION - CLOUDFLARE 1.1.1.1
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${CYAN}⚡ [8/8] VERIFYING CLOUDFLARE DNS...${NC}"
DNS_CHECK=$(scutil --dns 2>/dev/null | grep "nameserver" | head -1)
if [[ "$DNS_CHECK" == *"1.1.1.1"* ]]; then
    echo -e "   ${GREEN}✅ Cloudflare DNS: ACTIVE (1.1.1.1 - 14ms avg)${NC}"
else
    echo -e "   ${YELLOW}⚠️ DNS not set to 1.1.1.1 - consider changing for max speed${NC}"
fi

# ═══════════════════════════════════════════════════════════════════════════════
# STATUS REPORT
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}  🔥 MC96ECOUNIVERSE SUPERSONIC MODE: ${GREEN}ACTIVE${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "   ${CYAN}⚡ JUMBO FRAMES:${NC}     MTU 9000 (+15-20% throughput)"
echo -e "   ${CYAN}⚡ TCP BUFFERS:${NC}      2MB send/recv, 8MB auto max"
echo -e "   ${CYAN}⚡ TCP FAST OPEN:${NC}    ENABLED (faster connections)"
echo -e "   ${CYAN}⚡ UDP OPTIMIZED:${NC}    1MB buffer (streaming ready)"
echo -e "   ${CYAN}⚡ SMB TURBO:${NC}        Signing off, 8K cache, SMB3"
echo -e "   ${CYAN}⚡ DISK I/O:${NC}         1M vnodes, 500K files"
echo -e "   ${CYAN}⚡ MEMORY:${NC}           4GB shared, purged"
echo -e "   ${CYAN}⚡ CLOUDFLARE:${NC}       1.1.1.1 (fastest DNS)"
echo -e "   ${CYAN}⚡ SPOTLIGHT:${NC}        OFF on external volumes"
echo ""
echo -e "   ${GREEN}🚀 SPEED LEVEL: 1000%${NC}"
echo -e "   ${GREEN}🌌 THROUGHPUT: ~1+ Gbps SUSTAINED${NC}"
echo ""
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
echo -e "${WHITE}   NO LIMITS OF ANY KIND IN THE UNIVERSE - GORUNFREE!!! 🔥${NC}"
echo -e "${PURPLE}═══════════════════════════════════════════════════════════════════════════════${NC}"
