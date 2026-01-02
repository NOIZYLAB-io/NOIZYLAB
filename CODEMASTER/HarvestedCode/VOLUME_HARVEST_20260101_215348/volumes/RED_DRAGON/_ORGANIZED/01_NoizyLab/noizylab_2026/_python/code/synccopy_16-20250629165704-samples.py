# Creation time: 29-06-25_17-04
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 718
PythonBatchCommandBase.running_progress = 507
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=508):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250629165704-samples"
    config_vars['ALL_SYNC_DIRS'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 2
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"16.0.5"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V16", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V15", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V16", r"/Applications/Waves/WaveShells V16", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 6
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MTI2NjYyNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUxMjMwMzI0fX19XX0_;CloudFront-Signature=VPkeZNaEgWAZ~BodijNxNhFwnftuXIuqUn4YyEKFJQHa1M5whMFxr0kworF3ZULW3dE0EBh82J0~NUPbslGA6ejAar8UIP67H01ag-wXuoC32Otog53Re1zMbo7A01uZ0ui6USAhGPrcXkIDNAFmGYhgqshvm4mYgxVsdaeF5GIjTGbjnOe0oZfEkHhrLS8JNmrXvm113ONqtYSNvzX8jcrlAVUwAEIL~53B6g0yv44e0NhwGUTb8PqIbjNk30q9OHDnc0ZRoDSSH7edSV9~ODi36t7lLGKa8IK4-enT3bT811WLiSPRmdQCzyV6xmwOBn5~G27gDQHiOmFAPwjhRQ__"
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
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
    config_vars['INDEX_CHECKSUM'] = r"d116cfee4d3b8ba823ca77d73db949cd9f5332df"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"63d9fef14341cb4766d5c3d12c3578eca2a2385e"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"02470b97-df76-4590-aa88-78f6b14d8610", r"25a9e054-94a3-49c3-bc24-d2a73eb664f8", r"88bdcef4-eced-43c4-9273-d00c31e9b06d", r"aeafdce2-ab51-4a48-8878-0f72e2e97e6f", r"af5979d5-c8e1-4b1d-9128-a1cc87a7747f", r"b6f33536-568c-4bd1-b2a0-dfb45a00be73", r"ccf1c8bd-e872-4bf8-b66e-a31f232b8e55", r"e57efed1-2cea-4be8-b7e1-d09b2f9d9f97")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 31
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165704.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 4
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 6
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-06-18 18:39:08.575155"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/06"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V16"
    config_vars['REQUIRE_REPO_REV'] = 6
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"34e29ead85a33957b970d8d3096a8857e036390a"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 206
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165704.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"Instrument_Data_Bass_Fingers__SD_Sample_Library_IID", r"Instrument_Data_Bass_Slapper__SD_Sample_Library_IID", r"Instrument_Data_Clavinet__SD_Sample_Library_IID", r"Instrument_Data_Electric200__SD_Sample_Library_IID", r"Instrument_Data_Electric88__SD_Sample_Library_IID", r"Instrument_Data_ElectricG80__SD_Sample_Library_IID", r"Instrument_Data_GrandRhapsody_SD_Sample_Library_IID", r"Waves_Audio_Factory_Pack_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"Instrument_Data_Bass_Fingers__SD_Sample_Library_IID", r"Instrument_Data_Bass_Slapper__SD_Sample_Library_IID", r"Instrument_Data_Clavinet__SD_Sample_Library_IID", r"Instrument_Data_Electric200__SD_Sample_Library_IID", r"Instrument_Data_Electric88__SD_Sample_Library_IID", r"Instrument_Data_ElectricG80__SD_Sample_Library_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_GrandRhapsody_SD_Sample_Library_IID", r"Sample_Libraries_Locations_Folder_IID", r"Waves_Audio_Factory_Pack_IID", r"Waves_Data_folder_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"wakgvrecrwcsksbc"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"Instrument_Data_Bass_Fingers__SD_Sample_Library_IID", r"Instrument_Data_Bass_Slapper__SD_Sample_Library_IID", r"Instrument_Data_Clavinet__SD_Sample_Library_IID", r"Instrument_Data_Electric200__SD_Sample_Library_IID", r"Instrument_Data_Electric88__SD_Sample_Library_IID", r"Instrument_Data_ElectricG80__SD_Sample_Library_IID", r"Instrument_Data_GrandRhapsody_SD_Sample_Library_IID", r"Waves_Audio_Factory_Pack_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-29 17:06:04.328083"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6", r"/Library/Application Support/Waves/Central/V16", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=509):
    with Stage(r"begin", prog_num=510):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=511):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=512) as copy_file_to_file_001_512:
            copy_file_to_file_001_512()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=513) as copy_file_to_file_002_513:
            copy_file_to_file_002_513()
    with Stage(r"sync", prog_num=514):
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=515):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=516) as make_dir_003_516:
                make_dir_003_516()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=517) as cd_004_517:
                cd_004_517()
                Progress(r"150 files already in cache", own_progress_count=150, prog_num=667)()
                with Stage(r"post_sync", prog_num=668):
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=669) as copy_file_to_file_005_669:
                        copy_file_to_file_005_669()
            Progress(r"Done sync", prog_num=670)()
    with Stage(r"copy", prog_num=671):
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=672) as run_in_thread_006_672:
            run_in_thread_006_672()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=673)()
        with Stage(r"create folders", prog_num=674):
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=675) as make_dir_007_675:
                make_dir_007_675()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=676) as make_dir_008_676:
                make_dir_008_676()
            with MakeDir(r"/Users/Shared/Waves/Sample Libraries Locations", chowner=True, prog_num=677) as make_dir_009_677:
                make_dir_009_677()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", prog_num=678) as cd_stage_010_678:
            cd_stage_010_678()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Fingers SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Fingers SD", no_artifacts=True, prog_num=679) as un_zip_011_679:
                un_zip_011_679()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Bass Fingers Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Fingers SD", prog_num=680) as create_symlink_012_680:
                create_symlink_012_680()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Slapper SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Slapper SD", no_artifacts=True, prog_num=681) as un_zip_013_681:
                un_zip_013_681()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Bass Slapper Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Bass Slapper SD", prog_num=682) as create_symlink_014_682:
                create_symlink_014_682()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Clavinet SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Clavinet SD", no_artifacts=True, prog_num=683) as un_zip_015_683:
                un_zip_015_683()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Clavinet Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Clavinet SD", prog_num=684) as create_symlink_016_684:
                create_symlink_016_684()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric200 SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric200 SD", no_artifacts=True, prog_num=685) as un_zip_017_685:
                un_zip_017_685()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Electric200 Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric200 SD", prog_num=686) as create_symlink_018_686:
                create_symlink_018_686()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric88 SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric88 SD", no_artifacts=True, prog_num=687) as un_zip_019_687:
                un_zip_019_687()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Electric88 Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Electric88 SD", prog_num=688) as create_symlink_020_688:
                create_symlink_020_688()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/ElectricG80 SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/ElectricG80 SD", no_artifacts=True, prog_num=689) as un_zip_021_689:
                un_zip_021_689()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/ElectricGrand80 Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/ElectricG80 SD", prog_num=690) as create_symlink_022_690:
                create_symlink_022_690()
            with RmSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/ElectricG80 Samples Folder", prog_num=691) as rm_symlink_023_691:
                rm_symlink_023_691()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody SD", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody SD", no_artifacts=True, prog_num=692) as un_zip_024_692:
                un_zip_024_692()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/GrandRhapsody Samples Folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody SD", prog_num=693) as create_symlink_025_693:
                create_symlink_025_693()
            with RmSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Grand Rhapsody Samples Folder", prog_num=694) as rm_symlink_026_694:
                rm_symlink_026_694()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", no_artifacts=True, prog_num=695) as un_zip_027_695:
                un_zip_027_695()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Waves Audio Factory Pack", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", prog_num=696) as create_symlink_028_696:
                create_symlink_028_696()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=697) as shell_command_029_697:
            shell_command_029_697()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=698) as script_command_030_698:
            script_command_030_698()
    with Stage(r"post-copy", prog_num=699):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=700) as make_dir_031_700:
            make_dir_031_700()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=701) as copy_file_to_file_032_701:
            copy_file_to_file_032_701()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=702) as chmod_033_702:
            chmod_033_702()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=703) as chmod_034_703:
            chmod_034_703()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=704) as copy_file_to_file_035_704:
            copy_file_to_file_035_704()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=705) as chmod_036_705:
            chmod_036_705()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=706) as copy_file_to_file_037_706:
            copy_file_to_file_037_706()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=707) as chmod_038_707:
            chmod_038_707()
        Progress(r"Done copy", prog_num=708)()
        Progress(r"Done synccopy", prog_num=709)()
    with Stage(r"post", prog_num=710):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=711) as make_dir_039_711:
            make_dir_039_711()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=712) as copy_file_to_file_040_712:
            copy_file_to_file_040_712()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=713) as make_dir_041_713:
            make_dir_041_713()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=714) as copy_file_to_file_042_714:
            copy_file_to_file_042_714()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=715) as make_dir_043_715:
            make_dir_043_715()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=716) as copy_file_to_file_044_716:
            copy_file_to_file_044_716()

with Stage(r"epilog", prog_num=717):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-samples.py", prog_num=718) as patch_py_batch_with_timings_045_718:
        patch_py_batch_with_timings_045_718()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


