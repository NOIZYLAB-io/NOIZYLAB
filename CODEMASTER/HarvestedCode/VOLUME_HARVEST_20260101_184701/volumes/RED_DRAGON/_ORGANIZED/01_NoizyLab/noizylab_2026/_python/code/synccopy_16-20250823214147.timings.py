# Creation time: 23-08-25_21-41
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 1593
PythonBatchCommandBase.running_progress = 604
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=605):  # 0m:0.000s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250823214147"
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
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NjAzNTcwOH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU1OTk5NDA4fX19XX0_;CloudFront-Signature=LNJzIzz7K-d92OmijtF3GxNPfvxfSCiByr-R046R~n2PuwNmQBCDUifzIhKh9In79Fhl3b7fcF4H2~chwSrdEC8pOh23eR9M6-KdH-Nb1eiDmV3bjHlzH82ynk3pJaj4Vf-rHDA8Bl7Tg~~xszDgFUkHzrjTBx9YZgd1fbodKd0o7ihkxh86RcWF5PziUSYQOh5jXUhuSqFECP2VHR9Am0o4qv0EuYQsGY4ZVvId27Kk8TlH1Ldki8h-LkWmnMXNB7tltjRWNKhG5lmkUEnatrt5VjCs28PM0G6UeUZeUPWmkaQS4x9s-e-WuOQnO5KpZruZRc-RFOxAzJI0mgrbGg__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NjAzNTcwOH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU1OTk5NDA4fX19XX0_;CloudFront-Signature=LNJzIzz7K-d92OmijtF3GxNPfvxfSCiByr-R046R~n2PuwNmQBCDUifzIhKh9In79Fhl3b7fcF4H2~chwSrdEC8pOh23eR9M6-KdH-Nb1eiDmV3bjHlzH82ynk3pJaj4Vf-rHDA8Bl7Tg~~xszDgFUkHzrjTBx9YZgd1fbodKd0o7ihkxh86RcWF5PziUSYQOh5jXUhuSqFECP2VHR9Am0o4qv0EuYQsGY4ZVvId27Kk8TlH1Ldki8h-LkWmnMXNB7tltjRWNKhG5lmkUEnatrt5VjCs28PM0G6UeUZeUPWmkaQS4x9s-e-WuOQnO5KpZruZRc-RFOxAzJI0mgrbGg__"
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
    config_vars['MAIN_INSTALL_TARGETS'] = (r"11aa65c2-9605-4b66-852a-19c00a8cad0a", r"2f8f4c91-26ba-4be8-8310-d0d605b4eab8", r"__UPDATE_INSTALLED_ITEMS__", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"c4fb99f7-fc70-4b1f-999a-9920272bce03", r"fc52bedf-6e86-4353-bb34-0847d8e9e78a")
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250823214147.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
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
    config_vars['REQUIRE_REPO_REV'] = 9
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
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"after-sync-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 984
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250823214147.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-07-06 12:14:08.392126"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.6.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = ""
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"COMMON_PLUGIN_DEPENDS_IID", r"ChainersChildExcludeList_IID", r"Clarity_Vx_DeReverb_IID", r"Clarity_Vx_DeReverb_Network__Data_Folders__IID", r"Clarity_Vx_DeReverb_Pro_IID", r"Clarity_Vx_DeReverb_Pro__Presets__IID", r"Clarity_Vx_DeReverb__Presets__IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx_Pro_IID", r"Clarity_Vx_Pro__Presets__IID", r"Clarity_Vx__Presets__IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_V16_1_IID", r"Get_General_Icons_IID", r"Immersive_Wrapper_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"IntelDlls_IID", r"LicenseNotifications_V16_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"ONNXRUNTIME_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PresetBrowser_V16_1_IID", r"Shutdown_Servers_IID", r"V9_V10_Organizer_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AAX_16_2_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_AU_16_2_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_VST_3_V16_2_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell1_WPAPI_2_16_2_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesLib1_16_0_74_IID", r"WavesLib1_16_2_30_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-07-06 12:14:08.392126 bm-mac-ado9"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"ttpossfxrtewyyie"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"Clarity_Vx_DeReverb_IID", r"Clarity_Vx_DeReverb_Pro_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Pro_IID", r"Immersive_Wrapper_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = (r"ChainersChildExcludeList_IID", r"Clarity_Vx_DeReverb_Network__Data_Folders__IID", r"Clarity_Vx_Onnx__Data_Folders__IID")
    config_vars['__NOW__'] = r"2025-08-23 21:43:23.406661"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 55623655
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 68
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

