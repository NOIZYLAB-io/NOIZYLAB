# Creation time: 06-09-25_12-24
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 6613
PythonBatchCommandBase.running_progress = 616
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=617):  # 0m:0.000s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac64", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac64")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250906122419"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", r"/Applications/Waves/Data/NKS FX")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 2
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"16.1.0"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V16", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V15", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V16", r"/Applications/Waves/WaveShells V16", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 19
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NzIxMTg1OX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU3MTc1NTU5fX19XX0_;CloudFront-Signature=DMSznZDSfBG1l61sIEYsakPtgVij1nDsgwRQJJaEEj1muBzptJ9g8VS41yoS0nIzdsmdPmuPMW58nEg9k7Nt5QogFULedZptp5XJV2pLFr4rauiWpzPzw89rgDhExUuTO7MeL6od9YoI-l~pnl5lcHfIonPEGD1NXroP64FMCyCVyl~NxsScw~XZbcQ0eakWj6j3TZbT3wblAhKaaxGGdQFGaiKXe5Mphc-a4LkpuCycOmyU-SfeUswDi-WZ~vj10rHs2WOehcC71RPh4F3PFbFLVuQGuJSwwkBx4Xoj7oezIKY-V1e2FzF1tyvU4lfmVdo4h2uOnGtUUsUz0lRwXw__"
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
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
    config_vars['HAVE_INFO_MAP_COPY_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FILE_NAME'] = r"have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FOR_COPY'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt"
    config_vars['HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['INDEX_CHECKSUM'] = r"4e73cfd164d791bf2ca8b305d869c06694774b74"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/19/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"acad9bc28601f35dc8b803b4398a3189323b5f41"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/19/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/19/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"in read_item_details_from_node 'common' was not identified correctly as current os"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"0386f35f-d467-42c1-9aa2-593d4f331cc6", r"51472ece-6f53-4926-8123-64330d6c6852", r"b158aea5-79f7-4a39-b9b9-f8c5e7c237c2", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"f4b4c760-76c5-4b08-b2f9-7df547f7bd19")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 19
    config_vars['MIN_REPO_REV'] = 2
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NEW_HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt"
    config_vars['NEW_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V16/new_require.yaml"
    config_vars['NI_SERVICE_CENTER'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NO_FLAGS_PATTERNS'] = (r"desktop.ini", r"*.ico")
    config_vars['NO_HARD_LINK_PATTERNS'] = (r"*Info.xml", r"*Info.plist", r"desktop.ini", r"*.ico")
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 2
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 4
    config_vars['OLD_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V16/old_require.yaml"
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250906122419.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 19
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-09-03 15:56:32.434034"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/19"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V16"
    config_vars['REQUIRE_REPO_REV'] = 32
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"d5c185dac2907e13705befd76e3560e63cd54e0d"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/19/instl/short-index.yaml"
    config_vars['SHOULD_NOT_BE_REQUIRED_BY'] = r"(Plugin\d+_\d+_Root_\d+_\d+_IID)|(GTR(_Internals|_Stomps|Solo_Stomps)_IID)"
    config_vars['SITE_BOOKKEEPING_DIR'] = r"/Library/Application Support"
    config_vars['SITE_HAVE_INFO_MAP_PATH'] = r"/Library/Application Support/Waves/Central/V16/have_info_map.txt"
    config_vars['SITE_REPO_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central/V16"
    config_vars['SITE_REQUIRE_FILE_NAME'] = r"require.yaml"
    config_vars['SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V16/require.yaml"
    config_vars['SITE_VENDOR_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central"
    config_vars['SOURCE_PREFIX'] = r"Mac"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16"
    config_vars['SYNC_BASE_URL_MAIN_ITEM'] = r"d36wza55md4dee.cloudfront.net"
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"before-copy-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac64", r"MacArm")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac64"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 5992
    config_vars['TO_SYNC_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/to_sync_info_map.txt"
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl"
    config_vars['USE_ZLIB'] = r"yes"
    config_vars['VENDOR_DIR_NAME'] = r"Waves/Central"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVES_APPS_DIR'] = r"/Applications/Waves/Applications V16"
    config_vars['WAVES_APPS_DIR_V10'] = r"/Applications/Waves/Applications V10"
    config_vars['WAVES_APPS_DIR_V11'] = r"/Applications/Waves/Applications V11"
    config_vars['WAVES_APPS_DIR_V12'] = r"/Applications/Waves/Applications V12"
    config_vars['WAVES_APPS_DIR_V13'] = r"/Applications/Waves/Applications V13"
    config_vars['WAVES_APPS_DIR_V14'] = r"/Applications/Waves/Applications V14"
    config_vars['WAVES_APPS_DIR_V15'] = r"/Applications/Waves/Applications V15"
    config_vars['WAVES_CENTRAL_EXTERNAL_DATA'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/data"
    config_vars['WAVES_CENTRAL_INSTALL_DIR'] = r"/Applications/Waves/Applications V16"
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
    config_vars['WAVES_PLUGINS_DIR'] = r"/Applications/Waves/Plug-Ins V16"
    config_vars['WAVES_PREFERENCES_DIR'] = r"/Users/rsp_ms/Library/Preferences/Waves Preferences"
    config_vars['WAVES_PROGRAMDATA_DIR'] = r"/Library/Application Support/Waves"
    config_vars['WAVES_SG_TEMPLATES_DIR'] = r"/Users/Shared/Waves/eMotion"
    config_vars['WAVES_SHARED_DIR'] = r"/Users/Shared/Waves"
    config_vars['WAVES_SHELLS_DIR'] = r"/Applications/Waves/WaveShells V16"
    config_vars['WAVES_SHELLS_DIR_V10'] = r"/Applications/Waves/WaveShells V10"
    config_vars['WAVES_SHELLS_DIR_V11'] = r"/Applications/Waves/WaveShells V11"
    config_vars['WAVES_SHELLS_DIR_V12'] = r"/Applications/Waves/WaveShells V12"
    config_vars['WAVES_SHELLS_DIR_V13'] = r"/Applications/Waves/WaveShells V13"
    config_vars['WAVES_SHELLS_DIR_V14'] = r"/Applications/Waves/WaveShells V14"
    config_vars['WAVES_SHELLS_DIR_V15'] = r"/Applications/Waves/WaveShells V15"
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
    config_vars['WAVES_UNUSED_PLUGINS_DIR'] = r"/Applications/Waves/Unused Plug-Ins V16"
    config_vars['WAVES_WPAPI_DIR'] = r"/Library/Audio/Plug-Ins/WPAPI"
    config_vars['WLE_EXEC_PATH'] = r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250906122419.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-08-23 23:57:51.343637"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.6.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac64", r"MacArm")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac64"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID"
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"AnalyzeAudioBundle_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_Data_Folders_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS_Models_Data_Folders_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"CR8_Sampler_Presets_IID", r"ChainersChildExcludeList_IID", r"Delete_Waves_Caches_IID", r"DemoMode_V16_1_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"Get_General_Icons_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InTrigger_Data_Folders_IID", r"InTrigger_IID", r"InTrigger_Live_IID", r"InTrigger_Live_Presets_IID", r"InTrigger_Presets_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"IntelDlls_IID", r"LicenseNotifications_V16_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"ORS_Modulators_Data_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_V16_1_IID", r"Shutdown_Servers_IID", r"V9_V10_Organizer_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AAX_16_1_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_AU_16_1_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_VST3_V16_1_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell1_WPAPI_2_16_1_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesLib1_16_0_23_IID", r"WavesLib1_16_1_99_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V16_1_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.2.1 2025-08-23 23:57:51.343637 bm-mac-ado12"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.2.1"
    config_vars['__INSTL_VERSION__'] = (2, 5, 2, 1)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"ewxksuyvehafqoir"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"COSMOS_Plugin_IID", r"COSMOS__IID", r"InPhase_IID", r"InPhase_LT_IID", r"InTrigger_IID", r"InTrigger_Live_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-09-06 12:25:57.207306"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"bm-mac-ado12"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19", r"/Library/Application Support/Waves/Central/V16", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"bm-mac-ado12"
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

with PythonBatchRuntime(r"synccopy", prog_num=618):  # 0m:21.786s
    with Stage(r"begin", prog_num=619):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=620):  # 0m:0.008s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=621) as copy_file_to_file_001_621:  # 0m:0.004s
            copy_file_to_file_001_621()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=622) as copy_file_to_file_002_622:  # 0m:0.004s
            copy_file_to_file_002_622()
    with Stage(r"sync", prog_num=623):  # 0m:3.108s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=624) as shell_command_003_624:  # 0m:0.009s
            shell_command_003_624()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=625) as shell_command_004_625:  # 0m:0.011s
            shell_command_004_625()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=626) as shell_command_005_626:  # 0m:0.950s
            shell_command_005_626()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=627) as shell_command_006_627:  # 0m:0.946s
            shell_command_006_627()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=628) as shell_command_007_628:  # 0m:0.007s
            shell_command_007_628()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=629) as shell_command_008_629:  # 0m:1.011s
            shell_command_008_629()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=630) as shell_command_009_630:  # 0m:0.007s
            shell_command_009_630()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=631) as shell_command_010_631:  # 0m:0.005s
            shell_command_010_631()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=632) as shell_command_011_632:  # 0m:0.149s
            shell_command_011_632()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=633):  # 0m:0.012s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=634) as make_dir_012_634:  # 0m:0.005s
                make_dir_012_634()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=635) as cd_013_635:  # 0m:0.007s
                cd_013_635()
                Progress(r"5529 files already in cache", own_progress_count=5529, prog_num=6164)()  # 0m:0.000s
                with Stage(r"post_sync", prog_num=6165):  # 0m:0.006s
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=6166) as copy_file_to_file_014_6166:  # 0m:0.006s
                        copy_file_to_file_014_6166()
            Progress(r"Done sync", prog_num=6167)()  # 0m:0.000s
    with Stage(r"copy", prog_num=6168):  # 0m:18.586s
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=6169) as run_in_thread_015_6169:  # 0m:0.000s
            run_in_thread_015_6169()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=6170)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=6171):  # 0m:0.106s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=6172) as make_dir_016_6172:  # 0m:0.004s
                make_dir_016_6172()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=6173) as make_dir_017_6173:  # 0m:0.004s
                make_dir_017_6173()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=6174) as make_dir_018_6174:  # 0m:0.004s
                make_dir_018_6174()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=6175) as make_dir_019_6175:  # 0m:0.006s
                make_dir_019_6175()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=6176) as make_dir_020_6176:  # 0m:0.004s
                make_dir_020_6176()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=6177) as make_dir_021_6177:  # 0m:0.004s
                make_dir_021_6177()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=6178) as make_dir_022_6178:  # 0m:0.004s
                make_dir_022_6178()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=6179) as make_dir_023_6179:  # 0m:0.004s
                make_dir_023_6179()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=6180) as make_dir_024_6180:  # 0m:0.005s
                make_dir_024_6180()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=6181) as make_dir_025_6181:  # 0m:0.005s
                make_dir_025_6181()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=6182) as make_dir_026_6182:  # 0m:0.005s
                make_dir_026_6182()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=6183) as make_dir_027_6183:  # 0m:0.005s
                make_dir_027_6183()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=6184) as make_dir_028_6184:  # 0m:0.004s
                make_dir_028_6184()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=6185) as make_dir_029_6185:  # 0m:0.005s
                make_dir_029_6185()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=6186) as make_dir_030_6186:  # 0m:0.004s
                make_dir_030_6186()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=6187) as make_dir_031_6187:  # 0m:0.004s
                make_dir_031_6187()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=6188) as make_dir_032_6188:  # 0m:0.004s
                make_dir_032_6188()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=6189) as make_dir_033_6189:  # 0m:0.004s
                make_dir_033_6189()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=6190) as make_dir_034_6190:  # 0m:0.004s
                make_dir_034_6190()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=6191) as make_dir_035_6191:  # 0m:0.004s
                make_dir_035_6191()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=6192) as make_dir_036_6192:  # 0m:0.004s
                make_dir_036_6192()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=6193) as make_dir_037_6193:  # 0m:0.005s
                make_dir_037_6193()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=6194) as make_dir_038_6194:  # 0m:0.004s
                make_dir_038_6194()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=6195) as make_dir_039_6195:  # 0m:0.005s
                make_dir_039_6195()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=6196) as rm_file_or_dir_040_6196:  # 0m:0.000s
            rm_file_or_dir_040_6196()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=6197) as shell_command_041_6197:  # 0m:0.009s
            shell_command_041_6197()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=6198) as shell_command_042_6198:  # 0m:0.014s
            shell_command_042_6198()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=6199) as shell_command_043_6199:  # 0m:1.096s
            shell_command_043_6199()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=6200) as shell_command_044_6200:  # 0m:1.132s
            shell_command_044_6200()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=6201) as shell_command_045_6201:  # 0m:0.006s
            shell_command_045_6201()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=6202) as shell_command_046_6202:  # 0m:1.046s
            shell_command_046_6202()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=6203) as shell_command_047_6203:  # 0m:0.006s
            shell_command_047_6203()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=6204) as shell_command_048_6204:  # 0m:0.008s
            shell_command_048_6204()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=6205) as shell_command_049_6205:  # 0m:0.168s
            shell_command_049_6205()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=6206) as cd_stage_050_6206:  # 0m:0.012s
            cd_stage_050_6206()
            with SetExecPermissionsInSyncFolder(prog_num=6207) as set_exec_permissions_in_sync_folder_051_6207:  # 0m:0.011s
                set_exec_permissions_in_sync_folder_051_6207()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=6208) as cd_stage_052_6208:  # 0m:0.044s
            cd_stage_052_6208()
            with Stage(r"copy", r"COSMOS__Application v16.0.50.51", prog_num=6209):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=6210) as should_copy_source_053_6210:  # ?
                    should_copy_source_053_6210()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=6211):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=6212) as copy_dir_to_dir_054_6212:  # ?
                            copy_dir_to_dir_054_6212()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=6213) as unwtar_055_6213:  # ?
                            unwtar_055_6213()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=6214, recursive=True) as chown_056_6214:  # 0m:0.002s
                            chown_056_6214()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=6224) as resolve_symlink_files_in_folder_057_6224:  # 0m:0.042s
                resolve_symlink_files_in_folder_057_6224()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=6225) as cd_stage_058_6225:  # 0m:0.028s
            cd_stage_058_6225()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=6226):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6227) as should_copy_source_059_6227:  # ?
                    should_copy_source_059_6227()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=6228):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=6229) as copy_dir_to_dir_060_6229:  # ?
                            copy_dir_to_dir_060_6229()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=6230, recursive=True) as chown_061_6230:  # 0m:0.001s
                            chown_061_6230()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=6231):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=6232) as should_copy_source_062_6232:  # ?
                    should_copy_source_062_6232()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=6233):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=6234) as copy_dir_to_dir_063_6234:  # ?
                            copy_dir_to_dir_063_6234()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=6235) as unwtar_064_6235:  # ?
                            unwtar_064_6235()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=6236, recursive=True) as chown_065_6236:  # 0m:0.000s
                            chown_065_6236()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.2", prog_num=6237):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6238) as should_copy_source_066_6238:  # ?
                    should_copy_source_066_6238()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=6239):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=6240) as copy_dir_to_dir_067_6240:  # ?
                            copy_dir_to_dir_067_6240()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=6241, recursive=True) as chown_068_6241:  # 0m:0.000s
                            chown_068_6241()
            with Stage(r"copy", r"InTrigger__Data_Folders v1.0.0.3", prog_num=6242):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/InTrigger", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6243) as should_copy_source_069_6243:  # ?
                    should_copy_source_069_6243()
                    with Stage(r"copy source", r"Common/Data/InTrigger", prog_num=6244):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/InTrigger", r".", delete_extraneous_files=True, prog_num=6245) as copy_dir_to_dir_070_6245:  # ?
                            copy_dir_to_dir_070_6245()
                        with Chown(path=r"/Applications/Waves/Data/InTrigger", user_id=-1, group_id=-1, prog_num=6246, recursive=True) as chown_071_6246:  # 0m:0.000s
                            chown_071_6246()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=6247):  # 0m:0.023s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6248) as should_copy_source_072_6248:  # 0m:0.023s
                    should_copy_source_072_6248()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=6249):  # 0m:0.022s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=6250) as copy_dir_to_dir_073_6250:  # 0m:0.022s
                            copy_dir_to_dir_073_6250()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=6251, recursive=True) as chown_074_6251:  # 0m:0.000s
                            chown_074_6251()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=6252) as cd_stage_075_6252:  # 0m:0.002s
            cd_stage_075_6252()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=6253):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6254) as should_copy_source_076_6254:  # ?
                    should_copy_source_076_6254()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=6255):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=6256) as copy_dir_to_dir_077_6256:  # ?
                            copy_dir_to_dir_077_6256()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=6257, recursive=True) as chown_078_6257:  # 0m:0.001s
                            chown_078_6257()
            with Stage(r"copy", r"InTrigger Live Presets v1.0.0.4", prog_num=6258):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger Live", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6259) as should_copy_source_079_6259:  # ?
                    should_copy_source_079_6259()
                    with Stage(r"copy source", r"Common/Data/Presets/InTrigger Live", prog_num=6260):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger Live", r".", delete_extraneous_files=True, prog_num=6261) as copy_dir_to_dir_080_6261:  # ?
                            copy_dir_to_dir_080_6261()
                        with Chown(path=r"/Applications/Waves/Data/Presets/InTrigger Live", user_id=-1, group_id=-1, prog_num=6262, recursive=True) as chown_081_6262:  # 0m:0.001s
                            chown_081_6262()
            with Stage(r"copy", r"InTrigger Presets v1.0.0.4", prog_num=6263):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6264) as should_copy_source_082_6264:  # ?
                    should_copy_source_082_6264()
                    with Stage(r"copy source", r"Common/Data/Presets/InTrigger", prog_num=6265):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger", r".", delete_extraneous_files=True, prog_num=6266) as copy_dir_to_dir_083_6266:  # ?
                            copy_dir_to_dir_083_6266()
                        with Chown(path=r"/Applications/Waves/Data/Presets/InTrigger", user_id=-1, group_id=-1, prog_num=6267, recursive=True) as chown_084_6267:  # 0m:0.000s
                            chown_084_6267()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=6268) as cd_stage_085_6268:  # 0m:3.756s
            cd_stage_085_6268()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=6269):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6270) as should_copy_source_086_6270:  # ?
                    should_copy_source_086_6270()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=6271):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=6272) as copy_dir_to_dir_087_6272:  # ?
                            copy_dir_to_dir_087_6272()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=6273) as unwtar_088_6273:  # ?
                            unwtar_088_6273()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=6274, recursive=True) as chown_089_6274:  # 0m:0.001s
                            chown_089_6274()
            with Stage(r"copy", r"InPhase v16.0.23.24", prog_num=6275):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6276) as should_copy_source_090_6276:  # ?
                    should_copy_source_090_6276()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=6277):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=6278) as copy_dir_to_dir_091_6278:  # ?
                            copy_dir_to_dir_091_6278()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=6279) as unwtar_092_6279:  # ?
                            unwtar_092_6279()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase.bundle", user_id=-1, group_id=-1, prog_num=6280, recursive=True) as chown_093_6280:  # 0m:0.000s
                            chown_093_6280()
            with Stage(r"copy", r"InPhase LT v16.0.23.24", prog_num=6281):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6282) as should_copy_source_094_6282:  # ?
                    should_copy_source_094_6282()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=6283):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=6284) as copy_dir_to_dir_095_6284:  # ?
                            copy_dir_to_dir_095_6284()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=6285) as unwtar_096_6285:  # ?
                            unwtar_096_6285()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=6286, recursive=True) as chown_097_6286:  # 0m:0.001s
                            chown_097_6286()
            with Stage(r"copy", r"InTrigger v16.1.99.101", prog_num=6287):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6288) as should_copy_source_098_6288:  # ?
                    should_copy_source_098_6288()
                    with Stage(r"copy source", r"Mac/Plugins/InTrigger.bundle", prog_num=6289):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", r".", delete_extraneous_files=True, prog_num=6290) as copy_dir_to_dir_099_6290:  # ?
                            copy_dir_to_dir_099_6290()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", where_to_unwtar=r".", prog_num=6291) as unwtar_100_6291:  # ?
                            unwtar_100_6291()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InTrigger.bundle", user_id=-1, group_id=-1, prog_num=6292, recursive=True) as chown_101_6292:  # 0m:0.000s
                            chown_101_6292()
            with Stage(r"copy", r"InTrigger Live v16.1.99.101", prog_num=6293):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6294) as should_copy_source_102_6294:  # ?
                    should_copy_source_102_6294()
                    with Stage(r"copy source", r"Mac/Plugins/InTrigger Live.bundle", prog_num=6295):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", r".", delete_extraneous_files=True, prog_num=6296) as copy_dir_to_dir_103_6296:  # ?
                            copy_dir_to_dir_103_6296()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", where_to_unwtar=r".", prog_num=6297) as unwtar_104_6297:  # ?
                            unwtar_104_6297()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InTrigger Live.bundle", user_id=-1, group_id=-1, prog_num=6298, recursive=True) as chown_105_6298:  # 0m:0.001s
                            chown_105_6298()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=6299):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6300) as should_copy_source_106_6300:  # ?
                    should_copy_source_106_6300()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=6301):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=6302) as copy_dir_to_dir_107_6302:  # ?
                            copy_dir_to_dir_107_6302()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=6303) as unwtar_108_6303:  # ?
                            unwtar_108_6303()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=6304, recursive=True) as chown_109_6304:  # 0m:0.000s
                            chown_109_6304()
            with Stage(r"copy", r"WavesLib1_16_1_99_101 v16.1.99.101", prog_num=6305):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=6306) as should_copy_source_110_6306:  # ?
                    should_copy_source_110_6306()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.1.99.framework", prog_num=6307):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", r".", delete_extraneous_files=True, prog_num=6308) as copy_dir_to_dir_111_6308:  # ?
                            copy_dir_to_dir_111_6308()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", where_to_unwtar=r".", prog_num=6309) as unwtar_112_6309:  # ?
                            unwtar_112_6309()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.1.99.framework", user_id=-1, group_id=-1, prog_num=6310, recursive=True) as chown_113_6310:  # 0m:0.003s
                            chown_113_6310()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=4, prog_num=6314) as resolve_symlink_files_in_folder_114_6314:  # 0m:3.296s
                resolve_symlink_files_in_folder_114_6314()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=6315) as shell_command_115_6315:  # 0m:0.105s
                shell_command_115_6315()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=6316) as script_command_116_6316:  # 0m:0.009s
                script_command_116_6316()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6317) as shell_command_117_6317:  # 0m:0.022s
                shell_command_117_6317()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=6318) as create_symlink_118_6318:  # 0m:0.001s
                create_symlink_118_6318()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=6319) as create_symlink_119_6319:  # 0m:0.000s
                create_symlink_119_6319()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=6320) as copy_glob_to_dir_120_6320:  # 0m:0.316s
                copy_glob_to_dir_120_6320()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=6321) as cd_stage_121_6321:  # 0m:0.001s
            cd_stage_121_6321()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=6322):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=6323) as should_copy_source_122_6323:  # ?
                    should_copy_source_122_6323()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=6324):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=6325) as copy_file_to_dir_123_6325:  # ?
                            copy_file_to_dir_123_6325()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6326) as chmod_and_chown_124_6326:  # 0m:0.000s
                            chmod_and_chown_124_6326()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=6327) as cd_stage_125_6327:  # 0m:0.020s
            cd_stage_125_6327()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.78.79", prog_num=6328):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=6329) as should_copy_source_126_6329:  # ?
                    should_copy_source_126_6329()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=6330):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=6331) as copy_dir_to_dir_127_6331:  # ?
                            copy_dir_to_dir_127_6331()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=6332) as unwtar_128_6332:  # ?
                            unwtar_128_6332()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=6333, recursive=True) as chown_129_6333:  # ?
                            chown_129_6333()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=6334) as shell_command_130_6334:  # 0m:0.001s
                            shell_command_130_6334()
            with Stage(r"copy", r"WaveShell1-AAX 16.1 v16.1.77.79", prog_num=6335):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=6336) as should_copy_source_131_6336:  # ?
                    should_copy_source_131_6336()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", prog_num=6337):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r".", delete_extraneous_files=True, prog_num=6338) as copy_dir_to_dir_132_6338:  # ?
                            copy_dir_to_dir_132_6338()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", where_to_unwtar=r".", prog_num=6339) as unwtar_133_6339:  # ?
                            unwtar_133_6339()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.1.aaxplugin", user_id=-1, group_id=-1, prog_num=6340, recursive=True) as chown_134_6340:  # ?
                            chown_134_6340()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.1.aaxplugin"', ignore_all_errors=True, prog_num=6341) as shell_command_135_6341:  # 0m:0.001s
                            shell_command_135_6341()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=6342):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=6343) as should_copy_source_136_6343:  # ?
                    should_copy_source_136_6343()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=6344):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=6345) as copy_dir_to_dir_137_6345:  # ?
                            copy_dir_to_dir_137_6345()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=6346) as unwtar_138_6346:  # ?
                            unwtar_138_6346()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=6347, recursive=True) as chown_139_6347:  # ?
                            chown_139_6347()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=6348) as break_hard_link_140_6348:  # ?
                            break_hard_link_140_6348()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=6349) as shell_command_141_6349:  # ?
                            shell_command_141_6349()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=6350, recursive=True) as chown_142_6350:  # ?
                            chown_142_6350()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=6351, recursive=True) as chmod_143_6351:  # 0m:0.002s
                            chmod_143_6351()
            with Stage(r"copy", r"WaveShell1-AU 16.1 v16.1.77.79", prog_num=6352):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=6353) as should_copy_source_144_6353:  # ?
                    should_copy_source_144_6353()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.1.component", prog_num=6354):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r".", delete_extraneous_files=True, prog_num=6355) as copy_dir_to_dir_145_6355:  # ?
                            copy_dir_to_dir_145_6355()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", where_to_unwtar=r".", prog_num=6356) as unwtar_146_6356:  # ?
                            unwtar_146_6356()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=6357, recursive=True) as chown_147_6357:  # ?
                            chown_147_6357()
                        with BreakHardLink(r"WaveShell1-AU 16.1.component/Contents/Info.plist", prog_num=6358) as break_hard_link_148_6358:  # ?
                            break_hard_link_148_6358()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.1.component"', ignore_all_errors=True, prog_num=6359) as shell_command_149_6359:  # ?
                            shell_command_149_6359()
                        with Chown(path=r"WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=6360, recursive=True) as chown_150_6360:  # ?
                            chown_150_6360()
                        with Chmod(path=r"WaveShell1-AU 16.1.component", mode="a+rwX", prog_num=6361, recursive=True) as chmod_151_6361:  # 0m:0.003s
                            chmod_151_6361()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.91.92", prog_num=6362):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=6363) as should_copy_source_152_6363:  # ?
                    should_copy_source_152_6363()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=6364):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=6365) as copy_dir_to_dir_153_6365:  # ?
                            copy_dir_to_dir_153_6365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=6366) as unwtar_154_6366:  # ?
                            unwtar_154_6366()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=6367, recursive=True) as chown_155_6367:  # ?
                            chown_155_6367()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=6368) as shell_command_156_6368:  # 0m:0.001s
                            shell_command_156_6368()
            with Stage(r"copy", r"WaveShell1-VST3 16.1 v16.1.77.79", prog_num=6369):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=6370) as should_copy_source_157_6370:  # ?
                    should_copy_source_157_6370()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.1.vst3", prog_num=6371):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r".", delete_extraneous_files=True, prog_num=6372) as copy_dir_to_dir_158_6372:  # ?
                            copy_dir_to_dir_158_6372()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", where_to_unwtar=r".", prog_num=6373) as unwtar_159_6373:  # ?
                            unwtar_159_6373()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.1.vst3", user_id=-1, group_id=-1, prog_num=6374, recursive=True) as chown_160_6374:  # ?
                            chown_160_6374()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.1.vst3"', ignore_all_errors=True, prog_num=6375) as shell_command_161_6375:  # 0m:0.001s
                            shell_command_161_6375()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=6376):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=6377) as should_copy_source_162_6377:  # ?
                    should_copy_source_162_6377()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=6378):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=6379) as copy_dir_to_dir_163_6379:  # ?
                            copy_dir_to_dir_163_6379()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=6380) as unwtar_164_6380:  # ?
                            unwtar_164_6380()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=6381, recursive=True) as chown_165_6381:  # ?
                            chown_165_6381()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6382) as shell_command_166_6382:  # ?
                            shell_command_166_6382()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6383) as script_command_167_6383:  # ?
                            script_command_167_6383()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6384) as shell_command_168_6384:  # 0m:0.001s
                            shell_command_168_6384()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.1 v16.1.77.79", prog_num=6385):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=6386) as should_copy_source_169_6386:  # ?
                    should_copy_source_169_6386()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", prog_num=6387):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r".", delete_extraneous_files=True, prog_num=6388) as copy_dir_to_dir_170_6388:  # ?
                            copy_dir_to_dir_170_6388()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", where_to_unwtar=r".", prog_num=6389) as unwtar_171_6389:  # ?
                            unwtar_171_6389()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.1.bundle", user_id=-1, group_id=-1, prog_num=6390, recursive=True) as chown_172_6390:  # ?
                            chown_172_6390()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6391) as shell_command_173_6391:  # ?
                            shell_command_173_6391()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6392) as script_command_174_6392:  # ?
                            script_command_174_6392()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6393) as shell_command_175_6393:  # 0m:0.001s
                            shell_command_175_6393()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=6394):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=6395) as should_copy_source_176_6395:  # ?
                    should_copy_source_176_6395()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=6396):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=6397) as copy_dir_to_dir_177_6397:  # ?
                            copy_dir_to_dir_177_6397()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=6398) as unwtar_178_6398:  # ?
                            unwtar_178_6398()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=6399, recursive=True) as chown_179_6399:  # 0m:0.001s
                            chown_179_6399()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=6400) as shell_command_180_6400:  # 0m:0.008s
                shell_command_180_6400()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=6401) as cd_stage_181_6401:  # 0m:0.003s
            cd_stage_181_6401()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.78.79", prog_num=6402):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=6403) as should_copy_source_182_6403:  # ?
                    should_copy_source_182_6403()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=6404):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=6405) as copy_dir_to_dir_183_6405:  # ?
                            copy_dir_to_dir_183_6405()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=6406) as unwtar_184_6406:  # ?
                            unwtar_184_6406()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=6407, recursive=True) as chown_185_6407:  # ?
                            chown_185_6407()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=6408) as shell_command_186_6408:  # 0m:0.001s
                            shell_command_186_6408()
            with Stage(r"copy", r"WaveShell1-AAX 16.1 v16.1.77.79", prog_num=6409):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=6410) as should_copy_source_187_6410:  # ?
                    should_copy_source_187_6410()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", prog_num=6411):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r".", delete_extraneous_files=True, prog_num=6412) as copy_dir_to_dir_188_6412:  # ?
                            copy_dir_to_dir_188_6412()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", where_to_unwtar=r".", prog_num=6413) as unwtar_189_6413:  # ?
                            unwtar_189_6413()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.1.aaxplugin", user_id=-1, group_id=-1, prog_num=6414, recursive=True) as chown_190_6414:  # ?
                            chown_190_6414()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.1.aaxplugin"', ignore_all_errors=True, prog_num=6415) as shell_command_191_6415:  # 0m:0.001s
                            shell_command_191_6415()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=6416) as cd_stage_192_6416:  # 0m:0.006s
            cd_stage_192_6416()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=6417):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=6418) as should_copy_source_193_6418:  # ?
                    should_copy_source_193_6418()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=6419):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=6420) as copy_file_to_dir_194_6420:  # ?
                            copy_file_to_dir_194_6420()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=6421) as chmod_and_chown_195_6421:  # 0m:0.001s
                            chmod_and_chown_195_6421()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=6422) as resolve_config_vars_in_file_196_6422:  # 0m:0.002s
                resolve_config_vars_in_file_196_6422()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=6423) as if_197_6423:  # 0m:0.001s
                if_197_6423()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=6424) as cd_stage_198_6424:  # 0m:0.001s
            cd_stage_198_6424()
            with Stage(r"copy", r"COSMOS_HTML v2.6.6", prog_num=6425):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=6426) as should_copy_source_199_6426:  # ?
                    should_copy_source_199_6426()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=6427):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=6428) as copy_dir_to_dir_200_6428:  # ?
                            copy_dir_to_dir_200_6428()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=6429, recursive=True) as chown_201_6429:  # 0m:0.001s
                            chown_201_6429()
            with Stage(r"copy", r"COSMOS_python v2.7.7", prog_num=6430):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=6431) as should_copy_source_202_6431:  # ?
                    should_copy_source_202_6431()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=6432):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=6433) as copy_dir_to_dir_203_6433:  # ?
                            copy_dir_to_dir_203_6433()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=6434) as unwtar_204_6434:  # ?
                            unwtar_204_6434()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=6435, recursive=True) as chown_205_6435:  # 0m:0.000s
                            chown_205_6435()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=6436) as cd_stage_206_6436:  # 0m:0.001s
            cd_stage_206_6436()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=6437):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=6438) as should_copy_source_207_6438:  # ?
                    should_copy_source_207_6438()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=6439):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=6440) as copy_dir_to_dir_208_6440:  # ?
                            copy_dir_to_dir_208_6440()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=6441) as unwtar_209_6441:  # ?
                            unwtar_209_6441()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=6442, recursive=True) as chown_210_6442:  # 0m:0.000s
                            chown_210_6442()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=6443) as cd_stage_211_6443:  # 0m:0.001s
            cd_stage_211_6443()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=6444):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=6445) as should_copy_source_212_6445:  # ?
                    should_copy_source_212_6445()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=6446):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=6447) as copy_dir_to_dir_213_6447:  # ?
                            copy_dir_to_dir_213_6447()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=6448, recursive=True) as chown_214_6448:  # 0m:0.000s
                            chown_214_6448()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=6449) as cd_stage_215_6449:  # 0m:0.001s
            cd_stage_215_6449()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=6450):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=6451) as should_copy_source_216_6451:  # ?
                    should_copy_source_216_6451()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=6452):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=6453) as copy_dir_to_dir_217_6453:  # ?
                            copy_dir_to_dir_217_6453()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=6454, recursive=True) as chown_218_6454:  # 0m:0.000s
                            chown_218_6454()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=6455) as cd_stage_219_6455:  # 0m:4.468s
            cd_stage_219_6455()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=6456) as rm_file_or_dir_220_6456:  # 0m:0.000s
                rm_file_or_dir_220_6456()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=6457):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=6458) as should_copy_source_221_6458:  # ?
                    should_copy_source_221_6458()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=6459):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6460) as copy_dir_to_dir_222_6460:  # ?
                            copy_dir_to_dir_222_6460()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=6461) as unwtar_223_6461:  # ?
                            unwtar_223_6461()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=6462, recursive=True) as chown_224_6462:  # 0m:0.001s
                            chown_224_6462()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=6463):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=6464) as should_copy_source_225_6464:  # 0m:0.004s
                    should_copy_source_225_6464()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=6465):  # 0m:0.004s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=6466) as unwtar_226_6466:  # 0m:0.004s
                            unwtar_226_6466()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=6467):  # 0m:4.436s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=6468) as should_copy_source_227_6468:  # 0m:4.436s
                    should_copy_source_227_6468()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=6469):  # 0m:4.435s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=6470) as copy_dir_to_dir_228_6470:  # 0m:0.012s
                            copy_dir_to_dir_228_6470()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=6471) as unwtar_229_6471:  # 0m:4.422s
                            unwtar_229_6471()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=6472, recursive=True) as chown_230_6472:  # 0m:0.000s
                            chown_230_6472()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=6473):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=6474) as should_copy_source_231_6474:  # ?
                    should_copy_source_231_6474()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=6475):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6476) as copy_dir_to_dir_232_6476:  # ?
                            copy_dir_to_dir_232_6476()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=6477) as chmod_233_6477:  # ?
                            chmod_233_6477()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=6478) as chmod_234_6478:  # ?
                            chmod_234_6478()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=6479, recursive=True) as chown_235_6479:  # 0m:0.001s
                            chown_235_6479()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=6482) as resolve_symlink_files_in_folder_236_6482:  # 0m:0.015s
                resolve_symlink_files_in_folder_236_6482()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6483) as shell_command_237_6483:  # 0m:0.010s
                shell_command_237_6483()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=6484) as cd_stage_238_6484:  # 0m:0.002s
            cd_stage_238_6484()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=6485):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=6486) as should_copy_source_239_6486:  # ?
                    should_copy_source_239_6486()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=6487):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=6488) as copy_dir_to_dir_240_6488:  # ?
                            copy_dir_to_dir_240_6488()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=6489, recursive=True) as chown_241_6489:  # 0m:0.001s
                            chown_241_6489()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=6490) as cd_stage_242_6490:  # 0m:0.005s
            cd_stage_242_6490()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=6491):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=6492) as should_copy_source_243_6492:  # ?
                    should_copy_source_243_6492()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=6493):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=6494, recursive=True) as chmod_244_6494:  # ?
                            chmod_244_6494()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6495) as copy_dir_to_dir_245_6495:  # ?
                            copy_dir_to_dir_245_6495()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=6496) as unwtar_246_6496:  # ?
                            unwtar_246_6496()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=6497, recursive=True) as chown_247_6497:  # ?
                            chown_247_6497()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=6498) as if_248_6498:  # 0m:0.001s
                            if_248_6498()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=6499) as cd_stage_249_6499:  # 0m:0.001s
            cd_stage_249_6499()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=6500):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=6501) as should_copy_source_250_6501:  # ?
                    should_copy_source_250_6501()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=6502):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=6503, recursive=True) as chmod_251_6503:  # ?
                            chmod_251_6503()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6504) as copy_dir_to_dir_252_6504:  # ?
                            copy_dir_to_dir_252_6504()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=6505) as unwtar_253_6505:  # ?
                            unwtar_253_6505()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=6506, recursive=True) as chown_254_6506:  # ?
                            chown_254_6506()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=6507) as if_255_6507:  # 0m:0.001s
                            if_255_6507()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=6508) as cd_stage_256_6508:  # 0m:2.230s
            cd_stage_256_6508()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=6509):  # 0m:1.156s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=6510) as should_copy_source_257_6510:  # 0m:1.156s
                    should_copy_source_257_6510()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=6511):  # 0m:1.155s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=6512) as copy_dir_to_dir_258_6512:  # 0m:0.170s
                            copy_dir_to_dir_258_6512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=6513) as unwtar_259_6513:  # 0m:0.914s
                            unwtar_259_6513()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=6514, recursive=True) as chown_260_6514:  # 0m:0.000s
                            chown_260_6514()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=6515) as break_hard_link_261_6515:  # 0m:0.013s
                            break_hard_link_261_6515()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=6516) as shell_command_262_6516:  # 0m:0.049s
                            shell_command_262_6516()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=6517, recursive=True) as chown_263_6517:  # 0m:0.000s
                            chown_263_6517()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=6518, recursive=True) as chmod_264_6518:  # 0m:0.008s
                            chmod_264_6518()
            with Stage(r"copy", r"WaveShell1-AU 16.1 v16.1.77.79", prog_num=6519):  # 0m:1.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=6520) as should_copy_source_265_6520:  # 0m:1.073s
                    should_copy_source_265_6520()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.1.component", prog_num=6521):  # 0m:1.073s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r".", delete_extraneous_files=True, prog_num=6522) as copy_dir_to_dir_266_6522:  # 0m:0.030s
                            copy_dir_to_dir_266_6522()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", where_to_unwtar=r".", prog_num=6523) as unwtar_267_6523:  # 0m:0.963s
                            unwtar_267_6523()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=6524, recursive=True) as chown_268_6524:  # 0m:0.000s
                            chown_268_6524()
                        with BreakHardLink(r"WaveShell1-AU 16.1.component/Contents/Info.plist", prog_num=6525) as break_hard_link_269_6525:  # 0m:0.018s
                            break_hard_link_269_6525()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.1.component"', ignore_all_errors=True, prog_num=6526) as shell_command_270_6526:  # 0m:0.051s
                            shell_command_270_6526()
                        with Chown(path=r"WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=6527, recursive=True) as chown_271_6527:  # 0m:0.000s
                            chown_271_6527()
                        with Chmod(path=r"WaveShell1-AU 16.1.component", mode="a+rwX", prog_num=6528, recursive=True) as chmod_272_6528:  # 0m:0.010s
                            chmod_272_6528()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=6529) as cd_stage_273_6529:  # 0m:0.003s
            cd_stage_273_6529()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.91.92", prog_num=6530):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=6531) as should_copy_source_274_6531:  # ?
                    should_copy_source_274_6531()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=6532):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=6533) as copy_dir_to_dir_275_6533:  # ?
                            copy_dir_to_dir_275_6533()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=6534) as unwtar_276_6534:  # ?
                            unwtar_276_6534()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=6535, recursive=True) as chown_277_6535:  # ?
                            chown_277_6535()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=6536) as shell_command_278_6536:  # 0m:0.001s
                            shell_command_278_6536()
            with Stage(r"copy", r"WaveShell1-VST3 16.1 v16.1.77.79", prog_num=6537):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=6538) as should_copy_source_279_6538:  # ?
                    should_copy_source_279_6538()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.1.vst3", prog_num=6539):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r".", delete_extraneous_files=True, prog_num=6540) as copy_dir_to_dir_280_6540:  # ?
                            copy_dir_to_dir_280_6540()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", where_to_unwtar=r".", prog_num=6541) as unwtar_281_6541:  # ?
                            unwtar_281_6541()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.1.vst3", user_id=-1, group_id=-1, prog_num=6542, recursive=True) as chown_282_6542:  # ?
                            chown_282_6542()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.1.vst3"', ignore_all_errors=True, prog_num=6543) as shell_command_283_6543:  # 0m:0.001s
                            shell_command_283_6543()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6544) as cd_stage_284_6544:  # 0m:0.008s
            cd_stage_284_6544()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=6545):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=6546) as should_copy_source_285_6546:  # ?
                    should_copy_source_285_6546()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=6547):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=6548) as copy_dir_to_dir_286_6548:  # ?
                            copy_dir_to_dir_286_6548()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=6549) as unwtar_287_6549:  # ?
                            unwtar_287_6549()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=6550, recursive=True) as chown_288_6550:  # ?
                            chown_288_6550()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6551) as shell_command_289_6551:  # ?
                            shell_command_289_6551()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6552) as script_command_290_6552:  # ?
                            script_command_290_6552()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6553) as shell_command_291_6553:  # 0m:0.001s
                            shell_command_291_6553()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.1 v16.1.77.79", prog_num=6554):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=6555) as should_copy_source_292_6555:  # ?
                    should_copy_source_292_6555()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", prog_num=6556):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r".", delete_extraneous_files=True, prog_num=6557) as copy_dir_to_dir_293_6557:  # ?
                            copy_dir_to_dir_293_6557()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", where_to_unwtar=r".", prog_num=6558) as unwtar_294_6558:  # ?
                            unwtar_294_6558()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", user_id=-1, group_id=-1, prog_num=6559, recursive=True) as chown_295_6559:  # ?
                            chown_295_6559()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6560) as shell_command_296_6560:  # ?
                            shell_command_296_6560()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6561) as script_command_297_6561:  # ?
                            script_command_297_6561()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6562) as shell_command_298_6562:  # 0m:0.004s
                            shell_command_298_6562()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6563) as create_symlink_299_6563:  # 0m:0.001s
                create_symlink_299_6563()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6564) as create_symlink_300_6564:  # 0m:0.001s
                create_symlink_300_6564()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=6565) as shell_command_301_6565:  # 0m:0.003s
            shell_command_301_6565()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=6566) as shell_command_302_6566:  # 0m:0.116s
            shell_command_302_6566()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=6567) as script_command_303_6567:  # 0m:0.011s
            script_command_303_6567()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=6568) as rm_file_or_dir_304_6568:  # 0m:0.030s
            rm_file_or_dir_304_6568()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=6569) as shell_command_305_6569:  # 0m:0.112s
            shell_command_305_6569()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=6570) as script_command_306_6570:  # 0m:0.009s
            script_command_306_6570()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=6571) as rm_file_or_dir_307_6571:  # 0m:0.001s
            rm_file_or_dir_307_6571()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=6572) as glober_308_6572:  # 0m:0.009s
            glober_308_6572()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=6573) as glober_309_6573:  # 0m:0.004s
            glober_309_6573()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=6574) as glober_310_6574:  # 0m:0.009s
            glober_310_6574()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=6575) as shell_command_311_6575:  # 0m:0.007s
            shell_command_311_6575()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=6576) as shell_command_312_6576:  # 0m:3.047s
            shell_command_312_6576()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=6577) as shell_command_313_6577:  # 0m:0.117s
            shell_command_313_6577()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=6578) as shell_command_314_6578:  # 0m:0.687s
            shell_command_314_6578()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=6579) as shell_command_315_6579:  # 0m:0.102s
            shell_command_315_6579()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=6580) as script_command_316_6580:  # 0m:0.008s
            script_command_316_6580()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=6581) as if_317_6581:  # 0m:0.001s
            if_317_6581()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=6582) as if_318_6582:  # 0m:0.000s
            if_318_6582()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=6583) as if_319_6583:  # 0m:0.000s
            if_319_6583()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=6584) as if_320_6584:  # 0m:0.000s
            if_320_6584()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=6585) as make_dir_321_6585:  # 0m:0.006s
            make_dir_321_6585()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=6586) as chmod_322_6586:  # 0m:0.000s
            chmod_322_6586()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=6587) as make_dir_323_6587:  # 0m:0.005s
            make_dir_323_6587()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=6588) as chmod_324_6588:  # 0m:0.000s
            chmod_324_6588()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=6589) as chmod_325_6589:  # 0m:0.000s
            chmod_325_6589()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=6590) as chmod_326_6590:  # 0m:0.000s
            chmod_326_6590()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=6591) as chmod_327_6591:  # 0m:0.000s
            chmod_327_6591()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=6592) as shell_command_328_6592:  # 0m:0.104s
            shell_command_328_6592()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=6593) as script_command_329_6593:  # 0m:0.010s
            script_command_329_6593()
    with Stage(r"post-copy", prog_num=6594):  # 0m:0.040s
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=6595) as make_dir_330_6595:  # 0m:0.005s
            make_dir_330_6595()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=6596) as copy_file_to_file_331_6596:  # 0m:0.013s
            copy_file_to_file_331_6596()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6597) as chmod_332_6597:  # 0m:0.001s
            chmod_332_6597()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6598) as chmod_333_6598:  # 0m:0.000s
            chmod_333_6598()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=6599) as copy_file_to_file_334_6599:  # 0m:0.008s
            copy_file_to_file_334_6599()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6600) as chmod_335_6600:  # 0m:0.001s
            chmod_335_6600()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=6601) as copy_file_to_file_336_6601:  # 0m:0.008s
            copy_file_to_file_336_6601()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6602) as chmod_337_6602:  # 0m:0.001s
            chmod_337_6602()
        Progress(r"Done copy", prog_num=6603)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=6604)()  # 0m:0.000s
    with Stage(r"post", prog_num=6605):  # 0m:0.044s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=6606) as make_dir_338_6606:  # 0m:0.005s
            make_dir_338_6606()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=6607) as copy_file_to_file_339_6607:  # 0m:0.008s
            copy_file_to_file_339_6607()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=6608) as make_dir_340_6608:  # 0m:0.007s
            make_dir_340_6608()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=6609) as copy_file_to_file_341_6609:  # 0m:0.007s
            copy_file_to_file_341_6609()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=6610) as make_dir_342_6610:  # 0m:0.007s
            make_dir_342_6610()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=6611) as copy_file_to_file_343_6611:  # 0m:0.009s
            copy_file_to_file_343_6611()

with Stage(r"epilog", prog_num=6612):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906122419.py", prog_num=6613) as patch_py_batch_with_timings_344_6613:  # ?
        patch_py_batch_with_timings_344_6613()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# copy time 0m:18.586s
