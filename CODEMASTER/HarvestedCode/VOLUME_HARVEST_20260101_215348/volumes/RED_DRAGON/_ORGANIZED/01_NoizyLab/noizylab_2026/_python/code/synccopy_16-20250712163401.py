# Creation time: 12-07-25_16-34
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 4862
PythonBatchCommandBase.running_progress = 567
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=568):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250712163401"
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
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 8
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MjM4ODQ0Mn0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUyMzUyMTQyfX19XX0_;CloudFront-Signature=FS5uQYxFL4g58xsDGh4D56BEJA0LFDgvQ6cfw1ug~90En5j~TIBsa5zNeJzEHBZMfGAJ9fH6gxuirDcrGoHsNYrv3ZMJ-DrR87Kz7IdnOcqAnmzECA-SgBzThJ1N-WShrumvtOXg-XNZkQicH0sYuDZRjVx9l2pgSHr521IPemNB~lCo7l3o~0p3BicaK5aEtf9ylfYHBZnBpB~9lyK-4J~umaJ3R6oJGhWXQujcH2p3Ix5A6Cs5WQLzjiYBa0SdiRX6iLF1XA5oR2XAjIfphc-LfwMtGp2SQirw2fi~OjO5Kahx3epLMVYLE65O3DDhlPh400ml5aWs5mN6I35Q7Q__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MjM4ODQ0Mn0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUyMzUyMTQyfX19XX0_;CloudFront-Signature=FS5uQYxFL4g58xsDGh4D56BEJA0LFDgvQ6cfw1ug~90En5j~TIBsa5zNeJzEHBZMfGAJ9fH6gxuirDcrGoHsNYrv3ZMJ-DrR87Kz7IdnOcqAnmzECA-SgBzThJ1N-WShrumvtOXg-XNZkQicH0sYuDZRjVx9l2pgSHr521IPemNB~lCo7l3o~0p3BicaK5aEtf9ylfYHBZnBpB~9lyK-4J~umaJ3R6oJGhWXQujcH2p3Ix5A6Cs5WQLzjiYBa0SdiRX6iLF1XA5oR2XAjIfphc-LfwMtGp2SQirw2fi~OjO5Kahx3epLMVYLE65O3DDhlPh400ml5aWs5mN6I35Q7Q__"
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
    config_vars['INDEX_CHECKSUM'] = r"98ba0fa689fb4a468e6c0f5b003673b24187a084"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/08/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"70d8c459014cfb2e16311bea315c82ee2726d01f"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/08/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/08/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = r"__UPDATE_INSTALLED_ITEMS__"
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 8
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250712163401.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 8
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-07-06 13:19:51.188412"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/08"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V16"
    config_vars['REQUIRE_REPO_REV'] = 31
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"84a1c956d9ed6ec0c4ccbffa5dad7d30dfa17d0c"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/08/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 4290
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250712163401.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = ""
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"AnalyzeAudioBundle_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_Data_Folders_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS_Models_Data_Folders_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"CR8_Sampler_Presets_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_V16_1_IID", r"Get_General_Icons_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"IntelDlls_IID", r"LicenseNotifications_V16_1_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"Main_Waves_folder_IID", r"Minimum_Requirements_IID", r"ORS_Modulators_Data_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PresetBrowser_V16_1_IID", r"Shutdown_Servers_IID", r"V9_V10_Organizer_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesLib1_16_0_23_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V16_1_IID", r"Waves_Data_folder_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"pqaeeglltcjcmxku"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = ""
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = (r"COSMOS_Application_IID", r"COSMOS_HTML_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"WavesLocalServer_IID")
    config_vars['__NOW__'] = r"2025-07-12 16:35:29.852368"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 184899485
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 107
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8", r"/Library/Application Support/Waves/Central/V16", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=569):
    with Stage(r"begin", prog_num=570):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=571):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=572) as copy_file_to_file_001_572:
            copy_file_to_file_001_572()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=573) as copy_file_to_file_002_573:
            copy_file_to_file_002_573()
    with Stage(r"sync", prog_num=574):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=575) as shell_command_003_575:
            shell_command_003_575()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=576) as shell_command_004_576:
            shell_command_004_576()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=577) as shell_command_005_577:
            shell_command_005_577()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=578) as shell_command_006_578:
            shell_command_006_578()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=579) as shell_command_007_579:
            shell_command_007_579()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=580) as shell_command_008_580:
            shell_command_008_580()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=581) as shell_command_009_581:
            shell_command_009_581()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=582) as shell_command_010_582:
            shell_command_010_582()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=583) as shell_command_011_583:
            shell_command_011_583()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=584):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=585) as make_dir_012_585:
                make_dir_012_585()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=586) as cd_013_586:
                cd_013_586()
                Progress(r"3704 files already in cache", own_progress_count=3704, prog_num=4290)()
                with CreateSyncFolders(own_progress_count=38, prog_num=4328) as create_sync_folders_014_4328:
                    create_sync_folders_014_4328()
                Progress(r"Downloading with 50 processes in parallel", prog_num=4329)()
                Progress(r"Downloading with curl parallel", prog_num=4330)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.py_curl/dl-00", total_files_to_download=107, previously_downloaded_files=0, total_bytes_to_download=184899485, own_progress_count=104, prog_num=4434, report_own_progress=False) as curl_with_internal_parallel_015_4434:
                    curl_with_internal_parallel_015_4434()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.py_curl/dl-01", total_files_to_download=107, previously_downloaded_files=104, total_bytes_to_download=184899485, own_progress_count=3, prog_num=4437, report_own_progress=False) as curl_with_internal_parallel_016_4437:
                    curl_with_internal_parallel_016_4437()
                Progress(r"Downloading 107 files done", prog_num=4438)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=4439) as run_in_thread_017_4439:
                    run_in_thread_017_4439()
                Progress(r"Check checksum ...", prog_num=4440)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=107, prog_num=4547) as check_download_folder_checksum_018_4547:
                    check_download_folder_checksum_018_4547()
                with Stage(r"post_sync", prog_num=4548):
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16...", prog_num=4549)()
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=4550, recursive=True) as chmod_and_chown_019_4550:
                        chmod_and_chown_019_4550()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=4551) as copy_file_to_file_020_4551:
                        copy_file_to_file_020_4551()
            Progress(r"Done sync", prog_num=4552)()
    with Stage(r"copy", prog_num=4553):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=4554)()
        with Stage(r"create folders", prog_num=4555):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=4556) as make_dir_021_4556:
                make_dir_021_4556()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=4557) as make_dir_022_4557:
                make_dir_022_4557()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=4558) as make_dir_023_4558:
                make_dir_023_4558()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=4559) as make_dir_024_4559:
                make_dir_024_4559()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=4560) as make_dir_025_4560:
                make_dir_025_4560()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=4561) as make_dir_026_4561:
                make_dir_026_4561()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=4562) as make_dir_027_4562:
                make_dir_027_4562()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=4563) as make_dir_028_4563:
                make_dir_028_4563()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=4564) as make_dir_029_4564:
                make_dir_029_4564()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=4565) as make_dir_030_4565:
                make_dir_030_4565()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=4566) as make_dir_031_4566:
                make_dir_031_4566()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=4567) as make_dir_032_4567:
                make_dir_032_4567()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=4568) as make_dir_033_4568:
                make_dir_033_4568()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=4569) as make_dir_034_4569:
                make_dir_034_4569()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=4570) as make_dir_035_4570:
                make_dir_035_4570()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=4571) as make_dir_036_4571:
                make_dir_036_4571()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=4572) as make_dir_037_4572:
                make_dir_037_4572()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=4573) as make_dir_038_4573:
                make_dir_038_4573()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=4574) as make_dir_039_4574:
                make_dir_039_4574()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=4575) as make_dir_040_4575:
                make_dir_040_4575()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=4576) as make_dir_041_4576:
                make_dir_041_4576()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=4577) as make_dir_042_4577:
                make_dir_042_4577()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=4578) as make_dir_043_4578:
                make_dir_043_4578()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=4579) as make_dir_044_4579:
                make_dir_044_4579()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=4580) as rm_file_or_dir_045_4580:
            rm_file_or_dir_045_4580()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=4581) as shell_command_046_4581:
            shell_command_046_4581()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=4582) as shell_command_047_4582:
            shell_command_047_4582()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=4583) as shell_command_048_4583:
            shell_command_048_4583()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=4584) as shell_command_049_4584:
            shell_command_049_4584()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=4585) as shell_command_050_4585:
            shell_command_050_4585()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=4586) as shell_command_051_4586:
            shell_command_051_4586()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=4587) as shell_command_052_4587:
            shell_command_052_4587()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=4588) as shell_command_053_4588:
            shell_command_053_4588()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=4589) as shell_command_054_4589:
            shell_command_054_4589()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=4590) as cd_stage_055_4590:
            cd_stage_055_4590()
            with SetExecPermissionsInSyncFolder(prog_num=4591) as set_exec_permissions_in_sync_folder_056_4591:
                set_exec_permissions_in_sync_folder_056_4591()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=4592) as cd_stage_057_4592:
            cd_stage_057_4592()
            with Stage(r"copy", r"COSMOS__Application v16.0.50.51", prog_num=4593):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=4594) as should_copy_source_058_4594:
                    should_copy_source_058_4594()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=4595):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=4596) as copy_dir_to_dir_059_4596:
                            copy_dir_to_dir_059_4596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=4597) as unwtar_060_4597:
                            unwtar_060_4597()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=4598, recursive=True) as chown_061_4598:
                            chown_061_4598()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=4608) as resolve_symlink_files_in_folder_062_4608:
                resolve_symlink_files_in_folder_062_4608()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=4609) as cd_stage_063_4609:
            cd_stage_063_4609()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=4610):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=4611) as should_copy_source_064_4611:
                    should_copy_source_064_4611()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=4612):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=4613) as copy_dir_to_dir_065_4613:
                            copy_dir_to_dir_065_4613()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=4614, recursive=True) as chown_066_4614:
                            chown_066_4614()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=4615):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=4616) as should_copy_source_067_4616:
                    should_copy_source_067_4616()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=4617):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=4618) as copy_dir_to_dir_068_4618:
                            copy_dir_to_dir_068_4618()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=4619) as unwtar_069_4619:
                            unwtar_069_4619()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=4620, recursive=True) as chown_070_4620:
                            chown_070_4620()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=4621):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=4622) as should_copy_source_071_4622:
                    should_copy_source_071_4622()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=4623):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=4624) as copy_dir_to_dir_072_4624:
                            copy_dir_to_dir_072_4624()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=4625, recursive=True) as chown_073_4625:
                            chown_073_4625()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=4626) as cd_stage_074_4626:
            cd_stage_074_4626()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=4627):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=4628) as should_copy_source_075_4628:
                    should_copy_source_075_4628()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=4629):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=4630) as copy_dir_to_dir_076_4630:
                            copy_dir_to_dir_076_4630()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=4631, recursive=True) as chown_077_4631:
                            chown_077_4631()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=4632) as cd_stage_078_4632:
            cd_stage_078_4632()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=4633):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=4634) as should_copy_source_079_4634:
                    should_copy_source_079_4634()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=4635):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=4636) as copy_dir_to_dir_080_4636:
                            copy_dir_to_dir_080_4636()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=4637) as unwtar_081_4637:
                            unwtar_081_4637()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=4638, recursive=True) as chown_082_4638:
                            chown_082_4638()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=4639):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=4640) as should_copy_source_083_4640:
                    should_copy_source_083_4640()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=4641):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=4642) as copy_dir_to_dir_084_4642:
                            copy_dir_to_dir_084_4642()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=4643) as unwtar_085_4643:
                            unwtar_085_4643()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=4644, recursive=True) as chown_086_4644:
                            chown_086_4644()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=2, prog_num=4646) as resolve_symlink_files_in_folder_087_4646:
                resolve_symlink_files_in_folder_087_4646()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=4647) as shell_command_088_4647:
                shell_command_088_4647()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=4648) as script_command_089_4648:
                script_command_089_4648()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=4649) as shell_command_090_4649:
                shell_command_090_4649()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=4650) as create_symlink_091_4650:
                create_symlink_091_4650()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=4651) as create_symlink_092_4651:
                create_symlink_092_4651()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=4652) as copy_glob_to_dir_093_4652:
                copy_glob_to_dir_093_4652()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=4653) as cd_stage_094_4653:
            cd_stage_094_4653()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=4654):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=4655) as should_copy_source_095_4655:
                    should_copy_source_095_4655()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=4656):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=4657) as copy_file_to_dir_096_4657:
                            copy_file_to_dir_096_4657()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=4658) as chmod_and_chown_097_4658:
                            chmod_and_chown_097_4658()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=4659) as cd_stage_098_4659:
            cd_stage_098_4659()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=4660):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=4661) as should_copy_source_099_4661:
                    should_copy_source_099_4661()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=4662):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=4663) as copy_dir_to_dir_100_4663:
                            copy_dir_to_dir_100_4663()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=4664) as unwtar_101_4664:
                            unwtar_101_4664()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=4665, recursive=True) as chown_102_4665:
                            chown_102_4665()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=4666) as shell_command_103_4666:
                            shell_command_103_4666()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=4667):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=4668) as should_copy_source_104_4668:
                    should_copy_source_104_4668()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=4669):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=4670) as copy_dir_to_dir_105_4670:
                            copy_dir_to_dir_105_4670()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=4671) as unwtar_106_4671:
                            unwtar_106_4671()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=4672, recursive=True) as chown_107_4672:
                            chown_107_4672()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=4673) as break_hard_link_108_4673:
                            break_hard_link_108_4673()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=4674) as shell_command_109_4674:
                            shell_command_109_4674()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=4675, recursive=True) as chown_110_4675:
                            chown_110_4675()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=4676, recursive=True) as chmod_111_4676:
                            chmod_111_4676()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=4677):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=4678) as should_copy_source_112_4678:
                    should_copy_source_112_4678()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=4679):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=4680) as copy_dir_to_dir_113_4680:
                            copy_dir_to_dir_113_4680()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=4681) as unwtar_114_4681:
                            unwtar_114_4681()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=4682, recursive=True) as chown_115_4682:
                            chown_115_4682()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=4683) as shell_command_116_4683:
                            shell_command_116_4683()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=4684):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=4685) as should_copy_source_117_4685:
                    should_copy_source_117_4685()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=4686):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=4687) as copy_dir_to_dir_118_4687:
                            copy_dir_to_dir_118_4687()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=4688) as unwtar_119_4688:
                            unwtar_119_4688()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=4689, recursive=True) as chown_120_4689:
                            chown_120_4689()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=4690) as shell_command_121_4690:
                shell_command_121_4690()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=4691) as cd_stage_122_4691:
            cd_stage_122_4691()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=4692):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=4693) as should_copy_source_123_4693:
                    should_copy_source_123_4693()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=4694):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=4695) as copy_dir_to_dir_124_4695:
                            copy_dir_to_dir_124_4695()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=4696) as unwtar_125_4696:
                            unwtar_125_4696()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=4697, recursive=True) as chown_126_4697:
                            chown_126_4697()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=4698) as shell_command_127_4698:
                            shell_command_127_4698()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=4699) as cd_stage_128_4699:
            cd_stage_128_4699()
            with Stage(r"copy", r"COSMOS_HTML v2.6.6", prog_num=4700):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=4701) as should_copy_source_129_4701:
                    should_copy_source_129_4701()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=4702):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=4703) as copy_dir_to_dir_130_4703:
                            copy_dir_to_dir_130_4703()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=4704, recursive=True) as chown_131_4704:
                            chown_131_4704()
            with Stage(r"copy", r"COSMOS_python v2.7.7", prog_num=4705):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=4706) as should_copy_source_132_4706:
                    should_copy_source_132_4706()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=4707):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=4708) as copy_dir_to_dir_133_4708:
                            copy_dir_to_dir_133_4708()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=4709) as unwtar_134_4709:
                            unwtar_134_4709()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=4710, recursive=True) as chown_135_4710:
                            chown_135_4710()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=4711) as cd_stage_136_4711:
            cd_stage_136_4711()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=4712):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=4713) as should_copy_source_137_4713:
                    should_copy_source_137_4713()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=4714):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=4715) as copy_dir_to_dir_138_4715:
                            copy_dir_to_dir_138_4715()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=4716) as unwtar_139_4716:
                            unwtar_139_4716()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=4717, recursive=True) as chown_140_4717:
                            chown_140_4717()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=4718) as cd_stage_141_4718:
            cd_stage_141_4718()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=4719):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=4720) as should_copy_source_142_4720:
                    should_copy_source_142_4720()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=4721):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=4722) as copy_dir_to_dir_143_4722:
                            copy_dir_to_dir_143_4722()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=4723, recursive=True) as chown_144_4723:
                            chown_144_4723()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=4724) as cd_stage_145_4724:
            cd_stage_145_4724()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=4725):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=4726) as should_copy_source_146_4726:
                    should_copy_source_146_4726()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=4727):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=4728) as copy_dir_to_dir_147_4728:
                            copy_dir_to_dir_147_4728()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=4729, recursive=True) as chown_148_4729:
                            chown_148_4729()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=4730) as cd_stage_149_4730:
            cd_stage_149_4730()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=4731):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=4732) as should_copy_source_150_4732:
                    should_copy_source_150_4732()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=4733):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=4734) as copy_dir_to_dir_151_4734:
                            copy_dir_to_dir_151_4734()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=4735, recursive=True) as chown_152_4735:
                            chown_152_4735()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=4736) as cd_stage_153_4736:
            cd_stage_153_4736()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=4737) as rm_file_or_dir_154_4737:
                rm_file_or_dir_154_4737()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=4738):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=4739) as should_copy_source_155_4739:
                    should_copy_source_155_4739()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=4740):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=4741) as copy_dir_to_dir_156_4741:
                            copy_dir_to_dir_156_4741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=4742) as unwtar_157_4742:
                            unwtar_157_4742()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=4743, recursive=True) as chown_158_4743:
                            chown_158_4743()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=4744):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=4745) as should_copy_source_159_4745:
                    should_copy_source_159_4745()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=4746):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=4747) as unwtar_160_4747:
                            unwtar_160_4747()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=4748):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=4749) as should_copy_source_161_4749:
                    should_copy_source_161_4749()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=4750):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=4751) as copy_dir_to_dir_162_4751:
                            copy_dir_to_dir_162_4751()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=4752) as unwtar_163_4752:
                            unwtar_163_4752()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=4753, recursive=True) as chown_164_4753:
                            chown_164_4753()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=4754):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=4755) as should_copy_source_165_4755:
                    should_copy_source_165_4755()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=4756):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=4757) as copy_dir_to_dir_166_4757:
                            copy_dir_to_dir_166_4757()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=4758) as chmod_167_4758:
                            chmod_167_4758()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=4759) as chmod_168_4759:
                            chmod_168_4759()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=4760, recursive=True) as chown_169_4760:
                            chown_169_4760()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=4763) as resolve_symlink_files_in_folder_170_4763:
                resolve_symlink_files_in_folder_170_4763()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=4764) as shell_command_171_4764:
                shell_command_171_4764()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=4765) as cd_stage_172_4765:
            cd_stage_172_4765()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=4766):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=4767) as should_copy_source_173_4767:
                    should_copy_source_173_4767()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=4768):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=4769) as copy_dir_to_dir_174_4769:
                            copy_dir_to_dir_174_4769()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=4770, recursive=True) as chown_175_4770:
                            chown_175_4770()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=4771) as cd_stage_176_4771:
            cd_stage_176_4771()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=4772):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=4773) as should_copy_source_177_4773:
                    should_copy_source_177_4773()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=4774):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=4775) as copy_dir_to_dir_178_4775:
                            copy_dir_to_dir_178_4775()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=4776, recursive=True) as chown_179_4776:
                            chown_179_4776()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=4777) as cd_stage_180_4777:
            cd_stage_180_4777()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=4778):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=4779) as should_copy_source_181_4779:
                    should_copy_source_181_4779()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=4780):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=4781, recursive=True) as chmod_182_4781:
                            chmod_182_4781()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=4782) as copy_dir_to_dir_183_4782:
                            copy_dir_to_dir_183_4782()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=4783) as unwtar_184_4783:
                            unwtar_184_4783()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=4784, recursive=True) as chown_185_4784:
                            chown_185_4784()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=4785) as if_186_4785:
                            if_186_4785()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=4786) as cd_stage_187_4786:
            cd_stage_187_4786()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=4787):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=4788) as should_copy_source_188_4788:
                    should_copy_source_188_4788()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=4789):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=4790, recursive=True) as chmod_189_4790:
                            chmod_189_4790()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=4791) as copy_dir_to_dir_190_4791:
                            copy_dir_to_dir_190_4791()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=4792) as unwtar_191_4792:
                            unwtar_191_4792()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=4793, recursive=True) as chown_192_4793:
                            chown_192_4793()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=4794) as if_193_4794:
                            if_193_4794()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=4795) as cd_stage_194_4795:
            cd_stage_194_4795()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=4796):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=4797) as should_copy_source_195_4797:
                    should_copy_source_195_4797()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=4798):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=4799) as copy_dir_to_dir_196_4799:
                            copy_dir_to_dir_196_4799()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=4800) as unwtar_197_4800:
                            unwtar_197_4800()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=4801, recursive=True) as chown_198_4801:
                            chown_198_4801()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=4802) as break_hard_link_199_4802:
                            break_hard_link_199_4802()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=4803) as shell_command_200_4803:
                            shell_command_200_4803()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=4804, recursive=True) as chown_201_4804:
                            chown_201_4804()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=4805, recursive=True) as chmod_202_4805:
                            chmod_202_4805()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=4806) as cd_stage_203_4806:
            cd_stage_203_4806()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=4807):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=4808) as should_copy_source_204_4808:
                    should_copy_source_204_4808()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=4809):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=4810) as copy_dir_to_dir_205_4810:
                            copy_dir_to_dir_205_4810()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=4811) as unwtar_206_4811:
                            unwtar_206_4811()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=4812, recursive=True) as chown_207_4812:
                            chown_207_4812()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=4813) as shell_command_208_4813:
                            shell_command_208_4813()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=4814) as shell_command_209_4814:
            shell_command_209_4814()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=4815) as shell_command_210_4815:
            shell_command_210_4815()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=4816) as script_command_211_4816:
            script_command_211_4816()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=4817) as rm_file_or_dir_212_4817:
            rm_file_or_dir_212_4817()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=4818) as shell_command_213_4818:
            shell_command_213_4818()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=4819) as script_command_214_4819:
            script_command_214_4819()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=4820) as rm_file_or_dir_215_4820:
            rm_file_or_dir_215_4820()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=4821) as glober_216_4821:
            glober_216_4821()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=4822) as glober_217_4822:
            glober_217_4822()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=4823) as glober_218_4823:
            glober_218_4823()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=4824) as shell_command_219_4824:
            shell_command_219_4824()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=4825) as shell_command_220_4825:
            shell_command_220_4825()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=4826) as shell_command_221_4826:
            shell_command_221_4826()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=4827) as shell_command_222_4827:
            shell_command_222_4827()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=4828) as shell_command_223_4828:
            shell_command_223_4828()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=4829) as script_command_224_4829:
            script_command_224_4829()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=4830) as if_225_4830:
            if_225_4830()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=4831) as if_226_4831:
            if_226_4831()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=4832) as if_227_4832:
            if_227_4832()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=4833) as if_228_4833:
            if_228_4833()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=4834) as make_dir_229_4834:
            make_dir_229_4834()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=4835) as chmod_230_4835:
            chmod_230_4835()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=4836) as make_dir_231_4836:
            make_dir_231_4836()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=4837) as chmod_232_4837:
            chmod_232_4837()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=4838) as chmod_233_4838:
            chmod_233_4838()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=4839) as chmod_234_4839:
            chmod_234_4839()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=4840) as chmod_235_4840:
            chmod_235_4840()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=4841) as shell_command_236_4841:
            shell_command_236_4841()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=4842) as script_command_237_4842:
            script_command_237_4842()
    with Stage(r"post-copy", prog_num=4843):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=4844) as make_dir_238_4844:
            make_dir_238_4844()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=4845) as copy_file_to_file_239_4845:
            copy_file_to_file_239_4845()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=4846) as chmod_240_4846:
            chmod_240_4846()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=4847) as chmod_241_4847:
            chmod_241_4847()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=4848) as copy_file_to_file_242_4848:
            copy_file_to_file_242_4848()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=4849) as chmod_243_4849:
            chmod_243_4849()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=4850) as copy_file_to_file_244_4850:
            copy_file_to_file_244_4850()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=4851) as chmod_245_4851:
            chmod_245_4851()
        Progress(r"Done copy", prog_num=4852)()
        Progress(r"Done synccopy", prog_num=4853)()
    with Stage(r"post", prog_num=4854):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=4855) as make_dir_246_4855:
            make_dir_246_4855()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=4856) as copy_file_to_file_247_4856:
            copy_file_to_file_247_4856()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=4857) as make_dir_248_4857:
            make_dir_248_4857()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=4858) as copy_file_to_file_249_4858:
            copy_file_to_file_249_4858()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=4859) as make_dir_250_4859:
            make_dir_250_4859()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/8/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=4860) as copy_file_to_file_251_4860:
            copy_file_to_file_251_4860()

with Stage(r"epilog", prog_num=4861):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250712163401.py", prog_num=4862) as patch_py_batch_with_timings_252_4862:
        patch_py_batch_with_timings_252_4862()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


