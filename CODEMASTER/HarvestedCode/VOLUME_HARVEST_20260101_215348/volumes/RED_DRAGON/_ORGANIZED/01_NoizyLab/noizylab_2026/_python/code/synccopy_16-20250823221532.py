# Creation time: 23-08-25_22-15
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 1057
PythonBatchCommandBase.running_progress = 549
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=550):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250823221532"
    config_vars['ALL_SYNC_DIRS'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 2
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"16.0.7"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V16", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V15", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V16", r"/Applications/Waves/WaveShells V16", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 15
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NjAzNzczM30sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU2MDAxNDMzfX19XX0_;CloudFront-Signature=hSeofsxWELqg8KbvIwHNP~aP4Qat~N5tv5fH4YGCgK4FCM453~bur3CMiD-zx~JBc1Xtr6jvv8wvrwVt5BbCNj7Uv70avZjAVcqEnZi4lLLKrT96adWlDTja-pxF2vxxR9Tqdf0Qu0~N1hWS5yXwpzIN83T2x11wGpfpXXS6oCnVHYqtFc~W4Wl7ft7rqXVAVUwRfAw0Icn2XM~hvP-p8zp8Fa~Y31ohXfJbOzh3~-fmShy7Lih-huEBWqkVO01qaH9zX4IKjyIKNshSKdX9f6oGSB40XABks73oUMNNe-cR1l3d1borTAEQqPuv29RqJAofQxz-oJxZjv0LI52vSw__"
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
    config_vars['INDEX_CHECKSUM'] = r"4c3d5d9c6036b44c145f1a2201e717d1784356a0"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/15/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"f8c8e87dc7502a39d6456bf43451f2ba39adecfe"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/15/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/15/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = r"fcdbc046-5e44-4d4d-b4ec-049d194c2458"
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 15
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250823221532.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 15
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-08-20 16:45:05.235803"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/15"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V16"
    config_vars['REQUIRE_REPO_REV'] = 15
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"39e1a93e9b0ed8f734382005351bb315cedec0d3"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/15/instl/short-index.yaml"
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
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 503
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250823221532.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-07-06 12:14:08.392126"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.6.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = ""
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"COMMON_PLUGIN_DEPENDS_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_V16_1_IID", r"Get_General_Icons_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"IntelDlls_IID", r"LicenseNotifications_V16_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PresetBrowser_V16_1_IID", r"Shutdown_Servers_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"V9_V10_Organizer_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesLib1_16_0_23_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-07-06 12:14:08.392126 bm-mac-ado9"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"sgwyffyndjvwqtsw"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = r"Silk_Vocal_IID"
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-08-23 22:17:04.868078"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"bm-mac-ado9"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15", r"/Library/Application Support/Waves/Central/V16", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"bm-mac-ado9"
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

with PythonBatchRuntime(r"synccopy", prog_num=551):
    with Stage(r"begin", prog_num=552):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=553):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=554) as copy_file_to_file_001_554:
            copy_file_to_file_001_554()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=555) as copy_file_to_file_002_555:
            copy_file_to_file_002_555()
    with Stage(r"sync", prog_num=556):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=557) as shell_command_003_557:
            shell_command_003_557()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=558) as shell_command_004_558:
            shell_command_004_558()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=559) as shell_command_005_559:
            shell_command_005_559()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=560) as shell_command_006_560:
            shell_command_006_560()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=561) as shell_command_007_561:
            shell_command_007_561()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=562) as shell_command_008_562:
            shell_command_008_562()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=563) as shell_command_009_563:
            shell_command_009_563()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=564) as shell_command_010_564:
            shell_command_010_564()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=565) as shell_command_011_565:
            shell_command_011_565()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=566):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=567) as make_dir_012_567:
                make_dir_012_567()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=568) as cd_013_568:
                cd_013_568()
                Progress(r"231 files already in cache", own_progress_count=231, prog_num=799)()
                with Stage(r"post_sync", prog_num=800):
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=801) as copy_file_to_file_014_801:
                        copy_file_to_file_014_801()
            Progress(r"Done sync", prog_num=802)()
    with Stage(r"copy", prog_num=803):
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=804) as run_in_thread_015_804:
            run_in_thread_015_804()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=805)()
        with Stage(r"create folders", prog_num=806):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=807) as make_dir_016_807:
                make_dir_016_807()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=808) as make_dir_017_808:
                make_dir_017_808()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=809) as make_dir_018_809:
                make_dir_018_809()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=810) as make_dir_019_810:
                make_dir_019_810()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=811) as make_dir_020_811:
                make_dir_020_811()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=812) as make_dir_021_812:
                make_dir_021_812()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=813) as make_dir_022_813:
                make_dir_022_813()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=814) as make_dir_023_814:
                make_dir_023_814()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=815) as make_dir_024_815:
                make_dir_024_815()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=816) as make_dir_025_816:
                make_dir_025_816()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=817) as make_dir_026_817:
                make_dir_026_817()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=818) as make_dir_027_818:
                make_dir_027_818()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=819) as make_dir_028_819:
                make_dir_028_819()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=820) as make_dir_029_820:
                make_dir_029_820()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=821) as make_dir_030_821:
                make_dir_030_821()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=822) as make_dir_031_822:
                make_dir_031_822()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=823) as make_dir_032_823:
                make_dir_032_823()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=824) as make_dir_033_824:
                make_dir_033_824()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=825) as make_dir_034_825:
                make_dir_034_825()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=826) as make_dir_035_826:
                make_dir_035_826()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=827) as make_dir_036_827:
                make_dir_036_827()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=828) as rm_file_or_dir_037_828:
            rm_file_or_dir_037_828()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=829) as shell_command_038_829:
            shell_command_038_829()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=830) as shell_command_039_830:
            shell_command_039_830()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=831) as shell_command_040_831:
            shell_command_040_831()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=832) as shell_command_041_832:
            shell_command_041_832()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=833) as shell_command_042_833:
            shell_command_042_833()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=834) as shell_command_043_834:
            shell_command_043_834()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=835) as shell_command_044_835:
            shell_command_044_835()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=836) as shell_command_045_836:
            shell_command_045_836()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=837) as shell_command_046_837:
            shell_command_046_837()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=838) as cd_stage_047_838:
            cd_stage_047_838()
            with SetExecPermissionsInSyncFolder(prog_num=839) as set_exec_permissions_in_sync_folder_048_839:
                set_exec_permissions_in_sync_folder_048_839()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=840) as cd_stage_049_840:
            cd_stage_049_840()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=841):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=842) as should_copy_source_050_842:
                    should_copy_source_050_842()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=843):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=844) as copy_dir_to_dir_051_844:
                            copy_dir_to_dir_051_844()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=845, recursive=True) as chown_052_845:
                            chown_052_845()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=846) as cd_stage_053_846:
            cd_stage_053_846()
            with Stage(r"copy", r"Silk Vocal v16.0.23.24", prog_num=847):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=848) as should_copy_source_054_848:
                    should_copy_source_054_848()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=849):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=850) as copy_dir_to_dir_055_850:
                            copy_dir_to_dir_055_850()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=851) as unwtar_056_851:
                            unwtar_056_851()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=852, recursive=True) as chown_057_852:
                            chown_057_852()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=853):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=854) as should_copy_source_058_854:
                    should_copy_source_058_854()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=855):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=856) as copy_dir_to_dir_059_856:
                            copy_dir_to_dir_059_856()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=857) as unwtar_060_857:
                            unwtar_060_857()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=858, recursive=True) as chown_061_858:
                            chown_061_858()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=2, prog_num=860) as resolve_symlink_files_in_folder_062_860:
                resolve_symlink_files_in_folder_062_860()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=861) as shell_command_063_861:
                shell_command_063_861()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=862) as script_command_064_862:
                script_command_064_862()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=863) as shell_command_065_863:
                shell_command_065_863()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=864) as create_symlink_066_864:
                create_symlink_066_864()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=865) as create_symlink_067_865:
                create_symlink_067_865()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=866) as copy_glob_to_dir_068_866:
                copy_glob_to_dir_068_866()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=867) as cd_stage_069_867:
            cd_stage_069_867()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=868):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=869) as should_copy_source_070_869:
                    should_copy_source_070_869()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=870):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=871) as copy_file_to_dir_071_871:
                            copy_file_to_dir_071_871()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=872) as chmod_and_chown_072_872:
                            chmod_and_chown_072_872()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=873) as cd_stage_073_873:
            cd_stage_073_873()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=874):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=875) as should_copy_source_074_875:
                    should_copy_source_074_875()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=876):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=877) as copy_dir_to_dir_075_877:
                            copy_dir_to_dir_075_877()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=878) as unwtar_076_878:
                            unwtar_076_878()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=879, recursive=True) as chown_077_879:
                            chown_077_879()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=880) as shell_command_078_880:
                            shell_command_078_880()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=881):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=882) as should_copy_source_079_882:
                    should_copy_source_079_882()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=883):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=884) as copy_dir_to_dir_080_884:
                            copy_dir_to_dir_080_884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=885) as unwtar_081_885:
                            unwtar_081_885()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=886, recursive=True) as chown_082_886:
                            chown_082_886()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=887) as break_hard_link_083_887:
                            break_hard_link_083_887()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=888) as shell_command_084_888:
                            shell_command_084_888()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=889, recursive=True) as chown_085_889:
                            chown_085_889()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=890, recursive=True) as chmod_086_890:
                            chmod_086_890()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=891):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=892) as should_copy_source_087_892:
                    should_copy_source_087_892()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=893):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=894) as copy_dir_to_dir_088_894:
                            copy_dir_to_dir_088_894()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=895) as unwtar_089_895:
                            unwtar_089_895()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=896, recursive=True) as chown_090_896:
                            chown_090_896()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=897) as shell_command_091_897:
                            shell_command_091_897()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=898):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=899) as should_copy_source_092_899:
                    should_copy_source_092_899()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=900):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=901) as copy_dir_to_dir_093_901:
                            copy_dir_to_dir_093_901()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=902) as unwtar_094_902:
                            unwtar_094_902()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=903, recursive=True) as chown_095_903:
                            chown_095_903()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=904) as shell_command_096_904:
                            shell_command_096_904()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=905) as script_command_097_905:
                            script_command_097_905()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=906) as shell_command_098_906:
                            shell_command_098_906()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=907):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=908) as should_copy_source_099_908:
                    should_copy_source_099_908()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=909):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=910) as copy_dir_to_dir_100_910:
                            copy_dir_to_dir_100_910()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=911) as unwtar_101_911:
                            unwtar_101_911()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=912, recursive=True) as chown_102_912:
                            chown_102_912()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=913) as shell_command_103_913:
                shell_command_103_913()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=914) as cd_stage_104_914:
            cd_stage_104_914()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=915):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=916) as should_copy_source_105_916:
                    should_copy_source_105_916()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=917):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=918) as copy_dir_to_dir_106_918:
                            copy_dir_to_dir_106_918()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=919) as unwtar_107_919:
                            unwtar_107_919()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=920, recursive=True) as chown_108_920:
                            chown_108_920()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=921) as shell_command_109_921:
                            shell_command_109_921()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=922) as cd_stage_110_922:
            cd_stage_110_922()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=923):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=924) as should_copy_source_111_924:
                    should_copy_source_111_924()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=925):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=926) as copy_dir_to_dir_112_926:
                            copy_dir_to_dir_112_926()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=927, recursive=True) as chown_113_927:
                            chown_113_927()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=928) as cd_stage_114_928:
            cd_stage_114_928()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=929):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=930) as should_copy_source_115_930:
                    should_copy_source_115_930()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=931):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=932) as copy_dir_to_dir_116_932:
                            copy_dir_to_dir_116_932()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=933, recursive=True) as chown_117_933:
                            chown_117_933()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=934) as cd_stage_118_934:
            cd_stage_118_934()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=935):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=936) as should_copy_source_119_936:
                    should_copy_source_119_936()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=937):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=938) as copy_dir_to_dir_120_938:
                            copy_dir_to_dir_120_938()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=939, recursive=True) as chown_121_939:
                            chown_121_939()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=940) as cd_stage_122_940:
            cd_stage_122_940()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=941) as rm_file_or_dir_123_941:
                rm_file_or_dir_123_941()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=942):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=943) as should_copy_source_124_943:
                    should_copy_source_124_943()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=944):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=945) as copy_dir_to_dir_125_945:
                            copy_dir_to_dir_125_945()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=946) as unwtar_126_946:
                            unwtar_126_946()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=947, recursive=True) as chown_127_947:
                            chown_127_947()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=948):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=949) as should_copy_source_128_949:
                    should_copy_source_128_949()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=950):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=951) as unwtar_129_951:
                            unwtar_129_951()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=952):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=953) as should_copy_source_130_953:
                    should_copy_source_130_953()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=954):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=955) as copy_dir_to_dir_131_955:
                            copy_dir_to_dir_131_955()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=956) as unwtar_132_956:
                            unwtar_132_956()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=957, recursive=True) as chown_133_957:
                            chown_133_957()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=958):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=959) as should_copy_source_134_959:
                    should_copy_source_134_959()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=960):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=961) as copy_dir_to_dir_135_961:
                            copy_dir_to_dir_135_961()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=962) as chmod_136_962:
                            chmod_136_962()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=963) as chmod_137_963:
                            chmod_137_963()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=964, recursive=True) as chown_138_964:
                            chown_138_964()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=967) as resolve_symlink_files_in_folder_139_967:
                resolve_symlink_files_in_folder_139_967()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=968) as shell_command_140_968:
                shell_command_140_968()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=969) as cd_stage_141_969:
            cd_stage_141_969()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=970):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=971) as should_copy_source_142_971:
                    should_copy_source_142_971()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=972):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=973) as copy_dir_to_dir_143_973:
                            copy_dir_to_dir_143_973()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=974, recursive=True) as chown_144_974:
                            chown_144_974()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=975) as cd_stage_145_975:
            cd_stage_145_975()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=976):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=977) as should_copy_source_146_977:
                    should_copy_source_146_977()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=978):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=979) as copy_dir_to_dir_147_979:
                            copy_dir_to_dir_147_979()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=980, recursive=True) as chown_148_980:
                            chown_148_980()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=981) as cd_stage_149_981:
            cd_stage_149_981()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=982):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=983) as should_copy_source_150_983:
                    should_copy_source_150_983()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=984):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=985, recursive=True) as chmod_151_985:
                            chmod_151_985()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=986) as copy_dir_to_dir_152_986:
                            copy_dir_to_dir_152_986()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=987) as unwtar_153_987:
                            unwtar_153_987()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=988, recursive=True) as chown_154_988:
                            chown_154_988()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=989) as if_155_989:
                            if_155_989()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=990) as cd_stage_156_990:
            cd_stage_156_990()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=991):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=992) as should_copy_source_157_992:
                    should_copy_source_157_992()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=993):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=994) as copy_dir_to_dir_158_994:
                            copy_dir_to_dir_158_994()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=995) as unwtar_159_995:
                            unwtar_159_995()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=996, recursive=True) as chown_160_996:
                            chown_160_996()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=997) as break_hard_link_161_997:
                            break_hard_link_161_997()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=998) as shell_command_162_998:
                            shell_command_162_998()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=999, recursive=True) as chown_163_999:
                            chown_163_999()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=1000, recursive=True) as chmod_164_1000:
                            chmod_164_1000()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=1001) as cd_stage_165_1001:
            cd_stage_165_1001()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=1002):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=1003) as should_copy_source_166_1003:
                    should_copy_source_166_1003()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=1004):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=1005) as copy_dir_to_dir_167_1005:
                            copy_dir_to_dir_167_1005()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=1006) as unwtar_168_1006:
                            unwtar_168_1006()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=1007, recursive=True) as chown_169_1007:
                            chown_169_1007()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=1008) as shell_command_170_1008:
                            shell_command_170_1008()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1009) as cd_stage_171_1009:
            cd_stage_171_1009()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=1010):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=1011) as should_copy_source_172_1011:
                    should_copy_source_172_1011()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=1012):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=1013) as copy_dir_to_dir_173_1013:
                            copy_dir_to_dir_173_1013()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=1014) as unwtar_174_1014:
                            unwtar_174_1014()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=1015, recursive=True) as chown_175_1015:
                            chown_175_1015()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=1016) as shell_command_176_1016:
                            shell_command_176_1016()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=1017) as script_command_177_1017:
                            script_command_177_1017()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1018) as shell_command_178_1018:
                            shell_command_178_1018()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1019) as create_symlink_179_1019:
                create_symlink_179_1019()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1020) as create_symlink_180_1020:
                create_symlink_180_1020()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=1021) as rm_file_or_dir_181_1021:
            rm_file_or_dir_181_1021()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=1022) as shell_command_182_1022:
            shell_command_182_1022()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=1023) as script_command_183_1023:
            script_command_183_1023()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=1024) as rm_file_or_dir_184_1024:
            rm_file_or_dir_184_1024()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=1025) as glober_185_1025:
            glober_185_1025()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=1026) as glober_186_1026:
            glober_186_1026()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=1027) as glober_187_1027:
            glober_187_1027()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1028) as shell_command_188_1028:
            shell_command_188_1028()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1029) as shell_command_189_1029:
            shell_command_189_1029()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1030) as shell_command_190_1030:
            shell_command_190_1030()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1031) as shell_command_191_1031:
            shell_command_191_1031()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=1032) as shell_command_192_1032:
            shell_command_192_1032()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=1033) as script_command_193_1033:
            script_command_193_1033()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=1034) as if_194_1034:
            if_194_1034()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=1035) as if_195_1035:
            if_195_1035()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=1036) as shell_command_196_1036:
            shell_command_196_1036()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=1037) as script_command_197_1037:
            script_command_197_1037()
    with Stage(r"post-copy", prog_num=1038):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=1039) as make_dir_198_1039:
            make_dir_198_1039()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=1040) as copy_file_to_file_199_1040:
            copy_file_to_file_199_1040()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1041) as chmod_200_1041:
            chmod_200_1041()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1042) as chmod_201_1042:
            chmod_201_1042()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1043) as copy_file_to_file_202_1043:
            copy_file_to_file_202_1043()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1044) as chmod_203_1044:
            chmod_203_1044()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=1045) as copy_file_to_file_204_1045:
            copy_file_to_file_204_1045()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1046) as chmod_205_1046:
            chmod_205_1046()
        Progress(r"Done copy", prog_num=1047)()
        Progress(r"Done synccopy", prog_num=1048)()
    with Stage(r"post", prog_num=1049):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=1050) as make_dir_206_1050:
            make_dir_206_1050()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=1051) as copy_file_to_file_207_1051:
            copy_file_to_file_207_1051()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=1052) as make_dir_208_1052:
            make_dir_208_1052()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=1053) as copy_file_to_file_209_1053:
            copy_file_to_file_209_1053()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=1054) as make_dir_210_1054:
            make_dir_210_1054()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=1055) as copy_file_to_file_211_1055:
            copy_file_to_file_211_1055()

with Stage(r"epilog", prog_num=1056):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823221532.py", prog_num=1057) as patch_py_batch_with_timings_212_1057:
        patch_py_batch_with_timings_212_1057()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


