#!/bin/bash
# Quick access to all major functions

CODE_MASTER="/Volumes/4TB_02/CODE_MASTER"

case "$1" in
    start|s) bash "$CODE_MASTER/WARP_SPEED_START.sh" ;;
    heal|h) bash "$CODE_MASTER/scripts/AUTOHEAL_WARP_SPEED_X1000.sh" ;;
    upgrade|u) bash "$CODE_MASTER/scripts/HYPER_DRIVE_UPGRADE_X1000.sh" ;;
    optimize|o) bash "$CODE_MASTER/scripts/ADVANCED_OPTIMIZER_X1000.sh" ;;
    status|st) df -h / && df -h /Volumes/4TB_02 2>/dev/null ;;
    *) echo "Usage: $0 {start|heal|upgrade|optimize|status}" ;;
esac
