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
PythonBatchCommandBase.total_progress = 5220
PythonBatchCommandBase.running_progress = 873
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=874):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"14-20250615162416"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", r"/Applications/Waves/Data/Video Sound Suite Impulses", r"/Applications/Waves/Data/Video Sound Suite Impulses")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.5.5"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V14", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 183
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NTA1Nn0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NzU2fX19XX0_;CloudFront-Signature=JkhiBwwGY4QW8-2GttlMdWx0JJ0GJqOTNxFufVWppasIBanqFZH-kLOs33-O12EqTbNhQ7pFAtmkeKB9ToW3AUHj4b35lSL4JHKVD38oueZpTP9SPsT6dPipODJ4GQulnX-R4FAYXzmikrjkXbU6ZukJ6mD4jujt6HmxN1HXXiJMRvMkSRoCLxUVeFxt9s4WyuB0BB0GqHRp7bGUvphXBgZg23FGHPgs3Rcg~kB2LiHukuBUvEP47os6PUGKfJqUqr4fKsuJFf~hL7syE9vqfuQj7afubRPu5quaORceIEfK-E8fnke6feEJs9KPDXXIACF7Q63b7LooxG-TxGruOg__"
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
    config_vars['INDEX_CHECKSUM'] = r"d2128b5ea2a9699fc59236d69d550088e382ea8e"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/83/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"c686916a1dee0b2c24576397363c57b5070075e7"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/83/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/83/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 3, 10)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"fixed create_venc.sh to not update pip itself with the global python"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183"
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
    config_vars['MAX_REPO_REV'] = 183
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162416.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 14
    config_vars['REPO_NAME'] = r"V14"
    config_vars['REPO_REV'] = 183
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V14_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-05-12 15:33:38.172315"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V14_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"01/83"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V14"
    config_vars['REQUIRE_REPO_REV'] = 183
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"0dec7fe2f775f9abb25b64e5208f54e6f7321047"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14/01/83/instl/short-index.yaml"
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
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"before-copy-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 4342
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
    config_vars['WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162416.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-05-22 15:27:15.823473"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"A-H_M_Documents_IID", r"A-H_M_IOM_IID", r"A-H_M_s3_Firmware_13_4_IID", r"A-H_M_s6_Firmware_13_4_IID", r"A-H_M_sq_Firmware_13_4_IID", r"A-H_M_v3_Firmware_14_12_IID", r"All_IOMs_IID", r"Apogee_Symphony_Documents_IID", r"Apogee_Symphony_Firmware_13_4_IID", r"Apogee_Symphony_IID", r"Apogee_Symphony_IOM_IID", r"Apogee_Symphony_micro_Firmware_13_4_IID", r"BR1_Documents_IID", r"BR1_Firmware_13_7_IID", r"BR1_IID", r"BR1_IOM_IID", r"Behringer_Wing_SoundGrid_IO_Driver_Firmware_14_25_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IOM_IID", r"Burl_BMB4_Documents_IID", r"Burl_BMB4_Firmware_13_4_IID", r"Burl_BMB4_IID", r"Burl_BMB4_IOM_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"Cadac_Documents_IID", r"Cadac_Firmware_13_4_IID", r"Cadac_IID", r"Cadac_IOM_IID", r"Calrec_Documents_IID", r"Calrec_Firmware_13_4_IID", r"Calrec_IID", r"Calrec_IOM_IID", r"Converter_IID", r"Crest_Tactus_Documents_IID", r"Crest_Tactus_Firmware_13_4_IID", r"Crest_Tactus_IID", r"Crest_Tactus_IO_Modules_IID", r"Crest_Tactus_micro_Firmware_13_4_IID", r"DLI_DLS_Documents_IID", r"DLI_DLS_IID", r"DLI_DLS_IOM_IID", r"DLI_DLS_eMotion_IID", r"DLI_Firmware_12_1_IID", r"DLI_Firmware_13_4_IID", r"DLS_Firmware_12_1_IID", r"DLS_Firmware_13_4_IID", r"DMI_Waves_Documents_IID", r"DMI_Waves_Firmware_13_7_IID", r"DMI_Waves_IID", r"DMI_Waves_IOM_IID", r"DN32_WSG_Documents_IID", r"DN32_WSG_Firmware_13_4_IID", r"DN32_WSG_IID", r"DN32_WSG_IOM_IID", r"DSPro_SG1000_Firmware_13_4_IID", r"DSPro_SG1000_Firmware_13_6_IID", r"DSPro_SG1000_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_13_4_IID", r"DSPro_SG1000_micro_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_15_1_IID", r"DSPro_SG1000_micro_V2_Firmware_15_1_IID", r"DSPro_SG4000_Documents_IID", r"DSPro_SG4000_Firmware_13_4_IID", r"DSPro_SG4000_Firmware_13_5_IID", r"DSPro_SG4000_Firmware_14_26_IID", r"DSPro_SG4000_IID", r"DSPro_SG4000_IOM_IID", r"DSPro_SG4000_micro_Firmware_13_4_IID", r"DSPro_SG4000_micro_Firmware_14_25_IID", r"DSPro_SG4000_micro_Firmware_15_2_IID", r"DSPro_SG4000_micro_V2_Firmware_15_2_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_2_IID", r"DiGiGrid_D_Driver_Documents_IID", r"DiGiGrid_D_Driver_Firmware_13_4_IID", r"DiGiGrid_D_Driver_IID", r"DiGiGrid_D_Driver_IOM_IID", r"DiGiGrid_M_Driver_Documents_IID", r"DiGiGrid_M_Driver_Firmware_13_4_IID", r"DiGiGrid_M_Driver_IID", r"DiGiGrid_M_Driver_IOM_IID", r"DiGiGrid_Q_Driver_Documents_IID", r"DiGiGrid_Q_Driver_Firmware_13_4_IID", r"DiGiGrid_Q_Driver_IID", r"DiGiGrid_Q_Driver_IOM_IID", r"DigiGrid_SoundGrid__Documents__IID", r"Digico_SD_IOM_IID", r"Digico_SD_card_13_4_IID", r"Digico_SD_card_Documents_IID", r"Digico_SD_card_Firmware_14_21_IID", r"Digico_SD_card_IOM_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_22_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_v2_micro_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IOM_IID", r"DirectOut_SG_MADI_Documents_IID", r"DirectOut_SG_MADI_Firmware_13_4_IID", r"DirectOut_SG_MADI_IID", r"DirectOut_SG_MADI_IOM_IID", r"DirectOut_SG_MADI_micro_Firmware_13_4_IID", r"DirectOut_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_SoundGrid_IO_Driver_IID", r"DirectOut_SoundGrid_IO_Driver_IOM_IID", r"Get_General_Icons_IID", r"Hear_Back_Documents_IID", r"Hear_Back_Firmware_10_0_IID", r"Hear_Back_Firmware_13_7_IID", r"Hear_Back_IID", r"Hear_Back_IOM_IID", r"Hear_Back_IO_Modules_IID", r"Hear_Back_Pro_V2_Firmware_13_7_IID", r"Hear_Tech_Documents_IID", r"Hear_Tech_Firmware_15_1_IID", r"Hear_Tech_Firmware_15_1_v2_IID", r"Hear_Tech_IID", r"Hear_Tech_IOM_IID", r"IOC_Documents_IID", r"IOC_Firmware_13_4_IID", r"IOC_IID", r"IOC_IOM_IID", r"IOC_micro_Firmware_13_4_IID", r"IONIC16_Firmware_S25_IID", r"IONIC16_Firmware_S50_IID", r"IONIC_Documents_IID", r"IONIC_IID", r"IONIC_IOM_IID", r"IOS_Documents_IID", r"IOS_Firmware_13_4_IID", r"IOS_IID", r"IOS_IOM_IID", r"IOS_XL_Documents_IID", r"IOS_XL_Firmware_13_4_IID", r"IOS_XL_IID", r"IOS_XL_IOM_IID", r"IOS_XL_micro_Firmware_13_4_IID", r"IOS_eMotion_IID", r"IOS_micro_Firmware_13_4_IID", r"IOX_Documents_IID", r"IOX_Firmware_13_4_IID", r"IOX_IID", r"IOX_IOM_IID", r"IOX_eMotion_IID", r"IOX_micro_Firmware_13_4_IID", r"IOs_FW_and_Modules__IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Insert_IID", r"IntelDlls_IID", r"JoeCo_Documents_IID", r"JoeCo_Firmware_13_4_IID", r"JoeCo_IID", r"JoeCo_IOM_IID", r"JoeCo_Utilities_IID", r"M-DL-WAVES3_IID", r"M-SQ-WAVES3_IID", r"M-Waves_V2_IID", r"MGB_Firmware_13_4_IID", r"MGB_MGO_Documents_IID", r"MGB_MGO_IID", r"MGB_MGO_IOM_IID", r"MGB_MGO_eMotion_IID", r"MGO_Firmware_13_4_IID", r"MKL_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MKL_x32_IID", r"MKL_x64_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"MixerSessionConverter_IID", r"MultiRack_SG_IO_Modules_IID", r"MyRemote_IID", r"Plugin_Infra__IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_2_IID", r"PresetBrowser_IID", r"QT_5_12_8_IID", r"QT_5_5_1_FOR_IO_MODULES_IID", r"QT_5_5_1_IID", r"QT_6_2_4_IID", r"Remote_IO_Modules_IID", r"Restart_required_IID", r"SGS_14_9_Firmware_IID", r"SG_Connect_IID", r"SG_Driver_Documents_IID", r"SG_Driver_Uninstaller_IID", r"SG_Driver_V12_2_IID", r"SG_Driver_V12_2_Install_IID", r"SG_Infra_and_Common__IID", r"SG_Studio_V11_8CH_IID", r"SG_Studio_V11_preferences_cleanup_IID", r"STG_1608_Firmware_13_4_IID", r"STG_1608_micro_Firmware_13_4_IID", r"STG_2412_Documents_IID", r"STG_2412_Firmware_13_4_IID", r"STG_2412_IID", r"STG_2412_IOM_IID", r"STG_2412_micro_Firmware_13_4_IID", r"SampleTestConverter_IID", r"Session_Converters_IID", r"Shutdown_Servers_IID", r"SoundGrid_Studio_IID", r"SoundGrid_Studio_Plugins__IID", r"SoundGrid_Studio_app__Application__IID", r"SoundGrid_Studio_app__Documents__IID", r"SoundGrid_Studio_app__IID", r"SoundGrid_Studio_app__Modules__IID", r"SoundGrid_Studio_app__Sessions_Structure__IID", r"SoundGrid_Studio_app__Shared_Folder__IID", r"SoundGrid_folder_IID", r"StudioRack_Data_IID", r"StudioRack_IID", r"StudioRack_Impulses_IID", r"StudioRack_Presets_Compatibility_IID", r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID", r"V9_V10_Organizer_IID", r"WAVE_SHELL_OBS_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_14_12_IID", r"WaveShell1_AAX_14_21_IID", r"WaveShell1_AU_14_12_IID", r"WaveShell1_AU_14_21_IID", r"WaveShell1_VST_2_V14_12_IID", r"WaveShell1_VST_2_V14_21_IID", r"WaveShell1_VST_3_V14_12_IID", r"WaveShell1_VST_3_V14_21_IID", r"WaveShell1_WPAPI_2_14_12_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesLib1_14_12_90_381_IID", r"WavesLib1_14_21_96_552_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V14_2_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"X-WSG_Documents_IID", r"X-WSG_IID", r"X-WSG_IOM_IID", r"X-WSG_s6_Firmware_13_4_IID", r"Y-16_Documents_IID", r"Y-16_IID", r"Y-16_IOM_IID", r"Y-16_s3_Firmware_13_4_IID", r"Y-16_s6_Firmware_13_4_IID", r"Y-16_v3_Firmware_14_21_IID", r"Yamaha_HY128v2_Firmware_IID", r"Yamaha_WSG_Firmware_13_4_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.7 2025-05-22 15:27:15.823473 BM-MAC-ADO5"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.7"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 7)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"xijklbjlyavyqhdw"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"SG_Studio_V11_8CH_IID", r"StudioRack_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-15 16:24:28.397050"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO5"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183", r"/Library/Application Support/Waves/Central/V14", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"BM-MAC-ADO5"
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

with PythonBatchRuntime(r"synccopy", prog_num=875):  # 1m:5.314s
    with Stage(r"begin", prog_num=876):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=877):  # 0m:0.014s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=878) as copy_file_to_file_001_878:  # 0m:0.008s
            copy_file_to_file_001_878()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=879) as copy_file_to_file_002_879:  # 0m:0.006s
            copy_file_to_file_002_879()
    with Stage(r"sync", prog_num=880):  # 0m:40.580s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=881) as shell_command_003_881:  # 0m:0.009s
            shell_command_003_881()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=882) as shell_command_004_882:  # 0m:0.012s
            shell_command_004_882()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=883) as shell_command_005_883:  # 0m:39.297s
            shell_command_005_883()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=884) as shell_command_006_884:  # 0m:0.010s
            shell_command_006_884()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=885) as shell_command_007_885:  # 0m:0.007s
            shell_command_007_885()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=886) as shell_command_008_886:  # 0m:1.228s
            shell_command_008_886()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V14", prog_num=887):  # 0m:0.017s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", chowner=True, prog_num=888) as make_dir_009_888:  # 0m:0.008s
                make_dir_009_888()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=889) as cd_010_889:  # 0m:0.008s
                cd_010_889()
                Progress(r"2287 files already in cache", own_progress_count=2287, prog_num=3176)()  # 0m:0.000s
                with Stage(r"post_sync", prog_num=3177):  # 0m:0.007s
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=3178) as copy_file_to_file_011_3178:  # 0m:0.007s
                        copy_file_to_file_011_3178()
            Progress(r"Done sync", prog_num=3179)()  # 0m:0.000s
    with Stage(r"copy", prog_num=3180):  # 0m:24.657s
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=3181) as run_in_thread_012_3181:  # 0m:0.000s
            run_in_thread_012_3181()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=3182)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=3183):  # 0m:0.235s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=3184) as make_dir_013_3184:  # 0m:0.008s
                make_dir_013_3184()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=3185) as make_dir_014_3185:  # 0m:0.005s
                make_dir_014_3185()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=3186) as make_dir_015_3186:  # 0m:0.007s
                make_dir_015_3186()
            with MakeDir(r"/Applications/Waves/Data/linux/lib/mkl", chowner=True, prog_num=3187) as make_dir_016_3187:  # 0m:0.006s
                make_dir_016_3187()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14", chowner=True, prog_num=3188) as make_dir_017_3188:  # 0m:0.005s
                make_dir_017_3188()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14/Documents", chowner=True, prog_num=3189) as make_dir_018_3189:  # 0m:0.005s
                make_dir_018_3189()
            with MakeDir(r"/Applications/Waves/SoundGrid", chowner=True, prog_num=3190) as make_dir_019_3190:  # 0m:0.005s
                make_dir_019_3190()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio", chowner=True, prog_num=3191) as make_dir_020_3191:  # 0m:0.008s
                make_dir_020_3191()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Documents", chowner=True, prog_num=3192) as make_dir_021_3192:  # 0m:0.005s
                make_dir_021_3192()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Modules", chowner=True, prog_num=3193) as make_dir_022_3193:  # 0m:0.006s
                make_dir_022_3193()
            with MakeDir(r"/Applications/Waves/SoundGrid/Documents", chowner=True, prog_num=3194) as make_dir_023_3194:  # 0m:0.006s
                make_dir_023_3194()
            with MakeDir(r"/Applications/Waves/SoundGrid/Utilities", chowner=True, prog_num=3195) as make_dir_024_3195:  # 0m:0.005s
                make_dir_024_3195()
            with MakeDir(r"/Applications/Waves/WaveShells V14", chowner=True, prog_num=3196) as make_dir_025_3196:  # 0m:0.009s
                make_dir_025_3196()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=3197) as make_dir_026_3197:  # 0m:0.004s
                make_dir_026_3197()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=3198) as make_dir_027_3198:  # 0m:0.006s
                make_dir_027_3198()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode", chowner=True, prog_num=3199) as make_dir_028_3199:  # 0m:0.004s
                make_dir_028_3199()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V14", chowner=True, prog_num=3200) as make_dir_029_3200:  # 0m:0.006s
                make_dir_029_3200()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=3201) as make_dir_030_3201:  # 0m:0.009s
                make_dir_030_3201()
            with MakeDir(r"/Library/Application Support/Waves/MyMon", chowner=True, prog_num=3202) as make_dir_031_3202:  # 0m:0.005s
                make_dir_031_3202()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser", chowner=True, prog_num=3203) as make_dir_032_3203:  # 0m:0.007s
                make_dir_032_3203()
            with MakeDir(r"/Library/Application Support/Waves/RemoteServices", chowner=True, prog_num=3204) as make_dir_033_3204:  # 0m:0.009s
                make_dir_033_3204()
            with MakeDir(r"/Library/Application Support/Waves/Session Converters", chowner=True, prog_num=3205) as make_dir_034_3205:  # 0m:0.005s
                make_dir_034_3205()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", chowner=True, prog_num=3206) as make_dir_035_3206:  # 0m:0.009s
                make_dir_035_3206()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", chowner=True, prog_num=3207) as make_dir_036_3207:  # 0m:0.005s
                make_dir_036_3207()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid IO Modules", chowner=True, prog_num=3208) as make_dir_037_3208:  # 0m:0.006s
                make_dir_037_3208()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=3209) as make_dir_038_3209:  # 0m:0.007s
                make_dir_038_3209()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=3210) as make_dir_039_3210:  # 0m:0.008s
                make_dir_039_3210()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=3211) as make_dir_040_3211:  # 0m:0.005s
                make_dir_040_3211()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=3212) as make_dir_041_3212:  # 0m:0.004s
                make_dir_041_3212()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=3213) as make_dir_042_3213:  # 0m:0.004s
                make_dir_042_3213()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=3214) as make_dir_043_3214:  # 0m:0.008s
                make_dir_043_3214()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=3215) as make_dir_044_3215:  # 0m:0.005s
                make_dir_044_3215()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=3216) as make_dir_045_3216:  # 0m:0.008s
                make_dir_045_3216()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/History", chowner=True, prog_num=3217) as make_dir_046_3217:  # 0m:0.007s
                make_dir_046_3217()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Sessions", chowner=True, prog_num=3218) as make_dir_047_3218:  # 0m:0.010s
                make_dir_047_3218()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Templates", chowner=True, prog_num=3219) as make_dir_048_3219:  # 0m:0.006s
                make_dir_048_3219()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=3220) as make_dir_049_3220:  # 0m:0.006s
                make_dir_049_3220()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=3221) as rm_file_or_dir_050_3221:  # 0m:0.000s
            rm_file_or_dir_050_3221()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=3222) as shell_command_051_3222:  # 0m:0.009s
            shell_command_051_3222()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=3223) as shell_command_052_3223:  # 0m:0.012s
            shell_command_052_3223()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=3224) as shell_command_053_3224:  # 0m:1.070s
            shell_command_053_3224()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=3225) as shell_command_054_3225:  # 0m:0.009s
            shell_command_054_3225()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=3226) as shell_command_055_3226:  # 0m:0.005s
            shell_command_055_3226()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=3227) as shell_command_056_3227:  # 0m:0.156s
            shell_command_056_3227()
        with ShellCommand(r"""osascript -e 'tell application "SoundGrid Studio" to quit' """, ignore_all_errors=True, prog_num=3228) as shell_command_057_3228:  # 0m:0.363s
            shell_command_057_3228()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=3229) as cd_stage_058_3229:  # 0m:0.012s
            cd_stage_058_3229()
            with SetExecPermissionsInSyncFolder(prog_num=3230) as set_exec_permissions_in_sync_folder_059_3230:  # 0m:0.012s
                set_exec_permissions_in_sync_folder_059_3230()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=3231) as cd_stage_060_3231:  # 0m:0.008s
            cd_stage_060_3231()
            with Stage(r"copy", r"StudioRack Data v1.0.0.5", prog_num=3232):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=3233) as should_copy_source_061_3233:  # ?
                    should_copy_source_061_3233()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=3234):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=3235) as copy_dir_to_dir_062_3235:  # ?
                            copy_dir_to_dir_062_3235()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=3236) as unwtar_063_3236:  # ?
                            unwtar_063_3236()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=3237, recursive=True) as chown_064_3237:  # 0m:0.000s
                            chown_064_3237()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.1.0", prog_num=3238):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=3239) as should_copy_source_065_3239:  # ?
                    should_copy_source_065_3239()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=3240):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=3241) as copy_dir_to_dir_066_3241:  # ?
                            copy_dir_to_dir_066_3241()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=3242, recursive=True) as chown_067_3242:  # 0m:0.006s
                            chown_067_3242()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=3243) as rm_globs_068_3243:  # 0m:0.001s
                rm_globs_068_3243()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=3244) as cd_stage_069_3244:  # 0m:0.031s
            cd_stage_069_3244()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=3245):  # 0m:0.031s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=3246) as should_copy_source_070_3246:  # 0m:0.018s
                    should_copy_source_070_3246()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=3247):  # 0m:0.017s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=3248) as copy_dir_to_dir_071_3248:  # 0m:0.017s
                            copy_dir_to_dir_071_3248()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=3249, recursive=True) as chown_072_3249:  # 0m:0.000s
                            chown_072_3249()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=3250) as should_copy_source_073_3250:  # 0m:0.013s
                    should_copy_source_073_3250()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=3251):  # 0m:0.013s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=3252) as copy_dir_to_dir_074_3252:  # 0m:0.012s
                            copy_dir_to_dir_074_3252()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=3253, recursive=True) as chown_075_3253:  # 0m:0.000s
                            chown_075_3253()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/linux/lib/mkl", prog_num=3254) as cd_stage_076_3254:  # 0m:0.007s
            cd_stage_076_3254()
            with Stage(r"copy", r"MKL_x32_IID v1.0.0.1", prog_num=3255):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=3256) as should_copy_source_077_3256:  # ?
                    should_copy_source_077_3256()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/ia32", prog_num=3257):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r".", delete_extraneous_files=True, prog_num=3258) as copy_dir_to_dir_078_3258:  # ?
                            copy_dir_to_dir_078_3258()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", where_to_unwtar=r".", prog_num=3259) as unwtar_079_3259:  # ?
                            unwtar_079_3259()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/ia32", user_id=-1, group_id=-1, prog_num=3260, recursive=True) as chown_080_3260:  # 0m:0.000s
                            chown_080_3260()
            with Stage(r"copy", r"MKL_x64_IID v1.0.0.1", prog_num=3261):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=3262) as should_copy_source_081_3262:  # ?
                    should_copy_source_081_3262()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/intel64", prog_num=3263):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r".", delete_extraneous_files=True, prog_num=3264) as copy_dir_to_dir_082_3264:  # ?
                            copy_dir_to_dir_082_3264()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", where_to_unwtar=r".", prog_num=3265) as unwtar_083_3265:  # ?
                            unwtar_083_3265()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/intel64", user_id=-1, group_id=-1, prog_num=3266, recursive=True) as chown_084_3266:  # 0m:0.006s
                            chown_084_3266()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14", prog_num=3267) as cd_stage_085_3267:  # 0m:0.160s
            cd_stage_085_3267()
            with Stage(r"copy", r"Insert v14.12.90.381", prog_num=3268):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3269) as should_copy_source_086_3269:  # ?
                    should_copy_source_086_3269()
                    with Stage(r"copy source", r"Mac/Plugins/Insert.bundle", prog_num=3270):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r".", delete_extraneous_files=True, prog_num=3271) as copy_dir_to_dir_087_3271:  # ?
                            copy_dir_to_dir_087_3271()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", where_to_unwtar=r".", prog_num=3272) as unwtar_088_3272:  # ?
                            unwtar_088_3272()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/Insert.bundle", user_id=-1, group_id=-1, prog_num=3273, recursive=True) as chown_089_3273:  # 0m:0.001s
                            chown_089_3273()
            with Stage(r"copy", r"StudioRack v14.21.96.552", prog_num=3274):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3275) as should_copy_source_090_3275:  # ?
                    should_copy_source_090_3275()
                    with Stage(r"copy source", r"Mac/Plugins/StudioRack.bundle", prog_num=3276):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r".", delete_extraneous_files=True, prog_num=3277) as copy_dir_to_dir_091_3277:  # ?
                            copy_dir_to_dir_091_3277()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", where_to_unwtar=r".", prog_num=3278) as unwtar_092_3278:  # ?
                            unwtar_092_3278()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/StudioRack.bundle", user_id=-1, group_id=-1, prog_num=3279, recursive=True) as chown_093_3279:  # 0m:0.001s
                            chown_093_3279()
            with Stage(r"copy", r"WavesLib1_14_12_90_381 v14.12.90.381", prog_num=3280):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3281) as should_copy_source_094_3281:  # ?
                    should_copy_source_094_3281()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.12.90.framework", prog_num=3282):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r".", delete_extraneous_files=True, prog_num=3283) as copy_dir_to_dir_095_3283:  # ?
                            copy_dir_to_dir_095_3283()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", where_to_unwtar=r".", prog_num=3284) as unwtar_096_3284:  # ?
                            unwtar_096_3284()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.12.90.framework", user_id=-1, group_id=-1, prog_num=3285, recursive=True) as chown_097_3285:  # 0m:0.000s
                            chown_097_3285()
            with Stage(r"copy", r"WavesLib1_14_21_96_552 v14.21.96.552", prog_num=3286):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3287) as should_copy_source_098_3287:  # ?
                    should_copy_source_098_3287()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.21.96.framework", prog_num=3288):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r".", delete_extraneous_files=True, prog_num=3289) as copy_dir_to_dir_099_3289:  # ?
                            copy_dir_to_dir_099_3289()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", where_to_unwtar=r".", prog_num=3290) as unwtar_100_3290:  # ?
                            unwtar_100_3290()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.21.96.framework", user_id=-1, group_id=-1, prog_num=3291, recursive=True) as chown_101_3291:  # 0m:0.000s
                            chown_101_3291()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V14", own_progress_count=4, prog_num=3295) as resolve_symlink_files_in_folder_102_3295:  # 0m:0.016s
                resolve_symlink_files_in_folder_102_3295()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V14" -c', ignore_all_errors=True, prog_num=3296) as shell_command_103_3296:  # 0m:0.106s
                shell_command_103_3296()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V14"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V14"/Icon?; fi', prog_num=3297) as script_command_104_3297:  # 0m:0.009s
                script_command_104_3297()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3298) as shell_command_105_3298:  # 0m:0.016s
                shell_command_105_3298()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=3299) as create_symlink_106_3299:  # 0m:0.001s
                create_symlink_106_3299()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=3300) as create_symlink_107_3300:  # 0m:0.000s
                create_symlink_107_3300()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=3301) as copy_glob_to_dir_108_3301:  # 0m:0.010s
                copy_glob_to_dir_108_3301()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14/Documents", prog_num=3302) as cd_stage_109_3302:  # 0m:0.000s
            cd_stage_109_3302()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=3303):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V14/Documents", skip_progress_count=3, prog_num=3304) as should_copy_source_110_3304:  # ?
                    should_copy_source_110_3304()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=3305):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=3306) as copy_file_to_dir_111_3306:  # ?
                            copy_file_to_dir_111_3306()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3307) as chmod_and_chown_112_3307:  # 0m:0.000s
                            chmod_and_chown_112_3307()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio", prog_num=3308) as cd_stage_113_3308:  # 0m:0.159s
            cd_stage_113_3308()
            with Stage(r"copy", r"SoundGrid Studio V11", prog_num=3309):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r"/Applications/Waves/SoundGrid Studio", skip_progress_count=4, prog_num=3310) as should_copy_source_114_3310:  # ?
                    should_copy_source_114_3310()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", prog_num=3311):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r".", delete_extraneous_files=True, prog_num=3312) as copy_dir_to_dir_115_3312:  # ?
                            copy_dir_to_dir_115_3312()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", where_to_unwtar=r".", prog_num=3313) as unwtar_116_3313:  # ?
                            unwtar_116_3313()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app", user_id=-1, group_id=-1, prog_num=3314, recursive=True) as chown_117_3314:  # 0m:0.001s
                            chown_117_3314()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio", own_progress_count=4, prog_num=3318) as resolve_symlink_files_in_folder_118_3318:  # 0m:0.015s
                resolve_symlink_files_in_folder_118_3318()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=3319) as shell_command_119_3319:  # 0m:0.013s
                shell_command_119_3319()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid Studio" -c', ignore_all_errors=True, prog_num=3320) as shell_command_120_3320:  # 0m:0.106s
                shell_command_120_3320()
            with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid Studio"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid Studio"/Icon?; fi', prog_num=3321) as script_command_121_3321:  # 0m:0.010s
                script_command_121_3321()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3322) as shell_command_122_3322:  # 0m:0.014s
                shell_command_122_3322()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=3323):  # 0m:0.005s
            with Cd(r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=3324) as cd_123_3324:  # 0m:0.005s
                cd_123_3324()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid Studio/Documents", prog_num=3325)()  # 0m:0.000s
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/eMotionST.pdf", prog_num=3326) as rm_file_124_3326:  # 0m:0.003s
                    rm_file_124_3326()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/StudioRack.pdf", prog_num=3327) as rm_file_125_3327:  # 0m:0.001s
                    rm_file_125_3327()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/SGST_QUICKSTART.mp4", prog_num=3328) as rm_file_126_3328:  # 0m:0.000s
                    rm_file_126_3328()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=3329) as cd_stage_127_3329:  # 0m:0.196s
            cd_stage_127_3329()
            with Stage(r"copy", r"SoundGrid Studio Documents", prog_num=3330):  # 0m:0.196s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=3, prog_num=3331) as should_copy_source_128_3331:  # ?
                    should_copy_source_128_3331()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", prog_num=3332):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=3333) as copy_file_to_dir_129_3333:  # ?
                            copy_file_to_dir_129_3333()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3334) as chmod_and_chown_130_3334:  # 0m:0.000s
                            chmod_and_chown_130_3334()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=3335) as should_copy_source_131_3335:  # 0m:0.178s
                    should_copy_source_131_3335()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", prog_num=3336):  # 0m:0.177s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4.wtar.aa", where_to_unwtar=r".", prog_num=3337) as unwtar_132_3337:  # 0m:0.177s
                            unwtar_132_3337()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=3338) as should_copy_source_133_3338:  # 0m:0.018s
                    should_copy_source_133_3338()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGStudio.pdf", prog_num=3339):  # 0m:0.018s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf.wtar.aa", where_to_unwtar=r".", prog_num=3340) as unwtar_134_3340:  # 0m:0.017s
                            unwtar_134_3340()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3341):  # 0m:0.002s
            with Cd(r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3342) as cd_135_3342:  # 0m:0.002s
                cd_135_3342()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid Studio/Modules", prog_num=3343)()  # 0m:0.000s
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/StudioRack.bundle", prog_num=3344) as rm_dir_136_3344:  # 0m:0.000s
                    rm_dir_136_3344()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/Overview.bundle", prog_num=3345) as rm_dir_137_3345:  # 0m:0.000s
                    rm_dir_137_3345()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-Track.bundle", prog_num=3346) as rm_dir_138_3346:  # 0m:0.000s
                    rm_dir_138_3346()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/StudioRackLib_9.7.framework", prog_num=3347) as rm_dir_139_3347:  # 0m:0.000s
                    rm_dir_139_3347()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackLib_9.7.framework", prog_num=3348) as rm_dir_140_3348:  # 0m:0.000s
                    rm_dir_140_3348()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackLib_11.0.framework", prog_num=3349) as rm_dir_141_3349:  # 0m:0.000s
                    rm_dir_141_3349()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewLib_9.7.framework", prog_num=3350) as rm_dir_142_3350:  # 0m:0.000s
                    rm_dir_142_3350()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_11.0.framework", prog_num=3351) as rm_dir_143_3351:  # 0m:0.000s
                    rm_dir_143_3351()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_11.0.framework", prog_num=3352) as rm_dir_144_3352:  # 0m:0.000s
                    rm_dir_144_3352()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_11.0.framework", prog_num=3353) as rm_dir_145_3353:  # 0m:0.000s
                    rm_dir_145_3353()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_12.4.framework", prog_num=3354) as rm_dir_146_3354:  # 0m:0.000s
                    rm_dir_146_3354()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_12.4.framework", prog_num=3355) as rm_dir_147_3355:  # 0m:0.000s
                    rm_dir_147_3355()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_12.4.framework", prog_num=3356) as rm_dir_148_3356:  # 0m:0.000s
                    rm_dir_148_3356()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_12.8.framework", prog_num=3357) as rm_dir_149_3357:  # 0m:0.000s
                    rm_dir_149_3357()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_12.8.framework", prog_num=3358) as rm_dir_150_3358:  # 0m:0.000s
                    rm_dir_150_3358()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_12.8.framework", prog_num=3359) as rm_dir_151_3359:  # 0m:0.000s
                    rm_dir_151_3359()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_13.3.framework", prog_num=3360) as rm_dir_152_3360:  # 0m:0.000s
                    rm_dir_152_3360()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_13.3.framework", prog_num=3361) as rm_dir_153_3361:  # 0m:0.000s
                    rm_dir_153_3361()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_13.3.framework", prog_num=3362) as rm_dir_154_3362:  # 0m:0.000s
                    rm_dir_154_3362()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3363) as cd_stage_155_3363:  # 0m:0.098s
            cd_stage_155_3363()
            with Stage(r"copy", r"SoundGrid Studio Modules", prog_num=3364):  # 0m:0.053s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3365) as should_copy_source_156_3365:  # ?
                    should_copy_source_156_3365()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", prog_num=3366):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r".", delete_extraneous_files=True, prog_num=3367) as copy_dir_to_dir_157_3367:  # ?
                            copy_dir_to_dir_157_3367()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", where_to_unwtar=r".", prog_num=3368) as unwtar_158_3368:  # ?
                            unwtar_158_3368()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoom.bundle", user_id=-1, group_id=-1, prog_num=3369, recursive=True) as chown_159_3369:  # 0m:0.005s
                            chown_159_3369()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3370) as should_copy_source_160_3370:  # ?
                    should_copy_source_160_3370()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", prog_num=3371):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3372) as copy_dir_to_dir_161_3372:  # ?
                            copy_dir_to_dir_161_3372()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", where_to_unwtar=r".", prog_num=3373) as unwtar_162_3373:  # ?
                            unwtar_162_3373()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3374, recursive=True) as chown_163_3374:  # 0m:0.000s
                            chown_163_3374()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3375) as should_copy_source_164_3375:  # ?
                    should_copy_source_164_3375()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", prog_num=3376):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r".", delete_extraneous_files=True, prog_num=3377) as copy_dir_to_dir_165_3377:  # ?
                            copy_dir_to_dir_165_3377()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", where_to_unwtar=r".", prog_num=3378) as unwtar_166_3378:  # ?
                            unwtar_166_3378()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", user_id=-1, group_id=-1, prog_num=3379, recursive=True) as chown_167_3379:  # 0m:0.000s
                            chown_167_3379()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3380) as should_copy_source_168_3380:  # ?
                    should_copy_source_168_3380()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", prog_num=3381):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3382) as copy_dir_to_dir_169_3382:  # ?
                            copy_dir_to_dir_169_3382()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=3383) as unwtar_170_3383:  # ?
                            unwtar_170_3383()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3384, recursive=True) as chown_171_3384:  # 0m:0.000s
                            chown_171_3384()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3385) as should_copy_source_172_3385:  # 0m:0.044s
                    should_copy_source_172_3385()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", prog_num=3386):  # 0m:0.043s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r".", delete_extraneous_files=True, prog_num=3387) as copy_dir_to_dir_173_3387:  # 0m:0.017s
                            copy_dir_to_dir_173_3387()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", where_to_unwtar=r".", prog_num=3388) as unwtar_174_3388:  # 0m:0.025s
                            unwtar_174_3388()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MIDICommunication.framework", user_id=-1, group_id=-1, prog_num=3389, recursive=True) as chown_175_3389:  # 0m:0.000s
                            chown_175_3389()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3390) as should_copy_source_176_3390:  # ?
                    should_copy_source_176_3390()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", prog_num=3391):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r".", delete_extraneous_files=True, prog_num=3392) as copy_dir_to_dir_177_3392:  # ?
                            copy_dir_to_dir_177_3392()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", where_to_unwtar=r".", prog_num=3393) as unwtar_178_3393:  # ?
                            unwtar_178_3393()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/Mackie_Control.bundle", user_id=-1, group_id=-1, prog_num=3394, recursive=True) as chown_179_3394:  # 0m:0.000s
                            chown_179_3394()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3395) as should_copy_source_180_3395:  # ?
                    should_copy_source_180_3395()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", prog_num=3396):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r".", delete_extraneous_files=True, prog_num=3397) as copy_dir_to_dir_181_3397:  # ?
                            copy_dir_to_dir_181_3397()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", where_to_unwtar=r".", prog_num=3398) as unwtar_182_3398:  # ?
                            unwtar_182_3398()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", user_id=-1, group_id=-1, prog_num=3399, recursive=True) as chown_183_3399:  # 0m:0.000s
                            chown_183_3399()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3400) as should_copy_source_184_3400:  # ?
                    should_copy_source_184_3400()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", prog_num=3401):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r".", delete_extraneous_files=True, prog_num=3402) as copy_dir_to_dir_185_3402:  # ?
                            copy_dir_to_dir_185_3402()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", where_to_unwtar=r".", prog_num=3403) as unwtar_186_3403:  # ?
                            unwtar_186_3403()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", user_id=-1, group_id=-1, prog_num=3404, recursive=True) as chown_187_3404:  # 0m:0.000s
                            chown_187_3404()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3405) as should_copy_source_188_3405:  # ?
                    should_copy_source_188_3405()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", prog_num=3406):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r".", delete_extraneous_files=True, prog_num=3407) as copy_dir_to_dir_189_3407:  # ?
                            copy_dir_to_dir_189_3407()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", where_to_unwtar=r".", prog_num=3408) as unwtar_190_3408:  # ?
                            unwtar_190_3408()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGST.bundle", user_id=-1, group_id=-1, prog_num=3409, recursive=True) as chown_191_3409:  # 0m:0.000s
                            chown_191_3409()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3410) as should_copy_source_192_3410:  # ?
                    should_copy_source_192_3410()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", prog_num=3411):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3412) as copy_dir_to_dir_193_3412:  # ?
                            copy_dir_to_dir_193_3412()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=3413) as unwtar_194_3413:  # ?
                            unwtar_194_3413()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3414, recursive=True) as chown_195_3414:  # 0m:0.000s
                            chown_195_3414()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3415) as should_copy_source_196_3415:  # ?
                    should_copy_source_196_3415()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", prog_num=3416):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r".", delete_extraneous_files=True, prog_num=3417) as copy_dir_to_dir_197_3417:  # ?
                            copy_dir_to_dir_197_3417()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", where_to_unwtar=r".", prog_num=3418) as unwtar_198_3418:  # ?
                            unwtar_198_3418()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/StudioRack_Control.bundle", user_id=-1, group_id=-1, prog_num=3419, recursive=True) as chown_199_3419:  # 0m:0.000s
                            chown_199_3419()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3420) as should_copy_source_200_3420:  # ?
                    should_copy_source_200_3420()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", prog_num=3421):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r".", delete_extraneous_files=True, prog_num=3422) as copy_dir_to_dir_201_3422:  # ?
                            copy_dir_to_dir_201_3422()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", where_to_unwtar=r".", prog_num=3423) as unwtar_202_3423:  # ?
                            unwtar_202_3423()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", user_id=-1, group_id=-1, prog_num=3424, recursive=True) as chown_203_3424:  # 0m:0.000s
                            chown_203_3424()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=3, prog_num=3425) as should_copy_source_204_3425:  # 0m:0.001s
                    should_copy_source_204_3425()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=3426):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r".", prog_num=3427) as copy_file_to_dir_205_3427:  # 0m:0.001s
                            copy_file_to_dir_205_3427()
                        with ChmodAndChown(path=r"com.WavesAudio.SoundGridStudioSilent.plist", mode="a+rw", user_id=-1, group_id=-1, prog_num=3428) as chmod_and_chown_206_3428:  # 0m:0.000s
                            chmod_and_chown_206_3428()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio/Modules", own_progress_count=8, prog_num=3436) as resolve_symlink_files_in_folder_207_3436:  # 0m:0.009s
                resolve_symlink_files_in_folder_207_3436()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3437) as shell_command_208_3437:  # 0m:0.015s
                shell_command_208_3437()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=3438) as shell_command_209_3438:  # 0m:0.015s
                shell_command_209_3438()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3439) as create_symlink_210_3439:  # 0m:0.004s
                create_symlink_210_3439()
            with CreateSymlink(r"/Users/Shared/Waves/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3440) as create_symlink_211_3440:  # 0m:0.001s
                create_symlink_211_3440()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Applications/Waves/SoundGrid/Documents", prog_num=3441):  # 0m:0.001s
            with Cd(r"/Applications/Waves/SoundGrid/Documents", prog_num=3442) as cd_212_3442:  # 0m:0.000s
                cd_212_3442()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid/Documents", prog_num=3443)()  # 0m:0.000s
                with RmFile(r"/Common/SoundGrid/Documents/yamaha-wsg-y16-manual.pdf", prog_num=3444) as rm_file_213_3444:  # 0m:0.000s
                    rm_file_213_3444()
                with RmFile(r"/Common/SoundGrid/Documents/Digico SD Waves Card User Guide.pdf", prog_num=3445) as rm_file_214_3445:  # 0m:0.000s
                    rm_file_214_3445()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Documents", prog_num=3446) as cd_stage_215_3446:  # 0m:0.040s
            cd_stage_215_3446()
            with Stage(r"copy", r"A-H_M_Documents", prog_num=3447):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3448) as should_copy_source_216_3448:  # ?
                    should_copy_source_216_3448()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", prog_num=3449):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r".", prog_num=3450) as copy_file_to_dir_217_3450:  # ?
                            copy_file_to_dir_217_3450()
                        with ChmodAndChown(path=r"A-H M-Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3451) as chmod_and_chown_218_3451:  # 0m:0.000s
                            chmod_and_chown_218_3451()
            with Stage(r"copy", r"Apogee Symphony pdf", prog_num=3452):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3453) as should_copy_source_219_3453:  # ?
                    should_copy_source_219_3453()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", prog_num=3454):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r".", prog_num=3455) as copy_file_to_dir_220_3455:  # ?
                            copy_file_to_dir_220_3455()
                        with ChmodAndChown(path=r"Apogee Symphony MKII SoundGrid User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3456) as chmod_and_chown_221_3456:  # 0m:0.000s
                            chmod_and_chown_221_3456()
            with Stage(r"copy", r"SG BR1 pdf", prog_num=3457):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3458) as should_copy_source_222_3458:  # ?
                    should_copy_source_222_3458()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG BR1.pdf", prog_num=3459):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r".", prog_num=3460) as copy_file_to_dir_223_3460:  # ?
                            copy_file_to_dir_223_3460()
                        with ChmodAndChown(path=r"SG BR1.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3461) as chmod_and_chown_224_3461:  # 0m:0.000s
                            chmod_and_chown_224_3461()
            with Stage(r"copy", r"Burl BMB4 pdf", prog_num=3462):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3463) as should_copy_source_225_3463:  # ?
                    should_copy_source_225_3463()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", prog_num=3464):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r".", prog_num=3465) as copy_file_to_dir_226_3465:  # ?
                            copy_file_to_dir_226_3465()
                        with ChmodAndChown(path=r"Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3466) as chmod_and_chown_227_3466:  # 0m:0.000s
                            chmod_and_chown_227_3466()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3467) as should_copy_source_228_3467:  # ?
                    should_copy_source_228_3467()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", prog_num=3468):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r".", prog_num=3469) as copy_file_to_dir_229_3469:  # ?
                            copy_file_to_dir_229_3469()
                        with ChmodAndChown(path=r"Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3470) as chmod_and_chown_230_3470:  # 0m:0.000s
                            chmod_and_chown_230_3470()
            with Stage(r"copy", r"Cadac pdf", prog_num=3471):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3472) as should_copy_source_231_3472:  # ?
                    should_copy_source_231_3472()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Cadac SG User Guide.pdf", prog_num=3473):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r".", prog_num=3474) as copy_file_to_dir_232_3474:  # ?
                            copy_file_to_dir_232_3474()
                        with ChmodAndChown(path=r"Cadac SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3475) as chmod_and_chown_233_3475:  # 0m:0.000s
                            chmod_and_chown_233_3475()
            with Stage(r"copy", r"Calrec pdf", prog_num=3476):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3477) as should_copy_source_234_3477:  # ?
                    should_copy_source_234_3477()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", prog_num=3478):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r".", prog_num=3479) as copy_file_to_dir_235_3479:  # ?
                            copy_file_to_dir_235_3479()
                        with ChmodAndChown(path=r"Calrec SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3480) as chmod_and_chown_236_3480:  # 0m:0.000s
                            chmod_and_chown_236_3480()
            with Stage(r"copy", r"Crest Tactus pdf", prog_num=3481):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3482) as should_copy_source_237_3482:  # ?
                    should_copy_source_237_3482()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus FOH OM.pdf", prog_num=3483):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r".", prog_num=3484) as copy_file_to_dir_238_3484:  # ?
                            copy_file_to_dir_238_3484()
                        with ChmodAndChown(path=r"Tactus FOH OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3485) as chmod_and_chown_239_3485:  # 0m:0.000s
                            chmod_and_chown_239_3485()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3486) as should_copy_source_240_3486:  # ?
                    should_copy_source_240_3486()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus Stage OM.pdf", prog_num=3487):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r".", prog_num=3488) as copy_file_to_dir_241_3488:  # ?
                            copy_file_to_dir_241_3488()
                        with ChmodAndChown(path=r"Tactus Stage OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3489) as chmod_and_chown_242_3489:  # 0m:0.000s
                            chmod_and_chown_242_3489()
            with Stage(r"copy", r"DLI DLS pdf", prog_num=3490):  # 0m:0.020s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=2, prog_num=3491) as should_copy_source_243_3491:  # 0m:0.020s
                    should_copy_source_243_3491()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DLI DLS User Guide.pdf", prog_num=3492):  # 0m:0.020s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf.wtar.aa", where_to_unwtar=r".", prog_num=3493) as unwtar_244_3493:  # 0m:0.020s
                            unwtar_244_3493()
            with Stage(r"copy", r"DMI Waves pdf", prog_num=3494):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3495) as should_copy_source_245_3495:  # ?
                    should_copy_source_245_3495()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DMI Waves User Guide.pdf", prog_num=3496):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r".", prog_num=3497) as copy_file_to_dir_246_3497:  # ?
                            copy_file_to_dir_246_3497()
                        with ChmodAndChown(path=r"DMI Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3498) as chmod_and_chown_247_3498:  # 0m:0.006s
                            chmod_and_chown_247_3498()
            with Stage(r"copy", r"DN32-WSG pdf", prog_num=3499):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3500) as should_copy_source_248_3500:  # ?
                    should_copy_source_248_3500()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", prog_num=3501):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r".", prog_num=3502) as copy_file_to_dir_249_3502:  # ?
                            copy_file_to_dir_249_3502()
                        with ChmodAndChown(path=r"DN32-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3503) as chmod_and_chown_250_3503:  # 0m:0.000s
                            chmod_and_chown_250_3503()
            with Stage(r"copy", r"DSPro SG4000 pdf", prog_num=3504):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3505) as should_copy_source_251_3505:  # ?
                    should_copy_source_251_3505()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", prog_num=3506):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r".", prog_num=3507) as copy_file_to_dir_252_3507:  # ?
                            copy_file_to_dir_252_3507()
                        with ChmodAndChown(path=r"STAGEGRID 1000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3508) as chmod_and_chown_253_3508:  # 0m:0.000s
                            chmod_and_chown_253_3508()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3509) as should_copy_source_254_3509:  # ?
                    should_copy_source_254_3509()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", prog_num=3510):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r".", prog_num=3511) as copy_file_to_dir_255_3511:  # ?
                            copy_file_to_dir_255_3511()
                        with ChmodAndChown(path=r"STAGEGRID 4000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3512) as chmod_and_chown_256_3512:  # 0m:0.000s
                            chmod_and_chown_256_3512()
            with Stage(r"copy", r"DiGiGrid D Driver pdf", prog_num=3513):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3514) as should_copy_source_257_3514:  # ?
                    should_copy_source_257_3514()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", prog_num=3515):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r".", prog_num=3516) as copy_file_to_dir_258_3516:  # ?
                            copy_file_to_dir_258_3516()
                        with ChmodAndChown(path=r"DiGiGrid D User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3517) as chmod_and_chown_259_3517:  # 0m:0.000s
                            chmod_and_chown_259_3517()
            with Stage(r"copy", r"DiGiGrid M Driver pdf", prog_num=3518):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3519) as should_copy_source_260_3519:  # ?
                    should_copy_source_260_3519()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", prog_num=3520):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r".", prog_num=3521) as copy_file_to_dir_261_3521:  # ?
                            copy_file_to_dir_261_3521()
                        with ChmodAndChown(path=r"DiGiGrid M User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3522) as chmod_and_chown_262_3522:  # 0m:0.000s
                            chmod_and_chown_262_3522()
            with Stage(r"copy", r"DiGiGrid Q Driver pdf", prog_num=3523):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3524) as should_copy_source_263_3524:  # ?
                    should_copy_source_263_3524()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", prog_num=3525):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r".", prog_num=3526) as copy_file_to_dir_264_3526:  # ?
                            copy_file_to_dir_264_3526()
                        with ChmodAndChown(path=r"DiGiGrid Q User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3527) as chmod_and_chown_265_3527:  # 0m:0.000s
                            chmod_and_chown_265_3527()
            with Stage(r"copy", r"DigiGrid S", prog_num=3528):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3529) as should_copy_source_266_3529:  # ?
                    should_copy_source_266_3529()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", prog_num=3530):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=3531) as copy_file_to_dir_267_3531:  # ?
                            copy_file_to_dir_267_3531()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3532) as chmod_and_chown_268_3532:  # 0m:0.000s
                            chmod_and_chown_268_3532()
            with Stage(r"copy", r"Digico SD card pdf", prog_num=3533):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3534) as should_copy_source_269_3534:  # ?
                    should_copy_source_269_3534()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", prog_num=3535):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r".", prog_num=3536) as copy_file_to_dir_270_3536:  # ?
                            copy_file_to_dir_270_3536()
                        with ChmodAndChown(path=r"DiGiCo SD SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3537) as chmod_and_chown_271_3537:  # 0m:0.000s
                            chmod_and_chown_271_3537()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid IO Driver", prog_num=3538):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3539) as should_copy_source_272_3539:  # ?
                    should_copy_source_272_3539()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", prog_num=3540):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r".", prog_num=3541) as copy_file_to_dir_273_3541:  # ?
                            copy_file_to_dir_273_3541()
                        with ChmodAndChown(path=r"DirectOut Exbox.SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3542) as chmod_and_chown_274_3542:  # 0m:0.000s
                            chmod_and_chown_274_3542()
            with Stage(r"copy", r"DirectOut SG.MADI pdf", prog_num=3543):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3544) as should_copy_source_275_3544:  # ?
                    should_copy_source_275_3544()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", prog_num=3545):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r".", prog_num=3546) as copy_file_to_dir_276_3546:  # ?
                            copy_file_to_dir_276_3546()
                        with ChmodAndChown(path=r"DirectOut SG.MADI User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3547) as chmod_and_chown_277_3547:  # 0m:0.000s
                            chmod_and_chown_277_3547()
            with Stage(r"copy", r"DirectOut SoundGrid IO Driver Documents", prog_num=3548):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3549) as should_copy_source_278_3549:  # ?
                    should_copy_source_278_3549()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", prog_num=3550):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r".", prog_num=3551) as copy_file_to_dir_279_3551:  # ?
                            copy_file_to_dir_279_3551()
                        with ChmodAndChown(path=r"DirectOut SG.IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3552) as chmod_and_chown_280_3552:  # 0m:0.000s
                            chmod_and_chown_280_3552()
            with Stage(r"copy", r"Hear Back pdf", prog_num=3553):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3554) as should_copy_source_281_3554:  # ?
                    should_copy_source_281_3554()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", prog_num=3555):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r".", prog_num=3556) as copy_file_to_dir_282_3556:  # ?
                            copy_file_to_dir_282_3556()
                        with ChmodAndChown(path=r"Hear Back PRO SG Card User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3557) as chmod_and_chown_283_3557:  # 0m:0.000s
                            chmod_and_chown_283_3557()
            with Stage(r"copy", r"HearTech pdf", prog_num=3558):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3559) as should_copy_source_284_3559:  # ?
                    should_copy_source_284_3559()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", prog_num=3560):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r".", prog_num=3561) as copy_file_to_dir_285_3561:  # ?
                            copy_file_to_dir_285_3561()
                        with ChmodAndChown(path=r"Hear Technologies SoundGrid Bridge User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3562) as chmod_and_chown_286_3562:  # 0m:0.000s
                            chmod_and_chown_286_3562()
            with Stage(r"copy", r"IOC pdf", prog_num=3563):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3564) as should_copy_source_287_3564:  # ?
                    should_copy_source_287_3564()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOC User Guide.pdf", prog_num=3565):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r".", prog_num=3566) as copy_file_to_dir_288_3566:  # ?
                            copy_file_to_dir_288_3566()
                        with ChmodAndChown(path=r"IOC User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3567) as chmod_and_chown_289_3567:  # 0m:0.000s
                            chmod_and_chown_289_3567()
            with Stage(r"copy", r"IONIC pdf", prog_num=3568):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3569) as should_copy_source_290_3569:  # ?
                    should_copy_source_290_3569()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", prog_num=3570):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r".", prog_num=3571) as copy_file_to_dir_291_3571:  # ?
                            copy_file_to_dir_291_3571()
                        with ChmodAndChown(path=r"IONIC 16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3572) as chmod_and_chown_292_3572:  # 0m:0.000s
                            chmod_and_chown_292_3572()
            with Stage(r"copy", r"IOS pdf", prog_num=3573):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3574) as should_copy_source_293_3574:  # ?
                    should_copy_source_293_3574()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS User Guide.pdf", prog_num=3575):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r".", prog_num=3576) as copy_file_to_dir_294_3576:  # ?
                            copy_file_to_dir_294_3576()
                        with ChmodAndChown(path=r"IOS User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3577) as chmod_and_chown_295_3577:  # 0m:0.000s
                            chmod_and_chown_295_3577()
            with Stage(r"copy", r"IOS-XL pdf", prog_num=3578):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3579) as should_copy_source_296_3579:  # ?
                    should_copy_source_296_3579()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS-XL User Guide.pdf", prog_num=3580):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r".", prog_num=3581) as copy_file_to_dir_297_3581:  # ?
                            copy_file_to_dir_297_3581()
                        with ChmodAndChown(path=r"IOS-XL User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3582) as chmod_and_chown_298_3582:  # 0m:0.000s
                            chmod_and_chown_298_3582()
            with Stage(r"copy", r"IOX pdf", prog_num=3583):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3584) as should_copy_source_299_3584:  # ?
                    should_copy_source_299_3584()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOX User Guide.pdf", prog_num=3585):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r".", prog_num=3586) as copy_file_to_dir_300_3586:  # ?
                            copy_file_to_dir_300_3586()
                        with ChmodAndChown(path=r"IOX User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3587) as chmod_and_chown_301_3587:  # 0m:0.000s
                            chmod_and_chown_301_3587()
            with Stage(r"copy", r"JoeCo BBSG24MP pdf", prog_num=3588):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3589) as should_copy_source_302_3589:  # ?
                    should_copy_source_302_3589()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", prog_num=3590):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r".", prog_num=3591) as copy_file_to_dir_303_3591:  # ?
                            copy_file_to_dir_303_3591()
                        with ChmodAndChown(path=r"JoeCo BBSG24MP User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3592) as chmod_and_chown_304_3592:  # 0m:0.004s
                            chmod_and_chown_304_3592()
            with Stage(r"copy", r"MGB MGO pdf", prog_num=3593):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3594) as should_copy_source_305_3594:  # ?
                    should_copy_source_305_3594()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", prog_num=3595):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r".", prog_num=3596) as copy_file_to_dir_306_3596:  # ?
                            copy_file_to_dir_306_3596()
                        with ChmodAndChown(path=r"DiGiGrid MGR User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3597) as chmod_and_chown_307_3597:  # 0m:0.000s
                            chmod_and_chown_307_3597()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3598) as should_copy_source_308_3598:  # ?
                    should_copy_source_308_3598()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/MGB MGO User Guide.pdf", prog_num=3599):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r".", prog_num=3600) as copy_file_to_dir_309_3600:  # ?
                            copy_file_to_dir_309_3600()
                        with ChmodAndChown(path=r"MGB MGO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3601) as chmod_and_chown_310_3601:  # 0m:0.000s
                            chmod_and_chown_310_3601()
            with Stage(r"copy", r"SG Driver pdf", prog_num=3602):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3603) as should_copy_source_311_3603:  # ?
                    should_copy_source_311_3603()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG Driver.pdf", prog_num=3604):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r".", prog_num=3605) as copy_file_to_dir_312_3605:  # ?
                            copy_file_to_dir_312_3605()
                        with ChmodAndChown(path=r"SG Driver.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3606) as chmod_and_chown_313_3606:  # 0m:0.000s
                            chmod_and_chown_313_3606()
            with Stage(r"copy", r"SoundStudio STG-2412 pdf", prog_num=3607):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3608) as should_copy_source_314_3608:  # ?
                    should_copy_source_314_3608()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-1608 User Guide.pdf", prog_num=3609):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r".", prog_num=3610) as copy_file_to_dir_315_3610:  # ?
                            copy_file_to_dir_315_3610()
                        with ChmodAndChown(path=r"STG-1608 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3611) as chmod_and_chown_316_3611:  # 0m:0.000s
                            chmod_and_chown_316_3611()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3612) as should_copy_source_317_3612:  # ?
                    should_copy_source_317_3612()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-2412 User Guide.pdf", prog_num=3613):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r".", prog_num=3614) as copy_file_to_dir_318_3614:  # ?
                            copy_file_to_dir_318_3614()
                        with ChmodAndChown(path=r"STG-2412 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3615) as chmod_and_chown_319_3615:  # 0m:0.000s
                            chmod_and_chown_319_3615()
            with Stage(r"copy", r"X-WSG pdf", prog_num=3616):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3617) as should_copy_source_320_3617:  # ?
                    should_copy_source_320_3617()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", prog_num=3618):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r".", prog_num=3619) as copy_file_to_dir_321_3619:  # ?
                            copy_file_to_dir_321_3619()
                        with ChmodAndChown(path=r"X-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3620) as chmod_and_chown_322_3620:  # 0m:0.000s
                            chmod_and_chown_322_3620()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3621) as should_copy_source_323_3621:  # ?
                    should_copy_source_323_3621()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG User Guide.pdf", prog_num=3622):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r".", prog_num=3623) as copy_file_to_dir_324_3623:  # ?
                            copy_file_to_dir_324_3623()
                        with ChmodAndChown(path=r"X-WSG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3624) as chmod_and_chown_325_3624:  # 0m:0.000s
                            chmod_and_chown_325_3624()
            with Stage(r"copy", r"Y-16_Documents", prog_num=3625):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3626) as should_copy_source_326_3626:  # ?
                    should_copy_source_326_3626()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", prog_num=3627):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r".", prog_num=3628) as copy_file_to_dir_327_3628:  # ?
                            copy_file_to_dir_327_3628()
                        with ChmodAndChown(path=r"WSG-HY128 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3629) as chmod_and_chown_328_3629:  # 0m:0.000s
                            chmod_and_chown_328_3629()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3630) as should_copy_source_329_3630:  # ?
                    should_copy_source_329_3630()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", prog_num=3631):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r".", prog_num=3632) as copy_file_to_dir_330_3632:  # ?
                            copy_file_to_dir_330_3632()
                        with ChmodAndChown(path=r"WSG-Y16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3633) as chmod_and_chown_331_3633:  # 0m:0.000s
                            chmod_and_chown_331_3633()
            with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/BMB4 SoundGrid Motherboard User Guide.pdf", prog_num=3634) as rm_file_or_dir_332_3634:  # 0m:0.000s
                rm_file_or_dir_332_3634()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Applications/Waves/SoundGrid/Utilities", prog_num=3635):  # 0m:0.001s
            with Cd(r"/Applications/Waves/SoundGrid/Utilities", prog_num=3636) as cd_333_3636:  # 0m:0.001s
                cd_333_3636()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid/Utilities", prog_num=3637)()  # 0m:0.000s
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriver.pkg", prog_num=3638) as rm_file_334_3638:  # 0m:0.000s
                    rm_file_334_3638()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV10.pkg", prog_num=3639) as rm_file_335_3639:  # 0m:0.000s
                    rm_file_335_3639()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.pkg", prog_num=3640) as rm_file_336_3640:  # 0m:0.000s
                    rm_file_336_3640()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.2.pkg", prog_num=3641) as rm_file_337_3641:  # 0m:0.000s
                    rm_file_337_3641()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.3.pkg", prog_num=3642) as rm_file_338_3642:  # 0m:0.000s
                    rm_file_338_3642()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV12.2.pkg", prog_num=3643) as rm_file_339_3643:  # 0m:0.000s
                    rm_file_339_3643()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV12.8.pkg", prog_num=3644) as rm_file_340_3644:  # 0m:0.000s
                    rm_file_340_3644()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV13.3.pkg", prog_num=3645) as rm_file_341_3645:  # 0m:0.000s
                    rm_file_341_3645()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.5.pkg", prog_num=3646) as rm_file_342_3646:  # 0m:0.000s
                    rm_file_342_3646()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.9.pkg", prog_num=3647) as rm_file_343_3647:  # 0m:0.000s
                    rm_file_343_3647()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Utilities", prog_num=3648) as cd_stage_344_3648:  # 0m:0.048s
            cd_stage_344_3648()
            with Stage(r"copy", r"JoeCo BBSG24MP utilities", prog_num=3649):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=3, prog_num=3650) as should_copy_source_345_3650:  # 0m:0.008s
                    should_copy_source_345_3650()
                    with Stage(r"copy source", r"Common/SoundGrid/JoeCo", prog_num=3651):  # 0m:0.008s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r".", delete_extraneous_files=True, prog_num=3652) as copy_dir_to_dir_346_3652:  # 0m:0.007s
                            copy_dir_to_dir_346_3652()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/JoeCo", user_id=-1, group_id=-1, prog_num=3653, recursive=True) as chown_347_3653:  # 0m:0.000s
                            chown_347_3653()
            with Stage(r"copy", r"SoundGrid Control Panel Uninstaller v14.26.48.665", prog_num=3654):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=4, prog_num=3655) as should_copy_source_348_3655:  # ?
                    should_copy_source_348_3655()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", prog_num=3656):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r".", delete_extraneous_files=True, prog_num=3657) as copy_dir_to_dir_349_3657:  # ?
                            copy_dir_to_dir_349_3657()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", where_to_unwtar=r".", prog_num=3658) as unwtar_350_3658:  # ?
                            unwtar_350_3658()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app", user_id=-1, group_id=-1, prog_num=3659, recursive=True) as chown_351_3659:  # 0m:0.000s
                            chown_351_3659()
            with Stage(r"copy", r"SoundGrid V14 ASIO / Core Audio Rec/PB Control Panel v14.26.48.665", prog_num=3660):  # 0m:0.040s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=2, prog_num=3661) as should_copy_source_352_3661:  # 0m:0.040s
                    should_copy_source_352_3661()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", prog_num=3662):  # 0m:0.039s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg.wtar.aa", where_to_unwtar=r".", prog_num=3663) as unwtar_353_3663:  # 0m:0.039s
                            unwtar_353_3663()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V14", prog_num=3664) as cd_stage_354_3664:  # 0m:0.027s
            cd_stage_354_3664()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=3665):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3666) as should_copy_source_355_3666:  # ?
                    should_copy_source_355_3666()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=3667):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=3668) as copy_dir_to_dir_356_3668:  # ?
                            copy_dir_to_dir_356_3668()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=3669) as unwtar_357_3669:  # ?
                            unwtar_357_3669()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=3670, recursive=True) as chown_358_3670:  # ?
                            chown_358_3670()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=3671) as shell_command_359_3671:  # 0m:0.000s
                            shell_command_359_3671()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=3672):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3673) as should_copy_source_360_3673:  # ?
                    should_copy_source_360_3673()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=3674):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=3675) as copy_dir_to_dir_361_3675:  # ?
                            copy_dir_to_dir_361_3675()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=3676) as unwtar_362_3676:  # ?
                            unwtar_362_3676()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=3677, recursive=True) as chown_363_3677:  # ?
                            chown_363_3677()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=3678) as shell_command_364_3678:  # 0m:0.000s
                            shell_command_364_3678()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=3679):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3680) as should_copy_source_365_3680:  # ?
                    should_copy_source_365_3680()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=3681):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=3682) as copy_dir_to_dir_366_3682:  # ?
                            copy_dir_to_dir_366_3682()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=3683) as unwtar_367_3683:  # ?
                            unwtar_367_3683()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=3684, recursive=True) as chown_368_3684:  # ?
                            chown_368_3684()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=3685) as shell_command_369_3685:  # 0m:0.000s
                            shell_command_369_3685()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=3686):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=3687) as should_copy_source_370_3687:  # ?
                    should_copy_source_370_3687()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=3688):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=3689) as copy_dir_to_dir_371_3689:  # ?
                            copy_dir_to_dir_371_3689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=3690) as unwtar_372_3690:  # ?
                            unwtar_372_3690()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=3691, recursive=True) as chown_373_3691:  # ?
                            chown_373_3691()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=3692) as break_hard_link_374_3692:  # ?
                            break_hard_link_374_3692()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=3693) as shell_command_375_3693:  # ?
                            shell_command_375_3693()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=3694, recursive=True) as chown_376_3694:  # ?
                            chown_376_3694()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=3695, recursive=True) as chmod_377_3695:  # 0m:0.001s
                            chmod_377_3695()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=3696):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=3697) as should_copy_source_378_3697:  # ?
                    should_copy_source_378_3697()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=3698):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=3699) as copy_dir_to_dir_379_3699:  # ?
                            copy_dir_to_dir_379_3699()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=3700) as unwtar_380_3700:  # ?
                            unwtar_380_3700()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=3701, recursive=True) as chown_381_3701:  # ?
                            chown_381_3701()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=3702) as break_hard_link_382_3702:  # ?
                            break_hard_link_382_3702()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=3703) as shell_command_383_3703:  # ?
                            shell_command_383_3703()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=3704, recursive=True) as chown_384_3704:  # ?
                            chown_384_3704()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=3705, recursive=True) as chmod_385_3705:  # 0m:0.000s
                            chmod_385_3705()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=3706):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3707) as should_copy_source_386_3707:  # ?
                    should_copy_source_386_3707()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=3708):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=3709) as copy_dir_to_dir_387_3709:  # ?
                            copy_dir_to_dir_387_3709()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=3710) as unwtar_388_3710:  # ?
                            unwtar_388_3710()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=3711, recursive=True) as chown_389_3711:  # ?
                            chown_389_3711()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=3712) as shell_command_390_3712:  # 0m:0.000s
                            shell_command_390_3712()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=3713):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3714) as should_copy_source_391_3714:  # ?
                    should_copy_source_391_3714()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=3715):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=3716) as copy_dir_to_dir_392_3716:  # ?
                            copy_dir_to_dir_392_3716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=3717) as unwtar_393_3717:  # ?
                            unwtar_393_3717()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=3718, recursive=True) as chown_394_3718:  # ?
                            chown_394_3718()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=3719) as shell_command_395_3719:  # 0m:0.000s
                            shell_command_395_3719()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=3720):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3721) as should_copy_source_396_3721:  # ?
                    should_copy_source_396_3721()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=3722):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=3723) as copy_dir_to_dir_397_3723:  # ?
                            copy_dir_to_dir_397_3723()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=3724) as unwtar_398_3724:  # ?
                            unwtar_398_3724()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=3725, recursive=True) as chown_399_3725:  # ?
                            chown_399_3725()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=3726) as shell_command_400_3726:  # 0m:0.000s
                            shell_command_400_3726()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=3727):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3728) as should_copy_source_401_3728:  # ?
                    should_copy_source_401_3728()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=3729):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=3730) as copy_dir_to_dir_402_3730:  # ?
                            copy_dir_to_dir_402_3730()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=3731) as unwtar_403_3731:  # ?
                            unwtar_403_3731()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=3732, recursive=True) as chown_404_3732:  # ?
                            chown_404_3732()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=3733) as shell_command_405_3733:  # 0m:0.000s
                            shell_command_405_3733()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=3734):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Applications/Waves/WaveShells V14", skip_progress_count=7, prog_num=3735) as should_copy_source_406_3735:  # ?
                    should_copy_source_406_3735()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=3736):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=3737) as copy_dir_to_dir_407_3737:  # ?
                            copy_dir_to_dir_407_3737()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=3738) as unwtar_408_3738:  # ?
                            unwtar_408_3738()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=3739, recursive=True) as chown_409_3739:  # ?
                            chown_409_3739()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=3740) as shell_command_410_3740:  # ?
                            shell_command_410_3740()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=3741) as script_command_411_3741:  # ?
                            script_command_411_3741()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3742) as shell_command_412_3742:  # 0m:0.000s
                            shell_command_412_3742()
            with Stage(r"copy", r"WaveShell-AU registration utility v14.12.90.381", prog_num=3743):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r"/Applications/Waves/WaveShells V14", skip_progress_count=4, prog_num=3744) as should_copy_source_413_3744:  # ?
                    should_copy_source_413_3744()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 14.app", prog_num=3745):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r".", delete_extraneous_files=True, prog_num=3746) as copy_dir_to_dir_414_3746:  # ?
                            copy_dir_to_dir_414_3746()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", where_to_unwtar=r".", prog_num=3747) as unwtar_415_3747:  # ?
                            unwtar_415_3747()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app", user_id=-1, group_id=-1, prog_num=3748, recursive=True) as chown_416_3748:  # 0m:0.004s
                            chown_416_3748()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 14.app"', ignore_all_errors=True, prog_num=3749) as shell_command_417_3749:  # 0m:0.013s
                shell_command_417_3749()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=3750) as cd_stage_418_3750:  # 0m:0.006s
            cd_stage_418_3750()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=3751):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=3752) as should_copy_source_419_3752:  # ?
                    should_copy_source_419_3752()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=3753):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=3754) as copy_dir_to_dir_420_3754:  # ?
                            copy_dir_to_dir_420_3754()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=3755) as unwtar_421_3755:  # ?
                            unwtar_421_3755()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=3756, recursive=True) as chown_422_3756:  # ?
                            chown_422_3756()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=3757) as shell_command_423_3757:  # 0m:0.001s
                            shell_command_423_3757()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=3758):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=3759) as should_copy_source_424_3759:  # ?
                    should_copy_source_424_3759()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=3760):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=3761) as copy_dir_to_dir_425_3761:  # ?
                            copy_dir_to_dir_425_3761()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=3762) as unwtar_426_3762:  # ?
                            unwtar_426_3762()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=3763, recursive=True) as chown_427_3763:  # ?
                            chown_427_3763()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=3764) as shell_command_428_3764:  # 0m:0.000s
                            shell_command_428_3764()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves", prog_num=3765) as cd_stage_429_3765:  # 0m:10.583s
            cd_stage_429_3765()
            with Stage(r"copy", r"Qt libraries 5.12.8", prog_num=3766):  # 0m:4.648s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3767) as should_copy_source_430_3767:  # 0m:4.648s
                    should_copy_source_430_3767()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.12.8", prog_num=3768):  # 0m:4.648s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r".", delete_extraneous_files=True, prog_num=3769) as copy_dir_to_dir_431_3769:  # 0m:0.601s
                            copy_dir_to_dir_431_3769()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", where_to_unwtar=r".", prog_num=3770) as unwtar_432_3770:  # 0m:4.046s
                            unwtar_432_3770()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.12.8", user_id=-1, group_id=-1, prog_num=3771, recursive=True) as chown_433_3771:  # 0m:0.000s
                            chown_433_3771()
            with Stage(r"copy", r"QT_5_5_1_FOR_IO_MODULES", prog_num=3772):  # 0m:3.589s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3773) as should_copy_source_434_3773:  # 0m:3.589s
                    should_copy_source_434_3773()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.5.1", prog_num=3774):  # 0m:3.588s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r".", delete_extraneous_files=True, prog_num=3775) as copy_dir_to_dir_435_3775:  # 0m:0.128s
                            copy_dir_to_dir_435_3775()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", where_to_unwtar=r".", prog_num=3776) as unwtar_436_3776:  # 0m:3.460s
                            unwtar_436_3776()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.5.1", user_id=-1, group_id=-1, prog_num=3777, recursive=True) as chown_437_3777:  # 0m:0.000s
                            chown_437_3777()
            with Stage(r"copy", r"Qt libraries 6.2.4", prog_num=3778):  # 0m:2.181s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3779) as should_copy_source_438_3779:  # 0m:2.181s
                    should_copy_source_438_3779()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_6.2.4", prog_num=3780):  # 0m:2.181s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r".", delete_extraneous_files=True, prog_num=3781) as copy_dir_to_dir_439_3781:  # 0m:0.100s
                            copy_dir_to_dir_439_3781()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", where_to_unwtar=r".", prog_num=3782) as unwtar_440_3782:  # 0m:2.080s
                            unwtar_440_3782()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_6.2.4", user_id=-1, group_id=-1, prog_num=3783, recursive=True) as chown_441_3783:  # 0m:0.000s
                            chown_441_3783()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves", own_progress_count=42, prog_num=3825) as resolve_symlink_files_in_folder_442_3825:  # 0m:0.164s
                resolve_symlink_files_in_folder_442_3825()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode", prog_num=3826) as cd_stage_443_3826:  # 0m:0.010s
            cd_stage_443_3826()
            with Stage(r"copy", r"Demo Mode v1.0", prog_num=3827):  # 0m:0.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r"/Library/Application Support/Waves/Demo Mode", skip_progress_count=3, prog_num=3828) as should_copy_source_444_3828:  # 0m:0.009s
                    should_copy_source_444_3828()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14", prog_num=3829):  # 0m:0.009s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r".", delete_extraneous_files=True, prog_num=3830) as copy_dir_to_dir_445_3830:  # 0m:0.009s
                            copy_dir_to_dir_445_3830()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14", user_id=-1, group_id=-1, prog_num=3831, recursive=True) as chown_446_3831:  # 0m:0.000s
                            chown_446_3831()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V14", prog_num=3832) as cd_stage_447_3832:  # 0m:0.000s
            cd_stage_447_3832()
            with Stage(r"copy", r"Demo Mode 2.2 v2.2", prog_num=3833):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r"/Library/Application Support/Waves/Demo Mode/V14", skip_progress_count=3, prog_num=3834) as should_copy_source_448_3834:  # ?
                    should_copy_source_448_3834()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14/2", prog_num=3835):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r".", delete_extraneous_files=True, prog_num=3836) as copy_dir_to_dir_449_3836:  # ?
                            copy_dir_to_dir_449_3836()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14/2", user_id=-1, group_id=-1, prog_num=3837, recursive=True) as chown_450_3837:  # 0m:0.000s
                            chown_450_3837()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=3838) as cd_stage_451_3838:  # 0m:5.416s
            cd_stage_451_3838()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=3839) as rm_file_or_dir_452_3839:  # 0m:0.000s
                rm_file_or_dir_452_3839()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.2.1.3", prog_num=3840):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=3841) as should_copy_source_453_3841:  # ?
                    should_copy_source_453_3841()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=3842):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r".", delete_extraneous_files=True, prog_num=3843) as copy_dir_to_dir_454_3843:  # ?
                            copy_dir_to_dir_454_3843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=3844) as unwtar_455_3844:  # ?
                            unwtar_455_3844()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=3845, recursive=True) as chown_456_3845:  # 0m:0.000s
                            chown_456_3845()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=3846):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=3847) as should_copy_source_457_3847:  # 0m:0.006s
                    should_copy_source_457_3847()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=3848):  # 0m:0.006s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=3849) as unwtar_458_3849:  # 0m:0.006s
                            unwtar_458_3849()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=3850):  # 0m:5.392s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=3851) as should_copy_source_459_3851:  # 0m:5.392s
                    should_copy_source_459_3851()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=3852):  # 0m:5.392s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=3853) as copy_dir_to_dir_460_3853:  # 0m:0.015s
                            copy_dir_to_dir_460_3853()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=3854) as unwtar_461_3854:  # 0m:5.377s
                            unwtar_461_3854()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=3855, recursive=True) as chown_462_3855:  # 0m:0.000s
                            chown_462_3855()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=3856):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=3857) as should_copy_source_463_3857:  # ?
                    should_copy_source_463_3857()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=3858):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=3859) as copy_dir_to_dir_464_3859:  # ?
                            copy_dir_to_dir_464_3859()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=3860) as chmod_465_3860:  # ?
                            chmod_465_3860()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=3861) as chmod_466_3861:  # ?
                            chmod_466_3861()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=3862, recursive=True) as chown_467_3862:  # 0m:0.001s
                            chown_467_3862()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=3865) as resolve_symlink_files_in_folder_468_3865:  # 0m:0.002s
                resolve_symlink_files_in_folder_468_3865()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3866) as shell_command_469_3866:  # 0m:0.013s
                shell_command_469_3866()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/MyMon", prog_num=3867) as cd_stage_470_3867:  # 0m:0.018s
            cd_stage_470_3867()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=3868):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/MyMon", skip_progress_count=4, prog_num=3869) as should_copy_source_471_3869:  # ?
                    should_copy_source_471_3869()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=3870):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=3871) as copy_dir_to_dir_472_3871:  # ?
                            copy_dir_to_dir_472_3871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=3872) as unwtar_473_3872:  # ?
                            unwtar_473_3872()
                        with Chown(path=r"/Library/Application Support/Waves/MyMon/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=3873, recursive=True) as chown_474_3873:  # 0m:0.005s
                            chown_474_3873()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3874) as shell_command_475_3874:  # 0m:0.012s
                shell_command_475_3874()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser", prog_num=3875) as cd_stage_476_3875:  # 0m:0.020s
            cd_stage_476_3875()
            with Stage(r"copy", r"Preset Browser 2.1 v2.1", prog_num=3876):  # 0m:0.010s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=3877) as should_copy_source_477_3877:  # 0m:0.010s
                    should_copy_source_477_3877()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=3878):  # 0m:0.010s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=3879) as copy_dir_to_dir_478_3879:  # 0m:0.010s
                            copy_dir_to_dir_478_3879()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=3880, recursive=True) as chown_479_3880:  # 0m:0.000s
                            chown_479_3880()
            with Stage(r"copy", r"Preset Browser V14 v1.9", prog_num=3881):  # 0m:0.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=3882) as should_copy_source_480_3882:  # 0m:0.009s
                    should_copy_source_480_3882()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=3883):  # 0m:0.009s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=3884) as copy_dir_to_dir_481_3884:  # 0m:0.008s
                            copy_dir_to_dir_481_3884()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=3885, recursive=True) as chown_482_3885:  # 0m:0.000s
                            chown_482_3885()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/RemoteServices", prog_num=3886) as cd_stage_483_3886:  # 0m:0.013s
            cd_stage_483_3886()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=3887):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/RemoteServices", skip_progress_count=4, prog_num=3888) as should_copy_source_484_3888:  # ?
                    should_copy_source_484_3888()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=3889):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=3890) as copy_dir_to_dir_485_3890:  # ?
                            copy_dir_to_dir_485_3890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=3891) as unwtar_486_3891:  # ?
                            unwtar_486_3891()
                        with Chown(path=r"/Library/Application Support/Waves/RemoteServices/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=3892, recursive=True) as chown_487_3892:  # 0m:0.000s
                            chown_487_3892()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3893) as shell_command_488_3893:  # 0m:0.013s
                shell_command_488_3893()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Session Converters", prog_num=3894) as cd_stage_489_3894:  # 0m:0.007s
            cd_stage_489_3894()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_9_9.bundle", prog_num=3895) as rm_file_or_dir_490_3895:  # 0m:0.000s
                rm_file_or_dir_490_3895()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_2_18.bundle", prog_num=3896) as rm_file_or_dir_491_3896:  # 0m:0.000s
                rm_file_or_dir_491_3896()
            with Stage(r"copy", r"Converter", prog_num=3897):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3898) as should_copy_source_492_3898:  # ?
                    should_copy_source_492_3898()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", prog_num=3899):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r".", delete_extraneous_files=True, prog_num=3900) as copy_dir_to_dir_493_3900:  # ?
                            copy_dir_to_dir_493_3900()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", where_to_unwtar=r".", prog_num=3901) as unwtar_494_3901:  # ?
                            unwtar_494_3901()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_2x.bundle", user_id=-1, group_id=-1, prog_num=3902, recursive=True) as chown_495_3902:  # 0m:0.000s
                            chown_495_3902()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3903) as should_copy_source_496_3903:  # ?
                    should_copy_source_496_3903()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", prog_num=3904):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r".", delete_extraneous_files=True, prog_num=3905) as copy_dir_to_dir_497_3905:  # ?
                            copy_dir_to_dir_497_3905()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", where_to_unwtar=r".", prog_num=3906) as unwtar_498_3906:  # ?
                            unwtar_498_3906()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_3x.bundle", user_id=-1, group_id=-1, prog_num=3907, recursive=True) as chown_499_3907:  # 0m:0.004s
                            chown_499_3907()
            with Stage(r"copy", r"MixerSessionConverter", prog_num=3908):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3909) as should_copy_source_500_3909:  # ?
                    should_copy_source_500_3909()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter.bundle", prog_num=3910):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r".", delete_extraneous_files=True, prog_num=3911) as copy_dir_to_dir_501_3911:  # ?
                            copy_dir_to_dir_501_3911()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", where_to_unwtar=r".", prog_num=3912) as unwtar_502_3912:  # ?
                            unwtar_502_3912()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter.bundle", user_id=-1, group_id=-1, prog_num=3913, recursive=True) as chown_503_3913:  # 0m:0.000s
                            chown_503_3913()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3914):  # 0m:0.022s
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3915) as cd_504_3915:  # 0m:0.022s
                cd_504_3915()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3916)()  # 0m:0.000s
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGB.wfi", prog_num=3917) as rm_file_505_3917:  # 0m:0.000s
                    rm_file_505_3917()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGB.wfi", prog_num=3918) as rm_file_506_3918:  # 0m:0.000s
                    rm_file_506_3918()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGB.wfi", prog_num=3919) as rm_file_507_3919:  # 0m:0.000s
                    rm_file_507_3919()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGO.wfi", prog_num=3920) as rm_file_508_3920:  # 0m:0.000s
                    rm_file_508_3920()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGO.wfi", prog_num=3921) as rm_file_509_3921:  # 0m:0.000s
                    rm_file_509_3921()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGO.wfi", prog_num=3922) as rm_file_510_3922:  # 0m:0.000s
                    rm_file_510_3922()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridD.wfi", prog_num=3923) as rm_file_511_3923:  # 0m:0.000s
                    rm_file_511_3923()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridD.wfi", prog_num=3924) as rm_file_512_3924:  # 0m:0.000s
                    rm_file_512_3924()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridD.wfi", prog_num=3925) as rm_file_513_3925:  # 0m:0.000s
                    rm_file_513_3925()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridM.wfi", prog_num=3926) as rm_file_514_3926:  # 0m:0.000s
                    rm_file_514_3926()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridM.wfi", prog_num=3927) as rm_file_515_3927:  # 0m:0.000s
                    rm_file_515_3927()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridM.wfi", prog_num=3928) as rm_file_516_3928:  # 0m:0.000s
                    rm_file_516_3928()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridQ.wfi", prog_num=3929) as rm_file_517_3929:  # 0m:0.000s
                    rm_file_517_3929()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridQ.wfi", prog_num=3930) as rm_file_518_3930:  # 0m:0.000s
                    rm_file_518_3930()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridQ.wfi", prog_num=3931) as rm_file_519_3931:  # 0m:0.000s
                    rm_file_519_3931()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLI.wfi", prog_num=3932) as rm_file_520_3932:  # 0m:0.000s
                    rm_file_520_3932()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLI.wfi", prog_num=3933) as rm_file_521_3933:  # 0m:0.000s
                    rm_file_521_3933()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLI.wfi", prog_num=3934) as rm_file_522_3934:  # 0m:0.000s
                    rm_file_522_3934()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLS.wfi", prog_num=3935) as rm_file_523_3935:  # 0m:0.000s
                    rm_file_523_3935()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLS.wfi", prog_num=3936) as rm_file_524_3936:  # 0m:0.000s
                    rm_file_524_3936()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLS.wfi", prog_num=3937) as rm_file_525_3937:  # 0m:0.000s
                    rm_file_525_3937()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s3.wfi", prog_num=3938) as rm_file_526_3938:  # 0m:0.000s
                    rm_file_526_3938()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s3.wfi", prog_num=3939) as rm_file_527_3939:  # 0m:0.000s
                    rm_file_527_3939()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s3.wfi", prog_num=3940) as rm_file_528_3940:  # 0m:0.000s
                    rm_file_528_3940()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s6.wfi", prog_num=3941) as rm_file_529_3941:  # 0m:0.000s
                    rm_file_529_3941()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s6.wfi", prog_num=3942) as rm_file_530_3942:  # 0m:0.000s
                    rm_file_530_3942()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s6.wfi", prog_num=3943) as rm_file_531_3943:  # 0m:0.000s
                    rm_file_531_3943()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_A_H_V3.wfi", prog_num=3944) as rm_file_532_3944:  # 0m:0.000s
                    rm_file_532_3944()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_A_H_V3.wfi", prog_num=3945) as rm_file_533_3945:  # 0m:0.000s
                    rm_file_533_3945()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_A_H_V3.wfi", prog_num=3946) as rm_file_534_3946:  # 0m:0.000s
                    rm_file_534_3946()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_A_H_V3.wfi", prog_num=3947) as rm_file_535_3947:  # 0m:0.000s
                    rm_file_535_3947()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_A_H_V3.wfi", prog_num=3948) as rm_file_536_3948:  # 0m:0.000s
                    rm_file_536_3948()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.9_A_H_V3.wfi", prog_num=3949) as rm_file_537_3949:  # 0m:0.000s
                    rm_file_537_3949()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_sq.wfi", prog_num=3950) as rm_file_538_3950:  # 0m:0.000s
                    rm_file_538_3950()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_sq.wfi", prog_num=3951) as rm_file_539_3951:  # 0m:0.000s
                    rm_file_539_3951()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_sq.wfi", prog_num=3952) as rm_file_540_3952:  # 0m:0.000s
                    rm_file_540_3952()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_X_WSG.wfi", prog_num=3953) as rm_file_541_3953:  # 0m:0.000s
                    rm_file_541_3953()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG.wfi", prog_num=3954) as rm_file_542_3954:  # 0m:0.000s
                    rm_file_542_3954()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG.wfi", prog_num=3955) as rm_file_543_3955:  # 0m:0.000s
                    rm_file_543_3955()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s3.wfi", prog_num=3956) as rm_file_544_3956:  # 0m:0.000s
                    rm_file_544_3956()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s3.wfi", prog_num=3957) as rm_file_545_3957:  # 0m:0.000s
                    rm_file_545_3957()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s3.wfi", prog_num=3958) as rm_file_546_3958:  # 0m:0.000s
                    rm_file_546_3958()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s3.wfi", prog_num=3959) as rm_file_547_3959:  # 0m:0.000s
                    rm_file_547_3959()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s6.wfi", prog_num=3960) as rm_file_548_3960:  # 0m:0.000s
                    rm_file_548_3960()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s6.wfi", prog_num=3961) as rm_file_549_3961:  # 0m:0.000s
                    rm_file_549_3961()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s6.wfi", prog_num=3962) as rm_file_550_3962:  # 0m:0.000s
                    rm_file_550_3962()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s6.wfi", prog_num=3963) as rm_file_551_3963:  # 0m:0.000s
                    rm_file_551_3963()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Hy.wfi", prog_num=3964) as rm_file_552_3964:  # 0m:0.000s
                    rm_file_552_3964()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Hy.wfi", prog_num=3965) as rm_file_553_3965:  # 0m:0.000s
                    rm_file_553_3965()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC.wfi", prog_num=3966) as rm_file_554_3966:  # 0m:0.000s
                    rm_file_554_3966()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC.wfi", prog_num=3967) as rm_file_555_3967:  # 0m:0.000s
                    rm_file_555_3967()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC.wfi", prog_num=3968) as rm_file_556_3968:  # 0m:0.000s
                    rm_file_556_3968()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC_micro.wfi", prog_num=3969) as rm_file_557_3969:  # 0m:0.000s
                    rm_file_557_3969()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC_micro.wfi", prog_num=3970) as rm_file_558_3970:  # 0m:0.000s
                    rm_file_558_3970()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC_micro.wfi", prog_num=3971) as rm_file_559_3971:  # 0m:0.000s
                    rm_file_559_3971()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS.wfi", prog_num=3972) as rm_file_560_3972:  # 0m:0.000s
                    rm_file_560_3972()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS.wfi", prog_num=3973) as rm_file_561_3973:  # 0m:0.000s
                    rm_file_561_3973()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS.wfi", prog_num=3974) as rm_file_562_3974:  # 0m:0.000s
                    rm_file_562_3974()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_micro.wfi", prog_num=3975) as rm_file_563_3975:  # 0m:0.000s
                    rm_file_563_3975()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_micro.wfi", prog_num=3976) as rm_file_564_3976:  # 0m:0.000s
                    rm_file_564_3976()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_micro.wfi", prog_num=3977) as rm_file_565_3977:  # 0m:0.000s
                    rm_file_565_3977()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.13_IONIC16_S25.wfi", prog_num=3978) as rm_file_566_3978:  # 0m:0.000s
                    rm_file_566_3978()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.22_IONIC16_S25.wfi", prog_num=3979) as rm_file_567_3979:  # 0m:0.000s
                    rm_file_567_3979()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL.wfi", prog_num=3980) as rm_file_568_3980:  # 0m:0.000s
                    rm_file_568_3980()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL.wfi", prog_num=3981) as rm_file_569_3981:  # 0m:0.000s
                    rm_file_569_3981()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL.wfi", prog_num=3982) as rm_file_570_3982:  # 0m:0.000s
                    rm_file_570_3982()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL_micro.wfi", prog_num=3983) as rm_file_571_3983:  # 0m:0.004s
                    rm_file_571_3983()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL_micro.wfi", prog_num=3984) as rm_file_572_3984:  # 0m:0.001s
                    rm_file_572_3984()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL_micro.wfi", prog_num=3985) as rm_file_573_3985:  # 0m:0.000s
                    rm_file_573_3985()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX.wfi", prog_num=3986) as rm_file_574_3986:  # 0m:0.000s
                    rm_file_574_3986()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX.wfi", prog_num=3987) as rm_file_575_3987:  # 0m:0.000s
                    rm_file_575_3987()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX.wfi", prog_num=3988) as rm_file_576_3988:  # 0m:0.000s
                    rm_file_576_3988()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX_micro.wfi", prog_num=3989) as rm_file_577_3989:  # 0m:0.000s
                    rm_file_577_3989()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX_micro.wfi", prog_num=3990) as rm_file_578_3990:  # 0m:0.000s
                    rm_file_578_3990()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX_micro.wfi", prog_num=3991) as rm_file_579_3991:  # 0m:0.000s
                    rm_file_579_3991()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Cadac.wfi", prog_num=3992) as rm_file_580_3992:  # 0m:0.000s
                    rm_file_580_3992()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Cadac.wfi", prog_num=3993) as rm_file_581_3993:  # 0m:0.000s
                    rm_file_581_3993()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Cadac.wfi", prog_num=3994) as rm_file_582_3994:  # 0m:0.000s
                    rm_file_582_3994()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex.wfi", prog_num=3995) as rm_file_583_3995:  # 0m:0.000s
                    rm_file_583_3995()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex.wfi", prog_num=3996) as rm_file_584_3996:  # 0m:0.000s
                    rm_file_584_3996()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex_micro.wfi", prog_num=3997) as rm_file_585_3997:  # 0m:0.000s
                    rm_file_585_3997()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex.wfi", prog_num=3998) as rm_file_586_3998:  # 0m:0.000s
                    rm_file_586_3998()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex_micro.wfi", prog_num=3999) as rm_file_587_3999:  # 0m:0.000s
                    rm_file_587_3999()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex_micro.wfi", prog_num=4000) as rm_file_588_4000:  # 0m:0.000s
                    rm_file_588_4000()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Calrec.wfi", prog_num=4001) as rm_file_589_4001:  # 0m:0.000s
                    rm_file_589_4001()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Calrec.wfi", prog_num=4002) as rm_file_590_4002:  # 0m:0.000s
                    rm_file_590_4002()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Calrec.wfi", prog_num=4003) as rm_file_591_4003:  # 0m:0.000s
                    rm_file_591_4003()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH.wfi", prog_num=4004) as rm_file_592_4004:  # 0m:0.000s
                    rm_file_592_4004()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB.wfi", prog_num=4005) as rm_file_593_4005:  # 0m:0.000s
                    rm_file_593_4005()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH.wfi", prog_num=4006) as rm_file_594_4006:  # 0m:0.000s
                    rm_file_594_4006()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB.wfi", prog_num=4007) as rm_file_595_4007:  # 0m:0.000s
                    rm_file_595_4007()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH.wfi", prog_num=4008) as rm_file_596_4008:  # 0m:0.000s
                    rm_file_596_4008()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB.wfi", prog_num=4009) as rm_file_597_4009:  # 0m:0.000s
                    rm_file_597_4009()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH_micro.wfi", prog_num=4010) as rm_file_598_4010:  # 0m:0.000s
                    rm_file_598_4010()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB_micro.wfi", prog_num=4011) as rm_file_599_4011:  # 0m:0.000s
                    rm_file_599_4011()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH_micro.wfi", prog_num=4012) as rm_file_600_4012:  # 0m:0.000s
                    rm_file_600_4012()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB_micro.wfi", prog_num=4013) as rm_file_601_4013:  # 0m:0.000s
                    rm_file_601_4013()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH_micro.wfi", prog_num=4014) as rm_file_602_4014:  # 0m:0.000s
                    rm_file_602_4014()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB_micro.wfi", prog_num=4015) as rm_file_603_4015:  # 0m:0.000s
                    rm_file_603_4015()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiCo_t2_64ch.wfi", prog_num=4016) as rm_file_604_4016:  # 0m:0.000s
                    rm_file_604_4016()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_DigiCo_t2_64ch.wfi", prog_num=4017) as rm_file_605_4017:  # 0m:0.000s
                    rm_file_605_4017()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiCo_t2_64ch.wfi", prog_num=4018) as rm_file_606_4018:  # 0m:0.000s
                    rm_file_606_4018()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiCo_t2_64ch.wfi", prog_num=4019) as rm_file_607_4019:  # 0m:0.000s
                    rm_file_607_4019()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Digico_SD_S6.wfi", prog_num=4020) as rm_file_608_4020:  # 0m:0.000s
                    rm_file_608_4020()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_Digico_SD_S6.wfi", prog_num=4021) as rm_file_609_4021:  # 0m:0.000s
                    rm_file_609_4021()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Digico_SD_S6.wfi", prog_num=4022) as rm_file_610_4022:  # 0m:0.000s
                    rm_file_610_4022()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Digico_SD_S6.wfi", prog_num=4023) as rm_file_611_4023:  # 0m:0.000s
                    rm_file_611_4023()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.8_Digico_SD_S6.wfi", prog_num=4024) as rm_file_612_4024:  # 0m:0.000s
                    rm_file_612_4024()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Digico_SD_S6.wfi", prog_num=4025) as rm_file_613_4025:  # 0m:0.000s
                    rm_file_613_4025()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Digico_SD_S6.wfi", prog_num=4026) as rm_file_614_4026:  # 0m:0.000s
                    rm_file_614_4026()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigicoDMI.wfi", prog_num=4027) as rm_file_615_4027:  # 0m:0.000s
                    rm_file_615_4027()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigicoDMI.wfi", prog_num=4028) as rm_file_616_4028:  # 0m:0.000s
                    rm_file_616_4028()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigicoDMI.wfi", prog_num=4029) as rm_file_617_4029:  # 0m:0.000s
                    rm_file_617_4029()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigicoDMI.wfi", prog_num=4030) as rm_file_618_4030:  # 0m:0.000s
                    rm_file_618_4030()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech.wfi", prog_num=4031) as rm_file_619_4031:  # 0m:0.000s
                    rm_file_619_4031()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech.wfi", prog_num=4032) as rm_file_620_4032:  # 0m:0.000s
                    rm_file_620_4032()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech.wfi", prog_num=4033) as rm_file_621_4033:  # 0m:0.000s
                    rm_file_621_4033()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech.wfi", prog_num=4034) as rm_file_622_4034:  # 0m:0.000s
                    rm_file_622_4034()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech_64ch.wfi", prog_num=4035) as rm_file_623_4035:  # 0m:0.000s
                    rm_file_623_4035()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech_64ch.wfi", prog_num=4036) as rm_file_624_4036:  # 0m:0.000s
                    rm_file_624_4036()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech_64ch.wfi", prog_num=4037) as rm_file_625_4037:  # 0m:0.000s
                    rm_file_625_4037()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech_64ch.wfi", prog_num=4038) as rm_file_626_4038:  # 0m:0.000s
                    rm_file_626_4038()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.12_Heartech_64ch.wfi", prog_num=4039) as rm_file_627_4039:  # 0m:0.000s
                    rm_file_627_4039()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412.wfi", prog_num=4040) as rm_file_628_4040:  # 0m:0.000s
                    rm_file_628_4040()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412.wfi", prog_num=4041) as rm_file_629_4041:  # 0m:0.000s
                    rm_file_629_4041()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412.wfi", prog_num=4042) as rm_file_630_4042:  # 0m:0.000s
                    rm_file_630_4042()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608.wfi", prog_num=4043) as rm_file_631_4043:  # 0m:0.000s
                    rm_file_631_4043()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608.wfi", prog_num=4044) as rm_file_632_4044:  # 0m:0.000s
                    rm_file_632_4044()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608.wfi", prog_num=4045) as rm_file_633_4045:  # 0m:0.000s
                    rm_file_633_4045()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412_micro.wfi", prog_num=4046) as rm_file_634_4046:  # 0m:0.000s
                    rm_file_634_4046()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412_micro.wfi", prog_num=4047) as rm_file_635_4047:  # 0m:0.000s
                    rm_file_635_4047()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412_micro.wfi", prog_num=4048) as rm_file_636_4048:  # 0m:0.000s
                    rm_file_636_4048()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608_micro.wfi", prog_num=4049) as rm_file_637_4049:  # 0m:0.000s
                    rm_file_637_4049()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608_micro.wfi", prog_num=4050) as rm_file_638_4050:  # 0m:0.000s
                    rm_file_638_4050()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608_micro.wfi", prog_num=4051) as rm_file_639_4051:  # 0m:0.000s
                    rm_file_639_4051()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut.wfi", prog_num=4052) as rm_file_640_4052:  # 0m:0.000s
                    rm_file_640_4052()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut.wfi", prog_num=4053) as rm_file_641_4053:  # 0m:0.000s
                    rm_file_641_4053()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut.wfi", prog_num=4054) as rm_file_642_4054:  # 0m:0.000s
                    rm_file_642_4054()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut_micro.wfi", prog_num=4055) as rm_file_643_4055:  # 0m:0.000s
                    rm_file_643_4055()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut_micro.wfi", prog_num=4056) as rm_file_644_4056:  # 0m:0.000s
                    rm_file_644_4056()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut_micro.wfi", prog_num=4057) as rm_file_645_4057:  # 0m:0.000s
                    rm_file_645_4057()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony.wfi", prog_num=4058) as rm_file_646_4058:  # 0m:0.000s
                    rm_file_646_4058()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony.wfi", prog_num=4059) as rm_file_647_4059:  # 0m:0.000s
                    rm_file_647_4059()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony.wfi", prog_num=4060) as rm_file_648_4060:  # 0m:0.000s
                    rm_file_648_4060()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony_micro.wfi", prog_num=4061) as rm_file_649_4061:  # 0m:0.000s
                    rm_file_649_4061()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony_micro.wfi", prog_num=4062) as rm_file_650_4062:  # 0m:0.000s
                    rm_file_650_4062()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony_micro.wfi", prog_num=4063) as rm_file_651_4063:  # 0m:0.000s
                    rm_file_651_4063()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_BurlAudio_Bmb4.wfi", prog_num=4064) as rm_file_652_4064:  # 0m:0.000s
                    rm_file_652_4064()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_BurlAudio_Bmb4.wfi", prog_num=4065) as rm_file_653_4065:  # 0m:0.000s
                    rm_file_653_4065()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=4066) as rm_file_654_4066:  # 0m:0.001s
                    rm_file_654_4066()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro.wfi", prog_num=4067) as rm_file_655_4067:  # 0m:0.000s
                    rm_file_655_4067()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro.wfi", prog_num=4068) as rm_file_656_4068:  # 0m:0.000s
                    rm_file_656_4068()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro.wfi", prog_num=4069) as rm_file_657_4069:  # 0m:0.000s
                    rm_file_657_4069()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro.wfi", prog_num=4070) as rm_file_658_4070:  # 0m:0.000s
                    rm_file_658_4070()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k.wfi", prog_num=4071) as rm_file_659_4071:  # 0m:0.000s
                    rm_file_659_4071()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k.wfi", prog_num=4072) as rm_file_660_4072:  # 0m:0.000s
                    rm_file_660_4072()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k.wfi", prog_num=4073) as rm_file_661_4073:  # 0m:0.000s
                    rm_file_661_4073()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k.wfi", prog_num=4074) as rm_file_662_4074:  # 0m:0.000s
                    rm_file_662_4074()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k_micro.wfi", prog_num=4075) as rm_file_663_4075:  # 0m:0.000s
                    rm_file_663_4075()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k_micro.wfi", prog_num=4076) as rm_file_664_4076:  # 0m:0.000s
                    rm_file_664_4076()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k_micro.wfi", prog_num=4077) as rm_file_665_4077:  # 0m:0.000s
                    rm_file_665_4077()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k_micro.wfi", prog_num=4078) as rm_file_666_4078:  # 0m:0.000s
                    rm_file_666_4078()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_sg1k_micro.wfi", prog_num=4079) as rm_file_667_4079:  # 0m:0.004s
                    rm_file_667_4079()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro_micro.wfi", prog_num=4080) as rm_file_668_4080:  # 0m:0.001s
                    rm_file_668_4080()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_micro.wfi", prog_num=4081) as rm_file_669_4081:  # 0m:0.000s
                    rm_file_669_4081()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_micro.wfi", prog_num=4082) as rm_file_670_4082:  # 0m:0.000s
                    rm_file_670_4082()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_micro.wfi", prog_num=4083) as rm_file_671_4083:  # 0m:0.000s
                    rm_file_671_4083()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_micro.wfi", prog_num=4084) as rm_file_672_4084:  # 0m:0.000s
                    rm_file_672_4084()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_micro.wfi", prog_num=4085) as rm_file_673_4085:  # 0m:0.000s
                    rm_file_673_4085()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Joeco.wfi", prog_num=4086) as rm_file_674_4086:  # 0m:0.000s
                    rm_file_674_4086()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Joeco.wfi", prog_num=4087) as rm_file_675_4087:  # 0m:0.000s
                    rm_file_675_4087()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Joeco.wfi", prog_num=4088) as rm_file_676_4088:  # 0m:0.000s
                    rm_file_676_4088()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_10.3_BR1_AVB.wfi", prog_num=4089) as rm_file_677_4089:  # 0m:0.000s
                    rm_file_677_4089()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_12.1_BR1_AVB.wfi", prog_num=4090) as rm_file_678_4090:  # 0m:0.000s
                    rm_file_678_4090()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_13.4_BR1_AVB.wfi", prog_num=4091) as rm_file_679_4091:  # 0m:0.000s
                    rm_file_679_4091()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_X_WSG_DN32.wfi", prog_num=4092) as rm_file_680_4092:  # 0m:0.000s
                    rm_file_680_4092()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG_DN32.wfi", prog_num=4093) as rm_file_681_4093:  # 0m:0.000s
                    rm_file_681_4093()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG_DN32.wfi", prog_num=4094) as rm_file_682_4094:  # 0m:0.000s
                    rm_file_682_4094()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=4095) as cd_stage_683_4095:  # 0m:0.104s
            cd_stage_683_4095()
            with Stage(r"copy", r"Allen & Heath M s3 Firmware v13.4.0.205", prog_num=4096):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4097) as should_copy_source_684_4097:  # ?
                    should_copy_source_684_4097()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", prog_num=4098):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r".", prog_num=4099) as copy_file_to_dir_685_4099:  # ?
                            copy_file_to_dir_685_4099()
                        with ChmodAndChown(path=r"IO_13.4_AH_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4100) as chmod_and_chown_686_4100:  # 0m:0.000s
                            chmod_and_chown_686_4100()
            with Stage(r"copy", r"Allen & Heath M s6 Firmware v13.4.0.205", prog_num=4101):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4102) as should_copy_source_687_4102:  # ?
                    should_copy_source_687_4102()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", prog_num=4103):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r".", prog_num=4104) as copy_file_to_dir_688_4104:  # ?
                            copy_file_to_dir_688_4104()
                        with ChmodAndChown(path=r"IO_13.4_AH_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4105) as chmod_and_chown_689_4105:  # 0m:0.000s
                            chmod_and_chown_689_4105()
            with Stage(r"copy", r"Allen & Heath sq Firmware v13.4.0.205", prog_num=4106):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4107) as should_copy_source_690_4107:  # ?
                    should_copy_source_690_4107()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", prog_num=4108):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r".", prog_num=4109) as copy_file_to_dir_691_4109:  # ?
                            copy_file_to_dir_691_4109()
                        with ChmodAndChown(path=r"IO_13.4_AH_sq.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4110) as chmod_and_chown_692_4110:  # 0m:0.000s
                            chmod_and_chown_692_4110()
            with Stage(r"copy", r"Allen & Heath M v3 Firmware v14.12.33.324", prog_num=4111):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4112) as should_copy_source_693_4112:  # ?
                    should_copy_source_693_4112()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", prog_num=4113):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r".", prog_num=4114) as copy_file_to_dir_694_4114:  # ?
                            copy_file_to_dir_694_4114()
                        with ChmodAndChown(path=r"IO_14.12_A_H_V3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4115) as chmod_and_chown_695_4115:  # 0m:0.000s
                            chmod_and_chown_695_4115()
            with Stage(r"copy", r"Apogee_Symphony_Firmware_13_4 v13.4.0.205", prog_num=4116):  # 0m:0.014s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4117) as should_copy_source_696_4117:  # 0m:0.014s
                    should_copy_source_696_4117()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", prog_num=4118):  # 0m:0.013s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4119) as unwtar_697_4119:  # 0m:0.013s
                            unwtar_697_4119()
            with Stage(r"copy", r"Apogee_Symphony_micro_Firmware_13_4 v13.4.0.205", prog_num=4120):  # 0m:0.032s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4121) as should_copy_source_698_4121:  # 0m:0.032s
                    should_copy_source_698_4121()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", prog_num=4122):  # 0m:0.032s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4123) as unwtar_699_4123:  # 0m:0.032s
                            unwtar_699_4123()
            with Stage(r"copy", r"SoundGrid BR-1 Firmware v13.7.87.375", prog_num=4124):  # 0m:0.027s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4125) as should_copy_source_700_4125:  # 0m:0.024s
                    should_copy_source_700_4125()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", prog_num=4126):  # 0m:0.023s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4127) as unwtar_701_4127:  # 0m:0.023s
                            unwtar_701_4127()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Firmware 14.25 v14.25.21.582", prog_num=4128):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4129) as should_copy_source_702_4129:  # ?
                    should_copy_source_702_4129()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", prog_num=4130):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r".", prog_num=4131) as copy_file_to_dir_703_4131:  # ?
                            copy_file_to_dir_703_4131()
                        with ChmodAndChown(path=r"IO_14.25_Behringer_WING_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4132) as chmod_and_chown_704_4132:  # 0m:0.000s
                            chmod_and_chown_704_4132()
            with Stage(r"copy", r"Burl Audio BMB4 Firmware v13.4.0.205", prog_num=4133):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4134) as should_copy_source_705_4134:  # 0m:0.005s
                    should_copy_source_705_4134()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=4135):  # 0m:0.005s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r".", prog_num=4136) as copy_file_to_dir_706_4136:  # 0m:0.004s
                            copy_file_to_dir_706_4136()
                        with ChmodAndChown(path=r"IO_13.4_BurlAudio_Bmb4.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4137) as chmod_and_chown_707_4137:  # 0m:0.001s
                            chmod_and_chown_707_4137()
            with Stage(r"copy", r"Cadac_Firmware_13_4 v13.4.0.205", prog_num=4138):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4139) as should_copy_source_708_4139:  # ?
                    should_copy_source_708_4139()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", prog_num=4140):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r".", prog_num=4141) as copy_file_to_dir_709_4141:  # ?
                            copy_file_to_dir_709_4141()
                        with ChmodAndChown(path=r"IO_13.4_Cadac.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4142) as chmod_and_chown_710_4142:  # 0m:0.000s
                            chmod_and_chown_710_4142()
            with Stage(r"copy", r"Calrec_Firmware_13_4 v13.4.0.205", prog_num=4143):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4144) as should_copy_source_711_4144:  # ?
                    should_copy_source_711_4144()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", prog_num=4145):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r".", prog_num=4146) as copy_file_to_dir_712_4146:  # ?
                            copy_file_to_dir_712_4146()
                        with ChmodAndChown(path=r"IO_13.4_Calrec.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4147) as chmod_and_chown_713_4147:  # 0m:0.000s
                            chmod_and_chown_713_4147()
            with Stage(r"copy", r"Crest Audio Tactus Firmware v13.4.0.205", prog_num=4148):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4149) as should_copy_source_714_4149:  # ?
                    should_copy_source_714_4149()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", prog_num=4150):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r".", prog_num=4151) as copy_file_to_dir_715_4151:  # ?
                            copy_file_to_dir_715_4151()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4152) as chmod_and_chown_716_4152:  # 0m:0.000s
                            chmod_and_chown_716_4152()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4153) as should_copy_source_717_4153:  # ?
                    should_copy_source_717_4153()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", prog_num=4154):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r".", prog_num=4155) as copy_file_to_dir_718_4155:  # ?
                            copy_file_to_dir_718_4155()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4156) as chmod_and_chown_719_4156:  # 0m:0.000s
                            chmod_and_chown_719_4156()
            with Stage(r"copy", r"Crest Audio Tactus micro Firmware v13.4.0.205", prog_num=4157):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4158) as should_copy_source_720_4158:  # ?
                    should_copy_source_720_4158()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", prog_num=4159):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r".", prog_num=4160) as copy_file_to_dir_721_4160:  # ?
                            copy_file_to_dir_721_4160()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4161) as chmod_and_chown_722_4161:  # 0m:0.000s
                            chmod_and_chown_722_4161()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4162) as should_copy_source_723_4162:  # ?
                    should_copy_source_723_4162()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", prog_num=4163):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r".", prog_num=4164) as copy_file_to_dir_724_4164:  # ?
                            copy_file_to_dir_724_4164()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4165) as chmod_and_chown_725_4165:  # 0m:0.000s
                            chmod_and_chown_725_4165()
            with Stage(r"copy", r"DigiGrid DLI Firmware v13.4.0.205", prog_num=4166):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4167) as should_copy_source_726_4167:  # ?
                    should_copy_source_726_4167()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", prog_num=4168):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r".", prog_num=4169) as copy_file_to_dir_727_4169:  # ?
                            copy_file_to_dir_727_4169()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4170) as chmod_and_chown_728_4170:  # 0m:0.000s
                            chmod_and_chown_728_4170()
            with Stage(r"copy", r"DigiGrid DLS Firmware v13.4.0.205", prog_num=4171):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4172) as should_copy_source_729_4172:  # ?
                    should_copy_source_729_4172()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", prog_num=4173):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r".", prog_num=4174) as copy_file_to_dir_730_4174:  # ?
                            copy_file_to_dir_730_4174()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4175) as chmod_and_chown_731_4175:  # 0m:0.000s
                            chmod_and_chown_731_4175()
            with Stage(r"copy", r"DMI_Waves_Firmware_13_7 v13.7.113.401", prog_num=4176):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4177) as should_copy_source_732_4177:  # ?
                    should_copy_source_732_4177()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", prog_num=4178):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r".", prog_num=4179) as copy_file_to_dir_733_4179:  # ?
                            copy_file_to_dir_733_4179()
                        with ChmodAndChown(path=r"IO_13.7_DigicoDMI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4180) as chmod_and_chown_734_4180:  # 0m:0.000s
                            chmod_and_chown_734_4180()
            with Stage(r"copy", r"DN32_WSG_Firmware_13_4 v13.4.0.205", prog_num=4181):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4182) as should_copy_source_735_4182:  # ?
                    should_copy_source_735_4182()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", prog_num=4183):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r".", prog_num=4184) as copy_file_to_dir_736_4184:  # ?
                            copy_file_to_dir_736_4184()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG_DN32.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4185) as chmod_and_chown_737_4185:  # 0m:0.000s
                            chmod_and_chown_737_4185()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_13_6 v13.6.12.288", prog_num=4186):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4187) as should_copy_source_738_4187:  # ?
                    should_copy_source_738_4187()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", prog_num=4188):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r".", prog_num=4189) as copy_file_to_dir_739_4189:  # ?
                            copy_file_to_dir_739_4189()
                        with ChmodAndChown(path=r"IO_13.6_Dspro_sg1k.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4190) as chmod_and_chown_740_4190:  # 0m:0.000s
                            chmod_and_chown_740_4190()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_14_25 v14.25.55.616", prog_num=4191):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4192) as should_copy_source_741_4192:  # ?
                    should_copy_source_741_4192()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", prog_num=4193):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r".", prog_num=4194) as copy_file_to_dir_742_4194:  # ?
                            copy_file_to_dir_742_4194()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg1k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4195) as chmod_and_chown_743_4195:  # 0m:0.000s
                            chmod_and_chown_743_4195()
            with Stage(r"copy", r"DSPro_SG1000_micro_Firmware_15_1 v15.1.2.45", prog_num=4196):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4197) as should_copy_source_744_4197:  # ?
                    should_copy_source_744_4197()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", prog_num=4198):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r".", prog_num=4199) as copy_file_to_dir_745_4199:  # ?
                            copy_file_to_dir_745_4199()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4200) as chmod_and_chown_746_4200:  # 0m:0.000s
                            chmod_and_chown_746_4200()
            with Stage(r"copy", r"DSPro_SG1000_micro_V2_Firmware_15_1 v15.1.2.45", prog_num=4201):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4202) as should_copy_source_747_4202:  # ?
                    should_copy_source_747_4202()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", prog_num=4203):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r".", prog_num=4204) as copy_file_to_dir_748_4204:  # ?
                            copy_file_to_dir_748_4204()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4205) as chmod_and_chown_749_4205:  # 0m:0.000s
                            chmod_and_chown_749_4205()
            with Stage(r"copy", r"DSPro SG4000 Firmware v13.5.0.227", prog_num=4206):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4207) as should_copy_source_750_4207:  # ?
                    should_copy_source_750_4207()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", prog_num=4208):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r".", prog_num=4209) as copy_file_to_dir_751_4209:  # ?
                            copy_file_to_dir_751_4209()
                        with ChmodAndChown(path=r"IO_13.5_Dspro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4210) as chmod_and_chown_752_4210:  # 0m:0.000s
                            chmod_and_chown_752_4210()
            with Stage(r"copy", r"DSPro SG4000 v2 Firmware v14.26.30.647", prog_num=4211):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4212) as should_copy_source_753_4212:  # ?
                    should_copy_source_753_4212()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", prog_num=4213):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r".", prog_num=4214) as copy_file_to_dir_754_4214:  # ?
                            copy_file_to_dir_754_4214()
                        with ChmodAndChown(path=r"IO_14.26_Dspro_sg4k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4215) as chmod_and_chown_755_4215:  # 0m:0.000s
                            chmod_and_chown_755_4215()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware V14.25 v14.25.55.616", prog_num=4216):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4217) as should_copy_source_756_4217:  # ?
                    should_copy_source_756_4217()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", prog_num=4218):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r".", prog_num=4219) as copy_file_to_dir_757_4219:  # ?
                            copy_file_to_dir_757_4219()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4220) as chmod_and_chown_758_4220:  # 0m:0.000s
                            chmod_and_chown_758_4220()
            with Stage(r"copy", r"DSPro SG4000 micro Firmware v15.2.25.98", prog_num=4221):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4222) as should_copy_source_759_4222:  # ?
                    should_copy_source_759_4222()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", prog_num=4223):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r".", prog_num=4224) as copy_file_to_dir_760_4224:  # ?
                            copy_file_to_dir_760_4224()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4225) as chmod_and_chown_761_4225:  # 0m:0.000s
                            chmod_and_chown_761_4225()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware v15.2.25.98", prog_num=4226):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4227) as should_copy_source_762_4227:  # ?
                    should_copy_source_762_4227()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", prog_num=4228):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r".", prog_num=4229) as copy_file_to_dir_763_4229:  # ?
                            copy_file_to_dir_763_4229()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4230) as chmod_and_chown_764_4230:  # 0m:0.000s
                            chmod_and_chown_764_4230()
            with Stage(r"copy", r"DiGiGrid D Firmware V13.4 v13.4.0.205", prog_num=4231):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4232) as should_copy_source_765_4232:  # ?
                    should_copy_source_765_4232()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", prog_num=4233):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r".", prog_num=4234) as copy_file_to_dir_766_4234:  # ?
                            copy_file_to_dir_766_4234()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridD.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4235) as chmod_and_chown_767_4235:  # 0m:0.000s
                            chmod_and_chown_767_4235()
            with Stage(r"copy", r"DiGiGrid_M_Driver_Firmware_13_4 v13.4.0.205", prog_num=4236):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4237) as should_copy_source_768_4237:  # ?
                    should_copy_source_768_4237()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", prog_num=4238):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r".", prog_num=4239) as copy_file_to_dir_769_4239:  # ?
                            copy_file_to_dir_769_4239()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridM.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4240) as chmod_and_chown_770_4240:  # 0m:0.000s
                            chmod_and_chown_770_4240()
            with Stage(r"copy", r"DiGiGrid Q Firmware V13.4 v13.4.0.205", prog_num=4241):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4242) as should_copy_source_771_4242:  # ?
                    should_copy_source_771_4242()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", prog_num=4243):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r".", prog_num=4244) as copy_file_to_dir_772_4244:  # ?
                            copy_file_to_dir_772_4244()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridQ.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4245) as chmod_and_chown_773_4245:  # 0m:0.000s
                            chmod_and_chown_773_4245()
            with Stage(r"copy", r"Digico SD card V13.4 v13.4.0.205", prog_num=4246):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4247) as should_copy_source_774_4247:  # ?
                    should_copy_source_774_4247()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", prog_num=4248):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r".", prog_num=4249) as copy_file_to_dir_775_4249:  # ?
                            copy_file_to_dir_775_4249()
                        with ChmodAndChown(path=r"IO_13.4_DigiCo_t2_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4250) as chmod_and_chown_776_4250:  # 0m:0.000s
                            chmod_and_chown_776_4250()
            with Stage(r"copy", r"Digico SD Firmware v14.21.36.492", prog_num=4251):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4252) as should_copy_source_777_4252:  # ?
                    should_copy_source_777_4252()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", prog_num=4253):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r".", prog_num=4254) as copy_file_to_dir_778_4254:  # ?
                            copy_file_to_dir_778_4254()
                        with ChmodAndChown(path=r"IO_14.21_Digico_SD_S6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4255) as chmod_and_chown_779_4255:  # 0m:0.000s
                            chmod_and_chown_779_4255()
            with Stage(r"copy", r"DirectOut Exbox Micro SoundGrid I/O Driver Firmware v14.22.9.506", prog_num=4256):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4257) as should_copy_source_780_4257:  # ?
                    should_copy_source_780_4257()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", prog_num=4258):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r".", prog_num=4259) as copy_file_to_dir_781_4259:  # ?
                            copy_file_to_dir_781_4259()
                        with ChmodAndChown(path=r"IO_14.22_DirectOut_Ex_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4260) as chmod_and_chown_782_4260:  # 0m:0.000s
                            chmod_and_chown_782_4260()
            with Stage(r"copy", r"DirectOut Exbox v2 SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=4261):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4262) as should_copy_source_783_4262:  # ?
                    should_copy_source_783_4262()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", prog_num=4263):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r".", prog_num=4264) as copy_file_to_dir_784_4264:  # ?
                            copy_file_to_dir_784_4264()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4265) as chmod_and_chown_785_4265:  # 0m:0.000s
                            chmod_and_chown_785_4265()
            with Stage(r"copy", r"DirectOut Exbox v2 Micro SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=4266):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4267) as should_copy_source_786_4267:  # ?
                    should_copy_source_786_4267()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", prog_num=4268):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r".", prog_num=4269) as copy_file_to_dir_787_4269:  # ?
                            copy_file_to_dir_787_4269()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4270) as chmod_and_chown_788_4270:  # 0m:0.004s
                            chmod_and_chown_788_4270()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=4271):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4272) as should_copy_source_789_4272:  # ?
                    should_copy_source_789_4272()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", prog_num=4273):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r".", prog_num=4274) as copy_file_to_dir_790_4274:  # ?
                            copy_file_to_dir_790_4274()
                        with ChmodAndChown(path=r"IO_14.18_DirectOut_Ex.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4275) as chmod_and_chown_791_4275:  # 0m:0.000s
                            chmod_and_chown_791_4275()
            with Stage(r"copy", r"DirectOut_SG_MADI_Firmware_13_4 v13.4.0.205", prog_num=4276):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4277) as should_copy_source_792_4277:  # ?
                    should_copy_source_792_4277()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", prog_num=4278):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r".", prog_num=4279) as copy_file_to_dir_793_4279:  # ?
                            copy_file_to_dir_793_4279()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4280) as chmod_and_chown_794_4280:  # 0m:0.000s
                            chmod_and_chown_794_4280()
            with Stage(r"copy", r"DirectOut_SG_MADI_micro_Firmware_13_4 v13.4.0.205", prog_num=4281):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4282) as should_copy_source_795_4282:  # ?
                    should_copy_source_795_4282()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", prog_num=4283):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r".", prog_num=4284) as copy_file_to_dir_796_4284:  # ?
                            copy_file_to_dir_796_4284()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4285) as chmod_and_chown_797_4285:  # 0m:0.000s
                            chmod_and_chown_797_4285()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=4286):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4287) as should_copy_source_798_4287:  # ?
                    should_copy_source_798_4287()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", prog_num=4288):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r".", prog_num=4289) as copy_file_to_dir_799_4289:  # ?
                            copy_file_to_dir_799_4289()
                        with ChmodAndChown(path=r"IO_14.18_Directout_sgio.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4290) as chmod_and_chown_800_4290:  # 0m:0.000s
                            chmod_and_chown_800_4290()
            with Stage(r"copy", r"HearBack Pro Firmware v13.7.33.321", prog_num=4291):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4292) as should_copy_source_801_4292:  # ?
                    should_copy_source_801_4292()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", prog_num=4293):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r".", prog_num=4294) as copy_file_to_dir_802_4294:  # ?
                            copy_file_to_dir_802_4294()
                        with ChmodAndChown(path=r"IO_13.7_Heartech.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4295) as chmod_and_chown_803_4295:  # 0m:0.000s
                            chmod_and_chown_803_4295()
            with Stage(r"copy", r"HearBack Pro V2 Firmware v13.7.118.406", prog_num=4296):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4297) as should_copy_source_804_4297:  # ?
                    should_copy_source_804_4297()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", prog_num=4298):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r".", prog_num=4299) as copy_file_to_dir_805_4299:  # ?
                            copy_file_to_dir_805_4299()
                        with ChmodAndChown(path=r"IO_13.7_Heartech_32ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4300) as chmod_and_chown_806_4300:  # 0m:0.000s
                            chmod_and_chown_806_4300()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v15.1.29.72", prog_num=4301):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4302) as should_copy_source_807_4302:  # ?
                    should_copy_source_807_4302()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", prog_num=4303):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r".", prog_num=4304) as copy_file_to_dir_808_4304:  # ?
                            copy_file_to_dir_808_4304()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4305) as chmod_and_chown_809_4305:  # 0m:0.000s
                            chmod_and_chown_809_4305()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v2 v15.1.29.72", prog_num=4306):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4307) as should_copy_source_810_4307:  # ?
                    should_copy_source_810_4307()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", prog_num=4308):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r".", prog_num=4309) as copy_file_to_dir_811_4309:  # ?
                            copy_file_to_dir_811_4309()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4310) as chmod_and_chown_812_4310:  # 0m:0.000s
                            chmod_and_chown_812_4310()
            with Stage(r"copy", r"DigiGrid IOC Firmware v13.4.0.205", prog_num=4311):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4312) as should_copy_source_813_4312:  # ?
                    should_copy_source_813_4312()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", prog_num=4313):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r".", prog_num=4314) as copy_file_to_dir_814_4314:  # ?
                            copy_file_to_dir_814_4314()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4315) as chmod_and_chown_815_4315:  # 0m:0.000s
                            chmod_and_chown_815_4315()
            with Stage(r"copy", r"DigiGrid IOC micro Firmware v13.4.0.205", prog_num=4316):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4317) as should_copy_source_816_4317:  # ?
                    should_copy_source_816_4317()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", prog_num=4318):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r".", prog_num=4319) as copy_file_to_dir_817_4319:  # ?
                            copy_file_to_dir_817_4319()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4320) as chmod_and_chown_818_4320:  # 0m:0.000s
                            chmod_and_chown_818_4320()
            with Stage(r"copy", r"IONIC16_Firmware_S25 v14.29.19.700", prog_num=4321):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4322) as should_copy_source_819_4322:  # ?
                    should_copy_source_819_4322()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", prog_num=4323):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r".", prog_num=4324) as copy_file_to_dir_820_4324:  # ?
                            copy_file_to_dir_820_4324()
                        with ChmodAndChown(path=r"IO_14.29_IONIC16_S25.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4325) as chmod_and_chown_821_4325:  # 0m:0.000s
                            chmod_and_chown_821_4325()
            with Stage(r"copy", r"IONIC16_Firmware_S50 v14.30.5.713", prog_num=4326):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4327) as should_copy_source_822_4327:  # ?
                    should_copy_source_822_4327()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", prog_num=4328):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r".", prog_num=4329) as copy_file_to_dir_823_4329:  # ?
                            copy_file_to_dir_823_4329()
                        with ChmodAndChown(path=r"IO_14.30_IONIC16_S50.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4330) as chmod_and_chown_824_4330:  # 0m:0.000s
                            chmod_and_chown_824_4330()
            with Stage(r"copy", r"DigiGrid IOS Firmware v13.4.0.205", prog_num=4331):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4332) as should_copy_source_825_4332:  # ?
                    should_copy_source_825_4332()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", prog_num=4333):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r".", prog_num=4334) as copy_file_to_dir_826_4334:  # ?
                            copy_file_to_dir_826_4334()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4335) as chmod_and_chown_827_4335:  # 0m:0.000s
                            chmod_and_chown_827_4335()
            with Stage(r"copy", r"DigiGrid IOS-XL Firmware v13.4.0.205", prog_num=4336):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4337) as should_copy_source_828_4337:  # ?
                    should_copy_source_828_4337()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", prog_num=4338):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r".", prog_num=4339) as copy_file_to_dir_829_4339:  # ?
                            copy_file_to_dir_829_4339()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4340) as chmod_and_chown_830_4340:  # 0m:0.000s
                            chmod_and_chown_830_4340()
            with Stage(r"copy", r"DigiGrid IOS-XL micro Firmware v13.4.0.205", prog_num=4341):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4342) as should_copy_source_831_4342:  # ?
                    should_copy_source_831_4342()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", prog_num=4343):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r".", prog_num=4344) as copy_file_to_dir_832_4344:  # ?
                            copy_file_to_dir_832_4344()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4345) as chmod_and_chown_833_4345:  # 0m:0.000s
                            chmod_and_chown_833_4345()
            with Stage(r"copy", r"DigiGrid IOS micro Firmware v13.4.0.205", prog_num=4346):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4347) as should_copy_source_834_4347:  # ?
                    should_copy_source_834_4347()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", prog_num=4348):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r".", prog_num=4349) as copy_file_to_dir_835_4349:  # ?
                            copy_file_to_dir_835_4349()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4350) as chmod_and_chown_836_4350:  # 0m:0.000s
                            chmod_and_chown_836_4350()
            with Stage(r"copy", r"DigiGrid IOX Firmware v13.4.0.205", prog_num=4351):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4352) as should_copy_source_837_4352:  # ?
                    should_copy_source_837_4352()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", prog_num=4353):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r".", prog_num=4354) as copy_file_to_dir_838_4354:  # ?
                            copy_file_to_dir_838_4354()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4355) as chmod_and_chown_839_4355:  # 0m:0.000s
                            chmod_and_chown_839_4355()
            with Stage(r"copy", r"DigiGrid IOX micro Firmware v13.4.0.205", prog_num=4356):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4357) as should_copy_source_840_4357:  # ?
                    should_copy_source_840_4357()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", prog_num=4358):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r".", prog_num=4359) as copy_file_to_dir_841_4359:  # ?
                            copy_file_to_dir_841_4359()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4360) as chmod_and_chown_842_4360:  # 0m:0.000s
                            chmod_and_chown_842_4360()
            with Stage(r"copy", r"JoeCo_Firmware_13_4 v13.4.0.205", prog_num=4361):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4362) as should_copy_source_843_4362:  # ?
                    should_copy_source_843_4362()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", prog_num=4363):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r".", prog_num=4364) as copy_file_to_dir_844_4364:  # ?
                            copy_file_to_dir_844_4364()
                        with ChmodAndChown(path=r"IO_13.4_Joeco.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4365) as chmod_and_chown_845_4365:  # 0m:0.000s
                            chmod_and_chown_845_4365()
            with Stage(r"copy", r"DigiGrid MGB Firmware v13.4.0.205", prog_num=4366):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4367) as should_copy_source_846_4367:  # ?
                    should_copy_source_846_4367()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", prog_num=4368):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r".", prog_num=4369) as copy_file_to_dir_847_4369:  # ?
                            copy_file_to_dir_847_4369()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4370) as chmod_and_chown_848_4370:  # 0m:0.000s
                            chmod_and_chown_848_4370()
            with Stage(r"copy", r"DigiGrid MGO Firmware v13.4.0.205", prog_num=4371):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4372) as should_copy_source_849_4372:  # ?
                    should_copy_source_849_4372()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", prog_num=4373):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r".", prog_num=4374) as copy_file_to_dir_850_4374:  # ?
                            copy_file_to_dir_850_4374()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGO.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4375) as chmod_and_chown_851_4375:  # 0m:0.000s
                            chmod_and_chown_851_4375()
            with Stage(r"copy", r"SoundStudio STG-1608 Firmware v13.4.0.205", prog_num=4376):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4377) as should_copy_source_852_4377:  # ?
                    should_copy_source_852_4377()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", prog_num=4378):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r".", prog_num=4379) as copy_file_to_dir_853_4379:  # ?
                            copy_file_to_dir_853_4379()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4380) as chmod_and_chown_854_4380:  # 0m:0.000s
                            chmod_and_chown_854_4380()
            with Stage(r"copy", r"SoundStudio STG-1608 micro Firmware V13.4 v13.4.0.205", prog_num=4381):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4382) as should_copy_source_855_4382:  # ?
                    should_copy_source_855_4382()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", prog_num=4383):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r".", prog_num=4384) as copy_file_to_dir_856_4384:  # ?
                            copy_file_to_dir_856_4384()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4385) as chmod_and_chown_857_4385:  # 0m:0.000s
                            chmod_and_chown_857_4385()
            with Stage(r"copy", r"SoundStudio STG-2412 Firmware v13.4.0.205", prog_num=4386):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4387) as should_copy_source_858_4387:  # ?
                    should_copy_source_858_4387()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", prog_num=4388):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r".", prog_num=4389) as copy_file_to_dir_859_4389:  # ?
                            copy_file_to_dir_859_4389()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4390) as chmod_and_chown_860_4390:  # 0m:0.006s
                            chmod_and_chown_860_4390()
            with Stage(r"copy", r"SoundStudio STG-2412 micro Firmware V13.4 v13.4.0.205", prog_num=4391):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4392) as should_copy_source_861_4392:  # ?
                    should_copy_source_861_4392()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", prog_num=4393):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r".", prog_num=4394) as copy_file_to_dir_862_4394:  # ?
                            copy_file_to_dir_862_4394()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4395) as chmod_and_chown_863_4395:  # 0m:0.000s
                            chmod_and_chown_863_4395()
            with Stage(r"copy", r"X-WSG_s6_Firmware_13_4 v13.4.0.205", prog_num=4396):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4397) as should_copy_source_864_4397:  # ?
                    should_copy_source_864_4397()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", prog_num=4398):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r".", prog_num=4399) as copy_file_to_dir_865_4399:  # ?
                            copy_file_to_dir_865_4399()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4400) as chmod_and_chown_866_4400:  # 0m:0.000s
                            chmod_and_chown_866_4400()
            with Stage(r"copy", r"WSG Y-16 s3 Firmware v13.4.0.205", prog_num=4401):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4402) as should_copy_source_867_4402:  # ?
                    should_copy_source_867_4402()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", prog_num=4403):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r".", prog_num=4404) as copy_file_to_dir_868_4404:  # ?
                            copy_file_to_dir_868_4404()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4405) as chmod_and_chown_869_4405:  # 0m:0.000s
                            chmod_and_chown_869_4405()
            with Stage(r"copy", r"WSG Y-16 s6 Firmware v13.4.0.205", prog_num=4406):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4407) as should_copy_source_870_4407:  # ?
                    should_copy_source_870_4407()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", prog_num=4408):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r".", prog_num=4409) as copy_file_to_dir_871_4409:  # ?
                            copy_file_to_dir_871_4409()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4410) as chmod_and_chown_872_4410:  # 0m:0.000s
                            chmod_and_chown_872_4410()
            with Stage(r"copy", r"WSG Y-16 v3 Firmware v14.21.16.472", prog_num=4411):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4412) as should_copy_source_873_4412:  # ?
                    should_copy_source_873_4412()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", prog_num=4413):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r".", prog_num=4414) as copy_file_to_dir_874_4414:  # ?
                            copy_file_to_dir_874_4414()
                        with ChmodAndChown(path=r"IO_14.21_MY16_v3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4415) as chmod_and_chown_875_4415:  # 0m:0.000s
                            chmod_and_chown_875_4415()
            with Stage(r"copy", r"Yamaha HY128 v2 Firmware v14.13.43.386", prog_num=4416):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4417) as should_copy_source_876_4417:  # ?
                    should_copy_source_876_4417()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", prog_num=4418):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r".", prog_num=4419) as copy_file_to_dir_877_4419:  # ?
                            copy_file_to_dir_877_4419()
                        with ChmodAndChown(path=r"IO_14.13_HY_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4420) as chmod_and_chown_878_4420:  # 0m:0.000s
                            chmod_and_chown_878_4420()
            with Stage(r"copy", r"Yamaha WSG-HY128 Firmware v13.4.0.205", prog_num=4421):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4422) as should_copy_source_879_4422:  # ?
                    should_copy_source_879_4422()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", prog_num=4423):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r".", prog_num=4424) as copy_file_to_dir_880_4424:  # ?
                            copy_file_to_dir_880_4424()
                        with ChmodAndChown(path=r"IO_13.4_Hy.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4425) as chmod_and_chown_881_4425:  # 0m:0.000s
                            chmod_and_chown_881_4425()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4426):  # 0m:0.001s
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4427) as cd_882_4427:  # 0m:0.001s
                cd_882_4427()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4428)()  # 0m:0.000s
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_9.7.wfi", prog_num=4429) as rm_file_883_4429:  # 0m:0.000s
                    rm_file_883_4429()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.0.wfi", prog_num=4430) as rm_file_884_4430:  # 0m:0.000s
                    rm_file_884_4430()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.2.wfi", prog_num=4431) as rm_file_885_4431:  # 0m:0.000s
                    rm_file_885_4431()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.3.wfi", prog_num=4432) as rm_file_886_4432:  # 0m:0.000s
                    rm_file_886_4432()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.1.wfi", prog_num=4433) as rm_file_887_4433:  # 0m:0.000s
                    rm_file_887_4433()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.2.wfi", prog_num=4434) as rm_file_888_4434:  # 0m:0.000s
                    rm_file_888_4434()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.2.wfi", prog_num=4435) as rm_file_889_4435:  # 0m:0.000s
                    rm_file_889_4435()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.8.wfi", prog_num=4436) as rm_file_890_4436:  # 0m:0.000s
                    rm_file_890_4436()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_13.3.wfi", prog_num=4437) as rm_file_891_4437:  # 0m:0.000s
                    rm_file_891_4437()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.6.wfi", prog_num=4438) as rm_file_892_4438:  # 0m:0.000s
                    rm_file_892_4438()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.9.wfi", prog_num=4439) as rm_file_893_4439:  # 0m:0.000s
                    rm_file_893_4439()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4440) as cd_stage_894_4440:  # 0m:0.019s
            cd_stage_894_4440()
            with Stage(r"copy", r"SoundGrid Server Firmware v14.26.104.721", prog_num=4441):  # 0m:0.019s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", skip_progress_count=2, prog_num=4442) as should_copy_source_895_4442:  # 0m:0.019s
                    should_copy_source_895_4442()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", prog_num=4443):  # 0m:0.019s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4444) as unwtar_896_4444:  # 0m:0.019s
                            unwtar_896_4444()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4445):  # 0m:0.028s
            with Cd(r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4446) as cd_897_4446:  # 0m:0.028s
                cd_897_4446()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4447)()  # 0m:0.000s
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=4448) as rm_dir_898_4448:  # 0m:0.000s
                    rm_dir_898_4448()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=4449) as rm_dir_899_4449:  # 0m:0.000s
                    rm_dir_899_4449()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=4450) as rm_dir_900_4450:  # 0m:0.000s
                    rm_dir_900_4450()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=4451) as rm_dir_901_4451:  # 0m:0.000s
                    rm_dir_901_4451()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.app", prog_num=4452) as rm_dir_902_4452:  # 0m:0.000s
                    rm_dir_902_4452()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.bundle", prog_num=4453) as rm_dir_903_4453:  # 0m:0.000s
                    rm_dir_903_4453()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.app", prog_num=4454) as rm_dir_904_4454:  # 0m:0.000s
                    rm_dir_904_4454()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.bundle", prog_num=4455) as rm_dir_905_4455:  # 0m:0.000s
                    rm_dir_905_4455()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.app", prog_num=4456) as rm_dir_906_4456:  # 0m:0.000s
                    rm_dir_906_4456()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.bundle", prog_num=4457) as rm_dir_907_4457:  # 0m:0.000s
                    rm_dir_907_4457()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.app", prog_num=4458) as rm_dir_908_4458:  # 0m:0.000s
                    rm_dir_908_4458()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.bundle", prog_num=4459) as rm_dir_909_4459:  # 0m:0.000s
                    rm_dir_909_4459()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.app", prog_num=4460) as rm_dir_910_4460:  # 0m:0.000s
                    rm_dir_910_4460()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.bundle", prog_num=4461) as rm_dir_911_4461:  # 0m:0.000s
                    rm_dir_911_4461()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.app", prog_num=4462) as rm_dir_912_4462:  # 0m:0.000s
                    rm_dir_912_4462()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.bundle", prog_num=4463) as rm_dir_913_4463:  # 0m:0.000s
                    rm_dir_913_4463()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.app", prog_num=4464) as rm_dir_914_4464:  # 0m:0.000s
                    rm_dir_914_4464()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.bundle", prog_num=4465) as rm_dir_915_4465:  # 0m:0.000s
                    rm_dir_915_4465()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.app", prog_num=4466) as rm_dir_916_4466:  # 0m:0.000s
                    rm_dir_916_4466()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.bundle", prog_num=4467) as rm_dir_917_4467:  # 0m:0.000s
                    rm_dir_917_4467()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.app", prog_num=4468) as rm_dir_918_4468:  # 0m:0.000s
                    rm_dir_918_4468()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.bundle", prog_num=4469) as rm_dir_919_4469:  # 0m:0.000s
                    rm_dir_919_4469()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.app", prog_num=4470) as rm_dir_920_4470:  # 0m:0.000s
                    rm_dir_920_4470()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.bundle", prog_num=4471) as rm_dir_921_4471:  # 0m:0.000s
                    rm_dir_921_4471()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.app", prog_num=4472) as rm_dir_922_4472:  # 0m:0.000s
                    rm_dir_922_4472()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.bundle", prog_num=4473) as rm_dir_923_4473:  # 0m:0.000s
                    rm_dir_923_4473()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.app", prog_num=4474) as rm_dir_924_4474:  # 0m:0.000s
                    rm_dir_924_4474()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.bundle", prog_num=4475) as rm_dir_925_4475:  # 0m:0.000s
                    rm_dir_925_4475()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 9.7.bundle", prog_num=4476) as rm_dir_926_4476:  # 0m:0.000s
                    rm_dir_926_4476()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 10.0.bundle", prog_num=4477) as rm_dir_927_4477:  # 0m:0.000s
                    rm_dir_927_4477()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 12.1.bundle", prog_num=4478) as rm_dir_928_4478:  # 0m:0.004s
                    rm_dir_928_4478()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 13.1.bundle", prog_num=4479) as rm_dir_929_4479:  # 0m:0.000s
                    rm_dir_929_4479()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 9.7.bundle", prog_num=4480) as rm_dir_930_4480:  # 0m:0.000s
                    rm_dir_930_4480()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 10.0.bundle", prog_num=4481) as rm_dir_931_4481:  # 0m:0.000s
                    rm_dir_931_4481()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 12.1.bundle", prog_num=4482) as rm_dir_932_4482:  # 0m:0.000s
                    rm_dir_932_4482()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 13.1.bundle", prog_num=4483) as rm_dir_933_4483:  # 0m:0.000s
                    rm_dir_933_4483()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.app", prog_num=4484) as rm_dir_934_4484:  # 0m:0.000s
                    rm_dir_934_4484()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.bundle", prog_num=4485) as rm_dir_935_4485:  # 0m:0.000s
                    rm_dir_935_4485()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.app", prog_num=4486) as rm_dir_936_4486:  # 0m:0.000s
                    rm_dir_936_4486()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.bundle", prog_num=4487) as rm_dir_937_4487:  # 0m:0.000s
                    rm_dir_937_4487()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.app", prog_num=4488) as rm_dir_938_4488:  # 0m:0.000s
                    rm_dir_938_4488()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.bundle", prog_num=4489) as rm_dir_939_4489:  # 0m:0.000s
                    rm_dir_939_4489()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=4490) as rm_dir_940_4490:  # 0m:0.000s
                    rm_dir_940_4490()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=4491) as rm_dir_941_4491:  # 0m:0.000s
                    rm_dir_941_4491()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.app", prog_num=4492) as rm_dir_942_4492:  # 0m:0.000s
                    rm_dir_942_4492()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.bundle", prog_num=4493) as rm_dir_943_4493:  # 0m:0.000s
                    rm_dir_943_4493()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.app", prog_num=4494) as rm_dir_944_4494:  # 0m:0.000s
                    rm_dir_944_4494()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.bundle", prog_num=4495) as rm_dir_945_4495:  # 0m:0.000s
                    rm_dir_945_4495()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.app", prog_num=4496) as rm_dir_946_4496:  # 0m:0.000s
                    rm_dir_946_4496()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.bundle", prog_num=4497) as rm_dir_947_4497:  # 0m:0.000s
                    rm_dir_947_4497()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.app", prog_num=4498) as rm_dir_948_4498:  # 0m:0.000s
                    rm_dir_948_4498()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.bundle", prog_num=4499) as rm_dir_949_4499:  # 0m:0.000s
                    rm_dir_949_4499()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.app", prog_num=4500) as rm_dir_950_4500:  # 0m:0.000s
                    rm_dir_950_4500()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.bundle", prog_num=4501) as rm_dir_951_4501:  # 0m:0.000s
                    rm_dir_951_4501()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.app", prog_num=4502) as rm_dir_952_4502:  # 0m:0.000s
                    rm_dir_952_4502()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.bundle", prog_num=4503) as rm_dir_953_4503:  # 0m:0.000s
                    rm_dir_953_4503()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.app", prog_num=4504) as rm_dir_954_4504:  # 0m:0.000s
                    rm_dir_954_4504()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.bundle", prog_num=4505) as rm_dir_955_4505:  # 0m:0.000s
                    rm_dir_955_4505()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.app", prog_num=4506) as rm_dir_956_4506:  # 0m:0.000s
                    rm_dir_956_4506()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.bundle", prog_num=4507) as rm_dir_957_4507:  # 0m:0.000s
                    rm_dir_957_4507()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.app", prog_num=4508) as rm_dir_958_4508:  # 0m:0.000s
                    rm_dir_958_4508()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.bundle", prog_num=4509) as rm_dir_959_4509:  # 0m:0.000s
                    rm_dir_959_4509()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.app", prog_num=4510) as rm_dir_960_4510:  # 0m:0.000s
                    rm_dir_960_4510()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.bundle", prog_num=4511) as rm_dir_961_4511:  # 0m:0.000s
                    rm_dir_961_4511()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.app", prog_num=4512) as rm_dir_962_4512:  # 0m:0.000s
                    rm_dir_962_4512()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.bundle", prog_num=4513) as rm_dir_963_4513:  # 0m:0.000s
                    rm_dir_963_4513()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.app", prog_num=4514) as rm_dir_964_4514:  # 0m:0.000s
                    rm_dir_964_4514()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.bundle", prog_num=4515) as rm_dir_965_4515:  # 0m:0.000s
                    rm_dir_965_4515()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.app", prog_num=4516) as rm_dir_966_4516:  # 0m:0.000s
                    rm_dir_966_4516()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.bundle", prog_num=4517) as rm_dir_967_4517:  # 0m:0.000s
                    rm_dir_967_4517()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.app", prog_num=4518) as rm_dir_968_4518:  # 0m:0.000s
                    rm_dir_968_4518()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.bundle", prog_num=4519) as rm_dir_969_4519:  # 0m:0.000s
                    rm_dir_969_4519()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.app", prog_num=4520) as rm_dir_970_4520:  # 0m:0.000s
                    rm_dir_970_4520()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.bundle", prog_num=4521) as rm_dir_971_4521:  # 0m:0.000s
                    rm_dir_971_4521()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.app", prog_num=4522) as rm_dir_972_4522:  # 0m:0.000s
                    rm_dir_972_4522()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.bundle", prog_num=4523) as rm_dir_973_4523:  # 0m:0.000s
                    rm_dir_973_4523()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.app", prog_num=4524) as rm_dir_974_4524:  # 0m:0.000s
                    rm_dir_974_4524()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.bundle", prog_num=4525) as rm_dir_975_4525:  # 0m:0.000s
                    rm_dir_975_4525()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.app", prog_num=4526) as rm_dir_976_4526:  # 0m:0.000s
                    rm_dir_976_4526()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.bundle", prog_num=4527) as rm_dir_977_4527:  # 0m:0.000s
                    rm_dir_977_4527()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.app", prog_num=4528) as rm_dir_978_4528:  # 0m:0.000s
                    rm_dir_978_4528()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.bundle", prog_num=4529) as rm_dir_979_4529:  # 0m:0.000s
                    rm_dir_979_4529()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.app", prog_num=4530) as rm_dir_980_4530:  # 0m:0.000s
                    rm_dir_980_4530()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.bundle", prog_num=4531) as rm_dir_981_4531:  # 0m:0.000s
                    rm_dir_981_4531()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.app", prog_num=4532) as rm_dir_982_4532:  # 0m:0.000s
                    rm_dir_982_4532()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.bundle", prog_num=4533) as rm_dir_983_4533:  # 0m:0.000s
                    rm_dir_983_4533()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.app", prog_num=4534) as rm_dir_984_4534:  # 0m:0.000s
                    rm_dir_984_4534()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.bundle", prog_num=4535) as rm_dir_985_4535:  # 0m:0.000s
                    rm_dir_985_4535()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.app", prog_num=4536) as rm_dir_986_4536:  # 0m:0.000s
                    rm_dir_986_4536()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.bundle", prog_num=4537) as rm_dir_987_4537:  # 0m:0.000s
                    rm_dir_987_4537()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=4538) as rm_dir_988_4538:  # 0m:0.000s
                    rm_dir_988_4538()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=4539) as rm_dir_989_4539:  # 0m:0.000s
                    rm_dir_989_4539()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=4540) as rm_dir_990_4540:  # 0m:0.000s
                    rm_dir_990_4540()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=4541) as rm_dir_991_4541:  # 0m:0.000s
                    rm_dir_991_4541()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.exe", prog_num=4542) as rm_file_992_4542:  # 0m:0.000s
                    rm_file_992_4542()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.exe", prog_num=4543) as rm_file_993_4543:  # 0m:0.000s
                    rm_file_993_4543()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.app", prog_num=4544) as rm_dir_994_4544:  # 0m:0.000s
                    rm_dir_994_4544()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.bundle", prog_num=4545) as rm_dir_995_4545:  # 0m:0.000s
                    rm_dir_995_4545()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.app", prog_num=4546) as rm_dir_996_4546:  # 0m:0.000s
                    rm_dir_996_4546()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.bundle", prog_num=4547) as rm_dir_997_4547:  # 0m:0.000s
                    rm_dir_997_4547()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.app", prog_num=4548) as rm_dir_998_4548:  # 0m:0.000s
                    rm_dir_998_4548()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.bundle", prog_num=4549) as rm_dir_999_4549:  # 0m:0.000s
                    rm_dir_999_4549()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.app", prog_num=4550) as rm_dir_1000_4550:  # 0m:0.000s
                    rm_dir_1000_4550()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.bundle", prog_num=4551) as rm_dir_1001_4551:  # 0m:0.000s
                    rm_dir_1001_4551()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.app", prog_num=4552) as rm_dir_1002_4552:  # 0m:0.000s
                    rm_dir_1002_4552()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.bundle", prog_num=4553) as rm_dir_1003_4553:  # 0m:0.000s
                    rm_dir_1003_4553()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.app", prog_num=4554) as rm_dir_1004_4554:  # 0m:0.000s
                    rm_dir_1004_4554()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.bundle", prog_num=4555) as rm_dir_1005_4555:  # 0m:0.000s
                    rm_dir_1005_4555()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.app", prog_num=4556) as rm_dir_1006_4556:  # 0m:0.000s
                    rm_dir_1006_4556()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.bundle", prog_num=4557) as rm_dir_1007_4557:  # 0m:0.000s
                    rm_dir_1007_4557()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.app", prog_num=4558) as rm_dir_1008_4558:  # 0m:0.000s
                    rm_dir_1008_4558()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.bundle", prog_num=4559) as rm_dir_1009_4559:  # 0m:0.000s
                    rm_dir_1009_4559()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.app", prog_num=4560) as rm_dir_1010_4560:  # 0m:0.000s
                    rm_dir_1010_4560()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.bundle", prog_num=4561) as rm_dir_1011_4561:  # 0m:0.000s
                    rm_dir_1011_4561()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.app", prog_num=4562) as rm_dir_1012_4562:  # 0m:0.000s
                    rm_dir_1012_4562()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.bundle", prog_num=4563) as rm_dir_1013_4563:  # 0m:0.000s
                    rm_dir_1013_4563()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.app", prog_num=4564) as rm_dir_1014_4564:  # 0m:0.000s
                    rm_dir_1014_4564()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.bundle", prog_num=4565) as rm_dir_1015_4565:  # 0m:0.000s
                    rm_dir_1015_4565()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.app", prog_num=4566) as rm_dir_1016_4566:  # 0m:0.004s
                    rm_dir_1016_4566()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.bundle", prog_num=4567) as rm_dir_1017_4567:  # 0m:0.001s
                    rm_dir_1017_4567()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.app", prog_num=4568) as rm_dir_1018_4568:  # 0m:0.000s
                    rm_dir_1018_4568()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.bundle", prog_num=4569) as rm_dir_1019_4569:  # 0m:0.000s
                    rm_dir_1019_4569()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.app", prog_num=4570) as rm_dir_1020_4570:  # 0m:0.000s
                    rm_dir_1020_4570()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.bundle", prog_num=4571) as rm_dir_1021_4571:  # 0m:0.000s
                    rm_dir_1021_4571()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.app", prog_num=4572) as rm_dir_1022_4572:  # 0m:0.000s
                    rm_dir_1022_4572()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.bundle", prog_num=4573) as rm_dir_1023_4573:  # 0m:0.000s
                    rm_dir_1023_4573()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.app", prog_num=4574) as rm_dir_1024_4574:  # 0m:0.000s
                    rm_dir_1024_4574()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.bundle", prog_num=4575) as rm_dir_1025_4575:  # 0m:0.000s
                    rm_dir_1025_4575()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.app", prog_num=4576) as rm_dir_1026_4576:  # 0m:0.000s
                    rm_dir_1026_4576()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.bundle", prog_num=4577) as rm_dir_1027_4577:  # 0m:0.000s
                    rm_dir_1027_4577()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.app", prog_num=4578) as rm_dir_1028_4578:  # 0m:0.000s
                    rm_dir_1028_4578()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.bundle", prog_num=4579) as rm_dir_1029_4579:  # 0m:0.000s
                    rm_dir_1029_4579()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.app", prog_num=4580) as rm_dir_1030_4580:  # 0m:0.000s
                    rm_dir_1030_4580()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.bundle", prog_num=4581) as rm_dir_1031_4581:  # 0m:0.000s
                    rm_dir_1031_4581()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.app", prog_num=4582) as rm_dir_1032_4582:  # 0m:0.000s
                    rm_dir_1032_4582()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.bundle", prog_num=4583) as rm_dir_1033_4583:  # 0m:0.000s
                    rm_dir_1033_4583()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.app", prog_num=4584) as rm_dir_1034_4584:  # 0m:0.000s
                    rm_dir_1034_4584()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.bundle", prog_num=4585) as rm_dir_1035_4585:  # 0m:0.000s
                    rm_dir_1035_4585()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.app", prog_num=4586) as rm_dir_1036_4586:  # 0m:0.000s
                    rm_dir_1036_4586()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.bundle", prog_num=4587) as rm_dir_1037_4587:  # 0m:0.000s
                    rm_dir_1037_4587()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.app", prog_num=4588) as rm_dir_1038_4588:  # 0m:0.000s
                    rm_dir_1038_4588()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.bundle", prog_num=4589) as rm_dir_1039_4589:  # 0m:0.000s
                    rm_dir_1039_4589()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.app", prog_num=4590) as rm_dir_1040_4590:  # 0m:0.000s
                    rm_dir_1040_4590()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.bundle", prog_num=4591) as rm_dir_1041_4591:  # 0m:0.000s
                    rm_dir_1041_4591()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.app", prog_num=4592) as rm_dir_1042_4592:  # 0m:0.000s
                    rm_dir_1042_4592()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.bundle", prog_num=4593) as rm_dir_1043_4593:  # 0m:0.000s
                    rm_dir_1043_4593()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.app", prog_num=4594) as rm_dir_1044_4594:  # 0m:0.000s
                    rm_dir_1044_4594()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.bundle", prog_num=4595) as rm_dir_1045_4595:  # 0m:0.000s
                    rm_dir_1045_4595()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.app", prog_num=4596) as rm_dir_1046_4596:  # 0m:0.000s
                    rm_dir_1046_4596()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.bundle", prog_num=4597) as rm_dir_1047_4597:  # 0m:0.000s
                    rm_dir_1047_4597()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.app", prog_num=4598) as rm_dir_1048_4598:  # 0m:0.000s
                    rm_dir_1048_4598()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.bundle", prog_num=4599) as rm_dir_1049_4599:  # 0m:0.000s
                    rm_dir_1049_4599()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.app", prog_num=4600) as rm_dir_1050_4600:  # 0m:0.000s
                    rm_dir_1050_4600()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.bundle", prog_num=4601) as rm_dir_1051_4601:  # 0m:0.000s
                    rm_dir_1051_4601()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.app", prog_num=4602) as rm_dir_1052_4602:  # 0m:0.000s
                    rm_dir_1052_4602()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.bundle", prog_num=4603) as rm_dir_1053_4603:  # 0m:0.000s
                    rm_dir_1053_4603()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.app", prog_num=4604) as rm_dir_1054_4604:  # 0m:0.000s
                    rm_dir_1054_4604()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.bundle", prog_num=4605) as rm_dir_1055_4605:  # 0m:0.000s
                    rm_dir_1055_4605()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.app", prog_num=4606) as rm_dir_1056_4606:  # 0m:0.000s
                    rm_dir_1056_4606()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.bundle", prog_num=4607) as rm_dir_1057_4607:  # 0m:0.000s
                    rm_dir_1057_4607()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.app", prog_num=4608) as rm_dir_1058_4608:  # 0m:0.000s
                    rm_dir_1058_4608()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.bundle", prog_num=4609) as rm_dir_1059_4609:  # 0m:0.000s
                    rm_dir_1059_4609()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.app", prog_num=4610) as rm_dir_1060_4610:  # 0m:0.000s
                    rm_dir_1060_4610()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.bundle", prog_num=4611) as rm_dir_1061_4611:  # 0m:0.000s
                    rm_dir_1061_4611()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.app", prog_num=4612) as rm_dir_1062_4612:  # 0m:0.000s
                    rm_dir_1062_4612()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.bundle", prog_num=4613) as rm_dir_1063_4613:  # 0m:0.000s
                    rm_dir_1063_4613()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.app", prog_num=4614) as rm_dir_1064_4614:  # 0m:0.000s
                    rm_dir_1064_4614()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.bundle", prog_num=4615) as rm_dir_1065_4615:  # 0m:0.000s
                    rm_dir_1065_4615()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.app", prog_num=4616) as rm_dir_1066_4616:  # 0m:0.000s
                    rm_dir_1066_4616()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.bundle", prog_num=4617) as rm_dir_1067_4617:  # 0m:0.000s
                    rm_dir_1067_4617()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.app", prog_num=4618) as rm_dir_1068_4618:  # 0m:0.000s
                    rm_dir_1068_4618()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.bundle", prog_num=4619) as rm_dir_1069_4619:  # 0m:0.000s
                    rm_dir_1069_4619()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.app", prog_num=4620) as rm_dir_1070_4620:  # 0m:0.000s
                    rm_dir_1070_4620()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.bundle", prog_num=4621) as rm_dir_1071_4621:  # 0m:0.000s
                    rm_dir_1071_4621()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.app", prog_num=4622) as rm_dir_1072_4622:  # 0m:0.000s
                    rm_dir_1072_4622()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.bundle", prog_num=4623) as rm_dir_1073_4623:  # 0m:0.000s
                    rm_dir_1073_4623()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.app", prog_num=4624) as rm_dir_1074_4624:  # 0m:0.000s
                    rm_dir_1074_4624()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.bundle", prog_num=4625) as rm_dir_1075_4625:  # 0m:0.000s
                    rm_dir_1075_4625()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.app", prog_num=4626) as rm_dir_1076_4626:  # 0m:0.000s
                    rm_dir_1076_4626()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.bundle", prog_num=4627) as rm_dir_1077_4627:  # 0m:0.000s
                    rm_dir_1077_4627()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.app", prog_num=4628) as rm_dir_1078_4628:  # 0m:0.000s
                    rm_dir_1078_4628()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.bundle", prog_num=4629) as rm_dir_1079_4629:  # 0m:0.000s
                    rm_dir_1079_4629()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.app", prog_num=4630) as rm_dir_1080_4630:  # 0m:0.000s
                    rm_dir_1080_4630()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.bundle", prog_num=4631) as rm_dir_1081_4631:  # 0m:0.000s
                    rm_dir_1081_4631()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.app", prog_num=4632) as rm_dir_1082_4632:  # 0m:0.000s
                    rm_dir_1082_4632()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.bundle", prog_num=4633) as rm_dir_1083_4633:  # 0m:0.000s
                    rm_dir_1083_4633()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.app", prog_num=4634) as rm_dir_1084_4634:  # 0m:0.000s
                    rm_dir_1084_4634()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.bundle", prog_num=4635) as rm_dir_1085_4635:  # 0m:0.000s
                    rm_dir_1085_4635()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 10.0.bundle", prog_num=4636) as rm_dir_1086_4636:  # 0m:0.000s
                    rm_dir_1086_4636()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 12.1.bundle", prog_num=4637) as rm_dir_1087_4637:  # 0m:0.000s
                    rm_dir_1087_4637()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 13.1.bundle", prog_num=4638) as rm_dir_1088_4638:  # 0m:0.000s
                    rm_dir_1088_4638()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.app", prog_num=4639) as rm_dir_1089_4639:  # 0m:0.000s
                    rm_dir_1089_4639()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.bundle", prog_num=4640) as rm_dir_1090_4640:  # 0m:0.000s
                    rm_dir_1090_4640()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.app", prog_num=4641) as rm_dir_1091_4641:  # 0m:0.000s
                    rm_dir_1091_4641()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.bundle", prog_num=4642) as rm_dir_1092_4642:  # 0m:0.000s
                    rm_dir_1092_4642()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.app", prog_num=4643) as rm_dir_1093_4643:  # 0m:0.000s
                    rm_dir_1093_4643()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.bundle", prog_num=4644) as rm_dir_1094_4644:  # 0m:0.000s
                    rm_dir_1094_4644()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.app", prog_num=4645) as rm_dir_1095_4645:  # 0m:0.000s
                    rm_dir_1095_4645()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.bundle", prog_num=4646) as rm_dir_1096_4646:  # 0m:0.000s
                    rm_dir_1096_4646()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.app", prog_num=4647) as rm_dir_1097_4647:  # 0m:0.004s
                    rm_dir_1097_4647()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.bundle", prog_num=4648) as rm_dir_1098_4648:  # 0m:0.000s
                    rm_dir_1098_4648()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.app", prog_num=4649) as rm_dir_1099_4649:  # 0m:0.000s
                    rm_dir_1099_4649()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.bundle", prog_num=4650) as rm_dir_1100_4650:  # 0m:0.000s
                    rm_dir_1100_4650()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.app", prog_num=4651) as rm_dir_1101_4651:  # 0m:0.000s
                    rm_dir_1101_4651()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.bundle", prog_num=4652) as rm_dir_1102_4652:  # 0m:0.000s
                    rm_dir_1102_4652()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.app", prog_num=4653) as rm_dir_1103_4653:  # 0m:0.000s
                    rm_dir_1103_4653()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.bundle", prog_num=4654) as rm_dir_1104_4654:  # 0m:0.000s
                    rm_dir_1104_4654()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.app", prog_num=4655) as rm_dir_1105_4655:  # 0m:0.000s
                    rm_dir_1105_4655()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.bundle", prog_num=4656) as rm_dir_1106_4656:  # 0m:0.000s
                    rm_dir_1106_4656()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.app", prog_num=4657) as rm_dir_1107_4657:  # 0m:0.000s
                    rm_dir_1107_4657()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.bundle", prog_num=4658) as rm_dir_1108_4658:  # 0m:0.000s
                    rm_dir_1108_4658()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.app", prog_num=4659) as rm_dir_1109_4659:  # 0m:0.000s
                    rm_dir_1109_4659()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.bundle", prog_num=4660) as rm_dir_1110_4660:  # 0m:0.000s
                    rm_dir_1110_4660()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4661) as cd_stage_1111_4661:  # 0m:0.055s
            cd_stage_1111_4661()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=4662) as rm_file_or_dir_1112_4662:  # 0m:0.000s
                rm_file_or_dir_1112_4662()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=4663) as rm_file_or_dir_1113_4663:  # 0m:0.000s
                rm_file_or_dir_1113_4663()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.app", prog_num=4664) as rm_file_or_dir_1114_4664:  # 0m:0.000s
                rm_file_or_dir_1114_4664()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.bundle", prog_num=4665) as rm_file_or_dir_1115_4665:  # 0m:0.000s
                rm_file_or_dir_1115_4665()
            with Stage(r"copy", r"Apogee Symphony MKII Control Panel v14.0.342.343", prog_num=4666):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4667) as should_copy_source_1116_4667:  # ?
                    should_copy_source_1116_4667()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.app", prog_num=4668):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r".", delete_extraneous_files=True, prog_num=4669) as copy_dir_to_dir_1117_4669:  # ?
                            copy_dir_to_dir_1117_4669()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", where_to_unwtar=r".", prog_num=4670) as unwtar_1118_4670:  # ?
                            unwtar_1118_4670()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.app", user_id=-1, group_id=-1, prog_num=4671, recursive=True) as chown_1119_4671:  # 0m:0.000s
                            chown_1119_4671()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4672) as should_copy_source_1120_4672:  # ?
                    should_copy_source_1120_4672()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.bundle", prog_num=4673):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r".", delete_extraneous_files=True, prog_num=4674) as copy_dir_to_dir_1121_4674:  # ?
                            copy_dir_to_dir_1121_4674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", where_to_unwtar=r".", prog_num=4675) as unwtar_1122_4675:  # ?
                            unwtar_1122_4675()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.bundle", user_id=-1, group_id=-1, prog_num=4676, recursive=True) as chown_1123_4676:  # 0m:0.000s
                            chown_1123_4676()
            with Stage(r"copy", r"SoundGrid BR-1 Control Panel v14.0.342.343", prog_num=4677):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4678) as should_copy_source_1124_4678:  # ?
                    should_copy_source_1124_4678()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.app", prog_num=4679):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r".", delete_extraneous_files=True, prog_num=4680) as copy_dir_to_dir_1125_4680:  # ?
                            copy_dir_to_dir_1125_4680()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", where_to_unwtar=r".", prog_num=4681) as unwtar_1126_4681:  # ?
                            unwtar_1126_4681()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.app", user_id=-1, group_id=-1, prog_num=4682, recursive=True) as chown_1127_4682:  # 0m:0.000s
                            chown_1127_4682()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4683) as should_copy_source_1128_4683:  # ?
                    should_copy_source_1128_4683()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", prog_num=4684):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r".", delete_extraneous_files=True, prog_num=4685) as copy_dir_to_dir_1129_4685:  # ?
                            copy_dir_to_dir_1129_4685()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", where_to_unwtar=r".", prog_num=4686) as unwtar_1130_4686:  # ?
                            unwtar_1130_4686()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.bundle", user_id=-1, group_id=-1, prog_num=4687, recursive=True) as chown_1131_4687:  # 0m:0.000s
                            chown_1131_4687()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Control Panel v14.0.436.437", prog_num=4688):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4689) as should_copy_source_1132_4689:  # ?
                    should_copy_source_1132_4689()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", prog_num=4690):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r".", delete_extraneous_files=True, prog_num=4691) as copy_dir_to_dir_1133_4691:  # ?
                            copy_dir_to_dir_1133_4691()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", where_to_unwtar=r".", prog_num=4692) as unwtar_1134_4692:  # ?
                            unwtar_1134_4692()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.app", user_id=-1, group_id=-1, prog_num=4693, recursive=True) as chown_1135_4693:  # 0m:0.000s
                            chown_1135_4693()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4694) as should_copy_source_1136_4694:  # ?
                    should_copy_source_1136_4694()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", prog_num=4695):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r".", delete_extraneous_files=True, prog_num=4696) as copy_dir_to_dir_1137_4696:  # ?
                            copy_dir_to_dir_1137_4696()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", where_to_unwtar=r".", prog_num=4697) as unwtar_1138_4697:  # ?
                            unwtar_1138_4697()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.bundle", user_id=-1, group_id=-1, prog_num=4698, recursive=True) as chown_1139_4698:  # 0m:0.000s
                            chown_1139_4698()
            with Stage(r"copy", r"BMB4 SoundGrid MotherBoard Control Panel v14.0.342.343", prog_num=4699):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4700) as should_copy_source_1140_4700:  # ?
                    should_copy_source_1140_4700()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", prog_num=4701):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r".", delete_extraneous_files=True, prog_num=4702) as copy_dir_to_dir_1141_4702:  # ?
                            copy_dir_to_dir_1141_4702()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", where_to_unwtar=r".", prog_num=4703) as unwtar_1142_4703:  # ?
                            unwtar_1142_4703()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.app", user_id=-1, group_id=-1, prog_num=4704, recursive=True) as chown_1143_4704:  # 0m:0.000s
                            chown_1143_4704()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4705) as should_copy_source_1144_4705:  # ?
                    should_copy_source_1144_4705()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", prog_num=4706):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r".", delete_extraneous_files=True, prog_num=4707) as copy_dir_to_dir_1145_4707:  # ?
                            copy_dir_to_dir_1145_4707()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", where_to_unwtar=r".", prog_num=4708) as unwtar_1146_4708:  # ?
                            unwtar_1146_4708()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.bundle", user_id=-1, group_id=-1, prog_num=4709, recursive=True) as chown_1147_4709:  # 0m:0.000s
                            chown_1147_4709()
            with Stage(r"copy", r"Cadac Control Panel v14.0.342.343", prog_num=4710):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4711) as should_copy_source_1148_4711:  # ?
                    should_copy_source_1148_4711()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Cadac Control.bundle", prog_num=4712):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r".", delete_extraneous_files=True, prog_num=4713) as copy_dir_to_dir_1149_4713:  # ?
                            copy_dir_to_dir_1149_4713()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", where_to_unwtar=r".", prog_num=4714) as unwtar_1150_4714:  # ?
                            unwtar_1150_4714()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control.bundle", user_id=-1, group_id=-1, prog_num=4715, recursive=True) as chown_1151_4715:  # 0m:0.000s
                            chown_1151_4715()
            with Stage(r"copy", r"Calrec Control Panel v14.0.342.343", prog_num=4716):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4717) as should_copy_source_1152_4717:  # ?
                    should_copy_source_1152_4717()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Calrec Control.bundle", prog_num=4718):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r".", delete_extraneous_files=True, prog_num=4719) as copy_dir_to_dir_1153_4719:  # ?
                            copy_dir_to_dir_1153_4719()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", where_to_unwtar=r".", prog_num=4720) as unwtar_1154_4720:  # ?
                            unwtar_1154_4720()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control.bundle", user_id=-1, group_id=-1, prog_num=4721, recursive=True) as chown_1155_4721:  # 0m:0.000s
                            chown_1155_4721()
            with Stage(r"copy", r"Crest Audio Tactus Control Panel v14.0.342.343", prog_num=4722):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4723) as should_copy_source_1156_4723:  # ?
                    should_copy_source_1156_4723()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", prog_num=4724):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r".", delete_extraneous_files=True, prog_num=4725) as copy_dir_to_dir_1157_4725:  # ?
                            copy_dir_to_dir_1157_4725()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", where_to_unwtar=r".", prog_num=4726) as unwtar_1158_4726:  # ?
                            unwtar_1158_4726()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.app", user_id=-1, group_id=-1, prog_num=4727, recursive=True) as chown_1159_4727:  # 0m:0.000s
                            chown_1159_4727()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4728) as should_copy_source_1160_4728:  # ?
                    should_copy_source_1160_4728()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", prog_num=4729):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r".", delete_extraneous_files=True, prog_num=4730) as copy_dir_to_dir_1161_4730:  # ?
                            copy_dir_to_dir_1161_4730()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", where_to_unwtar=r".", prog_num=4731) as unwtar_1162_4731:  # ?
                            unwtar_1162_4731()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.bundle", user_id=-1, group_id=-1, prog_num=4732, recursive=True) as chown_1163_4732:  # 0m:0.000s
                            chown_1163_4732()
            with Stage(r"copy", r"DigiGrid DLI/DLS Control Panel v14.0.342.343", prog_num=4733):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4734) as should_copy_source_1164_4734:  # ?
                    should_copy_source_1164_4734()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", prog_num=4735):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r".", delete_extraneous_files=True, prog_num=4736) as copy_dir_to_dir_1165_4736:  # ?
                            copy_dir_to_dir_1165_4736()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", where_to_unwtar=r".", prog_num=4737) as unwtar_1166_4737:  # ?
                            unwtar_1166_4737()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.app", user_id=-1, group_id=-1, prog_num=4738, recursive=True) as chown_1167_4738:  # 0m:0.001s
                            chown_1167_4738()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4739) as should_copy_source_1168_4739:  # ?
                    should_copy_source_1168_4739()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", prog_num=4740):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r".", delete_extraneous_files=True, prog_num=4741) as copy_dir_to_dir_1169_4741:  # ?
                            copy_dir_to_dir_1169_4741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", where_to_unwtar=r".", prog_num=4742) as unwtar_1170_4742:  # ?
                            unwtar_1170_4742()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.bundle", user_id=-1, group_id=-1, prog_num=4743, recursive=True) as chown_1171_4743:  # 0m:0.006s
                            chown_1171_4743()
            with Stage(r"copy", r"DMI Waves Control Panel v14.0.342.343", prog_num=4744):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4745) as should_copy_source_1172_4745:  # ?
                    should_copy_source_1172_4745()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.app", prog_num=4746):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r".", delete_extraneous_files=True, prog_num=4747) as copy_dir_to_dir_1173_4747:  # ?
                            copy_dir_to_dir_1173_4747()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", where_to_unwtar=r".", prog_num=4748) as unwtar_1174_4748:  # ?
                            unwtar_1174_4748()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.app", user_id=-1, group_id=-1, prog_num=4749, recursive=True) as chown_1175_4749:  # 0m:0.000s
                            chown_1175_4749()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4750) as should_copy_source_1176_4750:  # ?
                    should_copy_source_1176_4750()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.bundle", prog_num=4751):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r".", delete_extraneous_files=True, prog_num=4752) as copy_dir_to_dir_1177_4752:  # ?
                            copy_dir_to_dir_1177_4752()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", where_to_unwtar=r".", prog_num=4753) as unwtar_1178_4753:  # ?
                            unwtar_1178_4753()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.bundle", user_id=-1, group_id=-1, prog_num=4754, recursive=True) as chown_1179_4754:  # 0m:0.000s
                            chown_1179_4754()
            with Stage(r"copy", r"DN32-WSG Control Panel v14.0.342.343", prog_num=4755):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4756) as should_copy_source_1180_4756:  # ?
                    should_copy_source_1180_4756()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", prog_num=4757):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r".", delete_extraneous_files=True, prog_num=4758) as copy_dir_to_dir_1181_4758:  # ?
                            copy_dir_to_dir_1181_4758()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", where_to_unwtar=r".", prog_num=4759) as unwtar_1182_4759:  # ?
                            unwtar_1182_4759()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.app", user_id=-1, group_id=-1, prog_num=4760, recursive=True) as chown_1183_4760:  # 0m:0.000s
                            chown_1183_4760()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4761) as should_copy_source_1184_4761:  # ?
                    should_copy_source_1184_4761()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", prog_num=4762):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=4763) as copy_dir_to_dir_1185_4763:  # ?
                            copy_dir_to_dir_1185_4763()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", where_to_unwtar=r".", prog_num=4764) as unwtar_1186_4764:  # ?
                            unwtar_1186_4764()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=4765, recursive=True) as chown_1187_4765:  # 0m:0.000s
                            chown_1187_4765()
            with Stage(r"copy", r"DSPro SG4000 / SG1000 Control Panel v14.0.342.343", prog_num=4766):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4767) as should_copy_source_1188_4767:  # ?
                    should_copy_source_1188_4767()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", prog_num=4768):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r".", delete_extraneous_files=True, prog_num=4769) as copy_dir_to_dir_1189_4769:  # ?
                            copy_dir_to_dir_1189_4769()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", where_to_unwtar=r".", prog_num=4770) as unwtar_1190_4770:  # ?
                            unwtar_1190_4770()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.app", user_id=-1, group_id=-1, prog_num=4771, recursive=True) as chown_1191_4771:  # 0m:0.000s
                            chown_1191_4771()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4772) as should_copy_source_1192_4772:  # ?
                    should_copy_source_1192_4772()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", prog_num=4773):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r".", delete_extraneous_files=True, prog_num=4774) as copy_dir_to_dir_1193_4774:  # ?
                            copy_dir_to_dir_1193_4774()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", where_to_unwtar=r".", prog_num=4775) as unwtar_1194_4775:  # ?
                            unwtar_1194_4775()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.bundle", user_id=-1, group_id=-1, prog_num=4776, recursive=True) as chown_1195_4776:  # 0m:0.000s
                            chown_1195_4776()
            with Stage(r"copy", r"DigiGrid D Control Panel v14.0.342.343", prog_num=4777):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4778) as should_copy_source_1196_4778:  # ?
                    should_copy_source_1196_4778()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", prog_num=4779):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r".", delete_extraneous_files=True, prog_num=4780) as copy_dir_to_dir_1197_4780:  # ?
                            copy_dir_to_dir_1197_4780()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", where_to_unwtar=r".", prog_num=4781) as unwtar_1198_4781:  # ?
                            unwtar_1198_4781()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.app", user_id=-1, group_id=-1, prog_num=4782, recursive=True) as chown_1199_4782:  # 0m:0.000s
                            chown_1199_4782()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4783) as should_copy_source_1200_4783:  # ?
                    should_copy_source_1200_4783()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", prog_num=4784):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r".", delete_extraneous_files=True, prog_num=4785) as copy_dir_to_dir_1201_4785:  # ?
                            copy_dir_to_dir_1201_4785()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", where_to_unwtar=r".", prog_num=4786) as unwtar_1202_4786:  # ?
                            unwtar_1202_4786()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.bundle", user_id=-1, group_id=-1, prog_num=4787, recursive=True) as chown_1203_4787:  # 0m:0.000s
                            chown_1203_4787()
            with Stage(r"copy", r"DigiGrid M Control Panel v$(ExternalVersion", prog_num=4788):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4789) as should_copy_source_1204_4789:  # ?
                    should_copy_source_1204_4789()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", prog_num=4790):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r".", delete_extraneous_files=True, prog_num=4791) as copy_dir_to_dir_1205_4791:  # ?
                            copy_dir_to_dir_1205_4791()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", where_to_unwtar=r".", prog_num=4792) as unwtar_1206_4792:  # ?
                            unwtar_1206_4792()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.app", user_id=-1, group_id=-1, prog_num=4793, recursive=True) as chown_1207_4793:  # 0m:0.000s
                            chown_1207_4793()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4794) as should_copy_source_1208_4794:  # ?
                    should_copy_source_1208_4794()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", prog_num=4795):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r".", delete_extraneous_files=True, prog_num=4796) as copy_dir_to_dir_1209_4796:  # ?
                            copy_dir_to_dir_1209_4796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", where_to_unwtar=r".", prog_num=4797) as unwtar_1210_4797:  # ?
                            unwtar_1210_4797()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.bundle", user_id=-1, group_id=-1, prog_num=4798, recursive=True) as chown_1211_4798:  # 0m:0.000s
                            chown_1211_4798()
            with Stage(r"copy", r"DigiGrid Q Control Panel v14.0.342.343", prog_num=4799):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4800) as should_copy_source_1212_4800:  # ?
                    should_copy_source_1212_4800()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", prog_num=4801):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r".", delete_extraneous_files=True, prog_num=4802) as copy_dir_to_dir_1213_4802:  # ?
                            copy_dir_to_dir_1213_4802()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", where_to_unwtar=r".", prog_num=4803) as unwtar_1214_4803:  # ?
                            unwtar_1214_4803()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.app", user_id=-1, group_id=-1, prog_num=4804, recursive=True) as chown_1215_4804:  # 0m:0.000s
                            chown_1215_4804()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4805) as should_copy_source_1216_4805:  # ?
                    should_copy_source_1216_4805()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", prog_num=4806):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r".", delete_extraneous_files=True, prog_num=4807) as copy_dir_to_dir_1217_4807:  # ?
                            copy_dir_to_dir_1217_4807()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", where_to_unwtar=r".", prog_num=4808) as unwtar_1218_4808:  # ?
                            unwtar_1218_4808()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.bundle", user_id=-1, group_id=-1, prog_num=4809, recursive=True) as chown_1219_4809:  # 0m:0.000s
                            chown_1219_4809()
            with Stage(r"copy", r"Digico SD Control Panel v14.0.7.8", prog_num=4810):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4811) as should_copy_source_1220_4811:  # ?
                    should_copy_source_1220_4811()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", prog_num=4812):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r".", delete_extraneous_files=True, prog_num=4813) as copy_dir_to_dir_1221_4813:  # ?
                            copy_dir_to_dir_1221_4813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", where_to_unwtar=r".", prog_num=4814) as unwtar_1222_4814:  # ?
                            unwtar_1222_4814()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.app", user_id=-1, group_id=-1, prog_num=4815, recursive=True) as chown_1223_4815:  # 0m:0.000s
                            chown_1223_4815()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4816) as should_copy_source_1224_4816:  # ?
                    should_copy_source_1224_4816()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", prog_num=4817):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r".", delete_extraneous_files=True, prog_num=4818) as copy_dir_to_dir_1225_4818:  # ?
                            copy_dir_to_dir_1225_4818()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", where_to_unwtar=r".", prog_num=4819) as unwtar_1226_4819:  # ?
                            unwtar_1226_4819()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.bundle", user_id=-1, group_id=-1, prog_num=4820, recursive=True) as chown_1227_4820:  # 0m:0.000s
                            chown_1227_4820()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Control Panel v14.0.342.343", prog_num=4821):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4822) as should_copy_source_1228_4822:  # ?
                    should_copy_source_1228_4822()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=4823):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=4824) as copy_dir_to_dir_1229_4824:  # ?
                            copy_dir_to_dir_1229_4824()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=4825) as unwtar_1230_4825:  # ?
                            unwtar_1230_4825()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=4826, recursive=True) as chown_1231_4826:  # 0m:0.005s
                            chown_1231_4826()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4827) as should_copy_source_1232_4827:  # ?
                    should_copy_source_1232_4827()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=4828):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=4829) as copy_dir_to_dir_1233_4829:  # ?
                            copy_dir_to_dir_1233_4829()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=4830) as unwtar_1234_4830:  # ?
                            unwtar_1234_4830()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=4831, recursive=True) as chown_1235_4831:  # 0m:0.001s
                            chown_1235_4831()
            with Stage(r"copy", r"DirectOut SG.MADI Control Panel v14.0.342.343", prog_num=4832):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4833) as should_copy_source_1236_4833:  # ?
                    should_copy_source_1236_4833()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", prog_num=4834):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r".", delete_extraneous_files=True, prog_num=4835) as copy_dir_to_dir_1237_4835:  # ?
                            copy_dir_to_dir_1237_4835()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", where_to_unwtar=r".", prog_num=4836) as unwtar_1238_4836:  # ?
                            unwtar_1238_4836()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.app", user_id=-1, group_id=-1, prog_num=4837, recursive=True) as chown_1239_4837:  # 0m:0.000s
                            chown_1239_4837()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4838) as should_copy_source_1240_4838:  # ?
                    should_copy_source_1240_4838()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", prog_num=4839):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r".", delete_extraneous_files=True, prog_num=4840) as copy_dir_to_dir_1241_4840:  # ?
                            copy_dir_to_dir_1241_4840()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", where_to_unwtar=r".", prog_num=4841) as unwtar_1242_4841:  # ?
                            unwtar_1242_4841()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.bundle", user_id=-1, group_id=-1, prog_num=4842, recursive=True) as chown_1243_4842:  # 0m:0.000s
                            chown_1243_4842()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Control Panel v13.1.261.180", prog_num=4843):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4844) as should_copy_source_1244_4844:  # ?
                    should_copy_source_1244_4844()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=4845):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=4846) as copy_dir_to_dir_1245_4846:  # ?
                            copy_dir_to_dir_1245_4846()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=4847) as unwtar_1246_4847:  # ?
                            unwtar_1246_4847()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=4848, recursive=True) as chown_1247_4848:  # 0m:0.000s
                            chown_1247_4848()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4849) as should_copy_source_1248_4849:  # ?
                    should_copy_source_1248_4849()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=4850):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=4851) as copy_dir_to_dir_1249_4851:  # ?
                            copy_dir_to_dir_1249_4851()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=4852) as unwtar_1250_4852:  # ?
                            unwtar_1250_4852()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=4853, recursive=True) as chown_1251_4853:  # 0m:0.000s
                            chown_1251_4853()
            with Stage(r"copy", r"Hear Technologies SG Control Panel v14.0.342.343", prog_num=4854):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4855) as should_copy_source_1252_4855:  # ?
                    should_copy_source_1252_4855()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", prog_num=4856):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r".", delete_extraneous_files=True, prog_num=4857) as copy_dir_to_dir_1253_4857:  # ?
                            copy_dir_to_dir_1253_4857()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", where_to_unwtar=r".", prog_num=4858) as unwtar_1254_4858:  # ?
                            unwtar_1254_4858()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.app", user_id=-1, group_id=-1, prog_num=4859, recursive=True) as chown_1255_4859:  # 0m:0.000s
                            chown_1255_4859()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4860) as should_copy_source_1256_4860:  # ?
                    should_copy_source_1256_4860()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", prog_num=4861):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r".", delete_extraneous_files=True, prog_num=4862) as copy_dir_to_dir_1257_4862:  # ?
                            copy_dir_to_dir_1257_4862()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", where_to_unwtar=r".", prog_num=4863) as unwtar_1258_4863:  # ?
                            unwtar_1258_4863()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.bundle", user_id=-1, group_id=-1, prog_num=4864, recursive=True) as chown_1259_4864:  # 0m:0.000s
                            chown_1259_4864()
            with Stage(r"copy", r"DigiGrid IOC Control Panel v14.0.342.343", prog_num=4865):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4866) as should_copy_source_1260_4866:  # ?
                    should_copy_source_1260_4866()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", prog_num=4867):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r".", delete_extraneous_files=True, prog_num=4868) as copy_dir_to_dir_1261_4868:  # ?
                            copy_dir_to_dir_1261_4868()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", where_to_unwtar=r".", prog_num=4869) as unwtar_1262_4869:  # ?
                            unwtar_1262_4869()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.app", user_id=-1, group_id=-1, prog_num=4870, recursive=True) as chown_1263_4870:  # 0m:0.000s
                            chown_1263_4870()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4871) as should_copy_source_1264_4871:  # ?
                    should_copy_source_1264_4871()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", prog_num=4872):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r".", delete_extraneous_files=True, prog_num=4873) as copy_dir_to_dir_1265_4873:  # ?
                            copy_dir_to_dir_1265_4873()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", where_to_unwtar=r".", prog_num=4874) as unwtar_1266_4874:  # ?
                            unwtar_1266_4874()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.bundle", user_id=-1, group_id=-1, prog_num=4875, recursive=True) as chown_1267_4875:  # 0m:0.000s
                            chown_1267_4875()
            with Stage(r"copy", r"IONIC16 Control Panel v14.0.134.135", prog_num=4876):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4877) as should_copy_source_1268_4877:  # ?
                    should_copy_source_1268_4877()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.app", prog_num=4878):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r".", delete_extraneous_files=True, prog_num=4879) as copy_dir_to_dir_1269_4879:  # ?
                            copy_dir_to_dir_1269_4879()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", where_to_unwtar=r".", prog_num=4880) as unwtar_1270_4880:  # ?
                            unwtar_1270_4880()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.app", user_id=-1, group_id=-1, prog_num=4881, recursive=True) as chown_1271_4881:  # 0m:0.000s
                            chown_1271_4881()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4882) as should_copy_source_1272_4882:  # ?
                    should_copy_source_1272_4882()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.bundle", prog_num=4883):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r".", delete_extraneous_files=True, prog_num=4884) as copy_dir_to_dir_1273_4884:  # ?
                            copy_dir_to_dir_1273_4884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", where_to_unwtar=r".", prog_num=4885) as unwtar_1274_4885:  # ?
                            unwtar_1274_4885()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.bundle", user_id=-1, group_id=-1, prog_num=4886, recursive=True) as chown_1275_4886:  # 0m:0.000s
                            chown_1275_4886()
            with Stage(r"copy", r"DigiGrid IOS Control Panel v14.0.342.343", prog_num=4887):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4888) as should_copy_source_1276_4888:  # ?
                    should_copy_source_1276_4888()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", prog_num=4889):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r".", delete_extraneous_files=True, prog_num=4890) as copy_dir_to_dir_1277_4890:  # ?
                            copy_dir_to_dir_1277_4890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", where_to_unwtar=r".", prog_num=4891) as unwtar_1278_4891:  # ?
                            unwtar_1278_4891()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.app", user_id=-1, group_id=-1, prog_num=4892, recursive=True) as chown_1279_4892:  # 0m:0.000s
                            chown_1279_4892()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4893) as should_copy_source_1280_4893:  # ?
                    should_copy_source_1280_4893()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", prog_num=4894):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r".", delete_extraneous_files=True, prog_num=4895) as copy_dir_to_dir_1281_4895:  # ?
                            copy_dir_to_dir_1281_4895()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", where_to_unwtar=r".", prog_num=4896) as unwtar_1282_4896:  # ?
                            unwtar_1282_4896()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.bundle", user_id=-1, group_id=-1, prog_num=4897, recursive=True) as chown_1283_4897:  # 0m:0.004s
                            chown_1283_4897()
            with Stage(r"copy", r"DigiGrid IOS-XL Control Panel v14.0.342.343", prog_num=4898):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4899) as should_copy_source_1284_4899:  # ?
                    should_copy_source_1284_4899()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", prog_num=4900):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r".", delete_extraneous_files=True, prog_num=4901) as copy_dir_to_dir_1285_4901:  # ?
                            copy_dir_to_dir_1285_4901()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", where_to_unwtar=r".", prog_num=4902) as unwtar_1286_4902:  # ?
                            unwtar_1286_4902()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.app", user_id=-1, group_id=-1, prog_num=4903, recursive=True) as chown_1287_4903:  # 0m:0.000s
                            chown_1287_4903()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4904) as should_copy_source_1288_4904:  # ?
                    should_copy_source_1288_4904()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", prog_num=4905):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r".", delete_extraneous_files=True, prog_num=4906) as copy_dir_to_dir_1289_4906:  # ?
                            copy_dir_to_dir_1289_4906()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", where_to_unwtar=r".", prog_num=4907) as unwtar_1290_4907:  # ?
                            unwtar_1290_4907()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.bundle", user_id=-1, group_id=-1, prog_num=4908, recursive=True) as chown_1291_4908:  # 0m:0.000s
                            chown_1291_4908()
            with Stage(r"copy", r"DigiGrid IOX Control Panel v14.0.342.343", prog_num=4909):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4910) as should_copy_source_1292_4910:  # ?
                    should_copy_source_1292_4910()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", prog_num=4911):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r".", delete_extraneous_files=True, prog_num=4912) as copy_dir_to_dir_1293_4912:  # ?
                            copy_dir_to_dir_1293_4912()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", where_to_unwtar=r".", prog_num=4913) as unwtar_1294_4913:  # ?
                            unwtar_1294_4913()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.app", user_id=-1, group_id=-1, prog_num=4914, recursive=True) as chown_1295_4914:  # 0m:0.000s
                            chown_1295_4914()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4915) as should_copy_source_1296_4915:  # ?
                    should_copy_source_1296_4915()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", prog_num=4916):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r".", delete_extraneous_files=True, prog_num=4917) as copy_dir_to_dir_1297_4917:  # ?
                            copy_dir_to_dir_1297_4917()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", where_to_unwtar=r".", prog_num=4918) as unwtar_1298_4918:  # ?
                            unwtar_1298_4918()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.bundle", user_id=-1, group_id=-1, prog_num=4919, recursive=True) as chown_1299_4919:  # 0m:0.000s
                            chown_1299_4919()
            with Stage(r"copy", r"JoeCo BBSG24MP Control Panel v14.0.342.343", prog_num=4920):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4921) as should_copy_source_1300_4921:  # ?
                    should_copy_source_1300_4921()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", prog_num=4922):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r".", delete_extraneous_files=True, prog_num=4923) as copy_dir_to_dir_1301_4923:  # ?
                            copy_dir_to_dir_1301_4923()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", where_to_unwtar=r".", prog_num=4924) as unwtar_1302_4924:  # ?
                            unwtar_1302_4924()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.app", user_id=-1, group_id=-1, prog_num=4925, recursive=True) as chown_1303_4925:  # 0m:0.000s
                            chown_1303_4925()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4926) as should_copy_source_1304_4926:  # ?
                    should_copy_source_1304_4926()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", prog_num=4927):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r".", delete_extraneous_files=True, prog_num=4928) as copy_dir_to_dir_1305_4928:  # ?
                            copy_dir_to_dir_1305_4928()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", where_to_unwtar=r".", prog_num=4929) as unwtar_1306_4929:  # ?
                            unwtar_1306_4929()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.bundle", user_id=-1, group_id=-1, prog_num=4930, recursive=True) as chown_1307_4930:  # 0m:0.000s
                            chown_1307_4930()
            with Stage(r"copy", r"M-DL-WAVES3 Control Panel v14.0.342.343", prog_num=4931):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4932) as should_copy_source_1308_4932:  # ?
                    should_copy_source_1308_4932()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", prog_num=4933):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=4934) as copy_dir_to_dir_1309_4934:  # ?
                            copy_dir_to_dir_1309_4934()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", where_to_unwtar=r".", prog_num=4935) as unwtar_1310_4935:  # ?
                            unwtar_1310_4935()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=4936, recursive=True) as chown_1311_4936:  # 0m:0.000s
                            chown_1311_4936()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4937) as should_copy_source_1312_4937:  # ?
                    should_copy_source_1312_4937()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", prog_num=4938):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=4939) as copy_dir_to_dir_1313_4939:  # ?
                            copy_dir_to_dir_1313_4939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=4940) as unwtar_1314_4940:  # ?
                            unwtar_1314_4940()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=4941, recursive=True) as chown_1315_4941:  # 0m:0.000s
                            chown_1315_4941()
            with Stage(r"copy", r"M-SQ-WAVES3 Control Panel v14.0.342.343", prog_num=4942):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4943) as should_copy_source_1316_4943:  # ?
                    should_copy_source_1316_4943()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", prog_num=4944):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=4945) as copy_dir_to_dir_1317_4945:  # ?
                            copy_dir_to_dir_1317_4945()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", where_to_unwtar=r".", prog_num=4946) as unwtar_1318_4946:  # ?
                            unwtar_1318_4946()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=4947, recursive=True) as chown_1319_4947:  # 0m:0.000s
                            chown_1319_4947()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4948) as should_copy_source_1320_4948:  # ?
                    should_copy_source_1320_4948()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", prog_num=4949):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=4950) as copy_dir_to_dir_1321_4950:  # ?
                            copy_dir_to_dir_1321_4950()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=4951) as unwtar_1322_4951:  # ?
                            unwtar_1322_4951()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=4952, recursive=True) as chown_1323_4952:  # 0m:0.000s
                            chown_1323_4952()
            with Stage(r"copy", r"M-Waves v2 Control Panel v14.0.342.343", prog_num=4953):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4954) as should_copy_source_1324_4954:  # ?
                    should_copy_source_1324_4954()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", prog_num=4955):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r".", delete_extraneous_files=True, prog_num=4956) as copy_dir_to_dir_1325_4956:  # ?
                            copy_dir_to_dir_1325_4956()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", where_to_unwtar=r".", prog_num=4957) as unwtar_1326_4957:  # ?
                            unwtar_1326_4957()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.app", user_id=-1, group_id=-1, prog_num=4958, recursive=True) as chown_1327_4958:  # 0m:0.000s
                            chown_1327_4958()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4959) as should_copy_source_1328_4959:  # ?
                    should_copy_source_1328_4959()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", prog_num=4960):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r".", delete_extraneous_files=True, prog_num=4961) as copy_dir_to_dir_1329_4961:  # ?
                            copy_dir_to_dir_1329_4961()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", where_to_unwtar=r".", prog_num=4962) as unwtar_1330_4962:  # ?
                            unwtar_1330_4962()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.bundle", user_id=-1, group_id=-1, prog_num=4963, recursive=True) as chown_1331_4963:  # 0m:0.000s
                            chown_1331_4963()
            with Stage(r"copy", r"DigiGrid MGB/MGO/MGR Control Panel v14.0.342.343", prog_num=4964):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4965) as should_copy_source_1332_4965:  # ?
                    should_copy_source_1332_4965()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", prog_num=4966):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r".", delete_extraneous_files=True, prog_num=4967) as copy_dir_to_dir_1333_4967:  # ?
                            copy_dir_to_dir_1333_4967()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", where_to_unwtar=r".", prog_num=4968) as unwtar_1334_4968:  # ?
                            unwtar_1334_4968()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.app", user_id=-1, group_id=-1, prog_num=4969, recursive=True) as chown_1335_4969:  # 0m:0.000s
                            chown_1335_4969()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4970) as should_copy_source_1336_4970:  # ?
                    should_copy_source_1336_4970()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", prog_num=4971):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r".", delete_extraneous_files=True, prog_num=4972) as copy_dir_to_dir_1337_4972:  # ?
                            copy_dir_to_dir_1337_4972()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", where_to_unwtar=r".", prog_num=4973) as unwtar_1338_4973:  # ?
                            unwtar_1338_4973()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.bundle", user_id=-1, group_id=-1, prog_num=4974, recursive=True) as chown_1339_4974:  # 0m:0.000s
                            chown_1339_4974()
            with Stage(r"copy", r"Waves Legacy SG Control Panels v14.0.342.343", prog_num=4975):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4976) as should_copy_source_1340_4976:  # ?
                    should_copy_source_1340_4976()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.app", prog_num=4977):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r".", delete_extraneous_files=True, prog_num=4978) as copy_dir_to_dir_1341_4978:  # ?
                            copy_dir_to_dir_1341_4978()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", where_to_unwtar=r".", prog_num=4979) as unwtar_1342_4979:  # ?
                            unwtar_1342_4979()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.app", user_id=-1, group_id=-1, prog_num=4980, recursive=True) as chown_1343_4980:  # 0m:0.000s
                            chown_1343_4980()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4981) as should_copy_source_1344_4981:  # ?
                    should_copy_source_1344_4981()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", prog_num=4982):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r".", delete_extraneous_files=True, prog_num=4983) as copy_dir_to_dir_1345_4983:  # ?
                            copy_dir_to_dir_1345_4983()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", where_to_unwtar=r".", prog_num=4984) as unwtar_1346_4984:  # ?
                            unwtar_1346_4984()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.bundle", user_id=-1, group_id=-1, prog_num=4985, recursive=True) as chown_1347_4985:  # 0m:0.000s
                            chown_1347_4985()
            with Stage(r"copy", r"Remote SG IO Control Panel v14.0.342.343", prog_num=4986):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4987) as should_copy_source_1348_4987:  # ?
                    should_copy_source_1348_4987()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", prog_num=4988):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r".", delete_extraneous_files=True, prog_num=4989) as copy_dir_to_dir_1349_4989:  # ?
                            copy_dir_to_dir_1349_4989()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", where_to_unwtar=r".", prog_num=4990) as unwtar_1350_4990:  # ?
                            unwtar_1350_4990()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.app", user_id=-1, group_id=-1, prog_num=4991, recursive=True) as chown_1351_4991:  # 0m:0.000s
                            chown_1351_4991()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4992) as should_copy_source_1352_4992:  # ?
                    should_copy_source_1352_4992()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", prog_num=4993):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r".", delete_extraneous_files=True, prog_num=4994) as copy_dir_to_dir_1353_4994:  # ?
                            copy_dir_to_dir_1353_4994()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", where_to_unwtar=r".", prog_num=4995) as unwtar_1354_4995:  # ?
                            unwtar_1354_4995()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.bundle", user_id=-1, group_id=-1, prog_num=4996, recursive=True) as chown_1355_4996:  # 0m:0.000s
                            chown_1355_4996()
            with Stage(r"copy", r"SG Connect v14.0.342.343", prog_num=4997):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4998) as should_copy_source_1356_4998:  # ?
                    should_copy_source_1356_4998()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SG Connect Control.bundle", prog_num=4999):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r".", delete_extraneous_files=True, prog_num=5000) as copy_dir_to_dir_1357_5000:  # ?
                            copy_dir_to_dir_1357_5000()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", where_to_unwtar=r".", prog_num=5001) as unwtar_1358_5001:  # ?
                            unwtar_1358_5001()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control.bundle", user_id=-1, group_id=-1, prog_num=5002, recursive=True) as chown_1359_5002:  # 0m:0.001s
                            chown_1359_5002()
            with Stage(r"copy", r"SoundStudio STG Control Panel v14.0.342.343", prog_num=5003):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5004) as should_copy_source_1360_5004:  # ?
                    should_copy_source_1360_5004()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", prog_num=5005):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r".", delete_extraneous_files=True, prog_num=5006) as copy_dir_to_dir_1361_5006:  # ?
                            copy_dir_to_dir_1361_5006()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", where_to_unwtar=r".", prog_num=5007) as unwtar_1362_5007:  # ?
                            unwtar_1362_5007()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.app", user_id=-1, group_id=-1, prog_num=5008, recursive=True) as chown_1363_5008:  # 0m:0.004s
                            chown_1363_5008()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5009) as should_copy_source_1364_5009:  # ?
                    should_copy_source_1364_5009()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", prog_num=5010):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r".", delete_extraneous_files=True, prog_num=5011) as copy_dir_to_dir_1365_5011:  # ?
                            copy_dir_to_dir_1365_5011()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", where_to_unwtar=r".", prog_num=5012) as unwtar_1366_5012:  # ?
                            unwtar_1366_5012()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.bundle", user_id=-1, group_id=-1, prog_num=5013, recursive=True) as chown_1367_5013:  # 0m:0.000s
                            chown_1367_5013()
            with Stage(r"copy", r"X-WSG Control Panel v14.0.342.343", prog_num=5014):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5015) as should_copy_source_1368_5015:  # ?
                    should_copy_source_1368_5015()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", prog_num=5016):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r".", delete_extraneous_files=True, prog_num=5017) as copy_dir_to_dir_1369_5017:  # ?
                            copy_dir_to_dir_1369_5017()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", where_to_unwtar=r".", prog_num=5018) as unwtar_1370_5018:  # ?
                            unwtar_1370_5018()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.app", user_id=-1, group_id=-1, prog_num=5019, recursive=True) as chown_1371_5019:  # 0m:0.000s
                            chown_1371_5019()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5020) as should_copy_source_1372_5020:  # ?
                    should_copy_source_1372_5020()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", prog_num=5021):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=5022) as copy_dir_to_dir_1373_5022:  # ?
                            copy_dir_to_dir_1373_5022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", where_to_unwtar=r".", prog_num=5023) as unwtar_1374_5023:  # ?
                            unwtar_1374_5023()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=5024, recursive=True) as chown_1375_5024:  # 0m:0.000s
                            chown_1375_5024()
            with Stage(r"copy", r"Yamaha SoundGrid IO Control Panel v14.0.342.343", prog_num=5025):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5026) as should_copy_source_1376_5026:  # ?
                    should_copy_source_1376_5026()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", prog_num=5027):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r".", delete_extraneous_files=True, prog_num=5028) as copy_dir_to_dir_1377_5028:  # ?
                            copy_dir_to_dir_1377_5028()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", where_to_unwtar=r".", prog_num=5029) as unwtar_1378_5029:  # ?
                            unwtar_1378_5029()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.app", user_id=-1, group_id=-1, prog_num=5030, recursive=True) as chown_1379_5030:  # 0m:0.000s
                            chown_1379_5030()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5031) as should_copy_source_1380_5031:  # ?
                    should_copy_source_1380_5031()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", prog_num=5032):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=5033) as copy_dir_to_dir_1381_5033:  # ?
                            copy_dir_to_dir_1381_5033()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", where_to_unwtar=r".", prog_num=5034) as unwtar_1382_5034:  # ?
                            unwtar_1382_5034()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.bundle", user_id=-1, group_id=-1, prog_num=5035, recursive=True) as chown_1383_5035:  # 0m:0.000s
                            chown_1383_5035()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5036) as shell_command_1384_5036:  # 0m:0.015s
                shell_command_1384_5036()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=5037) as cd_stage_1385_5037:  # 0m:0.005s
            cd_stage_1385_5037()
            with Stage(r"copy", r"Waves Local Server v12.14.471.472", prog_num=5038):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=5, prog_num=5039) as should_copy_source_1386_5039:  # ?
                    should_copy_source_1386_5039()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=5040):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=5041) as copy_dir_to_dir_1387_5041:  # ?
                            copy_dir_to_dir_1387_5041()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=5042) as unwtar_1388_5042:  # ?
                            unwtar_1388_5042()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=5043, recursive=True) as chown_1389_5043:  # ?
                            chown_1389_5043()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5044) as if_1390_5044:  # 0m:0.001s
                            if_1390_5044()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=5045) as cd_stage_1391_5045:  # 0m:0.001s
            cd_stage_1391_5045()
            with Stage(r"copy", r"WavesPluginServer_V14_2 v13.6.444.720", prog_num=5046):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=5047) as should_copy_source_1392_5047:  # ?
                    should_copy_source_1392_5047()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", prog_num=5048):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=5049) as copy_dir_to_dir_1393_5049:  # ?
                            copy_dir_to_dir_1393_5049()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", where_to_unwtar=r".", prog_num=5050) as unwtar_1394_5050:  # ?
                            unwtar_1394_5050()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle", user_id=-1, group_id=-1, prog_num=5051, recursive=True) as chown_1395_5051:  # ?
                            chown_1395_5051()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5052) as if_1396_5052:  # 0m:0.001s
                            if_1396_5052()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=5053) as cd_stage_1397_5053:  # 0m:2.181s
            cd_stage_1397_5053()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=5054):  # 0m:1.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=5055) as should_copy_source_1398_5055:  # 0m:1.074s
                    should_copy_source_1398_5055()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=5056):  # 0m:1.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=5057) as copy_dir_to_dir_1399_5057:  # 0m:0.024s
                            copy_dir_to_dir_1399_5057()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=5058) as unwtar_1400_5058:  # 0m:0.981s
                            unwtar_1400_5058()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=5059, recursive=True) as chown_1401_5059:  # 0m:0.000s
                            chown_1401_5059()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=5060) as break_hard_link_1402_5060:  # 0m:0.012s
                            break_hard_link_1402_5060()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=5061) as shell_command_1403_5061:  # 0m:0.048s
                            shell_command_1403_5061()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=5062, recursive=True) as chown_1404_5062:  # 0m:0.000s
                            chown_1404_5062()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=5063, recursive=True) as chmod_1405_5063:  # 0m:0.007s
                            chmod_1405_5063()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=5064):  # 0m:1.106s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=5065) as should_copy_source_1406_5065:  # 0m:1.106s
                    should_copy_source_1406_5065()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=5066):  # 0m:1.105s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=5067) as copy_dir_to_dir_1407_5067:  # 0m:0.026s
                            copy_dir_to_dir_1407_5067()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=5068) as unwtar_1408_5068:  # 0m:1.005s
                            unwtar_1408_5068()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=5069, recursive=True) as chown_1409_5069:  # 0m:0.000s
                            chown_1409_5069()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=5070) as break_hard_link_1410_5070:  # 0m:0.019s
                            break_hard_link_1410_5070()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=5071) as shell_command_1411_5071:  # 0m:0.047s
                            shell_command_1411_5071()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=5072, recursive=True) as chown_1412_5072:  # 0m:0.000s
                            chown_1412_5072()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=5073, recursive=True) as chmod_1413_5073:  # 0m:0.007s
                            chmod_1413_5073()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=5074) as cd_stage_1414_5074:  # 0m:0.003s
            cd_stage_1414_5074()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=5075):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5076) as should_copy_source_1415_5076:  # ?
                    should_copy_source_1415_5076()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=5077):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=5078) as copy_dir_to_dir_1416_5078:  # ?
                            copy_dir_to_dir_1416_5078()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=5079) as unwtar_1417_5079:  # ?
                            unwtar_1417_5079()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=5080, recursive=True) as chown_1418_5080:  # ?
                            chown_1418_5080()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=5081) as shell_command_1419_5081:  # 0m:0.001s
                            shell_command_1419_5081()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=5082):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5083) as should_copy_source_1420_5083:  # ?
                    should_copy_source_1420_5083()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=5084):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=5085) as copy_dir_to_dir_1421_5085:  # ?
                            copy_dir_to_dir_1421_5085()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=5086) as unwtar_1422_5086:  # ?
                            unwtar_1422_5086()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=5087, recursive=True) as chown_1423_5087:  # ?
                            chown_1423_5087()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=5088) as shell_command_1424_5088:  # 0m:0.001s
                            shell_command_1424_5088()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=5089):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5090) as should_copy_source_1425_5090:  # ?
                    should_copy_source_1425_5090()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=5091):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=5092) as copy_dir_to_dir_1426_5092:  # ?
                            copy_dir_to_dir_1426_5092()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=5093) as unwtar_1427_5093:  # ?
                            unwtar_1427_5093()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=5094, recursive=True) as chown_1428_5094:  # ?
                            chown_1428_5094()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=5095) as shell_command_1429_5095:  # 0m:0.000s
                            shell_command_1429_5095()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=5096) as cd_stage_1430_5096:  # 0m:0.001s
            cd_stage_1430_5096()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=5097):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=5098) as should_copy_source_1431_5098:  # ?
                    should_copy_source_1431_5098()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=5099):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=5100) as copy_dir_to_dir_1432_5100:  # ?
                            copy_dir_to_dir_1432_5100()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=5101) as unwtar_1433_5101:  # ?
                            unwtar_1433_5101()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=5102, recursive=True) as chown_1434_5102:  # ?
                            chown_1434_5102()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=5103) as shell_command_1435_5103:  # 0m:0.000s
                            shell_command_1435_5103()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=5104):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=5105) as should_copy_source_1436_5105:  # ?
                    should_copy_source_1436_5105()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=5106):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=5107) as copy_dir_to_dir_1437_5107:  # ?
                            copy_dir_to_dir_1437_5107()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=5108) as unwtar_1438_5108:  # ?
                            unwtar_1438_5108()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=5109, recursive=True) as chown_1439_5109:  # ?
                            chown_1439_5109()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=5110) as shell_command_1440_5110:  # 0m:0.000s
                            shell_command_1440_5110()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5111) as cd_stage_1441_5111:  # 0m:0.001s
            cd_stage_1441_5111()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=5112):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=5113) as should_copy_source_1442_5113:  # ?
                    should_copy_source_1442_5113()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=5114):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=5115) as copy_dir_to_dir_1443_5115:  # ?
                            copy_dir_to_dir_1443_5115()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=5116) as unwtar_1444_5116:  # ?
                            unwtar_1444_5116()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=5117, recursive=True) as chown_1445_5117:  # ?
                            chown_1445_5117()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=5118) as shell_command_1446_5118:  # ?
                            shell_command_1446_5118()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=5119) as script_command_1447_5119:  # ?
                            script_command_1447_5119()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5120) as shell_command_1448_5120:  # 0m:0.000s
                            shell_command_1448_5120()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5121) as create_symlink_1449_5121:  # 0m:0.000s
                create_symlink_1449_5121()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5122) as create_symlink_1450_5122:  # 0m:0.000s
                create_symlink_1450_5122()
        with CdStage(r"copy_to_folder", r"/Users/Shared/Waves/SoundGrid Studio/Templates", prog_num=5123) as cd_stage_1451_5123:  # 0m:0.001s
            cd_stage_1451_5123()
            with Stage(r"copy", r"SoundGrid Studio Sessions Structure", prog_num=5124):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r"/Users/Shared/Waves/SoundGrid Studio/Templates", skip_progress_count=3, prog_num=5125) as should_copy_source_1452_5125:  # ?
                    should_copy_source_1452_5125()
                    with Stage(r"copy source", r"Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", prog_num=5126):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r".", prog_num=5127) as copy_file_to_dir_1453_5127:  # ?
                            copy_file_to_dir_1453_5127()
                        with ChmodAndChown(path=r"Empty Session.sgst", mode="a+rw", user_id=-1, group_id=-1, prog_num=5128) as chmod_and_chown_1454_5128:  # 0m:0.001s
                            chmod_and_chown_1454_5128()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=5129) as cd_stage_1455_5129:  # 0m:0.006s
            cd_stage_1455_5129()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Lamps/Vocal/Vocal 2 (Lead).xps", prog_num=5130) as rm_file_or_dir_1456_5130:  # 0m:0.001s
                rm_file_or_dir_1456_5130()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Factory", prog_num=5131) as rm_file_or_dir_1457_5131:  # 0m:0.000s
                rm_file_or_dir_1457_5131()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/GroupOrder.xps", prog_num=5132) as rm_file_or_dir_1458_5132:  # 0m:0.000s
                rm_file_or_dir_1458_5132()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Kori Andres", prog_num=5133) as rm_file_or_dir_1459_5133:  # 0m:0.000s
                rm_file_or_dir_1459_5133()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/Symphony II SoundGrid User Guide", prog_num=5134) as rm_file_or_dir_1460_5134:  # 0m:0.000s
            rm_file_or_dir_1460_5134()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=5135) as rm_file_or_dir_1461_5135:  # 0m:0.000s
            rm_file_or_dir_1461_5135()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack and Network Streaming with HD-HDX-HDNative - external Server.emo", prog_num=5136) as rm_file_or_dir_1462_5136:  # 0m:0.000s
            rm_file_or_dir_1462_5136()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack Processing for HD-HDX-HDNative Systems - external Server.emo", prog_num=5137) as rm_file_or_dir_1463_5137:  # 0m:0.000s
            rm_file_or_dir_1463_5137()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Mixing with StudioRack - external Server.emo", prog_num=5138) as rm_file_or_dir_1464_5138:  # 0m:0.000s
            rm_file_or_dir_1464_5138()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Recording thru eMotion Mixer - external Server.emo", prog_num=5139) as rm_file_or_dir_1465_5139:  # 0m:0.000s
            rm_file_or_dir_1465_5139()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and External Mixing  - external Server.emo", prog_num=5140) as rm_file_or_dir_1466_5140:  # 0m:0.000s
            rm_file_or_dir_1466_5140()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and Monitoring - external Server.emo", prog_num=5141) as rm_file_or_dir_1467_5141:  # 0m:0.000s
            rm_file_or_dir_1467_5141()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=5142) as rm_file_or_dir_1468_5142:  # 0m:0.000s
            rm_file_or_dir_1468_5142()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack and Network Streaming with HD-HDX-HDNative.emo", prog_num=5143) as rm_file_or_dir_1469_5143:  # 0m:0.000s
            rm_file_or_dir_1469_5143()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack Processing for HD-HDX-HDNative Systems.emo", prog_num=5144) as rm_file_or_dir_1470_5144:  # 0m:0.000s
            rm_file_or_dir_1470_5144()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Mixing with StudioRack.emo", prog_num=5145) as rm_file_or_dir_1471_5145:  # 0m:0.000s
            rm_file_or_dir_1471_5145()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Recording thru eMotion Mixer.emo", prog_num=5146) as rm_file_or_dir_1472_5146:  # 0m:0.000s
            rm_file_or_dir_1472_5146()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and External Mixing.emo", prog_num=5147) as rm_file_or_dir_1473_5147:  # 0m:0.000s
            rm_file_or_dir_1473_5147()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and Monitoring.emo", prog_num=5148) as rm_file_or_dir_1474_5148:  # 0m:0.000s
            rm_file_or_dir_1474_5148()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS DLI REC-PB Standalone.emo", prog_num=5149) as rm_file_or_dir_1475_5149:  # 0m:0.000s
            rm_file_or_dir_1475_5149()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=5150) as rm_file_or_dir_1476_5150:  # 0m:0.001s
            rm_file_or_dir_1476_5150()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid D User Guide.pdf", prog_num=5151) as rm_file_or_dir_1477_5151:  # 0m:0.000s
            rm_file_or_dir_1477_5151()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid M User Guide.pdf", prog_num=5152) as rm_file_or_dir_1478_5152:  # 0m:0.000s
            rm_file_or_dir_1478_5152()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid Q User Guide.pdf", prog_num=5153) as rm_file_or_dir_1479_5153:  # 0m:0.000s
            rm_file_or_dir_1479_5153()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - Recording thru eMotion Mixer.emo", prog_num=5154) as rm_file_or_dir_1480_5154:  # 0m:0.000s
            rm_file_or_dir_1480_5154()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - REC-PB Standalone.emo", prog_num=5155) as rm_file_or_dir_1481_5155:  # 0m:0.000s
            rm_file_or_dir_1481_5155()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - StudioRack Processing and Monitoring.emo", prog_num=5156) as rm_file_or_dir_1482_5156:  # 0m:0.000s
            rm_file_or_dir_1482_5156()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - Recording thru eMotion Mixer - external Server.emo", prog_num=5157) as rm_file_or_dir_1483_5157:  # 0m:0.000s
            rm_file_or_dir_1483_5157()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - REC-PB Standalone.emo", prog_num=5158) as rm_file_or_dir_1484_5158:  # 0m:0.000s
            rm_file_or_dir_1484_5158()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - StudioRack Processing and Monitoring - external Server.emo", prog_num=5159) as rm_file_or_dir_1485_5159:  # 0m:0.000s
            rm_file_or_dir_1485_5159()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/MGB MGO REC-PB Standalone.emo", prog_num=5160) as rm_file_or_dir_1486_5160:  # 0m:0.000s
            rm_file_or_dir_1486_5160()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/2x MGB MGO REC-PB 96Khz Standalone.emo", prog_num=5161) as rm_file_or_dir_1487_5161:  # 0m:0.000s
            rm_file_or_dir_1487_5161()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=5162) as shell_command_1488_5162:  # 0m:0.099s
            shell_command_1488_5162()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=5163) as script_command_1489_5163:  # 0m:0.010s
            script_command_1489_5163()
        with ShellCommand(r"echo This installation requires that you restart your computer.", message=r"Restart_required_IID post-install step 1", prog_num=5164) as shell_command_1490_5164:  # 0m:0.010s
            shell_command_1490_5164()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=ScriptCommand(r'echo "#!/bin/bash" >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"; echo installer -pkg \"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg\" -target / >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"; chmod a+rwx "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh" '), if_false=ShellCommand(r'sudo installer -pkg "/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg" -target /', message=r"Installing SoundGrid Driver V14.12", ignore_all_errors=True), prog_num=5165) as if_1491_5165:  # 0m:0.010s
            if_1491_5165()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudioModulesFolder_ScanView.txt", prog_num=5166) as rm_file_or_dir_1492_5166:  # 0m:0.001s
            rm_file_or_dir_1492_5166()
        with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/SampleTestConverter.bundle", prog_num=5167) as rm_file_or_dir_1493_5167:  # 0m:0.000s
            rm_file_or_dir_1493_5167()
        with ShellCommand(r"""osascript -e 'tell application "System Events" to delete login item "SoundGrid Studio"' """, ignore_all_errors=True, prog_num=5168) as shell_command_1494_5168:  # 0m:0.107s
            shell_command_1494_5168()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.NoSplashScreen.sh", prog_num=5169) as rm_file_or_dir_1495_5169:  # 0m:0.000s
            rm_file_or_dir_1495_5169()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGridStudioSilent.app", prog_num=5170) as rm_file_or_dir_1496_5170:  # 0m:0.000s
            rm_file_or_dir_1496_5170()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/SoundGridStudioSilent.app", prog_num=5171) as rm_file_or_dir_1497_5171:  # 0m:0.000s
            rm_file_or_dir_1497_5171()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=5172) as rm_file_or_dir_1498_5172:  # 0m:0.000s
            rm_file_or_dir_1498_5172()
        with ShellCommand(r'chmod a=r,u+w "/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=5173) as shell_command_1499_5173:  # 0m:0.007s
            shell_command_1499_5173()
        with If(IsFile(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudio.Mixer SoundGrid.preferences"), if_false=CopyFileToFile(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist", r"${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5174) as if_1500_5174:  # 0m:0.001s
            if_1500_5174()
        with ShellCommand(r'chmod a=r,u+w "${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=5175) as shell_command_1501_5175:  # 0m:0.008s
            shell_command_1501_5175()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid" -c', ignore_all_errors=True, prog_num=5176) as shell_command_1502_5176:  # 0m:0.102s
            shell_command_1502_5176()
        with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid"/Icon?; fi', prog_num=5177) as script_command_1503_5177:  # 0m:0.008s
            script_command_1503_5177()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=5178) as rm_file_or_dir_1504_5178:  # 0m:0.001s
            rm_file_or_dir_1504_5178()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=5179) as touch_1505_5179:  # 0m:0.000s
            touch_1505_5179()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst/Contents/Info.plist", Touch, r"path", prog_num=5180) as glober_1506_5180:  # 0m:0.002s
            glober_1506_5180()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=5181) as glober_1507_5181:  # 0m:0.009s
            glober_1507_5181()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=5182) as glober_1508_5182:  # 0m:0.002s
            glober_1508_5182()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=5183) as glober_1509_5183:  # 0m:0.002s
            glober_1509_5183()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=5184) as glober_1510_5184:  # 0m:0.000s
            glober_1510_5184()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=5185) as shell_command_1511_5185:  # 0m:2.886s
            shell_command_1511_5185()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V14" -c', ignore_all_errors=True, prog_num=5186) as shell_command_1512_5186:  # 0m:0.101s
            shell_command_1512_5186()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V14"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V14"/Icon?; fi', prog_num=5187) as script_command_1513_5187:  # 0m:0.011s
            script_command_1513_5187()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=5188) as if_1514_5188:  # 0m:0.000s
            if_1514_5188()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=5189) as if_1515_5189:  # 0m:0.000s
            if_1515_5189()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=5190) as if_1516_5190:  # 0m:0.000s
            if_1516_5190()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=5191) as if_1517_5191:  # 0m:0.000s
            if_1517_5191()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=5192) as make_dir_1518_5192:  # 0m:0.006s
            make_dir_1518_5192()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=5193) as chmod_1519_5193:  # 0m:0.000s
            chmod_1519_5193()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", prog_num=5194) as make_dir_1520_5194:  # 0m:0.005s
            make_dir_1520_5194()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=5195) as chmod_1521_5195:  # 0m:0.000s
            chmod_1521_5195()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=5196) as chmod_1522_5196:  # 0m:0.000s
            chmod_1522_5196()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=5197) as chmod_1523_5197:  # 0m:0.000s
            chmod_1523_5197()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=5198) as chmod_1524_5198:  # 0m:0.000s
            chmod_1524_5198()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=5199) as shell_command_1525_5199:  # 0m:0.098s
            shell_command_1525_5199()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=5200) as script_command_1526_5200:  # 0m:0.011s
            script_command_1526_5200()
    with Stage(r"post-copy", prog_num=5201):  # 0m:0.029s
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=5202) as make_dir_1527_5202:  # 0m:0.006s
            make_dir_1527_5202()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V14/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=5203) as copy_file_to_file_1528_5203:  # 0m:0.008s
            copy_file_to_file_1528_5203()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5204) as chmod_1529_5204:  # 0m:0.000s
            chmod_1529_5204()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5205) as chmod_1530_5205:  # 0m:0.000s
            chmod_1530_5205()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Library/Application Support/Waves/Central/V14/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=5206) as copy_file_to_file_1531_5206:  # 0m:0.006s
            copy_file_to_file_1531_5206()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5207) as chmod_1532_5207:  # 0m:0.000s
            chmod_1532_5207()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml", hard_links=False, copy_owner=True, prog_num=5208) as copy_file_to_file_1533_5208:  # 0m:0.008s
            copy_file_to_file_1533_5208()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5209) as chmod_1534_5209:  # 0m:0.000s
            chmod_1534_5209()
        Progress(r"Done copy", prog_num=5210)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=5211)()  # 0m:0.000s
    with Stage(r"post", prog_num=5212):  # 0m:0.033s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=5213) as make_dir_1535_5213:  # 0m:0.005s
            make_dir_1535_5213()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/V14_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=5214) as copy_file_to_file_1536_5214:  # 0m:0.005s
            copy_file_to_file_1536_5214()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=5215) as make_dir_1537_5215:  # 0m:0.005s
            make_dir_1537_5215()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=5216) as copy_file_to_file_1538_5216:  # 0m:0.005s
            copy_file_to_file_1538_5216()
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=5217) as make_dir_1539_5217:  # 0m:0.004s
            make_dir_1539_5217()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Library/Application Support/Waves/Central/V14/index.yaml", hard_links=False, copy_owner=True, prog_num=5218) as copy_file_to_file_1540_5218:  # 0m:0.008s
            copy_file_to_file_1540_5218()

with Stage(r"epilog", prog_num=5219):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416.py", prog_num=5220) as patch_py_batch_with_timings_1541_5220:  # ?
        patch_py_batch_with_timings_1541_5220()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# copy time 0m:24.657s
