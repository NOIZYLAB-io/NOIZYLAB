# Creation time: 20-01-25_14-26
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 4
PythonBatchCommandBase.running_progress = 0
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()


with PythonBatchRuntime(r"exec", prog_num=1):  # 0m:0.000s
    with Stage(r"doit", prog_num=2):  # 0m:0.000s
        pass

with Stage(r"epilog", prog_num=3):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/versionManager/version-manager_15-20250120142650.py", prog_num=4) as patch_py_batch_with_timings_001_4:  # ?
        patch_py_batch_with_timings_001_4()

log.info("Shakespeare says: All's Well That Ends Well")
# eof

# doit time 0m:0.000s
