# Creation time: 08-05-25_01-00
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 7187
PythonBatchCommandBase.running_progress = 870
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=871):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"14-20250508010011"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", r"/Applications/Waves/Data/Video Sound Suite Impulses", r"/Applications/Waves/Data/Video Sound Suite Impulses")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.4.7"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V14", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 180
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NjcxNjQxMX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQ2NjgwMTExfX19XX0_;CloudFront-Signature=TrwCKW1ajlzu3PHe0Ip9dDmoV2InNeJi-rJ~b8BJpDG6abj~TkH18ntKJkqDS8FSGJBCXfUGXT~7iT8PEbX-1wNuw5Bq~PB7kIFr9ONEnK5tVqtQBBkATd~k1yRhjuQyF3MSdRIjRqihe8QWsmG2lA8P8fkwNXGeJElkk~ygjYh0rtwkBAfdrKAtw0BopFbo~n4v3-FtX~57OhPj5TW-GlI0tatYlU52l-lDCR3dQW-uF1RLGV2vuqt5jOOEyKaj3NFR1oBqEOAc4CZJCi1GreDrRtobi5whEsgRW3EjDU4a6Jv3mWE3CMH8Pfxn7F7Kqen2GeGBm6DaD9Y7fVuDGQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NjcxNjQxMX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQ2NjgwMTExfX19XX0_;CloudFront-Signature=TrwCKW1ajlzu3PHe0Ip9dDmoV2InNeJi-rJ~b8BJpDG6abj~TkH18ntKJkqDS8FSGJBCXfUGXT~7iT8PEbX-1wNuw5Bq~PB7kIFr9ONEnK5tVqtQBBkATd~k1yRhjuQyF3MSdRIjRqihe8QWsmG2lA8P8fkwNXGeJElkk~ygjYh0rtwkBAfdrKAtw0BopFbo~n4v3-FtX~57OhPj5TW-GlI0tatYlU52l-lDCR3dQW-uF1RLGV2vuqt5jOOEyKaj3NFR1oBqEOAc4CZJCi1GreDrRtobi5whEsgRW3EjDU4a6Jv3mWE3CMH8Pfxn7F7Kqen2GeGBm6DaD9Y7fVuDGQ__"
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14"
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
    config_vars['HAVE_INFO_MAP_COPY_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FILE_NAME'] = r"have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FOR_COPY'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt"
    config_vars['HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['INDEX_CHECKSUM'] = r"4c4cb4c13a2e3d1b4f1d1d65d363fe153b09bfa8"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/80/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"42d804192e402dc258a859dbcd600da0b1204550"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/80/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/80/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 3, 10)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"Fixed reporting of bad actions in verify repo"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"1dc38c2d-aaf6-45d1-a67f-2c1448d41d8f", r"45197058-00f3-4e1e-9381-cd0d545356b5")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 180
    config_vars['MIN_REPO_REV'] = 1
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NEW_HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt"
    config_vars['NEW_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/new_require.yaml"
    config_vars['NI_SERVICE_CENTER'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NO_FLAGS_PATTERNS'] = (r"desktop.ini", r"*.ico")
    config_vars['NO_HARD_LINK_PATTERNS'] = (r"*Info.xml", r"*Info.plist", r"desktop.ini", r"*.ico")
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 2
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 4
    config_vars['OLD_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/old_require.yaml"
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250508010011.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180/index.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 14
    config_vars['REPO_NAME'] = r"V14"
    config_vars['REPO_REV'] = 180
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V14_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-04-01 09:25:16.994053"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V14_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"01/80"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_REV'] = 0
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"3ddb3ee569deabdc0c392cacb78c33786bf20ed7"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/80/instl/short-index.yaml"
    config_vars['SHOULD_NOT_BE_REQUIRED_BY'] = r"(Plugin\d+_\d+_Root_\d+_\d+_IID)|(GTR(_Internals|_Stomps|Solo_Stomps)_IID)"
    config_vars['SITE_BOOKKEEPING_DIR'] = r"/Library/Application Support"
    config_vars['SITE_HAVE_INFO_MAP_PATH'] = r"/Library/Application Support/Waves/Central/V14/have_info_map.txt"
    config_vars['SITE_REPO_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central/V14"
    config_vars['SITE_REQUIRE_FILE_NAME'] = r"require.yaml"
    config_vars['SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/require.yaml"
    config_vars['SITE_VENDOR_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central"
    config_vars['SOURCE_PREFIX'] = r"Mac"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14"
    config_vars['SYNC_BASE_URL_MAIN_ITEM'] = r"d36wza55md4dee.cloudfront.net"
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"after-sync-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 6312
    config_vars['TO_SYNC_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/to_sync_info_map.txt"
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl"
    config_vars['USE_ZLIB'] = r"yes"
    config_vars['VENDOR_DIR_NAME'] = r"Waves/Central"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVES_APPS_DIR'] = r"/Applications/Waves/Applications V14"
    config_vars['WAVES_APPS_DIR_V10'] = r"/Applications/Waves/Applications V10"
    config_vars['WAVES_APPS_DIR_V11'] = r"/Applications/Waves/Applications V11"
    config_vars['WAVES_APPS_DIR_V12'] = r"/Applications/Waves/Applications V12"
    config_vars['WAVES_APPS_DIR_V13'] = r"/Applications/Waves/Applications V13"
    config_vars['WAVES_CENTRAL_EXTERNAL_DATA'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/data"
    config_vars['WAVES_CENTRAL_INSTALL_DIR'] = r"/Applications/Waves/Applications V14"
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
    config_vars['WAVES_PLUGINS_DIR'] = r"/Applications/Waves/Plug-Ins V14"
    config_vars['WAVES_PREFERENCES_DIR'] = r"/Users/rsp_ms/Library/Preferences/Waves Preferences"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WAVES_SG_TEMPLATES_DIR'] = r"/Users/Shared/Waves/eMotion"
    config_vars['WAVES_SHARED_DIR'] = r"/Users/Shared/Waves"
    config_vars['WAVES_SHELLS_DIR'] = r"/Applications/Waves/WaveShells V14"
    config_vars['WAVES_SHELLS_DIR_V10'] = r"/Applications/Waves/WaveShells V10"
    config_vars['WAVES_SHELLS_DIR_V11'] = r"/Applications/Waves/WaveShells V11"
    config_vars['WAVES_SHELLS_DIR_V12'] = r"/Applications/Waves/WaveShells V12"
    config_vars['WAVES_SHELLS_DIR_V13'] = r"/Applications/Waves/WaveShells V13"
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
    config_vars['WAVES_UNUSED_PLUGINS_DIR'] = r"/Applications/Waves/Unused Plug-Ins V14"
    config_vars['WAVES_WPAPI_DIR'] = r"/Library/Audio/Plug-Ins/WPAPI"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250508010011.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"unknown compilation time"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.4.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"A-H_M_Documents_IID", r"A-H_M_IOM_IID", r"A-H_M_s3_Firmware_13_4_IID", r"A-H_M_s6_Firmware_13_4_IID", r"A-H_M_sq_Firmware_13_4_IID", r"A-H_M_v3_Firmware_14_12_IID", r"All_IOMs_IID", r"Apogee_Symphony_Documents_IID", r"Apogee_Symphony_Firmware_13_4_IID", r"Apogee_Symphony_IID", r"Apogee_Symphony_IOM_IID", r"Apogee_Symphony_micro_Firmware_13_4_IID", r"BR1_Documents_IID", r"BR1_Firmware_13_7_IID", r"BR1_IID", r"BR1_IOM_IID", r"Behringer_Wing_SoundGrid_IO_Driver_Firmware_14_25_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IOM_IID", r"Burl_BMB4_Documents_IID", r"Burl_BMB4_Firmware_13_4_IID", r"Burl_BMB4_IID", r"Burl_BMB4_IOM_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"Cadac_Documents_IID", r"Cadac_Firmware_13_4_IID", r"Cadac_IID", r"Cadac_IOM_IID", r"Calrec_Documents_IID", r"Calrec_Firmware_13_4_IID", r"Calrec_IID", r"Calrec_IOM_IID", r"Converter_IID", r"Crest_Tactus_Documents_IID", r"Crest_Tactus_Firmware_13_4_IID", r"Crest_Tactus_IID", r"Crest_Tactus_IO_Modules_IID", r"Crest_Tactus_micro_Firmware_13_4_IID", r"DLI_DLS_Documents_IID", r"DLI_DLS_IID", r"DLI_DLS_IOM_IID", r"DLI_DLS_eMotion_IID", r"DLI_Firmware_12_1_IID", r"DLI_Firmware_13_4_IID", r"DLS_Firmware_12_1_IID", r"DLS_Firmware_13_4_IID", r"DMI_Waves_Documents_IID", r"DMI_Waves_Firmware_13_7_IID", r"DMI_Waves_IID", r"DMI_Waves_IOM_IID", r"DN32_WSG_Documents_IID", r"DN32_WSG_Firmware_13_4_IID", r"DN32_WSG_IID", r"DN32_WSG_IOM_IID", r"DSPro_SG1000_Firmware_13_4_IID", r"DSPro_SG1000_Firmware_13_6_IID", r"DSPro_SG1000_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_13_4_IID", r"DSPro_SG1000_micro_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_15_1_IID", r"DSPro_SG1000_micro_V2_Firmware_15_1_IID", r"DSPro_SG4000_Documents_IID", r"DSPro_SG4000_Firmware_13_4_IID", r"DSPro_SG4000_Firmware_13_5_IID", r"DSPro_SG4000_Firmware_14_26_IID", r"DSPro_SG4000_IID", r"DSPro_SG4000_IOM_IID", r"DSPro_SG4000_micro_Firmware_13_4_IID", r"DSPro_SG4000_micro_Firmware_14_25_IID", r"DSPro_SG4000_micro_Firmware_15_2_IID", r"DSPro_SG4000_micro_V2_Firmware_15_2_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_2_IID", r"DiGiGrid_D_Driver_Documents_IID", r"DiGiGrid_D_Driver_Firmware_13_4_IID", r"DiGiGrid_D_Driver_IID", r"DiGiGrid_D_Driver_IOM_IID", r"DiGiGrid_M_Driver_Documents_IID", r"DiGiGrid_M_Driver_Firmware_13_4_IID", r"DiGiGrid_M_Driver_IID", r"DiGiGrid_M_Driver_IOM_IID", r"DiGiGrid_Q_Driver_Documents_IID", r"DiGiGrid_Q_Driver_Firmware_13_4_IID", r"DiGiGrid_Q_Driver_IID", r"DiGiGrid_Q_Driver_IOM_IID", r"DigiGrid_SoundGrid__Documents__IID", r"Digico_SD_IOM_IID", r"Digico_SD_card_13_4_IID", r"Digico_SD_card_Documents_IID", r"Digico_SD_card_Firmware_14_21_IID", r"Digico_SD_card_IOM_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_22_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_v2_micro_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IOM_IID", r"DirectOut_SG_MADI_Documents_IID", r"DirectOut_SG_MADI_Firmware_13_4_IID", r"DirectOut_SG_MADI_IID", r"DirectOut_SG_MADI_IOM_IID", r"DirectOut_SG_MADI_micro_Firmware_13_4_IID", r"DirectOut_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_SoundGrid_IO_Driver_IID", r"DirectOut_SoundGrid_IO_Driver_IOM_IID", r"Get_General_Icons_IID", r"Hear_Back_Documents_IID", r"Hear_Back_Firmware_10_0_IID", r"Hear_Back_Firmware_13_7_IID", r"Hear_Back_IID", r"Hear_Back_IOM_IID", r"Hear_Back_IO_Modules_IID", r"Hear_Back_Pro_V2_Firmware_13_7_IID", r"Hear_Tech_Documents_IID", r"Hear_Tech_Firmware_15_1_IID", r"Hear_Tech_Firmware_15_1_v2_IID", r"Hear_Tech_IID", r"Hear_Tech_IOM_IID", r"IOC_Documents_IID", r"IOC_Firmware_13_4_IID", r"IOC_IID", r"IOC_IOM_IID", r"IOC_micro_Firmware_13_4_IID", r"IONIC16_Firmware_S25_IID", r"IONIC16_Firmware_S50_IID", r"IONIC_Documents_IID", r"IONIC_IID", r"IONIC_IOM_IID", r"IOS_Documents_IID", r"IOS_Firmware_13_4_IID", r"IOS_IID", r"IOS_IOM_IID", r"IOS_XL_Documents_IID", r"IOS_XL_Firmware_13_4_IID", r"IOS_XL_IID", r"IOS_XL_IOM_IID", r"IOS_XL_micro_Firmware_13_4_IID", r"IOS_eMotion_IID", r"IOS_micro_Firmware_13_4_IID", r"IOX_Documents_IID", r"IOX_Firmware_13_4_IID", r"IOX_IID", r"IOX_IOM_IID", r"IOX_eMotion_IID", r"IOX_micro_Firmware_13_4_IID", r"IOs_FW_and_Modules__IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Insert_IID", r"IntelDlls_IID", r"JoeCo_Documents_IID", r"JoeCo_Firmware_13_4_IID", r"JoeCo_IID", r"JoeCo_IOM_IID", r"JoeCo_Utilities_IID", r"M-DL-WAVES3_IID", r"M-SQ-WAVES3_IID", r"M-Waves_V2_IID", r"MGB_Firmware_13_4_IID", r"MGB_MGO_Documents_IID", r"MGB_MGO_IID", r"MGB_MGO_IOM_IID", r"MGB_MGO_eMotion_IID", r"MGO_Firmware_13_4_IID", r"MKL_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MKL_x32_IID", r"MKL_x64_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"MixerSessionConverter_IID", r"MultiRack_SG_IO_Modules_IID", r"MyRemote_IID", r"Plugin_Infra__IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_2_IID", r"PresetBrowser_IID", r"QT_5_12_8_IID", r"QT_5_5_1_FOR_IO_MODULES_IID", r"QT_5_5_1_IID", r"QT_6_2_4_IID", r"Remote_IO_Modules_IID", r"Restart_required_IID", r"SGS_14_9_Firmware_IID", r"SG_Connect_IID", r"SG_Driver_Documents_IID", r"SG_Driver_Uninstaller_IID", r"SG_Driver_V12_2_IID", r"SG_Driver_V12_2_Install_IID", r"SG_Infra_and_Common__IID", r"SG_Studio_V11_8CH_IID", r"SG_Studio_V11_preferences_cleanup_IID", r"STG_1608_Firmware_13_4_IID", r"STG_1608_micro_Firmware_13_4_IID", r"STG_2412_Documents_IID", r"STG_2412_Firmware_13_4_IID", r"STG_2412_IID", r"STG_2412_IOM_IID", r"STG_2412_micro_Firmware_13_4_IID", r"SampleTestConverter_IID", r"Session_Converters_IID", r"Shutdown_Servers_IID", r"SoundGrid_Studio_IID", r"SoundGrid_Studio_Plugins__IID", r"SoundGrid_Studio_app__Application__IID", r"SoundGrid_Studio_app__Documents__IID", r"SoundGrid_Studio_app__IID", r"SoundGrid_Studio_app__Modules__IID", r"SoundGrid_Studio_app__Sessions_Structure__IID", r"SoundGrid_Studio_app__Shared_Folder__IID", r"SoundGrid_folder_IID", r"StudioRack_Data_IID", r"StudioRack_IID", r"StudioRack_Impulses_IID", r"StudioRack_Presets_Compatibility_IID", r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID", r"V9_V10_Organizer_IID", r"WAVE_SHELL_OBS_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_14_12_IID", r"WaveShell1_AAX_14_21_IID", r"WaveShell1_AU_14_12_IID", r"WaveShell1_AU_14_21_IID", r"WaveShell1_VST_2_V14_12_IID", r"WaveShell1_VST_2_V14_21_IID", r"WaveShell1_VST_3_V14_12_IID", r"WaveShell1_VST_3_V14_21_IID", r"WaveShell1_WPAPI_2_14_12_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesLib1_14_12_90_381_IID", r"WavesLib1_14_21_96_552_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V14_2_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"X-WSG_Documents_IID", r"X-WSG_IID", r"X-WSG_IOM_IID", r"X-WSG_s6_Firmware_13_4_IID", r"Y-16_Documents_IID", r"Y-16_IID", r"Y-16_IOM_IID", r"Y-16_s3_Firmware_13_4_IID", r"Y-16_s6_Firmware_13_4_IID", r"Y-16_v3_Firmware_14_21_IID", r"Yamaha_HY128v2_Firmware_IID", r"Yamaha_WSG_Firmware_13_4_IID")
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.2 unknown compilation time RSPMS.local"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.2"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 2)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"nipmnmixhomyopsv"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"SG_Studio_V11_8CH_IID", r"StudioRack_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-05-08 01:00:16.873919"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 1667671796
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 1996
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"RSPMS.local"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
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

with PythonBatchRuntime(r"synccopy", prog_num=872):  # 1m:55.735s
    with Stage(r"begin", prog_num=873):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=874):  # 0m:0.006s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=875) as copy_file_to_file_001_875:  # 0m:0.000s
            copy_file_to_file_001_875()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=876) as copy_file_to_file_002_876:  # 0m:0.006s
            copy_file_to_file_002_876()
    with Stage(r"sync", prog_num=877):  # 0m:20.434s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=878) as shell_command_003_878:  # 0m:0.009s
            shell_command_003_878()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=879) as shell_command_004_879:  # 0m:0.012s
            shell_command_004_879()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=880) as shell_command_005_880:  # 0m:0.005s
            shell_command_005_880()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=881) as shell_command_006_881:  # 0m:0.005s
            shell_command_006_881()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=882) as shell_command_007_882:  # 0m:0.005s
            shell_command_007_882()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=883) as shell_command_008_883:  # 0m:1.164s
            shell_command_008_883()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V14", prog_num=884):  # 0m:19.233s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", chowner=True, prog_num=885) as make_dir_009_885:  # 0m:0.006s
                make_dir_009_885()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=886) as cd_010_886:  # 0m:19.226s
                cd_010_886()
                Progress(r"291 files already in cache", own_progress_count=291, prog_num=1177)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=428, prog_num=1605) as create_sync_folders_011_1605:  # 0m:0.065s
                    create_sync_folders_011_1605()
                Progress(r"Downloading with 50 processes in parallel", prog_num=1606)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=1607)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.py_curl/dl-00", total_files_to_download=1996, previously_downloaded_files=0, total_bytes_to_download=1667671796, own_progress_count=1971, prog_num=3578, report_own_progress=False) as curl_with_internal_parallel_012_3578:  # 0m:17.387s
                    curl_with_internal_parallel_012_3578()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.py_curl/dl-01", total_files_to_download=1996, previously_downloaded_files=1971, total_bytes_to_download=1667671796, own_progress_count=25, prog_num=3603, report_own_progress=False) as curl_with_internal_parallel_013_3603:  # 0m:0.170s
                    curl_with_internal_parallel_013_3603()
                Progress(r"Downloading 1996 files done", prog_num=3604)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=3605) as run_in_thread_014_3605:  # 0m:0.000s
                    run_in_thread_014_3605()
                Progress(r"Check checksum ...", prog_num=3606)()  # 0m:0.000s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=1996, prog_num=5602) as check_download_folder_checksum_015_5602:  # 0m:1.540s
                    check_download_folder_checksum_015_5602()
                with Stage(r"post_sync", prog_num=5603):  # 0m:0.063s
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14...", prog_num=5604)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=5605, recursive=True) as chmod_and_chown_016_5605:  # 0m:0.052s
                        chmod_and_chown_016_5605()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=5606) as copy_file_to_file_017_5606:  # 0m:0.011s
                        copy_file_to_file_017_5606()
            Progress(r"Done sync", prog_num=5607)()  # 0m:0.000s
    with Stage(r"copy", prog_num=5608):  # 1m:35.223s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=5609)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=5610):  # 0m:0.141s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=5611) as make_dir_018_5611:  # 0m:0.009s
                make_dir_018_5611()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=5612) as make_dir_019_5612:  # 0m:0.006s
                make_dir_019_5612()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=5613) as make_dir_020_5613:  # 0m:0.008s
                make_dir_020_5613()
            with MakeDir(r"/Applications/Waves/Data/linux/lib/mkl", chowner=True, prog_num=5614) as make_dir_021_5614:  # 0m:0.001s
                make_dir_021_5614()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14", chowner=True, prog_num=5615) as make_dir_022_5615:  # 0m:0.000s
                make_dir_022_5615()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14/Documents", chowner=True, prog_num=5616) as make_dir_023_5616:  # 0m:0.000s
                make_dir_023_5616()
            with MakeDir(r"/Applications/Waves/SoundGrid", chowner=True, prog_num=5617) as make_dir_024_5617:  # 0m:0.000s
                make_dir_024_5617()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio", chowner=True, prog_num=5618) as make_dir_025_5618:  # 0m:0.000s
                make_dir_025_5618()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Documents", chowner=True, prog_num=5619) as make_dir_026_5619:  # 0m:0.000s
                make_dir_026_5619()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Modules", chowner=True, prog_num=5620) as make_dir_027_5620:  # 0m:0.000s
                make_dir_027_5620()
            with MakeDir(r"/Applications/Waves/SoundGrid/Documents", chowner=True, prog_num=5621) as make_dir_028_5621:  # 0m:0.000s
                make_dir_028_5621()
            with MakeDir(r"/Applications/Waves/SoundGrid/Utilities", chowner=True, prog_num=5622) as make_dir_029_5622:  # 0m:0.000s
                make_dir_029_5622()
            with MakeDir(r"/Applications/Waves/WaveShells V14", chowner=True, prog_num=5623) as make_dir_030_5623:  # 0m:0.000s
                make_dir_030_5623()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=5624) as make_dir_031_5624:  # 0m:0.009s
                make_dir_031_5624()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=5625) as make_dir_032_5625:  # 0m:0.005s
                make_dir_032_5625()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode", chowner=True, prog_num=5626) as make_dir_033_5626:  # 0m:0.008s
                make_dir_033_5626()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V14", chowner=True, prog_num=5627) as make_dir_034_5627:  # 0m:0.000s
                make_dir_034_5627()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=5628) as make_dir_035_5628:  # 0m:0.006s
                make_dir_035_5628()
            with MakeDir(r"/Library/Application Support/Waves/MyMon", chowner=True, prog_num=5629) as make_dir_036_5629:  # 0m:0.000s
                make_dir_036_5629()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser", chowner=True, prog_num=5630) as make_dir_037_5630:  # 0m:0.004s
                make_dir_037_5630()
            with MakeDir(r"/Library/Application Support/Waves/RemoteServices", chowner=True, prog_num=5631) as make_dir_038_5631:  # 0m:0.000s
                make_dir_038_5631()
            with MakeDir(r"/Library/Application Support/Waves/Session Converters", chowner=True, prog_num=5632) as make_dir_039_5632:  # 0m:0.003s
                make_dir_039_5632()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", chowner=True, prog_num=5633) as make_dir_040_5633:  # 0m:0.001s
                make_dir_040_5633()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", chowner=True, prog_num=5634) as make_dir_041_5634:  # 0m:0.000s
                make_dir_041_5634()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid IO Modules", chowner=True, prog_num=5635) as make_dir_042_5635:  # 0m:0.000s
                make_dir_042_5635()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=5636) as make_dir_043_5636:  # 0m:0.005s
                make_dir_043_5636()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=5637) as make_dir_044_5637:  # 0m:0.008s
                make_dir_044_5637()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=5638) as make_dir_045_5638:  # 0m:0.011s
                make_dir_045_5638()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=5639) as make_dir_046_5639:  # 0m:0.007s
                make_dir_046_5639()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=5640) as make_dir_047_5640:  # 0m:0.007s
                make_dir_047_5640()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=5641) as make_dir_048_5641:  # 0m:0.004s
                make_dir_048_5641()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=5642) as make_dir_049_5642:  # 0m:0.006s
                make_dir_049_5642()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=5643) as make_dir_050_5643:  # 0m:0.006s
                make_dir_050_5643()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/History", chowner=True, prog_num=5644) as make_dir_051_5644:  # 0m:0.008s
                make_dir_051_5644()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Sessions", chowner=True, prog_num=5645) as make_dir_052_5645:  # 0m:0.006s
                make_dir_052_5645()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Templates", chowner=True, prog_num=5646) as make_dir_053_5646:  # 0m:0.005s
                make_dir_053_5646()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=5647) as make_dir_054_5647:  # 0m:0.007s
                make_dir_054_5647()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=5648) as rm_file_or_dir_055_5648:  # 0m:0.000s
            rm_file_or_dir_055_5648()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=5649) as shell_command_056_5649:  # 0m:0.008s
            shell_command_056_5649()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=5650) as shell_command_057_5650:  # 0m:0.013s
            shell_command_057_5650()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=5651) as shell_command_058_5651:  # 0m:0.009s
            shell_command_058_5651()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=5652) as shell_command_059_5652:  # 0m:0.010s
            shell_command_059_5652()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=5653) as shell_command_060_5653:  # 0m:0.010s
            shell_command_060_5653()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=5654) as shell_command_061_5654:  # 0m:0.158s
            shell_command_061_5654()
        with ShellCommand(r"""osascript -e 'tell application "SoundGrid Studio" to quit' """, ignore_all_errors=True, prog_num=5655) as shell_command_062_5655:  # 0m:1.831s
            shell_command_062_5655()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=5656) as cd_stage_063_5656:  # 0m:0.010s
            cd_stage_063_5656()
            with SetExecPermissionsInSyncFolder(prog_num=5657) as set_exec_permissions_in_sync_folder_064_5657:  # 0m:0.010s
                set_exec_permissions_in_sync_folder_064_5657()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=5658) as cd_stage_065_5658:  # 0m:5.477s
            cd_stage_065_5658()
            with Stage(r"copy", r"StudioRack Data v1.0.0.5", prog_num=5659):  # 0m:5.318s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=5660) as should_copy_source_066_5660:  # 0m:5.318s
                    should_copy_source_066_5660()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=5661):  # 0m:5.317s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=5662) as copy_dir_to_dir_067_5662:  # 0m:0.037s
                            copy_dir_to_dir_067_5662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=5663) as unwtar_068_5663:  # 0m:5.280s
                            unwtar_068_5663()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=5664, recursive=True) as chown_069_5664:  # 0m:0.000s
                            chown_069_5664()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.1.0", prog_num=5665):  # 0m:0.157s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=5666) as should_copy_source_070_5666:  # 0m:0.157s
                    should_copy_source_070_5666()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=5667):  # 0m:0.157s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=5668) as copy_dir_to_dir_071_5668:  # 0m:0.156s
                            copy_dir_to_dir_071_5668()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=5669, recursive=True) as chown_072_5669:  # 0m:0.000s
                            chown_072_5669()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=5670) as rm_globs_073_5670:  # 0m:0.001s
                rm_globs_073_5670()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=5671) as cd_stage_074_5671:  # 0m:0.040s
            cd_stage_074_5671()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=5672):  # 0m:0.034s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=5673) as should_copy_source_075_5673:  # 0m:0.015s
                    should_copy_source_075_5673()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=5674):  # 0m:0.014s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=5675) as copy_dir_to_dir_076_5675:  # 0m:0.014s
                            copy_dir_to_dir_076_5675()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=5676, recursive=True) as chown_077_5676:  # 0m:0.000s
                            chown_077_5676()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=5677) as should_copy_source_078_5677:  # 0m:0.019s
                    should_copy_source_078_5677()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=5678):  # 0m:0.018s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=5679) as copy_dir_to_dir_079_5679:  # 0m:0.018s
                            copy_dir_to_dir_079_5679()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=5680, recursive=True) as chown_080_5680:  # 0m:0.000s
                            chown_080_5680()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/linux/lib/mkl", prog_num=5681) as cd_stage_081_5681:  # 0m:11.674s
            cd_stage_081_5681()
            with Stage(r"copy", r"MKL_x32_IID v1.0.0.1", prog_num=5682):  # 0m:3.466s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=5683) as should_copy_source_082_5683:  # 0m:3.465s
                    should_copy_source_082_5683()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/ia32", prog_num=5684):  # 0m:3.465s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r".", delete_extraneous_files=True, prog_num=5685) as copy_dir_to_dir_083_5685:  # 0m:0.002s
                            copy_dir_to_dir_083_5685()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", where_to_unwtar=r".", prog_num=5686) as unwtar_084_5686:  # 0m:3.463s
                            unwtar_084_5686()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/ia32", user_id=-1, group_id=-1, prog_num=5687, recursive=True) as chown_085_5687:  # 0m:0.000s
                            chown_085_5687()
            with Stage(r"copy", r"MKL_x64_IID v1.0.0.1", prog_num=5688):  # 0m:8.208s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=5689) as should_copy_source_086_5689:  # 0m:8.208s
                    should_copy_source_086_5689()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/intel64", prog_num=5690):  # 0m:8.208s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r".", delete_extraneous_files=True, prog_num=5691) as copy_dir_to_dir_087_5691:  # 0m:0.001s
                            copy_dir_to_dir_087_5691()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", where_to_unwtar=r".", prog_num=5692) as unwtar_088_5692:  # 0m:8.206s
                            unwtar_088_5692()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/intel64", user_id=-1, group_id=-1, prog_num=5693, recursive=True) as chown_089_5693:  # 0m:0.001s
                            chown_089_5693()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14", prog_num=5694) as cd_stage_090_5694:  # 0m:3.753s
            cd_stage_090_5694()
            with Stage(r"copy", r"Insert v14.12.90.381", prog_num=5695):  # 0m:0.142s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=5696) as should_copy_source_091_5696:  # 0m:0.142s
                    should_copy_source_091_5696()
                    with Stage(r"copy source", r"Mac/Plugins/Insert.bundle", prog_num=5697):  # 0m:0.142s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r".", delete_extraneous_files=True, prog_num=5698) as copy_dir_to_dir_092_5698:  # 0m:0.003s
                            copy_dir_to_dir_092_5698()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", where_to_unwtar=r".", prog_num=5699) as unwtar_093_5699:  # 0m:0.139s
                            unwtar_093_5699()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/Insert.bundle", user_id=-1, group_id=-1, prog_num=5700, recursive=True) as chown_094_5700:  # 0m:0.000s
                            chown_094_5700()
            with Stage(r"copy", r"StudioRack v14.21.96.552", prog_num=5701):  # 0m:2.459s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=5702) as should_copy_source_095_5702:  # 0m:2.458s
                    should_copy_source_095_5702()
                    with Stage(r"copy source", r"Mac/Plugins/StudioRack.bundle", prog_num=5703):  # 0m:2.458s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r".", delete_extraneous_files=True, prog_num=5704) as copy_dir_to_dir_096_5704:  # 0m:0.016s
                            copy_dir_to_dir_096_5704()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", where_to_unwtar=r".", prog_num=5705) as unwtar_097_5705:  # 0m:2.442s
                            unwtar_097_5705()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/StudioRack.bundle", user_id=-1, group_id=-1, prog_num=5706, recursive=True) as chown_098_5706:  # 0m:0.000s
                            chown_098_5706()
            with Stage(r"copy", r"WavesLib1_14_12_90_381 v14.12.90.381", prog_num=5707):  # 0m:0.490s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=5708) as should_copy_source_099_5708:  # 0m:0.490s
                    should_copy_source_099_5708()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.12.90.framework", prog_num=5709):  # 0m:0.490s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r".", delete_extraneous_files=True, prog_num=5710) as copy_dir_to_dir_100_5710:  # 0m:0.002s
                            copy_dir_to_dir_100_5710()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", where_to_unwtar=r".", prog_num=5711) as unwtar_101_5711:  # 0m:0.488s
                            unwtar_101_5711()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.12.90.framework", user_id=-1, group_id=-1, prog_num=5712, recursive=True) as chown_102_5712:  # 0m:0.000s
                            chown_102_5712()
            with Stage(r"copy", r"WavesLib1_14_21_96_552 v14.21.96.552", prog_num=5713):  # 0m:0.460s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=5714) as should_copy_source_103_5714:  # 0m:0.460s
                    should_copy_source_103_5714()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.21.96.framework", prog_num=5715):  # 0m:0.460s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r".", delete_extraneous_files=True, prog_num=5716) as copy_dir_to_dir_104_5716:  # 0m:0.002s
                            copy_dir_to_dir_104_5716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", where_to_unwtar=r".", prog_num=5717) as unwtar_105_5717:  # 0m:0.457s
                            unwtar_105_5717()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.21.96.framework", user_id=-1, group_id=-1, prog_num=5718, recursive=True) as chown_106_5718:  # 0m:0.000s
                            chown_106_5718()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V14", own_progress_count=4, prog_num=5722) as resolve_symlink_files_in_folder_107_5722:  # 0m:0.004s
                resolve_symlink_files_in_folder_107_5722()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V14" -c', ignore_all_errors=True, prog_num=5723) as shell_command_108_5723:  # 0m:0.115s
                shell_command_108_5723()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V14"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V14"/Icon?; fi', prog_num=5724) as script_command_109_5724:  # 0m:0.012s
                script_command_109_5724()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5725) as shell_command_110_5725:  # 0m:0.059s
                shell_command_110_5725()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=5726) as create_symlink_111_5726:  # 0m:0.001s
                create_symlink_111_5726()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=5727) as create_symlink_112_5727:  # 0m:0.000s
                create_symlink_112_5727()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=5728) as copy_glob_to_dir_113_5728:  # 0m:0.010s
                copy_glob_to_dir_113_5728()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14/Documents", prog_num=5729) as cd_stage_114_5729:  # 0m:0.001s
            cd_stage_114_5729()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=5730):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V14/Documents", skip_progress_count=3, prog_num=5731) as should_copy_source_115_5731:  # 0m:0.001s
                    should_copy_source_115_5731()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=5732):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=5733) as copy_file_to_dir_116_5733:  # 0m:0.000s
                            copy_file_to_dir_116_5733()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5734) as chmod_and_chown_117_5734:  # 0m:0.000s
                            chmod_and_chown_117_5734()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio", prog_num=5735) as cd_stage_118_5735:  # 0m:0.927s
            cd_stage_118_5735()
            with Stage(r"copy", r"SoundGrid Studio V11", prog_num=5736):  # 0m:0.793s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r"/Applications/Waves/SoundGrid Studio", skip_progress_count=4, prog_num=5737) as should_copy_source_119_5737:  # 0m:0.793s
                    should_copy_source_119_5737()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", prog_num=5738):  # 0m:0.793s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r".", delete_extraneous_files=True, prog_num=5739) as copy_dir_to_dir_120_5739:  # 0m:0.003s
                            copy_dir_to_dir_120_5739()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", where_to_unwtar=r".", prog_num=5740) as unwtar_121_5740:  # 0m:0.789s
                            unwtar_121_5740()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app", user_id=-1, group_id=-1, prog_num=5741, recursive=True) as chown_122_5741:  # 0m:0.000s
                            chown_122_5741()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio", own_progress_count=4, prog_num=5745) as resolve_symlink_files_in_folder_123_5745:  # 0m:0.002s
                resolve_symlink_files_in_folder_123_5745()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=5746) as shell_command_124_5746:  # 0m:0.011s
                shell_command_124_5746()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid Studio" -c', ignore_all_errors=True, prog_num=5747) as shell_command_125_5747:  # 0m:0.098s
                shell_command_125_5747()
            with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid Studio"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid Studio"/Icon?; fi', prog_num=5748) as script_command_126_5748:  # 0m:0.012s
                script_command_126_5748()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5749) as shell_command_127_5749:  # 0m:0.011s
                shell_command_127_5749()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=5750) as cd_stage_128_5750:  # 0m:10.291s
            cd_stage_128_5750()
            with Stage(r"copy", r"SoundGrid Studio Documents", prog_num=5751):  # 0m:10.291s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=3, prog_num=5752) as should_copy_source_129_5752:  # 0m:0.001s
                    should_copy_source_129_5752()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", prog_num=5753):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=5754) as copy_file_to_dir_130_5754:  # 0m:0.000s
                            copy_file_to_dir_130_5754()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5755) as chmod_and_chown_131_5755:  # 0m:0.000s
                            chmod_and_chown_131_5755()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=5756) as should_copy_source_132_5756:  # 0m:9.821s
                    should_copy_source_132_5756()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", prog_num=5757):  # 0m:9.821s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4.wtar.aa", where_to_unwtar=r".", prog_num=5758) as unwtar_133_5758:  # 0m:9.821s
                            unwtar_133_5758()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=5759) as should_copy_source_134_5759:  # 0m:0.468s
                    should_copy_source_134_5759()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGStudio.pdf", prog_num=5760):  # 0m:0.468s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf.wtar.aa", where_to_unwtar=r".", prog_num=5761) as unwtar_135_5761:  # 0m:0.467s
                            unwtar_135_5761()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=5762) as cd_stage_136_5762:  # 0m:2.225s
            cd_stage_136_5762()
            with Stage(r"copy", r"SoundGrid Studio Modules", prog_num=5763):  # 0m:1.842s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5764) as should_copy_source_137_5764:  # 0m:0.103s
                    should_copy_source_137_5764()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", prog_num=5765):  # 0m:0.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r".", delete_extraneous_files=True, prog_num=5766) as copy_dir_to_dir_138_5766:  # 0m:0.001s
                            copy_dir_to_dir_138_5766()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", where_to_unwtar=r".", prog_num=5767) as unwtar_139_5767:  # 0m:0.101s
                            unwtar_139_5767()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoom.bundle", user_id=-1, group_id=-1, prog_num=5768, recursive=True) as chown_140_5768:  # 0m:0.000s
                            chown_140_5768()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5769) as should_copy_source_141_5769:  # 0m:0.315s
                    should_copy_source_141_5769()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", prog_num=5770):  # 0m:0.315s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=5771) as copy_dir_to_dir_142_5771:  # 0m:0.001s
                            copy_dir_to_dir_142_5771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", where_to_unwtar=r".", prog_num=5772) as unwtar_143_5772:  # 0m:0.313s
                            unwtar_143_5772()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", user_id=-1, group_id=-1, prog_num=5773, recursive=True) as chown_144_5773:  # 0m:0.000s
                            chown_144_5773()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5774) as should_copy_source_145_5774:  # 0m:0.265s
                    should_copy_source_145_5774()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", prog_num=5775):  # 0m:0.265s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r".", delete_extraneous_files=True, prog_num=5776) as copy_dir_to_dir_146_5776:  # 0m:0.002s
                            copy_dir_to_dir_146_5776()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", where_to_unwtar=r".", prog_num=5777) as unwtar_147_5777:  # 0m:0.262s
                            unwtar_147_5777()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", user_id=-1, group_id=-1, prog_num=5778, recursive=True) as chown_148_5778:  # 0m:0.000s
                            chown_148_5778()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5779) as should_copy_source_149_5779:  # 0m:0.316s
                    should_copy_source_149_5779()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", prog_num=5780):  # 0m:0.316s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=5781) as copy_dir_to_dir_150_5781:  # 0m:0.001s
                            copy_dir_to_dir_150_5781()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=5782) as unwtar_151_5782:  # 0m:0.314s
                            unwtar_151_5782()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=5783, recursive=True) as chown_152_5783:  # 0m:0.000s
                            chown_152_5783()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5784) as should_copy_source_153_5784:  # 0m:0.027s
                    should_copy_source_153_5784()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", prog_num=5785):  # 0m:0.027s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r".", delete_extraneous_files=True, prog_num=5786) as copy_dir_to_dir_154_5786:  # 0m:0.002s
                            copy_dir_to_dir_154_5786()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", where_to_unwtar=r".", prog_num=5787) as unwtar_155_5787:  # 0m:0.025s
                            unwtar_155_5787()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MIDICommunication.framework", user_id=-1, group_id=-1, prog_num=5788, recursive=True) as chown_156_5788:  # 0m:0.000s
                            chown_156_5788()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5789) as should_copy_source_157_5789:  # 0m:0.053s
                    should_copy_source_157_5789()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", prog_num=5790):  # 0m:0.053s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r".", delete_extraneous_files=True, prog_num=5791) as copy_dir_to_dir_158_5791:  # 0m:0.001s
                            copy_dir_to_dir_158_5791()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", where_to_unwtar=r".", prog_num=5792) as unwtar_159_5792:  # 0m:0.051s
                            unwtar_159_5792()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/Mackie_Control.bundle", user_id=-1, group_id=-1, prog_num=5793, recursive=True) as chown_160_5793:  # 0m:0.000s
                            chown_160_5793()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5794) as should_copy_source_161_5794:  # 0m:0.053s
                    should_copy_source_161_5794()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", prog_num=5795):  # 0m:0.052s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r".", delete_extraneous_files=True, prog_num=5796) as copy_dir_to_dir_162_5796:  # 0m:0.001s
                            copy_dir_to_dir_162_5796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", where_to_unwtar=r".", prog_num=5797) as unwtar_163_5797:  # 0m:0.051s
                            unwtar_163_5797()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", user_id=-1, group_id=-1, prog_num=5798, recursive=True) as chown_164_5798:  # 0m:0.000s
                            chown_164_5798()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5799) as should_copy_source_165_5799:  # 0m:0.058s
                    should_copy_source_165_5799()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", prog_num=5800):  # 0m:0.057s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r".", delete_extraneous_files=True, prog_num=5801) as copy_dir_to_dir_166_5801:  # 0m:0.001s
                            copy_dir_to_dir_166_5801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", where_to_unwtar=r".", prog_num=5802) as unwtar_167_5802:  # 0m:0.056s
                            unwtar_167_5802()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", user_id=-1, group_id=-1, prog_num=5803, recursive=True) as chown_168_5803:  # 0m:0.000s
                            chown_168_5803()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5804) as should_copy_source_169_5804:  # 0m:0.123s
                    should_copy_source_169_5804()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", prog_num=5805):  # 0m:0.123s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r".", delete_extraneous_files=True, prog_num=5806) as copy_dir_to_dir_170_5806:  # 0m:0.002s
                            copy_dir_to_dir_170_5806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", where_to_unwtar=r".", prog_num=5807) as unwtar_171_5807:  # 0m:0.121s
                            unwtar_171_5807()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGST.bundle", user_id=-1, group_id=-1, prog_num=5808, recursive=True) as chown_172_5808:  # 0m:0.000s
                            chown_172_5808()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5809) as should_copy_source_173_5809:  # 0m:0.310s
                    should_copy_source_173_5809()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", prog_num=5810):  # 0m:0.309s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=5811) as copy_dir_to_dir_174_5811:  # 0m:0.001s
                            copy_dir_to_dir_174_5811()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=5812) as unwtar_175_5812:  # 0m:0.308s
                            unwtar_175_5812()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=5813, recursive=True) as chown_176_5813:  # 0m:0.000s
                            chown_176_5813()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5814) as should_copy_source_177_5814:  # 0m:0.057s
                    should_copy_source_177_5814()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", prog_num=5815):  # 0m:0.057s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r".", delete_extraneous_files=True, prog_num=5816) as copy_dir_to_dir_178_5816:  # 0m:0.001s
                            copy_dir_to_dir_178_5816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", where_to_unwtar=r".", prog_num=5817) as unwtar_179_5817:  # 0m:0.055s
                            unwtar_179_5817()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/StudioRack_Control.bundle", user_id=-1, group_id=-1, prog_num=5818, recursive=True) as chown_180_5818:  # 0m:0.000s
                            chown_180_5818()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=5819) as should_copy_source_181_5819:  # 0m:0.160s
                    should_copy_source_181_5819()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", prog_num=5820):  # 0m:0.160s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r".", delete_extraneous_files=True, prog_num=5821) as copy_dir_to_dir_182_5821:  # 0m:0.001s
                            copy_dir_to_dir_182_5821()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", where_to_unwtar=r".", prog_num=5822) as unwtar_183_5822:  # 0m:0.158s
                            unwtar_183_5822()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", user_id=-1, group_id=-1, prog_num=5823, recursive=True) as chown_184_5823:  # 0m:0.000s
                            chown_184_5823()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=3, prog_num=5824) as should_copy_source_185_5824:  # 0m:0.001s
                    should_copy_source_185_5824()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=5825):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r".", prog_num=5826) as copy_file_to_dir_186_5826:  # 0m:0.001s
                            copy_file_to_dir_186_5826()
                        with ChmodAndChown(path=r"com.WavesAudio.SoundGridStudioSilent.plist", mode="a+rw", user_id=-1, group_id=-1, prog_num=5827) as chmod_and_chown_187_5827:  # 0m:0.000s
                            chmod_and_chown_187_5827()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio/Modules", own_progress_count=8, prog_num=5835) as resolve_symlink_files_in_folder_188_5835:  # 0m:0.004s
                resolve_symlink_files_in_folder_188_5835()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5836) as shell_command_189_5836:  # 0m:0.182s
                shell_command_189_5836()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=5837) as shell_command_190_5837:  # 0m:0.195s
                shell_command_190_5837()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=5838) as create_symlink_191_5838:  # 0m:0.001s
                create_symlink_191_5838()
            with CreateSymlink(r"/Users/Shared/Waves/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=5839) as create_symlink_192_5839:  # 0m:0.000s
                create_symlink_192_5839()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Documents", prog_num=5840) as cd_stage_193_5840:  # 0m:0.411s
            cd_stage_193_5840()
            with Stage(r"copy", r"A-H_M_Documents", prog_num=5841):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5842) as should_copy_source_194_5842:  # 0m:0.001s
                    should_copy_source_194_5842()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", prog_num=5843):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r".", prog_num=5844) as copy_file_to_dir_195_5844:  # 0m:0.000s
                            copy_file_to_dir_195_5844()
                        with ChmodAndChown(path=r"A-H M-Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5845) as chmod_and_chown_196_5845:  # 0m:0.000s
                            chmod_and_chown_196_5845()
            with Stage(r"copy", r"Apogee Symphony pdf", prog_num=5846):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5847) as should_copy_source_197_5847:  # 0m:0.001s
                    should_copy_source_197_5847()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", prog_num=5848):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r".", prog_num=5849) as copy_file_to_dir_198_5849:  # 0m:0.000s
                            copy_file_to_dir_198_5849()
                        with ChmodAndChown(path=r"Apogee Symphony MKII SoundGrid User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5850) as chmod_and_chown_199_5850:  # 0m:0.000s
                            chmod_and_chown_199_5850()
            with Stage(r"copy", r"SG BR1 pdf", prog_num=5851):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5852) as should_copy_source_200_5852:  # 0m:0.001s
                    should_copy_source_200_5852()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG BR1.pdf", prog_num=5853):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r".", prog_num=5854) as copy_file_to_dir_201_5854:  # 0m:0.000s
                            copy_file_to_dir_201_5854()
                        with ChmodAndChown(path=r"SG BR1.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5855) as chmod_and_chown_202_5855:  # 0m:0.000s
                            chmod_and_chown_202_5855()
            with Stage(r"copy", r"Burl BMB4 pdf", prog_num=5856):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5857) as should_copy_source_203_5857:  # 0m:0.001s
                    should_copy_source_203_5857()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", prog_num=5858):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r".", prog_num=5859) as copy_file_to_dir_204_5859:  # 0m:0.000s
                            copy_file_to_dir_204_5859()
                        with ChmodAndChown(path=r"Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5860) as chmod_and_chown_205_5860:  # 0m:0.000s
                            chmod_and_chown_205_5860()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5861) as should_copy_source_206_5861:  # 0m:0.001s
                    should_copy_source_206_5861()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", prog_num=5862):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r".", prog_num=5863) as copy_file_to_dir_207_5863:  # 0m:0.000s
                            copy_file_to_dir_207_5863()
                        with ChmodAndChown(path=r"Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5864) as chmod_and_chown_208_5864:  # 0m:0.000s
                            chmod_and_chown_208_5864()
            with Stage(r"copy", r"Cadac pdf", prog_num=5865):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5866) as should_copy_source_209_5866:  # 0m:0.001s
                    should_copy_source_209_5866()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Cadac SG User Guide.pdf", prog_num=5867):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r".", prog_num=5868) as copy_file_to_dir_210_5868:  # 0m:0.000s
                            copy_file_to_dir_210_5868()
                        with ChmodAndChown(path=r"Cadac SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5869) as chmod_and_chown_211_5869:  # 0m:0.000s
                            chmod_and_chown_211_5869()
            with Stage(r"copy", r"Calrec pdf", prog_num=5870):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5871) as should_copy_source_212_5871:  # 0m:0.001s
                    should_copy_source_212_5871()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", prog_num=5872):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r".", prog_num=5873) as copy_file_to_dir_213_5873:  # 0m:0.000s
                            copy_file_to_dir_213_5873()
                        with ChmodAndChown(path=r"Calrec SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5874) as chmod_and_chown_214_5874:  # 0m:0.000s
                            chmod_and_chown_214_5874()
            with Stage(r"copy", r"Crest Tactus pdf", prog_num=5875):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5876) as should_copy_source_215_5876:  # 0m:0.001s
                    should_copy_source_215_5876()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus FOH OM.pdf", prog_num=5877):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r".", prog_num=5878) as copy_file_to_dir_216_5878:  # 0m:0.000s
                            copy_file_to_dir_216_5878()
                        with ChmodAndChown(path=r"Tactus FOH OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5879) as chmod_and_chown_217_5879:  # 0m:0.000s
                            chmod_and_chown_217_5879()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5880) as should_copy_source_218_5880:  # 0m:0.001s
                    should_copy_source_218_5880()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus Stage OM.pdf", prog_num=5881):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r".", prog_num=5882) as copy_file_to_dir_219_5882:  # 0m:0.000s
                            copy_file_to_dir_219_5882()
                        with ChmodAndChown(path=r"Tactus Stage OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5883) as chmod_and_chown_220_5883:  # 0m:0.000s
                            chmod_and_chown_220_5883()
            with Stage(r"copy", r"DLI DLS pdf", prog_num=5884):  # 0m:0.377s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=2, prog_num=5885) as should_copy_source_221_5885:  # 0m:0.377s
                    should_copy_source_221_5885()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DLI DLS User Guide.pdf", prog_num=5886):  # 0m:0.376s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf.wtar.aa", where_to_unwtar=r".", prog_num=5887) as unwtar_222_5887:  # 0m:0.376s
                            unwtar_222_5887()
            with Stage(r"copy", r"DMI Waves pdf", prog_num=5888):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5889) as should_copy_source_223_5889:  # 0m:0.001s
                    should_copy_source_223_5889()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DMI Waves User Guide.pdf", prog_num=5890):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r".", prog_num=5891) as copy_file_to_dir_224_5891:  # 0m:0.001s
                            copy_file_to_dir_224_5891()
                        with ChmodAndChown(path=r"DMI Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5892) as chmod_and_chown_225_5892:  # 0m:0.000s
                            chmod_and_chown_225_5892()
            with Stage(r"copy", r"DN32-WSG pdf", prog_num=5893):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5894) as should_copy_source_226_5894:  # 0m:0.001s
                    should_copy_source_226_5894()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", prog_num=5895):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r".", prog_num=5896) as copy_file_to_dir_227_5896:  # 0m:0.000s
                            copy_file_to_dir_227_5896()
                        with ChmodAndChown(path=r"DN32-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5897) as chmod_and_chown_228_5897:  # 0m:0.000s
                            chmod_and_chown_228_5897()
            with Stage(r"copy", r"DSPro SG4000 pdf", prog_num=5898):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5899) as should_copy_source_229_5899:  # 0m:0.001s
                    should_copy_source_229_5899()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", prog_num=5900):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r".", prog_num=5901) as copy_file_to_dir_230_5901:  # 0m:0.000s
                            copy_file_to_dir_230_5901()
                        with ChmodAndChown(path=r"STAGEGRID 1000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5902) as chmod_and_chown_231_5902:  # 0m:0.000s
                            chmod_and_chown_231_5902()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5903) as should_copy_source_232_5903:  # 0m:0.001s
                    should_copy_source_232_5903()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", prog_num=5904):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r".", prog_num=5905) as copy_file_to_dir_233_5905:  # 0m:0.000s
                            copy_file_to_dir_233_5905()
                        with ChmodAndChown(path=r"STAGEGRID 4000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5906) as chmod_and_chown_234_5906:  # 0m:0.000s
                            chmod_and_chown_234_5906()
            with Stage(r"copy", r"DiGiGrid D Driver pdf", prog_num=5907):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5908) as should_copy_source_235_5908:  # 0m:0.001s
                    should_copy_source_235_5908()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", prog_num=5909):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r".", prog_num=5910) as copy_file_to_dir_236_5910:  # 0m:0.000s
                            copy_file_to_dir_236_5910()
                        with ChmodAndChown(path=r"DiGiGrid D User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5911) as chmod_and_chown_237_5911:  # 0m:0.000s
                            chmod_and_chown_237_5911()
            with Stage(r"copy", r"DiGiGrid M Driver pdf", prog_num=5912):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5913) as should_copy_source_238_5913:  # 0m:0.001s
                    should_copy_source_238_5913()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", prog_num=5914):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r".", prog_num=5915) as copy_file_to_dir_239_5915:  # 0m:0.000s
                            copy_file_to_dir_239_5915()
                        with ChmodAndChown(path=r"DiGiGrid M User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5916) as chmod_and_chown_240_5916:  # 0m:0.000s
                            chmod_and_chown_240_5916()
            with Stage(r"copy", r"DiGiGrid Q Driver pdf", prog_num=5917):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5918) as should_copy_source_241_5918:  # 0m:0.001s
                    should_copy_source_241_5918()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", prog_num=5919):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r".", prog_num=5920) as copy_file_to_dir_242_5920:  # 0m:0.000s
                            copy_file_to_dir_242_5920()
                        with ChmodAndChown(path=r"DiGiGrid Q User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5921) as chmod_and_chown_243_5921:  # 0m:0.000s
                            chmod_and_chown_243_5921()
            with Stage(r"copy", r"DigiGrid S", prog_num=5922):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5923) as should_copy_source_244_5923:  # 0m:0.001s
                    should_copy_source_244_5923()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", prog_num=5924):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=5925) as copy_file_to_dir_245_5925:  # 0m:0.000s
                            copy_file_to_dir_245_5925()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5926) as chmod_and_chown_246_5926:  # 0m:0.000s
                            chmod_and_chown_246_5926()
            with Stage(r"copy", r"Digico SD card pdf", prog_num=5927):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5928) as should_copy_source_247_5928:  # 0m:0.001s
                    should_copy_source_247_5928()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", prog_num=5929):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r".", prog_num=5930) as copy_file_to_dir_248_5930:  # 0m:0.000s
                            copy_file_to_dir_248_5930()
                        with ChmodAndChown(path=r"DiGiCo SD SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5931) as chmod_and_chown_249_5931:  # 0m:0.000s
                            chmod_and_chown_249_5931()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid IO Driver", prog_num=5932):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5933) as should_copy_source_250_5933:  # 0m:0.001s
                    should_copy_source_250_5933()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", prog_num=5934):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r".", prog_num=5935) as copy_file_to_dir_251_5935:  # 0m:0.000s
                            copy_file_to_dir_251_5935()
                        with ChmodAndChown(path=r"DirectOut Exbox.SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5936) as chmod_and_chown_252_5936:  # 0m:0.000s
                            chmod_and_chown_252_5936()
            with Stage(r"copy", r"DirectOut SG.MADI pdf", prog_num=5937):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5938) as should_copy_source_253_5938:  # 0m:0.001s
                    should_copy_source_253_5938()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", prog_num=5939):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r".", prog_num=5940) as copy_file_to_dir_254_5940:  # 0m:0.000s
                            copy_file_to_dir_254_5940()
                        with ChmodAndChown(path=r"DirectOut SG.MADI User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5941) as chmod_and_chown_255_5941:  # 0m:0.000s
                            chmod_and_chown_255_5941()
            with Stage(r"copy", r"DirectOut SoundGrid IO Driver Documents", prog_num=5942):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5943) as should_copy_source_256_5943:  # 0m:0.001s
                    should_copy_source_256_5943()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", prog_num=5944):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r".", prog_num=5945) as copy_file_to_dir_257_5945:  # 0m:0.000s
                            copy_file_to_dir_257_5945()
                        with ChmodAndChown(path=r"DirectOut SG.IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5946) as chmod_and_chown_258_5946:  # 0m:0.000s
                            chmod_and_chown_258_5946()
            with Stage(r"copy", r"Hear Back pdf", prog_num=5947):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5948) as should_copy_source_259_5948:  # 0m:0.001s
                    should_copy_source_259_5948()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", prog_num=5949):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r".", prog_num=5950) as copy_file_to_dir_260_5950:  # 0m:0.000s
                            copy_file_to_dir_260_5950()
                        with ChmodAndChown(path=r"Hear Back PRO SG Card User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5951) as chmod_and_chown_261_5951:  # 0m:0.000s
                            chmod_and_chown_261_5951()
            with Stage(r"copy", r"HearTech pdf", prog_num=5952):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5953) as should_copy_source_262_5953:  # 0m:0.001s
                    should_copy_source_262_5953()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", prog_num=5954):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r".", prog_num=5955) as copy_file_to_dir_263_5955:  # 0m:0.001s
                            copy_file_to_dir_263_5955()
                        with ChmodAndChown(path=r"Hear Technologies SoundGrid Bridge User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5956) as chmod_and_chown_264_5956:  # 0m:0.000s
                            chmod_and_chown_264_5956()
            with Stage(r"copy", r"IOC pdf", prog_num=5957):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5958) as should_copy_source_265_5958:  # 0m:0.002s
                    should_copy_source_265_5958()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOC User Guide.pdf", prog_num=5959):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r".", prog_num=5960) as copy_file_to_dir_266_5960:  # 0m:0.001s
                            copy_file_to_dir_266_5960()
                        with ChmodAndChown(path=r"IOC User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5961) as chmod_and_chown_267_5961:  # 0m:0.000s
                            chmod_and_chown_267_5961()
            with Stage(r"copy", r"IONIC pdf", prog_num=5962):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5963) as should_copy_source_268_5963:  # 0m:0.001s
                    should_copy_source_268_5963()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", prog_num=5964):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r".", prog_num=5965) as copy_file_to_dir_269_5965:  # 0m:0.000s
                            copy_file_to_dir_269_5965()
                        with ChmodAndChown(path=r"IONIC 16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5966) as chmod_and_chown_270_5966:  # 0m:0.000s
                            chmod_and_chown_270_5966()
            with Stage(r"copy", r"IOS pdf", prog_num=5967):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5968) as should_copy_source_271_5968:  # 0m:0.001s
                    should_copy_source_271_5968()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS User Guide.pdf", prog_num=5969):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r".", prog_num=5970) as copy_file_to_dir_272_5970:  # 0m:0.000s
                            copy_file_to_dir_272_5970()
                        with ChmodAndChown(path=r"IOS User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5971) as chmod_and_chown_273_5971:  # 0m:0.000s
                            chmod_and_chown_273_5971()
            with Stage(r"copy", r"IOS-XL pdf", prog_num=5972):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5973) as should_copy_source_274_5973:  # 0m:0.001s
                    should_copy_source_274_5973()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS-XL User Guide.pdf", prog_num=5974):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r".", prog_num=5975) as copy_file_to_dir_275_5975:  # 0m:0.000s
                            copy_file_to_dir_275_5975()
                        with ChmodAndChown(path=r"IOS-XL User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5976) as chmod_and_chown_276_5976:  # 0m:0.000s
                            chmod_and_chown_276_5976()
            with Stage(r"copy", r"IOX pdf", prog_num=5977):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5978) as should_copy_source_277_5978:  # 0m:0.001s
                    should_copy_source_277_5978()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOX User Guide.pdf", prog_num=5979):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r".", prog_num=5980) as copy_file_to_dir_278_5980:  # 0m:0.000s
                            copy_file_to_dir_278_5980()
                        with ChmodAndChown(path=r"IOX User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5981) as chmod_and_chown_279_5981:  # 0m:0.000s
                            chmod_and_chown_279_5981()
            with Stage(r"copy", r"JoeCo BBSG24MP pdf", prog_num=5982):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5983) as should_copy_source_280_5983:  # 0m:0.001s
                    should_copy_source_280_5983()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", prog_num=5984):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r".", prog_num=5985) as copy_file_to_dir_281_5985:  # 0m:0.000s
                            copy_file_to_dir_281_5985()
                        with ChmodAndChown(path=r"JoeCo BBSG24MP User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5986) as chmod_and_chown_282_5986:  # 0m:0.000s
                            chmod_and_chown_282_5986()
            with Stage(r"copy", r"MGB MGO pdf", prog_num=5987):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5988) as should_copy_source_283_5988:  # 0m:0.001s
                    should_copy_source_283_5988()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", prog_num=5989):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r".", prog_num=5990) as copy_file_to_dir_284_5990:  # 0m:0.000s
                            copy_file_to_dir_284_5990()
                        with ChmodAndChown(path=r"DiGiGrid MGR User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5991) as chmod_and_chown_285_5991:  # 0m:0.000s
                            chmod_and_chown_285_5991()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5992) as should_copy_source_286_5992:  # 0m:0.001s
                    should_copy_source_286_5992()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/MGB MGO User Guide.pdf", prog_num=5993):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r".", prog_num=5994) as copy_file_to_dir_287_5994:  # 0m:0.000s
                            copy_file_to_dir_287_5994()
                        with ChmodAndChown(path=r"MGB MGO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=5995) as chmod_and_chown_288_5995:  # 0m:0.000s
                            chmod_and_chown_288_5995()
            with Stage(r"copy", r"SG Driver pdf", prog_num=5996):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=5997) as should_copy_source_289_5997:  # 0m:0.001s
                    should_copy_source_289_5997()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG Driver.pdf", prog_num=5998):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r".", prog_num=5999) as copy_file_to_dir_290_5999:  # 0m:0.000s
                            copy_file_to_dir_290_5999()
                        with ChmodAndChown(path=r"SG Driver.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6000) as chmod_and_chown_291_6000:  # 0m:0.000s
                            chmod_and_chown_291_6000()
            with Stage(r"copy", r"SoundStudio STG-2412 pdf", prog_num=6001):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6002) as should_copy_source_292_6002:  # 0m:0.001s
                    should_copy_source_292_6002()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-1608 User Guide.pdf", prog_num=6003):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r".", prog_num=6004) as copy_file_to_dir_293_6004:  # 0m:0.000s
                            copy_file_to_dir_293_6004()
                        with ChmodAndChown(path=r"STG-1608 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6005) as chmod_and_chown_294_6005:  # 0m:0.000s
                            chmod_and_chown_294_6005()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6006) as should_copy_source_295_6006:  # 0m:0.001s
                    should_copy_source_295_6006()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-2412 User Guide.pdf", prog_num=6007):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r".", prog_num=6008) as copy_file_to_dir_296_6008:  # 0m:0.000s
                            copy_file_to_dir_296_6008()
                        with ChmodAndChown(path=r"STG-2412 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6009) as chmod_and_chown_297_6009:  # 0m:0.000s
                            chmod_and_chown_297_6009()
            with Stage(r"copy", r"X-WSG pdf", prog_num=6010):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6011) as should_copy_source_298_6011:  # 0m:0.001s
                    should_copy_source_298_6011()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", prog_num=6012):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r".", prog_num=6013) as copy_file_to_dir_299_6013:  # 0m:0.000s
                            copy_file_to_dir_299_6013()
                        with ChmodAndChown(path=r"X-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6014) as chmod_and_chown_300_6014:  # 0m:0.000s
                            chmod_and_chown_300_6014()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6015) as should_copy_source_301_6015:  # 0m:0.001s
                    should_copy_source_301_6015()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG User Guide.pdf", prog_num=6016):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r".", prog_num=6017) as copy_file_to_dir_302_6017:  # 0m:0.000s
                            copy_file_to_dir_302_6017()
                        with ChmodAndChown(path=r"X-WSG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6018) as chmod_and_chown_303_6018:  # 0m:0.000s
                            chmod_and_chown_303_6018()
            with Stage(r"copy", r"Y-16_Documents", prog_num=6019):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6020) as should_copy_source_304_6020:  # 0m:0.001s
                    should_copy_source_304_6020()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", prog_num=6021):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r".", prog_num=6022) as copy_file_to_dir_305_6022:  # 0m:0.001s
                            copy_file_to_dir_305_6022()
                        with ChmodAndChown(path=r"WSG-HY128 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6023) as chmod_and_chown_306_6023:  # 0m:0.000s
                            chmod_and_chown_306_6023()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=6024) as should_copy_source_307_6024:  # 0m:0.001s
                    should_copy_source_307_6024()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", prog_num=6025):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r".", prog_num=6026) as copy_file_to_dir_308_6026:  # 0m:0.000s
                            copy_file_to_dir_308_6026()
                        with ChmodAndChown(path=r"WSG-Y16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6027) as chmod_and_chown_309_6027:  # 0m:0.000s
                            chmod_and_chown_309_6027()
            with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/BMB4 SoundGrid Motherboard User Guide.pdf", prog_num=6028) as rm_file_or_dir_310_6028:  # 0m:0.000s
                rm_file_or_dir_310_6028()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Utilities", prog_num=6029) as cd_stage_311_6029:  # 0m:1.792s
            cd_stage_311_6029()
            with Stage(r"copy", r"JoeCo BBSG24MP utilities", prog_num=6030):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=3, prog_num=6031) as should_copy_source_312_6031:  # 0m:0.002s
                    should_copy_source_312_6031()
                    with Stage(r"copy source", r"Common/SoundGrid/JoeCo", prog_num=6032):  # 0m:0.002s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r".", delete_extraneous_files=True, prog_num=6033) as copy_dir_to_dir_313_6033:  # 0m:0.001s
                            copy_dir_to_dir_313_6033()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/JoeCo", user_id=-1, group_id=-1, prog_num=6034, recursive=True) as chown_314_6034:  # 0m:0.000s
                            chown_314_6034()
            with Stage(r"copy", r"SoundGrid Control Panel Uninstaller v14.26.48.665", prog_num=6035):  # 0m:0.032s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=4, prog_num=6036) as should_copy_source_315_6036:  # 0m:0.032s
                    should_copy_source_315_6036()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", prog_num=6037):  # 0m:0.032s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r".", delete_extraneous_files=True, prog_num=6038) as copy_dir_to_dir_316_6038:  # 0m:0.003s
                            copy_dir_to_dir_316_6038()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", where_to_unwtar=r".", prog_num=6039) as unwtar_317_6039:  # 0m:0.028s
                            unwtar_317_6039()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app", user_id=-1, group_id=-1, prog_num=6040, recursive=True) as chown_318_6040:  # 0m:0.000s
                            chown_318_6040()
            with Stage(r"copy", r"SoundGrid V14 ASIO / Core Audio Rec/PB Control Panel v14.26.48.665", prog_num=6041):  # 0m:1.758s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=2, prog_num=6042) as should_copy_source_319_6042:  # 0m:1.758s
                    should_copy_source_319_6042()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", prog_num=6043):  # 0m:1.757s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg.wtar.aa", where_to_unwtar=r".", prog_num=6044) as unwtar_320_6044:  # 0m:1.757s
                            unwtar_320_6044()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V14", prog_num=6045) as cd_stage_321_6045:  # 0m:6.214s
            cd_stage_321_6045()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=6046):  # 0m:0.377s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6047) as should_copy_source_322_6047:  # 0m:0.377s
                    should_copy_source_322_6047()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=6048):  # 0m:0.377s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=6049) as copy_dir_to_dir_323_6049:  # 0m:0.001s
                            copy_dir_to_dir_323_6049()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=6050) as unwtar_324_6050:  # 0m:0.363s
                            unwtar_324_6050()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=6051, recursive=True) as chown_325_6051:  # 0m:0.000s
                            chown_325_6051()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=6052) as shell_command_326_6052:  # 0m:0.012s
                            shell_command_326_6052()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=6053):  # 0m:0.749s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6054) as should_copy_source_327_6054:  # 0m:0.748s
                    should_copy_source_327_6054()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=6055):  # 0m:0.748s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=6056) as copy_dir_to_dir_328_6056:  # 0m:0.003s
                            copy_dir_to_dir_328_6056()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=6057) as unwtar_329_6057:  # 0m:0.695s
                            unwtar_329_6057()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=6058, recursive=True) as chown_330_6058:  # 0m:0.000s
                            chown_330_6058()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=6059) as shell_command_331_6059:  # 0m:0.050s
                            shell_command_331_6059()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=6060):  # 0m:0.697s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6061) as should_copy_source_332_6061:  # 0m:0.696s
                    should_copy_source_332_6061()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=6062):  # 0m:0.696s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=6063) as copy_dir_to_dir_333_6063:  # 0m:0.004s
                            copy_dir_to_dir_333_6063()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=6064) as unwtar_334_6064:  # 0m:0.645s
                            unwtar_334_6064()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=6065, recursive=True) as chown_335_6065:  # 0m:0.000s
                            chown_335_6065()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=6066) as shell_command_336_6066:  # 0m:0.047s
                            shell_command_336_6066()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=6067):  # 0m:0.732s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=6068) as should_copy_source_337_6068:  # 0m:0.732s
                    should_copy_source_337_6068()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=6069):  # 0m:0.731s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=6070) as copy_dir_to_dir_338_6070:  # 0m:0.002s
                            copy_dir_to_dir_338_6070()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=6071) as unwtar_339_6071:  # 0m:0.655s
                            unwtar_339_6071()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=6072, recursive=True) as chown_340_6072:  # 0m:0.000s
                            chown_340_6072()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=6073) as break_hard_link_341_6073:  # 0m:0.015s
                            break_hard_link_341_6073()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=6074) as shell_command_342_6074:  # 0m:0.049s
                            shell_command_342_6074()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=6075, recursive=True) as chown_343_6075:  # 0m:0.000s
                            chown_343_6075()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=6076, recursive=True) as chmod_344_6076:  # 0m:0.009s
                            chmod_344_6076()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=6077):  # 0m:0.704s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=6078) as should_copy_source_345_6078:  # 0m:0.704s
                    should_copy_source_345_6078()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=6079):  # 0m:0.704s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=6080) as copy_dir_to_dir_346_6080:  # 0m:0.002s
                            copy_dir_to_dir_346_6080()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=6081) as unwtar_347_6081:  # 0m:0.625s
                            unwtar_347_6081()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=6082, recursive=True) as chown_348_6082:  # 0m:0.000s
                            chown_348_6082()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=6083) as break_hard_link_349_6083:  # 0m:0.017s
                            break_hard_link_349_6083()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=6084) as shell_command_350_6084:  # 0m:0.050s
                            shell_command_350_6084()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=6085, recursive=True) as chown_351_6085:  # 0m:0.000s
                            chown_351_6085()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=6086, recursive=True) as chmod_352_6086:  # 0m:0.009s
                            chmod_352_6086()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=6087):  # 0m:0.441s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6088) as should_copy_source_353_6088:  # 0m:0.441s
                    should_copy_source_353_6088()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=6089):  # 0m:0.441s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=6090) as copy_dir_to_dir_354_6090:  # 0m:0.002s
                            copy_dir_to_dir_354_6090()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=6091) as unwtar_355_6091:  # 0m:0.388s
                            unwtar_355_6091()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=6092, recursive=True) as chown_356_6092:  # 0m:0.000s
                            chown_356_6092()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=6093) as shell_command_357_6093:  # 0m:0.050s
                            shell_command_357_6093()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=6094):  # 0m:0.422s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6095) as should_copy_source_358_6095:  # 0m:0.422s
                    should_copy_source_358_6095()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=6096):  # 0m:0.421s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=6097) as copy_dir_to_dir_359_6097:  # 0m:0.002s
                            copy_dir_to_dir_359_6097()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=6098) as unwtar_360_6098:  # 0m:0.373s
                            unwtar_360_6098()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=6099, recursive=True) as chown_361_6099:  # 0m:0.000s
                            chown_361_6099()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=6100) as shell_command_362_6100:  # 0m:0.046s
                            shell_command_362_6100()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=6101):  # 0m:0.753s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6102) as should_copy_source_363_6102:  # 0m:0.753s
                    should_copy_source_363_6102()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=6103):  # 0m:0.753s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=6104) as copy_dir_to_dir_364_6104:  # 0m:0.002s
                            copy_dir_to_dir_364_6104()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=6105) as unwtar_365_6105:  # 0m:0.703s
                            unwtar_365_6105()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=6106, recursive=True) as chown_366_6106:  # 0m:0.000s
                            chown_366_6106()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=6107) as shell_command_367_6107:  # 0m:0.047s
                            shell_command_367_6107()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=6108):  # 0m:0.724s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=6109) as should_copy_source_368_6109:  # 0m:0.723s
                    should_copy_source_368_6109()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=6110):  # 0m:0.723s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=6111) as copy_dir_to_dir_369_6111:  # 0m:0.002s
                            copy_dir_to_dir_369_6111()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=6112) as unwtar_370_6112:  # 0m:0.673s
                            unwtar_370_6112()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=6113, recursive=True) as chown_371_6113:  # 0m:0.000s
                            chown_371_6113()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=6114) as shell_command_372_6114:  # 0m:0.048s
                            shell_command_372_6114()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=6115):  # 0m:0.377s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Applications/Waves/WaveShells V14", skip_progress_count=7, prog_num=6116) as should_copy_source_373_6116:  # 0m:0.377s
                    should_copy_source_373_6116()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=6117):  # 0m:0.377s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=6118) as copy_dir_to_dir_374_6118:  # 0m:0.001s
                            copy_dir_to_dir_374_6118()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=6119) as unwtar_375_6119:  # 0m:0.191s
                            unwtar_375_6119()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=6120, recursive=True) as chown_376_6120:  # 0m:0.000s
                            chown_376_6120()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6121) as shell_command_377_6121:  # 0m:0.116s
                            shell_command_377_6121()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6122) as script_command_378_6122:  # 0m:0.012s
                            script_command_378_6122()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6123) as shell_command_379_6123:  # 0m:0.055s
                            shell_command_379_6123()
            with Stage(r"copy", r"WaveShell-AU registration utility v14.12.90.381", prog_num=6124):  # 0m:0.131s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r"/Applications/Waves/WaveShells V14", skip_progress_count=4, prog_num=6125) as should_copy_source_380_6125:  # 0m:0.131s
                    should_copy_source_380_6125()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 14.app", prog_num=6126):  # 0m:0.131s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r".", delete_extraneous_files=True, prog_num=6127) as copy_dir_to_dir_381_6127:  # 0m:0.002s
                            copy_dir_to_dir_381_6127()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", where_to_unwtar=r".", prog_num=6128) as unwtar_382_6128:  # 0m:0.128s
                            unwtar_382_6128()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app", user_id=-1, group_id=-1, prog_num=6129, recursive=True) as chown_383_6129:  # 0m:0.000s
                            chown_383_6129()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 14.app"', ignore_all_errors=True, prog_num=6130) as shell_command_384_6130:  # 0m:0.104s
                shell_command_384_6130()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=6131) as cd_stage_385_6131:  # 0m:1.466s
            cd_stage_385_6131()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=6132):  # 0m:0.743s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=6133) as should_copy_source_386_6133:  # 0m:0.742s
                    should_copy_source_386_6133()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=6134):  # 0m:0.742s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=6135) as copy_dir_to_dir_387_6135:  # 0m:0.003s
                            copy_dir_to_dir_387_6135()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=6136) as unwtar_388_6136:  # 0m:0.685s
                            unwtar_388_6136()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=6137, recursive=True) as chown_389_6137:  # 0m:0.000s
                            chown_389_6137()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=6138) as shell_command_390_6138:  # 0m:0.054s
                            shell_command_390_6138()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=6139):  # 0m:0.723s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=6140) as should_copy_source_391_6140:  # 0m:0.722s
                    should_copy_source_391_6140()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=6141):  # 0m:0.722s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=6142) as copy_dir_to_dir_392_6142:  # 0m:0.004s
                            copy_dir_to_dir_392_6142()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=6143) as unwtar_393_6143:  # 0m:0.666s
                            unwtar_393_6143()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=6144, recursive=True) as chown_394_6144:  # 0m:0.000s
                            chown_394_6144()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=6145) as shell_command_395_6145:  # 0m:0.051s
                            shell_command_395_6145()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves", prog_num=6146) as cd_stage_396_6146:  # 0m:6.634s
            cd_stage_396_6146()
            with Stage(r"copy", r"Qt libraries 5.12.8", prog_num=6147):  # 0m:3.088s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=6148) as should_copy_source_397_6148:  # 0m:3.087s
                    should_copy_source_397_6148()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.12.8", prog_num=6149):  # 0m:3.087s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r".", delete_extraneous_files=True, prog_num=6150) as copy_dir_to_dir_398_6150:  # 0m:0.297s
                            copy_dir_to_dir_398_6150()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", where_to_unwtar=r".", prog_num=6151) as unwtar_399_6151:  # 0m:2.790s
                            unwtar_399_6151()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.12.8", user_id=-1, group_id=-1, prog_num=6152, recursive=True) as chown_400_6152:  # 0m:0.000s
                            chown_400_6152()
            with Stage(r"copy", r"QT_5_5_1_FOR_IO_MODULES", prog_num=6153):  # 0m:2.193s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=6154) as should_copy_source_401_6154:  # 0m:2.193s
                    should_copy_source_401_6154()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.5.1", prog_num=6155):  # 0m:2.193s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r".", delete_extraneous_files=True, prog_num=6156) as copy_dir_to_dir_402_6156:  # 0m:0.008s
                            copy_dir_to_dir_402_6156()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", where_to_unwtar=r".", prog_num=6157) as unwtar_403_6157:  # 0m:2.184s
                            unwtar_403_6157()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.5.1", user_id=-1, group_id=-1, prog_num=6158, recursive=True) as chown_404_6158:  # 0m:0.000s
                            chown_404_6158()
            with Stage(r"copy", r"Qt libraries 6.2.4", prog_num=6159):  # 0m:1.322s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=6160) as should_copy_source_405_6160:  # 0m:1.322s
                    should_copy_source_405_6160()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_6.2.4", prog_num=6161):  # 0m:1.322s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r".", delete_extraneous_files=True, prog_num=6162) as copy_dir_to_dir_406_6162:  # 0m:0.006s
                            copy_dir_to_dir_406_6162()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", where_to_unwtar=r".", prog_num=6163) as unwtar_407_6163:  # 0m:1.315s
                            unwtar_407_6163()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_6.2.4", user_id=-1, group_id=-1, prog_num=6164, recursive=True) as chown_408_6164:  # 0m:0.000s
                            chown_408_6164()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves", own_progress_count=42, prog_num=6206) as resolve_symlink_files_in_folder_409_6206:  # 0m:0.030s
                resolve_symlink_files_in_folder_409_6206()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode", prog_num=6207) as cd_stage_410_6207:  # 0m:0.020s
            cd_stage_410_6207()
            with Stage(r"copy", r"Demo Mode v1.0", prog_num=6208):  # 0m:0.020s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r"/Library/Application Support/Waves/Demo Mode", skip_progress_count=3, prog_num=6209) as should_copy_source_411_6209:  # 0m:0.020s
                    should_copy_source_411_6209()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14", prog_num=6210):  # 0m:0.019s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r".", delete_extraneous_files=True, prog_num=6211) as copy_dir_to_dir_412_6211:  # 0m:0.019s
                            copy_dir_to_dir_412_6211()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14", user_id=-1, group_id=-1, prog_num=6212, recursive=True) as chown_413_6212:  # 0m:0.000s
                            chown_413_6212()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V14", prog_num=6213) as cd_stage_414_6213:  # 0m:0.000s
            cd_stage_414_6213()
            with Stage(r"copy", r"Demo Mode 2.2 v2.2", prog_num=6214):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r"/Library/Application Support/Waves/Demo Mode/V14", skip_progress_count=3, prog_num=6215) as should_copy_source_415_6215:  # ?
                    should_copy_source_415_6215()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14/2", prog_num=6216):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r".", delete_extraneous_files=True, prog_num=6217) as copy_dir_to_dir_416_6217:  # ?
                            copy_dir_to_dir_416_6217()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14/2", user_id=-1, group_id=-1, prog_num=6218, recursive=True) as chown_417_6218:  # 0m:0.000s
                            chown_417_6218()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=6219) as cd_stage_418_6219:  # 0m:3.310s
            cd_stage_418_6219()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=6220) as rm_file_or_dir_419_6220:  # 0m:0.000s
                rm_file_or_dir_419_6220()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.2.1.3", prog_num=6221):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=6222) as should_copy_source_420_6222:  # ?
                    should_copy_source_420_6222()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=6223):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r".", delete_extraneous_files=True, prog_num=6224) as copy_dir_to_dir_421_6224:  # ?
                            copy_dir_to_dir_421_6224()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=6225) as unwtar_422_6225:  # ?
                            unwtar_422_6225()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=6226, recursive=True) as chown_423_6226:  # 0m:0.001s
                            chown_423_6226()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=6227):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=6228) as should_copy_source_424_6228:  # 0m:0.004s
                    should_copy_source_424_6228()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=6229):  # 0m:0.004s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=6230) as unwtar_425_6230:  # 0m:0.004s
                            unwtar_425_6230()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=6231):  # 0m:3.241s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=6232) as should_copy_source_426_6232:  # 0m:3.241s
                    should_copy_source_426_6232()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=6233):  # 0m:3.240s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=6234) as copy_dir_to_dir_427_6234:  # 0m:0.015s
                            copy_dir_to_dir_427_6234()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=6235) as unwtar_428_6235:  # 0m:3.225s
                            unwtar_428_6235()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=6236, recursive=True) as chown_429_6236:  # 0m:0.000s
                            chown_429_6236()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=6237):  # 0m:0.050s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=6238) as should_copy_source_430_6238:  # 0m:0.050s
                    should_copy_source_430_6238()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=6239):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6240) as copy_dir_to_dir_431_6240:  # 0m:0.049s
                            copy_dir_to_dir_431_6240()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=6241) as chmod_432_6241:  # 0m:0.000s
                            chmod_432_6241()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=6242) as chmod_433_6242:  # 0m:0.000s
                            chmod_433_6242()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=6243, recursive=True) as chown_434_6243:  # 0m:0.000s
                            chown_434_6243()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=6246) as resolve_symlink_files_in_folder_435_6246:  # 0m:0.002s
                resolve_symlink_files_in_folder_435_6246()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6247) as shell_command_436_6247:  # 0m:0.012s
                shell_command_436_6247()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/MyMon", prog_num=6248) as cd_stage_437_6248:  # 0m:1.952s
            cd_stage_437_6248()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=6249):  # 0m:1.939s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/MyMon", skip_progress_count=4, prog_num=6250) as should_copy_source_438_6250:  # 0m:1.939s
                    should_copy_source_438_6250()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=6251):  # 0m:1.939s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=6252) as copy_dir_to_dir_439_6252:  # 0m:0.001s
                            copy_dir_to_dir_439_6252()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=6253) as unwtar_440_6253:  # 0m:1.937s
                            unwtar_440_6253()
                        with Chown(path=r"/Library/Application Support/Waves/MyMon/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=6254, recursive=True) as chown_441_6254:  # 0m:0.000s
                            chown_441_6254()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6255) as shell_command_442_6255:  # 0m:0.012s
                shell_command_442_6255()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser", prog_num=6256) as cd_stage_443_6256:  # 0m:0.035s
            cd_stage_443_6256()
            with Stage(r"copy", r"Preset Browser 2.1 v2.1", prog_num=6257):  # 0m:0.024s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=6258) as should_copy_source_444_6258:  # 0m:0.024s
                    should_copy_source_444_6258()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=6259):  # 0m:0.024s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=6260) as copy_dir_to_dir_445_6260:  # 0m:0.024s
                            copy_dir_to_dir_445_6260()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=6261, recursive=True) as chown_446_6261:  # 0m:0.000s
                            chown_446_6261()
            with Stage(r"copy", r"Preset Browser V14 v1.9", prog_num=6262):  # 0m:0.010s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=6263) as should_copy_source_447_6263:  # 0m:0.010s
                    should_copy_source_447_6263()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=6264):  # 0m:0.010s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=6265) as copy_dir_to_dir_448_6265:  # 0m:0.009s
                            copy_dir_to_dir_448_6265()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=6266, recursive=True) as chown_449_6266:  # 0m:0.000s
                            chown_449_6266()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/RemoteServices", prog_num=6267) as cd_stage_450_6267:  # 0m:1.951s
            cd_stage_450_6267()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=6268):  # 0m:1.934s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/RemoteServices", skip_progress_count=4, prog_num=6269) as should_copy_source_451_6269:  # 0m:1.934s
                    should_copy_source_451_6269()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=6270):  # 0m:1.934s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=6271) as copy_dir_to_dir_452_6271:  # 0m:0.002s
                            copy_dir_to_dir_452_6271()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=6272) as unwtar_453_6272:  # 0m:1.932s
                            unwtar_453_6272()
                        with Chown(path=r"/Library/Application Support/Waves/RemoteServices/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=6273, recursive=True) as chown_454_6273:  # 0m:0.000s
                            chown_454_6273()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6274) as shell_command_455_6274:  # 0m:0.016s
                shell_command_455_6274()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Session Converters", prog_num=6275) as cd_stage_456_6275:  # 0m:0.355s
            cd_stage_456_6275()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_9_9.bundle", prog_num=6276) as rm_file_or_dir_457_6276:  # 0m:0.000s
                rm_file_or_dir_457_6276()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_2_18.bundle", prog_num=6277) as rm_file_or_dir_458_6277:  # 0m:0.000s
                rm_file_or_dir_458_6277()
            with Stage(r"copy", r"Converter", prog_num=6278):  # 0m:0.277s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=6279) as should_copy_source_459_6279:  # 0m:0.086s
                    should_copy_source_459_6279()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", prog_num=6280):  # 0m:0.086s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r".", delete_extraneous_files=True, prog_num=6281) as copy_dir_to_dir_460_6281:  # 0m:0.001s
                            copy_dir_to_dir_460_6281()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", where_to_unwtar=r".", prog_num=6282) as unwtar_461_6282:  # 0m:0.085s
                            unwtar_461_6282()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_2x.bundle", user_id=-1, group_id=-1, prog_num=6283, recursive=True) as chown_462_6283:  # 0m:0.000s
                            chown_462_6283()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=6284) as should_copy_source_463_6284:  # 0m:0.191s
                    should_copy_source_463_6284()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", prog_num=6285):  # 0m:0.190s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r".", delete_extraneous_files=True, prog_num=6286) as copy_dir_to_dir_464_6286:  # 0m:0.001s
                            copy_dir_to_dir_464_6286()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", where_to_unwtar=r".", prog_num=6287) as unwtar_465_6287:  # 0m:0.189s
                            unwtar_465_6287()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_3x.bundle", user_id=-1, group_id=-1, prog_num=6288, recursive=True) as chown_466_6288:  # 0m:0.000s
                            chown_466_6288()
            with Stage(r"copy", r"MixerSessionConverter", prog_num=6289):  # 0m:0.077s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=6290) as should_copy_source_467_6290:  # 0m:0.077s
                    should_copy_source_467_6290()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter.bundle", prog_num=6291):  # 0m:0.077s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r".", delete_extraneous_files=True, prog_num=6292) as copy_dir_to_dir_468_6292:  # 0m:0.001s
                            copy_dir_to_dir_468_6292()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", where_to_unwtar=r".", prog_num=6293) as unwtar_469_6293:  # 0m:0.076s
                            unwtar_469_6293()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter.bundle", user_id=-1, group_id=-1, prog_num=6294, recursive=True) as chown_470_6294:  # 0m:0.000s
                            chown_470_6294()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=6295) as cd_stage_471_6295:  # 0m:1.375s
            cd_stage_471_6295()
            with Stage(r"copy", r"Allen & Heath M s3 Firmware v13.4.0.205", prog_num=6296):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6297) as should_copy_source_472_6297:  # 0m:0.001s
                    should_copy_source_472_6297()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", prog_num=6298):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r".", prog_num=6299) as copy_file_to_dir_473_6299:  # 0m:0.000s
                            copy_file_to_dir_473_6299()
                        with ChmodAndChown(path=r"IO_13.4_AH_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6300) as chmod_and_chown_474_6300:  # 0m:0.000s
                            chmod_and_chown_474_6300()
            with Stage(r"copy", r"Allen & Heath M s6 Firmware v13.4.0.205", prog_num=6301):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6302) as should_copy_source_475_6302:  # 0m:0.001s
                    should_copy_source_475_6302()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", prog_num=6303):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r".", prog_num=6304) as copy_file_to_dir_476_6304:  # 0m:0.000s
                            copy_file_to_dir_476_6304()
                        with ChmodAndChown(path=r"IO_13.4_AH_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6305) as chmod_and_chown_477_6305:  # 0m:0.000s
                            chmod_and_chown_477_6305()
            with Stage(r"copy", r"Allen & Heath sq Firmware v13.4.0.205", prog_num=6306):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6307) as should_copy_source_478_6307:  # 0m:0.001s
                    should_copy_source_478_6307()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", prog_num=6308):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r".", prog_num=6309) as copy_file_to_dir_479_6309:  # 0m:0.000s
                            copy_file_to_dir_479_6309()
                        with ChmodAndChown(path=r"IO_13.4_AH_sq.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6310) as chmod_and_chown_480_6310:  # 0m:0.000s
                            chmod_and_chown_480_6310()
            with Stage(r"copy", r"Allen & Heath M v3 Firmware v14.12.33.324", prog_num=6311):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6312) as should_copy_source_481_6312:  # 0m:0.001s
                    should_copy_source_481_6312()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", prog_num=6313):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r".", prog_num=6314) as copy_file_to_dir_482_6314:  # 0m:0.000s
                            copy_file_to_dir_482_6314()
                        with ChmodAndChown(path=r"IO_14.12_A_H_V3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6315) as chmod_and_chown_483_6315:  # 0m:0.000s
                            chmod_and_chown_483_6315()
            with Stage(r"copy", r"Apogee_Symphony_Firmware_13_4 v13.4.0.205", prog_num=6316):  # 0m:0.235s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=6317) as should_copy_source_484_6317:  # 0m:0.235s
                    should_copy_source_484_6317()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", prog_num=6318):  # 0m:0.234s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi.wtar.aa", where_to_unwtar=r".", prog_num=6319) as unwtar_485_6319:  # 0m:0.234s
                            unwtar_485_6319()
            with Stage(r"copy", r"Apogee_Symphony_micro_Firmware_13_4 v13.4.0.205", prog_num=6320):  # 0m:0.571s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=6321) as should_copy_source_486_6321:  # 0m:0.570s
                    should_copy_source_486_6321()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", prog_num=6322):  # 0m:0.570s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi.wtar.aa", where_to_unwtar=r".", prog_num=6323) as unwtar_487_6323:  # 0m:0.570s
                            unwtar_487_6323()
            with Stage(r"copy", r"SoundGrid BR-1 Firmware v13.7.87.375", prog_num=6324):  # 0m:0.517s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=6325) as should_copy_source_488_6325:  # 0m:0.517s
                    should_copy_source_488_6325()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", prog_num=6326):  # 0m:0.516s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi.wtar.aa", where_to_unwtar=r".", prog_num=6327) as unwtar_489_6327:  # 0m:0.516s
                            unwtar_489_6327()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Firmware 14.25 v14.25.21.582", prog_num=6328):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6329) as should_copy_source_490_6329:  # 0m:0.001s
                    should_copy_source_490_6329()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", prog_num=6330):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r".", prog_num=6331) as copy_file_to_dir_491_6331:  # 0m:0.001s
                            copy_file_to_dir_491_6331()
                        with ChmodAndChown(path=r"IO_14.25_Behringer_WING_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6332) as chmod_and_chown_492_6332:  # 0m:0.000s
                            chmod_and_chown_492_6332()
            with Stage(r"copy", r"Burl Audio BMB4 Firmware v13.4.0.205", prog_num=6333):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6334) as should_copy_source_493_6334:  # 0m:0.001s
                    should_copy_source_493_6334()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=6335):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r".", prog_num=6336) as copy_file_to_dir_494_6336:  # 0m:0.000s
                            copy_file_to_dir_494_6336()
                        with ChmodAndChown(path=r"IO_13.4_BurlAudio_Bmb4.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6337) as chmod_and_chown_495_6337:  # 0m:0.000s
                            chmod_and_chown_495_6337()
            with Stage(r"copy", r"Cadac_Firmware_13_4 v13.4.0.205", prog_num=6338):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6339) as should_copy_source_496_6339:  # 0m:0.001s
                    should_copy_source_496_6339()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", prog_num=6340):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r".", prog_num=6341) as copy_file_to_dir_497_6341:  # 0m:0.000s
                            copy_file_to_dir_497_6341()
                        with ChmodAndChown(path=r"IO_13.4_Cadac.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6342) as chmod_and_chown_498_6342:  # 0m:0.000s
                            chmod_and_chown_498_6342()
            with Stage(r"copy", r"Calrec_Firmware_13_4 v13.4.0.205", prog_num=6343):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6344) as should_copy_source_499_6344:  # 0m:0.001s
                    should_copy_source_499_6344()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", prog_num=6345):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r".", prog_num=6346) as copy_file_to_dir_500_6346:  # 0m:0.000s
                            copy_file_to_dir_500_6346()
                        with ChmodAndChown(path=r"IO_13.4_Calrec.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6347) as chmod_and_chown_501_6347:  # 0m:0.000s
                            chmod_and_chown_501_6347()
            with Stage(r"copy", r"Crest Audio Tactus Firmware v13.4.0.205", prog_num=6348):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6349) as should_copy_source_502_6349:  # 0m:0.001s
                    should_copy_source_502_6349()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", prog_num=6350):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r".", prog_num=6351) as copy_file_to_dir_503_6351:  # 0m:0.000s
                            copy_file_to_dir_503_6351()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6352) as chmod_and_chown_504_6352:  # 0m:0.000s
                            chmod_and_chown_504_6352()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6353) as should_copy_source_505_6353:  # 0m:0.001s
                    should_copy_source_505_6353()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", prog_num=6354):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r".", prog_num=6355) as copy_file_to_dir_506_6355:  # 0m:0.000s
                            copy_file_to_dir_506_6355()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6356) as chmod_and_chown_507_6356:  # 0m:0.000s
                            chmod_and_chown_507_6356()
            with Stage(r"copy", r"Crest Audio Tactus micro Firmware v13.4.0.205", prog_num=6357):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6358) as should_copy_source_508_6358:  # 0m:0.001s
                    should_copy_source_508_6358()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", prog_num=6359):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r".", prog_num=6360) as copy_file_to_dir_509_6360:  # 0m:0.000s
                            copy_file_to_dir_509_6360()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6361) as chmod_and_chown_510_6361:  # 0m:0.000s
                            chmod_and_chown_510_6361()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6362) as should_copy_source_511_6362:  # 0m:0.001s
                    should_copy_source_511_6362()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", prog_num=6363):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r".", prog_num=6364) as copy_file_to_dir_512_6364:  # 0m:0.000s
                            copy_file_to_dir_512_6364()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6365) as chmod_and_chown_513_6365:  # 0m:0.000s
                            chmod_and_chown_513_6365()
            with Stage(r"copy", r"DigiGrid DLI Firmware v13.4.0.205", prog_num=6366):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6367) as should_copy_source_514_6367:  # 0m:0.001s
                    should_copy_source_514_6367()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", prog_num=6368):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r".", prog_num=6369) as copy_file_to_dir_515_6369:  # 0m:0.000s
                            copy_file_to_dir_515_6369()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6370) as chmod_and_chown_516_6370:  # 0m:0.000s
                            chmod_and_chown_516_6370()
            with Stage(r"copy", r"DigiGrid DLS Firmware v13.4.0.205", prog_num=6371):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6372) as should_copy_source_517_6372:  # 0m:0.001s
                    should_copy_source_517_6372()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", prog_num=6373):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r".", prog_num=6374) as copy_file_to_dir_518_6374:  # 0m:0.000s
                            copy_file_to_dir_518_6374()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6375) as chmod_and_chown_519_6375:  # 0m:0.000s
                            chmod_and_chown_519_6375()
            with Stage(r"copy", r"DMI_Waves_Firmware_13_7 v13.7.113.401", prog_num=6376):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6377) as should_copy_source_520_6377:  # 0m:0.001s
                    should_copy_source_520_6377()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", prog_num=6378):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r".", prog_num=6379) as copy_file_to_dir_521_6379:  # 0m:0.000s
                            copy_file_to_dir_521_6379()
                        with ChmodAndChown(path=r"IO_13.7_DigicoDMI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6380) as chmod_and_chown_522_6380:  # 0m:0.000s
                            chmod_and_chown_522_6380()
            with Stage(r"copy", r"DN32_WSG_Firmware_13_4 v13.4.0.205", prog_num=6381):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6382) as should_copy_source_523_6382:  # 0m:0.001s
                    should_copy_source_523_6382()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", prog_num=6383):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r".", prog_num=6384) as copy_file_to_dir_524_6384:  # 0m:0.000s
                            copy_file_to_dir_524_6384()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG_DN32.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6385) as chmod_and_chown_525_6385:  # 0m:0.000s
                            chmod_and_chown_525_6385()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_13_6 v13.6.12.288", prog_num=6386):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6387) as should_copy_source_526_6387:  # 0m:0.001s
                    should_copy_source_526_6387()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", prog_num=6388):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r".", prog_num=6389) as copy_file_to_dir_527_6389:  # 0m:0.000s
                            copy_file_to_dir_527_6389()
                        with ChmodAndChown(path=r"IO_13.6_Dspro_sg1k.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6390) as chmod_and_chown_528_6390:  # 0m:0.000s
                            chmod_and_chown_528_6390()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_14_25 v14.25.55.616", prog_num=6391):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6392) as should_copy_source_529_6392:  # 0m:0.001s
                    should_copy_source_529_6392()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", prog_num=6393):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r".", prog_num=6394) as copy_file_to_dir_530_6394:  # 0m:0.000s
                            copy_file_to_dir_530_6394()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg1k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6395) as chmod_and_chown_531_6395:  # 0m:0.000s
                            chmod_and_chown_531_6395()
            with Stage(r"copy", r"DSPro_SG1000_micro_Firmware_15_1 v15.1.2.45", prog_num=6396):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6397) as should_copy_source_532_6397:  # 0m:0.001s
                    should_copy_source_532_6397()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", prog_num=6398):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r".", prog_num=6399) as copy_file_to_dir_533_6399:  # 0m:0.000s
                            copy_file_to_dir_533_6399()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6400) as chmod_and_chown_534_6400:  # 0m:0.000s
                            chmod_and_chown_534_6400()
            with Stage(r"copy", r"DSPro_SG1000_micro_V2_Firmware_15_1 v15.1.2.45", prog_num=6401):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6402) as should_copy_source_535_6402:  # 0m:0.001s
                    should_copy_source_535_6402()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", prog_num=6403):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r".", prog_num=6404) as copy_file_to_dir_536_6404:  # 0m:0.000s
                            copy_file_to_dir_536_6404()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6405) as chmod_and_chown_537_6405:  # 0m:0.000s
                            chmod_and_chown_537_6405()
            with Stage(r"copy", r"DSPro SG4000 Firmware v13.5.0.227", prog_num=6406):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6407) as should_copy_source_538_6407:  # 0m:0.001s
                    should_copy_source_538_6407()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", prog_num=6408):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r".", prog_num=6409) as copy_file_to_dir_539_6409:  # 0m:0.000s
                            copy_file_to_dir_539_6409()
                        with ChmodAndChown(path=r"IO_13.5_Dspro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6410) as chmod_and_chown_540_6410:  # 0m:0.000s
                            chmod_and_chown_540_6410()
            with Stage(r"copy", r"DSPro SG4000 v2 Firmware v14.26.30.647", prog_num=6411):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6412) as should_copy_source_541_6412:  # 0m:0.001s
                    should_copy_source_541_6412()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", prog_num=6413):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r".", prog_num=6414) as copy_file_to_dir_542_6414:  # 0m:0.000s
                            copy_file_to_dir_542_6414()
                        with ChmodAndChown(path=r"IO_14.26_Dspro_sg4k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6415) as chmod_and_chown_543_6415:  # 0m:0.000s
                            chmod_and_chown_543_6415()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware V14.25 v14.25.55.616", prog_num=6416):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6417) as should_copy_source_544_6417:  # 0m:0.001s
                    should_copy_source_544_6417()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", prog_num=6418):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r".", prog_num=6419) as copy_file_to_dir_545_6419:  # 0m:0.000s
                            copy_file_to_dir_545_6419()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6420) as chmod_and_chown_546_6420:  # 0m:0.000s
                            chmod_and_chown_546_6420()
            with Stage(r"copy", r"DSPro SG4000 micro Firmware v15.2.25.98", prog_num=6421):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6422) as should_copy_source_547_6422:  # 0m:0.001s
                    should_copy_source_547_6422()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", prog_num=6423):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r".", prog_num=6424) as copy_file_to_dir_548_6424:  # 0m:0.000s
                            copy_file_to_dir_548_6424()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6425) as chmod_and_chown_549_6425:  # 0m:0.000s
                            chmod_and_chown_549_6425()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware v15.2.25.98", prog_num=6426):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6427) as should_copy_source_550_6427:  # 0m:0.001s
                    should_copy_source_550_6427()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", prog_num=6428):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r".", prog_num=6429) as copy_file_to_dir_551_6429:  # 0m:0.000s
                            copy_file_to_dir_551_6429()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6430) as chmod_and_chown_552_6430:  # 0m:0.000s
                            chmod_and_chown_552_6430()
            with Stage(r"copy", r"DiGiGrid D Firmware V13.4 v13.4.0.205", prog_num=6431):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6432) as should_copy_source_553_6432:  # 0m:0.001s
                    should_copy_source_553_6432()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", prog_num=6433):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r".", prog_num=6434) as copy_file_to_dir_554_6434:  # 0m:0.000s
                            copy_file_to_dir_554_6434()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridD.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6435) as chmod_and_chown_555_6435:  # 0m:0.000s
                            chmod_and_chown_555_6435()
            with Stage(r"copy", r"DiGiGrid_M_Driver_Firmware_13_4 v13.4.0.205", prog_num=6436):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6437) as should_copy_source_556_6437:  # 0m:0.001s
                    should_copy_source_556_6437()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", prog_num=6438):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r".", prog_num=6439) as copy_file_to_dir_557_6439:  # 0m:0.000s
                            copy_file_to_dir_557_6439()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridM.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6440) as chmod_and_chown_558_6440:  # 0m:0.000s
                            chmod_and_chown_558_6440()
            with Stage(r"copy", r"DiGiGrid Q Firmware V13.4 v13.4.0.205", prog_num=6441):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6442) as should_copy_source_559_6442:  # 0m:0.001s
                    should_copy_source_559_6442()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", prog_num=6443):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r".", prog_num=6444) as copy_file_to_dir_560_6444:  # 0m:0.000s
                            copy_file_to_dir_560_6444()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridQ.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6445) as chmod_and_chown_561_6445:  # 0m:0.000s
                            chmod_and_chown_561_6445()
            with Stage(r"copy", r"Digico SD card V13.4 v13.4.0.205", prog_num=6446):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6447) as should_copy_source_562_6447:  # 0m:0.001s
                    should_copy_source_562_6447()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", prog_num=6448):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r".", prog_num=6449) as copy_file_to_dir_563_6449:  # 0m:0.000s
                            copy_file_to_dir_563_6449()
                        with ChmodAndChown(path=r"IO_13.4_DigiCo_t2_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6450) as chmod_and_chown_564_6450:  # 0m:0.000s
                            chmod_and_chown_564_6450()
            with Stage(r"copy", r"Digico SD Firmware v14.21.36.492", prog_num=6451):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6452) as should_copy_source_565_6452:  # 0m:0.001s
                    should_copy_source_565_6452()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", prog_num=6453):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r".", prog_num=6454) as copy_file_to_dir_566_6454:  # 0m:0.000s
                            copy_file_to_dir_566_6454()
                        with ChmodAndChown(path=r"IO_14.21_Digico_SD_S6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6455) as chmod_and_chown_567_6455:  # 0m:0.000s
                            chmod_and_chown_567_6455()
            with Stage(r"copy", r"DirectOut Exbox Micro SoundGrid I/O Driver Firmware v14.22.9.506", prog_num=6456):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6457) as should_copy_source_568_6457:  # 0m:0.001s
                    should_copy_source_568_6457()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", prog_num=6458):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r".", prog_num=6459) as copy_file_to_dir_569_6459:  # 0m:0.000s
                            copy_file_to_dir_569_6459()
                        with ChmodAndChown(path=r"IO_14.22_DirectOut_Ex_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6460) as chmod_and_chown_570_6460:  # 0m:0.000s
                            chmod_and_chown_570_6460()
            with Stage(r"copy", r"DirectOut Exbox v2 SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=6461):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6462) as should_copy_source_571_6462:  # 0m:0.001s
                    should_copy_source_571_6462()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", prog_num=6463):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r".", prog_num=6464) as copy_file_to_dir_572_6464:  # 0m:0.000s
                            copy_file_to_dir_572_6464()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6465) as chmod_and_chown_573_6465:  # 0m:0.000s
                            chmod_and_chown_573_6465()
            with Stage(r"copy", r"DirectOut Exbox v2 Micro SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=6466):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6467) as should_copy_source_574_6467:  # 0m:0.001s
                    should_copy_source_574_6467()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", prog_num=6468):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r".", prog_num=6469) as copy_file_to_dir_575_6469:  # 0m:0.000s
                            copy_file_to_dir_575_6469()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6470) as chmod_and_chown_576_6470:  # 0m:0.000s
                            chmod_and_chown_576_6470()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=6471):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6472) as should_copy_source_577_6472:  # 0m:0.001s
                    should_copy_source_577_6472()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", prog_num=6473):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r".", prog_num=6474) as copy_file_to_dir_578_6474:  # 0m:0.000s
                            copy_file_to_dir_578_6474()
                        with ChmodAndChown(path=r"IO_14.18_DirectOut_Ex.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6475) as chmod_and_chown_579_6475:  # 0m:0.000s
                            chmod_and_chown_579_6475()
            with Stage(r"copy", r"DirectOut_SG_MADI_Firmware_13_4 v13.4.0.205", prog_num=6476):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6477) as should_copy_source_580_6477:  # 0m:0.001s
                    should_copy_source_580_6477()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", prog_num=6478):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r".", prog_num=6479) as copy_file_to_dir_581_6479:  # 0m:0.000s
                            copy_file_to_dir_581_6479()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6480) as chmod_and_chown_582_6480:  # 0m:0.000s
                            chmod_and_chown_582_6480()
            with Stage(r"copy", r"DirectOut_SG_MADI_micro_Firmware_13_4 v13.4.0.205", prog_num=6481):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6482) as should_copy_source_583_6482:  # 0m:0.001s
                    should_copy_source_583_6482()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", prog_num=6483):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r".", prog_num=6484) as copy_file_to_dir_584_6484:  # 0m:0.000s
                            copy_file_to_dir_584_6484()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6485) as chmod_and_chown_585_6485:  # 0m:0.000s
                            chmod_and_chown_585_6485()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=6486):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6487) as should_copy_source_586_6487:  # 0m:0.001s
                    should_copy_source_586_6487()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", prog_num=6488):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r".", prog_num=6489) as copy_file_to_dir_587_6489:  # 0m:0.000s
                            copy_file_to_dir_587_6489()
                        with ChmodAndChown(path=r"IO_14.18_Directout_sgio.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6490) as chmod_and_chown_588_6490:  # 0m:0.000s
                            chmod_and_chown_588_6490()
            with Stage(r"copy", r"HearBack Pro Firmware v13.7.33.321", prog_num=6491):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6492) as should_copy_source_589_6492:  # 0m:0.001s
                    should_copy_source_589_6492()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", prog_num=6493):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r".", prog_num=6494) as copy_file_to_dir_590_6494:  # 0m:0.000s
                            copy_file_to_dir_590_6494()
                        with ChmodAndChown(path=r"IO_13.7_Heartech.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6495) as chmod_and_chown_591_6495:  # 0m:0.000s
                            chmod_and_chown_591_6495()
            with Stage(r"copy", r"HearBack Pro V2 Firmware v13.7.118.406", prog_num=6496):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6497) as should_copy_source_592_6497:  # 0m:0.001s
                    should_copy_source_592_6497()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", prog_num=6498):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r".", prog_num=6499) as copy_file_to_dir_593_6499:  # 0m:0.000s
                            copy_file_to_dir_593_6499()
                        with ChmodAndChown(path=r"IO_13.7_Heartech_32ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6500) as chmod_and_chown_594_6500:  # 0m:0.000s
                            chmod_and_chown_594_6500()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v15.1.29.72", prog_num=6501):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6502) as should_copy_source_595_6502:  # 0m:0.001s
                    should_copy_source_595_6502()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", prog_num=6503):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r".", prog_num=6504) as copy_file_to_dir_596_6504:  # 0m:0.000s
                            copy_file_to_dir_596_6504()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6505) as chmod_and_chown_597_6505:  # 0m:0.000s
                            chmod_and_chown_597_6505()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v2 v15.1.29.72", prog_num=6506):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6507) as should_copy_source_598_6507:  # 0m:0.001s
                    should_copy_source_598_6507()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", prog_num=6508):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r".", prog_num=6509) as copy_file_to_dir_599_6509:  # 0m:0.000s
                            copy_file_to_dir_599_6509()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6510) as chmod_and_chown_600_6510:  # 0m:0.000s
                            chmod_and_chown_600_6510()
            with Stage(r"copy", r"DigiGrid IOC Firmware v13.4.0.205", prog_num=6511):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6512) as should_copy_source_601_6512:  # 0m:0.001s
                    should_copy_source_601_6512()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", prog_num=6513):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r".", prog_num=6514) as copy_file_to_dir_602_6514:  # 0m:0.000s
                            copy_file_to_dir_602_6514()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6515) as chmod_and_chown_603_6515:  # 0m:0.000s
                            chmod_and_chown_603_6515()
            with Stage(r"copy", r"DigiGrid IOC micro Firmware v13.4.0.205", prog_num=6516):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6517) as should_copy_source_604_6517:  # 0m:0.001s
                    should_copy_source_604_6517()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", prog_num=6518):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r".", prog_num=6519) as copy_file_to_dir_605_6519:  # 0m:0.000s
                            copy_file_to_dir_605_6519()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6520) as chmod_and_chown_606_6520:  # 0m:0.000s
                            chmod_and_chown_606_6520()
            with Stage(r"copy", r"IONIC16_Firmware_S25 v14.29.19.700", prog_num=6521):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6522) as should_copy_source_607_6522:  # 0m:0.001s
                    should_copy_source_607_6522()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", prog_num=6523):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r".", prog_num=6524) as copy_file_to_dir_608_6524:  # 0m:0.000s
                            copy_file_to_dir_608_6524()
                        with ChmodAndChown(path=r"IO_14.29_IONIC16_S25.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6525) as chmod_and_chown_609_6525:  # 0m:0.000s
                            chmod_and_chown_609_6525()
            with Stage(r"copy", r"IONIC16_Firmware_S50 v14.30.5.713", prog_num=6526):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6527) as should_copy_source_610_6527:  # 0m:0.001s
                    should_copy_source_610_6527()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", prog_num=6528):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r".", prog_num=6529) as copy_file_to_dir_611_6529:  # 0m:0.000s
                            copy_file_to_dir_611_6529()
                        with ChmodAndChown(path=r"IO_14.30_IONIC16_S50.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6530) as chmod_and_chown_612_6530:  # 0m:0.000s
                            chmod_and_chown_612_6530()
            with Stage(r"copy", r"DigiGrid IOS Firmware v13.4.0.205", prog_num=6531):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6532) as should_copy_source_613_6532:  # 0m:0.001s
                    should_copy_source_613_6532()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", prog_num=6533):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r".", prog_num=6534) as copy_file_to_dir_614_6534:  # 0m:0.000s
                            copy_file_to_dir_614_6534()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6535) as chmod_and_chown_615_6535:  # 0m:0.000s
                            chmod_and_chown_615_6535()
            with Stage(r"copy", r"DigiGrid IOS-XL Firmware v13.4.0.205", prog_num=6536):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6537) as should_copy_source_616_6537:  # 0m:0.001s
                    should_copy_source_616_6537()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", prog_num=6538):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r".", prog_num=6539) as copy_file_to_dir_617_6539:  # 0m:0.000s
                            copy_file_to_dir_617_6539()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6540) as chmod_and_chown_618_6540:  # 0m:0.000s
                            chmod_and_chown_618_6540()
            with Stage(r"copy", r"DigiGrid IOS-XL micro Firmware v13.4.0.205", prog_num=6541):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6542) as should_copy_source_619_6542:  # 0m:0.001s
                    should_copy_source_619_6542()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", prog_num=6543):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r".", prog_num=6544) as copy_file_to_dir_620_6544:  # 0m:0.000s
                            copy_file_to_dir_620_6544()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6545) as chmod_and_chown_621_6545:  # 0m:0.000s
                            chmod_and_chown_621_6545()
            with Stage(r"copy", r"DigiGrid IOS micro Firmware v13.4.0.205", prog_num=6546):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6547) as should_copy_source_622_6547:  # 0m:0.001s
                    should_copy_source_622_6547()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", prog_num=6548):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r".", prog_num=6549) as copy_file_to_dir_623_6549:  # 0m:0.000s
                            copy_file_to_dir_623_6549()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6550) as chmod_and_chown_624_6550:  # 0m:0.000s
                            chmod_and_chown_624_6550()
            with Stage(r"copy", r"DigiGrid IOX Firmware v13.4.0.205", prog_num=6551):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6552) as should_copy_source_625_6552:  # 0m:0.001s
                    should_copy_source_625_6552()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", prog_num=6553):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r".", prog_num=6554) as copy_file_to_dir_626_6554:  # 0m:0.000s
                            copy_file_to_dir_626_6554()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6555) as chmod_and_chown_627_6555:  # 0m:0.000s
                            chmod_and_chown_627_6555()
            with Stage(r"copy", r"DigiGrid IOX micro Firmware v13.4.0.205", prog_num=6556):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6557) as should_copy_source_628_6557:  # 0m:0.001s
                    should_copy_source_628_6557()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", prog_num=6558):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r".", prog_num=6559) as copy_file_to_dir_629_6559:  # 0m:0.000s
                            copy_file_to_dir_629_6559()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6560) as chmod_and_chown_630_6560:  # 0m:0.000s
                            chmod_and_chown_630_6560()
            with Stage(r"copy", r"JoeCo_Firmware_13_4 v13.4.0.205", prog_num=6561):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6562) as should_copy_source_631_6562:  # 0m:0.001s
                    should_copy_source_631_6562()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", prog_num=6563):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r".", prog_num=6564) as copy_file_to_dir_632_6564:  # 0m:0.000s
                            copy_file_to_dir_632_6564()
                        with ChmodAndChown(path=r"IO_13.4_Joeco.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6565) as chmod_and_chown_633_6565:  # 0m:0.000s
                            chmod_and_chown_633_6565()
            with Stage(r"copy", r"DigiGrid MGB Firmware v13.4.0.205", prog_num=6566):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6567) as should_copy_source_634_6567:  # 0m:0.001s
                    should_copy_source_634_6567()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", prog_num=6568):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r".", prog_num=6569) as copy_file_to_dir_635_6569:  # 0m:0.000s
                            copy_file_to_dir_635_6569()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6570) as chmod_and_chown_636_6570:  # 0m:0.000s
                            chmod_and_chown_636_6570()
            with Stage(r"copy", r"DigiGrid MGO Firmware v13.4.0.205", prog_num=6571):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6572) as should_copy_source_637_6572:  # 0m:0.001s
                    should_copy_source_637_6572()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", prog_num=6573):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r".", prog_num=6574) as copy_file_to_dir_638_6574:  # 0m:0.000s
                            copy_file_to_dir_638_6574()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGO.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6575) as chmod_and_chown_639_6575:  # 0m:0.000s
                            chmod_and_chown_639_6575()
            with Stage(r"copy", r"SoundStudio STG-1608 Firmware v13.4.0.205", prog_num=6576):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6577) as should_copy_source_640_6577:  # 0m:0.001s
                    should_copy_source_640_6577()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", prog_num=6578):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r".", prog_num=6579) as copy_file_to_dir_641_6579:  # 0m:0.000s
                            copy_file_to_dir_641_6579()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6580) as chmod_and_chown_642_6580:  # 0m:0.000s
                            chmod_and_chown_642_6580()
            with Stage(r"copy", r"SoundStudio STG-1608 micro Firmware V13.4 v13.4.0.205", prog_num=6581):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6582) as should_copy_source_643_6582:  # 0m:0.001s
                    should_copy_source_643_6582()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", prog_num=6583):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r".", prog_num=6584) as copy_file_to_dir_644_6584:  # 0m:0.000s
                            copy_file_to_dir_644_6584()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6585) as chmod_and_chown_645_6585:  # 0m:0.000s
                            chmod_and_chown_645_6585()
            with Stage(r"copy", r"SoundStudio STG-2412 Firmware v13.4.0.205", prog_num=6586):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6587) as should_copy_source_646_6587:  # 0m:0.001s
                    should_copy_source_646_6587()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", prog_num=6588):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r".", prog_num=6589) as copy_file_to_dir_647_6589:  # 0m:0.000s
                            copy_file_to_dir_647_6589()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6590) as chmod_and_chown_648_6590:  # 0m:0.000s
                            chmod_and_chown_648_6590()
            with Stage(r"copy", r"SoundStudio STG-2412 micro Firmware V13.4 v13.4.0.205", prog_num=6591):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6592) as should_copy_source_649_6592:  # 0m:0.001s
                    should_copy_source_649_6592()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", prog_num=6593):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r".", prog_num=6594) as copy_file_to_dir_650_6594:  # 0m:0.000s
                            copy_file_to_dir_650_6594()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6595) as chmod_and_chown_651_6595:  # 0m:0.000s
                            chmod_and_chown_651_6595()
            with Stage(r"copy", r"X-WSG_s6_Firmware_13_4 v13.4.0.205", prog_num=6596):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6597) as should_copy_source_652_6597:  # 0m:0.001s
                    should_copy_source_652_6597()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", prog_num=6598):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r".", prog_num=6599) as copy_file_to_dir_653_6599:  # 0m:0.000s
                            copy_file_to_dir_653_6599()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6600) as chmod_and_chown_654_6600:  # 0m:0.000s
                            chmod_and_chown_654_6600()
            with Stage(r"copy", r"WSG Y-16 s3 Firmware v13.4.0.205", prog_num=6601):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6602) as should_copy_source_655_6602:  # 0m:0.001s
                    should_copy_source_655_6602()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", prog_num=6603):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r".", prog_num=6604) as copy_file_to_dir_656_6604:  # 0m:0.000s
                            copy_file_to_dir_656_6604()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6605) as chmod_and_chown_657_6605:  # 0m:0.000s
                            chmod_and_chown_657_6605()
            with Stage(r"copy", r"WSG Y-16 s6 Firmware v13.4.0.205", prog_num=6606):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6607) as should_copy_source_658_6607:  # 0m:0.001s
                    should_copy_source_658_6607()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", prog_num=6608):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r".", prog_num=6609) as copy_file_to_dir_659_6609:  # 0m:0.000s
                            copy_file_to_dir_659_6609()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6610) as chmod_and_chown_660_6610:  # 0m:0.000s
                            chmod_and_chown_660_6610()
            with Stage(r"copy", r"WSG Y-16 v3 Firmware v14.21.16.472", prog_num=6611):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6612) as should_copy_source_661_6612:  # 0m:0.001s
                    should_copy_source_661_6612()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", prog_num=6613):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r".", prog_num=6614) as copy_file_to_dir_662_6614:  # 0m:0.000s
                            copy_file_to_dir_662_6614()
                        with ChmodAndChown(path=r"IO_14.21_MY16_v3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6615) as chmod_and_chown_663_6615:  # 0m:0.000s
                            chmod_and_chown_663_6615()
            with Stage(r"copy", r"Yamaha HY128 v2 Firmware v14.13.43.386", prog_num=6616):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6617) as should_copy_source_664_6617:  # 0m:0.001s
                    should_copy_source_664_6617()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", prog_num=6618):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r".", prog_num=6619) as copy_file_to_dir_665_6619:  # 0m:0.000s
                            copy_file_to_dir_665_6619()
                        with ChmodAndChown(path=r"IO_14.13_HY_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6620) as chmod_and_chown_666_6620:  # 0m:0.000s
                            chmod_and_chown_666_6620()
            with Stage(r"copy", r"Yamaha WSG-HY128 Firmware v13.4.0.205", prog_num=6621):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=6622) as should_copy_source_667_6622:  # 0m:0.001s
                    should_copy_source_667_6622()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", prog_num=6623):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r".", prog_num=6624) as copy_file_to_dir_668_6624:  # 0m:0.000s
                            copy_file_to_dir_668_6624()
                        with ChmodAndChown(path=r"IO_13.4_Hy.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=6625) as chmod_and_chown_669_6625:  # 0m:0.000s
                            chmod_and_chown_669_6625()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=6626) as cd_stage_670_6626:  # 0m:0.548s
            cd_stage_670_6626()
            with Stage(r"copy", r"SoundGrid Server Firmware v14.26.104.721", prog_num=6627):  # 0m:0.548s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", skip_progress_count=2, prog_num=6628) as should_copy_source_671_6628:  # 0m:0.548s
                    should_copy_source_671_6628()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", prog_num=6629):  # 0m:0.548s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi.wtar.aa", where_to_unwtar=r".", prog_num=6630) as unwtar_672_6630:  # 0m:0.548s
                            unwtar_672_6630()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=6631) as cd_stage_673_6631:  # 0m:8.318s
            cd_stage_673_6631()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=6632) as rm_file_or_dir_674_6632:  # 0m:0.000s
                rm_file_or_dir_674_6632()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=6633) as rm_file_or_dir_675_6633:  # 0m:0.000s
                rm_file_or_dir_675_6633()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.app", prog_num=6634) as rm_file_or_dir_676_6634:  # 0m:0.000s
                rm_file_or_dir_676_6634()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.bundle", prog_num=6635) as rm_file_or_dir_677_6635:  # 0m:0.000s
                rm_file_or_dir_677_6635()
            with Stage(r"copy", r"Apogee Symphony MKII Control Panel v14.0.342.343", prog_num=6636):  # 0m:0.507s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6637) as should_copy_source_678_6637:  # 0m:0.402s
                    should_copy_source_678_6637()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.app", prog_num=6638):  # 0m:0.402s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r".", delete_extraneous_files=True, prog_num=6639) as copy_dir_to_dir_679_6639:  # 0m:0.001s
                            copy_dir_to_dir_679_6639()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", where_to_unwtar=r".", prog_num=6640) as unwtar_680_6640:  # 0m:0.400s
                            unwtar_680_6640()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.app", user_id=-1, group_id=-1, prog_num=6641, recursive=True) as chown_681_6641:  # 0m:0.000s
                            chown_681_6641()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6642) as should_copy_source_682_6642:  # 0m:0.105s
                    should_copy_source_682_6642()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.bundle", prog_num=6643):  # 0m:0.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r".", delete_extraneous_files=True, prog_num=6644) as copy_dir_to_dir_683_6644:  # 0m:0.002s
                            copy_dir_to_dir_683_6644()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", where_to_unwtar=r".", prog_num=6645) as unwtar_684_6645:  # 0m:0.103s
                            unwtar_684_6645()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.bundle", user_id=-1, group_id=-1, prog_num=6646, recursive=True) as chown_685_6646:  # 0m:0.000s
                            chown_685_6646()
            with Stage(r"copy", r"SoundGrid BR-1 Control Panel v14.0.342.343", prog_num=6647):  # 0m:0.183s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6648) as should_copy_source_686_6648:  # 0m:0.114s
                    should_copy_source_686_6648()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.app", prog_num=6649):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r".", delete_extraneous_files=True, prog_num=6650) as copy_dir_to_dir_687_6650:  # 0m:0.002s
                            copy_dir_to_dir_687_6650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", where_to_unwtar=r".", prog_num=6651) as unwtar_688_6651:  # 0m:0.112s
                            unwtar_688_6651()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.app", user_id=-1, group_id=-1, prog_num=6652, recursive=True) as chown_689_6652:  # 0m:0.000s
                            chown_689_6652()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6653) as should_copy_source_690_6653:  # 0m:0.068s
                    should_copy_source_690_6653()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", prog_num=6654):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r".", delete_extraneous_files=True, prog_num=6655) as copy_dir_to_dir_691_6655:  # 0m:0.002s
                            copy_dir_to_dir_691_6655()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", where_to_unwtar=r".", prog_num=6656) as unwtar_692_6656:  # 0m:0.066s
                            unwtar_692_6656()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.bundle", user_id=-1, group_id=-1, prog_num=6657, recursive=True) as chown_693_6657:  # 0m:0.000s
                            chown_693_6657()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Control Panel v14.0.436.437", prog_num=6658):  # 0m:0.181s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6659) as should_copy_source_694_6659:  # 0m:0.110s
                    should_copy_source_694_6659()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", prog_num=6660):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r".", delete_extraneous_files=True, prog_num=6661) as copy_dir_to_dir_695_6661:  # 0m:0.002s
                            copy_dir_to_dir_695_6661()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", where_to_unwtar=r".", prog_num=6662) as unwtar_696_6662:  # 0m:0.108s
                            unwtar_696_6662()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.app", user_id=-1, group_id=-1, prog_num=6663, recursive=True) as chown_697_6663:  # 0m:0.000s
                            chown_697_6663()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6664) as should_copy_source_698_6664:  # 0m:0.071s
                    should_copy_source_698_6664()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", prog_num=6665):  # 0m:0.070s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r".", delete_extraneous_files=True, prog_num=6666) as copy_dir_to_dir_699_6666:  # 0m:0.001s
                            copy_dir_to_dir_699_6666()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", where_to_unwtar=r".", prog_num=6667) as unwtar_700_6667:  # 0m:0.069s
                            unwtar_700_6667()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.bundle", user_id=-1, group_id=-1, prog_num=6668, recursive=True) as chown_701_6668:  # 0m:0.000s
                            chown_701_6668()
            with Stage(r"copy", r"BMB4 SoundGrid MotherBoard Control Panel v14.0.342.343", prog_num=6669):  # 0m:0.165s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6670) as should_copy_source_702_6670:  # 0m:0.102s
                    should_copy_source_702_6670()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", prog_num=6671):  # 0m:0.102s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r".", delete_extraneous_files=True, prog_num=6672) as copy_dir_to_dir_703_6672:  # 0m:0.002s
                            copy_dir_to_dir_703_6672()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", where_to_unwtar=r".", prog_num=6673) as unwtar_704_6673:  # 0m:0.100s
                            unwtar_704_6673()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.app", user_id=-1, group_id=-1, prog_num=6674, recursive=True) as chown_705_6674:  # 0m:0.000s
                            chown_705_6674()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6675) as should_copy_source_706_6675:  # 0m:0.063s
                    should_copy_source_706_6675()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", prog_num=6676):  # 0m:0.063s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r".", delete_extraneous_files=True, prog_num=6677) as copy_dir_to_dir_707_6677:  # 0m:0.001s
                            copy_dir_to_dir_707_6677()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", where_to_unwtar=r".", prog_num=6678) as unwtar_708_6678:  # 0m:0.061s
                            unwtar_708_6678()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.bundle", user_id=-1, group_id=-1, prog_num=6679, recursive=True) as chown_709_6679:  # 0m:0.000s
                            chown_709_6679()
            with Stage(r"copy", r"Cadac Control Panel v14.0.342.343", prog_num=6680):  # 0m:0.060s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6681) as should_copy_source_710_6681:  # 0m:0.060s
                    should_copy_source_710_6681()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Cadac Control.bundle", prog_num=6682):  # 0m:0.060s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r".", delete_extraneous_files=True, prog_num=6683) as copy_dir_to_dir_711_6683:  # 0m:0.001s
                            copy_dir_to_dir_711_6683()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", where_to_unwtar=r".", prog_num=6684) as unwtar_712_6684:  # 0m:0.058s
                            unwtar_712_6684()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control.bundle", user_id=-1, group_id=-1, prog_num=6685, recursive=True) as chown_713_6685:  # 0m:0.000s
                            chown_713_6685()
            with Stage(r"copy", r"Calrec Control Panel v14.0.342.343", prog_num=6686):  # 0m:0.057s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6687) as should_copy_source_714_6687:  # 0m:0.057s
                    should_copy_source_714_6687()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Calrec Control.bundle", prog_num=6688):  # 0m:0.056s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r".", delete_extraneous_files=True, prog_num=6689) as copy_dir_to_dir_715_6689:  # 0m:0.001s
                            copy_dir_to_dir_715_6689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", where_to_unwtar=r".", prog_num=6690) as unwtar_716_6690:  # 0m:0.055s
                            unwtar_716_6690()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control.bundle", user_id=-1, group_id=-1, prog_num=6691, recursive=True) as chown_717_6691:  # 0m:0.000s
                            chown_717_6691()
            with Stage(r"copy", r"Crest Audio Tactus Control Panel v14.0.342.343", prog_num=6692):  # 0m:0.231s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6693) as should_copy_source_718_6693:  # 0m:0.157s
                    should_copy_source_718_6693()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", prog_num=6694):  # 0m:0.157s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r".", delete_extraneous_files=True, prog_num=6695) as copy_dir_to_dir_719_6695:  # 0m:0.002s
                            copy_dir_to_dir_719_6695()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", where_to_unwtar=r".", prog_num=6696) as unwtar_720_6696:  # 0m:0.155s
                            unwtar_720_6696()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.app", user_id=-1, group_id=-1, prog_num=6697, recursive=True) as chown_721_6697:  # 0m:0.000s
                            chown_721_6697()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6698) as should_copy_source_722_6698:  # 0m:0.074s
                    should_copy_source_722_6698()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", prog_num=6699):  # 0m:0.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r".", delete_extraneous_files=True, prog_num=6700) as copy_dir_to_dir_723_6700:  # 0m:0.001s
                            copy_dir_to_dir_723_6700()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", where_to_unwtar=r".", prog_num=6701) as unwtar_724_6701:  # 0m:0.072s
                            unwtar_724_6701()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.bundle", user_id=-1, group_id=-1, prog_num=6702, recursive=True) as chown_725_6702:  # 0m:0.000s
                            chown_725_6702()
            with Stage(r"copy", r"DigiGrid DLI/DLS Control Panel v14.0.342.343", prog_num=6703):  # 0m:0.508s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6704) as should_copy_source_726_6704:  # 0m:0.373s
                    should_copy_source_726_6704()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", prog_num=6705):  # 0m:0.372s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r".", delete_extraneous_files=True, prog_num=6706) as copy_dir_to_dir_727_6706:  # 0m:0.001s
                            copy_dir_to_dir_727_6706()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", where_to_unwtar=r".", prog_num=6707) as unwtar_728_6707:  # 0m:0.370s
                            unwtar_728_6707()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.app", user_id=-1, group_id=-1, prog_num=6708, recursive=True) as chown_729_6708:  # 0m:0.000s
                            chown_729_6708()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6709) as should_copy_source_730_6709:  # 0m:0.135s
                    should_copy_source_730_6709()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", prog_num=6710):  # 0m:0.135s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r".", delete_extraneous_files=True, prog_num=6711) as copy_dir_to_dir_731_6711:  # 0m:0.001s
                            copy_dir_to_dir_731_6711()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", where_to_unwtar=r".", prog_num=6712) as unwtar_732_6712:  # 0m:0.133s
                            unwtar_732_6712()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.bundle", user_id=-1, group_id=-1, prog_num=6713, recursive=True) as chown_733_6713:  # 0m:0.000s
                            chown_733_6713()
            with Stage(r"copy", r"DMI Waves Control Panel v14.0.342.343", prog_num=6714):  # 0m:0.152s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6715) as should_copy_source_734_6715:  # 0m:0.092s
                    should_copy_source_734_6715()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.app", prog_num=6716):  # 0m:0.092s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r".", delete_extraneous_files=True, prog_num=6717) as copy_dir_to_dir_735_6717:  # 0m:0.002s
                            copy_dir_to_dir_735_6717()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", where_to_unwtar=r".", prog_num=6718) as unwtar_736_6718:  # 0m:0.090s
                            unwtar_736_6718()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.app", user_id=-1, group_id=-1, prog_num=6719, recursive=True) as chown_737_6719:  # 0m:0.000s
                            chown_737_6719()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6720) as should_copy_source_738_6720:  # 0m:0.060s
                    should_copy_source_738_6720()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.bundle", prog_num=6721):  # 0m:0.060s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r".", delete_extraneous_files=True, prog_num=6722) as copy_dir_to_dir_739_6722:  # 0m:0.001s
                            copy_dir_to_dir_739_6722()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", where_to_unwtar=r".", prog_num=6723) as unwtar_740_6723:  # 0m:0.058s
                            unwtar_740_6723()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.bundle", user_id=-1, group_id=-1, prog_num=6724, recursive=True) as chown_741_6724:  # 0m:0.000s
                            chown_741_6724()
            with Stage(r"copy", r"DN32-WSG Control Panel v14.0.342.343", prog_num=6725):  # 0m:0.181s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6726) as should_copy_source_742_6726:  # 0m:0.114s
                    should_copy_source_742_6726()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", prog_num=6727):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r".", delete_extraneous_files=True, prog_num=6728) as copy_dir_to_dir_743_6728:  # 0m:0.001s
                            copy_dir_to_dir_743_6728()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", where_to_unwtar=r".", prog_num=6729) as unwtar_744_6729:  # 0m:0.112s
                            unwtar_744_6729()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.app", user_id=-1, group_id=-1, prog_num=6730, recursive=True) as chown_745_6730:  # 0m:0.000s
                            chown_745_6730()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6731) as should_copy_source_746_6731:  # 0m:0.067s
                    should_copy_source_746_6731()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", prog_num=6732):  # 0m:0.067s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=6733) as copy_dir_to_dir_747_6733:  # 0m:0.001s
                            copy_dir_to_dir_747_6733()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", where_to_unwtar=r".", prog_num=6734) as unwtar_748_6734:  # 0m:0.065s
                            unwtar_748_6734()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=6735, recursive=True) as chown_749_6735:  # 0m:0.000s
                            chown_749_6735()
            with Stage(r"copy", r"DSPro SG4000 / SG1000 Control Panel v14.0.342.343", prog_num=6736):  # 0m:0.266s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6737) as should_copy_source_750_6737:  # 0m:0.190s
                    should_copy_source_750_6737()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", prog_num=6738):  # 0m:0.190s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r".", delete_extraneous_files=True, prog_num=6739) as copy_dir_to_dir_751_6739:  # 0m:0.002s
                            copy_dir_to_dir_751_6739()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", where_to_unwtar=r".", prog_num=6740) as unwtar_752_6740:  # 0m:0.188s
                            unwtar_752_6740()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.app", user_id=-1, group_id=-1, prog_num=6741, recursive=True) as chown_753_6741:  # 0m:0.000s
                            chown_753_6741()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6742) as should_copy_source_754_6742:  # 0m:0.076s
                    should_copy_source_754_6742()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", prog_num=6743):  # 0m:0.075s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r".", delete_extraneous_files=True, prog_num=6744) as copy_dir_to_dir_755_6744:  # 0m:0.001s
                            copy_dir_to_dir_755_6744()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", where_to_unwtar=r".", prog_num=6745) as unwtar_756_6745:  # 0m:0.074s
                            unwtar_756_6745()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.bundle", user_id=-1, group_id=-1, prog_num=6746, recursive=True) as chown_757_6746:  # 0m:0.000s
                            chown_757_6746()
            with Stage(r"copy", r"DigiGrid D Control Panel v14.0.342.343", prog_num=6747):  # 0m:0.186s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6748) as should_copy_source_758_6748:  # 0m:0.120s
                    should_copy_source_758_6748()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", prog_num=6749):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r".", delete_extraneous_files=True, prog_num=6750) as copy_dir_to_dir_759_6750:  # 0m:0.001s
                            copy_dir_to_dir_759_6750()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", where_to_unwtar=r".", prog_num=6751) as unwtar_760_6751:  # 0m:0.118s
                            unwtar_760_6751()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.app", user_id=-1, group_id=-1, prog_num=6752, recursive=True) as chown_761_6752:  # 0m:0.000s
                            chown_761_6752()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6753) as should_copy_source_762_6753:  # 0m:0.065s
                    should_copy_source_762_6753()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", prog_num=6754):  # 0m:0.065s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r".", delete_extraneous_files=True, prog_num=6755) as copy_dir_to_dir_763_6755:  # 0m:0.001s
                            copy_dir_to_dir_763_6755()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", where_to_unwtar=r".", prog_num=6756) as unwtar_764_6756:  # 0m:0.064s
                            unwtar_764_6756()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.bundle", user_id=-1, group_id=-1, prog_num=6757, recursive=True) as chown_765_6757:  # 0m:0.000s
                            chown_765_6757()
            with Stage(r"copy", r"DigiGrid M Control Panel v$(ExternalVersion", prog_num=6758):  # 0m:0.189s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6759) as should_copy_source_766_6759:  # 0m:0.117s
                    should_copy_source_766_6759()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", prog_num=6760):  # 0m:0.117s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r".", delete_extraneous_files=True, prog_num=6761) as copy_dir_to_dir_767_6761:  # 0m:0.001s
                            copy_dir_to_dir_767_6761()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", where_to_unwtar=r".", prog_num=6762) as unwtar_768_6762:  # 0m:0.115s
                            unwtar_768_6762()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.app", user_id=-1, group_id=-1, prog_num=6763, recursive=True) as chown_769_6763:  # 0m:0.000s
                            chown_769_6763()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6764) as should_copy_source_770_6764:  # 0m:0.072s
                    should_copy_source_770_6764()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", prog_num=6765):  # 0m:0.072s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r".", delete_extraneous_files=True, prog_num=6766) as copy_dir_to_dir_771_6766:  # 0m:0.001s
                            copy_dir_to_dir_771_6766()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", where_to_unwtar=r".", prog_num=6767) as unwtar_772_6767:  # 0m:0.070s
                            unwtar_772_6767()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.bundle", user_id=-1, group_id=-1, prog_num=6768, recursive=True) as chown_773_6768:  # 0m:0.000s
                            chown_773_6768()
            with Stage(r"copy", r"DigiGrid Q Control Panel v14.0.342.343", prog_num=6769):  # 0m:0.217s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6770) as should_copy_source_774_6770:  # 0m:0.140s
                    should_copy_source_774_6770()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", prog_num=6771):  # 0m:0.140s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r".", delete_extraneous_files=True, prog_num=6772) as copy_dir_to_dir_775_6772:  # 0m:0.002s
                            copy_dir_to_dir_775_6772()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", where_to_unwtar=r".", prog_num=6773) as unwtar_776_6773:  # 0m:0.138s
                            unwtar_776_6773()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.app", user_id=-1, group_id=-1, prog_num=6774, recursive=True) as chown_777_6774:  # 0m:0.000s
                            chown_777_6774()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6775) as should_copy_source_778_6775:  # 0m:0.076s
                    should_copy_source_778_6775()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", prog_num=6776):  # 0m:0.076s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r".", delete_extraneous_files=True, prog_num=6777) as copy_dir_to_dir_779_6777:  # 0m:0.002s
                            copy_dir_to_dir_779_6777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", where_to_unwtar=r".", prog_num=6778) as unwtar_780_6778:  # 0m:0.074s
                            unwtar_780_6778()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.bundle", user_id=-1, group_id=-1, prog_num=6779, recursive=True) as chown_781_6779:  # 0m:0.000s
                            chown_781_6779()
            with Stage(r"copy", r"Digico SD Control Panel v14.0.7.8", prog_num=6780):  # 0m:0.155s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6781) as should_copy_source_782_6781:  # 0m:0.089s
                    should_copy_source_782_6781()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", prog_num=6782):  # 0m:0.089s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r".", delete_extraneous_files=True, prog_num=6783) as copy_dir_to_dir_783_6783:  # 0m:0.002s
                            copy_dir_to_dir_783_6783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", where_to_unwtar=r".", prog_num=6784) as unwtar_784_6784:  # 0m:0.087s
                            unwtar_784_6784()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.app", user_id=-1, group_id=-1, prog_num=6785, recursive=True) as chown_785_6785:  # 0m:0.000s
                            chown_785_6785()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6786) as should_copy_source_786_6786:  # 0m:0.066s
                    should_copy_source_786_6786()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", prog_num=6787):  # 0m:0.065s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r".", delete_extraneous_files=True, prog_num=6788) as copy_dir_to_dir_787_6788:  # 0m:0.001s
                            copy_dir_to_dir_787_6788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", where_to_unwtar=r".", prog_num=6789) as unwtar_788_6789:  # 0m:0.064s
                            unwtar_788_6789()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.bundle", user_id=-1, group_id=-1, prog_num=6790, recursive=True) as chown_789_6790:  # 0m:0.000s
                            chown_789_6790()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Control Panel v14.0.342.343", prog_num=6791):  # 0m:0.162s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6792) as should_copy_source_790_6792:  # 0m:0.095s
                    should_copy_source_790_6792()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=6793):  # 0m:0.095s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=6794) as copy_dir_to_dir_791_6794:  # 0m:0.002s
                            copy_dir_to_dir_791_6794()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=6795) as unwtar_792_6795:  # 0m:0.093s
                            unwtar_792_6795()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=6796, recursive=True) as chown_793_6796:  # 0m:0.000s
                            chown_793_6796()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6797) as should_copy_source_794_6797:  # 0m:0.066s
                    should_copy_source_794_6797()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=6798):  # 0m:0.066s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=6799) as copy_dir_to_dir_795_6799:  # 0m:0.001s
                            copy_dir_to_dir_795_6799()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=6800) as unwtar_796_6800:  # 0m:0.064s
                            unwtar_796_6800()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=6801, recursive=True) as chown_797_6801:  # 0m:0.000s
                            chown_797_6801()
            with Stage(r"copy", r"DirectOut SG.MADI Control Panel v14.0.342.343", prog_num=6802):  # 0m:0.223s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6803) as should_copy_source_798_6803:  # 0m:0.141s
                    should_copy_source_798_6803()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", prog_num=6804):  # 0m:0.140s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r".", delete_extraneous_files=True, prog_num=6805) as copy_dir_to_dir_799_6805:  # 0m:0.002s
                            copy_dir_to_dir_799_6805()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", where_to_unwtar=r".", prog_num=6806) as unwtar_800_6806:  # 0m:0.139s
                            unwtar_800_6806()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.app", user_id=-1, group_id=-1, prog_num=6807, recursive=True) as chown_801_6807:  # 0m:0.000s
                            chown_801_6807()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6808) as should_copy_source_802_6808:  # 0m:0.082s
                    should_copy_source_802_6808()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", prog_num=6809):  # 0m:0.082s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r".", delete_extraneous_files=True, prog_num=6810) as copy_dir_to_dir_803_6810:  # 0m:0.001s
                            copy_dir_to_dir_803_6810()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", where_to_unwtar=r".", prog_num=6811) as unwtar_804_6811:  # 0m:0.080s
                            unwtar_804_6811()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.bundle", user_id=-1, group_id=-1, prog_num=6812, recursive=True) as chown_805_6812:  # 0m:0.000s
                            chown_805_6812()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Control Panel v13.1.261.180", prog_num=6813):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6814) as should_copy_source_806_6814:  # ?
                    should_copy_source_806_6814()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=6815):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=6816) as copy_dir_to_dir_807_6816:  # ?
                            copy_dir_to_dir_807_6816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=6817) as unwtar_808_6817:  # ?
                            unwtar_808_6817()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=6818, recursive=True) as chown_809_6818:  # 0m:0.000s
                            chown_809_6818()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6819) as should_copy_source_810_6819:  # ?
                    should_copy_source_810_6819()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=6820):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=6821) as copy_dir_to_dir_811_6821:  # ?
                            copy_dir_to_dir_811_6821()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=6822) as unwtar_812_6822:  # ?
                            unwtar_812_6822()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=6823, recursive=True) as chown_813_6823:  # 0m:0.000s
                            chown_813_6823()
            with Stage(r"copy", r"Hear Technologies SG Control Panel v14.0.342.343", prog_num=6824):  # 0m:0.247s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6825) as should_copy_source_814_6825:  # 0m:0.177s
                    should_copy_source_814_6825()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", prog_num=6826):  # 0m:0.177s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r".", delete_extraneous_files=True, prog_num=6827) as copy_dir_to_dir_815_6827:  # 0m:0.004s
                            copy_dir_to_dir_815_6827()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", where_to_unwtar=r".", prog_num=6828) as unwtar_816_6828:  # 0m:0.173s
                            unwtar_816_6828()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.app", user_id=-1, group_id=-1, prog_num=6829, recursive=True) as chown_817_6829:  # 0m:0.000s
                            chown_817_6829()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6830) as should_copy_source_818_6830:  # 0m:0.070s
                    should_copy_source_818_6830()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", prog_num=6831):  # 0m:0.070s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r".", delete_extraneous_files=True, prog_num=6832) as copy_dir_to_dir_819_6832:  # 0m:0.001s
                            copy_dir_to_dir_819_6832()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", where_to_unwtar=r".", prog_num=6833) as unwtar_820_6833:  # 0m:0.068s
                            unwtar_820_6833()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.bundle", user_id=-1, group_id=-1, prog_num=6834, recursive=True) as chown_821_6834:  # 0m:0.000s
                            chown_821_6834()
            with Stage(r"copy", r"DigiGrid IOC Control Panel v14.0.342.343", prog_num=6835):  # 0m:0.319s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6836) as should_copy_source_822_6836:  # 0m:0.234s
                    should_copy_source_822_6836()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", prog_num=6837):  # 0m:0.234s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r".", delete_extraneous_files=True, prog_num=6838) as copy_dir_to_dir_823_6838:  # 0m:0.002s
                            copy_dir_to_dir_823_6838()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", where_to_unwtar=r".", prog_num=6839) as unwtar_824_6839:  # 0m:0.232s
                            unwtar_824_6839()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.app", user_id=-1, group_id=-1, prog_num=6840, recursive=True) as chown_825_6840:  # 0m:0.000s
                            chown_825_6840()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6841) as should_copy_source_826_6841:  # 0m:0.084s
                    should_copy_source_826_6841()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", prog_num=6842):  # 0m:0.084s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r".", delete_extraneous_files=True, prog_num=6843) as copy_dir_to_dir_827_6843:  # 0m:0.001s
                            copy_dir_to_dir_827_6843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", where_to_unwtar=r".", prog_num=6844) as unwtar_828_6844:  # 0m:0.082s
                            unwtar_828_6844()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.bundle", user_id=-1, group_id=-1, prog_num=6845, recursive=True) as chown_829_6845:  # 0m:0.000s
                            chown_829_6845()
            with Stage(r"copy", r"IONIC16 Control Panel v14.0.134.135", prog_num=6846):  # 0m:0.285s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6847) as should_copy_source_830_6847:  # 0m:0.201s
                    should_copy_source_830_6847()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.app", prog_num=6848):  # 0m:0.201s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r".", delete_extraneous_files=True, prog_num=6849) as copy_dir_to_dir_831_6849:  # 0m:0.002s
                            copy_dir_to_dir_831_6849()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", where_to_unwtar=r".", prog_num=6850) as unwtar_832_6850:  # 0m:0.199s
                            unwtar_832_6850()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.app", user_id=-1, group_id=-1, prog_num=6851, recursive=True) as chown_833_6851:  # 0m:0.000s
                            chown_833_6851()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6852) as should_copy_source_834_6852:  # 0m:0.083s
                    should_copy_source_834_6852()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.bundle", prog_num=6853):  # 0m:0.083s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r".", delete_extraneous_files=True, prog_num=6854) as copy_dir_to_dir_835_6854:  # 0m:0.001s
                            copy_dir_to_dir_835_6854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", where_to_unwtar=r".", prog_num=6855) as unwtar_836_6855:  # 0m:0.081s
                            unwtar_836_6855()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.bundle", user_id=-1, group_id=-1, prog_num=6856, recursive=True) as chown_837_6856:  # 0m:0.000s
                            chown_837_6856()
            with Stage(r"copy", r"DigiGrid IOS Control Panel v14.0.342.343", prog_num=6857):  # 0m:0.325s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6858) as should_copy_source_838_6858:  # 0m:0.240s
                    should_copy_source_838_6858()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", prog_num=6859):  # 0m:0.240s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r".", delete_extraneous_files=True, prog_num=6860) as copy_dir_to_dir_839_6860:  # 0m:0.001s
                            copy_dir_to_dir_839_6860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", where_to_unwtar=r".", prog_num=6861) as unwtar_840_6861:  # 0m:0.238s
                            unwtar_840_6861()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.app", user_id=-1, group_id=-1, prog_num=6862, recursive=True) as chown_841_6862:  # 0m:0.000s
                            chown_841_6862()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6863) as should_copy_source_842_6863:  # 0m:0.084s
                    should_copy_source_842_6863()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", prog_num=6864):  # 0m:0.084s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r".", delete_extraneous_files=True, prog_num=6865) as copy_dir_to_dir_843_6865:  # 0m:0.002s
                            copy_dir_to_dir_843_6865()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", where_to_unwtar=r".", prog_num=6866) as unwtar_844_6866:  # 0m:0.082s
                            unwtar_844_6866()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.bundle", user_id=-1, group_id=-1, prog_num=6867, recursive=True) as chown_845_6867:  # 0m:0.000s
                            chown_845_6867()
            with Stage(r"copy", r"DigiGrid IOS-XL Control Panel v14.0.342.343", prog_num=6868):  # 0m:0.325s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6869) as should_copy_source_846_6869:  # 0m:0.240s
                    should_copy_source_846_6869()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", prog_num=6870):  # 0m:0.240s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r".", delete_extraneous_files=True, prog_num=6871) as copy_dir_to_dir_847_6871:  # 0m:0.001s
                            copy_dir_to_dir_847_6871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", where_to_unwtar=r".", prog_num=6872) as unwtar_848_6872:  # 0m:0.238s
                            unwtar_848_6872()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.app", user_id=-1, group_id=-1, prog_num=6873, recursive=True) as chown_849_6873:  # 0m:0.000s
                            chown_849_6873()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6874) as should_copy_source_850_6874:  # 0m:0.085s
                    should_copy_source_850_6874()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", prog_num=6875):  # 0m:0.085s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r".", delete_extraneous_files=True, prog_num=6876) as copy_dir_to_dir_851_6876:  # 0m:0.001s
                            copy_dir_to_dir_851_6876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", where_to_unwtar=r".", prog_num=6877) as unwtar_852_6877:  # 0m:0.083s
                            unwtar_852_6877()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.bundle", user_id=-1, group_id=-1, prog_num=6878, recursive=True) as chown_853_6878:  # 0m:0.000s
                            chown_853_6878()
            with Stage(r"copy", r"DigiGrid IOX Control Panel v14.0.342.343", prog_num=6879):  # 0m:0.320s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6880) as should_copy_source_854_6880:  # 0m:0.241s
                    should_copy_source_854_6880()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", prog_num=6881):  # 0m:0.241s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r".", delete_extraneous_files=True, prog_num=6882) as copy_dir_to_dir_855_6882:  # 0m:0.001s
                            copy_dir_to_dir_855_6882()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", where_to_unwtar=r".", prog_num=6883) as unwtar_856_6883:  # 0m:0.239s
                            unwtar_856_6883()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.app", user_id=-1, group_id=-1, prog_num=6884, recursive=True) as chown_857_6884:  # 0m:0.000s
                            chown_857_6884()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6885) as should_copy_source_858_6885:  # 0m:0.078s
                    should_copy_source_858_6885()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", prog_num=6886):  # 0m:0.078s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r".", delete_extraneous_files=True, prog_num=6887) as copy_dir_to_dir_859_6887:  # 0m:0.001s
                            copy_dir_to_dir_859_6887()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", where_to_unwtar=r".", prog_num=6888) as unwtar_860_6888:  # 0m:0.076s
                            unwtar_860_6888()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.bundle", user_id=-1, group_id=-1, prog_num=6889, recursive=True) as chown_861_6889:  # 0m:0.000s
                            chown_861_6889()
            with Stage(r"copy", r"JoeCo BBSG24MP Control Panel v14.0.342.343", prog_num=6890):  # 0m:0.234s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6891) as should_copy_source_862_6891:  # 0m:0.152s
                    should_copy_source_862_6891()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", prog_num=6892):  # 0m:0.152s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r".", delete_extraneous_files=True, prog_num=6893) as copy_dir_to_dir_863_6893:  # 0m:0.002s
                            copy_dir_to_dir_863_6893()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", where_to_unwtar=r".", prog_num=6894) as unwtar_864_6894:  # 0m:0.150s
                            unwtar_864_6894()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.app", user_id=-1, group_id=-1, prog_num=6895, recursive=True) as chown_865_6895:  # 0m:0.000s
                            chown_865_6895()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6896) as should_copy_source_866_6896:  # 0m:0.082s
                    should_copy_source_866_6896()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", prog_num=6897):  # 0m:0.082s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r".", delete_extraneous_files=True, prog_num=6898) as copy_dir_to_dir_867_6898:  # 0m:0.002s
                            copy_dir_to_dir_867_6898()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", where_to_unwtar=r".", prog_num=6899) as unwtar_868_6899:  # 0m:0.080s
                            unwtar_868_6899()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.bundle", user_id=-1, group_id=-1, prog_num=6900, recursive=True) as chown_869_6900:  # 0m:0.000s
                            chown_869_6900()
            with Stage(r"copy", r"M-DL-WAVES3 Control Panel v14.0.342.343", prog_num=6901):  # 0m:0.183s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6902) as should_copy_source_870_6902:  # 0m:0.114s
                    should_copy_source_870_6902()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", prog_num=6903):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=6904) as copy_dir_to_dir_871_6904:  # 0m:0.002s
                            copy_dir_to_dir_871_6904()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", where_to_unwtar=r".", prog_num=6905) as unwtar_872_6905:  # 0m:0.112s
                            unwtar_872_6905()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=6906, recursive=True) as chown_873_6906:  # 0m:0.000s
                            chown_873_6906()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6907) as should_copy_source_874_6907:  # 0m:0.068s
                    should_copy_source_874_6907()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", prog_num=6908):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=6909) as copy_dir_to_dir_875_6909:  # 0m:0.001s
                            copy_dir_to_dir_875_6909()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=6910) as unwtar_876_6910:  # 0m:0.066s
                            unwtar_876_6910()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=6911, recursive=True) as chown_877_6911:  # 0m:0.000s
                            chown_877_6911()
            with Stage(r"copy", r"M-SQ-WAVES3 Control Panel v14.0.342.343", prog_num=6912):  # 0m:0.185s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6913) as should_copy_source_878_6913:  # 0m:0.119s
                    should_copy_source_878_6913()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", prog_num=6914):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=6915) as copy_dir_to_dir_879_6915:  # 0m:0.002s
                            copy_dir_to_dir_879_6915()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", where_to_unwtar=r".", prog_num=6916) as unwtar_880_6916:  # 0m:0.117s
                            unwtar_880_6916()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=6917, recursive=True) as chown_881_6917:  # 0m:0.000s
                            chown_881_6917()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6918) as should_copy_source_882_6918:  # 0m:0.066s
                    should_copy_source_882_6918()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", prog_num=6919):  # 0m:0.066s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=6920) as copy_dir_to_dir_883_6920:  # 0m:0.002s
                            copy_dir_to_dir_883_6920()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=6921) as unwtar_884_6921:  # 0m:0.064s
                            unwtar_884_6921()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=6922, recursive=True) as chown_885_6922:  # 0m:0.000s
                            chown_885_6922()
            with Stage(r"copy", r"M-Waves v2 Control Panel v14.0.342.343", prog_num=6923):  # 0m:0.187s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6924) as should_copy_source_886_6924:  # 0m:0.119s
                    should_copy_source_886_6924()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", prog_num=6925):  # 0m:0.119s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r".", delete_extraneous_files=True, prog_num=6926) as copy_dir_to_dir_887_6926:  # 0m:0.002s
                            copy_dir_to_dir_887_6926()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", where_to_unwtar=r".", prog_num=6927) as unwtar_888_6927:  # 0m:0.117s
                            unwtar_888_6927()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.app", user_id=-1, group_id=-1, prog_num=6928, recursive=True) as chown_889_6928:  # 0m:0.000s
                            chown_889_6928()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6929) as should_copy_source_890_6929:  # 0m:0.068s
                    should_copy_source_890_6929()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", prog_num=6930):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r".", delete_extraneous_files=True, prog_num=6931) as copy_dir_to_dir_891_6931:  # 0m:0.001s
                            copy_dir_to_dir_891_6931()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", where_to_unwtar=r".", prog_num=6932) as unwtar_892_6932:  # 0m:0.066s
                            unwtar_892_6932()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.bundle", user_id=-1, group_id=-1, prog_num=6933, recursive=True) as chown_893_6933:  # 0m:0.000s
                            chown_893_6933()
            with Stage(r"copy", r"DigiGrid MGB/MGO/MGR Control Panel v14.0.342.343", prog_num=6934):  # 0m:0.243s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6935) as should_copy_source_894_6935:  # 0m:0.171s
                    should_copy_source_894_6935()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", prog_num=6936):  # 0m:0.171s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r".", delete_extraneous_files=True, prog_num=6937) as copy_dir_to_dir_895_6937:  # 0m:0.002s
                            copy_dir_to_dir_895_6937()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", where_to_unwtar=r".", prog_num=6938) as unwtar_896_6938:  # 0m:0.169s
                            unwtar_896_6938()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.app", user_id=-1, group_id=-1, prog_num=6939, recursive=True) as chown_897_6939:  # 0m:0.000s
                            chown_897_6939()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6940) as should_copy_source_898_6940:  # 0m:0.072s
                    should_copy_source_898_6940()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", prog_num=6941):  # 0m:0.071s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r".", delete_extraneous_files=True, prog_num=6942) as copy_dir_to_dir_899_6942:  # 0m:0.001s
                            copy_dir_to_dir_899_6942()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", where_to_unwtar=r".", prog_num=6943) as unwtar_900_6943:  # 0m:0.070s
                            unwtar_900_6943()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.bundle", user_id=-1, group_id=-1, prog_num=6944, recursive=True) as chown_901_6944:  # 0m:0.000s
                            chown_901_6944()
            with Stage(r"copy", r"Waves Legacy SG Control Panels v14.0.342.343", prog_num=6945):  # 0m:0.150s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6946) as should_copy_source_902_6946:  # 0m:0.080s
                    should_copy_source_902_6946()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.app", prog_num=6947):  # 0m:0.080s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r".", delete_extraneous_files=True, prog_num=6948) as copy_dir_to_dir_903_6948:  # 0m:0.002s
                            copy_dir_to_dir_903_6948()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", where_to_unwtar=r".", prog_num=6949) as unwtar_904_6949:  # 0m:0.078s
                            unwtar_904_6949()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.app", user_id=-1, group_id=-1, prog_num=6950, recursive=True) as chown_905_6950:  # 0m:0.000s
                            chown_905_6950()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6951) as should_copy_source_906_6951:  # 0m:0.070s
                    should_copy_source_906_6951()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", prog_num=6952):  # 0m:0.069s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r".", delete_extraneous_files=True, prog_num=6953) as copy_dir_to_dir_907_6953:  # 0m:0.001s
                            copy_dir_to_dir_907_6953()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", where_to_unwtar=r".", prog_num=6954) as unwtar_908_6954:  # 0m:0.068s
                            unwtar_908_6954()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.bundle", user_id=-1, group_id=-1, prog_num=6955, recursive=True) as chown_909_6955:  # 0m:0.000s
                            chown_909_6955()
            with Stage(r"copy", r"Remote SG IO Control Panel v14.0.342.343", prog_num=6956):  # 0m:0.164s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6957) as should_copy_source_910_6957:  # 0m:0.098s
                    should_copy_source_910_6957()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", prog_num=6958):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r".", delete_extraneous_files=True, prog_num=6959) as copy_dir_to_dir_911_6959:  # 0m:0.001s
                            copy_dir_to_dir_911_6959()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", where_to_unwtar=r".", prog_num=6960) as unwtar_912_6960:  # 0m:0.096s
                            unwtar_912_6960()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.app", user_id=-1, group_id=-1, prog_num=6961, recursive=True) as chown_913_6961:  # 0m:0.000s
                            chown_913_6961()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6962) as should_copy_source_914_6962:  # 0m:0.066s
                    should_copy_source_914_6962()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", prog_num=6963):  # 0m:0.066s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r".", delete_extraneous_files=True, prog_num=6964) as copy_dir_to_dir_915_6964:  # 0m:0.001s
                            copy_dir_to_dir_915_6964()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", where_to_unwtar=r".", prog_num=6965) as unwtar_916_6965:  # 0m:0.064s
                            unwtar_916_6965()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.bundle", user_id=-1, group_id=-1, prog_num=6966, recursive=True) as chown_917_6966:  # 0m:0.000s
                            chown_917_6966()
            with Stage(r"copy", r"SG Connect v14.0.342.343", prog_num=6967):  # 0m:0.064s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6968) as should_copy_source_918_6968:  # 0m:0.064s
                    should_copy_source_918_6968()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SG Connect Control.bundle", prog_num=6969):  # 0m:0.063s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r".", delete_extraneous_files=True, prog_num=6970) as copy_dir_to_dir_919_6970:  # 0m:0.001s
                            copy_dir_to_dir_919_6970()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", where_to_unwtar=r".", prog_num=6971) as unwtar_920_6971:  # 0m:0.062s
                            unwtar_920_6971()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control.bundle", user_id=-1, group_id=-1, prog_num=6972, recursive=True) as chown_921_6972:  # 0m:0.000s
                            chown_921_6972()
            with Stage(r"copy", r"SoundStudio STG Control Panel v14.0.342.343", prog_num=6973):  # 0m:0.265s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6974) as should_copy_source_922_6974:  # 0m:0.184s
                    should_copy_source_922_6974()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", prog_num=6975):  # 0m:0.184s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r".", delete_extraneous_files=True, prog_num=6976) as copy_dir_to_dir_923_6976:  # 0m:0.001s
                            copy_dir_to_dir_923_6976()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", where_to_unwtar=r".", prog_num=6977) as unwtar_924_6977:  # 0m:0.182s
                            unwtar_924_6977()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.app", user_id=-1, group_id=-1, prog_num=6978, recursive=True) as chown_925_6978:  # 0m:0.000s
                            chown_925_6978()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6979) as should_copy_source_926_6979:  # 0m:0.081s
                    should_copy_source_926_6979()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", prog_num=6980):  # 0m:0.081s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r".", delete_extraneous_files=True, prog_num=6981) as copy_dir_to_dir_927_6981:  # 0m:0.001s
                            copy_dir_to_dir_927_6981()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", where_to_unwtar=r".", prog_num=6982) as unwtar_928_6982:  # 0m:0.079s
                            unwtar_928_6982()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.bundle", user_id=-1, group_id=-1, prog_num=6983, recursive=True) as chown_929_6983:  # 0m:0.000s
                            chown_929_6983()
            with Stage(r"copy", r"X-WSG Control Panel v14.0.342.343", prog_num=6984):  # 0m:0.180s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6985) as should_copy_source_930_6985:  # 0m:0.111s
                    should_copy_source_930_6985()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", prog_num=6986):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r".", delete_extraneous_files=True, prog_num=6987) as copy_dir_to_dir_931_6987:  # 0m:0.001s
                            copy_dir_to_dir_931_6987()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", where_to_unwtar=r".", prog_num=6988) as unwtar_932_6988:  # 0m:0.109s
                            unwtar_932_6988()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.app", user_id=-1, group_id=-1, prog_num=6989, recursive=True) as chown_933_6989:  # 0m:0.000s
                            chown_933_6989()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6990) as should_copy_source_934_6990:  # 0m:0.069s
                    should_copy_source_934_6990()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", prog_num=6991):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=6992) as copy_dir_to_dir_935_6992:  # 0m:0.001s
                            copy_dir_to_dir_935_6992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", where_to_unwtar=r".", prog_num=6993) as unwtar_936_6993:  # 0m:0.067s
                            unwtar_936_6993()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=6994, recursive=True) as chown_937_6994:  # 0m:0.000s
                            chown_937_6994()
            with Stage(r"copy", r"Yamaha SoundGrid IO Control Panel v14.0.342.343", prog_num=6995):  # 0m:0.169s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=6996) as should_copy_source_938_6996:  # 0m:0.103s
                    should_copy_source_938_6996()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", prog_num=6997):  # 0m:0.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r".", delete_extraneous_files=True, prog_num=6998) as copy_dir_to_dir_939_6998:  # 0m:0.002s
                            copy_dir_to_dir_939_6998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", where_to_unwtar=r".", prog_num=6999) as unwtar_940_6999:  # 0m:0.101s
                            unwtar_940_6999()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.app", user_id=-1, group_id=-1, prog_num=7000, recursive=True) as chown_941_7000:  # 0m:0.000s
                            chown_941_7000()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=7001) as should_copy_source_942_7001:  # 0m:0.066s
                    should_copy_source_942_7001()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", prog_num=7002):  # 0m:0.066s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=7003) as copy_dir_to_dir_943_7003:  # 0m:0.002s
                            copy_dir_to_dir_943_7003()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", where_to_unwtar=r".", prog_num=7004) as unwtar_944_7004:  # 0m:0.064s
                            unwtar_944_7004()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.bundle", user_id=-1, group_id=-1, prog_num=7005, recursive=True) as chown_945_7005:  # 0m:0.000s
                            chown_945_7005()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=7006) as shell_command_946_7006:  # 0m:0.844s
                shell_command_946_7006()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=7007) as cd_stage_947_7007:  # 0m:0.002s
            cd_stage_947_7007()
            with Stage(r"copy", r"Waves Local Server v12.14.471.472", prog_num=7008):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=5, prog_num=7009) as should_copy_source_948_7009:  # ?
                    should_copy_source_948_7009()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=7010):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=7011) as copy_dir_to_dir_949_7011:  # ?
                            copy_dir_to_dir_949_7011()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=7012) as unwtar_950_7012:  # ?
                            unwtar_950_7012()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=7013, recursive=True) as chown_951_7013:  # ?
                            chown_951_7013()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=7014) as if_952_7014:  # 0m:0.001s
                            if_952_7014()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=7015) as cd_stage_953_7015:  # 0m:15.835s
            cd_stage_953_7015()
            with Stage(r"copy", r"WavesPluginServer_V14_2 v13.6.444.720", prog_num=7016):  # 0m:15.835s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=7017) as should_copy_source_954_7017:  # 0m:15.835s
                    should_copy_source_954_7017()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", prog_num=7018):  # 0m:15.835s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=7019) as copy_dir_to_dir_955_7019:  # 0m:0.003s
                            copy_dir_to_dir_955_7019()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", where_to_unwtar=r".", prog_num=7020) as unwtar_956_7020:  # 0m:15.831s
                            unwtar_956_7020()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle", user_id=-1, group_id=-1, prog_num=7021, recursive=True) as chown_957_7021:  # 0m:0.000s
                            chown_957_7021()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=7022) as if_958_7022:  # 0m:0.001s
                            if_958_7022()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=7023) as cd_stage_959_7023:  # 0m:1.443s
            cd_stage_959_7023()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=7024):  # 0m:0.741s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=7025) as should_copy_source_960_7025:  # 0m:0.741s
                    should_copy_source_960_7025()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=7026):  # 0m:0.740s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=7027) as copy_dir_to_dir_961_7027:  # 0m:0.002s
                            copy_dir_to_dir_961_7027()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=7028) as unwtar_962_7028:  # 0m:0.663s
                            unwtar_962_7028()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=7029, recursive=True) as chown_963_7029:  # 0m:0.000s
                            chown_963_7029()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=7030) as break_hard_link_964_7030:  # 0m:0.018s
                            break_hard_link_964_7030()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=7031) as shell_command_965_7031:  # 0m:0.049s
                            shell_command_965_7031()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=7032, recursive=True) as chown_966_7032:  # 0m:0.000s
                            chown_966_7032()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=7033, recursive=True) as chmod_967_7033:  # 0m:0.008s
                            chmod_967_7033()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=7034):  # 0m:0.702s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=7035) as should_copy_source_968_7035:  # 0m:0.702s
                    should_copy_source_968_7035()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=7036):  # 0m:0.702s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=7037) as copy_dir_to_dir_969_7037:  # 0m:0.002s
                            copy_dir_to_dir_969_7037()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=7038) as unwtar_970_7038:  # 0m:0.628s
                            unwtar_970_7038()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=7039, recursive=True) as chown_971_7039:  # 0m:0.000s
                            chown_971_7039()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=7040) as break_hard_link_972_7040:  # 0m:0.015s
                            break_hard_link_972_7040()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=7041) as shell_command_973_7041:  # 0m:0.047s
                            shell_command_973_7041()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=7042, recursive=True) as chown_974_7042:  # 0m:0.000s
                            chown_974_7042()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=7043, recursive=True) as chmod_975_7043:  # 0m:0.009s
                            chmod_975_7043()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=7044) as cd_stage_976_7044:  # 0m:1.275s
            cd_stage_976_7044()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=7045):  # 0m:0.401s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=7046) as should_copy_source_977_7046:  # 0m:0.401s
                    should_copy_source_977_7046()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=7047):  # 0m:0.400s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=7048) as copy_dir_to_dir_978_7048:  # 0m:0.022s
                            copy_dir_to_dir_978_7048()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=7049) as unwtar_979_7049:  # 0m:0.367s
                            unwtar_979_7049()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=7050, recursive=True) as chown_980_7050:  # 0m:0.000s
                            chown_980_7050()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=7051) as shell_command_981_7051:  # 0m:0.011s
                            shell_command_981_7051()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=7052):  # 0m:0.443s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=7053) as should_copy_source_982_7053:  # 0m:0.443s
                    should_copy_source_982_7053()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=7054):  # 0m:0.442s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=7055) as copy_dir_to_dir_983_7055:  # 0m:0.002s
                            copy_dir_to_dir_983_7055()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=7056) as unwtar_984_7056:  # 0m:0.391s
                            unwtar_984_7056()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=7057, recursive=True) as chown_985_7057:  # 0m:0.000s
                            chown_985_7057()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=7058) as shell_command_986_7058:  # 0m:0.049s
                            shell_command_986_7058()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=7059):  # 0m:0.430s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=7060) as should_copy_source_987_7060:  # 0m:0.430s
                    should_copy_source_987_7060()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=7061):  # 0m:0.429s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=7062) as copy_dir_to_dir_988_7062:  # 0m:0.002s
                            copy_dir_to_dir_988_7062()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=7063) as unwtar_989_7063:  # 0m:0.378s
                            unwtar_989_7063()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=7064, recursive=True) as chown_990_7064:  # 0m:0.000s
                            chown_990_7064()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=7065) as shell_command_991_7065:  # 0m:0.049s
                            shell_command_991_7065()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=7066) as cd_stage_992_7066:  # 0m:1.498s
            cd_stage_992_7066()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=7067):  # 0m:0.767s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=7068) as should_copy_source_993_7068:  # 0m:0.767s
                    should_copy_source_993_7068()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=7069):  # 0m:0.767s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=7070) as copy_dir_to_dir_994_7070:  # 0m:0.002s
                            copy_dir_to_dir_994_7070()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=7071) as unwtar_995_7071:  # 0m:0.715s
                            unwtar_995_7071()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=7072, recursive=True) as chown_996_7072:  # 0m:0.000s
                            chown_996_7072()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=7073) as shell_command_997_7073:  # 0m:0.050s
                            shell_command_997_7073()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=7074):  # 0m:0.730s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=7075) as should_copy_source_998_7075:  # 0m:0.729s
                    should_copy_source_998_7075()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=7076):  # 0m:0.729s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=7077) as copy_dir_to_dir_999_7077:  # 0m:0.002s
                            copy_dir_to_dir_999_7077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=7078) as unwtar_1000_7078:  # 0m:0.678s
                            unwtar_1000_7078()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=7079, recursive=True) as chown_1001_7079:  # 0m:0.000s
                            chown_1001_7079()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=7080) as shell_command_1002_7080:  # 0m:0.048s
                            shell_command_1002_7080()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=7081) as cd_stage_1003_7081:  # 0m:0.366s
            cd_stage_1003_7081()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=7082):  # 0m:0.365s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=7083) as should_copy_source_1004_7083:  # 0m:0.365s
                    should_copy_source_1004_7083()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=7084):  # 0m:0.364s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=7085) as copy_dir_to_dir_1005_7085:  # 0m:0.001s
                            copy_dir_to_dir_1005_7085()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=7086) as unwtar_1006_7086:  # 0m:0.196s
                            unwtar_1006_7086()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=7087, recursive=True) as chown_1007_7087:  # 0m:0.000s
                            chown_1007_7087()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=7088) as shell_command_1008_7088:  # 0m:0.095s
                            shell_command_1008_7088()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=7089) as script_command_1009_7089:  # 0m:0.013s
                            script_command_1009_7089()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=7090) as shell_command_1010_7090:  # 0m:0.059s
                            shell_command_1010_7090()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=7091) as create_symlink_1011_7091:  # 0m:0.001s
                create_symlink_1011_7091()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=7092) as create_symlink_1012_7092:  # 0m:0.000s
                create_symlink_1012_7092()
        with CdStage(r"copy_to_folder", r"/Users/Shared/Waves/SoundGrid Studio/Templates", prog_num=7093) as cd_stage_1013_7093:  # 0m:0.002s
            cd_stage_1013_7093()
            with Stage(r"copy", r"SoundGrid Studio Sessions Structure", prog_num=7094):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r"/Users/Shared/Waves/SoundGrid Studio/Templates", skip_progress_count=3, prog_num=7095) as should_copy_source_1014_7095:  # 0m:0.001s
                    should_copy_source_1014_7095()
                    with Stage(r"copy source", r"Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", prog_num=7096):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r".", prog_num=7097) as copy_file_to_dir_1015_7097:  # 0m:0.001s
                            copy_file_to_dir_1015_7097()
                        with ChmodAndChown(path=r"Empty Session.sgst", mode="a+rw", user_id=-1, group_id=-1, prog_num=7098) as chmod_and_chown_1016_7098:  # 0m:0.000s
                            chmod_and_chown_1016_7098()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=7099) as cd_stage_1017_7099:  # 0m:0.000s
            cd_stage_1017_7099()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Lamps/Vocal/Vocal 2 (Lead).xps", prog_num=7100) as rm_file_or_dir_1018_7100:  # 0m:0.000s
                rm_file_or_dir_1018_7100()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Factory", prog_num=7101) as rm_file_or_dir_1019_7101:  # 0m:0.000s
                rm_file_or_dir_1019_7101()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/GroupOrder.xps", prog_num=7102) as rm_file_or_dir_1020_7102:  # 0m:0.000s
                rm_file_or_dir_1020_7102()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Kori Andres", prog_num=7103) as rm_file_or_dir_1021_7103:  # 0m:0.000s
                rm_file_or_dir_1021_7103()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/Symphony II SoundGrid User Guide", prog_num=7104) as rm_file_or_dir_1022_7104:  # 0m:0.000s
            rm_file_or_dir_1022_7104()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=7105) as rm_file_or_dir_1023_7105:  # 0m:0.000s
            rm_file_or_dir_1023_7105()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack and Network Streaming with HD-HDX-HDNative - external Server.emo", prog_num=7106) as rm_file_or_dir_1024_7106:  # 0m:0.000s
            rm_file_or_dir_1024_7106()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack Processing for HD-HDX-HDNative Systems - external Server.emo", prog_num=7107) as rm_file_or_dir_1025_7107:  # 0m:0.000s
            rm_file_or_dir_1025_7107()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Mixing with StudioRack - external Server.emo", prog_num=7108) as rm_file_or_dir_1026_7108:  # 0m:0.000s
            rm_file_or_dir_1026_7108()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Recording thru eMotion Mixer - external Server.emo", prog_num=7109) as rm_file_or_dir_1027_7109:  # 0m:0.000s
            rm_file_or_dir_1027_7109()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and External Mixing  - external Server.emo", prog_num=7110) as rm_file_or_dir_1028_7110:  # 0m:0.000s
            rm_file_or_dir_1028_7110()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and Monitoring - external Server.emo", prog_num=7111) as rm_file_or_dir_1029_7111:  # 0m:0.000s
            rm_file_or_dir_1029_7111()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=7112) as rm_file_or_dir_1030_7112:  # 0m:0.000s
            rm_file_or_dir_1030_7112()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack and Network Streaming with HD-HDX-HDNative.emo", prog_num=7113) as rm_file_or_dir_1031_7113:  # 0m:0.000s
            rm_file_or_dir_1031_7113()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack Processing for HD-HDX-HDNative Systems.emo", prog_num=7114) as rm_file_or_dir_1032_7114:  # 0m:0.000s
            rm_file_or_dir_1032_7114()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Mixing with StudioRack.emo", prog_num=7115) as rm_file_or_dir_1033_7115:  # 0m:0.000s
            rm_file_or_dir_1033_7115()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Recording thru eMotion Mixer.emo", prog_num=7116) as rm_file_or_dir_1034_7116:  # 0m:0.000s
            rm_file_or_dir_1034_7116()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and External Mixing.emo", prog_num=7117) as rm_file_or_dir_1035_7117:  # 0m:0.000s
            rm_file_or_dir_1035_7117()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and Monitoring.emo", prog_num=7118) as rm_file_or_dir_1036_7118:  # 0m:0.000s
            rm_file_or_dir_1036_7118()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS DLI REC-PB Standalone.emo", prog_num=7119) as rm_file_or_dir_1037_7119:  # 0m:0.000s
            rm_file_or_dir_1037_7119()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=7120) as rm_file_or_dir_1038_7120:  # 0m:0.037s
            rm_file_or_dir_1038_7120()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid D User Guide.pdf", prog_num=7121) as rm_file_or_dir_1039_7121:  # 0m:0.000s
            rm_file_or_dir_1039_7121()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid M User Guide.pdf", prog_num=7122) as rm_file_or_dir_1040_7122:  # 0m:0.000s
            rm_file_or_dir_1040_7122()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid Q User Guide.pdf", prog_num=7123) as rm_file_or_dir_1041_7123:  # 0m:0.000s
            rm_file_or_dir_1041_7123()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - Recording thru eMotion Mixer.emo", prog_num=7124) as rm_file_or_dir_1042_7124:  # 0m:0.000s
            rm_file_or_dir_1042_7124()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - REC-PB Standalone.emo", prog_num=7125) as rm_file_or_dir_1043_7125:  # 0m:0.000s
            rm_file_or_dir_1043_7125()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - StudioRack Processing and Monitoring.emo", prog_num=7126) as rm_file_or_dir_1044_7126:  # 0m:0.000s
            rm_file_or_dir_1044_7126()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - Recording thru eMotion Mixer - external Server.emo", prog_num=7127) as rm_file_or_dir_1045_7127:  # 0m:0.000s
            rm_file_or_dir_1045_7127()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - REC-PB Standalone.emo", prog_num=7128) as rm_file_or_dir_1046_7128:  # 0m:0.000s
            rm_file_or_dir_1046_7128()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - StudioRack Processing and Monitoring - external Server.emo", prog_num=7129) as rm_file_or_dir_1047_7129:  # 0m:0.000s
            rm_file_or_dir_1047_7129()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/MGB MGO REC-PB Standalone.emo", prog_num=7130) as rm_file_or_dir_1048_7130:  # 0m:0.000s
            rm_file_or_dir_1048_7130()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/2x MGB MGO REC-PB 96Khz Standalone.emo", prog_num=7131) as rm_file_or_dir_1049_7131:  # 0m:0.000s
            rm_file_or_dir_1049_7131()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=7132) as shell_command_1050_7132:  # 0m:0.101s
            shell_command_1050_7132()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=7133) as script_command_1051_7133:  # 0m:0.012s
            script_command_1051_7133()
        with ShellCommand(r"echo This installation requires that you restart your computer.", message=r"Restart_required_IID post-install step 1", prog_num=7134) as shell_command_1052_7134:  # 0m:0.009s
            shell_command_1052_7134()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=ScriptCommand(r'echo "#!/bin/bash" >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"; echo installer -pkg \"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg\" -target / >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"; chmod a+rwx "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh" '), if_false=ShellCommand(r'sudo installer -pkg "/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg" -target /', message=r"Installing SoundGrid Driver V14.12", ignore_all_errors=True), prog_num=7135) as if_1053_7135:  # 0m:0.007s
            if_1053_7135()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudioModulesFolder_ScanView.txt", prog_num=7136) as rm_file_or_dir_1054_7136:  # 0m:0.000s
            rm_file_or_dir_1054_7136()
        with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/SampleTestConverter.bundle", prog_num=7137) as rm_file_or_dir_1055_7137:  # 0m:0.000s
            rm_file_or_dir_1055_7137()
        with ShellCommand(r"""osascript -e 'tell application "System Events" to delete login item "SoundGrid Studio"' """, ignore_all_errors=True, prog_num=7138) as shell_command_1056_7138:  # 0m:0.379s
            shell_command_1056_7138()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.NoSplashScreen.sh", prog_num=7139) as rm_file_or_dir_1057_7139:  # 0m:0.000s
            rm_file_or_dir_1057_7139()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGridStudioSilent.app", prog_num=7140) as rm_file_or_dir_1058_7140:  # 0m:0.000s
            rm_file_or_dir_1058_7140()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/SoundGridStudioSilent.app", prog_num=7141) as rm_file_or_dir_1059_7141:  # 0m:0.000s
            rm_file_or_dir_1059_7141()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=7142) as rm_file_or_dir_1060_7142:  # 0m:0.000s
            rm_file_or_dir_1060_7142()
        with ShellCommand(r'chmod a=r,u+w "/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=7143) as shell_command_1061_7143:  # 0m:0.011s
            shell_command_1061_7143()
        with If(IsFile(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudio.Mixer SoundGrid.preferences"), if_false=CopyFileToFile(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist", r"/${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=7144) as if_1062_7144:  # 0m:0.010s
            if_1062_7144()
        with ShellCommand(r'chmod a=r,u+w "${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=7145) as shell_command_1063_7145:  # 0m:0.009s
            shell_command_1063_7145()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid" -c', ignore_all_errors=True, prog_num=7146) as shell_command_1064_7146:  # 0m:0.094s
            shell_command_1064_7146()
        with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid"/Icon?; fi', prog_num=7147) as script_command_1065_7147:  # 0m:0.013s
            script_command_1065_7147()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=7148) as rm_file_or_dir_1066_7148:  # 0m:0.000s
            rm_file_or_dir_1066_7148()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=7149) as touch_1067_7149:  # 0m:0.000s
            touch_1067_7149()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst/Contents/Info.plist", Touch, r"path", prog_num=7150) as glober_1068_7150:  # 0m:0.001s
            glober_1068_7150()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=7151) as glober_1069_7151:  # 0m:0.000s
            glober_1069_7151()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=7152) as shell_command_1070_7152:  # 0m:2.898s
            shell_command_1070_7152()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V14" -c', ignore_all_errors=True, prog_num=7153) as shell_command_1071_7153:  # 0m:0.098s
            shell_command_1071_7153()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V14"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V14"/Icon?; fi', prog_num=7154) as script_command_1072_7154:  # 0m:0.012s
            script_command_1072_7154()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=7155) as if_1073_7155:  # 0m:0.000s
            if_1073_7155()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=7156) as if_1074_7156:  # 0m:0.000s
            if_1074_7156()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=7157) as if_1075_7157:  # 0m:0.000s
            if_1075_7157()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=7158) as if_1076_7158:  # 0m:0.000s
            if_1076_7158()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=7159) as make_dir_1077_7159:  # 0m:0.008s
            make_dir_1077_7159()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=7160) as chmod_1078_7160:  # 0m:0.000s
            chmod_1078_7160()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", prog_num=7161) as make_dir_1079_7161:  # 0m:0.000s
            make_dir_1079_7161()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=7162) as chmod_1080_7162:  # 0m:0.000s
            chmod_1080_7162()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=7163) as chmod_1081_7163:  # 0m:0.000s
            chmod_1081_7163()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=7164) as chmod_1082_7164:  # 0m:0.000s
            chmod_1082_7164()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=7165) as chmod_1083_7165:  # 0m:0.000s
            chmod_1083_7165()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=7166) as shell_command_1084_7166:  # 0m:0.121s
            shell_command_1084_7166()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=7167) as script_command_1085_7167:  # 0m:0.013s
            script_command_1085_7167()
    with Stage(r"post-copy", prog_num=7168):  # 0m:0.027s
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=7169) as make_dir_1086_7169:  # 0m:0.009s
            make_dir_1086_7169()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V14/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=7170) as copy_file_to_file_1087_7170:  # 0m:0.009s
            copy_file_to_file_1087_7170()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=7171) as chmod_1088_7171:  # 0m:0.000s
            chmod_1088_7171()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=7172) as chmod_1089_7172:  # 0m:0.000s
            chmod_1089_7172()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Library/Application Support/Waves/Central/V14/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=7173) as copy_file_to_file_1090_7173:  # 0m:0.000s
            copy_file_to_file_1090_7173()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=7174) as chmod_1091_7174:  # 0m:0.000s
            chmod_1091_7174()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml", hard_links=False, copy_owner=True, prog_num=7175) as copy_file_to_file_1092_7175:  # 0m:0.007s
            copy_file_to_file_1092_7175()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=7176) as chmod_1093_7176:  # 0m:0.000s
            chmod_1093_7176()
        Progress(r"Done copy", prog_num=7177)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=7178)()  # 0m:0.000s
    with Stage(r"post", prog_num=7179):  # 0m:0.045s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=7180) as make_dir_1094_7180:  # 0m:0.009s
            make_dir_1094_7180()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/V14_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=7181) as copy_file_to_file_1095_7181:  # 0m:0.007s
            copy_file_to_file_1095_7181()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=7182) as make_dir_1096_7182:  # 0m:0.006s
            make_dir_1096_7182()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=7183) as copy_file_to_file_1097_7183:  # 0m:0.008s
            copy_file_to_file_1097_7183()
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=7184) as make_dir_1098_7184:  # 0m:0.008s
            make_dir_1098_7184()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/180/index.yaml", r"/Library/Application Support/Waves/Central/V14/index.yaml", hard_links=False, copy_owner=True, prog_num=7185) as copy_file_to_file_1099_7185:  # 0m:0.007s
            copy_file_to_file_1099_7185()

with Stage(r"epilog", prog_num=7186):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011.py", prog_num=7187) as patch_py_batch_with_timings_1100_7187:  # ?
        patch_py_batch_with_timings_1100_7187()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 1667671796 bytes in 0m:20.434s, 81613209 bytes per second
# copy time 1m:35.223s
