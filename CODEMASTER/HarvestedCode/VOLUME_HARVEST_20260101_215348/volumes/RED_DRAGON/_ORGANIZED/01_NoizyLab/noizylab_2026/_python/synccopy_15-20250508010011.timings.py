# Creation time: 08-05-25_01-02
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 13649
PythonBatchCommandBase.running_progress = 1224
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1225):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250508010011"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.4.7"
    config_vars['CENTRAL_WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V15", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V15", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 53
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NjcxNjQxMX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQ2NjgwMTExfX19XX0_;CloudFront-Signature=TrwCKW1ajlzu3PHe0Ip9dDmoV2InNeJi-rJ~b8BJpDG6abj~TkH18ntKJkqDS8FSGJBCXfUGXT~7iT8PEbX-1wNuw5Bq~PB7kIFr9ONEnK5tVqtQBBkATd~k1yRhjuQyF3MSdRIjRqihe8QWsmG2lA8P8fkwNXGeJElkk~ygjYh0rtwkBAfdrKAtw0BopFbo~n4v3-FtX~57OhPj5TW-GlI0tatYlU52l-lDCR3dQW-uF1RLGV2vuqt5jOOEyKaj3NFR1oBqEOAc4CZJCi1GreDrRtobi5whEsgRW3EjDU4a6Jv3mWE3CMH8Pfxn7F7Kqen2GeGBm6DaD9Y7fVuDGQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NjcxNjQxMX0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzQ2NjgwMTExfX19XX0_;CloudFront-Signature=TrwCKW1ajlzu3PHe0Ip9dDmoV2InNeJi-rJ~b8BJpDG6abj~TkH18ntKJkqDS8FSGJBCXfUGXT~7iT8PEbX-1wNuw5Bq~PB7kIFr9ONEnK5tVqtQBBkATd~k1yRhjuQyF3MSdRIjRqihe8QWsmG2lA8P8fkwNXGeJElkk~ygjYh0rtwkBAfdrKAtw0BopFbo~n4v3-FtX~57OhPj5TW-GlI0tatYlU52l-lDCR3dQW-uF1RLGV2vuqt5jOOEyKaj3NFR1oBqEOAc4CZJCi1GreDrRtobi5whEsgRW3EjDU4a6Jv3mWE3CMH8Pfxn7F7Kqen2GeGBm6DaD9Y7fVuDGQ__"
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
    config_vars['INDEX_CHECKSUM'] = r"66ce77b6f94f9e3d2b5f50844f00981c8ce93125"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/53/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"27ce44a61cdbadf4216506c62c15574db7911d1f"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/53/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/53/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"Fixed reporting of bad actions in verify repo"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"1374eaac-1f40-4629-a1bd-7fad36931856", r"1b2e3046-b634-4fc3-92df-100722e72a75", r"1d2e15ad-514e-4894-b13c-087940f2c275", r"215572dc-9c91-4912-a0a9-d68096edc994", r"22195f90-44a7-41aa-8e89-7cd4032a553e", r"239c7584-82a0-420d-bfae-8885b3a52538", r"289510f1-fdf8-45ee-ae8d-4f42cc82ca64", r"29e06aff-907d-4711-a74e-3f8a59d69d79", r"2acada14-94c5-4414-9d64-454da34b0639", r"2d71ad91-bddb-42f2-a652-835830176f9f", r"30917ee9-a700-481d-85d7-2062c35a9802", r"3164b0cb-806c-4bdd-a286-260f9c6eb04c", r"329dbe6a-233e-4f8f-ac70-f5b55036845b", r"34ec8670-67d0-4e60-9e6a-3a3d15146c3c", r"386ca2e5-2636-495f-810e-49eceb953b9f", r"3c217951-f061-42a9-a797-c6ae08355e8d", r"3cc8e3c0-c209-4128-a2f6-32be589badbf", r"3d47fe76-e1f9-4cbf-b155-715460ee749f", r"423381b7-4e7e-41e2-a69a-518aefd4ef13", r"49e069d6-907d-4991-a74e-3f8959d69830", r"51472ece-6f53-4926-8123-64330d6c6852", r"53a2fb95-8424-429f-a2c8-21e86b847f0a", r"558c21cb-b648-48a3-a23b-db455ecc2d55", r"5634fda9-ea28-4316-9476-527b8e7279a9", r"5daf4282-f6c5-4e00-b7d5-cac37ad48604", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"63b0a9f9-a701-4596-acb7-ab671e5addd9", r"6983b49f-2238-4e1e-8828-50ca84f58737", r"6c7cdfec-03f7-4d62-84c3-9ea633067fc9", r"72e4f2f3-cc29-4635-8715-a7977a943920", r"7707a80e-06f0-412a-b2de-baa2c332bb13", r"7c01bd8c-6267-48ce-8707-9df05b786b7b", r"811b0faa-6979-4500-a187-791e07c79138", r"87d5ca54-c659-460d-92ca-d25786210a25", r"8ce7a272-1741-4893-b516-e93ce40db756", r"911c58f1-0b6b-42f7-93dd-a571b29860fc", r"96f2b292-8c3b-49f4-8193-4f7783654547", r"aa264888-988b-421c-89c9-629934734f37", r"ab09a527-4793-44f2-9353-c25cc1f4b856", r"ae4b9cc6-a30f-42ad-b4db-28cb21cda94b", r"b158aea5-79f7-4a39-b9b9-f8c5e7c237c2", r"b3964c48-04db-470f-b5b8-fa2b340a6fd4", r"b8a31ecd-5110-4d10-ba3d-ca56215b3745", r"c19c1d27-90ca-43e3-b503-9c7f2da272bc", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"ca9a4322-a903-43ec-95d7-ccbbb475d2d5", r"d1b17f75-9fbf-4af9-9c8e-ebb7068998b9", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"dfc80d80-ad21-11e0-804c-b7fd7bebd530", r"e023b7a0-ad21-11e0-80bf-b7fd7bebd530", r"e0427e39-ad21-11e0-832d-b7fd7bebd530", r"e06158e4-ad21-11e0-80ed-b7fd7bebd530", r"e09dd956-ad21-11e0-80a8-b7fd7bebd530", r"e10288b9-ad21-11e0-8381-b7fd7bebd530", r"e1e91460-ad21-11e0-8303-b7fd7bebd530", r"e22cd127-ad21-11e0-822b-b7fd7bebd530", r"e39dce24-16c9-4f4a-bb98-545e10052b75", r"e3a57973-ad21-11e0-818c-b7fd7bebd530", r"e3c605a4-ad21-11e0-8113-b7fd7bebd530", r"e47a4b22-ad21-11e0-80ba-b7fd7bebd530", r"e4b00ec4-ad21-11e0-834b-b7fd7bebd530", r"e4e5fb53-131e-45e0-91c1-d78aa4f5c69f", r"e4e72e7b-ad21-11e0-81a6-b7fd7bebd530", r"e5100b89-ad21-11e0-81a0-b7fd7bebd530", r"e551833a-ad21-11e0-8177-b7fd7bebd530", r"e591e90a-ad21-11e0-83a1-b7fd7bebd530", r"e5ce4a76-ad21-11e0-832b-b7fd7bebd530", r"e5ecb58a-ad21-11e0-820b-b7fd7bebd530", r"e60ab8c6-ad21-11e0-8364-b7fd7bebd530", r"e6281b3c-ad21-11e0-8087-b7fd7bebd530", r"e646beb6-ad21-11e0-83c3-b7fd7bebd530", r"e6675177-ad21-11e0-833e-b7fd7bebd530", r"e686154a-ad21-11e0-806f-b7fd7bebd530", r"e686394e-ad21-11e0-8185-b7fd7bebd530", r"e6a8de66-ad21-11e0-81f4-b7fd7bebd530", r"e6c7625a-ad21-11e0-8262-b7fd7bebd530", r"e6ead714-ad21-11e0-82a6-b7fd7bebd530", r"e7069133-ad21-11e0-82c1-b7fd7bebd530", r"e7223951-ad21-11e0-82d3-b7fd7bebd530", r"e73ed1fb-ad21-11e0-8035-b7fd7bebd530", r"e759bc5f-ad21-11e0-827d-b7fd7bebd530", r"e775f5e1-ad21-11e0-809f-b7fd7bebd530", r"e790fd1a-ad21-11e0-82c3-b7fd7bebd530", r"e7af58a0-ad21-11e0-832f-b7fd7bebd530", r"e7cd30b4-ad21-11e0-8385-b7fd7bebd530", r"e808505c-ad21-11e0-83e8-b7fd7bebd530", r"e8f6b97d-ad21-11e0-8088-b7fd7bebd530", r"e92b2cea-ad21-11e0-8218-b7fd7bebd530", r"e9797602-ad21-11e0-8369-b7fd7bebd530", r"e9ef3ffd-ad21-11e0-83e3-b7fd7bebd530", r"ea1152ba-ad21-11e0-8305-b7fd7bebd530", r"ea4ad51a-ad21-11e0-8137-b7fd7bebd530", r"ea812d41-ad21-11e0-80f3-b7fd7bebd530", r"ea9c2b7e-ad21-11e0-8327-b7fd7bebd530", r"eab8d633-ad21-11e0-81eb-b7fd7bebd530", r"eb0c63ec-ad21-11e0-8288-b7fd7bebd530", r"eb542f98-ad21-11e0-8222-b7fd7bebd530", r"eb621b67-ad21-11e0-8319-b7fd7bebd530", r"ec32123c-ad21-11e0-83d2-b7fd7bebd530", r"ec53f8dd-ad21-11e0-8276-b7fd7bebd530", r"ec541a62-ad21-11e0-8150-b7fd7bebd530", r"ec719e28-ad21-11e0-8100-b7fd7bebd530", r"ec971ad7-ad21-11e0-8359-b7fd7bebd530", r"ec97493f-ad21-11e0-803e-b7fd7bebd530", r"ed13f26a-ad21-11e0-8216-b7fd7bebd530", r"ed14136b-ad21-11e0-837c-b7fd7bebd530", r"ed748b6e-ad21-11e0-83bb-b7fd7bebd530", r"edff65f4-ad21-11e0-8126-b7fd7bebd530", r"ee3dacf8-ad21-11e0-83ec-b7fd7bebd530", r"ee76f044-ad21-11e0-8170-b7fd7bebd530", r"ee93e582-ad21-11e0-8390-b7fd7bebd530", r"ef202a69-ad21-11e0-839b-b7fd7bebd530", r"ef3b4d52-ad21-11e0-8109-b7fd7bebd530", r"ef6067d8-ad21-11e0-8308-b7fd7bebd530", r"ef7b9575-ad21-11e0-81f1-b7fd7bebd530", r"ef9640eb-ad21-11e0-83ab-b7fd7bebd530", r"efb10934-ad21-11e0-8058-b7fd7bebd530", r"efce20a0-ad21-11e0-8012-b7fd7bebd530", r"efe96c20-ad21-11e0-833c-b7fd7bebd530", r"f00484d0-ad21-11e0-8357-b7fd7bebd530", r"f01f84d6-ad21-11e0-822a-b7fd7bebd530", r"f03a7463-ad21-11e0-830f-b7fd7bebd530", r"f056c254-ad21-11e0-8310-b7fd7bebd530", r"f169fb78-ad21-11e0-8276-b7fd7bebd530", r"f1e2bcde-ad21-11e0-800a-b7fd7bebd530", r"f202b779-ad21-11e0-8344-b7fd7bebd530", r"f2214239-ad21-11e0-82e2-b7fd7bebd530", r"f23de82a-ad21-11e0-803b-b7fd7bebd530", r"f25bce3b-ad21-11e0-8126-b7fd7bebd530", r"f2781703-ad21-11e0-8147-b7fd7bebd530", r"f2a5ad2a-ad21-11e0-8185-b7fd7bebd530", r"f2f168c9-ad21-11e0-803f-b7fd7bebd530", r"f3315154-ad21-11e0-8140-b7fd7bebd530", r"f3513e7f-ad21-11e0-83f7-b7fd7bebd530", r"f3515f5a-ad21-11e0-81da-b7fd7bebd530", r"fcdbc046-5e44-4d4d-b4ec-049d194c2458")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 53
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250508010011.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 53
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-04-27 15:05:10.194151"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/53"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_NAME'] = r"V15"
    config_vars['REQUIRE_REPO_REV'] = 43
    config_vars['REQUIRE_S3_BUCKET_NAME'] = r"instl"
    config_vars['REQUIRE_SYNC_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15"
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"87f93a30bd66ac00b540162293eca13b3010343e"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/53/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 12420
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250508010011.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"unknown compilation time"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.4.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Q_Clone_Presets_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS__Data_Folders__IID", r"COSMOS__IID", r"COSMOS__Models_Data_Folders__IID", r"COSMOS_python_IID", r"Center_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Enigma_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"Get_General_Icons_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LicenseNotifications_1_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"ORS_Modulators_Data_IID", r"OpenVino_IID", r"PAZ_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"ReWire_IID", r"ReWire_backup_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"SOC_Presets_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"SuperTap_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"WLM_IID", r"WLM_Plus_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_10_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_10_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_VST_3_V15_10_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_10_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_15_10_46_IID", r"WavesLib1_15_5_139_IID", r"WavesLib1_15_5_79_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V15_2_IID", r"WavesReWireDevice_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.2 unknown compilation time RSPMS.local"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.2"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 2)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"duzrmfcdpugpgckd"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS__IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-05-08 01:03:16.270494"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 130687960
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 36
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"RSPMS.local"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=1226):  # 2m:3.592s
    with Stage(r"begin", prog_num=1227):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1228):  # 0m:0.018s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1229) as copy_file_to_file_001_1229:  # 0m:0.010s
            copy_file_to_file_001_1229()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1230) as copy_file_to_file_002_1230:  # 0m:0.008s
            copy_file_to_file_002_1230()
    with Stage(r"sync", prog_num=1231):  # 1m:16.782s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1232) as shell_command_003_1232:  # 0m:0.013s
            shell_command_003_1232()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1233) as shell_command_004_1233:  # 0m:0.016s
            shell_command_004_1233()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1234) as shell_command_005_1234:  # 0m:40.102s
            shell_command_005_1234()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1235) as shell_command_006_1235:  # 0m:0.012s
            shell_command_006_1235()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1236) as shell_command_007_1236:  # 0m:34.428s
            shell_command_007_1236()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1237) as shell_command_008_1237:  # 0m:0.012s
            shell_command_008_1237()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1238) as shell_command_009_1238:  # 0m:0.010s
            shell_command_009_1238()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1239) as shell_command_010_1239:  # 0m:0.242s
            shell_command_010_1239()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=1240):  # 0m:1.948s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=1241) as make_dir_011_1241:  # 0m:0.010s
                make_dir_011_1241()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=1242) as cd_012_1242:  # 0m:1.937s
                cd_012_1242()
                Progress(r"10053 files already in cache", own_progress_count=10053, prog_num=11295)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=25, prog_num=11320) as create_sync_folders_013_11320:  # 0m:0.187s
                    create_sync_folders_013_11320()
                Progress(r"Downloading with 50 processes in parallel", prog_num=11321)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=11322)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.py_curl/dl-00", total_files_to_download=36, previously_downloaded_files=0, total_bytes_to_download=130687960, own_progress_count=33, prog_num=11355, report_own_progress=False) as curl_with_internal_parallel_014_11355:  # 0m:1.332s
                    curl_with_internal_parallel_014_11355()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.py_curl/dl-01", total_files_to_download=36, previously_downloaded_files=33, total_bytes_to_download=130687960, own_progress_count=3, prog_num=11358, report_own_progress=False) as curl_with_internal_parallel_015_11358:  # 0m:0.080s
                    curl_with_internal_parallel_015_11358()
                Progress(r"Downloading 36 files done", prog_num=11359)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=11360) as run_in_thread_016_11360:  # 0m:0.000s
                    run_in_thread_016_11360()
                Progress(r"Check checksum ...", prog_num=11361)()  # 0m:0.000s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=36, prog_num=11397) as check_download_folder_checksum_017_11397:  # 0m:0.133s
                    check_download_folder_checksum_017_11397()
                with Stage(r"post_sync", prog_num=11398):  # 0m:0.203s
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15...", prog_num=11399)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=11400, recursive=True) as chmod_and_chown_018_11400:  # 0m:0.190s
                        chmod_and_chown_018_11400()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=11401) as copy_file_to_file_019_11401:  # 0m:0.013s
                        copy_file_to_file_019_11401()
            Progress(r"Done sync", prog_num=11402)()  # 0m:0.000s
    with Stage(r"copy", prog_num=11403):  # 0m:46.641s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11404)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=11405):  # 0m:0.397s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=11406) as make_dir_020_11406:  # 0m:0.012s
                make_dir_020_11406()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=11407) as make_dir_021_11407:  # 0m:0.015s
                make_dir_021_11407()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=11408) as make_dir_022_11408:  # 0m:0.011s
                make_dir_022_11408()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=11409) as make_dir_023_11409:  # 0m:0.006s
                make_dir_023_11409()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=11410) as make_dir_024_11410:  # 0m:0.008s
                make_dir_024_11410()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=11411) as make_dir_025_11411:  # 0m:0.015s
                make_dir_025_11411()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=11412) as make_dir_026_11412:  # 0m:0.009s
                make_dir_026_11412()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=11413) as make_dir_027_11413:  # 0m:0.009s
                make_dir_027_11413()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=11414) as make_dir_028_11414:  # 0m:0.010s
                make_dir_028_11414()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=11415) as make_dir_029_11415:  # 0m:0.006s
                make_dir_029_11415()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=11416) as make_dir_030_11416:  # 0m:0.010s
                make_dir_030_11416()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=11417) as make_dir_031_11417:  # 0m:0.009s
                make_dir_031_11417()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=11418) as make_dir_032_11418:  # 0m:0.017s
                make_dir_032_11418()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=11419) as make_dir_033_11419:  # 0m:0.011s
                make_dir_033_11419()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=11420) as make_dir_034_11420:  # 0m:0.010s
                make_dir_034_11420()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=11421) as make_dir_035_11421:  # 0m:0.014s
                make_dir_035_11421()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/GTR", chowner=True, prog_num=11422) as make_dir_036_11422:  # 0m:0.010s
                make_dir_036_11422()
            with MakeDir(r"/Applications/Waves/ReWire", chowner=True, prog_num=11423) as make_dir_037_11423:  # 0m:0.006s
                make_dir_037_11423()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=11424) as make_dir_038_11424:  # 0m:0.012s
                make_dir_038_11424()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=11425) as make_dir_039_11425:  # 0m:0.006s
                make_dir_039_11425()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=11426) as make_dir_040_11426:  # 0m:0.008s
                make_dir_040_11426()
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=11427) as make_dir_041_11427:  # 0m:0.006s
                make_dir_041_11427()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=11428) as make_dir_042_11428:  # 0m:0.006s
                make_dir_042_11428()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=11429) as make_dir_043_11429:  # 0m:0.013s
                make_dir_043_11429()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=11430) as make_dir_044_11430:  # 0m:0.017s
                make_dir_044_11430()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=11431) as make_dir_045_11431:  # 0m:0.014s
                make_dir_045_11431()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=11432) as make_dir_046_11432:  # 0m:0.009s
                make_dir_046_11432()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=11433) as make_dir_047_11433:  # 0m:0.006s
                make_dir_047_11433()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=11434) as make_dir_048_11434:  # 0m:0.009s
                make_dir_048_11434()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=11435) as make_dir_049_11435:  # 0m:0.009s
                make_dir_049_11435()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=11436) as make_dir_050_11436:  # 0m:0.013s
                make_dir_050_11436()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=11437) as make_dir_051_11437:  # 0m:0.014s
                make_dir_051_11437()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=11438) as make_dir_052_11438:  # 0m:0.013s
                make_dir_052_11438()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=11439) as make_dir_053_11439:  # 0m:0.017s
                make_dir_053_11439()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=11440) as make_dir_054_11440:  # 0m:0.012s
                make_dir_054_11440()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=11441) as make_dir_055_11441:  # 0m:0.013s
                make_dir_055_11441()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=11442) as make_dir_056_11442:  # 0m:0.010s
                make_dir_056_11442()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=11443) as rm_file_or_dir_057_11443:  # 0m:0.012s
            rm_file_or_dir_057_11443()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=11444) as rm_file_or_dir_058_11444:  # 0m:0.001s
            rm_file_or_dir_058_11444()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=11445) as shell_command_059_11445:  # 0m:0.010s
            shell_command_059_11445()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=11446) as shell_command_060_11446:  # 0m:0.013s
            shell_command_060_11446()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=11447) as shell_command_061_11447:  # 0m:1.128s
            shell_command_061_11447()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11448) as shell_command_062_11448:  # 0m:0.013s
            shell_command_062_11448()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11449) as shell_command_063_11449:  # 0m:1.110s
            shell_command_063_11449()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=11450) as shell_command_064_11450:  # 0m:0.011s
            shell_command_064_11450()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=11451) as shell_command_065_11451:  # 0m:0.014s
            shell_command_065_11451()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=11452) as shell_command_066_11452:  # 0m:0.168s
            shell_command_066_11452()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11453) as cd_stage_067_11453:  # 0m:0.019s
            cd_stage_067_11453()
            with SetExecPermissionsInSyncFolder(prog_num=11454) as set_exec_permissions_in_sync_folder_068_11454:  # 0m:0.014s
                set_exec_permissions_in_sync_folder_068_11454()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=11455) as cd_stage_069_11455:  # 0m:0.140s
            cd_stage_069_11455()
            with Stage(r"copy", r"Bass Slapper application v15.5.79.262", prog_num=11456):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11457) as should_copy_source_070_11457:  # ?
                    should_copy_source_070_11457()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=11458):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=11459) as copy_dir_to_dir_071_11459:  # ?
                            copy_dir_to_dir_071_11459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=11460) as unwtar_072_11460:  # ?
                            unwtar_072_11460()
                        with Chown(path=r"/Applications/Waves/Applications V15/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=11461, recursive=True) as chown_073_11461:  # 0m:0.001s
                            chown_073_11461()
            with Stage(r"copy", r"Electric Grand 80 application v15.5.79.262", prog_num=11462):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11463) as should_copy_source_074_11463:  # ?
                    should_copy_source_074_11463()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=11464):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=11465) as copy_dir_to_dir_075_11465:  # ?
                            copy_dir_to_dir_075_11465()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=11466) as unwtar_076_11466:  # ?
                            unwtar_076_11466()
                        with Chown(path=r"/Applications/Waves/Applications V15/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=11467, recursive=True) as chown_077_11467:  # 0m:0.001s
                            chown_077_11467()
            with Stage(r"copy", r"GTR application v15.5.79.262", prog_num=11468):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11469) as should_copy_source_078_11469:  # ?
                    should_copy_source_078_11469()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=11470):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=11471) as copy_dir_to_dir_079_11471:  # ?
                            copy_dir_to_dir_079_11471()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=11472) as unwtar_080_11472:  # ?
                            unwtar_080_11472()
                        with Chown(path=r"/Applications/Waves/Applications V15/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=11473, recursive=True) as chown_081_11473:  # 0m:0.007s
                            chown_081_11473()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=11474) as shell_command_082_11474:  # 0m:0.116s
                shell_command_082_11474()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=11475) as script_command_083_11475:  # 0m:0.014s
                script_command_083_11475()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=11476) as cd_stage_084_11476:  # 0m:0.016s
            cd_stage_084_11476()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=11477):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=11478) as should_copy_source_085_11478:  # ?
                    should_copy_source_085_11478()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=11479):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=11480) as copy_dir_to_dir_086_11480:  # ?
                            copy_dir_to_dir_086_11480()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=11481) as unwtar_087_11481:  # ?
                            unwtar_087_11481()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=11482, recursive=True) as chown_088_11482:  # 0m:0.001s
                            chown_088_11482()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=11492) as resolve_symlink_files_in_folder_089_11492:  # 0m:0.013s
                resolve_symlink_files_in_folder_089_11492()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=11493) as cd_stage_090_11493:  # 0m:0.076s
            cd_stage_090_11493()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=11494):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11495) as should_copy_source_091_11495:  # ?
                    should_copy_source_091_11495()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=11496):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=11497) as copy_dir_to_dir_092_11497:  # ?
                            copy_dir_to_dir_092_11497()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=11498, recursive=True) as chown_093_11498:  # 0m:0.001s
                            chown_093_11498()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=11499):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11500) as should_copy_source_094_11500:  # ?
                    should_copy_source_094_11500()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=11501):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=11502) as copy_dir_to_dir_095_11502:  # ?
                            copy_dir_to_dir_095_11502()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=11503) as unwtar_096_11503:  # ?
                            unwtar_096_11503()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=11504, recursive=True) as chown_097_11504:  # 0m:0.001s
                            chown_097_11504()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=11505):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11506) as should_copy_source_098_11506:  # ?
                    should_copy_source_098_11506()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=11507):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=11508) as copy_dir_to_dir_099_11508:  # ?
                            copy_dir_to_dir_099_11508()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=11509, recursive=True) as chown_100_11509:  # 0m:0.006s
                            chown_100_11509()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=11510):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11511) as should_copy_source_101_11511:  # ?
                    should_copy_source_101_11511()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=11512):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11513) as copy_dir_to_dir_102_11513:  # ?
                            copy_dir_to_dir_102_11513()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=11514, recursive=True) as chown_103_11514:  # 0m:0.001s
                            chown_103_11514()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=11515):  # 0m:0.042s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11516) as should_copy_source_104_11516:  # 0m:0.042s
                    should_copy_source_104_11516()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=11517):  # 0m:0.042s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=11518) as copy_dir_to_dir_105_11518:  # 0m:0.041s
                            copy_dir_to_dir_105_11518()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=11519, recursive=True) as chown_106_11519:  # 0m:0.000s
                            chown_106_11519()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=11520):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11521) as should_copy_source_107_11521:  # ?
                    should_copy_source_107_11521()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=11522):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=11523) as copy_dir_to_dir_108_11523:  # ?
                            copy_dir_to_dir_108_11523()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=11524, recursive=True) as chown_109_11524:  # 0m:0.001s
                            chown_109_11524()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=11525):  # 0m:0.023s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11526) as should_copy_source_110_11526:  # 0m:0.023s
                    should_copy_source_110_11526()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=11527):  # 0m:0.023s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=11528) as copy_dir_to_dir_111_11528:  # 0m:0.011s
                            copy_dir_to_dir_111_11528()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=11529) as unwtar_112_11529:  # 0m:0.012s
                            unwtar_112_11529()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=11530, recursive=True) as chown_113_11530:  # 0m:0.000s
                            chown_113_11530()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=11531) as cd_stage_114_11531:  # 0m:10.055s
            cd_stage_114_11531()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=11532):  # 0m:10.054s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=11533) as should_copy_source_115_11533:  # 0m:0.001s
                    should_copy_source_115_11533()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=11534):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r".", prog_num=11535) as copy_file_to_dir_116_11535:  # 0m:0.001s
                            copy_file_to_dir_116_11535()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=11536) as chmod_and_chown_117_11536:  # 0m:0.000s
                            chmod_and_chown_117_11536()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=11537) as should_copy_source_118_11537:  # 0m:10.053s
                    should_copy_source_118_11537()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=11538):  # 0m:10.053s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=11539) as copy_dir_to_dir_119_11539:  # 0m:0.013s
                            copy_dir_to_dir_119_11539()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=11540) as unwtar_120_11540:  # 0m:10.039s
                            unwtar_120_11540()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=11541, recursive=True) as chown_121_11541:  # 0m:0.000s
                            chown_121_11541()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=11542) as cd_stage_122_11542:  # 0m:0.119s
            cd_stage_122_11542()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=11543):  # 0m:0.030s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11544) as should_copy_source_123_11544:  # 0m:0.013s
                    should_copy_source_123_11544()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=11545):  # 0m:0.013s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=11546) as copy_dir_to_dir_124_11546:  # 0m:0.012s
                            copy_dir_to_dir_124_11546()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=11547, recursive=True) as chown_125_11547:  # 0m:0.000s
                            chown_125_11547()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11548) as should_copy_source_126_11548:  # 0m:0.017s
                    should_copy_source_126_11548()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=11549):  # 0m:0.016s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=11550) as copy_dir_to_dir_127_11550:  # 0m:0.016s
                            copy_dir_to_dir_127_11550()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=11551, recursive=True) as chown_128_11551:  # 0m:0.000s
                            chown_128_11551()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=11552):  # 0m:0.089s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11553) as should_copy_source_129_11553:  # 0m:0.013s
                    should_copy_source_129_11553()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=11554):  # 0m:0.012s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=11555) as copy_dir_to_dir_130_11555:  # 0m:0.012s
                            copy_dir_to_dir_130_11555()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=11556, recursive=True) as chown_131_11556:  # 0m:0.000s
                            chown_131_11556()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11557) as should_copy_source_132_11557:  # 0m:0.076s
                    should_copy_source_132_11557()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=11558):  # 0m:0.076s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=11559) as copy_dir_to_dir_133_11559:  # 0m:0.075s
                            copy_dir_to_dir_133_11559()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=11560, recursive=True) as chown_134_11560:  # 0m:0.000s
                            chown_134_11560()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=11561) as cd_stage_135_11561:  # 0m:0.000s
            cd_stage_135_11561()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=11562):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=11563) as should_copy_source_136_11563:  # ?
                    should_copy_source_136_11563()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=11564):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=11565) as copy_file_to_dir_137_11565:  # ?
                            copy_file_to_dir_137_11565()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=11566) as chmod_and_chown_138_11566:  # 0m:0.000s
                            chmod_and_chown_138_11566()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=11567) as cd_stage_139_11567:  # 0m:0.034s
            cd_stage_139_11567()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=11568):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11569) as should_copy_source_140_11569:  # ?
                    should_copy_source_140_11569()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=11570):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=11571) as copy_dir_to_dir_141_11571:  # ?
                            copy_dir_to_dir_141_11571()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=11572, recursive=True) as chown_142_11572:  # 0m:0.001s
                            chown_142_11572()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=11573):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11574) as should_copy_source_143_11574:  # ?
                    should_copy_source_143_11574()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=11575):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=11576) as copy_dir_to_dir_144_11576:  # ?
                            copy_dir_to_dir_144_11576()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=11577, recursive=True) as chown_145_11577:  # 0m:0.001s
                            chown_145_11577()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=11578):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11579) as should_copy_source_146_11579:  # ?
                    should_copy_source_146_11579()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=11580):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11581) as copy_dir_to_dir_147_11581:  # ?
                            copy_dir_to_dir_147_11581()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=11582, recursive=True) as chown_148_11582:  # 0m:0.001s
                            chown_148_11582()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=11583):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11584) as should_copy_source_149_11584:  # ?
                    should_copy_source_149_11584()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=11585):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=11586) as copy_dir_to_dir_150_11586:  # ?
                            copy_dir_to_dir_150_11586()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=11587, recursive=True) as chown_151_11587:  # 0m:0.001s
                            chown_151_11587()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=11588):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11589) as should_copy_source_152_11589:  # ?
                    should_copy_source_152_11589()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=11590):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=11591) as copy_dir_to_dir_153_11591:  # ?
                            copy_dir_to_dir_153_11591()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=11592, recursive=True) as chown_154_11592:  # 0m:0.006s
                            chown_154_11592()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=11593):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11594) as should_copy_source_155_11594:  # ?
                    should_copy_source_155_11594()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=11595):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=11596) as copy_dir_to_dir_156_11596:  # ?
                            copy_dir_to_dir_156_11596()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=11597, recursive=True) as chown_157_11597:  # 0m:0.001s
                            chown_157_11597()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=11598):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11599) as should_copy_source_158_11599:  # ?
                    should_copy_source_158_11599()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=11600):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=11601) as copy_dir_to_dir_159_11601:  # ?
                            copy_dir_to_dir_159_11601()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=11602, recursive=True) as chown_160_11602:  # 0m:0.001s
                            chown_160_11602()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=11603):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11604) as should_copy_source_161_11604:  # ?
                    should_copy_source_161_11604()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=11605):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=11606) as copy_dir_to_dir_162_11606:  # ?
                            copy_dir_to_dir_162_11606()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=11607, recursive=True) as chown_163_11607:  # 0m:0.001s
                            chown_163_11607()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=11608):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11609) as should_copy_source_164_11609:  # ?
                    should_copy_source_164_11609()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=11610):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=11611) as copy_dir_to_dir_165_11611:  # ?
                            copy_dir_to_dir_165_11611()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=11612, recursive=True) as chown_166_11612:  # 0m:0.001s
                            chown_166_11612()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=11613):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11614) as should_copy_source_167_11614:  # ?
                    should_copy_source_167_11614()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=11615):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=11616) as copy_dir_to_dir_168_11616:  # ?
                            copy_dir_to_dir_168_11616()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=11617, recursive=True) as chown_169_11617:  # 0m:0.001s
                            chown_169_11617()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=11618):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11619) as should_copy_source_170_11619:  # ?
                    should_copy_source_170_11619()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=11620):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=11621) as copy_dir_to_dir_171_11621:  # ?
                            copy_dir_to_dir_171_11621()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=11622, recursive=True) as chown_172_11622:  # 0m:0.006s
                            chown_172_11622()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=11623):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11624) as should_copy_source_173_11624:  # ?
                    should_copy_source_173_11624()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=11625):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=11626) as copy_dir_to_dir_174_11626:  # ?
                            copy_dir_to_dir_174_11626()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=11627, recursive=True) as chown_175_11627:  # 0m:0.001s
                            chown_175_11627()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=11628):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11629) as should_copy_source_176_11629:  # ?
                    should_copy_source_176_11629()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=11630):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=11631) as copy_dir_to_dir_177_11631:  # ?
                            copy_dir_to_dir_177_11631()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=11632, recursive=True) as chown_178_11632:  # 0m:0.001s
                            chown_178_11632()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=11633):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11634) as should_copy_source_179_11634:  # ?
                    should_copy_source_179_11634()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=11635):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=11636) as copy_dir_to_dir_180_11636:  # ?
                            copy_dir_to_dir_180_11636()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=11637, recursive=True) as chown_181_11637:  # 0m:0.001s
                            chown_181_11637()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=11638):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11639) as should_copy_source_182_11639:  # ?
                    should_copy_source_182_11639()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=11640):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=11641) as copy_dir_to_dir_183_11641:  # ?
                            copy_dir_to_dir_183_11641()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=11642, recursive=True) as chown_184_11642:  # 0m:0.001s
                            chown_184_11642()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=11643):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11644) as should_copy_source_185_11644:  # ?
                    should_copy_source_185_11644()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=11645):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=11646) as copy_dir_to_dir_186_11646:  # ?
                            copy_dir_to_dir_186_11646()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=11647, recursive=True) as chown_187_11647:  # 0m:0.001s
                            chown_187_11647()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=11648):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11649) as should_copy_source_188_11649:  # ?
                    should_copy_source_188_11649()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=11650):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11651) as copy_dir_to_dir_189_11651:  # ?
                            copy_dir_to_dir_189_11651()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11652, recursive=True) as chown_190_11652:  # 0m:0.001s
                            chown_190_11652()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=11653):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11654) as should_copy_source_191_11654:  # ?
                    should_copy_source_191_11654()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=11655):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11656) as copy_dir_to_dir_192_11656:  # ?
                            copy_dir_to_dir_192_11656()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11657, recursive=True) as chown_193_11657:  # 0m:0.006s
                            chown_193_11657()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=11658):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11659) as should_copy_source_194_11659:  # ?
                    should_copy_source_194_11659()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=11660):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=11661) as copy_dir_to_dir_195_11661:  # ?
                            copy_dir_to_dir_195_11661()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=11662, recursive=True) as chown_196_11662:  # 0m:0.001s
                            chown_196_11662()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=11663) as cd_stage_197_11663:  # 0m:0.011s
            cd_stage_197_11663()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=11664):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11665) as should_copy_source_198_11665:  # ?
                    should_copy_source_198_11665()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=11666):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=11667) as copy_dir_to_dir_199_11667:  # ?
                            copy_dir_to_dir_199_11667()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=11668, recursive=True) as chown_200_11668:  # 0m:0.001s
                            chown_200_11668()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=11669):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11670) as should_copy_source_201_11670:  # ?
                    should_copy_source_201_11670()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=11671):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=11672) as copy_dir_to_dir_202_11672:  # ?
                            copy_dir_to_dir_202_11672()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=11673, recursive=True) as chown_203_11673:  # 0m:0.001s
                            chown_203_11673()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=11674):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11675) as should_copy_source_204_11675:  # ?
                    should_copy_source_204_11675()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=11676):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=11677) as copy_dir_to_dir_205_11677:  # ?
                            copy_dir_to_dir_205_11677()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=11678, recursive=True) as chown_206_11678:  # 0m:0.001s
                            chown_206_11678()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=11679):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11680) as should_copy_source_207_11680:  # ?
                    should_copy_source_207_11680()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=11681):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=11682) as copy_dir_to_dir_208_11682:  # ?
                            copy_dir_to_dir_208_11682()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=11683, recursive=True) as chown_209_11683:  # 0m:0.000s
                            chown_209_11683()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=11684):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11685) as should_copy_source_210_11685:  # ?
                    should_copy_source_210_11685()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=11686):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=11687) as copy_dir_to_dir_211_11687:  # ?
                            copy_dir_to_dir_211_11687()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=11688, recursive=True) as chown_212_11688:  # 0m:0.001s
                            chown_212_11688()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=11689):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11690) as should_copy_source_213_11690:  # ?
                    should_copy_source_213_11690()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=11691):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=11692) as copy_dir_to_dir_214_11692:  # ?
                            copy_dir_to_dir_214_11692()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=11693, recursive=True) as chown_215_11693:  # 0m:0.006s
                            chown_215_11693()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=11694):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11695) as should_copy_source_216_11695:  # ?
                    should_copy_source_216_11695()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=11696):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=11697) as copy_dir_to_dir_217_11697:  # ?
                            copy_dir_to_dir_217_11697()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=11698, recursive=True) as chown_218_11698:  # 0m:0.001s
                            chown_218_11698()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=11699) as cd_stage_219_11699:  # 0m:0.002s
            cd_stage_219_11699()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=11700):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11701) as should_copy_source_220_11701:  # ?
                    should_copy_source_220_11701()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=11702):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11703) as copy_dir_to_dir_221_11703:  # ?
                            copy_dir_to_dir_221_11703()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11704, recursive=True) as chown_222_11704:  # 0m:0.001s
                            chown_222_11704()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=11705):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11706) as should_copy_source_223_11706:  # ?
                    should_copy_source_223_11706()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=11707):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11708) as copy_dir_to_dir_224_11708:  # ?
                            copy_dir_to_dir_224_11708()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11709, recursive=True) as chown_225_11709:  # 0m:0.001s
                            chown_225_11709()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=11710) as cd_stage_226_11710:  # 0m:0.154s
            cd_stage_226_11710()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=11711):  # 0m:0.154s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11712) as should_copy_source_227_11712:  # 0m:0.015s
                    should_copy_source_227_11712()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=11713):  # 0m:0.014s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=11714) as unwtar_228_11714:  # 0m:0.014s
                            unwtar_228_11714()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11715) as should_copy_source_229_11715:  # 0m:0.140s
                    should_copy_source_229_11715()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=11716):  # 0m:0.139s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=11717) as unwtar_230_11717:  # 0m:0.139s
                            unwtar_230_11717()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=11718) as cd_stage_231_11718:  # 0m:0.021s
            cd_stage_231_11718()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=11719):  # 0m:0.021s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=11720) as should_copy_source_232_11720:  # 0m:0.021s
                    should_copy_source_232_11720()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=11721):  # 0m:0.021s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=11722) as unwtar_233_11722:  # 0m:0.020s
                            unwtar_233_11722()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=11723) as cd_stage_234_11723:  # 0m:2.015s
            cd_stage_234_11723()
            with Stage(r"copy", r"ARPlates v15.5.79.262", prog_num=11724):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11725) as should_copy_source_235_11725:  # ?
                    should_copy_source_235_11725()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=11726):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=11727) as copy_dir_to_dir_236_11727:  # ?
                            copy_dir_to_dir_236_11727()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=11728) as unwtar_237_11728:  # ?
                            unwtar_237_11728()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=11729, recursive=True) as chown_238_11729:  # 0m:0.001s
                            chown_238_11729()
            with Stage(r"copy", r"Abbey Road Vinyl v15.5.79.262", prog_num=11730):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11731) as should_copy_source_239_11731:  # ?
                    should_copy_source_239_11731()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=11732):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=11733) as copy_dir_to_dir_240_11733:  # ?
                            copy_dir_to_dir_240_11733()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=11734) as unwtar_241_11734:  # ?
                            unwtar_241_11734()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=11735, recursive=True) as chown_242_11735:  # 0m:0.001s
                            chown_242_11735()
            with Stage(r"copy", r"Aphex AX v15.5.79.262", prog_num=11736):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11737) as should_copy_source_243_11737:  # ?
                    should_copy_source_243_11737()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=11738):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=11739) as copy_dir_to_dir_244_11739:  # ?
                            copy_dir_to_dir_244_11739()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=11740) as unwtar_245_11740:  # ?
                            unwtar_245_11740()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=11741, recursive=True) as chown_246_11741:  # 0m:0.000s
                            chown_246_11741()
            with Stage(r"copy", r"AudioTrack v15.5.79.262", prog_num=11742):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11743) as should_copy_source_247_11743:  # ?
                    should_copy_source_247_11743()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=11744):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=11745) as copy_dir_to_dir_248_11745:  # ?
                            copy_dir_to_dir_248_11745()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=11746) as unwtar_249_11746:  # ?
                            unwtar_249_11746()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=11747, recursive=True) as chown_250_11747:  # 0m:0.001s
                            chown_250_11747()
            with Stage(r"copy", r"Bass Rider v15.5.79.262", prog_num=11748):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11749) as should_copy_source_251_11749:  # ?
                    should_copy_source_251_11749()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=11750):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=11751) as copy_dir_to_dir_252_11751:  # ?
                            copy_dir_to_dir_252_11751()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=11752) as unwtar_253_11752:  # ?
                            unwtar_253_11752()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=11753, recursive=True) as chown_254_11753:  # 0m:0.001s
                            chown_254_11753()
            with Stage(r"copy", r"Bass Slapper v15.5.79.262", prog_num=11754):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11755) as should_copy_source_255_11755:  # ?
                    should_copy_source_255_11755()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=11756):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=11757) as copy_dir_to_dir_256_11757:  # ?
                            copy_dir_to_dir_256_11757()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=11758) as unwtar_257_11758:  # ?
                            unwtar_257_11758()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=11759, recursive=True) as chown_258_11759:  # 0m:0.000s
                            chown_258_11759()
            with Stage(r"copy", r"Brauer Motion v15.5.79.262", prog_num=11760):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11761) as should_copy_source_259_11761:  # ?
                    should_copy_source_259_11761()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=11762):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=11763) as copy_dir_to_dir_260_11763:  # ?
                            copy_dir_to_dir_260_11763()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=11764) as unwtar_261_11764:  # ?
                            unwtar_261_11764()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=11765, recursive=True) as chown_262_11765:  # 0m:0.001s
                            chown_262_11765()
            with Stage(r"copy", r"Butch Vig Vocals v15.5.79.262", prog_num=11766):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11767) as should_copy_source_263_11767:  # ?
                    should_copy_source_263_11767()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=11768):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11769) as copy_dir_to_dir_264_11769:  # ?
                            copy_dir_to_dir_264_11769()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=11770) as unwtar_265_11770:  # ?
                            unwtar_265_11770()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=11771, recursive=True) as chown_266_11771:  # 0m:0.000s
                            chown_266_11771()
            with Stage(r"copy", r"C1 v15.5.79.262", prog_num=11772):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11773) as should_copy_source_267_11773:  # ?
                    should_copy_source_267_11773()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=11774):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=11775) as copy_dir_to_dir_268_11775:  # ?
                            copy_dir_to_dir_268_11775()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=11776) as unwtar_269_11776:  # ?
                            unwtar_269_11776()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C1.bundle", user_id=-1, group_id=-1, prog_num=11777, recursive=True) as chown_270_11777:  # 0m:0.001s
                            chown_270_11777()
            with Stage(r"copy", r"C4 v15.5.79.262", prog_num=11778):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11779) as should_copy_source_271_11779:  # ?
                    should_copy_source_271_11779()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=11780):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=11781) as copy_dir_to_dir_272_11781:  # ?
                            copy_dir_to_dir_272_11781()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=11782) as unwtar_273_11782:  # ?
                            unwtar_273_11782()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C4.bundle", user_id=-1, group_id=-1, prog_num=11783, recursive=True) as chown_274_11783:  # 0m:0.008s
                            chown_274_11783()
            with Stage(r"copy", r"CLA-2A v15.5.79.262", prog_num=11784):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11785) as should_copy_source_275_11785:  # ?
                    should_copy_source_275_11785()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=11786):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=11787) as copy_dir_to_dir_276_11787:  # ?
                            copy_dir_to_dir_276_11787()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=11788) as unwtar_277_11788:  # ?
                            unwtar_277_11788()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=11789, recursive=True) as chown_278_11789:  # 0m:0.001s
                            chown_278_11789()
            with Stage(r"copy", r"CLA-3A v15.5.79.262", prog_num=11790):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11791) as should_copy_source_279_11791:  # ?
                    should_copy_source_279_11791()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=11792):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=11793) as copy_dir_to_dir_280_11793:  # ?
                            copy_dir_to_dir_280_11793()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=11794) as unwtar_281_11794:  # ?
                            unwtar_281_11794()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=11795, recursive=True) as chown_282_11795:  # 0m:0.001s
                            chown_282_11795()
            with Stage(r"copy", r"CLA-76 v15.5.79.262", prog_num=11796):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11797) as should_copy_source_283_11797:  # ?
                    should_copy_source_283_11797()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=11798):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=11799) as copy_dir_to_dir_284_11799:  # ?
                            copy_dir_to_dir_284_11799()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=11800) as unwtar_285_11800:  # ?
                            unwtar_285_11800()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=11801, recursive=True) as chown_286_11801:  # 0m:0.001s
                            chown_286_11801()
            with Stage(r"copy", r"CLA Bass v15.5.79.262", prog_num=11802):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11803) as should_copy_source_287_11803:  # ?
                    should_copy_source_287_11803()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=11804):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=11805) as copy_dir_to_dir_288_11805:  # ?
                            copy_dir_to_dir_288_11805()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=11806) as unwtar_289_11806:  # ?
                            unwtar_289_11806()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=11807, recursive=True) as chown_290_11807:  # 0m:0.001s
                            chown_290_11807()
            with Stage(r"copy", r"CLA Guitars v15.5.79.262", prog_num=11808):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11809) as should_copy_source_291_11809:  # ?
                    should_copy_source_291_11809()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=11810):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=11811) as copy_dir_to_dir_292_11811:  # ?
                            copy_dir_to_dir_292_11811()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=11812) as unwtar_293_11812:  # ?
                            unwtar_293_11812()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=11813, recursive=True) as chown_294_11813:  # 0m:0.001s
                            chown_294_11813()
            with Stage(r"copy", r"CLA Unplugged v15.5.79.262", prog_num=11814):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11815) as should_copy_source_295_11815:  # ?
                    should_copy_source_295_11815()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=11816):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=11817) as copy_dir_to_dir_296_11817:  # ?
                            copy_dir_to_dir_296_11817()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=11818) as unwtar_297_11818:  # ?
                            unwtar_297_11818()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=11819, recursive=True) as chown_298_11819:  # 0m:0.001s
                            chown_298_11819()
            with Stage(r"copy", r"CLA Vocals v15.5.79.262", prog_num=11820):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11821) as should_copy_source_299_11821:  # ?
                    should_copy_source_299_11821()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=11822):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11823) as copy_dir_to_dir_300_11823:  # ?
                            copy_dir_to_dir_300_11823()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=11824) as unwtar_301_11824:  # ?
                            unwtar_301_11824()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=11825, recursive=True) as chown_302_11825:  # 0m:0.007s
                            chown_302_11825()
            with Stage(r"copy", r"Center v15.5.79.262", prog_num=11826):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11827) as should_copy_source_303_11827:  # ?
                    should_copy_source_303_11827()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=11828):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=11829) as copy_dir_to_dir_304_11829:  # ?
                            copy_dir_to_dir_304_11829()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=11830) as unwtar_305_11830:  # ?
                            unwtar_305_11830()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Center.bundle", user_id=-1, group_id=-1, prog_num=11831, recursive=True) as chown_306_11831:  # 0m:0.001s
                            chown_306_11831()
            with Stage(r"copy", r"Clarity Vx v15.5.79.262", prog_num=11832):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11833) as should_copy_source_307_11833:  # ?
                    should_copy_source_307_11833()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=11834):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=11835) as copy_dir_to_dir_308_11835:  # ?
                            copy_dir_to_dir_308_11835()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=11836) as unwtar_309_11836:  # ?
                            unwtar_309_11836()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=11837, recursive=True) as chown_310_11837:  # 0m:0.001s
                            chown_310_11837()
            with Stage(r"copy", r"Saphira v15.5.79.262", prog_num=11838):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11839) as should_copy_source_311_11839:  # ?
                    should_copy_source_311_11839()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=11840):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=11841) as copy_dir_to_dir_312_11841:  # ?
                            copy_dir_to_dir_312_11841()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=11842) as unwtar_313_11842:  # ?
                            unwtar_313_11842()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Saphira.bundle", user_id=-1, group_id=-1, prog_num=11843, recursive=True) as chown_314_11843:  # 0m:0.001s
                            chown_314_11843()
            with Stage(r"copy", r"Submarine v15.5.79.262", prog_num=11844):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11845) as should_copy_source_315_11845:  # ?
                    should_copy_source_315_11845()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=11846):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=11847) as copy_dir_to_dir_316_11847:  # ?
                            copy_dir_to_dir_316_11847()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=11848) as unwtar_317_11848:  # ?
                            unwtar_317_11848()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Submarine.bundle", user_id=-1, group_id=-1, prog_num=11849, recursive=True) as chown_318_11849:  # 0m:0.001s
                            chown_318_11849()
            with Stage(r"copy", r"DeBreath v15.5.79.262", prog_num=11850):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11851) as should_copy_source_319_11851:  # ?
                    should_copy_source_319_11851()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=11852):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=11853) as copy_dir_to_dir_320_11853:  # ?
                            copy_dir_to_dir_320_11853()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=11854) as unwtar_321_11854:  # ?
                            unwtar_321_11854()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=11855, recursive=True) as chown_322_11855:  # 0m:0.001s
                            chown_322_11855()
            with Stage(r"copy", r"DeEsser v15.5.79.262", prog_num=11856):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11857) as should_copy_source_323_11857:  # ?
                    should_copy_source_323_11857()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=11858):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=11859) as copy_dir_to_dir_324_11859:  # ?
                            copy_dir_to_dir_324_11859()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=11860) as unwtar_325_11860:  # ?
                            unwtar_325_11860()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=11861, recursive=True) as chown_326_11861:  # 0m:0.001s
                            chown_326_11861()
            with Stage(r"copy", r"Doppler v15.5.79.262", prog_num=11862):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11863) as should_copy_source_327_11863:  # ?
                    should_copy_source_327_11863()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=11864):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=11865) as copy_dir_to_dir_328_11865:  # ?
                            copy_dir_to_dir_328_11865()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=11866) as unwtar_329_11866:  # ?
                            unwtar_329_11866()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doppler.bundle", user_id=-1, group_id=-1, prog_num=11867, recursive=True) as chown_330_11867:  # 0m:0.001s
                            chown_330_11867()
            with Stage(r"copy", r"Doubler v15.5.79.262", prog_num=11868):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11869) as should_copy_source_331_11869:  # ?
                    should_copy_source_331_11869()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=11870):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=11871) as copy_dir_to_dir_332_11871:  # ?
                            copy_dir_to_dir_332_11871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=11872) as unwtar_333_11872:  # ?
                            unwtar_333_11872()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doubler.bundle", user_id=-1, group_id=-1, prog_num=11873, recursive=True) as chown_334_11873:  # 0m:0.006s
                            chown_334_11873()
            with Stage(r"copy", r"EMO-F2 v15.5.79.262", prog_num=11874):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11875) as should_copy_source_335_11875:  # ?
                    should_copy_source_335_11875()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=11876):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=11877) as copy_dir_to_dir_336_11877:  # ?
                            copy_dir_to_dir_336_11877()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=11878) as unwtar_337_11878:  # ?
                            unwtar_337_11878()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=11879, recursive=True) as chown_338_11879:  # 0m:0.001s
                            chown_338_11879()
            with Stage(r"copy", r"EMO-Q4 v15.5.79.262", prog_num=11880):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11881) as should_copy_source_339_11881:  # ?
                    should_copy_source_339_11881()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=11882):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=11883) as copy_dir_to_dir_340_11883:  # ?
                            copy_dir_to_dir_340_11883()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=11884) as unwtar_341_11884:  # ?
                            unwtar_341_11884()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=11885, recursive=True) as chown_342_11885:  # 0m:0.001s
                            chown_342_11885()
            with Stage(r"copy", r"EddieKramer DR v15.5.79.262", prog_num=11886):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11887) as should_copy_source_343_11887:  # ?
                    should_copy_source_343_11887()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=11888):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=11889) as copy_dir_to_dir_344_11889:  # ?
                            copy_dir_to_dir_344_11889()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=11890) as unwtar_345_11890:  # ?
                            unwtar_345_11890()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=11891, recursive=True) as chown_346_11891:  # 0m:0.000s
                            chown_346_11891()
            with Stage(r"copy", r"EddieKramer VC v15.5.79.262", prog_num=11892):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11893) as should_copy_source_347_11893:  # ?
                    should_copy_source_347_11893()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=11894):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=11895) as copy_dir_to_dir_348_11895:  # ?
                            copy_dir_to_dir_348_11895()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=11896) as unwtar_349_11896:  # ?
                            unwtar_349_11896()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=11897, recursive=True) as chown_350_11897:  # 0m:0.001s
                            chown_350_11897()
            with Stage(r"copy", r"Electric Grand 80 v15.5.79.262", prog_num=11898):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11899) as should_copy_source_351_11899:  # ?
                    should_copy_source_351_11899()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=11900):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=11901) as copy_dir_to_dir_352_11901:  # ?
                            copy_dir_to_dir_352_11901()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=11902) as unwtar_353_11902:  # ?
                            unwtar_353_11902()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=11903, recursive=True) as chown_354_11903:  # 0m:0.001s
                            chown_354_11903()
            with Stage(r"copy", r"Enigma v15.5.79.262", prog_num=11904):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11905) as should_copy_source_355_11905:  # ?
                    should_copy_source_355_11905()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=11906):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=11907) as copy_dir_to_dir_356_11907:  # ?
                            copy_dir_to_dir_356_11907()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=11908) as unwtar_357_11908:  # ?
                            unwtar_357_11908()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Enigma.bundle", user_id=-1, group_id=-1, prog_num=11909, recursive=True) as chown_358_11909:  # 0m:0.001s
                            chown_358_11909()
            with Stage(r"copy", r"GTRAmp v15.5.79.262", prog_num=11910):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11911) as should_copy_source_359_11911:  # ?
                    should_copy_source_359_11911()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=11912):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=11913) as copy_dir_to_dir_360_11913:  # ?
                            copy_dir_to_dir_360_11913()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=11914) as unwtar_361_11914:  # ?
                            unwtar_361_11914()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=11915, recursive=True) as chown_362_11915:  # 0m:0.001s
                            chown_362_11915()
            with Stage(r"copy", r"GTRStomp v15.5.79.262", prog_num=11916):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11917) as should_copy_source_363_11917:  # ?
                    should_copy_source_363_11917()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=11918):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=11919) as copy_dir_to_dir_364_11919:  # ?
                            copy_dir_to_dir_364_11919()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=11920) as unwtar_365_11920:  # ?
                            unwtar_365_11920()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=11921, recursive=True) as chown_366_11921:  # 0m:0.001s
                            chown_366_11921()
            with Stage(r"copy", r"GTRToolRack v15.5.79.262", prog_num=11922):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11923) as should_copy_source_367_11923:  # ?
                    should_copy_source_367_11923()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=11924):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=11925) as copy_dir_to_dir_368_11925:  # ?
                            copy_dir_to_dir_368_11925()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=11926) as unwtar_369_11926:  # ?
                            unwtar_369_11926()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=11927, recursive=True) as chown_370_11927:  # 0m:0.007s
                            chown_370_11927()
            with Stage(r"copy", r"GTRTuner v15.5.79.262", prog_num=11928):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11929) as should_copy_source_371_11929:  # ?
                    should_copy_source_371_11929()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=11930):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=11931) as copy_dir_to_dir_372_11931:  # ?
                            copy_dir_to_dir_372_11931()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=11932) as unwtar_373_11932:  # ?
                            unwtar_373_11932()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=11933, recursive=True) as chown_374_11933:  # 0m:0.001s
                            chown_374_11933()
            with Stage(r"copy", r"Greg Wells MixCentric v15.5.79.262", prog_num=11934):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11935) as should_copy_source_375_11935:  # ?
                    should_copy_source_375_11935()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=11936):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=11937) as copy_dir_to_dir_376_11937:  # ?
                            copy_dir_to_dir_376_11937()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=11938) as unwtar_377_11938:  # ?
                            unwtar_377_11938()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=11939, recursive=True) as chown_378_11939:  # 0m:0.001s
                            chown_378_11939()
            with Stage(r"copy", r"Greg Wells PianoCentric v15.5.79.262", prog_num=11940):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11941) as should_copy_source_379_11941:  # ?
                    should_copy_source_379_11941()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=11942):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=11943) as copy_dir_to_dir_380_11943:  # ?
                            copy_dir_to_dir_380_11943()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=11944) as unwtar_381_11944:  # ?
                            unwtar_381_11944()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=11945, recursive=True) as chown_382_11945:  # 0m:0.000s
                            chown_382_11945()
            with Stage(r"copy", r"Greg Wells ToneCentric v15.5.79.262", prog_num=11946):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11947) as should_copy_source_383_11947:  # ?
                    should_copy_source_383_11947()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=11948):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=11949) as copy_dir_to_dir_384_11949:  # ?
                            copy_dir_to_dir_384_11949()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=11950) as unwtar_385_11950:  # ?
                            unwtar_385_11950()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=11951, recursive=True) as chown_386_11951:  # 0m:0.001s
                            chown_386_11951()
            with Stage(r"copy", r"H-Comp v15.5.79.262", prog_num=11952):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11953) as should_copy_source_387_11953:  # ?
                    should_copy_source_387_11953()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=11954):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=11955) as copy_dir_to_dir_388_11955:  # ?
                            copy_dir_to_dir_388_11955()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=11956) as unwtar_389_11956:  # ?
                            unwtar_389_11956()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=11957, recursive=True) as chown_390_11957:  # 0m:0.001s
                            chown_390_11957()
            with Stage(r"copy", r"H-Delay v15.5.79.262", prog_num=11958):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11959) as should_copy_source_391_11959:  # ?
                    should_copy_source_391_11959()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=11960):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=11961) as copy_dir_to_dir_392_11961:  # ?
                            copy_dir_to_dir_392_11961()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=11962) as unwtar_393_11962:  # ?
                            unwtar_393_11962()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=11963, recursive=True) as chown_394_11963:  # 0m:0.001s
                            chown_394_11963()
            with Stage(r"copy", r"H-Reverb v15.5.79.262", prog_num=11964):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11965) as should_copy_source_395_11965:  # ?
                    should_copy_source_395_11965()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=11966):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=11967) as copy_dir_to_dir_396_11967:  # ?
                            copy_dir_to_dir_396_11967()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=11968) as unwtar_397_11968:  # ?
                            unwtar_397_11968()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=11969, recursive=True) as chown_398_11969:  # 0m:0.001s
                            chown_398_11969()
            with Stage(r"copy", r"IR-L v15.5.79.262", prog_num=11970):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11971) as should_copy_source_399_11971:  # ?
                    should_copy_source_399_11971()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=11972):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=11973) as copy_dir_to_dir_400_11973:  # ?
                            copy_dir_to_dir_400_11973()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=11974) as unwtar_401_11974:  # ?
                            unwtar_401_11974()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/IR-L.bundle", user_id=-1, group_id=-1, prog_num=11975, recursive=True) as chown_402_11975:  # 0m:0.007s
                            chown_402_11975()
            with Stage(r"copy", r"InPhase v15.5.79.262", prog_num=11976):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11977) as should_copy_source_403_11977:  # ?
                    should_copy_source_403_11977()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=11978):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=11979) as copy_dir_to_dir_404_11979:  # ?
                            copy_dir_to_dir_404_11979()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=11980) as unwtar_405_11980:  # ?
                            unwtar_405_11980()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase.bundle", user_id=-1, group_id=-1, prog_num=11981, recursive=True) as chown_406_11981:  # 0m:0.001s
                            chown_406_11981()
            with Stage(r"copy", r"InPhase LT v15.5.79.262", prog_num=11982):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11983) as should_copy_source_407_11983:  # ?
                    should_copy_source_407_11983()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=11984):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=11985) as copy_dir_to_dir_408_11985:  # ?
                            copy_dir_to_dir_408_11985()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=11986) as unwtar_409_11986:  # ?
                            unwtar_409_11986()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=11987, recursive=True) as chown_410_11987:  # 0m:0.001s
                            chown_410_11987()
            with Stage(r"copy", r"J37 v15.5.79.262", prog_num=11988):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11989) as should_copy_source_411_11989:  # ?
                    should_copy_source_411_11989()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=11990):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=11991) as copy_dir_to_dir_412_11991:  # ?
                            copy_dir_to_dir_412_11991()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=11992) as unwtar_413_11992:  # ?
                            unwtar_413_11992()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/J37.bundle", user_id=-1, group_id=-1, prog_num=11993, recursive=True) as chown_414_11993:  # 0m:0.001s
                            chown_414_11993()
            with Stage(r"copy", r"JJP-Vocals v15.5.79.262", prog_num=11994):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11995) as should_copy_source_415_11995:  # ?
                    should_copy_source_415_11995()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=11996):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11997) as copy_dir_to_dir_416_11997:  # ?
                            copy_dir_to_dir_416_11997()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=11998) as unwtar_417_11998:  # ?
                            unwtar_417_11998()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=11999, recursive=True) as chown_418_11999:  # 0m:0.001s
                            chown_418_11999()
            with Stage(r"copy", r"Key Detector v15.5.79.262", prog_num=12000):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12001) as should_copy_source_419_12001:  # ?
                    should_copy_source_419_12001()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=12002):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=12003) as copy_dir_to_dir_420_12003:  # ?
                            copy_dir_to_dir_420_12003()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=12004) as unwtar_421_12004:  # ?
                            unwtar_421_12004()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=12005, recursive=True) as chown_422_12005:  # 0m:0.001s
                            chown_422_12005()
            with Stage(r"copy", r"KingsMic v15.5.79.262", prog_num=12006):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12007) as should_copy_source_423_12007:  # ?
                    should_copy_source_423_12007()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=12008):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=12009) as copy_dir_to_dir_424_12009:  # ?
                            copy_dir_to_dir_424_12009()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=12010) as unwtar_425_12010:  # ?
                            unwtar_425_12010()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=12011, recursive=True) as chown_426_12011:  # 0m:0.001s
                            chown_426_12011()
            with Stage(r"copy", r"KramerHLS v15.5.79.262", prog_num=12012):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12013) as should_copy_source_427_12013:  # ?
                    should_copy_source_427_12013()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=12014):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=12015) as copy_dir_to_dir_428_12015:  # ?
                            copy_dir_to_dir_428_12015()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=12016) as unwtar_429_12016:  # ?
                            unwtar_429_12016()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=12017, recursive=True) as chown_430_12017:  # 0m:0.000s
                            chown_430_12017()
            with Stage(r"copy", r"KramerPIE v15.5.79.262", prog_num=12018):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12019) as should_copy_source_431_12019:  # ?
                    should_copy_source_431_12019()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=12020):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=12021) as copy_dir_to_dir_432_12021:  # ?
                            copy_dir_to_dir_432_12021()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=12022) as unwtar_433_12022:  # ?
                            unwtar_433_12022()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=12023, recursive=True) as chown_434_12023:  # 0m:0.001s
                            chown_434_12023()
            with Stage(r"copy", r"KramerTape v15.5.79.262", prog_num=12024):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12025) as should_copy_source_435_12025:  # ?
                    should_copy_source_435_12025()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=12026):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=12027) as copy_dir_to_dir_436_12027:  # ?
                            copy_dir_to_dir_436_12027()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=12028) as unwtar_437_12028:  # ?
                            unwtar_437_12028()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=12029, recursive=True) as chown_438_12029:  # 0m:0.001s
                            chown_438_12029()
            with Stage(r"copy", r"L1 v15.5.79.262", prog_num=12030):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12031) as should_copy_source_439_12031:  # ?
                    should_copy_source_439_12031()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=12032):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=12033) as copy_dir_to_dir_440_12033:  # ?
                            copy_dir_to_dir_440_12033()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=12034) as unwtar_441_12034:  # ?
                            unwtar_441_12034()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L1.bundle", user_id=-1, group_id=-1, prog_num=12035, recursive=True) as chown_442_12035:  # 0m:0.008s
                            chown_442_12035()
            with Stage(r"copy", r"L2 v15.5.79.262", prog_num=12036):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12037) as should_copy_source_443_12037:  # ?
                    should_copy_source_443_12037()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=12038):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=12039) as copy_dir_to_dir_444_12039:  # ?
                            copy_dir_to_dir_444_12039()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=12040) as unwtar_445_12040:  # ?
                            unwtar_445_12040()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L2.bundle", user_id=-1, group_id=-1, prog_num=12041, recursive=True) as chown_446_12041:  # 0m:0.001s
                            chown_446_12041()
            with Stage(r"copy", r"L3-16 v15.5.79.262", prog_num=12042):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12043) as should_copy_source_447_12043:  # ?
                    should_copy_source_447_12043()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=12044):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=12045) as copy_dir_to_dir_448_12045:  # ?
                            copy_dir_to_dir_448_12045()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=12046) as unwtar_449_12046:  # ?
                            unwtar_449_12046()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-16.bundle", user_id=-1, group_id=-1, prog_num=12047, recursive=True) as chown_450_12047:  # 0m:0.000s
                            chown_450_12047()
            with Stage(r"copy", r"L3-LL Multi v15.5.79.262", prog_num=12048):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12049) as should_copy_source_451_12049:  # ?
                    should_copy_source_451_12049()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=12050):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=12051) as copy_dir_to_dir_452_12051:  # ?
                            copy_dir_to_dir_452_12051()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=12052) as unwtar_453_12052:  # ?
                            unwtar_453_12052()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=12053, recursive=True) as chown_454_12053:  # 0m:0.001s
                            chown_454_12053()
            with Stage(r"copy", r"L3-LL Ultra v15.5.79.262", prog_num=12054):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12055) as should_copy_source_455_12055:  # ?
                    should_copy_source_455_12055()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=12056):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=12057) as copy_dir_to_dir_456_12057:  # ?
                            copy_dir_to_dir_456_12057()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=12058) as unwtar_457_12058:  # ?
                            unwtar_457_12058()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=12059, recursive=True) as chown_458_12059:  # 0m:0.000s
                            chown_458_12059()
            with Stage(r"copy", r"L3 Multi v15.5.79.262", prog_num=12060):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12061) as should_copy_source_459_12061:  # ?
                    should_copy_source_459_12061()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=12062):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=12063) as copy_dir_to_dir_460_12063:  # ?
                            copy_dir_to_dir_460_12063()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=12064) as unwtar_461_12064:  # ?
                            unwtar_461_12064()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=12065, recursive=True) as chown_462_12065:  # 0m:0.001s
                            chown_462_12065()
            with Stage(r"copy", r"L3 Ultra v15.5.79.262", prog_num=12066):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12067) as should_copy_source_463_12067:  # ?
                    should_copy_source_463_12067()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=12068):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=12069) as copy_dir_to_dir_464_12069:  # ?
                            copy_dir_to_dir_464_12069()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=12070) as unwtar_465_12070:  # ?
                            unwtar_465_12070()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=12071, recursive=True) as chown_466_12071:  # 0m:0.001s
                            chown_466_12071()
            with Stage(r"copy", r"LinEQ v15.5.79.262", prog_num=12072):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12073) as should_copy_source_467_12073:  # ?
                    should_copy_source_467_12073()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=12074):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=12075) as copy_dir_to_dir_468_12075:  # ?
                            copy_dir_to_dir_468_12075()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=12076) as unwtar_469_12076:  # ?
                            unwtar_469_12076()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=12077, recursive=True) as chown_470_12077:  # 0m:0.001s
                            chown_470_12077()
            with Stage(r"copy", r"LinMB v15.5.79.262", prog_num=12078):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12079) as should_copy_source_471_12079:  # ?
                    should_copy_source_471_12079()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=12080):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=12081) as copy_dir_to_dir_472_12081:  # ?
                            copy_dir_to_dir_472_12081()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=12082) as unwtar_473_12082:  # ?
                            unwtar_473_12082()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinMB.bundle", user_id=-1, group_id=-1, prog_num=12083, recursive=True) as chown_474_12083:  # 0m:0.008s
                            chown_474_12083()
            with Stage(r"copy", r"LoAir v15.5.79.262", prog_num=12084):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12085) as should_copy_source_475_12085:  # ?
                    should_copy_source_475_12085()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=12086):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=12087) as copy_dir_to_dir_476_12087:  # ?
                            copy_dir_to_dir_476_12087()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=12088) as unwtar_477_12088:  # ?
                            unwtar_477_12088()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LoAir.bundle", user_id=-1, group_id=-1, prog_num=12089, recursive=True) as chown_478_12089:  # 0m:0.001s
                            chown_478_12089()
            with Stage(r"copy", r"Lofi Space v15.5.79.262", prog_num=12090):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12091) as should_copy_source_479_12091:  # ?
                    should_copy_source_479_12091()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=12092):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=12093) as copy_dir_to_dir_480_12093:  # ?
                            copy_dir_to_dir_480_12093()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=12094) as unwtar_481_12094:  # ?
                            unwtar_481_12094()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=12095, recursive=True) as chown_482_12095:  # 0m:0.000s
                            chown_482_12095()
            with Stage(r"copy", r"MV2 v15.5.79.262", prog_num=12096):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12097) as should_copy_source_483_12097:  # ?
                    should_copy_source_483_12097()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=12098):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=12099) as copy_dir_to_dir_484_12099:  # ?
                            copy_dir_to_dir_484_12099()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=12100) as unwtar_485_12100:  # ?
                            unwtar_485_12100()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MV2.bundle", user_id=-1, group_id=-1, prog_num=12101, recursive=True) as chown_486_12101:  # 0m:0.000s
                            chown_486_12101()
            with Stage(r"copy", r"Magma Springs v15.5.79.262", prog_num=12102):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12103) as should_copy_source_487_12103:  # ?
                    should_copy_source_487_12103()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=12104):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=12105) as copy_dir_to_dir_488_12105:  # ?
                            copy_dir_to_dir_488_12105()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=12106) as unwtar_489_12106:  # ?
                            unwtar_489_12106()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=12107, recursive=True) as chown_490_12107:  # 0m:0.000s
                            chown_490_12107()
            with Stage(r"copy", r"MannyM-TripleD v15.5.79.262", prog_num=12108):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12109) as should_copy_source_491_12109:  # ?
                    should_copy_source_491_12109()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=12110):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=12111) as copy_dir_to_dir_492_12111:  # ?
                            copy_dir_to_dir_492_12111()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=12112) as unwtar_493_12112:  # ?
                            unwtar_493_12112()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=12113, recursive=True) as chown_494_12113:  # 0m:0.000s
                            chown_494_12113()
            with Stage(r"copy", r"Maserati DRM v15.5.79.262", prog_num=12114):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12115) as should_copy_source_495_12115:  # ?
                    should_copy_source_495_12115()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=12116):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=12117) as copy_dir_to_dir_496_12117:  # ?
                            copy_dir_to_dir_496_12117()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=12118) as unwtar_497_12118:  # ?
                            unwtar_497_12118()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=12119, recursive=True) as chown_498_12119:  # 0m:0.001s
                            chown_498_12119()
            with Stage(r"copy", r"Maserati VX1 v15.5.79.262", prog_num=12120):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12121) as should_copy_source_499_12121:  # ?
                    should_copy_source_499_12121()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=12122):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=12123) as copy_dir_to_dir_500_12123:  # ?
                            copy_dir_to_dir_500_12123()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=12124) as unwtar_501_12124:  # ?
                            unwtar_501_12124()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=12125, recursive=True) as chown_502_12125:  # 0m:0.001s
                            chown_502_12125()
            with Stage(r"copy", r"MaxxBass v15.5.79.262", prog_num=12126):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12127) as should_copy_source_503_12127:  # ?
                    should_copy_source_503_12127()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=12128):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=12129) as copy_dir_to_dir_504_12129:  # ?
                            copy_dir_to_dir_504_12129()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=12130) as unwtar_505_12130:  # ?
                            unwtar_505_12130()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=12131, recursive=True) as chown_506_12131:  # 0m:0.001s
                            chown_506_12131()
            with Stage(r"copy", r"MaxxVolume v15.5.79.262", prog_num=12132):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12133) as should_copy_source_507_12133:  # ?
                    should_copy_source_507_12133()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=12134):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=12135) as copy_dir_to_dir_508_12135:  # ?
                            copy_dir_to_dir_508_12135()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=12136) as unwtar_509_12136:  # ?
                            unwtar_509_12136()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=12137, recursive=True) as chown_510_12137:  # 0m:0.001s
                            chown_510_12137()
            with Stage(r"copy", r"MetaFilter v15.5.79.262", prog_num=12138):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12139) as should_copy_source_511_12139:  # ?
                    should_copy_source_511_12139()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=12140):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=12141) as copy_dir_to_dir_512_12141:  # ?
                            copy_dir_to_dir_512_12141()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=12142) as unwtar_513_12142:  # ?
                            unwtar_513_12142()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=12143, recursive=True) as chown_514_12143:  # 0m:0.001s
                            chown_514_12143()
            with Stage(r"copy", r"MetaFlanger v15.5.79.262", prog_num=12144):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12145) as should_copy_source_515_12145:  # ?
                    should_copy_source_515_12145()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=12146):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12147) as copy_dir_to_dir_516_12147:  # ?
                            copy_dir_to_dir_516_12147()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=12148) as unwtar_517_12148:  # ?
                            unwtar_517_12148()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=12149, recursive=True) as chown_518_12149:  # 0m:0.006s
                            chown_518_12149()
            with Stage(r"copy", r"MondoMod v15.5.79.262", prog_num=12150):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12151) as should_copy_source_519_12151:  # ?
                    should_copy_source_519_12151()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=12152):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=12153) as copy_dir_to_dir_520_12153:  # ?
                            copy_dir_to_dir_520_12153()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=12154) as unwtar_521_12154:  # ?
                            unwtar_521_12154()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=12155, recursive=True) as chown_522_12155:  # 0m:0.000s
                            chown_522_12155()
            with Stage(r"copy", r"Morphoder v15.5.79.262", prog_num=12156):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12157) as should_copy_source_523_12157:  # ?
                    should_copy_source_523_12157()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=12158):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=12159) as copy_dir_to_dir_524_12159:  # ?
                            copy_dir_to_dir_524_12159()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=12160) as unwtar_525_12160:  # ?
                            unwtar_525_12160()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=12161, recursive=True) as chown_526_12161:  # 0m:0.001s
                            chown_526_12161()
            with Stage(r"copy", r"NLS v15.5.79.262", prog_num=12162):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12163) as should_copy_source_527_12163:  # ?
                    should_copy_source_527_12163()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=12164):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=12165) as copy_dir_to_dir_528_12165:  # ?
                            copy_dir_to_dir_528_12165()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=12166) as unwtar_529_12166:  # ?
                            unwtar_529_12166()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NLS.bundle", user_id=-1, group_id=-1, prog_num=12167, recursive=True) as chown_530_12167:  # 0m:0.001s
                            chown_530_12167()
            with Stage(r"copy", r"NX v15.5.79.262", prog_num=12168):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12169) as should_copy_source_531_12169:  # ?
                    should_copy_source_531_12169()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=12170):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=12171) as copy_dir_to_dir_532_12171:  # ?
                            copy_dir_to_dir_532_12171()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=12172) as unwtar_533_12172:  # ?
                            unwtar_533_12172()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NX.bundle", user_id=-1, group_id=-1, prog_num=12173, recursive=True) as chown_534_12173:  # 0m:0.001s
                            chown_534_12173()
            with Stage(r"copy", r"OKDriver v15.5.79.262", prog_num=12174):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12175) as should_copy_source_535_12175:  # ?
                    should_copy_source_535_12175()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=12176):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=12177) as copy_dir_to_dir_536_12177:  # ?
                            copy_dir_to_dir_536_12177()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=12178) as unwtar_537_12178:  # ?
                            unwtar_537_12178()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=12179, recursive=True) as chown_538_12179:  # 0m:0.001s
                            chown_538_12179()
            with Stage(r"copy", r"OKFilter v15.5.79.262", prog_num=12180):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12181) as should_copy_source_539_12181:  # ?
                    should_copy_source_539_12181()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=12182):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=12183) as copy_dir_to_dir_540_12183:  # ?
                            copy_dir_to_dir_540_12183()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=12184) as unwtar_541_12184:  # ?
                            unwtar_541_12184()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=12185, recursive=True) as chown_542_12185:  # 0m:0.000s
                            chown_542_12185()
            with Stage(r"copy", r"OKPhatter v15.5.79.262", prog_num=12186):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12187) as should_copy_source_543_12187:  # ?
                    should_copy_source_543_12187()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=12188):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=12189) as copy_dir_to_dir_544_12189:  # ?
                            copy_dir_to_dir_544_12189()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=12190) as unwtar_545_12190:  # ?
                            unwtar_545_12190()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=12191, recursive=True) as chown_546_12191:  # 0m:0.000s
                            chown_546_12191()
            with Stage(r"copy", r"OKPumper v15.5.79.262", prog_num=12192):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12193) as should_copy_source_547_12193:  # ?
                    should_copy_source_547_12193()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=12194):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=12195) as copy_dir_to_dir_548_12195:  # ?
                            copy_dir_to_dir_548_12195()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=12196) as unwtar_549_12196:  # ?
                            unwtar_549_12196()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=12197, recursive=True) as chown_550_12197:  # 0m:0.001s
                            chown_550_12197()
            with Stage(r"copy", r"PAZ v15.5.79.262", prog_num=12198):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12199) as should_copy_source_551_12199:  # ?
                    should_copy_source_551_12199()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=12200):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=12201) as copy_dir_to_dir_552_12201:  # ?
                            copy_dir_to_dir_552_12201()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=12202) as unwtar_553_12202:  # ?
                            unwtar_553_12202()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PAZ.bundle", user_id=-1, group_id=-1, prog_num=12203, recursive=True) as chown_554_12203:  # 0m:0.001s
                            chown_554_12203()
            with Stage(r"copy", r"PS22 v15.5.79.262", prog_num=12204):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12205) as should_copy_source_555_12205:  # ?
                    should_copy_source_555_12205()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=12206):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=12207) as copy_dir_to_dir_556_12207:  # ?
                            copy_dir_to_dir_556_12207()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=12208) as unwtar_557_12208:  # ?
                            unwtar_557_12208()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PS22.bundle", user_id=-1, group_id=-1, prog_num=12209, recursive=True) as chown_558_12209:  # 0m:0.001s
                            chown_558_12209()
            with Stage(r"copy", r"PuigChild v15.5.79.262", prog_num=12210):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12211) as should_copy_source_559_12211:  # ?
                    should_copy_source_559_12211()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=12212):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=12213) as copy_dir_to_dir_560_12213:  # ?
                            copy_dir_to_dir_560_12213()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=12214) as unwtar_561_12214:  # ?
                            unwtar_561_12214()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=12215, recursive=True) as chown_562_12215:  # 0m:0.008s
                            chown_562_12215()
            with Stage(r"copy", r"PuigTec v15.5.79.262", prog_num=12216):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12217) as should_copy_source_563_12217:  # ?
                    should_copy_source_563_12217()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=12218):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=12219) as copy_dir_to_dir_564_12219:  # ?
                            copy_dir_to_dir_564_12219()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=12220) as unwtar_565_12220:  # ?
                            unwtar_565_12220()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=12221, recursive=True) as chown_566_12221:  # 0m:0.001s
                            chown_566_12221()
            with Stage(r"copy", r"Q10 v15.5.79.262", prog_num=12222):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12223) as should_copy_source_567_12223:  # ?
                    should_copy_source_567_12223()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=12224):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=12225) as copy_dir_to_dir_568_12225:  # ?
                            copy_dir_to_dir_568_12225()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=12226) as unwtar_569_12226:  # ?
                            unwtar_569_12226()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q10.bundle", user_id=-1, group_id=-1, prog_num=12227, recursive=True) as chown_570_12227:  # 0m:0.001s
                            chown_570_12227()
            with Stage(r"copy", r"Q-Clone v15.5.79.262", prog_num=12228):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12229) as should_copy_source_571_12229:  # ?
                    should_copy_source_571_12229()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=12230):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=12231) as copy_dir_to_dir_572_12231:  # ?
                            copy_dir_to_dir_572_12231()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=12232) as unwtar_573_12232:  # ?
                            unwtar_573_12232()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=12233, recursive=True) as chown_574_12233:  # 0m:0.000s
                            chown_574_12233()
            with Stage(r"copy", r"RBass v15.5.79.262", prog_num=12234):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12235) as should_copy_source_575_12235:  # ?
                    should_copy_source_575_12235()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=12236):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=12237) as copy_dir_to_dir_576_12237:  # ?
                            copy_dir_to_dir_576_12237()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=12238) as unwtar_577_12238:  # ?
                            unwtar_577_12238()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RBass.bundle", user_id=-1, group_id=-1, prog_num=12239, recursive=True) as chown_578_12239:  # 0m:0.001s
                            chown_578_12239()
            with Stage(r"copy", r"RChannel v15.5.79.262", prog_num=12240):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12241) as should_copy_source_579_12241:  # ?
                    should_copy_source_579_12241()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=12242):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=12243) as copy_dir_to_dir_580_12243:  # ?
                            copy_dir_to_dir_580_12243()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=12244) as unwtar_581_12244:  # ?
                            unwtar_581_12244()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RChannel.bundle", user_id=-1, group_id=-1, prog_num=12245, recursive=True) as chown_582_12245:  # 0m:0.001s
                            chown_582_12245()
            with Stage(r"copy", r"RComp v15.5.79.262", prog_num=12246):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12247) as should_copy_source_583_12247:  # ?
                    should_copy_source_583_12247()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=12248):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=12249) as copy_dir_to_dir_584_12249:  # ?
                            copy_dir_to_dir_584_12249()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=12250) as unwtar_585_12250:  # ?
                            unwtar_585_12250()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RComp.bundle", user_id=-1, group_id=-1, prog_num=12251, recursive=True) as chown_586_12251:  # 0m:0.000s
                            chown_586_12251()
            with Stage(r"copy", r"RDeEsser v15.5.79.262", prog_num=12252):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12253) as should_copy_source_587_12253:  # ?
                    should_copy_source_587_12253()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=12254):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=12255) as copy_dir_to_dir_588_12255:  # ?
                            copy_dir_to_dir_588_12255()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=12256) as unwtar_589_12256:  # ?
                            unwtar_589_12256()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=12257, recursive=True) as chown_590_12257:  # 0m:0.000s
                            chown_590_12257()
            with Stage(r"copy", r"REDD17 v15.5.79.262", prog_num=12258):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12259) as should_copy_source_591_12259:  # ?
                    should_copy_source_591_12259()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=12260):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=12261) as copy_dir_to_dir_592_12261:  # ?
                            copy_dir_to_dir_592_12261()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=12262) as unwtar_593_12262:  # ?
                            unwtar_593_12262()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD17.bundle", user_id=-1, group_id=-1, prog_num=12263, recursive=True) as chown_594_12263:  # 0m:0.000s
                            chown_594_12263()
            with Stage(r"copy", r"REDD37-51 v15.5.79.262", prog_num=12264):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12265) as should_copy_source_595_12265:  # ?
                    should_copy_source_595_12265()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=12266):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=12267) as copy_dir_to_dir_596_12267:  # ?
                            copy_dir_to_dir_596_12267()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=12268) as unwtar_597_12268:  # ?
                            unwtar_597_12268()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=12269, recursive=True) as chown_598_12269:  # 0m:0.000s
                            chown_598_12269()
            with Stage(r"copy", r"REQ v15.5.79.262", prog_num=12270):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12271) as should_copy_source_599_12271:  # ?
                    should_copy_source_599_12271()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=12272):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=12273) as copy_dir_to_dir_600_12273:  # ?
                            copy_dir_to_dir_600_12273()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=12274) as unwtar_601_12274:  # ?
                            unwtar_601_12274()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REQ.bundle", user_id=-1, group_id=-1, prog_num=12275, recursive=True) as chown_602_12275:  # 0m:0.007s
                            chown_602_12275()
            with Stage(r"copy", r"RS56 v15.5.79.262", prog_num=12276):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12277) as should_copy_source_603_12277:  # ?
                    should_copy_source_603_12277()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=12278):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=12279) as copy_dir_to_dir_604_12279:  # ?
                            copy_dir_to_dir_604_12279()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=12280) as unwtar_605_12280:  # ?
                            unwtar_605_12280()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RS56.bundle", user_id=-1, group_id=-1, prog_num=12281, recursive=True) as chown_606_12281:  # 0m:0.001s
                            chown_606_12281()
            with Stage(r"copy", r"RVerb v15.5.79.262", prog_num=12282):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12283) as should_copy_source_607_12283:  # ?
                    should_copy_source_607_12283()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=12284):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=12285) as copy_dir_to_dir_608_12285:  # ?
                            copy_dir_to_dir_608_12285()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=12286) as unwtar_609_12286:  # ?
                            unwtar_609_12286()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVerb.bundle", user_id=-1, group_id=-1, prog_num=12287, recursive=True) as chown_610_12287:  # 0m:0.000s
                            chown_610_12287()
            with Stage(r"copy", r"RVox v15.5.79.262", prog_num=12288):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12289) as should_copy_source_611_12289:  # ?
                    should_copy_source_611_12289()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=12290):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=12291) as copy_dir_to_dir_612_12291:  # ?
                            copy_dir_to_dir_612_12291()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=12292) as unwtar_613_12292:  # ?
                            unwtar_613_12292()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVox.bundle", user_id=-1, group_id=-1, prog_num=12293, recursive=True) as chown_614_12293:  # 0m:0.001s
                            chown_614_12293()
            with Stage(r"copy", r"Reel ADT v15.5.79.262", prog_num=12294):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12295) as should_copy_source_615_12295:  # ?
                    should_copy_source_615_12295()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=12296):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=12297) as copy_dir_to_dir_616_12297:  # ?
                            copy_dir_to_dir_616_12297()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=12298) as unwtar_617_12298:  # ?
                            unwtar_617_12298()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=12299, recursive=True) as chown_618_12299:  # 0m:0.000s
                            chown_618_12299()
            with Stage(r"copy", r"RenAxx v15.5.79.262", prog_num=12300):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12301) as should_copy_source_619_12301:  # ?
                    should_copy_source_619_12301()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=12302):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=12303) as copy_dir_to_dir_620_12303:  # ?
                            copy_dir_to_dir_620_12303()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=12304) as unwtar_621_12304:  # ?
                            unwtar_621_12304()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=12305, recursive=True) as chown_622_12305:  # 0m:0.000s
                            chown_622_12305()
            with Stage(r"copy", r"Retro Fi v15.5.79.262", prog_num=12306):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12307) as should_copy_source_623_12307:  # ?
                    should_copy_source_623_12307()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=12308):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=12309) as copy_dir_to_dir_624_12309:  # ?
                            copy_dir_to_dir_624_12309()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=12310) as unwtar_625_12310:  # ?
                            unwtar_625_12310()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=12311, recursive=True) as chown_626_12311:  # 0m:0.001s
                            chown_626_12311()
            with Stage(r"copy", r"S1 v15.5.79.262", prog_num=12312):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12313) as should_copy_source_627_12313:  # ?
                    should_copy_source_627_12313()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=12314):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=12315) as copy_dir_to_dir_628_12315:  # ?
                            copy_dir_to_dir_628_12315()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=12316) as unwtar_629_12316:  # ?
                            unwtar_629_12316()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/S1.bundle", user_id=-1, group_id=-1, prog_num=12317, recursive=True) as chown_630_12317:  # 0m:0.001s
                            chown_630_12317()
            with Stage(r"copy", r"Scheps 73 v15.5.79.262", prog_num=12318):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12319) as should_copy_source_631_12319:  # ?
                    should_copy_source_631_12319()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=12320):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=12321) as copy_dir_to_dir_632_12321:  # ?
                            copy_dir_to_dir_632_12321()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=12322) as unwtar_633_12322:  # ?
                            unwtar_633_12322()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=12323, recursive=True) as chown_634_12323:  # 0m:0.000s
                            chown_634_12323()
            with Stage(r"copy", r"Scheps Omni Channel v15.5.79.262", prog_num=12324):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12325) as should_copy_source_635_12325:  # ?
                    should_copy_source_635_12325()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=12326):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=12327) as copy_dir_to_dir_636_12327:  # ?
                            copy_dir_to_dir_636_12327()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=12328) as unwtar_637_12328:  # ?
                            unwtar_637_12328()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=12329, recursive=True) as chown_638_12329:  # 0m:0.001s
                            chown_638_12329()
            with Stage(r"copy", r"Scheps Parallel Particles v15.5.79.262", prog_num=12330):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12331) as should_copy_source_639_12331:  # ?
                    should_copy_source_639_12331()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=12332):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=12333) as copy_dir_to_dir_640_12333:  # ?
                            copy_dir_to_dir_640_12333()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=12334) as unwtar_641_12334:  # ?
                            unwtar_641_12334()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=12335, recursive=True) as chown_642_12335:  # 0m:0.001s
                            chown_642_12335()
            with Stage(r"copy", r"Sibilance v15.5.79.262", prog_num=12336):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12337) as should_copy_source_643_12337:  # ?
                    should_copy_source_643_12337()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=12338):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=12339) as copy_dir_to_dir_644_12339:  # ?
                            copy_dir_to_dir_644_12339()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=12340) as unwtar_645_12340:  # ?
                            unwtar_645_12340()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=12341, recursive=True) as chown_646_12341:  # 0m:0.000s
                            chown_646_12341()
            with Stage(r"copy", r"Emo Signal Generator v15.5.79.262", prog_num=12342):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12343) as should_copy_source_647_12343:  # ?
                    should_copy_source_647_12343()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=12344):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=12345) as copy_dir_to_dir_648_12345:  # ?
                            copy_dir_to_dir_648_12345()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=12346) as unwtar_649_12346:  # ?
                            unwtar_649_12346()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=12347, recursive=True) as chown_650_12347:  # 0m:0.001s
                            chown_650_12347()
            with Stage(r"copy", r"Silk Vocal v15.10.46.293", prog_num=12348):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12349) as should_copy_source_651_12349:  # ?
                    should_copy_source_651_12349()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=12350):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=12351) as copy_dir_to_dir_652_12351:  # ?
                            copy_dir_to_dir_652_12351()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=12352) as unwtar_653_12352:  # ?
                            unwtar_653_12352()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=12353, recursive=True) as chown_654_12353:  # 0m:0.001s
                            chown_654_12353()
            with Stage(r"copy", r"Smack Attack v15.5.79.262", prog_num=12354):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12355) as should_copy_source_655_12355:  # ?
                    should_copy_source_655_12355()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=12356):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=12357) as copy_dir_to_dir_656_12357:  # ?
                            copy_dir_to_dir_656_12357()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=12358) as unwtar_657_12358:  # ?
                            unwtar_657_12358()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=12359, recursive=True) as chown_658_12359:  # 0m:0.001s
                            chown_658_12359()
            with Stage(r"copy", r"SoundShifter v15.5.79.262", prog_num=12360):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12361) as should_copy_source_659_12361:  # ?
                    should_copy_source_659_12361()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=12362):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=12363) as copy_dir_to_dir_660_12363:  # ?
                            copy_dir_to_dir_660_12363()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=12364) as unwtar_661_12364:  # ?
                            unwtar_661_12364()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=12365, recursive=True) as chown_662_12365:  # 0m:0.001s
                            chown_662_12365()
            with Stage(r"copy", r"Spherix Immersive Compressor v15.5.79.262", prog_num=12366):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12367) as should_copy_source_663_12367:  # ?
                    should_copy_source_663_12367()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=12368):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=12369) as copy_dir_to_dir_664_12369:  # ?
                            copy_dir_to_dir_664_12369()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=12370) as unwtar_665_12370:  # ?
                            unwtar_665_12370()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=12371, recursive=True) as chown_666_12371:  # 0m:0.001s
                            chown_666_12371()
            with Stage(r"copy", r"Spherix Immersive Limiter v15.5.79.262", prog_num=12372):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12373) as should_copy_source_667_12373:  # ?
                    should_copy_source_667_12373()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=12374):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=12375) as copy_dir_to_dir_668_12375:  # ?
                            copy_dir_to_dir_668_12375()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=12376) as unwtar_669_12376:  # ?
                            unwtar_669_12376()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=12377, recursive=True) as chown_670_12377:  # 0m:0.001s
                            chown_670_12377()
            with Stage(r"copy", r"SuperTap v15.5.79.262", prog_num=12378):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12379) as should_copy_source_671_12379:  # ?
                    should_copy_source_671_12379()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=12380):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=12381) as copy_dir_to_dir_672_12381:  # ?
                            copy_dir_to_dir_672_12381()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=12382) as unwtar_673_12382:  # ?
                            unwtar_673_12382()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=12383, recursive=True) as chown_674_12383:  # 0m:0.007s
                            chown_674_12383()
            with Stage(r"copy", r"TG12345 v15.5.79.262", prog_num=12384):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12385) as should_copy_source_675_12385:  # ?
                    should_copy_source_675_12385()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=12386):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=12387) as copy_dir_to_dir_676_12387:  # ?
                            copy_dir_to_dir_676_12387()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=12388) as unwtar_677_12388:  # ?
                            unwtar_677_12388()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TG12345.bundle", user_id=-1, group_id=-1, prog_num=12389, recursive=True) as chown_678_12389:  # 0m:0.001s
                            chown_678_12389()
            with Stage(r"copy", r"AR TG Meter Bridge v15.5.79.262", prog_num=12390):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12391) as should_copy_source_679_12391:  # ?
                    should_copy_source_679_12391()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=12392):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=12393) as copy_dir_to_dir_680_12393:  # ?
                            copy_dir_to_dir_680_12393()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=12394) as unwtar_681_12394:  # ?
                            unwtar_681_12394()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=12395, recursive=True) as chown_682_12395:  # 0m:0.001s
                            chown_682_12395()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v15.5.79.262", prog_num=12396):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12397) as should_copy_source_683_12397:  # ?
                    should_copy_source_683_12397()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=12398):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=12399) as copy_dir_to_dir_684_12399:  # ?
                            copy_dir_to_dir_684_12399()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=12400) as unwtar_685_12400:  # ?
                            unwtar_685_12400()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=12401, recursive=True) as chown_686_12401:  # 0m:0.000s
                            chown_686_12401()
            with Stage(r"copy", r"TransX v15.5.79.262", prog_num=12402):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12403) as should_copy_source_687_12403:  # ?
                    should_copy_source_687_12403()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=12404):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=12405) as copy_dir_to_dir_688_12405:  # ?
                            copy_dir_to_dir_688_12405()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=12406) as unwtar_689_12406:  # ?
                            unwtar_689_12406()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TransX.bundle", user_id=-1, group_id=-1, prog_num=12407, recursive=True) as chown_690_12407:  # 0m:0.001s
                            chown_690_12407()
            with Stage(r"copy", r"TrueVerb v15.5.79.262", prog_num=12408):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12409) as should_copy_source_691_12409:  # ?
                    should_copy_source_691_12409()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=12410):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=12411) as copy_dir_to_dir_692_12411:  # ?
                            copy_dir_to_dir_692_12411()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=12412) as unwtar_693_12412:  # ?
                            unwtar_693_12412()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=12413, recursive=True) as chown_694_12413:  # 0m:0.001s
                            chown_694_12413()
            with Stage(r"copy", r"UM v15.5.79.262", prog_num=12414):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12415) as should_copy_source_695_12415:  # ?
                    should_copy_source_695_12415()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=12416):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=12417) as copy_dir_to_dir_696_12417:  # ?
                            copy_dir_to_dir_696_12417()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=12418) as unwtar_697_12418:  # ?
                            unwtar_697_12418()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UM.bundle", user_id=-1, group_id=-1, prog_num=12419, recursive=True) as chown_698_12419:  # 0m:0.001s
                            chown_698_12419()
            with Stage(r"copy", r"UltraPitch v15.5.79.262", prog_num=12420):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12421) as should_copy_source_699_12421:  # ?
                    should_copy_source_699_12421()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=12422):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=12423) as copy_dir_to_dir_700_12423:  # ?
                            copy_dir_to_dir_700_12423()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=12424) as unwtar_701_12424:  # ?
                            unwtar_701_12424()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=12425, recursive=True) as chown_702_12425:  # 0m:0.001s
                            chown_702_12425()
            with Stage(r"copy", r"VComp v15.5.79.262", prog_num=12426):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12427) as should_copy_source_703_12427:  # ?
                    should_copy_source_703_12427()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=12428):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=12429) as copy_dir_to_dir_704_12429:  # ?
                            copy_dir_to_dir_704_12429()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=12430) as unwtar_705_12430:  # ?
                            unwtar_705_12430()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VComp.bundle", user_id=-1, group_id=-1, prog_num=12431, recursive=True) as chown_706_12431:  # 0m:0.001s
                            chown_706_12431()
            with Stage(r"copy", r"VEQ3 v15.5.79.262", prog_num=12432):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12433) as should_copy_source_707_12433:  # ?
                    should_copy_source_707_12433()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=12434):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=12435) as copy_dir_to_dir_708_12435:  # ?
                            copy_dir_to_dir_708_12435()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=12436) as unwtar_709_12436:  # ?
                            unwtar_709_12436()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=12437, recursive=True) as chown_710_12437:  # 0m:0.007s
                            chown_710_12437()
            with Stage(r"copy", r"VEQ4 v15.5.79.262", prog_num=12438):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12439) as should_copy_source_711_12439:  # ?
                    should_copy_source_711_12439()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=12440):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=12441) as copy_dir_to_dir_712_12441:  # ?
                            copy_dir_to_dir_712_12441()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=12442) as unwtar_713_12442:  # ?
                            unwtar_713_12442()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=12443, recursive=True) as chown_714_12443:  # 0m:0.001s
                            chown_714_12443()
            with Stage(r"copy", r"VU Meter v15.5.79.262", prog_num=12444):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12445) as should_copy_source_715_12445:  # ?
                    should_copy_source_715_12445()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=12446):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=12447) as copy_dir_to_dir_716_12447:  # ?
                            copy_dir_to_dir_716_12447()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=12448) as unwtar_717_12448:  # ?
                            unwtar_717_12448()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=12449, recursive=True) as chown_718_12449:  # 0m:0.001s
                            chown_718_12449()
            with Stage(r"copy", r"Vitamin v15.5.79.262", prog_num=12450):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12451) as should_copy_source_719_12451:  # ?
                    should_copy_source_719_12451()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=12452):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=12453) as copy_dir_to_dir_720_12453:  # ?
                            copy_dir_to_dir_720_12453()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=12454) as unwtar_721_12454:  # ?
                            unwtar_721_12454()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=12455, recursive=True) as chown_722_12455:  # 0m:0.001s
                            chown_722_12455()
            with Stage(r"copy", r"Vocal Rider v15.5.79.262", prog_num=12456):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12457) as should_copy_source_723_12457:  # ?
                    should_copy_source_723_12457()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=12458):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=12459) as copy_dir_to_dir_724_12459:  # ?
                            copy_dir_to_dir_724_12459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=12460) as unwtar_725_12460:  # ?
                            unwtar_725_12460()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=12461, recursive=True) as chown_726_12461:  # 0m:0.001s
                            chown_726_12461()
            with Stage(r"copy", r"Voltage Amps Bass v15.5.79.262", prog_num=12462):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12463) as should_copy_source_727_12463:  # ?
                    should_copy_source_727_12463()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=12464):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=12465) as copy_dir_to_dir_728_12465:  # ?
                            copy_dir_to_dir_728_12465()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=12466) as unwtar_729_12466:  # ?
                            unwtar_729_12466()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=12467, recursive=True) as chown_730_12467:  # 0m:0.001s
                            chown_730_12467()
            with Stage(r"copy", r"Voltage Amps Guitar v15.5.79.262", prog_num=12468):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12469) as should_copy_source_731_12469:  # ?
                    should_copy_source_731_12469()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=12470):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=12471) as copy_dir_to_dir_732_12471:  # ?
                            copy_dir_to_dir_732_12471()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=12472) as unwtar_733_12472:  # ?
                            unwtar_733_12472()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=12473, recursive=True) as chown_734_12473:  # 0m:0.001s
                            chown_734_12473()
            with Stage(r"copy", r"WLM v15.5.79.262", prog_num=12474):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12475) as should_copy_source_735_12475:  # ?
                    should_copy_source_735_12475()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=12476):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=12477) as copy_dir_to_dir_736_12477:  # ?
                            copy_dir_to_dir_736_12477()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=12478) as unwtar_737_12478:  # ?
                            unwtar_737_12478()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM.bundle", user_id=-1, group_id=-1, prog_num=12479, recursive=True) as chown_738_12479:  # 0m:0.001s
                            chown_738_12479()
            with Stage(r"copy", r"WLM Plus v15.5.79.262", prog_num=12480):  # 0m:0.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12481) as should_copy_source_739_12481:  # ?
                    should_copy_source_739_12481()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=12482):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=12483) as copy_dir_to_dir_740_12483:  # ?
                            copy_dir_to_dir_740_12483()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=12484) as unwtar_741_12484:  # ?
                            unwtar_741_12484()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=12485, recursive=True) as chown_742_12485:  # 0m:0.002s
                            chown_742_12485()
            with Stage(r"copy", r"WavesHeadTracker v15.5.79.262", prog_num=12486):  # 0m:0.115s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=5, prog_num=12487) as should_copy_source_743_12487:  # 0m:0.115s
                    should_copy_source_743_12487()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=12488):  # 0m:0.115s
                        with RmFileOrDir(r"/WavesHeadTracker", prog_num=12489) as rm_file_or_dir_744_12489:  # 0m:0.000s
                            rm_file_or_dir_744_12489()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=12490) as copy_dir_to_dir_745_12490:  # 0m:0.026s
                            copy_dir_to_dir_745_12490()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=12491) as unwtar_746_12491:  # 0m:0.088s
                            unwtar_746_12491()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=12492, recursive=True) as chown_747_12492:  # 0m:0.000s
                            chown_747_12492()
            with Stage(r"copy", r"WavesLib1_15_10_46_293 v15.10.46.293", prog_num=12493):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12494) as should_copy_source_748_12494:  # ?
                    should_copy_source_748_12494()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.10.46.framework", prog_num=12495):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r".", delete_extraneous_files=True, prog_num=12496) as copy_dir_to_dir_749_12496:  # ?
                            copy_dir_to_dir_749_12496()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", where_to_unwtar=r".", prog_num=12497) as unwtar_750_12497:  # ?
                            unwtar_750_12497()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.10.46.framework", user_id=-1, group_id=-1, prog_num=12498, recursive=True) as chown_751_12498:  # 0m:0.001s
                            chown_751_12498()
            with Stage(r"copy", r"WavesLib1_15_5_139_322 v15.5.139.322", prog_num=12499):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12500) as should_copy_source_752_12500:  # ?
                    should_copy_source_752_12500()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.139.framework", prog_num=12501):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r".", delete_extraneous_files=True, prog_num=12502) as copy_dir_to_dir_753_12502:  # ?
                            copy_dir_to_dir_753_12502()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", where_to_unwtar=r".", prog_num=12503) as unwtar_754_12503:  # ?
                            unwtar_754_12503()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.139.framework", user_id=-1, group_id=-1, prog_num=12504, recursive=True) as chown_755_12504:  # 0m:0.001s
                            chown_755_12504()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=12505):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12506) as should_copy_source_756_12506:  # ?
                    should_copy_source_756_12506()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=12507):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=12508) as copy_dir_to_dir_757_12508:  # ?
                            copy_dir_to_dir_757_12508()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=12509) as unwtar_758_12509:  # ?
                            unwtar_758_12509()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=12510, recursive=True) as chown_759_12510:  # 0m:0.001s
                            chown_759_12510()
            with Stage(r"copy", r"WavesTune v15.5.79.262", prog_num=12511):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12512) as should_copy_source_760_12512:  # ?
                    should_copy_source_760_12512()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=12513):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=12514) as copy_dir_to_dir_761_12514:  # ?
                            copy_dir_to_dir_761_12514()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=12515) as unwtar_762_12515:  # ?
                            unwtar_762_12515()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=12516, recursive=True) as chown_763_12516:  # 0m:0.001s
                            chown_763_12516()
            with Stage(r"copy", r"WavesTune LT v15.5.79.262", prog_num=12517):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12518) as should_copy_source_764_12518:  # ?
                    should_copy_source_764_12518()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=12519):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=12520) as copy_dir_to_dir_765_12520:  # ?
                            copy_dir_to_dir_765_12520()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=12521) as unwtar_766_12521:  # ?
                            unwtar_766_12521()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=12522, recursive=True) as chown_767_12522:  # 0m:0.001s
                            chown_767_12522()
            with Stage(r"copy", r"Waves Harmony v15.5.139.322", prog_num=12523):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12524) as should_copy_source_768_12524:  # ?
                    should_copy_source_768_12524()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=12525):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=12526) as copy_dir_to_dir_769_12526:  # ?
                            copy_dir_to_dir_769_12526()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=12527) as unwtar_770_12527:  # ?
                            unwtar_770_12527()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=12528, recursive=True) as chown_771_12528:  # 0m:0.001s
                            chown_771_12528()
            with Stage(r"copy", r"Waves Tune Real-Time v15.5.79.262", prog_num=12529):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12530) as should_copy_source_772_12530:  # ?
                    should_copy_source_772_12530()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=12531):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=12532) as copy_dir_to_dir_773_12532:  # ?
                            copy_dir_to_dir_773_12532()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=12533) as unwtar_774_12533:  # ?
                            unwtar_774_12533()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=12534, recursive=True) as chown_775_12534:  # 0m:0.007s
                            chown_775_12534()
            with Stage(r"copy", r"X-Click v15.5.79.262", prog_num=12535):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12536) as should_copy_source_776_12536:  # ?
                    should_copy_source_776_12536()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=12537):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=12538) as copy_dir_to_dir_777_12538:  # ?
                            copy_dir_to_dir_777_12538()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=12539) as unwtar_778_12539:  # ?
                            unwtar_778_12539()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Click.bundle", user_id=-1, group_id=-1, prog_num=12540, recursive=True) as chown_779_12540:  # 0m:0.001s
                            chown_779_12540()
            with Stage(r"copy", r"X-Crackle v15.5.79.262", prog_num=12541):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12542) as should_copy_source_780_12542:  # ?
                    should_copy_source_780_12542()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=12543):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=12544) as copy_dir_to_dir_781_12544:  # ?
                            copy_dir_to_dir_781_12544()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=12545) as unwtar_782_12545:  # ?
                            unwtar_782_12545()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=12546, recursive=True) as chown_783_12546:  # 0m:0.001s
                            chown_783_12546()
            with Stage(r"copy", r"X-Hum v15.5.79.262", prog_num=12547):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12548) as should_copy_source_784_12548:  # ?
                    should_copy_source_784_12548()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=12549):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=12550) as copy_dir_to_dir_785_12550:  # ?
                            copy_dir_to_dir_785_12550()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=12551) as unwtar_786_12551:  # ?
                            unwtar_786_12551()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=12552, recursive=True) as chown_787_12552:  # 0m:0.001s
                            chown_787_12552()
            with Stage(r"copy", r"X-Noise v15.5.79.262", prog_num=12553):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12554) as should_copy_source_788_12554:  # ?
                    should_copy_source_788_12554()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=12555):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12556) as copy_dir_to_dir_789_12556:  # ?
                            copy_dir_to_dir_789_12556()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=12557) as unwtar_790_12557:  # ?
                            unwtar_790_12557()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=12558, recursive=True) as chown_791_12558:  # 0m:0.001s
                            chown_791_12558()
            with Stage(r"copy", r"Z-Noise v15.5.79.262", prog_num=12559):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12560) as should_copy_source_792_12560:  # ?
                    should_copy_source_792_12560()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=12561):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12562) as copy_dir_to_dir_793_12562:  # ?
                            copy_dir_to_dir_793_12562()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=12563) as unwtar_794_12563:  # ?
                            unwtar_794_12563()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=12564, recursive=True) as chown_795_12564:  # 0m:0.001s
                            chown_795_12564()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=6, prog_num=12570) as resolve_symlink_files_in_folder_796_12570:  # 0m:1.382s
                resolve_symlink_files_in_folder_796_12570()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=12571) as shell_command_797_12571:  # 0m:0.097s
                shell_command_797_12571()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=12572) as script_command_798_12572:  # 0m:0.015s
                script_command_798_12572()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12573) as shell_command_799_12573:  # 0m:0.024s
                shell_command_799_12573()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12574) as create_symlink_800_12574:  # 0m:0.001s
                create_symlink_800_12574()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12575) as create_symlink_801_12575:  # 0m:0.000s
                create_symlink_801_12575()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=12576) as copy_glob_to_dir_802_12576:  # 0m:0.184s
                copy_glob_to_dir_802_12576()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=12577) as cd_stage_803_12577:  # 0m:0.001s
            cd_stage_803_12577()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=12578):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=12579) as should_copy_source_804_12579:  # ?
                    should_copy_source_804_12579()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=12580):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=12581) as copy_file_to_dir_805_12581:  # ?
                            copy_file_to_dir_805_12581()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=12582) as chmod_and_chown_806_12582:  # 0m:0.000s
                            chmod_and_chown_806_12582()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/GTR", prog_num=12583) as cd_stage_807_12583:  # 0m:0.085s
            cd_stage_807_12583()
            with Stage(r"copy", r"GTR Stomps v15.5.79.262", prog_num=12584):  # 0m:0.017s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12585) as should_copy_source_808_12585:  # ?
                    should_copy_source_808_12585()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=12586):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=12587) as copy_dir_to_dir_809_12587:  # ?
                            copy_dir_to_dir_809_12587()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=12588) as unwtar_810_12588:  # ?
                            unwtar_810_12588()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=12589, recursive=True) as chown_811_12589:  # 0m:0.001s
                            chown_811_12589()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12590) as should_copy_source_812_12590:  # ?
                    should_copy_source_812_12590()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=12591):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=12592) as copy_dir_to_dir_813_12592:  # ?
                            copy_dir_to_dir_813_12592()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=12593) as unwtar_814_12593:  # ?
                            unwtar_814_12593()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=12594, recursive=True) as chown_815_12594:  # 0m:0.001s
                            chown_815_12594()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12595) as should_copy_source_816_12595:  # ?
                    should_copy_source_816_12595()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=12596):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=12597) as copy_dir_to_dir_817_12597:  # ?
                            copy_dir_to_dir_817_12597()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=12598) as unwtar_818_12598:  # ?
                            unwtar_818_12598()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=12599, recursive=True) as chown_819_12599:  # 0m:0.001s
                            chown_819_12599()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12600) as should_copy_source_820_12600:  # ?
                    should_copy_source_820_12600()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=12601):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=12602) as copy_dir_to_dir_821_12602:  # ?
                            copy_dir_to_dir_821_12602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=12603) as unwtar_822_12603:  # ?
                            unwtar_822_12603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=12604, recursive=True) as chown_823_12604:  # 0m:0.001s
                            chown_823_12604()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12605) as should_copy_source_824_12605:  # ?
                    should_copy_source_824_12605()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=12606):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=12607) as copy_dir_to_dir_825_12607:  # ?
                            copy_dir_to_dir_825_12607()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=12608) as unwtar_826_12608:  # ?
                            unwtar_826_12608()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=12609, recursive=True) as chown_827_12609:  # 0m:0.001s
                            chown_827_12609()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12610) as should_copy_source_828_12610:  # ?
                    should_copy_source_828_12610()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=12611):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=12612) as copy_dir_to_dir_829_12612:  # ?
                            copy_dir_to_dir_829_12612()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=12613) as unwtar_830_12613:  # ?
                            unwtar_830_12613()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=12614, recursive=True) as chown_831_12614:  # 0m:0.001s
                            chown_831_12614()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12615) as should_copy_source_832_12615:  # ?
                    should_copy_source_832_12615()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=12616):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=12617) as copy_dir_to_dir_833_12617:  # ?
                            copy_dir_to_dir_833_12617()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=12618) as unwtar_834_12618:  # ?
                            unwtar_834_12618()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=12619, recursive=True) as chown_835_12619:  # 0m:0.001s
                            chown_835_12619()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12620) as should_copy_source_836_12620:  # ?
                    should_copy_source_836_12620()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=12621):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=12622) as copy_dir_to_dir_837_12622:  # ?
                            copy_dir_to_dir_837_12622()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=12623) as unwtar_838_12623:  # ?
                            unwtar_838_12623()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=12624, recursive=True) as chown_839_12624:  # 0m:0.001s
                            chown_839_12624()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12625) as should_copy_source_840_12625:  # ?
                    should_copy_source_840_12625()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=12626):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12627) as copy_dir_to_dir_841_12627:  # ?
                            copy_dir_to_dir_841_12627()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=12628) as unwtar_842_12628:  # ?
                            unwtar_842_12628()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=12629, recursive=True) as chown_843_12629:  # 0m:0.001s
                            chown_843_12629()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12630) as should_copy_source_844_12630:  # ?
                    should_copy_source_844_12630()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=12631):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=12632) as copy_dir_to_dir_845_12632:  # ?
                            copy_dir_to_dir_845_12632()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=12633) as unwtar_846_12633:  # ?
                            unwtar_846_12633()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=12634, recursive=True) as chown_847_12634:  # 0m:0.001s
                            chown_847_12634()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12635) as should_copy_source_848_12635:  # ?
                    should_copy_source_848_12635()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=12636):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=12637) as copy_dir_to_dir_849_12637:  # ?
                            copy_dir_to_dir_849_12637()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=12638) as unwtar_850_12638:  # ?
                            unwtar_850_12638()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=12639, recursive=True) as chown_851_12639:  # 0m:0.001s
                            chown_851_12639()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12640) as should_copy_source_852_12640:  # ?
                    should_copy_source_852_12640()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=12641):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=12642) as copy_dir_to_dir_853_12642:  # ?
                            copy_dir_to_dir_853_12642()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=12643) as unwtar_854_12643:  # ?
                            unwtar_854_12643()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=12644, recursive=True) as chown_855_12644:  # 0m:0.001s
                            chown_855_12644()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12645) as should_copy_source_856_12645:  # ?
                    should_copy_source_856_12645()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=12646):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=12647) as copy_dir_to_dir_857_12647:  # ?
                            copy_dir_to_dir_857_12647()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=12648) as unwtar_858_12648:  # ?
                            unwtar_858_12648()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=12649, recursive=True) as chown_859_12649:  # 0m:0.001s
                            chown_859_12649()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12650) as should_copy_source_860_12650:  # ?
                    should_copy_source_860_12650()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=12651):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=12652) as copy_dir_to_dir_861_12652:  # ?
                            copy_dir_to_dir_861_12652()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=12653) as unwtar_862_12653:  # ?
                            unwtar_862_12653()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=12654, recursive=True) as chown_863_12654:  # 0m:0.001s
                            chown_863_12654()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12655) as should_copy_source_864_12655:  # ?
                    should_copy_source_864_12655()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=12656):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=12657) as copy_dir_to_dir_865_12657:  # ?
                            copy_dir_to_dir_865_12657()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=12658) as unwtar_866_12658:  # ?
                            unwtar_866_12658()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=12659, recursive=True) as chown_867_12659:  # 0m:0.001s
                            chown_867_12659()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12660) as should_copy_source_868_12660:  # ?
                    should_copy_source_868_12660()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=12661):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=12662) as copy_dir_to_dir_869_12662:  # ?
                            copy_dir_to_dir_869_12662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=12663) as unwtar_870_12663:  # ?
                            unwtar_870_12663()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=12664, recursive=True) as chown_871_12664:  # 0m:0.001s
                            chown_871_12664()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12665) as should_copy_source_872_12665:  # ?
                    should_copy_source_872_12665()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=12666):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=12667) as copy_dir_to_dir_873_12667:  # ?
                            copy_dir_to_dir_873_12667()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=12668) as unwtar_874_12668:  # ?
                            unwtar_874_12668()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=12669, recursive=True) as chown_875_12669:  # 0m:0.001s
                            chown_875_12669()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12670) as should_copy_source_876_12670:  # ?
                    should_copy_source_876_12670()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=12671):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=12672) as copy_dir_to_dir_877_12672:  # ?
                            copy_dir_to_dir_877_12672()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=12673) as unwtar_878_12673:  # ?
                            unwtar_878_12673()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=12674, recursive=True) as chown_879_12674:  # 0m:0.001s
                            chown_879_12674()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12675) as should_copy_source_880_12675:  # ?
                    should_copy_source_880_12675()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=12676):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=12677) as copy_dir_to_dir_881_12677:  # ?
                            copy_dir_to_dir_881_12677()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=12678) as unwtar_882_12678:  # ?
                            unwtar_882_12678()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=12679, recursive=True) as chown_883_12679:  # 0m:0.001s
                            chown_883_12679()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12680) as should_copy_source_884_12680:  # ?
                    should_copy_source_884_12680()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=12681):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=12682) as copy_dir_to_dir_885_12682:  # ?
                            copy_dir_to_dir_885_12682()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=12683) as unwtar_886_12683:  # ?
                            unwtar_886_12683()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=12684, recursive=True) as chown_887_12684:  # 0m:0.000s
                            chown_887_12684()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12685) as should_copy_source_888_12685:  # ?
                    should_copy_source_888_12685()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=12686):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=12687) as copy_dir_to_dir_889_12687:  # ?
                            copy_dir_to_dir_889_12687()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=12688) as unwtar_890_12688:  # ?
                            unwtar_890_12688()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=12689, recursive=True) as chown_891_12689:  # 0m:0.000s
                            chown_891_12689()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12690) as should_copy_source_892_12690:  # ?
                    should_copy_source_892_12690()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=12691):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=12692) as copy_dir_to_dir_893_12692:  # ?
                            copy_dir_to_dir_893_12692()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=12693) as unwtar_894_12693:  # ?
                            unwtar_894_12693()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=12694, recursive=True) as chown_895_12694:  # 0m:0.000s
                            chown_895_12694()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12695) as should_copy_source_896_12695:  # ?
                    should_copy_source_896_12695()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=12696):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=12697) as copy_dir_to_dir_897_12697:  # ?
                            copy_dir_to_dir_897_12697()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=12698) as unwtar_898_12698:  # ?
                            unwtar_898_12698()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=12699, recursive=True) as chown_899_12699:  # 0m:0.001s
                            chown_899_12699()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12700) as should_copy_source_900_12700:  # ?
                    should_copy_source_900_12700()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=12701):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=12702) as copy_dir_to_dir_901_12702:  # ?
                            copy_dir_to_dir_901_12702()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=12703) as unwtar_902_12703:  # ?
                            unwtar_902_12703()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=12704, recursive=True) as chown_903_12704:  # 0m:0.001s
                            chown_903_12704()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12705) as should_copy_source_904_12705:  # ?
                    should_copy_source_904_12705()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=12706):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=12707) as copy_dir_to_dir_905_12707:  # ?
                            copy_dir_to_dir_905_12707()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=12708) as unwtar_906_12708:  # ?
                            unwtar_906_12708()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=12709, recursive=True) as chown_907_12709:  # 0m:0.001s
                            chown_907_12709()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12710) as shell_command_908_12710:  # 0m:0.063s
                shell_command_908_12710()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/ReWire", prog_num=12711) as cd_stage_909_12711:  # 0m:0.161s
            cd_stage_909_12711()
            with Stage(r"copy", r"backup ReWire to Waves folder", prog_num=12712):  # 0m:0.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12713) as should_copy_source_910_12713:  # ?
                    should_copy_source_910_12713()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=12714):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=12715) as copy_dir_to_dir_911_12715:  # ?
                            copy_dir_to_dir_911_12715()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=12716) as unwtar_912_12716:  # ?
                            unwtar_912_12716()
                        with Chown(path=r"/Applications/Waves/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=12717, recursive=True) as chown_913_12717:  # 0m:0.002s
                            chown_913_12717()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12718) as should_copy_source_914_12718:  # ?
                    should_copy_source_914_12718()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=12719):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=12720) as copy_dir_to_dir_915_12720:  # ?
                            copy_dir_to_dir_915_12720()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=12721) as unwtar_916_12721:  # ?
                            unwtar_916_12721()
                        with Chown(path=r"/Applications/Waves/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=12722, recursive=True) as chown_917_12722:  # 0m:0.001s
                            chown_917_12722()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/ReWire" -c', ignore_all_errors=True, prog_num=12723) as shell_command_918_12723:  # 0m:0.109s
                shell_command_918_12723()
            with ScriptCommand(r'if [ -f "/Applications/Waves/ReWire"/Icon? ]; then chmod a+rw "/Applications/Waves/ReWire"/Icon?; fi', prog_num=12724) as script_command_919_12724:  # 0m:0.013s
                script_command_919_12724()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12725) as shell_command_920_12725:  # 0m:0.030s
                shell_command_920_12725()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=12726) as cd_stage_921_12726:  # 0m:0.029s
            cd_stage_921_12726()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12727):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12728) as should_copy_source_922_12728:  # ?
                    should_copy_source_922_12728()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12729):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12730) as copy_dir_to_dir_923_12730:  # ?
                            copy_dir_to_dir_923_12730()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12731) as unwtar_924_12731:  # ?
                            unwtar_924_12731()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12732, recursive=True) as chown_925_12732:  # ?
                            chown_925_12732()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12733) as shell_command_926_12733:  # 0m:0.001s
                            shell_command_926_12733()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12734):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12735) as should_copy_source_927_12735:  # ?
                    should_copy_source_927_12735()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12736):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12737) as copy_dir_to_dir_928_12737:  # ?
                            copy_dir_to_dir_928_12737()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12738) as unwtar_929_12738:  # ?
                            unwtar_929_12738()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12739, recursive=True) as chown_930_12739:  # ?
                            chown_930_12739()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12740) as shell_command_931_12740:  # 0m:0.001s
                            shell_command_931_12740()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=12741):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12742) as should_copy_source_932_12742:  # ?
                    should_copy_source_932_12742()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=12743):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=12744) as copy_dir_to_dir_933_12744:  # ?
                            copy_dir_to_dir_933_12744()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=12745) as unwtar_934_12745:  # ?
                            unwtar_934_12745()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12746, recursive=True) as chown_935_12746:  # ?
                            chown_935_12746()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=12747) as break_hard_link_936_12747:  # ?
                            break_hard_link_936_12747()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=12748) as shell_command_937_12748:  # ?
                            shell_command_937_12748()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12749, recursive=True) as chown_938_12749:  # ?
                            chown_938_12749()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=12750, recursive=True) as chmod_939_12750:  # 0m:0.001s
                            chmod_939_12750()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=12751):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12752) as should_copy_source_940_12752:  # ?
                    should_copy_source_940_12752()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=12753):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=12754) as copy_dir_to_dir_941_12754:  # ?
                            copy_dir_to_dir_941_12754()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=12755) as unwtar_942_12755:  # ?
                            unwtar_942_12755()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12756, recursive=True) as chown_943_12756:  # ?
                            chown_943_12756()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=12757) as break_hard_link_944_12757:  # ?
                            break_hard_link_944_12757()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=12758) as shell_command_945_12758:  # ?
                            shell_command_945_12758()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12759, recursive=True) as chown_946_12759:  # ?
                            chown_946_12759()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=12760, recursive=True) as chmod_947_12760:  # 0m:0.001s
                            chmod_947_12760()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=12761):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12762) as should_copy_source_948_12762:  # ?
                    should_copy_source_948_12762()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=12763):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=12764) as copy_dir_to_dir_949_12764:  # ?
                            copy_dir_to_dir_949_12764()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=12765) as unwtar_950_12765:  # ?
                            unwtar_950_12765()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=12766, recursive=True) as chown_951_12766:  # ?
                            chown_951_12766()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=12767) as shell_command_952_12767:  # 0m:0.001s
                            shell_command_952_12767()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=12768):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12769) as should_copy_source_953_12769:  # ?
                    should_copy_source_953_12769()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=12770):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=12771) as copy_dir_to_dir_954_12771:  # ?
                            copy_dir_to_dir_954_12771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=12772) as unwtar_955_12772:  # ?
                            unwtar_955_12772()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=12773, recursive=True) as chown_956_12773:  # ?
                            chown_956_12773()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=12774) as shell_command_957_12774:  # 0m:0.001s
                            shell_command_957_12774()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=12775):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12776) as should_copy_source_958_12776:  # ?
                    should_copy_source_958_12776()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=12777):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=12778) as copy_dir_to_dir_959_12778:  # ?
                            copy_dir_to_dir_959_12778()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=12779) as unwtar_960_12779:  # ?
                            unwtar_960_12779()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=12780, recursive=True) as chown_961_12780:  # ?
                            chown_961_12780()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12781) as shell_command_962_12781:  # ?
                            shell_command_962_12781()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12782) as script_command_963_12782:  # ?
                            script_command_963_12782()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12783) as shell_command_964_12783:  # 0m:0.007s
                            shell_command_964_12783()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=12784):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12785) as should_copy_source_965_12785:  # ?
                    should_copy_source_965_12785()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=12786):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=12787) as copy_dir_to_dir_966_12787:  # ?
                            copy_dir_to_dir_966_12787()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=12788) as unwtar_967_12788:  # ?
                            unwtar_967_12788()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=12789, recursive=True) as chown_968_12789:  # ?
                            chown_968_12789()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12790) as shell_command_969_12790:  # ?
                            shell_command_969_12790()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12791) as script_command_970_12791:  # ?
                            script_command_970_12791()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12792) as shell_command_971_12792:  # 0m:0.001s
                            shell_command_971_12792()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=12793):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=12794) as should_copy_source_972_12794:  # ?
                    should_copy_source_972_12794()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=12795):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=12796) as copy_dir_to_dir_973_12796:  # ?
                            copy_dir_to_dir_973_12796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=12797) as unwtar_974_12797:  # ?
                            unwtar_974_12797()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=12798, recursive=True) as chown_975_12798:  # 0m:0.001s
                            chown_975_12798()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=12799) as shell_command_976_12799:  # 0m:0.012s
                shell_command_976_12799()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=12800) as cd_stage_977_12800:  # 0m:0.002s
            cd_stage_977_12800()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12801):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12802) as should_copy_source_978_12802:  # ?
                    should_copy_source_978_12802()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12803):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12804) as copy_dir_to_dir_979_12804:  # ?
                            copy_dir_to_dir_979_12804()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12805) as unwtar_980_12805:  # ?
                            unwtar_980_12805()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12806, recursive=True) as chown_981_12806:  # ?
                            chown_981_12806()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12807) as shell_command_982_12807:  # 0m:0.001s
                            shell_command_982_12807()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12808):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12809) as should_copy_source_983_12809:  # ?
                    should_copy_source_983_12809()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12810):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12811) as copy_dir_to_dir_984_12811:  # ?
                            copy_dir_to_dir_984_12811()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12812) as unwtar_985_12812:  # ?
                            unwtar_985_12812()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12813, recursive=True) as chown_986_12813:  # ?
                            chown_986_12813()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12814) as shell_command_987_12814:  # 0m:0.001s
                            shell_command_987_12814()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=12815) as cd_stage_988_12815:  # 0m:0.162s
            cd_stage_988_12815()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=12816):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12817) as should_copy_source_989_12817:  # ?
                    should_copy_source_989_12817()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=12818):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=12819) as copy_file_to_dir_990_12819:  # ?
                            copy_file_to_dir_990_12819()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12820) as chmod_and_chown_991_12820:  # 0m:0.000s
                            chmod_and_chown_991_12820()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=12821):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12822) as should_copy_source_992_12822:  # ?
                    should_copy_source_992_12822()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=12823):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=12824) as copy_file_to_dir_993_12824:  # ?
                            copy_file_to_dir_993_12824()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12825) as chmod_and_chown_994_12825:  # 0m:0.000s
                            chmod_and_chown_994_12825()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=12826):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12827) as should_copy_source_995_12827:  # ?
                    should_copy_source_995_12827()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=12828):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=12829) as copy_file_to_dir_996_12829:  # ?
                            copy_file_to_dir_996_12829()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12830) as chmod_and_chown_997_12830:  # 0m:0.000s
                            chmod_and_chown_997_12830()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=12831):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12832) as should_copy_source_998_12832:  # ?
                    should_copy_source_998_12832()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=12833):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=12834) as copy_file_to_dir_999_12834:  # ?
                            copy_file_to_dir_999_12834()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12835) as chmod_and_chown_1000_12835:  # 0m:0.000s
                            chmod_and_chown_1000_12835()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=12836):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12837) as should_copy_source_1001_12837:  # ?
                    should_copy_source_1001_12837()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=12838):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=12839) as copy_file_to_dir_1002_12839:  # ?
                            copy_file_to_dir_1002_12839()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12840) as chmod_and_chown_1003_12840:  # 0m:0.000s
                            chmod_and_chown_1003_12840()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=12841):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12842) as should_copy_source_1004_12842:  # ?
                    should_copy_source_1004_12842()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=12843):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=12844) as copy_file_to_dir_1005_12844:  # ?
                            copy_file_to_dir_1005_12844()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12845) as chmod_and_chown_1006_12845:  # 0m:0.000s
                            chmod_and_chown_1006_12845()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=12846):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12847) as should_copy_source_1007_12847:  # ?
                    should_copy_source_1007_12847()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=12848):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=12849) as copy_file_to_dir_1008_12849:  # ?
                            copy_file_to_dir_1008_12849()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12850) as chmod_and_chown_1009_12850:  # 0m:0.000s
                            chmod_and_chown_1009_12850()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=12851):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12852) as should_copy_source_1010_12852:  # ?
                    should_copy_source_1010_12852()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=12853):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=12854) as copy_file_to_dir_1011_12854:  # ?
                            copy_file_to_dir_1011_12854()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12855) as chmod_and_chown_1012_12855:  # 0m:0.000s
                            chmod_and_chown_1012_12855()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=12856):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12857) as should_copy_source_1013_12857:  # ?
                    should_copy_source_1013_12857()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=12858):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=12859) as copy_file_to_dir_1014_12859:  # ?
                            copy_file_to_dir_1014_12859()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12860) as chmod_and_chown_1015_12860:  # 0m:0.000s
                            chmod_and_chown_1015_12860()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=12861):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12862) as should_copy_source_1016_12862:  # ?
                    should_copy_source_1016_12862()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=12863):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=12864) as copy_file_to_dir_1017_12864:  # ?
                            copy_file_to_dir_1017_12864()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12865) as chmod_and_chown_1018_12865:  # 0m:0.000s
                            chmod_and_chown_1018_12865()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=12866):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12867) as should_copy_source_1019_12867:  # ?
                    should_copy_source_1019_12867()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=12868):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=12869) as copy_file_to_dir_1020_12869:  # ?
                            copy_file_to_dir_1020_12869()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12870) as chmod_and_chown_1021_12870:  # 0m:0.000s
                            chmod_and_chown_1021_12870()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=12871):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12872) as should_copy_source_1022_12872:  # ?
                    should_copy_source_1022_12872()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=12873):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=12874) as copy_file_to_dir_1023_12874:  # ?
                            copy_file_to_dir_1023_12874()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12875) as chmod_and_chown_1024_12875:  # 0m:0.000s
                            chmod_and_chown_1024_12875()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=12876):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12877) as should_copy_source_1025_12877:  # ?
                    should_copy_source_1025_12877()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=12878):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=12879) as copy_file_to_dir_1026_12879:  # ?
                            copy_file_to_dir_1026_12879()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12880) as chmod_and_chown_1027_12880:  # 0m:0.000s
                            chmod_and_chown_1027_12880()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=12881):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12882) as should_copy_source_1028_12882:  # ?
                    should_copy_source_1028_12882()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=12883):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=12884) as copy_file_to_dir_1029_12884:  # ?
                            copy_file_to_dir_1029_12884()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12885) as chmod_and_chown_1030_12885:  # 0m:0.000s
                            chmod_and_chown_1030_12885()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=12886):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12887) as should_copy_source_1031_12887:  # ?
                    should_copy_source_1031_12887()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=12888):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=12889) as copy_file_to_dir_1032_12889:  # ?
                            copy_file_to_dir_1032_12889()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12890) as chmod_and_chown_1033_12890:  # 0m:0.000s
                            chmod_and_chown_1033_12890()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=12891):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12892) as should_copy_source_1034_12892:  # ?
                    should_copy_source_1034_12892()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=12893):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=12894) as copy_file_to_dir_1035_12894:  # ?
                            copy_file_to_dir_1035_12894()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12895) as chmod_and_chown_1036_12895:  # 0m:0.000s
                            chmod_and_chown_1036_12895()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=12896):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12897) as should_copy_source_1037_12897:  # ?
                    should_copy_source_1037_12897()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=12898):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=12899) as copy_file_to_dir_1038_12899:  # ?
                            copy_file_to_dir_1038_12899()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12900) as chmod_and_chown_1039_12900:  # 0m:0.000s
                            chmod_and_chown_1039_12900()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=12901):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12902) as should_copy_source_1040_12902:  # ?
                    should_copy_source_1040_12902()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=12903):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=12904) as copy_file_to_dir_1041_12904:  # ?
                            copy_file_to_dir_1041_12904()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12905) as chmod_and_chown_1042_12905:  # 0m:0.000s
                            chmod_and_chown_1042_12905()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=12906):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12907) as should_copy_source_1043_12907:  # ?
                    should_copy_source_1043_12907()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=12908):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=12909) as copy_file_to_dir_1044_12909:  # ?
                            copy_file_to_dir_1044_12909()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12910) as chmod_and_chown_1045_12910:  # 0m:0.000s
                            chmod_and_chown_1045_12910()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=12911):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12912) as should_copy_source_1046_12912:  # ?
                    should_copy_source_1046_12912()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=12913):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=12914) as copy_file_to_dir_1047_12914:  # ?
                            copy_file_to_dir_1047_12914()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12915) as chmod_and_chown_1048_12915:  # 0m:0.000s
                            chmod_and_chown_1048_12915()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=12916):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12917) as should_copy_source_1049_12917:  # ?
                    should_copy_source_1049_12917()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=12918):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=12919) as copy_file_to_dir_1050_12919:  # ?
                            copy_file_to_dir_1050_12919()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12920) as chmod_and_chown_1051_12920:  # 0m:0.000s
                            chmod_and_chown_1051_12920()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=12921):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12922) as should_copy_source_1052_12922:  # ?
                    should_copy_source_1052_12922()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=12923):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=12924) as copy_file_to_dir_1053_12924:  # ?
                            copy_file_to_dir_1053_12924()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12925) as chmod_and_chown_1054_12925:  # 0m:0.000s
                            chmod_and_chown_1054_12925()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=12926):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12927) as should_copy_source_1055_12927:  # ?
                    should_copy_source_1055_12927()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=12928):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=12929) as copy_file_to_dir_1056_12929:  # ?
                            copy_file_to_dir_1056_12929()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12930) as chmod_and_chown_1057_12930:  # 0m:0.000s
                            chmod_and_chown_1057_12930()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=12931):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12932) as should_copy_source_1058_12932:  # ?
                    should_copy_source_1058_12932()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=12933):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=12934) as copy_file_to_dir_1059_12934:  # ?
                            copy_file_to_dir_1059_12934()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12935) as chmod_and_chown_1060_12935:  # 0m:0.000s
                            chmod_and_chown_1060_12935()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=12936):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12937) as should_copy_source_1061_12937:  # ?
                    should_copy_source_1061_12937()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=12938):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=12939) as copy_file_to_dir_1062_12939:  # ?
                            copy_file_to_dir_1062_12939()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12940) as chmod_and_chown_1063_12940:  # 0m:0.000s
                            chmod_and_chown_1063_12940()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=12941):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12942) as should_copy_source_1064_12942:  # ?
                    should_copy_source_1064_12942()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=12943):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=12944) as copy_file_to_dir_1065_12944:  # ?
                            copy_file_to_dir_1065_12944()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12945) as chmod_and_chown_1066_12945:  # 0m:0.000s
                            chmod_and_chown_1066_12945()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=12946):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12947) as should_copy_source_1067_12947:  # ?
                    should_copy_source_1067_12947()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=12948):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=12949) as copy_file_to_dir_1068_12949:  # ?
                            copy_file_to_dir_1068_12949()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12950) as chmod_and_chown_1069_12950:  # 0m:0.000s
                            chmod_and_chown_1069_12950()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=12951):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12952) as should_copy_source_1070_12952:  # ?
                    should_copy_source_1070_12952()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=12953):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=12954) as copy_file_to_dir_1071_12954:  # ?
                            copy_file_to_dir_1071_12954()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12955) as chmod_and_chown_1072_12955:  # 0m:0.000s
                            chmod_and_chown_1072_12955()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=12956):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12957) as should_copy_source_1073_12957:  # ?
                    should_copy_source_1073_12957()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=12958):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=12959) as copy_file_to_dir_1074_12959:  # ?
                            copy_file_to_dir_1074_12959()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12960) as chmod_and_chown_1075_12960:  # 0m:0.000s
                            chmod_and_chown_1075_12960()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=12961):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12962) as should_copy_source_1076_12962:  # ?
                    should_copy_source_1076_12962()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=12963):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=12964) as copy_file_to_dir_1077_12964:  # ?
                            copy_file_to_dir_1077_12964()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12965) as chmod_and_chown_1078_12965:  # 0m:0.000s
                            chmod_and_chown_1078_12965()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=12966):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12967) as should_copy_source_1079_12967:  # ?
                    should_copy_source_1079_12967()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=12968):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=12969) as copy_file_to_dir_1080_12969:  # ?
                            copy_file_to_dir_1080_12969()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12970) as chmod_and_chown_1081_12970:  # 0m:0.000s
                            chmod_and_chown_1081_12970()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=12971):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12972) as should_copy_source_1082_12972:  # ?
                    should_copy_source_1082_12972()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=12973):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=12974) as copy_file_to_dir_1083_12974:  # ?
                            copy_file_to_dir_1083_12974()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12975) as chmod_and_chown_1084_12975:  # 0m:0.000s
                            chmod_and_chown_1084_12975()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=12976):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12977) as should_copy_source_1085_12977:  # ?
                    should_copy_source_1085_12977()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=12978):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=12979) as copy_file_to_dir_1086_12979:  # ?
                            copy_file_to_dir_1086_12979()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12980) as chmod_and_chown_1087_12980:  # 0m:0.000s
                            chmod_and_chown_1087_12980()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=12981):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12982) as should_copy_source_1088_12982:  # ?
                    should_copy_source_1088_12982()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=12983):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=12984) as copy_file_to_dir_1089_12984:  # ?
                            copy_file_to_dir_1089_12984()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12985) as chmod_and_chown_1090_12985:  # 0m:0.000s
                            chmod_and_chown_1090_12985()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=12986):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12987) as should_copy_source_1091_12987:  # ?
                    should_copy_source_1091_12987()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=12988):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=12989) as copy_file_to_dir_1092_12989:  # ?
                            copy_file_to_dir_1092_12989()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12990) as chmod_and_chown_1093_12990:  # 0m:0.000s
                            chmod_and_chown_1093_12990()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=12991):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12992) as should_copy_source_1094_12992:  # ?
                    should_copy_source_1094_12992()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=12993):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=12994) as copy_file_to_dir_1095_12994:  # ?
                            copy_file_to_dir_1095_12994()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12995) as chmod_and_chown_1096_12995:  # 0m:0.000s
                            chmod_and_chown_1096_12995()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=12996):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12997) as should_copy_source_1097_12997:  # ?
                    should_copy_source_1097_12997()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=12998):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=12999) as copy_file_to_dir_1098_12999:  # ?
                            copy_file_to_dir_1098_12999()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13000) as chmod_and_chown_1099_13000:  # 0m:0.000s
                            chmod_and_chown_1099_13000()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=13001):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13002) as should_copy_source_1100_13002:  # ?
                    should_copy_source_1100_13002()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=13003):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=13004) as copy_file_to_dir_1101_13004:  # ?
                            copy_file_to_dir_1101_13004()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13005) as chmod_and_chown_1102_13005:  # 0m:0.000s
                            chmod_and_chown_1102_13005()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=13006):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13007) as should_copy_source_1103_13007:  # ?
                    should_copy_source_1103_13007()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=13008):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=13009) as copy_file_to_dir_1104_13009:  # ?
                            copy_file_to_dir_1104_13009()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13010) as chmod_and_chown_1105_13010:  # 0m:0.000s
                            chmod_and_chown_1105_13010()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=13011):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13012) as should_copy_source_1106_13012:  # ?
                    should_copy_source_1106_13012()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=13013):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=13014) as copy_file_to_dir_1107_13014:  # ?
                            copy_file_to_dir_1107_13014()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13015) as chmod_and_chown_1108_13015:  # 0m:0.000s
                            chmod_and_chown_1108_13015()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=13016):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13017) as should_copy_source_1109_13017:  # ?
                    should_copy_source_1109_13017()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=13018):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=13019) as copy_file_to_dir_1110_13019:  # ?
                            copy_file_to_dir_1110_13019()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13020) as chmod_and_chown_1111_13020:  # 0m:0.000s
                            chmod_and_chown_1111_13020()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=13021):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13022) as should_copy_source_1112_13022:  # ?
                    should_copy_source_1112_13022()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=13023):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=13024) as copy_file_to_dir_1113_13024:  # ?
                            copy_file_to_dir_1113_13024()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13025) as chmod_and_chown_1114_13025:  # 0m:0.000s
                            chmod_and_chown_1114_13025()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=13026):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13027) as should_copy_source_1115_13027:  # ?
                    should_copy_source_1115_13027()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=13028):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=13029) as copy_file_to_dir_1116_13029:  # ?
                            copy_file_to_dir_1116_13029()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13030) as chmod_and_chown_1117_13030:  # 0m:0.000s
                            chmod_and_chown_1117_13030()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=13031):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13032) as should_copy_source_1118_13032:  # ?
                    should_copy_source_1118_13032()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=13033):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=13034) as copy_file_to_dir_1119_13034:  # ?
                            copy_file_to_dir_1119_13034()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13035) as chmod_and_chown_1120_13035:  # 0m:0.000s
                            chmod_and_chown_1120_13035()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=13036):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13037) as should_copy_source_1121_13037:  # ?
                    should_copy_source_1121_13037()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=13038):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=13039) as copy_file_to_dir_1122_13039:  # ?
                            copy_file_to_dir_1122_13039()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13040) as chmod_and_chown_1123_13040:  # 0m:0.000s
                            chmod_and_chown_1123_13040()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=13041):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13042) as should_copy_source_1124_13042:  # ?
                    should_copy_source_1124_13042()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=13043):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=13044) as copy_file_to_dir_1125_13044:  # ?
                            copy_file_to_dir_1125_13044()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13045) as chmod_and_chown_1126_13045:  # 0m:0.000s
                            chmod_and_chown_1126_13045()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=13046):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13047) as should_copy_source_1127_13047:  # ?
                    should_copy_source_1127_13047()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=13048):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=13049) as copy_file_to_dir_1128_13049:  # ?
                            copy_file_to_dir_1128_13049()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13050) as chmod_and_chown_1129_13050:  # 0m:0.000s
                            chmod_and_chown_1129_13050()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=13051):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13052) as should_copy_source_1130_13052:  # ?
                    should_copy_source_1130_13052()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=13053):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=13054) as copy_file_to_dir_1131_13054:  # ?
                            copy_file_to_dir_1131_13054()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13055) as chmod_and_chown_1132_13055:  # 0m:0.000s
                            chmod_and_chown_1132_13055()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13056) as should_copy_source_1133_13056:  # ?
                    should_copy_source_1133_13056()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=13057):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=13058) as copy_file_to_dir_1134_13058:  # ?
                            copy_file_to_dir_1134_13058()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13059) as chmod_and_chown_1135_13059:  # 0m:0.000s
                            chmod_and_chown_1135_13059()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=13060):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13061) as should_copy_source_1136_13061:  # ?
                    should_copy_source_1136_13061()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=13062):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=13063) as copy_file_to_dir_1137_13063:  # ?
                            copy_file_to_dir_1137_13063()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13064) as chmod_and_chown_1138_13064:  # 0m:0.001s
                            chmod_and_chown_1138_13064()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=13065):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13066) as should_copy_source_1139_13066:  # ?
                    should_copy_source_1139_13066()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=13067):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=13068) as copy_file_to_dir_1140_13068:  # ?
                            copy_file_to_dir_1140_13068()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13069) as chmod_and_chown_1141_13069:  # 0m:0.000s
                            chmod_and_chown_1141_13069()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=13070):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13071) as should_copy_source_1142_13071:  # ?
                    should_copy_source_1142_13071()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=13072):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=13073) as copy_file_to_dir_1143_13073:  # ?
                            copy_file_to_dir_1143_13073()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13074) as chmod_and_chown_1144_13074:  # 0m:0.000s
                            chmod_and_chown_1144_13074()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=13075):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13076) as should_copy_source_1145_13076:  # ?
                    should_copy_source_1145_13076()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=13077):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=13078) as copy_file_to_dir_1146_13078:  # ?
                            copy_file_to_dir_1146_13078()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13079) as chmod_and_chown_1147_13079:  # 0m:0.000s
                            chmod_and_chown_1147_13079()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=13080):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13081) as should_copy_source_1148_13081:  # ?
                    should_copy_source_1148_13081()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=13082):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=13083) as copy_file_to_dir_1149_13083:  # ?
                            copy_file_to_dir_1149_13083()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13084) as chmod_and_chown_1150_13084:  # 0m:0.000s
                            chmod_and_chown_1150_13084()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=13085):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13086) as should_copy_source_1151_13086:  # ?
                    should_copy_source_1151_13086()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=13087):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=13088) as copy_file_to_dir_1152_13088:  # ?
                            copy_file_to_dir_1152_13088()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13089) as chmod_and_chown_1153_13089:  # 0m:0.000s
                            chmod_and_chown_1153_13089()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=13090):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13091) as should_copy_source_1154_13091:  # ?
                    should_copy_source_1154_13091()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=13092):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=13093) as copy_file_to_dir_1155_13093:  # ?
                            copy_file_to_dir_1155_13093()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13094) as chmod_and_chown_1156_13094:  # 0m:0.000s
                            chmod_and_chown_1156_13094()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=13095):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13096) as should_copy_source_1157_13096:  # ?
                    should_copy_source_1157_13096()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=13097):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=13098) as copy_file_to_dir_1158_13098:  # ?
                            copy_file_to_dir_1158_13098()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13099) as chmod_and_chown_1159_13099:  # 0m:0.000s
                            chmod_and_chown_1159_13099()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=13100):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13101) as should_copy_source_1160_13101:  # ?
                    should_copy_source_1160_13101()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=13102):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=13103) as copy_file_to_dir_1161_13103:  # ?
                            copy_file_to_dir_1161_13103()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13104) as chmod_and_chown_1162_13104:  # 0m:0.000s
                            chmod_and_chown_1162_13104()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=13105):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13106) as should_copy_source_1163_13106:  # ?
                    should_copy_source_1163_13106()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=13107):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=13108) as copy_file_to_dir_1164_13108:  # ?
                            copy_file_to_dir_1164_13108()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13109) as chmod_and_chown_1165_13109:  # 0m:0.000s
                            chmod_and_chown_1165_13109()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=13110):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13111) as should_copy_source_1166_13111:  # ?
                    should_copy_source_1166_13111()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=13112):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=13113) as copy_file_to_dir_1167_13113:  # ?
                            copy_file_to_dir_1167_13113()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13114) as chmod_and_chown_1168_13114:  # 0m:0.000s
                            chmod_and_chown_1168_13114()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=13115):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13116) as should_copy_source_1169_13116:  # ?
                    should_copy_source_1169_13116()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=13117):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=13118) as copy_file_to_dir_1170_13118:  # ?
                            copy_file_to_dir_1170_13118()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13119) as chmod_and_chown_1171_13119:  # 0m:0.000s
                            chmod_and_chown_1171_13119()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=13120):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13121) as should_copy_source_1172_13121:  # ?
                    should_copy_source_1172_13121()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=13122):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=13123) as copy_file_to_dir_1173_13123:  # ?
                            copy_file_to_dir_1173_13123()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13124) as chmod_and_chown_1174_13124:  # 0m:0.000s
                            chmod_and_chown_1174_13124()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=13125):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13126) as should_copy_source_1175_13126:  # ?
                    should_copy_source_1175_13126()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=13127):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=13128) as copy_file_to_dir_1176_13128:  # ?
                            copy_file_to_dir_1176_13128()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13129) as chmod_and_chown_1177_13129:  # 0m:0.000s
                            chmod_and_chown_1177_13129()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=13130):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13131) as should_copy_source_1178_13131:  # ?
                    should_copy_source_1178_13131()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=13132):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=13133) as copy_file_to_dir_1179_13133:  # ?
                            copy_file_to_dir_1179_13133()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13134) as chmod_and_chown_1180_13134:  # 0m:0.000s
                            chmod_and_chown_1180_13134()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=13135):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13136) as should_copy_source_1181_13136:  # ?
                    should_copy_source_1181_13136()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=13137):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=13138) as copy_file_to_dir_1182_13138:  # ?
                            copy_file_to_dir_1182_13138()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13139) as chmod_and_chown_1183_13139:  # 0m:0.000s
                            chmod_and_chown_1183_13139()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=13140):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13141) as should_copy_source_1184_13141:  # ?
                    should_copy_source_1184_13141()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=13142):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=13143) as copy_file_to_dir_1185_13143:  # ?
                            copy_file_to_dir_1185_13143()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13144) as chmod_and_chown_1186_13144:  # 0m:0.000s
                            chmod_and_chown_1186_13144()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=13145):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13146) as should_copy_source_1187_13146:  # ?
                    should_copy_source_1187_13146()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=13147):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=13148) as copy_file_to_dir_1188_13148:  # ?
                            copy_file_to_dir_1188_13148()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13149) as chmod_and_chown_1189_13149:  # 0m:0.000s
                            chmod_and_chown_1189_13149()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=13150):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13151) as should_copy_source_1190_13151:  # ?
                    should_copy_source_1190_13151()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=13152):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=13153) as copy_file_to_dir_1191_13153:  # ?
                            copy_file_to_dir_1191_13153()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13154) as chmod_and_chown_1192_13154:  # 0m:0.000s
                            chmod_and_chown_1192_13154()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=13155):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13156) as should_copy_source_1193_13156:  # ?
                    should_copy_source_1193_13156()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=13157):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=13158) as copy_file_to_dir_1194_13158:  # ?
                            copy_file_to_dir_1194_13158()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13159) as chmod_and_chown_1195_13159:  # 0m:0.000s
                            chmod_and_chown_1195_13159()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=13160):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13161) as should_copy_source_1196_13161:  # ?
                    should_copy_source_1196_13161()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=13162):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=13163) as copy_file_to_dir_1197_13163:  # ?
                            copy_file_to_dir_1197_13163()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13164) as chmod_and_chown_1198_13164:  # 0m:0.000s
                            chmod_and_chown_1198_13164()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=13165):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13166) as should_copy_source_1199_13166:  # ?
                    should_copy_source_1199_13166()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=13167):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=13168) as copy_file_to_dir_1200_13168:  # ?
                            copy_file_to_dir_1200_13168()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13169) as chmod_and_chown_1201_13169:  # 0m:0.000s
                            chmod_and_chown_1201_13169()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=13170):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13171) as should_copy_source_1202_13171:  # ?
                    should_copy_source_1202_13171()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=13172):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=13173) as copy_file_to_dir_1203_13173:  # ?
                            copy_file_to_dir_1203_13173()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13174) as chmod_and_chown_1204_13174:  # 0m:0.000s
                            chmod_and_chown_1204_13174()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=13175):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13176) as should_copy_source_1205_13176:  # ?
                    should_copy_source_1205_13176()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=13177):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=13178) as copy_file_to_dir_1206_13178:  # ?
                            copy_file_to_dir_1206_13178()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13179) as chmod_and_chown_1207_13179:  # 0m:0.000s
                            chmod_and_chown_1207_13179()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=13180):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13181) as should_copy_source_1208_13181:  # ?
                    should_copy_source_1208_13181()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=13182):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=13183) as copy_file_to_dir_1209_13183:  # ?
                            copy_file_to_dir_1209_13183()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13184) as chmod_and_chown_1210_13184:  # 0m:0.008s
                            chmod_and_chown_1210_13184()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=13185):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13186) as should_copy_source_1211_13186:  # ?
                    should_copy_source_1211_13186()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=13187):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=13188) as copy_file_to_dir_1212_13188:  # ?
                            copy_file_to_dir_1212_13188()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13189) as chmod_and_chown_1213_13189:  # 0m:0.000s
                            chmod_and_chown_1213_13189()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=13190):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13191) as should_copy_source_1214_13191:  # ?
                    should_copy_source_1214_13191()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=13192):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=13193) as copy_file_to_dir_1215_13193:  # ?
                            copy_file_to_dir_1215_13193()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13194) as chmod_and_chown_1216_13194:  # 0m:0.000s
                            chmod_and_chown_1216_13194()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=13195):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13196) as should_copy_source_1217_13196:  # ?
                    should_copy_source_1217_13196()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=13197):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=13198) as copy_file_to_dir_1218_13198:  # ?
                            copy_file_to_dir_1218_13198()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13199) as chmod_and_chown_1219_13199:  # 0m:0.000s
                            chmod_and_chown_1219_13199()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13200) as should_copy_source_1220_13200:  # ?
                    should_copy_source_1220_13200()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=13201):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=13202) as copy_file_to_dir_1221_13202:  # ?
                            copy_file_to_dir_1221_13202()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13203) as chmod_and_chown_1222_13203:  # 0m:0.000s
                            chmod_and_chown_1222_13203()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13204) as should_copy_source_1223_13204:  # ?
                    should_copy_source_1223_13204()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=13205):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=13206) as copy_file_to_dir_1224_13206:  # ?
                            copy_file_to_dir_1224_13206()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13207) as chmod_and_chown_1225_13207:  # 0m:0.000s
                            chmod_and_chown_1225_13207()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=13208):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13209) as should_copy_source_1226_13209:  # ?
                    should_copy_source_1226_13209()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=13210):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=13211) as copy_file_to_dir_1227_13211:  # ?
                            copy_file_to_dir_1227_13211()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13212) as chmod_and_chown_1228_13212:  # 0m:0.000s
                            chmod_and_chown_1228_13212()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=13213):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13214) as should_copy_source_1229_13214:  # ?
                    should_copy_source_1229_13214()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=13215):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=13216) as copy_file_to_dir_1230_13216:  # ?
                            copy_file_to_dir_1230_13216()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13217) as chmod_and_chown_1231_13217:  # 0m:0.000s
                            chmod_and_chown_1231_13217()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=13218):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13219) as should_copy_source_1232_13219:  # ?
                    should_copy_source_1232_13219()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=13220):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=13221) as copy_file_to_dir_1233_13221:  # ?
                            copy_file_to_dir_1233_13221()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13222) as chmod_and_chown_1234_13222:  # 0m:0.000s
                            chmod_and_chown_1234_13222()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=13223):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13224) as should_copy_source_1235_13224:  # ?
                    should_copy_source_1235_13224()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=13225):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=13226) as copy_file_to_dir_1236_13226:  # ?
                            copy_file_to_dir_1236_13226()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13227) as chmod_and_chown_1237_13227:  # 0m:0.000s
                            chmod_and_chown_1237_13227()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=13228):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13229) as should_copy_source_1238_13229:  # ?
                    should_copy_source_1238_13229()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=13230):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=13231) as copy_file_to_dir_1239_13231:  # ?
                            copy_file_to_dir_1239_13231()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13232) as chmod_and_chown_1240_13232:  # 0m:0.000s
                            chmod_and_chown_1240_13232()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=13233):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13234) as should_copy_source_1241_13234:  # ?
                    should_copy_source_1241_13234()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=13235):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=13236) as copy_file_to_dir_1242_13236:  # ?
                            copy_file_to_dir_1242_13236()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13237) as chmod_and_chown_1243_13237:  # 0m:0.000s
                            chmod_and_chown_1243_13237()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=13238):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13239) as should_copy_source_1244_13239:  # ?
                    should_copy_source_1244_13239()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=13240):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=13241) as copy_file_to_dir_1245_13241:  # ?
                            copy_file_to_dir_1245_13241()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13242) as chmod_and_chown_1246_13242:  # 0m:0.000s
                            chmod_and_chown_1246_13242()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=13243):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13244) as should_copy_source_1247_13244:  # ?
                    should_copy_source_1247_13244()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=13245):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=13246) as copy_file_to_dir_1248_13246:  # ?
                            copy_file_to_dir_1248_13246()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13247) as chmod_and_chown_1249_13247:  # 0m:0.000s
                            chmod_and_chown_1249_13247()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=13248) as resolve_config_vars_in_file_1250_13248:  # 0m:0.001s
                resolve_config_vars_in_file_1250_13248()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=13249) as if_1251_13249:  # 0m:0.001s
                if_1251_13249()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=13250) as resolve_config_vars_in_file_1252_13250:  # 0m:0.000s
                resolve_config_vars_in_file_1252_13250()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=13251) as if_1253_13251:  # 0m:0.000s
                if_1253_13251()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=13252) as resolve_config_vars_in_file_1254_13252:  # 0m:0.000s
                resolve_config_vars_in_file_1254_13252()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=13253) as if_1255_13253:  # 0m:0.001s
                if_1255_13253()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=13254) as resolve_config_vars_in_file_1256_13254:  # 0m:0.000s
                resolve_config_vars_in_file_1256_13254()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=13255) as if_1257_13255:  # 0m:0.000s
                if_1257_13255()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=13256) as resolve_config_vars_in_file_1258_13256:  # 0m:0.000s
                resolve_config_vars_in_file_1258_13256()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=13257) as if_1259_13257:  # 0m:0.000s
                if_1259_13257()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13258) as resolve_config_vars_in_file_1260_13258:  # 0m:0.000s
                resolve_config_vars_in_file_1260_13258()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=13259) as if_1261_13259:  # 0m:0.007s
                if_1261_13259()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=13260) as resolve_config_vars_in_file_1262_13260:  # 0m:0.000s
                resolve_config_vars_in_file_1262_13260()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=13261) as if_1263_13261:  # 0m:0.001s
                if_1263_13261()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=13262) as resolve_config_vars_in_file_1264_13262:  # 0m:0.000s
                resolve_config_vars_in_file_1264_13262()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=13263) as if_1265_13263:  # 0m:0.000s
                if_1265_13263()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=13264) as resolve_config_vars_in_file_1266_13264:  # 0m:0.000s
                resolve_config_vars_in_file_1266_13264()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=13265) as if_1267_13265:  # 0m:0.000s
                if_1267_13265()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=13266) as resolve_config_vars_in_file_1268_13266:  # 0m:0.000s
                resolve_config_vars_in_file_1268_13266()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=13267) as if_1269_13267:  # 0m:0.000s
                if_1269_13267()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=13268) as resolve_config_vars_in_file_1270_13268:  # 0m:0.000s
                resolve_config_vars_in_file_1270_13268()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=13269) as if_1271_13269:  # 0m:0.000s
                if_1271_13269()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=13270) as resolve_config_vars_in_file_1272_13270:  # 0m:0.000s
                resolve_config_vars_in_file_1272_13270()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=13271) as if_1273_13271:  # 0m:0.000s
                if_1273_13271()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=13272) as resolve_config_vars_in_file_1274_13272:  # 0m:0.000s
                resolve_config_vars_in_file_1274_13272()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=13273) as if_1275_13273:  # 0m:0.000s
                if_1275_13273()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=13274) as resolve_config_vars_in_file_1276_13274:  # 0m:0.006s
                resolve_config_vars_in_file_1276_13274()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=13275) as if_1277_13275:  # 0m:0.001s
                if_1277_13275()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=13276) as resolve_config_vars_in_file_1278_13276:  # 0m:0.001s
                resolve_config_vars_in_file_1278_13276()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=13277) as if_1279_13277:  # 0m:0.000s
                if_1279_13277()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=13278) as resolve_config_vars_in_file_1280_13278:  # 0m:0.000s
                resolve_config_vars_in_file_1280_13278()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=13279) as if_1281_13279:  # 0m:0.000s
                if_1281_13279()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13280) as resolve_config_vars_in_file_1282_13280:  # 0m:0.000s
                resolve_config_vars_in_file_1282_13280()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=13281) as if_1283_13281:  # 0m:0.000s
                if_1283_13281()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13282) as resolve_config_vars_in_file_1284_13282:  # 0m:0.000s
                resolve_config_vars_in_file_1284_13282()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=13283) as if_1285_13283:  # 0m:0.000s
                if_1285_13283()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13284) as resolve_config_vars_in_file_1286_13284:  # 0m:0.000s
                resolve_config_vars_in_file_1286_13284()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=13285) as if_1287_13285:  # 0m:0.000s
                if_1287_13285()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=13286) as resolve_config_vars_in_file_1288_13286:  # 0m:0.000s
                resolve_config_vars_in_file_1288_13286()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=13287) as if_1289_13287:  # 0m:0.000s
                if_1289_13287()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=13288) as resolve_config_vars_in_file_1290_13288:  # 0m:0.000s
                resolve_config_vars_in_file_1290_13288()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=13289) as if_1291_13289:  # 0m:0.000s
                if_1291_13289()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=13290) as resolve_config_vars_in_file_1292_13290:  # 0m:0.000s
                resolve_config_vars_in_file_1292_13290()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=13291) as if_1293_13291:  # 0m:0.001s
                if_1293_13291()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=13292) as resolve_config_vars_in_file_1294_13292:  # 0m:0.005s
                resolve_config_vars_in_file_1294_13292()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=13293) as if_1295_13293:  # 0m:0.001s
                if_1295_13293()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13294) as resolve_config_vars_in_file_1296_13294:  # 0m:0.000s
                resolve_config_vars_in_file_1296_13294()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=13295) as if_1297_13295:  # 0m:0.000s
                if_1297_13295()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=13296) as rm_file_or_dir_1298_13296:  # 0m:0.000s
                rm_file_or_dir_1298_13296()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=13297) as resolve_config_vars_in_file_1299_13297:  # 0m:0.000s
                resolve_config_vars_in_file_1299_13297()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=13298) as if_1300_13298:  # 0m:0.000s
                if_1300_13298()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=13299) as rm_file_or_dir_1301_13299:  # 0m:0.000s
                rm_file_or_dir_1301_13299()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=13300) as resolve_config_vars_in_file_1302_13300:  # 0m:0.000s
                resolve_config_vars_in_file_1302_13300()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=13301) as if_1303_13301:  # 0m:0.000s
                if_1303_13301()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=13302) as resolve_config_vars_in_file_1304_13302:  # 0m:0.000s
                resolve_config_vars_in_file_1304_13302()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=13303) as if_1305_13303:  # 0m:0.000s
                if_1305_13303()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=13304) as resolve_config_vars_in_file_1306_13304:  # 0m:0.000s
                resolve_config_vars_in_file_1306_13304()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=13305) as if_1307_13305:  # 0m:0.000s
                if_1307_13305()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=13306) as resolve_config_vars_in_file_1308_13306:  # 0m:0.000s
                resolve_config_vars_in_file_1308_13306()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=13307) as if_1309_13307:  # 0m:0.006s
                if_1309_13307()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=13308) as resolve_config_vars_in_file_1310_13308:  # 0m:0.001s
                resolve_config_vars_in_file_1310_13308()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=13309) as if_1311_13309:  # 0m:0.000s
                if_1311_13309()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=13310) as resolve_config_vars_in_file_1312_13310:  # 0m:0.000s
                resolve_config_vars_in_file_1312_13310()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=13311) as if_1313_13311:  # 0m:0.000s
                if_1313_13311()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13312) as resolve_config_vars_in_file_1314_13312:  # 0m:0.000s
                resolve_config_vars_in_file_1314_13312()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=13313) as if_1315_13313:  # 0m:0.000s
                if_1315_13313()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13314) as resolve_config_vars_in_file_1316_13314:  # 0m:0.000s
                resolve_config_vars_in_file_1316_13314()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=13315) as if_1317_13315:  # 0m:0.000s
                if_1317_13315()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=13316) as resolve_config_vars_in_file_1318_13316:  # 0m:0.001s
                resolve_config_vars_in_file_1318_13316()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=13317) as if_1319_13317:  # 0m:0.000s
                if_1319_13317()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=13318) as resolve_config_vars_in_file_1320_13318:  # 0m:0.000s
                resolve_config_vars_in_file_1320_13318()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=13319) as if_1321_13319:  # 0m:0.000s
                if_1321_13319()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=13320) as resolve_config_vars_in_file_1322_13320:  # 0m:0.000s
                resolve_config_vars_in_file_1322_13320()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=13321) as if_1323_13321:  # 0m:0.000s
                if_1323_13321()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13322) as resolve_config_vars_in_file_1324_13322:  # 0m:0.000s
                resolve_config_vars_in_file_1324_13322()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=13323) as if_1325_13323:  # 0m:0.000s
                if_1325_13323()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=13324) as resolve_config_vars_in_file_1326_13324:  # 0m:0.000s
                resolve_config_vars_in_file_1326_13324()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=13325) as if_1327_13325:  # 0m:0.006s
                if_1327_13325()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=13326) as resolve_config_vars_in_file_1328_13326:  # 0m:0.001s
                resolve_config_vars_in_file_1328_13326()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=13327) as if_1329_13327:  # 0m:0.000s
                if_1329_13327()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=13328) as resolve_config_vars_in_file_1330_13328:  # 0m:0.000s
                resolve_config_vars_in_file_1330_13328()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=13329) as if_1331_13329:  # 0m:0.000s
                if_1331_13329()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=13330) as resolve_config_vars_in_file_1332_13330:  # 0m:0.000s
                resolve_config_vars_in_file_1332_13330()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=13331) as if_1333_13331:  # 0m:0.000s
                if_1333_13331()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=13332) as resolve_config_vars_in_file_1334_13332:  # 0m:0.000s
                resolve_config_vars_in_file_1334_13332()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=13333) as if_1335_13333:  # 0m:0.000s
                if_1335_13333()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=13334) as resolve_config_vars_in_file_1336_13334:  # 0m:0.000s
                resolve_config_vars_in_file_1336_13334()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=13335) as if_1337_13335:  # 0m:0.000s
                if_1337_13335()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=13336) as resolve_config_vars_in_file_1338_13336:  # 0m:0.000s
                resolve_config_vars_in_file_1338_13336()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=13337) as if_1339_13337:  # 0m:0.000s
                if_1339_13337()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=13338) as resolve_config_vars_in_file_1340_13338:  # 0m:0.000s
                resolve_config_vars_in_file_1340_13338()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=13339) as if_1341_13339:  # 0m:0.000s
                if_1341_13339()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=13340) as resolve_config_vars_in_file_1342_13340:  # 0m:0.000s
                resolve_config_vars_in_file_1342_13340()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=13341) as if_1343_13341:  # 0m:0.000s
                if_1343_13341()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=13342) as resolve_config_vars_in_file_1344_13342:  # 0m:0.000s
                resolve_config_vars_in_file_1344_13342()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=13343) as if_1345_13343:  # 0m:0.000s
                if_1345_13343()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=13344) as resolve_config_vars_in_file_1346_13344:  # 0m:0.001s
                resolve_config_vars_in_file_1346_13344()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=13345) as if_1347_13345:  # 0m:0.001s
                if_1347_13345()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=13346) as move_file_to_file_1348_13346:  # 0m:0.020s
                move_file_to_file_1348_13346()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=13347) as resolve_config_vars_in_file_1349_13347:  # 0m:0.001s
                resolve_config_vars_in_file_1349_13347()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=13348) as if_1350_13348:  # 0m:0.000s
                if_1350_13348()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=13349) as resolve_config_vars_in_file_1351_13349:  # 0m:0.001s
                resolve_config_vars_in_file_1351_13349()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=13350) as if_1352_13350:  # 0m:0.000s
                if_1352_13350()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=13351) as resolve_config_vars_in_file_1353_13351:  # 0m:0.000s
                resolve_config_vars_in_file_1353_13351()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=13352) as if_1354_13352:  # 0m:0.000s
                if_1354_13352()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=13353) as resolve_config_vars_in_file_1355_13353:  # 0m:0.000s
                resolve_config_vars_in_file_1355_13353()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=13354) as if_1356_13354:  # 0m:0.000s
                if_1356_13354()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=13355) as resolve_config_vars_in_file_1357_13355:  # 0m:0.000s
                resolve_config_vars_in_file_1357_13355()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=13356) as if_1358_13356:  # 0m:0.000s
                if_1358_13356()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13357) as resolve_config_vars_in_file_1359_13357:  # 0m:0.000s
                resolve_config_vars_in_file_1359_13357()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=13358) as if_1360_13358:  # 0m:0.001s
                if_1360_13358()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=13359) as resolve_config_vars_in_file_1361_13359:  # 0m:0.006s
                resolve_config_vars_in_file_1361_13359()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=13360) as if_1362_13360:  # 0m:0.001s
                if_1362_13360()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=13361) as resolve_config_vars_in_file_1363_13361:  # 0m:0.000s
                resolve_config_vars_in_file_1363_13361()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=13362) as if_1364_13362:  # 0m:0.000s
                if_1364_13362()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=13363) as resolve_config_vars_in_file_1365_13363:  # 0m:0.000s
                resolve_config_vars_in_file_1365_13363()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=13364) as if_1366_13364:  # 0m:0.000s
                if_1366_13364()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=13365) as resolve_config_vars_in_file_1367_13365:  # 0m:0.000s
                resolve_config_vars_in_file_1367_13365()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=13366) as if_1368_13366:  # 0m:0.000s
                if_1368_13366()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=13367) as resolve_config_vars_in_file_1369_13367:  # 0m:0.000s
                resolve_config_vars_in_file_1369_13367()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=13368) as if_1370_13368:  # 0m:0.000s
                if_1370_13368()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=13369) as resolve_config_vars_in_file_1371_13369:  # 0m:0.000s
                resolve_config_vars_in_file_1371_13369()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=13370) as if_1372_13370:  # 0m:0.000s
                if_1372_13370()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13371) as resolve_config_vars_in_file_1373_13371:  # 0m:0.000s
                resolve_config_vars_in_file_1373_13371()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=13372) as if_1374_13372:  # 0m:0.000s
                if_1374_13372()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=13373) as resolve_config_vars_in_file_1375_13373:  # 0m:0.000s
                resolve_config_vars_in_file_1375_13373()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=13374) as if_1376_13374:  # 0m:0.000s
                if_1376_13374()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=13375) as resolve_config_vars_in_file_1377_13375:  # 0m:0.000s
                resolve_config_vars_in_file_1377_13375()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=13376) as if_1378_13376:  # 0m:0.000s
                if_1378_13376()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=13377) as resolve_config_vars_in_file_1379_13377:  # 0m:0.006s
                resolve_config_vars_in_file_1379_13377()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=13378) as if_1380_13378:  # 0m:0.001s
                if_1380_13378()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=13379) as resolve_config_vars_in_file_1381_13379:  # 0m:0.000s
                resolve_config_vars_in_file_1381_13379()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=13380) as if_1382_13380:  # 0m:0.000s
                if_1382_13380()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=13381) as resolve_config_vars_in_file_1383_13381:  # 0m:0.000s
                resolve_config_vars_in_file_1383_13381()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=13382) as if_1384_13382:  # 0m:0.000s
                if_1384_13382()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=13383) as resolve_config_vars_in_file_1385_13383:  # 0m:0.000s
                resolve_config_vars_in_file_1385_13383()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=13384) as if_1386_13384:  # 0m:0.000s
                if_1386_13384()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=13385) as resolve_config_vars_in_file_1387_13385:  # 0m:0.000s
                resolve_config_vars_in_file_1387_13385()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=13386) as if_1388_13386:  # 0m:0.000s
                if_1388_13386()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=13387) as resolve_config_vars_in_file_1389_13387:  # 0m:0.000s
                resolve_config_vars_in_file_1389_13387()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=13388) as if_1390_13388:  # 0m:0.000s
                if_1390_13388()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=13389) as resolve_config_vars_in_file_1391_13389:  # 0m:0.000s
                resolve_config_vars_in_file_1391_13389()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=13390) as if_1392_13390:  # 0m:0.000s
                if_1392_13390()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13391) as resolve_config_vars_in_file_1393_13391:  # 0m:0.000s
                resolve_config_vars_in_file_1393_13391()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=13392) as if_1394_13392:  # 0m:0.000s
                if_1394_13392()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13393) as resolve_config_vars_in_file_1395_13393:  # 0m:0.000s
                resolve_config_vars_in_file_1395_13393()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=13394) as if_1396_13394:  # 0m:0.000s
                if_1396_13394()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=13395) as resolve_config_vars_in_file_1397_13395:  # 0m:0.000s
                resolve_config_vars_in_file_1397_13395()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=13396) as if_1398_13396:  # 0m:0.001s
                if_1398_13396()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13397) as resolve_config_vars_in_file_1399_13397:  # 0m:0.000s
                resolve_config_vars_in_file_1399_13397()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=13398) as if_1400_13398:  # 0m:0.000s
                if_1400_13398()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=13399) as resolve_config_vars_in_file_1401_13399:  # 0m:0.000s
                resolve_config_vars_in_file_1401_13399()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=13400) as if_1402_13400:  # 0m:0.000s
                if_1402_13400()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13401) as resolve_config_vars_in_file_1403_13401:  # 0m:0.000s
                resolve_config_vars_in_file_1403_13401()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=13402) as if_1404_13402:  # 0m:0.000s
                if_1404_13402()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=13403) as rm_file_or_dir_1405_13403:  # 0m:0.000s
                rm_file_or_dir_1405_13403()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=13404) as rm_file_or_dir_1406_13404:  # 0m:0.000s
                rm_file_or_dir_1406_13404()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=13405) as rm_file_or_dir_1407_13405:  # 0m:0.000s
                rm_file_or_dir_1407_13405()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13406) as resolve_config_vars_in_file_1408_13406:  # 0m:0.000s
                resolve_config_vars_in_file_1408_13406()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=13407) as if_1409_13407:  # 0m:0.000s
                if_1409_13407()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13408) as resolve_config_vars_in_file_1410_13408:  # 0m:0.000s
                resolve_config_vars_in_file_1410_13408()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=13409) as if_1411_13409:  # 0m:0.000s
                if_1411_13409()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=13410) as resolve_config_vars_in_file_1412_13410:  # 0m:0.000s
                resolve_config_vars_in_file_1412_13410()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=13411) as if_1413_13411:  # 0m:0.000s
                if_1413_13411()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=13412) as rm_file_or_dir_1414_13412:  # 0m:0.000s
                rm_file_or_dir_1414_13412()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=13413) as rm_file_or_dir_1415_13413:  # 0m:0.000s
                rm_file_or_dir_1415_13413()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=13414) as rm_file_or_dir_1416_13414:  # 0m:0.000s
                rm_file_or_dir_1416_13414()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=13415) as resolve_config_vars_in_file_1417_13415:  # 0m:0.000s
                resolve_config_vars_in_file_1417_13415()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=13416) as if_1418_13416:  # 0m:0.000s
                if_1418_13416()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=13417) as resolve_config_vars_in_file_1419_13417:  # 0m:0.000s
                resolve_config_vars_in_file_1419_13417()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=13418) as if_1420_13418:  # 0m:0.000s
                if_1420_13418()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13419) as resolve_config_vars_in_file_1421_13419:  # 0m:0.000s
                resolve_config_vars_in_file_1421_13419()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=13420) as if_1422_13420:  # 0m:0.000s
                if_1422_13420()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=13421) as resolve_config_vars_in_file_1423_13421:  # 0m:0.000s
                resolve_config_vars_in_file_1423_13421()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=13422) as if_1424_13422:  # 0m:0.000s
                if_1424_13422()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13423) as resolve_config_vars_in_file_1425_13423:  # 0m:0.000s
                resolve_config_vars_in_file_1425_13423()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=13424) as if_1426_13424:  # 0m:0.000s
                if_1426_13424()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=13425) as resolve_config_vars_in_file_1427_13425:  # 0m:0.006s
                resolve_config_vars_in_file_1427_13425()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=13426) as if_1428_13426:  # 0m:0.001s
                if_1428_13426()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=13427) as resolve_config_vars_in_file_1429_13427:  # 0m:0.000s
                resolve_config_vars_in_file_1429_13427()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=13428) as if_1430_13428:  # 0m:0.000s
                if_1430_13428()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=13429) as resolve_config_vars_in_file_1431_13429:  # 0m:0.000s
                resolve_config_vars_in_file_1431_13429()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=13430) as if_1432_13430:  # 0m:0.000s
                if_1432_13430()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=13431) as cd_stage_1433_13431:  # 0m:0.022s
            cd_stage_1433_13431()
            with Stage(r"copy", r"WavesReWireDevice v13.0.0.129", prog_num=13432):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13433) as should_copy_source_1434_13433:  # ?
                    should_copy_source_1434_13433()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=13434):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=13435) as copy_dir_to_dir_1435_13435:  # ?
                            copy_dir_to_dir_1435_13435()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=13436) as unwtar_1436_13436:  # ?
                            unwtar_1436_13436()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=13437, recursive=True) as chown_1437_13437:  # 0m:0.001s
                            chown_1437_13437()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13438) as should_copy_source_1438_13438:  # ?
                    should_copy_source_1438_13438()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=13439):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=13440) as copy_dir_to_dir_1439_13440:  # ?
                            copy_dir_to_dir_1439_13440()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=13441) as unwtar_1440_13441:  # ?
                            unwtar_1440_13441()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=13442, recursive=True) as chown_1441_13442:  # 0m:0.000s
                            chown_1441_13442()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13443) as shell_command_1442_13443:  # 0m:0.020s
                shell_command_1442_13443()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=13444) as cd_stage_1443_13444:  # 0m:0.003s
            cd_stage_1443_13444()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=13445):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=13446) as should_copy_source_1444_13446:  # ?
                    should_copy_source_1444_13446()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=13447):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=13448) as copy_dir_to_dir_1445_13448:  # ?
                            copy_dir_to_dir_1445_13448()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=13449, recursive=True) as chown_1446_13449:  # 0m:0.001s
                            chown_1446_13449()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=13450):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=13451) as should_copy_source_1447_13451:  # ?
                    should_copy_source_1447_13451()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=13452):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=13453) as copy_dir_to_dir_1448_13453:  # ?
                            copy_dir_to_dir_1448_13453()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=13454) as unwtar_1449_13454:  # ?
                            unwtar_1449_13454()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=13455, recursive=True) as chown_1450_13455:  # 0m:0.001s
                            chown_1450_13455()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=13456) as cd_stage_1451_13456:  # 0m:0.001s
            cd_stage_1451_13456()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=13457):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=13458) as should_copy_source_1452_13458:  # ?
                    should_copy_source_1452_13458()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=13459):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=13460) as copy_dir_to_dir_1453_13460:  # ?
                            copy_dir_to_dir_1453_13460()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=13461) as unwtar_1454_13461:  # ?
                            unwtar_1454_13461()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=13462, recursive=True) as chown_1455_13462:  # 0m:0.001s
                            chown_1455_13462()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=13463) as cd_stage_1456_13463:  # 0m:0.001s
            cd_stage_1456_13463()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=13464):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=13465) as should_copy_source_1457_13465:  # ?
                    should_copy_source_1457_13465()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=13466):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=13467) as copy_dir_to_dir_1458_13467:  # ?
                            copy_dir_to_dir_1458_13467()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=13468, recursive=True) as chown_1459_13468:  # 0m:0.001s
                            chown_1459_13468()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=13469) as cd_stage_1460_13469:  # 0m:0.001s
            cd_stage_1460_13469()
            with Stage(r"copy", r"License Notifications 1.1 v1.1", prog_num=13470):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=13471) as should_copy_source_1461_13471:  # ?
                    should_copy_source_1461_13471()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=13472):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=13473) as copy_dir_to_dir_1462_13473:  # ?
                            copy_dir_to_dir_1462_13473()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=13474, recursive=True) as chown_1463_13474:  # 0m:0.001s
                            chown_1463_13474()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=13475) as cd_stage_1464_13475:  # 0m:10.621s
            cd_stage_1464_13475()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=13476) as rm_file_or_dir_1465_13476:  # 0m:0.000s
                rm_file_or_dir_1465_13476()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=13477):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=13478) as should_copy_source_1466_13478:  # ?
                    should_copy_source_1466_13478()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=13479):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13480) as copy_dir_to_dir_1467_13480:  # ?
                            copy_dir_to_dir_1467_13480()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=13481) as unwtar_1468_13481:  # ?
                            unwtar_1468_13481()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=13482, recursive=True) as chown_1469_13482:  # 0m:0.001s
                            chown_1469_13482()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=13483):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=13484) as should_copy_source_1470_13484:  # 0m:0.005s
                    should_copy_source_1470_13484()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=13485):  # 0m:0.005s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=13486) as unwtar_1471_13486:  # 0m:0.004s
                            unwtar_1471_13486()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=13487):  # 0m:5.793s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13488) as should_copy_source_1472_13488:  # 0m:5.793s
                    should_copy_source_1472_13488()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=13489):  # 0m:5.793s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=13490) as copy_dir_to_dir_1473_13490:  # 0m:0.011s
                            copy_dir_to_dir_1473_13490()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=13491) as unwtar_1474_13491:  # 0m:5.781s
                            unwtar_1474_13491()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=13492, recursive=True) as chown_1475_13492:  # 0m:0.000s
                            chown_1475_13492()
            with Stage(r"copy", r"OpenVino_2021.4.689 v2021.4.689", prog_num=13493):  # 0m:4.805s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13494) as should_copy_source_1476_13494:  # 0m:4.805s
                    should_copy_source_1476_13494()
                    with Stage(r"copy source", r"Mac/Modules/openvino", prog_num=13495):  # 0m:4.804s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r".", delete_extraneous_files=True, prog_num=13496) as copy_dir_to_dir_1477_13496:  # 0m:0.325s
                            copy_dir_to_dir_1477_13496()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", where_to_unwtar=r".", prog_num=13497) as unwtar_1478_13497:  # 0m:4.479s
                            unwtar_1478_13497()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/openvino", user_id=-1, group_id=-1, prog_num=13498, recursive=True) as chown_1479_13498:  # 0m:0.000s
                            chown_1479_13498()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=13499):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=13500) as should_copy_source_1480_13500:  # ?
                    should_copy_source_1480_13500()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=13501):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13502) as copy_dir_to_dir_1481_13502:  # ?
                            copy_dir_to_dir_1481_13502()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=13503) as chmod_1482_13503:  # ?
                            chmod_1482_13503()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=13504) as chmod_1483_13504:  # ?
                            chmod_1483_13504()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=13505, recursive=True) as chown_1484_13505:  # 0m:0.001s
                            chown_1484_13505()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=13508) as resolve_symlink_files_in_folder_1485_13508:  # 0m:0.002s
                resolve_symlink_files_in_folder_1485_13508()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13509) as shell_command_1486_13509:  # 0m:0.014s
                shell_command_1486_13509()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=13510) as cd_stage_1487_13510:  # 0m:0.001s
            cd_stage_1487_13510()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=13511):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=13512) as should_copy_source_1488_13512:  # ?
                    should_copy_source_1488_13512()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=13513):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=13514) as copy_dir_to_dir_1489_13514:  # ?
                            copy_dir_to_dir_1489_13514()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=13515, recursive=True) as chown_1490_13515:  # 0m:0.001s
                            chown_1490_13515()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=13516) as cd_stage_1491_13516:  # 0m:2.409s
            cd_stage_1491_13516()
            with Stage(r"copy", r"Waves Local Server v12.15.417.313", prog_num=13517):  # 0m:2.409s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=13518) as should_copy_source_1492_13518:  # 0m:2.409s
                    should_copy_source_1492_13518()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=13519):  # 0m:2.408s
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=13520, recursive=True) as chmod_1493_13520:  # 0m:0.011s
                            chmod_1493_13520()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13521) as copy_dir_to_dir_1494_13521:  # 0m:0.071s
                            copy_dir_to_dir_1494_13521()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=13522) as unwtar_1495_13522:  # 0m:2.325s
                            unwtar_1495_13522()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=13523, recursive=True) as chown_1496_13523:  # 0m:0.000s
                            chown_1496_13523()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13524) as if_1497_13524:  # 0m:0.001s
                            if_1497_13524()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=13525) as cd_stage_1498_13525:  # 0m:10.410s
            cd_stage_1498_13525()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.178.179", prog_num=13526):  # 0m:10.409s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=13527) as should_copy_source_1499_13527:  # 0m:10.409s
                    should_copy_source_1499_13527()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=13528):  # 0m:10.409s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13529) as copy_dir_to_dir_1500_13529:  # 0m:0.195s
                            copy_dir_to_dir_1500_13529()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=13530) as unwtar_1501_13530:  # 0m:10.212s
                            unwtar_1501_13530()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=13531, recursive=True) as chown_1502_13531:  # 0m:0.000s
                            chown_1502_13531()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250508010011-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13532) as if_1503_13532:  # 0m:0.001s
                            if_1503_13532()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=13533) as cd_stage_1504_13533:  # 0m:2.676s
            cd_stage_1504_13533()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=13534):  # 0m:1.314s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13535) as should_copy_source_1505_13535:  # 0m:1.314s
                    should_copy_source_1505_13535()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=13536):  # 0m:1.313s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=13537) as copy_dir_to_dir_1506_13537:  # 0m:0.031s
                            copy_dir_to_dir_1506_13537()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=13538) as unwtar_1507_13538:  # 0m:1.189s
                            unwtar_1507_13538()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13539, recursive=True) as chown_1508_13539:  # 0m:0.004s
                            chown_1508_13539()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=13540) as break_hard_link_1509_13540:  # 0m:0.028s
                            break_hard_link_1509_13540()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=13541) as shell_command_1510_13541:  # 0m:0.051s
                            shell_command_1510_13541()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13542, recursive=True) as chown_1511_13542:  # 0m:0.000s
                            chown_1511_13542()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=13543, recursive=True) as chmod_1512_13543:  # 0m:0.010s
                            chmod_1512_13543()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=13544):  # 0m:1.361s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13545) as should_copy_source_1513_13545:  # 0m:1.361s
                    should_copy_source_1513_13545()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=13546):  # 0m:1.360s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=13547) as copy_dir_to_dir_1514_13547:  # 0m:0.107s
                            copy_dir_to_dir_1514_13547()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=13548) as unwtar_1515_13548:  # 0m:1.159s
                            unwtar_1515_13548()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13549, recursive=True) as chown_1516_13549:  # 0m:0.000s
                            chown_1516_13549()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=13550) as break_hard_link_1517_13550:  # 0m:0.030s
                            break_hard_link_1517_13550()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=13551) as shell_command_1518_13551:  # 0m:0.053s
                            shell_command_1518_13551()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13552, recursive=True) as chown_1519_13552:  # 0m:0.001s
                            chown_1519_13552()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=13553, recursive=True) as chmod_1520_13553:  # 0m:0.009s
                            chmod_1520_13553()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=13554) as cd_stage_1521_13554:  # 0m:0.002s
            cd_stage_1521_13554()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=13555):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13556) as should_copy_source_1522_13556:  # ?
                    should_copy_source_1522_13556()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=13557):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=13558) as copy_dir_to_dir_1523_13558:  # ?
                            copy_dir_to_dir_1523_13558()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=13559) as unwtar_1524_13559:  # ?
                            unwtar_1524_13559()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=13560, recursive=True) as chown_1525_13560:  # ?
                            chown_1525_13560()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=13561) as shell_command_1526_13561:  # 0m:0.001s
                            shell_command_1526_13561()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=13562):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13563) as should_copy_source_1527_13563:  # ?
                    should_copy_source_1527_13563()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=13564):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=13565) as copy_dir_to_dir_1528_13565:  # ?
                            copy_dir_to_dir_1528_13565()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=13566) as unwtar_1529_13566:  # ?
                            unwtar_1529_13566()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=13567, recursive=True) as chown_1530_13567:  # ?
                            chown_1530_13567()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=13568) as shell_command_1531_13568:  # 0m:0.000s
                            shell_command_1531_13568()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13569) as cd_stage_1532_13569:  # 0m:0.002s
            cd_stage_1532_13569()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=13570):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13571) as should_copy_source_1533_13571:  # ?
                    should_copy_source_1533_13571()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=13572):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=13573) as copy_dir_to_dir_1534_13573:  # ?
                            copy_dir_to_dir_1534_13573()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=13574) as unwtar_1535_13574:  # ?
                            unwtar_1535_13574()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=13575, recursive=True) as chown_1536_13575:  # ?
                            chown_1536_13575()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13576) as shell_command_1537_13576:  # ?
                            shell_command_1537_13576()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13577) as script_command_1538_13577:  # ?
                            script_command_1538_13577()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13578) as shell_command_1539_13578:  # 0m:0.001s
                            shell_command_1539_13578()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=13579):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13580) as should_copy_source_1540_13580:  # ?
                    should_copy_source_1540_13580()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=13581):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=13582) as copy_dir_to_dir_1541_13582:  # ?
                            copy_dir_to_dir_1541_13582()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=13583) as unwtar_1542_13583:  # ?
                            unwtar_1542_13583()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=13584, recursive=True) as chown_1543_13584:  # ?
                            chown_1543_13584()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13585) as shell_command_1544_13585:  # ?
                            shell_command_1544_13585()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13586) as script_command_1545_13586:  # ?
                            script_command_1545_13586()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13587) as shell_command_1546_13587:  # 0m:0.001s
                            shell_command_1546_13587()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13588) as create_symlink_1547_13588:  # 0m:0.000s
                create_symlink_1547_13588()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13589) as create_symlink_1548_13589:  # 0m:0.000s
                create_symlink_1548_13589()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=13590) as cd_stage_1549_13590:  # 0m:0.000s
            cd_stage_1549_13590()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=13591) as rm_file_or_dir_1550_13591:  # 0m:0.000s
                rm_file_or_dir_1550_13591()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=13592) as cd_stage_1551_13592:  # 0m:0.000s
            cd_stage_1551_13592()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=13593) as rm_file_or_dir_1552_13593:  # 0m:0.000s
                rm_file_or_dir_1552_13593()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=13594) as rm_file_or_dir_1553_13594:  # 0m:0.000s
                rm_file_or_dir_1553_13594()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=13595) as rm_file_or_dir_1554_13595:  # 0m:0.000s
                rm_file_or_dir_1554_13595()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=13596) as shell_command_1555_13596:  # 0m:0.009s
            shell_command_1555_13596()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=13597) as shell_command_1556_13597:  # 0m:0.093s
            shell_command_1556_13597()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=13598) as script_command_1557_13598:  # 0m:0.014s
            script_command_1557_13598()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=13599) as rm_file_or_dir_1558_13599:  # 0m:0.001s
            rm_file_or_dir_1558_13599()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13600) as move_dir_to_dir_1559_13600:  # 0m:0.000s
            move_dir_to_dir_1559_13600()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13601) as move_dir_to_dir_1560_13601:  # 0m:0.000s
            move_dir_to_dir_1560_13601()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13602) as move_dir_to_dir_1561_13602:  # 0m:0.000s
            move_dir_to_dir_1561_13602()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13603) as move_dir_to_dir_1562_13603:  # 0m:0.000s
            move_dir_to_dir_1562_13603()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=13604) as make_dirs_1563_13604:  # 0m:0.011s
            make_dirs_1563_13604()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13605) as move_dir_to_dir_1564_13605:  # 0m:0.000s
            move_dir_to_dir_1564_13605()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13606) as move_dir_to_dir_1565_13606:  # 0m:0.000s
            move_dir_to_dir_1565_13606()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=13607) as shell_command_1566_13607:  # 0m:0.100s
            shell_command_1566_13607()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=13608) as script_command_1567_13608:  # 0m:0.011s
            script_command_1567_13608()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=13609) as rm_file_or_dir_1568_13609:  # 0m:0.001s
            rm_file_or_dir_1568_13609()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13610) as glober_1569_13610:  # 0m:0.001s
            glober_1569_13610()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=13611) as glober_1570_13611:  # 0m:0.001s
            glober_1570_13611()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13612) as glober_1571_13612:  # 0m:0.001s
            glober_1571_13612()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=13613) as glober_1572_13613:  # 0m:0.001s
            glober_1572_13613()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=13614) as shell_command_1573_13614:  # 0m:4.002s
            shell_command_1573_13614()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=13615) as shell_command_1574_13615:  # 0m:0.106s
            shell_command_1574_13615()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=13616) as script_command_1575_13616:  # 0m:0.012s
            script_command_1575_13616()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=13617) as if_1576_13617:  # 0m:0.001s
            if_1576_13617()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13618) as if_1577_13618:  # 0m:0.000s
            if_1577_13618()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=13619) as if_1578_13619:  # 0m:0.000s
            if_1578_13619()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13620) as if_1579_13620:  # 0m:0.000s
            if_1579_13620()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=13621) as make_dir_1580_13621:  # 0m:0.011s
            make_dir_1580_13621()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=13622) as chmod_1581_13622:  # 0m:0.001s
            chmod_1581_13622()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=13623) as make_dir_1582_13623:  # 0m:0.015s
            make_dir_1582_13623()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=13624) as chmod_1583_13624:  # 0m:0.001s
            chmod_1583_13624()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13625) as chmod_1584_13625:  # 0m:0.000s
            chmod_1584_13625()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13626) as chmod_1585_13626:  # 0m:0.000s
            chmod_1585_13626()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=13627) as chmod_1586_13627:  # 0m:0.000s
            chmod_1586_13627()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=13628) as shell_command_1587_13628:  # 0m:0.100s
            shell_command_1587_13628()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=13629) as script_command_1588_13629:  # 0m:0.013s
            script_command_1588_13629()
    with Stage(r"post-copy", prog_num=13630):  # 0m:0.062s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13631) as make_dir_1589_13631:  # 0m:0.011s
            make_dir_1589_13631()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=13632) as copy_file_to_file_1590_13632:  # 0m:0.018s
            copy_file_to_file_1590_13632()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13633) as chmod_1591_13633:  # 0m:0.000s
            chmod_1591_13633()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13634) as chmod_1592_13634:  # 0m:0.000s
            chmod_1592_13634()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=13635) as copy_file_to_file_1593_13635:  # 0m:0.015s
            copy_file_to_file_1593_13635()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13636) as chmod_1594_13636:  # 0m:0.000s
            chmod_1594_13636()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=13637) as copy_file_to_file_1595_13637:  # 0m:0.015s
            copy_file_to_file_1595_13637()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13638) as chmod_1596_13638:  # 0m:0.000s
            chmod_1596_13638()
        Progress(r"Done copy", prog_num=13639)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=13640)()  # 0m:0.000s
    with Stage(r"post", prog_num=13641):  # 0m:0.088s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13642) as make_dir_1597_13642:  # 0m:0.015s
            make_dir_1597_13642()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=13643) as copy_file_to_file_1598_13643:  # 0m:0.016s
            copy_file_to_file_1598_13643()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13644) as make_dir_1599_13644:  # 0m:0.012s
            make_dir_1599_13644()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=13645) as copy_file_to_file_1600_13645:  # 0m:0.014s
            copy_file_to_file_1600_13645()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13646) as make_dir_1601_13646:  # 0m:0.015s
            make_dir_1601_13646()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/53/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=13647) as copy_file_to_file_1602_13647:  # 0m:0.016s
            copy_file_to_file_1602_13647()

with Stage(r"epilog", prog_num=13648):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250508010011.py", prog_num=13649) as patch_py_batch_with_timings_1603_13649:  # ?
        patch_py_batch_with_timings_1603_13649()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 130687960 bytes in 1m:16.782s, 1702064 bytes per second
# copy time 0m:46.641s
