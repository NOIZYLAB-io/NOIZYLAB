# Creation time: 15-06-25_16-21
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 5190
PythonBatchCommandBase.running_progress = 878
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=879):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"14-20250615162139"
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
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NDkwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NjAwfX19XX0_;CloudFront-Signature=eEo47m2OwJbNsuelAVRCGSiXKH~nscmDg6~fbF2GY~kLLVG8HbLNFTawibq-Riwrig2sZj0cTel~CxE0Iy8tWQpVivDeL8UbwqgEdlPp9j8xjtghfmV9Va~90e3STS0WgC2s2dLsV3qhIo~CtsOORZset~grRaqdz484ku6I6fawGWi39d3HAKpuCqqghHdleEcDpV-On6y32MDruFqUfwKdAXOywDQd03JsiB7lIRMaGd-WVLWq4Bq~ufJnv4FwBjGF~qwdXfvHaf7rHHOpt~i7rjQeIWdTdKg51uaqaIHKx2kNo0vYVxgahEk9ksVIHU2dyhyJS0yozyee8Xj~wQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NDkwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NjAwfX19XX0_;CloudFront-Signature=eEo47m2OwJbNsuelAVRCGSiXKH~nscmDg6~fbF2GY~kLLVG8HbLNFTawibq-Riwrig2sZj0cTel~CxE0Iy8tWQpVivDeL8UbwqgEdlPp9j8xjtghfmV9Va~90e3STS0WgC2s2dLsV3qhIo~CtsOORZset~grRaqdz484ku6I6fawGWi39d3HAKpuCqqghHdleEcDpV-On6y32MDruFqUfwKdAXOywDQd03JsiB7lIRMaGd-WVLWq4Bq~ufJnv4FwBjGF~qwdXfvHaf7rHHOpt~i7rjQeIWdTdKg51uaqaIHKx2kNo0vYVxgahEk9ksVIHU2dyhyJS0yozyee8Xj~wQ__"
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162139.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml")
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
    config_vars['REQUIRE_REPO_REV'] = 180
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 4307
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162139.log", r"--run")
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
    config_vars['__INVOCATION_RANDOM_ID__'] = r"jdsaksleacoknjvv"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"SG_Studio_V11_8CH_IID", r"StudioRack_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-15 16:21:51.269858"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 1103
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 1
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

