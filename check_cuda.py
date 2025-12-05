import subprocess
from ipc import IPC

ipc_ = IPC.connect()

def cuda_available():
    # Check for nvidia-smi
    try:
        output = subprocess.check_output(['nvidia-smi'], stderr=subprocess.STDOUT)
        return True
    except Exception:
        pass
    # Check if nvcc is installed (CUDA toolkit)
    try:
        output = subprocess.check_output(['nvcc', '--version'], stderr=subprocess.STDOUT)
        return True
    except Exception:
        pass
    return False

if cuda_available():
    ipc_.set("cuda_available", True)
else:
    ipc_.set("cuda_available", False)