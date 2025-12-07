from qdrant_client import AsyncQdrantClient
from BASE.utils.path_selector import PathSelector
from BASE.utils.platform_detector import PlatformDetector
import requests
from time import sleep
from ipc import IPC

ipc_ = IPC.connect()


import subprocess
def start_qdrant_server():
    qdrant_process = subprocess.Popen([
        PathSelector.get_base_path() / "qdrant.exe" if PlatformDetector.is_windows() else PathSelector.get_base_path() / "qdrant",
        "--config-path", PathSelector.get_base_path() / "qdrant_config.yaml"
    ])

    # BEFORE RETURNING, WAIT FOR THE SERVER TO START
    while True:
        resp = requests.get("http://127.0.0.1:45225/")
        if resp.status_code == 200:
            ipc_.set("qdrant_ready", True)
            break
        else:
            print("Waiting for Qdrant server to start...")
            sleep(3)
            continue

    return qdrant_process


def get_qdrant_client():
    qdrant_client = AsyncQdrantClient(
        host="127.0.0.1", 
        port=45225, 
        grpc_port=45226, 
        prefer_grpc=True
    )

    return qdrant_client

def get_inmemory_client():
    return AsyncQdrantClient(":memory:")