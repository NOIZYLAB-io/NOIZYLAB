# Creation time: 12-07-25_16-37
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 22
PythonBatchCommandBase.running_progress = 6
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=7):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = 20
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = 501
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250712163741"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"16.0.5"
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['CURRENT_DOIT_DESCRIPTION'] = r"Doing it"
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+", r"Clean_old_plist_Native_NI")
    config_vars['EXIT_ON_EXEC_EXCEPTION'] = r"False"
    config_vars['FIX_ALL_PERMISSIONS_SYMBOLIC_MODE'] = r"u+rwx,go+rx"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['MAIN_DOIT_ITEMS'] = r"STOP_SERVERS"
    config_vars['MAIN_INSTALL_TARGETS'] = r"STOP_SERVERS"
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 0
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 0
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/doit-output-16-20250712163741.log"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlDoIt.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/Unload-Running-Processes.yaml")
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"$(REPO_NAME)_repo_rev.yaml"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"$(REPO_NAME)_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 12
    config_vars['WAVES_DIR'] = r"/Applications/Waves"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WLE_EXEC_PATH'] = r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"doit", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/doit-output-16-20250712163741.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"activate-repo-rev", r"check-checksum", r"check-instl-folder-integrity", r"checksum", r"collect-manifests", r"command-list", r"copy", r"depend", r"doit", r"dump-config-vars", r"exec", r"fail", r"file-sizes", r"fix-perm", r"fix-props", r"fix-symlinks", r"gui", r"help", r"ls", r"parallel-run", r"read-info-map", r"read-yaml", r"remove", r"report-versions", r"resolve", r"run-process", r"short-index", r"stage2svn", r"svn2stage", r"sync", r"synccopy", r"test-import", r"translate-guids", r"translate_url", r"uninstall", r"unwtar", r"up-short-index", r"up2s3", r"verify-index", r"verify-repo", r"version", r"wait-on-action-trigger", r"wtar", r"wtar-staging-folder", r"wzip")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DOIT_TARGETS__'] = r"STOP_SERVERS"
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 0
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"yqdheojwsdgdqogg"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"doit"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.yaml"
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.py"
    config_vars['__NOW__'] = r"2025-07-12 16:37:41.801464"
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses", r"/Applications/Waves Central.app/Contents/Resources/res/external/data")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"BM-MAC-ADO6"
    config_vars['__SQLITE_VERSION__'] = r"3.45.1"
    config_vars['__SUDO_USER__'] = r"no set"
    config_vars['__SYSTEM_LOG_FILE_PATH__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/instl/instl.log"
    config_vars['__USER_CONFIG_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_CONFIG_FILE_NAME__'] = r"instl_config.yaml"
    config_vars['__USER_CONFIG_FILE_PATH__'] = r"/Users/rsp_ms/instl_config.yaml"
    config_vars['__USER_DATA_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_DESKTOP_DIR__'] = r"/Users/rsp_ms/Desktop"
    config_vars['__USER_HOME_DIR__'] = r"/Users/rsp_ms"
    config_vars['__USER_ID__'] = 0

with PythonBatchRuntime(r"doit", prog_num=8):
    with Stage(r"begin", prog_num=9):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre_doit", prog_num=10):
        pass
    with Stage(r"doit", prog_num=11):
        with Stage(r"Shutting down servers...", prog_num=12):
            # --- Begin STOP_SERVERS Shutting down servers
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=13) as shell_command_001_13:
                shell_command_001_13()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=14) as shell_command_002_14:
                shell_command_002_14()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=15) as shell_command_003_15:
                shell_command_003_15()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.1", ignore_all_errors=True, prog_num=16) as shell_command_004_16:
                shell_command_004_16()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=17) as shell_command_005_17:
                shell_command_005_17()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=18) as shell_command_006_18:
                shell_command_006_18()
            with If(IsFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient"), if_true=ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop Waves Local Client", suspend=5), ignore_all_errors=True, prog_num=19) as if_007_19:
                if_007_19()
            # --- End STOP_SERVERS Shutting down servers
    with Stage(r"post_doit", prog_num=20):
        print("Done Doing it")

with Stage(r"epilog", prog_num=21):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/unload_running_processes_16-20250712163741.py", prog_num=22) as patch_py_batch_with_timings_008_22:
        patch_py_batch_with_timings_008_22()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


