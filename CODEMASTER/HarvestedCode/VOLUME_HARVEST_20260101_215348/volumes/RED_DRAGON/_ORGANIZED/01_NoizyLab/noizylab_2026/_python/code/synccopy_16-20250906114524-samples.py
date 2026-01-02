# Creation time: 06-09-25_11-49
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 3505
PythonBatchCommandBase.running_progress = 529
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=530):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac64", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac64")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250906114524-samples"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries")
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
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NzIwOTUyNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU3MTczMjI0fX19XX0_;CloudFront-Signature=itoRg22ZNa1CwZ7o8tfIKYxieuNdR4KOLPK4Cf1enckxxuaNynKP1aYzv0v0BV3MIfO30aYFEG3x7LyD9psha2yx5nphoEdJp9vY7P-dR~ZDqYBFzIurNJPwCA1vJb4GBrAfJsh~2ljOVGPTlRkzndu-mHCM2MqmqAZ~YKz0S1-tSJIYkiUWvpGWI9fpBS1ioSMhxFKh5GisVJIQxpexrrgjhPdIjmMB4MBtNaAtdVonwRg0PCCQyG~H5n-32-k3tio8ImQx4sGeA8SaB4YcxJmIBtChq0guZogsLka-0vSTMg1k8y7mgOS~GcDO87ttzan0NDOiamG3qrbQWiSY7w__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1NzIwOTUyNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzU3MTczMjI0fX19XX0_;CloudFront-Signature=itoRg22ZNa1CwZ7o8tfIKYxieuNdR4KOLPK4Cf1enckxxuaNynKP1aYzv0v0BV3MIfO30aYFEG3x7LyD9psha2yx5nphoEdJp9vY7P-dR~ZDqYBFzIurNJPwCA1vJb4GBrAfJsh~2ljOVGPTlRkzndu-mHCM2MqmqAZ~YKz0S1-tSJIYkiUWvpGWI9fpBS1ioSMhxFKh5GisVJIQxpexrrgjhPdIjmMB4MBtNaAtdVonwRg0PCCQyG~H5n-32-k3tio8ImQx4sGeA8SaB4YcxJmIBtChq0guZogsLka-0vSTMg1k8y7mgOS~GcDO87ttzan0NDOiamG3qrbQWiSY7w__"
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
    config_vars['MAIN_INSTALL_TARGETS'] = (r"aeafdce2-ab51-4a48-8878-0f72e2e97e6f", r"e9325d8c-9b84-4ecd-b435-07252b4b1c85")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 32
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250906114524.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 4
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
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
    config_vars['REQUIRE_REPO_REV'] = 19
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
    config_vars['SYNC_FOLDER_MANIFEST_FILE'] = r"after-sync-sync-folder-manifest.txt"
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac64", r"MacArm")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac64"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 2971
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250906114524.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-08-23 23:57:51.343637"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.6.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac64", r"MacArm")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac64"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"InTrigger_Factory_Pack_IID", r"Waves_Audio_Factory_Pack_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"InTrigger_Factory_Pack_IID", r"Instrument_Data_Folder_IID", r"Sample_Libraries_Locations_Folder_IID", r"Waves_Audio_Factory_Pack_IID", r"Waves_Data_folder_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.2.1 2025-08-23 23:57:51.343637 bm-mac-ado12"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.2.1"
    config_vars['__INSTL_VERSION__'] = (2, 5, 2, 1)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"xrunavoinetsjtey"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"InTrigger_Factory_Pack_IID", r"Waves_Audio_Factory_Pack_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-09-06 11:50:50.861539"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 247502569
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 1415
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

