from functorch import dim
# Example: create a tensor and use dim functions
import torch

x = torch.randn(3, 4)
# Use dim functionality (replace with actual usage)
# result = dim.some_function(x)

import subprocess

def get_usb_devices():
    cmd = 'ioreg -p IOUSB -l -w 0'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if any(key in line for key in ['USB Vendor Name', 'USB Product Name', 'idVendor', 'idProduct']):
            print(line)

get_usb_devices()