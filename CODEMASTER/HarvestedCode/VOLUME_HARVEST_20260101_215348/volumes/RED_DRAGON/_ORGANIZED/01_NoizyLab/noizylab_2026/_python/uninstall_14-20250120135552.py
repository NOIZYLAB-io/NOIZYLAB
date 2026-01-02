# Creation time: 20-01-25_13-56
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 1205
PythonBatchCommandBase.running_progress = 315
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=316):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"14-20250120135552"
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.3.3"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V14", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V14", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = r"$(REPO_REV)"
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COPY_IGNORE_PATTERNS'] = (r"*.wtar.??", r"*.wtar", r"*.done", r"._*")
    config_vars['COPY_SOURCES_ROOT_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14"
    config_vars['CURL_CONFIG_FILE_NAME'] = r"dl"
    config_vars['CURL_CONNECT_TIMEOUT'] = 32
    config_vars['CURL_MAX_TIME'] = 600
    config_vars['CURL_RETRIES'] = 6
    config_vars['CURL_RETRY_DELAY'] = 12
    config_vars['Clean_old_plist_Native_NI'] = "If(IsConfigVarDefined(\"POST_INSTALL_SCRIPT_FILE\"), if_true=ScriptCommand(r\"\"\"echo rm -f \\\"$(__Clean_old_plist_Native_NI_1__)\\\" >> \"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_10-20250120135552-post-script.sh\" ;chmod a+rwx \"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_10-20250120135552-post-script.sh\" \"\"\"),if_false=RmFileOrDir(r\'\'\'$(__Clean_old_plist_Native_NI_1__)\'\'\'))"
    config_vars['DB_FILE_EXT'] = r"sqlite"
    config_vars['DEFAULT_IID_VERSION'] = r"0.0.0"
    config_vars['DIRECT_SYNC_INSTRUMENT_DATA'] = r"yes"
    config_vars['DONT_WRITE_CONFIG_VARS'] = (r"__CREDENTIALS__", r"__HELP_SUBJECT__", r"__INSTL_DATA_FOLDER__", r"__INSTL_DEFAULTS_FOLDER__", r"__USER_TEMP_DIR__", r"AWS_.+", r"INDEX_SIG", r"INFO_MAP_SIG", r"PUBLIC_KEY", r"SVN_REVISION", r".+_template", r"template_.+")
    config_vars['DOWNLOAD_TOOL_PATH'] = r"/curl"
    config_vars['EXIT_ON_EXEC_EXCEPTION'] = r"False"
    config_vars['FIX_ALL_PERMISSIONS_SYMBOLIC_MODE'] = r"u+rwx,go+rx"
    config_vars['Fix_Folder_Permissions'] = r'''Chmod(r"""$(__Fix_Folder_Permissions_1__)""", 'a+rwx' , message="UnLocking $(__Fix_Folder_Permissions_1__)", ignore_all_errors=True)'''
    config_vars['Fix_Folder_Permissions_Recursive'] = r'''Chmod(r"""$(__Fix_Folder_Permissions_Recursive_1__)""", 'a+rwX' , message="UnLocking $(__Fix_Folder_Permissions_Recursive_1__)", recursive=True, ignore_all_errors=True)'''
    config_vars['HAVE_INFO_MAP_COPY_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/new_have_info_map.txt"
    config_vars['HAVE_INFO_MAP_FILE_NAME'] = r"have_info_map.txt"
    config_vars['HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/have_info_map.txt"
    config_vars['HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 3, 10)
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/$(REPO_REV)/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/$(REPO_REV)"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_INSTALL_TARGETS'] = r"3b717287-aa1e-48f8-833f-ce3261c53f01"
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 177
    config_vars['MIN_REPO_REV'] = 1
    config_vars['MKDIR_SYMBOLIC_MODE'] = 493
    config_vars['Mac_ALL_OS_NAMES'] = r"Mac"
    config_vars['NEW_HAVE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/new_have_info_map.txt"
    config_vars['NEW_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/new_require.yaml"
    config_vars['NI_SERVICE_CENTER'] = r"/Library/Application Support/Native Instruments/Service Center"
    config_vars['NO_FLAGS_PATTERNS'] = (r"desktop.ini", r"*.ico")
    config_vars['NO_HARD_LINK_PATTERNS'] = (r"*Info.xml", r"*Info.plist", r"desktop.ini", r"*.ico")
    config_vars['NUM_DIGITS_PER_FOLDER_REPO_REV_HIERARCHY'] = 0
    config_vars['NUM_DIGITS_REPO_REV_HIERARCHY'] = 0
    config_vars['OLD_SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/old_require.yaml"
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/doit-output-20250120135552.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_SYNC'] = 16
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_10-20250120135552-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_10-20250120135552-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_10-20250120135552-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14-uninstall.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V14.yaml", r"/Library/Application Support/Waves/Central/V14/index.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 14
    config_vars['REPO_NAME'] = r"V14"
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V14_repo_rev.yaml"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V14_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V14"
    config_vars['REQUIRE_REPO_REV'] = 177
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V14"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHOULD_NOT_BE_REQUIRED_BY'] = r"(Plugin\d+_\d+_Root_\d+_\d+_IID)|(GTR(_Internals|_Stomps|Solo_Stomps)_IID)"
    config_vars['SITE_BOOKKEEPING_DIR'] = r"/Library/Application Support"
    config_vars['SITE_HAVE_INFO_MAP_PATH'] = r"/Library/Application Support/Waves/Central/V14/have_info_map.txt"
    config_vars['SITE_REPO_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central/V14"
    config_vars['SITE_REQUIRE_FILE_NAME'] = r"require.yaml"
    config_vars['SITE_REQUIRE_FILE_PATH'] = r"/Library/Application Support/Waves/Central/V14/require.yaml"
    config_vars['SITE_VENDOR_BOOKKEEPING_DIR'] = r"/Library/Application Support/Waves/Central"
    config_vars['SOURCE_PREFIX'] = r"Mac"
    config_vars['SPECIAL_BUILD_IN_IIDS'] = (r"__ALL_ITEMS_IID__", r"__ALL_GUIDS_IID__", r"__UPDATE_INSTALLED_ITEMS__", r"__REPAIR_INSTALLED_ITEMS__")
    config_vars['Set_Bundles_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Current_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/Mac/Icons/Folder.icns" --folder "$PWD" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f ./Icon? ]; then chmod a+rw ./Icon?; fi""")')
    config_vars['Set_Libs_Icon'] = r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension framework --folder . -c""", ignore_all_errors=True)'
    config_vars['Set_Specific_Folder_Icon'] = (r'ShellCommand(r""""/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/Mac/Icons/Folder.icns" --folder "$(__Set_Specific_Folder_Icon_1__)" -c""", ignore_all_errors=True)', r'ScriptCommand(r"""if [ -f "$(__Set_Specific_Folder_Icon_1__)"/Icon? ]; then chmod a+rw "$(__Set_Specific_Folder_Icon_1__)"/Icon?; fi""")')
    config_vars['TARGET_OS'] = r"Mac"
    config_vars['TARGET_OS_NAMES'] = (r"Mac", r"Mac32")
    config_vars['TARGET_OS_SECOND_NAME'] = r"Mac32"
    config_vars['TAR_MANIFEST_FILE_NAME'] = r"__TAR_CONTENT__.txt"
    config_vars['THIRD_PARTY_FOLDERS'] = (r"/Library/Audio/Plug-Ins/Components", r"/Library/Application Support/Digidesign/Plug-Ins", r"/Library/Audio/Plug-Ins/VST", r"/Library/Audio/Plug-Ins/VST3", r"/Library/Application Support/Avid/Audio/Plug-Ins", r"/Library/Application Support/Native Instruments/Service Center", r"/Library/Application Support/Propellerhead Software/ReWire")
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 886
    config_vars['TO_SYNC_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/$(S3_BUCKET_NAME)/V14/bookkeeping/to_sync_info_map.txt"
    config_vars['USER_CACHE_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl"
    config_vars['VENDOR_DIR_NAME'] = r"Waves/Central"
    config_vars['WAVESHELL_AAX_DIR'] = r"/Library/Application Support/Avid/Audio/Plug-Ins"
    config_vars['WAVES_APPS_DIR'] = r"/Applications/Waves/Applications V14"
    config_vars['WAVES_APPS_DIR_V10'] = r"/Applications/Waves/Applications V10"
    config_vars['WAVES_APPS_DIR_V11'] = r"/Applications/Waves/Applications V11"
    config_vars['WAVES_APPS_DIR_V12'] = r"/Applications/Waves/Applications V12"
    config_vars['WAVES_APPS_DIR_V13'] = r"/Applications/Waves/Applications V13"
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"uninstall", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/unloadRunningProcesses/doit-output-20250120135552.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2024-12-26 10:46:09.983540"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.2"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = ""
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"A-H_M_Documents_IID", r"A-H_M_IOM_IID", r"A-H_M_s3_Firmware_13_4_IID", r"A-H_M_s6_Firmware_13_4_IID", r"A-H_M_sq_Firmware_13_4_IID", r"A-H_M_v3_Firmware_14_12_IID", r"All_IOMs_IID", r"Apogee_Symphony_Documents_IID", r"Apogee_Symphony_Firmware_13_4_IID", r"Apogee_Symphony_IID", r"Apogee_Symphony_IOM_IID", r"Apogee_Symphony_micro_Firmware_13_4_IID", r"BR1_Documents_IID", r"BR1_Firmware_13_7_IID", r"BR1_IID", r"BR1_IOM_IID", r"Behringer_Wing_SoundGrid_IO_Driver_Firmware_14_25_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IOM_IID", r"Burl_BMB4_Documents_IID", r"Burl_BMB4_Firmware_13_4_IID", r"Burl_BMB4_IID", r"Burl_BMB4_IOM_IID", r"Cadac_Documents_IID", r"Cadac_Firmware_13_4_IID", r"Cadac_IID", r"Cadac_IOM_IID", r"Calrec_Documents_IID", r"Calrec_Firmware_13_4_IID", r"Calrec_IID", r"Calrec_IOM_IID", r"Converter_IID", r"Crest_Tactus_Documents_IID", r"Crest_Tactus_Firmware_13_4_IID", r"Crest_Tactus_IID", r"Crest_Tactus_IO_Modules_IID", r"Crest_Tactus_micro_Firmware_13_4_IID", r"DLI_DLS_Documents_IID", r"DLI_DLS_IID", r"DLI_DLS_IOM_IID", r"DLI_DLS_eMotion_IID", r"DLI_Firmware_12_1_IID", r"DLI_Firmware_13_4_IID", r"DLS_Firmware_12_1_IID", r"DLS_Firmware_13_4_IID", r"DMI_Waves_Documents_IID", r"DMI_Waves_Firmware_13_7_IID", r"DMI_Waves_IID", r"DMI_Waves_IOM_IID", r"DN32_WSG_Documents_IID", r"DN32_WSG_Firmware_13_4_IID", r"DN32_WSG_IID", r"DN32_WSG_IOM_IID", r"DSPro_SG1000_Firmware_13_4_IID", r"DSPro_SG1000_Firmware_13_6_IID", r"DSPro_SG1000_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_13_4_IID", r"DSPro_SG1000_micro_Firmware_14_25_IID", r"DSPro_SG1000_micro_Firmware_15_1_IID", r"DSPro_SG1000_micro_V2_Firmware_15_1_IID", r"DSPro_SG4000_Documents_IID", r"DSPro_SG4000_Firmware_13_4_IID", r"DSPro_SG4000_Firmware_13_5_IID", r"DSPro_SG4000_Firmware_14_26_IID", r"DSPro_SG4000_IID", r"DSPro_SG4000_IOM_IID", r"DSPro_SG4000_micro_Firmware_13_4_IID", r"DSPro_SG4000_micro_Firmware_14_25_IID", r"DSPro_SG4000_micro_Firmware_15_2_IID", r"DSPro_SG4000_micro_V2_Firmware_15_2_IID", r"DiGiGrid_D_Driver_Documents_IID", r"DiGiGrid_D_Driver_Firmware_13_4_IID", r"DiGiGrid_D_Driver_IID", r"DiGiGrid_D_Driver_IOM_IID", r"DiGiGrid_M_Driver_Documents_IID", r"DiGiGrid_M_Driver_Firmware_13_4_IID", r"DiGiGrid_M_Driver_IID", r"DiGiGrid_M_Driver_IOM_IID", r"DiGiGrid_Q_Driver_Documents_IID", r"DiGiGrid_Q_Driver_Firmware_13_4_IID", r"DiGiGrid_Q_Driver_IID", r"DiGiGrid_Q_Driver_IOM_IID", r"DigiGrid_SoundGrid__Documents__IID", r"Digico_SD_IOM_IID", r"Digico_SD_card_13_4_IID", r"Digico_SD_card_Documents_IID", r"Digico_SD_card_Firmware_14_21_IID", r"Digico_SD_card_IOM_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_22_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_IID", r"DirectOut_Exbox_Micro_SoundGrid_IO_Driver_Firmware_14_25_v2_micro_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IOM_IID", r"DirectOut_SG_MADI_Documents_IID", r"DirectOut_SG_MADI_Firmware_13_4_IID", r"DirectOut_SG_MADI_IID", r"DirectOut_SG_MADI_IOM_IID", r"DirectOut_SG_MADI_micro_Firmware_13_4_IID", r"DirectOut_SoundGrid_IO_Driver_Documents_IID", r"DirectOut_SoundGrid_IO_Driver_Firmware_14_18_IID", r"DirectOut_SoundGrid_IO_Driver_IID", r"DirectOut_SoundGrid_IO_Driver_IOM_IID", r"Hear_Back_Documents_IID", r"Hear_Back_Firmware_10_0_IID", r"Hear_Back_Firmware_13_7_IID", r"Hear_Back_IID", r"Hear_Back_IOM_IID", r"Hear_Back_IO_Modules_IID", r"Hear_Back_Pro_V2_Firmware_13_7_IID", r"Hear_Tech_Documents_IID", r"Hear_Tech_Firmware_15_1_IID", r"Hear_Tech_Firmware_15_1_v2_IID", r"Hear_Tech_IID", r"Hear_Tech_IOM_IID", r"IOC_Documents_IID", r"IOC_Firmware_13_4_IID", r"IOC_IID", r"IOC_IOM_IID", r"IOC_micro_Firmware_13_4_IID", r"IONIC16_Firmware_S25_IID", r"IONIC16_Firmware_S50_IID", r"IONIC_Documents_IID", r"IONIC_IID", r"IONIC_IOM_IID", r"IOS_Documents_IID", r"IOS_Firmware_13_4_IID", r"IOS_IID", r"IOS_IOM_IID", r"IOS_XL_Documents_IID", r"IOS_XL_Firmware_13_4_IID", r"IOS_XL_IID", r"IOS_XL_IOM_IID", r"IOS_XL_micro_Firmware_13_4_IID", r"IOS_eMotion_IID", r"IOS_micro_Firmware_13_4_IID", r"IOX_Documents_IID", r"IOX_Firmware_13_4_IID", r"IOX_IID", r"IOX_IOM_IID", r"IOX_eMotion_IID", r"IOX_micro_Firmware_13_4_IID", r"IOs_FW_and_Modules__IID", r"Insert_IID", r"JoeCo_Documents_IID", r"JoeCo_Firmware_13_4_IID", r"JoeCo_IID", r"JoeCo_IOM_IID", r"JoeCo_Utilities_IID", r"M-DL-WAVES3_IID", r"M-SQ-WAVES3_IID", r"M-Waves_V2_IID", r"MGB_Firmware_13_4_IID", r"MGB_MGO_Documents_IID", r"MGB_MGO_IID", r"MGB_MGO_IOM_IID", r"MGB_MGO_eMotion_IID", r"MGO_Firmware_13_4_IID", r"MKL_IID", r"MKL_x32_IID", r"MKL_x64_IID", r"MixerSessionConverter_IID", r"MultiRack_SG_IO_Modules_IID", r"MyRemote_IID", r"Plugin_Infra__IID", r"QT_5_12_8_IID", r"QT_5_5_1_FOR_IO_MODULES_IID", r"QT_5_5_1_IID", r"QT_6_2_4_IID", r"Remote_IO_Modules_IID", r"Restart_required_IID", r"SGS_14_9_Firmware_IID", r"SG_Connect_IID", r"SG_Driver_Documents_IID", r"SG_Driver_Uninstaller_IID", r"SG_Driver_V12_2_IID", r"SG_Driver_V12_2_Install_IID", r"SG_Infra_and_Common__IID", r"SG_Studio_V11_8CH_IID", r"SG_Studio_V11_preferences_cleanup_IID", r"STG_1608_Firmware_13_4_IID", r"STG_1608_micro_Firmware_13_4_IID", r"STG_2412_Documents_IID", r"STG_2412_Firmware_13_4_IID", r"STG_2412_IID", r"STG_2412_IOM_IID", r"STG_2412_micro_Firmware_13_4_IID", r"SampleTestConverter_IID", r"Session_Converters_IID", r"SoundGrid_Studio_IID", r"SoundGrid_Studio_Plugins__IID", r"SoundGrid_Studio_app__Application__IID", r"SoundGrid_Studio_app__Documents__IID", r"SoundGrid_Studio_app__IID", r"SoundGrid_Studio_app__Modules__IID", r"SoundGrid_Studio_app__Sessions_Structure__IID", r"SoundGrid_Studio_app__Shared_Folder__IID", r"SoundGrid_folder_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_14_12_IID", r"WaveShell1_AU_14_12_IID", r"WaveShell1_VST_2_V14_12_IID", r"WaveShell1_VST_3_V14_12_IID", r"WaveShell1_WPAPI_2_14_12_IID", r"WavesLib1_14_12_90_381_IID", r"X-WSG_Documents_IID", r"X-WSG_IID", r"X-WSG_IOM_IID", r"X-WSG_s6_Firmware_13_4_IID", r"Y-16_Documents_IID", r"Y-16_IID", r"Y-16_IOM_IID", r"Y-16_s3_Firmware_13_4_IID", r"Y-16_s6_Firmware_13_4_IID", r"Y-16_v3_Firmware_14_21_IID", r"Yamaha_HY128v2_Firmware_IID", r"Yamaha_WSG_Firmware_13_4_IID")
    config_vars['__GITHUB_BRANCH__'] = r"python3.9"
    config_vars['__GROUP_ID__'] = 0
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.4.2.3 2024-12-26 10:46:09.983540 bm-mac4"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.4.2.3"
    config_vars['__INSTL_VERSION__'] = (2, 4, 2, 3)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"nxsnlozqsspyepsr"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"uninstall"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"A-H_M_Common_IID", r"A-H_M_Firmware_IID", r"A-H_M_IOM_IID", r"A-H_M_IO_Modules_IID", r"A-H_M_s3_Firmware_10_0_IID", r"A-H_M_s3_Firmware_10_3_IID", r"A-H_M_s3_Firmware_12_1_IID", r"A-H_M_s6_Firmware_10_0_IID", r"A-H_M_s6_Firmware_10_3_IID", r"A-H_M_s6_Firmware_12_1_IID", r"A-H_M_sq_Firmware_10_0_IID", r"A-H_M_sq_Firmware_10_3_IID", r"A-H_M_sq_Firmware_12_1_IID", r"A-H_M_v3_Firmware_10_0_IID", r"A-H_M_v3_Firmware_10_3_IID", r"A-H_M_v3_Firmware_12_1_IID", r"A-H_M_v3_Firmware_13_4_IID", r"A-H_M_v3_Firmware_13_5_IID", r"A-H_M_v3_Firmware_14_9_IID", r"Apogee_Symphony_Common_IID", r"Apogee_Symphony_Firmware_10_0_IID", r"Apogee_Symphony_Firmware_10_3_IID", r"Apogee_Symphony_Firmware_12_1_IID", r"Apogee_Symphony_IID", r"Apogee_Symphony_micro_Firmware_10_0_IID", r"Apogee_Symphony_micro_Firmware_10_3_IID", r"Apogee_Symphony_micro_Firmware_12_1_IID", r"BR1_Common_IID", r"BR1_Firmware_10_3_IID", r"BR1_Firmware_12_1_IID", r"BR1_Firmware_13_4_IID", r"BR1_IID", r"Behringer_Wing_SoundGrid_IO_Driver_Common_IID", r"Behringer_Wing_SoundGrid_IO_Driver_IID", r"Burl_BMB4_Common_IID", r"Burl_BMB4_Firmware_10_0_IID", r"Burl_BMB4_Firmware_10_3_IID", r"Burl_BMB4_Firmware_12_1_IID", r"Burl_BMB4_IID", r"Cadac_Common_IID", r"Cadac_Firmware_10_0_IID", r"Cadac_Firmware_10_3_IID", r"Cadac_Firmware_12_3_IID", r"Cadac_IID", r"Cadac_IO_Modules_IID", r"Calrec_Common_IID", r"Calrec_Firmware_10_0_IID", r"Calrec_Firmware_10_3_IID", r"Calrec_Firmware_12_3_IID", r"Calrec_IID", r"Calrec_IO_Modules_IID", r"Cloud_MX_Audio_Mixer_IID", r"Crest_Tactus_FOH_IID", r"Crest_Tactus_Firmware_10_0_IID", r"Crest_Tactus_Firmware_10_3_IID", r"Crest_Tactus_Firmware_12_1_IID", r"Crest_Tactus_IO_Modules_IID", r"Crest_Tactus_Stage_IID", r"Crest_Tactus_micro_Firmware_10_0_IID", r"Crest_Tactus_micro_Firmware_10_3_IID", r"Crest_Tactus_micro_Firmware_12_1_IID", r"DLI_DLS_Common_IID", r"DLI_DLS_Firmware_IID", r"DLI_DLS_IID", r"DLI_DLS_IO_Modules_IID", r"DLI_Firmware_10_0_IID", r"DLI_Firmware_10_3_IID", r"DLI_Firmware_12_1_IID", r"DLS_Firmware_10_0_IID", r"DLS_Firmware_10_3_IID", r"DLS_Firmware_12_1_IID", r"DMI_Waves_Common_IID", r"DMI_Waves_Firmware_10_0_IID", r"DMI_Waves_Firmware_10_3_IID", r"DMI_Waves_Firmware_12_1_IID", r"DMI_Waves_Firmware_13_4_IID", r"DMI_Waves_IID", r"DMI_Waves_IO_Modules_IID", r"DN32_WSG_Common_IID", r"DN32_WSG_Firmware_10_2_IID", r"DN32_WSG_Firmware_10_3_IID", r"DN32_WSG_Firmware_12_1_IID", r"DN32_WSG_IID", r"DSPro_SG1000_Firmware_10_3_IID", r"DSPro_SG1000_Firmware_12_3_IID", r"DSPro_SG1000_Firmware_13_4_IID", r"DSPro_SG1000_Firmware_13_5_IID", r"DSPro_SG1000_micro_Firmware_10_3_IID", r"DSPro_SG1000_micro_Firmware_12_3_IID", r"DSPro_SG1000_micro_Firmware_13_4_IID", r"DSPro_SG1000_micro_Firmware_13_5_IID", r"DSPro_SG1000_micro_Firmware_13_7_IID", r"DSPro_SG1000_micro_Firmware_14_25_IID", r"DSPro_SG4000_Common_IID", r"DSPro_SG4000_Firmware_10_0_IID", r"DSPro_SG4000_Firmware_10_3_IID", r"DSPro_SG4000_Firmware_12_3_IID", r"DSPro_SG4000_Firmware_13_4_IID", r"DSPro_SG4000_IID", r"DSPro_SG4000_micro_Firmware_10_0_IID", r"DSPro_SG4000_micro_Firmware_10_3_IID", r"DSPro_SG4000_micro_Firmware_12_3_IID", r"DSPro_SG4000_micro_Firmware_13_4_IID", r"DSPro_SG4000_micro_Firmware_13_5_IID", r"DSPro_SG4000_micro_Firmware_13_7_IID", r"DiGiGrid_D_Driver_Common_IID", r"DiGiGrid_D_Driver_Firmware_10_0_IID", r"DiGiGrid_D_Driver_Firmware_10_3_IID", r"DiGiGrid_D_Driver_Firmware_12_1_IID", r"DiGiGrid_D_Driver_IID", r"DiGiGrid_D_Driver_IO_Modules_IID", r"DiGiGrid_M_Driver_Common_IID", r"DiGiGrid_M_Driver_Firmware_10_0_IID", r"DiGiGrid_M_Driver_Firmware_10_3_IID", r"DiGiGrid_M_Driver_Firmware_12_1_IID", r"DiGiGrid_M_Driver_IID", r"DiGiGrid_M_Driver_IO_Modules_IID", r"DiGiGrid_Q_Driver_Common_IID", r"DiGiGrid_Q_Driver_Firmware_10_0_IID", r"DiGiGrid_Q_Driver_Firmware_10_3_IID", r"DiGiGrid_Q_Driver_Firmware_12_1_IID", r"DiGiGrid_Q_Driver_IID", r"DiGiGrid_Q_Driver_IO_Modules_IID", r"Digico_SD_IOM_IID", r"Digico_SD_card_10_0_IID", r"Digico_SD_card_10_3_IID", r"Digico_SD_card_12_1_IID", r"Digico_SD_card_Common_IID", r"Digico_SD_card_Firmware_10_0_IID", r"Digico_SD_card_Firmware_10_2_IID", r"Digico_SD_card_Firmware_10_3_IID", r"Digico_SD_card_Firmware_12_1_IID", r"Digico_SD_card_Firmware_12_8_IID", r"Digico_SD_card_Firmware_13_4_IID", r"Digico_SD_card_Firmware_13_7_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Common_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Firmware_12_1_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_IID", r"DirectOut_SG_MADI_Common_IID", r"DirectOut_SG_MADI_Firmware_10_0_IID", r"DirectOut_SG_MADI_Firmware_10_3_IID", r"DirectOut_SG_MADI_Firmware_12_1_IID", r"DirectOut_SG_MADI_IID", r"DirectOut_SG_MADI_micro_Firmware_10_0_IID", r"DirectOut_SG_MADI_micro_Firmware_10_3_IID", r"DirectOut_SG_MADI_micro_Firmware_12_1_IID", r"DirectOut_SoundGrid_IO_Driver_Common_IID", r"DirectOut_SoundGrid_IO_Driver_IID", r"HearBack_Pro_V2_IID", r"Hear_Back_Common_IID", r"Hear_Back_Firmware_10_0_IID", r"Hear_Back_Firmware_10_3_IID", r"Hear_Back_Firmware_12_3_IID", r"Hear_Back_Firmware_13_4_IID", r"Hear_Back_IO_Modules_IID", r"Hear_Tech_Common_IID", r"Hear_Tech_Firmware_10_0_IID", r"Hear_Tech_Firmware_10_3_IID", r"Hear_Tech_Firmware_12_3_IID", r"Hear_Tech_Firmware_13_4_IID", r"Hear_Tech_Firmware_13_7_IID", r"Hear_Tech_Firmware_14_12_IID", r"Hear_Tech_IID", r"IOC_Common_IID", r"IOC_Firmware_10_0_IID", r"IOC_Firmware_10_3_IID", r"IOC_Firmware_12_1_IID", r"IOC_IID", r"IOC_IO_Modules_IID", r"IOC_micro_Firmware_10_0_IID", r"IOC_micro_Firmware_10_3_IID", r"IOC_micro_Firmware_12_1_IID", r"IONIC_Common_IID", r"IONIC_IID", r"IONIC_IOM_IID", r"IONIC_IO_Modules_IID", r"IOS_Common_IID", r"IOS_Firmware_10_0_IID", r"IOS_Firmware_10_3_IID", r"IOS_Firmware_12_1_IID", r"IOS_IID", r"IOS_IO_Modules_IID", r"IOS_XL_Common_IID", r"IOS_XL_Firmware_10_0_IID", r"IOS_XL_Firmware_10_3_IID", r"IOS_XL_Firmware_12_1_IID", r"IOS_XL_IID", r"IOS_XL_micro_Firmware_10_0_IID", r"IOS_XL_micro_Firmware_10_3_IID", r"IOS_XL_micro_Firmware_12_1_IID", r"IOS_micro_Firmware_10_0_IID", r"IOS_micro_Firmware_10_3_IID", r"IOS_micro_Firmware_12_1_IID", r"IOX_Common_IID", r"IOX_Firmware_10_0_IID", r"IOX_Firmware_10_3_IID", r"IOX_Firmware_12_1_IID", r"IOX_IID", r"IOX_IO_Modules_IID", r"IOX_micro_Firmware_10_0_IID", r"IOX_micro_Firmware_10_3_IID", r"IOX_micro_Firmware_12_1_IID", r"IO_MODULES_COMMON_IID", r"IO_MODULES_PLUGIN_INHERIT_IID", r"JoeCo_Common_IID", r"JoeCo_Firmware_10_0_IID", r"JoeCo_Firmware_10_3_IID", r"JoeCo_Firmware_12_1_IID", r"JoeCo_IID", r"LiveRack_IID", r"M-DL-WAVES3_IID", r"M-SQ-WAVES3_IID", r"M-Waves_V2_IID", r"MGB_Firmware_10_0_IID", r"MGB_Firmware_10_3_IID", r"MGB_Firmware_13_0_IID", r"MGB_MGO_Common_IID", r"MGB_MGO_Firmware_IID", r"MGB_MGO_IID", r"MGB_MGO_IO_Modules_IID", r"MGO_Firmware_10_0_IID", r"MGO_Firmware_10_3_IID", r"MGO_Firmware_13_0_IID", r"MultiRack_SG_IO_Modules_IID", r"MyRemote_IID", r"Remote_IO_Modules_IID", r"SGINV_IID", r"SGRCK_IID", r"SG_Connect_IID", r"SG_Driver_V12_2_guid_IID", r"SG_Driver_V14_guid_IID", r"SG_Inventory_Common_IID", r"SG_Studio_V11_16CH_IID", r"SG_Studio_V11_32CH_IID", r"SG_Studio_V11_64CH_IID", r"SG_Studio_V11_8CH_IID", r"SG_for_Venue_IO_13_1_IID", r"STG_1608_Firmware_10_0_IID", r"STG_1608_Firmware_10_3_IID", r"STG_1608_Firmware_12_3_IID", r"STG_1608_micro_Firmware_10_0_IID", r"STG_1608_micro_Firmware_10_3_IID", r"STG_1608_micro_Firmware_12_3_IID", r"STG_2412_Common_IID", r"STG_2412_Firmware_10_0_IID", r"STG_2412_Firmware_10_3_IID", r"STG_2412_Firmware_12_3_IID", r"STG_2412_IID", r"STG_2412_micro_Firmware_10_0_IID", r"STG_2412_micro_Firmware_10_3_IID", r"STG_2412_micro_Firmware_12_3_IID", r"SoundGrid_QRec_IID", r"SoundGrid_Studio_app__Application__IID", r"SuperRack_Performer__IID", r"SuperRack_SoundGrid_Offline_Mode_IID", r"SuperRack_SoundGrid__IID", r"UNINSTALL_AS_APPLICATION", r"X-WSG_Common_IID", r"X-WSG_IID", r"X-WSG_s6_Firmware_10_0_IID", r"X-WSG_s6_Firmware_10_3_IID", r"X-WSG_s6_Firmware_12_1_IID", r"Y-16_Common_IID", r"Y-16_Firmware_IID", r"Y-16_IID", r"Y-16_IO_Modules_IID", r"Y-16_s3_Firmware_10_0_IID", r"Y-16_s3_Firmware_10_3_IID", r"Y-16_s3_Firmware_12_3_IID", r"Y-16_s6_Firmware_10_0_IID", r"Y-16_s6_Firmware_10_3_IID", r"Y-16_s6_Firmware_12_3_IID", r"Yamaha_WSG_Firmware_10_3_IID", r"Yamaha_WSG_Firmware_12_3_IID", r"eMotion_LV1_16CH_IID", r"eMotion_LV1_32CH_IID", r"eMotion_LV1_64CH_IID", r"eMotion_LV1_Native_16CH_IID", r"eMotion_LV1_Native_32CH_IID", r"eMotion_LV1_Native_64CH_IID", r"eMotion_LV1_Session_Editor_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-01-20 13:56:09.733579"
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = (r"A-H_M_Common_IID", r"A-H_M_Firmware_IID", r"A-H_M_IO_Modules_IID", r"A-H_M_s3_Firmware_10_0_IID", r"A-H_M_s3_Firmware_10_3_IID", r"A-H_M_s3_Firmware_12_1_IID", r"A-H_M_s6_Firmware_10_0_IID", r"A-H_M_s6_Firmware_10_3_IID", r"A-H_M_s6_Firmware_12_1_IID", r"A-H_M_sq_Firmware_10_0_IID", r"A-H_M_sq_Firmware_10_3_IID", r"A-H_M_sq_Firmware_12_1_IID", r"A-H_M_v3_Firmware_10_0_IID", r"A-H_M_v3_Firmware_10_3_IID", r"A-H_M_v3_Firmware_12_1_IID", r"A-H_M_v3_Firmware_13_4_IID", r"A-H_M_v3_Firmware_13_5_IID", r"A-H_M_v3_Firmware_14_9_IID", r"Apogee_Symphony_Common_IID", r"Apogee_Symphony_Firmware_10_0_IID", r"Apogee_Symphony_Firmware_10_3_IID", r"Apogee_Symphony_Firmware_12_1_IID", r"Apogee_Symphony_micro_Firmware_10_0_IID", r"Apogee_Symphony_micro_Firmware_10_3_IID", r"Apogee_Symphony_micro_Firmware_12_1_IID", r"BR1_Common_IID", r"BR1_Firmware_10_3_IID", r"BR1_Firmware_12_1_IID", r"BR1_Firmware_13_4_IID", r"Behringer_Wing_SoundGrid_IO_Driver_Common_IID", r"Burl_BMB4_Common_IID", r"Burl_BMB4_Firmware_10_0_IID", r"Burl_BMB4_Firmware_10_3_IID", r"Burl_BMB4_Firmware_12_1_IID", r"Cadac_Common_IID", r"Cadac_Firmware_10_0_IID", r"Cadac_Firmware_10_3_IID", r"Cadac_Firmware_12_3_IID", r"Cadac_IO_Modules_IID", r"Calrec_Common_IID", r"Calrec_Firmware_10_0_IID", r"Calrec_Firmware_10_3_IID", r"Calrec_Firmware_12_3_IID", r"Calrec_IO_Modules_IID", r"Cloud_MX_Audio_Mixer_IID", r"Crest_Tactus_FOH_IID", r"Crest_Tactus_Firmware_10_0_IID", r"Crest_Tactus_Firmware_10_3_IID", r"Crest_Tactus_Firmware_12_1_IID", r"Crest_Tactus_Stage_IID", r"Crest_Tactus_micro_Firmware_10_0_IID", r"Crest_Tactus_micro_Firmware_10_3_IID", r"Crest_Tactus_micro_Firmware_12_1_IID", r"DLI_DLS_Common_IID", r"DLI_DLS_Firmware_IID", r"DLI_DLS_IO_Modules_IID", r"DLI_Firmware_10_0_IID", r"DLI_Firmware_10_3_IID", r"DLS_Firmware_10_0_IID", r"DLS_Firmware_10_3_IID", r"DMI_Waves_Common_IID", r"DMI_Waves_Firmware_10_0_IID", r"DMI_Waves_Firmware_10_3_IID", r"DMI_Waves_Firmware_12_1_IID", r"DMI_Waves_Firmware_13_4_IID", r"DMI_Waves_IO_Modules_IID", r"DN32_WSG_Common_IID", r"DN32_WSG_Firmware_10_2_IID", r"DN32_WSG_Firmware_10_3_IID", r"DN32_WSG_Firmware_12_1_IID", r"DSPro_SG1000_Firmware_10_3_IID", r"DSPro_SG1000_Firmware_12_3_IID", r"DSPro_SG1000_Firmware_13_5_IID", r"DSPro_SG1000_micro_Firmware_10_3_IID", r"DSPro_SG1000_micro_Firmware_12_3_IID", r"DSPro_SG1000_micro_Firmware_13_5_IID", r"DSPro_SG1000_micro_Firmware_13_7_IID", r"DSPro_SG4000_Common_IID", r"DSPro_SG4000_Firmware_10_0_IID", r"DSPro_SG4000_Firmware_10_3_IID", r"DSPro_SG4000_Firmware_12_3_IID", r"DSPro_SG4000_micro_Firmware_10_0_IID", r"DSPro_SG4000_micro_Firmware_10_3_IID", r"DSPro_SG4000_micro_Firmware_12_3_IID", r"DSPro_SG4000_micro_Firmware_13_5_IID", r"DSPro_SG4000_micro_Firmware_13_7_IID", r"DiGiGrid_D_Driver_Common_IID", r"DiGiGrid_D_Driver_Firmware_10_0_IID", r"DiGiGrid_D_Driver_Firmware_10_3_IID", r"DiGiGrid_D_Driver_Firmware_12_1_IID", r"DiGiGrid_D_Driver_IO_Modules_IID", r"DiGiGrid_M_Driver_Common_IID", r"DiGiGrid_M_Driver_Firmware_10_0_IID", r"DiGiGrid_M_Driver_Firmware_10_3_IID", r"DiGiGrid_M_Driver_Firmware_12_1_IID", r"DiGiGrid_M_Driver_IO_Modules_IID", r"DiGiGrid_Q_Driver_Common_IID", r"DiGiGrid_Q_Driver_Firmware_10_0_IID", r"DiGiGrid_Q_Driver_Firmware_10_3_IID", r"DiGiGrid_Q_Driver_Firmware_12_1_IID", r"DiGiGrid_Q_Driver_IO_Modules_IID", r"Digico_SD_card_10_0_IID", r"Digico_SD_card_10_3_IID", r"Digico_SD_card_12_1_IID", r"Digico_SD_card_Common_IID", r"Digico_SD_card_Firmware_10_0_IID", r"Digico_SD_card_Firmware_10_2_IID", r"Digico_SD_card_Firmware_10_3_IID", r"Digico_SD_card_Firmware_12_1_IID", r"Digico_SD_card_Firmware_12_8_IID", r"Digico_SD_card_Firmware_13_4_IID", r"Digico_SD_card_Firmware_13_7_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Common_IID", r"DirectOut_Exbox_SoundGrid_IO_Driver_Firmware_12_1_IID", r"DirectOut_SG_MADI_Common_IID", r"DirectOut_SG_MADI_Firmware_10_0_IID", r"DirectOut_SG_MADI_Firmware_10_3_IID", r"DirectOut_SG_MADI_Firmware_12_1_IID", r"DirectOut_SG_MADI_micro_Firmware_10_0_IID", r"DirectOut_SG_MADI_micro_Firmware_10_3_IID", r"DirectOut_SG_MADI_micro_Firmware_12_1_IID", r"DirectOut_SoundGrid_IO_Driver_Common_IID", r"HearBack_Pro_V2_IID", r"Hear_Back_Common_IID", r"Hear_Back_Firmware_10_3_IID", r"Hear_Back_Firmware_12_3_IID", r"Hear_Back_Firmware_13_4_IID", r"Hear_Tech_Common_IID", r"Hear_Tech_Firmware_10_0_IID", r"Hear_Tech_Firmware_10_3_IID", r"Hear_Tech_Firmware_12_3_IID", r"Hear_Tech_Firmware_13_4_IID", r"Hear_Tech_Firmware_13_7_IID", r"Hear_Tech_Firmware_14_12_IID", r"IOC_Common_IID", r"IOC_Firmware_10_0_IID", r"IOC_Firmware_10_3_IID", r"IOC_Firmware_12_1_IID", r"IOC_IO_Modules_IID", r"IOC_micro_Firmware_10_0_IID", r"IOC_micro_Firmware_10_3_IID", r"IOC_micro_Firmware_12_1_IID", r"IONIC_Common_IID", r"IONIC_IO_Modules_IID", r"IOS_Common_IID", r"IOS_Firmware_10_0_IID", r"IOS_Firmware_10_3_IID", r"IOS_Firmware_12_1_IID", r"IOS_IO_Modules_IID", r"IOS_XL_Common_IID", r"IOS_XL_Firmware_10_0_IID", r"IOS_XL_Firmware_10_3_IID", r"IOS_XL_Firmware_12_1_IID", r"IOS_XL_micro_Firmware_10_0_IID", r"IOS_XL_micro_Firmware_10_3_IID", r"IOS_XL_micro_Firmware_12_1_IID", r"IOS_micro_Firmware_10_0_IID", r"IOS_micro_Firmware_10_3_IID", r"IOS_micro_Firmware_12_1_IID", r"IOX_Common_IID", r"IOX_Firmware_10_0_IID", r"IOX_Firmware_10_3_IID", r"IOX_Firmware_12_1_IID", r"IOX_IO_Modules_IID", r"IOX_micro_Firmware_10_0_IID", r"IOX_micro_Firmware_10_3_IID", r"IOX_micro_Firmware_12_1_IID", r"IO_MODULES_COMMON_IID", r"IO_MODULES_PLUGIN_INHERIT_IID", r"JoeCo_Common_IID", r"JoeCo_Firmware_10_0_IID", r"JoeCo_Firmware_10_3_IID", r"JoeCo_Firmware_12_1_IID", r"LiveRack_IID", r"MGB_Firmware_10_0_IID", r"MGB_Firmware_10_3_IID", r"MGB_Firmware_13_0_IID", r"MGB_MGO_Common_IID", r"MGB_MGO_Firmware_IID", r"MGB_MGO_IO_Modules_IID", r"MGO_Firmware_10_0_IID", r"MGO_Firmware_10_3_IID", r"MGO_Firmware_13_0_IID", r"SGINV_IID", r"SGRCK_IID", r"SG_Driver_V12_2_guid_IID", r"SG_Driver_V14_guid_IID", r"SG_Inventory_Common_IID", r"SG_Studio_V11_16CH_IID", r"SG_Studio_V11_32CH_IID", r"SG_Studio_V11_64CH_IID", r"SG_for_Venue_IO_13_1_IID", r"STG_1608_Firmware_10_0_IID", r"STG_1608_Firmware_10_3_IID", r"STG_1608_Firmware_12_3_IID", r"STG_1608_micro_Firmware_10_0_IID", r"STG_1608_micro_Firmware_10_3_IID", r"STG_1608_micro_Firmware_12_3_IID", r"STG_2412_Common_IID", r"STG_2412_Firmware_10_0_IID", r"STG_2412_Firmware_10_3_IID", r"STG_2412_Firmware_12_3_IID", r"STG_2412_micro_Firmware_10_0_IID", r"STG_2412_micro_Firmware_10_3_IID", r"STG_2412_micro_Firmware_12_3_IID", r"SoundGrid_QRec_IID", r"SuperRack_Performer__IID", r"SuperRack_SoundGrid_Offline_Mode_IID", r"SuperRack_SoundGrid__IID", r"UNINSTALL_AS_APPLICATION", r"X-WSG_Common_IID", r"X-WSG_s6_Firmware_10_0_IID", r"X-WSG_s6_Firmware_10_3_IID", r"X-WSG_s6_Firmware_12_1_IID", r"Y-16_Common_IID", r"Y-16_Firmware_IID", r"Y-16_IO_Modules_IID", r"Y-16_s3_Firmware_10_0_IID", r"Y-16_s3_Firmware_10_3_IID", r"Y-16_s3_Firmware_12_3_IID", r"Y-16_s6_Firmware_10_0_IID", r"Y-16_s6_Firmware_10_3_IID", r"Y-16_s6_Firmware_12_3_IID", r"Yamaha_WSG_Firmware_10_3_IID", r"Yamaha_WSG_Firmware_12_3_IID", r"eMotion_LV1_16CH_IID", r"eMotion_LV1_32CH_IID", r"eMotion_LV1_64CH_IID", r"eMotion_LV1_Native_16CH_IID", r"eMotion_LV1_Native_32CH_IID", r"eMotion_LV1_Native_64CH_IID", r"eMotion_LV1_Session_Editor_IID")
    config_vars['__PLATFORM_NODE__'] = r"bm-mac4"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_COMPILER__'] = r"site-packages"
    config_vars['__PYTHON_VERSION__'] = (3, 9, 4, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Library/Application Support/Waves/Central/V14", r"/Library/Application Support/Waves/Central/V14", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
    config_vars['__SITE_CONFIG_DIR__'] = r"/Library/Application Support"
    config_vars['__SITE_DATA_DIR__'] = r"/Library/Application Support"
    config_vars['__SOCKET_HOSTNAME__'] = r"bm-mac4"
    config_vars['__SQLITE_VERSION__'] = r"3.34.0"
    config_vars['__SUDO_USER__'] = r"no set"
    config_vars['__SYSTEM_LOG_FILE_PATH__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/instl/instl.log"
    config_vars['__TARGET_DIR__'] = r"/Applications/Waves/Data/linux/lib/mkl"
    config_vars['__USER_CONFIG_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_CONFIG_FILE_NAME__'] = r"instl_config.yaml"
    config_vars['__USER_CONFIG_FILE_PATH__'] = r"/Users/rsp_ms/instl_config.yaml"
    config_vars['__USER_DATA_DIR__'] = r"/Users/rsp_ms/Library/Application Support"
    config_vars['__USER_DESKTOP_DIR__'] = r"/Users/rsp_ms/Desktop"
    config_vars['__USER_HOME_DIR__'] = r"/Users/rsp_ms"
    config_vars['__USER_ID__'] = 0

with PythonBatchRuntime(r"uninstall", prog_num=317):
    with Stage(r"begin", prog_num=318):
        PythonBatchCommandBase.set_a_kwargs_default("ignore_all_errors", True)
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=319):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=320) as copy_file_to_file_001_320:
            copy_file_to_file_001_320()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=321) as copy_file_to_file_002_321:
            copy_file_to_file_002_321()
    with Stage(r"remove", prog_num=322):
        Progress(r"Start remove", prog_num=323)()
        with ShellCommand(r"""osascript -e 'tell application "SoundGrid Studio" to quit' """, ignore_all_errors=True, prog_num=324) as shell_command_003_324:
            shell_command_003_324()
        with ShellCommand(r"""osascript -e 'tell application "System Events" to delete login item "SoundGrid Studio"' """, ignore_all_errors=True, prog_num=325) as shell_command_004_325:
            shell_command_004_325()
        with ShellCommand(r"launchctl unload /Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", ignore_all_errors=True, prog_num=326) as shell_command_005_326:
            shell_command_005_326()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist"', ignore_all_errors=True, prog_num=327) as shell_command_006_327:
            shell_command_006_327()
        with RmFileOrDir(r"/${HOME}/Library/LaunchAgents/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=328) as rm_file_or_dir_007_328:
            rm_file_or_dir_007_328()
        with Stage(r"Remove from folder", r"/Users/Shared/Waves/SoundGrid Studio/Templates", prog_num=329):
            with Stage(r"Remove", r"SoundGrid Studio Sessions Structure", prog_num=330):
                with RmFile(r"/Users/Shared/Waves/SoundGrid Studio/Templates/Empty Session.sgst", prog_num=331) as rm_file_008_331:
                    rm_file_008_331()
        with Stage(r"Remove from folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=332):
            with Stage(r"Remove", r"WaveShell1-WPAPI_2 14.12", prog_num=333):
                with RmDir(r"//Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 14.12.bundle", prog_num=334) as rm_dir_009_334:
                    rm_dir_009_334()
        with Stage(r"Remove from folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=335):
            with Stage(r"Remove", r"WaveShell1-VST3 14.12", prog_num=336):
                with RmDir(r"//Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 14.12.vst3", prog_num=337) as rm_dir_010_337:
                    rm_dir_010_337()
        with Stage(r"Remove from folder", r"/Library/Audio/Plug-Ins/VST", prog_num=338):
            with Stage(r"Remove", r"WaveShell1-VST 14.12", prog_num=339):
                with RmDir(r"//Library/Audio/Plug-Ins/VST/WaveShell1-VST 14.12.vst", prog_num=340) as rm_dir_011_340:
                    rm_dir_011_340()
        with Stage(r"Remove from folder", r"/Library/Audio/Plug-Ins/Components", prog_num=341):
            with Stage(r"Remove", r"WaveShell1-AU 14.12", prog_num=342):
                with RmDir(r"//Library/Audio/Plug-Ins/Components/WaveShell1-AU 14.12.component", prog_num=343) as rm_dir_012_343:
                    rm_dir_012_343()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=344):
            with Cd(r"/Library/Application Support/Waves/SoundGrid IO Modules", prog_num=345) as cd_013_345:
                cd_013_345()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid IO Modules", prog_num=346)()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=347) as rm_dir_014_347:
                    rm_dir_014_347()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=348) as rm_dir_015_348:
                    rm_dir_015_348()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=349) as rm_dir_016_349:
                    rm_dir_016_349()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=350) as rm_dir_017_350:
                    rm_dir_017_350()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.app", prog_num=351) as rm_dir_018_351:
                    rm_dir_018_351()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 10.0.bundle", prog_num=352) as rm_dir_019_352:
                    rm_dir_019_352()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.app", prog_num=353) as rm_dir_020_353:
                    rm_dir_020_353()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 12.1.bundle", prog_num=354) as rm_dir_021_354:
                    rm_dir_021_354()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.app", prog_num=355) as rm_dir_022_355:
                    rm_dir_022_355()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control 13.1.bundle", prog_num=356) as rm_dir_023_356:
                    rm_dir_023_356()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.app", prog_num=357) as rm_dir_024_357:
                    rm_dir_024_357()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 10.0.bundle", prog_num=358) as rm_dir_025_358:
                    rm_dir_025_358()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.app", prog_num=359) as rm_dir_026_359:
                    rm_dir_026_359()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 12.1.bundle", prog_num=360) as rm_dir_027_360:
                    rm_dir_027_360()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.app", prog_num=361) as rm_dir_028_361:
                    rm_dir_028_361()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII 13.1.bundle", prog_num=362) as rm_dir_029_362:
                    rm_dir_029_362()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.app", prog_num=363) as rm_dir_030_363:
                    rm_dir_030_363()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 10.0.bundle", prog_num=364) as rm_dir_031_364:
                    rm_dir_031_364()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.app", prog_num=365) as rm_dir_032_365:
                    rm_dir_032_365()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 12.1.bundle", prog_num=366) as rm_dir_033_366:
                    rm_dir_033_366()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.app", prog_num=367) as rm_dir_034_367:
                    rm_dir_034_367()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1 13.1.bundle", prog_num=368) as rm_dir_035_368:
                    rm_dir_035_368()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.app", prog_num=369) as rm_dir_036_369:
                    rm_dir_036_369()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 10.0.bundle", prog_num=370) as rm_dir_037_370:
                    rm_dir_037_370()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.app", prog_num=371) as rm_dir_038_371:
                    rm_dir_038_371()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 12.1.bundle", prog_num=372) as rm_dir_039_372:
                    rm_dir_039_372()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.app", prog_num=373) as rm_dir_040_373:
                    rm_dir_040_373()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control 13.1.bundle", prog_num=374) as rm_dir_041_374:
                    rm_dir_041_374()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 9.7.bundle", prog_num=375) as rm_dir_042_375:
                    rm_dir_042_375()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 10.0.bundle", prog_num=376) as rm_dir_043_376:
                    rm_dir_043_376()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 12.1.bundle", prog_num=377) as rm_dir_044_377:
                    rm_dir_044_377()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control 13.1.bundle", prog_num=378) as rm_dir_045_378:
                    rm_dir_045_378()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 9.7.bundle", prog_num=379) as rm_dir_046_379:
                    rm_dir_046_379()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 10.0.bundle", prog_num=380) as rm_dir_047_380:
                    rm_dir_047_380()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 12.1.bundle", prog_num=381) as rm_dir_048_381:
                    rm_dir_048_381()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control 13.1.bundle", prog_num=382) as rm_dir_049_382:
                    rm_dir_049_382()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.app", prog_num=383) as rm_dir_050_383:
                    rm_dir_050_383()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 9.7.bundle", prog_num=384) as rm_dir_051_384:
                    rm_dir_051_384()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.app", prog_num=385) as rm_dir_052_385:
                    rm_dir_052_385()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 10.0.bundle", prog_num=386) as rm_dir_053_386:
                    rm_dir_053_386()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.app", prog_num=387) as rm_dir_054_387:
                    rm_dir_054_387()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 12.1.bundle", prog_num=388) as rm_dir_055_388:
                    rm_dir_055_388()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.app", prog_num=389) as rm_dir_056_389:
                    rm_dir_056_389()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control 13.1.bundle", prog_num=390) as rm_dir_057_390:
                    rm_dir_057_390()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.app", prog_num=391) as rm_dir_058_391:
                    rm_dir_058_391()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 9.7.bundle", prog_num=392) as rm_dir_059_392:
                    rm_dir_059_392()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.app", prog_num=393) as rm_dir_060_393:
                    rm_dir_060_393()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 10.0.bundle", prog_num=394) as rm_dir_061_394:
                    rm_dir_061_394()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.app", prog_num=395) as rm_dir_062_395:
                    rm_dir_062_395()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 12.1.bundle", prog_num=396) as rm_dir_063_396:
                    rm_dir_063_396()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.app", prog_num=397) as rm_dir_064_397:
                    rm_dir_064_397()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control 13.1.bundle", prog_num=398) as rm_dir_065_398:
                    rm_dir_065_398()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.app", prog_num=399) as rm_dir_066_399:
                    rm_dir_066_399()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 10.0.bundle", prog_num=400) as rm_dir_067_400:
                    rm_dir_067_400()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.app", prog_num=401) as rm_dir_068_401:
                    rm_dir_068_401()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 12.1.bundle", prog_num=402) as rm_dir_069_402:
                    rm_dir_069_402()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.app", prog_num=403) as rm_dir_070_403:
                    rm_dir_070_403()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DMI Control 13.1.bundle", prog_num=404) as rm_dir_071_404:
                    rm_dir_071_404()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.app", prog_num=405) as rm_dir_072_405:
                    rm_dir_072_405()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 10.0.bundle", prog_num=406) as rm_dir_073_406:
                    rm_dir_073_406()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.app", prog_num=407) as rm_dir_074_407:
                    rm_dir_074_407()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 12.1.bundle", prog_num=408) as rm_dir_075_408:
                    rm_dir_075_408()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.app", prog_num=409) as rm_dir_076_409:
                    rm_dir_076_409()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control 13.1.bundle", prog_num=410) as rm_dir_077_410:
                    rm_dir_077_410()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.app", prog_num=411) as rm_dir_078_411:
                    rm_dir_078_411()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 10.0.bundle", prog_num=412) as rm_dir_079_412:
                    rm_dir_079_412()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.app", prog_num=413) as rm_dir_080_413:
                    rm_dir_080_413()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 12.1.bundle", prog_num=414) as rm_dir_081_414:
                    rm_dir_081_414()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.app", prog_num=415) as rm_dir_082_415:
                    rm_dir_082_415()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control 13.1.bundle", prog_num=416) as rm_dir_083_416:
                    rm_dir_083_416()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.app", prog_num=417) as rm_dir_084_417:
                    rm_dir_084_417()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 9.7.bundle", prog_num=418) as rm_dir_085_418:
                    rm_dir_085_418()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.app", prog_num=419) as rm_dir_086_419:
                    rm_dir_086_419()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 10.0.bundle", prog_num=420) as rm_dir_087_420:
                    rm_dir_087_420()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.app", prog_num=421) as rm_dir_088_421:
                    rm_dir_088_421()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 12.1.bundle", prog_num=422) as rm_dir_089_422:
                    rm_dir_089_422()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.app", prog_num=423) as rm_dir_090_423:
                    rm_dir_090_423()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control 13.1.bundle", prog_num=424) as rm_dir_091_424:
                    rm_dir_091_424()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.app", prog_num=425) as rm_dir_092_425:
                    rm_dir_092_425()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 10.0.bundle", prog_num=426) as rm_dir_093_426:
                    rm_dir_093_426()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.app", prog_num=427) as rm_dir_094_427:
                    rm_dir_094_427()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 12.1.bundle", prog_num=428) as rm_dir_095_428:
                    rm_dir_095_428()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.app", prog_num=429) as rm_dir_096_429:
                    rm_dir_096_429()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control 13.1.bundle", prog_num=430) as rm_dir_097_430:
                    rm_dir_097_430()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.app", prog_num=431) as rm_dir_098_431:
                    rm_dir_098_431()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 10.0.bundle", prog_num=432) as rm_dir_099_432:
                    rm_dir_099_432()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.app", prog_num=433) as rm_dir_100_433:
                    rm_dir_100_433()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 12.1.bundle", prog_num=434) as rm_dir_101_434:
                    rm_dir_101_434()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.app", prog_num=435) as rm_dir_102_435:
                    rm_dir_102_435()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control 13.1.bundle", prog_num=436) as rm_dir_103_436:
                    rm_dir_103_436()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.app", prog_num=437) as rm_dir_104_437:
                    rm_dir_104_437()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.bundle", prog_num=438) as rm_dir_105_438:
                    rm_dir_105_438()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.app", prog_num=439) as rm_dir_106_439:
                    rm_dir_106_439()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.bundle", prog_num=440) as rm_dir_107_440:
                    rm_dir_107_440()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 12.1.exe", prog_num=441) as rm_file_108_441:
                    rm_file_108_441()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface 13.1.exe", prog_num=442) as rm_file_109_442:
                    rm_file_109_442()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.app", prog_num=443) as rm_dir_110_443:
                    rm_dir_110_443()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 10.0.bundle", prog_num=444) as rm_dir_111_444:
                    rm_dir_111_444()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.app", prog_num=445) as rm_dir_112_445:
                    rm_dir_112_445()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 12.1.bundle", prog_num=446) as rm_dir_113_446:
                    rm_dir_113_446()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.app", prog_num=447) as rm_dir_114_447:
                    rm_dir_114_447()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control 13.1.bundle", prog_num=448) as rm_dir_115_448:
                    rm_dir_115_448()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.app", prog_num=449) as rm_dir_116_449:
                    rm_dir_116_449()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 10.0.bundle", prog_num=450) as rm_dir_117_450:
                    rm_dir_117_450()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.app", prog_num=451) as rm_dir_118_451:
                    rm_dir_118_451()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 12.1.bundle", prog_num=452) as rm_dir_119_452:
                    rm_dir_119_452()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.app", prog_num=453) as rm_dir_120_453:
                    rm_dir_120_453()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control 13.1.bundle", prog_num=454) as rm_dir_121_454:
                    rm_dir_121_454()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.app", prog_num=455) as rm_dir_122_455:
                    rm_dir_122_455()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 9.7.bundle", prog_num=456) as rm_dir_123_456:
                    rm_dir_123_456()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.app", prog_num=457) as rm_dir_124_457:
                    rm_dir_124_457()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 10.0.bundle", prog_num=458) as rm_dir_125_458:
                    rm_dir_125_458()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.app", prog_num=459) as rm_dir_126_459:
                    rm_dir_126_459()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 12.1.bundle", prog_num=460) as rm_dir_127_460:
                    rm_dir_127_460()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.app", prog_num=461) as rm_dir_128_461:
                    rm_dir_128_461()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control 13.1.bundle", prog_num=462) as rm_dir_129_462:
                    rm_dir_129_462()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.app", prog_num=463) as rm_dir_130_463:
                    rm_dir_130_463()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 9.7.bundle", prog_num=464) as rm_dir_131_464:
                    rm_dir_131_464()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.app", prog_num=465) as rm_dir_132_465:
                    rm_dir_132_465()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 10.0.bundle", prog_num=466) as rm_dir_133_466:
                    rm_dir_133_466()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.app", prog_num=467) as rm_dir_134_467:
                    rm_dir_134_467()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 12.1.bundle", prog_num=468) as rm_dir_135_468:
                    rm_dir_135_468()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.app", prog_num=469) as rm_dir_136_469:
                    rm_dir_136_469()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control 13.1.bundle", prog_num=470) as rm_dir_137_470:
                    rm_dir_137_470()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.app", prog_num=471) as rm_dir_138_471:
                    rm_dir_138_471()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 10.0.bundle", prog_num=472) as rm_dir_139_472:
                    rm_dir_139_472()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.app", prog_num=473) as rm_dir_140_473:
                    rm_dir_140_473()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 12.1.bundle", prog_num=474) as rm_dir_141_474:
                    rm_dir_141_474()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.app", prog_num=475) as rm_dir_142_475:
                    rm_dir_142_475()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control 13.1.bundle", prog_num=476) as rm_dir_143_476:
                    rm_dir_143_476()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.app", prog_num=477) as rm_dir_144_477:
                    rm_dir_144_477()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 9.7.bundle", prog_num=478) as rm_dir_145_478:
                    rm_dir_145_478()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.app", prog_num=479) as rm_dir_146_479:
                    rm_dir_146_479()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 10.0.bundle", prog_num=480) as rm_dir_147_480:
                    rm_dir_147_480()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.app", prog_num=481) as rm_dir_148_481:
                    rm_dir_148_481()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 12.1.bundle", prog_num=482) as rm_dir_149_482:
                    rm_dir_149_482()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.app", prog_num=483) as rm_dir_150_483:
                    rm_dir_150_483()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control 13.1.bundle", prog_num=484) as rm_dir_151_484:
                    rm_dir_151_484()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.app", prog_num=485) as rm_dir_152_485:
                    rm_dir_152_485()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 10.0.bundle", prog_num=486) as rm_dir_153_486:
                    rm_dir_153_486()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.app", prog_num=487) as rm_dir_154_487:
                    rm_dir_154_487()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 12.1.bundle", prog_num=488) as rm_dir_155_488:
                    rm_dir_155_488()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.app", prog_num=489) as rm_dir_156_489:
                    rm_dir_156_489()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control 13.1.bundle", prog_num=490) as rm_dir_157_490:
                    rm_dir_157_490()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.app", prog_num=491) as rm_dir_158_491:
                    rm_dir_158_491()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 10.0.bundle", prog_num=492) as rm_dir_159_492:
                    rm_dir_159_492()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.app", prog_num=493) as rm_dir_160_493:
                    rm_dir_160_493()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 12.1.bundle", prog_num=494) as rm_dir_161_494:
                    rm_dir_161_494()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.app", prog_num=495) as rm_dir_162_495:
                    rm_dir_162_495()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control 13.1.bundle", prog_num=496) as rm_dir_163_496:
                    rm_dir_163_496()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.app", prog_num=497) as rm_dir_164_497:
                    rm_dir_164_497()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 10.0.bundle", prog_num=498) as rm_dir_165_498:
                    rm_dir_165_498()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.app", prog_num=499) as rm_dir_166_499:
                    rm_dir_166_499()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 12.1.bundle", prog_num=500) as rm_dir_167_500:
                    rm_dir_167_500()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.app", prog_num=501) as rm_dir_168_501:
                    rm_dir_168_501()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control 13.1.bundle", prog_num=502) as rm_dir_169_502:
                    rm_dir_169_502()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.app", prog_num=503) as rm_dir_170_503:
                    rm_dir_170_503()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 9.7.bundle", prog_num=504) as rm_dir_171_504:
                    rm_dir_171_504()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.app", prog_num=505) as rm_dir_172_505:
                    rm_dir_172_505()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v3 Control 10.0.bundle", prog_num=506) as rm_dir_173_506:
                    rm_dir_173_506()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.app", prog_num=507) as rm_dir_174_507:
                    rm_dir_174_507()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 10.0.bundle", prog_num=508) as rm_dir_175_508:
                    rm_dir_175_508()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.app", prog_num=509) as rm_dir_176_509:
                    rm_dir_176_509()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 12.1.bundle", prog_num=510) as rm_dir_177_510:
                    rm_dir_177_510()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.app", prog_num=511) as rm_dir_178_511:
                    rm_dir_178_511()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control 13.1.bundle", prog_num=512) as rm_dir_179_512:
                    rm_dir_179_512()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.app", prog_num=513) as rm_dir_180_513:
                    rm_dir_180_513()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 9.7.bundle", prog_num=514) as rm_dir_181_514:
                    rm_dir_181_514()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.app", prog_num=515) as rm_dir_182_515:
                    rm_dir_182_515()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 10.0.bundle", prog_num=516) as rm_dir_183_516:
                    rm_dir_183_516()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.app", prog_num=517) as rm_dir_184_517:
                    rm_dir_184_517()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 12.1.bundle", prog_num=518) as rm_dir_185_518:
                    rm_dir_185_518()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.app", prog_num=519) as rm_dir_186_519:
                    rm_dir_186_519()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control 13.1.bundle", prog_num=520) as rm_dir_187_520:
                    rm_dir_187_520()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.app", prog_num=521) as rm_dir_188_521:
                    rm_dir_188_521()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 9.7.bundle", prog_num=522) as rm_dir_189_522:
                    rm_dir_189_522()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.app", prog_num=523) as rm_dir_190_523:
                    rm_dir_190_523()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 10.0.bundle", prog_num=524) as rm_dir_191_524:
                    rm_dir_191_524()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.app", prog_num=525) as rm_dir_192_525:
                    rm_dir_192_525()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 12.1.bundle", prog_num=526) as rm_dir_193_526:
                    rm_dir_193_526()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.app", prog_num=527) as rm_dir_194_527:
                    rm_dir_194_527()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control 13.1.bundle", prog_num=528) as rm_dir_195_528:
                    rm_dir_195_528()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.app", prog_num=529) as rm_dir_196_529:
                    rm_dir_196_529()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 10.0.bundle", prog_num=530) as rm_dir_197_530:
                    rm_dir_197_530()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.app", prog_num=531) as rm_dir_198_531:
                    rm_dir_198_531()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 12.1.bundle", prog_num=532) as rm_dir_199_532:
                    rm_dir_199_532()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.app", prog_num=533) as rm_dir_200_533:
                    rm_dir_200_533()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control 13.1.bundle", prog_num=534) as rm_dir_201_534:
                    rm_dir_201_534()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 10.0.bundle", prog_num=535) as rm_dir_202_535:
                    rm_dir_202_535()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 12.1.bundle", prog_num=536) as rm_dir_203_536:
                    rm_dir_203_536()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control 13.1.bundle", prog_num=537) as rm_dir_204_537:
                    rm_dir_204_537()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.app", prog_num=538) as rm_dir_205_538:
                    rm_dir_205_538()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 10.0.bundle", prog_num=539) as rm_dir_206_539:
                    rm_dir_206_539()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.app", prog_num=540) as rm_dir_207_540:
                    rm_dir_207_540()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 12.1.bundle", prog_num=541) as rm_dir_208_541:
                    rm_dir_208_541()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.app", prog_num=542) as rm_dir_209_542:
                    rm_dir_209_542()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control 13.1.bundle", prog_num=543) as rm_dir_210_543:
                    rm_dir_210_543()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.app", prog_num=544) as rm_dir_211_544:
                    rm_dir_211_544()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 10.0.bundle", prog_num=545) as rm_dir_212_545:
                    rm_dir_212_545()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.app", prog_num=546) as rm_dir_213_546:
                    rm_dir_213_546()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 12.1.bundle", prog_num=547) as rm_dir_214_547:
                    rm_dir_214_547()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.app", prog_num=548) as rm_dir_215_548:
                    rm_dir_215_548()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control 13.1.bundle", prog_num=549) as rm_dir_216_549:
                    rm_dir_216_549()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.app", prog_num=550) as rm_dir_217_550:
                    rm_dir_217_550()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 9.7.bundle", prog_num=551) as rm_dir_218_551:
                    rm_dir_218_551()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.app", prog_num=552) as rm_dir_219_552:
                    rm_dir_219_552()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/WSG Y-16 v2 Control 10.0.bundle", prog_num=553) as rm_dir_220_553:
                    rm_dir_220_553()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.app", prog_num=554) as rm_dir_221_554:
                    rm_dir_221_554()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 10.0.bundle", prog_num=555) as rm_dir_222_555:
                    rm_dir_222_555()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.app", prog_num=556) as rm_dir_223_556:
                    rm_dir_223_556()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 12.1.bundle", prog_num=557) as rm_dir_224_557:
                    rm_dir_224_557()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.app", prog_num=558) as rm_dir_225_558:
                    rm_dir_225_558()
                with RmDir(r"/Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control 13.1.bundle", prog_num=559) as rm_dir_226_559:
                    rm_dir_226_559()
            with Stage(r"Remove", r"Apogee Symphony MKII Control Panel", prog_num=560):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.app", prog_num=561) as rm_dir_227_561:
                    rm_dir_227_561()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Symphony MKII.bundle", prog_num=562) as rm_dir_228_562:
                    rm_dir_228_562()
            with Stage(r"Remove", r"SoundGrid BR-1 Control Panel", prog_num=563):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.app", prog_num=564) as rm_dir_229_564:
                    rm_dir_229_564()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid BR1.bundle", prog_num=565) as rm_dir_230_565:
                    rm_dir_230_565()
            with Stage(r"Remove", r"Behringer Wing SoundGrid I/O Driver Control Panel", prog_num=566):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.app", prog_num=567) as rm_dir_231_567:
                    rm_dir_231_567()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid Wing Control.bundle", prog_num=568) as rm_dir_232_568:
                    rm_dir_232_568()
            with Stage(r"Remove", r"BMB4 SoundGrid MotherBoard Control Panel", prog_num=569):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.app", prog_num=570) as rm_dir_233_570:
                    rm_dir_233_570()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/BMB4 Motherboard Control.bundle", prog_num=571) as rm_dir_234_571:
                    rm_dir_234_571()
            with Stage(r"Remove", r"Cadac Control Panel", prog_num=572):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Cadac Control.bundle", prog_num=573) as rm_dir_235_573:
                    rm_dir_235_573()
            with Stage(r"Remove", r"Calrec Control Panel", prog_num=574):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Calrec Control.bundle", prog_num=575) as rm_dir_236_575:
                    rm_dir_236_575()
            with Stage(r"Remove", r"Crest Audio Tactus Control Panel", prog_num=576):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.app", prog_num=577) as rm_dir_237_577:
                    rm_dir_237_577()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Tactus Stage FOH Control.bundle", prog_num=578) as rm_dir_238_578:
                    rm_dir_238_578()
            with Stage(r"Remove", r"DigiGrid DLI/DLS Control Panel", prog_num=579):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.app", prog_num=580) as rm_dir_239_580:
                    rm_dir_239_580()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid DLI DLS Control.bundle", prog_num=581) as rm_dir_240_581:
                    rm_dir_240_581()
            with Stage(r"Remove", r"DMI Waves Control Panel", prog_num=582):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.app", prog_num=583) as rm_dir_241_583:
                    rm_dir_241_583()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DMI Control.bundle", prog_num=584) as rm_dir_242_584:
                    rm_dir_242_584()
            with Stage(r"Remove", r"DN32-WSG Control Panel", prog_num=585):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.app", prog_num=586) as rm_dir_243_586:
                    rm_dir_243_586()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid DN32-WSG Control.bundle", prog_num=587) as rm_dir_244_587:
                    rm_dir_244_587()
            with Stage(r"Remove", r"DSPro SG4000 / SG1000 Control Panel", prog_num=588):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.app", prog_num=589) as rm_dir_245_589:
                    rm_dir_245_589()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DSPro SG4000 Control.bundle", prog_num=590) as rm_dir_246_590:
                    rm_dir_246_590()
            with Stage(r"Remove", r"DigiGrid D Control Panel", prog_num=591):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.app", prog_num=592) as rm_dir_247_592:
                    rm_dir_247_592()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid D Control.bundle", prog_num=593) as rm_dir_248_593:
                    rm_dir_248_593()
            with Stage(r"Remove", r"DigiGrid M Control Panel", prog_num=594):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.app", prog_num=595) as rm_dir_249_595:
                    rm_dir_249_595()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid M Control.bundle", prog_num=596) as rm_dir_250_596:
                    rm_dir_250_596()
            with Stage(r"Remove", r"DigiGrid Q Control Panel", prog_num=597):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.app", prog_num=598) as rm_dir_251_598:
                    rm_dir_251_598()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid Q Control.bundle", prog_num=599) as rm_dir_252_599:
                    rm_dir_252_599()
            with Stage(r"Remove", r"Digico SD Control Panel", prog_num=600):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.app", prog_num=601) as rm_dir_253_601:
                    rm_dir_253_601()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiCo SD Control.bundle", prog_num=602) as rm_dir_254_602:
                    rm_dir_254_602()
            with Stage(r"Remove", r"DirectOut Exbox SoundGrid I/O Driver Control Panel", prog_num=603):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", prog_num=604) as rm_dir_255_604:
                    rm_dir_255_604()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=605) as rm_dir_256_605:
                    rm_dir_256_605()
            with Stage(r"Remove", r"DirectOut SG.MADI Control Panel", prog_num=606):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.app", prog_num=607) as rm_dir_257_607:
                    rm_dir_257_607()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SG.MADI Control.bundle", prog_num=608) as rm_dir_258_608:
                    rm_dir_258_608()
            with Stage(r"Remove", r"DirectOut SoundGrid I/O Driver Control Panel", prog_num=609):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.app", prog_num=610) as rm_dir_259_610:
                    rm_dir_259_610()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DirectOut SoundGrid Interface.bundle", prog_num=611) as rm_dir_260_611:
                    rm_dir_260_611()
            with Stage(r"Remove", r"Hear Technologies SG Control Panel", prog_num=612):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.app", prog_num=613) as rm_dir_261_613:
                    rm_dir_261_613()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Hear Technologies SG Control.bundle", prog_num=614) as rm_dir_262_614:
                    rm_dir_262_614()
            with Stage(r"Remove", r"DigiGrid IOC Control Panel", prog_num=615):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.app", prog_num=616) as rm_dir_263_616:
                    rm_dir_263_616()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOC Control.bundle", prog_num=617) as rm_dir_264_617:
                    rm_dir_264_617()
            with Stage(r"Remove", r"IONIC16 Control Panel", prog_num=618):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.app", prog_num=619) as rm_dir_265_619:
                    rm_dir_265_619()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/IONIC Control.bundle", prog_num=620) as rm_dir_266_620:
                    rm_dir_266_620()
            with Stage(r"Remove", r"DigiGrid IOS Control Panel", prog_num=621):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.app", prog_num=622) as rm_dir_267_622:
                    rm_dir_267_622()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS Control.bundle", prog_num=623) as rm_dir_268_623:
                    rm_dir_268_623()
            with Stage(r"Remove", r"DigiGrid IOS-XL Control Panel", prog_num=624):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.app", prog_num=625) as rm_dir_269_625:
                    rm_dir_269_625()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOS-XL Control.bundle", prog_num=626) as rm_dir_270_626:
                    rm_dir_270_626()
            with Stage(r"Remove", r"DigiGrid IOX Control Panel", prog_num=627):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.app", prog_num=628) as rm_dir_271_628:
                    rm_dir_271_628()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid IOX Control.bundle", prog_num=629) as rm_dir_272_629:
                    rm_dir_272_629()
            with Stage(r"Remove", r"JoeCo BBSG24MP Control Panel", prog_num=630):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.app", prog_num=631) as rm_dir_273_631:
                    rm_dir_273_631()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/JoeCo BBSG24MP Control.bundle", prog_num=632) as rm_dir_274_632:
                    rm_dir_274_632()
            with Stage(r"Remove", r"M-DL-WAVES3 Control Panel", prog_num=633):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.app", prog_num=634) as rm_dir_275_634:
                    rm_dir_275_634()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-DL-WAVES3 Control.bundle", prog_num=635) as rm_dir_276_635:
                    rm_dir_276_635()
            with Stage(r"Remove", r"M-SQ-WAVES3 Control Panel", prog_num=636):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.app", prog_num=637) as rm_dir_277_637:
                    rm_dir_277_637()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-SQ-WAVES3 Control.bundle", prog_num=638) as rm_dir_278_638:
                    rm_dir_278_638()
            with Stage(r"Remove", r"M-Waves v2 Control Panel", prog_num=639):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.app", prog_num=640) as rm_dir_279_640:
                    rm_dir_279_640()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/M-Waves v2 Control.bundle", prog_num=641) as rm_dir_280_641:
                    rm_dir_280_641()
            with Stage(r"Remove", r"DigiGrid MGB/MGO/MGR Control Panel", prog_num=642):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.app", prog_num=643) as rm_dir_281_643:
                    rm_dir_281_643()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/DiGiGrid MGB MGO Control.bundle", prog_num=644) as rm_dir_282_644:
                    rm_dir_282_644()
            with Stage(r"Remove", r"Waves Legacy SG Control Panels", prog_num=645):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.app", prog_num=646) as rm_dir_283_646:
                    rm_dir_283_646()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Waves Legacy Control.bundle", prog_num=647) as rm_dir_284_647:
                    rm_dir_284_647()
            with Stage(r"Remove", r"Remote SG IO Control Panel", prog_num=648):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.app", prog_num=649) as rm_dir_285_649:
                    rm_dir_285_649()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/RIOMGeneral Control.bundle", prog_num=650) as rm_dir_286_650:
                    rm_dir_286_650()
            with Stage(r"Remove", r"SG Connect", prog_num=651):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SG Connect Control.bundle", prog_num=652) as rm_dir_287_652:
                    rm_dir_287_652()
            with Stage(r"Remove", r"SoundStudio STG Control Panel", prog_num=653):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.app", prog_num=654) as rm_dir_288_654:
                    rm_dir_288_654()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundStudio STG Control.bundle", prog_num=655) as rm_dir_289_655:
                    rm_dir_289_655()
            with Stage(r"Remove", r"X-WSG Control Panel", prog_num=656):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.app", prog_num=657) as rm_dir_290_657:
                    rm_dir_290_657()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/SoundGrid X-WSG Control.bundle", prog_num=658) as rm_dir_291_658:
                    rm_dir_291_658()
            with Stage(r"Remove", r"Yamaha SoundGrid IO Control Panel", prog_num=659):
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.app", prog_num=660) as rm_dir_292_660:
                    rm_dir_292_660()
                with RmDir(r"//Library/Application Support/Waves/SoundGrid IO Modules/Yamaha WSG Control.bundle", prog_num=661) as rm_dir_293_661:
                    rm_dir_293_661()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=662):
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=663) as cd_294_663:
                cd_294_663()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/SGS", prog_num=664)()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_9.7.wfi", prog_num=665) as rm_file_295_665:
                    rm_file_295_665()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.0.wfi", prog_num=666) as rm_file_296_666:
                    rm_file_296_666()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.2.wfi", prog_num=667) as rm_file_297_667:
                    rm_file_297_667()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_10.3.wfi", prog_num=668) as rm_file_298_668:
                    rm_file_298_668()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.1.wfi", prog_num=669) as rm_file_299_669:
                    rm_file_299_669()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_11.2.wfi", prog_num=670) as rm_file_300_670:
                    rm_file_300_670()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.2.wfi", prog_num=671) as rm_file_301_671:
                    rm_file_301_671()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_12.8.wfi", prog_num=672) as rm_file_302_672:
                    rm_file_302_672()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_13.3.wfi", prog_num=673) as rm_file_303_673:
                    rm_file_303_673()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.6.wfi", prog_num=674) as rm_file_304_674:
                    rm_file_304_674()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.9.wfi", prog_num=675) as rm_file_305_675:
                    rm_file_305_675()
            with Stage(r"Remove", r"SoundGrid Server Firmware", prog_num=676):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/SGS/SGS_14.26.wfi", prog_num=677) as rm_file_306_677:
                    rm_file_306_677()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=678):
            with Cd(r"/Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=679) as cd_307_679:
                cd_307_679()
                Progress(r"remove previous versions /Library/Application Support/Waves/SoundGrid Firmware/IO", prog_num=680)()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGB.wfi", prog_num=681) as rm_file_308_681:
                    rm_file_308_681()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGB.wfi", prog_num=682) as rm_file_309_682:
                    rm_file_309_682()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGB.wfi", prog_num=683) as rm_file_310_683:
                    rm_file_310_683()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_MGO.wfi", prog_num=684) as rm_file_311_684:
                    rm_file_311_684()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_MGO.wfi", prog_num=685) as rm_file_312_685:
                    rm_file_312_685()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_MGO.wfi", prog_num=686) as rm_file_313_686:
                    rm_file_313_686()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridD.wfi", prog_num=687) as rm_file_314_687:
                    rm_file_314_687()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridD.wfi", prog_num=688) as rm_file_315_688:
                    rm_file_315_688()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridD.wfi", prog_num=689) as rm_file_316_689:
                    rm_file_316_689()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridM.wfi", prog_num=690) as rm_file_317_690:
                    rm_file_317_690()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridM.wfi", prog_num=691) as rm_file_318_691:
                    rm_file_318_691()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridM.wfi", prog_num=692) as rm_file_319_692:
                    rm_file_319_692()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiGridQ.wfi", prog_num=693) as rm_file_320_693:
                    rm_file_320_693()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiGridQ.wfi", prog_num=694) as rm_file_321_694:
                    rm_file_321_694()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiGridQ.wfi", prog_num=695) as rm_file_322_695:
                    rm_file_322_695()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLI.wfi", prog_num=696) as rm_file_323_696:
                    rm_file_323_696()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLI.wfi", prog_num=697) as rm_file_324_697:
                    rm_file_324_697()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLI.wfi", prog_num=698) as rm_file_325_698:
                    rm_file_325_698()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_DLS.wfi", prog_num=699) as rm_file_326_699:
                    rm_file_326_699()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_DLS.wfi", prog_num=700) as rm_file_327_700:
                    rm_file_327_700()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_DLS.wfi", prog_num=701) as rm_file_328_701:
                    rm_file_328_701()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s3.wfi", prog_num=702) as rm_file_329_702:
                    rm_file_329_702()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s3.wfi", prog_num=703) as rm_file_330_703:
                    rm_file_330_703()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s3.wfi", prog_num=704) as rm_file_331_704:
                    rm_file_331_704()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_s6.wfi", prog_num=705) as rm_file_332_705:
                    rm_file_332_705()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_s6.wfi", prog_num=706) as rm_file_333_706:
                    rm_file_333_706()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_s6.wfi", prog_num=707) as rm_file_334_707:
                    rm_file_334_707()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_A_H_V3.wfi", prog_num=708) as rm_file_335_708:
                    rm_file_335_708()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_A_H_V3.wfi", prog_num=709) as rm_file_336_709:
                    rm_file_336_709()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_A_H_V3.wfi", prog_num=710) as rm_file_337_710:
                    rm_file_337_710()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_A_H_V3.wfi", prog_num=711) as rm_file_338_711:
                    rm_file_338_711()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_A_H_V3.wfi", prog_num=712) as rm_file_339_712:
                    rm_file_339_712()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.9_A_H_V3.wfi", prog_num=713) as rm_file_340_713:
                    rm_file_340_713()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_AH_sq.wfi", prog_num=714) as rm_file_341_714:
                    rm_file_341_714()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_AH_sq.wfi", prog_num=715) as rm_file_342_715:
                    rm_file_342_715()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_AH_sq.wfi", prog_num=716) as rm_file_343_716:
                    rm_file_343_716()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_X_WSG.wfi", prog_num=717) as rm_file_344_717:
                    rm_file_344_717()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG.wfi", prog_num=718) as rm_file_345_718:
                    rm_file_345_718()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG.wfi", prog_num=719) as rm_file_346_719:
                    rm_file_346_719()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s3.wfi", prog_num=720) as rm_file_347_720:
                    rm_file_347_720()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s3.wfi", prog_num=721) as rm_file_348_721:
                    rm_file_348_721()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s3.wfi", prog_num=722) as rm_file_349_722:
                    rm_file_349_722()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s3.wfi", prog_num=723) as rm_file_350_723:
                    rm_file_350_723()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_yamaha_s6.wfi", prog_num=724) as rm_file_351_724:
                    rm_file_351_724()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_yamaha_s6.wfi", prog_num=725) as rm_file_352_725:
                    rm_file_352_725()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_yamaha_s6.wfi", prog_num=726) as rm_file_353_726:
                    rm_file_353_726()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_yamaha_s6.wfi", prog_num=727) as rm_file_354_727:
                    rm_file_354_727()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Hy.wfi", prog_num=728) as rm_file_355_728:
                    rm_file_355_728()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Hy.wfi", prog_num=729) as rm_file_356_729:
                    rm_file_356_729()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC.wfi", prog_num=730) as rm_file_357_730:
                    rm_file_357_730()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC.wfi", prog_num=731) as rm_file_358_731:
                    rm_file_358_731()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC.wfi", prog_num=732) as rm_file_359_732:
                    rm_file_359_732()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOC_micro.wfi", prog_num=733) as rm_file_360_733:
                    rm_file_360_733()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOC_micro.wfi", prog_num=734) as rm_file_361_734:
                    rm_file_361_734()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOC_micro.wfi", prog_num=735) as rm_file_362_735:
                    rm_file_362_735()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS.wfi", prog_num=736) as rm_file_363_736:
                    rm_file_363_736()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS.wfi", prog_num=737) as rm_file_364_737:
                    rm_file_364_737()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS.wfi", prog_num=738) as rm_file_365_738:
                    rm_file_365_738()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_micro.wfi", prog_num=739) as rm_file_366_739:
                    rm_file_366_739()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_micro.wfi", prog_num=740) as rm_file_367_740:
                    rm_file_367_740()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_micro.wfi", prog_num=741) as rm_file_368_741:
                    rm_file_368_741()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.13_IONIC16_S25.wfi", prog_num=742) as rm_file_369_742:
                    rm_file_369_742()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.22_IONIC16_S25.wfi", prog_num=743) as rm_file_370_743:
                    rm_file_370_743()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL.wfi", prog_num=744) as rm_file_371_744:
                    rm_file_371_744()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL.wfi", prog_num=745) as rm_file_372_745:
                    rm_file_372_745()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL.wfi", prog_num=746) as rm_file_373_746:
                    rm_file_373_746()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOS_XL_micro.wfi", prog_num=747) as rm_file_374_747:
                    rm_file_374_747()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOS_XL_micro.wfi", prog_num=748) as rm_file_375_748:
                    rm_file_375_748()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOS_XL_micro.wfi", prog_num=749) as rm_file_376_749:
                    rm_file_376_749()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX.wfi", prog_num=750) as rm_file_377_750:
                    rm_file_377_750()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX.wfi", prog_num=751) as rm_file_378_751:
                    rm_file_378_751()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX.wfi", prog_num=752) as rm_file_379_752:
                    rm_file_379_752()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DiGiGrid_IOX_micro.wfi", prog_num=753) as rm_file_380_753:
                    rm_file_380_753()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DiGiGrid_IOX_micro.wfi", prog_num=754) as rm_file_381_754:
                    rm_file_381_754()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DiGiGrid_IOX_micro.wfi", prog_num=755) as rm_file_382_755:
                    rm_file_382_755()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Cadac.wfi", prog_num=756) as rm_file_383_756:
                    rm_file_383_756()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Cadac.wfi", prog_num=757) as rm_file_384_757:
                    rm_file_384_757()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Cadac.wfi", prog_num=758) as rm_file_385_758:
                    rm_file_385_758()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex.wfi", prog_num=759) as rm_file_386_759:
                    rm_file_386_759()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex.wfi", prog_num=760) as rm_file_387_760:
                    rm_file_387_760()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex_micro.wfi", prog_num=761) as rm_file_388_761:
                    rm_file_388_761()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.9_DirectOut_Ex.wfi", prog_num=762) as rm_file_389_762:
                    rm_file_389_762()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_Ex_micro.wfi", prog_num=763) as rm_file_390_763:
                    rm_file_390_763()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DirectOut_Ex_micro.wfi", prog_num=764) as rm_file_391_764:
                    rm_file_391_764()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Calrec.wfi", prog_num=765) as rm_file_392_765:
                    rm_file_392_765()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Calrec.wfi", prog_num=766) as rm_file_393_766:
                    rm_file_393_766()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Calrec.wfi", prog_num=767) as rm_file_394_767:
                    rm_file_394_767()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH.wfi", prog_num=768) as rm_file_395_768:
                    rm_file_395_768()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB.wfi", prog_num=769) as rm_file_396_769:
                    rm_file_396_769()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH.wfi", prog_num=770) as rm_file_397_770:
                    rm_file_397_770()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB.wfi", prog_num=771) as rm_file_398_771:
                    rm_file_398_771()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH.wfi", prog_num=772) as rm_file_399_772:
                    rm_file_399_772()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB.wfi", prog_num=773) as rm_file_400_773:
                    rm_file_400_773()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_FOH_micro.wfi", prog_num=774) as rm_file_401_774:
                    rm_file_401_774()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_PV_SB_micro.wfi", prog_num=775) as rm_file_402_775:
                    rm_file_402_775()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_FOH_micro.wfi", prog_num=776) as rm_file_403_776:
                    rm_file_403_776()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_PV_SB_micro.wfi", prog_num=777) as rm_file_404_777:
                    rm_file_404_777()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_FOH_micro.wfi", prog_num=778) as rm_file_405_778:
                    rm_file_405_778()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_PV_SB_micro.wfi", prog_num=779) as rm_file_406_779:
                    rm_file_406_779()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigiCo_t2_64ch.wfi", prog_num=780) as rm_file_407_780:
                    rm_file_407_780()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_DigiCo_t2_64ch.wfi", prog_num=781) as rm_file_408_781:
                    rm_file_408_781()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigiCo_t2_64ch.wfi", prog_num=782) as rm_file_409_782:
                    rm_file_409_782()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigiCo_t2_64ch.wfi", prog_num=783) as rm_file_410_783:
                    rm_file_410_783()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Digico_SD_S6.wfi", prog_num=784) as rm_file_411_784:
                    rm_file_411_784()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_Digico_SD_S6.wfi", prog_num=785) as rm_file_412_785:
                    rm_file_412_785()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Digico_SD_S6.wfi", prog_num=786) as rm_file_413_786:
                    rm_file_413_786()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Digico_SD_S6.wfi", prog_num=787) as rm_file_414_787:
                    rm_file_414_787()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.8_Digico_SD_S6.wfi", prog_num=788) as rm_file_415_788:
                    rm_file_415_788()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Digico_SD_S6.wfi", prog_num=789) as rm_file_416_789:
                    rm_file_416_789()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Digico_SD_S6.wfi", prog_num=790) as rm_file_417_790:
                    rm_file_417_790()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DigicoDMI.wfi", prog_num=791) as rm_file_418_791:
                    rm_file_418_791()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DigicoDMI.wfi", prog_num=792) as rm_file_419_792:
                    rm_file_419_792()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DigicoDMI.wfi", prog_num=793) as rm_file_420_793:
                    rm_file_420_793()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigicoDMI.wfi", prog_num=794) as rm_file_421_794:
                    rm_file_421_794()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech.wfi", prog_num=795) as rm_file_422_795:
                    rm_file_422_795()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech.wfi", prog_num=796) as rm_file_423_796:
                    rm_file_423_796()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech.wfi", prog_num=797) as rm_file_424_797:
                    rm_file_424_797()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech.wfi", prog_num=798) as rm_file_425_798:
                    rm_file_425_798()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Heartech_64ch.wfi", prog_num=799) as rm_file_426_799:
                    rm_file_426_799()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Heartech_64ch.wfi", prog_num=800) as rm_file_427_800:
                    rm_file_427_800()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Heartech_64ch.wfi", prog_num=801) as rm_file_428_801:
                    rm_file_428_801()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Heartech_64ch.wfi", prog_num=802) as rm_file_429_802:
                    rm_file_429_802()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.12_Heartech_64ch.wfi", prog_num=803) as rm_file_430_803:
                    rm_file_430_803()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412.wfi", prog_num=804) as rm_file_431_804:
                    rm_file_431_804()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412.wfi", prog_num=805) as rm_file_432_805:
                    rm_file_432_805()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412.wfi", prog_num=806) as rm_file_433_806:
                    rm_file_433_806()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608.wfi", prog_num=807) as rm_file_434_807:
                    rm_file_434_807()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608.wfi", prog_num=808) as rm_file_435_808:
                    rm_file_435_808()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608.wfi", prog_num=809) as rm_file_436_809:
                    rm_file_436_809()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_2412_micro.wfi", prog_num=810) as rm_file_437_810:
                    rm_file_437_810()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_2412_micro.wfi", prog_num=811) as rm_file_438_811:
                    rm_file_438_811()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_2412_micro.wfi", prog_num=812) as rm_file_439_812:
                    rm_file_439_812()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_SoundStudio_STG_1608_micro.wfi", prog_num=813) as rm_file_440_813:
                    rm_file_440_813()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_SoundStudio_STG_1608_micro.wfi", prog_num=814) as rm_file_441_814:
                    rm_file_441_814()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_SoundStudio_STG_1608_micro.wfi", prog_num=815) as rm_file_442_815:
                    rm_file_442_815()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut.wfi", prog_num=816) as rm_file_443_816:
                    rm_file_443_816()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut.wfi", prog_num=817) as rm_file_444_817:
                    rm_file_444_817()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut.wfi", prog_num=818) as rm_file_445_818:
                    rm_file_445_818()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_DirectOut_micro.wfi", prog_num=819) as rm_file_446_819:
                    rm_file_446_819()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_DirectOut_micro.wfi", prog_num=820) as rm_file_447_820:
                    rm_file_447_820()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_DirectOut_micro.wfi", prog_num=821) as rm_file_448_821:
                    rm_file_448_821()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony.wfi", prog_num=822) as rm_file_449_822:
                    rm_file_449_822()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony.wfi", prog_num=823) as rm_file_450_823:
                    rm_file_450_823()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony.wfi", prog_num=824) as rm_file_451_824:
                    rm_file_451_824()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Symphony_micro.wfi", prog_num=825) as rm_file_452_825:
                    rm_file_452_825()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Symphony_micro.wfi", prog_num=826) as rm_file_453_826:
                    rm_file_453_826()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Symphony_micro.wfi", prog_num=827) as rm_file_454_827:
                    rm_file_454_827()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_BurlAudio_Bmb4.wfi", prog_num=828) as rm_file_455_828:
                    rm_file_455_828()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_BurlAudio_Bmb4.wfi", prog_num=829) as rm_file_456_829:
                    rm_file_456_829()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=830) as rm_file_457_830:
                    rm_file_457_830()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro.wfi", prog_num=831) as rm_file_458_831:
                    rm_file_458_831()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro.wfi", prog_num=832) as rm_file_459_832:
                    rm_file_459_832()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro.wfi", prog_num=833) as rm_file_460_833:
                    rm_file_460_833()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro.wfi", prog_num=834) as rm_file_461_834:
                    rm_file_461_834()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k.wfi", prog_num=835) as rm_file_462_835:
                    rm_file_462_835()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k.wfi", prog_num=836) as rm_file_463_836:
                    rm_file_463_836()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k.wfi", prog_num=837) as rm_file_464_837:
                    rm_file_464_837()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k.wfi", prog_num=838) as rm_file_465_838:
                    rm_file_465_838()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_sg1k_micro.wfi", prog_num=839) as rm_file_466_839:
                    rm_file_466_839()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_sg1k_micro.wfi", prog_num=840) as rm_file_467_840:
                    rm_file_467_840()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_sg1k_micro.wfi", prog_num=841) as rm_file_468_841:
                    rm_file_468_841()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_sg1k_micro.wfi", prog_num=842) as rm_file_469_842:
                    rm_file_469_842()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_sg1k_micro.wfi", prog_num=843) as rm_file_470_843:
                    rm_file_470_843()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Dspro_micro.wfi", prog_num=844) as rm_file_471_844:
                    rm_file_471_844()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Dspro_micro.wfi", prog_num=845) as rm_file_472_845:
                    rm_file_472_845()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.3_Dspro_micro.wfi", prog_num=846) as rm_file_473_846:
                    rm_file_473_846()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Dspro_micro.wfi", prog_num=847) as rm_file_474_847:
                    rm_file_474_847()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro_micro.wfi", prog_num=848) as rm_file_475_848:
                    rm_file_475_848()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Dspro_micro.wfi", prog_num=849) as rm_file_476_849:
                    rm_file_476_849()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.0_Joeco.wfi", prog_num=850) as rm_file_477_850:
                    rm_file_477_850()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_Joeco.wfi", prog_num=851) as rm_file_478_851:
                    rm_file_478_851()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_Joeco.wfi", prog_num=852) as rm_file_479_852:
                    rm_file_479_852()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_10.3_BR1_AVB.wfi", prog_num=853) as rm_file_480_853:
                    rm_file_480_853()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_12.1_BR1_AVB.wfi", prog_num=854) as rm_file_481_854:
                    rm_file_481_854()
                with RmFile(r"/Common/SoundGrid/Firmware/IO/IO_13.4_BR1_AVB.wfi", prog_num=855) as rm_file_482_855:
                    rm_file_482_855()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.2_X_WSG_DN32.wfi", prog_num=856) as rm_file_483_856:
                    rm_file_483_856()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_10.3_X_WSG_DN32.wfi", prog_num=857) as rm_file_484_857:
                    rm_file_484_857()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_12.1_X_WSG_DN32.wfi", prog_num=858) as rm_file_485_858:
                    rm_file_485_858()
            with Stage(r"Remove", r"Allen & Heath M s3 Firmware", prog_num=859):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_AH_s3.wfi", prog_num=860) as rm_file_486_860:
                    rm_file_486_860()
            with Stage(r"Remove", r"Allen & Heath M s6 Firmware", prog_num=861):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_AH_s6.wfi", prog_num=862) as rm_file_487_862:
                    rm_file_487_862()
            with Stage(r"Remove", r"Allen & Heath sq Firmware", prog_num=863):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_AH_sq.wfi", prog_num=864) as rm_file_488_864:
                    rm_file_488_864()
            with Stage(r"Remove", r"Allen & Heath M v3 Firmware", prog_num=865):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.12_A_H_V3.wfi", prog_num=866) as rm_file_489_866:
                    rm_file_489_866()
            with Stage(r"Remove", r"Apogee_Symphony_Firmware_13_4", prog_num=867):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Symphony.wfi", prog_num=868) as rm_file_490_868:
                    rm_file_490_868()
            with Stage(r"Remove", r"Apogee_Symphony_micro_Firmware_13_4", prog_num=869):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Symphony_micro.wfi", prog_num=870) as rm_file_491_870:
                    rm_file_491_870()
            with Stage(r"Remove", r"SoundGrid BR-1 Firmware", prog_num=871):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_BR1_AVB.wfi", prog_num=872) as rm_file_492_872:
                    rm_file_492_872()
            with Stage(r"Remove", r"Behringer Wing SoundGrid I/O Driver Firmware 14.25", prog_num=873):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.25_Behringer_WING_v2.wfi", prog_num=874) as rm_file_493_874:
                    rm_file_493_874()
            with Stage(r"Remove", r"Burl Audio BMB4 Firmware", prog_num=875):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_BurlAudio_Bmb4.wfi", prog_num=876) as rm_file_494_876:
                    rm_file_494_876()
            with Stage(r"Remove", r"Cadac_Firmware_13_4", prog_num=877):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Cadac.wfi", prog_num=878) as rm_file_495_878:
                    rm_file_495_878()
            with Stage(r"Remove", r"Calrec_Firmware_13_4", prog_num=879):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Calrec.wfi", prog_num=880) as rm_file_496_880:
                    rm_file_496_880()
            with Stage(r"Remove", r"Crest Audio Tactus Firmware", prog_num=881):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_PV_FOH.wfi", prog_num=882) as rm_file_497_882:
                    rm_file_497_882()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_PV_SB.wfi", prog_num=883) as rm_file_498_883:
                    rm_file_498_883()
            with Stage(r"Remove", r"Crest Audio Tactus micro Firmware", prog_num=884):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_PV_FOH_micro.wfi", prog_num=885) as rm_file_499_885:
                    rm_file_499_885()
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_PV_SB_micro.wfi", prog_num=886) as rm_file_500_886:
                    rm_file_500_886()
            with Stage(r"Remove", r"DigiGrid DLI Firmware", prog_num=887):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_DLI.wfi", prog_num=888) as rm_file_501_888:
                    rm_file_501_888()
            with Stage(r"Remove", r"DigiGrid DLS Firmware", prog_num=889):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_DLS.wfi", prog_num=890) as rm_file_502_890:
                    rm_file_502_890()
            with Stage(r"Remove", r"DMI_Waves_Firmware_13_7", prog_num=891):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_DigicoDMI.wfi", prog_num=892) as rm_file_503_892:
                    rm_file_503_892()
            with Stage(r"Remove", r"DN32_WSG_Firmware_13_4", prog_num=893):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_X_WSG_DN32.wfi", prog_num=894) as rm_file_504_894:
                    rm_file_504_894()
            with Stage(r"Remove", r"DSPro_SG1000_Firmware_13_6", prog_num=895):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.6_Dspro_sg1k.wfi", prog_num=896) as rm_file_505_896:
                    rm_file_505_896()
            with Stage(r"Remove", r"DSPro_SG1000_Firmware_14_25", prog_num=897):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.25_Dspro_sg1k_v2.wfi", prog_num=898) as rm_file_506_898:
                    rm_file_506_898()
            with Stage(r"Remove", r"DSPro_SG1000_micro_Firmware_15_1", prog_num=899):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.1_Dspro_sg1k_micro.wfi", prog_num=900) as rm_file_507_900:
                    rm_file_507_900()
            with Stage(r"Remove", r"DSPro_SG1000_micro_V2_Firmware_15_1", prog_num=901):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.1_Dspro_sg1k_v2_micro.wfi", prog_num=902) as rm_file_508_902:
                    rm_file_508_902()
            with Stage(r"Remove", r"DSPro SG4000 Firmware", prog_num=903):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.5_Dspro.wfi", prog_num=904) as rm_file_509_904:
                    rm_file_509_904()
            with Stage(r"Remove", r"DSPro SG4000 v2 Firmware", prog_num=905):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.26_Dspro_sg4k_v2.wfi", prog_num=906) as rm_file_510_906:
                    rm_file_510_906()
            with Stage(r"Remove", r"DSPro SG4000 v2 micro Firmware V14.25", prog_num=907):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.25_Dspro_sg4k_v2_micro.wfi", prog_num=908) as rm_file_511_908:
                    rm_file_511_908()
            with Stage(r"Remove", r"DSPro SG4000 micro Firmware", prog_num=909):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.2_Dspro_micro.wfi", prog_num=910) as rm_file_512_910:
                    rm_file_512_910()
            with Stage(r"Remove", r"DSPro SG4000 v2 micro Firmware", prog_num=911):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.2_Dspro_sg4k_v2_micro.wfi", prog_num=912) as rm_file_513_912:
                    rm_file_513_912()
            with Stage(r"Remove", r"DiGiGrid D Firmware V13.4", prog_num=913):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigiGridD.wfi", prog_num=914) as rm_file_514_914:
                    rm_file_514_914()
            with Stage(r"Remove", r"DiGiGrid_M_Driver_Firmware_13_4", prog_num=915):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigiGridM.wfi", prog_num=916) as rm_file_515_916:
                    rm_file_515_916()
            with Stage(r"Remove", r"DiGiGrid Q Firmware V13.4", prog_num=917):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigiGridQ.wfi", prog_num=918) as rm_file_516_918:
                    rm_file_516_918()
            with Stage(r"Remove", r"Digico SD card V13.4", prog_num=919):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DigiCo_t2_64ch.wfi", prog_num=920) as rm_file_517_920:
                    rm_file_517_920()
            with Stage(r"Remove", r"Digico SD Firmware", prog_num=921):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.21_Digico_SD_S6.wfi", prog_num=922) as rm_file_518_922:
                    rm_file_518_922()
            with Stage(r"Remove", r"DirectOut Exbox Micro SoundGrid I/O Driver Firmware", prog_num=923):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.22_DirectOut_Ex_micro.wfi", prog_num=924) as rm_file_519_924:
                    rm_file_519_924()
            with Stage(r"Remove", r"DirectOut Exbox v2 SoundGrid I/O Driver Firmware", prog_num=925):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.25_DirectOut_Ex_v2.wfi", prog_num=926) as rm_file_520_926:
                    rm_file_520_926()
            with Stage(r"Remove", r"DirectOut Exbox v2 Micro SoundGrid I/O Driver Firmware", prog_num=927):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.25_DirectOut_Ex_v2_micro.wfi", prog_num=928) as rm_file_521_928:
                    rm_file_521_928()
            with Stage(r"Remove", r"DirectOut Exbox SoundGrid I/O Driver Firmware", prog_num=929):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.18_DirectOut_Ex.wfi", prog_num=930) as rm_file_522_930:
                    rm_file_522_930()
            with Stage(r"Remove", r"DirectOut_SG_MADI_Firmware_13_4", prog_num=931):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut.wfi", prog_num=932) as rm_file_523_932:
                    rm_file_523_932()
            with Stage(r"Remove", r"DirectOut_SG_MADI_micro_Firmware_13_4", prog_num=933):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DirectOut_micro.wfi", prog_num=934) as rm_file_524_934:
                    rm_file_524_934()
            with Stage(r"Remove", r"DirectOut SoundGrid I/O Driver Firmware", prog_num=935):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.18_Directout_sgio.wfi", prog_num=936) as rm_file_525_936:
                    rm_file_525_936()
            with Stage(r"Remove", r"HearBack Pro Firmware", prog_num=937):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Heartech.wfi", prog_num=938) as rm_file_526_938:
                    rm_file_526_938()
            with Stage(r"Remove", r"HearBack Pro V2 Firmware", prog_num=939):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.7_Heartech_32ch.wfi", prog_num=940) as rm_file_527_940:
                    rm_file_527_940()
            with Stage(r"Remove", r"HearTech SG Bridge Firmware", prog_num=941):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.1_Heartech_64ch.wfi", prog_num=942) as rm_file_528_942:
                    rm_file_528_942()
            with Stage(r"Remove", r"HearTech SG Bridge Firmware v2", prog_num=943):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_15.1_Heartech_64ch_v2.wfi", prog_num=944) as rm_file_529_944:
                    rm_file_529_944()
            with Stage(r"Remove", r"DigiGrid IOC Firmware", prog_num=945):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOC.wfi", prog_num=946) as rm_file_530_946:
                    rm_file_530_946()
            with Stage(r"Remove", r"DigiGrid IOC micro Firmware", prog_num=947):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOC_micro.wfi", prog_num=948) as rm_file_531_948:
                    rm_file_531_948()
            with Stage(r"Remove", r"IONIC16_Firmware_S25", prog_num=949):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.29_IONIC16_S25.wfi", prog_num=950) as rm_file_532_950:
                    rm_file_532_950()
            with Stage(r"Remove", r"IONIC16_Firmware_S50", prog_num=951):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.30_IONIC16_S50.wfi", prog_num=952) as rm_file_533_952:
                    rm_file_533_952()
            with Stage(r"Remove", r"DigiGrid IOS Firmware", prog_num=953):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOS.wfi", prog_num=954) as rm_file_534_954:
                    rm_file_534_954()
            with Stage(r"Remove", r"DigiGrid IOS-XL Firmware", prog_num=955):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOS_XL.wfi", prog_num=956) as rm_file_535_956:
                    rm_file_535_956()
            with Stage(r"Remove", r"DigiGrid IOS-XL micro Firmware", prog_num=957):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOS_XL_micro.wfi", prog_num=958) as rm_file_536_958:
                    rm_file_536_958()
            with Stage(r"Remove", r"DigiGrid IOS micro Firmware", prog_num=959):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOS_micro.wfi", prog_num=960) as rm_file_537_960:
                    rm_file_537_960()
            with Stage(r"Remove", r"DigiGrid IOX Firmware", prog_num=961):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOX.wfi", prog_num=962) as rm_file_538_962:
                    rm_file_538_962()
            with Stage(r"Remove", r"DigiGrid IOX micro Firmware", prog_num=963):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_IOX_micro.wfi", prog_num=964) as rm_file_539_964:
                    rm_file_539_964()
            with Stage(r"Remove", r"JoeCo_Firmware_13_4", prog_num=965):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Joeco.wfi", prog_num=966) as rm_file_540_966:
                    rm_file_540_966()
            with Stage(r"Remove", r"DigiGrid MGB Firmware", prog_num=967):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_MGB.wfi", prog_num=968) as rm_file_541_968:
                    rm_file_541_968()
            with Stage(r"Remove", r"DigiGrid MGO Firmware", prog_num=969):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_DiGiGrid_MGO.wfi", prog_num=970) as rm_file_542_970:
                    rm_file_542_970()
            with Stage(r"Remove", r"SoundStudio STG-1608 Firmware", prog_num=971):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_SoundStudio_STG_1608.wfi", prog_num=972) as rm_file_543_972:
                    rm_file_543_972()
            with Stage(r"Remove", r"SoundStudio STG-1608 micro Firmware V13.4", prog_num=973):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_SoundStudio_STG_1608_micro.wfi", prog_num=974) as rm_file_544_974:
                    rm_file_544_974()
            with Stage(r"Remove", r"SoundStudio STG-2412 Firmware", prog_num=975):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_SoundStudio_STG_2412.wfi", prog_num=976) as rm_file_545_976:
                    rm_file_545_976()
            with Stage(r"Remove", r"SoundStudio STG-2412 micro Firmware V13.4", prog_num=977):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_SoundStudio_STG_2412_micro.wfi", prog_num=978) as rm_file_546_978:
                    rm_file_546_978()
            with Stage(r"Remove", r"X-WSG_s6_Firmware_13_4", prog_num=979):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_X_WSG.wfi", prog_num=980) as rm_file_547_980:
                    rm_file_547_980()
            with Stage(r"Remove", r"WSG Y-16 s3 Firmware", prog_num=981):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_yamaha_s3.wfi", prog_num=982) as rm_file_548_982:
                    rm_file_548_982()
            with Stage(r"Remove", r"WSG Y-16 s6 Firmware", prog_num=983):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_yamaha_s6.wfi", prog_num=984) as rm_file_549_984:
                    rm_file_549_984()
            with Stage(r"Remove", r"WSG Y-16 v3 Firmware", prog_num=985):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.21_MY16_v3.wfi", prog_num=986) as rm_file_550_986:
                    rm_file_550_986()
            with Stage(r"Remove", r"Yamaha HY128 v2 Firmware", prog_num=987):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_14.13_HY_v2.wfi", prog_num=988) as rm_file_551_988:
                    rm_file_551_988()
            with Stage(r"Remove", r"Yamaha WSG-HY128 Firmware", prog_num=989):
                with RmFile(r"/Library/Application Support/Waves/SoundGrid Firmware/IO/IO_13.4_Hy.wfi", prog_num=990) as rm_file_552_990:
                    rm_file_552_990()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves/RemoteServices", prog_num=991):
            with Stage(r"Remove", r"MyRemote", prog_num=992):
                with RmDir(r"//Library/Application Support/Waves/RemoteServices/MyMonService.bundle", prog_num=993) as rm_dir_553_993:
                    rm_dir_553_993()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves/MyMon", prog_num=994):
            with Stage(r"Remove", r"MyRemote", prog_num=995):
                with RmDir(r"//Library/Application Support/Waves/MyMon/MyMonService.bundle", prog_num=996) as rm_dir_554_996:
                    rm_dir_554_996()
        with Stage(r"Remove from folder", r"/Library/Application Support/Waves", prog_num=997):
            with Stage(r"Remove", r"Qt libraries 5.12.8", prog_num=998):
                with RmDir(r"//Library/Application Support/Waves/WavesQtLibs_5.12.8", prog_num=999) as rm_dir_555_999:
                    rm_dir_555_999()
            with Stage(r"Remove", r"QT_5_5_1_FOR_IO_MODULES", prog_num=1000):
                with RmDir(r"//Library/Application Support/Waves/WavesQtLibs_5.5.1", prog_num=1001) as rm_dir_556_1001:
                    rm_dir_556_1001()
            with Stage(r"Remove", r"Qt libraries 6.2.4", prog_num=1002):
                with RmDir(r"//Library/Application Support/Waves/WavesQtLibs_6.2.4", prog_num=1003) as rm_dir_557_1003:
                    rm_dir_557_1003()
        with Stage(r"Remove from folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=1004):
            with Stage(r"Remove", r"WaveShell1-AAX 14.12", prog_num=1005):
                with RmDir(r"//Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 14.12.aaxplugin", prog_num=1006) as rm_dir_558_1006:
                    rm_dir_558_1006()
        with Stage(r"Remove from folder", r"/Applications/Waves/WaveShells V14", prog_num=1007):
            with Stage(r"Remove", r"WaveShell1-AAX 14.12", prog_num=1008):
                with RmDir(r"//Applications/Waves/WaveShells V14/WaveShell1-AAX 14.12.aaxplugin", prog_num=1009) as rm_dir_559_1009:
                    rm_dir_559_1009()
            with Stage(r"Remove", r"WaveShell1-AU 14.12", prog_num=1010):
                with RmDir(r"//Applications/Waves/WaveShells V14/WaveShell1-AU 14.12.component", prog_num=1011) as rm_dir_560_1011:
                    rm_dir_560_1011()
            with Stage(r"Remove", r"WaveShell1-VST 14.12", prog_num=1012):
                with RmDir(r"//Applications/Waves/WaveShells V14/WaveShell1-VST 14.12.vst", prog_num=1013) as rm_dir_561_1013:
                    rm_dir_561_1013()
            with Stage(r"Remove", r"WaveShell1-VST3 14.12", prog_num=1014):
                with RmDir(r"//Applications/Waves/WaveShells V14/WaveShell1-VST3 14.12.vst3", prog_num=1015) as rm_dir_562_1015:
                    rm_dir_562_1015()
            with Stage(r"Remove", r"WaveShell1-WPAPI_2 14.12", prog_num=1016):
                with RmDir(r"//Applications/Waves/WaveShells V14/WaveShell1-WPAPI_2 14.12.bundle", prog_num=1017) as rm_dir_563_1017:
                    rm_dir_563_1017()
        with Stage(r"Remove from folder", r"/Applications/Waves/SoundGrid/Utilities", prog_num=1018):
            with Cd(r"/Applications/Waves/SoundGrid/Utilities", prog_num=1019) as cd_564_1019:
                cd_564_1019()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid/Utilities", prog_num=1020)()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriver.pkg", prog_num=1021) as rm_file_565_1021:
                    rm_file_565_1021()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV10.pkg", prog_num=1022) as rm_file_566_1022:
                    rm_file_566_1022()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.pkg", prog_num=1023) as rm_file_567_1023:
                    rm_file_567_1023()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.2.pkg", prog_num=1024) as rm_file_568_1024:
                    rm_file_568_1024()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV11.3.pkg", prog_num=1025) as rm_file_569_1025:
                    rm_file_569_1025()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV12.2.pkg", prog_num=1026) as rm_file_570_1026:
                    rm_file_570_1026()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV12.8.pkg", prog_num=1027) as rm_file_571_1027:
                    rm_file_571_1027()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV13.3.pkg", prog_num=1028) as rm_file_572_1028:
                    rm_file_572_1028()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.5.pkg", prog_num=1029) as rm_file_573_1029:
                    rm_file_573_1029()
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.9.pkg", prog_num=1030) as rm_file_574_1030:
                    rm_file_574_1030()
            with ShellCommand(r'"/Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app/Contents/MacOS/SoundGridDriverUninstaller.py"', message=r"Uninstalling SoundGrid Driver", ignore_all_errors=True, prog_num=1031) as shell_command_575_1031:
                shell_command_575_1031()
            with Stage(r"Remove", r"JoeCo BBSG24MP utilities", prog_num=1032):
                with RmDir(r"//Applications/Waves/SoundGrid/Utilities/JoeCo", prog_num=1033) as rm_dir_576_1033:
                    rm_dir_576_1033()
            with Stage(r"Remove", r"SoundGrid Control Panel Uninstaller", prog_num=1034):
                with RmDir(r"//Applications/Waves/SoundGrid/Utilities/SoundGrid Driver Uninstaller.app", prog_num=1035) as rm_dir_577_1035:
                    rm_dir_577_1035()
            with Stage(r"Remove", r"SoundGrid V14 ASIO / Core Audio Rec/PB Control Panel", prog_num=1036):
                with RmFile(r"/Applications/Waves/SoundGrid/Utilities/SoundGridDriverV14.12.pkg", prog_num=1037) as rm_file_578_1037:
                    rm_file_578_1037()
        with Stage(r"Remove from folder", r"/Applications/Waves/SoundGrid/Documents", prog_num=1038):
            with Cd(r"/Applications/Waves/SoundGrid/Documents", prog_num=1039) as cd_579_1039:
                cd_579_1039()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid/Documents", prog_num=1040)()
                with RmFile(r"/Common/SoundGrid/Documents/yamaha-wsg-y16-manual.pdf", prog_num=1041) as rm_file_580_1041:
                    rm_file_580_1041()
                with RmFile(r"/Common/SoundGrid/Documents/Digico SD Waves Card User Guide.pdf", prog_num=1042) as rm_file_581_1042:
                    rm_file_581_1042()
            with Stage(r"Remove", r"A-H_M_Documents", prog_num=1043):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/A-H M-Waves User Guide.pdf", prog_num=1044) as rm_file_582_1044:
                    rm_file_582_1044()
            with Stage(r"Remove", r"Apogee Symphony pdf", prog_num=1045):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Apogee Symphony MKII SoundGrid User Guide.pdf", prog_num=1046) as rm_file_583_1046:
                    rm_file_583_1046()
            with Stage(r"Remove", r"SG BR1 pdf", prog_num=1047):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/SG BR1.pdf", prog_num=1048) as rm_file_584_1048:
                    rm_file_584_1048()
            with Stage(r"Remove", r"Burl BMB4 pdf", prog_num=1049):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Burl Audio_B16-BMB4_Mothership_User_Guide.pdf", prog_num=1050) as rm_file_585_1050:
                    rm_file_585_1050()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Burl Audio_B80-BMB4_Mothership_User_Guide.pdf", prog_num=1051) as rm_file_586_1051:
                    rm_file_586_1051()
            with Stage(r"Remove", r"Cadac pdf", prog_num=1052):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Cadac SG User Guide.pdf", prog_num=1053) as rm_file_587_1053:
                    rm_file_587_1053()
            with Stage(r"Remove", r"Calrec pdf", prog_num=1054):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Calrec SoundGrid IO User Guide.pdf", prog_num=1055) as rm_file_588_1055:
                    rm_file_588_1055()
            with Stage(r"Remove", r"Crest Tactus pdf", prog_num=1056):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Tactus FOH OM.pdf", prog_num=1057) as rm_file_589_1057:
                    rm_file_589_1057()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Tactus Stage OM.pdf", prog_num=1058) as rm_file_590_1058:
                    rm_file_590_1058()
            with Stage(r"Remove", r"DLI DLS pdf", prog_num=1059):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DLI DLS User Guide.pdf", prog_num=1060) as rm_file_591_1060:
                    rm_file_591_1060()
            with Stage(r"Remove", r"DMI Waves pdf", prog_num=1061):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DMI Waves User Guide.pdf", prog_num=1062) as rm_file_592_1062:
                    rm_file_592_1062()
            with Stage(r"Remove", r"DN32-WSG pdf", prog_num=1063):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DN32-WSG Quick Start Guide.pdf", prog_num=1064) as rm_file_593_1064:
                    rm_file_593_1064()
            with Stage(r"Remove", r"DSPro SG4000 pdf", prog_num=1065):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/STAGEGRID 1000 User Guide.pdf", prog_num=1066) as rm_file_594_1066:
                    rm_file_594_1066()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/STAGEGRID 4000 User Guide.pdf", prog_num=1067) as rm_file_595_1067:
                    rm_file_595_1067()
            with Stage(r"Remove", r"DiGiGrid D Driver pdf", prog_num=1068):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiGrid D User Guide.pdf", prog_num=1069) as rm_file_596_1069:
                    rm_file_596_1069()
            with Stage(r"Remove", r"DiGiGrid M Driver pdf", prog_num=1070):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiGrid M User Guide.pdf", prog_num=1071) as rm_file_597_1071:
                    rm_file_597_1071()
            with Stage(r"Remove", r"DiGiGrid Q Driver pdf", prog_num=1072):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiGrid Q User Guide.pdf", prog_num=1073) as rm_file_598_1073:
                    rm_file_598_1073()
            with Stage(r"Remove", r"DigiGrid S", prog_num=1074):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiGrid S User Guide.pdf", prog_num=1075) as rm_file_599_1075:
                    rm_file_599_1075()
            with Stage(r"Remove", r"Digico SD card pdf", prog_num=1076):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiCo SD SoundGrid IO User Guide.pdf", prog_num=1077) as rm_file_600_1077:
                    rm_file_600_1077()
            with Stage(r"Remove", r"DirectOut Exbox SoundGrid IO Driver", prog_num=1078):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DirectOut Exbox.SG User Guide.pdf", prog_num=1079) as rm_file_601_1079:
                    rm_file_601_1079()
            with Stage(r"Remove", r"DirectOut SG.MADI pdf", prog_num=1080):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DirectOut SG.MADI User Guide.pdf", prog_num=1081) as rm_file_602_1081:
                    rm_file_602_1081()
            with Stage(r"Remove", r"DirectOut SoundGrid IO Driver Documents", prog_num=1082):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DirectOut SG.IO User Guide.pdf", prog_num=1083) as rm_file_603_1083:
                    rm_file_603_1083()
            with Stage(r"Remove", r"Hear Back pdf", prog_num=1084):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Hear Back PRO SG Card User Guide.pdf", prog_num=1085) as rm_file_604_1085:
                    rm_file_604_1085()
            with Stage(r"Remove", r"HearTech pdf", prog_num=1086):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/Hear Technologies SoundGrid Bridge User Guide.pdf", prog_num=1087) as rm_file_605_1087:
                    rm_file_605_1087()
            with Stage(r"Remove", r"IOC pdf", prog_num=1088):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/IOC User Guide.pdf", prog_num=1089) as rm_file_606_1089:
                    rm_file_606_1089()
            with Stage(r"Remove", r"IONIC pdf", prog_num=1090):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/IONIC 16 User Guide.pdf", prog_num=1091) as rm_file_607_1091:
                    rm_file_607_1091()
            with Stage(r"Remove", r"IOS pdf", prog_num=1092):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/IOS User Guide.pdf", prog_num=1093) as rm_file_608_1093:
                    rm_file_608_1093()
            with Stage(r"Remove", r"IOS-XL pdf", prog_num=1094):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/IOS-XL User Guide.pdf", prog_num=1095) as rm_file_609_1095:
                    rm_file_609_1095()
            with Stage(r"Remove", r"IOX pdf", prog_num=1096):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/IOX User Guide.pdf", prog_num=1097) as rm_file_610_1097:
                    rm_file_610_1097()
            with Stage(r"Remove", r"JoeCo BBSG24MP pdf", prog_num=1098):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/JoeCo BBSG24MP User Guide.pdf", prog_num=1099) as rm_file_611_1099:
                    rm_file_611_1099()
            with Stage(r"Remove", r"MGB MGO pdf", prog_num=1100):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/DiGiGrid MGR User Guide.pdf", prog_num=1101) as rm_file_612_1101:
                    rm_file_612_1101()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/MGB MGO User Guide.pdf", prog_num=1102) as rm_file_613_1102:
                    rm_file_613_1102()
            with Stage(r"Remove", r"SG Driver pdf", prog_num=1103):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/SG Driver.pdf", prog_num=1104) as rm_file_614_1104:
                    rm_file_614_1104()
            with Stage(r"Remove", r"SoundStudio STG-2412 pdf", prog_num=1105):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/STG-1608 User Guide.pdf", prog_num=1106) as rm_file_615_1106:
                    rm_file_615_1106()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/STG-2412 User Guide.pdf", prog_num=1107) as rm_file_616_1107:
                    rm_file_616_1107()
            with Stage(r"Remove", r"X-WSG pdf", prog_num=1108):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/X-WSG Quick Start Guide.pdf", prog_num=1109) as rm_file_617_1109:
                    rm_file_617_1109()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/X-WSG User Guide.pdf", prog_num=1110) as rm_file_618_1110:
                    rm_file_618_1110()
            with Stage(r"Remove", r"Y-16_Documents", prog_num=1111):
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/WSG-HY128 User Guide.pdf", prog_num=1112) as rm_file_619_1112:
                    rm_file_619_1112()
                with RmFile(r"/Applications/Waves/SoundGrid/Documents/WSG-Y16 User Guide.pdf", prog_num=1113) as rm_file_620_1113:
                    rm_file_620_1113()
        with Stage(r"Remove from folder", r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=1114):
            with Cd(r"/Applications/Waves/SoundGrid Studio/Modules", prog_num=1115) as cd_621_1115:
                cd_621_1115()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid Studio/Modules", prog_num=1116)()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/StudioRack.bundle", prog_num=1117) as rm_dir_622_1117:
                    rm_dir_622_1117()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/Overview.bundle", prog_num=1118) as rm_dir_623_1118:
                    rm_dir_623_1118()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-Track.bundle", prog_num=1119) as rm_dir_624_1119:
                    rm_dir_624_1119()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/StudioRackLib_9.7.framework", prog_num=1120) as rm_dir_625_1120:
                    rm_dir_625_1120()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackLib_9.7.framework", prog_num=1121) as rm_dir_626_1121:
                    rm_dir_626_1121()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackLib_11.0.framework", prog_num=1122) as rm_dir_627_1122:
                    rm_dir_627_1122()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewLib_9.7.framework", prog_num=1123) as rm_dir_628_1123:
                    rm_dir_628_1123()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_11.0.framework", prog_num=1124) as rm_dir_629_1124:
                    rm_dir_629_1124()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_11.0.framework", prog_num=1125) as rm_dir_630_1125:
                    rm_dir_630_1125()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_11.0.framework", prog_num=1126) as rm_dir_631_1126:
                    rm_dir_631_1126()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_12.4.framework", prog_num=1127) as rm_dir_632_1127:
                    rm_dir_632_1127()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_12.4.framework", prog_num=1128) as rm_dir_633_1128:
                    rm_dir_633_1128()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_12.4.framework", prog_num=1129) as rm_dir_634_1129:
                    rm_dir_634_1129()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_12.8.framework", prog_num=1130) as rm_dir_635_1130:
                    rm_dir_635_1130()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_12.8.framework", prog_num=1131) as rm_dir_636_1131:
                    rm_dir_636_1131()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_12.8.framework", prog_num=1132) as rm_dir_637_1132:
                    rm_dir_637_1132()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_13.3.framework", prog_num=1133) as rm_dir_638_1133:
                    rm_dir_638_1133()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_13.3.framework", prog_num=1134) as rm_dir_639_1134:
                    rm_dir_639_1134()
                with RmDir(r"/Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_13.3.framework", prog_num=1135) as rm_dir_640_1135:
                    rm_dir_640_1135()
            with Stage(r"Remove", r"SoundGrid Studio Modules", prog_num=1136):
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/ControlRoom.bundle", prog_num=1137) as rm_dir_641_1137:
                    rm_dir_641_1137()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/ControlRoomLib_14.9.framework", prog_num=1138) as rm_dir_642_1138:
                    rm_dir_642_1138()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGST.bundle", prog_num=1139) as rm_dir_643_1139:
                    rm_dir_643_1139()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/EMO-TrackSGSTLib_14.9.framework", prog_num=1140) as rm_dir_644_1140:
                    rm_dir_644_1140()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/MIDICommunication.framework", prog_num=1141) as rm_dir_645_1141:
                    rm_dir_645_1141()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/Mackie_Control.bundle", prog_num=1142) as rm_dir_646_1142:
                    rm_dir_646_1142()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/MiDiPLUS_Control.bundle", prog_num=1143) as rm_dir_647_1143:
                    rm_dir_647_1143()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/MixerController_MyMon_Control.bundle", prog_num=1144) as rm_dir_648_1144:
                    rm_dir_648_1144()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/OverviewSGST.bundle", prog_num=1145) as rm_dir_649_1145:
                    rm_dir_649_1145()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/OverviewSGSTLib_14.9.framework", prog_num=1146) as rm_dir_650_1146:
                    rm_dir_650_1146()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/StudioRack_Control.bundle", prog_num=1147) as rm_dir_651_1147:
                    rm_dir_651_1147()
                with RmDir(r"//Applications/Waves/SoundGrid Studio/Modules/SurfaceDriver_App.bundle", prog_num=1148) as rm_dir_652_1148:
                    rm_dir_652_1148()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Modules/com.WavesAudio.SoundGridStudioSilent.plist", prog_num=1149) as rm_file_653_1149:
                    rm_file_653_1149()
            with RmSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves SG Studio Modules", prog_num=1150) as rm_symlink_654_1150:
                rm_symlink_654_1150()
            with RmSymlink(r"/Users/Shared/Waves/Waves SG Studio Modules", prog_num=1151) as rm_symlink_655_1151:
                rm_symlink_655_1151()
        with Stage(r"Remove from folder", r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=1152):
            with Cd(r"/Applications/Waves/SoundGrid Studio/Documents", prog_num=1153) as cd_656_1153:
                cd_656_1153()
                Progress(r"remove previous versions /Applications/Waves/SoundGrid Studio/Documents", prog_num=1154)()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/eMotionST.pdf", prog_num=1155) as rm_file_657_1155:
                    rm_file_657_1155()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/StudioRack.pdf", prog_num=1156) as rm_file_658_1156:
                    rm_file_658_1156()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/SGST_QUICKSTART.mp4", prog_num=1157) as rm_file_659_1157:
                    rm_file_659_1157()
            with Stage(r"Remove", r"SoundGrid Studio Documents", prog_num=1158):
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/DiGiGrid S User Guide.pdf", prog_num=1159) as rm_file_660_1159:
                    rm_file_660_1159()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/SGS_QUICKSTART.mp4", prog_num=1160) as rm_file_661_1160:
                    rm_file_661_1160()
                with RmFile(r"/Applications/Waves/SoundGrid Studio/Documents/SGStudio.pdf", prog_num=1161) as rm_file_662_1161:
                    rm_file_662_1161()
        with Stage(r"Remove from folder", r"/Applications/Waves/SoundGrid Studio", prog_num=1162):
            with Stage(r"Remove", r"SoundGrid Studio V11", prog_num=1163):
                with RmDir(r"//Applications/Waves/SoundGrid Studio/SoundGrid Studio.app", prog_num=1164) as rm_dir_663_1164:
                    rm_dir_663_1164()
        with Stage(r"Remove from folder", r"/Applications/Waves/Plug-Ins V14", prog_num=1165):
            with Stage(r"Remove", r"Insert", prog_num=1166):
                with RmDir(r"//Applications/Waves/Plug-Ins V14/Insert.bundle", prog_num=1167) as rm_dir_664_1167:
                    rm_dir_664_1167()
            with Stage(r"Remove", r"WavesLib1_14_12_90_381", prog_num=1168):
                with RmDir(r"//Applications/Waves/Plug-Ins V14/WavesLib1_14.12.90.framework", prog_num=1169) as rm_dir_665_1169:
                    rm_dir_665_1169()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=1170) as rm_file_or_dir_666_1170:
            rm_file_or_dir_666_1170()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack and Network Streaming with HD-HDX-HDNative - external Server.emo", prog_num=1171) as rm_file_or_dir_667_1171:
            rm_file_or_dir_667_1171()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - IO - StudioRack Processing for HD-HDX-HDNative Systems - external Server.emo", prog_num=1172) as rm_file_or_dir_668_1172:
            rm_file_or_dir_668_1172()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Mixing with StudioRack - external Server.emo", prog_num=1173) as rm_file_or_dir_669_1173:
            rm_file_or_dir_669_1173()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - Recording thru eMotion Mixer - external Server.emo", prog_num=1174) as rm_file_or_dir_670_1174:
            rm_file_or_dir_670_1174()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and External Mixing  - external Server.emo", prog_num=1175) as rm_file_or_dir_671_1175:
            rm_file_or_dir_671_1175()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLI - SGP - StudioRack Processing and Monitoring - external Server.emo", prog_num=1176) as rm_file_or_dir_672_1176:
            rm_file_or_dir_672_1176()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - Network Streaming with HD-HDX-HDNative.emo", prog_num=1177) as rm_file_or_dir_673_1177:
            rm_file_or_dir_673_1177()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack and Network Streaming with HD-HDX-HDNative.emo", prog_num=1178) as rm_file_or_dir_674_1178:
            rm_file_or_dir_674_1178()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - IO - StudioRack Processing for HD-HDX-HDNative Systems.emo", prog_num=1179) as rm_file_or_dir_675_1179:
            rm_file_or_dir_675_1179()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Mixing with StudioRack.emo", prog_num=1180) as rm_file_or_dir_676_1180:
            rm_file_or_dir_676_1180()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - Recording thru eMotion Mixer.emo", prog_num=1181) as rm_file_or_dir_677_1181:
            rm_file_or_dir_677_1181()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and External Mixing.emo", prog_num=1182) as rm_file_or_dir_678_1182:
            rm_file_or_dir_678_1182()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS - SGP - StudioRack Processing and Monitoring.emo", prog_num=1183) as rm_file_or_dir_679_1183:
            rm_file_or_dir_679_1183()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/DLS DLI REC-PB Standalone.emo", prog_num=1184) as rm_file_or_dir_680_1184:
            rm_file_or_dir_680_1184()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - Recording thru eMotion Mixer.emo", prog_num=1185) as rm_file_or_dir_681_1185:
            rm_file_or_dir_681_1185()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - REC-PB Standalone.emo", prog_num=1186) as rm_file_or_dir_682_1186:
            rm_file_or_dir_682_1186()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOS - StudioRack Processing and Monitoring.emo", prog_num=1187) as rm_file_or_dir_683_1187:
            rm_file_or_dir_683_1187()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - Recording thru eMotion Mixer - external Server.emo", prog_num=1188) as rm_file_or_dir_684_1188:
            rm_file_or_dir_684_1188()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - REC-PB Standalone.emo", prog_num=1189) as rm_file_or_dir_685_1189:
            rm_file_or_dir_685_1189()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/IOX - StudioRack Processing and Monitoring - external Server.emo", prog_num=1190) as rm_file_or_dir_686_1190:
            rm_file_or_dir_686_1190()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/MGB MGO REC-PB Standalone.emo", prog_num=1191) as rm_file_or_dir_687_1191:
            rm_file_or_dir_687_1191()
        with RmFileOrDir(r"/Users/Shared/Waves/eMotion/Templates/2x MGB MGO REC-PB 96Khz Standalone.emo", prog_num=1192) as rm_file_or_dir_688_1192:
            rm_file_or_dir_688_1192()
        with RemoveEmptyFolders(r"/Applications/Waves/SoundGrid", prog_num=1193) as remove_empty_folders_689_1193:
            remove_empty_folders_689_1193()
        with RmGlobs(r"/Applications/Waves/SoundGrid Studio", r"*.bundle", r"*.dll", r"*.framework", prog_num=1194) as rm_globs_690_1194:
            rm_globs_690_1194()
        with RemoveEmptyFolders(r"/Applications/Waves/SoundGrid Studio", prog_num=1195) as remove_empty_folders_691_1195:
            remove_empty_folders_691_1195()
        with RemoveEmptyFolders(r"/Applications/Waves", prog_num=1196) as remove_empty_folders_692_1196:
            remove_empty_folders_692_1196()
        with RemoveEmptyFolders(r"/Library/Application Support/Waves", prog_num=1197) as remove_empty_folders_693_1197:
            remove_empty_folders_693_1197()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1198) as chmod_694_1198:
            chmod_694_1198()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1199) as chmod_695_1199:
            chmod_695_1199()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/require.yaml", r"/Library/Application Support/Waves/Central/V14/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1200) as copy_file_to_file_696_1200:
            copy_file_to_file_696_1200()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1201) as chmod_697_1201:
            chmod_697_1201()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V14/new_require.yaml", r"/Library/Application Support/Waves/Central/V14/require.yaml", hard_links=False, copy_owner=True, prog_num=1202) as copy_file_to_file_698_1202:
            copy_file_to_file_698_1202()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V14/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=1203) as chmod_699_1203:
            chmod_699_1203()

with Stage(r"epilog", prog_num=1204):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/uninstall/uninstall_14-20250120135552.py", prog_num=1205) as patch_py_batch_with_timings_700_1205:
        patch_py_batch_with_timings_700_1205()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


