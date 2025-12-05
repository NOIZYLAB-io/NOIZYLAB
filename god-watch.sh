#!/bin/bash
# GOD Performance Watch - Ultra-Fast Monitoring
# CB_01 - Fish Music Inc
# GORUNFREE! 🎸🔥

watch -n 2 -c 'clear && echo -e "\033[1;35m⚡ GOD LIVE STATUS\033[0m" && echo "" && echo -e "\033[1;36mCPU:\033[0m" && top -l 1 -o cpu -n 3 | tail -4 && echo "" && echo -e "\033[1;36mMEMORY:\033[0m $(( $(sysctl -n hw.memsize) / 1024 / 1024 / 1024 ))GB total" && vm_stat | head -5 && echo "" && echo -e "\033[1;36mDISK:\033[0m" && df -h / | tail -1 && echo "" && echo -e "\033[1;35mGORUNFREE! 🎸🔥\033[0m"'
