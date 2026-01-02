# Creation time: 29-06-25_16-54
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 976
PythonBatchCommandBase.running_progress = 478
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=479):  # 0m:0.000s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250629165446"
    config_vars['ALL_SYNC_DIRS'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"16.0.5"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V15", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V15", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 59
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MTI2NjQ4N30sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUxMjMwMTg3fX19XX0_;CloudFront-Signature=XFQ2x0I3yXeD1edmP6BiZpB-Q7GECmSBBcF9iRLR7ljx~dKW5Lp12bc-16yjo3FhP1QuqQpH~rL~WnjJi-Rl6Qj8LbOcnOQqZBYvv5azI9kWHWcLFw-RmtOJsMkIS8C09dWqF7Vh5cNqe5boaiPPTMlFX~C7J8~11fmfqFO5waa56exfmoChyJI1jGb-2ydoquqxHEnKobGwNUeqW1bONfxiGtGniRypP-ytOyl8pJckuyr7U9adrWyhEle8CtXwAVsr3lz83Sb80-6dHKv0OQuO04P~-ntBdDxvk1c80cr1CVWn3lqAcNI9y-7YCuF~ysU3D-zpJXVvonLUxEp6DA__"
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['CREATE_APP_SHORTCUTS'] = r"yes"
    config_vars['CURL_CONFIG_FILE_NAME'] = r"dl"
    config_vars['CURL_CONNECT_TIMEOUT'] = 32
    config_vars['CURL_MAX_TIME'] = 600
    config_vars['CURL_RETRIES'] = 6
    config_vars['CURL_RETRY_DELAY'] = 12
    config_vars['CUSTOM_HEADERS'] = r'register.waves.com:{"Client-Name":"Waves Central"}'
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DEFAULT_IID_VERSION'] = r"0.0.0"
    config_vars['DIRECT_SYNC_INSTRUMENT_DATA'] = r"yes"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+", r"Clean_old_plist_Native_NI")
    config_vars['DOWNLOAD_TOOL_PATH'] = r"/curl"
    config_vars['EXIT_ON_EXEC_EXCEPTION'] = r"False"
    config_vars['FIX_ALL_PERMISSIONS_SYMBOLIC_MODE'] = r"u+rwx,go+rx"
    config_vars['Fix_Folder_Permissions'] = r'''Chmod(r"""$(__Fix_Folder_Permissions_1__)""", 'a+rwx' , message="UnLocking $(__Fix_Folder_Permissions_1__)", ignore_all_errors=True)'''
    config_vars['Fix_Folder_Permissions_Recursive'] = r'''Chmod(r"""$(__Fix_Folder_Permissions_Recursive_1__)""", 'a+rwX' , message="UnLocking $(__Fix_Folder_Permissions_Recursive_1__)", recursive=True, ignore_all_errors=True)'''
    config_vars['HAVE_INFO_MAP_COPY_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FILE_NAME'] = r"have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FOR_COPY'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt"
    config_vars['HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['INDEX_CHECKSUM'] = r"f92abdecad4a6427c158f4ca0302ab5be6a6de94"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"085814c5e8648b4cf8579f15da7e845477bd3c7f"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"dfc80d80-ad21-11e0-804c-b7fd7bebd530", r"e06158e4-ad21-11e0-80ed-b7fd7bebd530")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 59
    config_vars['MIN_REPO_REV'] = 1
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NEW_HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt"
    config_vars['NEW_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V15/new_require.yaml"
    config_vars['NI_SERVICE_CENTER'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NO_FLAGS_PATTERNS'] = (r"desktop.ini", r"*.ico")
    config_vars['NO_HARD_LINK_PATTERNS'] = (r"*Info.xml", r"*Info.plist", r"desktop.ini", r"*.ico")
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 2
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 4
    config_vars['OLD_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V15/old_require.yaml"
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165446.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 59
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-05-30 10:29:38.857115"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/59"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V15"
    config_vars['REQUIRE_REPO_REV'] = 59
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"52074f48d72fd4ac2fa9f1f7e661cd948b2e8653"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/short-index.yaml"
    config_vars['SHOULD_NOT_BE_REQUIRED_BY'] = r"(Plugin\d+_\d+_Root_\d+_\d+_IID)|(GTR(_Internals|_Stomps|Solo_Stomps)_IID)"
    config_vars['SITE_BOOKKEEPING_DIR'] = r"/Library/Application Support"
    config_vars['SITE_HAVE_INFO_MAP_PATH'] = r"/Library/Application Support/Waves/Central/V15/have_info_map.txt"
    config_vars['SITE_REPO_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central/V15"
    config_vars['SITE_REQUIRE_FILE_NAME'] = r"require.yaml"
    config_vars['SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V15/require.yaml"
    config_vars['SITE_VENDOR_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central"
    config_vars['SOURCE_PREFIX'] = r"Mac"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15"
    config_vars['SYNC_BASE_URL_MAIN_ITEM'] = r"d36wza55md4dee.cloudfront.net"
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"before-copy-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 493
    config_vars['TO_SYNC_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/to_sync_info_map.txt"
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl"
    config_vars['USE_ZLIB'] = r"yes"
    config_vars['VENDOR_DIR_NAME'] = r"Waves/Central"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVES_APPS_DIR'] = r"/Applications/Waves/Applications V15"
    config_vars['WAVES_APPS_DIR_V10'] = r"/Applications/Waves/Applications V10"
    config_vars['WAVES_APPS_DIR_V11'] = r"/Applications/Waves/Applications V11"
    config_vars['WAVES_APPS_DIR_V12'] = r"/Applications/Waves/Applications V12"
    config_vars['WAVES_APPS_DIR_V13'] = r"/Applications/Waves/Applications V13"
    config_vars['WAVES_APPS_DIR_V14'] = r"/Applications/Waves/Applications V14"
    config_vars['WAVES_CENTRAL_EXTERNAL_DATA'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/data"
    config_vars['WAVES_CENTRAL_INSTALL_DIR'] = r"/Applications/Waves/Applications V15"
    config_vars['WAVES_COSMOS_DIR'] = r"/Applications/Waves/COSMOS"
    config_vars['WAVES_DATA_UTILITIES'] = r"/Applications/Waves/Data/Utilities"
    config_vars['WAVES_DIR'] = r"/Applications/Waves"
    config_vars['WAVES_DRIVERS_DIR'] = r"/Applications/Waves/SoundGrid"
    config_vars['WAVES_EMOTION_LV1_DIR'] = r"/Applications/Waves/eMotion LV1"
    config_vars['WAVES_EMOTION_LV1_NATIVE_DIR'] = r"/Applications/Waves/eMotion LV1 Native"
    config_vars['WAVES_INSTRUMENT_DATA_DEFAULT_DIR'] = r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries"
    config_vars['WAVES_INSTRUMENT_DATA_DIR'] = r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries"
    config_vars['WAVES_INSTRUMENT_DATA_MISC_DIR'] = r"/Applications/Waves/Data/Instrument Data/Misc"
    config_vars['WAVES_INSTRUMENT_DATA_NKS_DIR'] = r"/Applications/Waves/Data/Instrument Data/NKS"
    config_vars['WAVES_INSTRUMENT_DATA_NKS_FX_DIR'] = r"/Applications/Waves/Data/NKS FX"
    config_vars['WAVES_LOCAL_SERVER_DIR'] = r"/Library/Application Support/Waves/WavesLocalServer"
    config_vars['WAVES_MODULES_DIR'] = r"/Library/Application Support/Waves/Modules"
    config_vars['WAVES_MULTIRACK_DIR'] = r"/Applications/Waves/MultiRack"
    config_vars['WAVES_MULTIRACK_FOR_KRAMER_DIR'] = r"/Applications/Waves/MultiRack for Kramer"
    config_vars['WAVES_NKS_FX_DIR'] = r"/Applications/Waves/Data/NKS FX"
    config_vars['WAVES_PIVOT_DIR'] = r"/Library/Application Support/Waves/Pivot"
    config_vars['WAVES_PLUGINS_DIR'] = r"/Applications/Waves/Plug-Ins V15"
    config_vars['WAVES_PREFERENCES_DIR'] = r"/Users/rsp_ms/Library/Preferences/Waves Preferences"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WAVES_SG_TEMPLATES_DIR'] = r"/Users/Shared/Waves/eMotion"
    config_vars['WAVES_SHARED_DIR'] = r"/Users/Shared/Waves"
    config_vars['WAVES_SHELLS_DIR'] = r"/Applications/Waves/WaveShells V15"
    config_vars['WAVES_SHELLS_DIR_V10'] = r"/Applications/Waves/WaveShells V10"
    config_vars['WAVES_SHELLS_DIR_V11'] = r"/Applications/Waves/WaveShells V11"
    config_vars['WAVES_SHELLS_DIR_V12'] = r"/Applications/Waves/WaveShells V12"
    config_vars['WAVES_SHELLS_DIR_V13'] = r"/Applications/Waves/WaveShells V13"
    config_vars['WAVES_SHELLS_DIR_V14'] = r"/Applications/Waves/WaveShells V14"
    config_vars['WAVES_SHELL_DIRS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Audio/Plug-Ins/WPAPI")
    config_vars['WAVES_SOUNDGRID_DIR'] = r"/Applications/Waves/SoundGrid"
    config_vars['WAVES_SOUNDGRID_DOCUMENTS_DIR'] = r"/Applications/Waves/SoundGrid/Documents"
    config_vars['WAVES_SOUNDGRID_FIRMWARE_DIR'] = r"/Library/Application Support/Waves/SoundGrid Firmware"
    config_vars['WAVES_SOUNDGRID_FOR_VENUE_DIR'] = r"/Applications/Waves/SoundGrid for Venue"
    config_vars['WAVES_SOUNDGRID_IO_MODULES_DIR'] = r"/Library/Application Support/Waves/SoundGrid IO Modules"
    config_vars['WAVES_SOUNDGRID_STUDIO_DIR'] = r"/Applications/Waves/SoundGrid Studio"
    config_vars['WAVES_SOUNDGRID_UTILITIES_DIR'] = r"/Applications/Waves/SoundGrid/Utilities"
    config_vars['WAVES_SUPERRACK_DIR'] = r"/Applications/Waves/SuperRack"
    config_vars['WAVES_SUPERRACK_PERFORMER_DIR'] = r"/Applications/Waves/SuperRack Performer"
    config_vars['WAVES_UNUSED_PLUGINS_DIR'] = r"/Applications/Waves/Unused Plug-Ins V15"
    config_vars['WAVES_WPAPI_DIR'] = r"/Library/Audio/Plug-Ins/WPAPI"
    config_vars['WLE_EXEC_PATH'] = r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165446.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = ""
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"Artist_DLLs_Common_Guid_IID", r"CLA_Bass_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"Get_General_Icons_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"IntelDlls_IID", r"LicenseNotifications_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"Shutdown_Servers_IID", r"V9_V10_Organizer_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesLib1_15_5_79_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"mxwtrumdsnefjfdt"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"Artist_DLLs_Common_Guid_IID", r"CLA_Bass_IID", r"CLA_Vocals_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-29 16:55:33.619542"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"BM-MAC-ADO6"
    config_vars['__SQLITE_VERSION__'] = r"3.45.1"
    config_vars['__SUDO_USER__'] = r"no set"
    config_vars['__SYNC_PREREQUISITE_VARIABLES__'] = (r"SYNC_BASE_URL", r"DOWNLOAD_TOOL_PATH", r"REPO_REV", r"LOCAL_REPO_SYNC_DIR")
    config_vars['__SYSTEM_LOG_FILE_PATH__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/instl/instl.log"
    config_vars['__USER_CONFIG_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_CONFIG_FILE_NAME__'] = r"instl_config.yaml"
    config_vars['__USER_CONFIG_FILE_PATH__'] = r"/Users/rsp_ms/instl_config.yaml"
    config_vars['__USER_DATA_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_DESKTOP_DIR__'] = r"/Users/rsp_ms/Desktop"
    config_vars['__USER_HOME_DIR__'] = r"/Users/rsp_ms"
    config_vars['__USER_ID__'] = 501

with PythonBatchRuntime(r"synccopy", prog_num=480):  # 0m:14.741s
    with Stage(r"begin", prog_num=481):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=482):  # 0m:0.007s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=483) as copy_file_to_file_001_483:  # 0m:0.004s
            copy_file_to_file_001_483()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=484) as copy_file_to_file_002_484:  # 0m:0.003s
            copy_file_to_file_002_484()
    with Stage(r"sync", prog_num=485):  # 0m:2.123s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=486) as shell_command_003_486:  # 0m:0.008s
            shell_command_003_486()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=487) as shell_command_004_487:  # 0m:0.010s
            shell_command_004_487()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=488) as shell_command_005_488:  # 0m:0.960s
            shell_command_005_488()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=489) as shell_command_006_489:  # 0m:0.007s
            shell_command_006_489()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=490) as shell_command_007_490:  # 0m:0.974s
            shell_command_007_490()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=491) as shell_command_008_491:  # 0m:0.007s
            shell_command_008_491()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=492) as shell_command_009_492:  # 0m:0.005s
            shell_command_009_492()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=493) as shell_command_010_493:  # 0m:0.140s
            shell_command_010_493()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=494):  # 0m:0.012s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=495) as make_dir_011_495:  # 0m:0.005s
                make_dir_011_495()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=496) as cd_012_496:  # 0m:0.006s
                cd_012_496()
                Progress(r"244 files already in cache", own_progress_count=244, prog_num=740)()  # 0m:0.000s
                with Stage(r"post_sync", prog_num=741):  # 0m:0.006s
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=742) as copy_file_to_file_013_742:  # 0m:0.006s
                        copy_file_to_file_013_742()
            Progress(r"Done sync", prog_num=743)()  # 0m:0.000s
    with Stage(r"copy", prog_num=744):  # 0m:12.547s
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=745) as run_in_thread_014_745:  # 0m:0.000s
            run_in_thread_014_745()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=746)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=747):  # 0m:0.066s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=748) as make_dir_015_748:  # 0m:0.003s
                make_dir_015_748()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=749) as make_dir_016_749:  # 0m:0.003s
                make_dir_016_749()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=750) as make_dir_017_750:  # 0m:0.007s
                make_dir_017_750()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=751) as make_dir_018_751:  # 0m:0.003s
                make_dir_018_751()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=752) as make_dir_019_752:  # 0m:0.003s
                make_dir_019_752()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=753) as make_dir_020_753:  # 0m:0.004s
                make_dir_020_753()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=754) as make_dir_021_754:  # 0m:0.003s
                make_dir_021_754()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=755) as make_dir_022_755:  # 0m:0.004s
                make_dir_022_755()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=756) as make_dir_023_756:  # 0m:0.003s
                make_dir_023_756()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=757) as make_dir_024_757:  # 0m:0.003s
                make_dir_024_757()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=758) as make_dir_025_758:  # 0m:0.004s
                make_dir_025_758()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=759) as make_dir_026_759:  # 0m:0.003s
                make_dir_026_759()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=760) as make_dir_027_760:  # 0m:0.004s
                make_dir_027_760()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=761) as make_dir_028_761:  # 0m:0.003s
                make_dir_028_761()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=762) as make_dir_029_762:  # 0m:0.004s
                make_dir_029_762()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=763) as make_dir_030_763:  # 0m:0.003s
                make_dir_030_763()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=764) as make_dir_031_764:  # 0m:0.007s
                make_dir_031_764()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=765) as rm_file_or_dir_032_765:  # 0m:0.000s
            rm_file_or_dir_032_765()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=766) as shell_command_033_766:  # 0m:0.007s
            shell_command_033_766()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=767) as shell_command_034_767:  # 0m:0.010s
            shell_command_034_767()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=768) as shell_command_035_768:  # 0m:1.050s
            shell_command_035_768()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=769) as shell_command_036_769:  # 0m:0.005s
            shell_command_036_769()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=770) as shell_command_037_770:  # 0m:1.062s
            shell_command_037_770()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=771) as shell_command_038_771:  # 0m:0.011s
            shell_command_038_771()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=772) as shell_command_039_772:  # 0m:0.005s
            shell_command_039_772()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=773) as shell_command_040_773:  # 0m:0.157s
            shell_command_040_773()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=774) as cd_stage_041_774:  # 0m:0.009s
            cd_stage_041_774()
            with SetExecPermissionsInSyncFolder(prog_num=775) as set_exec_permissions_in_sync_folder_042_775:  # 0m:0.009s
                set_exec_permissions_in_sync_folder_042_775()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=776) as cd_stage_043_776:  # 0m:1.463s
            cd_stage_043_776()
            with Stage(r"copy", r"CLA Bass v15.5.79.262", prog_num=777):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=778) as should_copy_source_044_778:  # ?
                    should_copy_source_044_778()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=779):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=780) as copy_dir_to_dir_045_780:  # ?
                            copy_dir_to_dir_045_780()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=781) as unwtar_046_781:  # ?
                            unwtar_046_781()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=782, recursive=True) as chown_047_782:  # 0m:0.001s
                            chown_047_782()
            with Stage(r"copy", r"CLA Vocals v15.5.79.262", prog_num=783):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=784) as should_copy_source_048_784:  # ?
                    should_copy_source_048_784()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=785):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=786) as copy_dir_to_dir_049_786:  # ?
                            copy_dir_to_dir_049_786()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=787) as unwtar_050_787:  # ?
                            unwtar_050_787()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=788, recursive=True) as chown_051_788:  # 0m:0.000s
                            chown_051_788()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=789):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=790) as should_copy_source_052_790:  # ?
                    should_copy_source_052_790()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=791):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=792) as copy_dir_to_dir_053_792:  # ?
                            copy_dir_to_dir_053_792()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=793) as unwtar_054_793:  # ?
                            unwtar_054_793()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=794, recursive=True) as chown_055_794:  # 0m:0.001s
                            chown_055_794()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=2, prog_num=796) as resolve_symlink_files_in_folder_056_796:  # 0m:1.214s
                resolve_symlink_files_in_folder_056_796()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=797) as shell_command_057_797:  # 0m:0.102s
                shell_command_057_797()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=798) as script_command_058_798:  # 0m:0.008s
                script_command_058_798()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=799) as shell_command_059_799:  # 0m:0.017s
                shell_command_059_799()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=800) as create_symlink_060_800:  # 0m:0.001s
                create_symlink_060_800()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=801) as create_symlink_061_801:  # 0m:0.000s
                create_symlink_061_801()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=802) as copy_glob_to_dir_062_802:  # 0m:0.119s
                copy_glob_to_dir_062_802()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=803) as cd_stage_063_803:  # 0m:0.000s
            cd_stage_063_803()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=804):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=805) as should_copy_source_064_805:  # ?
                    should_copy_source_064_805()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=806):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=807) as copy_file_to_dir_065_807:  # ?
                            copy_file_to_dir_065_807()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=808) as chmod_and_chown_066_808:  # 0m:0.000s
                            chmod_and_chown_066_808()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=809) as cd_stage_067_809:  # 0m:0.012s
            cd_stage_067_809()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=810):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=811) as should_copy_source_068_811:  # ?
                    should_copy_source_068_811()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=812):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=813) as copy_dir_to_dir_069_813:  # ?
                            copy_dir_to_dir_069_813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=814) as unwtar_070_814:  # ?
                            unwtar_070_814()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=815, recursive=True) as chown_071_815:  # ?
                            chown_071_815()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=816) as shell_command_072_816:  # 0m:0.001s
                            shell_command_072_816()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=817):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=818) as should_copy_source_073_818:  # ?
                    should_copy_source_073_818()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=819):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=820) as copy_dir_to_dir_074_820:  # ?
                            copy_dir_to_dir_074_820()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=821) as unwtar_075_821:  # ?
                            unwtar_075_821()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=822, recursive=True) as chown_076_822:  # ?
                            chown_076_822()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=823) as break_hard_link_077_823:  # ?
                            break_hard_link_077_823()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=824) as shell_command_078_824:  # ?
                            shell_command_078_824()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=825, recursive=True) as chown_079_825:  # ?
                            chown_079_825()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=826, recursive=True) as chmod_080_826:  # 0m:0.001s
                            chmod_080_826()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=827):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=828) as should_copy_source_081_828:  # ?
                    should_copy_source_081_828()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=829):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=830) as copy_dir_to_dir_082_830:  # ?
                            copy_dir_to_dir_082_830()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=831) as unwtar_083_831:  # ?
                            unwtar_083_831()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=832, recursive=True) as chown_084_832:  # ?
                            chown_084_832()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=833) as shell_command_085_833:  # 0m:0.000s
                            shell_command_085_833()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=834):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=835) as should_copy_source_086_835:  # ?
                    should_copy_source_086_835()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=836):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=837) as copy_dir_to_dir_087_837:  # ?
                            copy_dir_to_dir_087_837()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=838) as unwtar_088_838:  # ?
                            unwtar_088_838()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=839, recursive=True) as chown_089_839:  # ?
                            chown_089_839()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=840) as shell_command_090_840:  # ?
                            shell_command_090_840()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=841) as script_command_091_841:  # ?
                            script_command_091_841()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=842) as shell_command_092_842:  # 0m:0.000s
                            shell_command_092_842()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=843):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=844) as should_copy_source_093_844:  # ?
                    should_copy_source_093_844()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=845):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=846) as copy_dir_to_dir_094_846:  # ?
                            copy_dir_to_dir_094_846()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=847) as unwtar_095_847:  # ?
                            unwtar_095_847()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=848, recursive=True) as chown_096_848:  # 0m:0.000s
                            chown_096_848()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=849) as shell_command_097_849:  # 0m:0.008s
                shell_command_097_849()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=850) as cd_stage_098_850:  # 0m:0.001s
            cd_stage_098_850()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=851):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=852) as should_copy_source_099_852:  # ?
                    should_copy_source_099_852()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=853):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=854) as copy_dir_to_dir_100_854:  # ?
                            copy_dir_to_dir_100_854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=855) as unwtar_101_855:  # ?
                            unwtar_101_855()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=856, recursive=True) as chown_102_856:  # ?
                            chown_102_856()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=857) as shell_command_103_857:  # 0m:0.001s
                            shell_command_103_857()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=858) as cd_stage_104_858:  # 0m:0.001s
            cd_stage_104_858()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=859):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=860) as should_copy_source_105_860:  # ?
                    should_copy_source_105_860()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=861):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=862) as copy_dir_to_dir_106_862:  # ?
                            copy_dir_to_dir_106_862()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=863, recursive=True) as chown_107_863:  # 0m:0.000s
                            chown_107_863()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=864) as cd_stage_108_864:  # 0m:0.004s
            cd_stage_108_864()
            with Stage(r"copy", r"License Notifications 1.1 v1.1", prog_num=865):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=866) as should_copy_source_109_866:  # ?
                    should_copy_source_109_866()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=867):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=868) as copy_dir_to_dir_110_868:  # ?
                            copy_dir_to_dir_110_868()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=869, recursive=True) as chown_111_869:  # 0m:0.004s
                            chown_111_869()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=870) as cd_stage_112_870:  # 0m:4.368s
            cd_stage_112_870()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=871) as rm_file_or_dir_113_871:  # 0m:0.000s
                rm_file_or_dir_113_871()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=872):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=873) as should_copy_source_114_873:  # ?
                    should_copy_source_114_873()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=874):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=875) as copy_dir_to_dir_115_875:  # ?
                            copy_dir_to_dir_115_875()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=876) as unwtar_116_876:  # ?
                            unwtar_116_876()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=877, recursive=True) as chown_117_877:  # 0m:0.000s
                            chown_117_877()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=878):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=879) as should_copy_source_118_879:  # 0m:0.004s
                    should_copy_source_118_879()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=880):  # 0m:0.004s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=881) as unwtar_119_881:  # 0m:0.004s
                            unwtar_119_881()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=882):  # 0m:4.348s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=883) as should_copy_source_120_883:  # 0m:4.348s
                    should_copy_source_120_883()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=884):  # 0m:4.347s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=885) as copy_dir_to_dir_121_885:  # 0m:0.012s
                            copy_dir_to_dir_121_885()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=886) as unwtar_122_886:  # 0m:4.335s
                            unwtar_122_886()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=887, recursive=True) as chown_123_887:  # 0m:0.000s
                            chown_123_887()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=888):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=889) as should_copy_source_124_889:  # ?
                    should_copy_source_124_889()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=890):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=891) as copy_dir_to_dir_125_891:  # ?
                            copy_dir_to_dir_125_891()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=892) as chmod_126_892:  # ?
                            chmod_126_892()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=893) as chmod_127_893:  # ?
                            chmod_127_893()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=894, recursive=True) as chown_128_894:  # 0m:0.000s
                            chown_128_894()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=897) as resolve_symlink_files_in_folder_129_897:  # 0m:0.003s
                resolve_symlink_files_in_folder_129_897()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=898) as shell_command_130_898:  # 0m:0.012s
                shell_command_130_898()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=899) as cd_stage_131_899:  # 0m:0.001s
            cd_stage_131_899()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=900):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=901) as should_copy_source_132_901:  # ?
                    should_copy_source_132_901()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=902):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=903) as copy_dir_to_dir_133_903:  # ?
                            copy_dir_to_dir_133_903()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=904, recursive=True) as chown_134_904:  # 0m:0.000s
                            chown_134_904()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=905) as cd_stage_135_905:  # 0m:0.001s
            cd_stage_135_905()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=906):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=907) as should_copy_source_136_907:  # ?
                    should_copy_source_136_907()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=908):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=909, recursive=True) as chmod_137_909:  # ?
                            chmod_137_909()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=910) as copy_dir_to_dir_138_910:  # ?
                            copy_dir_to_dir_138_910()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=911) as unwtar_139_911:  # ?
                            unwtar_139_911()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=912, recursive=True) as chown_140_912:  # ?
                            chown_140_912()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=913) as if_141_913:  # 0m:0.001s
                            if_141_913()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=914) as cd_stage_142_914:  # 0m:1.027s
            cd_stage_142_914()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=915):  # 0m:1.026s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=916) as should_copy_source_143_916:  # 0m:1.026s
                    should_copy_source_143_916()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=917):  # 0m:1.026s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=918) as copy_dir_to_dir_144_918:  # 0m:0.079s
                            copy_dir_to_dir_144_918()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=919) as unwtar_145_919:  # 0m:0.884s
                            unwtar_145_919()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=920, recursive=True) as chown_146_920:  # 0m:0.000s
                            chown_146_920()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=921) as break_hard_link_147_921:  # 0m:0.011s
                            break_hard_link_147_921()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=922) as shell_command_148_922:  # 0m:0.045s
                            shell_command_148_922()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=923, recursive=True) as chown_149_923:  # 0m:0.000s
                            chown_149_923()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=924, recursive=True) as chmod_150_924:  # 0m:0.006s
                            chmod_150_924()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=925) as cd_stage_151_925:  # 0m:0.001s
            cd_stage_151_925()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=926):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=927) as should_copy_source_152_927:  # ?
                    should_copy_source_152_927()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=928):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=929) as copy_dir_to_dir_153_929:  # ?
                            copy_dir_to_dir_153_929()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=930) as unwtar_154_930:  # ?
                            unwtar_154_930()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=931, recursive=True) as chown_155_931:  # ?
                            chown_155_931()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=932) as shell_command_156_932:  # 0m:0.001s
                            shell_command_156_932()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=933) as cd_stage_157_933:  # 0m:0.001s
            cd_stage_157_933()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=934):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=935) as should_copy_source_158_935:  # ?
                    should_copy_source_158_935()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=936):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=937) as copy_dir_to_dir_159_937:  # ?
                            copy_dir_to_dir_159_937()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=938) as unwtar_160_938:  # ?
                            unwtar_160_938()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=939, recursive=True) as chown_161_939:  # ?
                            chown_161_939()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=940) as shell_command_162_940:  # ?
                            shell_command_162_940()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=941) as script_command_163_941:  # ?
                            script_command_163_941()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=942) as shell_command_164_942:  # 0m:0.000s
                            shell_command_164_942()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=943) as create_symlink_165_943:  # 0m:0.000s
                create_symlink_165_943()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=944) as create_symlink_166_944:  # 0m:0.000s
                create_symlink_166_944()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=945) as rm_file_or_dir_167_945:  # 0m:0.386s
            rm_file_or_dir_167_945()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=946) as shell_command_168_946:  # 0m:0.098s
            shell_command_168_946()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=947) as script_command_169_947:  # 0m:0.007s
            script_command_169_947()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=948) as rm_file_or_dir_170_948:  # 0m:0.001s
            rm_file_or_dir_170_948()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=949) as glober_171_949:  # 0m:0.004s
            glober_171_949()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=950) as glober_172_950:  # 0m:0.004s
            glober_172_950()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=951) as glober_173_951:  # 0m:0.002s
            glober_173_951()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=952) as shell_command_174_952:  # 0m:2.671s
            shell_command_174_952()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=953) as shell_command_175_953:  # 0m:0.099s
            shell_command_175_953()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=954) as script_command_176_954:  # 0m:0.007s
            script_command_176_954()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=955) as if_177_955:  # 0m:0.006s
            if_177_955()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=956) as if_178_956:  # 0m:0.000s
            if_178_956()
    with Stage(r"post-copy", prog_num=957):  # 0m:0.028s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=958) as make_dir_179_958:  # 0m:0.007s
            make_dir_179_958()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=959) as copy_file_to_file_180_959:  # 0m:0.006s
            copy_file_to_file_180_959()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=960) as chmod_181_960:  # 0m:0.000s
            chmod_181_960()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=961) as chmod_182_961:  # 0m:0.000s
            chmod_182_961()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=962) as copy_file_to_file_183_962:  # 0m:0.007s
            copy_file_to_file_183_962()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=963) as chmod_184_963:  # 0m:0.000s
            chmod_184_963()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=964) as copy_file_to_file_185_964:  # 0m:0.007s
            copy_file_to_file_185_964()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=965) as chmod_186_965:  # 0m:0.000s
            chmod_186_965()
        Progress(r"Done copy", prog_num=966)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=967)()  # 0m:0.000s
    with Stage(r"post", prog_num=968):  # 0m:0.036s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=969) as make_dir_187_969:  # 0m:0.004s
            make_dir_187_969()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=970) as copy_file_to_file_188_970:  # 0m:0.007s
            copy_file_to_file_188_970()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=971) as make_dir_189_971:  # 0m:0.006s
            make_dir_189_971()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=972) as copy_file_to_file_190_972:  # 0m:0.008s
            copy_file_to_file_190_972()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=973) as make_dir_191_973:  # 0m:0.004s
            make_dir_191_973()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=974) as copy_file_to_file_192_974:  # 0m:0.006s
            copy_file_to_file_192_974()

with Stage(r"epilog", prog_num=975):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250629165446.py", prog_num=976) as patch_py_batch_with_timings_193_976:  # ?
        patch_py_batch_with_timings_193_976()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# copy time 0m:12.547s
