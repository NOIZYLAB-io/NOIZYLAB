#!/bin/bash

# ===================================
# Auto-mount Windows share from GABRIEL
# ===================================

PC_IP="192.168.1.24"
PC_USER="rsp_ms"
SHARE_NAME="SharedMusic"
MOUNT_POINT="/Volumes/${SHARE_NAME}"

# Check if PC is reachable
ping -c 1 -W 1 $PC_IP > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "PC ($PC_IP) is offline. Skipping mount."
    exit 0
fi

# Create the mount directory if missing
if [ ! -d "$MOUNT_POINT" ]; then
    mkdir -p "$MOUNT_POINT"
fi

# If already mounted, skip
mount | grep "on ${MOUNT_POINT}" > /dev/null
if [ $? -eq 0 ]; then
    echo "Already mounted at ${MOUNT_POINT}"
    exit 0
fi

# Mount using SMB (pulls password from Keychain)
mount_smbfs //$PC_USER@$PC_IP/$SHARE_NAME $MOUNT_POINT

# Confirm
if mount | grep "on ${MOUNT_POINT}" > /dev/null; then
    echo "Mounted successfully at ${MOUNT_POINT}"
else
    echo "Mount failed — check SMB path or credentials."
fi
