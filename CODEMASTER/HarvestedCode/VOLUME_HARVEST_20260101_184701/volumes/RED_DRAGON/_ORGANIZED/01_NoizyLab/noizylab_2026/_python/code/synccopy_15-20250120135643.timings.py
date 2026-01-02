# Creation time: 20-01-25_13-57
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 13419
PythonBatchCommandBase.running_progress = 1159
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1160):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250120135643"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", r"/Applications/Waves/Data", r"/Applications/Waves/Data", r"/Applications/Waves/Data", r"/Applications/Waves/Data/Instrument Data/NKS", r"/Applications/Waves/Data/Instrument Data/NKS", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/Presets", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.3.3"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V15", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V15", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 31
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczNzQzNTQwNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzM3Mzk5MTA0fX19XX0_;CloudFront-Signature=Hkkr5vwfI2S2vlfQ8J~HZTIJvWab9QB81qQX5W4NCzXbqicWlfHGKBZRRcGy9~5g9lEFErNSHl-D2Nx5BcTQNJqzUDgAEOH70h-kAJLtpYioYJajoTGcS5HDAHg6n9ZB3xhrJvGwpbAh8YcvyC9kqQyKyo5wDfDAGPXOPnUS6DsyVRmT91JcyDncX5MQDe~xvdF80udhwya8GBjGj6ZeTOVL5xtwWKXO3V3glMPTcrVj27z8wd9JlP8VztKdcdGL~7K2BuVLS~QfbX9waLDVKC05ltIKiY5kIYa~wxVsiYJN9imLXSuCEUNzsJ21NgJecFK06NDNTB0QbVoLJ6G9lQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTczNzQzNTQwNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzM3Mzk5MTA0fX19XX0_;CloudFront-Signature=Hkkr5vwfI2S2vlfQ8J~HZTIJvWab9QB81qQX5W4NCzXbqicWlfHGKBZRRcGy9~5g9lEFErNSHl-D2Nx5BcTQNJqzUDgAEOH70h-kAJLtpYioYJajoTGcS5HDAHg6n9ZB3xhrJvGwpbAh8YcvyC9kqQyKyo5wDfDAGPXOPnUS6DsyVRmT91JcyDncX5MQDe~xvdF80udhwya8GBjGj6ZeTOVL5xtwWKXO3V3glMPTcrVj27z8wd9JlP8VztKdcdGL~7K2BuVLS~QfbX9waLDVKC05ltIKiY5kIYa~wxVsiYJN9imLXSuCEUNzsJ21NgJecFK06NDNTB0QbVoLJ6G9lQ__"
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['CREATE_APP_SHORTCUTS'] = r"yes"
    config_vars['CURL_CONFIG_FILE_NAME'] = r"dl"
    config_vars['CURL_CONNECT_TIMEOUT'] = 32
    config_vars['CURL_MAX_TIME'] = 600
    config_vars['CURL_RETRIES'] = 6
    config_vars['CURL_RETRY_DELAY'] = 12
    config_vars['CUSTOM_HEADERS'] = r'register.waves.com:{"Client-Name":"Waves Central"}'
    config_vars['Clean_old_plist_Native_NI'] = "If(IsConfigVarDefined(\"POST_INSTALL_SCRIPT_FILE\"), if_true=ScriptCommand(r\"\"\"echo rm -f \\\"$(__Clean_old_plist_Native_NI_1__)\\\" >> \"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh\" ;chmod a+rwx \"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh\" \"\"\"),if_false=RmFileOrDir(r\'\'\'$(__Clean_old_plist_Native_NI_1__)\'\'\'))"
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DEFAULT_IID_VERSION'] = r"0.0.0"
    config_vars['DIRECT_SYNC_INSTRUMENT_DATA'] = r"yes"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+")
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
    config_vars['INDEX_CHECKSUM'] = r"a2682782824bf8869ecc13e49254be7494935dd9"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/31/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"4aff4a43dfd859e7a622c3c331ecc840437f2166"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/31/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/31/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_INSTALL_TARGETS'] = r"__REPAIR_INSTALLED_ITEMS__"
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 31
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250120135643.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 16
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 31
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-01-19 08:23:59.602700"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/31"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V15"
    config_vars['REQUIRE_REPO_REV'] = 31
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"56b0784b7f4ff0d4f196902acdf2b541f5c33726"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/31/instl/short-index.yaml"
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
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"after-sync-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 12255
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
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250120135643.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2024-12-26 10:46:09.983540"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.2"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Q_Clone_Presets_IID", r"Waves_Audio_Factory_Pack_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS__Data_Folders__IID", r"COSMOS__IID", r"COSMOS__Models_Data_Folders__IID", r"COSMOS_python_IID", r"Center_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Enigma_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"Get_General_Icons_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LicenseNotifications_1_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"ORS_Modulators_Data_IID", r"OpenVino_IID", r"PAZ_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"ReWire_IID", r"ReWire_backup_IID", r"Reel_ADT_IID", r"Remove_9_6_leftovers_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"SOC_Presets_IID", r"Sample_Libraries_Locations_Folder_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"SuperTap_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"WLM_IID", r"WLM_Plus_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_15_5_79_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V15_2_IID", r"WavesReWireDevice_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Audio_Factory_Pack_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__GITHUB_BRANCH__'] = r"python3.9"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.4.2.3 2024-12-26 10:46:09.983540 bm-mac4"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.4.2.3"
    config_vars['__INSTL_VERSION__'] = (2, 4, 2, 3)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"wqayzjnknokgkgcg"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS__IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Audio_Factory_Pack_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-01-20 13:58:30.329880"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 4050180330
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 40
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"bm-mac4"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_COMPILER__'] = r"site-packages"
    config_vars['__PYTHON_VERSION__'] = (3, 9, 4, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"bm-mac4"
    config_vars['__SQLITE_VERSION__'] = r"3.34.0"
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

with PythonBatchRuntime(r"synccopy", prog_num=1161):  # 4m:36.361s
    with Stage(r"begin", prog_num=1162):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1163):  # 0m:0.017s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1164) as copy_file_to_file_001_1164:  # 0m:0.010s
            copy_file_to_file_001_1164()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1165) as copy_file_to_file_002_1165:  # 0m:0.007s
            copy_file_to_file_002_1165()
    with Stage(r"sync", prog_num=1166):  # 1m:46.805s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1167) as shell_command_003_1167:  # 0m:0.009s
            shell_command_003_1167()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1168) as shell_command_004_1168:  # 0m:0.013s
            shell_command_004_1168()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1169) as shell_command_005_1169:  # 0m:0.991s
            shell_command_005_1169()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1170) as shell_command_006_1170:  # 0m:0.010s
            shell_command_006_1170()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1171) as shell_command_007_1171:  # 0m:44.155s
            shell_command_007_1171()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1172) as shell_command_008_1172:  # 0m:0.011s
            shell_command_008_1172()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1173) as shell_command_009_1173:  # 0m:0.010s
            shell_command_009_1173()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1174) as shell_command_010_1174:  # 0m:0.237s
            shell_command_010_1174()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=1175):  # 1m:1.369s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=1176) as make_dir_011_1176:  # 0m:0.009s
                make_dir_011_1176()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=1177) as cd_012_1177:  # 1m:1.359s
                cd_012_1177()
                Progress(r"9980 files already in cache", own_progress_count=9980, prog_num=11157)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=6, prog_num=11163) as create_sync_folders_013_11163:  # 0m:0.047s
                    create_sync_folders_013_11163()
                Progress(r"Downloading with 16 processes in parallel", prog_num=11164)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=11165)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.py_curl/dl-00", total_files_to_download=40, previously_downloaded_files=0, total_bytes_to_download=4050180330, own_progress_count=40, prog_num=11205, report_own_progress=False) as curl_with_internal_parallel_014_11205:  # 0m:58.430s
                    curl_with_internal_parallel_014_11205()
                Progress(r"Downloading 40 files done", prog_num=11206)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=11207) as run_in_thread_015_11207:  # 0m:0.000s
                    run_in_thread_015_11207()
                Progress(r"Check checksum ...", prog_num=11208)()  # 0m:0.000s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=40, prog_num=11248) as check_download_folder_checksum_016_11248:  # 0m:2.839s
                    check_download_folder_checksum_016_11248()
                with Stage(r"post_sync", prog_num=11249):  # 0m:0.041s
                    Progress(r"Adjust ownership and permissions /Applications/Waves/Data/Instrument Data/NKS/Electric Grand 80...", prog_num=11250)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Applications/Waves/Data/Instrument Data/NKS/Electric Grand 80", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=11251, recursive=True) as chmod_and_chown_017_11251:  # 0m:0.010s
                        chmod_and_chown_017_11251()
                    Progress(r"Adjust ownership and permissions /Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack...", prog_num=11252)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=11253, recursive=True) as chmod_and_chown_018_11253:  # 0m:0.013s
                        chmod_and_chown_018_11253()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=11254) as copy_file_to_file_019_11254:  # 0m:0.016s
                        copy_file_to_file_019_11254()
            Progress(r"Done sync", prog_num=11255)()  # 0m:0.000s
    with Stage(r"copy", prog_num=11256):  # 2m:49.447s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11257)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=11258):  # 0m:0.334s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=11259) as make_dir_020_11259:  # 0m:0.011s
                make_dir_020_11259()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=11260) as make_dir_021_11260:  # 0m:0.006s
                make_dir_021_11260()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=11261) as make_dir_022_11261:  # 0m:0.012s
                make_dir_022_11261()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=11262) as make_dir_023_11262:  # 0m:0.011s
                make_dir_023_11262()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=11263) as make_dir_024_11263:  # 0m:0.006s
                make_dir_024_11263()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=11264) as make_dir_025_11264:  # 0m:0.009s
                make_dir_025_11264()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=11265) as make_dir_026_11265:  # 0m:0.010s
                make_dir_026_11265()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=11266) as make_dir_027_11266:  # 0m:0.009s
                make_dir_027_11266()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=11267) as make_dir_028_11267:  # 0m:0.009s
                make_dir_028_11267()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=11268) as make_dir_029_11268:  # 0m:0.006s
                make_dir_029_11268()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=11269) as make_dir_030_11269:  # 0m:0.010s
                make_dir_030_11269()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=11270) as make_dir_031_11270:  # 0m:0.007s
                make_dir_031_11270()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=11271) as make_dir_032_11271:  # 0m:0.009s
                make_dir_032_11271()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=11272) as make_dir_033_11272:  # 0m:0.011s
                make_dir_033_11272()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=11273) as make_dir_034_11273:  # 0m:0.011s
                make_dir_034_11273()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=11274) as make_dir_035_11274:  # 0m:0.009s
                make_dir_035_11274()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/GTR", chowner=True, prog_num=11275) as make_dir_036_11275:  # 0m:0.010s
                make_dir_036_11275()
            with MakeDir(r"/Applications/Waves/ReWire", chowner=True, prog_num=11276) as make_dir_037_11276:  # 0m:0.009s
                make_dir_037_11276()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=11277) as make_dir_038_11277:  # 0m:0.009s
                make_dir_038_11277()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=11278) as make_dir_039_11278:  # 0m:0.009s
                make_dir_039_11278()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=11279) as make_dir_040_11279:  # 0m:0.006s
                make_dir_040_11279()
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=11280) as make_dir_041_11280:  # 0m:0.008s
                make_dir_041_11280()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=11281) as make_dir_042_11281:  # 0m:0.006s
                make_dir_042_11281()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=11282) as make_dir_043_11282:  # 0m:0.009s
                make_dir_043_11282()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=11283) as make_dir_044_11283:  # 0m:0.009s
                make_dir_044_11283()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=11284) as make_dir_045_11284:  # 0m:0.006s
                make_dir_045_11284()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=11285) as make_dir_046_11285:  # 0m:0.017s
                make_dir_046_11285()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=11286) as make_dir_047_11286:  # 0m:0.007s
                make_dir_047_11286()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=11287) as make_dir_048_11287:  # 0m:0.017s
                make_dir_048_11287()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=11288) as make_dir_049_11288:  # 0m:0.006s
                make_dir_049_11288()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=11289) as make_dir_050_11289:  # 0m:0.007s
                make_dir_050_11289()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=11290) as make_dir_051_11290:  # 0m:0.006s
                make_dir_051_11290()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=11291) as make_dir_052_11291:  # 0m:0.007s
                make_dir_052_11291()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=11292) as make_dir_053_11292:  # 0m:0.006s
                make_dir_053_11292()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=11293) as make_dir_054_11293:  # 0m:0.007s
                make_dir_054_11293()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=11294) as make_dir_055_11294:  # 0m:0.006s
                make_dir_055_11294()
            with MakeDir(r"/Users/Shared/Waves/Sample Libraries Locations", chowner=True, prog_num=11295) as make_dir_056_11295:  # 0m:0.009s
                make_dir_056_11295()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=11296) as make_dir_057_11296:  # 0m:0.008s
                make_dir_057_11296()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=11297) as rm_file_or_dir_058_11297:  # 0m:0.004s
            rm_file_or_dir_058_11297()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=11298) as rm_file_or_dir_059_11298:  # 0m:0.000s
            rm_file_or_dir_059_11298()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=11299) as shell_command_060_11299:  # 0m:0.012s
            shell_command_060_11299()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=11300) as shell_command_061_11300:  # 0m:0.017s
            shell_command_061_11300()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=11301) as shell_command_062_11301:  # 0m:1.020s
            shell_command_062_11301()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11302) as shell_command_063_11302:  # 0m:0.013s
            shell_command_063_11302()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11303) as shell_command_064_11303:  # 0m:1.047s
            shell_command_064_11303()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=11304) as shell_command_065_11304:  # 0m:0.012s
            shell_command_065_11304()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=11305) as shell_command_066_11305:  # 0m:0.011s
            shell_command_066_11305()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=11306) as shell_command_067_11306:  # 0m:0.171s
            shell_command_067_11306()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11307) as cd_stage_068_11307:  # 0m:0.015s
            cd_stage_068_11307()
            with SetExecPermissionsInSyncFolder(prog_num=11308) as set_exec_permissions_in_sync_folder_069_11308:  # 0m:0.014s
                set_exec_permissions_in_sync_folder_069_11308()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=11309) as cd_stage_070_11309:  # 0m:1.312s
            cd_stage_070_11309()
            with Stage(r"copy", r"Bass Slapper application v15.5.79.262", prog_num=11310):  # 0m:0.372s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11311) as should_copy_source_071_11311:  # 0m:0.371s
                    should_copy_source_071_11311()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=11312):  # 0m:0.371s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=11313) as copy_dir_to_dir_072_11313:  # 0m:0.031s
                            copy_dir_to_dir_072_11313()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=11314) as unwtar_073_11314:  # 0m:0.340s
                            unwtar_073_11314()
                        with Chown(path=r"/Applications/Waves/Applications V15/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=11315, recursive=True) as chown_074_11315:  # 0m:0.000s
                            chown_074_11315()
            with Stage(r"copy", r"Electric Grand 80 application v15.5.79.262", prog_num=11316):  # 0m:0.408s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11317) as should_copy_source_075_11317:  # 0m:0.408s
                    should_copy_source_075_11317()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=11318):  # 0m:0.408s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=11319) as copy_dir_to_dir_076_11319:  # 0m:0.037s
                            copy_dir_to_dir_076_11319()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=11320) as unwtar_077_11320:  # 0m:0.370s
                            unwtar_077_11320()
                        with Chown(path=r"/Applications/Waves/Applications V15/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=11321, recursive=True) as chown_078_11321:  # 0m:0.000s
                            chown_078_11321()
            with Stage(r"copy", r"GTR application v15.5.79.262", prog_num=11322):  # 0m:0.400s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11323) as should_copy_source_079_11323:  # 0m:0.400s
                    should_copy_source_079_11323()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=11324):  # 0m:0.400s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=11325) as copy_dir_to_dir_080_11325:  # 0m:0.038s
                            copy_dir_to_dir_080_11325()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=11326) as unwtar_081_11326:  # 0m:0.361s
                            unwtar_081_11326()
                        with Chown(path=r"/Applications/Waves/Applications V15/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=11327, recursive=True) as chown_082_11327:  # 0m:0.000s
                            chown_082_11327()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=11328) as shell_command_083_11328:  # 0m:0.119s
                shell_command_083_11328()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=11329) as script_command_084_11329:  # 0m:0.012s
                script_command_084_11329()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=11330) as cd_stage_085_11330:  # 0m:17.129s
            cd_stage_085_11330()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=11331):  # 0m:17.114s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=11332) as should_copy_source_086_11332:  # 0m:17.114s
                    should_copy_source_086_11332()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=11333):  # 0m:17.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=11334) as copy_dir_to_dir_087_11334:  # 0m:0.281s
                            copy_dir_to_dir_087_11334()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=11335) as unwtar_088_11335:  # 0m:16.832s
                            unwtar_088_11335()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=11336, recursive=True) as chown_089_11336:  # 0m:0.000s
                            chown_089_11336()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=11346) as resolve_symlink_files_in_folder_090_11346:  # 0m:0.014s
                resolve_symlink_files_in_folder_090_11346()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=11347) as cd_stage_091_11347:  # 0m:6.159s
            cd_stage_091_11347()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=11348):  # 0m:0.016s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11349) as should_copy_source_092_11349:  # 0m:0.016s
                    should_copy_source_092_11349()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=11350):  # 0m:0.016s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=11351) as copy_dir_to_dir_093_11351:  # 0m:0.015s
                            copy_dir_to_dir_093_11351()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=11352, recursive=True) as chown_094_11352:  # 0m:0.000s
                            chown_094_11352()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=11353):  # 0m:5.834s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11354) as should_copy_source_095_11354:  # 0m:5.834s
                    should_copy_source_095_11354()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=11355):  # 0m:5.834s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=11356) as copy_dir_to_dir_096_11356:  # 0m:0.013s
                            copy_dir_to_dir_096_11356()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=11357) as unwtar_097_11357:  # 0m:5.820s
                            unwtar_097_11357()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=11358, recursive=True) as chown_098_11358:  # 0m:0.001s
                            chown_098_11358()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=11359):  # 0m:0.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11360) as should_copy_source_099_11360:  # 0m:0.074s
                    should_copy_source_099_11360()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=11361):  # 0m:0.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=11362) as copy_dir_to_dir_100_11362:  # 0m:0.073s
                            copy_dir_to_dir_100_11362()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=11363, recursive=True) as chown_101_11363:  # 0m:0.000s
                            chown_101_11363()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=11364):  # 0m:0.037s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11365) as should_copy_source_102_11365:  # 0m:0.037s
                    should_copy_source_102_11365()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=11366):  # 0m:0.036s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11367) as copy_dir_to_dir_103_11367:  # 0m:0.036s
                            copy_dir_to_dir_103_11367()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=11368, recursive=True) as chown_104_11368:  # 0m:0.000s
                            chown_104_11368()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=11369):  # 0m:0.046s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11370) as should_copy_source_105_11370:  # 0m:0.046s
                    should_copy_source_105_11370()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=11371):  # 0m:0.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=11372) as copy_dir_to_dir_106_11372:  # 0m:0.046s
                            copy_dir_to_dir_106_11372()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=11373, recursive=True) as chown_107_11373:  # 0m:0.000s
                            chown_107_11373()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=11374):  # 0m:0.062s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11375) as should_copy_source_108_11375:  # 0m:0.062s
                    should_copy_source_108_11375()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=11376):  # 0m:0.061s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=11377) as copy_dir_to_dir_109_11377:  # 0m:0.061s
                            copy_dir_to_dir_109_11377()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=11378, recursive=True) as chown_110_11378:  # 0m:0.000s
                            chown_110_11378()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=11379):  # 0m:0.090s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11380) as should_copy_source_111_11380:  # 0m:0.090s
                    should_copy_source_111_11380()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=11381):  # 0m:0.089s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=11382) as copy_dir_to_dir_112_11382:  # 0m:0.053s
                            copy_dir_to_dir_112_11382()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=11383) as unwtar_113_11383:  # 0m:0.036s
                            unwtar_113_11383()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=11384, recursive=True) as chown_114_11384:  # 0m:0.000s
                            chown_114_11384()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=11385) as cd_stage_115_11385:  # 0m:10.896s
            cd_stage_115_11385()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=11386):  # 0m:10.895s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=11387) as should_copy_source_116_11387:  # 0m:0.001s
                    should_copy_source_116_11387()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=11388):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r".", prog_num=11389) as copy_file_to_dir_117_11389:  # 0m:0.001s
                            copy_file_to_dir_117_11389()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=11390) as chmod_and_chown_118_11390:  # 0m:0.000s
                            chmod_and_chown_118_11390()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=11391) as should_copy_source_119_11391:  # 0m:10.894s
                    should_copy_source_119_11391()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=11392):  # 0m:10.894s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=11393) as copy_dir_to_dir_120_11393:  # 0m:0.012s
                            copy_dir_to_dir_120_11393()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=11394) as unwtar_121_11394:  # 0m:10.881s
                            unwtar_121_11394()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=11395, recursive=True) as chown_122_11395:  # 0m:0.000s
                            chown_122_11395()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=11396) as cd_stage_123_11396:  # 0m:0.131s
            cd_stage_123_11396()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=11397):  # 0m:0.034s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11398) as should_copy_source_124_11398:  # 0m:0.019s
                    should_copy_source_124_11398()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=11399):  # 0m:0.018s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=11400) as copy_dir_to_dir_125_11400:  # 0m:0.018s
                            copy_dir_to_dir_125_11400()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=11401, recursive=True) as chown_126_11401:  # 0m:0.000s
                            chown_126_11401()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11402) as should_copy_source_127_11402:  # 0m:0.015s
                    should_copy_source_127_11402()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=11403):  # 0m:0.015s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=11404) as copy_dir_to_dir_128_11404:  # 0m:0.014s
                            copy_dir_to_dir_128_11404()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=11405, recursive=True) as chown_129_11405:  # 0m:0.000s
                            chown_129_11405()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=11406):  # 0m:0.097s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11407) as should_copy_source_130_11407:  # 0m:0.014s
                    should_copy_source_130_11407()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=11408):  # 0m:0.014s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=11409) as copy_dir_to_dir_131_11409:  # 0m:0.013s
                            copy_dir_to_dir_131_11409()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=11410, recursive=True) as chown_132_11410:  # 0m:0.000s
                            chown_132_11410()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11411) as should_copy_source_133_11411:  # 0m:0.082s
                    should_copy_source_133_11411()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=11412):  # 0m:0.082s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=11413) as copy_dir_to_dir_134_11413:  # 0m:0.081s
                            copy_dir_to_dir_134_11413()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=11414, recursive=True) as chown_135_11414:  # 0m:0.000s
                            chown_135_11414()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=11415) as cd_stage_136_11415:  # 0m:0.001s
            cd_stage_136_11415()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=11416):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=11417) as should_copy_source_137_11417:  # ?
                    should_copy_source_137_11417()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=11418):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=11419) as copy_file_to_dir_138_11419:  # ?
                            copy_file_to_dir_138_11419()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=11420) as chmod_and_chown_139_11420:  # 0m:0.000s
                            chmod_and_chown_139_11420()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=11421) as cd_stage_140_11421:  # 0m:9.361s
            cd_stage_140_11421()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=11422):  # 0m:0.030s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11423) as should_copy_source_141_11423:  # 0m:0.030s
                    should_copy_source_141_11423()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=11424):  # 0m:0.030s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=11425) as copy_dir_to_dir_142_11425:  # 0m:0.029s
                            copy_dir_to_dir_142_11425()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=11426, recursive=True) as chown_143_11426:  # 0m:0.000s
                            chown_143_11426()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=11427):  # 0m:0.714s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11428) as should_copy_source_144_11428:  # 0m:0.714s
                    should_copy_source_144_11428()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=11429):  # 0m:0.713s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=11430) as copy_dir_to_dir_145_11430:  # 0m:0.713s
                            copy_dir_to_dir_145_11430()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=11431, recursive=True) as chown_146_11431:  # 0m:0.000s
                            chown_146_11431()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=11432):  # 0m:0.534s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11433) as should_copy_source_147_11433:  # 0m:0.534s
                    should_copy_source_147_11433()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=11434):  # 0m:0.533s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11435) as copy_dir_to_dir_148_11435:  # 0m:0.533s
                            copy_dir_to_dir_148_11435()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=11436, recursive=True) as chown_149_11436:  # 0m:0.000s
                            chown_149_11436()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=11437):  # 0m:0.233s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11438) as should_copy_source_150_11438:  # 0m:0.232s
                    should_copy_source_150_11438()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=11439):  # 0m:0.232s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=11440) as copy_dir_to_dir_151_11440:  # 0m:0.232s
                            copy_dir_to_dir_151_11440()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=11441, recursive=True) as chown_152_11441:  # 0m:0.000s
                            chown_152_11441()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=11442):  # 0m:0.711s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11443) as should_copy_source_153_11443:  # 0m:0.711s
                    should_copy_source_153_11443()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=11444):  # 0m:0.711s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=11445) as copy_dir_to_dir_154_11445:  # 0m:0.710s
                            copy_dir_to_dir_154_11445()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=11446, recursive=True) as chown_155_11446:  # 0m:0.000s
                            chown_155_11446()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=11447):  # 0m:0.248s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11448) as should_copy_source_156_11448:  # 0m:0.248s
                    should_copy_source_156_11448()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=11449):  # 0m:0.248s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=11450) as copy_dir_to_dir_157_11450:  # 0m:0.247s
                            copy_dir_to_dir_157_11450()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=11451, recursive=True) as chown_158_11451:  # 0m:0.001s
                            chown_158_11451()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=11452):  # 0m:0.223s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11453) as should_copy_source_159_11453:  # 0m:0.223s
                    should_copy_source_159_11453()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=11454):  # 0m:0.216s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=11455) as copy_dir_to_dir_160_11455:  # 0m:0.215s
                            copy_dir_to_dir_160_11455()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=11456, recursive=True) as chown_161_11456:  # 0m:0.000s
                            chown_161_11456()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=11457):  # 0m:1.088s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11458) as should_copy_source_162_11458:  # 0m:1.088s
                    should_copy_source_162_11458()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=11459):  # 0m:1.087s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=11460) as copy_dir_to_dir_163_11460:  # 0m:1.087s
                            copy_dir_to_dir_163_11460()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=11461, recursive=True) as chown_164_11461:  # 0m:0.000s
                            chown_164_11461()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=11462):  # 0m:0.877s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11463) as should_copy_source_165_11463:  # 0m:0.877s
                    should_copy_source_165_11463()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=11464):  # 0m:0.876s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=11465) as copy_dir_to_dir_166_11465:  # 0m:0.876s
                            copy_dir_to_dir_166_11465()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=11466, recursive=True) as chown_167_11466:  # 0m:0.000s
                            chown_167_11466()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=11467):  # 0m:0.194s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11468) as should_copy_source_168_11468:  # 0m:0.194s
                    should_copy_source_168_11468()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=11469):  # 0m:0.194s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=11470) as copy_dir_to_dir_169_11470:  # 0m:0.193s
                            copy_dir_to_dir_169_11470()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=11471, recursive=True) as chown_170_11471:  # 0m:0.000s
                            chown_170_11471()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=11472):  # 0m:0.171s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11473) as should_copy_source_171_11473:  # 0m:0.171s
                    should_copy_source_171_11473()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=11474):  # 0m:0.171s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=11475) as copy_dir_to_dir_172_11475:  # 0m:0.171s
                            copy_dir_to_dir_172_11475()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=11476, recursive=True) as chown_173_11476:  # 0m:0.000s
                            chown_173_11476()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=11477):  # 0m:0.993s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11478) as should_copy_source_174_11478:  # 0m:0.993s
                    should_copy_source_174_11478()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=11479):  # 0m:0.992s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=11480) as copy_dir_to_dir_175_11480:  # 0m:0.992s
                            copy_dir_to_dir_175_11480()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=11481, recursive=True) as chown_176_11481:  # 0m:0.000s
                            chown_176_11481()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=11482):  # 0m:0.260s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11483) as should_copy_source_177_11483:  # 0m:0.260s
                    should_copy_source_177_11483()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=11484):  # 0m:0.260s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=11485) as copy_dir_to_dir_178_11485:  # 0m:0.259s
                            copy_dir_to_dir_178_11485()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=11486, recursive=True) as chown_179_11486:  # 0m:0.000s
                            chown_179_11486()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=11487):  # 0m:0.082s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11488) as should_copy_source_180_11488:  # 0m:0.082s
                    should_copy_source_180_11488()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=11489):  # 0m:0.081s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=11490) as copy_dir_to_dir_181_11490:  # 0m:0.081s
                            copy_dir_to_dir_181_11490()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=11491, recursive=True) as chown_182_11491:  # 0m:0.000s
                            chown_182_11491()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=11492):  # 0m:0.096s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11493) as should_copy_source_183_11493:  # 0m:0.096s
                    should_copy_source_183_11493()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=11494):  # 0m:0.096s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=11495) as copy_dir_to_dir_184_11495:  # 0m:0.096s
                            copy_dir_to_dir_184_11495()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=11496, recursive=True) as chown_185_11496:  # 0m:0.000s
                            chown_185_11496()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=11497):  # 0m:0.635s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11498) as should_copy_source_186_11498:  # 0m:0.635s
                    should_copy_source_186_11498()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=11499):  # 0m:0.635s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11500) as copy_dir_to_dir_187_11500:  # 0m:0.634s
                            copy_dir_to_dir_187_11500()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11501, recursive=True) as chown_188_11501:  # 0m:0.000s
                            chown_188_11501()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=11502):  # 0m:0.916s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11503) as should_copy_source_189_11503:  # 0m:0.915s
                    should_copy_source_189_11503()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=11504):  # 0m:0.915s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11505) as copy_dir_to_dir_190_11505:  # 0m:0.915s
                            copy_dir_to_dir_190_11505()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11506, recursive=True) as chown_191_11506:  # 0m:0.000s
                            chown_191_11506()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=11507):  # 0m:1.355s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11508) as should_copy_source_192_11508:  # 0m:1.354s
                    should_copy_source_192_11508()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=11509):  # 0m:1.354s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=11510) as copy_dir_to_dir_193_11510:  # 0m:1.354s
                            copy_dir_to_dir_193_11510()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=11511, recursive=True) as chown_194_11511:  # 0m:0.000s
                            chown_194_11511()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=11512) as cd_stage_195_11512:  # 0m:0.202s
            cd_stage_195_11512()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=11513):  # 0m:0.018s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11514) as should_copy_source_196_11514:  # 0m:0.018s
                    should_copy_source_196_11514()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=11515):  # 0m:0.018s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=11516) as copy_dir_to_dir_197_11516:  # 0m:0.017s
                            copy_dir_to_dir_197_11516()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=11517, recursive=True) as chown_198_11517:  # 0m:0.000s
                            chown_198_11517()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=11518):  # 0m:0.027s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11519) as should_copy_source_199_11519:  # 0m:0.027s
                    should_copy_source_199_11519()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=11520):  # 0m:0.022s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=11521) as copy_dir_to_dir_200_11521:  # 0m:0.021s
                            copy_dir_to_dir_200_11521()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=11522, recursive=True) as chown_201_11522:  # 0m:0.000s
                            chown_201_11522()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=11523):  # 0m:0.017s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11524) as should_copy_source_202_11524:  # 0m:0.017s
                    should_copy_source_202_11524()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=11525):  # 0m:0.017s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=11526) as copy_dir_to_dir_203_11526:  # 0m:0.016s
                            copy_dir_to_dir_203_11526()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=11527, recursive=True) as chown_204_11527:  # 0m:0.000s
                            chown_204_11527()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=11528):  # 0m:0.017s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11529) as should_copy_source_205_11529:  # 0m:0.017s
                    should_copy_source_205_11529()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=11530):  # 0m:0.016s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=11531) as copy_dir_to_dir_206_11531:  # 0m:0.016s
                            copy_dir_to_dir_206_11531()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=11532, recursive=True) as chown_207_11532:  # 0m:0.000s
                            chown_207_11532()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=11533):  # 0m:0.031s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11534) as should_copy_source_208_11534:  # 0m:0.031s
                    should_copy_source_208_11534()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=11535):  # 0m:0.031s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=11536) as copy_dir_to_dir_209_11536:  # 0m:0.030s
                            copy_dir_to_dir_209_11536()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=11537, recursive=True) as chown_210_11537:  # 0m:0.000s
                            chown_210_11537()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=11538):  # 0m:0.020s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11539) as should_copy_source_211_11539:  # 0m:0.020s
                    should_copy_source_211_11539()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=11540):  # 0m:0.020s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=11541) as copy_dir_to_dir_212_11541:  # 0m:0.020s
                            copy_dir_to_dir_212_11541()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=11542, recursive=True) as chown_213_11542:  # 0m:0.000s
                            chown_213_11542()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=11543):  # 0m:0.066s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11544) as should_copy_source_214_11544:  # 0m:0.065s
                    should_copy_source_214_11544()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=11545):  # 0m:0.065s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=11546) as copy_dir_to_dir_215_11546:  # 0m:0.065s
                            copy_dir_to_dir_215_11546()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=11547, recursive=True) as chown_216_11547:  # 0m:0.000s
                            chown_216_11547()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=11548) as cd_stage_217_11548:  # 0m:0.032s
            cd_stage_217_11548()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=11549):  # 0m:0.011s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11550) as should_copy_source_218_11550:  # 0m:0.011s
                    should_copy_source_218_11550()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=11551):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11552) as copy_dir_to_dir_219_11552:  # 0m:0.010s
                            copy_dir_to_dir_219_11552()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11553, recursive=True) as chown_220_11553:  # 0m:0.000s
                            chown_220_11553()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=11554):  # 0m:0.020s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11555) as should_copy_source_221_11555:  # 0m:0.019s
                    should_copy_source_221_11555()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=11556):  # 0m:0.019s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11557) as copy_dir_to_dir_222_11557:  # 0m:0.014s
                            copy_dir_to_dir_222_11557()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11558, recursive=True) as chown_223_11558:  # 0m:0.000s
                            chown_223_11558()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=11559) as cd_stage_224_11559:  # 0m:0.144s
            cd_stage_224_11559()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=11560):  # 0m:0.144s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11561) as should_copy_source_225_11561:  # 0m:0.015s
                    should_copy_source_225_11561()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=11562):  # 0m:0.015s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=11563) as unwtar_226_11563:  # 0m:0.015s
                            unwtar_226_11563()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11564) as should_copy_source_227_11564:  # 0m:0.128s
                    should_copy_source_227_11564()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=11565):  # 0m:0.128s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=11566) as unwtar_228_11566:  # 0m:0.128s
                            unwtar_228_11566()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=11567) as cd_stage_229_11567:  # 0m:0.023s
            cd_stage_229_11567()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=11568):  # 0m:0.023s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=11569) as should_copy_source_230_11569:  # 0m:0.023s
                    should_copy_source_230_11569()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=11570):  # 0m:0.022s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=11571) as unwtar_231_11571:  # 0m:0.022s
                            unwtar_231_11571()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=11572) as cd_stage_232_11572:  # 1m:30.224s
            cd_stage_232_11572()
            with Stage(r"copy", r"ARPlates v15.5.79.262", prog_num=11573):  # 0m:1.534s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11574) as should_copy_source_233_11574:  # 0m:1.529s
                    should_copy_source_233_11574()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=11575):  # 0m:1.528s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=11576) as copy_dir_to_dir_234_11576:  # 0m:0.055s
                            copy_dir_to_dir_234_11576()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=11577) as unwtar_235_11577:  # 0m:1.472s
                            unwtar_235_11577()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=11578, recursive=True) as chown_236_11578:  # 0m:0.000s
                            chown_236_11578()
            with Stage(r"copy", r"Abbey Road Vinyl v15.5.79.262", prog_num=11579):  # 0m:3.348s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11580) as should_copy_source_237_11580:  # 0m:3.348s
                    should_copy_source_237_11580()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=11581):  # 0m:3.347s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=11582) as copy_dir_to_dir_238_11582:  # 0m:0.059s
                            copy_dir_to_dir_238_11582()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=11583) as unwtar_239_11583:  # 0m:3.288s
                            unwtar_239_11583()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=11584, recursive=True) as chown_240_11584:  # 0m:0.000s
                            chown_240_11584()
            with Stage(r"copy", r"Aphex AX v15.5.79.262", prog_num=11585):  # 0m:0.202s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11586) as should_copy_source_241_11586:  # 0m:0.201s
                    should_copy_source_241_11586()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=11587):  # 0m:0.201s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=11588) as copy_dir_to_dir_242_11588:  # 0m:0.055s
                            copy_dir_to_dir_242_11588()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=11589) as unwtar_243_11589:  # 0m:0.145s
                            unwtar_243_11589()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=11590, recursive=True) as chown_244_11590:  # 0m:0.000s
                            chown_244_11590()
            with Stage(r"copy", r"AudioTrack v15.5.79.262", prog_num=11591):  # 0m:0.274s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11592) as should_copy_source_245_11592:  # 0m:0.274s
                    should_copy_source_245_11592()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=11593):  # 0m:0.274s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=11594) as copy_dir_to_dir_246_11594:  # 0m:0.062s
                            copy_dir_to_dir_246_11594()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=11595) as unwtar_247_11595:  # 0m:0.211s
                            unwtar_247_11595()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=11596, recursive=True) as chown_248_11596:  # 0m:0.000s
                            chown_248_11596()
            with Stage(r"copy", r"Bass Rider v15.5.79.262", prog_num=11597):  # 0m:0.190s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11598) as should_copy_source_249_11598:  # 0m:0.190s
                    should_copy_source_249_11598()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=11599):  # 0m:0.190s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=11600) as copy_dir_to_dir_250_11600:  # 0m:0.063s
                            copy_dir_to_dir_250_11600()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=11601) as unwtar_251_11601:  # 0m:0.126s
                            unwtar_251_11601()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=11602, recursive=True) as chown_252_11602:  # 0m:0.000s
                            chown_252_11602()
            with Stage(r"copy", r"Bass Slapper v15.5.79.262", prog_num=11603):  # 0m:5.772s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11604) as should_copy_source_253_11604:  # 0m:5.772s
                    should_copy_source_253_11604()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=11605):  # 0m:5.771s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=11606) as copy_dir_to_dir_254_11606:  # 0m:0.238s
                            copy_dir_to_dir_254_11606()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=11607) as unwtar_255_11607:  # 0m:5.533s
                            unwtar_255_11607()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=11608, recursive=True) as chown_256_11608:  # 0m:0.000s
                            chown_256_11608()
            with Stage(r"copy", r"Brauer Motion v15.5.79.262", prog_num=11609):  # 0m:0.376s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11610) as should_copy_source_257_11610:  # 0m:0.376s
                    should_copy_source_257_11610()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=11611):  # 0m:0.376s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=11612) as copy_dir_to_dir_258_11612:  # 0m:0.055s
                            copy_dir_to_dir_258_11612()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=11613) as unwtar_259_11613:  # 0m:0.320s
                            unwtar_259_11613()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=11614, recursive=True) as chown_260_11614:  # 0m:0.000s
                            chown_260_11614()
            with Stage(r"copy", r"Butch Vig Vocals v15.5.79.262", prog_num=11615):  # 0m:3.167s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11616) as should_copy_source_261_11616:  # 0m:3.166s
                    should_copy_source_261_11616()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=11617):  # 0m:3.166s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11618) as copy_dir_to_dir_262_11618:  # 0m:0.435s
                            copy_dir_to_dir_262_11618()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=11619) as unwtar_263_11619:  # 0m:2.731s
                            unwtar_263_11619()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=11620, recursive=True) as chown_264_11620:  # 0m:0.000s
                            chown_264_11620()
            with Stage(r"copy", r"C1 v15.5.79.262", prog_num=11621):  # 0m:0.577s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11622) as should_copy_source_265_11622:  # 0m:0.577s
                    should_copy_source_265_11622()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=11623):  # 0m:0.577s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=11624) as copy_dir_to_dir_266_11624:  # 0m:0.056s
                            copy_dir_to_dir_266_11624()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=11625) as unwtar_267_11625:  # 0m:0.520s
                            unwtar_267_11625()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C1.bundle", user_id=-1, group_id=-1, prog_num=11626, recursive=True) as chown_268_11626:  # 0m:0.000s
                            chown_268_11626()
            with Stage(r"copy", r"C4 v15.5.79.262", prog_num=11627):  # 0m:0.207s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11628) as should_copy_source_269_11628:  # 0m:0.207s
                    should_copy_source_269_11628()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=11629):  # 0m:0.206s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=11630) as copy_dir_to_dir_270_11630:  # 0m:0.063s
                            copy_dir_to_dir_270_11630()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=11631) as unwtar_271_11631:  # 0m:0.142s
                            unwtar_271_11631()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C4.bundle", user_id=-1, group_id=-1, prog_num=11632, recursive=True) as chown_272_11632:  # 0m:0.000s
                            chown_272_11632()
            with Stage(r"copy", r"CLA-2A v15.5.79.262", prog_num=11633):  # 0m:0.207s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11634) as should_copy_source_273_11634:  # 0m:0.206s
                    should_copy_source_273_11634()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=11635):  # 0m:0.206s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=11636) as copy_dir_to_dir_274_11636:  # 0m:0.053s
                            copy_dir_to_dir_274_11636()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=11637) as unwtar_275_11637:  # 0m:0.153s
                            unwtar_275_11637()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=11638, recursive=True) as chown_276_11638:  # 0m:0.000s
                            chown_276_11638()
            with Stage(r"copy", r"CLA-3A v15.5.79.262", prog_num=11639):  # 0m:0.300s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11640) as should_copy_source_277_11640:  # 0m:0.300s
                    should_copy_source_277_11640()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=11641):  # 0m:0.300s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=11642) as copy_dir_to_dir_278_11642:  # 0m:0.050s
                            copy_dir_to_dir_278_11642()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=11643) as unwtar_279_11643:  # 0m:0.250s
                            unwtar_279_11643()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=11644, recursive=True) as chown_280_11644:  # 0m:0.000s
                            chown_280_11644()
            with Stage(r"copy", r"CLA-76 v15.5.79.262", prog_num=11645):  # 0m:0.227s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11646) as should_copy_source_281_11646:  # 0m:0.227s
                    should_copy_source_281_11646()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=11647):  # 0m:0.227s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=11648) as copy_dir_to_dir_282_11648:  # 0m:0.056s
                            copy_dir_to_dir_282_11648()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=11649) as unwtar_283_11649:  # 0m:0.171s
                            unwtar_283_11649()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=11650, recursive=True) as chown_284_11650:  # 0m:0.000s
                            chown_284_11650()
            with Stage(r"copy", r"CLA Bass v15.5.79.262", prog_num=11651):  # 0m:1.758s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11652) as should_copy_source_285_11652:  # 0m:1.758s
                    should_copy_source_285_11652()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=11653):  # 0m:1.758s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=11654) as copy_dir_to_dir_286_11654:  # 0m:0.653s
                            copy_dir_to_dir_286_11654()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=11655) as unwtar_287_11655:  # 0m:1.105s
                            unwtar_287_11655()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=11656, recursive=True) as chown_288_11656:  # 0m:0.000s
                            chown_288_11656()
            with Stage(r"copy", r"CLA Guitars v15.5.79.262", prog_num=11657):  # 0m:1.466s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11658) as should_copy_source_289_11658:  # 0m:1.466s
                    should_copy_source_289_11658()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=11659):  # 0m:1.466s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=11660) as copy_dir_to_dir_290_11660:  # 0m:0.491s
                            copy_dir_to_dir_290_11660()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=11661) as unwtar_291_11661:  # 0m:0.974s
                            unwtar_291_11661()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=11662, recursive=True) as chown_292_11662:  # 0m:0.000s
                            chown_292_11662()
            with Stage(r"copy", r"CLA Unplugged v15.5.79.262", prog_num=11663):  # 0m:1.266s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11664) as should_copy_source_293_11664:  # 0m:1.266s
                    should_copy_source_293_11664()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=11665):  # 0m:1.266s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=11666) as copy_dir_to_dir_294_11666:  # 0m:0.438s
                            copy_dir_to_dir_294_11666()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=11667) as unwtar_295_11667:  # 0m:0.827s
                            unwtar_295_11667()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=11668, recursive=True) as chown_296_11668:  # 0m:0.000s
                            chown_296_11668()
            with Stage(r"copy", r"CLA Vocals v15.5.79.262", prog_num=11669):  # 0m:1.453s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11670) as should_copy_source_297_11670:  # 0m:1.452s
                    should_copy_source_297_11670()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=11671):  # 0m:1.452s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11672) as copy_dir_to_dir_298_11672:  # 0m:0.508s
                            copy_dir_to_dir_298_11672()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=11673) as unwtar_299_11673:  # 0m:0.944s
                            unwtar_299_11673()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=11674, recursive=True) as chown_300_11674:  # 0m:0.000s
                            chown_300_11674()
            with Stage(r"copy", r"Center v15.5.79.262", prog_num=11675):  # 0m:0.184s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11676) as should_copy_source_301_11676:  # 0m:0.183s
                    should_copy_source_301_11676()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=11677):  # 0m:0.183s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=11678) as copy_dir_to_dir_302_11678:  # 0m:0.049s
                            copy_dir_to_dir_302_11678()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=11679) as unwtar_303_11679:  # 0m:0.134s
                            unwtar_303_11679()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Center.bundle", user_id=-1, group_id=-1, prog_num=11680, recursive=True) as chown_304_11680:  # 0m:0.001s
                            chown_304_11680()
            with Stage(r"copy", r"Clarity Vx v15.5.79.262", prog_num=11681):  # 0m:1.901s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11682) as should_copy_source_305_11682:  # 0m:1.901s
                    should_copy_source_305_11682()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=11683):  # 0m:1.901s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=11684) as copy_dir_to_dir_306_11684:  # 0m:0.052s
                            copy_dir_to_dir_306_11684()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=11685) as unwtar_307_11685:  # 0m:1.848s
                            unwtar_307_11685()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=11686, recursive=True) as chown_308_11686:  # 0m:0.000s
                            chown_308_11686()
            with Stage(r"copy", r"Saphira v15.5.79.262", prog_num=11687):  # 0m:0.899s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11688) as should_copy_source_309_11688:  # 0m:0.899s
                    should_copy_source_309_11688()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=11689):  # 0m:0.898s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=11690) as copy_dir_to_dir_310_11690:  # 0m:0.255s
                            copy_dir_to_dir_310_11690()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=11691) as unwtar_311_11691:  # 0m:0.643s
                            unwtar_311_11691()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Saphira.bundle", user_id=-1, group_id=-1, prog_num=11692, recursive=True) as chown_312_11692:  # 0m:0.000s
                            chown_312_11692()
            with Stage(r"copy", r"Submarine v15.5.79.262", prog_num=11693):  # 0m:0.244s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11694) as should_copy_source_313_11694:  # 0m:0.244s
                    should_copy_source_313_11694()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=11695):  # 0m:0.243s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=11696) as copy_dir_to_dir_314_11696:  # 0m:0.057s
                            copy_dir_to_dir_314_11696()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=11697) as unwtar_315_11697:  # 0m:0.186s
                            unwtar_315_11697()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Submarine.bundle", user_id=-1, group_id=-1, prog_num=11698, recursive=True) as chown_316_11698:  # 0m:0.000s
                            chown_316_11698()
            with Stage(r"copy", r"DeBreath v15.5.79.262", prog_num=11699):  # 0m:0.211s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11700) as should_copy_source_317_11700:  # 0m:0.211s
                    should_copy_source_317_11700()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=11701):  # 0m:0.211s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=11702) as copy_dir_to_dir_318_11702:  # 0m:0.050s
                            copy_dir_to_dir_318_11702()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=11703) as unwtar_319_11703:  # 0m:0.161s
                            unwtar_319_11703()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=11704, recursive=True) as chown_320_11704:  # 0m:0.000s
                            chown_320_11704()
            with Stage(r"copy", r"DeEsser v15.5.79.262", prog_num=11705):  # 0m:0.180s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11706) as should_copy_source_321_11706:  # 0m:0.180s
                    should_copy_source_321_11706()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=11707):  # 0m:0.180s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=11708) as copy_dir_to_dir_322_11708:  # 0m:0.059s
                            copy_dir_to_dir_322_11708()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=11709) as unwtar_323_11709:  # 0m:0.121s
                            unwtar_323_11709()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=11710, recursive=True) as chown_324_11710:  # 0m:0.000s
                            chown_324_11710()
            with Stage(r"copy", r"Doppler v15.5.79.262", prog_num=11711):  # 0m:0.167s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11712) as should_copy_source_325_11712:  # 0m:0.166s
                    should_copy_source_325_11712()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=11713):  # 0m:0.166s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=11714) as copy_dir_to_dir_326_11714:  # 0m:0.051s
                            copy_dir_to_dir_326_11714()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=11715) as unwtar_327_11715:  # 0m:0.115s
                            unwtar_327_11715()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doppler.bundle", user_id=-1, group_id=-1, prog_num=11716, recursive=True) as chown_328_11716:  # 0m:0.000s
                            chown_328_11716()
            with Stage(r"copy", r"Doubler v15.5.79.262", prog_num=11717):  # 0m:0.413s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11718) as should_copy_source_329_11718:  # 0m:0.413s
                    should_copy_source_329_11718()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=11719):  # 0m:0.412s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=11720) as copy_dir_to_dir_330_11720:  # 0m:0.055s
                            copy_dir_to_dir_330_11720()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=11721) as unwtar_331_11721:  # 0m:0.357s
                            unwtar_331_11721()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doubler.bundle", user_id=-1, group_id=-1, prog_num=11722, recursive=True) as chown_332_11722:  # 0m:0.000s
                            chown_332_11722()
            with Stage(r"copy", r"EMO-F2 v15.5.79.262", prog_num=11723):  # 0m:0.243s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11724) as should_copy_source_333_11724:  # 0m:0.242s
                    should_copy_source_333_11724()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=11725):  # 0m:0.237s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=11726) as copy_dir_to_dir_334_11726:  # 0m:0.058s
                            copy_dir_to_dir_334_11726()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=11727) as unwtar_335_11727:  # 0m:0.178s
                            unwtar_335_11727()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=11728, recursive=True) as chown_336_11728:  # 0m:0.000s
                            chown_336_11728()
            with Stage(r"copy", r"EMO-Q4 v15.5.79.262", prog_num=11729):  # 0m:0.329s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11730) as should_copy_source_337_11730:  # 0m:0.329s
                    should_copy_source_337_11730()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=11731):  # 0m:0.328s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=11732) as copy_dir_to_dir_338_11732:  # 0m:0.054s
                            copy_dir_to_dir_338_11732()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=11733) as unwtar_339_11733:  # 0m:0.275s
                            unwtar_339_11733()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=11734, recursive=True) as chown_340_11734:  # 0m:0.000s
                            chown_340_11734()
            with Stage(r"copy", r"EddieKramer DR v15.5.79.262", prog_num=11735):  # 0m:1.199s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11736) as should_copy_source_341_11736:  # 0m:1.198s
                    should_copy_source_341_11736()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=11737):  # 0m:1.198s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=11738) as copy_dir_to_dir_342_11738:  # 0m:0.345s
                            copy_dir_to_dir_342_11738()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=11739) as unwtar_343_11739:  # 0m:0.852s
                            unwtar_343_11739()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=11740, recursive=True) as chown_344_11740:  # 0m:0.000s
                            chown_344_11740()
            with Stage(r"copy", r"EddieKramer VC v15.5.79.262", prog_num=11741):  # 0m:1.371s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11742) as should_copy_source_345_11742:  # 0m:1.371s
                    should_copy_source_345_11742()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=11743):  # 0m:1.370s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=11744) as copy_dir_to_dir_346_11744:  # 0m:0.390s
                            copy_dir_to_dir_346_11744()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=11745) as unwtar_347_11745:  # 0m:0.980s
                            unwtar_347_11745()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=11746, recursive=True) as chown_348_11746:  # 0m:0.000s
                            chown_348_11746()
            with Stage(r"copy", r"Electric Grand 80 v15.5.79.262", prog_num=11747):  # 0m:4.136s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11748) as should_copy_source_349_11748:  # 0m:4.136s
                    should_copy_source_349_11748()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=11749):  # 0m:4.136s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=11750) as copy_dir_to_dir_350_11750:  # 0m:0.221s
                            copy_dir_to_dir_350_11750()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=11751) as unwtar_351_11751:  # 0m:3.914s
                            unwtar_351_11751()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=11752, recursive=True) as chown_352_11752:  # 0m:0.000s
                            chown_352_11752()
            with Stage(r"copy", r"Enigma v15.5.79.262", prog_num=11753):  # 0m:0.387s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11754) as should_copy_source_353_11754:  # 0m:0.387s
                    should_copy_source_353_11754()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=11755):  # 0m:0.387s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=11756) as copy_dir_to_dir_354_11756:  # 0m:0.051s
                            copy_dir_to_dir_354_11756()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=11757) as unwtar_355_11757:  # 0m:0.335s
                            unwtar_355_11757()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Enigma.bundle", user_id=-1, group_id=-1, prog_num=11758, recursive=True) as chown_356_11758:  # 0m:0.000s
                            chown_356_11758()
            with Stage(r"copy", r"GTRAmp v15.5.79.262", prog_num=11759):  # 0m:1.320s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11760) as should_copy_source_357_11760:  # 0m:1.320s
                    should_copy_source_357_11760()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=11761):  # 0m:1.320s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=11762) as copy_dir_to_dir_358_11762:  # 0m:0.056s
                            copy_dir_to_dir_358_11762()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=11763) as unwtar_359_11763:  # 0m:1.263s
                            unwtar_359_11763()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=11764, recursive=True) as chown_360_11764:  # 0m:0.000s
                            chown_360_11764()
            with Stage(r"copy", r"GTRStomp v15.5.79.262", prog_num=11765):  # 0m:0.265s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11766) as should_copy_source_361_11766:  # 0m:0.265s
                    should_copy_source_361_11766()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=11767):  # 0m:0.265s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=11768) as copy_dir_to_dir_362_11768:  # 0m:0.045s
                            copy_dir_to_dir_362_11768()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=11769) as unwtar_363_11769:  # 0m:0.220s
                            unwtar_363_11769()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=11770, recursive=True) as chown_364_11770:  # 0m:0.000s
                            chown_364_11770()
            with Stage(r"copy", r"GTRToolRack v15.5.79.262", prog_num=11771):  # 0m:1.661s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11772) as should_copy_source_365_11772:  # 0m:1.661s
                    should_copy_source_365_11772()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=11773):  # 0m:1.661s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=11774) as copy_dir_to_dir_366_11774:  # 0m:0.216s
                            copy_dir_to_dir_366_11774()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=11775) as unwtar_367_11775:  # 0m:1.444s
                            unwtar_367_11775()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=11776, recursive=True) as chown_368_11776:  # 0m:0.000s
                            chown_368_11776()
            with Stage(r"copy", r"GTRTuner v15.5.79.262", prog_num=11777):  # 0m:0.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11778) as should_copy_source_369_11778:  # 0m:0.172s
                    should_copy_source_369_11778()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=11779):  # 0m:0.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=11780) as copy_dir_to_dir_370_11780:  # 0m:0.062s
                            copy_dir_to_dir_370_11780()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=11781) as unwtar_371_11781:  # 0m:0.109s
                            unwtar_371_11781()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=11782, recursive=True) as chown_372_11782:  # 0m:0.000s
                            chown_372_11782()
            with Stage(r"copy", r"Greg Wells MixCentric v15.5.79.262", prog_num=11783):  # 0m:1.968s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11784) as should_copy_source_373_11784:  # 0m:1.968s
                    should_copy_source_373_11784()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=11785):  # 0m:1.968s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=11786) as copy_dir_to_dir_374_11786:  # 0m:0.312s
                            copy_dir_to_dir_374_11786()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=11787) as unwtar_375_11787:  # 0m:1.655s
                            unwtar_375_11787()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=11788, recursive=True) as chown_376_11788:  # 0m:0.000s
                            chown_376_11788()
            with Stage(r"copy", r"Greg Wells PianoCentric v15.5.79.262", prog_num=11789):  # 0m:1.955s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11790) as should_copy_source_377_11790:  # 0m:1.955s
                    should_copy_source_377_11790()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=11791):  # 0m:1.955s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=11792) as copy_dir_to_dir_378_11792:  # 0m:0.353s
                            copy_dir_to_dir_378_11792()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=11793) as unwtar_379_11793:  # 0m:1.601s
                            unwtar_379_11793()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=11794, recursive=True) as chown_380_11794:  # 0m:0.000s
                            chown_380_11794()
            with Stage(r"copy", r"Greg Wells ToneCentric v15.5.79.262", prog_num=11795):  # 0m:1.976s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11796) as should_copy_source_381_11796:  # 0m:1.976s
                    should_copy_source_381_11796()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=11797):  # 0m:1.975s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=11798) as copy_dir_to_dir_382_11798:  # 0m:0.280s
                            copy_dir_to_dir_382_11798()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=11799) as unwtar_383_11799:  # 0m:1.694s
                            unwtar_383_11799()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=11800, recursive=True) as chown_384_11800:  # 0m:0.000s
                            chown_384_11800()
            with Stage(r"copy", r"H-Comp v15.5.79.262", prog_num=11801):  # 0m:1.179s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11802) as should_copy_source_385_11802:  # 0m:1.179s
                    should_copy_source_385_11802()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=11803):  # 0m:1.179s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=11804) as copy_dir_to_dir_386_11804:  # 0m:0.064s
                            copy_dir_to_dir_386_11804()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=11805) as unwtar_387_11805:  # 0m:1.114s
                            unwtar_387_11805()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=11806, recursive=True) as chown_388_11806:  # 0m:0.000s
                            chown_388_11806()
            with Stage(r"copy", r"H-Delay v15.5.79.262", prog_num=11807):  # 0m:0.217s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11808) as should_copy_source_389_11808:  # 0m:0.216s
                    should_copy_source_389_11808()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=11809):  # 0m:0.216s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=11810) as copy_dir_to_dir_390_11810:  # 0m:0.059s
                            copy_dir_to_dir_390_11810()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=11811) as unwtar_391_11811:  # 0m:0.156s
                            unwtar_391_11811()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=11812, recursive=True) as chown_392_11812:  # 0m:0.000s
                            chown_392_11812()
            with Stage(r"copy", r"H-Reverb v15.5.79.262", prog_num=11813):  # 0m:0.400s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11814) as should_copy_source_393_11814:  # 0m:0.399s
                    should_copy_source_393_11814()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=11815):  # 0m:0.399s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=11816) as copy_dir_to_dir_394_11816:  # 0m:0.059s
                            copy_dir_to_dir_394_11816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=11817) as unwtar_395_11817:  # 0m:0.339s
                            unwtar_395_11817()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=11818, recursive=True) as chown_396_11818:  # 0m:0.000s
                            chown_396_11818()
            with Stage(r"copy", r"IR-L v15.5.79.262", prog_num=11819):  # 0m:0.301s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11820) as should_copy_source_397_11820:  # 0m:0.300s
                    should_copy_source_397_11820()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=11821):  # 0m:0.300s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=11822) as copy_dir_to_dir_398_11822:  # 0m:0.051s
                            copy_dir_to_dir_398_11822()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=11823) as unwtar_399_11823:  # 0m:0.249s
                            unwtar_399_11823()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/IR-L.bundle", user_id=-1, group_id=-1, prog_num=11824, recursive=True) as chown_400_11824:  # 0m:0.000s
                            chown_400_11824()
            with Stage(r"copy", r"InPhase v15.5.79.262", prog_num=11825):  # 0m:0.206s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11826) as should_copy_source_401_11826:  # 0m:0.206s
                    should_copy_source_401_11826()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=11827):  # 0m:0.206s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=11828) as copy_dir_to_dir_402_11828:  # 0m:0.063s
                            copy_dir_to_dir_402_11828()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=11829) as unwtar_403_11829:  # 0m:0.143s
                            unwtar_403_11829()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase.bundle", user_id=-1, group_id=-1, prog_num=11830, recursive=True) as chown_404_11830:  # 0m:0.000s
                            chown_404_11830()
            with Stage(r"copy", r"InPhase LT v15.5.79.262", prog_num=11831):  # 0m:0.191s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11832) as should_copy_source_405_11832:  # 0m:0.191s
                    should_copy_source_405_11832()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=11833):  # 0m:0.185s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=11834) as copy_dir_to_dir_406_11834:  # 0m:0.048s
                            copy_dir_to_dir_406_11834()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=11835) as unwtar_407_11835:  # 0m:0.136s
                            unwtar_407_11835()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=11836, recursive=True) as chown_408_11836:  # 0m:0.000s
                            chown_408_11836()
            with Stage(r"copy", r"J37 v15.5.79.262", prog_num=11837):  # 0m:1.750s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11838) as should_copy_source_409_11838:  # 0m:1.750s
                    should_copy_source_409_11838()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=11839):  # 0m:1.749s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=11840) as copy_dir_to_dir_410_11840:  # 0m:0.055s
                            copy_dir_to_dir_410_11840()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=11841) as unwtar_411_11841:  # 0m:1.694s
                            unwtar_411_11841()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/J37.bundle", user_id=-1, group_id=-1, prog_num=11842, recursive=True) as chown_412_11842:  # 0m:0.000s
                            chown_412_11842()
            with Stage(r"copy", r"JJP-Vocals v15.5.79.262", prog_num=11843):  # 0m:1.570s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11844) as should_copy_source_413_11844:  # 0m:1.570s
                    should_copy_source_413_11844()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=11845):  # 0m:1.569s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11846) as copy_dir_to_dir_414_11846:  # 0m:0.708s
                            copy_dir_to_dir_414_11846()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=11847) as unwtar_415_11847:  # 0m:0.861s
                            unwtar_415_11847()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=11848, recursive=True) as chown_416_11848:  # 0m:0.000s
                            chown_416_11848()
            with Stage(r"copy", r"Key Detector v15.5.79.262", prog_num=11849):  # 0m:0.179s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11850) as should_copy_source_417_11850:  # 0m:0.179s
                    should_copy_source_417_11850()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=11851):  # 0m:0.178s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=11852) as copy_dir_to_dir_418_11852:  # 0m:0.028s
                            copy_dir_to_dir_418_11852()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=11853) as unwtar_419_11853:  # 0m:0.150s
                            unwtar_419_11853()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=11854, recursive=True) as chown_420_11854:  # 0m:0.000s
                            chown_420_11854()
            with Stage(r"copy", r"KingsMic v15.5.79.262", prog_num=11855):  # 0m:0.178s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11856) as should_copy_source_421_11856:  # 0m:0.178s
                    should_copy_source_421_11856()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=11857):  # 0m:0.178s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=11858) as copy_dir_to_dir_422_11858:  # 0m:0.034s
                            copy_dir_to_dir_422_11858()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=11859) as unwtar_423_11859:  # 0m:0.144s
                            unwtar_423_11859()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=11860, recursive=True) as chown_424_11860:  # 0m:0.000s
                            chown_424_11860()
            with Stage(r"copy", r"KramerHLS v15.5.79.262", prog_num=11861):  # 0m:0.153s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11862) as should_copy_source_425_11862:  # 0m:0.153s
                    should_copy_source_425_11862()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=11863):  # 0m:0.153s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=11864) as copy_dir_to_dir_426_11864:  # 0m:0.032s
                            copy_dir_to_dir_426_11864()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=11865) as unwtar_427_11865:  # 0m:0.120s
                            unwtar_427_11865()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=11866, recursive=True) as chown_428_11866:  # 0m:0.000s
                            chown_428_11866()
            with Stage(r"copy", r"KramerPIE v15.5.79.262", prog_num=11867):  # 0m:0.122s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11868) as should_copy_source_429_11868:  # 0m:0.121s
                    should_copy_source_429_11868()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=11869):  # 0m:0.121s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=11870) as copy_dir_to_dir_430_11870:  # 0m:0.034s
                            copy_dir_to_dir_430_11870()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=11871) as unwtar_431_11871:  # 0m:0.086s
                            unwtar_431_11871()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=11872, recursive=True) as chown_432_11872:  # 0m:0.000s
                            chown_432_11872()
            with Stage(r"copy", r"KramerTape v15.5.79.262", prog_num=11873):  # 0m:0.645s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11874) as should_copy_source_433_11874:  # 0m:0.645s
                    should_copy_source_433_11874()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=11875):  # 0m:0.645s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=11876) as copy_dir_to_dir_434_11876:  # 0m:0.033s
                            copy_dir_to_dir_434_11876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=11877) as unwtar_435_11877:  # 0m:0.611s
                            unwtar_435_11877()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=11878, recursive=True) as chown_436_11878:  # 0m:0.000s
                            chown_436_11878()
            with Stage(r"copy", r"L1 v15.5.79.262", prog_num=11879):  # 0m:0.195s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11880) as should_copy_source_437_11880:  # 0m:0.195s
                    should_copy_source_437_11880()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=11881):  # 0m:0.194s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=11882) as copy_dir_to_dir_438_11882:  # 0m:0.033s
                            copy_dir_to_dir_438_11882()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=11883) as unwtar_439_11883:  # 0m:0.161s
                            unwtar_439_11883()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L1.bundle", user_id=-1, group_id=-1, prog_num=11884, recursive=True) as chown_440_11884:  # 0m:0.000s
                            chown_440_11884()
            with Stage(r"copy", r"L2 v15.5.79.262", prog_num=11885):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11886) as should_copy_source_441_11886:  # 0m:0.110s
                    should_copy_source_441_11886()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=11887):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=11888) as copy_dir_to_dir_442_11888:  # 0m:0.037s
                            copy_dir_to_dir_442_11888()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=11889) as unwtar_443_11889:  # 0m:0.072s
                            unwtar_443_11889()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L2.bundle", user_id=-1, group_id=-1, prog_num=11890, recursive=True) as chown_444_11890:  # 0m:0.000s
                            chown_444_11890()
            with Stage(r"copy", r"L3-16 v15.5.79.262", prog_num=11891):  # 0m:0.919s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11892) as should_copy_source_445_11892:  # 0m:0.919s
                    should_copy_source_445_11892()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=11893):  # 0m:0.918s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=11894) as copy_dir_to_dir_446_11894:  # 0m:0.039s
                            copy_dir_to_dir_446_11894()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=11895) as unwtar_447_11895:  # 0m:0.879s
                            unwtar_447_11895()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-16.bundle", user_id=-1, group_id=-1, prog_num=11896, recursive=True) as chown_448_11896:  # 0m:0.000s
                            chown_448_11896()
            with Stage(r"copy", r"L3-LL Multi v15.5.79.262", prog_num=11897):  # 0m:0.123s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11898) as should_copy_source_449_11898:  # 0m:0.123s
                    should_copy_source_449_11898()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=11899):  # 0m:0.123s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=11900) as copy_dir_to_dir_450_11900:  # 0m:0.033s
                            copy_dir_to_dir_450_11900()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=11901) as unwtar_451_11901:  # 0m:0.089s
                            unwtar_451_11901()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=11902, recursive=True) as chown_452_11902:  # 0m:0.000s
                            chown_452_11902()
            with Stage(r"copy", r"L3-LL Ultra v15.5.79.262", prog_num=11903):  # 0m:0.118s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11904) as should_copy_source_453_11904:  # 0m:0.118s
                    should_copy_source_453_11904()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=11905):  # 0m:0.118s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=11906) as copy_dir_to_dir_454_11906:  # 0m:0.026s
                            copy_dir_to_dir_454_11906()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=11907) as unwtar_455_11907:  # 0m:0.092s
                            unwtar_455_11907()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=11908, recursive=True) as chown_456_11908:  # 0m:0.000s
                            chown_456_11908()
            with Stage(r"copy", r"L3 Multi v15.5.79.262", prog_num=11909):  # 0m:0.127s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11910) as should_copy_source_457_11910:  # 0m:0.127s
                    should_copy_source_457_11910()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=11911):  # 0m:0.126s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=11912) as copy_dir_to_dir_458_11912:  # 0m:0.032s
                            copy_dir_to_dir_458_11912()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=11913) as unwtar_459_11913:  # 0m:0.090s
                            unwtar_459_11913()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=11914, recursive=True) as chown_460_11914:  # 0m:0.004s
                            chown_460_11914()
            with Stage(r"copy", r"L3 Ultra v15.5.79.262", prog_num=11915):  # 0m:0.120s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11916) as should_copy_source_461_11916:  # 0m:0.120s
                    should_copy_source_461_11916()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=11917):  # 0m:0.120s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=11918) as copy_dir_to_dir_462_11918:  # 0m:0.032s
                            copy_dir_to_dir_462_11918()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=11919) as unwtar_463_11919:  # 0m:0.087s
                            unwtar_463_11919()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=11920, recursive=True) as chown_464_11920:  # 0m:0.000s
                            chown_464_11920()
            with Stage(r"copy", r"LinEQ v15.5.79.262", prog_num=11921):  # 0m:0.180s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11922) as should_copy_source_465_11922:  # 0m:0.180s
                    should_copy_source_465_11922()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=11923):  # 0m:0.180s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=11924) as copy_dir_to_dir_466_11924:  # 0m:0.039s
                            copy_dir_to_dir_466_11924()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=11925) as unwtar_467_11925:  # 0m:0.140s
                            unwtar_467_11925()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=11926, recursive=True) as chown_468_11926:  # 0m:0.000s
                            chown_468_11926()
            with Stage(r"copy", r"LinMB v15.5.79.262", prog_num=11927):  # 0m:0.130s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11928) as should_copy_source_469_11928:  # 0m:0.130s
                    should_copy_source_469_11928()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=11929):  # 0m:0.130s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=11930) as copy_dir_to_dir_470_11930:  # 0m:0.033s
                            copy_dir_to_dir_470_11930()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=11931) as unwtar_471_11931:  # 0m:0.096s
                            unwtar_471_11931()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinMB.bundle", user_id=-1, group_id=-1, prog_num=11932, recursive=True) as chown_472_11932:  # 0m:0.000s
                            chown_472_11932()
            with Stage(r"copy", r"LoAir v15.5.79.262", prog_num=11933):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11934) as should_copy_source_473_11934:  # 0m:0.110s
                    should_copy_source_473_11934()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=11935):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=11936) as copy_dir_to_dir_474_11936:  # 0m:0.029s
                            copy_dir_to_dir_474_11936()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=11937) as unwtar_475_11937:  # 0m:0.080s
                            unwtar_475_11937()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LoAir.bundle", user_id=-1, group_id=-1, prog_num=11938, recursive=True) as chown_476_11938:  # 0m:0.000s
                            chown_476_11938()
            with Stage(r"copy", r"Lofi Space v15.5.79.262", prog_num=11939):  # 0m:1.174s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11940) as should_copy_source_477_11940:  # 0m:1.174s
                    should_copy_source_477_11940()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=11941):  # 0m:1.174s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=11942) as copy_dir_to_dir_478_11942:  # 0m:0.352s
                            copy_dir_to_dir_478_11942()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=11943) as unwtar_479_11943:  # 0m:0.821s
                            unwtar_479_11943()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=11944, recursive=True) as chown_480_11944:  # 0m:0.001s
                            chown_480_11944()
            with Stage(r"copy", r"MV2 v15.5.79.262", prog_num=11945):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11946) as should_copy_source_481_11946:  # 0m:0.111s
                    should_copy_source_481_11946()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=11947):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=11948) as copy_dir_to_dir_482_11948:  # 0m:0.038s
                            copy_dir_to_dir_482_11948()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=11949) as unwtar_483_11949:  # 0m:0.072s
                            unwtar_483_11949()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MV2.bundle", user_id=-1, group_id=-1, prog_num=11950, recursive=True) as chown_484_11950:  # 0m:0.000s
                            chown_484_11950()
            with Stage(r"copy", r"Magma Springs v15.5.79.262", prog_num=11951):  # 0m:0.793s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11952) as should_copy_source_485_11952:  # 0m:0.793s
                    should_copy_source_485_11952()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=11953):  # 0m:0.792s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=11954) as copy_dir_to_dir_486_11954:  # 0m:0.186s
                            copy_dir_to_dir_486_11954()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=11955) as unwtar_487_11955:  # 0m:0.606s
                            unwtar_487_11955()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=11956, recursive=True) as chown_488_11956:  # 0m:0.000s
                            chown_488_11956()
            with Stage(r"copy", r"MannyM-TripleD v15.5.79.262", prog_num=11957):  # 0m:0.454s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11958) as should_copy_source_489_11958:  # 0m:0.454s
                    should_copy_source_489_11958()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=11959):  # 0m:0.454s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=11960) as copy_dir_to_dir_490_11960:  # 0m:0.120s
                            copy_dir_to_dir_490_11960()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=11961) as unwtar_491_11961:  # 0m:0.333s
                            unwtar_491_11961()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=11962, recursive=True) as chown_492_11962:  # 0m:0.000s
                            chown_492_11962()
            with Stage(r"copy", r"Maserati DRM v15.5.79.262", prog_num=11963):  # 0m:0.206s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11964) as should_copy_source_493_11964:  # 0m:0.205s
                    should_copy_source_493_11964()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=11965):  # 0m:0.205s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=11966) as copy_dir_to_dir_494_11966:  # 0m:0.067s
                            copy_dir_to_dir_494_11966()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=11967) as unwtar_495_11967:  # 0m:0.138s
                            unwtar_495_11967()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=11968, recursive=True) as chown_496_11968:  # 0m:0.000s
                            chown_496_11968()
            with Stage(r"copy", r"Maserati VX1 v15.5.79.262", prog_num=11969):  # 0m:0.949s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11970) as should_copy_source_497_11970:  # 0m:0.948s
                    should_copy_source_497_11970()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=11971):  # 0m:0.948s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=11972) as copy_dir_to_dir_498_11972:  # 0m:0.266s
                            copy_dir_to_dir_498_11972()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=11973) as unwtar_499_11973:  # 0m:0.682s
                            unwtar_499_11973()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=11974, recursive=True) as chown_500_11974:  # 0m:0.000s
                            chown_500_11974()
            with Stage(r"copy", r"MaxxBass v15.5.79.262", prog_num=11975):  # 0m:0.108s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11976) as should_copy_source_501_11976:  # 0m:0.108s
                    should_copy_source_501_11976()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=11977):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=11978) as copy_dir_to_dir_502_11978:  # 0m:0.030s
                            copy_dir_to_dir_502_11978()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=11979) as unwtar_503_11979:  # 0m:0.077s
                            unwtar_503_11979()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=11980, recursive=True) as chown_504_11980:  # 0m:0.000s
                            chown_504_11980()
            with Stage(r"copy", r"MaxxVolume v15.5.79.262", prog_num=11981):  # 0m:0.126s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11982) as should_copy_source_505_11982:  # 0m:0.126s
                    should_copy_source_505_11982()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=11983):  # 0m:0.126s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=11984) as copy_dir_to_dir_506_11984:  # 0m:0.036s
                            copy_dir_to_dir_506_11984()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=11985) as unwtar_507_11985:  # 0m:0.089s
                            unwtar_507_11985()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=11986, recursive=True) as chown_508_11986:  # 0m:0.000s
                            chown_508_11986()
            with Stage(r"copy", r"MetaFilter v15.5.79.262", prog_num=11987):  # 0m:0.282s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11988) as should_copy_source_509_11988:  # 0m:0.282s
                    should_copy_source_509_11988()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=11989):  # 0m:0.281s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=11990) as copy_dir_to_dir_510_11990:  # 0m:0.027s
                            copy_dir_to_dir_510_11990()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=11991) as unwtar_511_11991:  # 0m:0.254s
                            unwtar_511_11991()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=11992, recursive=True) as chown_512_11992:  # 0m:0.000s
                            chown_512_11992()
            with Stage(r"copy", r"MetaFlanger v15.5.79.262", prog_num=11993):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11994) as should_copy_source_513_11994:  # 0m:0.116s
                    should_copy_source_513_11994()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=11995):  # 0m:0.116s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=11996) as copy_dir_to_dir_514_11996:  # 0m:0.032s
                            copy_dir_to_dir_514_11996()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=11997) as unwtar_515_11997:  # 0m:0.083s
                            unwtar_515_11997()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=11998, recursive=True) as chown_516_11998:  # 0m:0.000s
                            chown_516_11998()
            with Stage(r"copy", r"MondoMod v15.5.79.262", prog_num=11999):  # 0m:0.120s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12000) as should_copy_source_517_12000:  # 0m:0.119s
                    should_copy_source_517_12000()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=12001):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=12002) as copy_dir_to_dir_518_12002:  # 0m:0.037s
                            copy_dir_to_dir_518_12002()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=12003) as unwtar_519_12003:  # 0m:0.081s
                            unwtar_519_12003()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=12004, recursive=True) as chown_520_12004:  # 0m:0.000s
                            chown_520_12004()
            with Stage(r"copy", r"Morphoder v15.5.79.262", prog_num=12005):  # 0m:0.280s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12006) as should_copy_source_521_12006:  # 0m:0.280s
                    should_copy_source_521_12006()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=12007):  # 0m:0.280s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=12008) as copy_dir_to_dir_522_12008:  # 0m:0.033s
                            copy_dir_to_dir_522_12008()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=12009) as unwtar_523_12009:  # 0m:0.246s
                            unwtar_523_12009()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=12010, recursive=True) as chown_524_12010:  # 0m:0.000s
                            chown_524_12010()
            with Stage(r"copy", r"NLS v15.5.79.262", prog_num=12011):  # 0m:0.677s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12012) as should_copy_source_525_12012:  # 0m:0.677s
                    should_copy_source_525_12012()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=12013):  # 0m:0.677s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=12014) as copy_dir_to_dir_526_12014:  # 0m:0.034s
                            copy_dir_to_dir_526_12014()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=12015) as unwtar_527_12015:  # 0m:0.643s
                            unwtar_527_12015()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NLS.bundle", user_id=-1, group_id=-1, prog_num=12016, recursive=True) as chown_528_12016:  # 0m:0.000s
                            chown_528_12016()
            with Stage(r"copy", r"NX v15.5.79.262", prog_num=12017):  # 0m:0.552s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12018) as should_copy_source_529_12018:  # 0m:0.552s
                    should_copy_source_529_12018()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=12019):  # 0m:0.551s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=12020) as copy_dir_to_dir_530_12020:  # 0m:0.030s
                            copy_dir_to_dir_530_12020()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=12021) as unwtar_531_12021:  # 0m:0.520s
                            unwtar_531_12021()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NX.bundle", user_id=-1, group_id=-1, prog_num=12022, recursive=True) as chown_532_12022:  # 0m:0.000s
                            chown_532_12022()
            with Stage(r"copy", r"OKDriver v15.5.79.262", prog_num=12023):  # 0m:0.114s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12024) as should_copy_source_533_12024:  # 0m:0.113s
                    should_copy_source_533_12024()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=12025):  # 0m:0.113s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=12026) as copy_dir_to_dir_534_12026:  # 0m:0.035s
                            copy_dir_to_dir_534_12026()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=12027) as unwtar_535_12027:  # 0m:0.077s
                            unwtar_535_12027()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=12028, recursive=True) as chown_536_12028:  # 0m:0.000s
                            chown_536_12028()
            with Stage(r"copy", r"OKFilter v15.5.79.262", prog_num=12029):  # 0m:0.120s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12030) as should_copy_source_537_12030:  # 0m:0.120s
                    should_copy_source_537_12030()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=12031):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=12032) as copy_dir_to_dir_538_12032:  # 0m:0.034s
                            copy_dir_to_dir_538_12032()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=12033) as unwtar_539_12033:  # 0m:0.085s
                            unwtar_539_12033()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=12034, recursive=True) as chown_540_12034:  # 0m:0.000s
                            chown_540_12034()
            with Stage(r"copy", r"OKPhatter v15.5.79.262", prog_num=12035):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12036) as should_copy_source_541_12036:  # 0m:0.110s
                    should_copy_source_541_12036()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=12037):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=12038) as copy_dir_to_dir_542_12038:  # 0m:0.030s
                            copy_dir_to_dir_542_12038()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=12039) as unwtar_543_12039:  # 0m:0.080s
                            unwtar_543_12039()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=12040, recursive=True) as chown_544_12040:  # 0m:0.000s
                            chown_544_12040()
            with Stage(r"copy", r"OKPumper v15.5.79.262", prog_num=12041):  # 0m:0.100s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12042) as should_copy_source_545_12042:  # 0m:0.099s
                    should_copy_source_545_12042()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=12043):  # 0m:0.099s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=12044) as copy_dir_to_dir_546_12044:  # 0m:0.031s
                            copy_dir_to_dir_546_12044()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=12045) as unwtar_547_12045:  # 0m:0.067s
                            unwtar_547_12045()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=12046, recursive=True) as chown_548_12046:  # 0m:0.000s
                            chown_548_12046()
            with Stage(r"copy", r"PAZ v15.5.79.262", prog_num=12047):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12048) as should_copy_source_549_12048:  # 0m:0.101s
                    should_copy_source_549_12048()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=12049):  # 0m:0.101s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=12050) as copy_dir_to_dir_550_12050:  # 0m:0.030s
                            copy_dir_to_dir_550_12050()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=12051) as unwtar_551_12051:  # 0m:0.070s
                            unwtar_551_12051()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PAZ.bundle", user_id=-1, group_id=-1, prog_num=12052, recursive=True) as chown_552_12052:  # 0m:0.000s
                            chown_552_12052()
            with Stage(r"copy", r"PS22 v15.5.79.262", prog_num=12053):  # 0m:0.109s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12054) as should_copy_source_553_12054:  # 0m:0.109s
                    should_copy_source_553_12054()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=12055):  # 0m:0.109s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=12056) as copy_dir_to_dir_554_12056:  # 0m:0.032s
                            copy_dir_to_dir_554_12056()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=12057) as unwtar_555_12057:  # 0m:0.076s
                            unwtar_555_12057()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PS22.bundle", user_id=-1, group_id=-1, prog_num=12058, recursive=True) as chown_556_12058:  # 0m:0.000s
                            chown_556_12058()
            with Stage(r"copy", r"PuigChild v15.5.79.262", prog_num=12059):  # 0m:1.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12060) as should_copy_source_557_12060:  # 0m:1.001s
                    should_copy_source_557_12060()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=12061):  # 0m:1.000s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=12062) as copy_dir_to_dir_558_12062:  # 0m:0.034s
                            copy_dir_to_dir_558_12062()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=12063) as unwtar_559_12063:  # 0m:0.966s
                            unwtar_559_12063()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=12064, recursive=True) as chown_560_12064:  # 0m:0.000s
                            chown_560_12064()
            with Stage(r"copy", r"PuigTec v15.5.79.262", prog_num=12065):  # 0m:1.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12066) as should_copy_source_561_12066:  # 0m:1.110s
                    should_copy_source_561_12066()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=12067):  # 0m:1.109s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=12068) as copy_dir_to_dir_562_12068:  # 0m:0.037s
                            copy_dir_to_dir_562_12068()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=12069) as unwtar_563_12069:  # 0m:1.071s
                            unwtar_563_12069()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=12070, recursive=True) as chown_564_12070:  # 0m:0.000s
                            chown_564_12070()
            with Stage(r"copy", r"Q10 v15.5.79.262", prog_num=12071):  # 0m:0.209s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12072) as should_copy_source_565_12072:  # 0m:0.209s
                    should_copy_source_565_12072()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=12073):  # 0m:0.209s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=12074) as copy_dir_to_dir_566_12074:  # 0m:0.034s
                            copy_dir_to_dir_566_12074()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=12075) as unwtar_567_12075:  # 0m:0.174s
                            unwtar_567_12075()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q10.bundle", user_id=-1, group_id=-1, prog_num=12076, recursive=True) as chown_568_12076:  # 0m:0.000s
                            chown_568_12076()
            with Stage(r"copy", r"Q-Clone v15.5.79.262", prog_num=12077):  # 0m:0.203s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12078) as should_copy_source_569_12078:  # 0m:0.203s
                    should_copy_source_569_12078()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=12079):  # 0m:0.203s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=12080) as copy_dir_to_dir_570_12080:  # 0m:0.035s
                            copy_dir_to_dir_570_12080()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=12081) as unwtar_571_12081:  # 0m:0.167s
                            unwtar_571_12081()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=12082, recursive=True) as chown_572_12082:  # 0m:0.000s
                            chown_572_12082()
            with Stage(r"copy", r"RBass v15.5.79.262", prog_num=12083):  # 0m:0.141s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12084) as should_copy_source_573_12084:  # 0m:0.141s
                    should_copy_source_573_12084()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=12085):  # 0m:0.141s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=12086) as copy_dir_to_dir_574_12086:  # 0m:0.033s
                            copy_dir_to_dir_574_12086()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=12087) as unwtar_575_12087:  # 0m:0.107s
                            unwtar_575_12087()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RBass.bundle", user_id=-1, group_id=-1, prog_num=12088, recursive=True) as chown_576_12088:  # 0m:0.000s
                            chown_576_12088()
            with Stage(r"copy", r"RChannel v15.5.79.262", prog_num=12089):  # 0m:0.206s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12090) as should_copy_source_577_12090:  # 0m:0.206s
                    should_copy_source_577_12090()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=12091):  # 0m:0.205s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=12092) as copy_dir_to_dir_578_12092:  # 0m:0.032s
                            copy_dir_to_dir_578_12092()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=12093) as unwtar_579_12093:  # 0m:0.172s
                            unwtar_579_12093()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RChannel.bundle", user_id=-1, group_id=-1, prog_num=12094, recursive=True) as chown_580_12094:  # 0m:0.000s
                            chown_580_12094()
            with Stage(r"copy", r"RComp v15.5.79.262", prog_num=12095):  # 0m:0.123s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12096) as should_copy_source_581_12096:  # 0m:0.123s
                    should_copy_source_581_12096()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=12097):  # 0m:0.123s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=12098) as copy_dir_to_dir_582_12098:  # 0m:0.033s
                            copy_dir_to_dir_582_12098()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=12099) as unwtar_583_12099:  # 0m:0.089s
                            unwtar_583_12099()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RComp.bundle", user_id=-1, group_id=-1, prog_num=12100, recursive=True) as chown_584_12100:  # 0m:0.000s
                            chown_584_12100()
            with Stage(r"copy", r"RDeEsser v15.5.79.262", prog_num=12101):  # 0m:0.239s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12102) as should_copy_source_585_12102:  # 0m:0.239s
                    should_copy_source_585_12102()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=12103):  # 0m:0.238s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=12104) as copy_dir_to_dir_586_12104:  # 0m:0.033s
                            copy_dir_to_dir_586_12104()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=12105) as unwtar_587_12105:  # 0m:0.205s
                            unwtar_587_12105()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=12106, recursive=True) as chown_588_12106:  # 0m:0.000s
                            chown_588_12106()
            with Stage(r"copy", r"REDD17 v15.5.79.262", prog_num=12107):  # 0m:0.143s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12108) as should_copy_source_589_12108:  # 0m:0.143s
                    should_copy_source_589_12108()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=12109):  # 0m:0.143s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=12110) as copy_dir_to_dir_590_12110:  # 0m:0.032s
                            copy_dir_to_dir_590_12110()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=12111) as unwtar_591_12111:  # 0m:0.110s
                            unwtar_591_12111()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD17.bundle", user_id=-1, group_id=-1, prog_num=12112, recursive=True) as chown_592_12112:  # 0m:0.000s
                            chown_592_12112()
            with Stage(r"copy", r"REDD37-51 v15.5.79.262", prog_num=12113):  # 0m:0.140s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12114) as should_copy_source_593_12114:  # 0m:0.140s
                    should_copy_source_593_12114()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=12115):  # 0m:0.140s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=12116) as copy_dir_to_dir_594_12116:  # 0m:0.032s
                            copy_dir_to_dir_594_12116()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=12117) as unwtar_595_12117:  # 0m:0.108s
                            unwtar_595_12117()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=12118, recursive=True) as chown_596_12118:  # 0m:0.000s
                            chown_596_12118()
            with Stage(r"copy", r"REQ v15.5.79.262", prog_num=12119):  # 0m:0.209s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12120) as should_copy_source_597_12120:  # 0m:0.209s
                    should_copy_source_597_12120()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=12121):  # 0m:0.209s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=12122) as copy_dir_to_dir_598_12122:  # 0m:0.031s
                            copy_dir_to_dir_598_12122()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=12123) as unwtar_599_12123:  # 0m:0.177s
                            unwtar_599_12123()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REQ.bundle", user_id=-1, group_id=-1, prog_num=12124, recursive=True) as chown_600_12124:  # 0m:0.000s
                            chown_600_12124()
            with Stage(r"copy", r"RS56 v15.5.79.262", prog_num=12125):  # 0m:0.558s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12126) as should_copy_source_601_12126:  # 0m:0.558s
                    should_copy_source_601_12126()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=12127):  # 0m:0.558s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=12128) as copy_dir_to_dir_602_12128:  # 0m:0.030s
                            copy_dir_to_dir_602_12128()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=12129) as unwtar_603_12129:  # 0m:0.527s
                            unwtar_603_12129()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RS56.bundle", user_id=-1, group_id=-1, prog_num=12130, recursive=True) as chown_604_12130:  # 0m:0.000s
                            chown_604_12130()
            with Stage(r"copy", r"RVerb v15.5.79.262", prog_num=12131):  # 0m:0.166s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12132) as should_copy_source_605_12132:  # 0m:0.166s
                    should_copy_source_605_12132()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=12133):  # 0m:0.165s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=12134) as copy_dir_to_dir_606_12134:  # 0m:0.033s
                            copy_dir_to_dir_606_12134()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=12135) as unwtar_607_12135:  # 0m:0.131s
                            unwtar_607_12135()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVerb.bundle", user_id=-1, group_id=-1, prog_num=12136, recursive=True) as chown_608_12136:  # 0m:0.000s
                            chown_608_12136()
            with Stage(r"copy", r"RVox v15.5.79.262", prog_num=12137):  # 0m:0.147s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12138) as should_copy_source_609_12138:  # 0m:0.147s
                    should_copy_source_609_12138()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=12139):  # 0m:0.146s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=12140) as copy_dir_to_dir_610_12140:  # 0m:0.034s
                            copy_dir_to_dir_610_12140()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=12141) as unwtar_611_12141:  # 0m:0.111s
                            unwtar_611_12141()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVox.bundle", user_id=-1, group_id=-1, prog_num=12142, recursive=True) as chown_612_12142:  # 0m:0.000s
                            chown_612_12142()
            with Stage(r"copy", r"Reel ADT v15.5.79.262", prog_num=12143):  # 0m:0.701s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12144) as should_copy_source_613_12144:  # 0m:0.701s
                    should_copy_source_613_12144()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=12145):  # 0m:0.700s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=12146) as copy_dir_to_dir_614_12146:  # 0m:0.032s
                            copy_dir_to_dir_614_12146()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=12147) as unwtar_615_12147:  # 0m:0.668s
                            unwtar_615_12147()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=12148, recursive=True) as chown_616_12148:  # 0m:0.000s
                            chown_616_12148()
            with Stage(r"copy", r"RenAxx v15.5.79.262", prog_num=12149):  # 0m:0.155s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12150) as should_copy_source_617_12150:  # 0m:0.155s
                    should_copy_source_617_12150()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=12151):  # 0m:0.155s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=12152) as copy_dir_to_dir_618_12152:  # 0m:0.033s
                            copy_dir_to_dir_618_12152()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=12153) as unwtar_619_12153:  # 0m:0.121s
                            unwtar_619_12153()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=12154, recursive=True) as chown_620_12154:  # 0m:0.000s
                            chown_620_12154()
            with Stage(r"copy", r"Retro Fi v15.5.79.262", prog_num=12155):  # 0m:2.153s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12156) as should_copy_source_621_12156:  # 0m:2.153s
                    should_copy_source_621_12156()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=12157):  # 0m:2.153s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=12158) as copy_dir_to_dir_622_12158:  # 0m:0.460s
                            copy_dir_to_dir_622_12158()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=12159) as unwtar_623_12159:  # 0m:1.692s
                            unwtar_623_12159()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=12160, recursive=True) as chown_624_12160:  # 0m:0.000s
                            chown_624_12160()
            with Stage(r"copy", r"S1 v15.5.79.262", prog_num=12161):  # 0m:0.146s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12162) as should_copy_source_625_12162:  # 0m:0.146s
                    should_copy_source_625_12162()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=12163):  # 0m:0.146s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=12164) as copy_dir_to_dir_626_12164:  # 0m:0.039s
                            copy_dir_to_dir_626_12164()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=12165) as unwtar_627_12165:  # 0m:0.106s
                            unwtar_627_12165()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/S1.bundle", user_id=-1, group_id=-1, prog_num=12166, recursive=True) as chown_628_12166:  # 0m:0.000s
                            chown_628_12166()
            with Stage(r"copy", r"Scheps 73 v15.5.79.262", prog_num=12167):  # 0m:0.852s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12168) as should_copy_source_629_12168:  # 0m:0.852s
                    should_copy_source_629_12168()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=12169):  # 0m:0.852s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=12170) as copy_dir_to_dir_630_12170:  # 0m:0.043s
                            copy_dir_to_dir_630_12170()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=12171) as unwtar_631_12171:  # 0m:0.808s
                            unwtar_631_12171()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=12172, recursive=True) as chown_632_12172:  # 0m:0.000s
                            chown_632_12172()
            with Stage(r"copy", r"Scheps Omni Channel v15.5.79.262", prog_num=12173):  # 0m:1.291s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12174) as should_copy_source_633_12174:  # 0m:1.290s
                    should_copy_source_633_12174()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=12175):  # 0m:1.290s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=12176) as copy_dir_to_dir_634_12176:  # 0m:0.265s
                            copy_dir_to_dir_634_12176()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=12177) as unwtar_635_12177:  # 0m:1.025s
                            unwtar_635_12177()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=12178, recursive=True) as chown_636_12178:  # 0m:0.000s
                            chown_636_12178()
            with Stage(r"copy", r"Scheps Parallel Particles v15.5.79.262", prog_num=12179):  # 0m:1.655s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12180) as should_copy_source_637_12180:  # 0m:1.654s
                    should_copy_source_637_12180()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=12181):  # 0m:1.654s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=12182) as copy_dir_to_dir_638_12182:  # 0m:0.229s
                            copy_dir_to_dir_638_12182()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=12183) as unwtar_639_12183:  # 0m:1.425s
                            unwtar_639_12183()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=12184, recursive=True) as chown_640_12184:  # 0m:0.000s
                            chown_640_12184()
            with Stage(r"copy", r"Sibilance v15.5.79.262", prog_num=12185):  # 0m:0.617s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12186) as should_copy_source_641_12186:  # 0m:0.617s
                    should_copy_source_641_12186()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=12187):  # 0m:0.617s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=12188) as copy_dir_to_dir_642_12188:  # 0m:0.038s
                            copy_dir_to_dir_642_12188()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=12189) as unwtar_643_12189:  # 0m:0.578s
                            unwtar_643_12189()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=12190, recursive=True) as chown_644_12190:  # 0m:0.000s
                            chown_644_12190()
            with Stage(r"copy", r"Emo Signal Generator v15.5.79.262", prog_num=12191):  # 0m:0.128s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12192) as should_copy_source_645_12192:  # 0m:0.128s
                    should_copy_source_645_12192()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=12193):  # 0m:0.128s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=12194) as copy_dir_to_dir_646_12194:  # 0m:0.045s
                            copy_dir_to_dir_646_12194()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=12195) as unwtar_647_12195:  # 0m:0.082s
                            unwtar_647_12195()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=12196, recursive=True) as chown_648_12196:  # 0m:0.000s
                            chown_648_12196()
            with Stage(r"copy", r"Smack Attack v15.5.79.262", prog_num=12197):  # 0m:0.221s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12198) as should_copy_source_649_12198:  # 0m:0.220s
                    should_copy_source_649_12198()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=12199):  # 0m:0.220s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=12200) as copy_dir_to_dir_650_12200:  # 0m:0.034s
                            copy_dir_to_dir_650_12200()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=12201) as unwtar_651_12201:  # 0m:0.185s
                            unwtar_651_12201()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=12202, recursive=True) as chown_652_12202:  # 0m:0.000s
                            chown_652_12202()
            with Stage(r"copy", r"SoundShifter v15.5.79.262", prog_num=12203):  # 0m:0.126s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12204) as should_copy_source_653_12204:  # 0m:0.126s
                    should_copy_source_653_12204()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=12205):  # 0m:0.125s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=12206) as copy_dir_to_dir_654_12206:  # 0m:0.033s
                            copy_dir_to_dir_654_12206()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=12207) as unwtar_655_12207:  # 0m:0.092s
                            unwtar_655_12207()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=12208, recursive=True) as chown_656_12208:  # 0m:0.000s
                            chown_656_12208()
            with Stage(r"copy", r"Spherix Immersive Compressor v15.5.79.262", prog_num=12209):  # 0m:0.165s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12210) as should_copy_source_657_12210:  # 0m:0.165s
                    should_copy_source_657_12210()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=12211):  # 0m:0.164s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=12212) as copy_dir_to_dir_658_12212:  # 0m:0.030s
                            copy_dir_to_dir_658_12212()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=12213) as unwtar_659_12213:  # 0m:0.134s
                            unwtar_659_12213()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=12214, recursive=True) as chown_660_12214:  # 0m:0.000s
                            chown_660_12214()
            with Stage(r"copy", r"Spherix Immersive Limiter v15.5.79.262", prog_num=12215):  # 0m:0.170s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12216) as should_copy_source_661_12216:  # 0m:0.170s
                    should_copy_source_661_12216()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=12217):  # 0m:0.169s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=12218) as copy_dir_to_dir_662_12218:  # 0m:0.031s
                            copy_dir_to_dir_662_12218()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=12219) as unwtar_663_12219:  # 0m:0.138s
                            unwtar_663_12219()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=12220, recursive=True) as chown_664_12220:  # 0m:0.000s
                            chown_664_12220()
            with Stage(r"copy", r"SuperTap v15.5.79.262", prog_num=12221):  # 0m:0.281s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12222) as should_copy_source_665_12222:  # 0m:0.281s
                    should_copy_source_665_12222()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=12223):  # 0m:0.281s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=12224) as copy_dir_to_dir_666_12224:  # 0m:0.032s
                            copy_dir_to_dir_666_12224()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=12225) as unwtar_667_12225:  # 0m:0.248s
                            unwtar_667_12225()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=12226, recursive=True) as chown_668_12226:  # 0m:0.000s
                            chown_668_12226()
            with Stage(r"copy", r"TG12345 v15.5.79.262", prog_num=12227):  # 0m:0.836s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12228) as should_copy_source_669_12228:  # 0m:0.836s
                    should_copy_source_669_12228()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=12229):  # 0m:0.836s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=12230) as copy_dir_to_dir_670_12230:  # 0m:0.034s
                            copy_dir_to_dir_670_12230()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=12231) as unwtar_671_12231:  # 0m:0.801s
                            unwtar_671_12231()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TG12345.bundle", user_id=-1, group_id=-1, prog_num=12232, recursive=True) as chown_672_12232:  # 0m:0.000s
                            chown_672_12232()
            with Stage(r"copy", r"AR TG Meter Bridge v15.5.79.262", prog_num=12233):  # 0m:0.194s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12234) as should_copy_source_673_12234:  # 0m:0.194s
                    should_copy_source_673_12234()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=12235):  # 0m:0.193s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=12236) as copy_dir_to_dir_674_12236:  # 0m:0.032s
                            copy_dir_to_dir_674_12236()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=12237) as unwtar_675_12237:  # 0m:0.161s
                            unwtar_675_12237()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=12238, recursive=True) as chown_676_12238:  # 0m:0.000s
                            chown_676_12238()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v15.5.79.262", prog_num=12239):  # 0m:1.309s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12240) as should_copy_source_677_12240:  # 0m:1.309s
                    should_copy_source_677_12240()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=12241):  # 0m:1.309s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=12242) as copy_dir_to_dir_678_12242:  # 0m:0.268s
                            copy_dir_to_dir_678_12242()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=12243) as unwtar_679_12243:  # 0m:1.040s
                            unwtar_679_12243()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=12244, recursive=True) as chown_680_12244:  # 0m:0.000s
                            chown_680_12244()
            with Stage(r"copy", r"TransX v15.5.79.262", prog_num=12245):  # 0m:0.105s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12246) as should_copy_source_681_12246:  # 0m:0.105s
                    should_copy_source_681_12246()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=12247):  # 0m:0.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=12248) as copy_dir_to_dir_682_12248:  # 0m:0.034s
                            copy_dir_to_dir_682_12248()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=12249) as unwtar_683_12249:  # 0m:0.071s
                            unwtar_683_12249()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TransX.bundle", user_id=-1, group_id=-1, prog_num=12250, recursive=True) as chown_684_12250:  # 0m:0.000s
                            chown_684_12250()
            with Stage(r"copy", r"TrueVerb v15.5.79.262", prog_num=12251):  # 0m:0.122s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12252) as should_copy_source_685_12252:  # 0m:0.121s
                    should_copy_source_685_12252()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=12253):  # 0m:0.121s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=12254) as copy_dir_to_dir_686_12254:  # 0m:0.032s
                            copy_dir_to_dir_686_12254()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=12255) as unwtar_687_12255:  # 0m:0.088s
                            unwtar_687_12255()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=12256, recursive=True) as chown_688_12256:  # 0m:0.000s
                            chown_688_12256()
            with Stage(r"copy", r"UM v15.5.79.262", prog_num=12257):  # 0m:0.120s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12258) as should_copy_source_689_12258:  # 0m:0.119s
                    should_copy_source_689_12258()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=12259):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=12260) as copy_dir_to_dir_690_12260:  # 0m:0.030s
                            copy_dir_to_dir_690_12260()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=12261) as unwtar_691_12261:  # 0m:0.089s
                            unwtar_691_12261()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UM.bundle", user_id=-1, group_id=-1, prog_num=12262, recursive=True) as chown_692_12262:  # 0m:0.000s
                            chown_692_12262()
            with Stage(r"copy", r"UltraPitch v15.5.79.262", prog_num=12263):  # 0m:0.147s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12264) as should_copy_source_693_12264:  # 0m:0.147s
                    should_copy_source_693_12264()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=12265):  # 0m:0.146s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=12266) as copy_dir_to_dir_694_12266:  # 0m:0.037s
                            copy_dir_to_dir_694_12266()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=12267) as unwtar_695_12267:  # 0m:0.109s
                            unwtar_695_12267()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=12268, recursive=True) as chown_696_12268:  # 0m:0.000s
                            chown_696_12268()
            with Stage(r"copy", r"VComp v15.5.79.262", prog_num=12269):  # 0m:0.283s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12270) as should_copy_source_697_12270:  # 0m:0.283s
                    should_copy_source_697_12270()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=12271):  # 0m:0.282s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=12272) as copy_dir_to_dir_698_12272:  # 0m:0.033s
                            copy_dir_to_dir_698_12272()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=12273) as unwtar_699_12273:  # 0m:0.249s
                            unwtar_699_12273()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VComp.bundle", user_id=-1, group_id=-1, prog_num=12274, recursive=True) as chown_700_12274:  # 0m:0.000s
                            chown_700_12274()
            with Stage(r"copy", r"VEQ3 v15.5.79.262", prog_num=12275):  # 0m:0.165s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12276) as should_copy_source_701_12276:  # 0m:0.165s
                    should_copy_source_701_12276()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=12277):  # 0m:0.165s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=12278) as copy_dir_to_dir_702_12278:  # 0m:0.030s
                            copy_dir_to_dir_702_12278()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=12279) as unwtar_703_12279:  # 0m:0.134s
                            unwtar_703_12279()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=12280, recursive=True) as chown_704_12280:  # 0m:0.000s
                            chown_704_12280()
            with Stage(r"copy", r"VEQ4 v15.5.79.262", prog_num=12281):  # 0m:0.173s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12282) as should_copy_source_705_12282:  # 0m:0.173s
                    should_copy_source_705_12282()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=12283):  # 0m:0.173s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=12284) as copy_dir_to_dir_706_12284:  # 0m:0.030s
                            copy_dir_to_dir_706_12284()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=12285) as unwtar_707_12285:  # 0m:0.142s
                            unwtar_707_12285()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=12286, recursive=True) as chown_708_12286:  # 0m:0.000s
                            chown_708_12286()
            with Stage(r"copy", r"VU Meter v15.5.79.262", prog_num=12287):  # 0m:2.202s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12288) as should_copy_source_709_12288:  # 0m:2.202s
                    should_copy_source_709_12288()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=12289):  # 0m:2.202s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=12290) as copy_dir_to_dir_710_12290:  # 0m:0.033s
                            copy_dir_to_dir_710_12290()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=12291) as unwtar_711_12291:  # 0m:2.169s
                            unwtar_711_12291()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=12292, recursive=True) as chown_712_12292:  # 0m:0.000s
                            chown_712_12292()
            with Stage(r"copy", r"Vitamin v15.5.79.262", prog_num=12293):  # 0m:0.114s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12294) as should_copy_source_713_12294:  # 0m:0.114s
                    should_copy_source_713_12294()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=12295):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=12296) as copy_dir_to_dir_714_12296:  # 0m:0.029s
                            copy_dir_to_dir_714_12296()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=12297) as unwtar_715_12297:  # 0m:0.084s
                            unwtar_715_12297()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=12298, recursive=True) as chown_716_12298:  # 0m:0.000s
                            chown_716_12298()
            with Stage(r"copy", r"Vocal Rider v15.5.79.262", prog_num=12299):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12300) as should_copy_source_717_12300:  # 0m:0.111s
                    should_copy_source_717_12300()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=12301):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=12302) as copy_dir_to_dir_718_12302:  # 0m:0.030s
                            copy_dir_to_dir_718_12302()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=12303) as unwtar_719_12303:  # 0m:0.080s
                            unwtar_719_12303()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=12304, recursive=True) as chown_720_12304:  # 0m:0.000s
                            chown_720_12304()
            with Stage(r"copy", r"Voltage Amps Bass v15.5.79.262", prog_num=12305):  # 0m:1.336s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12306) as should_copy_source_721_12306:  # 0m:1.336s
                    should_copy_source_721_12306()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=12307):  # 0m:1.336s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=12308) as copy_dir_to_dir_722_12308:  # 0m:0.344s
                            copy_dir_to_dir_722_12308()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=12309) as unwtar_723_12309:  # 0m:0.991s
                            unwtar_723_12309()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=12310, recursive=True) as chown_724_12310:  # 0m:0.000s
                            chown_724_12310()
            with Stage(r"copy", r"Voltage Amps Guitar v15.5.79.262", prog_num=12311):  # 0m:1.385s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12312) as should_copy_source_725_12312:  # 0m:1.385s
                    should_copy_source_725_12312()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=12313):  # 0m:1.385s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=12314) as copy_dir_to_dir_726_12314:  # 0m:0.341s
                            copy_dir_to_dir_726_12314()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=12315) as unwtar_727_12315:  # 0m:1.043s
                            unwtar_727_12315()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=12316, recursive=True) as chown_728_12316:  # 0m:0.000s
                            chown_728_12316()
            with Stage(r"copy", r"WLM v15.5.79.262", prog_num=12317):  # 0m:0.191s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12318) as should_copy_source_729_12318:  # 0m:0.191s
                    should_copy_source_729_12318()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=12319):  # 0m:0.191s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=12320) as copy_dir_to_dir_730_12320:  # 0m:0.037s
                            copy_dir_to_dir_730_12320()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=12321) as unwtar_731_12321:  # 0m:0.153s
                            unwtar_731_12321()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM.bundle", user_id=-1, group_id=-1, prog_num=12322, recursive=True) as chown_732_12322:  # 0m:0.000s
                            chown_732_12322()
            with Stage(r"copy", r"WLM Plus v15.5.79.262", prog_num=12323):  # 0m:0.182s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12324) as should_copy_source_733_12324:  # 0m:0.182s
                    should_copy_source_733_12324()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=12325):  # 0m:0.181s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=12326) as copy_dir_to_dir_734_12326:  # 0m:0.032s
                            copy_dir_to_dir_734_12326()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=12327) as unwtar_735_12327:  # 0m:0.148s
                            unwtar_735_12327()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=12328, recursive=True) as chown_736_12328:  # 0m:0.000s
                            chown_736_12328()
            with Stage(r"copy", r"WavesHeadTracker v15.5.79.262", prog_num=12329):  # 0m:2.262s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=5, prog_num=12330) as should_copy_source_737_12330:  # 0m:2.261s
                    should_copy_source_737_12330()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=12331):  # 0m:2.261s
                        with RmFileOrDir(r"/WavesHeadTracker", prog_num=12332) as rm_file_or_dir_738_12332:  # 0m:0.000s
                            rm_file_or_dir_738_12332()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=12333) as copy_dir_to_dir_739_12333:  # 0m:0.050s
                            copy_dir_to_dir_739_12333()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=12334) as unwtar_740_12334:  # 0m:2.210s
                            unwtar_740_12334()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=12335, recursive=True) as chown_741_12335:  # 0m:0.000s
                            chown_741_12335()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=12336):  # 0m:0.381s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12337) as should_copy_source_742_12337:  # 0m:0.381s
                    should_copy_source_742_12337()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=12338):  # 0m:0.381s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=12339) as copy_dir_to_dir_743_12339:  # 0m:0.011s
                            copy_dir_to_dir_743_12339()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=12340) as unwtar_744_12340:  # 0m:0.369s
                            unwtar_744_12340()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=12341, recursive=True) as chown_745_12341:  # 0m:0.000s
                            chown_745_12341()
            with Stage(r"copy", r"WavesTune v15.5.79.262", prog_num=12342):  # 0m:0.164s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12343) as should_copy_source_746_12343:  # 0m:0.164s
                    should_copy_source_746_12343()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=12344):  # 0m:0.163s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=12345) as copy_dir_to_dir_747_12345:  # 0m:0.034s
                            copy_dir_to_dir_747_12345()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=12346) as unwtar_748_12346:  # 0m:0.128s
                            unwtar_748_12346()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=12347, recursive=True) as chown_749_12347:  # 0m:0.000s
                            chown_749_12347()
            with Stage(r"copy", r"WavesTune LT v15.5.79.262", prog_num=12348):  # 0m:0.162s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12349) as should_copy_source_750_12349:  # 0m:0.162s
                    should_copy_source_750_12349()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=12350):  # 0m:0.161s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=12351) as copy_dir_to_dir_751_12351:  # 0m:0.037s
                            copy_dir_to_dir_751_12351()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=12352) as unwtar_752_12352:  # 0m:0.124s
                            unwtar_752_12352()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=12353, recursive=True) as chown_753_12353:  # 0m:0.000s
                            chown_753_12353()
            with Stage(r"copy", r"Waves Harmony v15.5.79.262", prog_num=12354):  # 0m:0.409s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12355) as should_copy_source_754_12355:  # 0m:0.409s
                    should_copy_source_754_12355()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=12356):  # 0m:0.408s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=12357) as copy_dir_to_dir_755_12357:  # 0m:0.033s
                            copy_dir_to_dir_755_12357()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=12358) as unwtar_756_12358:  # 0m:0.375s
                            unwtar_756_12358()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=12359, recursive=True) as chown_757_12359:  # 0m:0.000s
                            chown_757_12359()
            with Stage(r"copy", r"Waves Tune Real-Time v15.5.79.262", prog_num=12360):  # 0m:0.292s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12361) as should_copy_source_758_12361:  # 0m:0.292s
                    should_copy_source_758_12361()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=12362):  # 0m:0.292s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=12363) as copy_dir_to_dir_759_12363:  # 0m:0.033s
                            copy_dir_to_dir_759_12363()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=12364) as unwtar_760_12364:  # 0m:0.259s
                            unwtar_760_12364()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=12365, recursive=True) as chown_761_12365:  # 0m:0.000s
                            chown_761_12365()
            with Stage(r"copy", r"X-Click v15.5.79.262", prog_num=12366):  # 0m:0.105s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12367) as should_copy_source_762_12367:  # 0m:0.105s
                    should_copy_source_762_12367()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=12368):  # 0m:0.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=12369) as copy_dir_to_dir_763_12369:  # 0m:0.034s
                            copy_dir_to_dir_763_12369()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=12370) as unwtar_764_12370:  # 0m:0.070s
                            unwtar_764_12370()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Click.bundle", user_id=-1, group_id=-1, prog_num=12371, recursive=True) as chown_765_12371:  # 0m:0.000s
                            chown_765_12371()
            with Stage(r"copy", r"X-Crackle v15.5.79.262", prog_num=12372):  # 0m:0.107s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12373) as should_copy_source_766_12373:  # 0m:0.107s
                    should_copy_source_766_12373()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=12374):  # 0m:0.107s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=12375) as copy_dir_to_dir_767_12375:  # 0m:0.029s
                            copy_dir_to_dir_767_12375()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=12376) as unwtar_768_12376:  # 0m:0.077s
                            unwtar_768_12376()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=12377, recursive=True) as chown_769_12377:  # 0m:0.000s
                            chown_769_12377()
            with Stage(r"copy", r"X-Hum v15.5.79.262", prog_num=12378):  # 0m:0.103s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12379) as should_copy_source_770_12379:  # 0m:0.103s
                    should_copy_source_770_12379()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=12380):  # 0m:0.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=12381) as copy_dir_to_dir_771_12381:  # 0m:0.032s
                            copy_dir_to_dir_771_12381()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=12382) as unwtar_772_12382:  # 0m:0.071s
                            unwtar_772_12382()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=12383, recursive=True) as chown_773_12383:  # 0m:0.000s
                            chown_773_12383()
            with Stage(r"copy", r"X-Noise v15.5.79.262", prog_num=12384):  # 0m:0.118s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12385) as should_copy_source_774_12385:  # 0m:0.117s
                    should_copy_source_774_12385()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=12386):  # 0m:0.117s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12387) as copy_dir_to_dir_775_12387:  # 0m:0.031s
                            copy_dir_to_dir_775_12387()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=12388) as unwtar_776_12388:  # 0m:0.086s
                            unwtar_776_12388()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=12389, recursive=True) as chown_777_12389:  # 0m:0.000s
                            chown_777_12389()
            with Stage(r"copy", r"Z-Noise v15.5.79.262", prog_num=12390):  # 0m:0.126s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12391) as should_copy_source_778_12391:  # 0m:0.125s
                    should_copy_source_778_12391()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=12392):  # 0m:0.125s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12393) as copy_dir_to_dir_779_12393:  # 0m:0.027s
                            copy_dir_to_dir_779_12393()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=12394) as unwtar_780_12394:  # 0m:0.098s
                            unwtar_780_12394()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=12395, recursive=True) as chown_781_12395:  # 0m:0.000s
                            chown_781_12395()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=2, prog_num=12397) as resolve_symlink_files_in_folder_782_12397:  # 0m:0.188s
                resolve_symlink_files_in_folder_782_12397()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=12398) as shell_command_783_12398:  # 0m:0.117s
                shell_command_783_12398()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=12399) as script_command_784_12399:  # 0m:0.013s
                script_command_784_12399()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12400) as shell_command_785_12400:  # 0m:4.039s
                shell_command_785_12400()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12401) as create_symlink_786_12401:  # 0m:0.001s
                create_symlink_786_12401()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12402) as create_symlink_787_12402:  # 0m:0.000s
                create_symlink_787_12402()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=12403) as copy_glob_to_dir_788_12403:  # 0m:0.059s
                copy_glob_to_dir_788_12403()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=12404) as cd_stage_789_12404:  # 0m:0.000s
            cd_stage_789_12404()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=12405):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=12406) as should_copy_source_790_12406:  # ?
                    should_copy_source_790_12406()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=12407):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=12408) as copy_file_to_dir_791_12408:  # ?
                            copy_file_to_dir_791_12408()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=12409) as chmod_and_chown_792_12409:  # 0m:0.000s
                            chmod_and_chown_792_12409()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/GTR", prog_num=12410) as cd_stage_793_12410:  # 0m:3.202s
            cd_stage_793_12410()
            with Stage(r"copy", r"GTR Stomps v15.5.79.262", prog_num=12411):  # 0m:2.417s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12412) as should_copy_source_794_12412:  # 0m:0.105s
                    should_copy_source_794_12412()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=12413):  # 0m:0.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=12414) as copy_dir_to_dir_795_12414:  # 0m:0.042s
                            copy_dir_to_dir_795_12414()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=12415) as unwtar_796_12415:  # 0m:0.063s
                            unwtar_796_12415()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=12416, recursive=True) as chown_797_12416:  # 0m:0.000s
                            chown_797_12416()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12417) as should_copy_source_798_12417:  # 0m:0.105s
                    should_copy_source_798_12417()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=12418):  # 0m:0.104s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=12419) as copy_dir_to_dir_799_12419:  # 0m:0.038s
                            copy_dir_to_dir_799_12419()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=12420) as unwtar_800_12420:  # 0m:0.066s
                            unwtar_800_12420()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=12421, recursive=True) as chown_801_12421:  # 0m:0.000s
                            chown_801_12421()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12422) as should_copy_source_802_12422:  # 0m:0.104s
                    should_copy_source_802_12422()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=12423):  # 0m:0.104s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=12424) as copy_dir_to_dir_803_12424:  # 0m:0.038s
                            copy_dir_to_dir_803_12424()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=12425) as unwtar_804_12425:  # 0m:0.065s
                            unwtar_804_12425()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=12426, recursive=True) as chown_805_12426:  # 0m:0.000s
                            chown_805_12426()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12427) as should_copy_source_806_12427:  # 0m:0.099s
                    should_copy_source_806_12427()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=12428):  # 0m:0.099s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=12429) as copy_dir_to_dir_807_12429:  # 0m:0.034s
                            copy_dir_to_dir_807_12429()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=12430) as unwtar_808_12430:  # 0m:0.065s
                            unwtar_808_12430()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=12431, recursive=True) as chown_809_12431:  # 0m:0.000s
                            chown_809_12431()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12432) as should_copy_source_810_12432:  # 0m:0.109s
                    should_copy_source_810_12432()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=12433):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=12434) as copy_dir_to_dir_811_12434:  # 0m:0.030s
                            copy_dir_to_dir_811_12434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=12435) as unwtar_812_12435:  # 0m:0.078s
                            unwtar_812_12435()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=12436, recursive=True) as chown_813_12436:  # 0m:0.000s
                            chown_813_12436()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12437) as should_copy_source_814_12437:  # 0m:0.097s
                    should_copy_source_814_12437()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=12438):  # 0m:0.097s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=12439) as copy_dir_to_dir_815_12439:  # 0m:0.034s
                            copy_dir_to_dir_815_12439()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=12440) as unwtar_816_12440:  # 0m:0.062s
                            unwtar_816_12440()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=12441, recursive=True) as chown_817_12441:  # 0m:0.000s
                            chown_817_12441()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12442) as should_copy_source_818_12442:  # 0m:0.098s
                    should_copy_source_818_12442()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=12443):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=12444) as copy_dir_to_dir_819_12444:  # 0m:0.033s
                            copy_dir_to_dir_819_12444()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=12445) as unwtar_820_12445:  # 0m:0.064s
                            unwtar_820_12445()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=12446, recursive=True) as chown_821_12446:  # 0m:0.000s
                            chown_821_12446()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12447) as should_copy_source_822_12447:  # 0m:0.093s
                    should_copy_source_822_12447()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=12448):  # 0m:0.093s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=12449) as copy_dir_to_dir_823_12449:  # 0m:0.034s
                            copy_dir_to_dir_823_12449()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=12450) as unwtar_824_12450:  # 0m:0.059s
                            unwtar_824_12450()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=12451, recursive=True) as chown_825_12451:  # 0m:0.000s
                            chown_825_12451()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12452) as should_copy_source_826_12452:  # 0m:0.098s
                    should_copy_source_826_12452()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=12453):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12454) as copy_dir_to_dir_827_12454:  # 0m:0.039s
                            copy_dir_to_dir_827_12454()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=12455) as unwtar_828_12455:  # 0m:0.058s
                            unwtar_828_12455()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=12456, recursive=True) as chown_829_12456:  # 0m:0.000s
                            chown_829_12456()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12457) as should_copy_source_830_12457:  # 0m:0.091s
                    should_copy_source_830_12457()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=12458):  # 0m:0.090s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=12459) as copy_dir_to_dir_831_12459:  # 0m:0.032s
                            copy_dir_to_dir_831_12459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=12460) as unwtar_832_12460:  # 0m:0.057s
                            unwtar_832_12460()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=12461, recursive=True) as chown_833_12461:  # 0m:0.000s
                            chown_833_12461()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12462) as should_copy_source_834_12462:  # 0m:0.091s
                    should_copy_source_834_12462()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=12463):  # 0m:0.091s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=12464) as copy_dir_to_dir_835_12464:  # 0m:0.033s
                            copy_dir_to_dir_835_12464()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=12465) as unwtar_836_12465:  # 0m:0.058s
                            unwtar_836_12465()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=12466, recursive=True) as chown_837_12466:  # 0m:0.000s
                            chown_837_12466()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12467) as should_copy_source_838_12467:  # 0m:0.091s
                    should_copy_source_838_12467()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=12468):  # 0m:0.090s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=12469) as copy_dir_to_dir_839_12469:  # 0m:0.031s
                            copy_dir_to_dir_839_12469()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=12470) as unwtar_840_12470:  # 0m:0.059s
                            unwtar_840_12470()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=12471, recursive=True) as chown_841_12471:  # 0m:0.000s
                            chown_841_12471()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12472) as should_copy_source_842_12472:  # 0m:0.091s
                    should_copy_source_842_12472()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=12473):  # 0m:0.091s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=12474) as copy_dir_to_dir_843_12474:  # 0m:0.032s
                            copy_dir_to_dir_843_12474()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=12475) as unwtar_844_12475:  # 0m:0.059s
                            unwtar_844_12475()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=12476, recursive=True) as chown_845_12476:  # 0m:0.000s
                            chown_845_12476()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12477) as should_copy_source_846_12477:  # 0m:0.103s
                    should_copy_source_846_12477()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=12478):  # 0m:0.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=12479) as copy_dir_to_dir_847_12479:  # 0m:0.039s
                            copy_dir_to_dir_847_12479()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=12480) as unwtar_848_12480:  # 0m:0.063s
                            unwtar_848_12480()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=12481, recursive=True) as chown_849_12481:  # 0m:0.000s
                            chown_849_12481()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12482) as should_copy_source_850_12482:  # 0m:0.090s
                    should_copy_source_850_12482()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=12483):  # 0m:0.090s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=12484) as copy_dir_to_dir_851_12484:  # 0m:0.031s
                            copy_dir_to_dir_851_12484()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=12485) as unwtar_852_12485:  # 0m:0.058s
                            unwtar_852_12485()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=12486, recursive=True) as chown_853_12486:  # 0m:0.000s
                            chown_853_12486()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12487) as should_copy_source_854_12487:  # 0m:0.097s
                    should_copy_source_854_12487()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=12488):  # 0m:0.096s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=12489) as copy_dir_to_dir_855_12489:  # 0m:0.033s
                            copy_dir_to_dir_855_12489()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=12490) as unwtar_856_12490:  # 0m:0.063s
                            unwtar_856_12490()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=12491, recursive=True) as chown_857_12491:  # 0m:0.000s
                            chown_857_12491()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12492) as should_copy_source_858_12492:  # 0m:0.098s
                    should_copy_source_858_12492()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=12493):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=12494) as copy_dir_to_dir_859_12494:  # 0m:0.037s
                            copy_dir_to_dir_859_12494()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=12495) as unwtar_860_12495:  # 0m:0.061s
                            unwtar_860_12495()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=12496, recursive=True) as chown_861_12496:  # 0m:0.000s
                            chown_861_12496()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12497) as should_copy_source_862_12497:  # 0m:0.091s
                    should_copy_source_862_12497()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=12498):  # 0m:0.091s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=12499) as copy_dir_to_dir_863_12499:  # 0m:0.032s
                            copy_dir_to_dir_863_12499()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=12500) as unwtar_864_12500:  # 0m:0.058s
                            unwtar_864_12500()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=12501, recursive=True) as chown_865_12501:  # 0m:0.000s
                            chown_865_12501()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12502) as should_copy_source_866_12502:  # 0m:0.093s
                    should_copy_source_866_12502()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=12503):  # 0m:0.092s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=12504) as copy_dir_to_dir_867_12504:  # 0m:0.032s
                            copy_dir_to_dir_867_12504()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=12505) as unwtar_868_12505:  # 0m:0.060s
                            unwtar_868_12505()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=12506, recursive=True) as chown_869_12506:  # 0m:0.000s
                            chown_869_12506()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12507) as should_copy_source_870_12507:  # 0m:0.093s
                    should_copy_source_870_12507()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=12508):  # 0m:0.092s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=12509) as copy_dir_to_dir_871_12509:  # 0m:0.031s
                            copy_dir_to_dir_871_12509()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=12510) as unwtar_872_12510:  # 0m:0.060s
                            unwtar_872_12510()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=12511, recursive=True) as chown_873_12511:  # 0m:0.000s
                            chown_873_12511()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12512) as should_copy_source_874_12512:  # 0m:0.097s
                    should_copy_source_874_12512()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=12513):  # 0m:0.097s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=12514) as copy_dir_to_dir_875_12514:  # 0m:0.031s
                            copy_dir_to_dir_875_12514()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=12515) as unwtar_876_12515:  # 0m:0.065s
                            unwtar_876_12515()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=12516, recursive=True) as chown_877_12516:  # 0m:0.000s
                            chown_877_12516()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12517) as should_copy_source_878_12517:  # 0m:0.099s
                    should_copy_source_878_12517()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=12518):  # 0m:0.099s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=12519) as copy_dir_to_dir_879_12519:  # 0m:0.034s
                            copy_dir_to_dir_879_12519()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=12520) as unwtar_880_12520:  # 0m:0.064s
                            unwtar_880_12520()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=12521, recursive=True) as chown_881_12521:  # 0m:0.000s
                            chown_881_12521()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12522) as should_copy_source_882_12522:  # 0m:0.098s
                    should_copy_source_882_12522()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=12523):  # 0m:0.097s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=12524) as copy_dir_to_dir_883_12524:  # 0m:0.035s
                            copy_dir_to_dir_883_12524()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=12525) as unwtar_884_12525:  # 0m:0.062s
                            unwtar_884_12525()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=12526, recursive=True) as chown_885_12526:  # 0m:0.000s
                            chown_885_12526()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12527) as should_copy_source_886_12527:  # 0m:0.093s
                    should_copy_source_886_12527()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=12528):  # 0m:0.092s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=12529) as copy_dir_to_dir_887_12529:  # 0m:0.034s
                            copy_dir_to_dir_887_12529()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=12530) as unwtar_888_12530:  # 0m:0.058s
                            unwtar_888_12530()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=12531, recursive=True) as chown_889_12531:  # 0m:0.000s
                            chown_889_12531()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12532) as should_copy_source_890_12532:  # 0m:0.091s
                    should_copy_source_890_12532()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=12533):  # 0m:0.091s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=12534) as copy_dir_to_dir_891_12534:  # 0m:0.030s
                            copy_dir_to_dir_891_12534()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=12535) as unwtar_892_12535:  # 0m:0.060s
                            unwtar_892_12535()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=12536, recursive=True) as chown_893_12536:  # 0m:0.000s
                            chown_893_12536()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12537) as shell_command_894_12537:  # 0m:0.785s
                shell_command_894_12537()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/ReWire", prog_num=12538) as cd_stage_895_12538:  # 0m:0.314s
            cd_stage_895_12538()
            with Stage(r"copy", r"backup ReWire to Waves folder", prog_num=12539):  # 0m:0.112s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12540) as should_copy_source_896_12540:  # 0m:0.052s
                    should_copy_source_896_12540()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=12541):  # 0m:0.052s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=12542) as copy_dir_to_dir_897_12542:  # 0m:0.020s
                            copy_dir_to_dir_897_12542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=12543) as unwtar_898_12543:  # 0m:0.031s
                            unwtar_898_12543()
                        with Chown(path=r"/Applications/Waves/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=12544, recursive=True) as chown_899_12544:  # 0m:0.000s
                            chown_899_12544()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12545) as should_copy_source_900_12545:  # 0m:0.060s
                    should_copy_source_900_12545()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=12546):  # 0m:0.060s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=12547) as copy_dir_to_dir_901_12547:  # 0m:0.018s
                            copy_dir_to_dir_901_12547()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=12548) as unwtar_902_12548:  # 0m:0.040s
                            unwtar_902_12548()
                        with Chown(path=r"/Applications/Waves/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=12549, recursive=True) as chown_903_12549:  # 0m:0.000s
                            chown_903_12549()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/ReWire" -c', ignore_all_errors=True, prog_num=12550) as shell_command_904_12550:  # 0m:0.118s
                shell_command_904_12550()
            with ScriptCommand(r'if [ -f "/Applications/Waves/ReWire"/Icon? ]; then chmod a+rw "/Applications/Waves/ReWire"/Icon?; fi', prog_num=12551) as script_command_905_12551:  # 0m:0.017s
                script_command_905_12551()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12552) as shell_command_906_12552:  # 0m:0.065s
                shell_command_906_12552()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=12553) as cd_stage_907_12553:  # 0m:3.143s
            cd_stage_907_12553()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.79.262", prog_num=12554):  # 0m:0.839s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12555) as should_copy_source_908_12555:  # 0m:0.839s
                    should_copy_source_908_12555()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12556):  # 0m:0.838s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12557) as copy_dir_to_dir_909_12557:  # 0m:0.064s
                            copy_dir_to_dir_909_12557()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12558) as unwtar_910_12558:  # 0m:0.718s
                            unwtar_910_12558()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12559, recursive=True) as chown_911_12559:  # 0m:0.000s
                            chown_911_12559()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12560) as shell_command_912_12560:  # 0m:0.055s
                            shell_command_912_12560()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=12561):  # 0m:0.792s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12562) as should_copy_source_913_12562:  # 0m:0.791s
                    should_copy_source_913_12562()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=12563):  # 0m:0.791s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=12564) as copy_dir_to_dir_914_12564:  # 0m:0.026s
                            copy_dir_to_dir_914_12564()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=12565) as unwtar_915_12565:  # 0m:0.682s
                            unwtar_915_12565()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12566, recursive=True) as chown_916_12566:  # 0m:0.000s
                            chown_916_12566()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=12567) as break_hard_link_917_12567:  # 0m:0.019s
                            break_hard_link_917_12567()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=12568) as shell_command_918_12568:  # 0m:0.052s
                            shell_command_918_12568()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12569, recursive=True) as chown_919_12569:  # 0m:0.000s
                            chown_919_12569()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=12570, recursive=True) as chmod_920_12570:  # 0m:0.011s
                            chmod_920_12570()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=12571):  # 0m:0.798s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12572) as should_copy_source_921_12572:  # 0m:0.797s
                    should_copy_source_921_12572()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=12573):  # 0m:0.797s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=12574) as copy_dir_to_dir_922_12574:  # 0m:0.018s
                            copy_dir_to_dir_922_12574()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=12575) as unwtar_923_12575:  # 0m:0.726s
                            unwtar_923_12575()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=12576, recursive=True) as chown_924_12576:  # 0m:0.000s
                            chown_924_12576()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=12577) as shell_command_925_12577:  # 0m:0.053s
                            shell_command_925_12577()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=12578):  # 0m:0.400s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12579) as should_copy_source_926_12579:  # 0m:0.399s
                    should_copy_source_926_12579()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=12580):  # 0m:0.399s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=12581) as copy_dir_to_dir_927_12581:  # 0m:0.024s
                            copy_dir_to_dir_927_12581()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=12582) as unwtar_928_12582:  # 0m:0.192s
                            unwtar_928_12582()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=12583, recursive=True) as chown_929_12583:  # 0m:0.000s
                            chown_929_12583()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12584) as shell_command_930_12584:  # 0m:0.106s
                            shell_command_930_12584()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12585) as script_command_931_12585:  # 0m:0.014s
                            script_command_931_12585()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12586) as shell_command_932_12586:  # 0m:0.061s
                            shell_command_932_12586()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=12587):  # 0m:0.193s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=12588) as should_copy_source_933_12588:  # 0m:0.192s
                    should_copy_source_933_12588()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=12589):  # 0m:0.192s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=12590) as copy_dir_to_dir_934_12590:  # 0m:0.031s
                            copy_dir_to_dir_934_12590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=12591) as unwtar_935_12591:  # 0m:0.161s
                            unwtar_935_12591()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=12592, recursive=True) as chown_936_12592:  # 0m:0.000s
                            chown_936_12592()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=12593) as shell_command_937_12593:  # 0m:0.120s
                shell_command_937_12593()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=12594) as cd_stage_938_12594:  # 0m:0.839s
            cd_stage_938_12594()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.79.262", prog_num=12595):  # 0m:0.838s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12596) as should_copy_source_939_12596:  # 0m:0.838s
                    should_copy_source_939_12596()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12597):  # 0m:0.838s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12598) as copy_dir_to_dir_940_12598:  # 0m:0.054s
                            copy_dir_to_dir_940_12598()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12599) as unwtar_941_12599:  # 0m:0.728s
                            unwtar_941_12599()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12600, recursive=True) as chown_942_12600:  # 0m:0.000s
                            chown_942_12600()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12601) as shell_command_943_12601:  # 0m:0.055s
                            shell_command_943_12601()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=12602) as cd_stage_944_12602:  # 0m:0.099s
            cd_stage_944_12602()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=12603):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12604) as should_copy_source_945_12604:  # ?
                    should_copy_source_945_12604()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=12605):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=12606) as copy_file_to_dir_946_12606:  # ?
                            copy_file_to_dir_946_12606()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12607) as chmod_and_chown_947_12607:  # 0m:0.001s
                            chmod_and_chown_947_12607()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=12608):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12609) as should_copy_source_948_12609:  # ?
                    should_copy_source_948_12609()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=12610):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=12611) as copy_file_to_dir_949_12611:  # ?
                            copy_file_to_dir_949_12611()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12612) as chmod_and_chown_950_12612:  # 0m:0.000s
                            chmod_and_chown_950_12612()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=12613):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12614) as should_copy_source_951_12614:  # ?
                    should_copy_source_951_12614()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=12615):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=12616) as copy_file_to_dir_952_12616:  # ?
                            copy_file_to_dir_952_12616()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12617) as chmod_and_chown_953_12617:  # 0m:0.000s
                            chmod_and_chown_953_12617()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=12618):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12619) as should_copy_source_954_12619:  # ?
                    should_copy_source_954_12619()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=12620):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=12621) as copy_file_to_dir_955_12621:  # ?
                            copy_file_to_dir_955_12621()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12622) as chmod_and_chown_956_12622:  # 0m:0.000s
                            chmod_and_chown_956_12622()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=12623):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12624) as should_copy_source_957_12624:  # ?
                    should_copy_source_957_12624()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=12625):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=12626) as copy_file_to_dir_958_12626:  # ?
                            copy_file_to_dir_958_12626()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12627) as chmod_and_chown_959_12627:  # 0m:0.000s
                            chmod_and_chown_959_12627()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=12628):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12629) as should_copy_source_960_12629:  # ?
                    should_copy_source_960_12629()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=12630):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=12631) as copy_file_to_dir_961_12631:  # ?
                            copy_file_to_dir_961_12631()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12632) as chmod_and_chown_962_12632:  # 0m:0.000s
                            chmod_and_chown_962_12632()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=12633):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12634) as should_copy_source_963_12634:  # ?
                    should_copy_source_963_12634()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=12635):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=12636) as copy_file_to_dir_964_12636:  # ?
                            copy_file_to_dir_964_12636()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12637) as chmod_and_chown_965_12637:  # 0m:0.000s
                            chmod_and_chown_965_12637()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=12638):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12639) as should_copy_source_966_12639:  # ?
                    should_copy_source_966_12639()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=12640):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=12641) as copy_file_to_dir_967_12641:  # ?
                            copy_file_to_dir_967_12641()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12642) as chmod_and_chown_968_12642:  # 0m:0.000s
                            chmod_and_chown_968_12642()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=12643):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12644) as should_copy_source_969_12644:  # ?
                    should_copy_source_969_12644()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=12645):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=12646) as copy_file_to_dir_970_12646:  # ?
                            copy_file_to_dir_970_12646()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12647) as chmod_and_chown_971_12647:  # 0m:0.000s
                            chmod_and_chown_971_12647()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=12648):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12649) as should_copy_source_972_12649:  # ?
                    should_copy_source_972_12649()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=12650):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=12651) as copy_file_to_dir_973_12651:  # ?
                            copy_file_to_dir_973_12651()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12652) as chmod_and_chown_974_12652:  # 0m:0.000s
                            chmod_and_chown_974_12652()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=12653):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12654) as should_copy_source_975_12654:  # ?
                    should_copy_source_975_12654()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=12655):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=12656) as copy_file_to_dir_976_12656:  # ?
                            copy_file_to_dir_976_12656()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12657) as chmod_and_chown_977_12657:  # 0m:0.000s
                            chmod_and_chown_977_12657()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=12658):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12659) as should_copy_source_978_12659:  # ?
                    should_copy_source_978_12659()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=12660):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=12661) as copy_file_to_dir_979_12661:  # ?
                            copy_file_to_dir_979_12661()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12662) as chmod_and_chown_980_12662:  # 0m:0.000s
                            chmod_and_chown_980_12662()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=12663):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12664) as should_copy_source_981_12664:  # ?
                    should_copy_source_981_12664()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=12665):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=12666) as copy_file_to_dir_982_12666:  # ?
                            copy_file_to_dir_982_12666()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12667) as chmod_and_chown_983_12667:  # 0m:0.000s
                            chmod_and_chown_983_12667()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=12668):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12669) as should_copy_source_984_12669:  # ?
                    should_copy_source_984_12669()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=12670):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=12671) as copy_file_to_dir_985_12671:  # ?
                            copy_file_to_dir_985_12671()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12672) as chmod_and_chown_986_12672:  # 0m:0.000s
                            chmod_and_chown_986_12672()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=12673):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12674) as should_copy_source_987_12674:  # ?
                    should_copy_source_987_12674()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=12675):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=12676) as copy_file_to_dir_988_12676:  # ?
                            copy_file_to_dir_988_12676()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12677) as chmod_and_chown_989_12677:  # 0m:0.000s
                            chmod_and_chown_989_12677()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=12678):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12679) as should_copy_source_990_12679:  # ?
                    should_copy_source_990_12679()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=12680):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=12681) as copy_file_to_dir_991_12681:  # ?
                            copy_file_to_dir_991_12681()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12682) as chmod_and_chown_992_12682:  # 0m:0.000s
                            chmod_and_chown_992_12682()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=12683):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12684) as should_copy_source_993_12684:  # ?
                    should_copy_source_993_12684()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=12685):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=12686) as copy_file_to_dir_994_12686:  # ?
                            copy_file_to_dir_994_12686()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12687) as chmod_and_chown_995_12687:  # 0m:0.000s
                            chmod_and_chown_995_12687()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=12688):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12689) as should_copy_source_996_12689:  # ?
                    should_copy_source_996_12689()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=12690):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=12691) as copy_file_to_dir_997_12691:  # ?
                            copy_file_to_dir_997_12691()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12692) as chmod_and_chown_998_12692:  # 0m:0.000s
                            chmod_and_chown_998_12692()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=12693):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12694) as should_copy_source_999_12694:  # ?
                    should_copy_source_999_12694()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=12695):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=12696) as copy_file_to_dir_1000_12696:  # ?
                            copy_file_to_dir_1000_12696()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12697) as chmod_and_chown_1001_12697:  # 0m:0.000s
                            chmod_and_chown_1001_12697()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=12698):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12699) as should_copy_source_1002_12699:  # ?
                    should_copy_source_1002_12699()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=12700):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=12701) as copy_file_to_dir_1003_12701:  # ?
                            copy_file_to_dir_1003_12701()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12702) as chmod_and_chown_1004_12702:  # 0m:0.000s
                            chmod_and_chown_1004_12702()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=12703):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12704) as should_copy_source_1005_12704:  # ?
                    should_copy_source_1005_12704()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=12705):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=12706) as copy_file_to_dir_1006_12706:  # ?
                            copy_file_to_dir_1006_12706()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12707) as chmod_and_chown_1007_12707:  # 0m:0.000s
                            chmod_and_chown_1007_12707()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=12708):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12709) as should_copy_source_1008_12709:  # ?
                    should_copy_source_1008_12709()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=12710):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=12711) as copy_file_to_dir_1009_12711:  # ?
                            copy_file_to_dir_1009_12711()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12712) as chmod_and_chown_1010_12712:  # 0m:0.000s
                            chmod_and_chown_1010_12712()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=12713):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12714) as should_copy_source_1011_12714:  # ?
                    should_copy_source_1011_12714()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=12715):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=12716) as copy_file_to_dir_1012_12716:  # ?
                            copy_file_to_dir_1012_12716()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12717) as chmod_and_chown_1013_12717:  # 0m:0.000s
                            chmod_and_chown_1013_12717()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=12718):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12719) as should_copy_source_1014_12719:  # ?
                    should_copy_source_1014_12719()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=12720):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=12721) as copy_file_to_dir_1015_12721:  # ?
                            copy_file_to_dir_1015_12721()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12722) as chmod_and_chown_1016_12722:  # 0m:0.000s
                            chmod_and_chown_1016_12722()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=12723):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12724) as should_copy_source_1017_12724:  # ?
                    should_copy_source_1017_12724()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=12725):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=12726) as copy_file_to_dir_1018_12726:  # ?
                            copy_file_to_dir_1018_12726()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12727) as chmod_and_chown_1019_12727:  # 0m:0.000s
                            chmod_and_chown_1019_12727()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=12728):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12729) as should_copy_source_1020_12729:  # ?
                    should_copy_source_1020_12729()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=12730):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=12731) as copy_file_to_dir_1021_12731:  # ?
                            copy_file_to_dir_1021_12731()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12732) as chmod_and_chown_1022_12732:  # 0m:0.000s
                            chmod_and_chown_1022_12732()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=12733):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12734) as should_copy_source_1023_12734:  # ?
                    should_copy_source_1023_12734()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=12735):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=12736) as copy_file_to_dir_1024_12736:  # ?
                            copy_file_to_dir_1024_12736()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12737) as chmod_and_chown_1025_12737:  # 0m:0.000s
                            chmod_and_chown_1025_12737()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=12738):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12739) as should_copy_source_1026_12739:  # ?
                    should_copy_source_1026_12739()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=12740):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=12741) as copy_file_to_dir_1027_12741:  # ?
                            copy_file_to_dir_1027_12741()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12742) as chmod_and_chown_1028_12742:  # 0m:0.000s
                            chmod_and_chown_1028_12742()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=12743):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12744) as should_copy_source_1029_12744:  # ?
                    should_copy_source_1029_12744()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=12745):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=12746) as copy_file_to_dir_1030_12746:  # ?
                            copy_file_to_dir_1030_12746()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12747) as chmod_and_chown_1031_12747:  # 0m:0.000s
                            chmod_and_chown_1031_12747()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=12748):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12749) as should_copy_source_1032_12749:  # ?
                    should_copy_source_1032_12749()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=12750):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=12751) as copy_file_to_dir_1033_12751:  # ?
                            copy_file_to_dir_1033_12751()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12752) as chmod_and_chown_1034_12752:  # 0m:0.000s
                            chmod_and_chown_1034_12752()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=12753):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12754) as should_copy_source_1035_12754:  # ?
                    should_copy_source_1035_12754()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=12755):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=12756) as copy_file_to_dir_1036_12756:  # ?
                            copy_file_to_dir_1036_12756()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12757) as chmod_and_chown_1037_12757:  # 0m:0.000s
                            chmod_and_chown_1037_12757()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=12758):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12759) as should_copy_source_1038_12759:  # ?
                    should_copy_source_1038_12759()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=12760):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=12761) as copy_file_to_dir_1039_12761:  # ?
                            copy_file_to_dir_1039_12761()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12762) as chmod_and_chown_1040_12762:  # 0m:0.000s
                            chmod_and_chown_1040_12762()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=12763):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12764) as should_copy_source_1041_12764:  # ?
                    should_copy_source_1041_12764()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=12765):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=12766) as copy_file_to_dir_1042_12766:  # ?
                            copy_file_to_dir_1042_12766()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12767) as chmod_and_chown_1043_12767:  # 0m:0.000s
                            chmod_and_chown_1043_12767()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=12768):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12769) as should_copy_source_1044_12769:  # ?
                    should_copy_source_1044_12769()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=12770):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=12771) as copy_file_to_dir_1045_12771:  # ?
                            copy_file_to_dir_1045_12771()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12772) as chmod_and_chown_1046_12772:  # 0m:0.000s
                            chmod_and_chown_1046_12772()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=12773):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12774) as should_copy_source_1047_12774:  # ?
                    should_copy_source_1047_12774()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=12775):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=12776) as copy_file_to_dir_1048_12776:  # ?
                            copy_file_to_dir_1048_12776()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12777) as chmod_and_chown_1049_12777:  # 0m:0.000s
                            chmod_and_chown_1049_12777()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=12778):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12779) as should_copy_source_1050_12779:  # ?
                    should_copy_source_1050_12779()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=12780):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=12781) as copy_file_to_dir_1051_12781:  # ?
                            copy_file_to_dir_1051_12781()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12782) as chmod_and_chown_1052_12782:  # 0m:0.000s
                            chmod_and_chown_1052_12782()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=12783):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12784) as should_copy_source_1053_12784:  # ?
                    should_copy_source_1053_12784()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=12785):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=12786) as copy_file_to_dir_1054_12786:  # ?
                            copy_file_to_dir_1054_12786()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12787) as chmod_and_chown_1055_12787:  # 0m:0.000s
                            chmod_and_chown_1055_12787()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=12788):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12789) as should_copy_source_1056_12789:  # ?
                    should_copy_source_1056_12789()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=12790):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=12791) as copy_file_to_dir_1057_12791:  # ?
                            copy_file_to_dir_1057_12791()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12792) as chmod_and_chown_1058_12792:  # 0m:0.000s
                            chmod_and_chown_1058_12792()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=12793):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12794) as should_copy_source_1059_12794:  # ?
                    should_copy_source_1059_12794()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=12795):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=12796) as copy_file_to_dir_1060_12796:  # ?
                            copy_file_to_dir_1060_12796()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12797) as chmod_and_chown_1061_12797:  # 0m:0.000s
                            chmod_and_chown_1061_12797()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=12798):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12799) as should_copy_source_1062_12799:  # ?
                    should_copy_source_1062_12799()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=12800):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=12801) as copy_file_to_dir_1063_12801:  # ?
                            copy_file_to_dir_1063_12801()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12802) as chmod_and_chown_1064_12802:  # 0m:0.000s
                            chmod_and_chown_1064_12802()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=12803):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12804) as should_copy_source_1065_12804:  # ?
                    should_copy_source_1065_12804()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=12805):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=12806) as copy_file_to_dir_1066_12806:  # ?
                            copy_file_to_dir_1066_12806()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12807) as chmod_and_chown_1067_12807:  # 0m:0.000s
                            chmod_and_chown_1067_12807()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=12808):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12809) as should_copy_source_1068_12809:  # ?
                    should_copy_source_1068_12809()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=12810):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=12811) as copy_file_to_dir_1069_12811:  # ?
                            copy_file_to_dir_1069_12811()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12812) as chmod_and_chown_1070_12812:  # 0m:0.000s
                            chmod_and_chown_1070_12812()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=12813):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12814) as should_copy_source_1071_12814:  # ?
                    should_copy_source_1071_12814()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=12815):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=12816) as copy_file_to_dir_1072_12816:  # ?
                            copy_file_to_dir_1072_12816()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12817) as chmod_and_chown_1073_12817:  # 0m:0.000s
                            chmod_and_chown_1073_12817()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=12818):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12819) as should_copy_source_1074_12819:  # ?
                    should_copy_source_1074_12819()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=12820):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=12821) as copy_file_to_dir_1075_12821:  # ?
                            copy_file_to_dir_1075_12821()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12822) as chmod_and_chown_1076_12822:  # 0m:0.000s
                            chmod_and_chown_1076_12822()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=12823):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12824) as should_copy_source_1077_12824:  # ?
                    should_copy_source_1077_12824()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=12825):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=12826) as copy_file_to_dir_1078_12826:  # ?
                            copy_file_to_dir_1078_12826()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12827) as chmod_and_chown_1079_12827:  # 0m:0.000s
                            chmod_and_chown_1079_12827()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=12828):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12829) as should_copy_source_1080_12829:  # ?
                    should_copy_source_1080_12829()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=12830):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=12831) as copy_file_to_dir_1081_12831:  # ?
                            copy_file_to_dir_1081_12831()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12832) as chmod_and_chown_1082_12832:  # 0m:0.000s
                            chmod_and_chown_1082_12832()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=12833):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12834) as should_copy_source_1083_12834:  # ?
                    should_copy_source_1083_12834()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=12835):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=12836) as copy_file_to_dir_1084_12836:  # ?
                            copy_file_to_dir_1084_12836()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12837) as chmod_and_chown_1085_12837:  # 0m:0.000s
                            chmod_and_chown_1085_12837()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=12838):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12839) as should_copy_source_1086_12839:  # ?
                    should_copy_source_1086_12839()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=12840):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=12841) as copy_file_to_dir_1087_12841:  # ?
                            copy_file_to_dir_1087_12841()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12842) as chmod_and_chown_1088_12842:  # 0m:0.000s
                            chmod_and_chown_1088_12842()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12843) as should_copy_source_1089_12843:  # ?
                    should_copy_source_1089_12843()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=12844):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=12845) as copy_file_to_dir_1090_12845:  # ?
                            copy_file_to_dir_1090_12845()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12846) as chmod_and_chown_1091_12846:  # 0m:0.000s
                            chmod_and_chown_1091_12846()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=12847):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12848) as should_copy_source_1092_12848:  # ?
                    should_copy_source_1092_12848()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=12849):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=12850) as copy_file_to_dir_1093_12850:  # ?
                            copy_file_to_dir_1093_12850()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12851) as chmod_and_chown_1094_12851:  # 0m:0.000s
                            chmod_and_chown_1094_12851()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=12852):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12853) as should_copy_source_1095_12853:  # ?
                    should_copy_source_1095_12853()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=12854):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=12855) as copy_file_to_dir_1096_12855:  # ?
                            copy_file_to_dir_1096_12855()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12856) as chmod_and_chown_1097_12856:  # 0m:0.000s
                            chmod_and_chown_1097_12856()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=12857):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12858) as should_copy_source_1098_12858:  # ?
                    should_copy_source_1098_12858()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=12859):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=12860) as copy_file_to_dir_1099_12860:  # ?
                            copy_file_to_dir_1099_12860()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12861) as chmod_and_chown_1100_12861:  # 0m:0.000s
                            chmod_and_chown_1100_12861()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=12862):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12863) as should_copy_source_1101_12863:  # ?
                    should_copy_source_1101_12863()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=12864):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=12865) as copy_file_to_dir_1102_12865:  # ?
                            copy_file_to_dir_1102_12865()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12866) as chmod_and_chown_1103_12866:  # 0m:0.000s
                            chmod_and_chown_1103_12866()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=12867):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12868) as should_copy_source_1104_12868:  # ?
                    should_copy_source_1104_12868()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=12869):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=12870) as copy_file_to_dir_1105_12870:  # ?
                            copy_file_to_dir_1105_12870()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12871) as chmod_and_chown_1106_12871:  # 0m:0.000s
                            chmod_and_chown_1106_12871()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=12872):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12873) as should_copy_source_1107_12873:  # ?
                    should_copy_source_1107_12873()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=12874):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=12875) as copy_file_to_dir_1108_12875:  # ?
                            copy_file_to_dir_1108_12875()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12876) as chmod_and_chown_1109_12876:  # 0m:0.000s
                            chmod_and_chown_1109_12876()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=12877):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12878) as should_copy_source_1110_12878:  # ?
                    should_copy_source_1110_12878()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=12879):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=12880) as copy_file_to_dir_1111_12880:  # ?
                            copy_file_to_dir_1111_12880()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12881) as chmod_and_chown_1112_12881:  # 0m:0.000s
                            chmod_and_chown_1112_12881()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=12882):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12883) as should_copy_source_1113_12883:  # ?
                    should_copy_source_1113_12883()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=12884):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=12885) as copy_file_to_dir_1114_12885:  # ?
                            copy_file_to_dir_1114_12885()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12886) as chmod_and_chown_1115_12886:  # 0m:0.000s
                            chmod_and_chown_1115_12886()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=12887):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12888) as should_copy_source_1116_12888:  # ?
                    should_copy_source_1116_12888()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=12889):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=12890) as copy_file_to_dir_1117_12890:  # ?
                            copy_file_to_dir_1117_12890()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12891) as chmod_and_chown_1118_12891:  # 0m:0.000s
                            chmod_and_chown_1118_12891()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=12892):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12893) as should_copy_source_1119_12893:  # ?
                    should_copy_source_1119_12893()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=12894):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=12895) as copy_file_to_dir_1120_12895:  # ?
                            copy_file_to_dir_1120_12895()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12896) as chmod_and_chown_1121_12896:  # 0m:0.000s
                            chmod_and_chown_1121_12896()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=12897):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12898) as should_copy_source_1122_12898:  # ?
                    should_copy_source_1122_12898()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=12899):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=12900) as copy_file_to_dir_1123_12900:  # ?
                            copy_file_to_dir_1123_12900()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12901) as chmod_and_chown_1124_12901:  # 0m:0.000s
                            chmod_and_chown_1124_12901()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=12902):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12903) as should_copy_source_1125_12903:  # ?
                    should_copy_source_1125_12903()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=12904):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=12905) as copy_file_to_dir_1126_12905:  # ?
                            copy_file_to_dir_1126_12905()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12906) as chmod_and_chown_1127_12906:  # 0m:0.000s
                            chmod_and_chown_1127_12906()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=12907):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12908) as should_copy_source_1128_12908:  # ?
                    should_copy_source_1128_12908()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=12909):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=12910) as copy_file_to_dir_1129_12910:  # ?
                            copy_file_to_dir_1129_12910()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12911) as chmod_and_chown_1130_12911:  # 0m:0.000s
                            chmod_and_chown_1130_12911()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=12912):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12913) as should_copy_source_1131_12913:  # ?
                    should_copy_source_1131_12913()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=12914):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=12915) as copy_file_to_dir_1132_12915:  # ?
                            copy_file_to_dir_1132_12915()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12916) as chmod_and_chown_1133_12916:  # 0m:0.000s
                            chmod_and_chown_1133_12916()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=12917):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12918) as should_copy_source_1134_12918:  # ?
                    should_copy_source_1134_12918()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=12919):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=12920) as copy_file_to_dir_1135_12920:  # ?
                            copy_file_to_dir_1135_12920()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12921) as chmod_and_chown_1136_12921:  # 0m:0.000s
                            chmod_and_chown_1136_12921()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=12922):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12923) as should_copy_source_1137_12923:  # ?
                    should_copy_source_1137_12923()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=12924):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=12925) as copy_file_to_dir_1138_12925:  # ?
                            copy_file_to_dir_1138_12925()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12926) as chmod_and_chown_1139_12926:  # 0m:0.000s
                            chmod_and_chown_1139_12926()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=12927):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12928) as should_copy_source_1140_12928:  # ?
                    should_copy_source_1140_12928()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=12929):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=12930) as copy_file_to_dir_1141_12930:  # ?
                            copy_file_to_dir_1141_12930()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12931) as chmod_and_chown_1142_12931:  # 0m:0.000s
                            chmod_and_chown_1142_12931()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=12932):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12933) as should_copy_source_1143_12933:  # ?
                    should_copy_source_1143_12933()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=12934):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=12935) as copy_file_to_dir_1144_12935:  # ?
                            copy_file_to_dir_1144_12935()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12936) as chmod_and_chown_1145_12936:  # 0m:0.000s
                            chmod_and_chown_1145_12936()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=12937):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12938) as should_copy_source_1146_12938:  # ?
                    should_copy_source_1146_12938()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=12939):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=12940) as copy_file_to_dir_1147_12940:  # ?
                            copy_file_to_dir_1147_12940()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12941) as chmod_and_chown_1148_12941:  # 0m:0.000s
                            chmod_and_chown_1148_12941()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=12942):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12943) as should_copy_source_1149_12943:  # ?
                    should_copy_source_1149_12943()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=12944):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=12945) as copy_file_to_dir_1150_12945:  # ?
                            copy_file_to_dir_1150_12945()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12946) as chmod_and_chown_1151_12946:  # 0m:0.000s
                            chmod_and_chown_1151_12946()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=12947):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12948) as should_copy_source_1152_12948:  # ?
                    should_copy_source_1152_12948()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=12949):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=12950) as copy_file_to_dir_1153_12950:  # ?
                            copy_file_to_dir_1153_12950()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12951) as chmod_and_chown_1154_12951:  # 0m:0.000s
                            chmod_and_chown_1154_12951()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=12952):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12953) as should_copy_source_1155_12953:  # ?
                    should_copy_source_1155_12953()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=12954):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=12955) as copy_file_to_dir_1156_12955:  # ?
                            copy_file_to_dir_1156_12955()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12956) as chmod_and_chown_1157_12956:  # 0m:0.000s
                            chmod_and_chown_1157_12956()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=12957):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12958) as should_copy_source_1158_12958:  # ?
                    should_copy_source_1158_12958()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=12959):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=12960) as copy_file_to_dir_1159_12960:  # ?
                            copy_file_to_dir_1159_12960()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12961) as chmod_and_chown_1160_12961:  # 0m:0.000s
                            chmod_and_chown_1160_12961()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=12962):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12963) as should_copy_source_1161_12963:  # ?
                    should_copy_source_1161_12963()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=12964):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=12965) as copy_file_to_dir_1162_12965:  # ?
                            copy_file_to_dir_1162_12965()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12966) as chmod_and_chown_1163_12966:  # 0m:0.000s
                            chmod_and_chown_1163_12966()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=12967):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12968) as should_copy_source_1164_12968:  # ?
                    should_copy_source_1164_12968()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=12969):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=12970) as copy_file_to_dir_1165_12970:  # ?
                            copy_file_to_dir_1165_12970()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12971) as chmod_and_chown_1166_12971:  # 0m:0.000s
                            chmod_and_chown_1166_12971()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=12972):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12973) as should_copy_source_1167_12973:  # ?
                    should_copy_source_1167_12973()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=12974):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=12975) as copy_file_to_dir_1168_12975:  # ?
                            copy_file_to_dir_1168_12975()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12976) as chmod_and_chown_1169_12976:  # 0m:0.000s
                            chmod_and_chown_1169_12976()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=12977):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12978) as should_copy_source_1170_12978:  # ?
                    should_copy_source_1170_12978()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=12979):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=12980) as copy_file_to_dir_1171_12980:  # ?
                            copy_file_to_dir_1171_12980()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12981) as chmod_and_chown_1172_12981:  # 0m:0.000s
                            chmod_and_chown_1172_12981()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=12982):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12983) as should_copy_source_1173_12983:  # ?
                    should_copy_source_1173_12983()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=12984):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=12985) as copy_file_to_dir_1174_12985:  # ?
                            copy_file_to_dir_1174_12985()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12986) as chmod_and_chown_1175_12986:  # 0m:0.000s
                            chmod_and_chown_1175_12986()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12987) as should_copy_source_1176_12987:  # ?
                    should_copy_source_1176_12987()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=12988):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=12989) as copy_file_to_dir_1177_12989:  # ?
                            copy_file_to_dir_1177_12989()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12990) as chmod_and_chown_1178_12990:  # 0m:0.000s
                            chmod_and_chown_1178_12990()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12991) as should_copy_source_1179_12991:  # ?
                    should_copy_source_1179_12991()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=12992):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=12993) as copy_file_to_dir_1180_12993:  # ?
                            copy_file_to_dir_1180_12993()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12994) as chmod_and_chown_1181_12994:  # 0m:0.000s
                            chmod_and_chown_1181_12994()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=12995):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12996) as should_copy_source_1182_12996:  # ?
                    should_copy_source_1182_12996()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=12997):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=12998) as copy_file_to_dir_1183_12998:  # ?
                            copy_file_to_dir_1183_12998()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12999) as chmod_and_chown_1184_12999:  # 0m:0.000s
                            chmod_and_chown_1184_12999()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=13000):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13001) as should_copy_source_1185_13001:  # ?
                    should_copy_source_1185_13001()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=13002):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=13003) as copy_file_to_dir_1186_13003:  # ?
                            copy_file_to_dir_1186_13003()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13004) as chmod_and_chown_1187_13004:  # 0m:0.000s
                            chmod_and_chown_1187_13004()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=13005):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13006) as should_copy_source_1188_13006:  # ?
                    should_copy_source_1188_13006()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=13007):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=13008) as copy_file_to_dir_1189_13008:  # ?
                            copy_file_to_dir_1189_13008()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13009) as chmod_and_chown_1190_13009:  # 0m:0.000s
                            chmod_and_chown_1190_13009()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=13010):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13011) as should_copy_source_1191_13011:  # ?
                    should_copy_source_1191_13011()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=13012):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=13013) as copy_file_to_dir_1192_13013:  # ?
                            copy_file_to_dir_1192_13013()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13014) as chmod_and_chown_1193_13014:  # 0m:0.000s
                            chmod_and_chown_1193_13014()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=13015):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13016) as should_copy_source_1194_13016:  # ?
                    should_copy_source_1194_13016()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=13017):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=13018) as copy_file_to_dir_1195_13018:  # ?
                            copy_file_to_dir_1195_13018()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13019) as chmod_and_chown_1196_13019:  # 0m:0.000s
                            chmod_and_chown_1196_13019()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=13020):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13021) as should_copy_source_1197_13021:  # ?
                    should_copy_source_1197_13021()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=13022):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=13023) as copy_file_to_dir_1198_13023:  # ?
                            copy_file_to_dir_1198_13023()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13024) as chmod_and_chown_1199_13024:  # 0m:0.000s
                            chmod_and_chown_1199_13024()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=13025):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13026) as should_copy_source_1200_13026:  # ?
                    should_copy_source_1200_13026()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=13027):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=13028) as copy_file_to_dir_1201_13028:  # ?
                            copy_file_to_dir_1201_13028()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13029) as chmod_and_chown_1202_13029:  # 0m:0.000s
                            chmod_and_chown_1202_13029()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=13030):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13031) as should_copy_source_1203_13031:  # ?
                    should_copy_source_1203_13031()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=13032):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=13033) as copy_file_to_dir_1204_13033:  # ?
                            copy_file_to_dir_1204_13033()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13034) as chmod_and_chown_1205_13034:  # 0m:0.000s
                            chmod_and_chown_1205_13034()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=13035) as resolve_config_vars_in_file_1206_13035:  # 0m:0.001s
                resolve_config_vars_in_file_1206_13035()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=13036) as if_1207_13036:  # 0m:0.001s
                if_1207_13036()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=13037) as resolve_config_vars_in_file_1208_13037:  # 0m:0.000s
                resolve_config_vars_in_file_1208_13037()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=13038) as if_1209_13038:  # 0m:0.000s
                if_1209_13038()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=13039) as resolve_config_vars_in_file_1210_13039:  # 0m:0.000s
                resolve_config_vars_in_file_1210_13039()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=13040) as if_1211_13040:  # 0m:0.000s
                if_1211_13040()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=13041) as resolve_config_vars_in_file_1212_13041:  # 0m:0.000s
                resolve_config_vars_in_file_1212_13041()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=13042) as if_1213_13042:  # 0m:0.000s
                if_1213_13042()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=13043) as resolve_config_vars_in_file_1214_13043:  # 0m:0.000s
                resolve_config_vars_in_file_1214_13043()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=13044) as if_1215_13044:  # 0m:0.000s
                if_1215_13044()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13045) as resolve_config_vars_in_file_1216_13045:  # 0m:0.000s
                resolve_config_vars_in_file_1216_13045()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=13046) as if_1217_13046:  # 0m:0.000s
                if_1217_13046()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=13047) as resolve_config_vars_in_file_1218_13047:  # 0m:0.000s
                resolve_config_vars_in_file_1218_13047()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=13048) as if_1219_13048:  # 0m:0.000s
                if_1219_13048()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=13049) as resolve_config_vars_in_file_1220_13049:  # 0m:0.000s
                resolve_config_vars_in_file_1220_13049()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=13050) as if_1221_13050:  # 0m:0.000s
                if_1221_13050()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=13051) as resolve_config_vars_in_file_1222_13051:  # 0m:0.000s
                resolve_config_vars_in_file_1222_13051()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=13052) as if_1223_13052:  # 0m:0.001s
                if_1223_13052()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=13053) as resolve_config_vars_in_file_1224_13053:  # 0m:0.000s
                resolve_config_vars_in_file_1224_13053()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=13054) as if_1225_13054:  # 0m:0.000s
                if_1225_13054()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=13055) as resolve_config_vars_in_file_1226_13055:  # 0m:0.000s
                resolve_config_vars_in_file_1226_13055()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=13056) as if_1227_13056:  # 0m:0.000s
                if_1227_13056()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=13057) as resolve_config_vars_in_file_1228_13057:  # 0m:0.001s
                resolve_config_vars_in_file_1228_13057()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=13058) as if_1229_13058:  # 0m:0.000s
                if_1229_13058()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=13059) as resolve_config_vars_in_file_1230_13059:  # 0m:0.001s
                resolve_config_vars_in_file_1230_13059()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=13060) as if_1231_13060:  # 0m:0.001s
                if_1231_13060()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=13061) as resolve_config_vars_in_file_1232_13061:  # 0m:0.000s
                resolve_config_vars_in_file_1232_13061()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=13062) as if_1233_13062:  # 0m:0.000s
                if_1233_13062()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=13063) as resolve_config_vars_in_file_1234_13063:  # 0m:0.000s
                resolve_config_vars_in_file_1234_13063()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=13064) as if_1235_13064:  # 0m:0.000s
                if_1235_13064()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=13065) as resolve_config_vars_in_file_1236_13065:  # 0m:0.000s
                resolve_config_vars_in_file_1236_13065()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=13066) as if_1237_13066:  # 0m:0.000s
                if_1237_13066()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13067) as resolve_config_vars_in_file_1238_13067:  # 0m:0.000s
                resolve_config_vars_in_file_1238_13067()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=13068) as if_1239_13068:  # 0m:0.000s
                if_1239_13068()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13069) as resolve_config_vars_in_file_1240_13069:  # 0m:0.000s
                resolve_config_vars_in_file_1240_13069()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=13070) as if_1241_13070:  # 0m:0.000s
                if_1241_13070()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13071) as resolve_config_vars_in_file_1242_13071:  # 0m:0.000s
                resolve_config_vars_in_file_1242_13071()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=13072) as if_1243_13072:  # 0m:0.000s
                if_1243_13072()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=13073) as resolve_config_vars_in_file_1244_13073:  # 0m:0.000s
                resolve_config_vars_in_file_1244_13073()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=13074) as if_1245_13074:  # 0m:0.000s
                if_1245_13074()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=13075) as resolve_config_vars_in_file_1246_13075:  # 0m:0.000s
                resolve_config_vars_in_file_1246_13075()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=13076) as if_1247_13076:  # 0m:0.000s
                if_1247_13076()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=13077) as resolve_config_vars_in_file_1248_13077:  # 0m:0.000s
                resolve_config_vars_in_file_1248_13077()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=13078) as if_1249_13078:  # 0m:0.000s
                if_1249_13078()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=13079) as resolve_config_vars_in_file_1250_13079:  # 0m:0.000s
                resolve_config_vars_in_file_1250_13079()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=13080) as if_1251_13080:  # 0m:0.000s
                if_1251_13080()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13081) as resolve_config_vars_in_file_1252_13081:  # 0m:0.000s
                resolve_config_vars_in_file_1252_13081()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=13082) as if_1253_13082:  # 0m:0.000s
                if_1253_13082()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=13083) as rm_file_or_dir_1254_13083:  # 0m:0.000s
                rm_file_or_dir_1254_13083()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=13084) as resolve_config_vars_in_file_1255_13084:  # 0m:0.000s
                resolve_config_vars_in_file_1255_13084()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=13085) as if_1256_13085:  # 0m:0.001s
                if_1256_13085()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=13086) as rm_file_or_dir_1257_13086:  # 0m:0.000s
                rm_file_or_dir_1257_13086()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=13087) as resolve_config_vars_in_file_1258_13087:  # 0m:0.000s
                resolve_config_vars_in_file_1258_13087()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=13088) as if_1259_13088:  # 0m:0.000s
                if_1259_13088()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=13089) as resolve_config_vars_in_file_1260_13089:  # 0m:0.000s
                resolve_config_vars_in_file_1260_13089()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=13090) as if_1261_13090:  # 0m:0.000s
                if_1261_13090()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=13091) as resolve_config_vars_in_file_1262_13091:  # 0m:0.000s
                resolve_config_vars_in_file_1262_13091()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=13092) as if_1263_13092:  # 0m:0.000s
                if_1263_13092()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=13093) as resolve_config_vars_in_file_1264_13093:  # 0m:0.001s
                resolve_config_vars_in_file_1264_13093()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=13094) as if_1265_13094:  # 0m:0.000s
                if_1265_13094()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=13095) as resolve_config_vars_in_file_1266_13095:  # 0m:0.000s
                resolve_config_vars_in_file_1266_13095()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=13096) as if_1267_13096:  # 0m:0.000s
                if_1267_13096()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=13097) as resolve_config_vars_in_file_1268_13097:  # 0m:0.000s
                resolve_config_vars_in_file_1268_13097()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=13098) as if_1269_13098:  # 0m:0.000s
                if_1269_13098()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13099) as resolve_config_vars_in_file_1270_13099:  # 0m:0.000s
                resolve_config_vars_in_file_1270_13099()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=13100) as if_1271_13100:  # 0m:0.001s
                if_1271_13100()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13101) as resolve_config_vars_in_file_1272_13101:  # 0m:0.000s
                resolve_config_vars_in_file_1272_13101()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=13102) as if_1273_13102:  # 0m:0.000s
                if_1273_13102()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=13103) as resolve_config_vars_in_file_1274_13103:  # 0m:0.000s
                resolve_config_vars_in_file_1274_13103()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=13104) as if_1275_13104:  # 0m:0.000s
                if_1275_13104()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=13105) as resolve_config_vars_in_file_1276_13105:  # 0m:0.000s
                resolve_config_vars_in_file_1276_13105()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=13106) as if_1277_13106:  # 0m:0.000s
                if_1277_13106()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=13107) as resolve_config_vars_in_file_1278_13107:  # 0m:0.000s
                resolve_config_vars_in_file_1278_13107()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=13108) as if_1279_13108:  # 0m:0.000s
                if_1279_13108()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13109) as resolve_config_vars_in_file_1280_13109:  # 0m:0.000s
                resolve_config_vars_in_file_1280_13109()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=13110) as if_1281_13110:  # 0m:0.000s
                if_1281_13110()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=13111) as resolve_config_vars_in_file_1282_13111:  # 0m:0.000s
                resolve_config_vars_in_file_1282_13111()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=13112) as if_1283_13112:  # 0m:0.000s
                if_1283_13112()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=13113) as resolve_config_vars_in_file_1284_13113:  # 0m:0.000s
                resolve_config_vars_in_file_1284_13113()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=13114) as if_1285_13114:  # 0m:0.000s
                if_1285_13114()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=13115) as resolve_config_vars_in_file_1286_13115:  # 0m:0.000s
                resolve_config_vars_in_file_1286_13115()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=13116) as if_1287_13116:  # 0m:0.000s
                if_1287_13116()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=13117) as resolve_config_vars_in_file_1288_13117:  # 0m:0.000s
                resolve_config_vars_in_file_1288_13117()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=13118) as if_1289_13118:  # 0m:0.000s
                if_1289_13118()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=13119) as resolve_config_vars_in_file_1290_13119:  # 0m:0.000s
                resolve_config_vars_in_file_1290_13119()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=13120) as if_1291_13120:  # 0m:0.000s
                if_1291_13120()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=13121) as resolve_config_vars_in_file_1292_13121:  # 0m:0.000s
                resolve_config_vars_in_file_1292_13121()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=13122) as if_1293_13122:  # 0m:0.000s
                if_1293_13122()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=13123) as resolve_config_vars_in_file_1294_13123:  # 0m:0.000s
                resolve_config_vars_in_file_1294_13123()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=13124) as if_1295_13124:  # 0m:0.000s
                if_1295_13124()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=13125) as resolve_config_vars_in_file_1296_13125:  # 0m:0.000s
                resolve_config_vars_in_file_1296_13125()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=13126) as if_1297_13126:  # 0m:0.000s
                if_1297_13126()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=13127) as resolve_config_vars_in_file_1298_13127:  # 0m:0.000s
                resolve_config_vars_in_file_1298_13127()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=13128) as if_1299_13128:  # 0m:0.000s
                if_1299_13128()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=13129) as resolve_config_vars_in_file_1300_13129:  # 0m:0.000s
                resolve_config_vars_in_file_1300_13129()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=13130) as if_1301_13130:  # 0m:0.000s
                if_1301_13130()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=13131) as resolve_config_vars_in_file_1302_13131:  # 0m:0.001s
                resolve_config_vars_in_file_1302_13131()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=13132) as if_1303_13132:  # 0m:0.000s
                if_1303_13132()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=13133) as move_file_to_file_1304_13133:  # 0m:0.011s
                move_file_to_file_1304_13133()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=13134) as resolve_config_vars_in_file_1305_13134:  # 0m:0.001s
                resolve_config_vars_in_file_1305_13134()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=13135) as if_1306_13135:  # 0m:0.001s
                if_1306_13135()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=13136) as resolve_config_vars_in_file_1307_13136:  # 0m:0.000s
                resolve_config_vars_in_file_1307_13136()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=13137) as if_1308_13137:  # 0m:0.000s
                if_1308_13137()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=13138) as resolve_config_vars_in_file_1309_13138:  # 0m:0.000s
                resolve_config_vars_in_file_1309_13138()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=13139) as if_1310_13139:  # 0m:0.000s
                if_1310_13139()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=13140) as resolve_config_vars_in_file_1311_13140:  # 0m:0.000s
                resolve_config_vars_in_file_1311_13140()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=13141) as if_1312_13141:  # 0m:0.000s
                if_1312_13141()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=13142) as resolve_config_vars_in_file_1313_13142:  # 0m:0.000s
                resolve_config_vars_in_file_1313_13142()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=13143) as if_1314_13143:  # 0m:0.000s
                if_1314_13143()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13144) as resolve_config_vars_in_file_1315_13144:  # 0m:0.000s
                resolve_config_vars_in_file_1315_13144()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=13145) as if_1316_13145:  # 0m:0.000s
                if_1316_13145()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=13146) as resolve_config_vars_in_file_1317_13146:  # 0m:0.000s
                resolve_config_vars_in_file_1317_13146()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=13147) as if_1318_13147:  # 0m:0.000s
                if_1318_13147()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=13148) as resolve_config_vars_in_file_1319_13148:  # 0m:0.000s
                resolve_config_vars_in_file_1319_13148()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=13149) as if_1320_13149:  # 0m:0.000s
                if_1320_13149()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=13150) as resolve_config_vars_in_file_1321_13150:  # 0m:0.000s
                resolve_config_vars_in_file_1321_13150()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=13151) as if_1322_13151:  # 0m:0.000s
                if_1322_13151()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=13152) as resolve_config_vars_in_file_1323_13152:  # 0m:0.000s
                resolve_config_vars_in_file_1323_13152()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=13153) as if_1324_13153:  # 0m:0.000s
                if_1324_13153()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=13154) as resolve_config_vars_in_file_1325_13154:  # 0m:0.000s
                resolve_config_vars_in_file_1325_13154()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=13155) as if_1326_13155:  # 0m:0.000s
                if_1326_13155()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=13156) as resolve_config_vars_in_file_1327_13156:  # 0m:0.000s
                resolve_config_vars_in_file_1327_13156()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=13157) as if_1328_13157:  # 0m:0.000s
                if_1328_13157()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13158) as resolve_config_vars_in_file_1329_13158:  # 0m:0.000s
                resolve_config_vars_in_file_1329_13158()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=13159) as if_1330_13159:  # 0m:0.000s
                if_1330_13159()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=13160) as resolve_config_vars_in_file_1331_13160:  # 0m:0.000s
                resolve_config_vars_in_file_1331_13160()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=13161) as if_1332_13161:  # 0m:0.000s
                if_1332_13161()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=13162) as resolve_config_vars_in_file_1333_13162:  # 0m:0.000s
                resolve_config_vars_in_file_1333_13162()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=13163) as if_1334_13163:  # 0m:0.000s
                if_1334_13163()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=13164) as resolve_config_vars_in_file_1335_13164:  # 0m:0.000s
                resolve_config_vars_in_file_1335_13164()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=13165) as if_1336_13165:  # 0m:0.000s
                if_1336_13165()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=13166) as resolve_config_vars_in_file_1337_13166:  # 0m:0.000s
                resolve_config_vars_in_file_1337_13166()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=13167) as if_1338_13167:  # 0m:0.000s
                if_1338_13167()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=13168) as resolve_config_vars_in_file_1339_13168:  # 0m:0.000s
                resolve_config_vars_in_file_1339_13168()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=13169) as if_1340_13169:  # 0m:0.000s
                if_1340_13169()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=13170) as resolve_config_vars_in_file_1341_13170:  # 0m:0.000s
                resolve_config_vars_in_file_1341_13170()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=13171) as if_1342_13171:  # 0m:0.000s
                if_1342_13171()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=13172) as resolve_config_vars_in_file_1343_13172:  # 0m:0.000s
                resolve_config_vars_in_file_1343_13172()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=13173) as if_1344_13173:  # 0m:0.000s
                if_1344_13173()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=13174) as resolve_config_vars_in_file_1345_13174:  # 0m:0.000s
                resolve_config_vars_in_file_1345_13174()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=13175) as if_1346_13175:  # 0m:0.000s
                if_1346_13175()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=13176) as resolve_config_vars_in_file_1347_13176:  # 0m:0.000s
                resolve_config_vars_in_file_1347_13176()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=13177) as if_1348_13177:  # 0m:0.000s
                if_1348_13177()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13178) as resolve_config_vars_in_file_1349_13178:  # 0m:0.000s
                resolve_config_vars_in_file_1349_13178()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=13179) as if_1350_13179:  # 0m:0.000s
                if_1350_13179()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13180) as resolve_config_vars_in_file_1351_13180:  # 0m:0.000s
                resolve_config_vars_in_file_1351_13180()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=13181) as if_1352_13181:  # 0m:0.000s
                if_1352_13181()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=13182) as resolve_config_vars_in_file_1353_13182:  # 0m:0.000s
                resolve_config_vars_in_file_1353_13182()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=13183) as if_1354_13183:  # 0m:0.000s
                if_1354_13183()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13184) as resolve_config_vars_in_file_1355_13184:  # 0m:0.000s
                resolve_config_vars_in_file_1355_13184()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=13185) as if_1356_13185:  # 0m:0.000s
                if_1356_13185()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=13186) as resolve_config_vars_in_file_1357_13186:  # 0m:0.000s
                resolve_config_vars_in_file_1357_13186()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=13187) as if_1358_13187:  # 0m:0.000s
                if_1358_13187()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13188) as resolve_config_vars_in_file_1359_13188:  # 0m:0.000s
                resolve_config_vars_in_file_1359_13188()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=13189) as if_1360_13189:  # 0m:0.000s
                if_1360_13189()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=13190) as rm_file_or_dir_1361_13190:  # 0m:0.000s
                rm_file_or_dir_1361_13190()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=13191) as rm_file_or_dir_1362_13191:  # 0m:0.000s
                rm_file_or_dir_1362_13191()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=13192) as rm_file_or_dir_1363_13192:  # 0m:0.000s
                rm_file_or_dir_1363_13192()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13193) as resolve_config_vars_in_file_1364_13193:  # 0m:0.000s
                resolve_config_vars_in_file_1364_13193()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=13194) as if_1365_13194:  # 0m:0.000s
                if_1365_13194()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13195) as resolve_config_vars_in_file_1366_13195:  # 0m:0.000s
                resolve_config_vars_in_file_1366_13195()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=13196) as if_1367_13196:  # 0m:0.000s
                if_1367_13196()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=13197) as resolve_config_vars_in_file_1368_13197:  # 0m:0.000s
                resolve_config_vars_in_file_1368_13197()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=13198) as if_1369_13198:  # 0m:0.000s
                if_1369_13198()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=13199) as rm_file_or_dir_1370_13199:  # 0m:0.000s
                rm_file_or_dir_1370_13199()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=13200) as rm_file_or_dir_1371_13200:  # 0m:0.000s
                rm_file_or_dir_1371_13200()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=13201) as rm_file_or_dir_1372_13201:  # 0m:0.000s
                rm_file_or_dir_1372_13201()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=13202) as resolve_config_vars_in_file_1373_13202:  # 0m:0.000s
                resolve_config_vars_in_file_1373_13202()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=13203) as if_1374_13203:  # 0m:0.000s
                if_1374_13203()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=13204) as resolve_config_vars_in_file_1375_13204:  # 0m:0.000s
                resolve_config_vars_in_file_1375_13204()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=13205) as if_1376_13205:  # 0m:0.000s
                if_1376_13205()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13206) as resolve_config_vars_in_file_1377_13206:  # 0m:0.000s
                resolve_config_vars_in_file_1377_13206()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=13207) as if_1378_13207:  # 0m:0.000s
                if_1378_13207()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=13208) as resolve_config_vars_in_file_1379_13208:  # 0m:0.000s
                resolve_config_vars_in_file_1379_13208()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=13209) as if_1380_13209:  # 0m:0.000s
                if_1380_13209()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13210) as resolve_config_vars_in_file_1381_13210:  # 0m:0.000s
                resolve_config_vars_in_file_1381_13210()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=13211) as if_1382_13211:  # 0m:0.000s
                if_1382_13211()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=13212) as resolve_config_vars_in_file_1383_13212:  # 0m:0.000s
                resolve_config_vars_in_file_1383_13212()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=13213) as if_1384_13213:  # 0m:0.000s
                if_1384_13213()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=13214) as resolve_config_vars_in_file_1385_13214:  # 0m:0.000s
                resolve_config_vars_in_file_1385_13214()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=13215) as if_1386_13215:  # 0m:0.000s
                if_1386_13215()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=13216) as resolve_config_vars_in_file_1387_13216:  # 0m:0.000s
                resolve_config_vars_in_file_1387_13216()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=13217) as if_1388_13217:  # 0m:0.000s
                if_1388_13217()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=13218) as cd_stage_1389_13218:  # 0m:0.181s
            cd_stage_1389_13218()
            with Stage(r"copy", r"WavesReWireDevice v13.0.0.129", prog_num=13219):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13220) as should_copy_source_1390_13220:  # 0m:0.055s
                    should_copy_source_1390_13220()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=13221):  # 0m:0.055s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=13222) as copy_dir_to_dir_1391_13222:  # 0m:0.022s
                            copy_dir_to_dir_1391_13222()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=13223) as unwtar_1392_13223:  # 0m:0.032s
                            unwtar_1392_13223()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=13224, recursive=True) as chown_1393_13224:  # 0m:0.000s
                            chown_1393_13224()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13225) as should_copy_source_1394_13225:  # 0m:0.060s
                    should_copy_source_1394_13225()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=13226):  # 0m:0.060s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=13227) as copy_dir_to_dir_1395_13227:  # 0m:0.018s
                            copy_dir_to_dir_1395_13227()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=13228) as unwtar_1396_13228:  # 0m:0.041s
                            unwtar_1396_13228()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=13229, recursive=True) as chown_1397_13229:  # 0m:0.000s
                            chown_1397_13229()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13230) as shell_command_1398_13230:  # 0m:0.064s
                shell_command_1398_13230()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=13231) as cd_stage_1399_13231:  # 0m:0.211s
            cd_stage_1399_13231()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=13232):  # 0m:0.021s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=13233) as should_copy_source_1400_13233:  # 0m:0.021s
                    should_copy_source_1400_13233()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=13234):  # 0m:0.020s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=13235) as copy_dir_to_dir_1401_13235:  # 0m:0.020s
                            copy_dir_to_dir_1401_13235()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=13236, recursive=True) as chown_1402_13236:  # 0m:0.000s
                            chown_1402_13236()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=13237):  # 0m:0.189s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=13238) as should_copy_source_1403_13238:  # 0m:0.189s
                    should_copy_source_1403_13238()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=13239):  # 0m:0.189s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=13240) as copy_dir_to_dir_1404_13240:  # 0m:0.144s
                            copy_dir_to_dir_1404_13240()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=13241) as unwtar_1405_13241:  # 0m:0.044s
                            unwtar_1405_13241()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=13242, recursive=True) as chown_1406_13242:  # 0m:0.000s
                            chown_1406_13242()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=13243) as cd_stage_1407_13243:  # 0m:0.106s
            cd_stage_1407_13243()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=13244):  # 0m:0.105s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=13245) as should_copy_source_1408_13245:  # 0m:0.105s
                    should_copy_source_1408_13245()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=13246):  # 0m:0.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=13247) as copy_dir_to_dir_1409_13247:  # 0m:0.033s
                            copy_dir_to_dir_1409_13247()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=13248) as unwtar_1410_13248:  # 0m:0.071s
                            unwtar_1410_13248()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=13249, recursive=True) as chown_1411_13249:  # 0m:0.000s
                            chown_1411_13249()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=13250) as cd_stage_1412_13250:  # 0m:0.021s
            cd_stage_1412_13250()
            with Stage(r"copy", r"Demo Mode V15 1.1 v1.1", prog_num=13251):  # 0m:0.021s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=13252) as should_copy_source_1413_13252:  # 0m:0.021s
                    should_copy_source_1413_13252()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=13253):  # 0m:0.020s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=13254) as copy_dir_to_dir_1414_13254:  # 0m:0.020s
                            copy_dir_to_dir_1414_13254()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=13255, recursive=True) as chown_1415_13255:  # 0m:0.000s
                            chown_1415_13255()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=13256) as cd_stage_1416_13256:  # 0m:0.010s
            cd_stage_1416_13256()
            with Stage(r"copy", r"License Notifications V15 1.1 v1.1", prog_num=13257):  # 0m:0.010s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=13258) as should_copy_source_1417_13258:  # 0m:0.010s
                    should_copy_source_1417_13258()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=13259):  # 0m:0.009s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=13260) as copy_dir_to_dir_1418_13260:  # 0m:0.009s
                            copy_dir_to_dir_1418_13260()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=13261, recursive=True) as chown_1419_13261:  # 0m:0.000s
                            chown_1419_13261()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=13262) as cd_stage_1420_13262:  # 0m:6.487s
            cd_stage_1420_13262()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=13263) as rm_file_or_dir_1421_13263:  # 0m:0.000s
                rm_file_or_dir_1421_13263()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=13264):  # 0m:0.046s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=13265) as should_copy_source_1422_13265:  # 0m:0.046s
                    should_copy_source_1422_13265()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=13266):  # 0m:0.045s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13267) as copy_dir_to_dir_1423_13267:  # 0m:0.028s
                            copy_dir_to_dir_1423_13267()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=13268) as unwtar_1424_13268:  # 0m:0.017s
                            unwtar_1424_13268()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=13269, recursive=True) as chown_1425_13269:  # 0m:0.000s
                            chown_1425_13269()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=13270):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=13271) as should_copy_source_1426_13271:  # 0m:0.004s
                    should_copy_source_1426_13271()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=13272):  # 0m:0.004s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=13273) as unwtar_1427_13273:  # 0m:0.004s
                            unwtar_1427_13273()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=13274):  # 0m:3.366s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13275) as should_copy_source_1428_13275:  # 0m:3.366s
                    should_copy_source_1428_13275()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=13276):  # 0m:3.366s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=13277) as copy_dir_to_dir_1429_13277:  # 0m:0.013s
                            copy_dir_to_dir_1429_13277()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=13278) as unwtar_1430_13278:  # 0m:3.352s
                            unwtar_1430_13278()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=13279, recursive=True) as chown_1431_13279:  # 0m:0.000s
                            chown_1431_13279()
            with Stage(r"copy", r"OpenVino_2021.4.689 v2021.4.689", prog_num=13280):  # 0m:2.946s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13281) as should_copy_source_1432_13281:  # 0m:2.946s
                    should_copy_source_1432_13281()
                    with Stage(r"copy source", r"Mac/Modules/openvino", prog_num=13282):  # 0m:2.946s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r".", delete_extraneous_files=True, prog_num=13283) as copy_dir_to_dir_1433_13283:  # 0m:0.220s
                            copy_dir_to_dir_1433_13283()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", where_to_unwtar=r".", prog_num=13284) as unwtar_1434_13284:  # 0m:2.725s
                            unwtar_1434_13284()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/openvino", user_id=-1, group_id=-1, prog_num=13285, recursive=True) as chown_1435_13285:  # 0m:0.000s
                            chown_1435_13285()
            with Stage(r"copy", r"remove old WavesLib and shells", prog_num=13286):  # 0m:0.056s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Utilities", r"/Library/Application Support/Waves/Modules", skip_progress_count=6, prog_num=13287) as should_copy_source_1436_13287:  # 0m:0.056s
                    should_copy_source_1436_13287()
                    with Stage(r"copy source", r"Common/Utilities", prog_num=13288):  # 0m:0.056s
                        with CopyDirContentsToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Utilities", r".", prog_num=13289) as copy_dir_contents_to_dir_1437_13289:  # 0m:0.022s
                            copy_dir_contents_to_dir_1437_13289()
                        with ChmodAndChown(path=r"V9", mode="a+rw", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=13290, recursive=True) as chmod_and_chown_1438_13290:  # 0m:0.008s
                            chmod_and_chown_1438_13290()
                        with ChmodAndChown(path=r"remove_leftovers.py", mode="a+rw", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=13291, recursive=True) as chmod_and_chown_1439_13291:  # 0m:0.008s
                            chmod_and_chown_1439_13291()
                        with ChmodAndChown(path=r"remove_leftovers_V10.py", mode="a+rw", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=13292, recursive=True) as chmod_and_chown_1440_13292:  # 0m:0.009s
                            chmod_and_chown_1440_13292()
                        with ChmodAndChown(path=r"V9/remove_leftovers.py", mode="a+rw", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=13293, recursive=True) as chmod_and_chown_1441_13293:  # 0m:0.008s
                            chmod_and_chown_1441_13293()
            with Stage(r"copy", r"WavesLicenseEngine v2.6.0.2", prog_num=13294):  # 0m:0.053s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=13295) as should_copy_source_1442_13295:  # 0m:0.053s
                    should_copy_source_1442_13295()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=13296):  # 0m:0.053s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13297) as copy_dir_to_dir_1443_13297:  # 0m:0.052s
                            copy_dir_to_dir_1443_13297()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=13298) as chmod_1444_13298:  # 0m:0.000s
                            chmod_1444_13298()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=13299) as chmod_1445_13299:  # 0m:0.000s
                            chmod_1445_13299()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=13300, recursive=True) as chown_1446_13300:  # 0m:0.000s
                            chown_1446_13300()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=13303) as resolve_symlink_files_in_folder_1447_13303:  # 0m:0.003s
                resolve_symlink_files_in_folder_1447_13303()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13304) as shell_command_1448_13304:  # 0m:0.012s
                shell_command_1448_13304()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=13305) as cd_stage_1449_13305:  # 0m:0.062s
            cd_stage_1449_13305()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=13306):  # 0m:0.062s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=13307) as should_copy_source_1450_13307:  # 0m:0.062s
                    should_copy_source_1450_13307()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=13308):  # 0m:0.061s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=13309) as copy_dir_to_dir_1451_13309:  # 0m:0.061s
                            copy_dir_to_dir_1451_13309()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=13310, recursive=True) as chown_1452_13310:  # 0m:0.000s
                            chown_1452_13310()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=13311) as cd_stage_1453_13311:  # 0m:1.369s
            cd_stage_1453_13311()
            with Stage(r"copy", r"Waves Local Server v12.15.303.199", prog_num=13312):  # 0m:1.369s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=5, prog_num=13313) as should_copy_source_1454_13313:  # 0m:1.369s
                    should_copy_source_1454_13313()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=13314):  # 0m:1.369s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13315) as copy_dir_to_dir_1455_13315:  # 0m:0.045s
                            copy_dir_to_dir_1455_13315()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=13316) as unwtar_1456_13316:  # 0m:1.322s
                            unwtar_1456_13316()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=13317, recursive=True) as chown_1457_13317:  # 0m:0.000s
                            chown_1457_13317()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13318) as if_1458_13318:  # 0m:0.001s
                            if_1458_13318()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=13319) as cd_stage_1459_13319:  # 0m:6.045s
            cd_stage_1459_13319()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.77.78", prog_num=13320):  # 0m:6.045s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=13321) as should_copy_source_1460_13321:  # 0m:6.045s
                    should_copy_source_1460_13321()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=13322):  # 0m:6.045s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13323) as copy_dir_to_dir_1461_13323:  # 0m:0.118s
                            copy_dir_to_dir_1461_13323()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=13324) as unwtar_1462_13324:  # 0m:5.925s
                            unwtar_1462_13324()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=13325, recursive=True) as chown_1463_13325:  # 0m:0.000s
                            chown_1463_13325()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_10-20250120135643-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13326) as if_1464_13326:  # 0m:0.001s
                            if_1464_13326()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=13327) as cd_stage_1465_13327:  # 0m:0.830s
            cd_stage_1465_13327()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=13328):  # 0m:0.829s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13329) as should_copy_source_1466_13329:  # 0m:0.829s
                    should_copy_source_1466_13329()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=13330):  # 0m:0.829s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=13331) as copy_dir_to_dir_1467_13331:  # 0m:0.048s
                            copy_dir_to_dir_1467_13331()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=13332) as unwtar_1468_13332:  # 0m:0.699s
                            unwtar_1468_13332()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13333, recursive=True) as chown_1469_13333:  # 0m:0.000s
                            chown_1469_13333()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=13334) as break_hard_link_1470_13334:  # 0m:0.019s
                            break_hard_link_1470_13334()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=13335) as shell_command_1471_13335:  # 0m:0.052s
                            shell_command_1471_13335()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13336, recursive=True) as chown_1472_13336:  # 0m:0.000s
                            chown_1472_13336()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=13337, recursive=True) as chmod_1473_13337:  # 0m:0.010s
                            chmod_1473_13337()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=13338) as cd_stage_1474_13338:  # 0m:0.815s
            cd_stage_1474_13338()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=13339):  # 0m:0.815s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13340) as should_copy_source_1475_13340:  # 0m:0.814s
                    should_copy_source_1475_13340()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=13341):  # 0m:0.814s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=13342) as copy_dir_to_dir_1476_13342:  # 0m:0.020s
                            copy_dir_to_dir_1476_13342()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=13343) as unwtar_1477_13343:  # 0m:0.735s
                            unwtar_1477_13343()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=13344, recursive=True) as chown_1478_13344:  # 0m:0.000s
                            chown_1478_13344()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=13345) as shell_command_1479_13345:  # 0m:0.058s
                            shell_command_1479_13345()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13346) as cd_stage_1480_13346:  # 0m:0.413s
            cd_stage_1480_13346()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=13347):  # 0m:0.411s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13348) as should_copy_source_1481_13348:  # 0m:0.411s
                    should_copy_source_1481_13348()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=13349):  # 0m:0.410s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=13350) as copy_dir_to_dir_1482_13350:  # 0m:0.026s
                            copy_dir_to_dir_1482_13350()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=13351) as unwtar_1483_13351:  # 0m:0.198s
                            unwtar_1483_13351()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=13352, recursive=True) as chown_1484_13352:  # 0m:0.000s
                            chown_1484_13352()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13353) as shell_command_1485_13353:  # 0m:0.114s
                            shell_command_1485_13353()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13354) as script_command_1486_13354:  # 0m:0.013s
                            script_command_1486_13354()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13355) as shell_command_1487_13355:  # 0m:0.058s
                            shell_command_1487_13355()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13356) as create_symlink_1488_13356:  # 0m:0.001s
                create_symlink_1488_13356()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13357) as create_symlink_1489_13357:  # 0m:0.000s
                create_symlink_1489_13357()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=13358) as cd_stage_1490_13358:  # 0m:0.000s
            cd_stage_1490_13358()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=13359) as rm_file_or_dir_1491_13359:  # 0m:0.000s
                rm_file_or_dir_1491_13359()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", prog_num=13360) as cd_stage_1492_13360:  # 0m:2.323s
            cd_stage_1492_13360()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", no_artifacts=True, prog_num=13361) as un_zip_1493_13361:  # 0m:2.322s
                un_zip_1493_13361()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Waves Audio Factory Pack", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", prog_num=13362) as create_symlink_1494_13362:  # 0m:0.001s
                create_symlink_1494_13362()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=13363) as cd_stage_1495_13363:  # 0m:0.000s
            cd_stage_1495_13363()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=13364) as rm_file_or_dir_1496_13364:  # 0m:0.000s
                rm_file_or_dir_1496_13364()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=13365) as rm_file_or_dir_1497_13365:  # 0m:0.000s
                rm_file_or_dir_1497_13365()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=13366) as rm_file_or_dir_1498_13366:  # 0m:0.000s
                rm_file_or_dir_1498_13366()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=13367) as shell_command_1499_13367:  # 0m:0.013s
            shell_command_1499_13367()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=13368) as shell_command_1500_13368:  # 0m:0.123s
            shell_command_1500_13368()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=13369) as script_command_1501_13369:  # 0m:0.012s
            script_command_1501_13369()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=13370) as rm_file_or_dir_1502_13370:  # 0m:0.000s
            rm_file_or_dir_1502_13370()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13371) as move_dir_to_dir_1503_13371:  # 0m:0.000s
            move_dir_to_dir_1503_13371()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13372) as move_dir_to_dir_1504_13372:  # 0m:0.000s
            move_dir_to_dir_1504_13372()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13373) as move_dir_to_dir_1505_13373:  # 0m:0.000s
            move_dir_to_dir_1505_13373()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13374) as move_dir_to_dir_1506_13374:  # 0m:0.000s
            move_dir_to_dir_1506_13374()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=13375) as make_dirs_1507_13375:  # 0m:0.009s
            make_dirs_1507_13375()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13376) as move_dir_to_dir_1508_13376:  # 0m:0.000s
            move_dir_to_dir_1508_13376()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13377) as move_dir_to_dir_1509_13377:  # 0m:0.000s
            move_dir_to_dir_1509_13377()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=13378) as shell_command_1510_13378:  # 0m:0.111s
            shell_command_1510_13378()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=13379) as script_command_1511_13379:  # 0m:0.013s
            script_command_1511_13379()
        with Exec(r"/Library/Application Support/Waves/Modules/remove_leftovers_V10.py", args=None, ignore_all_errors=True, prog_num=13380) as exec_1512_13380:  # 0m:0.016s
            exec_1512_13380()
        with If(IsFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/../V9/Common/Utilities/remove_leftovers.py"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/Modules/V9/remove_leftovers.py", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V9/Common/Utilities/remove_leftovers.py", hard_links=False), prog_num=13381) as if_1513_13381:  # 0m:0.000s
            if_1513_13381()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=13382) as rm_file_or_dir_1514_13382:  # 0m:0.000s
            rm_file_or_dir_1514_13382()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13383) as glober_1515_13383:  # 0m:0.001s
            glober_1515_13383()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=13384) as shell_command_1516_13384:  # 0m:4.124s
            shell_command_1516_13384()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=13385) as shell_command_1517_13385:  # 0m:0.122s
            shell_command_1517_13385()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=13386) as script_command_1518_13386:  # 0m:0.013s
            script_command_1518_13386()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=13387) as if_1519_13387:  # 0m:0.000s
            if_1519_13387()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13388) as if_1520_13388:  # 0m:0.000s
            if_1520_13388()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=13389) as if_1521_13389:  # 0m:0.000s
            if_1521_13389()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13390) as if_1522_13390:  # 0m:0.000s
            if_1522_13390()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=13391) as make_dir_1523_13391:  # 0m:0.008s
            make_dir_1523_13391()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=13392) as chmod_1524_13392:  # 0m:0.000s
            chmod_1524_13392()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=13393) as make_dir_1525_13393:  # 0m:0.008s
            make_dir_1525_13393()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=13394) as chmod_1526_13394:  # 0m:0.000s
            chmod_1526_13394()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13395) as chmod_1527_13395:  # 0m:0.000s
            chmod_1527_13395()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13396) as chmod_1528_13396:  # 0m:0.000s
            chmod_1528_13396()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=13397) as chmod_1529_13397:  # 0m:0.000s
            chmod_1529_13397()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=13398) as shell_command_1530_13398:  # 0m:0.108s
            shell_command_1530_13398()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=13399) as script_command_1531_13399:  # 0m:0.014s
            script_command_1531_13399()
    with Stage(r"post-copy", prog_num=13400):  # 0m:0.035s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13401) as make_dir_1532_13401:  # 0m:0.009s
            make_dir_1532_13401()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=13402) as copy_file_to_file_1533_13402:  # 0m:0.009s
            copy_file_to_file_1533_13402()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13403) as chmod_1534_13403:  # 0m:0.000s
            chmod_1534_13403()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13404) as chmod_1535_13404:  # 0m:0.000s
            chmod_1535_13404()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=13405) as copy_file_to_file_1536_13405:  # 0m:0.008s
            copy_file_to_file_1536_13405()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13406) as chmod_1537_13406:  # 0m:0.000s
            chmod_1537_13406()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=13407) as copy_file_to_file_1538_13407:  # 0m:0.007s
            copy_file_to_file_1538_13407()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13408) as chmod_1539_13408:  # 0m:0.000s
            chmod_1539_13408()
        Progress(r"Done copy", prog_num=13409)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=13410)()  # 0m:0.000s
    with Stage(r"post", prog_num=13411):  # 0m:0.055s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13412) as make_dir_1540_13412:  # 0m:0.007s
            make_dir_1540_13412()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=13413) as copy_file_to_file_1541_13413:  # 0m:0.010s
            copy_file_to_file_1541_13413()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13414) as make_dir_1542_13414:  # 0m:0.011s
            make_dir_1542_13414()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=13415) as copy_file_to_file_1543_13415:  # 0m:0.009s
            copy_file_to_file_1543_13415()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13416) as make_dir_1544_13416:  # 0m:0.007s
            make_dir_1544_13416()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/31/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=13417) as copy_file_to_file_1545_13417:  # 0m:0.011s
            copy_file_to_file_1545_13417()

with Stage(r"epilog", prog_num=13418):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250120135643.py", prog_num=13419) as patch_py_batch_with_timings_1546_13419:  # ?
        patch_py_batch_with_timings_1546_13419()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 4050180330 bytes in 1m:46.805s, 37921109 bytes per second
# copy time 2m:49.447s
