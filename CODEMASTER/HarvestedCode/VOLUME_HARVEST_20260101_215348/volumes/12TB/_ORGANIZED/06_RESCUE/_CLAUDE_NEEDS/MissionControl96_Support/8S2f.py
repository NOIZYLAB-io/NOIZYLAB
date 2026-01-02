chmod +x ~/Documents/NoizyFish/BigBubba/agents/keyboard_flash_bubba.sh
~/Documents/NoizyFish/BigBubba/agents/keyboard_flash_bubba.sh
ioreg -p IOUSB -l -w 0 | grep -E '"USB Vendor Name"|"USB Product Name"|"idVendor"|"idProduct"'