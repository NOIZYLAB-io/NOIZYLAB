#!/usr/bin/env python3
# Creation time: 20-01-25_14-25
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 105
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
    config_vars['ACTION_ID'] = r"15-20250120142536"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.3.3"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['CURRENT_DOIT_DESCRIPTION'] = r"Doing it"
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+")
    config_vars['EXIT_ON_EXEC_EXCEPTION'] = r"False"
    config_vars['FIX_ALL_PERMISSIONS_SYMBOLIC_MODE'] = r"u+rwx,go+rx"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAIN_DOIT_ITEMS'] = (r"STOP_SERVERS", r"CLEAN_WAVES_PROGRAMDATA_DIR", r"CLEAN_USER_CACHE_DIR", r"CLEAN_WAVES_CACHE_DIR", r"CLEAN_REWIRE_DIR", r"CLEAN_WAVES_SOUNDGRID_FOR_VENUE_DIR", r"CLEAN_SHELLS_DIR", r"CLEAN_PLUGINS_DIR", r"CLEAN_WAVES_SESSION_FILES", r"CLEAN_WAVES_APPLICATIONS_DIR", r"CLEAN_WAVES_SOUNDGRID_STUDIO_DIR", r"CLEAN_WAVES_EMOTION_LV1_DIR", r"CLEAN_WAVES_NDI_DIR", r"CLEAN_WAVES_SUPERRACK_DIR", r"CLEAN_WAVES_MULTIRACK_DIR", r"CLEAN_WAVES_SOUNDGRID_QREC_DIR", r"CLEAN_WAVES_COSMOS_DIR", r"CLEAN_WAVES_DATA_DIR", r"CLEAN_WAVES_PREFERENCES_DIR", r"CLEAN_WAVES_LOCAL_SERVER_DIR", r"CLEAN_WAVES_LOCAL_USER_WAVES_DIR", r"CLEAN_USER_WAVES_DIR", r"CLEAN_WAVES_WPAPI_DIR", r"CLEAN_WAVESHELL_AAX_DIR", r"CLEAN_MACOS_WAVESHELL_AU_DIR", r"CLEAN_WAVESHELL_VST_DIR", r"CLEAN_WAVESHELL_VST3_DIR", r"CLEAN_WIN_WAVESHELL_DAE_DIR", r"CLEAN_NATIVE_INSTRUMENTS_DIR", r"CLEAN_WAVES_SOUNDGRID_DIR", r"CLEAN_NI_PLIST_FILES", r"CLEAN_WIN_STARTUP_DIR", r"CLEAN_WIN_DESKTOP_DIR", r"CLEAN_LAUNCH_AGENTS_DIR", r"CLEAN_COSMOS_FILES", r"CLEAN_SOUNDGRID_RELATED_FILES")
    config_vars['MAIN_INSTALL_TARGETS'] = (r"STOP_SERVERS", r"CLEAN_WAVES_PROGRAMDATA_DIR", r"CLEAN_USER_CACHE_DIR", r"CLEAN_WAVES_CACHE_DIR", r"CLEAN_REWIRE_DIR", r"CLEAN_WAVES_SOUNDGRID_FOR_VENUE_DIR", r"CLEAN_SHELLS_DIR", r"CLEAN_PLUGINS_DIR", r"CLEAN_WAVES_SESSION_FILES", r"CLEAN_WAVES_APPLICATIONS_DIR", r"CLEAN_WAVES_SOUNDGRID_STUDIO_DIR", r"CLEAN_WAVES_EMOTION_LV1_DIR", r"CLEAN_WAVES_NDI_DIR", r"CLEAN_WAVES_SUPERRACK_DIR", r"CLEAN_WAVES_MULTIRACK_DIR", r"CLEAN_WAVES_SOUNDGRID_QREC_DIR", r"CLEAN_WAVES_COSMOS_DIR", r"CLEAN_WAVES_DATA_DIR", r"CLEAN_WAVES_PREFERENCES_DIR", r"CLEAN_WAVES_LOCAL_SERVER_DIR", r"CLEAN_WAVES_LOCAL_USER_WAVES_DIR", r"CLEAN_USER_WAVES_DIR", r"CLEAN_WAVES_WPAPI_DIR", r"CLEAN_WAVESHELL_AAX_DIR", r"CLEAN_MACOS_WAVESHELL_AU_DIR", r"CLEAN_WAVESHELL_VST_DIR", r"CLEAN_WAVESHELL_VST3_DIR", r"CLEAN_WIN_WAVESHELL_DAE_DIR", r"CLEAN_NATIVE_INSTRUMENTS_DIR", r"CLEAN_WAVES_SOUNDGRID_DIR", r"CLEAN_NI_PLIST_FILES", r"CLEAN_WIN_STARTUP_DIR", r"CLEAN_WIN_DESKTOP_DIR", r"CLEAN_LAUNCH_AGENTS_DIR", r"CLEAN_COSMOS_FILES", r"CLEAN_SOUNDGRID_RELATED_FILES")
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NATIVE_INSTRUMENTS_DIR'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 0
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 0
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/doit-output-15-20250120142536.log"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlDoIt.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/cleanup.yaml")
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"$(REPO_NAME)_repo_rev.yaml"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"$(REPO_NAME)_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REWIRE_DIR'] = r"/Applications/Waves/ReWire"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SOUNDGRID_UNINSTALLER_FILE'] = r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app/Contents/MacOS//SoundGridDriverUninstaller.py"
    config_vars['SOUNDGRID_UNINSTALLER_PARENT_DIR'] = r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app/Contents/MacOS"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 95
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio"
    config_vars['USER_LOGS_FOLDER'] = r"/Users/rsp_ms/Library/Logs/Waves Audio"
    config_vars['USER_WAVES_DIR'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVES_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves"
    config_vars['WAVES_CENTRAL_EXTERNAL_DATA'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/data"
    config_vars['WAVES_COSMOS_DIR'] = r"/Applications/Waves/COSMOS"
    config_vars['WAVES_DATA_DIR'] = r"/Applications/Waves/Data"
    config_vars['WAVES_DIR'] = r"/Applications/Waves"
    config_vars['WAVES_EMOTION_LV1_DIR'] = r"/Applications/Waves/eMotion LV1"
    config_vars['WAVES_MULTIRACK_DIR'] = r"/Applications/Waves/MultiRack"
    config_vars['WAVES_PREFERENCES_DIR'] = r"/Users/rsp_ms/Library/Preferences/Waves Preferences"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WAVES_SHARED_FOLDER'] = r"/Users/Shared/Waves"
    config_vars['WAVES_SOUNDGRID_DIR'] = r"/Applications/Waves/SoundGrid"
    config_vars['WAVES_SOUNDGRID_FOR_VENUE_DIR'] = r"/Applications/Waves/SoundGrid for Venue"
    config_vars['WAVES_SOUNDGRID_QREC_DIR'] = r"/Applications/Waves/SoundGrid QRec"
    config_vars['WAVES_SOUNDGRID_STUDIO_DIR'] = r"/Applications/Waves/SoundGrid Studio"
    config_vars['WAVES_SUPERRACK_DIR'] = r"/Applications/Waves/SuperRack"
    config_vars['WAVES_WPAPI_DIR'] = r"/Library/Audio/Plug-Ins/WPAPI"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"doit", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/doit-output-15-20250120142536.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"activate-repo-rev", r"check-checksum", r"check-instl-folder-integrity", r"checksum", r"collect-manifests", r"command-list", r"copy", r"depend", r"doit", r"dump-config-vars", r"exec", r"fail", r"file-sizes", r"fix-perm", r"fix-props", r"fix-symlinks", r"gui", r"help", r"ls", r"parallel-run", r"read-info-map", r"read-yaml", r"remove", r"report-versions", r"resolve", r"run-process", r"short-index", r"stage2svn", r"svn2stage", r"sync", r"synccopy", r"test-import", r"translate-guids", r"translate_url", r"uninstall", r"unwtar", r"up-short-index", r"up2s3", r"verify-index", r"verify-repo", r"version", r"wait-on-action-trigger", r"wtar", r"wtar-staging-folder", r"wzip")
    config_vars['__COMPILATION_TIME__'] = r"2024-12-26 10:46:09.983540"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.2"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DOIT_TARGETS__'] = (r"STOP_SERVERS", r"CLEAN_WAVES_PROGRAMDATA_DIR", r"CLEAN_USER_CACHE_DIR", r"CLEAN_WAVES_CACHE_DIR", r"CLEAN_REWIRE_DIR", r"CLEAN_WAVES_SOUNDGRID_FOR_VENUE_DIR", r"CLEAN_SHELLS_DIR", r"CLEAN_PLUGINS_DIR", r"CLEAN_WAVES_SESSION_FILES", r"CLEAN_WAVES_APPLICATIONS_DIR", r"CLEAN_WAVES_SOUNDGRID_STUDIO_DIR", r"CLEAN_WAVES_EMOTION_LV1_DIR", r"CLEAN_WAVES_NDI_DIR", r"CLEAN_WAVES_SUPERRACK_DIR", r"CLEAN_WAVES_MULTIRACK_DIR", r"CLEAN_WAVES_SOUNDGRID_QREC_DIR", r"CLEAN_WAVES_COSMOS_DIR", r"CLEAN_WAVES_DATA_DIR", r"CLEAN_WAVES_PREFERENCES_DIR", r"CLEAN_WAVES_LOCAL_SERVER_DIR", r"CLEAN_WAVES_LOCAL_USER_WAVES_DIR", r"CLEAN_USER_WAVES_DIR", r"CLEAN_WAVES_WPAPI_DIR", r"CLEAN_WAVESHELL_AAX_DIR", r"CLEAN_MACOS_WAVESHELL_AU_DIR", r"CLEAN_WAVESHELL_VST_DIR", r"CLEAN_WAVESHELL_VST3_DIR", r"CLEAN_WIN_WAVESHELL_DAE_DIR", r"CLEAN_NATIVE_INSTRUMENTS_DIR", r"CLEAN_WAVES_SOUNDGRID_DIR", r"CLEAN_NI_PLIST_FILES", r"CLEAN_WIN_STARTUP_DIR", r"CLEAN_WIN_DESKTOP_DIR", r"CLEAN_LAUNCH_AGENTS_DIR", r"CLEAN_COSMOS_FILES", r"CLEAN_SOUNDGRID_RELATED_FILES")
    config_vars['__GITHUB_BRANCH__'] = r"python3.9"
    config_vars['__GROUP_ID__'] = 0
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.4.2.3 2024-12-26 10:46:09.983540 bm-mac4"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.4.2.3"
    config_vars['__INSTL_VERSION__'] = (2, 4, 2, 3)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"vxcutwritwfqobwo"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"doit"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.yaml"
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.py"
    config_vars['__NOW__'] = r"2025-01-20 14:25:37.326920"
    config_vars['__PLATFORM_NODE__'] = r"bm-mac4"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_COMPILER__'] = r"site-packages"
    config_vars['__PYTHON_VERSION__'] = (3, 9, 4, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup", r"/Applications/Waves Central.app/Contents/Resources/res/external/data")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"bm-mac4"
    config_vars['__SQLITE_VERSION__'] = r"3.34.0"
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
            with ShellCommand(r'launchctl unload "/Users/rsp_ms/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=13) as shell_command_001_13:
                shell_command_001_13()
            with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=14) as shell_command_002_14:
                shell_command_002_14()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=15) as shell_command_003_15:
                shell_command_003_15()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=16) as shell_command_004_16:
                shell_command_004_16()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=17) as shell_command_005_17:
                shell_command_005_17()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.1", ignore_all_errors=True, prog_num=18) as shell_command_006_18:
                shell_command_006_18()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.1", ignore_all_errors=True, prog_num=19) as shell_command_007_19:
                shell_command_007_19()
            with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=20) as shell_command_008_20:
                shell_command_008_20()
            with If(IsFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient"), if_true=ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop Waves Local Server", suspend=5), ignore_all_errors=True, prog_num=21) as if_009_21:
                if_009_21()
            # --- End STOP_SERVERS Shutting down servers
        with Stage(r"Clean main waves dir...", prog_num=22):
            # --- Begin CLEAN_WAVES_PROGRAMDATA_DIR Clean main waves dir
            with Glober(r"/Library/Application Support/Waves/*", RmFileOrDir, r"path", excludes=[r"Redis*"], prog_num=23) as glober_010_23:
                glober_010_23()
            # --- End CLEAN_WAVES_PROGRAMDATA_DIR Clean main waves dir
        with Stage(r"Clean /Users/rsp_ms/Library/Caches/Waves Audio...", prog_num=24):
            # --- Begin CLEAN_USER_CACHE_DIR Clean /Users/rsp_ms/Library/Caches/Waves Audio
            with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves Audio", prog_num=25) as rm_file_or_dir_011_25:
                rm_file_or_dir_011_25()
            # --- End CLEAN_USER_CACHE_DIR Clean /Users/rsp_ms/Library/Caches/Waves Audio
        with Stage(r"Clean waves cache dir...", prog_num=26):
            # --- Begin CLEAN_WAVES_CACHE_DIR Clean waves cache dir
            with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=27) as rm_file_or_dir_012_27:
                rm_file_or_dir_012_27()
            # --- End CLEAN_WAVES_CACHE_DIR Clean waves cache dir
        with Stage(r"Clean /Applications/Waves/ReWire...", prog_num=28):
            # --- Begin CLEAN_REWIRE_DIR Clean /Applications/Waves/ReWire
            with RmFileOrDir(r"/Applications/Waves/ReWire", prog_num=29) as rm_file_or_dir_013_29:
                rm_file_or_dir_013_29()
            # --- End CLEAN_REWIRE_DIR Clean /Applications/Waves/ReWire
        with Stage(r"Clean /Applications/Waves/SoundGrid for Venue...", prog_num=30):
            # --- Begin CLEAN_WAVES_SOUNDGRID_FOR_VENUE_DIR Clean /Applications/Waves/SoundGrid for Venue
            with RmFileOrDir(r"/Applications/Waves/SoundGrid for Venue", prog_num=31) as rm_file_or_dir_014_31:
                rm_file_or_dir_014_31()
            # --- End CLEAN_WAVES_SOUNDGRID_FOR_VENUE_DIR Clean /Applications/Waves/SoundGrid for Venue
        with Stage(r"Clean /Applications/Waves/WaveShells...", prog_num=32):
            # --- Begin CLEAN_SHELLS_DIR Clean /Applications/Waves/WaveShells
            with Glober(r"/Applications/Waves/WaveShells V*", RmFileOrDir, r"path", prog_num=33) as glober_015_33:
                glober_015_33()
            # --- End CLEAN_SHELLS_DIR Clean /Applications/Waves/WaveShells
        with Stage(r"Clean /Applications/Waves/Plug-Ins...", prog_num=34):
            # --- Begin CLEAN_PLUGINS_DIR Clean /Applications/Waves/Plug-Ins
            with Glober(r"/Applications/Waves/Plug-Ins V*", RmFileOrDir, r"path", prog_num=35) as glober_016_35:
                glober_016_35()
            with Glober(r"/Applications/Waves/Unused Plug-Ins V*", RmFileOrDir, r"path", prog_num=36) as glober_017_36:
                glober_017_36()
            # --- End CLEAN_PLUGINS_DIR Clean /Applications/Waves/Plug-Ins
        with Stage(r"Clean session files originated from /Users/Shared/Waves...", prog_num=37):
            # --- Begin CLEAN_WAVES_SESSION_FILES Clean session files originated from /Users/Shared/Waves
            with Glober(r"/Users/Shared/Waves/eMotion/Sessions/CurrentLV1.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=38) as glober_018_38:
                glober_018_38()
            with Glober(r"/Users/Shared/Waves/eMotion LV1 Native/Sessions/CurrentLV1Native.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=39) as glober_019_39:
                glober_019_39()
            with Glober(r"/Users/Shared/Waves/SuperRack SoundGrid/Sessions/CurrentSPRK.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=40) as glober_020_40:
                glober_020_40()
            with Glober(r"/Users/Shared/Waves/SuperRack/Sessions/CurrentSPRKN.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=41) as glober_021_41:
                glober_021_41()
            with Glober(r"/Users/Shared/Waves/SoundGrid Studio/Sessions/CurrentSGStudio.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=42) as glober_022_42:
                glober_022_42()
            with Glober(r"/Users/Shared/Waves/SoundGrid Inventory/Sessions/CurrentSoundGridForVenue.dat*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=43) as glober_023_43:
                glober_023_43()
            with Glober(r"/Users/Shared/Waves/*", RmSymlink, r"path", ignore_all_errors=True, prog_num=44) as glober_024_44:
                glober_024_44()
            # --- End CLEAN_WAVES_SESSION_FILES Clean session files originated from /Users/Shared/Waves
        with Stage(r"Clean /Applications/Waves/Applications...", prog_num=45):
            # --- Begin CLEAN_WAVES_APPLICATIONS_DIR Clean /Applications/Waves/Applications
            with Glober(r"/Applications/Waves/Applications V*", RmFileOrDir, r"path", prog_num=46) as glober_025_46:
                glober_025_46()
            with RmFileOrDir(r"/Applications/Waves/Applications", ignore_all_errors=True, prog_num=47) as rm_file_or_dir_026_47:
                rm_file_or_dir_026_47()
            # --- End CLEAN_WAVES_APPLICATIONS_DIR Clean /Applications/Waves/Applications
        with Stage(r"Clean /Applications/Waves/SoundGrid Studio...", prog_num=48):
            # --- Begin CLEAN_WAVES_SOUNDGRID_STUDIO_DIR Clean /Applications/Waves/SoundGrid Studio
            with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio", prog_num=49) as rm_file_or_dir_027_49:
                rm_file_or_dir_027_49()
            # --- End CLEAN_WAVES_SOUNDGRID_STUDIO_DIR Clean /Applications/Waves/SoundGrid Studio
        with Stage(r"Clean /Applications/Waves/eMotion LV1...", prog_num=50):
            # --- Begin CLEAN_WAVES_EMOTION_LV1_DIR Clean /Applications/Waves/eMotion LV1
            with Glober(r"/Applications/Waves/eMotion LV1*", RmFileOrDir, r"path", prog_num=51) as glober_028_51:
                glober_028_51()
            # --- End CLEAN_WAVES_EMOTION_LV1_DIR Clean /Applications/Waves/eMotion LV1
        with Stage(r"Clean ${WAVES_NDI_DIR}...", prog_num=52):
            # --- Begin CLEAN_WAVES_NDI_DIR Clean ${WAVES_NDI_DIR}
            with RmFileOrDir(r"/${WAVES_NDI_DIR}", prog_num=53) as rm_file_or_dir_029_53:
                rm_file_or_dir_029_53()
            # --- End CLEAN_WAVES_NDI_DIR Clean ${WAVES_NDI_DIR}
        with Stage(r"Clean /Applications/Waves/SuperRack...", prog_num=54):
            # --- Begin CLEAN_WAVES_SUPERRACK_DIR Clean /Applications/Waves/SuperRack
            with Glober(r"/Applications/Waves/SuperRack*", RmFileOrDir, r"path", prog_num=55) as glober_030_55:
                glober_030_55()
            # --- End CLEAN_WAVES_SUPERRACK_DIR Clean /Applications/Waves/SuperRack
        with Stage(r"Clean /Applications/Waves/MultiRack...", prog_num=56):
            # --- Begin CLEAN_WAVES_MULTIRACK_DIR Clean /Applications/Waves/MultiRack
            with RmFileOrDir(r"/Applications/Waves/MultiRack", prog_num=57) as rm_file_or_dir_031_57:
                rm_file_or_dir_031_57()
            # --- End CLEAN_WAVES_MULTIRACK_DIR Clean /Applications/Waves/MultiRack
        with Stage(r"Clean /Applications/Waves/SoundGrid QRec...", prog_num=58):
            # --- Begin CLEAN_WAVES_SOUNDGRID_QREC_DIR Clean /Applications/Waves/SoundGrid QRec
            with RmFileOrDir(r"/Applications/Waves/SoundGrid QRec", prog_num=59) as rm_file_or_dir_032_59:
                rm_file_or_dir_032_59()
            # --- End CLEAN_WAVES_SOUNDGRID_QREC_DIR Clean /Applications/Waves/SoundGrid QRec
        with Stage(r"Clean /Applications/Waves/COSMOS...", prog_num=60):
            # --- Begin CLEAN_WAVES_COSMOS_DIR Clean /Applications/Waves/COSMOS
            with RmFileOrDir(r"/Applications/Waves/COSMOS", prog_num=61) as rm_file_or_dir_033_61:
                rm_file_or_dir_033_61()
            # --- End CLEAN_WAVES_COSMOS_DIR Clean /Applications/Waves/COSMOS
        with Stage(r"Clean /Applications/Waves/Data with a few exceptions...", prog_num=62):
            # --- Begin CLEAN_WAVES_DATA_DIR Clean /Applications/Waves/Data with a few exceptions
            with Glober(r"/Applications/Waves/Data/*", RmFileOrDir, r"path", excludes=[r"Instrument Data*",r"IR1Impulses*",r"Presets*",r"Setup Libraries*",r"Waves Gems*"], prog_num=63) as glober_034_63:
                glober_034_63()
            # --- End CLEAN_WAVES_DATA_DIR Clean /Applications/Waves/Data with a few exceptions
        with Stage(r"Clean /Users/rsp_ms/Library/Preferences/Waves Preferences...", prog_num=64):
            # --- Begin CLEAN_WAVES_PREFERENCES_DIR Clean /Users/rsp_ms/Library/Preferences/Waves Preferences
            with Glober(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins*", RmSymlink, r"path", prog_num=65) as glober_035_65:
                glober_035_65()
            with Glober(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/*Studio Modules*", RmSymlink, r"path", prog_num=66) as glober_036_66:
                glober_036_66()
            with RmSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves EMotion LV1 Modules", prog_num=67) as rm_symlink_037_67:
                rm_symlink_037_67()
            with Glober(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/*", RmFileOrDir, r"path", excludes=[r"wls.config*",r"FeatureFlags.yaml*",r"ForceUseGUIScanner*",r"Waves Central.json*"], prog_num=68) as glober_038_68:
                glober_038_68()
            # --- End CLEAN_WAVES_PREFERENCES_DIR Clean /Users/rsp_ms/Library/Preferences/Waves Preferences
        with Stage(r"Clean /Users/rsp_ms/Library/Application Support/Waves Audio\Waves Local Server and database...", prog_num=69):
            # --- Begin CLEAN_WAVES_LOCAL_SERVER_DIR Clean /Users/rsp_ms/Library/Application Support/Waves Audio\Waves Local Server and database
            with RmFileOrDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Local Server", prog_num=70) as rm_file_or_dir_039_70:
                rm_file_or_dir_039_70()
            # --- End CLEAN_WAVES_LOCAL_SERVER_DIR Clean /Users/rsp_ms/Library/Application Support/Waves Audio\Waves Local Server and database
        with Stage(r"Clean user Waves Audio directory...", prog_num=71):
            # --- Begin CLEAN_USER_WAVES_DIR Clean user Waves Audio directory
            with Glober(r"/Users/rsp_ms/Library/Application Support/Waves Audio/*", RmFileOrDir, r"path", excludes=[r"Waves Central*",r"Waves Plugin Server*"], prog_num=72) as glober_040_72:
                glober_040_72()
            with Glober(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/*", RmFileOrDir, r"path", excludes=[r"Logs*"], prog_num=73) as glober_041_73:
                glober_041_73()
            with Glober(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/*", RmFileOrDir, r"path", excludes=[r"cosmos.sqlit*"], prog_num=74) as glober_042_74:
                glober_042_74()
            # --- End CLEAN_USER_WAVES_DIR Clean user Waves Audio directory
        with Stage(r"Clean /Library/Audio/Plug-Ins/WPAPI...", prog_num=75):
            # --- Begin CLEAN_WAVES_WPAPI_DIR Clean /Library/Audio/Plug-Ins/WPAPI
            with Glober(r"/Library/Audio/Plug-Ins/WPAPI/WaveShell*", RmFileOrDir, r"path", prog_num=76) as glober_043_76:
                glober_043_76()
            # --- End CLEAN_WAVES_WPAPI_DIR Clean /Library/Audio/Plug-Ins/WPAPI
        with Stage(r"Clean /Library/Application Support/Avid/Audio/Plug-Ins...", prog_num=77):
            # --- Begin CLEAN_WAVESHELL_AAX_DIR Clean /Library/Application Support/Avid/Audio/Plug-Ins
            with Glober(r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell*", RmFileOrDir, r"path", prog_num=78) as glober_044_78:
                glober_044_78()
            # --- End CLEAN_WAVESHELL_AAX_DIR Clean /Library/Application Support/Avid/Audio/Plug-Ins
        with Stage(r"Clean /Library/Audio/Plug-Ins/Components...", prog_num=79):
            # --- Begin CLEAN_MACOS_WAVESHELL_AU_DIR Clean /Library/Audio/Plug-Ins/Components
            with Glober(r"/Library/Audio/Plug-Ins/Components/WaveShell*", RmFileOrDir, r"path", prog_num=80) as glober_045_80:
                glober_045_80()
            # --- End CLEAN_MACOS_WAVESHELL_AU_DIR Clean /Library/Audio/Plug-Ins/Components
        with Stage(r"Clean vst dir...", prog_num=81):
            # --- Begin CLEAN_WAVESHELL_VST_DIR Clean vst dir
            with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*", RmFileOrDir, r"path", prog_num=82) as glober_046_82:
                glober_046_82()
            with RmFileOrDir(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", prog_num=83) as rm_file_or_dir_047_83:
                rm_file_or_dir_047_83()
            # --- End CLEAN_WAVESHELL_VST_DIR Clean vst dir
        with Stage(r"Clean vst3 dir...", prog_num=84):
            # --- Begin CLEAN_WAVESHELL_VST3_DIR Clean vst3 dir
            with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*", RmFileOrDir, r"path", prog_num=85) as glober_048_85:
                glober_048_85()
            # --- End CLEAN_WAVESHELL_VST3_DIR Clean vst3 dir
        with Stage(r"Clean /Library/Application Support/Native Instruments/Service Center...", prog_num=86):
            # --- Begin CLEAN_NATIVE_INSTRUMENTS_DIR Clean /Library/Application Support/Native Instruments/Service Center
            with Glober(r"/Library/Application Support/Native Instruments/Service Center/Waves-*.xml", RmFileOrDir, r"path", prog_num=87) as glober_049_87:
                glober_049_87()
            # --- End CLEAN_NATIVE_INSTRUMENTS_DIR Clean /Library/Application Support/Native Instruments/Service Center
        with Stage(r"Clean /Applications/Waves/SoundGrid...", prog_num=88):
            # --- Begin CLEAN_WAVES_SOUNDGRID_DIR Clean /Applications/Waves/SoundGrid
            with If(IsFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app/Contents/MacOS//SoundGridDriverUninstaller.py"), if_true=ShellCommand(r'"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app/Contents/MacOS//SoundGridDriverUninstaller.py"', message=r"Uninstalling SoundGrid Driver", ignore_all_errors=True), prog_num=89) as if_050_89:
                if_050_89()
            with RmFileOrDir(r"/Applications/Waves/SoundGrid", prog_num=90) as rm_file_or_dir_051_90:
                rm_file_or_dir_051_90()
            # --- End CLEAN_WAVES_SOUNDGRID_DIR Clean /Applications/Waves/SoundGrid
        with Stage(r"Clean /Library/Preferences/com.native-instruments.Waves...", prog_num=91):
            # --- Begin CLEAN_NI_PLIST_FILES Clean /Library/Preferences/com.native-instruments.Waves
            with Glober(r"/Library/Preferences/com.native-instruments.Waves-*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=92) as glober_052_92:
                glober_052_92()
            with Glober(r"/tmp/com.native-instruments.Waves-*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=93) as glober_053_93:
                glober_053_93()
            # --- End CLEAN_NI_PLIST_FILES Clean /Library/Preferences/com.native-instruments.Waves
        with Stage(r"clean waves plist files in /Library/LaunchAgents directory...", prog_num=94):
            # --- Begin CLEAN_LAUNCH_AGENTS_DIR clean waves plist files in /Library/LaunchAgents directory
            with Glober(r"/Library/LaunchAgents/com.waves.*.agent.plist", RmFileOrDir, r"path", prog_num=95) as glober_054_95:
                glober_054_95()
            # --- End CLEAN_LAUNCH_AGENTS_DIR clean waves plist files in /Library/LaunchAgents directory
        with Stage(r"clean COSMOS related files...", prog_num=96):
            # --- Begin CLEAN_COSMOS_FILES clean COSMOS related files
            with RmFile(r"/Users/rsp_ms/Library/Application Support/COSMOS", prog_num=97) as rm_file_055_97:
                rm_file_055_97()
            with RmFile(r"/Users/rsp_ms/Library/Preferences/com.waves.COSMOS.plist", prog_num=98) as rm_file_056_98:
                rm_file_056_98()
            # --- End CLEAN_COSMOS_FILES clean COSMOS related files
        with Stage(r"Clean SoundGrid-related .plist files...", prog_num=99):
            # --- Begin CLEAN_SOUNDGRID_RELATED_FILES Clean SoundGrid-related .plist files
            with Glober(r"/Library/LaunchDaemons/com.waves.daemon.SoundGrid*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=100) as glober_057_100:
                glober_057_100()
            with Glober(r"/Library/LaunchAgents/com.waves.daemon.SoundGrid*", RmFileOrDir, r"path", ignore_all_errors=True, prog_num=101) as glober_058_101:
                glober_058_101()
            with RmFileOrDir(r"/Users/rsp_ms/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=102) as rm_file_or_dir_059_102:
                rm_file_or_dir_059_102()
            # --- End CLEAN_SOUNDGRID_RELATED_FILES Clean SoundGrid-related .plist files
    with Stage(r"post_doit", prog_num=103):
        print("Done Doing it")

with Stage(r"epilog", prog_num=104):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/cleanup/cleanup_15-20250120142536.py", prog_num=105) as patch_py_batch_with_timings_060_105:
        patch_py_batch_with_timings_060_105()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