with PythonBatchRuntime(r"synccopy", prog_num=531):
    with Stage(r"begin", prog_num=532):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=533):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=534) as copy_file_to_file_001_534:
            copy_file_to_file_001_534()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=535) as copy_file_to_file_002_535:
            copy_file_to_file_002_535()
    with Stage(r"sync", prog_num=536):
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=537):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=538) as make_dir_003_538:
                make_dir_003_538()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=539) as cd_004_539:
                cd_004_539()
                Progress(r"40 files already in cache", own_progress_count=40, prog_num=579)()
                with CreateSyncFolders(own_progress_count=54, prog_num=633) as create_sync_folders_005_633:
                    create_sync_folders_005_633()
                Progress(r"Downloading with 4 processes in parallel", prog_num=634)()
                Progress(r"Downloading with curl parallel", prog_num=635)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.py_curl/dl-00", total_files_to_download=1415, previously_downloaded_files=0, total_bytes_to_download=247502569, own_progress_count=1414, prog_num=2049, report_own_progress=False) as curl_with_internal_parallel_006_2049:
                    curl_with_internal_parallel_006_2049()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.py_curl/dl-01", total_files_to_download=1415, previously_downloaded_files=1414, total_bytes_to_download=247502569, prog_num=2050, report_own_progress=False) as curl_with_internal_parallel_007_2050:
                    curl_with_internal_parallel_007_2050()
                Progress(r"Downloading 1415 files done", prog_num=2051)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=2052) as run_in_thread_008_2052:
                    run_in_thread_008_2052()
                Progress(r"Check checksum ...", prog_num=2053)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=1415, prog_num=3468) as check_download_folder_checksum_009_3468:
                    check_download_folder_checksum_009_3468()
                with Stage(r"post_sync", prog_num=3469):
                    Progress(r"Adjust ownership and permissions /Applications/Waves/Data/Instrument Data/Waves Sample Libraries/InTrigger Factory Pack...", prog_num=3470)()
                    with ChmodAndChown(path=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/InTrigger Factory Pack", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=3471, recursive=True) as chmod_and_chown_010_3471:
                        chmod_and_chown_010_3471()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=3472) as copy_file_to_file_011_3472:
                        copy_file_to_file_011_3472()
            Progress(r"Done sync", prog_num=3473)()
    with Stage(r"copy", prog_num=3474):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=3475)()
        with Stage(r"create folders", prog_num=3476):
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=3477) as make_dir_012_3477:
                make_dir_012_3477()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=3478) as make_dir_013_3478:
                make_dir_013_3478()
            with MakeDir(r"/Users/Shared/Waves/Sample Libraries Locations", chowner=True, prog_num=3479) as make_dir_014_3479:
                make_dir_014_3479()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", prog_num=3480) as cd_stage_015_3480:
            cd_stage_015_3480()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/InTrigger Factory Pack", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/InTrigger Factory Pack", prog_num=3481) as create_symlink_016_3481:
                create_symlink_016_3481()
            with UnZip(source_zip=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", target_folder=r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", no_artifacts=True, prog_num=3482) as un_zip_017_3482:
                un_zip_017_3482()
            with CreateSymlink(r"/Users/Shared/Waves/Sample Libraries Locations/Waves Audio Factory Pack", r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Waves Audio Factory Pack", prog_num=3483) as create_symlink_018_3483:
                create_symlink_018_3483()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=3484) as shell_command_019_3484:
            shell_command_019_3484()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=3485) as script_command_020_3485:
            script_command_020_3485()
    with Stage(r"post-copy", prog_num=3486):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=3487) as make_dir_021_3487:
            make_dir_021_3487()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=3488) as copy_file_to_file_022_3488:
            copy_file_to_file_022_3488()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=3489) as chmod_023_3489:
            chmod_023_3489()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=3490) as chmod_024_3490:
            chmod_024_3490()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=3491) as copy_file_to_file_025_3491:
            copy_file_to_file_025_3491()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=3492) as chmod_026_3492:
            chmod_026_3492()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=3493) as copy_file_to_file_027_3493:
            copy_file_to_file_027_3493()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=3494) as chmod_028_3494:
            chmod_028_3494()
        Progress(r"Done copy", prog_num=3495)()
        Progress(r"Done synccopy", prog_num=3496)()
    with Stage(r"post", prog_num=3497):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=3498) as make_dir_029_3498:
            make_dir_029_3498()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=3499) as copy_file_to_file_030_3499:
            copy_file_to_file_030_3499()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=3500) as make_dir_031_3500:
            make_dir_031_3500()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=3501) as copy_file_to_file_032_3501:
            copy_file_to_file_032_3501()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=3502) as make_dir_033_3502:
            make_dir_033_3502()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=3503) as copy_file_to_file_034_3503:
            copy_file_to_file_034_3503()

with Stage(r"epilog", prog_num=3504):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-samples.py", prog_num=3505) as patch_py_batch_with_timings_035_3505:
        patch_py_batch_with_timings_035_3505()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


