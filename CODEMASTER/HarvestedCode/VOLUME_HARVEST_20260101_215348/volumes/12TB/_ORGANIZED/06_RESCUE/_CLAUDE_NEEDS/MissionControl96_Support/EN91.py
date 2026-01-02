import psutil, subprocess, os, time
from uap.protocol import UapEvent, Signer; import requests
SIG=os.getenv("MESH_SHARED_SECRET","changeme")
BASE=f"http://{os.getenv('NOIZY_BIND','127.0.0.1')}:{os.getenv('UAP_WS_PORT','8123')}"
signer=Signer(SIG)
def make_agent(bus=None):
    def run():
        cpu=psutil.cpu_percent()
        if cpu>75:
            subprocess.Popen(["python","services/mind.py"])
            body=UapEvent(topic="autoscale",payload={"spawned":True,"cpu":cpu}).to_json()
            requests.post(BASE+"/uap/publish",data=body,headers={"x-uap-signature":signer.sign(body)},timeout=1)
    return run