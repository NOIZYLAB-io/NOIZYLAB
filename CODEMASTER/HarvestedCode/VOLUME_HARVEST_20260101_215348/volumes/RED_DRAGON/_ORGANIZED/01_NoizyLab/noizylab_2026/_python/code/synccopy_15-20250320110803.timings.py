# Creation time: 20-03-25_11-08
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 6674
PythonBatchCommandBase.running_progress = 611
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=612):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250320110803"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/Video Sound Suite Impulses", r"/Applications/Waves/Data/Video Sound Suite Impulses")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.4.4"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V15", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V15", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 43
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MjUxOTI4NH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQyNDgyOTg0fX19XX0_;CloudFront-Signature=gJHzf7yo3iTQ-ryI9Nnk2xkIIE0PMGwaNtv9f3EFXEk2Ii2pWSGxq6wswyY4gfLUdQRHJlr9yIImH~0sw77RTGwQTj0QP4OC6qjvQHEw2tG0Ke2RMOuXXSz4gmp~IO585~s1sRdKPhHPNJCHXEbfQtXK-M1yXFCaYOzhEzJla-waLIhQZNNgJbWWpekuIltci9FpxsIT5HS0T5orIdpDcMfzrI1c~IQ1w~swZlVdsawaZ3LsW3pbc9Xr-vQ2DLQIPPN-2PbH16vrLS7UXdB4wYHHCESpqrRlrMw7AKkYuiMU~PawoF~Vz91oWi16YI9MhnWSbQiAol3FWAS8cEROTQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0MjUxOTI4NH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQyNDgyOTg0fX19XX0_;CloudFront-Signature=gJHzf7yo3iTQ-ryI9Nnk2xkIIE0PMGwaNtv9f3EFXEk2Ii2pWSGxq6wswyY4gfLUdQRHJlr9yIImH~0sw77RTGwQTj0QP4OC6qjvQHEw2tG0Ke2RMOuXXSz4gmp~IO585~s1sRdKPhHPNJCHXEbfQtXK-M1yXFCaYOzhEzJla-waLIhQZNNgJbWWpekuIltci9FpxsIT5HS0T5orIdpDcMfzrI1c~IQ1w~swZlVdsawaZ3LsW3pbc9Xr-vQ2DLQIPPN-2PbH16vrLS7UXdB4wYHHCESpqrRlrMw7AKkYuiMU~PawoF~Vz91oWi16YI9MhnWSbQiAol3FWAS8cEROTQ__"
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
    config_vars['INDEX_CHECKSUM'] = r"3f11ba1bd989ecea2be5ef80b7837423b554bce0"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/43/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"79ee9586466dcdd7284843ec12a41ddbcf4aa5f5"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/43/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/43/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"215572dc-9c91-4912-a0a9-d68096edc994", r"3ddd87ba-616d-4b2e-b4ec-71dfee0e0230", r"45197058-00f3-4e1e-9381-cd0d545356b5", r"45a63c82-a4d3-43cb-926b-1daea4ffc4cc", r"507d025d-2709-4049-908f-7f9ae0a26e84", r"597fd39c-dc58-4d40-9a73-1bdc07a11e85", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"__UPDATE_INSTALLED_ITEMS__", r"c93e0e0e-c552-46d1-9dd1-3a8ea700ba3a", r"e143b292-29ba-4885-aae7-c7f52a22ffc9", r"e2521210-ad21-11e0-838c-b7fd7bebd530")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 43
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250320110803.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 43
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-03-10 10:59:21.187407"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/43"
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
    config_vars['SHORT_INDEX_CHECKSUM'] = r"167c6b3530575213695e279b2714325969b141d0"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/43/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 6058
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250320110803.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"unknown compilation time"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.3.2"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"SV_Instruments_Presets_IID", r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID", r"Instrument_Data_NKS_FX_EMO_D5_IID", r"Instrument_Data_NKS_FX_MannyM-Delay_IID", r"Instrument_Data_NKS_FX_OVox_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"Abbey_Road_Saturator_Presets_IID", r"AnalyzeAudioBundle_IID", r"Artist_DLLs_Common_Guid_IID", r"Berzerk_Distortion_Presets_IID", r"CLA_MixHub_IID", r"CLA_MixHub_Presets_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS__Data_Folders__IID", r"COSMOS__IID", r"COSMOS__Models_Data_Folders__IID", r"COSMOS_python_IID", r"CR8App_IID", r"CR8_Sampler_IID", r"CR8_Sampler_Presets_IID", r"Character_Filters_Data_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"EMO_D5_IID", r"FFmpeg_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"Get_General_Icons_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_NKS_FX_EMO_D5_IID", r"Instrument_Data_NKS_FX_MannyM-Delay_IID", r"Instrument_Data_NKS_FX_OVox_IID", r"IntelDlls_IID", r"LFE360_IID", r"LicenseNotifications_1_IID", r"MDMX_Fuzz_Presets_IID", r"MDMX_OverDrive_Presets_IID", r"MDMX_Screamer_Presets_IID", r"MIDIArpSeq_IID", r"MIDIChords_IID", r"MIDIKeyboard_IID", r"MIDIMonitor_IID", r"MIDIRange_IID", r"MIDITranspose_IID", r"MIDIVelocity_IID", r"MIDIVoicing_IID", r"MIDI_PLUGINS_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"MannyM-Delay_IID", r"Minimum_Requirements_IID", r"ModFX_Autopan_IID", r"ModFX_Chorus_IID", r"ModFX_Compressor_IID", r"ModFX_Delay_IID", r"ModFX_Distortion_IID", r"ModFX_IID", r"ModFX_Limiter_IID", r"ModFX_Reverb_IID", r"MultiMod_Presets_IID", r"MultiMod_Rack_IID", r"MultiMod_Shapes_folder_IID", r"MusicRack_IID", r"MusicRack_app_IID", r"Note_Mapping_Data_IID", r"ORS_Modulators_Data_IID", r"OVox_Instrument_Presets_IID", r"OVox_Presets_IID", r"OVox_Vocal_ReSynthesis_IID", r"OVox_app_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"S360_IID", r"SV_Instruments_Presets_IID", r"Shutdown_Servers_IID", r"StudioRack_Data_IID", r"StudioRack_IID", r"StudioRack_Impulses_IID", r"StudioRack_Presets_Compatibility_IID", r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID", r"TRACT_IID", r"V9_V10_Organizer_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_OBS_V15_5_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesLib1_15_5_139_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V15_2_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_EMO_D5_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-Delay_IID", r"XML_and_Registry_for_Native_Instruments_OVox_IID")
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.0 unknown compilation time RSPMS.local"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.0"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 0)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"lekitgigcvidrteg"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"Artist_DLLs_Common_Guid_IID", r"CLA_MixHub_IID", r"EMO_D5_IID", r"MannyM-Delay_IID", r"MultiMod_Rack_IID", r"MusicRack_IID", r"OVox_Vocal_ReSynthesis_IID", r"StudioRack_IID", r"TRACT_IID", r"Waves_Harmony_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = (r"CR8App_IID", r"CR8_Sampler_IID", r"LFE360_IID", r"MIDIArpSeq_IID", r"MIDIChords_IID", r"MIDIKeyboard_IID", r"MIDIMonitor_IID", r"MIDIRange_IID", r"MIDITranspose_IID", r"MIDIVelocity_IID", r"MIDIVoicing_IID", r"ModFX_Autopan_IID", r"ModFX_Chorus_IID", r"ModFX_Compressor_IID", r"ModFX_Delay_IID", r"ModFX_Distortion_IID", r"ModFX_Limiter_IID", r"ModFX_Reverb_IID", r"MusicRack_app_IID", r"OVox_app_IID", r"S360_IID", r"WaveShell1_AAX_15_5_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID")
    config_vars['__NOW__'] = r"2025-03-20 11:08:54.921699"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 218750888
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 253
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"RSPMS.local"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=613):  # 1m:33.932s
    with Stage(r"begin", prog_num=614):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=615):  # 0m:0.014s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=616) as copy_file_to_file_001_616:  # 0m:0.006s
            copy_file_to_file_001_616()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=617) as copy_file_to_file_002_617:  # 0m:0.008s
            copy_file_to_file_002_617()
    with Stage(r"sync", prog_num=618):  # 0m:51.047s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=619) as shell_command_003_619:  # 0m:0.013s
            shell_command_003_619()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=620) as shell_command_004_620:  # 0m:0.014s
            shell_command_004_620()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=621) as shell_command_005_621:  # 0m:44.421s
            shell_command_005_621()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=622) as shell_command_006_622:  # 0m:0.008s
            shell_command_006_622()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=623) as shell_command_007_623:  # 0m:0.006s
            shell_command_007_623()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=624) as shell_command_008_624:  # 0m:0.006s
            shell_command_008_624()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=625) as shell_command_009_625:  # 0m:0.005s
            shell_command_009_625()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=626) as shell_command_010_626:  # 0m:1.501s
            shell_command_010_626()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=627):  # 0m:5.073s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=628) as make_dir_011_628:  # 0m:0.008s
                make_dir_011_628()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=629) as cd_012_629:  # 0m:5.064s
                cd_012_629()
                with Stage(r"remove_redundant_files_in_sync_folder", prog_num=630):  # 0m:0.200s
                    with RmFile(r"Mac/Plugins/CLA MixHub.bundle/Contents/PlugIns/CLAMHComp.bundle/Contents/PNG_.zip.wtar.aa", prog_num=631) as rm_file_013_631:  # 0m:0.001s
                        rm_file_013_631()
                    with RmFile(r"Mac/Plugins/CLA MixHub.bundle/Contents/PlugIns/CLAMHComp.bundle/Contents/PNG_.zip.wtar.ab", prog_num=632) as rm_file_014_632:  # 0m:0.001s
                        rm_file_014_632()
                    with RmFile(r"Mac/Plugins/CLA MixHub.bundle/Contents/PlugIns/CLAMHEQ.bundle/Contents/PNG_.zip.wtar.aa", prog_num=633) as rm_file_015_633:  # 0m:0.001s
                        rm_file_015_633()
                    with RmFile(r"Mac/Plugins/CLA MixHub.bundle/Contents/PlugIns/CLAMHEQ.bundle/Contents/PNG_.zip.wtar.ab", prog_num=634) as rm_file_016_634:  # 0m:0.000s
                        rm_file_016_634()
                    with RemoveEmptyFolders(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=635) as remove_empty_folders_017_635:  # 0m:0.197s
                        remove_empty_folders_017_635()
                Progress(r"4725 files already in cache", own_progress_count=4725, prog_num=5360)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=154, prog_num=5514) as create_sync_folders_018_5514:  # 0m:0.834s
                    create_sync_folders_018_5514()
                Progress(r"Downloading with 50 processes in parallel", prog_num=5515)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=5516)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.py_curl/dl-00", total_files_to_download=253, previously_downloaded_files=0, total_bytes_to_download=218750888, own_progress_count=195, prog_num=5711, report_own_progress=False) as curl_with_internal_parallel_019_5711:  # 0m:3.333s
                    curl_with_internal_parallel_019_5711()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.py_curl/dl-01", total_files_to_download=253, previously_downloaded_files=195, total_bytes_to_download=218750888, own_progress_count=58, prog_num=5769, report_own_progress=False) as curl_with_internal_parallel_020_5769:  # 0m:0.200s
                    curl_with_internal_parallel_020_5769()
                Progress(r"Downloading 253 files done", prog_num=5770)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=5771) as run_in_thread_021_5771:  # 0m:0.001s
                    run_in_thread_021_5771()
                Progress(r"Check checksum ...", prog_num=5772)()  # 0m:0.000s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=253, prog_num=6025) as check_download_folder_checksum_022_6025:  # 0m:0.251s
                    check_download_folder_checksum_022_6025()
                with Stage(r"post_sync", prog_num=6026):  # 0m:0.244s
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15...", prog_num=6027)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=6028, recursive=True) as chmod_and_chown_023_6028:  # 0m:0.230s
                        chmod_and_chown_023_6028()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=6029) as copy_file_to_file_024_6029:  # 0m:0.013s
                        copy_file_to_file_024_6029()
            Progress(r"Done sync", prog_num=6030)()  # 0m:0.000s
    with Stage(r"copy", prog_num=6031):  # 0m:42.788s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=6032)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=6033):  # 0m:0.240s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=6034) as make_dir_025_6034:  # 0m:0.010s
                make_dir_025_6034()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=6035) as make_dir_026_6035:  # 0m:0.005s
                make_dir_026_6035()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=6036) as make_dir_027_6036:  # 0m:0.008s
                make_dir_027_6036()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=6037) as make_dir_028_6037:  # 0m:0.006s
                make_dir_028_6037()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=6038) as make_dir_029_6038:  # 0m:0.016s
                make_dir_029_6038()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=6039) as make_dir_030_6039:  # 0m:0.012s
                make_dir_030_6039()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=6040) as make_dir_031_6040:  # 0m:0.011s
                make_dir_031_6040()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=6041) as make_dir_032_6041:  # 0m:0.011s
                make_dir_032_6041()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/MIDI", chowner=True, prog_num=6042) as make_dir_033_6042:  # 0m:0.006s
                make_dir_033_6042()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/ModFX", chowner=True, prog_num=6043) as make_dir_034_6043:  # 0m:0.009s
                make_dir_034_6043()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=6044) as make_dir_035_6044:  # 0m:0.006s
                make_dir_035_6044()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=6045) as make_dir_036_6045:  # 0m:0.004s
                make_dir_036_6045()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=6046) as make_dir_037_6046:  # 0m:0.005s
                make_dir_037_6046()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=6047) as make_dir_038_6047:  # 0m:0.007s
                make_dir_038_6047()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=6048) as make_dir_039_6048:  # 0m:0.008s
                make_dir_039_6048()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=6049) as make_dir_040_6049:  # 0m:0.010s
                make_dir_040_6049()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=6050) as make_dir_041_6050:  # 0m:0.006s
                make_dir_041_6050()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=6051) as make_dir_042_6051:  # 0m:0.010s
                make_dir_042_6051()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=6052) as make_dir_043_6052:  # 0m:0.005s
                make_dir_043_6052()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=6053) as make_dir_044_6053:  # 0m:0.009s
                make_dir_044_6053()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=6054) as make_dir_045_6054:  # 0m:0.009s
                make_dir_045_6054()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=6055) as make_dir_046_6055:  # 0m:0.005s
                make_dir_046_6055()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=6056) as make_dir_047_6056:  # 0m:0.009s
                make_dir_047_6056()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=6057) as make_dir_048_6057:  # 0m:0.006s
                make_dir_048_6057()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=6058) as make_dir_049_6058:  # 0m:0.011s
                make_dir_049_6058()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=6059) as make_dir_050_6059:  # 0m:0.011s
                make_dir_050_6059()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=6060) as make_dir_051_6060:  # 0m:0.006s
                make_dir_051_6060()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=6061) as make_dir_052_6061:  # 0m:0.005s
                make_dir_052_6061()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings/MMod", chowner=True, prog_num=6062) as make_dir_053_6062:  # 0m:0.006s
                make_dir_053_6062()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=6063) as make_dir_054_6063:  # 0m:0.007s
                make_dir_054_6063()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=6064) as rm_file_or_dir_055_6064:  # 0m:0.000s
            rm_file_or_dir_055_6064()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=6065) as shell_command_056_6065:  # 0m:0.011s
            shell_command_056_6065()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=6066) as shell_command_057_6066:  # 0m:0.012s
            shell_command_057_6066()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=6067) as shell_command_058_6067:  # 0m:1.046s
            shell_command_058_6067()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=6068) as shell_command_059_6068:  # 0m:0.011s
            shell_command_059_6068()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=6069) as shell_command_060_6069:  # 0m:0.009s
            shell_command_060_6069()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=6070) as shell_command_061_6070:  # 0m:0.005s
            shell_command_061_6070()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=6071) as shell_command_062_6071:  # 0m:0.006s
            shell_command_062_6071()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=6072) as shell_command_063_6072:  # 0m:0.165s
            shell_command_063_6072()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=6073) as cd_stage_064_6073:  # 0m:0.013s
            cd_stage_064_6073()
            with SetExecPermissionsInSyncFolder(prog_num=6074) as set_exec_permissions_in_sync_folder_065_6074:  # 0m:0.012s
                set_exec_permissions_in_sync_folder_065_6074()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=6075) as cd_stage_066_6075:  # 0m:1.116s
            cd_stage_066_6075()
            with Stage(r"copy", r"CR8 Sampler application v15.5.139.322", prog_num=6076):  # 0m:0.318s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/CR8 Sampler.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=6077) as should_copy_source_067_6077:  # 0m:0.318s
                    should_copy_source_067_6077()
                    with Stage(r"copy source", r"Mac/Apps/CR8 Sampler.app", prog_num=6078):  # 0m:0.317s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/CR8 Sampler.app", r".", delete_extraneous_files=True, prog_num=6079) as copy_dir_to_dir_068_6079:  # 0m:0.034s
                            copy_dir_to_dir_068_6079()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/CR8 Sampler.app", where_to_unwtar=r".", prog_num=6080) as unwtar_069_6080:  # 0m:0.283s
                            unwtar_069_6080()
                        with Chown(path=r"/Applications/Waves/Applications V15/CR8 Sampler.app", user_id=-1, group_id=-1, prog_num=6081, recursive=True) as chown_070_6081:  # 0m:0.000s
                            chown_070_6081()
            with Stage(r"copy", r"StudioVerse Instruments App v15.5.139.322", prog_num=6082):  # 0m:0.320s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/StudioVerse Instruments.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=6083) as should_copy_source_071_6083:  # 0m:0.320s
                    should_copy_source_071_6083()
                    with Stage(r"copy source", r"Mac/Apps/StudioVerse Instruments.app", prog_num=6084):  # 0m:0.320s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/StudioVerse Instruments.app", r".", delete_extraneous_files=True, prog_num=6085) as copy_dir_to_dir_072_6085:  # 0m:0.032s
                            copy_dir_to_dir_072_6085()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/StudioVerse Instruments.app", where_to_unwtar=r".", prog_num=6086) as unwtar_073_6086:  # 0m:0.287s
                            unwtar_073_6086()
                        with Chown(path=r"/Applications/Waves/Applications V15/StudioVerse Instruments.app", user_id=-1, group_id=-1, prog_num=6087, recursive=True) as chown_074_6087:  # 0m:0.000s
                            chown_074_6087()
            with Stage(r"copy", r"OVox Vocal ReSynthesis application v15.5.139.322", prog_num=6088):  # 0m:0.328s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/OVox.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=6089) as should_copy_source_075_6089:  # 0m:0.328s
                    should_copy_source_075_6089()
                    with Stage(r"copy source", r"Mac/Apps/OVox.app", prog_num=6090):  # 0m:0.327s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/OVox.app", r".", delete_extraneous_files=True, prog_num=6091) as copy_dir_to_dir_076_6091:  # 0m:0.032s
                            copy_dir_to_dir_076_6091()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/OVox.app", where_to_unwtar=r".", prog_num=6092) as unwtar_077_6092:  # 0m:0.294s
                            unwtar_077_6092()
                        with Chown(path=r"/Applications/Waves/Applications V15/OVox.app", user_id=-1, group_id=-1, prog_num=6093, recursive=True) as chown_078_6093:  # 0m:0.000s
                            chown_078_6093()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=6094) as shell_command_079_6094:  # 0m:0.142s
                shell_command_079_6094()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=6095) as script_command_080_6095:  # 0m:0.008s
                script_command_080_6095()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=6096) as cd_stage_081_6096:  # 0m:0.008s
            cd_stage_081_6096()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=6097):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=6098) as should_copy_source_082_6098:  # ?
                    should_copy_source_082_6098()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=6099):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=6100) as copy_dir_to_dir_083_6100:  # ?
                            copy_dir_to_dir_083_6100()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=6101) as unwtar_084_6101:  # ?
                            unwtar_084_6101()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=6102, recursive=True) as chown_085_6102:  # 0m:0.001s
                            chown_085_6102()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=6112) as resolve_symlink_files_in_folder_086_6112:  # 0m:0.007s
                resolve_symlink_files_in_folder_086_6112()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=6113) as cd_stage_087_6113:  # 0m:0.059s
            cd_stage_087_6113()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=6114):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6115) as should_copy_source_088_6115:  # ?
                    should_copy_source_088_6115()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=6116):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=6117) as copy_dir_to_dir_089_6117:  # ?
                            copy_dir_to_dir_089_6117()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=6118, recursive=True) as chown_090_6118:  # 0m:0.004s
                            chown_090_6118()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=6119):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=6120) as should_copy_source_091_6120:  # ?
                    should_copy_source_091_6120()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=6121):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=6122) as copy_dir_to_dir_092_6122:  # ?
                            copy_dir_to_dir_092_6122()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=6123) as unwtar_093_6123:  # ?
                            unwtar_093_6123()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=6124, recursive=True) as chown_094_6124:  # 0m:0.000s
                            chown_094_6124()
            with Stage(r"copy", r"Character Filters Data v1.0.0.9", prog_num=6125):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Character Filters", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6126) as should_copy_source_095_6126:  # ?
                    should_copy_source_095_6126()
                    with Stage(r"copy source", r"Common/Data/Character Filters", prog_num=6127):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Character Filters", r".", delete_extraneous_files=True, prog_num=6128) as copy_dir_to_dir_096_6128:  # ?
                            copy_dir_to_dir_096_6128()
                        with Chown(path=r"/Applications/Waves/Data/Character Filters", user_id=-1, group_id=-1, prog_num=6129, recursive=True) as chown_097_6129:  # 0m:0.000s
                            chown_097_6129()
            with Stage(r"copy", r"Note Mapping Data v1.0.0.10", prog_num=6130):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Note Mapping", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=6131) as should_copy_source_098_6131:  # ?
                    should_copy_source_098_6131()
                    with Stage(r"copy source", r"Common/Data/Note Mapping", prog_num=6132):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Note Mapping", r".", delete_extraneous_files=True, prog_num=6133) as copy_dir_to_dir_099_6133:  # ?
                            copy_dir_to_dir_099_6133()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Note Mapping", where_to_unwtar=r".", prog_num=6134) as unwtar_100_6134:  # ?
                            unwtar_100_6134()
                        with Chown(path=r"/Applications/Waves/Data/Note Mapping", user_id=-1, group_id=-1, prog_num=6135, recursive=True) as chown_101_6135:  # 0m:0.000s
                            chown_101_6135()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=6136):  # 0m:0.028s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6137) as should_copy_source_102_6137:  # 0m:0.028s
                    should_copy_source_102_6137()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=6138):  # 0m:0.028s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=6139) as copy_dir_to_dir_103_6139:  # 0m:0.028s
                            copy_dir_to_dir_103_6139()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=6140, recursive=True) as chown_104_6140:  # 0m:0.000s
                            chown_104_6140()
            with Stage(r"copy", r"StudioRack Data v1.0.0.6", prog_num=6141):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=6142) as should_copy_source_105_6142:  # ?
                    should_copy_source_105_6142()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=6143):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=6144) as copy_dir_to_dir_106_6144:  # ?
                            copy_dir_to_dir_106_6144()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=6145) as unwtar_107_6145:  # ?
                            unwtar_107_6145()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=6146, recursive=True) as chown_108_6146:  # 0m:0.001s
                            chown_108_6146()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.2.0", prog_num=6147):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=6148) as should_copy_source_109_6148:  # ?
                    should_copy_source_109_6148()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=6149):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=6150) as copy_dir_to_dir_110_6150:  # ?
                            copy_dir_to_dir_110_6150()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=6151, recursive=True) as chown_111_6151:  # 0m:0.000s
                            chown_111_6151()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=6152):  # 0m:0.022s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=6153) as should_copy_source_112_6153:  # 0m:0.022s
                    should_copy_source_112_6153()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=6154):  # 0m:0.018s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=6155) as copy_dir_to_dir_113_6155:  # 0m:0.008s
                            copy_dir_to_dir_113_6155()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=6156) as unwtar_114_6156:  # 0m:0.009s
                            unwtar_114_6156()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=6157, recursive=True) as chown_115_6157:  # 0m:0.000s
                            chown_115_6157()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Chromatic.scale", prog_num=6158) as rm_file_or_dir_116_6158:  # 0m:0.000s
                rm_file_or_dir_116_6158()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Major.scale", prog_num=6159) as rm_file_or_dir_117_6159:  # 0m:0.000s
                rm_file_or_dir_117_6159()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Natural Minor.scale", prog_num=6160) as rm_file_or_dir_118_6160:  # 0m:0.000s
                rm_file_or_dir_118_6160()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=6161) as rm_globs_119_6161:  # 0m:0.000s
                rm_globs_119_6161()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=6162) as cd_stage_120_6162:  # 0m:0.029s
            cd_stage_120_6162()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=6163):  # 0m:0.029s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=6164) as should_copy_source_121_6164:  # 0m:0.012s
                    should_copy_source_121_6164()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=6165):  # 0m:0.012s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=6166) as copy_dir_to_dir_122_6166:  # 0m:0.012s
                            copy_dir_to_dir_122_6166()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=6167, recursive=True) as chown_123_6167:  # 0m:0.000s
                            chown_123_6167()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=6168) as should_copy_source_124_6168:  # 0m:0.016s
                    should_copy_source_124_6168()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=6169):  # 0m:0.016s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=6170) as copy_dir_to_dir_125_6170:  # 0m:0.013s
                            copy_dir_to_dir_125_6170()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=6171, recursive=True) as chown_126_6171:  # 0m:0.000s
                            chown_126_6171()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=6172) as cd_stage_127_6172:  # 0m:0.009s
            cd_stage_127_6172()
            with Stage(r"copy", r"Abbey Road Saturator Presets v1.0.0.6", prog_num=6173):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Abbey Road Saturator", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6174) as should_copy_source_128_6174:  # ?
                    should_copy_source_128_6174()
                    with Stage(r"copy source", r"Common/Data/Presets/Abbey Road Saturator", prog_num=6175):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Abbey Road Saturator", r".", delete_extraneous_files=True, prog_num=6176) as copy_dir_to_dir_129_6176:  # ?
                            copy_dir_to_dir_129_6176()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Abbey Road Saturator", user_id=-1, group_id=-1, prog_num=6177, recursive=True) as chown_130_6177:  # 0m:0.000s
                            chown_130_6177()
            with Stage(r"copy", r"Berzerk Distortion Presets v1.0.0.5", prog_num=6178):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Berzerk Distortion", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6179) as should_copy_source_131_6179:  # ?
                    should_copy_source_131_6179()
                    with Stage(r"copy source", r"Common/Data/Presets/Berzerk Distortion", prog_num=6180):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Berzerk Distortion", r".", delete_extraneous_files=True, prog_num=6181) as copy_dir_to_dir_132_6181:  # ?
                            copy_dir_to_dir_132_6181()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Berzerk Distortion", user_id=-1, group_id=-1, prog_num=6182, recursive=True) as chown_133_6182:  # 0m:0.000s
                            chown_133_6182()
            with Stage(r"copy", r"CLA MixHub Presets v1.0.0.8", prog_num=6183):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/CLA MixHub", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6184) as should_copy_source_134_6184:  # ?
                    should_copy_source_134_6184()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA MixHub", prog_num=6185):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/CLA MixHub", r".", delete_extraneous_files=True, prog_num=6186) as copy_dir_to_dir_135_6186:  # ?
                            copy_dir_to_dir_135_6186()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA MixHub", user_id=-1, group_id=-1, prog_num=6187, recursive=True) as chown_136_6187:  # 0m:0.001s
                            chown_136_6187()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=6188):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6189) as should_copy_source_137_6189:  # ?
                    should_copy_source_137_6189()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=6190):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=6191) as copy_dir_to_dir_138_6191:  # ?
                            copy_dir_to_dir_138_6191()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=6192, recursive=True) as chown_139_6192:  # 0m:0.004s
                            chown_139_6192()
            with Stage(r"copy", r"MDMX Fuzz Presets v1.0.0.4", prog_num=6193):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX Fuzz", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6194) as should_copy_source_140_6194:  # ?
                    should_copy_source_140_6194()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Fuzz", prog_num=6195):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX Fuzz", r".", delete_extraneous_files=True, prog_num=6196) as copy_dir_to_dir_141_6196:  # ?
                            copy_dir_to_dir_141_6196()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Fuzz", user_id=-1, group_id=-1, prog_num=6197, recursive=True) as chown_142_6197:  # 0m:0.000s
                            chown_142_6197()
            with Stage(r"copy", r"MDMX OverDrive Presets v1.0.0.4", prog_num=6198):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX OverDrive", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6199) as should_copy_source_143_6199:  # ?
                    should_copy_source_143_6199()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX OverDrive", prog_num=6200):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX OverDrive", r".", delete_extraneous_files=True, prog_num=6201) as copy_dir_to_dir_144_6201:  # ?
                            copy_dir_to_dir_144_6201()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX OverDrive", user_id=-1, group_id=-1, prog_num=6202, recursive=True) as chown_145_6202:  # 0m:0.000s
                            chown_145_6202()
            with Stage(r"copy", r"MDMX Screamer Presets v1.0.0.4", prog_num=6203):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX Screamer", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6204) as should_copy_source_146_6204:  # ?
                    should_copy_source_146_6204()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Screamer", prog_num=6205):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MDMX Screamer", r".", delete_extraneous_files=True, prog_num=6206) as copy_dir_to_dir_147_6206:  # ?
                            copy_dir_to_dir_147_6206()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Screamer", user_id=-1, group_id=-1, prog_num=6207, recursive=True) as chown_148_6207:  # 0m:0.000s
                            chown_148_6207()
            with Stage(r"copy", r"MultiMod Distortion Rack Presets v1.0.0.11", prog_num=6208):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MultiMod Rack", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6209) as should_copy_source_149_6209:  # ?
                    should_copy_source_149_6209()
                    with Stage(r"copy source", r"Common/Data/Presets/MultiMod Rack", prog_num=6210):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MultiMod Rack", r".", delete_extraneous_files=True, prog_num=6211) as copy_dir_to_dir_150_6211:  # ?
                            copy_dir_to_dir_150_6211()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MultiMod Rack", user_id=-1, group_id=-1, prog_num=6212, recursive=True) as chown_151_6212:  # 0m:0.000s
                            chown_151_6212()
            with Stage(r"copy", r"OVox Instrument Presets v1.0.0.1", prog_num=6213):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/OVox Instrument", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6214) as should_copy_source_152_6214:  # ?
                    should_copy_source_152_6214()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Instrument", prog_num=6215):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/OVox Instrument", r".", delete_extraneous_files=True, prog_num=6216) as copy_dir_to_dir_153_6216:  # ?
                            copy_dir_to_dir_153_6216()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Instrument", user_id=-1, group_id=-1, prog_num=6217, recursive=True) as chown_154_6217:  # 0m:0.000s
                            chown_154_6217()
            with Stage(r"copy", r"OVox Vocal ReSynthesis Presets v1.1.0.2", prog_num=6218):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/OVox Vocal ReSynthesis", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6219) as should_copy_source_155_6219:  # ?
                    should_copy_source_155_6219()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Vocal ReSynthesis", prog_num=6220):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/OVox Vocal ReSynthesis", r".", delete_extraneous_files=True, prog_num=6221) as copy_dir_to_dir_156_6221:  # ?
                            copy_dir_to_dir_156_6221()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Vocal ReSynthesis", user_id=-1, group_id=-1, prog_num=6222, recursive=True) as chown_157_6222:  # 0m:0.000s
                            chown_157_6222()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=6223):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=6224) as should_copy_source_158_6224:  # ?
                    should_copy_source_158_6224()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=6225):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=6226) as copy_dir_to_dir_159_6226:  # ?
                            copy_dir_to_dir_159_6226()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=6227, recursive=True) as chown_160_6227:  # 0m:0.000s
                            chown_160_6227()
            with RmFileOrDir(r"/Applications/Waves/Data/CLA MixHub Data", prog_num=6228) as rm_file_or_dir_161_6228:  # 0m:0.000s
                rm_file_or_dir_161_6228()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=6229) as cd_stage_162_6229:  # 0m:22.220s
            cd_stage_162_6229()
            with Stage(r"copy", r"CLA MixHub v15.5.139.322", prog_num=6230):  # 0m:5.844s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA MixHub.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6231) as should_copy_source_163_6231:  # 0m:5.844s
                    should_copy_source_163_6231()
                    with Stage(r"copy source", r"Mac/Plugins/CLA MixHub.bundle", prog_num=6232):  # 0m:5.843s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA MixHub.bundle", r".", delete_extraneous_files=True, prog_num=6233) as copy_dir_to_dir_164_6233:  # 0m:0.204s
                            copy_dir_to_dir_164_6233()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA MixHub.bundle", where_to_unwtar=r".", prog_num=6234) as unwtar_165_6234:  # 0m:5.638s
                            unwtar_165_6234()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA MixHub.bundle", user_id=-1, group_id=-1, prog_num=6235, recursive=True) as chown_166_6235:  # 0m:0.000s
                            chown_166_6235()
            with Stage(r"copy", r"CR8_Sampler v15.5.139.322", prog_num=6236):  # 0m:1.787s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CR8 Sampler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6237) as should_copy_source_167_6237:  # 0m:1.787s
                    should_copy_source_167_6237()
                    with Stage(r"copy source", r"Mac/Plugins/CR8 Sampler.bundle", prog_num=6238):  # 0m:1.786s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CR8 Sampler.bundle", r".", delete_extraneous_files=True, prog_num=6239) as copy_dir_to_dir_168_6239:  # 0m:0.087s
                            copy_dir_to_dir_168_6239()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CR8 Sampler.bundle", where_to_unwtar=r".", prog_num=6240) as unwtar_169_6240:  # 0m:1.698s
                            unwtar_169_6240()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CR8 Sampler.bundle", user_id=-1, group_id=-1, prog_num=6241, recursive=True) as chown_170_6241:  # 0m:0.000s
                            chown_170_6241()
            with Stage(r"copy", r"EMO-D5 v15.5.139.322", prog_num=6242):  # 0m:0.300s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-D5.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6243) as should_copy_source_171_6243:  # 0m:0.300s
                    should_copy_source_171_6243()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-D5.bundle", prog_num=6244):  # 0m:0.299s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-D5.bundle", r".", delete_extraneous_files=True, prog_num=6245) as copy_dir_to_dir_172_6245:  # 0m:0.037s
                            copy_dir_to_dir_172_6245()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-D5.bundle", where_to_unwtar=r".", prog_num=6246) as unwtar_173_6246:  # 0m:0.261s
                            unwtar_173_6246()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-D5.bundle", user_id=-1, group_id=-1, prog_num=6247, recursive=True) as chown_174_6247:  # 0m:0.000s
                            chown_174_6247()
            with Stage(r"copy", r"LFE360 v15.5.139.322", prog_num=6248):  # 0m:0.123s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LFE360.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6249) as should_copy_source_175_6249:  # 0m:0.123s
                    should_copy_source_175_6249()
                    with Stage(r"copy source", r"Mac/Plugins/LFE360.bundle", prog_num=6250):  # 0m:0.123s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LFE360.bundle", r".", delete_extraneous_files=True, prog_num=6251) as copy_dir_to_dir_176_6251:  # 0m:0.037s
                            copy_dir_to_dir_176_6251()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LFE360.bundle", where_to_unwtar=r".", prog_num=6252) as unwtar_177_6252:  # 0m:0.085s
                            unwtar_177_6252()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LFE360.bundle", user_id=-1, group_id=-1, prog_num=6253, recursive=True) as chown_178_6253:  # 0m:0.000s
                            chown_178_6253()
            with Stage(r"copy", r"MannyM-Delay v15.5.139.322", prog_num=6254):  # 0m:1.364s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-Delay.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6255) as should_copy_source_179_6255:  # 0m:1.364s
                    should_copy_source_179_6255()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Delay.bundle", prog_num=6256):  # 0m:1.363s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-Delay.bundle", r".", delete_extraneous_files=True, prog_num=6257) as copy_dir_to_dir_180_6257:  # 0m:0.406s
                            copy_dir_to_dir_180_6257()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-Delay.bundle", where_to_unwtar=r".", prog_num=6258) as unwtar_181_6258:  # 0m:0.957s
                            unwtar_181_6258()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MannyM-Delay.bundle", user_id=-1, group_id=-1, prog_num=6259, recursive=True) as chown_182_6259:  # 0m:0.000s
                            chown_182_6259()
            with Stage(r"copy", r"MultiMod Rack v15.5.139.322", prog_num=6260):  # 0m:2.721s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MultiMod Rack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6261) as should_copy_source_183_6261:  # 0m:2.721s
                    should_copy_source_183_6261()
                    with Stage(r"copy source", r"Mac/Plugins/MultiMod Rack.bundle", prog_num=6262):  # 0m:2.720s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MultiMod Rack.bundle", r".", delete_extraneous_files=True, prog_num=6263) as copy_dir_to_dir_184_6263:  # 0m:0.311s
                            copy_dir_to_dir_184_6263()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MultiMod Rack.bundle", where_to_unwtar=r".", prog_num=6264) as unwtar_185_6264:  # 0m:2.409s
                            unwtar_185_6264()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MultiMod Rack.bundle", user_id=-1, group_id=-1, prog_num=6265, recursive=True) as chown_186_6265:  # 0m:0.000s
                            chown_186_6265()
            with Stage(r"copy", r"StudioVerse Instruments v15.5.139.322", prog_num=6266):  # 0m:3.540s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Instruments.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6267) as should_copy_source_187_6267:  # 0m:3.540s
                    should_copy_source_187_6267()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Instruments.bundle", prog_num=6268):  # 0m:3.539s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Instruments.bundle", r".", delete_extraneous_files=True, prog_num=6269) as copy_dir_to_dir_188_6269:  # 0m:0.197s
                            copy_dir_to_dir_188_6269()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Instruments.bundle", where_to_unwtar=r".", prog_num=6270) as unwtar_189_6270:  # 0m:3.341s
                            unwtar_189_6270()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/StudioVerse Instruments.bundle", user_id=-1, group_id=-1, prog_num=6271, recursive=True) as chown_190_6271:  # 0m:0.000s
                            chown_190_6271()
            with Stage(r"copy", r"OVox v15.5.139.322", prog_num=6272):  # 0m:0.698s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OVox.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6273) as should_copy_source_191_6273:  # 0m:0.697s
                    should_copy_source_191_6273()
                    with Stage(r"copy source", r"Mac/Plugins/OVox.bundle", prog_num=6274):  # 0m:0.697s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OVox.bundle", r".", delete_extraneous_files=True, prog_num=6275) as copy_dir_to_dir_192_6275:  # 0m:0.032s
                            copy_dir_to_dir_192_6275()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OVox.bundle", where_to_unwtar=r".", prog_num=6276) as unwtar_193_6276:  # 0m:0.664s
                            unwtar_193_6276()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OVox.bundle", user_id=-1, group_id=-1, prog_num=6277, recursive=True) as chown_194_6277:  # 0m:0.000s
                            chown_194_6277()
            with Stage(r"copy", r"S360 v15.5.139.322", prog_num=6278):  # 0m:0.175s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S360.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6279) as should_copy_source_195_6279:  # 0m:0.175s
                    should_copy_source_195_6279()
                    with Stage(r"copy source", r"Mac/Plugins/S360.bundle", prog_num=6280):  # 0m:0.175s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S360.bundle", r".", delete_extraneous_files=True, prog_num=6281) as copy_dir_to_dir_196_6281:  # 0m:0.038s
                            copy_dir_to_dir_196_6281()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S360.bundle", where_to_unwtar=r".", prog_num=6282) as unwtar_197_6282:  # 0m:0.136s
                            unwtar_197_6282()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/S360.bundle", user_id=-1, group_id=-1, prog_num=6283, recursive=True) as chown_198_6283:  # 0m:0.000s
                            chown_198_6283()
            with Stage(r"copy", r"StudioVerse Audio Effects v15.5.139.322", prog_num=6284):  # 0m:2.378s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Audio Effects.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6285) as should_copy_source_199_6285:  # 0m:2.378s
                    should_copy_source_199_6285()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Audio Effects.bundle", prog_num=6286):  # 0m:2.377s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Audio Effects.bundle", r".", delete_extraneous_files=True, prog_num=6287) as copy_dir_to_dir_200_6287:  # 0m:0.146s
                            copy_dir_to_dir_200_6287()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/StudioVerse Audio Effects.bundle", where_to_unwtar=r".", prog_num=6288) as unwtar_201_6288:  # 0m:2.231s
                            unwtar_201_6288()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/StudioVerse Audio Effects.bundle", user_id=-1, group_id=-1, prog_num=6289, recursive=True) as chown_202_6289:  # 0m:0.000s
                            chown_202_6289()
            with Stage(r"copy", r"TRACT v15.5.139.322", prog_num=6290):  # 0m:0.395s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TRACT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6291) as should_copy_source_203_6291:  # 0m:0.395s
                    should_copy_source_203_6291()
                    with Stage(r"copy source", r"Mac/Plugins/TRACT.bundle", prog_num=6292):  # 0m:0.395s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TRACT.bundle", r".", delete_extraneous_files=True, prog_num=6293) as copy_dir_to_dir_204_6293:  # 0m:0.033s
                            copy_dir_to_dir_204_6293()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TRACT.bundle", where_to_unwtar=r".", prog_num=6294) as unwtar_205_6294:  # 0m:0.361s
                            unwtar_205_6294()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TRACT.bundle", user_id=-1, group_id=-1, prog_num=6295, recursive=True) as chown_206_6295:  # 0m:0.000s
                            chown_206_6295()
            with Stage(r"copy", r"WavesLib1_15_5_139_322 v15.5.139.322", prog_num=6296):  # 0m:0.568s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6297) as should_copy_source_207_6297:  # 0m:0.568s
                    should_copy_source_207_6297()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.139.framework", prog_num=6298):  # 0m:0.567s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r".", delete_extraneous_files=True, prog_num=6299) as copy_dir_to_dir_208_6299:  # 0m:0.002s
                            copy_dir_to_dir_208_6299()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", where_to_unwtar=r".", prog_num=6300) as unwtar_209_6300:  # 0m:0.565s
                            unwtar_209_6300()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.139.framework", user_id=-1, group_id=-1, prog_num=6301, recursive=True) as chown_210_6301:  # 0m:0.000s
                            chown_210_6301()
            with Stage(r"copy", r"Waves Harmony v15.5.139.322", prog_num=6302):  # 0m:0.592s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=6303) as should_copy_source_211_6303:  # 0m:0.592s
                    should_copy_source_211_6303()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=6304):  # 0m:0.591s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=6305) as copy_dir_to_dir_212_6305:  # 0m:0.034s
                            copy_dir_to_dir_212_6305()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=6306) as unwtar_213_6306:  # 0m:0.557s
                            unwtar_213_6306()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=6307, recursive=True) as chown_214_6307:  # 0m:0.000s
                            chown_214_6307()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=2, prog_num=6309) as resolve_symlink_files_in_folder_215_6309:  # 0m:1.015s
                resolve_symlink_files_in_folder_215_6309()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=6310) as shell_command_216_6310:  # 0m:0.108s
                shell_command_216_6310()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=6311) as script_command_217_6311:  # 0m:0.009s
                script_command_217_6311()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6312) as shell_command_218_6312:  # 0m:0.427s
                shell_command_218_6312()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=6313) as create_symlink_219_6313:  # 0m:0.001s
                create_symlink_219_6313()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=6314) as create_symlink_220_6314:  # 0m:0.000s
                create_symlink_220_6314()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=6315) as copy_glob_to_dir_221_6315:  # 0m:0.174s
                copy_glob_to_dir_221_6315()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=6316) as cd_stage_222_6316:  # 0m:0.001s
            cd_stage_222_6316()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=6317):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=6318) as should_copy_source_223_6318:  # ?
                    should_copy_source_223_6318()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=6319):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=6320) as copy_file_to_dir_224_6320:  # ?
                            copy_file_to_dir_224_6320()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=6321) as chmod_and_chown_225_6321:  # 0m:0.000s
                            chmod_and_chown_225_6321()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/MIDI", prog_num=6322) as cd_stage_226_6322:  # 0m:0.899s
            cd_stage_226_6322()
            with Stage(r"copy", r"MidiArpSeq v15.5.139.322", prog_num=6323):  # 0m:0.117s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6324) as should_copy_source_227_6324:  # 0m:0.116s
                    should_copy_source_227_6324()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIArpSeq.bundle", prog_num=6325):  # 0m:0.116s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r".", delete_extraneous_files=True, prog_num=6326) as copy_dir_to_dir_228_6326:  # 0m:0.038s
                            copy_dir_to_dir_228_6326()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIArpSeq.bundle", where_to_unwtar=r".", prog_num=6327) as unwtar_229_6327:  # 0m:0.077s
                            unwtar_229_6327()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIArpSeq.bundle", user_id=-1, group_id=-1, prog_num=6328, recursive=True) as chown_230_6328:  # 0m:0.000s
                            chown_230_6328()
            with Stage(r"copy", r"MIDIChords v15.5.139.322", prog_num=6329):  # 0m:0.144s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIChords.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6330) as should_copy_source_231_6330:  # 0m:0.144s
                    should_copy_source_231_6330()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIChords.bundle", prog_num=6331):  # 0m:0.143s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIChords.bundle", r".", delete_extraneous_files=True, prog_num=6332) as copy_dir_to_dir_232_6332:  # 0m:0.033s
                            copy_dir_to_dir_232_6332()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIChords.bundle", where_to_unwtar=r".", prog_num=6333) as unwtar_233_6333:  # 0m:0.110s
                            unwtar_233_6333()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIChords.bundle", user_id=-1, group_id=-1, prog_num=6334, recursive=True) as chown_234_6334:  # 0m:0.000s
                            chown_234_6334()
            with Stage(r"copy", r"MIDIKeyboard v15.5.139.322", prog_num=6335):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6336) as should_copy_source_235_6336:  # 0m:0.109s
                    should_copy_source_235_6336()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIKeyboard.bundle", prog_num=6337):  # 0m:0.109s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r".", delete_extraneous_files=True, prog_num=6338) as copy_dir_to_dir_236_6338:  # 0m:0.033s
                            copy_dir_to_dir_236_6338()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIKeyboard.bundle", where_to_unwtar=r".", prog_num=6339) as unwtar_237_6339:  # 0m:0.075s
                            unwtar_237_6339()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIKeyboard.bundle", user_id=-1, group_id=-1, prog_num=6340, recursive=True) as chown_238_6340:  # 0m:0.000s
                            chown_238_6340()
            with Stage(r"copy", r"MIDIMonitor v15.5.139.322", prog_num=6341):  # 0m:0.115s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIMonitor.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6342) as should_copy_source_239_6342:  # 0m:0.115s
                    should_copy_source_239_6342()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIMonitor.bundle", prog_num=6343):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIMonitor.bundle", r".", delete_extraneous_files=True, prog_num=6344) as copy_dir_to_dir_240_6344:  # 0m:0.033s
                            copy_dir_to_dir_240_6344()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIMonitor.bundle", where_to_unwtar=r".", prog_num=6345) as unwtar_241_6345:  # 0m:0.081s
                            unwtar_241_6345()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIMonitor.bundle", user_id=-1, group_id=-1, prog_num=6346, recursive=True) as chown_242_6346:  # 0m:0.000s
                            chown_242_6346()
            with Stage(r"copy", r"MIDIRange v15.5.139.322", prog_num=6347):  # 0m:0.108s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIRange.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6348) as should_copy_source_243_6348:  # 0m:0.108s
                    should_copy_source_243_6348()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIRange.bundle", prog_num=6349):  # 0m:0.107s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIRange.bundle", r".", delete_extraneous_files=True, prog_num=6350) as copy_dir_to_dir_244_6350:  # 0m:0.034s
                            copy_dir_to_dir_244_6350()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIRange.bundle", where_to_unwtar=r".", prog_num=6351) as unwtar_245_6351:  # 0m:0.073s
                            unwtar_245_6351()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIRange.bundle", user_id=-1, group_id=-1, prog_num=6352, recursive=True) as chown_246_6352:  # 0m:0.000s
                            chown_246_6352()
            with Stage(r"copy", r"MIDITranspose v15.5.139.322", prog_num=6353):  # 0m:0.104s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDITranspose.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6354) as should_copy_source_247_6354:  # 0m:0.104s
                    should_copy_source_247_6354()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDITranspose.bundle", prog_num=6355):  # 0m:0.103s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDITranspose.bundle", r".", delete_extraneous_files=True, prog_num=6356) as copy_dir_to_dir_248_6356:  # 0m:0.032s
                            copy_dir_to_dir_248_6356()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDITranspose.bundle", where_to_unwtar=r".", prog_num=6357) as unwtar_249_6357:  # 0m:0.071s
                            unwtar_249_6357()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDITranspose.bundle", user_id=-1, group_id=-1, prog_num=6358, recursive=True) as chown_250_6358:  # 0m:0.000s
                            chown_250_6358()
            with Stage(r"copy", r"MIDIVelocity v15.5.139.322", prog_num=6359):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVelocity.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6360) as should_copy_source_251_6360:  # 0m:0.101s
                    should_copy_source_251_6360()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVelocity.bundle", prog_num=6361):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVelocity.bundle", r".", delete_extraneous_files=True, prog_num=6362) as copy_dir_to_dir_252_6362:  # 0m:0.027s
                            copy_dir_to_dir_252_6362()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVelocity.bundle", where_to_unwtar=r".", prog_num=6363) as unwtar_253_6363:  # 0m:0.072s
                            unwtar_253_6363()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIVelocity.bundle", user_id=-1, group_id=-1, prog_num=6364, recursive=True) as chown_254_6364:  # 0m:0.000s
                            chown_254_6364()
            with Stage(r"copy", r"MIDIVoicing v15.5.139.322", prog_num=6365):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVoicing.bundle", r"/Applications/Waves/Plug-Ins V15/MIDI", skip_progress_count=4, prog_num=6366) as should_copy_source_255_6366:  # 0m:0.101s
                    should_copy_source_255_6366()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVoicing.bundle", prog_num=6367):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVoicing.bundle", r".", delete_extraneous_files=True, prog_num=6368) as copy_dir_to_dir_256_6368:  # 0m:0.032s
                            copy_dir_to_dir_256_6368()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MIDI/MIDIVoicing.bundle", where_to_unwtar=r".", prog_num=6369) as unwtar_257_6369:  # 0m:0.067s
                            unwtar_257_6369()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MIDI/MIDIVoicing.bundle", user_id=-1, group_id=-1, prog_num=6370, recursive=True) as chown_258_6370:  # 0m:0.000s
                            chown_258_6370()
        with Stage(r"remove_previous_sources_instructions_for_target_folder", r"/Applications/Waves/Plug-Ins V15/ModFX", prog_num=6371):  # 0m:0.001s
            with Cd(r"/Applications/Waves/Plug-Ins V15/ModFX", prog_num=6372) as cd_259_6372:  # 0m:0.001s
                cd_259_6372()
                Progress(r"remove previous versions /Applications/Waves/Plug-Ins V15/ModFX", prog_num=6373)()  # 0m:0.000s
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Autopan.bundle", prog_num=6374) as rm_dir_260_6374:  # 0m:0.000s
                    rm_dir_260_6374()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Chorus.bundle", prog_num=6375) as rm_dir_261_6375:  # 0m:0.000s
                    rm_dir_261_6375()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Compressor.bundle", prog_num=6376) as rm_dir_262_6376:  # 0m:0.000s
                    rm_dir_262_6376()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Delay.bundle", prog_num=6377) as rm_dir_263_6377:  # 0m:0.000s
                    rm_dir_263_6377()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Distortion.bundle", prog_num=6378) as rm_dir_264_6378:  # 0m:0.000s
                    rm_dir_264_6378()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Limiter.bundle", prog_num=6379) as rm_dir_265_6379:  # 0m:0.000s
                    rm_dir_265_6379()
                with RmDir(r"/Applications/Waves/Plug-Ins V15/ModFX/Reverb.bundle", prog_num=6380) as rm_dir_266_6380:  # 0m:0.000s
                    rm_dir_266_6380()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/ModFX", prog_num=6381) as cd_stage_267_6381:  # 0m:0.917s
            cd_stage_267_6381()
            with Stage(r"copy", r"ModFX Autopan v15.5.139.322", prog_num=6382):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6383) as should_copy_source_268_6383:  # 0m:0.110s
                    should_copy_source_268_6383()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Autopan.bundle", prog_num=6384):  # 0m:0.109s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r".", delete_extraneous_files=True, prog_num=6385) as copy_dir_to_dir_269_6385:  # 0m:0.032s
                            copy_dir_to_dir_269_6385()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Autopan.bundle", where_to_unwtar=r".", prog_num=6386) as unwtar_270_6386:  # 0m:0.077s
                            unwtar_270_6386()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Autopan.bundle", user_id=-1, group_id=-1, prog_num=6387, recursive=True) as chown_271_6387:  # 0m:0.000s
                            chown_271_6387()
            with Stage(r"copy", r"ModFX Chorus v15.5.139.322", prog_num=6388):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6389) as should_copy_source_272_6389:  # 0m:0.111s
                    should_copy_source_272_6389()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Chorus.bundle", prog_num=6390):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r".", delete_extraneous_files=True, prog_num=6391) as copy_dir_to_dir_273_6391:  # 0m:0.035s
                            copy_dir_to_dir_273_6391()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Chorus.bundle", where_to_unwtar=r".", prog_num=6392) as unwtar_274_6392:  # 0m:0.075s
                            unwtar_274_6392()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Chorus.bundle", user_id=-1, group_id=-1, prog_num=6393, recursive=True) as chown_275_6393:  # 0m:0.000s
                            chown_275_6393()
            with Stage(r"copy", r"ModFX Compressor v15.5.139.322", prog_num=6394):  # 0m:0.109s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6395) as should_copy_source_276_6395:  # 0m:0.109s
                    should_copy_source_276_6395()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Compressor.bundle", prog_num=6396):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r".", delete_extraneous_files=True, prog_num=6397) as copy_dir_to_dir_277_6397:  # 0m:0.031s
                            copy_dir_to_dir_277_6397()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Compressor.bundle", where_to_unwtar=r".", prog_num=6398) as unwtar_278_6398:  # 0m:0.076s
                            unwtar_278_6398()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Compressor.bundle", user_id=-1, group_id=-1, prog_num=6399, recursive=True) as chown_279_6399:  # 0m:0.000s
                            chown_279_6399()
            with Stage(r"copy", r"ModFX Delay v15.5.139.322", prog_num=6400):  # 0m:0.107s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Delay.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6401) as should_copy_source_280_6401:  # 0m:0.107s
                    should_copy_source_280_6401()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Delay.bundle", prog_num=6402):  # 0m:0.106s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Delay.bundle", r".", delete_extraneous_files=True, prog_num=6403) as copy_dir_to_dir_281_6403:  # 0m:0.030s
                            copy_dir_to_dir_281_6403()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Delay.bundle", where_to_unwtar=r".", prog_num=6404) as unwtar_282_6404:  # 0m:0.076s
                            unwtar_282_6404()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Delay.bundle", user_id=-1, group_id=-1, prog_num=6405, recursive=True) as chown_283_6405:  # 0m:0.000s
                            chown_283_6405()
            with Stage(r"copy", r"ModFX Distortion v15.5.139.322", prog_num=6406):  # 0m:0.154s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6407) as should_copy_source_284_6407:  # 0m:0.154s
                    should_copy_source_284_6407()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Distortion.bundle", prog_num=6408):  # 0m:0.154s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r".", delete_extraneous_files=True, prog_num=6409) as copy_dir_to_dir_285_6409:  # 0m:0.035s
                            copy_dir_to_dir_285_6409()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Distortion.bundle", where_to_unwtar=r".", prog_num=6410) as unwtar_286_6410:  # 0m:0.118s
                            unwtar_286_6410()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Distortion.bundle", user_id=-1, group_id=-1, prog_num=6411, recursive=True) as chown_287_6411:  # 0m:0.000s
                            chown_287_6411()
            with Stage(r"copy", r"ModFX Limiter v15.5.139.322", prog_num=6412):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6413) as should_copy_source_288_6413:  # 0m:0.101s
                    should_copy_source_288_6413()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Limiter.bundle", prog_num=6414):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r".", delete_extraneous_files=True, prog_num=6415) as copy_dir_to_dir_289_6415:  # 0m:0.033s
                            copy_dir_to_dir_289_6415()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Limiter.bundle", where_to_unwtar=r".", prog_num=6416) as unwtar_290_6416:  # 0m:0.066s
                            unwtar_290_6416()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Limiter.bundle", user_id=-1, group_id=-1, prog_num=6417, recursive=True) as chown_291_6417:  # 0m:0.000s
                            chown_291_6417()
            with Stage(r"copy", r"ModFX Reverb v15.5.139.322", prog_num=6418):  # 0m:0.223s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r"/Applications/Waves/Plug-Ins V15/ModFX", skip_progress_count=4, prog_num=6419) as should_copy_source_292_6419:  # 0m:0.223s
                    should_copy_source_292_6419()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Reverb.bundle", prog_num=6420):  # 0m:0.222s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r".", delete_extraneous_files=True, prog_num=6421) as copy_dir_to_dir_293_6421:  # 0m:0.038s
                            copy_dir_to_dir_293_6421()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ModFX/ModFX_Reverb.bundle", where_to_unwtar=r".", prog_num=6422) as unwtar_294_6422:  # 0m:0.184s
                            unwtar_294_6422()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ModFX/ModFX_Reverb.bundle", user_id=-1, group_id=-1, prog_num=6423, recursive=True) as chown_295_6423:  # 0m:0.000s
                            chown_295_6423()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=6424) as cd_stage_296_6424:  # 0m:1.208s
            cd_stage_296_6424()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=6425):  # 0m:1.190s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=6426) as should_copy_source_297_6426:  # 0m:1.190s
                    should_copy_source_297_6426()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=6427):  # 0m:1.190s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=6428) as copy_dir_to_dir_298_6428:  # 0m:0.050s
                            copy_dir_to_dir_298_6428()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=6429) as unwtar_299_6429:  # 0m:1.090s
                            unwtar_299_6429()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=6430, recursive=True) as chown_300_6430:  # 0m:0.000s
                            chown_300_6430()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=6431) as shell_command_301_6431:  # 0m:0.049s
                            shell_command_301_6431()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=6432):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=6433) as should_copy_source_302_6433:  # ?
                    should_copy_source_302_6433()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=6434):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=6435) as copy_dir_to_dir_303_6435:  # ?
                            copy_dir_to_dir_303_6435()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=6436) as unwtar_304_6436:  # ?
                            unwtar_304_6436()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=6437, recursive=True) as chown_305_6437:  # ?
                            chown_305_6437()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=6438) as break_hard_link_306_6438:  # ?
                            break_hard_link_306_6438()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=6439) as shell_command_307_6439:  # ?
                            shell_command_307_6439()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=6440, recursive=True) as chown_308_6440:  # ?
                            chown_308_6440()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=6441, recursive=True) as chmod_309_6441:  # 0m:0.004s
                            chmod_309_6441()
            with Stage(r"copy", r"WaveShell1-OBS 15.5 v15.5.79.262", prog_num=6442):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=6443) as should_copy_source_310_6443:  # ?
                    should_copy_source_310_6443()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=6444):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=6445) as copy_dir_to_dir_311_6445:  # ?
                            copy_dir_to_dir_311_6445()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=6446) as unwtar_312_6446:  # ?
                            unwtar_312_6446()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=6447, recursive=True) as chown_313_6447:  # ?
                            chown_313_6447()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=6448) as shell_command_314_6448:  # 0m:0.001s
                            shell_command_314_6448()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=6449):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=6450) as should_copy_source_315_6450:  # ?
                    should_copy_source_315_6450()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=6451):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=6452) as copy_dir_to_dir_316_6452:  # ?
                            copy_dir_to_dir_316_6452()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=6453) as unwtar_317_6453:  # ?
                            unwtar_317_6453()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=6454, recursive=True) as chown_318_6454:  # ?
                            chown_318_6454()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=6455) as shell_command_319_6455:  # 0m:0.001s
                            shell_command_319_6455()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=6456):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=6457) as should_copy_source_320_6457:  # ?
                    should_copy_source_320_6457()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=6458):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=6459) as copy_dir_to_dir_321_6459:  # ?
                            copy_dir_to_dir_321_6459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=6460) as unwtar_322_6460:  # ?
                            unwtar_322_6460()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=6461, recursive=True) as chown_323_6461:  # ?
                            chown_323_6461()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6462) as shell_command_324_6462:  # ?
                            shell_command_324_6462()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6463) as script_command_325_6463:  # ?
                            script_command_325_6463()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6464) as shell_command_326_6464:  # 0m:0.001s
                            shell_command_326_6464()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=6465):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=6466) as should_copy_source_327_6466:  # ?
                    should_copy_source_327_6466()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=6467):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=6468) as copy_dir_to_dir_328_6468:  # ?
                            copy_dir_to_dir_328_6468()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=6469) as unwtar_329_6469:  # ?
                            unwtar_329_6469()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=6470, recursive=True) as chown_330_6470:  # 0m:0.001s
                            chown_330_6470()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=6471) as shell_command_331_6471:  # 0m:0.009s
                shell_command_331_6471()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=6472) as cd_stage_332_6472:  # 0m:1.200s
            cd_stage_332_6472()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=6473):  # 0m:1.199s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=6474) as should_copy_source_333_6474:  # 0m:1.199s
                    should_copy_source_333_6474()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=6475):  # 0m:1.198s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=6476) as copy_dir_to_dir_334_6476:  # 0m:0.054s
                            copy_dir_to_dir_334_6476()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=6477) as unwtar_335_6477:  # 0m:1.092s
                            unwtar_335_6477()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=6478, recursive=True) as chown_336_6478:  # 0m:0.000s
                            chown_336_6478()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=6479) as shell_command_337_6479:  # 0m:0.052s
                            shell_command_337_6479()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=6480) as cd_stage_338_6480:  # 0m:0.004s
            cd_stage_338_6480()
            with Stage(r"copy", r"EMO-D5 XML and Registry for Native Instruments", prog_num=6481):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=6482) as should_copy_source_339_6482:  # ?
                    should_copy_source_339_6482()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", prog_num=6483):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r".", prog_num=6484) as copy_file_to_dir_340_6484:  # ?
                            copy_file_to_dir_340_6484()
                        with ChmodAndChown(path=r"Waves-EMO-D5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=6485) as chmod_and_chown_341_6485:  # 0m:0.001s
                            chmod_and_chown_341_6485()
            with Stage(r"copy", r"MannyM-Delay XML and Registry for Native Instruments", prog_num=6486):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=6487) as should_copy_source_342_6487:  # ?
                    should_copy_source_342_6487()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", prog_num=6488):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r".", prog_num=6489) as copy_file_to_dir_343_6489:  # ?
                            copy_file_to_dir_343_6489()
                        with ChmodAndChown(path=r"Waves-MannyM-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=6490) as chmod_and_chown_344_6490:  # 0m:0.000s
                            chmod_and_chown_344_6490()
            with Stage(r"copy", r"OVox XML and Registry for Native Instruments", prog_num=6491):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=6492) as should_copy_source_345_6492:  # ?
                    should_copy_source_345_6492()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", prog_num=6493):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r".", prog_num=6494) as copy_file_to_dir_346_6494:  # ?
                            copy_file_to_dir_346_6494()
                        with ChmodAndChown(path=r"Waves-OVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=6495) as chmod_and_chown_347_6495:  # 0m:0.000s
                            chmod_and_chown_347_6495()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-D5", "NKS_DATA_VERSION": "1.0"}, prog_num=6496) as resolve_config_vars_in_file_348_6496:  # 0m:0.001s
                resolve_config_vars_in_file_348_6496()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True), prog_num=6497) as if_349_6497:  # 0m:0.001s
                if_349_6497()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=6498) as resolve_config_vars_in_file_350_6498:  # 0m:0.000s
                resolve_config_vars_in_file_350_6498()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True), prog_num=6499) as if_351_6499:  # 0m:0.000s
                if_351_6499()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OVox", "NKS_DATA_VERSION": "1.0"}, prog_num=6500) as resolve_config_vars_in_file_352_6500:  # 0m:0.000s
                resolve_config_vars_in_file_352_6500()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True), prog_num=6501) as if_353_6501:  # 0m:0.000s
                if_353_6501()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=6502) as cd_stage_354_6502:  # 0m:0.001s
            cd_stage_354_6502()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=6503):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=6504) as should_copy_source_355_6504:  # ?
                    should_copy_source_355_6504()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=6505):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=6506) as copy_dir_to_dir_356_6506:  # ?
                            copy_dir_to_dir_356_6506()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=6507, recursive=True) as chown_357_6507:  # 0m:0.000s
                            chown_357_6507()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=6508):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=6509) as should_copy_source_358_6509:  # ?
                    should_copy_source_358_6509()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=6510):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=6511) as copy_dir_to_dir_359_6511:  # ?
                            copy_dir_to_dir_359_6511()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=6512) as unwtar_360_6512:  # ?
                            unwtar_360_6512()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=6513, recursive=True) as chown_361_6513:  # 0m:0.000s
                            chown_361_6513()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=6514) as cd_stage_362_6514:  # 0m:0.000s
            cd_stage_362_6514()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=6515):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=6516) as should_copy_source_363_6516:  # ?
                    should_copy_source_363_6516()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=6517):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=6518) as copy_dir_to_dir_364_6518:  # ?
                            copy_dir_to_dir_364_6518()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=6519) as unwtar_365_6519:  # ?
                            unwtar_365_6519()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=6520, recursive=True) as chown_366_6520:  # 0m:0.000s
                            chown_366_6520()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=6521) as cd_stage_367_6521:  # 0m:0.005s
            cd_stage_367_6521()
            with Stage(r"copy", r"Demo Mode V15 1.1 v1.1", prog_num=6522):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=6523) as should_copy_source_368_6523:  # ?
                    should_copy_source_368_6523()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=6524):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=6525) as copy_dir_to_dir_369_6525:  # ?
                            copy_dir_to_dir_369_6525()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=6526, recursive=True) as chown_370_6526:  # 0m:0.001s
                            chown_370_6526()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=6527) as cd_stage_371_6527:  # 0m:0.000s
            cd_stage_371_6527()
            with Stage(r"copy", r"License Notifications V15 1.1 v1.1", prog_num=6528):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=6529) as should_copy_source_372_6529:  # ?
                    should_copy_source_372_6529()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=6530):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=6531) as copy_dir_to_dir_373_6531:  # ?
                            copy_dir_to_dir_373_6531()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=6532, recursive=True) as chown_374_6532:  # 0m:0.000s
                            chown_374_6532()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=6533) as cd_stage_375_6533:  # 0m:5.168s
            cd_stage_375_6533()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=6534) as rm_file_or_dir_376_6534:  # 0m:0.000s
                rm_file_or_dir_376_6534()
            with Stage(r"copy", r"ffmpeg v6.1.1", prog_num=6535):  # 0m:0.052s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/ffmpeg", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=6536) as should_copy_source_377_6536:  # 0m:0.052s
                    should_copy_source_377_6536()
                    with Stage(r"copy source", r"Mac/Modules/ffmpeg", prog_num=6537):  # 0m:0.052s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/ffmpeg.wtar.aa", where_to_unwtar=r".", prog_num=6538) as unwtar_378_6538:  # 0m:0.052s
                            unwtar_378_6538()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=6539):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=6540) as should_copy_source_379_6540:  # ?
                    should_copy_source_379_6540()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=6541):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6542) as copy_dir_to_dir_380_6542:  # ?
                            copy_dir_to_dir_380_6542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=6543) as unwtar_381_6543:  # ?
                            unwtar_381_6543()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=6544, recursive=True) as chown_382_6544:  # 0m:0.005s
                            chown_382_6544()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=6545):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=6546) as should_copy_source_383_6546:  # 0m:0.004s
                    should_copy_source_383_6546()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=6547):  # 0m:0.004s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=6548) as unwtar_384_6548:  # 0m:0.004s
                            unwtar_384_6548()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=6549):  # 0m:5.034s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=6550) as should_copy_source_385_6550:  # 0m:5.034s
                    should_copy_source_385_6550()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=6551):  # 0m:5.033s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=6552) as copy_dir_to_dir_386_6552:  # 0m:0.015s
                            copy_dir_to_dir_386_6552()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=6553) as unwtar_387_6553:  # 0m:5.017s
                            unwtar_387_6553()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=6554, recursive=True) as chown_388_6554:  # 0m:0.001s
                            chown_388_6554()
            with Stage(r"copy", r"WavesLicenseEngine v2.6.0.3", prog_num=6555):  # 0m:0.056s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=6556) as should_copy_source_389_6556:  # 0m:0.055s
                    should_copy_source_389_6556()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=6557):  # 0m:0.055s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6558) as copy_dir_to_dir_390_6558:  # 0m:0.054s
                            copy_dir_to_dir_390_6558()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=6559) as chmod_391_6559:  # 0m:0.000s
                            chmod_391_6559()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=6560) as chmod_392_6560:  # 0m:0.000s
                            chmod_392_6560()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=6561, recursive=True) as chown_393_6561:  # 0m:0.000s
                            chown_393_6561()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=6564) as resolve_symlink_files_in_folder_394_6564:  # 0m:0.006s
                resolve_symlink_files_in_folder_394_6564()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6565) as shell_command_395_6565:  # 0m:0.011s
                shell_command_395_6565()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=6566) as cd_stage_396_6566:  # 0m:0.002s
            cd_stage_396_6566()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=6567):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=6568) as should_copy_source_397_6568:  # ?
                    should_copy_source_397_6568()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=6569):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=6570) as copy_dir_to_dir_398_6570:  # ?
                            copy_dir_to_dir_398_6570()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=6571, recursive=True) as chown_399_6571:  # 0m:0.001s
                            chown_399_6571()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=6572) as cd_stage_400_6572:  # 0m:2.124s
            cd_stage_400_6572()
            with Stage(r"copy", r"Waves Local Server v12.15.351.247", prog_num=6573):  # 0m:2.124s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=6574) as should_copy_source_401_6574:  # 0m:2.124s
                    should_copy_source_401_6574()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=6575):  # 0m:2.124s
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=6576, recursive=True) as chmod_402_6576:  # 0m:0.007s
                            chmod_402_6576()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6577) as copy_dir_to_dir_403_6577:  # 0m:0.044s
                            copy_dir_to_dir_403_6577()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=6578) as unwtar_404_6578:  # 0m:2.071s
                            unwtar_404_6578()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=6579, recursive=True) as chown_405_6579:  # 0m:0.000s
                            chown_405_6579()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=6580) as if_406_6580:  # 0m:0.001s
                            if_406_6580()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=6581) as cd_stage_407_6581:  # 0m:0.001s
            cd_stage_407_6581()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.77.78", prog_num=6582):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=6583) as should_copy_source_408_6583:  # ?
                    should_copy_source_408_6583()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=6584):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=6585) as copy_dir_to_dir_409_6585:  # ?
                            copy_dir_to_dir_409_6585()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=6586) as unwtar_410_6586:  # ?
                            unwtar_410_6586()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=6587, recursive=True) as chown_411_6587:  # ?
                            chown_411_6587()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=6588) as if_412_6588:  # 0m:0.000s
                            if_412_6588()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=6589) as cd_stage_413_6589:  # 0m:1.151s
            cd_stage_413_6589()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=6590):  # 0m:1.150s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=6591) as should_copy_source_414_6591:  # 0m:1.150s
                    should_copy_source_414_6591()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=6592):  # 0m:1.146s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=6593) as copy_dir_to_dir_415_6593:  # 0m:0.093s
                            copy_dir_to_dir_415_6593()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=6594) as unwtar_416_6594:  # 0m:0.978s
                            unwtar_416_6594()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=6595, recursive=True) as chown_417_6595:  # 0m:0.000s
                            chown_417_6595()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=6596) as break_hard_link_418_6596:  # 0m:0.016s
                            break_hard_link_418_6596()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=6597) as shell_command_419_6597:  # 0m:0.049s
                            shell_command_419_6597()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=6598, recursive=True) as chown_420_6598:  # 0m:0.000s
                            chown_420_6598()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=6599, recursive=True) as chmod_421_6599:  # 0m:0.008s
                            chmod_421_6599()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=6600) as cd_stage_422_6600:  # 0m:0.004s
            cd_stage_422_6600()
            with Stage(r"copy", r"WaveShell1-OBS 15.5 v15.5.79.262", prog_num=6601):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=6602) as should_copy_source_423_6602:  # ?
                    should_copy_source_423_6602()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=6603):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=6604) as copy_dir_to_dir_424_6604:  # ?
                            copy_dir_to_dir_424_6604()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=6605) as unwtar_425_6605:  # ?
                            unwtar_425_6605()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=6606, recursive=True) as chown_426_6606:  # ?
                            chown_426_6606()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=6607) as shell_command_427_6607:  # 0m:0.004s
                            shell_command_427_6607()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=6608) as cd_stage_428_6608:  # 0m:0.001s
            cd_stage_428_6608()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=6609):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=6610) as should_copy_source_429_6610:  # ?
                    should_copy_source_429_6610()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=6611):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=6612) as copy_dir_to_dir_430_6612:  # ?
                            copy_dir_to_dir_430_6612()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=6613) as unwtar_431_6613:  # ?
                            unwtar_431_6613()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=6614, recursive=True) as chown_432_6614:  # ?
                            chown_432_6614()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=6615) as shell_command_433_6615:  # 0m:0.001s
                            shell_command_433_6615()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6616) as cd_stage_434_6616:  # 0m:0.001s
            cd_stage_434_6616()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=6617):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=6618) as should_copy_source_435_6618:  # ?
                    should_copy_source_435_6618()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=6619):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=6620) as copy_dir_to_dir_436_6620:  # ?
                            copy_dir_to_dir_436_6620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=6621) as unwtar_437_6621:  # ?
                            unwtar_437_6621()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=6622, recursive=True) as chown_438_6622:  # ?
                            chown_438_6622()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=6623) as shell_command_439_6623:  # ?
                            shell_command_439_6623()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=6624) as script_command_440_6624:  # ?
                            script_command_440_6624()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=6625) as shell_command_441_6625:  # 0m:0.000s
                            shell_command_441_6625()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6626) as create_symlink_442_6626:  # 0m:0.000s
                create_symlink_442_6626()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=6627) as create_symlink_443_6627:  # 0m:0.000s
                create_symlink_443_6627()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=6628) as shell_command_444_6628:  # 0m:0.005s
            shell_command_444_6628()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=6629) as shell_command_445_6629:  # 0m:0.109s
            shell_command_445_6629()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=6630) as script_command_446_6630:  # 0m:0.009s
            script_command_446_6630()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=6631) as rm_file_or_dir_447_6631:  # 0m:0.416s
            rm_file_or_dir_447_6631()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=6632) as shell_command_448_6632:  # 0m:0.101s
            shell_command_448_6632()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=6633) as script_command_449_6633:  # 0m:0.008s
            script_command_449_6633()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=6634) as rm_file_or_dir_450_6634:  # 0m:0.000s
            rm_file_or_dir_450_6634()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=6635) as touch_451_6635:  # 0m:0.000s
            touch_451_6635()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=6636) as glober_452_6636:  # 0m:0.001s
            glober_452_6636()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=6637) as glober_453_6637:  # 0m:0.001s
            glober_453_6637()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=6638) as glober_454_6638:  # 0m:0.001s
            glober_454_6638()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=6639) as shell_command_455_6639:  # 0m:4.238s
            shell_command_455_6639()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=6640) as shell_command_456_6640:  # 0m:0.107s
            shell_command_456_6640()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=6641) as script_command_457_6641:  # 0m:0.007s
            script_command_457_6641()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=6642) as if_458_6642:  # 0m:0.004s
            if_458_6642()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=6643) as if_459_6643:  # 0m:0.001s
            if_459_6643()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=6644) as if_460_6644:  # 0m:0.000s
            if_460_6644()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=6645) as if_461_6645:  # 0m:0.000s
            if_461_6645()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=6646) as make_dir_462_6646:  # 0m:0.010s
            make_dir_462_6646()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=6647) as chmod_463_6647:  # 0m:0.000s
            chmod_463_6647()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=6648) as make_dir_464_6648:  # 0m:0.008s
            make_dir_464_6648()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=6649) as chmod_465_6649:  # 0m:0.001s
            chmod_465_6649()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=6650) as chmod_466_6650:  # 0m:0.000s
            chmod_466_6650()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=6651) as chmod_467_6651:  # 0m:0.000s
            chmod_467_6651()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=6652) as chmod_468_6652:  # 0m:0.000s
            chmod_468_6652()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=6653) as shell_command_469_6653:  # 0m:0.102s
            shell_command_469_6653()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=6654) as script_command_470_6654:  # 0m:0.009s
            script_command_470_6654()
    with Stage(r"post-copy", prog_num=6655):  # 0m:0.035s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=6656) as make_dir_471_6656:  # 0m:0.005s
            make_dir_471_6656()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=6657) as copy_file_to_file_472_6657:  # 0m:0.012s
            copy_file_to_file_472_6657()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6658) as chmod_473_6658:  # 0m:0.001s
            chmod_473_6658()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6659) as chmod_474_6659:  # 0m:0.000s
            chmod_474_6659()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=6660) as copy_file_to_file_475_6660:  # 0m:0.008s
            copy_file_to_file_475_6660()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6661) as chmod_476_6661:  # 0m:0.001s
            chmod_476_6661()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=6662) as copy_file_to_file_477_6662:  # 0m:0.008s
            copy_file_to_file_477_6662()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=6663) as chmod_478_6663:  # 0m:0.000s
            chmod_478_6663()
        Progress(r"Done copy", prog_num=6664)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=6665)()  # 0m:0.000s
    with Stage(r"post", prog_num=6666):  # 0m:0.047s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=6667) as make_dir_479_6667:  # 0m:0.004s
            make_dir_479_6667()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=6668) as copy_file_to_file_480_6668:  # 0m:0.011s
            copy_file_to_file_480_6668()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=6669) as make_dir_481_6669:  # 0m:0.005s
            make_dir_481_6669()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=6670) as copy_file_to_file_482_6670:  # 0m:0.012s
            copy_file_to_file_482_6670()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=6671) as make_dir_483_6671:  # 0m:0.005s
            make_dir_483_6671()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/43/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=6672) as copy_file_to_file_484_6672:  # 0m:0.009s
            copy_file_to_file_484_6672()

with Stage(r"epilog", prog_num=6673):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250320110803.py", prog_num=6674) as patch_py_batch_with_timings_485_6674:  # ?
        patch_py_batch_with_timings_485_6674()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 218750888 bytes in 0m:51.047s, 4285250 bytes per second
# copy time 0m:42.788s