with PythonBatchRuntime(r"synccopy", prog_num=880):
    with Stage(r"begin", prog_num=881):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=882):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=883) as copy_file_to_file_001_883:
            copy_file_to_file_001_883()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=884) as copy_file_to_file_002_884:
            copy_file_to_file_002_884()
    with Stage(r"sync", prog_num=885):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=886) as shell_command_003_886:
            shell_command_003_886()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=887) as shell_command_004_887:
            shell_command_004_887()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=888) as shell_command_005_888:
            shell_command_005_888()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=889) as shell_command_006_889:
            shell_command_006_889()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=890) as shell_command_007_890:
            shell_command_007_890()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=891) as shell_command_008_891:
            shell_command_008_891()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V14", prog_num=892):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", chowner=True, prog_num=893) as make_dir_009_893:
                make_dir_009_893()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=894) as cd_010_894:
                cd_010_894()
                Progress(r"2286 files already in cache", own_progress_count=2286, prog_num=3180)()
                with CreateSyncFolders(own_progress_count=4, prog_num=3184) as create_sync_folders_011_3184:
                    create_sync_folders_011_3184()
                Progress(r"Downloading with 50 processes in parallel", prog_num=3185)()
                Progress(r"Downloading with curl parallel", prog_num=3186)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.py_curl/dl-00", total_files_to_download=1, previously_downloaded_files=0, total_bytes_to_download=1103, prog_num=3187, report_own_progress=False) as curl_with_internal_parallel_012_3187:
                    curl_with_internal_parallel_012_3187()
                Progress(r"Downloading 1 file done", prog_num=3188)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=3189) as run_in_thread_013_3189:
                    run_in_thread_013_3189()
                Progress(r"Check checksum ...", prog_num=3190)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, prog_num=3191) as check_download_folder_checksum_014_3191:
                    check_download_folder_checksum_014_3191()
                with Stage(r"post_sync", prog_num=3192):
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14...", prog_num=3193)()
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=3194, recursive=True) as chmod_and_chown_015_3194:
                        chmod_and_chown_015_3194()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=3195) as copy_file_to_file_016_3195:
                        copy_file_to_file_016_3195()
            Progress(r"Done sync", prog_num=3196)()
    with Stage(r"copy", prog_num=3197):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=3198)()
        with Stage(r"create folders", prog_num=3199):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=3200) as make_dir_017_3200:
                make_dir_017_3200()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=3201) as make_dir_018_3201:
                make_dir_018_3201()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=3202) as make_dir_019_3202:
                make_dir_019_3202()
            with MakeDir(r"/Applications/Waves/Data/linux/lib/mkl", chowner=True, prog_num=3203) as make_dir_020_3203:
                make_dir_020_3203()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14", chowner=True, prog_num=3204) as make_dir_021_3204:
                make_dir_021_3204()
            with MakeDir(r"/Applications/Waves/Plug-Ins V14/Documents", chowner=True, prog_num=3205) as make_dir_022_3205:
                make_dir_022_3205()
            with MakeDir(r"/Applications/Waves/SoundGrid", chowner=True, prog_num=3206) as make_dir_023_3206:
                make_dir_023_3206()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio", chowner=True, prog_num=3207) as make_dir_024_3207:
                make_dir_024_3207()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Documents", chowner=True, prog_num=3208) as make_dir_025_3208:
                make_dir_025_3208()
            with MakeDir(r"/Applications/Waves/SoundGrid Studio/Modules", chowner=True, prog_num=3209) as make_dir_026_3209:
                make_dir_026_3209()
            with MakeDir(r"/Applications/Waves/SoundGrid/Documents", chowner=True, prog_num=3210) as make_dir_027_3210:
                make_dir_027_3210()
            with MakeDir(r"/Applications/Waves/SoundGrid/Utilities", chowner=True, prog_num=3211) as make_dir_028_3211:
                make_dir_028_3211()
            with MakeDir(r"/Applications/Waves/WaveShells V14", chowner=True, prog_num=3212) as make_dir_029_3212:
                make_dir_029_3212()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=3213) as make_dir_030_3213:
                make_dir_030_3213()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=3214) as make_dir_031_3214:
                make_dir_031_3214()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode", chowner=True, prog_num=3215) as make_dir_032_3215:
                make_dir_032_3215()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V14", chowner=True, prog_num=3216) as make_dir_033_3216:
                make_dir_033_3216()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=3217) as make_dir_034_3217:
                make_dir_034_3217()
            with MakeDir(r"/Library/Application Support/Waves/MyMon", chowner=True, prog_num=3218) as make_dir_035_3218:
                make_dir_035_3218()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser", chowner=True, prog_num=3219) as make_dir_036_3219:
                make_dir_036_3219()
            with MakeDir(r"/Library/Application Support/Waves/RemoteServices", chowner=True, prog_num=3220) as make_dir_037_3220:
                make_dir_037_3220()
            with MakeDir(r"/Library/Application Support/Waves/Session Converters", chowner=True, prog_num=3221) as make_dir_038_3221:
                make_dir_038_3221()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", chowner=True, prog_num=3222) as make_dir_039_3222:
                make_dir_039_3222()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", chowner=True, prog_num=3223) as make_dir_040_3223:
                make_dir_040_3223()
            with MakeDir(r"/Library/Application Support/Waves/SoundGrid IO Modules", chowner=True, prog_num=3224) as make_dir_041_3224:
                make_dir_041_3224()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=3225) as make_dir_042_3225:
                make_dir_042_3225()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=3226) as make_dir_043_3226:
                make_dir_043_3226()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=3227) as make_dir_044_3227:
                make_dir_044_3227()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=3228) as make_dir_045_3228:
                make_dir_045_3228()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=3229) as make_dir_046_3229:
                make_dir_046_3229()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=3230) as make_dir_047_3230:
                make_dir_047_3230()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=3231) as make_dir_048_3231:
                make_dir_048_3231()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=3232) as make_dir_049_3232:
                make_dir_049_3232()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/History", chowner=True, prog_num=3233) as make_dir_050_3233:
                make_dir_050_3233()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Sessions", chowner=True, prog_num=3234) as make_dir_051_3234:
                make_dir_051_3234()
            with MakeDir(r"/Users/Shared/Waves/SoundGrid Studio/Templates", chowner=True, prog_num=3235) as make_dir_052_3235:
                make_dir_052_3235()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=3236) as make_dir_053_3236:
                make_dir_053_3236()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=3237) as rm_file_or_dir_054_3237:
            rm_file_or_dir_054_3237()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=3238) as shell_command_055_3238:
            shell_command_055_3238()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=3239) as shell_command_056_3239:
            shell_command_056_3239()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=3240) as shell_command_057_3240:
            shell_command_057_3240()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=3241) as shell_command_058_3241:
            shell_command_058_3241()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=3242) as shell_command_059_3242:
            shell_command_059_3242()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=3243) as shell_command_060_3243:
            shell_command_060_3243()
        with ShellCommand(r"""osascript -e 'tell application "SoundGrid Studio" to quit' """, ignore_all_errors=True, prog_num=3244) as shell_command_061_3244:
            shell_command_061_3244()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14", prog_num=3245) as cd_stage_062_3245:
            cd_stage_062_3245()
            with SetExecPermissionsInSyncFolder(prog_num=3246) as set_exec_permissions_in_sync_folder_063_3246:
                set_exec_permissions_in_sync_folder_063_3246()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=3247) as cd_stage_064_3247:
            cd_stage_064_3247()
            with Stage(r"copy", r"StudioRack Data v1.0.0.5", prog_num=3248):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=3249) as should_copy_source_065_3249:
                    should_copy_source_065_3249()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=3250):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=3251) as copy_dir_to_dir_066_3251:
                            copy_dir_to_dir_066_3251()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=3252) as unwtar_067_3252:
                            unwtar_067_3252()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=3253, recursive=True) as chown_068_3253:
                            chown_068_3253()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.1.0", prog_num=3254):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=3255) as should_copy_source_069_3255:
                    should_copy_source_069_3255()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=3256):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=3257) as copy_dir_to_dir_070_3257:
                            copy_dir_to_dir_070_3257()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=3258, recursive=True) as chown_071_3258:
                            chown_071_3258()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=3259) as rm_globs_072_3259:
                rm_globs_072_3259()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=3260) as cd_stage_073_3260:
            cd_stage_073_3260()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=3261):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=3262) as should_copy_source_074_3262:
                    should_copy_source_074_3262()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=3263):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=3264) as copy_dir_to_dir_075_3264:
                            copy_dir_to_dir_075_3264()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=3265, recursive=True) as chown_076_3265:
                            chown_076_3265()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=3266) as should_copy_source_077_3266:
                    should_copy_source_077_3266()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=3267):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=3268) as copy_dir_to_dir_078_3268:
                            copy_dir_to_dir_078_3268()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=3269, recursive=True) as chown_079_3269:
                            chown_079_3269()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/linux/lib/mkl", prog_num=3270) as cd_stage_080_3270:
            cd_stage_080_3270()
            with Stage(r"copy", r"MKL_x32_IID v1.0.0.1", prog_num=3271):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=3272) as should_copy_source_081_3272:
                    should_copy_source_081_3272()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/ia32", prog_num=3273):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", r".", delete_extraneous_files=True, prog_num=3274) as copy_dir_to_dir_082_3274:
                            copy_dir_to_dir_082_3274()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/ia32", where_to_unwtar=r".", prog_num=3275) as unwtar_083_3275:
                            unwtar_083_3275()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/ia32", user_id=-1, group_id=-1, prog_num=3276, recursive=True) as chown_084_3276:
                            chown_084_3276()
            with Stage(r"copy", r"MKL_x64_IID v1.0.0.1", prog_num=3277):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r"/Applications/Waves/Data/linux/lib/mkl", skip_progress_count=4, prog_num=3278) as should_copy_source_085_3278:
                    should_copy_source_085_3278()
                    with Stage(r"copy source", r"Common/Data/linux/lib/mkl/intel64", prog_num=3279):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", r".", delete_extraneous_files=True, prog_num=3280) as copy_dir_to_dir_086_3280:
                            copy_dir_to_dir_086_3280()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Data/linux/lib/mkl/intel64", where_to_unwtar=r".", prog_num=3281) as unwtar_087_3281:
                            unwtar_087_3281()
                        with Chown(path=r"/Applications/Waves/Data/linux/lib/mkl/intel64", user_id=-1, group_id=-1, prog_num=3282, recursive=True) as chown_088_3282:
                            chown_088_3282()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14", prog_num=3283) as cd_stage_089_3283:
            cd_stage_089_3283()
            with Stage(r"copy", r"Insert v14.12.90.381", prog_num=3284):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3285) as should_copy_source_090_3285:
                    should_copy_source_090_3285()
                    with Stage(r"copy source", r"Mac/Plugins/Insert.bundle", prog_num=3286):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", r".", delete_extraneous_files=True, prog_num=3287) as copy_dir_to_dir_091_3287:
                            copy_dir_to_dir_091_3287()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/Insert.bundle", where_to_unwtar=r".", prog_num=3288) as unwtar_092_3288:
                            unwtar_092_3288()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/Insert.bundle", user_id=-1, group_id=-1, prog_num=3289, recursive=True) as chown_093_3289:
                            chown_093_3289()
            with Stage(r"copy", r"StudioRack v14.21.96.552", prog_num=3290):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3291) as should_copy_source_094_3291:
                    should_copy_source_094_3291()
                    with Stage(r"copy source", r"Mac/Plugins/StudioRack.bundle", prog_num=3292):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", r".", delete_extraneous_files=True, prog_num=3293) as copy_dir_to_dir_095_3293:
                            copy_dir_to_dir_095_3293()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/StudioRack.bundle", where_to_unwtar=r".", prog_num=3294) as unwtar_096_3294:
                            unwtar_096_3294()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/StudioRack.bundle", user_id=-1, group_id=-1, prog_num=3295, recursive=True) as chown_097_3295:
                            chown_097_3295()
            with Stage(r"copy", r"WavesLib1_14_12_90_381 v14.12.90.381", prog_num=3296):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3297) as should_copy_source_098_3297:
                    should_copy_source_098_3297()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.12.90.framework", prog_num=3298):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", r".", delete_extraneous_files=True, prog_num=3299) as copy_dir_to_dir_099_3299:
                            copy_dir_to_dir_099_3299()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.12.90.framework", where_to_unwtar=r".", prog_num=3300) as unwtar_100_3300:
                            unwtar_100_3300()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.12.90.framework", user_id=-1, group_id=-1, prog_num=3301, recursive=True) as chown_101_3301:
                            chown_101_3301()
            with Stage(r"copy", r"WavesLib1_14_21_96_552 v14.21.96.552", prog_num=3302):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r"/Applications/Waves/Plug-Ins V14", skip_progress_count=4, prog_num=3303) as should_copy_source_102_3303:
                    should_copy_source_102_3303()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_14.21.96.framework", prog_num=3304):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", r".", delete_extraneous_files=True, prog_num=3305) as copy_dir_to_dir_103_3305:
                            copy_dir_to_dir_103_3305()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Plugins/WavesLib1_14.21.96.framework", where_to_unwtar=r".", prog_num=3306) as unwtar_104_3306:
                            unwtar_104_3306()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V14/WavesLib1_14.21.96.framework", user_id=-1, group_id=-1, prog_num=3307, recursive=True) as chown_105_3307:
                            chown_105_3307()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V14", own_progress_count=4, prog_num=3311) as resolve_symlink_files_in_folder_106_3311:
                resolve_symlink_files_in_folder_106_3311()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V14" -c', ignore_all_errors=True, prog_num=3312) as shell_command_107_3312:
                shell_command_107_3312()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V14"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V14"/Icon?; fi', prog_num=3313) as script_command_108_3313:
                script_command_108_3313()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3314) as shell_command_109_3314:
                shell_command_109_3314()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=3315) as create_symlink_110_3315:
                create_symlink_110_3315()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V14", r"/Applications/Waves/Plug-Ins V14", prog_num=3316) as create_symlink_111_3316:
                create_symlink_111_3316()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=3317) as copy_glob_to_dir_112_3317:
                copy_glob_to_dir_112_3317()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V14/Documents", prog_num=3318) as cd_stage_113_3318:
            cd_stage_113_3318()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=3319):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V14/Documents", skip_progress_count=3, prog_num=3320) as should_copy_source_114_3320:
                    should_copy_source_114_3320()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=3321):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=3322) as copy_file_to_dir_115_3322:
                            copy_file_to_dir_115_3322()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3323) as chmod_and_chown_116_3323:
                            chmod_and_chown_116_3323()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio", prog_num=3324) as cd_stage_117_3324:
            cd_stage_117_3324()
            with Stage(r"copy", r"SoundGrid Studio V11", prog_num=3325):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r"/Applications/Waves/SoundGrid Studio", skip_progress_count=4, prog_num=3326) as should_copy_source_118_3326:
                    should_copy_source_118_3326()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", prog_num=3327):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", r".", delete_extraneous_files=True, prog_num=3328) as copy_dir_to_dir_119_3328:
                            copy_dir_to_dir_119_3328()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/SoundGrid Studio.app", where_to_unwtar=r".", prog_num=3329) as unwtar_120_3329:
                            unwtar_120_3329()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app", user_id=-1, group_id=-1, prog_num=3330, recursive=True) as chown_121_3330:
                            chown_121_3330()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio", own_progress_count=4, prog_num=3334) as resolve_symlink_files_in_folder_122_3334:
                resolve_symlink_files_in_folder_122_3334()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=3335) as shell_command_123_3335:
                shell_command_123_3335()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid Studio" -c', ignore_all_errors=True, prog_num=3336) as shell_command_124_3336:
                shell_command_124_3336()
            with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid Studio"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid Studio"/Icon?; fi', prog_num=3337) as script_command_125_3337:
                script_command_125_3337()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3338) as shell_command_126_3338:
                shell_command_126_3338()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=3339) as cd_stage_127_3339:
            cd_stage_127_3339()
            with Stage(r"copy", r"SoundGrid Studio Documents", prog_num=3340):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=3, prog_num=3341) as should_copy_source_128_3341:
                    should_copy_source_128_3341()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", prog_num=3342):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=3343) as copy_file_to_dir_129_3343:
                            copy_file_to_dir_129_3343()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3344) as chmod_and_chown_130_3344:
                            chmod_and_chown_130_3344()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=3345) as should_copy_source_131_3345:
                    should_copy_source_131_3345()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4", prog_num=3346):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGS_QUICKSTART.mp4.wtar.aa", where_to_unwtar=r".", prog_num=3347) as unwtar_132_3347:
                            unwtar_132_3347()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf", r"/Applications/Waves/SoundGrid Studio/Documents", skip_progress_count=2, prog_num=3348) as should_copy_source_133_3348:
                    should_copy_source_133_3348()
                    with Stage(r"copy source", r"Common/SoundGrid/Studio/Documents/SGStudio.pdf", prog_num=3349):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Studio/Documents/SGStudio.pdf.wtar.aa", where_to_unwtar=r".", prog_num=3350) as unwtar_134_3350:
                            unwtar_134_3350()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3351) as cd_stage_135_3351:
            cd_stage_135_3351()
            with Stage(r"copy", r"SoundGrid Studio Modules", prog_num=3352):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3353) as should_copy_source_136_3353:
                    should_copy_source_136_3353()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", prog_num=3354):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", r".", delete_extraneous_files=True, prog_num=3355) as copy_dir_to_dir_137_3355:
                            copy_dir_to_dir_137_3355()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoom.bundle", where_to_unwtar=r".", prog_num=3356) as unwtar_138_3356:
                            unwtar_138_3356()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoom.bundle", user_id=-1, group_id=-1, prog_num=3357, recursive=True) as chown_139_3357:
                            chown_139_3357()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3358) as should_copy_source_140_3358:
                    should_copy_source_140_3358()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", prog_num=3359):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3360) as copy_dir_to_dir_141_3360:
                            copy_dir_to_dir_141_3360()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", where_to_unwtar=r".", prog_num=3361) as unwtar_142_3361:
                            unwtar_142_3361()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3362, recursive=True) as chown_143_3362:
                            chown_143_3362()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3363) as should_copy_source_144_3363:
                    should_copy_source_144_3363()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", prog_num=3364):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", r".", delete_extraneous_files=True, prog_num=3365) as copy_dir_to_dir_145_3365:
                            copy_dir_to_dir_145_3365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", where_to_unwtar=r".", prog_num=3366) as unwtar_146_3366:
                            unwtar_146_3366()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", user_id=-1, group_id=-1, prog_num=3367, recursive=True) as chown_147_3367:
                            chown_147_3367()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3368) as should_copy_source_148_3368:
                    should_copy_source_148_3368()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", prog_num=3369):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3370) as copy_dir_to_dir_149_3370:
                            copy_dir_to_dir_149_3370()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=3371) as unwtar_150_3371:
                            unwtar_150_3371()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3372, recursive=True) as chown_151_3372:
                            chown_151_3372()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3373) as should_copy_source_152_3373:
                    should_copy_source_152_3373()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", prog_num=3374):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", r".", delete_extraneous_files=True, prog_num=3375) as copy_dir_to_dir_153_3375:
                            copy_dir_to_dir_153_3375()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MIDICommunication.framework", where_to_unwtar=r".", prog_num=3376) as unwtar_154_3376:
                            unwtar_154_3376()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MIDICommunication.framework", user_id=-1, group_id=-1, prog_num=3377, recursive=True) as chown_155_3377:
                            chown_155_3377()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3378) as should_copy_source_156_3378:
                    should_copy_source_156_3378()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", prog_num=3379):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", r".", delete_extraneous_files=True, prog_num=3380) as copy_dir_to_dir_157_3380:
                            copy_dir_to_dir_157_3380()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/Mackie_Control.bundle", where_to_unwtar=r".", prog_num=3381) as unwtar_158_3381:
                            unwtar_158_3381()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/Mackie_Control.bundle", user_id=-1, group_id=-1, prog_num=3382, recursive=True) as chown_159_3382:
                            chown_159_3382()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3383) as should_copy_source_160_3383:
                    should_copy_source_160_3383()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", prog_num=3384):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", r".", delete_extraneous_files=True, prog_num=3385) as copy_dir_to_dir_161_3385:
                            copy_dir_to_dir_161_3385()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", where_to_unwtar=r".", prog_num=3386) as unwtar_162_3386:
                            unwtar_162_3386()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", user_id=-1, group_id=-1, prog_num=3387, recursive=True) as chown_163_3387:
                            chown_163_3387()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3388) as should_copy_source_164_3388:
                    should_copy_source_164_3388()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", prog_num=3389):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", r".", delete_extraneous_files=True, prog_num=3390) as copy_dir_to_dir_165_3390:
                            copy_dir_to_dir_165_3390()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", where_to_unwtar=r".", prog_num=3391) as unwtar_166_3391:
                            unwtar_166_3391()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", user_id=-1, group_id=-1, prog_num=3392, recursive=True) as chown_167_3392:
                            chown_167_3392()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3393) as should_copy_source_168_3393:
                    should_copy_source_168_3393()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", prog_num=3394):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", r".", delete_extraneous_files=True, prog_num=3395) as copy_dir_to_dir_169_3395:
                            copy_dir_to_dir_169_3395()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGST.bundle", where_to_unwtar=r".", prog_num=3396) as unwtar_170_3396:
                            unwtar_170_3396()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGST.bundle", user_id=-1, group_id=-1, prog_num=3397, recursive=True) as chown_171_3397:
                            chown_171_3397()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3398) as should_copy_source_172_3398:
                    should_copy_source_172_3398()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", prog_num=3399):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", r".", delete_extraneous_files=True, prog_num=3400) as copy_dir_to_dir_173_3400:
                            copy_dir_to_dir_173_3400()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", where_to_unwtar=r".", prog_num=3401) as unwtar_174_3401:
                            unwtar_174_3401()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", user_id=-1, group_id=-1, prog_num=3402, recursive=True) as chown_175_3402:
                            chown_175_3402()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3403) as should_copy_source_176_3403:
                    should_copy_source_176_3403()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", prog_num=3404):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", r".", delete_extraneous_files=True, prog_num=3405) as copy_dir_to_dir_177_3405:
                            copy_dir_to_dir_177_3405()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/StudioRack_Control.bundle", where_to_unwtar=r".", prog_num=3406) as unwtar_178_3406:
                            unwtar_178_3406()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/StudioRack_Control.bundle", user_id=-1, group_id=-1, prog_num=3407, recursive=True) as chown_179_3407:
                            chown_179_3407()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=4, prog_num=3408) as should_copy_source_180_3408:
                    should_copy_source_180_3408()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", prog_num=3409):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", r".", delete_extraneous_files=True, prog_num=3410) as copy_dir_to_dir_181_3410:
                            copy_dir_to_dir_181_3410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", where_to_unwtar=r".", prog_num=3411) as unwtar_182_3411:
                            unwtar_182_3411()
                        with Chown(path=r"/Applications/Waves/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", user_id=-1, group_id=-1, prog_num=3412, recursive=True) as chown_183_3412:
                            chown_183_3412()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r"/Applications/Waves/SoundGrid Studio/Modules", skip_progress_count=3, prog_num=3413) as should_copy_source_184_3413:
                    should_copy_source_184_3413()
                    with Stage(r"copy source", r"Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=3414):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", r".", prog_num=3415) as copy_file_to_dir_185_3415:
                            copy_file_to_dir_185_3415()
                        with ChmodAndChown(path=r"com.WavesAudio.SoundGridStudioSilent.plist", mode="a+rw", user_id=-1, group_id=-1, prog_num=3416) as chmod_and_chown_186_3416:
                            chmod_and_chown_186_3416()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/SoundGrid Studio/Modules", own_progress_count=8, prog_num=3424) as resolve_symlink_files_in_folder_187_3424:
                resolve_symlink_files_in_folder_187_3424()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3425) as shell_command_188_3425:
                shell_command_188_3425()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c', ignore_all_errors=True, prog_num=3426) as shell_command_189_3426:
                shell_command_189_3426()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3427) as create_symlink_190_3427:
                create_symlink_190_3427()
            with CreateSymlink(r"/Users/Shared/Waves/Waves SG Studio Modules", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=3428) as create_symlink_191_3428:
                create_symlink_191_3428()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Documents", prog_num=3429) as cd_stage_192_3429:
            cd_stage_192_3429()
            with Stage(r"copy", r"A-H_M_Documents", prog_num=3430):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3431) as should_copy_source_193_3431:
                    should_copy_source_193_3431()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", prog_num=3432):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/A-H M-Waves User Guide.pdf", r".", prog_num=3433) as copy_file_to_dir_194_3433:
                            copy_file_to_dir_194_3433()
                        with ChmodAndChown(path=r"A-H M-Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3434) as chmod_and_chown_195_3434:
                            chmod_and_chown_195_3434()
            with Stage(r"copy", r"Apogee Symphony pdf", prog_num=3435):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3436) as should_copy_source_196_3436:
                    should_copy_source_196_3436()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", prog_num=3437):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", r".", prog_num=3438) as copy_file_to_dir_197_3438:
                            copy_file_to_dir_197_3438()
                        with ChmodAndChown(path=r"Apogee Symphony MKII SoundGrid User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3439) as chmod_and_chown_198_3439:
                            chmod_and_chown_198_3439()
            with Stage(r"copy", r"SG BR1 pdf", prog_num=3440):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3441) as should_copy_source_199_3441:
                    should_copy_source_199_3441()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG BR1.pdf", prog_num=3442):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG BR1.pdf", r".", prog_num=3443) as copy_file_to_dir_200_3443:
                            copy_file_to_dir_200_3443()
                        with ChmodAndChown(path=r"SG BR1.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3444) as chmod_and_chown_201_3444:
                            chmod_and_chown_201_3444()
            with Stage(r"copy", r"Burl BMB4 pdf", prog_num=3445):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3446) as should_copy_source_202_3446:
                    should_copy_source_202_3446()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", prog_num=3447):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", r".", prog_num=3448) as copy_file_to_dir_203_3448:
                            copy_file_to_dir_203_3448()
                        with ChmodAndChown(path=r"Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3449) as chmod_and_chown_204_3449:
                            chmod_and_chown_204_3449()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3450) as should_copy_source_205_3450:
                    should_copy_source_205_3450()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", prog_num=3451):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", r".", prog_num=3452) as copy_file_to_dir_206_3452:
                            copy_file_to_dir_206_3452()
                        with ChmodAndChown(path=r"Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3453) as chmod_and_chown_207_3453:
                            chmod_and_chown_207_3453()
            with Stage(r"copy", r"Cadac pdf", prog_num=3454):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3455) as should_copy_source_208_3455:
                    should_copy_source_208_3455()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Cadac SG User Guide.pdf", prog_num=3456):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Cadac SG User Guide.pdf", r".", prog_num=3457) as copy_file_to_dir_209_3457:
                            copy_file_to_dir_209_3457()
                        with ChmodAndChown(path=r"Cadac SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3458) as chmod_and_chown_210_3458:
                            chmod_and_chown_210_3458()
            with Stage(r"copy", r"Calrec pdf", prog_num=3459):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3460) as should_copy_source_211_3460:
                    should_copy_source_211_3460()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", prog_num=3461):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", r".", prog_num=3462) as copy_file_to_dir_212_3462:
                            copy_file_to_dir_212_3462()
                        with ChmodAndChown(path=r"Calrec SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3463) as chmod_and_chown_213_3463:
                            chmod_and_chown_213_3463()
            with Stage(r"copy", r"Crest Tactus pdf", prog_num=3464):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3465) as should_copy_source_214_3465:
                    should_copy_source_214_3465()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus FOH OM.pdf", prog_num=3466):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus FOH OM.pdf", r".", prog_num=3467) as copy_file_to_dir_215_3467:
                            copy_file_to_dir_215_3467()
                        with ChmodAndChown(path=r"Tactus FOH OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3468) as chmod_and_chown_216_3468:
                            chmod_and_chown_216_3468()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3469) as should_copy_source_217_3469:
                    should_copy_source_217_3469()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Tactus Stage OM.pdf", prog_num=3470):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Tactus Stage OM.pdf", r".", prog_num=3471) as copy_file_to_dir_218_3471:
                            copy_file_to_dir_218_3471()
                        with ChmodAndChown(path=r"Tactus Stage OM.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3472) as chmod_and_chown_219_3472:
                            chmod_and_chown_219_3472()
            with Stage(r"copy", r"DLI DLS pdf", prog_num=3473):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=2, prog_num=3474) as should_copy_source_220_3474:
                    should_copy_source_220_3474()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DLI DLS User Guide.pdf", prog_num=3475):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DLI DLS User Guide.pdf.wtar.aa", where_to_unwtar=r".", prog_num=3476) as unwtar_221_3476:
                            unwtar_221_3476()
            with Stage(r"copy", r"DMI Waves pdf", prog_num=3477):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3478) as should_copy_source_222_3478:
                    should_copy_source_222_3478()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DMI Waves User Guide.pdf", prog_num=3479):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DMI Waves User Guide.pdf", r".", prog_num=3480) as copy_file_to_dir_223_3480:
                            copy_file_to_dir_223_3480()
                        with ChmodAndChown(path=r"DMI Waves User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3481) as chmod_and_chown_224_3481:
                            chmod_and_chown_224_3481()
            with Stage(r"copy", r"DN32-WSG pdf", prog_num=3482):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3483) as should_copy_source_225_3483:
                    should_copy_source_225_3483()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", prog_num=3484):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", r".", prog_num=3485) as copy_file_to_dir_226_3485:
                            copy_file_to_dir_226_3485()
                        with ChmodAndChown(path=r"DN32-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3486) as chmod_and_chown_227_3486:
                            chmod_and_chown_227_3486()
            with Stage(r"copy", r"DSPro SG4000 pdf", prog_num=3487):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3488) as should_copy_source_228_3488:
                    should_copy_source_228_3488()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", prog_num=3489):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", r".", prog_num=3490) as copy_file_to_dir_229_3490:
                            copy_file_to_dir_229_3490()
                        with ChmodAndChown(path=r"STAGEGRID 1000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3491) as chmod_and_chown_230_3491:
                            chmod_and_chown_230_3491()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3492) as should_copy_source_231_3492:
                    should_copy_source_231_3492()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", prog_num=3493):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", r".", prog_num=3494) as copy_file_to_dir_232_3494:
                            copy_file_to_dir_232_3494()
                        with ChmodAndChown(path=r"STAGEGRID 4000 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3495) as chmod_and_chown_233_3495:
                            chmod_and_chown_233_3495()
            with Stage(r"copy", r"DiGiGrid D Driver pdf", prog_num=3496):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3497) as should_copy_source_234_3497:
                    should_copy_source_234_3497()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", prog_num=3498):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid D User Guide.pdf", r".", prog_num=3499) as copy_file_to_dir_235_3499:
                            copy_file_to_dir_235_3499()
                        with ChmodAndChown(path=r"DiGiGrid D User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3500) as chmod_and_chown_236_3500:
                            chmod_and_chown_236_3500()
            with Stage(r"copy", r"DiGiGrid M Driver pdf", prog_num=3501):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3502) as should_copy_source_237_3502:
                    should_copy_source_237_3502()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", prog_num=3503):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid M User Guide.pdf", r".", prog_num=3504) as copy_file_to_dir_238_3504:
                            copy_file_to_dir_238_3504()
                        with ChmodAndChown(path=r"DiGiGrid M User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3505) as chmod_and_chown_239_3505:
                            chmod_and_chown_239_3505()
            with Stage(r"copy", r"DiGiGrid Q Driver pdf", prog_num=3506):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3507) as should_copy_source_240_3507:
                    should_copy_source_240_3507()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", prog_num=3508):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", r".", prog_num=3509) as copy_file_to_dir_241_3509:
                            copy_file_to_dir_241_3509()
                        with ChmodAndChown(path=r"DiGiGrid Q User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3510) as chmod_and_chown_242_3510:
                            chmod_and_chown_242_3510()
            with Stage(r"copy", r"DigiGrid S", prog_num=3511):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3512) as should_copy_source_243_3512:
                    should_copy_source_243_3512()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", prog_num=3513):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid S User Guide.pdf", r".", prog_num=3514) as copy_file_to_dir_244_3514:
                            copy_file_to_dir_244_3514()
                        with ChmodAndChown(path=r"DiGiGrid S User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3515) as chmod_and_chown_245_3515:
                            chmod_and_chown_245_3515()
            with Stage(r"copy", r"Digico SD card pdf", prog_num=3516):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3517) as should_copy_source_246_3517:
                    should_copy_source_246_3517()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", prog_num=3518):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", r".", prog_num=3519) as copy_file_to_dir_247_3519:
                            copy_file_to_dir_247_3519()
                        with ChmodAndChown(path=r"DiGiCo SD SoundGrid IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3520) as chmod_and_chown_248_3520:
                            chmod_and_chown_248_3520()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid IO Driver", prog_num=3521):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3522) as should_copy_source_249_3522:
                    should_copy_source_249_3522()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", prog_num=3523):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", r".", prog_num=3524) as copy_file_to_dir_250_3524:
                            copy_file_to_dir_250_3524()
                        with ChmodAndChown(path=r"DirectOut Exbox.SG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3525) as chmod_and_chown_251_3525:
                            chmod_and_chown_251_3525()
            with Stage(r"copy", r"DirectOut SG.MADI pdf", prog_num=3526):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3527) as should_copy_source_252_3527:
                    should_copy_source_252_3527()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", prog_num=3528):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", r".", prog_num=3529) as copy_file_to_dir_253_3529:
                            copy_file_to_dir_253_3529()
                        with ChmodAndChown(path=r"DirectOut SG.MADI User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3530) as chmod_and_chown_254_3530:
                            chmod_and_chown_254_3530()
            with Stage(r"copy", r"DirectOut SoundGrid IO Driver Documents", prog_num=3531):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3532) as should_copy_source_255_3532:
                    should_copy_source_255_3532()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", prog_num=3533):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", r".", prog_num=3534) as copy_file_to_dir_256_3534:
                            copy_file_to_dir_256_3534()
                        with ChmodAndChown(path=r"DirectOut SG.IO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3535) as chmod_and_chown_257_3535:
                            chmod_and_chown_257_3535()
            with Stage(r"copy", r"Hear Back pdf", prog_num=3536):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3537) as should_copy_source_258_3537:
                    should_copy_source_258_3537()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", prog_num=3538):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", r".", prog_num=3539) as copy_file_to_dir_259_3539:
                            copy_file_to_dir_259_3539()
                        with ChmodAndChown(path=r"Hear Back PRO SG Card User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3540) as chmod_and_chown_260_3540:
                            chmod_and_chown_260_3540()
            with Stage(r"copy", r"HearTech pdf", prog_num=3541):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3542) as should_copy_source_261_3542:
                    should_copy_source_261_3542()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", prog_num=3543):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", r".", prog_num=3544) as copy_file_to_dir_262_3544:
                            copy_file_to_dir_262_3544()
                        with ChmodAndChown(path=r"Hear Technologies SoundGrid Bridge User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3545) as chmod_and_chown_263_3545:
                            chmod_and_chown_263_3545()
            with Stage(r"copy", r"IOC pdf", prog_num=3546):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3547) as should_copy_source_264_3547:
                    should_copy_source_264_3547()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOC User Guide.pdf", prog_num=3548):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOC User Guide.pdf", r".", prog_num=3549) as copy_file_to_dir_265_3549:
                            copy_file_to_dir_265_3549()
                        with ChmodAndChown(path=r"IOC User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3550) as chmod_and_chown_266_3550:
                            chmod_and_chown_266_3550()
            with Stage(r"copy", r"IONIC pdf", prog_num=3551):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3552) as should_copy_source_267_3552:
                    should_copy_source_267_3552()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", prog_num=3553):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IONIC 16 User Guide.pdf", r".", prog_num=3554) as copy_file_to_dir_268_3554:
                            copy_file_to_dir_268_3554()
                        with ChmodAndChown(path=r"IONIC 16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3555) as chmod_and_chown_269_3555:
                            chmod_and_chown_269_3555()
            with Stage(r"copy", r"IOS pdf", prog_num=3556):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3557) as should_copy_source_270_3557:
                    should_copy_source_270_3557()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS User Guide.pdf", prog_num=3558):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS User Guide.pdf", r".", prog_num=3559) as copy_file_to_dir_271_3559:
                            copy_file_to_dir_271_3559()
                        with ChmodAndChown(path=r"IOS User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3560) as chmod_and_chown_272_3560:
                            chmod_and_chown_272_3560()
            with Stage(r"copy", r"IOS-XL pdf", prog_num=3561):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3562) as should_copy_source_273_3562:
                    should_copy_source_273_3562()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOS-XL User Guide.pdf", prog_num=3563):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOS-XL User Guide.pdf", r".", prog_num=3564) as copy_file_to_dir_274_3564:
                            copy_file_to_dir_274_3564()
                        with ChmodAndChown(path=r"IOS-XL User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3565) as chmod_and_chown_275_3565:
                            chmod_and_chown_275_3565()
            with Stage(r"copy", r"IOX pdf", prog_num=3566):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3567) as should_copy_source_276_3567:
                    should_copy_source_276_3567()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/IOX User Guide.pdf", prog_num=3568):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/IOX User Guide.pdf", r".", prog_num=3569) as copy_file_to_dir_277_3569:
                            copy_file_to_dir_277_3569()
                        with ChmodAndChown(path=r"IOX User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3570) as chmod_and_chown_278_3570:
                            chmod_and_chown_278_3570()
            with Stage(r"copy", r"JoeCo BBSG24MP pdf", prog_num=3571):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3572) as should_copy_source_279_3572:
                    should_copy_source_279_3572()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", prog_num=3573):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", r".", prog_num=3574) as copy_file_to_dir_280_3574:
                            copy_file_to_dir_280_3574()
                        with ChmodAndChown(path=r"JoeCo BBSG24MP User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3575) as chmod_and_chown_281_3575:
                            chmod_and_chown_281_3575()
            with Stage(r"copy", r"MGB MGO pdf", prog_num=3576):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3577) as should_copy_source_282_3577:
                    should_copy_source_282_3577()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", prog_num=3578):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", r".", prog_num=3579) as copy_file_to_dir_283_3579:
                            copy_file_to_dir_283_3579()
                        with ChmodAndChown(path=r"DiGiGrid MGR User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3580) as chmod_and_chown_284_3580:
                            chmod_and_chown_284_3580()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3581) as should_copy_source_285_3581:
                    should_copy_source_285_3581()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/MGB MGO User Guide.pdf", prog_num=3582):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/MGB MGO User Guide.pdf", r".", prog_num=3583) as copy_file_to_dir_286_3583:
                            copy_file_to_dir_286_3583()
                        with ChmodAndChown(path=r"MGB MGO User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3584) as chmod_and_chown_287_3584:
                            chmod_and_chown_287_3584()
            with Stage(r"copy", r"SG Driver pdf", prog_num=3585):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3586) as should_copy_source_288_3586:
                    should_copy_source_288_3586()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/SG Driver.pdf", prog_num=3587):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/SG Driver.pdf", r".", prog_num=3588) as copy_file_to_dir_289_3588:
                            copy_file_to_dir_289_3588()
                        with ChmodAndChown(path=r"SG Driver.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3589) as chmod_and_chown_290_3589:
                            chmod_and_chown_290_3589()
            with Stage(r"copy", r"SoundStudio STG-2412 pdf", prog_num=3590):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3591) as should_copy_source_291_3591:
                    should_copy_source_291_3591()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-1608 User Guide.pdf", prog_num=3592):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-1608 User Guide.pdf", r".", prog_num=3593) as copy_file_to_dir_292_3593:
                            copy_file_to_dir_292_3593()
                        with ChmodAndChown(path=r"STG-1608 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3594) as chmod_and_chown_293_3594:
                            chmod_and_chown_293_3594()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3595) as should_copy_source_294_3595:
                    should_copy_source_294_3595()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/STG-2412 User Guide.pdf", prog_num=3596):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/STG-2412 User Guide.pdf", r".", prog_num=3597) as copy_file_to_dir_295_3597:
                            copy_file_to_dir_295_3597()
                        with ChmodAndChown(path=r"STG-2412 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3598) as chmod_and_chown_296_3598:
                            chmod_and_chown_296_3598()
            with Stage(r"copy", r"X-WSG pdf", prog_num=3599):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3600) as should_copy_source_297_3600:
                    should_copy_source_297_3600()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", prog_num=3601):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", r".", prog_num=3602) as copy_file_to_dir_298_3602:
                            copy_file_to_dir_298_3602()
                        with ChmodAndChown(path=r"X-WSG Quick Start Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3603) as chmod_and_chown_299_3603:
                            chmod_and_chown_299_3603()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3604) as should_copy_source_300_3604:
                    should_copy_source_300_3604()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/X-WSG User Guide.pdf", prog_num=3605):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/X-WSG User Guide.pdf", r".", prog_num=3606) as copy_file_to_dir_301_3606:
                            copy_file_to_dir_301_3606()
                        with ChmodAndChown(path=r"X-WSG User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3607) as chmod_and_chown_302_3607:
                            chmod_and_chown_302_3607()
            with Stage(r"copy", r"Y-16_Documents", prog_num=3608):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3609) as should_copy_source_303_3609:
                    should_copy_source_303_3609()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", prog_num=3610):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-HY128 User Guide.pdf", r".", prog_num=3611) as copy_file_to_dir_304_3611:
                            copy_file_to_dir_304_3611()
                        with ChmodAndChown(path=r"WSG-HY128 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3612) as chmod_and_chown_305_3612:
                            chmod_and_chown_305_3612()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r"/Applications/Waves/SoundGrid/Documents", skip_progress_count=3, prog_num=3613) as should_copy_source_306_3613:
                    should_copy_source_306_3613()
                    with Stage(r"copy source", r"Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", prog_num=3614):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Documents/WSG-Y16 User Guide.pdf", r".", prog_num=3615) as copy_file_to_dir_307_3615:
                            copy_file_to_dir_307_3615()
                        with ChmodAndChown(path=r"WSG-Y16 User Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=3616) as chmod_and_chown_308_3616:
                            chmod_and_chown_308_3616()
            with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/BMB4 SoundGrid Motherboard User Guide.pdf", prog_num=3617) as rm_file_or_dir_309_3617:
                rm_file_or_dir_309_3617()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/SoundGrid/Utilities", prog_num=3618) as cd_stage_310_3618:
            cd_stage_310_3618()
            with Stage(r"copy", r"JoeCo BBSG24MP utilities", prog_num=3619):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=3, prog_num=3620) as should_copy_source_311_3620:
                    should_copy_source_311_3620()
                    with Stage(r"copy source", r"Common/SoundGrid/JoeCo", prog_num=3621):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/JoeCo", r".", delete_extraneous_files=True, prog_num=3622) as copy_dir_to_dir_312_3622:
                            copy_dir_to_dir_312_3622()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/JoeCo", user_id=-1, group_id=-1, prog_num=3623, recursive=True) as chown_313_3623:
                            chown_313_3623()
            with Stage(r"copy", r"SoundGrid Control Panel Uninstaller v14.26.48.665", prog_num=3624):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=4, prog_num=3625) as should_copy_source_314_3625:
                    should_copy_source_314_3625()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", prog_num=3626):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", r".", delete_extraneous_files=True, prog_num=3627) as copy_dir_to_dir_315_3627:
                            copy_dir_to_dir_315_3627()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGrid Driver Uninstaller.app", where_to_unwtar=r".", prog_num=3628) as unwtar_316_3628:
                            unwtar_316_3628()
                        with Chown(path=r"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app", user_id=-1, group_id=-1, prog_num=3629, recursive=True) as chown_317_3629:
                            chown_317_3629()
            with Stage(r"copy", r"SoundGrid V14 ASIO / Core Audio Rec/PB Control Panel v14.26.48.665", prog_num=3630):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", r"/Applications/Waves/SoundGrid/Utilities", skip_progress_count=2, prog_num=3631) as should_copy_source_318_3631:
                    should_copy_source_318_3631()
                    with Stage(r"copy source", r"Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg", prog_num=3632):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/Drivers/SoundGridDriverV14.12.pkg.wtar.aa", where_to_unwtar=r".", prog_num=3633) as unwtar_319_3633:
                            unwtar_319_3633()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V14", prog_num=3634) as cd_stage_320_3634:
            cd_stage_320_3634()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=3635):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3636) as should_copy_source_321_3636:
                    should_copy_source_321_3636()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=3637):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=3638) as copy_dir_to_dir_322_3638:
                            copy_dir_to_dir_322_3638()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=3639) as unwtar_323_3639:
                            unwtar_323_3639()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=3640, recursive=True) as chown_324_3640:
                            chown_324_3640()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=3641) as shell_command_325_3641:
                            shell_command_325_3641()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=3642):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3643) as should_copy_source_326_3643:
                    should_copy_source_326_3643()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=3644):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=3645) as copy_dir_to_dir_327_3645:
                            copy_dir_to_dir_327_3645()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=3646) as unwtar_328_3646:
                            unwtar_328_3646()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=3647, recursive=True) as chown_329_3647:
                            chown_329_3647()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=3648) as shell_command_330_3648:
                            shell_command_330_3648()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=3649):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3650) as should_copy_source_331_3650:
                    should_copy_source_331_3650()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=3651):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=3652) as copy_dir_to_dir_332_3652:
                            copy_dir_to_dir_332_3652()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=3653) as unwtar_333_3653:
                            unwtar_333_3653()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=3654, recursive=True) as chown_334_3654:
                            chown_334_3654()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=3655) as shell_command_335_3655:
                            shell_command_335_3655()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=3656):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=3657) as should_copy_source_336_3657:
                    should_copy_source_336_3657()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=3658):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=3659) as copy_dir_to_dir_337_3659:
                            copy_dir_to_dir_337_3659()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=3660) as unwtar_338_3660:
                            unwtar_338_3660()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=3661, recursive=True) as chown_339_3661:
                            chown_339_3661()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=3662) as break_hard_link_340_3662:
                            break_hard_link_340_3662()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=3663) as shell_command_341_3663:
                            shell_command_341_3663()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=3664, recursive=True) as chown_342_3664:
                            chown_342_3664()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=3665, recursive=True) as chmod_343_3665:
                            chmod_343_3665()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=3666):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Applications/Waves/WaveShells V14", skip_progress_count=8, prog_num=3667) as should_copy_source_344_3667:
                    should_copy_source_344_3667()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=3668):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=3669) as copy_dir_to_dir_345_3669:
                            copy_dir_to_dir_345_3669()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=3670) as unwtar_346_3670:
                            unwtar_346_3670()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=3671, recursive=True) as chown_347_3671:
                            chown_347_3671()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=3672) as break_hard_link_348_3672:
                            break_hard_link_348_3672()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=3673) as shell_command_349_3673:
                            shell_command_349_3673()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=3674, recursive=True) as chown_350_3674:
                            chown_350_3674()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=3675, recursive=True) as chmod_351_3675:
                            chmod_351_3675()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=3676):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3677) as should_copy_source_352_3677:
                    should_copy_source_352_3677()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=3678):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=3679) as copy_dir_to_dir_353_3679:
                            copy_dir_to_dir_353_3679()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=3680) as unwtar_354_3680:
                            unwtar_354_3680()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=3681, recursive=True) as chown_355_3681:
                            chown_355_3681()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=3682) as shell_command_356_3682:
                            shell_command_356_3682()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=3683):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3684) as should_copy_source_357_3684:
                    should_copy_source_357_3684()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=3685):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=3686) as copy_dir_to_dir_358_3686:
                            copy_dir_to_dir_358_3686()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=3687) as unwtar_359_3687:
                            unwtar_359_3687()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=3688, recursive=True) as chown_360_3688:
                            chown_360_3688()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=3689) as shell_command_361_3689:
                            shell_command_361_3689()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=3690):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3691) as should_copy_source_362_3691:
                    should_copy_source_362_3691()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=3692):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=3693) as copy_dir_to_dir_363_3693:
                            copy_dir_to_dir_363_3693()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=3694) as unwtar_364_3694:
                            unwtar_364_3694()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=3695, recursive=True) as chown_365_3695:
                            chown_365_3695()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=3696) as shell_command_366_3696:
                            shell_command_366_3696()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=3697):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Applications/Waves/WaveShells V14", skip_progress_count=5, prog_num=3698) as should_copy_source_367_3698:
                    should_copy_source_367_3698()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=3699):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=3700) as copy_dir_to_dir_368_3700:
                            copy_dir_to_dir_368_3700()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=3701) as unwtar_369_3701:
                            unwtar_369_3701()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=3702, recursive=True) as chown_370_3702:
                            chown_370_3702()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=3703) as shell_command_371_3703:
                            shell_command_371_3703()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=3704):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Applications/Waves/WaveShells V14", skip_progress_count=7, prog_num=3705) as should_copy_source_372_3705:
                    should_copy_source_372_3705()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=3706):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=3707) as copy_dir_to_dir_373_3707:
                            copy_dir_to_dir_373_3707()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=3708) as unwtar_374_3708:
                            unwtar_374_3708()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=3709, recursive=True) as chown_375_3709:
                            chown_375_3709()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=3710) as shell_command_376_3710:
                            shell_command_376_3710()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=3711) as script_command_377_3711:
                            script_command_377_3711()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3712) as shell_command_378_3712:
                            shell_command_378_3712()
            with Stage(r"copy", r"WaveShell-AU registration utility v14.12.90.381", prog_num=3713):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r"/Applications/Waves/WaveShells V14", skip_progress_count=4, prog_num=3714) as should_copy_source_379_3714:
                    should_copy_source_379_3714()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 14.app", prog_num=3715):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", r".", delete_extraneous_files=True, prog_num=3716) as copy_dir_to_dir_380_3716:
                            copy_dir_to_dir_380_3716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves AU Reg Utility 14.app", where_to_unwtar=r".", prog_num=3717) as unwtar_381_3717:
                            unwtar_381_3717()
                        with Chown(path=r"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app", user_id=-1, group_id=-1, prog_num=3718, recursive=True) as chown_382_3718:
                            chown_382_3718()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 14.app"', ignore_all_errors=True, prog_num=3719) as shell_command_383_3719:
                shell_command_383_3719()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=3720) as cd_stage_384_3720:
            cd_stage_384_3720()
            with Stage(r"copy", r"WaveShell1-AAX 14.12 v14.12.122.413", prog_num=3721):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=3722) as should_copy_source_385_3722:
                    should_copy_source_385_3722()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", prog_num=3723):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", r".", delete_extraneous_files=True, prog_num=3724) as copy_dir_to_dir_386_3724:
                            copy_dir_to_dir_386_3724()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.12.aaxplugin", where_to_unwtar=r".", prog_num=3725) as unwtar_387_3725:
                            unwtar_387_3725()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.12.aaxplugin", user_id=-1, group_id=-1, prog_num=3726, recursive=True) as chown_388_3726:
                            chown_388_3726()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.12.aaxplugin"', ignore_all_errors=True, prog_num=3727) as shell_command_389_3727:
                            shell_command_389_3727()
            with Stage(r"copy", r"WaveShell1-AAX 14.21 v14.21.96.553", prog_num=3728):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=3729) as should_copy_source_390_3729:
                    should_copy_source_390_3729()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", prog_num=3730):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", r".", delete_extraneous_files=True, prog_num=3731) as copy_dir_to_dir_391_3731:
                            copy_dir_to_dir_391_3731()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AAX 14.21.aaxplugin", where_to_unwtar=r".", prog_num=3732) as unwtar_392_3732:
                            unwtar_392_3732()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.21.aaxplugin", user_id=-1, group_id=-1, prog_num=3733, recursive=True) as chown_393_3733:
                            chown_393_3733()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 14.21.aaxplugin"', ignore_all_errors=True, prog_num=3734) as shell_command_394_3734:
                            shell_command_394_3734()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves", prog_num=3735) as cd_stage_395_3735:
            cd_stage_395_3735()
            with Stage(r"copy", r"Qt libraries 5.12.8", prog_num=3736):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3737) as should_copy_source_396_3737:
                    should_copy_source_396_3737()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.12.8", prog_num=3738):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", r".", delete_extraneous_files=True, prog_num=3739) as copy_dir_to_dir_397_3739:
                            copy_dir_to_dir_397_3739()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.12.8", where_to_unwtar=r".", prog_num=3740) as unwtar_398_3740:
                            unwtar_398_3740()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.12.8", user_id=-1, group_id=-1, prog_num=3741, recursive=True) as chown_399_3741:
                            chown_399_3741()
            with Stage(r"copy", r"QT_5_5_1_FOR_IO_MODULES", prog_num=3742):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3743) as should_copy_source_400_3743:
                    should_copy_source_400_3743()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_5.5.1", prog_num=3744):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", r".", delete_extraneous_files=True, prog_num=3745) as copy_dir_to_dir_401_3745:
                            copy_dir_to_dir_401_3745()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_5.5.1", where_to_unwtar=r".", prog_num=3746) as unwtar_402_3746:
                            unwtar_402_3746()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_5.5.1", user_id=-1, group_id=-1, prog_num=3747, recursive=True) as chown_403_3747:
                            chown_403_3747()
            with Stage(r"copy", r"Qt libraries 6.2.4", prog_num=3748):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r"/Library/Application Support/Waves", skip_progress_count=4, prog_num=3749) as should_copy_source_404_3749:
                    should_copy_source_404_3749()
                    with Stage(r"copy source", r"Mac/Apps/WavesQtLibs_6.2.4", prog_num=3750):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", r".", delete_extraneous_files=True, prog_num=3751) as copy_dir_to_dir_405_3751:
                            copy_dir_to_dir_405_3751()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Apps/WavesQtLibs_6.2.4", where_to_unwtar=r".", prog_num=3752) as unwtar_406_3752:
                            unwtar_406_3752()
                        with Chown(path=r"/Library/Application Support/Waves/WavesQtLibs_6.2.4", user_id=-1, group_id=-1, prog_num=3753, recursive=True) as chown_407_3753:
                            chown_407_3753()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves", own_progress_count=42, prog_num=3795) as resolve_symlink_files_in_folder_408_3795:
                resolve_symlink_files_in_folder_408_3795()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode", prog_num=3796) as cd_stage_409_3796:
            cd_stage_409_3796()
            with Stage(r"copy", r"Demo Mode v1.0", prog_num=3797):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r"/Library/Application Support/Waves/Demo Mode", skip_progress_count=3, prog_num=3798) as should_copy_source_410_3798:
                    should_copy_source_410_3798()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14", prog_num=3799):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14", r".", delete_extraneous_files=True, prog_num=3800) as copy_dir_to_dir_411_3800:
                            copy_dir_to_dir_411_3800()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14", user_id=-1, group_id=-1, prog_num=3801, recursive=True) as chown_412_3801:
                            chown_412_3801()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V14", prog_num=3802) as cd_stage_413_3802:
            cd_stage_413_3802()
            with Stage(r"copy", r"Demo Mode 2.2 v2.2", prog_num=3803):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r"/Library/Application Support/Waves/Demo Mode/V14", skip_progress_count=3, prog_num=3804) as should_copy_source_414_3804:
                    should_copy_source_414_3804()
                    with Stage(r"copy source", r"Mac/Demo Mode/V14/2", prog_num=3805):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Demo Mode/V14/2", r".", delete_extraneous_files=True, prog_num=3806) as copy_dir_to_dir_415_3806:
                            copy_dir_to_dir_415_3806()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V14/2", user_id=-1, group_id=-1, prog_num=3807, recursive=True) as chown_416_3807:
                            chown_416_3807()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=3808) as cd_stage_417_3808:
            cd_stage_417_3808()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=3809) as rm_file_or_dir_418_3809:
                rm_file_or_dir_418_3809()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.2.1.3", prog_num=3810):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=3811) as should_copy_source_419_3811:
                    should_copy_source_419_3811()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=3812):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", r".", delete_extraneous_files=True, prog_num=3813) as copy_dir_to_dir_420_3813:
                            copy_dir_to_dir_420_3813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=3814) as unwtar_421_3814:
                            unwtar_421_3814()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=3815, recursive=True) as chown_422_3815:
                            chown_422_3815()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=3816):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=3817) as should_copy_source_423_3817:
                    should_copy_source_423_3817()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=3818):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=3819) as unwtar_424_3819:
                            unwtar_424_3819()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=3820):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=3821) as should_copy_source_425_3821:
                    should_copy_source_425_3821()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=3822):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=3823) as copy_dir_to_dir_426_3823:
                            copy_dir_to_dir_426_3823()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=3824) as unwtar_427_3824:
                            unwtar_427_3824()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=3825, recursive=True) as chown_428_3825:
                            chown_428_3825()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=3826):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=3827) as should_copy_source_429_3827:
                    should_copy_source_429_3827()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=3828):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=3829) as copy_dir_to_dir_430_3829:
                            copy_dir_to_dir_430_3829()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=3830) as chmod_431_3830:
                            chmod_431_3830()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=3831) as chmod_432_3831:
                            chmod_432_3831()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=3832, recursive=True) as chown_433_3832:
                            chown_433_3832()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=3835) as resolve_symlink_files_in_folder_434_3835:
                resolve_symlink_files_in_folder_434_3835()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3836) as shell_command_435_3836:
                shell_command_435_3836()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/MyMon", prog_num=3837) as cd_stage_436_3837:
            cd_stage_436_3837()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=3838):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/MyMon", skip_progress_count=4, prog_num=3839) as should_copy_source_437_3839:
                    should_copy_source_437_3839()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=3840):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=3841) as copy_dir_to_dir_438_3841:
                            copy_dir_to_dir_438_3841()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=3842) as unwtar_439_3842:
                            unwtar_439_3842()
                        with Chown(path=r"/Library/Application Support/Waves/MyMon/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=3843, recursive=True) as chown_440_3843:
                            chown_440_3843()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3844) as shell_command_441_3844:
                shell_command_441_3844()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser", prog_num=3845) as cd_stage_442_3845:
            cd_stage_442_3845()
            with Stage(r"copy", r"Preset Browser 2.1 v2.1", prog_num=3846):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=3847) as should_copy_source_443_3847:
                    should_copy_source_443_3847()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=3848):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=3849) as copy_dir_to_dir_444_3849:
                            copy_dir_to_dir_444_3849()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=3850, recursive=True) as chown_445_3850:
                            chown_445_3850()
            with Stage(r"copy", r"Preset Browser V14 v1.9", prog_num=3851):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r"/Library/Application Support/Waves/Preset Browser", skip_progress_count=3, prog_num=3852) as should_copy_source_446_3852:
                    should_copy_source_446_3852()
                    with Stage(r"copy source", r"Mac/Preset Browser/V14", prog_num=3853):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Preset Browser/V14", r".", delete_extraneous_files=True, prog_num=3854) as copy_dir_to_dir_447_3854:
                            copy_dir_to_dir_447_3854()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V14", user_id=-1, group_id=-1, prog_num=3855, recursive=True) as chown_448_3855:
                            chown_448_3855()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/RemoteServices", prog_num=3856) as cd_stage_449_3856:
            cd_stage_449_3856()
            with Stage(r"copy", r"MyRemote v14.2.0.112", prog_num=3857):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r"/Library/Application Support/Waves/RemoteServices", skip_progress_count=4, prog_num=3858) as should_copy_source_450_3858:
                    should_copy_source_450_3858()
                    with Stage(r"copy source", r"Mac/SoundGrid/MyMon/MyMonService.bundle", prog_num=3859):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", r".", delete_extraneous_files=True, prog_num=3860) as copy_dir_to_dir_451_3860:
                            copy_dir_to_dir_451_3860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/MyMon/MyMonService.bundle", where_to_unwtar=r".", prog_num=3861) as unwtar_452_3861:
                            unwtar_452_3861()
                        with Chown(path=r"/Library/Application Support/Waves/RemoteServices/MyMonService.bundle", user_id=-1, group_id=-1, prog_num=3862, recursive=True) as chown_453_3862:
                            chown_453_3862()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=3863) as shell_command_454_3863:
                shell_command_454_3863()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Session Converters", prog_num=3864) as cd_stage_455_3864:
            cd_stage_455_3864()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_9_9.bundle", prog_num=3865) as rm_file_or_dir_456_3865:
                rm_file_or_dir_456_3865()
            with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/Converter_2_18.bundle", prog_num=3866) as rm_file_or_dir_457_3866:
                rm_file_or_dir_457_3866()
            with Stage(r"copy", r"Converter", prog_num=3867):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3868) as should_copy_source_458_3868:
                    should_copy_source_458_3868()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", prog_num=3869):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", r".", delete_extraneous_files=True, prog_num=3870) as copy_dir_to_dir_459_3870:
                            copy_dir_to_dir_459_3870()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_2x.bundle", where_to_unwtar=r".", prog_num=3871) as unwtar_460_3871:
                            unwtar_460_3871()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_2x.bundle", user_id=-1, group_id=-1, prog_num=3872, recursive=True) as chown_461_3872:
                            chown_461_3872()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3873) as should_copy_source_462_3873:
                    should_copy_source_462_3873()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", prog_num=3874):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", r".", delete_extraneous_files=True, prog_num=3875) as copy_dir_to_dir_463_3875:
                            copy_dir_to_dir_463_3875()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter_3x.bundle", where_to_unwtar=r".", prog_num=3876) as unwtar_464_3876:
                            unwtar_464_3876()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter_3x.bundle", user_id=-1, group_id=-1, prog_num=3877, recursive=True) as chown_465_3877:
                            chown_465_3877()
            with Stage(r"copy", r"MixerSessionConverter", prog_num=3878):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r"/Library/Application Support/Waves/Session Converters", skip_progress_count=4, prog_num=3879) as should_copy_source_466_3879:
                    should_copy_source_466_3879()
                    with Stage(r"copy source", r"Mac/Mixer/Session Converters/MixerSessionConverter.bundle", prog_num=3880):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", r".", delete_extraneous_files=True, prog_num=3881) as copy_dir_to_dir_467_3881:
                            copy_dir_to_dir_467_3881()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Mixer/Session Converters/MixerSessionConverter.bundle", where_to_unwtar=r".", prog_num=3882) as unwtar_468_3882:
                            unwtar_468_3882()
                        with Chown(path=r"/Library/Application Support/Waves/Session Converters/MixerSessionConverter.bundle", user_id=-1, group_id=-1, prog_num=3883, recursive=True) as chown_469_3883:
                            chown_469_3883()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3884):
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3885) as cd_470_3885:
                cd_470_3885()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=3886)()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGB.wfi", prog_num=3887) as rm_file_471_3887:
                    rm_file_471_3887()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGB.wfi", prog_num=3888) as rm_file_472_3888:
                    rm_file_472_3888()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGB.wfi", prog_num=3889) as rm_file_473_3889:
                    rm_file_473_3889()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGO.wfi", prog_num=3890) as rm_file_474_3890:
                    rm_file_474_3890()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGO.wfi", prog_num=3891) as rm_file_475_3891:
                    rm_file_475_3891()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGO.wfi", prog_num=3892) as rm_file_476_3892:
                    rm_file_476_3892()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridD.wfi", prog_num=3893) as rm_file_477_3893:
                    rm_file_477_3893()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridD.wfi", prog_num=3894) as rm_file_478_3894:
                    rm_file_478_3894()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridD.wfi", prog_num=3895) as rm_file_479_3895:
                    rm_file_479_3895()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridM.wfi", prog_num=3896) as rm_file_480_3896:
                    rm_file_480_3896()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridM.wfi", prog_num=3897) as rm_file_481_3897:
                    rm_file_481_3897()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridM.wfi", prog_num=3898) as rm_file_482_3898:
                    rm_file_482_3898()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridQ.wfi", prog_num=3899) as rm_file_483_3899:
                    rm_file_483_3899()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridQ.wfi", prog_num=3900) as rm_file_484_3900:
                    rm_file_484_3900()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridQ.wfi", prog_num=3901) as rm_file_485_3901:
                    rm_file_485_3901()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLI.wfi", prog_num=3902) as rm_file_486_3902:
                    rm_file_486_3902()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLI.wfi", prog_num=3903) as rm_file_487_3903:
                    rm_file_487_3903()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLI.wfi", prog_num=3904) as rm_file_488_3904:
                    rm_file_488_3904()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLS.wfi", prog_num=3905) as rm_file_489_3905:
                    rm_file_489_3905()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLS.wfi", prog_num=3906) as rm_file_490_3906:
                    rm_file_490_3906()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLS.wfi", prog_num=3907) as rm_file_491_3907:
                    rm_file_491_3907()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s3.wfi", prog_num=3908) as rm_file_492_3908:
                    rm_file_492_3908()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s3.wfi", prog_num=3909) as rm_file_493_3909:
                    rm_file_493_3909()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s3.wfi", prog_num=3910) as rm_file_494_3910:
                    rm_file_494_3910()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s6.wfi", prog_num=3911) as rm_file_495_3911:
                    rm_file_495_3911()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s6.wfi", prog_num=3912) as rm_file_496_3912:
                    rm_file_496_3912()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s6.wfi", prog_num=3913) as rm_file_497_3913:
                    rm_file_497_3913()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_A_H_V3.wfi", prog_num=3914) as rm_file_498_3914:
                    rm_file_498_3914()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_A_H_V3.wfi", prog_num=3915) as rm_file_499_3915:
                    rm_file_499_3915()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_A_H_V3.wfi", prog_num=3916) as rm_file_500_3916:
                    rm_file_500_3916()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_A_H_V3.wfi", prog_num=3917) as rm_file_501_3917:
                    rm_file_501_3917()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_A_H_V3.wfi", prog_num=3918) as rm_file_502_3918:
                    rm_file_502_3918()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.9_A_H_V3.wfi", prog_num=3919) as rm_file_503_3919:
                    rm_file_503_3919()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_sq.wfi", prog_num=3920) as rm_file_504_3920:
                    rm_file_504_3920()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_sq.wfi", prog_num=3921) as rm_file_505_3921:
                    rm_file_505_3921()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_sq.wfi", prog_num=3922) as rm_file_506_3922:
                    rm_file_506_3922()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_X_WSG.wfi", prog_num=3923) as rm_file_507_3923:
                    rm_file_507_3923()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG.wfi", prog_num=3924) as rm_file_508_3924:
                    rm_file_508_3924()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG.wfi", prog_num=3925) as rm_file_509_3925:
                    rm_file_509_3925()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s3.wfi", prog_num=3926) as rm_file_510_3926:
                    rm_file_510_3926()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s3.wfi", prog_num=3927) as rm_file_511_3927:
                    rm_file_511_3927()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s3.wfi", prog_num=3928) as rm_file_512_3928:
                    rm_file_512_3928()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s3.wfi", prog_num=3929) as rm_file_513_3929:
                    rm_file_513_3929()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s6.wfi", prog_num=3930) as rm_file_514_3930:
                    rm_file_514_3930()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s6.wfi", prog_num=3931) as rm_file_515_3931:
                    rm_file_515_3931()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s6.wfi", prog_num=3932) as rm_file_516_3932:
                    rm_file_516_3932()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s6.wfi", prog_num=3933) as rm_file_517_3933:
                    rm_file_517_3933()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Hy.wfi", prog_num=3934) as rm_file_518_3934:
                    rm_file_518_3934()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Hy.wfi", prog_num=3935) as rm_file_519_3935:
                    rm_file_519_3935()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC.wfi", prog_num=3936) as rm_file_520_3936:
                    rm_file_520_3936()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC.wfi", prog_num=3937) as rm_file_521_3937:
                    rm_file_521_3937()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC.wfi", prog_num=3938) as rm_file_522_3938:
                    rm_file_522_3938()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC_micro.wfi", prog_num=3939) as rm_file_523_3939:
                    rm_file_523_3939()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC_micro.wfi", prog_num=3940) as rm_file_524_3940:
                    rm_file_524_3940()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC_micro.wfi", prog_num=3941) as rm_file_525_3941:
                    rm_file_525_3941()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS.wfi", prog_num=3942) as rm_file_526_3942:
                    rm_file_526_3942()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS.wfi", prog_num=3943) as rm_file_527_3943:
                    rm_file_527_3943()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS.wfi", prog_num=3944) as rm_file_528_3944:
                    rm_file_528_3944()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_micro.wfi", prog_num=3945) as rm_file_529_3945:
                    rm_file_529_3945()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_micro.wfi", prog_num=3946) as rm_file_530_3946:
                    rm_file_530_3946()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_micro.wfi", prog_num=3947) as rm_file_531_3947:
                    rm_file_531_3947()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.13_IONIC16_S25.wfi", prog_num=3948) as rm_file_532_3948:
                    rm_file_532_3948()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.22_IONIC16_S25.wfi", prog_num=3949) as rm_file_533_3949:
                    rm_file_533_3949()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL.wfi", prog_num=3950) as rm_file_534_3950:
                    rm_file_534_3950()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL.wfi", prog_num=3951) as rm_file_535_3951:
                    rm_file_535_3951()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL.wfi", prog_num=3952) as rm_file_536_3952:
                    rm_file_536_3952()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL_micro.wfi", prog_num=3953) as rm_file_537_3953:
                    rm_file_537_3953()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL_micro.wfi", prog_num=3954) as rm_file_538_3954:
                    rm_file_538_3954()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL_micro.wfi", prog_num=3955) as rm_file_539_3955:
                    rm_file_539_3955()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX.wfi", prog_num=3956) as rm_file_540_3956:
                    rm_file_540_3956()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX.wfi", prog_num=3957) as rm_file_541_3957:
                    rm_file_541_3957()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX.wfi", prog_num=3958) as rm_file_542_3958:
                    rm_file_542_3958()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX_micro.wfi", prog_num=3959) as rm_file_543_3959:
                    rm_file_543_3959()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX_micro.wfi", prog_num=3960) as rm_file_544_3960:
                    rm_file_544_3960()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX_micro.wfi", prog_num=3961) as rm_file_545_3961:
                    rm_file_545_3961()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Cadac.wfi", prog_num=3962) as rm_file_546_3962:
                    rm_file_546_3962()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Cadac.wfi", prog_num=3963) as rm_file_547_3963:
                    rm_file_547_3963()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Cadac.wfi", prog_num=3964) as rm_file_548_3964:
                    rm_file_548_3964()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex.wfi", prog_num=3965) as rm_file_549_3965:
                    rm_file_549_3965()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex.wfi", prog_num=3966) as rm_file_550_3966:
                    rm_file_550_3966()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex_micro.wfi", prog_num=3967) as rm_file_551_3967:
                    rm_file_551_3967()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex.wfi", prog_num=3968) as rm_file_552_3968:
                    rm_file_552_3968()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex_micro.wfi", prog_num=3969) as rm_file_553_3969:
                    rm_file_553_3969()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex_micro.wfi", prog_num=3970) as rm_file_554_3970:
                    rm_file_554_3970()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Calrec.wfi", prog_num=3971) as rm_file_555_3971:
                    rm_file_555_3971()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Calrec.wfi", prog_num=3972) as rm_file_556_3972:
                    rm_file_556_3972()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Calrec.wfi", prog_num=3973) as rm_file_557_3973:
                    rm_file_557_3973()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH.wfi", prog_num=3974) as rm_file_558_3974:
                    rm_file_558_3974()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB.wfi", prog_num=3975) as rm_file_559_3975:
                    rm_file_559_3975()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH.wfi", prog_num=3976) as rm_file_560_3976:
                    rm_file_560_3976()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB.wfi", prog_num=3977) as rm_file_561_3977:
                    rm_file_561_3977()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH.wfi", prog_num=3978) as rm_file_562_3978:
                    rm_file_562_3978()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB.wfi", prog_num=3979) as rm_file_563_3979:
                    rm_file_563_3979()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH_micro.wfi", prog_num=3980) as rm_file_564_3980:
                    rm_file_564_3980()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB_micro.wfi", prog_num=3981) as rm_file_565_3981:
                    rm_file_565_3981()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH_micro.wfi", prog_num=3982) as rm_file_566_3982:
                    rm_file_566_3982()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB_micro.wfi", prog_num=3983) as rm_file_567_3983:
                    rm_file_567_3983()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH_micro.wfi", prog_num=3984) as rm_file_568_3984:
                    rm_file_568_3984()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB_micro.wfi", prog_num=3985) as rm_file_569_3985:
                    rm_file_569_3985()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiCo_t2_64ch.wfi", prog_num=3986) as rm_file_570_3986:
                    rm_file_570_3986()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_DigiCo_t2_64ch.wfi", prog_num=3987) as rm_file_571_3987:
                    rm_file_571_3987()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiCo_t2_64ch.wfi", prog_num=3988) as rm_file_572_3988:
                    rm_file_572_3988()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiCo_t2_64ch.wfi", prog_num=3989) as rm_file_573_3989:
                    rm_file_573_3989()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Digico_SD_S6.wfi", prog_num=3990) as rm_file_574_3990:
                    rm_file_574_3990()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_Digico_SD_S6.wfi", prog_num=3991) as rm_file_575_3991:
                    rm_file_575_3991()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Digico_SD_S6.wfi", prog_num=3992) as rm_file_576_3992:
                    rm_file_576_3992()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Digico_SD_S6.wfi", prog_num=3993) as rm_file_577_3993:
                    rm_file_577_3993()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.8_Digico_SD_S6.wfi", prog_num=3994) as rm_file_578_3994:
                    rm_file_578_3994()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Digico_SD_S6.wfi", prog_num=3995) as rm_file_579_3995:
                    rm_file_579_3995()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Digico_SD_S6.wfi", prog_num=3996) as rm_file_580_3996:
                    rm_file_580_3996()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigicoDMI.wfi", prog_num=3997) as rm_file_581_3997:
                    rm_file_581_3997()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigicoDMI.wfi", prog_num=3998) as rm_file_582_3998:
                    rm_file_582_3998()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigicoDMI.wfi", prog_num=3999) as rm_file_583_3999:
                    rm_file_583_3999()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigicoDMI.wfi", prog_num=4000) as rm_file_584_4000:
                    rm_file_584_4000()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech.wfi", prog_num=4001) as rm_file_585_4001:
                    rm_file_585_4001()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech.wfi", prog_num=4002) as rm_file_586_4002:
                    rm_file_586_4002()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech.wfi", prog_num=4003) as rm_file_587_4003:
                    rm_file_587_4003()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech.wfi", prog_num=4004) as rm_file_588_4004:
                    rm_file_588_4004()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech_64ch.wfi", prog_num=4005) as rm_file_589_4005:
                    rm_file_589_4005()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech_64ch.wfi", prog_num=4006) as rm_file_590_4006:
                    rm_file_590_4006()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech_64ch.wfi", prog_num=4007) as rm_file_591_4007:
                    rm_file_591_4007()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech_64ch.wfi", prog_num=4008) as rm_file_592_4008:
                    rm_file_592_4008()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.12_Heartech_64ch.wfi", prog_num=4009) as rm_file_593_4009:
                    rm_file_593_4009()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412.wfi", prog_num=4010) as rm_file_594_4010:
                    rm_file_594_4010()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412.wfi", prog_num=4011) as rm_file_595_4011:
                    rm_file_595_4011()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412.wfi", prog_num=4012) as rm_file_596_4012:
                    rm_file_596_4012()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608.wfi", prog_num=4013) as rm_file_597_4013:
                    rm_file_597_4013()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608.wfi", prog_num=4014) as rm_file_598_4014:
                    rm_file_598_4014()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608.wfi", prog_num=4015) as rm_file_599_4015:
                    rm_file_599_4015()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412_micro.wfi", prog_num=4016) as rm_file_600_4016:
                    rm_file_600_4016()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412_micro.wfi", prog_num=4017) as rm_file_601_4017:
                    rm_file_601_4017()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412_micro.wfi", prog_num=4018) as rm_file_602_4018:
                    rm_file_602_4018()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608_micro.wfi", prog_num=4019) as rm_file_603_4019:
                    rm_file_603_4019()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608_micro.wfi", prog_num=4020) as rm_file_604_4020:
                    rm_file_604_4020()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608_micro.wfi", prog_num=4021) as rm_file_605_4021:
                    rm_file_605_4021()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut.wfi", prog_num=4022) as rm_file_606_4022:
                    rm_file_606_4022()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut.wfi", prog_num=4023) as rm_file_607_4023:
                    rm_file_607_4023()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut.wfi", prog_num=4024) as rm_file_608_4024:
                    rm_file_608_4024()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut_micro.wfi", prog_num=4025) as rm_file_609_4025:
                    rm_file_609_4025()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut_micro.wfi", prog_num=4026) as rm_file_610_4026:
                    rm_file_610_4026()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut_micro.wfi", prog_num=4027) as rm_file_611_4027:
                    rm_file_611_4027()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony.wfi", prog_num=4028) as rm_file_612_4028:
                    rm_file_612_4028()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony.wfi", prog_num=4029) as rm_file_613_4029:
                    rm_file_613_4029()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony.wfi", prog_num=4030) as rm_file_614_4030:
                    rm_file_614_4030()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony_micro.wfi", prog_num=4031) as rm_file_615_4031:
                    rm_file_615_4031()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony_micro.wfi", prog_num=4032) as rm_file_616_4032:
                    rm_file_616_4032()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony_micro.wfi", prog_num=4033) as rm_file_617_4033:
                    rm_file_617_4033()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_BurlAudio_Bmb4.wfi", prog_num=4034) as rm_file_618_4034:
                    rm_file_618_4034()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_BurlAudio_Bmb4.wfi", prog_num=4035) as rm_file_619_4035:
                    rm_file_619_4035()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=4036) as rm_file_620_4036:
                    rm_file_620_4036()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro.wfi", prog_num=4037) as rm_file_621_4037:
                    rm_file_621_4037()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro.wfi", prog_num=4038) as rm_file_622_4038:
                    rm_file_622_4038()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro.wfi", prog_num=4039) as rm_file_623_4039:
                    rm_file_623_4039()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro.wfi", prog_num=4040) as rm_file_624_4040:
                    rm_file_624_4040()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k.wfi", prog_num=4041) as rm_file_625_4041:
                    rm_file_625_4041()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k.wfi", prog_num=4042) as rm_file_626_4042:
                    rm_file_626_4042()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k.wfi", prog_num=4043) as rm_file_627_4043:
                    rm_file_627_4043()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k.wfi", prog_num=4044) as rm_file_628_4044:
                    rm_file_628_4044()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k_micro.wfi", prog_num=4045) as rm_file_629_4045:
                    rm_file_629_4045()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k_micro.wfi", prog_num=4046) as rm_file_630_4046:
                    rm_file_630_4046()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k_micro.wfi", prog_num=4047) as rm_file_631_4047:
                    rm_file_631_4047()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k_micro.wfi", prog_num=4048) as rm_file_632_4048:
                    rm_file_632_4048()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_sg1k_micro.wfi", prog_num=4049) as rm_file_633_4049:
                    rm_file_633_4049()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro_micro.wfi", prog_num=4050) as rm_file_634_4050:
                    rm_file_634_4050()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_micro.wfi", prog_num=4051) as rm_file_635_4051:
                    rm_file_635_4051()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_micro.wfi", prog_num=4052) as rm_file_636_4052:
                    rm_file_636_4052()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_micro.wfi", prog_num=4053) as rm_file_637_4053:
                    rm_file_637_4053()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_micro.wfi", prog_num=4054) as rm_file_638_4054:
                    rm_file_638_4054()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_micro.wfi", prog_num=4055) as rm_file_639_4055:
                    rm_file_639_4055()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Joeco.wfi", prog_num=4056) as rm_file_640_4056:
                    rm_file_640_4056()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Joeco.wfi", prog_num=4057) as rm_file_641_4057:
                    rm_file_641_4057()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Joeco.wfi", prog_num=4058) as rm_file_642_4058:
                    rm_file_642_4058()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_10.3_BR1_AVB.wfi", prog_num=4059) as rm_file_643_4059:
                    rm_file_643_4059()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_12.1_BR1_AVB.wfi", prog_num=4060) as rm_file_644_4060:
                    rm_file_644_4060()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_13.4_BR1_AVB.wfi", prog_num=4061) as rm_file_645_4061:
                    rm_file_645_4061()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_X_WSG_DN32.wfi", prog_num=4062) as rm_file_646_4062:
                    rm_file_646_4062()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG_DN32.wfi", prog_num=4063) as rm_file_647_4063:
                    rm_file_647_4063()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG_DN32.wfi", prog_num=4064) as rm_file_648_4064:
                    rm_file_648_4064()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=4065) as cd_stage_649_4065:
            cd_stage_649_4065()
            with Stage(r"copy", r"Allen & Heath M s3 Firmware v13.4.0.205", prog_num=4066):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4067) as should_copy_source_650_4067:
                    should_copy_source_650_4067()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", prog_num=4068):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s3.wfi", r".", prog_num=4069) as copy_file_to_dir_651_4069:
                            copy_file_to_dir_651_4069()
                        with ChmodAndChown(path=r"IO_13.4_AH_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4070) as chmod_and_chown_652_4070:
                            chmod_and_chown_652_4070()
            with Stage(r"copy", r"Allen & Heath M s6 Firmware v13.4.0.205", prog_num=4071):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4072) as should_copy_source_653_4072:
                    should_copy_source_653_4072()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", prog_num=4073):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_s6.wfi", r".", prog_num=4074) as copy_file_to_dir_654_4074:
                            copy_file_to_dir_654_4074()
                        with ChmodAndChown(path=r"IO_13.4_AH_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4075) as chmod_and_chown_655_4075:
                            chmod_and_chown_655_4075()
            with Stage(r"copy", r"Allen & Heath sq Firmware v13.4.0.205", prog_num=4076):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4077) as should_copy_source_656_4077:
                    should_copy_source_656_4077()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", prog_num=4078):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_AH_sq.wfi", r".", prog_num=4079) as copy_file_to_dir_657_4079:
                            copy_file_to_dir_657_4079()
                        with ChmodAndChown(path=r"IO_13.4_AH_sq.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4080) as chmod_and_chown_658_4080:
                            chmod_and_chown_658_4080()
            with Stage(r"copy", r"Allen & Heath M v3 Firmware v14.12.33.324", prog_num=4081):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4082) as should_copy_source_659_4082:
                    should_copy_source_659_4082()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", prog_num=4083):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.12_A_H_V3.wfi", r".", prog_num=4084) as copy_file_to_dir_660_4084:
                            copy_file_to_dir_660_4084()
                        with ChmodAndChown(path=r"IO_14.12_A_H_V3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4085) as chmod_and_chown_661_4085:
                            chmod_and_chown_661_4085()
            with Stage(r"copy", r"Apogee_Symphony_Firmware_13_4 v13.4.0.205", prog_num=4086):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4087) as should_copy_source_662_4087:
                    should_copy_source_662_4087()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi", prog_num=4088):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4089) as unwtar_663_4089:
                            unwtar_663_4089()
            with Stage(r"copy", r"Apogee_Symphony_micro_Firmware_13_4 v13.4.0.205", prog_num=4090):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4091) as should_copy_source_664_4091:
                    should_copy_source_664_4091()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi", prog_num=4092):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Symphony_micro.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4093) as unwtar_665_4093:
                            unwtar_665_4093()
            with Stage(r"copy", r"SoundGrid BR-1 Firmware v13.7.87.375", prog_num=4094):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=2, prog_num=4095) as should_copy_source_666_4095:
                    should_copy_source_666_4095()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi", prog_num=4096):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_BR1_AVB.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4097) as unwtar_667_4097:
                            unwtar_667_4097()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Firmware 14.25 v14.25.21.582", prog_num=4098):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4099) as should_copy_source_668_4099:
                    should_copy_source_668_4099()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", prog_num=4100):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", r".", prog_num=4101) as copy_file_to_dir_669_4101:
                            copy_file_to_dir_669_4101()
                        with ChmodAndChown(path=r"IO_14.25_Behringer_WING_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4102) as chmod_and_chown_670_4102:
                            chmod_and_chown_670_4102()
            with Stage(r"copy", r"Burl Audio BMB4 Firmware v13.4.0.205", prog_num=4103):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4104) as should_copy_source_671_4104:
                    should_copy_source_671_4104()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=4105):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", r".", prog_num=4106) as copy_file_to_dir_672_4106:
                            copy_file_to_dir_672_4106()
                        with ChmodAndChown(path=r"IO_13.4_BurlAudio_Bmb4.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4107) as chmod_and_chown_673_4107:
                            chmod_and_chown_673_4107()
            with Stage(r"copy", r"Cadac_Firmware_13_4 v13.4.0.205", prog_num=4108):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4109) as should_copy_source_674_4109:
                    should_copy_source_674_4109()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", prog_num=4110):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Cadac.wfi", r".", prog_num=4111) as copy_file_to_dir_675_4111:
                            copy_file_to_dir_675_4111()
                        with ChmodAndChown(path=r"IO_13.4_Cadac.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4112) as chmod_and_chown_676_4112:
                            chmod_and_chown_676_4112()
            with Stage(r"copy", r"Calrec_Firmware_13_4 v13.4.0.205", prog_num=4113):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4114) as should_copy_source_677_4114:
                    should_copy_source_677_4114()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", prog_num=4115):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Calrec.wfi", r".", prog_num=4116) as copy_file_to_dir_678_4116:
                            copy_file_to_dir_678_4116()
                        with ChmodAndChown(path=r"IO_13.4_Calrec.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4117) as chmod_and_chown_679_4117:
                            chmod_and_chown_679_4117()
            with Stage(r"copy", r"Crest Audio Tactus Firmware v13.4.0.205", prog_num=4118):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4119) as should_copy_source_680_4119:
                    should_copy_source_680_4119()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", prog_num=4120):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH.wfi", r".", prog_num=4121) as copy_file_to_dir_681_4121:
                            copy_file_to_dir_681_4121()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4122) as chmod_and_chown_682_4122:
                            chmod_and_chown_682_4122()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4123) as should_copy_source_683_4123:
                    should_copy_source_683_4123()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", prog_num=4124):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB.wfi", r".", prog_num=4125) as copy_file_to_dir_684_4125:
                            copy_file_to_dir_684_4125()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4126) as chmod_and_chown_685_4126:
                            chmod_and_chown_685_4126()
            with Stage(r"copy", r"Crest Audio Tactus micro Firmware v13.4.0.205", prog_num=4127):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4128) as should_copy_source_686_4128:
                    should_copy_source_686_4128()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", prog_num=4129):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_FOH_micro.wfi", r".", prog_num=4130) as copy_file_to_dir_687_4130:
                            copy_file_to_dir_687_4130()
                        with ChmodAndChown(path=r"IO_13.4_PV_FOH_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4131) as chmod_and_chown_688_4131:
                            chmod_and_chown_688_4131()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4132) as should_copy_source_689_4132:
                    should_copy_source_689_4132()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", prog_num=4133):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_PV_SB_micro.wfi", r".", prog_num=4134) as copy_file_to_dir_690_4134:
                            copy_file_to_dir_690_4134()
                        with ChmodAndChown(path=r"IO_13.4_PV_SB_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4135) as chmod_and_chown_691_4135:
                            chmod_and_chown_691_4135()
            with Stage(r"copy", r"DigiGrid DLI Firmware v13.4.0.205", prog_num=4136):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4137) as should_copy_source_692_4137:
                    should_copy_source_692_4137()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", prog_num=4138):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", r".", prog_num=4139) as copy_file_to_dir_693_4139:
                            copy_file_to_dir_693_4139()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4140) as chmod_and_chown_694_4140:
                            chmod_and_chown_694_4140()
            with Stage(r"copy", r"DigiGrid DLS Firmware v13.4.0.205", prog_num=4141):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4142) as should_copy_source_695_4142:
                    should_copy_source_695_4142()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", prog_num=4143):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", r".", prog_num=4144) as copy_file_to_dir_696_4144:
                            copy_file_to_dir_696_4144()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_DLS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4145) as chmod_and_chown_697_4145:
                            chmod_and_chown_697_4145()
            with Stage(r"copy", r"DMI_Waves_Firmware_13_7 v13.7.113.401", prog_num=4146):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4147) as should_copy_source_698_4147:
                    should_copy_source_698_4147()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", prog_num=4148):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_DigicoDMI.wfi", r".", prog_num=4149) as copy_file_to_dir_699_4149:
                            copy_file_to_dir_699_4149()
                        with ChmodAndChown(path=r"IO_13.7_DigicoDMI.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4150) as chmod_and_chown_700_4150:
                            chmod_and_chown_700_4150()
            with Stage(r"copy", r"DN32_WSG_Firmware_13_4 v13.4.0.205", prog_num=4151):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4152) as should_copy_source_701_4152:
                    should_copy_source_701_4152()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", prog_num=4153):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG_DN32.wfi", r".", prog_num=4154) as copy_file_to_dir_702_4154:
                            copy_file_to_dir_702_4154()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG_DN32.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4155) as chmod_and_chown_703_4155:
                            chmod_and_chown_703_4155()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_13_6 v13.6.12.288", prog_num=4156):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4157) as should_copy_source_704_4157:
                    should_copy_source_704_4157()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", prog_num=4158):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.6_Dspro_sg1k.wfi", r".", prog_num=4159) as copy_file_to_dir_705_4159:
                            copy_file_to_dir_705_4159()
                        with ChmodAndChown(path=r"IO_13.6_Dspro_sg1k.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4160) as chmod_and_chown_706_4160:
                            chmod_and_chown_706_4160()
            with Stage(r"copy", r"DSPro_SG1000_Firmware_14_25 v14.25.55.616", prog_num=4161):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4162) as should_copy_source_707_4162:
                    should_copy_source_707_4162()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", prog_num=4163):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", r".", prog_num=4164) as copy_file_to_dir_708_4164:
                            copy_file_to_dir_708_4164()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg1k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4165) as chmod_and_chown_709_4165:
                            chmod_and_chown_709_4165()
            with Stage(r"copy", r"DSPro_SG1000_micro_Firmware_15_1 v15.1.2.45", prog_num=4166):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4167) as should_copy_source_710_4167:
                    should_copy_source_710_4167()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", prog_num=4168):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", r".", prog_num=4169) as copy_file_to_dir_711_4169:
                            copy_file_to_dir_711_4169()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4170) as chmod_and_chown_712_4170:
                            chmod_and_chown_712_4170()
            with Stage(r"copy", r"DSPro_SG1000_micro_V2_Firmware_15_1 v15.1.2.45", prog_num=4171):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4172) as should_copy_source_713_4172:
                    should_copy_source_713_4172()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", prog_num=4173):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", r".", prog_num=4174) as copy_file_to_dir_714_4174:
                            copy_file_to_dir_714_4174()
                        with ChmodAndChown(path=r"IO_15.1_Dspro_sg1k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4175) as chmod_and_chown_715_4175:
                            chmod_and_chown_715_4175()
            with Stage(r"copy", r"DSPro SG4000 Firmware v13.5.0.227", prog_num=4176):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4177) as should_copy_source_716_4177:
                    should_copy_source_716_4177()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", prog_num=4178):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.5_Dspro.wfi", r".", prog_num=4179) as copy_file_to_dir_717_4179:
                            copy_file_to_dir_717_4179()
                        with ChmodAndChown(path=r"IO_13.5_Dspro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4180) as chmod_and_chown_718_4180:
                            chmod_and_chown_718_4180()
            with Stage(r"copy", r"DSPro SG4000 v2 Firmware v14.26.30.647", prog_num=4181):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4182) as should_copy_source_719_4182:
                    should_copy_source_719_4182()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", prog_num=4183):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", r".", prog_num=4184) as copy_file_to_dir_720_4184:
                            copy_file_to_dir_720_4184()
                        with ChmodAndChown(path=r"IO_14.26_Dspro_sg4k_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4185) as chmod_and_chown_721_4185:
                            chmod_and_chown_721_4185()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware V14.25 v14.25.55.616", prog_num=4186):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4187) as should_copy_source_722_4187:
                    should_copy_source_722_4187()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", prog_num=4188):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", r".", prog_num=4189) as copy_file_to_dir_723_4189:
                            copy_file_to_dir_723_4189()
                        with ChmodAndChown(path=r"IO_14.25_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4190) as chmod_and_chown_724_4190:
                            chmod_and_chown_724_4190()
            with Stage(r"copy", r"DSPro SG4000 micro Firmware v15.2.25.98", prog_num=4191):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4192) as should_copy_source_725_4192:
                    should_copy_source_725_4192()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", prog_num=4193):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_micro.wfi", r".", prog_num=4194) as copy_file_to_dir_726_4194:
                            copy_file_to_dir_726_4194()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4195) as chmod_and_chown_727_4195:
                            chmod_and_chown_727_4195()
            with Stage(r"copy", r"DSPro SG4000 v2 micro Firmware v15.2.25.98", prog_num=4196):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4197) as should_copy_source_728_4197:
                    should_copy_source_728_4197()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", prog_num=4198):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", r".", prog_num=4199) as copy_file_to_dir_729_4199:
                            copy_file_to_dir_729_4199()
                        with ChmodAndChown(path=r"IO_15.2_Dspro_sg4k_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4200) as chmod_and_chown_730_4200:
                            chmod_and_chown_730_4200()
            with Stage(r"copy", r"DiGiGrid D Firmware V13.4 v13.4.0.205", prog_num=4201):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4202) as should_copy_source_731_4202:
                    should_copy_source_731_4202()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", prog_num=4203):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridD.wfi", r".", prog_num=4204) as copy_file_to_dir_732_4204:
                            copy_file_to_dir_732_4204()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridD.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4205) as chmod_and_chown_733_4205:
                            chmod_and_chown_733_4205()
            with Stage(r"copy", r"DiGiGrid_M_Driver_Firmware_13_4 v13.4.0.205", prog_num=4206):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4207) as should_copy_source_734_4207:
                    should_copy_source_734_4207()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", prog_num=4208):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridM.wfi", r".", prog_num=4209) as copy_file_to_dir_735_4209:
                            copy_file_to_dir_735_4209()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridM.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4210) as chmod_and_chown_736_4210:
                            chmod_and_chown_736_4210()
            with Stage(r"copy", r"DiGiGrid Q Firmware V13.4 v13.4.0.205", prog_num=4211):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4212) as should_copy_source_737_4212:
                    should_copy_source_737_4212()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", prog_num=4213):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiGridQ.wfi", r".", prog_num=4214) as copy_file_to_dir_738_4214:
                            copy_file_to_dir_738_4214()
                        with ChmodAndChown(path=r"IO_13.4_DigiGridQ.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4215) as chmod_and_chown_739_4215:
                            chmod_and_chown_739_4215()
            with Stage(r"copy", r"Digico SD card V13.4 v13.4.0.205", prog_num=4216):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4217) as should_copy_source_740_4217:
                    should_copy_source_740_4217()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", prog_num=4218):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", r".", prog_num=4219) as copy_file_to_dir_741_4219:
                            copy_file_to_dir_741_4219()
                        with ChmodAndChown(path=r"IO_13.4_DigiCo_t2_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4220) as chmod_and_chown_742_4220:
                            chmod_and_chown_742_4220()
            with Stage(r"copy", r"Digico SD Firmware v14.21.36.492", prog_num=4221):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4222) as should_copy_source_743_4222:
                    should_copy_source_743_4222()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", prog_num=4223):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_Digico_SD_S6.wfi", r".", prog_num=4224) as copy_file_to_dir_744_4224:
                            copy_file_to_dir_744_4224()
                        with ChmodAndChown(path=r"IO_14.21_Digico_SD_S6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4225) as chmod_and_chown_745_4225:
                            chmod_and_chown_745_4225()
            with Stage(r"copy", r"DirectOut Exbox Micro SoundGrid I/O Driver Firmware v14.22.9.506", prog_num=4226):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4227) as should_copy_source_746_4227:
                    should_copy_source_746_4227()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", prog_num=4228):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", r".", prog_num=4229) as copy_file_to_dir_747_4229:
                            copy_file_to_dir_747_4229()
                        with ChmodAndChown(path=r"IO_14.22_DirectOut_Ex_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4230) as chmod_and_chown_748_4230:
                            chmod_and_chown_748_4230()
            with Stage(r"copy", r"DirectOut Exbox v2 SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=4231):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4232) as should_copy_source_749_4232:
                    should_copy_source_749_4232()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", prog_num=4233):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", r".", prog_num=4234) as copy_file_to_dir_750_4234:
                            copy_file_to_dir_750_4234()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4235) as chmod_and_chown_751_4235:
                            chmod_and_chown_751_4235()
            with Stage(r"copy", r"DirectOut Exbox v2 Micro SoundGrid I/O Driver Firmware v14.25.3.564", prog_num=4236):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4237) as should_copy_source_752_4237:
                    should_copy_source_752_4237()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", prog_num=4238):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", r".", prog_num=4239) as copy_file_to_dir_753_4239:
                            copy_file_to_dir_753_4239()
                        with ChmodAndChown(path=r"IO_14.25_DirectOut_Ex_v2_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4240) as chmod_and_chown_754_4240:
                            chmod_and_chown_754_4240()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=4241):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4242) as should_copy_source_755_4242:
                    should_copy_source_755_4242()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", prog_num=4243):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_DirectOut_Ex.wfi", r".", prog_num=4244) as copy_file_to_dir_756_4244:
                            copy_file_to_dir_756_4244()
                        with ChmodAndChown(path=r"IO_14.18_DirectOut_Ex.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4245) as chmod_and_chown_757_4245:
                            chmod_and_chown_757_4245()
            with Stage(r"copy", r"DirectOut_SG_MADI_Firmware_13_4 v13.4.0.205", prog_num=4246):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4247) as should_copy_source_758_4247:
                    should_copy_source_758_4247()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", prog_num=4248):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut.wfi", r".", prog_num=4249) as copy_file_to_dir_759_4249:
                            copy_file_to_dir_759_4249()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4250) as chmod_and_chown_760_4250:
                            chmod_and_chown_760_4250()
            with Stage(r"copy", r"DirectOut_SG_MADI_micro_Firmware_13_4 v13.4.0.205", prog_num=4251):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4252) as should_copy_source_761_4252:
                    should_copy_source_761_4252()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", prog_num=4253):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DirectOut_micro.wfi", r".", prog_num=4254) as copy_file_to_dir_762_4254:
                            copy_file_to_dir_762_4254()
                        with ChmodAndChown(path=r"IO_13.4_DirectOut_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4255) as chmod_and_chown_763_4255:
                            chmod_and_chown_763_4255()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Firmware v14.18.25.455", prog_num=4256):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4257) as should_copy_source_764_4257:
                    should_copy_source_764_4257()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", prog_num=4258):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.18_Directout_sgio.wfi", r".", prog_num=4259) as copy_file_to_dir_765_4259:
                            copy_file_to_dir_765_4259()
                        with ChmodAndChown(path=r"IO_14.18_Directout_sgio.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4260) as chmod_and_chown_766_4260:
                            chmod_and_chown_766_4260()
            with Stage(r"copy", r"HearBack Pro Firmware v13.7.33.321", prog_num=4261):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4262) as should_copy_source_767_4262:
                    should_copy_source_767_4262()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", prog_num=4263):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech.wfi", r".", prog_num=4264) as copy_file_to_dir_768_4264:
                            copy_file_to_dir_768_4264()
                        with ChmodAndChown(path=r"IO_13.7_Heartech.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4265) as chmod_and_chown_769_4265:
                            chmod_and_chown_769_4265()
            with Stage(r"copy", r"HearBack Pro V2 Firmware v13.7.118.406", prog_num=4266):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4267) as should_copy_source_770_4267:
                    should_copy_source_770_4267()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", prog_num=4268):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.7_Heartech_32ch.wfi", r".", prog_num=4269) as copy_file_to_dir_771_4269:
                            copy_file_to_dir_771_4269()
                        with ChmodAndChown(path=r"IO_13.7_Heartech_32ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4270) as chmod_and_chown_772_4270:
                            chmod_and_chown_772_4270()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v15.1.29.72", prog_num=4271):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4272) as should_copy_source_773_4272:
                    should_copy_source_773_4272()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", prog_num=4273):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch.wfi", r".", prog_num=4274) as copy_file_to_dir_774_4274:
                            copy_file_to_dir_774_4274()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4275) as chmod_and_chown_775_4275:
                            chmod_and_chown_775_4275()
            with Stage(r"copy", r"HearTech SG Bridge Firmware v2 v15.1.29.72", prog_num=4276):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4277) as should_copy_source_776_4277:
                    should_copy_source_776_4277()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", prog_num=4278):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", r".", prog_num=4279) as copy_file_to_dir_777_4279:
                            copy_file_to_dir_777_4279()
                        with ChmodAndChown(path=r"IO_15.1_Heartech_64ch_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4280) as chmod_and_chown_778_4280:
                            chmod_and_chown_778_4280()
            with Stage(r"copy", r"DigiGrid IOC Firmware v13.4.0.205", prog_num=4281):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4282) as should_copy_source_779_4282:
                    should_copy_source_779_4282()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", prog_num=4283):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", r".", prog_num=4284) as copy_file_to_dir_780_4284:
                            copy_file_to_dir_780_4284()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4285) as chmod_and_chown_781_4285:
                            chmod_and_chown_781_4285()
            with Stage(r"copy", r"DigiGrid IOC micro Firmware v13.4.0.205", prog_num=4286):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4287) as should_copy_source_782_4287:
                    should_copy_source_782_4287()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", prog_num=4288):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", r".", prog_num=4289) as copy_file_to_dir_783_4289:
                            copy_file_to_dir_783_4289()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOC_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4290) as chmod_and_chown_784_4290:
                            chmod_and_chown_784_4290()
            with Stage(r"copy", r"IONIC16_Firmware_S25 v14.29.19.700", prog_num=4291):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4292) as should_copy_source_785_4292:
                    should_copy_source_785_4292()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", prog_num=4293):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.29_IONIC16_S25.wfi", r".", prog_num=4294) as copy_file_to_dir_786_4294:
                            copy_file_to_dir_786_4294()
                        with ChmodAndChown(path=r"IO_14.29_IONIC16_S25.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4295) as chmod_and_chown_787_4295:
                            chmod_and_chown_787_4295()
            with Stage(r"copy", r"IONIC16_Firmware_S50 v14.30.5.713", prog_num=4296):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4297) as should_copy_source_788_4297:
                    should_copy_source_788_4297()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", prog_num=4298):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.30_IONIC16_S50.wfi", r".", prog_num=4299) as copy_file_to_dir_789_4299:
                            copy_file_to_dir_789_4299()
                        with ChmodAndChown(path=r"IO_14.30_IONIC16_S50.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4300) as chmod_and_chown_790_4300:
                            chmod_and_chown_790_4300()
            with Stage(r"copy", r"DigiGrid IOS Firmware v13.4.0.205", prog_num=4301):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4302) as should_copy_source_791_4302:
                    should_copy_source_791_4302()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", prog_num=4303):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", r".", prog_num=4304) as copy_file_to_dir_792_4304:
                            copy_file_to_dir_792_4304()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4305) as chmod_and_chown_793_4305:
                            chmod_and_chown_793_4305()
            with Stage(r"copy", r"DigiGrid IOS-XL Firmware v13.4.0.205", prog_num=4306):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4307) as should_copy_source_794_4307:
                    should_copy_source_794_4307()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", prog_num=4308):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", r".", prog_num=4309) as copy_file_to_dir_795_4309:
                            copy_file_to_dir_795_4309()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4310) as chmod_and_chown_796_4310:
                            chmod_and_chown_796_4310()
            with Stage(r"copy", r"DigiGrid IOS-XL micro Firmware v13.4.0.205", prog_num=4311):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4312) as should_copy_source_797_4312:
                    should_copy_source_797_4312()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", prog_num=4313):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", r".", prog_num=4314) as copy_file_to_dir_798_4314:
                            copy_file_to_dir_798_4314()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_XL_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4315) as chmod_and_chown_799_4315:
                            chmod_and_chown_799_4315()
            with Stage(r"copy", r"DigiGrid IOS micro Firmware v13.4.0.205", prog_num=4316):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4317) as should_copy_source_800_4317:
                    should_copy_source_800_4317()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", prog_num=4318):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", r".", prog_num=4319) as copy_file_to_dir_801_4319:
                            copy_file_to_dir_801_4319()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOS_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4320) as chmod_and_chown_802_4320:
                            chmod_and_chown_802_4320()
            with Stage(r"copy", r"DigiGrid IOX Firmware v13.4.0.205", prog_num=4321):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4322) as should_copy_source_803_4322:
                    should_copy_source_803_4322()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", prog_num=4323):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", r".", prog_num=4324) as copy_file_to_dir_804_4324:
                            copy_file_to_dir_804_4324()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4325) as chmod_and_chown_805_4325:
                            chmod_and_chown_805_4325()
            with Stage(r"copy", r"DigiGrid IOX micro Firmware v13.4.0.205", prog_num=4326):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4327) as should_copy_source_806_4327:
                    should_copy_source_806_4327()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", prog_num=4328):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", r".", prog_num=4329) as copy_file_to_dir_807_4329:
                            copy_file_to_dir_807_4329()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_IOX_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4330) as chmod_and_chown_808_4330:
                            chmod_and_chown_808_4330()
            with Stage(r"copy", r"JoeCo_Firmware_13_4 v13.4.0.205", prog_num=4331):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4332) as should_copy_source_809_4332:
                    should_copy_source_809_4332()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", prog_num=4333):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Joeco.wfi", r".", prog_num=4334) as copy_file_to_dir_810_4334:
                            copy_file_to_dir_810_4334()
                        with ChmodAndChown(path=r"IO_13.4_Joeco.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4335) as chmod_and_chown_811_4335:
                            chmod_and_chown_811_4335()
            with Stage(r"copy", r"DigiGrid MGB Firmware v13.4.0.205", prog_num=4336):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4337) as should_copy_source_812_4337:
                    should_copy_source_812_4337()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", prog_num=4338):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", r".", prog_num=4339) as copy_file_to_dir_813_4339:
                            copy_file_to_dir_813_4339()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGB.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4340) as chmod_and_chown_814_4340:
                            chmod_and_chown_814_4340()
            with Stage(r"copy", r"DigiGrid MGO Firmware v13.4.0.205", prog_num=4341):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4342) as should_copy_source_815_4342:
                    should_copy_source_815_4342()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", prog_num=4343):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", r".", prog_num=4344) as copy_file_to_dir_816_4344:
                            copy_file_to_dir_816_4344()
                        with ChmodAndChown(path=r"IO_13.4_DiGiGrid_MGO.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4345) as chmod_and_chown_817_4345:
                            chmod_and_chown_817_4345()
            with Stage(r"copy", r"SoundStudio STG-1608 Firmware v13.4.0.205", prog_num=4346):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4347) as should_copy_source_818_4347:
                    should_copy_source_818_4347()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", prog_num=4348):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", r".", prog_num=4349) as copy_file_to_dir_819_4349:
                            copy_file_to_dir_819_4349()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4350) as chmod_and_chown_820_4350:
                            chmod_and_chown_820_4350()
            with Stage(r"copy", r"SoundStudio STG-1608 micro Firmware V13.4 v13.4.0.205", prog_num=4351):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4352) as should_copy_source_821_4352:
                    should_copy_source_821_4352()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", prog_num=4353):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", r".", prog_num=4354) as copy_file_to_dir_822_4354:
                            copy_file_to_dir_822_4354()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_1608_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4355) as chmod_and_chown_823_4355:
                            chmod_and_chown_823_4355()
            with Stage(r"copy", r"SoundStudio STG-2412 Firmware v13.4.0.205", prog_num=4356):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4357) as should_copy_source_824_4357:
                    should_copy_source_824_4357()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", prog_num=4358):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", r".", prog_num=4359) as copy_file_to_dir_825_4359:
                            copy_file_to_dir_825_4359()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4360) as chmod_and_chown_826_4360:
                            chmod_and_chown_826_4360()
            with Stage(r"copy", r"SoundStudio STG-2412 micro Firmware V13.4 v13.4.0.205", prog_num=4361):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4362) as should_copy_source_827_4362:
                    should_copy_source_827_4362()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", prog_num=4363):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", r".", prog_num=4364) as copy_file_to_dir_828_4364:
                            copy_file_to_dir_828_4364()
                        with ChmodAndChown(path=r"IO_13.4_SoundStudio_STG_2412_micro.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4365) as chmod_and_chown_829_4365:
                            chmod_and_chown_829_4365()
            with Stage(r"copy", r"X-WSG_s6_Firmware_13_4 v13.4.0.205", prog_num=4366):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4367) as should_copy_source_830_4367:
                    should_copy_source_830_4367()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", prog_num=4368):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_X_WSG.wfi", r".", prog_num=4369) as copy_file_to_dir_831_4369:
                            copy_file_to_dir_831_4369()
                        with ChmodAndChown(path=r"IO_13.4_X_WSG.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4370) as chmod_and_chown_832_4370:
                            chmod_and_chown_832_4370()
            with Stage(r"copy", r"WSG Y-16 s3 Firmware v13.4.0.205", prog_num=4371):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4372) as should_copy_source_833_4372:
                    should_copy_source_833_4372()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", prog_num=4373):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s3.wfi", r".", prog_num=4374) as copy_file_to_dir_834_4374:
                            copy_file_to_dir_834_4374()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4375) as chmod_and_chown_835_4375:
                            chmod_and_chown_835_4375()
            with Stage(r"copy", r"WSG Y-16 s6 Firmware v13.4.0.205", prog_num=4376):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4377) as should_copy_source_836_4377:
                    should_copy_source_836_4377()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", prog_num=4378):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_yamaha_s6.wfi", r".", prog_num=4379) as copy_file_to_dir_837_4379:
                            copy_file_to_dir_837_4379()
                        with ChmodAndChown(path=r"IO_13.4_yamaha_s6.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4380) as chmod_and_chown_838_4380:
                            chmod_and_chown_838_4380()
            with Stage(r"copy", r"WSG Y-16 v3 Firmware v14.21.16.472", prog_num=4381):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4382) as should_copy_source_839_4382:
                    should_copy_source_839_4382()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", prog_num=4383):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.21_MY16_v3.wfi", r".", prog_num=4384) as copy_file_to_dir_840_4384:
                            copy_file_to_dir_840_4384()
                        with ChmodAndChown(path=r"IO_14.21_MY16_v3.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4385) as chmod_and_chown_841_4385:
                            chmod_and_chown_841_4385()
            with Stage(r"copy", r"Yamaha HY128 v2 Firmware v14.13.43.386", prog_num=4386):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4387) as should_copy_source_842_4387:
                    should_copy_source_842_4387()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", prog_num=4388):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_14.13_HY_v2.wfi", r".", prog_num=4389) as copy_file_to_dir_843_4389:
                            copy_file_to_dir_843_4389()
                        with ChmodAndChown(path=r"IO_14.13_HY_v2.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4390) as chmod_and_chown_844_4390:
                            chmod_and_chown_844_4390()
            with Stage(r"copy", r"Yamaha WSG-HY128 Firmware v13.4.0.205", prog_num=4391):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", skip_progress_count=3, prog_num=4392) as should_copy_source_845_4392:
                    should_copy_source_845_4392()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", prog_num=4393):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/IO/IO_13.4_Hy.wfi", r".", prog_num=4394) as copy_file_to_dir_846_4394:
                            copy_file_to_dir_846_4394()
                        with ChmodAndChown(path=r"IO_13.4_Hy.wfi", mode="a+rw", user_id=-1, group_id=-1, prog_num=4395) as chmod_and_chown_847_4395:
                            chmod_and_chown_847_4395()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4396):
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4397) as cd_848_4397:
                cd_848_4397()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4398)()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_9.7.wfi", prog_num=4399) as rm_file_849_4399:
                    rm_file_849_4399()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.0.wfi", prog_num=4400) as rm_file_850_4400:
                    rm_file_850_4400()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.2.wfi", prog_num=4401) as rm_file_851_4401:
                    rm_file_851_4401()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.3.wfi", prog_num=4402) as rm_file_852_4402:
                    rm_file_852_4402()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.1.wfi", prog_num=4403) as rm_file_853_4403:
                    rm_file_853_4403()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.2.wfi", prog_num=4404) as rm_file_854_4404:
                    rm_file_854_4404()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.2.wfi", prog_num=4405) as rm_file_855_4405:
                    rm_file_855_4405()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.8.wfi", prog_num=4406) as rm_file_856_4406:
                    rm_file_856_4406()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_13.3.wfi", prog_num=4407) as rm_file_857_4407:
                    rm_file_857_4407()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.6.wfi", prog_num=4408) as rm_file_858_4408:
                    rm_file_858_4408()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.9.wfi", prog_num=4409) as rm_file_859_4409:
                    rm_file_859_4409()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=4410) as cd_stage_860_4410:
            cd_stage_860_4410()
            with Stage(r"copy", r"SoundGrid Server Firmware v14.26.104.721", prog_num=4411):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", skip_progress_count=2, prog_num=4412) as should_copy_source_861_4412:
                    should_copy_source_861_4412()
                    with Stage(r"copy source", r"Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi", prog_num=4413):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Firmware/SGS/SGS_14.26.wfi.wtar.aa", where_to_unwtar=r".", prog_num=4414) as unwtar_862_4414:
                            unwtar_862_4414()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4415):
            with Cd(r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4416) as cd_863_4416:
                cd_863_4416()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4417)()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=4418) as rm_dir_864_4418:
                    rm_dir_864_4418()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=4419) as rm_dir_865_4419:
                    rm_dir_865_4419()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=4420) as rm_dir_866_4420:
                    rm_dir_866_4420()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=4421) as rm_dir_867_4421:
                    rm_dir_867_4421()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.app", prog_num=4422) as rm_dir_868_4422:
                    rm_dir_868_4422()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.bundle", prog_num=4423) as rm_dir_869_4423:
                    rm_dir_869_4423()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.app", prog_num=4424) as rm_dir_870_4424:
                    rm_dir_870_4424()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.bundle", prog_num=4425) as rm_dir_871_4425:
                    rm_dir_871_4425()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.app", prog_num=4426) as rm_dir_872_4426:
                    rm_dir_872_4426()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.bundle", prog_num=4427) as rm_dir_873_4427:
                    rm_dir_873_4427()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.app", prog_num=4428) as rm_dir_874_4428:
                    rm_dir_874_4428()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.bundle", prog_num=4429) as rm_dir_875_4429:
                    rm_dir_875_4429()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.app", prog_num=4430) as rm_dir_876_4430:
                    rm_dir_876_4430()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.bundle", prog_num=4431) as rm_dir_877_4431:
                    rm_dir_877_4431()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.app", prog_num=4432) as rm_dir_878_4432:
                    rm_dir_878_4432()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.bundle", prog_num=4433) as rm_dir_879_4433:
                    rm_dir_879_4433()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.app", prog_num=4434) as rm_dir_880_4434:
                    rm_dir_880_4434()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.bundle", prog_num=4435) as rm_dir_881_4435:
                    rm_dir_881_4435()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.app", prog_num=4436) as rm_dir_882_4436:
                    rm_dir_882_4436()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.bundle", prog_num=4437) as rm_dir_883_4437:
                    rm_dir_883_4437()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.app", prog_num=4438) as rm_dir_884_4438:
                    rm_dir_884_4438()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.bundle", prog_num=4439) as rm_dir_885_4439:
                    rm_dir_885_4439()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.app", prog_num=4440) as rm_dir_886_4440:
                    rm_dir_886_4440()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.bundle", prog_num=4441) as rm_dir_887_4441:
                    rm_dir_887_4441()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.app", prog_num=4442) as rm_dir_888_4442:
                    rm_dir_888_4442()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.bundle", prog_num=4443) as rm_dir_889_4443:
                    rm_dir_889_4443()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.app", prog_num=4444) as rm_dir_890_4444:
                    rm_dir_890_4444()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.bundle", prog_num=4445) as rm_dir_891_4445:
                    rm_dir_891_4445()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 9.7.bundle", prog_num=4446) as rm_dir_892_4446:
                    rm_dir_892_4446()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 10.0.bundle", prog_num=4447) as rm_dir_893_4447:
                    rm_dir_893_4447()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 12.1.bundle", prog_num=4448) as rm_dir_894_4448:
                    rm_dir_894_4448()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 13.1.bundle", prog_num=4449) as rm_dir_895_4449:
                    rm_dir_895_4449()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 9.7.bundle", prog_num=4450) as rm_dir_896_4450:
                    rm_dir_896_4450()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 10.0.bundle", prog_num=4451) as rm_dir_897_4451:
                    rm_dir_897_4451()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 12.1.bundle", prog_num=4452) as rm_dir_898_4452:
                    rm_dir_898_4452()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 13.1.bundle", prog_num=4453) as rm_dir_899_4453:
                    rm_dir_899_4453()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.app", prog_num=4454) as rm_dir_900_4454:
                    rm_dir_900_4454()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.bundle", prog_num=4455) as rm_dir_901_4455:
                    rm_dir_901_4455()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.app", prog_num=4456) as rm_dir_902_4456:
                    rm_dir_902_4456()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.bundle", prog_num=4457) as rm_dir_903_4457:
                    rm_dir_903_4457()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.app", prog_num=4458) as rm_dir_904_4458:
                    rm_dir_904_4458()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.bundle", prog_num=4459) as rm_dir_905_4459:
                    rm_dir_905_4459()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=4460) as rm_dir_906_4460:
                    rm_dir_906_4460()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=4461) as rm_dir_907_4461:
                    rm_dir_907_4461()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.app", prog_num=4462) as rm_dir_908_4462:
                    rm_dir_908_4462()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.bundle", prog_num=4463) as rm_dir_909_4463:
                    rm_dir_909_4463()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.app", prog_num=4464) as rm_dir_910_4464:
                    rm_dir_910_4464()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.bundle", prog_num=4465) as rm_dir_911_4465:
                    rm_dir_911_4465()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.app", prog_num=4466) as rm_dir_912_4466:
                    rm_dir_912_4466()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.bundle", prog_num=4467) as rm_dir_913_4467:
                    rm_dir_913_4467()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.app", prog_num=4468) as rm_dir_914_4468:
                    rm_dir_914_4468()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.bundle", prog_num=4469) as rm_dir_915_4469:
                    rm_dir_915_4469()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.app", prog_num=4470) as rm_dir_916_4470:
                    rm_dir_916_4470()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.bundle", prog_num=4471) as rm_dir_917_4471:
                    rm_dir_917_4471()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.app", prog_num=4472) as rm_dir_918_4472:
                    rm_dir_918_4472()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.bundle", prog_num=4473) as rm_dir_919_4473:
                    rm_dir_919_4473()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.app", prog_num=4474) as rm_dir_920_4474:
                    rm_dir_920_4474()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.bundle", prog_num=4475) as rm_dir_921_4475:
                    rm_dir_921_4475()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.app", prog_num=4476) as rm_dir_922_4476:
                    rm_dir_922_4476()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.bundle", prog_num=4477) as rm_dir_923_4477:
                    rm_dir_923_4477()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.app", prog_num=4478) as rm_dir_924_4478:
                    rm_dir_924_4478()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.bundle", prog_num=4479) as rm_dir_925_4479:
                    rm_dir_925_4479()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.app", prog_num=4480) as rm_dir_926_4480:
                    rm_dir_926_4480()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.bundle", prog_num=4481) as rm_dir_927_4481:
                    rm_dir_927_4481()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.app", prog_num=4482) as rm_dir_928_4482:
                    rm_dir_928_4482()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.bundle", prog_num=4483) as rm_dir_929_4483:
                    rm_dir_929_4483()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.app", prog_num=4484) as rm_dir_930_4484:
                    rm_dir_930_4484()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.bundle", prog_num=4485) as rm_dir_931_4485:
                    rm_dir_931_4485()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.app", prog_num=4486) as rm_dir_932_4486:
                    rm_dir_932_4486()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.bundle", prog_num=4487) as rm_dir_933_4487:
                    rm_dir_933_4487()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.app", prog_num=4488) as rm_dir_934_4488:
                    rm_dir_934_4488()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.bundle", prog_num=4489) as rm_dir_935_4489:
                    rm_dir_935_4489()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.app", prog_num=4490) as rm_dir_936_4490:
                    rm_dir_936_4490()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.bundle", prog_num=4491) as rm_dir_937_4491:
                    rm_dir_937_4491()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.app", prog_num=4492) as rm_dir_938_4492:
                    rm_dir_938_4492()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.bundle", prog_num=4493) as rm_dir_939_4493:
                    rm_dir_939_4493()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.app", prog_num=4494) as rm_dir_940_4494:
                    rm_dir_940_4494()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.bundle", prog_num=4495) as rm_dir_941_4495:
                    rm_dir_941_4495()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.app", prog_num=4496) as rm_dir_942_4496:
                    rm_dir_942_4496()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.bundle", prog_num=4497) as rm_dir_943_4497:
                    rm_dir_943_4497()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.app", prog_num=4498) as rm_dir_944_4498:
                    rm_dir_944_4498()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.bundle", prog_num=4499) as rm_dir_945_4499:
                    rm_dir_945_4499()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.app", prog_num=4500) as rm_dir_946_4500:
                    rm_dir_946_4500()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.bundle", prog_num=4501) as rm_dir_947_4501:
                    rm_dir_947_4501()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.app", prog_num=4502) as rm_dir_948_4502:
                    rm_dir_948_4502()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.bundle", prog_num=4503) as rm_dir_949_4503:
                    rm_dir_949_4503()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.app", prog_num=4504) as rm_dir_950_4504:
                    rm_dir_950_4504()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.bundle", prog_num=4505) as rm_dir_951_4505:
                    rm_dir_951_4505()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.app", prog_num=4506) as rm_dir_952_4506:
                    rm_dir_952_4506()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.bundle", prog_num=4507) as rm_dir_953_4507:
                    rm_dir_953_4507()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=4508) as rm_dir_954_4508:
                    rm_dir_954_4508()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=4509) as rm_dir_955_4509:
                    rm_dir_955_4509()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=4510) as rm_dir_956_4510:
                    rm_dir_956_4510()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=4511) as rm_dir_957_4511:
                    rm_dir_957_4511()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.exe", prog_num=4512) as rm_file_958_4512:
                    rm_file_958_4512()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.exe", prog_num=4513) as rm_file_959_4513:
                    rm_file_959_4513()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.app", prog_num=4514) as rm_dir_960_4514:
                    rm_dir_960_4514()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.bundle", prog_num=4515) as rm_dir_961_4515:
                    rm_dir_961_4515()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.app", prog_num=4516) as rm_dir_962_4516:
                    rm_dir_962_4516()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.bundle", prog_num=4517) as rm_dir_963_4517:
                    rm_dir_963_4517()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.app", prog_num=4518) as rm_dir_964_4518:
                    rm_dir_964_4518()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.bundle", prog_num=4519) as rm_dir_965_4519:
                    rm_dir_965_4519()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.app", prog_num=4520) as rm_dir_966_4520:
                    rm_dir_966_4520()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.bundle", prog_num=4521) as rm_dir_967_4521:
                    rm_dir_967_4521()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.app", prog_num=4522) as rm_dir_968_4522:
                    rm_dir_968_4522()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.bundle", prog_num=4523) as rm_dir_969_4523:
                    rm_dir_969_4523()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.app", prog_num=4524) as rm_dir_970_4524:
                    rm_dir_970_4524()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.bundle", prog_num=4525) as rm_dir_971_4525:
                    rm_dir_971_4525()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.app", prog_num=4526) as rm_dir_972_4526:
                    rm_dir_972_4526()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.bundle", prog_num=4527) as rm_dir_973_4527:
                    rm_dir_973_4527()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.app", prog_num=4528) as rm_dir_974_4528:
                    rm_dir_974_4528()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.bundle", prog_num=4529) as rm_dir_975_4529:
                    rm_dir_975_4529()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.app", prog_num=4530) as rm_dir_976_4530:
                    rm_dir_976_4530()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.bundle", prog_num=4531) as rm_dir_977_4531:
                    rm_dir_977_4531()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.app", prog_num=4532) as rm_dir_978_4532:
                    rm_dir_978_4532()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.bundle", prog_num=4533) as rm_dir_979_4533:
                    rm_dir_979_4533()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.app", prog_num=4534) as rm_dir_980_4534:
                    rm_dir_980_4534()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.bundle", prog_num=4535) as rm_dir_981_4535:
                    rm_dir_981_4535()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.app", prog_num=4536) as rm_dir_982_4536:
                    rm_dir_982_4536()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.bundle", prog_num=4537) as rm_dir_983_4537:
                    rm_dir_983_4537()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.app", prog_num=4538) as rm_dir_984_4538:
                    rm_dir_984_4538()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.bundle", prog_num=4539) as rm_dir_985_4539:
                    rm_dir_985_4539()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.app", prog_num=4540) as rm_dir_986_4540:
                    rm_dir_986_4540()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.bundle", prog_num=4541) as rm_dir_987_4541:
                    rm_dir_987_4541()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.app", prog_num=4542) as rm_dir_988_4542:
                    rm_dir_988_4542()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.bundle", prog_num=4543) as rm_dir_989_4543:
                    rm_dir_989_4543()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.app", prog_num=4544) as rm_dir_990_4544:
                    rm_dir_990_4544()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.bundle", prog_num=4545) as rm_dir_991_4545:
                    rm_dir_991_4545()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.app", prog_num=4546) as rm_dir_992_4546:
                    rm_dir_992_4546()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.bundle", prog_num=4547) as rm_dir_993_4547:
                    rm_dir_993_4547()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.app", prog_num=4548) as rm_dir_994_4548:
                    rm_dir_994_4548()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.bundle", prog_num=4549) as rm_dir_995_4549:
                    rm_dir_995_4549()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.app", prog_num=4550) as rm_dir_996_4550:
                    rm_dir_996_4550()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.bundle", prog_num=4551) as rm_dir_997_4551:
                    rm_dir_997_4551()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.app", prog_num=4552) as rm_dir_998_4552:
                    rm_dir_998_4552()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.bundle", prog_num=4553) as rm_dir_999_4553:
                    rm_dir_999_4553()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.app", prog_num=4554) as rm_dir_1000_4554:
                    rm_dir_1000_4554()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.bundle", prog_num=4555) as rm_dir_1001_4555:
                    rm_dir_1001_4555()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.app", prog_num=4556) as rm_dir_1002_4556:
                    rm_dir_1002_4556()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.bundle", prog_num=4557) as rm_dir_1003_4557:
                    rm_dir_1003_4557()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.app", prog_num=4558) as rm_dir_1004_4558:
                    rm_dir_1004_4558()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.bundle", prog_num=4559) as rm_dir_1005_4559:
                    rm_dir_1005_4559()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.app", prog_num=4560) as rm_dir_1006_4560:
                    rm_dir_1006_4560()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.bundle", prog_num=4561) as rm_dir_1007_4561:
                    rm_dir_1007_4561()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.app", prog_num=4562) as rm_dir_1008_4562:
                    rm_dir_1008_4562()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.bundle", prog_num=4563) as rm_dir_1009_4563:
                    rm_dir_1009_4563()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.app", prog_num=4564) as rm_dir_1010_4564:
                    rm_dir_1010_4564()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.bundle", prog_num=4565) as rm_dir_1011_4565:
                    rm_dir_1011_4565()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.app", prog_num=4566) as rm_dir_1012_4566:
                    rm_dir_1012_4566()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.bundle", prog_num=4567) as rm_dir_1013_4567:
                    rm_dir_1013_4567()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.app", prog_num=4568) as rm_dir_1014_4568:
                    rm_dir_1014_4568()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.bundle", prog_num=4569) as rm_dir_1015_4569:
                    rm_dir_1015_4569()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.app", prog_num=4570) as rm_dir_1016_4570:
                    rm_dir_1016_4570()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.bundle", prog_num=4571) as rm_dir_1017_4571:
                    rm_dir_1017_4571()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.app", prog_num=4572) as rm_dir_1018_4572:
                    rm_dir_1018_4572()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.bundle", prog_num=4573) as rm_dir_1019_4573:
                    rm_dir_1019_4573()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.app", prog_num=4574) as rm_dir_1020_4574:
                    rm_dir_1020_4574()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.bundle", prog_num=4575) as rm_dir_1021_4575:
                    rm_dir_1021_4575()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.app", prog_num=4576) as rm_dir_1022_4576:
                    rm_dir_1022_4576()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.bundle", prog_num=4577) as rm_dir_1023_4577:
                    rm_dir_1023_4577()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.app", prog_num=4578) as rm_dir_1024_4578:
                    rm_dir_1024_4578()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.bundle", prog_num=4579) as rm_dir_1025_4579:
                    rm_dir_1025_4579()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.app", prog_num=4580) as rm_dir_1026_4580:
                    rm_dir_1026_4580()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.bundle", prog_num=4581) as rm_dir_1027_4581:
                    rm_dir_1027_4581()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.app", prog_num=4582) as rm_dir_1028_4582:
                    rm_dir_1028_4582()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.bundle", prog_num=4583) as rm_dir_1029_4583:
                    rm_dir_1029_4583()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.app", prog_num=4584) as rm_dir_1030_4584:
                    rm_dir_1030_4584()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.bundle", prog_num=4585) as rm_dir_1031_4585:
                    rm_dir_1031_4585()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.app", prog_num=4586) as rm_dir_1032_4586:
                    rm_dir_1032_4586()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.bundle", prog_num=4587) as rm_dir_1033_4587:
                    rm_dir_1033_4587()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.app", prog_num=4588) as rm_dir_1034_4588:
                    rm_dir_1034_4588()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.bundle", prog_num=4589) as rm_dir_1035_4589:
                    rm_dir_1035_4589()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.app", prog_num=4590) as rm_dir_1036_4590:
                    rm_dir_1036_4590()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.bundle", prog_num=4591) as rm_dir_1037_4591:
                    rm_dir_1037_4591()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.app", prog_num=4592) as rm_dir_1038_4592:
                    rm_dir_1038_4592()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.bundle", prog_num=4593) as rm_dir_1039_4593:
                    rm_dir_1039_4593()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.app", prog_num=4594) as rm_dir_1040_4594:
                    rm_dir_1040_4594()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.bundle", prog_num=4595) as rm_dir_1041_4595:
                    rm_dir_1041_4595()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.app", prog_num=4596) as rm_dir_1042_4596:
                    rm_dir_1042_4596()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.bundle", prog_num=4597) as rm_dir_1043_4597:
                    rm_dir_1043_4597()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.app", prog_num=4598) as rm_dir_1044_4598:
                    rm_dir_1044_4598()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.bundle", prog_num=4599) as rm_dir_1045_4599:
                    rm_dir_1045_4599()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.app", prog_num=4600) as rm_dir_1046_4600:
                    rm_dir_1046_4600()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.bundle", prog_num=4601) as rm_dir_1047_4601:
                    rm_dir_1047_4601()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.app", prog_num=4602) as rm_dir_1048_4602:
                    rm_dir_1048_4602()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.bundle", prog_num=4603) as rm_dir_1049_4603:
                    rm_dir_1049_4603()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.app", prog_num=4604) as rm_dir_1050_4604:
                    rm_dir_1050_4604()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.bundle", prog_num=4605) as rm_dir_1051_4605:
                    rm_dir_1051_4605()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 10.0.bundle", prog_num=4606) as rm_dir_1052_4606:
                    rm_dir_1052_4606()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 12.1.bundle", prog_num=4607) as rm_dir_1053_4607:
                    rm_dir_1053_4607()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 13.1.bundle", prog_num=4608) as rm_dir_1054_4608:
                    rm_dir_1054_4608()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.app", prog_num=4609) as rm_dir_1055_4609:
                    rm_dir_1055_4609()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.bundle", prog_num=4610) as rm_dir_1056_4610:
                    rm_dir_1056_4610()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.app", prog_num=4611) as rm_dir_1057_4611:
                    rm_dir_1057_4611()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.bundle", prog_num=4612) as rm_dir_1058_4612:
                    rm_dir_1058_4612()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.app", prog_num=4613) as rm_dir_1059_4613:
                    rm_dir_1059_4613()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.bundle", prog_num=4614) as rm_dir_1060_4614:
                    rm_dir_1060_4614()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.app", prog_num=4615) as rm_dir_1061_4615:
                    rm_dir_1061_4615()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.bundle", prog_num=4616) as rm_dir_1062_4616:
                    rm_dir_1062_4616()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.app", prog_num=4617) as rm_dir_1063_4617:
                    rm_dir_1063_4617()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.bundle", prog_num=4618) as rm_dir_1064_4618:
                    rm_dir_1064_4618()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.app", prog_num=4619) as rm_dir_1065_4619:
                    rm_dir_1065_4619()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.bundle", prog_num=4620) as rm_dir_1066_4620:
                    rm_dir_1066_4620()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.app", prog_num=4621) as rm_dir_1067_4621:
                    rm_dir_1067_4621()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.bundle", prog_num=4622) as rm_dir_1068_4622:
                    rm_dir_1068_4622()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.app", prog_num=4623) as rm_dir_1069_4623:
                    rm_dir_1069_4623()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.bundle", prog_num=4624) as rm_dir_1070_4624:
                    rm_dir_1070_4624()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.app", prog_num=4625) as rm_dir_1071_4625:
                    rm_dir_1071_4625()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.bundle", prog_num=4626) as rm_dir_1072_4626:
                    rm_dir_1072_4626()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.app", prog_num=4627) as rm_dir_1073_4627:
                    rm_dir_1073_4627()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.bundle", prog_num=4628) as rm_dir_1074_4628:
                    rm_dir_1074_4628()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.app", prog_num=4629) as rm_dir_1075_4629:
                    rm_dir_1075_4629()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.bundle", prog_num=4630) as rm_dir_1076_4630:
                    rm_dir_1076_4630()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=4631) as cd_stage_1077_4631:
            cd_stage_1077_4631()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=4632) as rm_file_or_dir_1078_4632:
                rm_file_or_dir_1078_4632()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=4633) as rm_file_or_dir_1079_4633:
                rm_file_or_dir_1079_4633()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.app", prog_num=4634) as rm_file_or_dir_1080_4634:
                rm_file_or_dir_1080_4634()
            with RmFileOrDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Heartech Control 12.3.bundle", prog_num=4635) as rm_file_or_dir_1081_4635:
                rm_file_or_dir_1081_4635()
            with Stage(r"copy", r"Apogee Symphony MKII Control Panel v14.0.342.343", prog_num=4636):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4637) as should_copy_source_1082_4637:
                    should_copy_source_1082_4637()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.app", prog_num=4638):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", r".", delete_extraneous_files=True, prog_num=4639) as copy_dir_to_dir_1083_4639:
                            copy_dir_to_dir_1083_4639()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.app", where_to_unwtar=r".", prog_num=4640) as unwtar_1084_4640:
                            unwtar_1084_4640()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.app", user_id=-1, group_id=-1, prog_num=4641, recursive=True) as chown_1085_4641:
                            chown_1085_4641()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4642) as should_copy_source_1086_4642:
                    should_copy_source_1086_4642()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Symphony MKII.bundle", prog_num=4643):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", r".", delete_extraneous_files=True, prog_num=4644) as copy_dir_to_dir_1087_4644:
                            copy_dir_to_dir_1087_4644()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Symphony MKII.bundle", where_to_unwtar=r".", prog_num=4645) as unwtar_1088_4645:
                            unwtar_1088_4645()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.bundle", user_id=-1, group_id=-1, prog_num=4646, recursive=True) as chown_1089_4646:
                            chown_1089_4646()
            with Stage(r"copy", r"SoundGrid BR-1 Control Panel v14.0.342.343", prog_num=4647):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4648) as should_copy_source_1090_4648:
                    should_copy_source_1090_4648()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.app", prog_num=4649):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", r".", delete_extraneous_files=True, prog_num=4650) as copy_dir_to_dir_1091_4650:
                            copy_dir_to_dir_1091_4650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.app", where_to_unwtar=r".", prog_num=4651) as unwtar_1092_4651:
                            unwtar_1092_4651()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.app", user_id=-1, group_id=-1, prog_num=4652, recursive=True) as chown_1093_4652:
                            chown_1093_4652()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4653) as should_copy_source_1094_4653:
                    should_copy_source_1094_4653()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", prog_num=4654):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", r".", delete_extraneous_files=True, prog_num=4655) as copy_dir_to_dir_1095_4655:
                            copy_dir_to_dir_1095_4655()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid BR1.bundle", where_to_unwtar=r".", prog_num=4656) as unwtar_1096_4656:
                            unwtar_1096_4656()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.bundle", user_id=-1, group_id=-1, prog_num=4657, recursive=True) as chown_1097_4657:
                            chown_1097_4657()
            with Stage(r"copy", r"Behringer Wing SoundGrid I/O Driver Control Panel v14.0.436.437", prog_num=4658):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4659) as should_copy_source_1098_4659:
                    should_copy_source_1098_4659()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", prog_num=4660):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", r".", delete_extraneous_files=True, prog_num=4661) as copy_dir_to_dir_1099_4661:
                            copy_dir_to_dir_1099_4661()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.app", where_to_unwtar=r".", prog_num=4662) as unwtar_1100_4662:
                            unwtar_1100_4662()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.app", user_id=-1, group_id=-1, prog_num=4663, recursive=True) as chown_1101_4663:
                            chown_1101_4663()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4664) as should_copy_source_1102_4664:
                    should_copy_source_1102_4664()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", prog_num=4665):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", r".", delete_extraneous_files=True, prog_num=4666) as copy_dir_to_dir_1103_4666:
                            copy_dir_to_dir_1103_4666()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid Wing Control.bundle", where_to_unwtar=r".", prog_num=4667) as unwtar_1104_4667:
                            unwtar_1104_4667()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.bundle", user_id=-1, group_id=-1, prog_num=4668, recursive=True) as chown_1105_4668:
                            chown_1105_4668()
            with Stage(r"copy", r"BMB4 SoundGrid MotherBoard Control Panel v14.0.342.343", prog_num=4669):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4670) as should_copy_source_1106_4670:
                    should_copy_source_1106_4670()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", prog_num=4671):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", r".", delete_extraneous_files=True, prog_num=4672) as copy_dir_to_dir_1107_4672:
                            copy_dir_to_dir_1107_4672()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.app", where_to_unwtar=r".", prog_num=4673) as unwtar_1108_4673:
                            unwtar_1108_4673()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.app", user_id=-1, group_id=-1, prog_num=4674, recursive=True) as chown_1109_4674:
                            chown_1109_4674()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4675) as should_copy_source_1110_4675:
                    should_copy_source_1110_4675()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", prog_num=4676):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", r".", delete_extraneous_files=True, prog_num=4677) as copy_dir_to_dir_1111_4677:
                            copy_dir_to_dir_1111_4677()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/BMB4 Motherboard Control.bundle", where_to_unwtar=r".", prog_num=4678) as unwtar_1112_4678:
                            unwtar_1112_4678()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.bundle", user_id=-1, group_id=-1, prog_num=4679, recursive=True) as chown_1113_4679:
                            chown_1113_4679()
            with Stage(r"copy", r"Cadac Control Panel v14.0.342.343", prog_num=4680):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4681) as should_copy_source_1114_4681:
                    should_copy_source_1114_4681()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Cadac Control.bundle", prog_num=4682):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", r".", delete_extraneous_files=True, prog_num=4683) as copy_dir_to_dir_1115_4683:
                            copy_dir_to_dir_1115_4683()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Cadac Control.bundle", where_to_unwtar=r".", prog_num=4684) as unwtar_1116_4684:
                            unwtar_1116_4684()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control.bundle", user_id=-1, group_id=-1, prog_num=4685, recursive=True) as chown_1117_4685:
                            chown_1117_4685()
            with Stage(r"copy", r"Calrec Control Panel v14.0.342.343", prog_num=4686):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4687) as should_copy_source_1118_4687:
                    should_copy_source_1118_4687()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Calrec Control.bundle", prog_num=4688):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", r".", delete_extraneous_files=True, prog_num=4689) as copy_dir_to_dir_1119_4689:
                            copy_dir_to_dir_1119_4689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Calrec Control.bundle", where_to_unwtar=r".", prog_num=4690) as unwtar_1120_4690:
                            unwtar_1120_4690()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control.bundle", user_id=-1, group_id=-1, prog_num=4691, recursive=True) as chown_1121_4691:
                            chown_1121_4691()
            with Stage(r"copy", r"Crest Audio Tactus Control Panel v14.0.342.343", prog_num=4692):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4693) as should_copy_source_1122_4693:
                    should_copy_source_1122_4693()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", prog_num=4694):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", r".", delete_extraneous_files=True, prog_num=4695) as copy_dir_to_dir_1123_4695:
                            copy_dir_to_dir_1123_4695()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.app", where_to_unwtar=r".", prog_num=4696) as unwtar_1124_4696:
                            unwtar_1124_4696()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.app", user_id=-1, group_id=-1, prog_num=4697, recursive=True) as chown_1125_4697:
                            chown_1125_4697()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4698) as should_copy_source_1126_4698:
                    should_copy_source_1126_4698()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", prog_num=4699):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", r".", delete_extraneous_files=True, prog_num=4700) as copy_dir_to_dir_1127_4700:
                            copy_dir_to_dir_1127_4700()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Tactus Stage FOH Control.bundle", where_to_unwtar=r".", prog_num=4701) as unwtar_1128_4701:
                            unwtar_1128_4701()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.bundle", user_id=-1, group_id=-1, prog_num=4702, recursive=True) as chown_1129_4702:
                            chown_1129_4702()
            with Stage(r"copy", r"DigiGrid DLI/DLS Control Panel v14.0.342.343", prog_num=4703):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4704) as should_copy_source_1130_4704:
                    should_copy_source_1130_4704()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", prog_num=4705):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", r".", delete_extraneous_files=True, prog_num=4706) as copy_dir_to_dir_1131_4706:
                            copy_dir_to_dir_1131_4706()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.app", where_to_unwtar=r".", prog_num=4707) as unwtar_1132_4707:
                            unwtar_1132_4707()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.app", user_id=-1, group_id=-1, prog_num=4708, recursive=True) as chown_1133_4708:
                            chown_1133_4708()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4709) as should_copy_source_1134_4709:
                    should_copy_source_1134_4709()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", prog_num=4710):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", r".", delete_extraneous_files=True, prog_num=4711) as copy_dir_to_dir_1135_4711:
                            copy_dir_to_dir_1135_4711()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid DLI DLS Control.bundle", where_to_unwtar=r".", prog_num=4712) as unwtar_1136_4712:
                            unwtar_1136_4712()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.bundle", user_id=-1, group_id=-1, prog_num=4713, recursive=True) as chown_1137_4713:
                            chown_1137_4713()
            with Stage(r"copy", r"DMI Waves Control Panel v14.0.342.343", prog_num=4714):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4715) as should_copy_source_1138_4715:
                    should_copy_source_1138_4715()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.app", prog_num=4716):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", r".", delete_extraneous_files=True, prog_num=4717) as copy_dir_to_dir_1139_4717:
                            copy_dir_to_dir_1139_4717()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.app", where_to_unwtar=r".", prog_num=4718) as unwtar_1140_4718:
                            unwtar_1140_4718()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.app", user_id=-1, group_id=-1, prog_num=4719, recursive=True) as chown_1141_4719:
                            chown_1141_4719()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4720) as should_copy_source_1142_4720:
                    should_copy_source_1142_4720()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DMI Control.bundle", prog_num=4721):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", r".", delete_extraneous_files=True, prog_num=4722) as copy_dir_to_dir_1143_4722:
                            copy_dir_to_dir_1143_4722()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DMI Control.bundle", where_to_unwtar=r".", prog_num=4723) as unwtar_1144_4723:
                            unwtar_1144_4723()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.bundle", user_id=-1, group_id=-1, prog_num=4724, recursive=True) as chown_1145_4724:
                            chown_1145_4724()
            with Stage(r"copy", r"DN32-WSG Control Panel v14.0.342.343", prog_num=4725):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4726) as should_copy_source_1146_4726:
                    should_copy_source_1146_4726()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", prog_num=4727):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", r".", delete_extraneous_files=True, prog_num=4728) as copy_dir_to_dir_1147_4728:
                            copy_dir_to_dir_1147_4728()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.app", where_to_unwtar=r".", prog_num=4729) as unwtar_1148_4729:
                            unwtar_1148_4729()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.app", user_id=-1, group_id=-1, prog_num=4730, recursive=True) as chown_1149_4730:
                            chown_1149_4730()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4731) as should_copy_source_1150_4731:
                    should_copy_source_1150_4731()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", prog_num=4732):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=4733) as copy_dir_to_dir_1151_4733:
                            copy_dir_to_dir_1151_4733()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid DN32-WSG Control.bundle", where_to_unwtar=r".", prog_num=4734) as unwtar_1152_4734:
                            unwtar_1152_4734()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=4735, recursive=True) as chown_1153_4735:
                            chown_1153_4735()
            with Stage(r"copy", r"DSPro SG4000 / SG1000 Control Panel v14.0.342.343", prog_num=4736):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4737) as should_copy_source_1154_4737:
                    should_copy_source_1154_4737()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", prog_num=4738):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", r".", delete_extraneous_files=True, prog_num=4739) as copy_dir_to_dir_1155_4739:
                            copy_dir_to_dir_1155_4739()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.app", where_to_unwtar=r".", prog_num=4740) as unwtar_1156_4740:
                            unwtar_1156_4740()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.app", user_id=-1, group_id=-1, prog_num=4741, recursive=True) as chown_1157_4741:
                            chown_1157_4741()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4742) as should_copy_source_1158_4742:
                    should_copy_source_1158_4742()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", prog_num=4743):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", r".", delete_extraneous_files=True, prog_num=4744) as copy_dir_to_dir_1159_4744:
                            copy_dir_to_dir_1159_4744()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DSPro SG4000 Control.bundle", where_to_unwtar=r".", prog_num=4745) as unwtar_1160_4745:
                            unwtar_1160_4745()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.bundle", user_id=-1, group_id=-1, prog_num=4746, recursive=True) as chown_1161_4746:
                            chown_1161_4746()
            with Stage(r"copy", r"DigiGrid D Control Panel v14.0.342.343", prog_num=4747):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4748) as should_copy_source_1162_4748:
                    should_copy_source_1162_4748()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", prog_num=4749):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", r".", delete_extraneous_files=True, prog_num=4750) as copy_dir_to_dir_1163_4750:
                            copy_dir_to_dir_1163_4750()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.app", where_to_unwtar=r".", prog_num=4751) as unwtar_1164_4751:
                            unwtar_1164_4751()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.app", user_id=-1, group_id=-1, prog_num=4752, recursive=True) as chown_1165_4752:
                            chown_1165_4752()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4753) as should_copy_source_1166_4753:
                    should_copy_source_1166_4753()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", prog_num=4754):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", r".", delete_extraneous_files=True, prog_num=4755) as copy_dir_to_dir_1167_4755:
                            copy_dir_to_dir_1167_4755()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid D Control.bundle", where_to_unwtar=r".", prog_num=4756) as unwtar_1168_4756:
                            unwtar_1168_4756()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.bundle", user_id=-1, group_id=-1, prog_num=4757, recursive=True) as chown_1169_4757:
                            chown_1169_4757()
            with Stage(r"copy", r"DigiGrid M Control Panel v$(ExternalVersion", prog_num=4758):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4759) as should_copy_source_1170_4759:
                    should_copy_source_1170_4759()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", prog_num=4760):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", r".", delete_extraneous_files=True, prog_num=4761) as copy_dir_to_dir_1171_4761:
                            copy_dir_to_dir_1171_4761()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.app", where_to_unwtar=r".", prog_num=4762) as unwtar_1172_4762:
                            unwtar_1172_4762()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.app", user_id=-1, group_id=-1, prog_num=4763, recursive=True) as chown_1173_4763:
                            chown_1173_4763()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4764) as should_copy_source_1174_4764:
                    should_copy_source_1174_4764()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", prog_num=4765):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", r".", delete_extraneous_files=True, prog_num=4766) as copy_dir_to_dir_1175_4766:
                            copy_dir_to_dir_1175_4766()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid M Control.bundle", where_to_unwtar=r".", prog_num=4767) as unwtar_1176_4767:
                            unwtar_1176_4767()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.bundle", user_id=-1, group_id=-1, prog_num=4768, recursive=True) as chown_1177_4768:
                            chown_1177_4768()
            with Stage(r"copy", r"DigiGrid Q Control Panel v14.0.342.343", prog_num=4769):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4770) as should_copy_source_1178_4770:
                    should_copy_source_1178_4770()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", prog_num=4771):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", r".", delete_extraneous_files=True, prog_num=4772) as copy_dir_to_dir_1179_4772:
                            copy_dir_to_dir_1179_4772()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.app", where_to_unwtar=r".", prog_num=4773) as unwtar_1180_4773:
                            unwtar_1180_4773()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.app", user_id=-1, group_id=-1, prog_num=4774, recursive=True) as chown_1181_4774:
                            chown_1181_4774()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4775) as should_copy_source_1182_4775:
                    should_copy_source_1182_4775()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", prog_num=4776):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", r".", delete_extraneous_files=True, prog_num=4777) as copy_dir_to_dir_1183_4777:
                            copy_dir_to_dir_1183_4777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid Q Control.bundle", where_to_unwtar=r".", prog_num=4778) as unwtar_1184_4778:
                            unwtar_1184_4778()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.bundle", user_id=-1, group_id=-1, prog_num=4779, recursive=True) as chown_1185_4779:
                            chown_1185_4779()
            with Stage(r"copy", r"Digico SD Control Panel v14.0.7.8", prog_num=4780):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4781) as should_copy_source_1186_4781:
                    should_copy_source_1186_4781()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", prog_num=4782):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", r".", delete_extraneous_files=True, prog_num=4783) as copy_dir_to_dir_1187_4783:
                            copy_dir_to_dir_1187_4783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.app", where_to_unwtar=r".", prog_num=4784) as unwtar_1188_4784:
                            unwtar_1188_4784()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.app", user_id=-1, group_id=-1, prog_num=4785, recursive=True) as chown_1189_4785:
                            chown_1189_4785()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4786) as should_copy_source_1190_4786:
                    should_copy_source_1190_4786()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", prog_num=4787):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", r".", delete_extraneous_files=True, prog_num=4788) as copy_dir_to_dir_1191_4788:
                            copy_dir_to_dir_1191_4788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiCo SD Control.bundle", where_to_unwtar=r".", prog_num=4789) as unwtar_1192_4789:
                            unwtar_1192_4789()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.bundle", user_id=-1, group_id=-1, prog_num=4790, recursive=True) as chown_1193_4790:
                            chown_1193_4790()
            with Stage(r"copy", r"DirectOut Exbox SoundGrid I/O Driver Control Panel v14.0.342.343", prog_num=4791):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4792) as should_copy_source_1194_4792:
                    should_copy_source_1194_4792()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=4793):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=4794) as copy_dir_to_dir_1195_4794:
                            copy_dir_to_dir_1195_4794()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=4795) as unwtar_1196_4795:
                            unwtar_1196_4795()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=4796, recursive=True) as chown_1197_4796:
                            chown_1197_4796()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4797) as should_copy_source_1198_4797:
                    should_copy_source_1198_4797()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=4798):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=4799) as copy_dir_to_dir_1199_4799:
                            copy_dir_to_dir_1199_4799()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=4800) as unwtar_1200_4800:
                            unwtar_1200_4800()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=4801, recursive=True) as chown_1201_4801:
                            chown_1201_4801()
            with Stage(r"copy", r"DirectOut SG.MADI Control Panel v14.0.342.343", prog_num=4802):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4803) as should_copy_source_1202_4803:
                    should_copy_source_1202_4803()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", prog_num=4804):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", r".", delete_extraneous_files=True, prog_num=4805) as copy_dir_to_dir_1203_4805:
                            copy_dir_to_dir_1203_4805()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.app", where_to_unwtar=r".", prog_num=4806) as unwtar_1204_4806:
                            unwtar_1204_4806()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.app", user_id=-1, group_id=-1, prog_num=4807, recursive=True) as chown_1205_4807:
                            chown_1205_4807()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4808) as should_copy_source_1206_4808:
                    should_copy_source_1206_4808()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", prog_num=4809):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", r".", delete_extraneous_files=True, prog_num=4810) as copy_dir_to_dir_1207_4810:
                            copy_dir_to_dir_1207_4810()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SG.MADI Control.bundle", where_to_unwtar=r".", prog_num=4811) as unwtar_1208_4811:
                            unwtar_1208_4811()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.bundle", user_id=-1, group_id=-1, prog_num=4812, recursive=True) as chown_1209_4812:
                            chown_1209_4812()
            with Stage(r"copy", r"DirectOut SoundGrid I/O Driver Control Panel v13.1.261.180", prog_num=4813):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4814) as should_copy_source_1210_4814:
                    should_copy_source_1210_4814()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", prog_num=4815):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", r".", delete_extraneous_files=True, prog_num=4816) as copy_dir_to_dir_1211_4816:
                            copy_dir_to_dir_1211_4816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.app", where_to_unwtar=r".", prog_num=4817) as unwtar_1212_4817:
                            unwtar_1212_4817()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", user_id=-1, group_id=-1, prog_num=4818, recursive=True) as chown_1213_4818:
                            chown_1213_4818()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4819) as should_copy_source_1214_4819:
                    should_copy_source_1214_4819()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=4820):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", r".", delete_extraneous_files=True, prog_num=4821) as copy_dir_to_dir_1215_4821:
                            copy_dir_to_dir_1215_4821()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DirectOut SoundGrid Interface.bundle", where_to_unwtar=r".", prog_num=4822) as unwtar_1216_4822:
                            unwtar_1216_4822()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", user_id=-1, group_id=-1, prog_num=4823, recursive=True) as chown_1217_4823:
                            chown_1217_4823()
            with Stage(r"copy", r"Hear Technologies SG Control Panel v14.0.342.343", prog_num=4824):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4825) as should_copy_source_1218_4825:
                    should_copy_source_1218_4825()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", prog_num=4826):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", r".", delete_extraneous_files=True, prog_num=4827) as copy_dir_to_dir_1219_4827:
                            copy_dir_to_dir_1219_4827()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.app", where_to_unwtar=r".", prog_num=4828) as unwtar_1220_4828:
                            unwtar_1220_4828()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.app", user_id=-1, group_id=-1, prog_num=4829, recursive=True) as chown_1221_4829:
                            chown_1221_4829()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4830) as should_copy_source_1222_4830:
                    should_copy_source_1222_4830()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", prog_num=4831):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", r".", delete_extraneous_files=True, prog_num=4832) as copy_dir_to_dir_1223_4832:
                            copy_dir_to_dir_1223_4832()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Hear Technologies SG Control.bundle", where_to_unwtar=r".", prog_num=4833) as unwtar_1224_4833:
                            unwtar_1224_4833()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.bundle", user_id=-1, group_id=-1, prog_num=4834, recursive=True) as chown_1225_4834:
                            chown_1225_4834()
            with Stage(r"copy", r"DigiGrid IOC Control Panel v14.0.342.343", prog_num=4835):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4836) as should_copy_source_1226_4836:
                    should_copy_source_1226_4836()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", prog_num=4837):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", r".", delete_extraneous_files=True, prog_num=4838) as copy_dir_to_dir_1227_4838:
                            copy_dir_to_dir_1227_4838()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.app", where_to_unwtar=r".", prog_num=4839) as unwtar_1228_4839:
                            unwtar_1228_4839()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.app", user_id=-1, group_id=-1, prog_num=4840, recursive=True) as chown_1229_4840:
                            chown_1229_4840()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4841) as should_copy_source_1230_4841:
                    should_copy_source_1230_4841()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", prog_num=4842):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", r".", delete_extraneous_files=True, prog_num=4843) as copy_dir_to_dir_1231_4843:
                            copy_dir_to_dir_1231_4843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOC Control.bundle", where_to_unwtar=r".", prog_num=4844) as unwtar_1232_4844:
                            unwtar_1232_4844()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.bundle", user_id=-1, group_id=-1, prog_num=4845, recursive=True) as chown_1233_4845:
                            chown_1233_4845()
            with Stage(r"copy", r"IONIC16 Control Panel v14.0.134.135", prog_num=4846):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4847) as should_copy_source_1234_4847:
                    should_copy_source_1234_4847()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.app", prog_num=4848):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", r".", delete_extraneous_files=True, prog_num=4849) as copy_dir_to_dir_1235_4849:
                            copy_dir_to_dir_1235_4849()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.app", where_to_unwtar=r".", prog_num=4850) as unwtar_1236_4850:
                            unwtar_1236_4850()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.app", user_id=-1, group_id=-1, prog_num=4851, recursive=True) as chown_1237_4851:
                            chown_1237_4851()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4852) as should_copy_source_1238_4852:
                    should_copy_source_1238_4852()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/IONIC Control.bundle", prog_num=4853):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", r".", delete_extraneous_files=True, prog_num=4854) as copy_dir_to_dir_1239_4854:
                            copy_dir_to_dir_1239_4854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/IONIC Control.bundle", where_to_unwtar=r".", prog_num=4855) as unwtar_1240_4855:
                            unwtar_1240_4855()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.bundle", user_id=-1, group_id=-1, prog_num=4856, recursive=True) as chown_1241_4856:
                            chown_1241_4856()
            with Stage(r"copy", r"DigiGrid IOS Control Panel v14.0.342.343", prog_num=4857):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4858) as should_copy_source_1242_4858:
                    should_copy_source_1242_4858()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", prog_num=4859):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", r".", delete_extraneous_files=True, prog_num=4860) as copy_dir_to_dir_1243_4860:
                            copy_dir_to_dir_1243_4860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.app", where_to_unwtar=r".", prog_num=4861) as unwtar_1244_4861:
                            unwtar_1244_4861()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.app", user_id=-1, group_id=-1, prog_num=4862, recursive=True) as chown_1245_4862:
                            chown_1245_4862()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4863) as should_copy_source_1246_4863:
                    should_copy_source_1246_4863()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", prog_num=4864):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", r".", delete_extraneous_files=True, prog_num=4865) as copy_dir_to_dir_1247_4865:
                            copy_dir_to_dir_1247_4865()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS Control.bundle", where_to_unwtar=r".", prog_num=4866) as unwtar_1248_4866:
                            unwtar_1248_4866()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.bundle", user_id=-1, group_id=-1, prog_num=4867, recursive=True) as chown_1249_4867:
                            chown_1249_4867()
            with Stage(r"copy", r"DigiGrid IOS-XL Control Panel v14.0.342.343", prog_num=4868):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4869) as should_copy_source_1250_4869:
                    should_copy_source_1250_4869()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", prog_num=4870):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", r".", delete_extraneous_files=True, prog_num=4871) as copy_dir_to_dir_1251_4871:
                            copy_dir_to_dir_1251_4871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.app", where_to_unwtar=r".", prog_num=4872) as unwtar_1252_4872:
                            unwtar_1252_4872()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.app", user_id=-1, group_id=-1, prog_num=4873, recursive=True) as chown_1253_4873:
                            chown_1253_4873()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4874) as should_copy_source_1254_4874:
                    should_copy_source_1254_4874()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", prog_num=4875):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", r".", delete_extraneous_files=True, prog_num=4876) as copy_dir_to_dir_1255_4876:
                            copy_dir_to_dir_1255_4876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOS-XL Control.bundle", where_to_unwtar=r".", prog_num=4877) as unwtar_1256_4877:
                            unwtar_1256_4877()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.bundle", user_id=-1, group_id=-1, prog_num=4878, recursive=True) as chown_1257_4878:
                            chown_1257_4878()
            with Stage(r"copy", r"DigiGrid IOX Control Panel v14.0.342.343", prog_num=4879):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4880) as should_copy_source_1258_4880:
                    should_copy_source_1258_4880()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", prog_num=4881):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", r".", delete_extraneous_files=True, prog_num=4882) as copy_dir_to_dir_1259_4882:
                            copy_dir_to_dir_1259_4882()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.app", where_to_unwtar=r".", prog_num=4883) as unwtar_1260_4883:
                            unwtar_1260_4883()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.app", user_id=-1, group_id=-1, prog_num=4884, recursive=True) as chown_1261_4884:
                            chown_1261_4884()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4885) as should_copy_source_1262_4885:
                    should_copy_source_1262_4885()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", prog_num=4886):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", r".", delete_extraneous_files=True, prog_num=4887) as copy_dir_to_dir_1263_4887:
                            copy_dir_to_dir_1263_4887()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid IOX Control.bundle", where_to_unwtar=r".", prog_num=4888) as unwtar_1264_4888:
                            unwtar_1264_4888()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.bundle", user_id=-1, group_id=-1, prog_num=4889, recursive=True) as chown_1265_4889:
                            chown_1265_4889()
            with Stage(r"copy", r"JoeCo BBSG24MP Control Panel v14.0.342.343", prog_num=4890):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4891) as should_copy_source_1266_4891:
                    should_copy_source_1266_4891()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", prog_num=4892):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", r".", delete_extraneous_files=True, prog_num=4893) as copy_dir_to_dir_1267_4893:
                            copy_dir_to_dir_1267_4893()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.app", where_to_unwtar=r".", prog_num=4894) as unwtar_1268_4894:
                            unwtar_1268_4894()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.app", user_id=-1, group_id=-1, prog_num=4895, recursive=True) as chown_1269_4895:
                            chown_1269_4895()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4896) as should_copy_source_1270_4896:
                    should_copy_source_1270_4896()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", prog_num=4897):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", r".", delete_extraneous_files=True, prog_num=4898) as copy_dir_to_dir_1271_4898:
                            copy_dir_to_dir_1271_4898()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/JoeCo BBSG24MP Control.bundle", where_to_unwtar=r".", prog_num=4899) as unwtar_1272_4899:
                            unwtar_1272_4899()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.bundle", user_id=-1, group_id=-1, prog_num=4900, recursive=True) as chown_1273_4900:
                            chown_1273_4900()
            with Stage(r"copy", r"M-DL-WAVES3 Control Panel v14.0.342.343", prog_num=4901):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4902) as should_copy_source_1274_4902:
                    should_copy_source_1274_4902()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", prog_num=4903):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=4904) as copy_dir_to_dir_1275_4904:
                            copy_dir_to_dir_1275_4904()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.app", where_to_unwtar=r".", prog_num=4905) as unwtar_1276_4905:
                            unwtar_1276_4905()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=4906, recursive=True) as chown_1277_4906:
                            chown_1277_4906()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4907) as should_copy_source_1278_4907:
                    should_copy_source_1278_4907()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", prog_num=4908):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=4909) as copy_dir_to_dir_1279_4909:
                            copy_dir_to_dir_1279_4909()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-DL-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=4910) as unwtar_1280_4910:
                            unwtar_1280_4910()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=4911, recursive=True) as chown_1281_4911:
                            chown_1281_4911()
            with Stage(r"copy", r"M-SQ-WAVES3 Control Panel v14.0.342.343", prog_num=4912):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4913) as should_copy_source_1282_4913:
                    should_copy_source_1282_4913()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", prog_num=4914):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", r".", delete_extraneous_files=True, prog_num=4915) as copy_dir_to_dir_1283_4915:
                            copy_dir_to_dir_1283_4915()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.app", where_to_unwtar=r".", prog_num=4916) as unwtar_1284_4916:
                            unwtar_1284_4916()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.app", user_id=-1, group_id=-1, prog_num=4917, recursive=True) as chown_1285_4917:
                            chown_1285_4917()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4918) as should_copy_source_1286_4918:
                    should_copy_source_1286_4918()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", prog_num=4919):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", r".", delete_extraneous_files=True, prog_num=4920) as copy_dir_to_dir_1287_4920:
                            copy_dir_to_dir_1287_4920()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-SQ-WAVES3 Control.bundle", where_to_unwtar=r".", prog_num=4921) as unwtar_1288_4921:
                            unwtar_1288_4921()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.bundle", user_id=-1, group_id=-1, prog_num=4922, recursive=True) as chown_1289_4922:
                            chown_1289_4922()
            with Stage(r"copy", r"M-Waves v2 Control Panel v14.0.342.343", prog_num=4923):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4924) as should_copy_source_1290_4924:
                    should_copy_source_1290_4924()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", prog_num=4925):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", r".", delete_extraneous_files=True, prog_num=4926) as copy_dir_to_dir_1291_4926:
                            copy_dir_to_dir_1291_4926()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.app", where_to_unwtar=r".", prog_num=4927) as unwtar_1292_4927:
                            unwtar_1292_4927()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.app", user_id=-1, group_id=-1, prog_num=4928, recursive=True) as chown_1293_4928:
                            chown_1293_4928()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4929) as should_copy_source_1294_4929:
                    should_copy_source_1294_4929()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", prog_num=4930):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", r".", delete_extraneous_files=True, prog_num=4931) as copy_dir_to_dir_1295_4931:
                            copy_dir_to_dir_1295_4931()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/M-Waves v2 Control.bundle", where_to_unwtar=r".", prog_num=4932) as unwtar_1296_4932:
                            unwtar_1296_4932()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.bundle", user_id=-1, group_id=-1, prog_num=4933, recursive=True) as chown_1297_4933:
                            chown_1297_4933()
            with Stage(r"copy", r"DigiGrid MGB/MGO/MGR Control Panel v14.0.342.343", prog_num=4934):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4935) as should_copy_source_1298_4935:
                    should_copy_source_1298_4935()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", prog_num=4936):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", r".", delete_extraneous_files=True, prog_num=4937) as copy_dir_to_dir_1299_4937:
                            copy_dir_to_dir_1299_4937()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.app", where_to_unwtar=r".", prog_num=4938) as unwtar_1300_4938:
                            unwtar_1300_4938()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.app", user_id=-1, group_id=-1, prog_num=4939, recursive=True) as chown_1301_4939:
                            chown_1301_4939()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4940) as should_copy_source_1302_4940:
                    should_copy_source_1302_4940()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", prog_num=4941):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", r".", delete_extraneous_files=True, prog_num=4942) as copy_dir_to_dir_1303_4942:
                            copy_dir_to_dir_1303_4942()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/DiGiGrid MGB MGO Control.bundle", where_to_unwtar=r".", prog_num=4943) as unwtar_1304_4943:
                            unwtar_1304_4943()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.bundle", user_id=-1, group_id=-1, prog_num=4944, recursive=True) as chown_1305_4944:
                            chown_1305_4944()
            with Stage(r"copy", r"Waves Legacy SG Control Panels v14.0.342.343", prog_num=4945):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4946) as should_copy_source_1306_4946:
                    should_copy_source_1306_4946()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.app", prog_num=4947):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", r".", delete_extraneous_files=True, prog_num=4948) as copy_dir_to_dir_1307_4948:
                            copy_dir_to_dir_1307_4948()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.app", where_to_unwtar=r".", prog_num=4949) as unwtar_1308_4949:
                            unwtar_1308_4949()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.app", user_id=-1, group_id=-1, prog_num=4950, recursive=True) as chown_1309_4950:
                            chown_1309_4950()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4951) as should_copy_source_1310_4951:
                    should_copy_source_1310_4951()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", prog_num=4952):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", r".", delete_extraneous_files=True, prog_num=4953) as copy_dir_to_dir_1311_4953:
                            copy_dir_to_dir_1311_4953()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Waves Legacy Control.bundle", where_to_unwtar=r".", prog_num=4954) as unwtar_1312_4954:
                            unwtar_1312_4954()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.bundle", user_id=-1, group_id=-1, prog_num=4955, recursive=True) as chown_1313_4955:
                            chown_1313_4955()
            with Stage(r"copy", r"Remote SG IO Control Panel v14.0.342.343", prog_num=4956):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4957) as should_copy_source_1314_4957:
                    should_copy_source_1314_4957()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", prog_num=4958):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", r".", delete_extraneous_files=True, prog_num=4959) as copy_dir_to_dir_1315_4959:
                            copy_dir_to_dir_1315_4959()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.app", where_to_unwtar=r".", prog_num=4960) as unwtar_1316_4960:
                            unwtar_1316_4960()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.app", user_id=-1, group_id=-1, prog_num=4961, recursive=True) as chown_1317_4961:
                            chown_1317_4961()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4962) as should_copy_source_1318_4962:
                    should_copy_source_1318_4962()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", prog_num=4963):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", r".", delete_extraneous_files=True, prog_num=4964) as copy_dir_to_dir_1319_4964:
                            copy_dir_to_dir_1319_4964()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/RIOMGeneral Control.bundle", where_to_unwtar=r".", prog_num=4965) as unwtar_1320_4965:
                            unwtar_1320_4965()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.bundle", user_id=-1, group_id=-1, prog_num=4966, recursive=True) as chown_1321_4966:
                            chown_1321_4966()
            with Stage(r"copy", r"SG Connect v14.0.342.343", prog_num=4967):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4968) as should_copy_source_1322_4968:
                    should_copy_source_1322_4968()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SG Connect Control.bundle", prog_num=4969):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", r".", delete_extraneous_files=True, prog_num=4970) as copy_dir_to_dir_1323_4970:
                            copy_dir_to_dir_1323_4970()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SG Connect Control.bundle", where_to_unwtar=r".", prog_num=4971) as unwtar_1324_4971:
                            unwtar_1324_4971()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control.bundle", user_id=-1, group_id=-1, prog_num=4972, recursive=True) as chown_1325_4972:
                            chown_1325_4972()
            with Stage(r"copy", r"SoundStudio STG Control Panel v14.0.342.343", prog_num=4973):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4974) as should_copy_source_1326_4974:
                    should_copy_source_1326_4974()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", prog_num=4975):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", r".", delete_extraneous_files=True, prog_num=4976) as copy_dir_to_dir_1327_4976:
                            copy_dir_to_dir_1327_4976()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.app", where_to_unwtar=r".", prog_num=4977) as unwtar_1328_4977:
                            unwtar_1328_4977()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.app", user_id=-1, group_id=-1, prog_num=4978, recursive=True) as chown_1329_4978:
                            chown_1329_4978()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4979) as should_copy_source_1330_4979:
                    should_copy_source_1330_4979()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", prog_num=4980):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", r".", delete_extraneous_files=True, prog_num=4981) as copy_dir_to_dir_1331_4981:
                            copy_dir_to_dir_1331_4981()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundStudio STG Control.bundle", where_to_unwtar=r".", prog_num=4982) as unwtar_1332_4982:
                            unwtar_1332_4982()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.bundle", user_id=-1, group_id=-1, prog_num=4983, recursive=True) as chown_1333_4983:
                            chown_1333_4983()
            with Stage(r"copy", r"X-WSG Control Panel v14.0.342.343", prog_num=4984):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4985) as should_copy_source_1334_4985:
                    should_copy_source_1334_4985()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", prog_num=4986):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", r".", delete_extraneous_files=True, prog_num=4987) as copy_dir_to_dir_1335_4987:
                            copy_dir_to_dir_1335_4987()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.app", where_to_unwtar=r".", prog_num=4988) as unwtar_1336_4988:
                            unwtar_1336_4988()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.app", user_id=-1, group_id=-1, prog_num=4989, recursive=True) as chown_1337_4989:
                            chown_1337_4989()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4990) as should_copy_source_1338_4990:
                    should_copy_source_1338_4990()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", prog_num=4991):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=4992) as copy_dir_to_dir_1339_4992:
                            copy_dir_to_dir_1339_4992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/SoundGrid X-WSG Control.bundle", where_to_unwtar=r".", prog_num=4993) as unwtar_1340_4993:
                            unwtar_1340_4993()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.bundle", user_id=-1, group_id=-1, prog_num=4994, recursive=True) as chown_1341_4994:
                            chown_1341_4994()
            with Stage(r"copy", r"Yamaha SoundGrid IO Control Panel v14.0.342.343", prog_num=4995):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=4996) as should_copy_source_1342_4996:
                    should_copy_source_1342_4996()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", prog_num=4997):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", r".", delete_extraneous_files=True, prog_num=4998) as copy_dir_to_dir_1343_4998:
                            copy_dir_to_dir_1343_4998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.app", where_to_unwtar=r".", prog_num=4999) as unwtar_1344_4999:
                            unwtar_1344_4999()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.app", user_id=-1, group_id=-1, prog_num=5000, recursive=True) as chown_1345_5000:
                            chown_1345_5000()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r"/Library/Application Support/Waves/SoundGrid IO Modules", skip_progress_count=4, prog_num=5001) as should_copy_source_1346_5001:
                    should_copy_source_1346_5001()
                    with Stage(r"copy source", r"Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", prog_num=5002):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", r".", delete_extraneous_files=True, prog_num=5003) as copy_dir_to_dir_1347_5003:
                            copy_dir_to_dir_1347_5003()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/SoundGrid/IO Modules/Yamaha WSG Control.bundle", where_to_unwtar=r".", prog_num=5004) as unwtar_1348_5004:
                            unwtar_1348_5004()
                        with Chown(path=r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.bundle", user_id=-1, group_id=-1, prog_num=5005, recursive=True) as chown_1349_5005:
                            chown_1349_5005()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5006) as shell_command_1350_5006:
                shell_command_1350_5006()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=5007) as cd_stage_1351_5007:
            cd_stage_1351_5007()
            with Stage(r"copy", r"Waves Local Server v12.14.471.472", prog_num=5008):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=5, prog_num=5009) as should_copy_source_1352_5009:
                    should_copy_source_1352_5009()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=5010):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=5011) as copy_dir_to_dir_1353_5011:
                            copy_dir_to_dir_1353_5011()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=5012) as unwtar_1354_5012:
                            unwtar_1354_5012()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=5013, recursive=True) as chown_1355_5013:
                            chown_1355_5013()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5014) as if_1356_5014:
                            if_1356_5014()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=5015) as cd_stage_1357_5015:
            cd_stage_1357_5015()
            with Stage(r"copy", r"WavesPluginServer_V14_2 v13.6.444.720", prog_num=5016):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=5017) as should_copy_source_1358_5017:
                    should_copy_source_1358_5017()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", prog_num=5018):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=5019) as copy_dir_to_dir_1359_5019:
                            copy_dir_to_dir_1359_5019()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/WavesPluginServer/WavesPluginServerV14.2.bundle", where_to_unwtar=r".", prog_num=5020) as unwtar_1360_5020:
                            unwtar_1360_5020()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle", user_id=-1, group_id=-1, prog_num=5021, recursive=True) as chown_1361_5021:
                            chown_1361_5021()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/com.waves.wps.agent.plist", r"/Library/LaunchAgents/com.waves.wps.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5022) as if_1362_5022:
                            if_1362_5022()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=5023) as cd_stage_1363_5023:
            cd_stage_1363_5023()
            with Stage(r"copy", r"WaveShell1-AU 14.12 v14.12.90.381", prog_num=5024):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=5025) as should_copy_source_1364_5025:
                    should_copy_source_1364_5025()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.12.component", prog_num=5026):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", r".", delete_extraneous_files=True, prog_num=5027) as copy_dir_to_dir_1365_5027:
                            copy_dir_to_dir_1365_5027()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.12.component", where_to_unwtar=r".", prog_num=5028) as unwtar_1366_5028:
                            unwtar_1366_5028()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=5029, recursive=True) as chown_1367_5029:
                            chown_1367_5029()
                        with BreakHardLink(r"WaveShell1-AU 14.12.component/Contents/Info.plist", prog_num=5030) as break_hard_link_1368_5030:
                            break_hard_link_1368_5030()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.12.component"', ignore_all_errors=True, prog_num=5031) as shell_command_1369_5031:
                            shell_command_1369_5031()
                        with Chown(path=r"WaveShell1-AU 14.12.component", user_id=-1, group_id=-1, prog_num=5032, recursive=True) as chown_1370_5032:
                            chown_1370_5032()
                        with Chmod(path=r"WaveShell1-AU 14.12.component", mode="a+rwX", prog_num=5033, recursive=True) as chmod_1371_5033:
                            chmod_1371_5033()
            with Stage(r"copy", r"WaveShell1-AU 14.21 v14.21.96.553", prog_num=5034):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=5035) as should_copy_source_1372_5035:
                    should_copy_source_1372_5035()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 14.21.component", prog_num=5036):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", r".", delete_extraneous_files=True, prog_num=5037) as copy_dir_to_dir_1373_5037:
                            copy_dir_to_dir_1373_5037()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-AU 14.21.component", where_to_unwtar=r".", prog_num=5038) as unwtar_1374_5038:
                            unwtar_1374_5038()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=5039, recursive=True) as chown_1375_5039:
                            chown_1375_5039()
                        with BreakHardLink(r"WaveShell1-AU 14.21.component/Contents/Info.plist", prog_num=5040) as break_hard_link_1376_5040:
                            break_hard_link_1376_5040()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 14.21.component"', ignore_all_errors=True, prog_num=5041) as shell_command_1377_5041:
                            shell_command_1377_5041()
                        with Chown(path=r"WaveShell1-AU 14.21.component", user_id=-1, group_id=-1, prog_num=5042, recursive=True) as chown_1378_5042:
                            chown_1378_5042()
                        with Chmod(path=r"WaveShell1-AU 14.21.component", mode="a+rwX", prog_num=5043, recursive=True) as chmod_1379_5043:
                            chmod_1379_5043()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=5044) as cd_stage_1380_5044:
            cd_stage_1380_5044()
            with Stage(r"copy", r"WaveShell OBS v14.21.96.553", prog_num=5045):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5046) as should_copy_source_1381_5046:
                    should_copy_source_1381_5046()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=5047):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=5048) as copy_dir_to_dir_1382_5048:
                            copy_dir_to_dir_1382_5048()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=5049) as unwtar_1383_5049:
                            unwtar_1383_5049()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=5050, recursive=True) as chown_1384_5050:
                            chown_1384_5050()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=5051) as shell_command_1385_5051:
                            shell_command_1385_5051()
            with Stage(r"copy", r"WaveShell1-VST 14.12 v14.12.90.381", prog_num=5052):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5053) as should_copy_source_1386_5053:
                    should_copy_source_1386_5053()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.12.vst", prog_num=5054):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", r".", delete_extraneous_files=True, prog_num=5055) as copy_dir_to_dir_1387_5055:
                            copy_dir_to_dir_1387_5055()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.12.vst", where_to_unwtar=r".", prog_num=5056) as unwtar_1388_5056:
                            unwtar_1388_5056()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.12.vst", user_id=-1, group_id=-1, prog_num=5057, recursive=True) as chown_1389_5057:
                            chown_1389_5057()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.12.vst"', ignore_all_errors=True, prog_num=5058) as shell_command_1390_5058:
                            shell_command_1390_5058()
            with Stage(r"copy", r"WaveShell1-VST 14.21 v14.21.96.553", prog_num=5059):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=5060) as should_copy_source_1391_5060:
                    should_copy_source_1391_5060()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST 14.21.vst", prog_num=5061):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", r".", delete_extraneous_files=True, prog_num=5062) as copy_dir_to_dir_1392_5062:
                            copy_dir_to_dir_1392_5062()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST 14.21.vst", where_to_unwtar=r".", prog_num=5063) as unwtar_1393_5063:
                            unwtar_1393_5063()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.21.vst", user_id=-1, group_id=-1, prog_num=5064, recursive=True) as chown_1394_5064:
                            chown_1394_5064()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST 14.21.vst"', ignore_all_errors=True, prog_num=5065) as shell_command_1395_5065:
                            shell_command_1395_5065()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=5066) as cd_stage_1396_5066:
            cd_stage_1396_5066()
            with Stage(r"copy", r"WaveShell1-VST3 14.12 v14.12.90.381", prog_num=5067):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=5068) as should_copy_source_1397_5068:
                    should_copy_source_1397_5068()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.12.vst3", prog_num=5069):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", r".", delete_extraneous_files=True, prog_num=5070) as copy_dir_to_dir_1398_5070:
                            copy_dir_to_dir_1398_5070()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.12.vst3", where_to_unwtar=r".", prog_num=5071) as unwtar_1399_5071:
                            unwtar_1399_5071()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.12.vst3", user_id=-1, group_id=-1, prog_num=5072, recursive=True) as chown_1400_5072:
                            chown_1400_5072()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.12.vst3"', ignore_all_errors=True, prog_num=5073) as shell_command_1401_5073:
                            shell_command_1401_5073()
            with Stage(r"copy", r"WaveShell1-VST3 14.21 v14.21.96.553", prog_num=5074):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=5075) as should_copy_source_1402_5075:
                    should_copy_source_1402_5075()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 14.21.vst3", prog_num=5076):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", r".", delete_extraneous_files=True, prog_num=5077) as copy_dir_to_dir_1403_5077:
                            copy_dir_to_dir_1403_5077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-VST3 14.21.vst3", where_to_unwtar=r".", prog_num=5078) as unwtar_1404_5078:
                            unwtar_1404_5078()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.21.vst3", user_id=-1, group_id=-1, prog_num=5079, recursive=True) as chown_1405_5079:
                            chown_1405_5079()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 14.21.vst3"', ignore_all_errors=True, prog_num=5080) as shell_command_1406_5080:
                            shell_command_1406_5080()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5081) as cd_stage_1407_5081:
            cd_stage_1407_5081()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 14.12 v14.12.90.381", prog_num=5082):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=5083) as should_copy_source_1408_5083:
                    should_copy_source_1408_5083()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", prog_num=5084):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", r".", delete_extraneous_files=True, prog_num=5085) as copy_dir_to_dir_1409_5085:
                            copy_dir_to_dir_1409_5085()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Shells/WaveShell1-WPAPI_2 14.12.bundle", where_to_unwtar=r".", prog_num=5086) as unwtar_1410_5086:
                            unwtar_1410_5086()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 14.12.bundle", user_id=-1, group_id=-1, prog_num=5087, recursive=True) as chown_1411_5087:
                            chown_1411_5087()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=5088) as shell_command_1412_5088:
                            shell_command_1412_5088()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=5089) as script_command_1413_5089:
                            script_command_1413_5089()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=5090) as shell_command_1414_5090:
                            shell_command_1414_5090()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5091) as create_symlink_1415_5091:
                create_symlink_1415_5091()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=5092) as create_symlink_1416_5092:
                create_symlink_1416_5092()
        with CdStage(r"copy_to_folder", r"/Users/Shared/Waves/SoundGrid Studio/Templates", prog_num=5093) as cd_stage_1417_5093:
            cd_stage_1417_5093()
            with Stage(r"copy", r"SoundGrid Studio Sessions Structure", prog_num=5094):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r"/Users/Shared/Waves/SoundGrid Studio/Templates", skip_progress_count=3, prog_num=5095) as should_copy_source_1418_5095:
                    should_copy_source_1418_5095()
                    with Stage(r"copy source", r"Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", prog_num=5096):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Common/SoundGrid/Empty Sessions/SGStudio2/Empty Session.sgst", r".", prog_num=5097) as copy_file_to_dir_1419_5097:
                            copy_file_to_dir_1419_5097()
                        with ChmodAndChown(path=r"Empty Session.sgst", mode="a+rw", user_id=-1, group_id=-1, prog_num=5098) as chmod_and_chown_1420_5098:
                            chmod_and_chown_1420_5098()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=5099) as cd_stage_1421_5099:
            cd_stage_1421_5099()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Lamps/Vocal/Vocal 2 (Lead).xps", prog_num=5100) as rm_file_or_dir_1422_5100:
                rm_file_or_dir_1422_5100()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Factory", prog_num=5101) as rm_file_or_dir_1423_5101:
                rm_file_or_dir_1423_5101()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/GroupOrder.xps", prog_num=5102) as rm_file_or_dir_1424_5102:
                rm_file_or_dir_1424_5102()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/StudioRack/Artists/Kori Andres", prog_num=5103) as rm_file_or_dir_1425_5103:
                rm_file_or_dir_1425_5103()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/Symphony II SoundGrid User Guide", prog_num=5104) as rm_file_or_dir_1426_5104:
            rm_file_or_dir_1426_5104()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=5105) as rm_file_or_dir_1427_5105:
            rm_file_or_dir_1427_5105()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack and Network Streaming with HD-HDX-HDNative - external Server.emo", prog_num=5106) as rm_file_or_dir_1428_5106:
            rm_file_or_dir_1428_5106()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack Processing for HD-HDX-HDNative Systems - external Server.emo", prog_num=5107) as rm_file_or_dir_1429_5107:
            rm_file_or_dir_1429_5107()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Mixing with StudioRack - external Server.emo", prog_num=5108) as rm_file_or_dir_1430_5108:
            rm_file_or_dir_1430_5108()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Recording thru eMotion Mixer - external Server.emo", prog_num=5109) as rm_file_or_dir_1431_5109:
            rm_file_or_dir_1431_5109()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and External Mixing  - external Server.emo", prog_num=5110) as rm_file_or_dir_1432_5110:
            rm_file_or_dir_1432_5110()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and Monitoring - external Server.emo", prog_num=5111) as rm_file_or_dir_1433_5111:
            rm_file_or_dir_1433_5111()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=5112) as rm_file_or_dir_1434_5112:
            rm_file_or_dir_1434_5112()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack and Network Streaming with HD-HDX-HDNative.emo", prog_num=5113) as rm_file_or_dir_1435_5113:
            rm_file_or_dir_1435_5113()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack Processing for HD-HDX-HDNative Systems.emo", prog_num=5114) as rm_file_or_dir_1436_5114:
            rm_file_or_dir_1436_5114()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Mixing with StudioRack.emo", prog_num=5115) as rm_file_or_dir_1437_5115:
            rm_file_or_dir_1437_5115()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Recording thru eMotion Mixer.emo", prog_num=5116) as rm_file_or_dir_1438_5116:
            rm_file_or_dir_1438_5116()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and External Mixing.emo", prog_num=5117) as rm_file_or_dir_1439_5117:
            rm_file_or_dir_1439_5117()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and Monitoring.emo", prog_num=5118) as rm_file_or_dir_1440_5118:
            rm_file_or_dir_1440_5118()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS DLI REC-PB Standalone.emo", prog_num=5119) as rm_file_or_dir_1441_5119:
            rm_file_or_dir_1441_5119()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=5120) as rm_file_or_dir_1442_5120:
            rm_file_or_dir_1442_5120()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid D User Guide.pdf", prog_num=5121) as rm_file_or_dir_1443_5121:
            rm_file_or_dir_1443_5121()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid M User Guide.pdf", prog_num=5122) as rm_file_or_dir_1444_5122:
            rm_file_or_dir_1444_5122()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid/Documents/._DiGiGrid Q User Guide.pdf", prog_num=5123) as rm_file_or_dir_1445_5123:
            rm_file_or_dir_1445_5123()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - Recording thru eMotion Mixer.emo", prog_num=5124) as rm_file_or_dir_1446_5124:
            rm_file_or_dir_1446_5124()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - REC-PB Standalone.emo", prog_num=5125) as rm_file_or_dir_1447_5125:
            rm_file_or_dir_1447_5125()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - StudioRack Processing and Monitoring.emo", prog_num=5126) as rm_file_or_dir_1448_5126:
            rm_file_or_dir_1448_5126()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - Recording thru eMotion Mixer - external Server.emo", prog_num=5127) as rm_file_or_dir_1449_5127:
            rm_file_or_dir_1449_5127()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - REC-PB Standalone.emo", prog_num=5128) as rm_file_or_dir_1450_5128:
            rm_file_or_dir_1450_5128()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - StudioRack Processing and Monitoring - external Server.emo", prog_num=5129) as rm_file_or_dir_1451_5129:
            rm_file_or_dir_1451_5129()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/MGB MGO REC-PB Standalone.emo", prog_num=5130) as rm_file_or_dir_1452_5130:
            rm_file_or_dir_1452_5130()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/2x MGB MGO REC-PB 96Khz Standalone.emo", prog_num=5131) as rm_file_or_dir_1453_5131:
            rm_file_or_dir_1453_5131()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=5132) as shell_command_1454_5132:
            shell_command_1454_5132()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=5133) as script_command_1455_5133:
            script_command_1455_5133()
        with ShellCommand(r"echo This installation requires that you restart your computer.", message=r"Restart_required_IID post-install step 1", prog_num=5134) as shell_command_1456_5134:
            shell_command_1456_5134()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=ScriptCommand(r'echo "#!/bin/bash" >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"; echo installer -pkg \"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg\" -target / >> "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"; chmod a+rwx "/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh" '), if_false=ShellCommand(r'sudo installer -pkg "/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg" -target /', message=r"Installing SoundGrid Driver V14.12", ignore_all_errors=True), prog_num=5135) as if_1457_5135:
            if_1457_5135()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudioModulesFolder_ScanView.txt", prog_num=5136) as rm_file_or_dir_1458_5136:
            rm_file_or_dir_1458_5136()
        with RmFileOrDir(r"/Library/Application Support/Waves/Session Converters/SampleTestConverter.bundle", prog_num=5137) as rm_file_or_dir_1459_5137:
            rm_file_or_dir_1459_5137()
        with ShellCommand(r"""osascript -e 'tell application "System Events" to delete login item "SoundGrid Studio"' """, ignore_all_errors=True, prog_num=5138) as shell_command_1460_5138:
            shell_command_1460_5138()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.NoSplashScreen.sh", prog_num=5139) as rm_file_or_dir_1461_5139:
            rm_file_or_dir_1461_5139()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/SoundGridStudioSilent.app", prog_num=5140) as rm_file_or_dir_1462_5140:
            rm_file_or_dir_1462_5140()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/SoundGridStudioSilent.app", prog_num=5141) as rm_file_or_dir_1463_5141:
            rm_file_or_dir_1463_5141()
        with RmFileOrDir(r"/Applications/Waves/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=5142) as rm_file_or_dir_1464_5142:
            rm_file_or_dir_1464_5142()
        with ShellCommand(r'chmod a=r,u+w "/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=5143) as shell_command_1465_5143:
            shell_command_1465_5143()
        with If(IsFile(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/SGStudio.Mixer SoundGrid.preferences"), if_false=CopyFileToFile(r"/Applications/Waves/SoundGrid Studio/SoundGrid Studio.app/Contents/Resources/com.WavesAudio.SoundGridStudioSilent.plist", r"${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=5144) as if_1466_5144:
            if_1466_5144()
        with ShellCommand(r'chmod a=r,u+w "${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=5145) as shell_command_1467_5145:
            shell_command_1467_5145()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/SoundGrid" -c', ignore_all_errors=True, prog_num=5146) as shell_command_1468_5146:
            shell_command_1468_5146()
        with ScriptCommand(r'if [ -f "/Applications/Waves/SoundGrid"/Icon? ]; then chmod a+rw "/Applications/Waves/SoundGrid"/Icon?; fi', prog_num=5147) as script_command_1469_5147:
            script_command_1469_5147()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=5148) as rm_file_or_dir_1470_5148:
            rm_file_or_dir_1470_5148()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=5149) as touch_1471_5149:
            touch_1471_5149()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst/Contents/Info.plist", Touch, r"path", prog_num=5150) as glober_1472_5150:
            glober_1472_5150()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=5151) as glober_1473_5151:
            glober_1473_5151()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=5152) as glober_1474_5152:
            glober_1474_5152()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=5153) as glober_1475_5153:
            glober_1475_5153()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=5154) as glober_1476_5154:
            glober_1476_5154()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=5155) as shell_command_1477_5155:
            shell_command_1477_5155()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V14" -c', ignore_all_errors=True, prog_num=5156) as shell_command_1478_5156:
            shell_command_1478_5156()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V14"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V14"/Icon?; fi', prog_num=5157) as script_command_1479_5157:
            script_command_1479_5157()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=5158) as if_1480_5158:
            if_1480_5158()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=5159) as if_1481_5159:
            if_1481_5159()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=5160) as if_1482_5160:
            if_1482_5160()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=5161) as if_1483_5161:
            if_1483_5161()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=5162) as make_dir_1484_5162:
            make_dir_1484_5162()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=5163) as chmod_1485_5163:
            chmod_1485_5163()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", prog_num=5164) as make_dir_1486_5164:
            make_dir_1486_5164()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=5165) as chmod_1487_5165:
            chmod_1487_5165()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=5166) as chmod_1488_5166:
            chmod_1488_5166()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V14.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=5167) as chmod_1489_5167:
            chmod_1489_5167()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=5168) as chmod_1490_5168:
            chmod_1490_5168()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=5169) as shell_command_1491_5169:
            shell_command_1491_5169()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=5170) as script_command_1492_5170:
            script_command_1492_5170()
    with Stage(r"post-copy", prog_num=5171):
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=5172) as make_dir_1493_5172:
            make_dir_1493_5172()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V14/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=5173) as copy_file_to_file_1494_5173:
            copy_file_to_file_1494_5173()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5174) as chmod_1495_5174:
            chmod_1495_5174()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5175) as chmod_1496_5175:
            chmod_1496_5175()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Library/Application Support/Waves/Central/V14/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=5176) as copy_file_to_file_1497_5176:
            copy_file_to_file_1497_5176()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5177) as chmod_1498_5177:
            chmod_1498_5177()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml", hard_links=False, copy_owner=True, prog_num=5178) as copy_file_to_file_1499_5178:
            copy_file_to_file_1499_5178()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=5179) as chmod_1500_5179:
            chmod_1500_5179()
        Progress(r"Done copy", prog_num=5180)()
        Progress(r"Done synccopy", prog_num=5181)()
    with Stage(r"post", prog_num=5182):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=5183) as make_dir_1501_5183:
            make_dir_1501_5183()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V14_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/V14_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=5184) as copy_file_to_file_1502_5184:
            copy_file_to_file_1502_5184()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping", chowner=True, prog_num=5185) as make_dir_1503_5185:
            make_dir_1503_5185()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=5186) as copy_file_to_file_1504_5186:
            copy_file_to_file_1504_5186()
        with MakeDir(r"/Library/Application Support/Waves/Central/V14", chowner=True, prog_num=5187) as make_dir_1505_5187:
            make_dir_1505_5187()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V14/bookkeeping/183/index.yaml", r"/Library/Application Support/Waves/Central/V14/index.yaml", hard_links=False, copy_owner=True, prog_num=5188) as copy_file_to_file_1506_5188:
            copy_file_to_file_1506_5188()

with Stage(r"epilog", prog_num=5189):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139.py", prog_num=5190) as patch_py_batch_with_timings_1507_5190:
        patch_py_batch_with_timings_1507_5190()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


