# Creation time: 15-06-25_16-24
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 103
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
    config_vars['ACTION_ID'] = r"16-20250615162407"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.5.5"
    config_vars['CHECK_WAVES_INSTRUMENT_DATA_DIR'] = r"/yes"
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['CURRENT_DOIT_DESCRIPTION'] = r"Doing it"
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+", r"Clean_old_plist_Native_NI")
    config_vars['EXIT_ON_EXEC_EXCEPTION'] = r"False"
    config_vars['FIX_ALL_PERMISSIONS_SYMBOLIC_MODE'] = r"u+rwx,go+rx"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"fixed create_venc.sh to not update pip itself with the global python"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['MAIN_DOIT_ITEMS'] = (r"PREFIX_WAVES_DIR", r"PREFIX_CENTRAL_APP_DATA_DIR", r"PREFIX_CENTRAL_LOGS_DIR", r"PREFIX_USER_WAVES_DIR", r"PREFIX_WAVES_APP_DATA_DIR", r"PREFIX_CACHE_DIR", r"PREFIX_WAVESHELL_VST_DIR", r"PREFIX_WAVESHELL_VST3_DIR", r"PREFIX_WAVESHELL_AAX_DIR", r"PREFIX_WAVES_WPAPI_DIR", r"PREFIX_WAVES_PROGRAMDATA_DIR", r"PREFIX_WAVES_LICENSES_DIR", r"PREFIX_WAVES_PREFERENCES_DIR", r"PREFIX_WAVES_SHARED_DIR", r"PREFIX_WAVESHELL_AU_DIR", r"PREFIX_WAVESHELL_DAE_DIR", r"PREFIX_LAUNCH_AGENTS_PLIST", r"PREFIX_WAVES_REWIRE_DIR", r"PREFIX_NATIVE_INSTRUMENTS_PLIST", r"PREFIX_NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR", r"PREFIX_SAMPLE_DIR", r"PREFIX_USER_LOGS_FOLDER", r"PREFIX_NUMBA_CACHE_FOLDER")
    config_vars['MAIN_INSTALL_TARGETS'] = (r"PREFIX_WAVES_DIR", r"PREFIX_CENTRAL_APP_DATA_DIR", r"PREFIX_CENTRAL_LOGS_DIR", r"PREFIX_USER_WAVES_DIR", r"PREFIX_WAVES_APP_DATA_DIR", r"PREFIX_CACHE_DIR", r"PREFIX_WAVESHELL_VST_DIR", r"PREFIX_WAVESHELL_VST3_DIR", r"PREFIX_WAVESHELL_AAX_DIR", r"PREFIX_WAVES_WPAPI_DIR", r"PREFIX_WAVES_PROGRAMDATA_DIR", r"PREFIX_WAVES_LICENSES_DIR", r"PREFIX_WAVES_PREFERENCES_DIR", r"PREFIX_WAVES_SHARED_DIR", r"PREFIX_WAVESHELL_AU_DIR", r"PREFIX_WAVESHELL_DAE_DIR", r"PREFIX_LAUNCH_AGENTS_PLIST", r"PREFIX_WAVES_REWIRE_DIR", r"PREFIX_NATIVE_INSTRUMENTS_PLIST", r"PREFIX_NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR", r"PREFIX_SAMPLE_DIR", r"PREFIX_USER_LOGS_FOLDER", r"PREFIX_NUMBA_CACHE_FOLDER")
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NUMBA_CACHE_FOLDER'] = r"/Users/rsp_ms/Library/Caches/numba"
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 0
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 0
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/doit-output-16-20250615162407.log"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlDoIt.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/prefix.yaml")
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 93
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio"
    config_vars['USER_LAUNCH_AGENTS_DIR'] = r"/Users/rsp_ms/Library/LaunchAgents"
    config_vars['USER_LOGS_FOLDER'] = r"/Users/rsp_ms/Library/Logs/Waves Audio"
    config_vars['USER_WAVES_DIR'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['WAVES_CENTRAL_APP_DATA_DIR'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central"
    config_vars['WAVES_CENTRAL_LOGS_DIR'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs"
    config_vars['WAVES_DATA_DIR'] = r"/Applications/Waves/Data"
    config_vars['WAVES_DIR'] = r"/Applications/Waves"
    config_vars['WAVES_INSTRUMENT_DATA_DIR'] = r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries"
    config_vars['WAVES_LICENSE_DIR'] = r"/Library/Application Support/Waves/Licenses"
    config_vars['WAVES_PREFERENCES_DIR'] = r"/Users/rsp_ms/Library/Preferences/Waves Preferences"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WAVES_REWIRE_DIR'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['WAVES_SHARED_DIR'] = r"/Users/Shared/Waves"
    config_vars['WAVES_WPAPI_DIR'] = r"/Library/Audio/Plug-Ins/WPAPI"
    config_vars['WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"doit", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/doit-output-16-20250615162407.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"activate-repo-rev", r"check-checksum", r"check-instl-folder-integrity", r"checksum", r"collect-manifests", r"command-list", r"copy", r"depend", r"doit", r"dump-config-vars", r"exec", r"fail", r"file-sizes", r"fix-perm", r"fix-props", r"fix-symlinks", r"gui", r"help", r"ls", r"parallel-run", r"read-info-map", r"read-yaml", r"remove", r"report-versions", r"resolve", r"run-process", r"short-index", r"stage2svn", r"svn2stage", r"sync", r"synccopy", r"test-import", r"translate-guids", r"translate_url", r"uninstall", r"unwtar", r"up-short-index", r"up2s3", r"verify-index", r"verify-repo", r"version", r"wait-on-action-trigger", r"wtar", r"wtar-staging-folder", r"wzip")
    config_vars['__COMPILATION_TIME__'] = r"2025-05-22 15:27:15.823473"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DOIT_TARGETS__'] = (r"PREFIX_WAVES_DIR", r"PREFIX_CENTRAL_APP_DATA_DIR", r"PREFIX_CENTRAL_LOGS_DIR", r"PREFIX_USER_WAVES_DIR", r"PREFIX_CACHE_DIR", r"PREFIX_WAVESHELL_VST_DIR", r"PREFIX_WAVESHELL_VST3_DIR", r"PREFIX_WAVESHELL_AAX_DIR", r"PREFIX_WAVES_WPAPI_DIR", r"PREFIX_WAVES_PROGRAMDATA_DIR", r"PREFIX_WAVES_LICENSES_DIR", r"PREFIX_WAVES_PREFERENCES_DIR", r"PREFIX_WAVES_SHARED_DIR", r"PREFIX_WAVESHELL_AU_DIR", r"PREFIX_WAVESHELL_DAE_DIR", r"PREFIX_LAUNCH_AGENTS_PLIST", r"PREFIX_WAVES_REWIRE_DIR", r"PREFIX_NATIVE_INSTRUMENTS_PLIST", r"PREFIX_NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR", r"PREFIX_SAMPLE_DIR", r"PREFIX_USER_LOGS_FOLDER", r"PREFIX_NUMBA_CACHE_FOLDER")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 0
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.7 2025-05-22 15:27:15.823473 BM-MAC-ADO5"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.7"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 7)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"hodrnavilyxdsvwi"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"doit"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.yaml"
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.py"
    config_vars['__NOW__'] = r"2025-06-15 16:24:08.248540"
    config_vars['__ORPHAN_DOIT_TARGETS__'] = r"PREFIX_WAVES_APP_DATA_DIR"
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO5"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer", r"/Applications/Waves Central.app/Contents/Resources/res/external/data")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"BM-MAC-ADO5"
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
        with Stage(r"Prefix /Applications/Waves...", prog_num=12):
            # --- Begin PREFIX_WAVES_DIR Prefix /Applications/Waves
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=13) as make_dir_001_13:
                make_dir_001_13()
            with Chown(path=r"/Applications/Waves", user_id=501, group_id=20, prog_num=14, recursive=True) as chown_002_14:
                chown_002_14()
            with Chmod(path=r"/Applications/Waves", mode="a+rwX", prog_num=15, recursive=True) as chmod_003_15:
                chmod_003_15()
            # --- End PREFIX_WAVES_DIR Prefix /Applications/Waves
        with Stage(r"Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central...", prog_num=16):
            # --- Begin PREFIX_CENTRAL_APP_DATA_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central
            with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central", chowner=True, prog_num=17) as make_dir_004_17:
                make_dir_004_17()
            with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central", mode="a+rwX", prog_num=18, recursive=True) as chmod_005_18:
                chmod_005_18()
            # --- End PREFIX_CENTRAL_APP_DATA_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central
        with Stage(r"Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs...", prog_num=19):
            # --- Begin PREFIX_CENTRAL_LOGS_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs
            with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs", chowner=True, prog_num=20) as make_dir_006_20:
                make_dir_006_20()
            with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs", mode="a+rwX", prog_num=21, recursive=True) as chmod_007_21:
                chmod_007_21()
            # --- End PREFIX_CENTRAL_LOGS_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs
        with Stage(r"Prefix /Users/rsp_ms/Library/Application Support/Waves Audio...", prog_num=22):
            # --- Begin PREFIX_USER_WAVES_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio
            with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio", chowner=True, prog_num=23) as make_dir_008_23:
                make_dir_008_23()
            with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio", mode="a+rwX", prog_num=24, recursive=True) as chmod_009_24:
                chmod_009_24()
            # --- End PREFIX_USER_WAVES_DIR Prefix /Users/rsp_ms/Library/Application Support/Waves Audio
        with Stage(r"Prefix /Users/rsp_ms/Library/Caches/Waves Audio...", prog_num=25):
            # --- Begin PREFIX_CACHE_DIR Prefix /Users/rsp_ms/Library/Caches/Waves Audio
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio", chowner=True, prog_num=26) as make_dir_010_26:
                make_dir_010_26()
            with Chown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio", user_id=501, group_id=20, prog_num=27, recursive=True) as chown_011_27:
                chown_011_27()
            with Chmod(path=r"/Users/rsp_ms/Library/Caches/Waves Audio", mode="a+rwX", prog_num=28, recursive=True) as chmod_012_28:
                chmod_012_28()
            # --- End PREFIX_CACHE_DIR Prefix /Users/rsp_ms/Library/Caches/Waves Audio
        with Stage(r"Prefix /Library/Audio/Plug-Ins/VST...", prog_num=29):
            # --- Begin PREFIX_WAVESHELL_VST_DIR Prefix /Library/Audio/Plug-Ins/VST
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=30) as make_dir_013_30:
                make_dir_013_30()
            with Chmod(path=r"/Library/Audio/Plug-Ins/VST", mode="a+rwX", ignore_if_not_exist=True, prog_num=31) as chmod_014_31:
                chmod_014_31()
            with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=32) as glober_015_32:
                glober_015_32()
            with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst", Chmod, None, r"a+rwX", recursive=True, prog_num=33) as glober_016_33:
                glober_016_33()
            # --- End PREFIX_WAVESHELL_VST_DIR Prefix /Library/Audio/Plug-Ins/VST
        with Stage(r"Prefix /Library/Audio/Plug-Ins/VST3...", prog_num=34):
            # --- Begin PREFIX_WAVESHELL_VST3_DIR Prefix /Library/Audio/Plug-Ins/VST3
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=35) as make_dir_017_35:
                make_dir_017_35()
            with Chmod(path=r"/Library/Audio/Plug-Ins/VST3", mode="a+rwX", ignore_if_not_exist=True, prog_num=36) as chmod_018_36:
                chmod_018_36()
            with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=37) as glober_019_37:
                glober_019_37()
            with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Chmod, None, r"a+rwX", recursive=True, prog_num=38) as glober_020_38:
                glober_020_38()
            # --- End PREFIX_WAVESHELL_VST3_DIR Prefix /Library/Audio/Plug-Ins/VST3
        with Stage(r"Prefix /Library/Application Support/Avid/Audio/Plug-Ins...", prog_num=39):
            # --- Begin PREFIX_WAVESHELL_AAX_DIR Prefix /Library/Application Support/Avid/Audio/Plug-Ins
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=40) as make_dir_021_40:
                make_dir_021_40()
            with Chmod(path=r"/Library/Application Support/Avid/Audio/Plug-Ins", mode="a+rwX", ignore_if_not_exist=True, prog_num=41) as chmod_022_41:
                chmod_022_41()
            with Glober(r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell*.aaxplugin", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=42) as glober_023_42:
                glober_023_42()
            with Glober(r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell*.aaxplugin", Chmod, None, r"a+rwX", recursive=True, prog_num=43) as glober_024_43:
                glober_024_43()
            # --- End PREFIX_WAVESHELL_AAX_DIR Prefix /Library/Application Support/Avid/Audio/Plug-Ins
        with Stage(r"Prefix /Library/Audio/Plug-Ins/WPAPI...", prog_num=44):
            # --- Begin PREFIX_WAVES_WPAPI_DIR Prefix /Library/Audio/Plug-Ins/WPAPI
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=45) as make_dir_025_45:
                make_dir_025_45()
            with Chmod(path=r"/Library/Audio/Plug-Ins/WPAPI", mode="a+rwX", prog_num=46) as chmod_026_46:
                chmod_026_46()
            with Glober(r"/Library/Audio/Plug-Ins/WPAPI/WaveShell*.bundle", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=47) as glober_027_47:
                glober_027_47()
            with Glober(r"/Library/Audio/Plug-Ins/WPAPI/WaveShell*.bundle", Chmod, None, r"a+rwX", recursive=True, prog_num=48) as glober_028_48:
                glober_028_48()
            # --- End PREFIX_WAVES_WPAPI_DIR Prefix /Library/Audio/Plug-Ins/WPAPI
        with Stage(r"Prefix /Library/Application Support/Waves...", prog_num=49):
            # --- Begin PREFIX_WAVES_PROGRAMDATA_DIR Prefix /Library/Application Support/Waves
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=50) as make_dir_029_50:
                make_dir_029_50()
            with Chown(path=r"/Library/Application Support/Waves", user_id=501, group_id=20, ignore_all_errors=True, prog_num=51, recursive=True) as chown_030_51:
                chown_030_51()
            with Chmod(path=r"/Library/Application Support/Waves", mode="a+rwX", prog_num=52, recursive=True) as chmod_031_52:
                chmod_031_52()
            # --- End PREFIX_WAVES_PROGRAMDATA_DIR Prefix /Library/Application Support/Waves
        with Stage(r"Prefix /Library/Application Support/Waves/Licenses...", prog_num=53):
            # --- Begin PREFIX_WAVES_LICENSES_DIR Prefix /Library/Application Support/Waves/Licenses
            with MakeDir(r"/Library/Application Support/Waves/Licenses", chowner=True, prog_num=54) as make_dir_032_54:
                make_dir_032_54()
            with Chmod(path=r"/Library/Application Support/Waves/Licenses", mode="a+rwX", prog_num=55, recursive=True) as chmod_033_55:
                chmod_033_55()
            # --- End PREFIX_WAVES_LICENSES_DIR Prefix /Library/Application Support/Waves/Licenses
        with Stage(r"Prefix /Users/rsp_ms/Library/Preferences/Waves Preferences...", prog_num=56):
            # --- Begin PREFIX_WAVES_PREFERENCES_DIR Prefix /Users/rsp_ms/Library/Preferences/Waves Preferences
            with Chmod(path=r"/Users/rsp_ms/Library/Preferences/Waves Preferences", mode="a+rwX", ignore_if_not_exist=True, prog_num=57, recursive=True) as chmod_034_57:
                chmod_034_57()
            # --- End PREFIX_WAVES_PREFERENCES_DIR Prefix /Users/rsp_ms/Library/Preferences/Waves Preferences
        with Stage(r"Prefix /Users/Shared/Waves...", prog_num=58):
            # --- Begin PREFIX_WAVES_SHARED_DIR Prefix /Users/Shared/Waves
            with MakeDir(r"/Users/Shared/Waves", prog_num=59) as make_dir_035_59:
                make_dir_035_59()
            with Chmod(path=r"/Users/Shared/Waves", mode="a+rwX", prog_num=60, recursive=True) as chmod_036_60:
                chmod_036_60()
            # --- End PREFIX_WAVES_SHARED_DIR Prefix /Users/Shared/Waves
        with Stage(r"Prefix /Library/Audio/Plug-Ins/Components...", prog_num=61):
            # --- Begin PREFIX_WAVESHELL_AU_DIR Prefix /Library/Audio/Plug-Ins/Components
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=62) as make_dir_037_62:
                make_dir_037_62()
            with Chmod(path=r"/Library/Audio/Plug-Ins/Components", mode="a+rwX", ignore_if_not_exist=True, prog_num=63) as chmod_038_63:
                chmod_038_63()
            with Glober(r"/Library/Audio/Plug-Ins/Components/WaveShell*.component", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=64) as glober_039_64:
                glober_039_64()
            with Glober(r"/Library/Audio/Plug-Ins/Components/WaveShell*.component", Chmod, None, r"a+rwX", recursive=True, prog_num=65) as glober_040_65:
                glober_040_65()
            # --- End PREFIX_WAVESHELL_AU_DIR Prefix /Library/Audio/Plug-Ins/Components
        with Stage(r"Prefix /Library/Application Support/Digidesign/Plug-Ins...", prog_num=66):
            # --- Begin PREFIX_WAVESHELL_DAE_DIR Prefix /Library/Application Support/Digidesign/Plug-Ins
            with Chmod(path=r"/Library/Application Support/Digidesign/Plug-Ins", mode="a+rwX", ignore_if_not_exist=True, prog_num=67) as chmod_041_67:
                chmod_041_67()
            with Glober(r"/Library/Application Support/Digidesign/Plug-Ins/WaveShell*.dpm", Chown, r"path", user_id=501, group_id=20, recursive=True, prog_num=68) as glober_042_68:
                glober_042_68()
            with Glober(r"/Library/Application Support/Digidesign/Plug-Ins/WaveShell*.dpm", Chmod, None, r"a+rwX", recursive=True, prog_num=69) as glober_043_69:
                glober_043_69()
            # --- End PREFIX_WAVESHELL_DAE_DIR Prefix /Library/Application Support/Digidesign/Plug-Ins
        with Stage(r"Fix files in /Users/rsp_ms/Library/LaunchAgents...", prog_num=70):
            # --- Begin PREFIX_LAUNCH_AGENTS_PLIST Fix files in /Users/rsp_ms/Library/LaunchAgents
            with Chown(path=r"/Users/rsp_ms/Library/LaunchAgents", user_id=501, group_id=20, ignore_all_errors=True, prog_num=71) as chown_044_71:
                chown_044_71()
            with Chmod(path=r"/Users/rsp_ms/Library/LaunchAgents", mode="u+rwX", ignore_all_errors=True, prog_num=72) as chmod_045_72:
                chmod_045_72()
            with Chmod(path=r"/Users/rsp_ms/Library/LaunchAgents", mode="go+rX", ignore_all_errors=True, prog_num=73) as chmod_046_73:
                chmod_046_73()
            with Chown(path=r"/Users/rsp_ms/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", user_id=501, group_id=20, ignore_all_errors=True, prog_num=74) as chown_047_74:
                chown_047_74()
            with Chmod(path=r"/Users/rsp_ms/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", mode="u+rw", ignore_all_errors=True, prog_num=75) as chmod_048_75:
                chmod_048_75()
            with Chmod(path=r"/Users/rsp_ms/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", mode="go+r", ignore_all_errors=True, prog_num=76) as chmod_049_76:
                chmod_049_76()
            # --- End PREFIX_LAUNCH_AGENTS_PLIST Fix files in /Users/rsp_ms/Library/LaunchAgents
        with Stage(r"Prefix /Library/Application Support/Propellerhead Software/ReWire...", prog_num=77):
            # --- Begin PREFIX_WAVES_REWIRE_DIR Prefix /Library/Application Support/Propellerhead Software/ReWire
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=78) as make_dir_050_78:
                make_dir_050_78()
            with Chmod(path=r"/Library/Application Support/Propellerhead Software/ReWire", mode="a+rwX", ignore_if_not_exist=True, prog_num=79) as chmod_051_79:
                chmod_051_79()
            with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=501, group_id=20, ignore_all_errors=True, prog_num=80, recursive=True) as chown_052_80:
                chown_052_80()
            with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=501, group_id=20, ignore_all_errors=True, prog_num=81, recursive=True) as chown_053_81:
                chown_053_81()
            with Chmod(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", mode="a+rwX", ignore_if_not_exist=True, prog_num=82, recursive=True) as chmod_054_82:
                chmod_054_82()
            with Chmod(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", mode="a+rwX", ignore_if_not_exist=True, prog_num=83, recursive=True) as chmod_055_83:
                chmod_055_83()
            # --- End PREFIX_WAVES_REWIRE_DIR Prefix /Library/Application Support/Propellerhead Software/ReWire
        with Stage(r"Prefix Native Instruments .plist files on Mac...", prog_num=84):
            # --- Begin PREFIX_NATIVE_INSTRUMENTS_PLIST Prefix Native Instruments .plist files on Mac
            with Glober(r"/Library/Preferences/com.native-instruments.Waves-*.plist", Chown, r"path", user_id=501, group_id=20, prog_num=85) as glober_056_85:
                glober_056_85()
            with Glober(r"/Library/Preferences/com.native-instruments.Waves-*.plist", Chmod, None, r"a+rwX", prog_num=86) as glober_057_86:
                glober_057_86()
            # --- End PREFIX_NATIVE_INSTRUMENTS_PLIST Prefix Native Instruments .plist files on Mac
        with Stage(r"Prefix /Library/Application Support/Native Instruments/Service Center...", prog_num=87):
            # --- Begin PREFIX_NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR Prefix /Library/Application Support/Native Instruments/Service Center
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=88) as make_dir_058_88:
                make_dir_058_88()
            with Chmod(path=r"/Library/Application Support/Native Instruments/Service Center", mode="a+rwX", ignore_if_not_exist=True, prog_num=89) as chmod_059_89:
                chmod_059_89()
            with Glober(r"/Library/Application Support/Native Instruments/Service Center/Waves-*", Chown, r"path", user_id=501, group_id=20, prog_num=90) as glober_060_90:
                glober_060_90()
            with Glober(r"/Library/Application Support/Native Instruments/Service Center/Waves-*", Chmod, None, r"a+rw", prog_num=91) as glober_061_91:
                glober_061_91()
            # --- End PREFIX_NATIVE_INSTRUMENTS_SERVICE_CENTER_DIR Prefix /Library/Application Support/Native Instruments/Service Center
        with Stage(r":Prefix /Applications/Waves/Data/Instrument Data/Waves Sample Libraries...", prog_num=92):
            # --- Begin PREFIX_SAMPLE_DIR :Prefix /Applications/Waves/Data/Instrument Data/Waves Sample Libraries
            with If(IsEq(r"yes", r"yes"), if_true=MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries"), prog_num=93) as if_062_93:
                if_062_93()
            # --- End PREFIX_SAMPLE_DIR :Prefix /Applications/Waves/Data/Instrument Data/Waves Sample Libraries
        with Stage(r"Prefix /Users/rsp_ms/Library/Logs/Waves Audio to read write all...", prog_num=94):
            # --- Begin PREFIX_USER_LOGS_FOLDER Prefix /Users/rsp_ms/Library/Logs/Waves Audio to read write all
            with Chown(path=r"/Users/rsp_ms/Library/Logs/Waves Audio", user_id=501, group_id=20, ignore_all_errors=True, prog_num=95) as chown_063_95:
                chown_063_95()
            with Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio", mode="go+rX", ignore_if_not_exist=True, prog_num=96) as chmod_064_96:
                chmod_064_96()
            with Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio", mode="u+rwX", ignore_if_not_exist=True, prog_num=97) as chmod_065_97:
                chmod_065_97()
            # --- End PREFIX_USER_LOGS_FOLDER Prefix /Users/rsp_ms/Library/Logs/Waves Audio to read write all
        with Stage(r"Prefix /Users/rsp_ms/Library/Caches/numba to read write all...", prog_num=98):
            # --- Begin PREFIX_NUMBA_CACHE_FOLDER Prefix /Users/rsp_ms/Library/Caches/numba to read write all
            with Chown(path=r"/Users/rsp_ms/Library/Caches/numba", user_id=501, group_id=20, ignore_all_errors=True, prog_num=99, recursive=True) as chown_066_99:
                chown_066_99()
            with Chmod(path=r"/Users/rsp_ms/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, prog_num=100, recursive=True) as chmod_067_100:
                chmod_067_100()
            # --- End PREFIX_NUMBA_CACHE_FOLDER Prefix /Users/rsp_ms/Library/Caches/numba to read write all
    with Stage(r"post_doit", prog_num=101):
        print("Done Doing it")

with Stage(r"epilog", prog_num=102):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/permissionFixer/permission-fixer_16-20250615162407.py", prog_num=103) as patch_py_batch_with_timings_068_103:
        patch_py_batch_with_timings_068_103()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


