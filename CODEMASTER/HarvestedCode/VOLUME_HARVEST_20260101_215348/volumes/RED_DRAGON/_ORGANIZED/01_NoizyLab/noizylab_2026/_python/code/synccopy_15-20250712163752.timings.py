# Creation time: 12-07-25_16-37
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 2937
PythonBatchCommandBase.running_progress = 579
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=580):  # 0m:0.000s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250712163752"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX")
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
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 60
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MjM4ODY3M30sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUyMzUyMzczfX19XX0_;CloudFront-Signature=fBUSirByiUa1thkxNmh5bIbrkONwLIENfNXSRRAQUi6EWePfz0a7uNjZ-vJMOH43gXYxv6MR4dALTQPwdp1lIZuxM2lfIqkKpegqJ4YI0Z5j0vETZBznM6cRql62iOf52eRReTJx3gppJQ12Cxfr4pYmBNsSCxl9K1ZW3ERp3uPtKnAxPLEntEm~6a04t5MgchuYaoaM1WAGYq~fl-SxtiC2EQDHnvF6ptcE9-MKPezjxI4JasG6D~~PLEf-8M9oq3G5uPq9fSU5JTiEr6nIZ4ZkPbqoPOuM0IYifUlqBNLXgHC9yCvCbe1yLljJBaNBFQ7M~9A2oSBj~egc19qLhw__"
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
    config_vars['INDEX_CHECKSUM'] = r"abdf7b5c30aab2b0aeaaa3302f92746485daa9dd"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/60/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"2f44e5a99b5bded35934d8a951443f59fdba385f"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/60/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/60/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"215572dc-9c91-4912-a0a9-d68096edc994", r"239c7584-82a0-420d-bfae-8885b3a52538", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"8ce7a272-1741-4893-b516-e93ce40db756", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"e10288b9-ad21-11e0-8381-b7fd7bebd530", r"e5100b89-ad21-11e0-81a0-b7fd7bebd530", r"e551833a-ad21-11e0-8177-b7fd7bebd530", r"e591e90a-ad21-11e0-83a1-b7fd7bebd530", r"ed748b6e-ad21-11e0-83bb-b7fd7bebd530", r"ef3b4d52-ad21-11e0-8109-b7fd7bebd530", r"ef7b9575-ad21-11e0-81f1-b7fd7bebd530", r"ef9640eb-ad21-11e0-83ab-b7fd7bebd530", r"f202b779-ad21-11e0-8344-b7fd7bebd530", r"f23de82a-ad21-11e0-803b-b7fd7bebd530", r"f3315154-ad21-11e0-8140-b7fd7bebd530", r"f3513e7f-ad21-11e0-83f7-b7fd7bebd530", r"f3515f5a-ad21-11e0-81da-b7fd7bebd530")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 60
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250712163752.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 60
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-06-29 17:29:52.393516"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/60"
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
    config_vars['SHORT_INDEX_CHECKSUM'] = r"f4061666f38697b8c1f562c22f13cd285ce4a94a"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/60/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 2353
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250712163752.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"AnalyzeAudioBundle_IID", r"Artist_DLLs_Common_Guid_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS__Data_Folders__IID", r"COSMOS__IID", r"COSMOS__Models_Data_Folders__IID", r"COSMOS_python_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"DeBreath_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"Doubler_IID", r"EddieKramer_VC_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"Get_General_Icons_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"IntelDlls_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"LicenseNotifications_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"ORS_Modulators_Data_IID", r"OpenVino_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"ReWire_IID", r"ReWire_backup_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Shutdown_Servers_IID", r"SoundShifter_IID", r"V9_V10_Organizer_IID", r"Vocal_Rider_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesLib1_15_5_139_IID", r"WavesLib1_15_5_79_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V15_2_IID", r"WavesReWireDevice_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"bvpioepynuojsbum"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"Artist_DLLs_Common_Guid_IID", r"Bass_Slapper_IID", r"COSMOS__IID", r"Clarity_Vx_IID", r"DeBreath_IID", r"Doubler_IID", r"EddieKramer_VC_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"RChannel_IID", r"RDeEsser_IID", r"RenAxx_IID", r"SoundShifter_IID", r"Vocal_Rider_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-07-12 16:38:42.375784"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=581):  # 0m:40.128s
    with Stage(r"begin", prog_num=582):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=583):  # 0m:0.007s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=584) as copy_file_to_file_001_584:  # 0m:0.004s
            copy_file_to_file_001_584()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=585) as copy_file_to_file_002_585:  # 0m:0.003s
            copy_file_to_file_002_585()
    with Stage(r"sync", prog_num=586):  # 0m:2.164s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=587) as shell_command_003_587:  # 0m:0.007s
            shell_command_003_587()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=588) as shell_command_004_588:  # 0m:0.009s
            shell_command_004_588()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=589) as shell_command_005_589:  # 0m:1.002s
            shell_command_005_589()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=590) as shell_command_006_590:  # 0m:0.007s
            shell_command_006_590()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=591) as shell_command_007_591:  # 0m:0.972s
            shell_command_007_591()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=592) as shell_command_008_592:  # 0m:0.006s
            shell_command_008_592()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=593) as shell_command_009_593:  # 0m:0.004s
            shell_command_009_593()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=594) as shell_command_010_594:  # 0m:0.146s
            shell_command_010_594()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=595):  # 0m:0.010s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=596) as make_dir_011_596:  # 0m:0.005s
                make_dir_011_596()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=597) as cd_012_597:  # 0m:0.005s
                cd_012_597()
                Progress(r"1783 files already in cache", own_progress_count=1783, prog_num=2380)()  # 0m:0.000s
                with Stage(r"post_sync", prog_num=2381):  # 0m:0.005s
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=2382) as copy_file_to_file_013_2382:  # 0m:0.005s
                        copy_file_to_file_013_2382()
            Progress(r"Done sync", prog_num=2383)()  # 0m:0.000s
    with Stage(r"copy", prog_num=2384):  # 0m:37.897s
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=2385) as run_in_thread_014_2385:  # 0m:0.000s
            run_in_thread_014_2385()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=2386)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=2387):  # 0m:0.103s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=2388) as make_dir_015_2388:  # 0m:0.004s
                make_dir_015_2388()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=2389) as make_dir_016_2389:  # 0m:0.003s
                make_dir_016_2389()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=2390) as make_dir_017_2390:  # 0m:0.004s
                make_dir_017_2390()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=2391) as make_dir_018_2391:  # 0m:0.003s
                make_dir_018_2391()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=2392) as make_dir_019_2392:  # 0m:0.003s
                make_dir_019_2392()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=2393) as make_dir_020_2393:  # 0m:0.004s
                make_dir_020_2393()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=2394) as make_dir_021_2394:  # 0m:0.003s
                make_dir_021_2394()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=2395) as make_dir_022_2395:  # 0m:0.004s
                make_dir_022_2395()
            with MakeDir(r"/Applications/Waves/ReWire", chowner=True, prog_num=2396) as make_dir_023_2396:  # 0m:0.003s
                make_dir_023_2396()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=2397) as make_dir_024_2397:  # 0m:0.003s
                make_dir_024_2397()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=2398) as make_dir_025_2398:  # 0m:0.004s
                make_dir_025_2398()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=2399) as make_dir_026_2399:  # 0m:0.003s
                make_dir_026_2399()
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=2400) as make_dir_027_2400:  # 0m:0.006s
                make_dir_027_2400()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=2401) as make_dir_028_2401:  # 0m:0.003s
                make_dir_028_2401()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=2402) as make_dir_029_2402:  # 0m:0.004s
                make_dir_029_2402()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=2403) as make_dir_030_2403:  # 0m:0.003s
                make_dir_030_2403()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=2404) as make_dir_031_2404:  # 0m:0.005s
                make_dir_031_2404()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=2405) as make_dir_032_2405:  # 0m:0.003s
                make_dir_032_2405()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=2406) as make_dir_033_2406:  # 0m:0.004s
                make_dir_033_2406()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=2407) as make_dir_034_2407:  # 0m:0.003s
                make_dir_034_2407()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=2408) as make_dir_035_2408:  # 0m:0.005s
                make_dir_035_2408()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=2409) as make_dir_036_2409:  # 0m:0.003s
                make_dir_036_2409()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=2410) as make_dir_037_2410:  # 0m:0.004s
                make_dir_037_2410()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=2411) as make_dir_038_2411:  # 0m:0.003s
                make_dir_038_2411()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=2412) as make_dir_039_2412:  # 0m:0.005s
                make_dir_039_2412()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=2413) as make_dir_040_2413:  # 0m:0.003s
                make_dir_040_2413()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=2414) as make_dir_041_2414:  # 0m:0.003s
                make_dir_041_2414()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=2415) as make_dir_042_2415:  # 0m:0.004s
                make_dir_042_2415()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=2416) as rm_file_or_dir_043_2416:  # 0m:0.005s
            rm_file_or_dir_043_2416()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=2417) as rm_file_or_dir_044_2417:  # 0m:0.000s
            rm_file_or_dir_044_2417()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=2418) as shell_command_045_2418:  # 0m:0.007s
            shell_command_045_2418()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=2419) as shell_command_046_2419:  # 0m:0.011s
            shell_command_046_2419()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=2420) as shell_command_047_2420:  # 0m:1.111s
            shell_command_047_2420()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=2421) as shell_command_048_2421:  # 0m:0.005s
            shell_command_048_2421()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=2422) as shell_command_049_2422:  # 0m:1.090s
            shell_command_049_2422()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=2423) as shell_command_050_2423:  # 0m:0.005s
            shell_command_050_2423()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=2424) as shell_command_051_2424:  # 0m:0.004s
            shell_command_051_2424()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=2425) as shell_command_052_2425:  # 0m:0.158s
            shell_command_052_2425()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=2426) as cd_stage_053_2426:  # 0m:0.011s
            cd_stage_053_2426()
            with SetExecPermissionsInSyncFolder(prog_num=2427) as set_exec_permissions_in_sync_folder_054_2427:  # 0m:0.010s
                set_exec_permissions_in_sync_folder_054_2427()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=2428) as cd_stage_055_2428:  # 0m:0.100s
            cd_stage_055_2428()
            with Stage(r"copy", r"Bass Slapper application v15.5.79.262", prog_num=2429):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=2430) as should_copy_source_056_2430:  # ?
                    should_copy_source_056_2430()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=2431):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=2432) as copy_dir_to_dir_057_2432:  # ?
                            copy_dir_to_dir_057_2432()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=2433) as unwtar_058_2433:  # ?
                            unwtar_058_2433()
                        with Chown(path=r"/Applications/Waves/Applications V15/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=2434, recursive=True) as chown_059_2434:  # 0m:0.000s
                            chown_059_2434()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=2435) as shell_command_060_2435:  # 0m:0.092s
                shell_command_060_2435()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=2436) as script_command_061_2436:  # 0m:0.007s
                script_command_061_2436()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=2437) as cd_stage_062_2437:  # 0m:11.046s
            cd_stage_062_2437()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=2438):  # 0m:11.033s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=2439) as should_copy_source_063_2439:  # 0m:11.033s
                    should_copy_source_063_2439()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=2440):  # 0m:11.033s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=2441) as copy_dir_to_dir_064_2441:  # 0m:0.150s
                            copy_dir_to_dir_064_2441()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=2442) as unwtar_065_2442:  # 0m:10.882s
                            unwtar_065_2442()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=2443, recursive=True) as chown_066_2443:  # 0m:0.000s
                            chown_066_2443()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=2453) as resolve_symlink_files_in_folder_067_2453:  # 0m:0.011s
                resolve_symlink_files_in_folder_067_2453()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=2454) as cd_stage_068_2454:  # 0m:4.077s
            cd_stage_068_2454()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=2455):  # 0m:0.239s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=2456) as should_copy_source_069_2456:  # 0m:0.238s
                    should_copy_source_069_2456()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=2457):  # 0m:0.238s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=2458) as copy_dir_to_dir_070_2458:  # 0m:0.238s
                            copy_dir_to_dir_070_2458()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=2459, recursive=True) as chown_071_2459:  # 0m:0.000s
                            chown_071_2459()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=2460):  # 0m:3.744s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=2461) as should_copy_source_072_2461:  # 0m:3.743s
                    should_copy_source_072_2461()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=2462):  # 0m:3.743s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=2463) as copy_dir_to_dir_073_2463:  # 0m:0.021s
                            copy_dir_to_dir_073_2463()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=2464) as unwtar_074_2464:  # 0m:3.722s
                            unwtar_074_2464()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=2465, recursive=True) as chown_075_2465:  # 0m:0.000s
                            chown_075_2465()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=2466):  # 0m:0.080s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=2467) as should_copy_source_076_2467:  # 0m:0.080s
                    should_copy_source_076_2467()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=2468):  # 0m:0.080s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=2469) as copy_dir_to_dir_077_2469:  # 0m:0.079s
                            copy_dir_to_dir_077_2469()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=2470, recursive=True) as chown_078_2470:  # 0m:0.000s
                            chown_078_2470()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=2471):  # 0m:0.015s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=2472) as should_copy_source_079_2472:  # 0m:0.015s
                    should_copy_source_079_2472()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=2473):  # 0m:0.014s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=2474) as copy_dir_to_dir_080_2474:  # 0m:0.005s
                            copy_dir_to_dir_080_2474()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=2475) as unwtar_081_2475:  # 0m:0.009s
                            unwtar_081_2475()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=2476, recursive=True) as chown_082_2476:  # 0m:0.000s
                            chown_082_2476()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=2477) as cd_stage_083_2477:  # 0m:6.913s
            cd_stage_083_2477()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=2478):  # 0m:6.913s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=2479) as should_copy_source_084_2479:  # 0m:0.001s
                    should_copy_source_084_2479()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=2480):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r".", prog_num=2481) as copy_file_to_dir_085_2481:  # 0m:0.001s
                            copy_file_to_dir_085_2481()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2482) as chmod_and_chown_086_2482:  # 0m:0.000s
                            chmod_and_chown_086_2482()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=2483) as should_copy_source_087_2483:  # 0m:6.912s
                    should_copy_source_087_2483()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=2484):  # 0m:6.912s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=2485) as copy_dir_to_dir_088_2485:  # 0m:0.009s
                            copy_dir_to_dir_088_2485()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=2486) as unwtar_089_2486:  # 0m:6.903s
                            unwtar_089_2486()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=2487, recursive=True) as chown_090_2487:  # 0m:0.000s
                            chown_090_2487()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=2488) as cd_stage_091_2488:  # 0m:0.007s
            cd_stage_091_2488()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=2489):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=2490) as should_copy_source_092_2490:  # ?
                    should_copy_source_092_2490()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=2491):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=2492) as copy_dir_to_dir_093_2492:  # ?
                            copy_dir_to_dir_093_2492()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=2493, recursive=True) as chown_094_2493:  # 0m:0.001s
                            chown_094_2493()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=2494):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=2495) as should_copy_source_095_2495:  # ?
                    should_copy_source_095_2495()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=2496):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=2497) as copy_dir_to_dir_096_2497:  # ?
                            copy_dir_to_dir_096_2497()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=2498, recursive=True) as chown_097_2498:  # 0m:0.001s
                            chown_097_2498()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=2499):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=2500) as should_copy_source_098_2500:  # ?
                    should_copy_source_098_2500()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=2501):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=2502) as copy_dir_to_dir_099_2502:  # ?
                            copy_dir_to_dir_099_2502()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=2503, recursive=True) as chown_100_2503:  # 0m:0.001s
                            chown_100_2503()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=2504):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=2505) as should_copy_source_101_2505:  # ?
                    should_copy_source_101_2505()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=2506):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=2507) as copy_dir_to_dir_102_2507:  # ?
                            copy_dir_to_dir_102_2507()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=2508, recursive=True) as chown_103_2508:  # 0m:0.001s
                            chown_103_2508()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=2509):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=2510) as should_copy_source_104_2510:  # ?
                    should_copy_source_104_2510()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=2511):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=2512) as copy_dir_to_dir_105_2512:  # ?
                            copy_dir_to_dir_105_2512()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=2513, recursive=True) as chown_106_2513:  # 0m:0.003s
                            chown_106_2513()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=2514) as cd_stage_107_2514:  # 0m:1.262s
            cd_stage_107_2514()
            with Stage(r"copy", r"Bass Slapper v15.5.79.262", prog_num=2515):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2516) as should_copy_source_108_2516:  # ?
                    should_copy_source_108_2516()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=2517):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=2518) as copy_dir_to_dir_109_2518:  # ?
                            copy_dir_to_dir_109_2518()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=2519) as unwtar_110_2519:  # ?
                            unwtar_110_2519()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=2520, recursive=True) as chown_111_2520:  # 0m:0.000s
                            chown_111_2520()
            with Stage(r"copy", r"Clarity Vx v15.5.79.262", prog_num=2521):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2522) as should_copy_source_112_2522:  # ?
                    should_copy_source_112_2522()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=2523):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=2524) as copy_dir_to_dir_113_2524:  # ?
                            copy_dir_to_dir_113_2524()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=2525) as unwtar_114_2525:  # ?
                            unwtar_114_2525()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=2526, recursive=True) as chown_115_2526:  # 0m:0.000s
                            chown_115_2526()
            with Stage(r"copy", r"DeBreath v15.5.79.262", prog_num=2527):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2528) as should_copy_source_116_2528:  # ?
                    should_copy_source_116_2528()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=2529):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=2530) as copy_dir_to_dir_117_2530:  # ?
                            copy_dir_to_dir_117_2530()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=2531) as unwtar_118_2531:  # ?
                            unwtar_118_2531()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=2532, recursive=True) as chown_119_2532:  # 0m:0.000s
                            chown_119_2532()
            with Stage(r"copy", r"Doubler v15.5.79.262", prog_num=2533):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2534) as should_copy_source_120_2534:  # ?
                    should_copy_source_120_2534()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=2535):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=2536) as copy_dir_to_dir_121_2536:  # ?
                            copy_dir_to_dir_121_2536()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=2537) as unwtar_122_2537:  # ?
                            unwtar_122_2537()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doubler.bundle", user_id=-1, group_id=-1, prog_num=2538, recursive=True) as chown_123_2538:  # 0m:0.000s
                            chown_123_2538()
            with Stage(r"copy", r"EddieKramer VC v15.5.79.262", prog_num=2539):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2540) as should_copy_source_124_2540:  # ?
                    should_copy_source_124_2540()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=2541):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=2542) as copy_dir_to_dir_125_2542:  # ?
                            copy_dir_to_dir_125_2542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=2543) as unwtar_126_2543:  # ?
                            unwtar_126_2543()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=2544, recursive=True) as chown_127_2544:  # 0m:0.000s
                            chown_127_2544()
            with Stage(r"copy", r"KramerHLS v15.5.79.262", prog_num=2545):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2546) as should_copy_source_128_2546:  # ?
                    should_copy_source_128_2546()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=2547):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=2548) as copy_dir_to_dir_129_2548:  # ?
                            copy_dir_to_dir_129_2548()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=2549) as unwtar_130_2549:  # ?
                            unwtar_130_2549()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=2550, recursive=True) as chown_131_2550:  # 0m:0.000s
                            chown_131_2550()
            with Stage(r"copy", r"KramerPIE v15.5.79.262", prog_num=2551):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2552) as should_copy_source_132_2552:  # ?
                    should_copy_source_132_2552()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=2553):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=2554) as copy_dir_to_dir_133_2554:  # ?
                            copy_dir_to_dir_133_2554()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=2555) as unwtar_134_2555:  # ?
                            unwtar_134_2555()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=2556, recursive=True) as chown_135_2556:  # 0m:0.000s
                            chown_135_2556()
            with Stage(r"copy", r"KramerTape v15.5.79.262", prog_num=2557):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2558) as should_copy_source_136_2558:  # ?
                    should_copy_source_136_2558()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=2559):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=2560) as copy_dir_to_dir_137_2560:  # ?
                            copy_dir_to_dir_137_2560()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=2561) as unwtar_138_2561:  # ?
                            unwtar_138_2561()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=2562, recursive=True) as chown_139_2562:  # 0m:0.000s
                            chown_139_2562()
            with Stage(r"copy", r"RChannel v15.5.79.262", prog_num=2563):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2564) as should_copy_source_140_2564:  # ?
                    should_copy_source_140_2564()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=2565):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=2566) as copy_dir_to_dir_141_2566:  # ?
                            copy_dir_to_dir_141_2566()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=2567) as unwtar_142_2567:  # ?
                            unwtar_142_2567()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RChannel.bundle", user_id=-1, group_id=-1, prog_num=2568, recursive=True) as chown_143_2568:  # 0m:0.000s
                            chown_143_2568()
            with Stage(r"copy", r"RDeEsser v15.5.79.262", prog_num=2569):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2570) as should_copy_source_144_2570:  # ?
                    should_copy_source_144_2570()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=2571):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=2572) as copy_dir_to_dir_145_2572:  # ?
                            copy_dir_to_dir_145_2572()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=2573) as unwtar_146_2573:  # ?
                            unwtar_146_2573()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=2574, recursive=True) as chown_147_2574:  # 0m:0.000s
                            chown_147_2574()
            with Stage(r"copy", r"RenAxx v15.5.79.262", prog_num=2575):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2576) as should_copy_source_148_2576:  # ?
                    should_copy_source_148_2576()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=2577):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=2578) as copy_dir_to_dir_149_2578:  # ?
                            copy_dir_to_dir_149_2578()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=2579) as unwtar_150_2579:  # ?
                            unwtar_150_2579()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=2580, recursive=True) as chown_151_2580:  # 0m:0.000s
                            chown_151_2580()
            with Stage(r"copy", r"SoundShifter v15.5.79.262", prog_num=2581):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2582) as should_copy_source_152_2582:  # ?
                    should_copy_source_152_2582()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=2583):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=2584) as copy_dir_to_dir_153_2584:  # ?
                            copy_dir_to_dir_153_2584()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=2585) as unwtar_154_2585:  # ?
                            unwtar_154_2585()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=2586, recursive=True) as chown_155_2586:  # 0m:0.000s
                            chown_155_2586()
            with Stage(r"copy", r"Vocal Rider v15.5.79.262", prog_num=2587):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2588) as should_copy_source_156_2588:  # ?
                    should_copy_source_156_2588()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=2589):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=2590) as copy_dir_to_dir_157_2590:  # ?
                            copy_dir_to_dir_157_2590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=2591) as unwtar_158_2591:  # ?
                            unwtar_158_2591()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=2592, recursive=True) as chown_159_2592:  # 0m:0.000s
                            chown_159_2592()
            with Stage(r"copy", r"WavesLib1_15_5_139_322 v15.5.139.322", prog_num=2593):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2594) as should_copy_source_160_2594:  # ?
                    should_copy_source_160_2594()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.139.framework", prog_num=2595):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r".", delete_extraneous_files=True, prog_num=2596) as copy_dir_to_dir_161_2596:  # ?
                            copy_dir_to_dir_161_2596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", where_to_unwtar=r".", prog_num=2597) as unwtar_162_2597:  # ?
                            unwtar_162_2597()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.139.framework", user_id=-1, group_id=-1, prog_num=2598, recursive=True) as chown_163_2598:  # 0m:0.000s
                            chown_163_2598()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=2599):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2600) as should_copy_source_164_2600:  # ?
                    should_copy_source_164_2600()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=2601):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=2602) as copy_dir_to_dir_165_2602:  # ?
                            copy_dir_to_dir_165_2602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=2603) as unwtar_166_2603:  # ?
                            unwtar_166_2603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=2604, recursive=True) as chown_167_2604:  # 0m:0.003s
                            chown_167_2604()
            with Stage(r"copy", r"WavesTune v15.5.79.262", prog_num=2605):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2606) as should_copy_source_168_2606:  # ?
                    should_copy_source_168_2606()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=2607):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=2608) as copy_dir_to_dir_169_2608:  # ?
                            copy_dir_to_dir_169_2608()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=2609) as unwtar_170_2609:  # ?
                            unwtar_170_2609()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=2610, recursive=True) as chown_171_2610:  # 0m:0.000s
                            chown_171_2610()
            with Stage(r"copy", r"WavesTune LT v15.5.79.262", prog_num=2611):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2612) as should_copy_source_172_2612:  # ?
                    should_copy_source_172_2612()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=2613):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=2614) as copy_dir_to_dir_173_2614:  # ?
                            copy_dir_to_dir_173_2614()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=2615) as unwtar_174_2615:  # ?
                            unwtar_174_2615()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=2616, recursive=True) as chown_175_2616:  # 0m:0.000s
                            chown_175_2616()
            with Stage(r"copy", r"Waves Harmony v15.5.139.322", prog_num=2617):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2618) as should_copy_source_176_2618:  # ?
                    should_copy_source_176_2618()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=2619):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=2620) as copy_dir_to_dir_177_2620:  # ?
                            copy_dir_to_dir_177_2620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=2621) as unwtar_178_2621:  # ?
                            unwtar_178_2621()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=2622, recursive=True) as chown_179_2622:  # 0m:0.000s
                            chown_179_2622()
            with Stage(r"copy", r"Waves Tune Real-Time v15.5.79.262", prog_num=2623):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=2624) as should_copy_source_180_2624:  # ?
                    should_copy_source_180_2624()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=2625):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=2626) as copy_dir_to_dir_181_2626:  # ?
                            copy_dir_to_dir_181_2626()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=2627) as unwtar_182_2627:  # ?
                            unwtar_182_2627()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=2628, recursive=True) as chown_183_2628:  # 0m:0.000s
                            chown_183_2628()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=4, prog_num=2632) as resolve_symlink_files_in_folder_184_2632:  # 0m:1.021s
                resolve_symlink_files_in_folder_184_2632()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=2633) as shell_command_185_2633:  # 0m:0.101s
                shell_command_185_2633()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=2634) as script_command_186_2634:  # 0m:0.008s
                script_command_186_2634()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2635) as shell_command_187_2635:  # 0m:0.017s
                shell_command_187_2635()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=2636) as create_symlink_188_2636:  # 0m:0.001s
                create_symlink_188_2636()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=2637) as create_symlink_189_2637:  # 0m:0.000s
                create_symlink_189_2637()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=2638) as copy_glob_to_dir_190_2638:  # 0m:0.104s
                copy_glob_to_dir_190_2638()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=2639) as cd_stage_191_2639:  # 0m:0.000s
            cd_stage_191_2639()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=2640):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=2641) as should_copy_source_192_2641:  # ?
                    should_copy_source_192_2641()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=2642):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=2643) as copy_file_to_dir_193_2643:  # ?
                            copy_file_to_dir_193_2643()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=2644) as chmod_and_chown_194_2644:  # 0m:0.000s
                            chmod_and_chown_194_2644()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/ReWire", prog_num=2645) as cd_stage_195_2645:  # 0m:0.124s
            cd_stage_195_2645()
            with Stage(r"copy", r"backup ReWire to Waves folder", prog_num=2646):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=2647) as should_copy_source_196_2647:  # ?
                    should_copy_source_196_2647()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=2648):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=2649) as copy_dir_to_dir_197_2649:  # ?
                            copy_dir_to_dir_197_2649()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=2650) as unwtar_198_2650:  # ?
                            unwtar_198_2650()
                        with Chown(path=r"/Applications/Waves/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=2651, recursive=True) as chown_199_2651:  # 0m:0.001s
                            chown_199_2651()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=2652) as should_copy_source_200_2652:  # ?
                    should_copy_source_200_2652()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=2653):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=2654) as copy_dir_to_dir_201_2654:  # ?
                            copy_dir_to_dir_201_2654()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=2655) as unwtar_202_2655:  # ?
                            unwtar_202_2655()
                        with Chown(path=r"/Applications/Waves/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=2656, recursive=True) as chown_203_2656:  # 0m:0.000s
                            chown_203_2656()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/ReWire" -c', ignore_all_errors=True, prog_num=2657) as shell_command_204_2657:  # 0m:0.107s
                shell_command_204_2657()
            with ScriptCommand(r'if [ -f "/Applications/Waves/ReWire"/Icon? ]; then chmod a+rw "/Applications/Waves/ReWire"/Icon?; fi', prog_num=2658) as script_command_205_2658:  # 0m:0.007s
                script_command_205_2658()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2659) as shell_command_206_2659:  # 0m:0.009s
                shell_command_206_2659()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=2660) as cd_stage_207_2660:  # 0m:0.013s
            cd_stage_207_2660()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=2661):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=2662) as should_copy_source_208_2662:  # ?
                    should_copy_source_208_2662()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=2663):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=2664) as copy_dir_to_dir_209_2664:  # ?
                            copy_dir_to_dir_209_2664()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=2665) as unwtar_210_2665:  # ?
                            unwtar_210_2665()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=2666, recursive=True) as chown_211_2666:  # ?
                            chown_211_2666()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=2667) as shell_command_212_2667:  # 0m:0.000s
                            shell_command_212_2667()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=2668):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=2669) as should_copy_source_213_2669:  # ?
                    should_copy_source_213_2669()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=2670):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=2671) as copy_dir_to_dir_214_2671:  # ?
                            copy_dir_to_dir_214_2671()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=2672) as unwtar_215_2672:  # ?
                            unwtar_215_2672()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=2673, recursive=True) as chown_216_2673:  # ?
                            chown_216_2673()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=2674) as break_hard_link_217_2674:  # ?
                            break_hard_link_217_2674()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=2675) as shell_command_218_2675:  # ?
                            shell_command_218_2675()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=2676, recursive=True) as chown_219_2676:  # ?
                            chown_219_2676()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=2677, recursive=True) as chmod_220_2677:  # 0m:0.000s
                            chmod_220_2677()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=2678):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=2679) as should_copy_source_221_2679:  # ?
                    should_copy_source_221_2679()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=2680):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=2681) as copy_dir_to_dir_222_2681:  # ?
                            copy_dir_to_dir_222_2681()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=2682) as unwtar_223_2682:  # ?
                            unwtar_223_2682()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=2683, recursive=True) as chown_224_2683:  # ?
                            chown_224_2683()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=2684) as shell_command_225_2684:  # 0m:0.001s
                            shell_command_225_2684()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=2685):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=2686) as should_copy_source_226_2686:  # ?
                    should_copy_source_226_2686()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=2687):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=2688) as copy_dir_to_dir_227_2688:  # ?
                            copy_dir_to_dir_227_2688()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=2689) as unwtar_228_2689:  # ?
                            unwtar_228_2689()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=2690, recursive=True) as chown_229_2690:  # ?
                            chown_229_2690()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=2691) as shell_command_230_2691:  # ?
                            shell_command_230_2691()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=2692) as script_command_231_2692:  # ?
                            script_command_231_2692()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2693) as shell_command_232_2693:  # 0m:0.001s
                            shell_command_232_2693()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=2694):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=2695) as should_copy_source_233_2695:  # ?
                    should_copy_source_233_2695()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=2696):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=2697) as copy_dir_to_dir_234_2697:  # ?
                            copy_dir_to_dir_234_2697()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=2698) as unwtar_235_2698:  # ?
                            unwtar_235_2698()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=2699, recursive=True) as chown_236_2699:  # 0m:0.000s
                            chown_236_2699()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=2700) as shell_command_237_2700:  # 0m:0.007s
                shell_command_237_2700()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=2701) as cd_stage_238_2701:  # 0m:0.001s
            cd_stage_238_2701()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=2702):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=2703) as should_copy_source_239_2703:  # ?
                    should_copy_source_239_2703()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=2704):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=2705) as copy_dir_to_dir_240_2705:  # ?
                            copy_dir_to_dir_240_2705()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=2706) as unwtar_241_2706:  # ?
                            unwtar_241_2706()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=2707, recursive=True) as chown_242_2707:  # ?
                            chown_242_2707()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=2708) as shell_command_243_2708:  # 0m:0.001s
                            shell_command_243_2708()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=2709) as cd_stage_244_2709:  # 0m:0.019s
            cd_stage_244_2709()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=2710):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2711) as should_copy_source_245_2711:  # 0m:0.001s
                    should_copy_source_245_2711()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=2712):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=2713) as copy_file_to_dir_246_2713:  # 0m:0.001s
                            copy_file_to_dir_246_2713()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2714) as chmod_and_chown_247_2714:  # 0m:0.000s
                            chmod_and_chown_247_2714()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=2715):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2716) as should_copy_source_248_2716:  # 0m:0.001s
                    should_copy_source_248_2716()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=2717):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=2718) as copy_file_to_dir_249_2718:  # 0m:0.001s
                            copy_file_to_dir_249_2718()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2719) as chmod_and_chown_250_2719:  # 0m:0.000s
                            chmod_and_chown_250_2719()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=2720):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2721) as should_copy_source_251_2721:  # 0m:0.004s
                    should_copy_source_251_2721()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=2722):  # 0m:0.004s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=2723) as copy_file_to_dir_252_2723:  # 0m:0.003s
                            copy_file_to_dir_252_2723()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2724) as chmod_and_chown_253_2724:  # 0m:0.000s
                            chmod_and_chown_253_2724()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=2725):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2726) as should_copy_source_254_2726:  # 0m:0.001s
                    should_copy_source_254_2726()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=2727):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=2728) as copy_file_to_dir_255_2728:  # 0m:0.000s
                            copy_file_to_dir_255_2728()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2729) as chmod_and_chown_256_2729:  # 0m:0.000s
                            chmod_and_chown_256_2729()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=2730):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2731) as should_copy_source_257_2731:  # 0m:0.001s
                    should_copy_source_257_2731()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=2732):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=2733) as copy_file_to_dir_258_2733:  # 0m:0.001s
                            copy_file_to_dir_258_2733()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2734) as chmod_and_chown_259_2734:  # 0m:0.000s
                            chmod_and_chown_259_2734()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=2735):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2736) as should_copy_source_260_2736:  # 0m:0.001s
                    should_copy_source_260_2736()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=2737):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=2738) as copy_file_to_dir_261_2738:  # 0m:0.000s
                            copy_file_to_dir_261_2738()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2739) as chmod_and_chown_262_2739:  # 0m:0.000s
                            chmod_and_chown_262_2739()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=2740):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=2741) as should_copy_source_263_2741:  # 0m:0.001s
                    should_copy_source_263_2741()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=2742):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=2743) as copy_file_to_dir_264_2743:  # 0m:0.000s
                            copy_file_to_dir_264_2743()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=2744) as chmod_and_chown_265_2744:  # 0m:0.000s
                            chmod_and_chown_265_2744()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=2745) as resolve_config_vars_in_file_266_2745:  # 0m:0.003s
                resolve_config_vars_in_file_266_2745()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=2746) as if_267_2746:  # 0m:0.001s
                if_267_2746()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=2747) as resolve_config_vars_in_file_268_2747:  # 0m:0.000s
                resolve_config_vars_in_file_268_2747()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=2748) as if_269_2748:  # 0m:0.000s
                if_269_2748()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=2749) as resolve_config_vars_in_file_270_2749:  # 0m:0.000s
                resolve_config_vars_in_file_270_2749()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=2750) as if_271_2750:  # 0m:0.000s
                if_271_2750()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=2751) as resolve_config_vars_in_file_272_2751:  # 0m:0.000s
                resolve_config_vars_in_file_272_2751()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=2752) as if_273_2752:  # 0m:0.000s
                if_273_2752()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=2753) as resolve_config_vars_in_file_274_2753:  # 0m:0.000s
                resolve_config_vars_in_file_274_2753()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=2754) as if_275_2754:  # 0m:0.000s
                if_275_2754()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=2755) as resolve_config_vars_in_file_276_2755:  # 0m:0.000s
                resolve_config_vars_in_file_276_2755()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=2756) as if_277_2756:  # 0m:0.000s
                if_277_2756()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=2757) as resolve_config_vars_in_file_278_2757:  # 0m:0.000s
                resolve_config_vars_in_file_278_2757()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=2758) as if_279_2758:  # 0m:0.000s
                if_279_2758()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=2759) as cd_stage_280_2759:  # 0m:0.018s
            cd_stage_280_2759()
            with Stage(r"copy", r"WavesReWireDevice v13.0.0.129", prog_num=2760):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=2761) as should_copy_source_281_2761:  # ?
                    should_copy_source_281_2761()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=2762):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=2763) as copy_dir_to_dir_282_2763:  # ?
                            copy_dir_to_dir_282_2763()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=2764) as unwtar_283_2764:  # ?
                            unwtar_283_2764()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=2765, recursive=True) as chown_284_2765:  # 0m:0.001s
                            chown_284_2765()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=2766) as should_copy_source_285_2766:  # ?
                    should_copy_source_285_2766()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=2767):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=2768) as copy_dir_to_dir_286_2768:  # ?
                            copy_dir_to_dir_286_2768()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=2769) as unwtar_287_2769:  # ?
                            unwtar_287_2769()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=2770, recursive=True) as chown_288_2770:  # 0m:0.000s
                            chown_288_2770()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2771) as shell_command_289_2771:  # 0m:0.017s
                shell_command_289_2771()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=2772) as cd_stage_290_2772:  # 0m:0.169s
            cd_stage_290_2772()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=2773):  # 0m:0.024s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=2774) as should_copy_source_291_2774:  # 0m:0.023s
                    should_copy_source_291_2774()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=2775):  # 0m:0.023s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=2776) as copy_dir_to_dir_292_2776:  # 0m:0.023s
                            copy_dir_to_dir_292_2776()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=2777, recursive=True) as chown_293_2777:  # 0m:0.000s
                            chown_293_2777()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=2778):  # 0m:0.145s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=2779) as should_copy_source_294_2779:  # 0m:0.145s
                    should_copy_source_294_2779()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=2780):  # 0m:0.144s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=2781) as copy_dir_to_dir_295_2781:  # 0m:0.098s
                            copy_dir_to_dir_295_2781()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=2782) as unwtar_296_2782:  # 0m:0.046s
                            unwtar_296_2782()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=2783, recursive=True) as chown_297_2783:  # 0m:0.000s
                            chown_297_2783()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=2784) as cd_stage_298_2784:  # 0m:0.099s
            cd_stage_298_2784()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=2785):  # 0m:0.099s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=2786) as should_copy_source_299_2786:  # 0m:0.099s
                    should_copy_source_299_2786()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=2787):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=2788) as copy_dir_to_dir_300_2788:  # 0m:0.019s
                            copy_dir_to_dir_300_2788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=2789) as unwtar_301_2789:  # 0m:0.079s
                            unwtar_301_2789()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=2790, recursive=True) as chown_302_2790:  # 0m:0.000s
                            chown_302_2790()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=2791) as cd_stage_303_2791:  # 0m:0.003s
            cd_stage_303_2791()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=2792):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=2793) as should_copy_source_304_2793:  # ?
                    should_copy_source_304_2793()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=2794):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=2795) as copy_dir_to_dir_305_2795:  # ?
                            copy_dir_to_dir_305_2795()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=2796, recursive=True) as chown_306_2796:  # 0m:0.000s
                            chown_306_2796()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=2797) as cd_stage_307_2797:  # 0m:0.001s
            cd_stage_307_2797()
            with Stage(r"copy", r"License Notifications 1.1 v1.1", prog_num=2798):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=2799) as should_copy_source_308_2799:  # ?
                    should_copy_source_308_2799()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=2800):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=2801) as copy_dir_to_dir_309_2801:  # ?
                            copy_dir_to_dir_309_2801()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=2802, recursive=True) as chown_310_2802:  # 0m:0.000s
                            chown_310_2802()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=2803) as cd_stage_311_2803:  # 0m:7.701s
            cd_stage_311_2803()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=2804) as rm_file_or_dir_312_2804:  # 0m:0.000s
                rm_file_or_dir_312_2804()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=2805):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=2806) as should_copy_source_313_2806:  # ?
                    should_copy_source_313_2806()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=2807):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=2808) as copy_dir_to_dir_314_2808:  # ?
                            copy_dir_to_dir_314_2808()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=2809) as unwtar_315_2809:  # ?
                            unwtar_315_2809()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=2810, recursive=True) as chown_316_2810:  # 0m:0.000s
                            chown_316_2810()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=2811):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=2812) as should_copy_source_317_2812:  # 0m:0.003s
                    should_copy_source_317_2812()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=2813):  # 0m:0.003s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=2814) as unwtar_318_2814:  # 0m:0.003s
                            unwtar_318_2814()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=2815):  # 0m:4.307s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=2816) as should_copy_source_319_2816:  # 0m:4.307s
                    should_copy_source_319_2816()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=2817):  # 0m:4.307s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=2818) as copy_dir_to_dir_320_2818:  # 0m:0.012s
                            copy_dir_to_dir_320_2818()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=2819) as unwtar_321_2819:  # 0m:4.294s
                            unwtar_321_2819()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=2820, recursive=True) as chown_322_2820:  # 0m:0.000s
                            chown_322_2820()
            with Stage(r"copy", r"OpenVino_2021.4.689 v2021.4.689", prog_num=2821):  # 0m:3.378s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=2822) as should_copy_source_323_2822:  # 0m:3.378s
                    should_copy_source_323_2822()
                    with Stage(r"copy source", r"Mac/Modules/openvino", prog_num=2823):  # 0m:3.378s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r".", delete_extraneous_files=True, prog_num=2824) as copy_dir_to_dir_324_2824:  # 0m:0.120s
                            copy_dir_to_dir_324_2824()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", where_to_unwtar=r".", prog_num=2825) as unwtar_325_2825:  # 0m:3.257s
                            unwtar_325_2825()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/openvino", user_id=-1, group_id=-1, prog_num=2826, recursive=True) as chown_326_2826:  # 0m:0.000s
                            chown_326_2826()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=2827):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=2828) as should_copy_source_327_2828:  # ?
                    should_copy_source_327_2828()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=2829):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=2830) as copy_dir_to_dir_328_2830:  # ?
                            copy_dir_to_dir_328_2830()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=2831) as chmod_329_2831:  # ?
                            chmod_329_2831()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=2832) as chmod_330_2832:  # ?
                            chmod_330_2832()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=2833, recursive=True) as chown_331_2833:  # 0m:0.000s
                            chown_331_2833()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=2836) as resolve_symlink_files_in_folder_332_2836:  # 0m:0.002s
                resolve_symlink_files_in_folder_332_2836()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2837) as shell_command_333_2837:  # 0m:0.010s
                shell_command_333_2837()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=2838) as cd_stage_334_2838:  # 0m:0.001s
            cd_stage_334_2838()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=2839):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=2840) as should_copy_source_335_2840:  # ?
                    should_copy_source_335_2840()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=2841):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=2842) as copy_dir_to_dir_336_2842:  # ?
                            copy_dir_to_dir_336_2842()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=2843, recursive=True) as chown_337_2843:  # 0m:0.000s
                            chown_337_2843()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=2844) as cd_stage_338_2844:  # 0m:0.001s
            cd_stage_338_2844()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=2845):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=2846) as should_copy_source_339_2846:  # ?
                    should_copy_source_339_2846()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=2847):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=2848, recursive=True) as chmod_340_2848:  # ?
                            chmod_340_2848()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=2849) as copy_dir_to_dir_341_2849:  # ?
                            copy_dir_to_dir_341_2849()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=2850) as unwtar_342_2850:  # ?
                            unwtar_342_2850()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=2851, recursive=True) as chown_343_2851:  # ?
                            chown_343_2851()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=2852) as if_344_2852:  # 0m:0.000s
                            if_344_2852()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=2853) as cd_stage_345_2853:  # 0m:0.001s
            cd_stage_345_2853()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.178.179", prog_num=2854):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=2855) as should_copy_source_346_2855:  # ?
                    should_copy_source_346_2855()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=2856):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=2857) as copy_dir_to_dir_347_2857:  # ?
                            copy_dir_to_dir_347_2857()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=2858) as unwtar_348_2858:  # ?
                            unwtar_348_2858()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=2859, recursive=True) as chown_349_2859:  # ?
                            chown_349_2859()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=2860) as if_350_2860:  # 0m:0.000s
                            if_350_2860()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=2861) as cd_stage_351_2861:  # 0m:1.014s
            cd_stage_351_2861()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=2862):  # 0m:1.014s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=2863) as should_copy_source_352_2863:  # 0m:1.014s
                    should_copy_source_352_2863()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=2864):  # 0m:1.013s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=2865) as copy_dir_to_dir_353_2865:  # 0m:0.062s
                            copy_dir_to_dir_353_2865()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=2866) as unwtar_354_2866:  # 0m:0.892s
                            unwtar_354_2866()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=2867, recursive=True) as chown_355_2867:  # 0m:0.000s
                            chown_355_2867()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=2868) as break_hard_link_356_2868:  # 0m:0.011s
                            break_hard_link_356_2868()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=2869) as shell_command_357_2869:  # 0m:0.044s
                            shell_command_357_2869()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=2870, recursive=True) as chown_358_2870:  # 0m:0.000s
                            chown_358_2870()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=2871, recursive=True) as chmod_359_2871:  # 0m:0.004s
                            chmod_359_2871()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=2872) as cd_stage_360_2872:  # 0m:0.001s
            cd_stage_360_2872()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=2873):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=2874) as should_copy_source_361_2874:  # ?
                    should_copy_source_361_2874()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=2875):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=2876) as copy_dir_to_dir_362_2876:  # ?
                            copy_dir_to_dir_362_2876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=2877) as unwtar_363_2877:  # ?
                            unwtar_363_2877()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=2878, recursive=True) as chown_364_2878:  # ?
                            chown_364_2878()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=2879) as shell_command_365_2879:  # 0m:0.000s
                            shell_command_365_2879()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=2880) as cd_stage_366_2880:  # 0m:0.001s
            cd_stage_366_2880()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=2881):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=2882) as should_copy_source_367_2882:  # ?
                    should_copy_source_367_2882()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=2883):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=2884) as copy_dir_to_dir_368_2884:  # ?
                            copy_dir_to_dir_368_2884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=2885) as unwtar_369_2885:  # ?
                            unwtar_369_2885()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=2886, recursive=True) as chown_370_2886:  # ?
                            chown_370_2886()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=2887) as shell_command_371_2887:  # ?
                            shell_command_371_2887()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=2888) as script_command_372_2888:  # ?
                            script_command_372_2888()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=2889) as shell_command_373_2889:  # 0m:0.001s
                            shell_command_373_2889()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=2890) as create_symlink_374_2890:  # 0m:0.000s
                create_symlink_374_2890()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=2891) as create_symlink_375_2891:  # 0m:0.000s
                create_symlink_375_2891()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=2892) as shell_command_376_2892:  # 0m:0.003s
            shell_command_376_2892()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=2893) as shell_command_377_2893:  # 0m:0.102s
            shell_command_377_2893()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=2894) as script_command_378_2894:  # 0m:0.007s
            script_command_378_2894()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=2895) as rm_file_or_dir_379_2895:  # 0m:0.001s
            rm_file_or_dir_379_2895()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=2896) as shell_command_380_2896:  # 0m:0.091s
            shell_command_380_2896()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=2897) as script_command_381_2897:  # 0m:0.007s
            script_command_381_2897()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=2898) as rm_file_or_dir_382_2898:  # 0m:0.000s
            rm_file_or_dir_382_2898()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=2899) as glober_383_2899:  # 0m:0.001s
            glober_383_2899()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=2900) as glober_384_2900:  # 0m:0.001s
            glober_384_2900()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=2901) as glober_385_2901:  # 0m:0.001s
            glober_385_2901()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=2902) as shell_command_386_2902:  # 0m:2.384s
            shell_command_386_2902()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=2903) as shell_command_387_2903:  # 0m:0.095s
            shell_command_387_2903()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=2904) as script_command_388_2904:  # 0m:0.007s
            script_command_388_2904()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=2905) as if_389_2905:  # 0m:0.000s
            if_389_2905()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=2906) as if_390_2906:  # 0m:0.000s
            if_390_2906()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=2907) as if_391_2907:  # 0m:0.000s
            if_391_2907()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=2908) as if_392_2908:  # 0m:0.000s
            if_392_2908()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=2909) as make_dir_393_2909:  # 0m:0.005s
            make_dir_393_2909()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=2910) as chmod_394_2910:  # 0m:0.000s
            chmod_394_2910()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=2911) as make_dir_395_2911:  # 0m:0.004s
            make_dir_395_2911()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=2912) as chmod_396_2912:  # 0m:0.000s
            chmod_396_2912()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=2913) as chmod_397_2913:  # 0m:0.000s
            chmod_397_2913()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=2914) as chmod_398_2914:  # 0m:0.003s
            chmod_398_2914()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=2915) as chmod_399_2915:  # 0m:0.000s
            chmod_399_2915()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=2916) as shell_command_400_2916:  # 0m:0.092s
            shell_command_400_2916()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=2917) as script_command_401_2917:  # 0m:0.007s
            script_command_401_2917()
    with Stage(r"post-copy", prog_num=2918):  # 0m:0.029s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=2919) as make_dir_402_2919:  # 0m:0.006s
            make_dir_402_2919()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=2920) as copy_file_to_file_403_2920:  # 0m:0.007s
            copy_file_to_file_403_2920()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=2921) as chmod_404_2921:  # 0m:0.001s
            chmod_404_2921()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=2922) as chmod_405_2922:  # 0m:0.000s
            chmod_405_2922()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=2923) as copy_file_to_file_406_2923:  # 0m:0.006s
            copy_file_to_file_406_2923()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=2924) as chmod_407_2924:  # 0m:0.000s
            chmod_407_2924()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=2925) as copy_file_to_file_408_2925:  # 0m:0.004s
            copy_file_to_file_408_2925()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=2926) as chmod_409_2926:  # 0m:0.003s
            chmod_409_2926()
        Progress(r"Done copy", prog_num=2927)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=2928)()  # 0m:0.000s
    with Stage(r"post", prog_num=2929):  # 0m:0.031s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=2930) as make_dir_410_2930:  # 0m:0.004s
            make_dir_410_2930()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=2931) as copy_file_to_file_411_2931:  # 0m:0.007s
            copy_file_to_file_411_2931()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=2932) as make_dir_412_2932:  # 0m:0.006s
            make_dir_412_2932()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=2933) as copy_file_to_file_413_2933:  # 0m:0.004s
            copy_file_to_file_413_2933()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=2934) as make_dir_414_2934:  # 0m:0.005s
            make_dir_414_2934()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/60/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=2935) as copy_file_to_file_415_2935:  # 0m:0.004s
            copy_file_to_file_415_2935()

with Stage(r"epilog", prog_num=2936):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250712163752.py", prog_num=2937) as patch_py_batch_with_timings_416_2937:  # ?
        patch_py_batch_with_timings_416_2937()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# copy time 0m:37.897s
