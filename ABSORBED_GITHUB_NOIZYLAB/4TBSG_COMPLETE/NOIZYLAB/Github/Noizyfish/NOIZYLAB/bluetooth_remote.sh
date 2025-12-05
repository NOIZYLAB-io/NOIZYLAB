#!/bin/zsh
# Bluetooth Remote Utility for macOS
# Lists paired and connected Bluetooth devices, and can disconnect or connect by name

list_devices() {
    echo "Paired Bluetooth Devices:"
    system_profiler SPBluetoothDataType | grep -A 20 'Devices (Paired, Configured, etc.):' | grep 'Name:'
    echo
    echo "Connected Bluetooth Devices:"
    system_profiler SPBluetoothDataType | grep 'Connected: Yes' -B 2 | grep 'Name:'
}

connect_device() {
    device_name="$1"
    echo "Connecting to $device_name (manual interaction may be required)..."
    # macOS does not provide a native CLI to connect, so this is a placeholder
    echo "Please connect using the Bluetooth menu or System Settings."
}

disconnect_device() {
    device_name="$1"
    echo "Disconnecting $device_name (manual interaction may be required)..."
    # macOS does not provide a native CLI to disconnect, so this is a placeholder
    echo "Please disconnect using the Bluetooth menu or System Settings."
}

case "$1" in
    list)
        list_devices
        ;;
    connect)
        connect_device "$2"
        ;;
    disconnect)
        disconnect_device "$2"
        ;;
    *)
        echo "Usage: $0 {list|connect <DeviceName>|disconnect <DeviceName>}"
        ;;
esac