with PythonBatchRuntime(r"synccopy", prog_num=606):  # 1m:1.972s
    with Stage(r"begin", prog_num=607):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=608):  # 0m:0.011s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=609) as copy_file_to_file_001_609:  # 0m:0.006s
            copy_file_to_file_001_609()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=610) as copy_file_to_file_002_610:  # 0m:0.005s
            copy_file_to_file_002_610()
    with Stage(r"sync", prog_num=611):  # 0m:10.331s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=612) as shell_command_003_612:  # 0m:0.019s
            shell_command_003_612()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=613) as shell_command_004_613:  # 0m:0.017s
            shell_command_004_613()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=614) as shell_command_005_614:  # 0m:1.060s
            shell_command_005_614()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=615) as shell_command_006_615:  # 0m:1.061s
            shell_command_006_615()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=616) as shell_command_007_616:  # 0m:0.008s
            shell_command_007_616()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=617) as shell_command_008_617:  # 0m:1.081s
            shell_command_008_617()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=618) as shell_command_009_618:  # 0m:0.008s
            shell_command_009_618()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=619) as shell_command_010_619:  # 0m:0.005s
            shell_command_010_619()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=620) as shell_command_011_620:  # 0m:0.148s
            shell_command_011_620()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=621):  # 0m:6.922s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=622) as make_dir_012_622:  # 0m:0.007s
                make_dir_012_622()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=623) as cd_013_623:  # 0m:6.914s
                cd_013_623()
                with Stage(r"remove_redundant_files_in_sync_folder", prog_num=624):  # 0m:0.456s
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139", prog_num=625) as rm_file_014_625:  # 0m:0.001s
                        rm_file_014_625()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139.bin.wtar.aa", prog_num=626) as rm_file_015_626:  # 0m:0.001s
                        rm_file_015_626()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139.data", prog_num=627) as rm_file_016_627:  # 0m:0.001s
                        rm_file_016_627()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139.nnw.wtar.aa", prog_num=628) as rm_file_017_628:  # 0m:0.000s
                        rm_file_017_628()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139.nnw.wtar.ab", prog_num=629) as rm_file_018_629:  # 0m:0.000s
                        rm_file_018_629()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D139/D139.stats", prog_num=630) as rm_file_019_630:  # 0m:0.000s
                        rm_file_019_630()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140", prog_num=631) as rm_file_020_631:  # 0m:0.000s
                        rm_file_020_631()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140.bin.wtar.aa", prog_num=632) as rm_file_021_632:  # 0m:0.000s
                        rm_file_021_632()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140.data", prog_num=633) as rm_file_022_633:  # 0m:0.000s
                        rm_file_022_633()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140.nnw.wtar.aa", prog_num=634) as rm_file_023_634:  # 0m:0.000s
                        rm_file_023_634()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140.nnw.wtar.ab", prog_num=635) as rm_file_024_635:  # 0m:0.000s
                        rm_file_024_635()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D140/D140.stats", prog_num=636) as rm_file_025_636:  # 0m:0.000s
                        rm_file_025_636()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141", prog_num=637) as rm_file_026_637:  # 0m:0.000s
                        rm_file_026_637()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141.bin.wtar.aa", prog_num=638) as rm_file_027_638:  # 0m:0.000s
                        rm_file_027_638()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141.data", prog_num=639) as rm_file_028_639:  # 0m:0.000s
                        rm_file_028_639()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141.nnw.wtar.aa", prog_num=640) as rm_file_029_640:  # 0m:0.000s
                        rm_file_029_640()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141.nnw.wtar.ab", prog_num=641) as rm_file_030_641:  # 0m:0.000s
                        rm_file_030_641()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D141/D141.stats", prog_num=642) as rm_file_031_642:  # 0m:0.001s
                        rm_file_031_642()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142", prog_num=643) as rm_file_032_643:  # 0m:0.000s
                        rm_file_032_643()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.bin.wtar.aa", prog_num=644) as rm_file_033_644:  # 0m:0.000s
                        rm_file_033_644()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.bin.wtar.ab", prog_num=645) as rm_file_034_645:  # 0m:0.000s
                        rm_file_034_645()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.data", prog_num=646) as rm_file_035_646:  # 0m:0.000s
                        rm_file_035_646()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.nnw.wtar.aa", prog_num=647) as rm_file_036_647:  # 0m:0.000s
                        rm_file_036_647()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.nnw.wtar.ab", prog_num=648) as rm_file_037_648:  # 0m:0.000s
                        rm_file_037_648()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D142/D142.stats", prog_num=649) as rm_file_038_649:  # 0m:0.000s
                        rm_file_038_649()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145", prog_num=650) as rm_file_039_650:  # 0m:0.000s
                        rm_file_039_650()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.bin.wtar.aa", prog_num=651) as rm_file_040_651:  # 0m:0.000s
                        rm_file_040_651()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.bin.wtar.ab", prog_num=652) as rm_file_041_652:  # 0m:0.000s
                        rm_file_041_652()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.data", prog_num=653) as rm_file_042_653:  # 0m:0.000s
                        rm_file_042_653()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.nnw.wtar.aa", prog_num=654) as rm_file_043_654:  # 0m:0.001s
                        rm_file_043_654()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.nnw.wtar.ab", prog_num=655) as rm_file_044_655:  # 0m:0.000s
                        rm_file_044_655()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D145/D145.stats", prog_num=656) as rm_file_045_656:  # 0m:0.000s
                        rm_file_045_656()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146", prog_num=657) as rm_file_046_657:  # 0m:0.000s
                        rm_file_046_657()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146.bin.wtar.aa", prog_num=658) as rm_file_047_658:  # 0m:0.000s
                        rm_file_047_658()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146.data", prog_num=659) as rm_file_048_659:  # 0m:0.000s
                        rm_file_048_659()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146.nnw.wtar.aa", prog_num=660) as rm_file_049_660:  # 0m:0.000s
                        rm_file_049_660()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146.nnw.wtar.ab", prog_num=661) as rm_file_050_661:  # 0m:0.000s
                        rm_file_050_661()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/D146/D146.stats", prog_num=662) as rm_file_051_662:  # 0m:0.000s
                        rm_file_051_662()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L", prog_num=663) as rm_file_052_663:  # 0m:0.000s
                        rm_file_052_663()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.bin.wtar.aa", prog_num=664) as rm_file_053_664:  # 0m:0.000s
                        rm_file_053_664()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.bin.wtar.ab", prog_num=665) as rm_file_054_665:  # 0m:0.000s
                        rm_file_054_665()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.data", prog_num=666) as rm_file_055_666:  # 0m:0.000s
                        rm_file_055_666()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.nnw.wtar.aa", prog_num=667) as rm_file_056_667:  # 0m:0.001s
                        rm_file_056_667()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.nnw.wtar.ab", prog_num=668) as rm_file_057_668:  # 0m:0.000s
                        rm_file_057_668()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127L/V127L.stats", prog_num=669) as rm_file_058_669:  # 0m:0.000s
                        rm_file_058_669()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH", prog_num=670) as rm_file_059_670:  # 0m:0.000s
                        rm_file_059_670()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH.bin.wtar.aa", prog_num=671) as rm_file_060_671:  # 0m:0.000s
                        rm_file_060_671()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH.data", prog_num=672) as rm_file_061_672:  # 0m:0.000s
                        rm_file_061_672()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH.nnw.wtar.aa", prog_num=673) as rm_file_062_673:  # 0m:0.000s
                        rm_file_062_673()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH.nnw.wtar.ab", prog_num=674) as rm_file_063_674:  # 0m:0.000s
                        rm_file_063_674()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V127_HH/V127_HH.stats", prog_num=675) as rm_file_064_675:  # 0m:0.000s
                        rm_file_064_675()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143", prog_num=676) as rm_file_065_676:  # 0m:0.000s
                        rm_file_065_676()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.bin.wtar.aa", prog_num=677) as rm_file_066_677:  # 0m:0.001s
                        rm_file_066_677()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.bin.wtar.ab", prog_num=678) as rm_file_067_678:  # 0m:0.000s
                        rm_file_067_678()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.data", prog_num=679) as rm_file_068_679:  # 0m:0.000s
                        rm_file_068_679()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.nnw.wtar.aa", prog_num=680) as rm_file_069_680:  # 0m:0.000s
                        rm_file_069_680()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.nnw.wtar.ab", prog_num=681) as rm_file_070_681:  # 0m:0.000s
                        rm_file_070_681()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V143/V143.stats", prog_num=682) as rm_file_071_682:  # 0m:0.000s
                        rm_file_071_682()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144", prog_num=683) as rm_file_072_683:  # 0m:0.000s
                        rm_file_072_683()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.bin.wtar.aa", prog_num=684) as rm_file_073_684:  # 0m:0.000s
                        rm_file_073_684()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.bin.wtar.ab", prog_num=685) as rm_file_074_685:  # 0m:0.000s
                        rm_file_074_685()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.data", prog_num=686) as rm_file_075_686:  # 0m:0.000s
                        rm_file_075_686()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.nnw.wtar.aa", prog_num=687) as rm_file_076_687:  # 0m:0.000s
                        rm_file_076_687()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.nnw.wtar.ab", prog_num=688) as rm_file_077_688:  # 0m:0.001s
                        rm_file_077_688()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V144/V144.stats", prog_num=689) as rm_file_078_689:  # 0m:0.000s
                        rm_file_078_689()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147", prog_num=690) as rm_file_079_690:  # 0m:0.000s
                        rm_file_079_690()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147.bin.wtar.aa", prog_num=691) as rm_file_080_691:  # 0m:0.000s
                        rm_file_080_691()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147.data", prog_num=692) as rm_file_081_692:  # 0m:0.000s
                        rm_file_081_692()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147.nnw.wtar.aa", prog_num=693) as rm_file_082_693:  # 0m:0.000s
                        rm_file_082_693()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147.nnw.wtar.ab", prog_num=694) as rm_file_083_694:  # 0m:0.000s
                        rm_file_083_694()
                    with RmFile(r"Common/Data/Clarity Vx DeReverb/Network/V147/V147.stats", prog_num=695) as rm_file_084_695:  # 0m:0.000s
                        rm_file_084_695()
                    with RemoveEmptyFolders(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=696) as remove_empty_folders_085_696:  # 0m:0.428s
                        remove_empty_folders_085_696()
                Progress(r"304 files already in cache", own_progress_count=304, prog_num=1000)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=35, prog_num=1035) as create_sync_folders_086_1035:  # 0m:0.099s
                    create_sync_folders_086_1035()
                Progress(r"Downloading with 50 processes in parallel", prog_num=1036)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=1037)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.py_curl/dl-00", total_files_to_download=68, previously_downloaded_files=0, total_bytes_to_download=55623655, own_progress_count=58, prog_num=1095, report_own_progress=False) as curl_with_internal_parallel_087_1095:  # 0m:4.311s
                    curl_with_internal_parallel_087_1095()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.py_curl/dl-01", total_files_to_download=68, previously_downloaded_files=58, total_bytes_to_download=55623655, own_progress_count=10, prog_num=1105, report_own_progress=False) as curl_with_internal_parallel_088_1105:  # 0m:0.274s
                    curl_with_internal_parallel_088_1105()
                Progress(r"Downloading 68 files done", prog_num=1106)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=1107) as run_in_thread_089_1107:  # 0m:0.001s
                    run_in_thread_089_1107()
                Progress(r"Check checksum ...", prog_num=1108)()  # 0m:0.001s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=68, prog_num=1176) as check_download_folder_checksum_090_1176:  # 0m:1.115s
                    check_download_folder_checksum_090_1176()
                with Stage(r"post_sync", prog_num=1177):  # 0m:0.656s
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16...", prog_num=1178)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=1179, recursive=True) as chmod_and_chown_091_1179:  # 0m:0.645s
                        chmod_and_chown_091_1179()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=1180) as copy_file_to_file_092_1180:  # 0m:0.010s
                        copy_file_to_file_092_1180()
            Progress(r"Done sync", prog_num=1181)()  # 0m:0.000s
    with Stage(r"copy", prog_num=1182):  # 0m:51.527s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1183)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=1184):  # 0m:0.113s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=1185) as make_dir_093_1185:  # 0m:0.007s
                make_dir_093_1185()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=1186) as make_dir_094_1186:  # 0m:0.004s
                make_dir_094_1186()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx/onnx/Network", chowner=True, prog_num=1187) as make_dir_095_1187:  # 0m:0.005s
                make_dir_095_1187()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=1188) as make_dir_096_1188:  # 0m:0.005s
                make_dir_096_1188()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=1189) as make_dir_097_1189:  # 0m:0.004s
                make_dir_097_1189()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=1190) as make_dir_098_1190:  # 0m:0.004s
                make_dir_098_1190()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=1191) as make_dir_099_1191:  # 0m:0.005s
                make_dir_099_1191()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=1192) as make_dir_100_1192:  # 0m:0.004s
                make_dir_100_1192()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=1193) as make_dir_101_1193:  # 0m:0.006s
                make_dir_101_1193()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=1194) as make_dir_102_1194:  # 0m:0.005s
                make_dir_102_1194()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=1195) as make_dir_103_1195:  # 0m:0.006s
                make_dir_103_1195()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=1196) as make_dir_104_1196:  # 0m:0.004s
                make_dir_104_1196()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=1197) as make_dir_105_1197:  # 0m:0.005s
                make_dir_105_1197()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=1198) as make_dir_106_1198:  # 0m:0.005s
                make_dir_106_1198()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=1199) as make_dir_107_1199:  # 0m:0.004s
                make_dir_107_1199()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=1200) as make_dir_108_1200:  # 0m:0.004s
                make_dir_108_1200()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=1201) as make_dir_109_1201:  # 0m:0.004s
                make_dir_109_1201()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=1202) as make_dir_110_1202:  # 0m:0.004s
                make_dir_110_1202()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=1203) as make_dir_111_1203:  # 0m:0.006s
                make_dir_111_1203()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=1204) as make_dir_112_1204:  # 0m:0.010s
                make_dir_112_1204()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=1205) as make_dir_113_1205:  # 0m:0.007s
                make_dir_113_1205()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=1206) as make_dir_114_1206:  # 0m:0.005s
                make_dir_114_1206()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=1207) as rm_file_or_dir_115_1207:  # 0m:0.000s
            rm_file_or_dir_115_1207()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1208) as shell_command_116_1208:  # 0m:0.009s
            shell_command_116_1208()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1209) as shell_command_117_1209:  # 0m:0.012s
            shell_command_117_1209()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=1210) as shell_command_118_1210:  # 0m:1.117s
            shell_command_118_1210()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1211) as shell_command_119_1211:  # 0m:1.139s
            shell_command_119_1211()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1212) as shell_command_120_1212:  # 0m:0.007s
            shell_command_120_1212()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1213) as shell_command_121_1213:  # 0m:1.115s
            shell_command_121_1213()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1214) as shell_command_122_1214:  # 0m:0.008s
            shell_command_122_1214()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1215) as shell_command_123_1215:  # 0m:0.009s
            shell_command_123_1215()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1216) as shell_command_124_1216:  # 0m:0.163s
            shell_command_124_1216()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1217) as cd_stage_125_1217:  # 0m:0.009s
            cd_stage_125_1217()
            with SetExecPermissionsInSyncFolder(prog_num=1218) as set_exec_permissions_in_sync_folder_126_1218:  # 0m:0.008s
                set_exec_permissions_in_sync_folder_126_1218()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=1219) as cd_stage_127_1219:  # 0m:3.553s
            cd_stage_127_1219()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.2", prog_num=1220):  # 0m:0.019s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=1221) as should_copy_source_128_1221:  # 0m:0.019s
                    should_copy_source_128_1221()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=1222):  # 0m:0.015s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=1223) as copy_dir_to_dir_129_1223:  # 0m:0.014s
                            copy_dir_to_dir_129_1223()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=1224, recursive=True) as chown_130_1224:  # 0m:0.000s
                            chown_130_1224()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Network__Data_Folders v1.0.1.7", prog_num=1225):  # 0m:3.533s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=1226) as should_copy_source_131_1226:  # 0m:3.533s
                    should_copy_source_131_1226()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx DeReverb", prog_num=1227):  # 0m:3.532s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=1228) as copy_dir_to_dir_132_1228:  # 0m:0.045s
                            copy_dir_to_dir_132_1228()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", where_to_unwtar=r".", prog_num=1229) as unwtar_133_1229:  # 0m:3.486s
                            unwtar_133_1229()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=1230, recursive=True) as chown_134_1230:  # 0m:0.000s
                            chown_134_1230()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", prog_num=1231) as cd_stage_135_1231:  # 0m:5.966s
            cd_stage_135_1231()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.5", prog_num=1232):  # 0m:5.965s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=3, prog_num=1233) as should_copy_source_136_1233:  # 0m:0.001s
                    should_copy_source_136_1233()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=1234):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r".", prog_num=1235) as copy_file_to_dir_137_1235:  # 0m:0.001s
                            copy_file_to_dir_137_1235()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=1236) as chmod_and_chown_138_1236:  # 0m:0.000s
                            chmod_and_chown_138_1236()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=1237) as should_copy_source_139_1237:  # 0m:1.738s
                    should_copy_source_139_1237()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/A", prog_num=1238):  # 0m:1.738s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", r".", delete_extraneous_files=True, prog_num=1239) as copy_dir_to_dir_140_1239:  # 0m:0.008s
                            copy_dir_to_dir_140_1239()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", where_to_unwtar=r".", prog_num=1240) as unwtar_141_1240:  # 0m:1.730s
                            unwtar_141_1240()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/A", user_id=-1, group_id=-1, prog_num=1241, recursive=True) as chown_142_1241:  # 0m:0.000s
                            chown_142_1241()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=1242) as should_copy_source_143_1242:  # 0m:1.750s
                    should_copy_source_143_1242()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/B", prog_num=1243):  # 0m:1.749s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", r".", delete_extraneous_files=True, prog_num=1244) as copy_dir_to_dir_144_1244:  # 0m:0.011s
                            copy_dir_to_dir_144_1244()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", where_to_unwtar=r".", prog_num=1245) as unwtar_145_1245:  # 0m:1.738s
                            unwtar_145_1245()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/B", user_id=-1, group_id=-1, prog_num=1246, recursive=True) as chown_146_1246:  # 0m:0.000s
                            chown_146_1246()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=1247) as should_copy_source_147_1247:  # 0m:1.826s
                    should_copy_source_147_1247()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/C", prog_num=1248):  # 0m:1.825s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", r".", delete_extraneous_files=True, prog_num=1249) as copy_dir_to_dir_148_1249:  # 0m:0.010s
                            copy_dir_to_dir_148_1249()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", where_to_unwtar=r".", prog_num=1250) as unwtar_149_1250:  # 0m:1.814s
                            unwtar_149_1250()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/C", user_id=-1, group_id=-1, prog_num=1251, recursive=True) as chown_150_1251:  # 0m:0.001s
                            chown_150_1251()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=1252) as should_copy_source_151_1252:  # 0m:0.650s
                    should_copy_source_151_1252()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/F", prog_num=1253):  # 0m:0.649s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", r".", delete_extraneous_files=True, prog_num=1254) as copy_dir_to_dir_152_1254:  # 0m:0.006s
                            copy_dir_to_dir_152_1254()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", where_to_unwtar=r".", prog_num=1255) as unwtar_153_1255:  # 0m:0.643s
                            unwtar_153_1255()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/F", user_id=-1, group_id=-1, prog_num=1256, recursive=True) as chown_154_1256:  # 0m:0.000s
                            chown_154_1256()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=1257) as cd_stage_155_1257:  # 0m:0.125s
            cd_stage_155_1257()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Pro__Presets v1.0.2.1", prog_num=1258):  # 0m:0.113s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=1259) as should_copy_source_156_1259:  # ?
                    should_copy_source_156_1259()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb Pro", prog_num=1260):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r".", delete_extraneous_files=True, prog_num=1261) as copy_dir_to_dir_157_1261:  # ?
                            copy_dir_to_dir_157_1261()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb Pro", user_id=-1, group_id=-1, prog_num=1262, recursive=True) as chown_158_1262:  # 0m:0.112s
                            chown_158_1262()
            with Stage(r"copy", r"Clarity_Vx_DeReverb__Presets v1.0.2.1", prog_num=1263):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=1264) as should_copy_source_159_1264:  # ?
                    should_copy_source_159_1264()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb", prog_num=1265):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=1266) as copy_dir_to_dir_160_1266:  # ?
                            copy_dir_to_dir_160_1266()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=1267, recursive=True) as chown_161_1267:  # 0m:0.005s
                            chown_161_1267()
            with Stage(r"copy", r"Clarity_Vx_Pro__Presets v1.0.1.8", prog_num=1268):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=1269) as should_copy_source_162_1269:  # ?
                    should_copy_source_162_1269()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx Pro", prog_num=1270):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r".", delete_extraneous_files=True, prog_num=1271) as copy_dir_to_dir_163_1271:  # ?
                            copy_dir_to_dir_163_1271()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx Pro", user_id=-1, group_id=-1, prog_num=1272, recursive=True) as chown_164_1272:  # 0m:0.003s
                            chown_164_1272()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=1273):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=1274) as should_copy_source_165_1274:  # ?
                    should_copy_source_165_1274()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=1275):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=1276) as copy_dir_to_dir_166_1276:  # ?
                            copy_dir_to_dir_166_1276()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=1277, recursive=True) as chown_167_1277:  # 0m:0.004s
                            chown_167_1277()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=1278) as cd_stage_168_1278:  # 0m:14.730s
            cd_stage_168_1278()
            with Stage(r"copy", r"Clarity Vx DeReverb v16.2.30.56", prog_num=1279):  # 0m:3.619s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1280) as should_copy_source_169_1280:  # 0m:3.619s
                    should_copy_source_169_1280()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb.bundle", prog_num=1281):  # 0m:3.618s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r".", delete_extraneous_files=True, prog_num=1282) as copy_dir_to_dir_170_1282:  # 0m:0.048s
                            copy_dir_to_dir_170_1282()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", where_to_unwtar=r".", prog_num=1283) as unwtar_171_1283:  # 0m:3.569s
                            unwtar_171_1283()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb.bundle", user_id=-1, group_id=-1, prog_num=1284, recursive=True) as chown_172_1284:  # 0m:0.000s
                            chown_172_1284()
            with Stage(r"copy", r"Clarity Vx DeReverb Pro v16.2.30.56", prog_num=1285):  # 0m:4.077s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1286) as should_copy_source_173_1286:  # 0m:4.077s
                    should_copy_source_173_1286()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb Pro.bundle", prog_num=1287):  # 0m:4.075s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r".", delete_extraneous_files=True, prog_num=1288) as copy_dir_to_dir_174_1288:  # 0m:0.051s
                            copy_dir_to_dir_174_1288()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", where_to_unwtar=r".", prog_num=1289) as unwtar_175_1289:  # 0m:4.019s
                            unwtar_175_1289()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb Pro.bundle", user_id=-1, group_id=-1, prog_num=1290, recursive=True) as chown_176_1290:  # 0m:0.005s
                            chown_176_1290()
            with Stage(r"copy", r"Clarity Vx v16.2.30.56", prog_num=1291):  # 0m:1.298s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1292) as should_copy_source_177_1292:  # 0m:1.297s
                    should_copy_source_177_1292()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=1293):  # 0m:1.295s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=1294) as copy_dir_to_dir_178_1294:  # 0m:0.051s
                            copy_dir_to_dir_178_1294()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=1295) as unwtar_179_1295:  # 0m:1.244s
                            unwtar_179_1295()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=1296, recursive=True) as chown_180_1296:  # 0m:0.000s
                            chown_180_1296()
            with Stage(r"copy", r"Clarity Vx Pro v16.2.30.56", prog_num=1297):  # 0m:1.291s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1298) as should_copy_source_181_1298:  # 0m:1.290s
                    should_copy_source_181_1298()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx Pro.bundle", prog_num=1299):  # 0m:1.285s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r".", delete_extraneous_files=True, prog_num=1300) as copy_dir_to_dir_182_1300:  # 0m:0.050s
                            copy_dir_to_dir_182_1300()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", where_to_unwtar=r".", prog_num=1301) as unwtar_183_1301:  # 0m:1.235s
                            unwtar_183_1301()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx Pro.bundle", user_id=-1, group_id=-1, prog_num=1302, recursive=True) as chown_184_1302:  # 0m:0.000s
                            chown_184_1302()
            with Stage(r"copy", r"Immersive Wrapper v16.0.74.75", prog_num=1303):  # 0m:0.416s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1304) as should_copy_source_185_1304:  # 0m:0.416s
                    should_copy_source_185_1304()
                    with Stage(r"copy source", r"Mac/Plugins/Immersive Wrapper.bundle", prog_num=1305):  # 0m:0.410s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r".", delete_extraneous_files=True, prog_num=1306) as copy_dir_to_dir_186_1306:  # 0m:0.052s
                            copy_dir_to_dir_186_1306()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", where_to_unwtar=r".", prog_num=1307) as unwtar_187_1307:  # 0m:0.356s
                            unwtar_187_1307()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Immersive Wrapper.bundle", user_id=-1, group_id=-1, prog_num=1308, recursive=True) as chown_188_1308:  # 0m:0.000s
                            chown_188_1308()
            with Stage(r"copy", r"WavesLib1_16_0_74_75 v16.0.74.75", prog_num=1309):  # 0m:0.593s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.74.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1310) as should_copy_source_189_1310:  # 0m:0.593s
                    should_copy_source_189_1310()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.74.framework", prog_num=1311):  # 0m:0.593s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.74.framework", r".", delete_extraneous_files=True, prog_num=1312) as copy_dir_to_dir_190_1312:  # 0m:0.007s
                            copy_dir_to_dir_190_1312()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.74.framework", where_to_unwtar=r".", prog_num=1313) as unwtar_191_1313:  # 0m:0.585s
                            unwtar_191_1313()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.74.framework", user_id=-1, group_id=-1, prog_num=1314, recursive=True) as chown_192_1314:  # 0m:0.000s
                            chown_192_1314()
            with Stage(r"copy", r"WavesLib1_16_2_30_56 v16.2.30.56", prog_num=1315):  # 0m:0.585s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=1316) as should_copy_source_193_1316:  # 0m:0.585s
                    should_copy_source_193_1316()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.2.30.framework", prog_num=1317):  # 0m:0.585s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", r".", delete_extraneous_files=True, prog_num=1318) as copy_dir_to_dir_194_1318:  # 0m:0.002s
                            copy_dir_to_dir_194_1318()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", where_to_unwtar=r".", prog_num=1319) as unwtar_195_1319:  # 0m:0.582s
                            unwtar_195_1319()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.2.30.framework", user_id=-1, group_id=-1, prog_num=1320, recursive=True) as chown_196_1320:  # 0m:0.001s
                            chown_196_1320()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=4, prog_num=1324) as resolve_symlink_files_in_folder_197_1324:  # 0m:2.188s
                resolve_symlink_files_in_folder_197_1324()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=1325) as shell_command_198_1325:  # 0m:0.121s
                shell_command_198_1325()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=1326) as script_command_199_1326:  # 0m:0.011s
                script_command_199_1326()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1327) as shell_command_200_1327:  # 0m:0.159s
                shell_command_200_1327()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=1328) as create_symlink_201_1328:  # 0m:0.001s
                create_symlink_201_1328()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=1329) as create_symlink_202_1329:  # 0m:0.000s
                create_symlink_202_1329()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=1330) as copy_glob_to_dir_203_1330:  # 0m:0.369s
                copy_glob_to_dir_203_1330()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=1331) as cd_stage_204_1331:  # 0m:0.001s
            cd_stage_204_1331()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=1332):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=1333) as should_copy_source_205_1333:  # ?
                    should_copy_source_205_1333()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=1334):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=1335) as copy_file_to_dir_206_1335:  # ?
                            copy_file_to_dir_206_1335()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=1336) as chmod_and_chown_207_1336:  # 0m:0.000s
                            chmod_and_chown_207_1336()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=1337) as cd_stage_208_1337:  # 0m:3.748s
            cd_stage_208_1337()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=1338):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=1339) as should_copy_source_209_1339:  # ?
                    should_copy_source_209_1339()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=1340):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=1341) as copy_dir_to_dir_210_1341:  # ?
                            copy_dir_to_dir_210_1341()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=1342) as unwtar_211_1342:  # ?
                            unwtar_211_1342()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=1343, recursive=True) as chown_212_1343:  # ?
                            chown_212_1343()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=1344) as shell_command_213_1344:  # 0m:0.001s
                            shell_command_213_1344()
            with Stage(r"copy", r"WaveShell1-AAX 16.2 v16.2.30.56", prog_num=1345):  # 0m:1.045s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=1346) as should_copy_source_214_1346:  # 0m:1.045s
                    should_copy_source_214_1346()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", prog_num=1347):  # 0m:1.045s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r".", delete_extraneous_files=True, prog_num=1348) as copy_dir_to_dir_215_1348:  # 0m:0.006s
                            copy_dir_to_dir_215_1348()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", where_to_unwtar=r".", prog_num=1349) as unwtar_216_1349:  # 0m:0.986s
                            unwtar_216_1349()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.2.aaxplugin", user_id=-1, group_id=-1, prog_num=1350, recursive=True) as chown_217_1350:  # 0m:0.000s
                            chown_217_1350()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.2.aaxplugin"', ignore_all_errors=True, prog_num=1351) as shell_command_218_1351:  # 0m:0.053s
                            shell_command_218_1351()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=1352):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=1353) as should_copy_source_219_1353:  # ?
                    should_copy_source_219_1353()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=1354):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=1355) as copy_dir_to_dir_220_1355:  # ?
                            copy_dir_to_dir_220_1355()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=1356) as unwtar_221_1356:  # ?
                            unwtar_221_1356()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=1357, recursive=True) as chown_222_1357:  # ?
                            chown_222_1357()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=1358) as break_hard_link_223_1358:  # ?
                            break_hard_link_223_1358()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=1359) as shell_command_224_1359:  # ?
                            shell_command_224_1359()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=1360, recursive=True) as chown_225_1360:  # ?
                            chown_225_1360()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=1361, recursive=True) as chmod_226_1361:  # 0m:0.001s
                            chmod_226_1361()
            with Stage(r"copy", r"WaveShell1-AU 16.2.component v16.2.30.56", prog_num=1362):  # 0m:1.103s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=1363) as should_copy_source_227_1363:  # 0m:1.103s
                    should_copy_source_227_1363()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.2.component", prog_num=1364):  # 0m:1.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r".", delete_extraneous_files=True, prog_num=1365) as copy_dir_to_dir_228_1365:  # 0m:0.003s
                            copy_dir_to_dir_228_1365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", where_to_unwtar=r".", prog_num=1366) as unwtar_229_1366:  # 0m:1.017s
                            unwtar_229_1366()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=1367, recursive=True) as chown_230_1367:  # 0m:0.000s
                            chown_230_1367()
                        with BreakHardLink(r"WaveShell1-AU 16.2.component/Contents/Info.plist", prog_num=1368) as break_hard_link_231_1368:  # 0m:0.018s
                            break_hard_link_231_1368()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.2.component"', ignore_all_errors=True, prog_num=1369) as shell_command_232_1369:  # 0m:0.054s
                            shell_command_232_1369()
                        with Chown(path=r"WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=1370, recursive=True) as chown_233_1370:  # 0m:0.000s
                            chown_233_1370()
                        with Chmod(path=r"WaveShell1-AU 16.2.component", mode="a+rwX", prog_num=1371, recursive=True) as chmod_234_1371:  # 0m:0.010s
                            chmod_234_1371()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=1372):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=1373) as should_copy_source_235_1373:  # ?
                    should_copy_source_235_1373()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=1374):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=1375) as copy_dir_to_dir_236_1375:  # ?
                            copy_dir_to_dir_236_1375()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=1376) as unwtar_237_1376:  # ?
                            unwtar_237_1376()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=1377, recursive=True) as chown_238_1377:  # ?
                            chown_238_1377()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=1378) as shell_command_239_1378:  # 0m:0.001s
                            shell_command_239_1378()
            with Stage(r"copy", r"WaveShell1-VST3 16.2 v16.2.30.56", prog_num=1379):  # 0m:1.118s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=1380) as should_copy_source_240_1380:  # 0m:1.118s
                    should_copy_source_240_1380()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.2.vst3", prog_num=1381):  # 0m:1.117s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r".", delete_extraneous_files=True, prog_num=1382) as copy_dir_to_dir_241_1382:  # 0m:0.002s
                            copy_dir_to_dir_241_1382()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", where_to_unwtar=r".", prog_num=1383) as unwtar_242_1383:  # 0m:1.063s
                            unwtar_242_1383()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.2.vst3", user_id=-1, group_id=-1, prog_num=1384, recursive=True) as chown_243_1384:  # 0m:0.000s
                            chown_243_1384()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.2.vst3"', ignore_all_errors=True, prog_num=1385) as shell_command_244_1385:  # 0m:0.052s
                            shell_command_244_1385()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=1386):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=1387) as should_copy_source_245_1387:  # ?
                    should_copy_source_245_1387()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=1388):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=1389) as copy_dir_to_dir_246_1389:  # ?
                            copy_dir_to_dir_246_1389()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=1390) as unwtar_247_1390:  # ?
                            unwtar_247_1390()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=1391, recursive=True) as chown_248_1391:  # ?
                            chown_248_1391()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=1392) as shell_command_249_1392:  # ?
                            shell_command_249_1392()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=1393) as script_command_250_1393:  # ?
                            script_command_250_1393()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1394) as shell_command_251_1394:  # 0m:0.001s
                            shell_command_251_1394()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.2 v16.2.30.56", prog_num=1395):  # 0m:0.463s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=1396) as should_copy_source_252_1396:  # 0m:0.463s
                    should_copy_source_252_1396()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", prog_num=1397):  # 0m:0.463s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r".", delete_extraneous_files=True, prog_num=1398) as copy_dir_to_dir_253_1398:  # 0m:0.006s
                            copy_dir_to_dir_253_1398()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", where_to_unwtar=r".", prog_num=1399) as unwtar_254_1399:  # 0m:0.276s
                            unwtar_254_1399()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.2.bundle", user_id=-1, group_id=-1, prog_num=1400, recursive=True) as chown_255_1400:  # 0m:0.000s
                            chown_255_1400()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=1401) as shell_command_256_1401:  # 0m:0.104s
                            shell_command_256_1401()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=1402) as script_command_257_1402:  # 0m:0.014s
                            script_command_257_1402()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1403) as shell_command_258_1403:  # 0m:0.063s
                            shell_command_258_1403()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=1404):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=1405) as should_copy_source_259_1405:  # ?
                    should_copy_source_259_1405()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=1406):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=1407) as copy_dir_to_dir_260_1407:  # ?
                            copy_dir_to_dir_260_1407()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=1408) as unwtar_261_1408:  # ?
                            unwtar_261_1408()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=1409, recursive=True) as chown_262_1409:  # 0m:0.001s
                            chown_262_1409()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=1410) as shell_command_263_1410:  # 0m:0.011s
                shell_command_263_1410()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=1411) as cd_stage_264_1411:  # 0m:1.160s
            cd_stage_264_1411()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=1412):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=1413) as should_copy_source_265_1413:  # ?
                    should_copy_source_265_1413()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=1414):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=1415) as copy_dir_to_dir_266_1415:  # ?
                            copy_dir_to_dir_266_1415()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=1416) as unwtar_267_1416:  # ?
                            unwtar_267_1416()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=1417, recursive=True) as chown_268_1417:  # ?
                            chown_268_1417()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=1418) as shell_command_269_1418:  # 0m:0.001s
                            shell_command_269_1418()
            with Stage(r"copy", r"WaveShell1-AAX 16.2 v16.2.30.56", prog_num=1419):  # 0m:1.158s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=1420) as should_copy_source_270_1420:  # 0m:1.158s
                    should_copy_source_270_1420()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", prog_num=1421):  # 0m:1.158s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r".", delete_extraneous_files=True, prog_num=1422) as copy_dir_to_dir_271_1422:  # 0m:0.013s
                            copy_dir_to_dir_271_1422()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", where_to_unwtar=r".", prog_num=1423) as unwtar_272_1423:  # 0m:1.095s
                            unwtar_272_1423()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.2.aaxplugin", user_id=-1, group_id=-1, prog_num=1424, recursive=True) as chown_273_1424:  # 0m:0.000s
                            chown_273_1424()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.2.aaxplugin"', ignore_all_errors=True, prog_num=1425) as shell_command_274_1425:  # 0m:0.050s
                            shell_command_274_1425()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=1426) as cd_stage_275_1426:  # 0m:0.004s
            cd_stage_275_1426()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=1427):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=1428) as should_copy_source_276_1428:  # ?
                    should_copy_source_276_1428()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=1429):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=1430) as copy_dir_to_dir_277_1430:  # ?
                            copy_dir_to_dir_277_1430()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=1431, recursive=True) as chown_278_1431:  # 0m:0.003s
                            chown_278_1431()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=1432) as cd_stage_279_1432:  # 0m:0.001s
            cd_stage_279_1432()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=1433):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=1434) as should_copy_source_280_1434:  # ?
                    should_copy_source_280_1434()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=1435):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=1436) as copy_dir_to_dir_281_1436:  # ?
                            copy_dir_to_dir_281_1436()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=1437, recursive=True) as chown_282_1437:  # 0m:0.001s
                            chown_282_1437()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=1438) as cd_stage_283_1438:  # 0m:0.001s
            cd_stage_283_1438()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=1439):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=1440) as should_copy_source_284_1440:  # ?
                    should_copy_source_284_1440()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=1441):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=1442) as copy_dir_to_dir_285_1442:  # ?
                            copy_dir_to_dir_285_1442()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=1443, recursive=True) as chown_286_1443:  # 0m:0.001s
                            chown_286_1443()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=1444) as cd_stage_287_1444:  # 0m:6.339s
            cd_stage_287_1444()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=1445) as rm_file_or_dir_288_1445:  # 0m:0.000s
                rm_file_or_dir_288_1445()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=1446):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=1447) as should_copy_source_289_1447:  # ?
                    should_copy_source_289_1447()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=1448):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=1449) as copy_dir_to_dir_290_1449:  # ?
                            copy_dir_to_dir_290_1449()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=1450) as unwtar_291_1450:  # ?
                            unwtar_291_1450()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=1451, recursive=True) as chown_292_1451:  # 0m:0.000s
                            chown_292_1451()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=1452):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=1453) as should_copy_source_293_1453:  # 0m:0.008s
                    should_copy_source_293_1453()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=1454):  # 0m:0.008s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=1455) as unwtar_294_1455:  # 0m:0.008s
                            unwtar_294_1455()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=1456):  # 0m:4.883s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=1457) as should_copy_source_295_1457:  # 0m:4.882s
                    should_copy_source_295_1457()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=1458):  # 0m:4.882s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=1459) as copy_dir_to_dir_296_1459:  # 0m:0.016s
                            copy_dir_to_dir_296_1459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=1460) as unwtar_297_1460:  # 0m:4.866s
                            unwtar_297_1460()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=1461, recursive=True) as chown_298_1461:  # 0m:0.000s
                            chown_298_1461()
            with Stage(r"copy", r"onnxruntime_1.19.0 v1.19.0", prog_num=1462):  # 0m:1.414s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=1463) as should_copy_source_299_1463:  # 0m:1.414s
                    should_copy_source_299_1463()
                    with Stage(r"copy source", r"Mac/Modules/onnxruntime", prog_num=1464):  # 0m:1.413s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r".", delete_extraneous_files=True, prog_num=1465) as copy_dir_to_dir_300_1465:  # 0m:0.013s
                            copy_dir_to_dir_300_1465()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", where_to_unwtar=r".", prog_num=1466) as unwtar_301_1466:  # 0m:1.396s
                            unwtar_301_1466()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/onnxruntime", user_id=-1, group_id=-1, prog_num=1467, recursive=True) as chown_302_1467:  # 0m:0.005s
                            chown_302_1467()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=1468):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=1469) as should_copy_source_303_1469:  # ?
                    should_copy_source_303_1469()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=1470):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=1471) as copy_dir_to_dir_304_1471:  # ?
                            copy_dir_to_dir_304_1471()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=1472) as chmod_305_1472:  # ?
                            chmod_305_1472()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=1473) as chmod_306_1473:  # ?
                            chmod_306_1473()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=1474, recursive=True) as chown_307_1474:  # 0m:0.001s
                            chown_307_1474()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=1477) as resolve_symlink_files_in_folder_308_1477:  # 0m:0.017s
                resolve_symlink_files_in_folder_308_1477()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1478) as shell_command_309_1478:  # 0m:0.016s
                shell_command_309_1478()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=1479) as cd_stage_310_1479:  # 0m:0.007s
            cd_stage_310_1479()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=1480):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=1481) as should_copy_source_311_1481:  # ?
                    should_copy_source_311_1481()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=1482):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=1483) as copy_dir_to_dir_312_1483:  # ?
                            copy_dir_to_dir_312_1483()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=1484, recursive=True) as chown_313_1484:  # 0m:0.006s
                            chown_313_1484()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=1485) as cd_stage_314_1485:  # 0m:0.002s
            cd_stage_314_1485()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=1486):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=1487) as should_copy_source_315_1487:  # ?
                    should_copy_source_315_1487()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=1488):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=1489) as copy_dir_to_dir_316_1489:  # ?
                            copy_dir_to_dir_316_1489()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=1490, recursive=True) as chown_317_1490:  # 0m:0.001s
                            chown_317_1490()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=1491) as cd_stage_318_1491:  # 0m:0.002s
            cd_stage_318_1491()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=1492):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=1493) as should_copy_source_319_1493:  # ?
                    should_copy_source_319_1493()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=1494):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=1495, recursive=True) as chmod_320_1495:  # ?
                            chmod_320_1495()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=1496) as copy_dir_to_dir_321_1496:  # ?
                            copy_dir_to_dir_321_1496()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=1497) as unwtar_322_1497:  # ?
                            unwtar_322_1497()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=1498, recursive=True) as chown_323_1498:  # ?
                            chown_323_1498()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=1499) as if_324_1499:  # 0m:0.001s
                            if_324_1499()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=1500) as cd_stage_325_1500:  # 0m:2.454s
            cd_stage_325_1500()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=1501):  # 0m:1.314s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=1502) as should_copy_source_326_1502:  # 0m:1.314s
                    should_copy_source_326_1502()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=1503):  # 0m:1.313s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=1504) as copy_dir_to_dir_327_1504:  # 0m:0.185s
                            copy_dir_to_dir_327_1504()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=1505) as unwtar_328_1505:  # 0m:1.039s
                            unwtar_328_1505()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=1506, recursive=True) as chown_329_1506:  # 0m:0.000s
                            chown_329_1506()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=1507) as break_hard_link_330_1507:  # 0m:0.018s
                            break_hard_link_330_1507()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=1508) as shell_command_331_1508:  # 0m:0.054s
                            shell_command_331_1508()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=1509, recursive=True) as chown_332_1509:  # 0m:0.000s
                            chown_332_1509()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=1510, recursive=True) as chmod_333_1510:  # 0m:0.016s
                            chmod_333_1510()
            with Stage(r"copy", r"WaveShell1-AU 16.2.component v16.2.30.56", prog_num=1511):  # 0m:1.139s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=1512) as should_copy_source_334_1512:  # 0m:1.139s
                    should_copy_source_334_1512()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.2.component", prog_num=1513):  # 0m:1.138s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r".", delete_extraneous_files=True, prog_num=1514) as copy_dir_to_dir_335_1514:  # 0m:0.003s
                            copy_dir_to_dir_335_1514()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", where_to_unwtar=r".", prog_num=1515) as unwtar_336_1515:  # 0m:1.052s
                            unwtar_336_1515()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=1516, recursive=True) as chown_337_1516:  # 0m:0.000s
                            chown_337_1516()
                        with BreakHardLink(r"WaveShell1-AU 16.2.component/Contents/Info.plist", prog_num=1517) as break_hard_link_338_1517:  # 0m:0.018s
                            break_hard_link_338_1517()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.2.component"', ignore_all_errors=True, prog_num=1518) as shell_command_339_1518:  # 0m:0.054s
                            shell_command_339_1518()
                        with Chown(path=r"WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=1519, recursive=True) as chown_340_1519:  # 0m:0.001s
                            chown_340_1519()
                        with Chmod(path=r"WaveShell1-AU 16.2.component", mode="a+rwX", prog_num=1520, recursive=True) as chmod_341_1520:  # 0m:0.010s
                            chmod_341_1520()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=1521) as cd_stage_342_1521:  # 0m:1.164s
            cd_stage_342_1521()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=1522):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=1523) as should_copy_source_343_1523:  # ?
                    should_copy_source_343_1523()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=1524):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=1525) as copy_dir_to_dir_344_1525:  # ?
                            copy_dir_to_dir_344_1525()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=1526) as unwtar_345_1526:  # ?
                            unwtar_345_1526()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=1527, recursive=True) as chown_346_1527:  # ?
                            chown_346_1527()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=1528) as shell_command_347_1528:  # 0m:0.001s
                            shell_command_347_1528()
            with Stage(r"copy", r"WaveShell1-VST3 16.2 v16.2.30.56", prog_num=1529):  # 0m:1.161s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=1530) as should_copy_source_348_1530:  # 0m:1.161s
                    should_copy_source_348_1530()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.2.vst3", prog_num=1531):  # 0m:1.161s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r".", delete_extraneous_files=True, prog_num=1532) as copy_dir_to_dir_349_1532:  # 0m:0.003s
                            copy_dir_to_dir_349_1532()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", where_to_unwtar=r".", prog_num=1533) as unwtar_350_1533:  # 0m:1.105s
                            unwtar_350_1533()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.2.vst3", user_id=-1, group_id=-1, prog_num=1534, recursive=True) as chown_351_1534:  # 0m:0.000s
                            chown_351_1534()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.2.vst3"', ignore_all_errors=True, prog_num=1535) as shell_command_352_1535:  # 0m:0.053s
                            shell_command_352_1535()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1536) as cd_stage_353_1536:  # 0m:0.479s
            cd_stage_353_1536()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=1537):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=1538) as should_copy_source_354_1538:  # ?
                    should_copy_source_354_1538()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=1539):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=1540) as copy_dir_to_dir_355_1540:  # ?
                            copy_dir_to_dir_355_1540()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=1541) as unwtar_356_1541:  # ?
                            unwtar_356_1541()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=1542, recursive=True) as chown_357_1542:  # ?
                            chown_357_1542()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=1543) as shell_command_358_1543:  # ?
                            shell_command_358_1543()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=1544) as script_command_359_1544:  # ?
                            script_command_359_1544()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1545) as shell_command_360_1545:  # 0m:0.004s
                            shell_command_360_1545()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.2 v16.2.30.56", prog_num=1546):  # 0m:0.472s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=1547) as should_copy_source_361_1547:  # 0m:0.472s
                    should_copy_source_361_1547()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", prog_num=1548):  # 0m:0.472s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r".", delete_extraneous_files=True, prog_num=1549) as copy_dir_to_dir_362_1549:  # 0m:0.007s
                            copy_dir_to_dir_362_1549()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", where_to_unwtar=r".", prog_num=1550) as unwtar_363_1550:  # 0m:0.289s
                            unwtar_363_1550()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", user_id=-1, group_id=-1, prog_num=1551, recursive=True) as chown_364_1551:  # 0m:0.000s
                            chown_364_1551()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=1552) as shell_command_365_1552:  # 0m:0.101s
                            shell_command_365_1552()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=1553) as script_command_366_1553:  # 0m:0.013s
                            script_command_366_1553()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=1554) as shell_command_367_1554:  # 0m:0.060s
                            shell_command_367_1554()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1555) as create_symlink_368_1555:  # 0m:0.001s
                create_symlink_368_1555()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=1556) as create_symlink_369_1556:  # 0m:0.001s
                create_symlink_369_1556()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=1557) as rm_file_or_dir_370_1557:  # 0m:0.483s
            rm_file_or_dir_370_1557()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=1558) as shell_command_371_1558:  # 0m:0.104s
            shell_command_371_1558()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=1559) as script_command_372_1559:  # 0m:0.012s
            script_command_372_1559()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=1560) as rm_file_or_dir_373_1560:  # 0m:0.001s
            rm_file_or_dir_373_1560()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=1561) as glober_374_1561:  # 0m:0.002s
            glober_374_1561()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=1562) as glober_375_1562:  # 0m:0.001s
            glober_375_1562()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=1563) as glober_376_1563:  # 0m:0.004s
            glober_376_1563()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1564) as shell_command_377_1564:  # 0m:0.010s
            shell_command_377_1564()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1565) as shell_command_378_1565:  # 0m:5.903s
            shell_command_378_1565()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1566) as shell_command_379_1566:  # 0m:0.310s
            shell_command_379_1566()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=1567) as shell_command_380_1567:  # 0m:1.020s
            shell_command_380_1567()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=1568) as shell_command_381_1568:  # 0m:0.107s
            shell_command_381_1568()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=1569) as script_command_382_1569:  # 0m:0.009s
            script_command_382_1569()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=1570) as if_383_1570:  # 0m:0.005s
            if_383_1570()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=1571) as if_384_1571:  # 0m:0.001s
            if_384_1571()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=1572) as shell_command_385_1572:  # 0m:0.108s
            shell_command_385_1572()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=1573) as script_command_386_1573:  # 0m:0.013s
            script_command_386_1573()
    with Stage(r"post-copy", prog_num=1574):  # 0m:0.051s
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=1575) as make_dir_387_1575:  # 0m:0.012s
            make_dir_387_1575()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=1576) as copy_file_to_file_388_1576:  # 0m:0.013s
            copy_file_to_file_388_1576()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1577) as chmod_389_1577:  # 0m:0.000s
            chmod_389_1577()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1578) as chmod_390_1578:  # 0m:0.000s
            chmod_390_1578()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1579) as copy_file_to_file_391_1579:  # 0m:0.011s
            copy_file_to_file_391_1579()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1580) as chmod_392_1580:  # 0m:0.000s
            chmod_392_1580()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=1581) as copy_file_to_file_393_1581:  # 0m:0.013s
            copy_file_to_file_393_1581()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1582) as chmod_394_1582:  # 0m:0.000s
            chmod_394_1582()
        Progress(r"Done copy", prog_num=1583)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=1584)()  # 0m:0.000s
    with Stage(r"post", prog_num=1585):  # 0m:0.052s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=1586) as make_dir_395_1586:  # 0m:0.011s
            make_dir_395_1586()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=1587) as copy_file_to_file_396_1587:  # 0m:0.012s
            copy_file_to_file_396_1587()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=1588) as make_dir_397_1588:  # 0m:0.006s
            make_dir_397_1588()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=1589) as copy_file_to_file_398_1589:  # 0m:0.008s
            copy_file_to_file_398_1589()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=1590) as make_dir_399_1590:  # 0m:0.007s
            make_dir_399_1590()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/15/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=1591) as copy_file_to_file_400_1591:  # 0m:0.007s
            copy_file_to_file_400_1591()

with Stage(r"epilog", prog_num=1592):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250823214147.py", prog_num=1593) as patch_py_batch_with_timings_401_1593:  # ?
        patch_py_batch_with_timings_401_1593()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 55623655 bytes in 0m:10.331s, 5384409 bytes per second
# copy time 0m:51.527s
