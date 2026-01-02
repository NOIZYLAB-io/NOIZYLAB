import torch
from functorch import dim
import subprocess

# Example tensor operation (customize as needed)
x = torch.randn(3, 4)
# result = dim.some_function(x)  # Replace with actual functorch usage

def get_usb_keyboards():
    cmd = 'ioreg -p IOUSB -l -w 0'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.splitlines()
    keyboard_info = []
    current_device = {}
    for line in lines:
        if '"USB Vendor Name"' in line:
            current_device['vendor'] = line.split('=')[-1].strip().strip('"')
        if '"USB Product Name"' in line:
            current_device['product'] = line.split('=')[-1].strip().strip('"')
        if '"idVendor"' in line:
            current_device['vid'] = line.split('=')[-1].strip()
        if '"idProduct"' in line:
            current_device['pid'] = line.split('=')[-1].strip()
        # If we have both vendor and product, check if it's a keyboard
        if 'vendor' in current_device and 'product' in current_device:
            if any(k in current_device['product'].lower() for k in ['keyboard', 'keychron', 'logitech', 'razer', 'corsair', 'ducky']):
                keyboard_info.append(current_device.copy())
            current_device = {}
    return keyboard_info

keyboards = get_usb_keyboards()
if keyboards:
    print("Detected USB keyboards:")
    for kb in keyboards:
        print(f"Vendor: {kb.get('vendor', '')}, Product: {kb.get('product', '')}, VID:PID={kb.get('vid', '')}:{kb.get('pid', '')}")
    # Here you could add code to manipulate the keyboard, e.g., call QMK Toolbox or other firmware tools
else:
    print("No USB keyboards detected. Make sure your keyboard is connected via USB.")

# Next steps: You can add code here to flash firmware, send commands, or configure your keyboard using detected VID/PID.