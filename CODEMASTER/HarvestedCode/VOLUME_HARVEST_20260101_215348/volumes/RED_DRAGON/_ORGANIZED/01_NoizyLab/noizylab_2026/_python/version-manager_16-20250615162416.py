# Creation time: 15-06-25_16-27
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 6
PythonBatchCommandBase.running_progress = 0
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()


with PythonBatchRuntime(r"exec", prog_num=1):
    with Stage(r"doit", prog_num=2):
        with ShellCommand(r"'/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility' -s", ignore_all_errors=True, prog_num=3) as shell_command_001_3:
            shell_command_001_3()
        with ShellCommand(r"'/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility' -s", ignore_all_errors=True, prog_num=4) as shell_command_002_4:
            shell_command_002_4()

with Stage(r"epilog", prog_num=5):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/versionManager/version-manager_16-20250615162416.py", prog_num=6) as patch_py_batch_with_timings_003_6:
        patch_py_batch_with_timings_003_6()

log.info("Shakespeare says: All's Well That Ends Well")
# eof

