# Creation time: 28-07-25_10-27
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 16995
PythonBatchCommandBase.running_progress = 1277
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1278):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250728102636"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX")
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
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 9
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1Mzc0ODc5Nn0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUzNzEyNDk2fX19XX0_;CloudFront-Signature=FLUHeUm9agYhFxUrPms-oBNMgDeDDis5WJEsrSzxmtpblFFGxIH3-psw1KPhv07QUBZEY2aZadCNose1PfBid37HG~-IQdd~ho1x3L53ss2wtbx03tVerjyQvOnR10xGLfiaNKCzJxrkJ52RsMltWcoATvi9fTG~giF4P523d2YLlUjiqw63HMKUud6u5UdI1VZoQPjGgmNv6qR8wHQfgQ5pddElUmLtX06qI5nFIcxuBEZs8nfssAtN0sRvGhpjlKQfQGqwJk-~8m6ZzaCCIwfZkYKBk-JxOePU68ZsXC6GCkbswvCzpSsjvvE1QOIqT-UrmDXO8h5pNjHS9TdNrA__"
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
    config_vars['INDEX_CHECKSUM'] = r"80c6dd28fcda4627bfd6aef575d14ae1d053dfeb"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/09/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"3d05d6347922069f7789de52564fbaeee7975cd8"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/09/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/09/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"1374eaac-1f40-4629-a1bd-7fad36931856", r"1b2e3046-b634-4fc3-92df-100722e72a75", r"1d2e15ad-514e-4894-b13c-087940f2c275", r"215572dc-9c91-4912-a0a9-d68096edc994", r"22195f90-44a7-41aa-8e89-7cd4032a553e", r"239c7584-82a0-420d-bfae-8885b3a52538", r"289510f1-fdf8-45ee-ae8d-4f42cc82ca64", r"29e06aff-907d-4711-a74e-3f8a59d69d79", r"2acada14-94c5-4414-9d64-454da34b0639", r"2d71ad91-bddb-42f2-a652-835830176f9f", r"30917ee9-a700-481d-85d7-2062c35a9802", r"3164b0cb-806c-4bdd-a286-260f9c6eb04c", r"329dbe6a-233e-4f8f-ac70-f5b55036845b", r"34ec8670-67d0-4e60-9e6a-3a3d15146c3c", r"386ca2e5-2636-495f-810e-49eceb953b9f", r"3c217951-f061-42a9-a797-c6ae08355e8d", r"3cc8e3c0-c209-4128-a2f6-32be589badbf", r"3d47fe76-e1f9-4cbf-b155-715460ee749f", r"423381b7-4e7e-41e2-a69a-518aefd4ef13", r"49e069d6-907d-4991-a74e-3f8959d69830", r"51472ece-6f53-4926-8123-64330d6c6852", r"53a2fb95-8424-429f-a2c8-21e86b847f0a", r"558c21cb-b648-48a3-a23b-db455ecc2d55", r"5634fda9-ea28-4316-9476-527b8e7279a9", r"5daf4282-f6c5-4e00-b7d5-cac37ad48604", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"63b0a9f9-a701-4596-acb7-ab671e5addd9", r"6983b49f-2238-4e1e-8828-50ca84f58737", r"6c7cdfec-03f7-4d62-84c3-9ea633067fc9", r"72e4f2f3-cc29-4635-8715-a7977a943920", r"7707a80e-06f0-412a-b2de-baa2c332bb13", r"7c01bd8c-6267-48ce-8707-9df05b786b7b", r"811b0faa-6979-4500-a187-791e07c79138", r"87d5ca54-c659-460d-92ca-d25786210a25", r"8ce7a272-1741-4893-b516-e93ce40db756", r"911c58f1-0b6b-42f7-93dd-a571b29860fc", r"96f2b292-8c3b-49f4-8193-4f7783654547", r"aa264888-988b-421c-89c9-629934734f37", r"ab09a527-4793-44f2-9353-c25cc1f4b856", r"ae4b9cc6-a30f-42ad-b4db-28cb21cda94b", r"b158aea5-79f7-4a39-b9b9-f8c5e7c237c2", r"b3964c48-04db-470f-b5b8-fa2b340a6fd4", r"b8a31ecd-5110-4d10-ba3d-ca56215b3745", r"c19c1d27-90ca-43e3-b503-9c7f2da272bc", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"ca9a4322-a903-43ec-95d7-ccbbb475d2d5", r"d1b17f75-9fbf-4af9-9c8e-ebb7068998b9", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"dfc80d80-ad21-11e0-804c-b7fd7bebd530", r"dfe64476-ad21-11e0-80e3-b7fd7bebd530", r"e0052ccd-ad21-11e0-81d6-b7fd7bebd530", r"e023b7a0-ad21-11e0-80bf-b7fd7bebd530", r"e0427e39-ad21-11e0-832d-b7fd7bebd530", r"e06158e4-ad21-11e0-80ed-b7fd7bebd530", r"e09dd956-ad21-11e0-80a8-b7fd7bebd530", r"e10288b9-ad21-11e0-8381-b7fd7bebd530", r"e1e91460-ad21-11e0-8303-b7fd7bebd530", r"e22cd127-ad21-11e0-822b-b7fd7bebd530", r"e39dce24-16c9-4f4a-bb98-545e10052b75", r"e3a57973-ad21-11e0-818c-b7fd7bebd530", r"e3c605a4-ad21-11e0-8113-b7fd7bebd530", r"e47a4b22-ad21-11e0-80ba-b7fd7bebd530", r"e4b00ec4-ad21-11e0-834b-b7fd7bebd530", r"e4e5fb53-131e-45e0-91c1-d78aa4f5c69f", r"e4e72e7b-ad21-11e0-81a6-b7fd7bebd530", r"e5100b89-ad21-11e0-81a0-b7fd7bebd530", r"e551833a-ad21-11e0-8177-b7fd7bebd530", r"e591e90a-ad21-11e0-83a1-b7fd7bebd530", r"e5ce4a76-ad21-11e0-832b-b7fd7bebd530", r"e5ecb58a-ad21-11e0-820b-b7fd7bebd530", r"e60ab8c6-ad21-11e0-8364-b7fd7bebd530", r"e6281b3c-ad21-11e0-8087-b7fd7bebd530", r"e646beb6-ad21-11e0-83c3-b7fd7bebd530", r"e6675177-ad21-11e0-833e-b7fd7bebd530", r"e686154a-ad21-11e0-806f-b7fd7bebd530", r"e686394e-ad21-11e0-8185-b7fd7bebd530", r"e6a8de66-ad21-11e0-81f4-b7fd7bebd530", r"e6c7625a-ad21-11e0-8262-b7fd7bebd530", r"e6ead714-ad21-11e0-82a6-b7fd7bebd530", r"e7069133-ad21-11e0-82c1-b7fd7bebd530", r"e7223951-ad21-11e0-82d3-b7fd7bebd530", r"e73ed1fb-ad21-11e0-8035-b7fd7bebd530", r"e759bc5f-ad21-11e0-827d-b7fd7bebd530", r"e775f5e1-ad21-11e0-809f-b7fd7bebd530", r"e790fd1a-ad21-11e0-82c3-b7fd7bebd530", r"e7af58a0-ad21-11e0-832f-b7fd7bebd530", r"e7cd30b4-ad21-11e0-8385-b7fd7bebd530", r"e808505c-ad21-11e0-83e8-b7fd7bebd530", r"e8f6b97d-ad21-11e0-8088-b7fd7bebd530", r"e92b2cea-ad21-11e0-8218-b7fd7bebd530", r"e9797602-ad21-11e0-8369-b7fd7bebd530", r"e9ef3ffd-ad21-11e0-83e3-b7fd7bebd530", r"ea1152ba-ad21-11e0-8305-b7fd7bebd530", r"ea4ad51a-ad21-11e0-8137-b7fd7bebd530", r"ea812d41-ad21-11e0-80f3-b7fd7bebd530", r"ea9c2b7e-ad21-11e0-8327-b7fd7bebd530", r"eab8d633-ad21-11e0-81eb-b7fd7bebd530", r"eb0c63ec-ad21-11e0-8288-b7fd7bebd530", r"eb542f98-ad21-11e0-8222-b7fd7bebd530", r"eb621b67-ad21-11e0-8319-b7fd7bebd530", r"ec32123c-ad21-11e0-83d2-b7fd7bebd530", r"ec53f8dd-ad21-11e0-8276-b7fd7bebd530", r"ec541a62-ad21-11e0-8150-b7fd7bebd530", r"ec719e28-ad21-11e0-8100-b7fd7bebd530", r"ec971ad7-ad21-11e0-8359-b7fd7bebd530", r"ec97493f-ad21-11e0-803e-b7fd7bebd530", r"ed13f26a-ad21-11e0-8216-b7fd7bebd530", r"ed14136b-ad21-11e0-837c-b7fd7bebd530", r"ed748b6e-ad21-11e0-83bb-b7fd7bebd530", r"edff65f4-ad21-11e0-8126-b7fd7bebd530", r"ee3dacf8-ad21-11e0-83ec-b7fd7bebd530", r"ee76f044-ad21-11e0-8170-b7fd7bebd530", r"ee93e582-ad21-11e0-8390-b7fd7bebd530", r"ef202a69-ad21-11e0-839b-b7fd7bebd530", r"ef3b4d52-ad21-11e0-8109-b7fd7bebd530", r"ef6067d8-ad21-11e0-8308-b7fd7bebd530", r"ef7b9575-ad21-11e0-81f1-b7fd7bebd530", r"ef9640eb-ad21-11e0-83ab-b7fd7bebd530", r"efb10934-ad21-11e0-8058-b7fd7bebd530", r"efce20a0-ad21-11e0-8012-b7fd7bebd530", r"efe96c20-ad21-11e0-833c-b7fd7bebd530", r"f00484d0-ad21-11e0-8357-b7fd7bebd530", r"f01f84d6-ad21-11e0-822a-b7fd7bebd530", r"f03a7463-ad21-11e0-830f-b7fd7bebd530", r"f056c254-ad21-11e0-8310-b7fd7bebd530", r"f169fb78-ad21-11e0-8276-b7fd7bebd530", r"f1e2bcde-ad21-11e0-800a-b7fd7bebd530", r"f202b779-ad21-11e0-8344-b7fd7bebd530", r"f2214239-ad21-11e0-82e2-b7fd7bebd530", r"f23de82a-ad21-11e0-803b-b7fd7bebd530", r"f25bce3b-ad21-11e0-8126-b7fd7bebd530", r"f2781703-ad21-11e0-8147-b7fd7bebd530", r"f2a5ad2a-ad21-11e0-8185-b7fd7bebd530", r"f2f168c9-ad21-11e0-803f-b7fd7bebd530", r"f3315154-ad21-11e0-8140-b7fd7bebd530", r"f3513e7f-ad21-11e0-83f7-b7fd7bebd530", r"f3515f5a-ad21-11e0-81da-b7fd7bebd530", r"fcdbc046-5e44-4d4d-b4ec-049d194c2458")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 9
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250728102636.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 9
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-07-21 16:42:19.224530"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/09"
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
    config_vars['SHORT_INDEX_CHECKSUM'] = r"c1905c156cf127692f0389bafcc218094b65fab9"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/09/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 15713
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250728102636.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-07-06 12:14:08.392126"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Q_Clone_Presets_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Effects_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_Data_Folders_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS_Models_Data_Folders_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"CR8_Sampler_Presets_IID", r"Center_IID", r"ChainersChildExcludeList_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_V16_1_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Enigma_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"Get_General_Icons_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LicenseNotifications_V16_1_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"ONNXRUNTIME_IID", r"ORS_Modulators_Data_IID", r"PAZ_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PresetBrowser_V16_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"SOC_Presets_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"SuperTap_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"WLM_IID", r"WLM_Plus_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_16_0_23_IID", r"WavesLib1_16_0_30_IID", r"WavesLib1_16_0_64_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V16_1_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-07-06 12:14:08.392126 bm-mac-ado9"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"ulgflclopokhkscn"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Effects_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-07-28 10:28:49.271864"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"bm-mac-ado9"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9", r"/Library/Application Support/Waves/Central/V16", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=1279):
    with Stage(r"begin", prog_num=1280):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1281):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1282) as copy_file_to_file_001_1282:
            copy_file_to_file_001_1282()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1283) as copy_file_to_file_002_1283:
            copy_file_to_file_002_1283()
    with Stage(r"sync", prog_num=1284):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1285) as shell_command_003_1285:
            shell_command_003_1285()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1286) as shell_command_004_1286:
            shell_command_004_1286()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=1287) as shell_command_005_1287:
            shell_command_005_1287()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1288) as shell_command_006_1288:
            shell_command_006_1288()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1289) as shell_command_007_1289:
            shell_command_007_1289()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1290) as shell_command_008_1290:
            shell_command_008_1290()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1291) as shell_command_009_1291:
            shell_command_009_1291()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1292) as shell_command_010_1292:
            shell_command_010_1292()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1293) as shell_command_011_1293:
            shell_command_011_1293()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=1294):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=1295) as make_dir_012_1295:
                make_dir_012_1295()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1296) as cd_013_1296:
                cd_013_1296()
                Progress(r"13498 files already in cache", own_progress_count=13498, prog_num=14794)()
                with Stage(r"post_sync", prog_num=14795):
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=14796) as copy_file_to_file_014_14796:
                        copy_file_to_file_014_14796()
            Progress(r"Done sync", prog_num=14797)()
    with Stage(r"copy", prog_num=14798):
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=14799) as run_in_thread_015_14799:
            run_in_thread_015_14799()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=14800)()
        with Stage(r"create folders", prog_num=14801):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=14802) as make_dir_016_14802:
                make_dir_016_14802()
            with MakeDir(r"/Applications/Waves/Applications V16", chowner=True, prog_num=14803) as make_dir_017_14803:
                make_dir_017_14803()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=14804) as make_dir_018_14804:
                make_dir_018_14804()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=14805) as make_dir_019_14805:
                make_dir_019_14805()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=14806) as make_dir_020_14806:
                make_dir_020_14806()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=14807) as make_dir_021_14807:
                make_dir_021_14807()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=14808) as make_dir_022_14808:
                make_dir_022_14808()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=14809) as make_dir_023_14809:
                make_dir_023_14809()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=14810) as make_dir_024_14810:
                make_dir_024_14810()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=14811) as make_dir_025_14811:
                make_dir_025_14811()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=14812) as make_dir_026_14812:
                make_dir_026_14812()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=14813) as make_dir_027_14813:
                make_dir_027_14813()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=14814) as make_dir_028_14814:
                make_dir_028_14814()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=14815) as make_dir_029_14815:
                make_dir_029_14815()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=14816) as make_dir_030_14816:
                make_dir_030_14816()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=14817) as make_dir_031_14817:
                make_dir_031_14817()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTR", chowner=True, prog_num=14818) as make_dir_032_14818:
                make_dir_032_14818()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=14819) as make_dir_033_14819:
                make_dir_033_14819()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=14820) as make_dir_034_14820:
                make_dir_034_14820()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=14821) as make_dir_035_14821:
                make_dir_035_14821()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=14822) as make_dir_036_14822:
                make_dir_036_14822()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=14823) as make_dir_037_14823:
                make_dir_037_14823()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=14824) as make_dir_038_14824:
                make_dir_038_14824()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=14825) as make_dir_039_14825:
                make_dir_039_14825()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=14826) as make_dir_040_14826:
                make_dir_040_14826()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=14827) as make_dir_041_14827:
                make_dir_041_14827()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=14828) as make_dir_042_14828:
                make_dir_042_14828()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=14829) as make_dir_043_14829:
                make_dir_043_14829()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=14830) as make_dir_044_14830:
                make_dir_044_14830()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=14831) as make_dir_045_14831:
                make_dir_045_14831()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=14832) as make_dir_046_14832:
                make_dir_046_14832()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=14833) as make_dir_047_14833:
                make_dir_047_14833()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=14834) as make_dir_048_14834:
                make_dir_048_14834()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=14835) as make_dir_049_14835:
                make_dir_049_14835()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=14836) as make_dir_050_14836:
                make_dir_050_14836()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=14837) as make_dir_051_14837:
                make_dir_051_14837()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=14838) as make_dir_052_14838:
                make_dir_052_14838()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=14839) as rm_file_or_dir_053_14839:
            rm_file_or_dir_053_14839()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=14840) as rm_file_or_dir_054_14840:
            rm_file_or_dir_054_14840()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=14841) as shell_command_055_14841:
            shell_command_055_14841()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=14842) as shell_command_056_14842:
            shell_command_056_14842()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=14843) as shell_command_057_14843:
            shell_command_057_14843()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=14844) as shell_command_058_14844:
            shell_command_058_14844()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=14845) as shell_command_059_14845:
            shell_command_059_14845()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=14846) as shell_command_060_14846:
            shell_command_060_14846()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=14847) as shell_command_061_14847:
            shell_command_061_14847()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=14848) as shell_command_062_14848:
            shell_command_062_14848()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=14849) as shell_command_063_14849:
            shell_command_063_14849()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=14850) as cd_stage_064_14850:
            cd_stage_064_14850()
            with SetExecPermissionsInSyncFolder(prog_num=14851) as set_exec_permissions_in_sync_folder_065_14851:
                set_exec_permissions_in_sync_folder_065_14851()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V16", prog_num=14852) as cd_stage_066_14852:
            cd_stage_066_14852()
            with Stage(r"copy", r"Bass Slapper application v16.0.23.24", prog_num=14853):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=14854) as should_copy_source_067_14854:
                    should_copy_source_067_14854()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=14855):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=14856) as copy_dir_to_dir_068_14856:
                            copy_dir_to_dir_068_14856()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=14857) as unwtar_069_14857:
                            unwtar_069_14857()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=14858, recursive=True) as chown_070_14858:
                            chown_070_14858()
            with Stage(r"copy", r"Electric Grand 80 application v16.0.23.24", prog_num=14859):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=14860) as should_copy_source_071_14860:
                    should_copy_source_071_14860()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=14861):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=14862) as copy_dir_to_dir_072_14862:
                            copy_dir_to_dir_072_14862()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=14863) as unwtar_073_14863:
                            unwtar_073_14863()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=14864, recursive=True) as chown_074_14864:
                            chown_074_14864()
            with Stage(r"copy", r"GTR application v16.0.23.24", prog_num=14865):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=14866) as should_copy_source_075_14866:
                    should_copy_source_075_14866()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=14867):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=14868) as copy_dir_to_dir_076_14868:
                            copy_dir_to_dir_076_14868()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=14869) as unwtar_077_14869:
                            unwtar_077_14869()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=14870, recursive=True) as chown_078_14870:
                            chown_078_14870()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V16" -c', ignore_all_errors=True, prog_num=14871) as shell_command_079_14871:
                shell_command_079_14871()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V16"/Icon?; fi', prog_num=14872) as script_command_080_14872:
                script_command_080_14872()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=14873) as cd_stage_081_14873:
            cd_stage_081_14873()
            with Stage(r"copy", r"COSMOS__Application v16.0.50.51", prog_num=14874):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=14875) as should_copy_source_082_14875:
                    should_copy_source_082_14875()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=14876):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=14877) as copy_dir_to_dir_083_14877:
                            copy_dir_to_dir_083_14877()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=14878) as unwtar_084_14878:
                            unwtar_084_14878()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=14879, recursive=True) as chown_085_14879:
                            chown_085_14879()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=14889) as resolve_symlink_files_in_folder_086_14889:
                resolve_symlink_files_in_folder_086_14889()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=14890) as cd_stage_087_14890:
            cd_stage_087_14890()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=14891):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14892) as should_copy_source_088_14892:
                    should_copy_source_088_14892()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=14893):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=14894) as copy_dir_to_dir_089_14894:
                            copy_dir_to_dir_089_14894()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=14895, recursive=True) as chown_090_14895:
                            chown_090_14895()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=14896):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=14897) as should_copy_source_091_14897:
                    should_copy_source_091_14897()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=14898):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=14899) as copy_dir_to_dir_092_14899:
                            copy_dir_to_dir_092_14899()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=14900) as unwtar_093_14900:
                            unwtar_093_14900()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=14901, recursive=True) as chown_094_14901:
                            chown_094_14901()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.1", prog_num=14902):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14903) as should_copy_source_095_14903:
                    should_copy_source_095_14903()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=14904):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=14905) as copy_dir_to_dir_096_14905:
                            copy_dir_to_dir_096_14905()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=14906, recursive=True) as chown_097_14906:
                            chown_097_14906()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=14907):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14908) as should_copy_source_098_14908:
                    should_copy_source_098_14908()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=14909):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=14910) as copy_dir_to_dir_099_14910:
                            copy_dir_to_dir_099_14910()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=14911, recursive=True) as chown_100_14911:
                            chown_100_14911()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=14912):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14913) as should_copy_source_101_14913:
                    should_copy_source_101_14913()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=14914):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=14915) as copy_dir_to_dir_102_14915:
                            copy_dir_to_dir_102_14915()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=14916, recursive=True) as chown_103_14916:
                            chown_103_14916()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=14917):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14918) as should_copy_source_104_14918:
                    should_copy_source_104_14918()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=14919):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=14920) as copy_dir_to_dir_105_14920:
                            copy_dir_to_dir_105_14920()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=14921, recursive=True) as chown_106_14921:
                            chown_106_14921()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=14922):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=14923) as should_copy_source_107_14923:
                    should_copy_source_107_14923()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=14924):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=14925) as copy_dir_to_dir_108_14925:
                            copy_dir_to_dir_108_14925()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=14926, recursive=True) as chown_109_14926:
                            chown_109_14926()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=14927):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=14928) as should_copy_source_110_14928:
                    should_copy_source_110_14928()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=14929):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=14930) as copy_dir_to_dir_111_14930:
                            copy_dir_to_dir_111_14930()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", where_to_unwtar=r".", prog_num=14931) as unwtar_112_14931:
                            unwtar_112_14931()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=14932, recursive=True) as chown_113_14932:
                            chown_113_14932()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=14933) as cd_stage_114_14933:
            cd_stage_114_14933()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=14934):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=14935) as should_copy_source_115_14935:
                    should_copy_source_115_14935()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=14936):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r".", prog_num=14937) as copy_file_to_dir_116_14937:
                            copy_file_to_dir_116_14937()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=14938) as chmod_and_chown_117_14938:
                            chmod_and_chown_117_14938()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=14939) as should_copy_source_118_14939:
                    should_copy_source_118_14939()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=14940):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=14941) as copy_dir_to_dir_119_14941:
                            copy_dir_to_dir_119_14941()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=14942) as unwtar_120_14942:
                            unwtar_120_14942()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=14943, recursive=True) as chown_121_14943:
                            chown_121_14943()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=14944) as cd_stage_122_14944:
            cd_stage_122_14944()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=14945):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=14946) as should_copy_source_123_14946:
                    should_copy_source_123_14946()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=14947):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=14948) as copy_dir_to_dir_124_14948:
                            copy_dir_to_dir_124_14948()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=14949, recursive=True) as chown_125_14949:
                            chown_125_14949()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=14950) as should_copy_source_126_14950:
                    should_copy_source_126_14950()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=14951):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=14952) as copy_dir_to_dir_127_14952:
                            copy_dir_to_dir_127_14952()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=14953, recursive=True) as chown_128_14953:
                            chown_128_14953()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=14954):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=14955) as should_copy_source_129_14955:
                    should_copy_source_129_14955()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=14956):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=14957) as copy_dir_to_dir_130_14957:
                            copy_dir_to_dir_130_14957()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=14958, recursive=True) as chown_131_14958:
                            chown_131_14958()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=14959) as should_copy_source_132_14959:
                    should_copy_source_132_14959()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=14960):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=14961) as copy_dir_to_dir_133_14961:
                            copy_dir_to_dir_133_14961()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=14962, recursive=True) as chown_134_14962:
                            chown_134_14962()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=14963) as cd_stage_135_14963:
            cd_stage_135_14963()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=14964):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=14965) as should_copy_source_136_14965:
                    should_copy_source_136_14965()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=14966):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=14967) as copy_file_to_dir_137_14967:
                            copy_file_to_dir_137_14967()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=14968) as chmod_and_chown_138_14968:
                            chmod_and_chown_138_14968()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=14969) as cd_stage_139_14969:
            cd_stage_139_14969()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=14970):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14971) as should_copy_source_140_14971:
                    should_copy_source_140_14971()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=14972):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=14973) as copy_dir_to_dir_141_14973:
                            copy_dir_to_dir_141_14973()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=14974, recursive=True) as chown_142_14974:
                            chown_142_14974()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=14975):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14976) as should_copy_source_143_14976:
                    should_copy_source_143_14976()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=14977):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=14978) as copy_dir_to_dir_144_14978:
                            copy_dir_to_dir_144_14978()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=14979, recursive=True) as chown_145_14979:
                            chown_145_14979()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=14980):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14981) as should_copy_source_146_14981:
                    should_copy_source_146_14981()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=14982):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=14983) as copy_dir_to_dir_147_14983:
                            copy_dir_to_dir_147_14983()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=14984, recursive=True) as chown_148_14984:
                            chown_148_14984()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=14985):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14986) as should_copy_source_149_14986:
                    should_copy_source_149_14986()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=14987):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=14988) as copy_dir_to_dir_150_14988:
                            copy_dir_to_dir_150_14988()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=14989, recursive=True) as chown_151_14989:
                            chown_151_14989()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=14990):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14991) as should_copy_source_152_14991:
                    should_copy_source_152_14991()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=14992):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=14993) as copy_dir_to_dir_153_14993:
                            copy_dir_to_dir_153_14993()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=14994, recursive=True) as chown_154_14994:
                            chown_154_14994()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=14995):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=14996) as should_copy_source_155_14996:
                    should_copy_source_155_14996()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=14997):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=14998) as copy_dir_to_dir_156_14998:
                            copy_dir_to_dir_156_14998()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=14999, recursive=True) as chown_157_14999:
                            chown_157_14999()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=15000):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15001) as should_copy_source_158_15001:
                    should_copy_source_158_15001()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=15002):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=15003) as copy_dir_to_dir_159_15003:
                            copy_dir_to_dir_159_15003()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=15004, recursive=True) as chown_160_15004:
                            chown_160_15004()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=15005):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15006) as should_copy_source_161_15006:
                    should_copy_source_161_15006()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=15007):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=15008) as copy_dir_to_dir_162_15008:
                            copy_dir_to_dir_162_15008()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=15009, recursive=True) as chown_163_15009:
                            chown_163_15009()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=15010):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15011) as should_copy_source_164_15011:
                    should_copy_source_164_15011()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=15012):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=15013) as copy_dir_to_dir_165_15013:
                            copy_dir_to_dir_165_15013()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=15014, recursive=True) as chown_166_15014:
                            chown_166_15014()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=15015):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15016) as should_copy_source_167_15016:
                    should_copy_source_167_15016()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=15017):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=15018) as copy_dir_to_dir_168_15018:
                            copy_dir_to_dir_168_15018()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=15019, recursive=True) as chown_169_15019:
                            chown_169_15019()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=15020):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15021) as should_copy_source_170_15021:
                    should_copy_source_170_15021()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=15022):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=15023) as copy_dir_to_dir_171_15023:
                            copy_dir_to_dir_171_15023()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=15024, recursive=True) as chown_172_15024:
                            chown_172_15024()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=15025):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15026) as should_copy_source_173_15026:
                    should_copy_source_173_15026()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=15027):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=15028) as copy_dir_to_dir_174_15028:
                            copy_dir_to_dir_174_15028()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=15029, recursive=True) as chown_175_15029:
                            chown_175_15029()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=15030):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15031) as should_copy_source_176_15031:
                    should_copy_source_176_15031()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=15032):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=15033) as copy_dir_to_dir_177_15033:
                            copy_dir_to_dir_177_15033()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=15034, recursive=True) as chown_178_15034:
                            chown_178_15034()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=15035):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15036) as should_copy_source_179_15036:
                    should_copy_source_179_15036()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=15037):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=15038) as copy_dir_to_dir_180_15038:
                            copy_dir_to_dir_180_15038()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=15039, recursive=True) as chown_181_15039:
                            chown_181_15039()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=15040):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15041) as should_copy_source_182_15041:
                    should_copy_source_182_15041()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=15042):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=15043) as copy_dir_to_dir_183_15043:
                            copy_dir_to_dir_183_15043()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=15044, recursive=True) as chown_184_15044:
                            chown_184_15044()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=15045):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15046) as should_copy_source_185_15046:
                    should_copy_source_185_15046()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=15047):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=15048) as copy_dir_to_dir_186_15048:
                            copy_dir_to_dir_186_15048()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=15049, recursive=True) as chown_187_15049:
                            chown_187_15049()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=15050):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15051) as should_copy_source_188_15051:
                    should_copy_source_188_15051()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=15052):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=15053) as copy_dir_to_dir_189_15053:
                            copy_dir_to_dir_189_15053()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=15054, recursive=True) as chown_190_15054:
                            chown_190_15054()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=15055):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15056) as should_copy_source_191_15056:
                    should_copy_source_191_15056()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=15057):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=15058) as copy_dir_to_dir_192_15058:
                            copy_dir_to_dir_192_15058()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=15059, recursive=True) as chown_193_15059:
                            chown_193_15059()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=15060):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15061) as should_copy_source_194_15061:
                    should_copy_source_194_15061()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=15062):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=15063) as copy_dir_to_dir_195_15063:
                            copy_dir_to_dir_195_15063()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=15064, recursive=True) as chown_196_15064:
                            chown_196_15064()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=15065):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=15066) as should_copy_source_197_15066:
                    should_copy_source_197_15066()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=15067):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=15068) as copy_dir_to_dir_198_15068:
                            copy_dir_to_dir_198_15068()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=15069, recursive=True) as chown_199_15069:
                            chown_199_15069()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=15070) as cd_stage_200_15070:
            cd_stage_200_15070()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=15071):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15072) as should_copy_source_201_15072:
                    should_copy_source_201_15072()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=15073):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=15074) as copy_dir_to_dir_202_15074:
                            copy_dir_to_dir_202_15074()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=15075, recursive=True) as chown_203_15075:
                            chown_203_15075()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=15076):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15077) as should_copy_source_204_15077:
                    should_copy_source_204_15077()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=15078):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=15079) as copy_dir_to_dir_205_15079:
                            copy_dir_to_dir_205_15079()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=15080, recursive=True) as chown_206_15080:
                            chown_206_15080()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=15081):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15082) as should_copy_source_207_15082:
                    should_copy_source_207_15082()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=15083):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=15084) as copy_dir_to_dir_208_15084:
                            copy_dir_to_dir_208_15084()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=15085, recursive=True) as chown_209_15085:
                            chown_209_15085()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=15086):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15087) as should_copy_source_210_15087:
                    should_copy_source_210_15087()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=15088):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=15089) as copy_dir_to_dir_211_15089:
                            copy_dir_to_dir_211_15089()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=15090, recursive=True) as chown_212_15090:
                            chown_212_15090()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=15091):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15092) as should_copy_source_213_15092:
                    should_copy_source_213_15092()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=15093):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=15094) as copy_dir_to_dir_214_15094:
                            copy_dir_to_dir_214_15094()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=15095, recursive=True) as chown_215_15095:
                            chown_215_15095()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=15096):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15097) as should_copy_source_216_15097:
                    should_copy_source_216_15097()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=15098):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=15099) as copy_dir_to_dir_217_15099:
                            copy_dir_to_dir_217_15099()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=15100, recursive=True) as chown_218_15100:
                            chown_218_15100()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=15101):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=15102) as should_copy_source_219_15102:
                    should_copy_source_219_15102()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=15103):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=15104) as copy_dir_to_dir_220_15104:
                            copy_dir_to_dir_220_15104()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=15105, recursive=True) as chown_221_15105:
                            chown_221_15105()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=15106) as cd_stage_222_15106:
            cd_stage_222_15106()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=15107):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=15108) as should_copy_source_223_15108:
                    should_copy_source_223_15108()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=15109):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=15110) as copy_dir_to_dir_224_15110:
                            copy_dir_to_dir_224_15110()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=15111, recursive=True) as chown_225_15111:
                            chown_225_15111()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=15112):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=15113) as should_copy_source_226_15113:
                    should_copy_source_226_15113()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=15114):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=15115) as copy_dir_to_dir_227_15115:
                            copy_dir_to_dir_227_15115()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=15116, recursive=True) as chown_228_15116:
                            chown_228_15116()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=15117) as cd_stage_229_15117:
            cd_stage_229_15117()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=15118):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=15119) as should_copy_source_230_15119:
                    should_copy_source_230_15119()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=15120):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=15121) as unwtar_231_15121:
                            unwtar_231_15121()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=15122) as should_copy_source_232_15122:
                    should_copy_source_232_15122()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=15123):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=15124) as unwtar_233_15124:
                            unwtar_233_15124()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=15125) as cd_stage_234_15125:
            cd_stage_234_15125()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=15126):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=15127) as should_copy_source_235_15127:
                    should_copy_source_235_15127()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=15128):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=15129) as unwtar_236_15129:
                            unwtar_236_15129()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=15130) as cd_stage_237_15130:
            cd_stage_237_15130()
            with Stage(r"copy", r"ARPlates v16.0.23.24", prog_num=15131):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15132) as should_copy_source_238_15132:
                    should_copy_source_238_15132()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=15133):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=15134) as copy_dir_to_dir_239_15134:
                            copy_dir_to_dir_239_15134()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=15135) as unwtar_240_15135:
                            unwtar_240_15135()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=15136, recursive=True) as chown_241_15136:
                            chown_241_15136()
            with Stage(r"copy", r"Abbey Road Vinyl v16.0.23.24", prog_num=15137):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15138) as should_copy_source_242_15138:
                    should_copy_source_242_15138()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=15139):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=15140) as copy_dir_to_dir_243_15140:
                            copy_dir_to_dir_243_15140()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=15141) as unwtar_244_15141:
                            unwtar_244_15141()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=15142, recursive=True) as chown_245_15142:
                            chown_245_15142()
            with Stage(r"copy", r"Aphex AX v16.0.23.24", prog_num=15143):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15144) as should_copy_source_246_15144:
                    should_copy_source_246_15144()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=15145):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=15146) as copy_dir_to_dir_247_15146:
                            copy_dir_to_dir_247_15146()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=15147) as unwtar_248_15147:
                            unwtar_248_15147()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=15148, recursive=True) as chown_249_15148:
                            chown_249_15148()
            with Stage(r"copy", r"AudioTrack v16.0.23.24", prog_num=15149):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15150) as should_copy_source_250_15150:
                    should_copy_source_250_15150()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=15151):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=15152) as copy_dir_to_dir_251_15152:
                            copy_dir_to_dir_251_15152()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=15153) as unwtar_252_15153:
                            unwtar_252_15153()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=15154, recursive=True) as chown_253_15154:
                            chown_253_15154()
            with Stage(r"copy", r"Bass Rider v16.0.23.24", prog_num=15155):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15156) as should_copy_source_254_15156:
                    should_copy_source_254_15156()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=15157):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=15158) as copy_dir_to_dir_255_15158:
                            copy_dir_to_dir_255_15158()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=15159) as unwtar_256_15159:
                            unwtar_256_15159()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=15160, recursive=True) as chown_257_15160:
                            chown_257_15160()
            with Stage(r"copy", r"Bass Slapper v16.0.23.24", prog_num=15161):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15162) as should_copy_source_258_15162:
                    should_copy_source_258_15162()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=15163):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=15164) as copy_dir_to_dir_259_15164:
                            copy_dir_to_dir_259_15164()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=15165) as unwtar_260_15165:
                            unwtar_260_15165()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=15166, recursive=True) as chown_261_15166:
                            chown_261_15166()
            with Stage(r"copy", r"Brauer Motion v16.0.23.24", prog_num=15167):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15168) as should_copy_source_262_15168:
                    should_copy_source_262_15168()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=15169):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=15170) as copy_dir_to_dir_263_15170:
                            copy_dir_to_dir_263_15170()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=15171) as unwtar_264_15171:
                            unwtar_264_15171()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=15172, recursive=True) as chown_265_15172:
                            chown_265_15172()
            with Stage(r"copy", r"Butch Vig Vocals v16.0.23.24", prog_num=15173):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15174) as should_copy_source_266_15174:
                    should_copy_source_266_15174()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=15175):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=15176) as copy_dir_to_dir_267_15176:
                            copy_dir_to_dir_267_15176()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=15177) as unwtar_268_15177:
                            unwtar_268_15177()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=15178, recursive=True) as chown_269_15178:
                            chown_269_15178()
            with Stage(r"copy", r"C1 v16.0.23.24", prog_num=15179):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15180) as should_copy_source_270_15180:
                    should_copy_source_270_15180()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=15181):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=15182) as copy_dir_to_dir_271_15182:
                            copy_dir_to_dir_271_15182()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=15183) as unwtar_272_15183:
                            unwtar_272_15183()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C1.bundle", user_id=-1, group_id=-1, prog_num=15184, recursive=True) as chown_273_15184:
                            chown_273_15184()
            with Stage(r"copy", r"C4 v16.0.23.24", prog_num=15185):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15186) as should_copy_source_274_15186:
                    should_copy_source_274_15186()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=15187):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=15188) as copy_dir_to_dir_275_15188:
                            copy_dir_to_dir_275_15188()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=15189) as unwtar_276_15189:
                            unwtar_276_15189()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C4.bundle", user_id=-1, group_id=-1, prog_num=15190, recursive=True) as chown_277_15190:
                            chown_277_15190()
            with Stage(r"copy", r"CLA-2A v16.0.23.24", prog_num=15191):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15192) as should_copy_source_278_15192:
                    should_copy_source_278_15192()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=15193):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=15194) as copy_dir_to_dir_279_15194:
                            copy_dir_to_dir_279_15194()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=15195) as unwtar_280_15195:
                            unwtar_280_15195()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=15196, recursive=True) as chown_281_15196:
                            chown_281_15196()
            with Stage(r"copy", r"CLA-3A v16.0.23.24", prog_num=15197):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15198) as should_copy_source_282_15198:
                    should_copy_source_282_15198()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=15199):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=15200) as copy_dir_to_dir_283_15200:
                            copy_dir_to_dir_283_15200()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=15201) as unwtar_284_15201:
                            unwtar_284_15201()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=15202, recursive=True) as chown_285_15202:
                            chown_285_15202()
            with Stage(r"copy", r"CLA-76 v16.0.23.24", prog_num=15203):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15204) as should_copy_source_286_15204:
                    should_copy_source_286_15204()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=15205):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=15206) as copy_dir_to_dir_287_15206:
                            copy_dir_to_dir_287_15206()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=15207) as unwtar_288_15207:
                            unwtar_288_15207()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=15208, recursive=True) as chown_289_15208:
                            chown_289_15208()
            with Stage(r"copy", r"CLA Bass v16.0.23.24", prog_num=15209):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15210) as should_copy_source_290_15210:
                    should_copy_source_290_15210()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=15211):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=15212) as copy_dir_to_dir_291_15212:
                            copy_dir_to_dir_291_15212()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=15213) as unwtar_292_15213:
                            unwtar_292_15213()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=15214, recursive=True) as chown_293_15214:
                            chown_293_15214()
            with Stage(r"copy", r"CLA Drums v16.0.23.24", prog_num=15215):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15216) as should_copy_source_294_15216:
                    should_copy_source_294_15216()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Drums.bundle", prog_num=15217):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r".", delete_extraneous_files=True, prog_num=15218) as copy_dir_to_dir_295_15218:
                            copy_dir_to_dir_295_15218()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", where_to_unwtar=r".", prog_num=15219) as unwtar_296_15219:
                            unwtar_296_15219()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Drums.bundle", user_id=-1, group_id=-1, prog_num=15220, recursive=True) as chown_297_15220:
                            chown_297_15220()
            with Stage(r"copy", r"CLA Effects v16.0.23.24", prog_num=15221):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15222) as should_copy_source_298_15222:
                    should_copy_source_298_15222()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Effects.bundle", prog_num=15223):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r".", delete_extraneous_files=True, prog_num=15224) as copy_dir_to_dir_299_15224:
                            copy_dir_to_dir_299_15224()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", where_to_unwtar=r".", prog_num=15225) as unwtar_300_15225:
                            unwtar_300_15225()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Effects.bundle", user_id=-1, group_id=-1, prog_num=15226, recursive=True) as chown_301_15226:
                            chown_301_15226()
            with Stage(r"copy", r"CLA Guitars v16.0.23.24", prog_num=15227):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15228) as should_copy_source_302_15228:
                    should_copy_source_302_15228()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=15229):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=15230) as copy_dir_to_dir_303_15230:
                            copy_dir_to_dir_303_15230()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=15231) as unwtar_304_15231:
                            unwtar_304_15231()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=15232, recursive=True) as chown_305_15232:
                            chown_305_15232()
            with Stage(r"copy", r"CLA Unplugged v16.0.23.24", prog_num=15233):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15234) as should_copy_source_306_15234:
                    should_copy_source_306_15234()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=15235):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=15236) as copy_dir_to_dir_307_15236:
                            copy_dir_to_dir_307_15236()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=15237) as unwtar_308_15237:
                            unwtar_308_15237()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=15238, recursive=True) as chown_309_15238:
                            chown_309_15238()
            with Stage(r"copy", r"CLA Vocals v16.0.23.24", prog_num=15239):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15240) as should_copy_source_310_15240:
                    should_copy_source_310_15240()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=15241):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=15242) as copy_dir_to_dir_311_15242:
                            copy_dir_to_dir_311_15242()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=15243) as unwtar_312_15243:
                            unwtar_312_15243()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=15244, recursive=True) as chown_313_15244:
                            chown_313_15244()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=15245):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15246) as should_copy_source_314_15246:
                    should_copy_source_314_15246()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=15247):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=15248) as copy_dir_to_dir_315_15248:
                            copy_dir_to_dir_315_15248()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=15249) as unwtar_316_15249:
                            unwtar_316_15249()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=15250, recursive=True) as chown_317_15250:
                            chown_317_15250()
            with Stage(r"copy", r"Center v16.0.23.24", prog_num=15251):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15252) as should_copy_source_318_15252:
                    should_copy_source_318_15252()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=15253):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=15254) as copy_dir_to_dir_319_15254:
                            copy_dir_to_dir_319_15254()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=15255) as unwtar_320_15255:
                            unwtar_320_15255()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Center.bundle", user_id=-1, group_id=-1, prog_num=15256, recursive=True) as chown_321_15256:
                            chown_321_15256()
            with Stage(r"copy", r"Clarity Vx v16.0.23.24", prog_num=15257):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15258) as should_copy_source_322_15258:
                    should_copy_source_322_15258()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=15259):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=15260) as copy_dir_to_dir_323_15260:
                            copy_dir_to_dir_323_15260()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=15261) as unwtar_324_15261:
                            unwtar_324_15261()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=15262, recursive=True) as chown_325_15262:
                            chown_325_15262()
            with Stage(r"copy", r"Saphira v16.0.23.24", prog_num=15263):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15264) as should_copy_source_326_15264:
                    should_copy_source_326_15264()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=15265):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=15266) as copy_dir_to_dir_327_15266:
                            copy_dir_to_dir_327_15266()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=15267) as unwtar_328_15267:
                            unwtar_328_15267()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Saphira.bundle", user_id=-1, group_id=-1, prog_num=15268, recursive=True) as chown_329_15268:
                            chown_329_15268()
            with Stage(r"copy", r"Submarine v16.0.23.24", prog_num=15269):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15270) as should_copy_source_330_15270:
                    should_copy_source_330_15270()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=15271):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=15272) as copy_dir_to_dir_331_15272:
                            copy_dir_to_dir_331_15272()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=15273) as unwtar_332_15273:
                            unwtar_332_15273()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Submarine.bundle", user_id=-1, group_id=-1, prog_num=15274, recursive=True) as chown_333_15274:
                            chown_333_15274()
            with Stage(r"copy", r"DeBreath v16.0.23.24", prog_num=15275):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15276) as should_copy_source_334_15276:
                    should_copy_source_334_15276()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=15277):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=15278) as copy_dir_to_dir_335_15278:
                            copy_dir_to_dir_335_15278()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=15279) as unwtar_336_15279:
                            unwtar_336_15279()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=15280, recursive=True) as chown_337_15280:
                            chown_337_15280()
            with Stage(r"copy", r"DeEsser v16.0.23.24", prog_num=15281):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15282) as should_copy_source_338_15282:
                    should_copy_source_338_15282()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=15283):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=15284) as copy_dir_to_dir_339_15284:
                            copy_dir_to_dir_339_15284()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=15285) as unwtar_340_15285:
                            unwtar_340_15285()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=15286, recursive=True) as chown_341_15286:
                            chown_341_15286()
            with Stage(r"copy", r"Doppler v16.0.23.24", prog_num=15287):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15288) as should_copy_source_342_15288:
                    should_copy_source_342_15288()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=15289):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=15290) as copy_dir_to_dir_343_15290:
                            copy_dir_to_dir_343_15290()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=15291) as unwtar_344_15291:
                            unwtar_344_15291()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doppler.bundle", user_id=-1, group_id=-1, prog_num=15292, recursive=True) as chown_345_15292:
                            chown_345_15292()
            with Stage(r"copy", r"Doubler v16.0.23.24", prog_num=15293):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15294) as should_copy_source_346_15294:
                    should_copy_source_346_15294()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=15295):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=15296) as copy_dir_to_dir_347_15296:
                            copy_dir_to_dir_347_15296()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=15297) as unwtar_348_15297:
                            unwtar_348_15297()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doubler.bundle", user_id=-1, group_id=-1, prog_num=15298, recursive=True) as chown_349_15298:
                            chown_349_15298()
            with Stage(r"copy", r"EMO-F2 v16.0.23.24", prog_num=15299):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15300) as should_copy_source_350_15300:
                    should_copy_source_350_15300()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=15301):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=15302) as copy_dir_to_dir_351_15302:
                            copy_dir_to_dir_351_15302()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=15303) as unwtar_352_15303:
                            unwtar_352_15303()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=15304, recursive=True) as chown_353_15304:
                            chown_353_15304()
            with Stage(r"copy", r"EMO-Q4 v16.0.23.24", prog_num=15305):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15306) as should_copy_source_354_15306:
                    should_copy_source_354_15306()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=15307):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=15308) as copy_dir_to_dir_355_15308:
                            copy_dir_to_dir_355_15308()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=15309) as unwtar_356_15309:
                            unwtar_356_15309()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=15310, recursive=True) as chown_357_15310:
                            chown_357_15310()
            with Stage(r"copy", r"EddieKramer DR v16.0.23.24", prog_num=15311):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15312) as should_copy_source_358_15312:
                    should_copy_source_358_15312()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=15313):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=15314) as copy_dir_to_dir_359_15314:
                            copy_dir_to_dir_359_15314()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=15315) as unwtar_360_15315:
                            unwtar_360_15315()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=15316, recursive=True) as chown_361_15316:
                            chown_361_15316()
            with Stage(r"copy", r"EddieKramer VC v16.0.23.24", prog_num=15317):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15318) as should_copy_source_362_15318:
                    should_copy_source_362_15318()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=15319):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=15320) as copy_dir_to_dir_363_15320:
                            copy_dir_to_dir_363_15320()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=15321) as unwtar_364_15321:
                            unwtar_364_15321()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=15322, recursive=True) as chown_365_15322:
                            chown_365_15322()
            with Stage(r"copy", r"Electric Grand 80 v16.0.23.24", prog_num=15323):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15324) as should_copy_source_366_15324:
                    should_copy_source_366_15324()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=15325):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=15326) as copy_dir_to_dir_367_15326:
                            copy_dir_to_dir_367_15326()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=15327) as unwtar_368_15327:
                            unwtar_368_15327()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=15328, recursive=True) as chown_369_15328:
                            chown_369_15328()
            with Stage(r"copy", r"Enigma v16.0.23.24", prog_num=15329):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15330) as should_copy_source_370_15330:
                    should_copy_source_370_15330()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=15331):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=15332) as copy_dir_to_dir_371_15332:
                            copy_dir_to_dir_371_15332()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=15333) as unwtar_372_15333:
                            unwtar_372_15333()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Enigma.bundle", user_id=-1, group_id=-1, prog_num=15334, recursive=True) as chown_373_15334:
                            chown_373_15334()
            with Stage(r"copy", r"GTRAmp v16.0.23.24", prog_num=15335):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15336) as should_copy_source_374_15336:
                    should_copy_source_374_15336()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=15337):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=15338) as copy_dir_to_dir_375_15338:
                            copy_dir_to_dir_375_15338()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=15339) as unwtar_376_15339:
                            unwtar_376_15339()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=15340, recursive=True) as chown_377_15340:
                            chown_377_15340()
            with Stage(r"copy", r"GTRStomp v16.0.23.24", prog_num=15341):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15342) as should_copy_source_378_15342:
                    should_copy_source_378_15342()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=15343):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=15344) as copy_dir_to_dir_379_15344:
                            copy_dir_to_dir_379_15344()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=15345) as unwtar_380_15345:
                            unwtar_380_15345()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=15346, recursive=True) as chown_381_15346:
                            chown_381_15346()
            with Stage(r"copy", r"GTRToolRack v16.0.23.24", prog_num=15347):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15348) as should_copy_source_382_15348:
                    should_copy_source_382_15348()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=15349):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=15350) as copy_dir_to_dir_383_15350:
                            copy_dir_to_dir_383_15350()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=15351) as unwtar_384_15351:
                            unwtar_384_15351()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=15352, recursive=True) as chown_385_15352:
                            chown_385_15352()
            with Stage(r"copy", r"GTRTuner v16.0.23.24", prog_num=15353):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15354) as should_copy_source_386_15354:
                    should_copy_source_386_15354()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=15355):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=15356) as copy_dir_to_dir_387_15356:
                            copy_dir_to_dir_387_15356()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=15357) as unwtar_388_15357:
                            unwtar_388_15357()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=15358, recursive=True) as chown_389_15358:
                            chown_389_15358()
            with Stage(r"copy", r"Greg Wells MixCentric v16.0.23.24", prog_num=15359):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15360) as should_copy_source_390_15360:
                    should_copy_source_390_15360()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=15361):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=15362) as copy_dir_to_dir_391_15362:
                            copy_dir_to_dir_391_15362()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=15363) as unwtar_392_15363:
                            unwtar_392_15363()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=15364, recursive=True) as chown_393_15364:
                            chown_393_15364()
            with Stage(r"copy", r"Greg Wells PianoCentric v16.0.23.24", prog_num=15365):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15366) as should_copy_source_394_15366:
                    should_copy_source_394_15366()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=15367):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=15368) as copy_dir_to_dir_395_15368:
                            copy_dir_to_dir_395_15368()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=15369) as unwtar_396_15369:
                            unwtar_396_15369()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=15370, recursive=True) as chown_397_15370:
                            chown_397_15370()
            with Stage(r"copy", r"Greg Wells ToneCentric v16.0.23.24", prog_num=15371):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15372) as should_copy_source_398_15372:
                    should_copy_source_398_15372()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=15373):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=15374) as copy_dir_to_dir_399_15374:
                            copy_dir_to_dir_399_15374()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=15375) as unwtar_400_15375:
                            unwtar_400_15375()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=15376, recursive=True) as chown_401_15376:
                            chown_401_15376()
            with Stage(r"copy", r"H-Comp v16.0.23.24", prog_num=15377):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15378) as should_copy_source_402_15378:
                    should_copy_source_402_15378()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=15379):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=15380) as copy_dir_to_dir_403_15380:
                            copy_dir_to_dir_403_15380()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=15381) as unwtar_404_15381:
                            unwtar_404_15381()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=15382, recursive=True) as chown_405_15382:
                            chown_405_15382()
            with Stage(r"copy", r"H-Delay v16.0.23.24", prog_num=15383):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15384) as should_copy_source_406_15384:
                    should_copy_source_406_15384()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=15385):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=15386) as copy_dir_to_dir_407_15386:
                            copy_dir_to_dir_407_15386()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=15387) as unwtar_408_15387:
                            unwtar_408_15387()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=15388, recursive=True) as chown_409_15388:
                            chown_409_15388()
            with Stage(r"copy", r"H-Reverb v16.0.23.24", prog_num=15389):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15390) as should_copy_source_410_15390:
                    should_copy_source_410_15390()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=15391):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=15392) as copy_dir_to_dir_411_15392:
                            copy_dir_to_dir_411_15392()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=15393) as unwtar_412_15393:
                            unwtar_412_15393()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=15394, recursive=True) as chown_413_15394:
                            chown_413_15394()
            with Stage(r"copy", r"IR-L v16.0.23.24", prog_num=15395):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15396) as should_copy_source_414_15396:
                    should_copy_source_414_15396()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=15397):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=15398) as copy_dir_to_dir_415_15398:
                            copy_dir_to_dir_415_15398()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=15399) as unwtar_416_15399:
                            unwtar_416_15399()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-L.bundle", user_id=-1, group_id=-1, prog_num=15400, recursive=True) as chown_417_15400:
                            chown_417_15400()
            with Stage(r"copy", r"InPhase v16.0.23.24", prog_num=15401):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15402) as should_copy_source_418_15402:
                    should_copy_source_418_15402()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=15403):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=15404) as copy_dir_to_dir_419_15404:
                            copy_dir_to_dir_419_15404()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=15405) as unwtar_420_15405:
                            unwtar_420_15405()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase.bundle", user_id=-1, group_id=-1, prog_num=15406, recursive=True) as chown_421_15406:
                            chown_421_15406()
            with Stage(r"copy", r"InPhase LT v16.0.23.24", prog_num=15407):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15408) as should_copy_source_422_15408:
                    should_copy_source_422_15408()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=15409):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=15410) as copy_dir_to_dir_423_15410:
                            copy_dir_to_dir_423_15410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=15411) as unwtar_424_15411:
                            unwtar_424_15411()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=15412, recursive=True) as chown_425_15412:
                            chown_425_15412()
            with Stage(r"copy", r"J37 v16.0.23.24", prog_num=15413):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15414) as should_copy_source_426_15414:
                    should_copy_source_426_15414()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=15415):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=15416) as copy_dir_to_dir_427_15416:
                            copy_dir_to_dir_427_15416()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=15417) as unwtar_428_15417:
                            unwtar_428_15417()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/J37.bundle", user_id=-1, group_id=-1, prog_num=15418, recursive=True) as chown_429_15418:
                            chown_429_15418()
            with Stage(r"copy", r"JJP-Vocals v16.0.23.24", prog_num=15419):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15420) as should_copy_source_430_15420:
                    should_copy_source_430_15420()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=15421):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=15422) as copy_dir_to_dir_431_15422:
                            copy_dir_to_dir_431_15422()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=15423) as unwtar_432_15423:
                            unwtar_432_15423()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=15424, recursive=True) as chown_433_15424:
                            chown_433_15424()
            with Stage(r"copy", r"Key Detector v16.0.23.24", prog_num=15425):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15426) as should_copy_source_434_15426:
                    should_copy_source_434_15426()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=15427):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=15428) as copy_dir_to_dir_435_15428:
                            copy_dir_to_dir_435_15428()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=15429) as unwtar_436_15429:
                            unwtar_436_15429()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=15430, recursive=True) as chown_437_15430:
                            chown_437_15430()
            with Stage(r"copy", r"KingsMic v16.0.23.24", prog_num=15431):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15432) as should_copy_source_438_15432:
                    should_copy_source_438_15432()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=15433):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=15434) as copy_dir_to_dir_439_15434:
                            copy_dir_to_dir_439_15434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=15435) as unwtar_440_15435:
                            unwtar_440_15435()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=15436, recursive=True) as chown_441_15436:
                            chown_441_15436()
            with Stage(r"copy", r"KramerHLS v16.0.23.24", prog_num=15437):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15438) as should_copy_source_442_15438:
                    should_copy_source_442_15438()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=15439):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=15440) as copy_dir_to_dir_443_15440:
                            copy_dir_to_dir_443_15440()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=15441) as unwtar_444_15441:
                            unwtar_444_15441()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=15442, recursive=True) as chown_445_15442:
                            chown_445_15442()
            with Stage(r"copy", r"KramerPIE v16.0.23.24", prog_num=15443):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15444) as should_copy_source_446_15444:
                    should_copy_source_446_15444()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=15445):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=15446) as copy_dir_to_dir_447_15446:
                            copy_dir_to_dir_447_15446()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=15447) as unwtar_448_15447:
                            unwtar_448_15447()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=15448, recursive=True) as chown_449_15448:
                            chown_449_15448()
            with Stage(r"copy", r"KramerTape v16.0.23.24", prog_num=15449):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15450) as should_copy_source_450_15450:
                    should_copy_source_450_15450()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=15451):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=15452) as copy_dir_to_dir_451_15452:
                            copy_dir_to_dir_451_15452()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=15453) as unwtar_452_15453:
                            unwtar_452_15453()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=15454, recursive=True) as chown_453_15454:
                            chown_453_15454()
            with Stage(r"copy", r"L1 v16.0.23.24", prog_num=15455):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15456) as should_copy_source_454_15456:
                    should_copy_source_454_15456()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=15457):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=15458) as copy_dir_to_dir_455_15458:
                            copy_dir_to_dir_455_15458()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=15459) as unwtar_456_15459:
                            unwtar_456_15459()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L1.bundle", user_id=-1, group_id=-1, prog_num=15460, recursive=True) as chown_457_15460:
                            chown_457_15460()
            with Stage(r"copy", r"L2 v16.0.23.24", prog_num=15461):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15462) as should_copy_source_458_15462:
                    should_copy_source_458_15462()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=15463):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=15464) as copy_dir_to_dir_459_15464:
                            copy_dir_to_dir_459_15464()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=15465) as unwtar_460_15465:
                            unwtar_460_15465()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L2.bundle", user_id=-1, group_id=-1, prog_num=15466, recursive=True) as chown_461_15466:
                            chown_461_15466()
            with Stage(r"copy", r"L3-16 v16.0.23.24", prog_num=15467):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15468) as should_copy_source_462_15468:
                    should_copy_source_462_15468()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=15469):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=15470) as copy_dir_to_dir_463_15470:
                            copy_dir_to_dir_463_15470()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=15471) as unwtar_464_15471:
                            unwtar_464_15471()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-16.bundle", user_id=-1, group_id=-1, prog_num=15472, recursive=True) as chown_465_15472:
                            chown_465_15472()
            with Stage(r"copy", r"L3-LL Multi v16.0.23.24", prog_num=15473):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15474) as should_copy_source_466_15474:
                    should_copy_source_466_15474()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=15475):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=15476) as copy_dir_to_dir_467_15476:
                            copy_dir_to_dir_467_15476()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=15477) as unwtar_468_15477:
                            unwtar_468_15477()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=15478, recursive=True) as chown_469_15478:
                            chown_469_15478()
            with Stage(r"copy", r"L3-LL Ultra v16.0.23.24", prog_num=15479):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15480) as should_copy_source_470_15480:
                    should_copy_source_470_15480()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=15481):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=15482) as copy_dir_to_dir_471_15482:
                            copy_dir_to_dir_471_15482()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=15483) as unwtar_472_15483:
                            unwtar_472_15483()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=15484, recursive=True) as chown_473_15484:
                            chown_473_15484()
            with Stage(r"copy", r"L3 Multi v16.0.23.24", prog_num=15485):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15486) as should_copy_source_474_15486:
                    should_copy_source_474_15486()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=15487):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=15488) as copy_dir_to_dir_475_15488:
                            copy_dir_to_dir_475_15488()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=15489) as unwtar_476_15489:
                            unwtar_476_15489()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=15490, recursive=True) as chown_477_15490:
                            chown_477_15490()
            with Stage(r"copy", r"L3 Ultra v16.0.23.24", prog_num=15491):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15492) as should_copy_source_478_15492:
                    should_copy_source_478_15492()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=15493):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=15494) as copy_dir_to_dir_479_15494:
                            copy_dir_to_dir_479_15494()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=15495) as unwtar_480_15495:
                            unwtar_480_15495()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=15496, recursive=True) as chown_481_15496:
                            chown_481_15496()
            with Stage(r"copy", r"LinEQ v16.0.23.24", prog_num=15497):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15498) as should_copy_source_482_15498:
                    should_copy_source_482_15498()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=15499):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=15500) as copy_dir_to_dir_483_15500:
                            copy_dir_to_dir_483_15500()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=15501) as unwtar_484_15501:
                            unwtar_484_15501()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=15502, recursive=True) as chown_485_15502:
                            chown_485_15502()
            with Stage(r"copy", r"LinMB v16.0.23.24", prog_num=15503):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15504) as should_copy_source_486_15504:
                    should_copy_source_486_15504()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=15505):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=15506) as copy_dir_to_dir_487_15506:
                            copy_dir_to_dir_487_15506()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=15507) as unwtar_488_15507:
                            unwtar_488_15507()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinMB.bundle", user_id=-1, group_id=-1, prog_num=15508, recursive=True) as chown_489_15508:
                            chown_489_15508()
            with Stage(r"copy", r"LoAir v16.0.23.24", prog_num=15509):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15510) as should_copy_source_490_15510:
                    should_copy_source_490_15510()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=15511):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=15512) as copy_dir_to_dir_491_15512:
                            copy_dir_to_dir_491_15512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=15513) as unwtar_492_15513:
                            unwtar_492_15513()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LoAir.bundle", user_id=-1, group_id=-1, prog_num=15514, recursive=True) as chown_493_15514:
                            chown_493_15514()
            with Stage(r"copy", r"Lofi Space v16.0.23.24", prog_num=15515):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15516) as should_copy_source_494_15516:
                    should_copy_source_494_15516()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=15517):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=15518) as copy_dir_to_dir_495_15518:
                            copy_dir_to_dir_495_15518()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=15519) as unwtar_496_15519:
                            unwtar_496_15519()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=15520, recursive=True) as chown_497_15520:
                            chown_497_15520()
            with Stage(r"copy", r"MV2 v16.0.23.24", prog_num=15521):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15522) as should_copy_source_498_15522:
                    should_copy_source_498_15522()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=15523):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=15524) as copy_dir_to_dir_499_15524:
                            copy_dir_to_dir_499_15524()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=15525) as unwtar_500_15525:
                            unwtar_500_15525()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV2.bundle", user_id=-1, group_id=-1, prog_num=15526, recursive=True) as chown_501_15526:
                            chown_501_15526()
            with Stage(r"copy", r"Magma Springs v16.0.23.24", prog_num=15527):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15528) as should_copy_source_502_15528:
                    should_copy_source_502_15528()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=15529):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=15530) as copy_dir_to_dir_503_15530:
                            copy_dir_to_dir_503_15530()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=15531) as unwtar_504_15531:
                            unwtar_504_15531()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=15532, recursive=True) as chown_505_15532:
                            chown_505_15532()
            with Stage(r"copy", r"MannyM-TripleD v16.0.23.24", prog_num=15533):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15534) as should_copy_source_506_15534:
                    should_copy_source_506_15534()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=15535):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=15536) as copy_dir_to_dir_507_15536:
                            copy_dir_to_dir_507_15536()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=15537) as unwtar_508_15537:
                            unwtar_508_15537()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=15538, recursive=True) as chown_509_15538:
                            chown_509_15538()
            with Stage(r"copy", r"Maserati DRM v16.0.23.24", prog_num=15539):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15540) as should_copy_source_510_15540:
                    should_copy_source_510_15540()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=15541):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=15542) as copy_dir_to_dir_511_15542:
                            copy_dir_to_dir_511_15542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=15543) as unwtar_512_15543:
                            unwtar_512_15543()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=15544, recursive=True) as chown_513_15544:
                            chown_513_15544()
            with Stage(r"copy", r"Maserati VX1 v16.0.23.24", prog_num=15545):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15546) as should_copy_source_514_15546:
                    should_copy_source_514_15546()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=15547):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=15548) as copy_dir_to_dir_515_15548:
                            copy_dir_to_dir_515_15548()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=15549) as unwtar_516_15549:
                            unwtar_516_15549()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=15550, recursive=True) as chown_517_15550:
                            chown_517_15550()
            with Stage(r"copy", r"MaxxBass v16.0.30.31", prog_num=15551):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15552) as should_copy_source_518_15552:
                    should_copy_source_518_15552()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=15553):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=15554) as copy_dir_to_dir_519_15554:
                            copy_dir_to_dir_519_15554()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=15555) as unwtar_520_15555:
                            unwtar_520_15555()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=15556, recursive=True) as chown_521_15556:
                            chown_521_15556()
            with Stage(r"copy", r"MaxxVolume v16.0.23.24", prog_num=15557):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15558) as should_copy_source_522_15558:
                    should_copy_source_522_15558()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=15559):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=15560) as copy_dir_to_dir_523_15560:
                            copy_dir_to_dir_523_15560()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=15561) as unwtar_524_15561:
                            unwtar_524_15561()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=15562, recursive=True) as chown_525_15562:
                            chown_525_15562()
            with Stage(r"copy", r"MetaFilter v16.0.23.24", prog_num=15563):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15564) as should_copy_source_526_15564:
                    should_copy_source_526_15564()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=15565):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=15566) as copy_dir_to_dir_527_15566:
                            copy_dir_to_dir_527_15566()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=15567) as unwtar_528_15567:
                            unwtar_528_15567()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=15568, recursive=True) as chown_529_15568:
                            chown_529_15568()
            with Stage(r"copy", r"MetaFlanger v16.0.23.24", prog_num=15569):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15570) as should_copy_source_530_15570:
                    should_copy_source_530_15570()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=15571):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=15572) as copy_dir_to_dir_531_15572:
                            copy_dir_to_dir_531_15572()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=15573) as unwtar_532_15573:
                            unwtar_532_15573()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=15574, recursive=True) as chown_533_15574:
                            chown_533_15574()
            with Stage(r"copy", r"MondoMod v16.0.23.24", prog_num=15575):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15576) as should_copy_source_534_15576:
                    should_copy_source_534_15576()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=15577):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=15578) as copy_dir_to_dir_535_15578:
                            copy_dir_to_dir_535_15578()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=15579) as unwtar_536_15579:
                            unwtar_536_15579()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=15580, recursive=True) as chown_537_15580:
                            chown_537_15580()
            with Stage(r"copy", r"Morphoder v16.0.23.24", prog_num=15581):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15582) as should_copy_source_538_15582:
                    should_copy_source_538_15582()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=15583):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=15584) as copy_dir_to_dir_539_15584:
                            copy_dir_to_dir_539_15584()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=15585) as unwtar_540_15585:
                            unwtar_540_15585()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=15586, recursive=True) as chown_541_15586:
                            chown_541_15586()
            with Stage(r"copy", r"NLS v16.0.23.24", prog_num=15587):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15588) as should_copy_source_542_15588:
                    should_copy_source_542_15588()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=15589):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=15590) as copy_dir_to_dir_543_15590:
                            copy_dir_to_dir_543_15590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=15591) as unwtar_544_15591:
                            unwtar_544_15591()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NLS.bundle", user_id=-1, group_id=-1, prog_num=15592, recursive=True) as chown_545_15592:
                            chown_545_15592()
            with Stage(r"copy", r"NX v16.0.23.24", prog_num=15593):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15594) as should_copy_source_546_15594:
                    should_copy_source_546_15594()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=15595):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=15596) as copy_dir_to_dir_547_15596:
                            copy_dir_to_dir_547_15596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=15597) as unwtar_548_15597:
                            unwtar_548_15597()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NX.bundle", user_id=-1, group_id=-1, prog_num=15598, recursive=True) as chown_549_15598:
                            chown_549_15598()
            with Stage(r"copy", r"OKDriver v16.0.23.24", prog_num=15599):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15600) as should_copy_source_550_15600:
                    should_copy_source_550_15600()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=15601):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=15602) as copy_dir_to_dir_551_15602:
                            copy_dir_to_dir_551_15602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=15603) as unwtar_552_15603:
                            unwtar_552_15603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=15604, recursive=True) as chown_553_15604:
                            chown_553_15604()
            with Stage(r"copy", r"OKFilter v16.0.23.24", prog_num=15605):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15606) as should_copy_source_554_15606:
                    should_copy_source_554_15606()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=15607):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=15608) as copy_dir_to_dir_555_15608:
                            copy_dir_to_dir_555_15608()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=15609) as unwtar_556_15609:
                            unwtar_556_15609()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=15610, recursive=True) as chown_557_15610:
                            chown_557_15610()
            with Stage(r"copy", r"OKPhatter v16.0.23.24", prog_num=15611):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15612) as should_copy_source_558_15612:
                    should_copy_source_558_15612()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=15613):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=15614) as copy_dir_to_dir_559_15614:
                            copy_dir_to_dir_559_15614()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=15615) as unwtar_560_15615:
                            unwtar_560_15615()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=15616, recursive=True) as chown_561_15616:
                            chown_561_15616()
            with Stage(r"copy", r"OKPumper v16.0.23.24", prog_num=15617):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15618) as should_copy_source_562_15618:
                    should_copy_source_562_15618()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=15619):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=15620) as copy_dir_to_dir_563_15620:
                            copy_dir_to_dir_563_15620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=15621) as unwtar_564_15621:
                            unwtar_564_15621()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=15622, recursive=True) as chown_565_15622:
                            chown_565_15622()
            with Stage(r"copy", r"PAZ v16.0.23.24", prog_num=15623):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15624) as should_copy_source_566_15624:
                    should_copy_source_566_15624()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=15625):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=15626) as copy_dir_to_dir_567_15626:
                            copy_dir_to_dir_567_15626()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=15627) as unwtar_568_15627:
                            unwtar_568_15627()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PAZ.bundle", user_id=-1, group_id=-1, prog_num=15628, recursive=True) as chown_569_15628:
                            chown_569_15628()
            with Stage(r"copy", r"PS22 v16.0.23.24", prog_num=15629):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15630) as should_copy_source_570_15630:
                    should_copy_source_570_15630()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=15631):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=15632) as copy_dir_to_dir_571_15632:
                            copy_dir_to_dir_571_15632()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=15633) as unwtar_572_15633:
                            unwtar_572_15633()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PS22.bundle", user_id=-1, group_id=-1, prog_num=15634, recursive=True) as chown_573_15634:
                            chown_573_15634()
            with Stage(r"copy", r"PuigChild v16.0.23.24", prog_num=15635):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15636) as should_copy_source_574_15636:
                    should_copy_source_574_15636()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=15637):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=15638) as copy_dir_to_dir_575_15638:
                            copy_dir_to_dir_575_15638()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=15639) as unwtar_576_15639:
                            unwtar_576_15639()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=15640, recursive=True) as chown_577_15640:
                            chown_577_15640()
            with Stage(r"copy", r"PuigTec v16.0.23.24", prog_num=15641):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15642) as should_copy_source_578_15642:
                    should_copy_source_578_15642()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=15643):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=15644) as copy_dir_to_dir_579_15644:
                            copy_dir_to_dir_579_15644()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=15645) as unwtar_580_15645:
                            unwtar_580_15645()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=15646, recursive=True) as chown_581_15646:
                            chown_581_15646()
            with Stage(r"copy", r"Q10 v16.0.23.24", prog_num=15647):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15648) as should_copy_source_582_15648:
                    should_copy_source_582_15648()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=15649):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=15650) as copy_dir_to_dir_583_15650:
                            copy_dir_to_dir_583_15650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=15651) as unwtar_584_15651:
                            unwtar_584_15651()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q10.bundle", user_id=-1, group_id=-1, prog_num=15652, recursive=True) as chown_585_15652:
                            chown_585_15652()
            with Stage(r"copy", r"Q-Clone v16.0.23.24", prog_num=15653):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15654) as should_copy_source_586_15654:
                    should_copy_source_586_15654()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=15655):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=15656) as copy_dir_to_dir_587_15656:
                            copy_dir_to_dir_587_15656()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=15657) as unwtar_588_15657:
                            unwtar_588_15657()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=15658, recursive=True) as chown_589_15658:
                            chown_589_15658()
            with Stage(r"copy", r"RBass v16.0.23.24", prog_num=15659):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15660) as should_copy_source_590_15660:
                    should_copy_source_590_15660()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=15661):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=15662) as copy_dir_to_dir_591_15662:
                            copy_dir_to_dir_591_15662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=15663) as unwtar_592_15663:
                            unwtar_592_15663()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RBass.bundle", user_id=-1, group_id=-1, prog_num=15664, recursive=True) as chown_593_15664:
                            chown_593_15664()
            with Stage(r"copy", r"RChannel v16.0.23.24", prog_num=15665):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15666) as should_copy_source_594_15666:
                    should_copy_source_594_15666()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=15667):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=15668) as copy_dir_to_dir_595_15668:
                            copy_dir_to_dir_595_15668()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=15669) as unwtar_596_15669:
                            unwtar_596_15669()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RChannel.bundle", user_id=-1, group_id=-1, prog_num=15670, recursive=True) as chown_597_15670:
                            chown_597_15670()
            with Stage(r"copy", r"RComp v16.0.23.24", prog_num=15671):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15672) as should_copy_source_598_15672:
                    should_copy_source_598_15672()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=15673):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=15674) as copy_dir_to_dir_599_15674:
                            copy_dir_to_dir_599_15674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=15675) as unwtar_600_15675:
                            unwtar_600_15675()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RComp.bundle", user_id=-1, group_id=-1, prog_num=15676, recursive=True) as chown_601_15676:
                            chown_601_15676()
            with Stage(r"copy", r"RDeEsser v16.0.23.24", prog_num=15677):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15678) as should_copy_source_602_15678:
                    should_copy_source_602_15678()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=15679):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=15680) as copy_dir_to_dir_603_15680:
                            copy_dir_to_dir_603_15680()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=15681) as unwtar_604_15681:
                            unwtar_604_15681()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=15682, recursive=True) as chown_605_15682:
                            chown_605_15682()
            with Stage(r"copy", r"REDD17 v16.0.23.24", prog_num=15683):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15684) as should_copy_source_606_15684:
                    should_copy_source_606_15684()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=15685):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=15686) as copy_dir_to_dir_607_15686:
                            copy_dir_to_dir_607_15686()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=15687) as unwtar_608_15687:
                            unwtar_608_15687()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD17.bundle", user_id=-1, group_id=-1, prog_num=15688, recursive=True) as chown_609_15688:
                            chown_609_15688()
            with Stage(r"copy", r"REDD37-51 v16.0.23.24", prog_num=15689):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15690) as should_copy_source_610_15690:
                    should_copy_source_610_15690()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=15691):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=15692) as copy_dir_to_dir_611_15692:
                            copy_dir_to_dir_611_15692()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=15693) as unwtar_612_15693:
                            unwtar_612_15693()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=15694, recursive=True) as chown_613_15694:
                            chown_613_15694()
            with Stage(r"copy", r"REQ v16.0.23.24", prog_num=15695):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15696) as should_copy_source_614_15696:
                    should_copy_source_614_15696()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=15697):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=15698) as copy_dir_to_dir_615_15698:
                            copy_dir_to_dir_615_15698()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=15699) as unwtar_616_15699:
                            unwtar_616_15699()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REQ.bundle", user_id=-1, group_id=-1, prog_num=15700, recursive=True) as chown_617_15700:
                            chown_617_15700()
            with Stage(r"copy", r"RS56 v16.0.23.24", prog_num=15701):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15702) as should_copy_source_618_15702:
                    should_copy_source_618_15702()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=15703):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=15704) as copy_dir_to_dir_619_15704:
                            copy_dir_to_dir_619_15704()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=15705) as unwtar_620_15705:
                            unwtar_620_15705()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RS56.bundle", user_id=-1, group_id=-1, prog_num=15706, recursive=True) as chown_621_15706:
                            chown_621_15706()
            with Stage(r"copy", r"RVerb v16.0.23.24", prog_num=15707):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15708) as should_copy_source_622_15708:
                    should_copy_source_622_15708()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=15709):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=15710) as copy_dir_to_dir_623_15710:
                            copy_dir_to_dir_623_15710()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=15711) as unwtar_624_15711:
                            unwtar_624_15711()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVerb.bundle", user_id=-1, group_id=-1, prog_num=15712, recursive=True) as chown_625_15712:
                            chown_625_15712()
            with Stage(r"copy", r"RVox v16.0.23.24", prog_num=15713):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15714) as should_copy_source_626_15714:
                    should_copy_source_626_15714()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=15715):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=15716) as copy_dir_to_dir_627_15716:
                            copy_dir_to_dir_627_15716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=15717) as unwtar_628_15717:
                            unwtar_628_15717()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVox.bundle", user_id=-1, group_id=-1, prog_num=15718, recursive=True) as chown_629_15718:
                            chown_629_15718()
            with Stage(r"copy", r"Reel ADT v16.0.23.24", prog_num=15719):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15720) as should_copy_source_630_15720:
                    should_copy_source_630_15720()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=15721):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=15722) as copy_dir_to_dir_631_15722:
                            copy_dir_to_dir_631_15722()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=15723) as unwtar_632_15723:
                            unwtar_632_15723()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=15724, recursive=True) as chown_633_15724:
                            chown_633_15724()
            with Stage(r"copy", r"RenAxx v16.0.23.24", prog_num=15725):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15726) as should_copy_source_634_15726:
                    should_copy_source_634_15726()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=15727):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=15728) as copy_dir_to_dir_635_15728:
                            copy_dir_to_dir_635_15728()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=15729) as unwtar_636_15729:
                            unwtar_636_15729()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=15730, recursive=True) as chown_637_15730:
                            chown_637_15730()
            with Stage(r"copy", r"Retro Fi v16.0.23.24", prog_num=15731):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15732) as should_copy_source_638_15732:
                    should_copy_source_638_15732()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=15733):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=15734) as copy_dir_to_dir_639_15734:
                            copy_dir_to_dir_639_15734()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=15735) as unwtar_640_15735:
                            unwtar_640_15735()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=15736, recursive=True) as chown_641_15736:
                            chown_641_15736()
            with Stage(r"copy", r"S1 v16.0.23.24", prog_num=15737):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15738) as should_copy_source_642_15738:
                    should_copy_source_642_15738()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=15739):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=15740) as copy_dir_to_dir_643_15740:
                            copy_dir_to_dir_643_15740()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=15741) as unwtar_644_15741:
                            unwtar_644_15741()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S1.bundle", user_id=-1, group_id=-1, prog_num=15742, recursive=True) as chown_645_15742:
                            chown_645_15742()
            with Stage(r"copy", r"Scheps 73 v16.0.23.24", prog_num=15743):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15744) as should_copy_source_646_15744:
                    should_copy_source_646_15744()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=15745):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=15746) as copy_dir_to_dir_647_15746:
                            copy_dir_to_dir_647_15746()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=15747) as unwtar_648_15747:
                            unwtar_648_15747()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=15748, recursive=True) as chown_649_15748:
                            chown_649_15748()
            with Stage(r"copy", r"Scheps Omni Channel v16.0.64.65", prog_num=15749):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15750) as should_copy_source_650_15750:
                    should_copy_source_650_15750()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=15751):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=15752) as copy_dir_to_dir_651_15752:
                            copy_dir_to_dir_651_15752()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=15753) as unwtar_652_15753:
                            unwtar_652_15753()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=15754, recursive=True) as chown_653_15754:
                            chown_653_15754()
            with Stage(r"copy", r"Scheps Parallel Particles v16.0.23.24", prog_num=15755):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15756) as should_copy_source_654_15756:
                    should_copy_source_654_15756()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=15757):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=15758) as copy_dir_to_dir_655_15758:
                            copy_dir_to_dir_655_15758()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=15759) as unwtar_656_15759:
                            unwtar_656_15759()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=15760, recursive=True) as chown_657_15760:
                            chown_657_15760()
            with Stage(r"copy", r"Sibilance v16.0.23.24", prog_num=15761):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15762) as should_copy_source_658_15762:
                    should_copy_source_658_15762()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=15763):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=15764) as copy_dir_to_dir_659_15764:
                            copy_dir_to_dir_659_15764()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=15765) as unwtar_660_15765:
                            unwtar_660_15765()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=15766, recursive=True) as chown_661_15766:
                            chown_661_15766()
            with Stage(r"copy", r"Emo Signal Generator v16.0.23.24", prog_num=15767):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15768) as should_copy_source_662_15768:
                    should_copy_source_662_15768()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=15769):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=15770) as copy_dir_to_dir_663_15770:
                            copy_dir_to_dir_663_15770()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=15771) as unwtar_664_15771:
                            unwtar_664_15771()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=15772, recursive=True) as chown_665_15772:
                            chown_665_15772()
            with Stage(r"copy", r"Silk Vocal v16.0.23.24", prog_num=15773):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15774) as should_copy_source_666_15774:
                    should_copy_source_666_15774()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=15775):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=15776) as copy_dir_to_dir_667_15776:
                            copy_dir_to_dir_667_15776()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=15777) as unwtar_668_15777:
                            unwtar_668_15777()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=15778, recursive=True) as chown_669_15778:
                            chown_669_15778()
            with Stage(r"copy", r"Smack Attack v16.0.23.24", prog_num=15779):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15780) as should_copy_source_670_15780:
                    should_copy_source_670_15780()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=15781):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=15782) as copy_dir_to_dir_671_15782:
                            copy_dir_to_dir_671_15782()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=15783) as unwtar_672_15783:
                            unwtar_672_15783()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=15784, recursive=True) as chown_673_15784:
                            chown_673_15784()
            with Stage(r"copy", r"SoundShifter v16.0.23.24", prog_num=15785):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15786) as should_copy_source_674_15786:
                    should_copy_source_674_15786()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=15787):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=15788) as copy_dir_to_dir_675_15788:
                            copy_dir_to_dir_675_15788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=15789) as unwtar_676_15789:
                            unwtar_676_15789()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=15790, recursive=True) as chown_677_15790:
                            chown_677_15790()
            with Stage(r"copy", r"Spherix Immersive Compressor v16.0.23.24", prog_num=15791):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15792) as should_copy_source_678_15792:
                    should_copy_source_678_15792()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=15793):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=15794) as copy_dir_to_dir_679_15794:
                            copy_dir_to_dir_679_15794()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=15795) as unwtar_680_15795:
                            unwtar_680_15795()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=15796, recursive=True) as chown_681_15796:
                            chown_681_15796()
            with Stage(r"copy", r"Spherix Immersive Limiter v16.0.23.24", prog_num=15797):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15798) as should_copy_source_682_15798:
                    should_copy_source_682_15798()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=15799):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=15800) as copy_dir_to_dir_683_15800:
                            copy_dir_to_dir_683_15800()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=15801) as unwtar_684_15801:
                            unwtar_684_15801()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=15802, recursive=True) as chown_685_15802:
                            chown_685_15802()
            with Stage(r"copy", r"SuperTap v16.0.23.24", prog_num=15803):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15804) as should_copy_source_686_15804:
                    should_copy_source_686_15804()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=15805):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=15806) as copy_dir_to_dir_687_15806:
                            copy_dir_to_dir_687_15806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=15807) as unwtar_688_15807:
                            unwtar_688_15807()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=15808, recursive=True) as chown_689_15808:
                            chown_689_15808()
            with Stage(r"copy", r"TG12345 v16.0.23.24", prog_num=15809):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15810) as should_copy_source_690_15810:
                    should_copy_source_690_15810()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=15811):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=15812) as copy_dir_to_dir_691_15812:
                            copy_dir_to_dir_691_15812()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=15813) as unwtar_692_15813:
                            unwtar_692_15813()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TG12345.bundle", user_id=-1, group_id=-1, prog_num=15814, recursive=True) as chown_693_15814:
                            chown_693_15814()
            with Stage(r"copy", r"AR TG Meter Bridge v16.0.23.24", prog_num=15815):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15816) as should_copy_source_694_15816:
                    should_copy_source_694_15816()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=15817):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=15818) as copy_dir_to_dir_695_15818:
                            copy_dir_to_dir_695_15818()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=15819) as unwtar_696_15819:
                            unwtar_696_15819()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=15820, recursive=True) as chown_697_15820:
                            chown_697_15820()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v16.0.23.24", prog_num=15821):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15822) as should_copy_source_698_15822:
                    should_copy_source_698_15822()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=15823):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=15824) as copy_dir_to_dir_699_15824:
                            copy_dir_to_dir_699_15824()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=15825) as unwtar_700_15825:
                            unwtar_700_15825()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=15826, recursive=True) as chown_701_15826:
                            chown_701_15826()
            with Stage(r"copy", r"TransX v16.0.23.24", prog_num=15827):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15828) as should_copy_source_702_15828:
                    should_copy_source_702_15828()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=15829):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=15830) as copy_dir_to_dir_703_15830:
                            copy_dir_to_dir_703_15830()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=15831) as unwtar_704_15831:
                            unwtar_704_15831()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TransX.bundle", user_id=-1, group_id=-1, prog_num=15832, recursive=True) as chown_705_15832:
                            chown_705_15832()
            with Stage(r"copy", r"TrueVerb v16.0.23.24", prog_num=15833):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15834) as should_copy_source_706_15834:
                    should_copy_source_706_15834()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=15835):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=15836) as copy_dir_to_dir_707_15836:
                            copy_dir_to_dir_707_15836()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=15837) as unwtar_708_15837:
                            unwtar_708_15837()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=15838, recursive=True) as chown_709_15838:
                            chown_709_15838()
            with Stage(r"copy", r"UM v16.0.23.24", prog_num=15839):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15840) as should_copy_source_710_15840:
                    should_copy_source_710_15840()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=15841):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=15842) as copy_dir_to_dir_711_15842:
                            copy_dir_to_dir_711_15842()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=15843) as unwtar_712_15843:
                            unwtar_712_15843()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UM.bundle", user_id=-1, group_id=-1, prog_num=15844, recursive=True) as chown_713_15844:
                            chown_713_15844()
            with Stage(r"copy", r"UltraPitch v16.0.23.24", prog_num=15845):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15846) as should_copy_source_714_15846:
                    should_copy_source_714_15846()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=15847):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=15848) as copy_dir_to_dir_715_15848:
                            copy_dir_to_dir_715_15848()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=15849) as unwtar_716_15849:
                            unwtar_716_15849()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=15850, recursive=True) as chown_717_15850:
                            chown_717_15850()
            with Stage(r"copy", r"VComp v16.0.23.24", prog_num=15851):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15852) as should_copy_source_718_15852:
                    should_copy_source_718_15852()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=15853):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=15854) as copy_dir_to_dir_719_15854:
                            copy_dir_to_dir_719_15854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=15855) as unwtar_720_15855:
                            unwtar_720_15855()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VComp.bundle", user_id=-1, group_id=-1, prog_num=15856, recursive=True) as chown_721_15856:
                            chown_721_15856()
            with Stage(r"copy", r"VEQ3 v16.0.23.24", prog_num=15857):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15858) as should_copy_source_722_15858:
                    should_copy_source_722_15858()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=15859):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=15860) as copy_dir_to_dir_723_15860:
                            copy_dir_to_dir_723_15860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=15861) as unwtar_724_15861:
                            unwtar_724_15861()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=15862, recursive=True) as chown_725_15862:
                            chown_725_15862()
            with Stage(r"copy", r"VEQ4 v16.0.23.24", prog_num=15863):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15864) as should_copy_source_726_15864:
                    should_copy_source_726_15864()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=15865):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=15866) as copy_dir_to_dir_727_15866:
                            copy_dir_to_dir_727_15866()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=15867) as unwtar_728_15867:
                            unwtar_728_15867()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=15868, recursive=True) as chown_729_15868:
                            chown_729_15868()
            with Stage(r"copy", r"VU Meter v16.0.23.24", prog_num=15869):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15870) as should_copy_source_730_15870:
                    should_copy_source_730_15870()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=15871):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=15872) as copy_dir_to_dir_731_15872:
                            copy_dir_to_dir_731_15872()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=15873) as unwtar_732_15873:
                            unwtar_732_15873()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=15874, recursive=True) as chown_733_15874:
                            chown_733_15874()
            with Stage(r"copy", r"Vitamin v16.0.23.24", prog_num=15875):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15876) as should_copy_source_734_15876:
                    should_copy_source_734_15876()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=15877):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=15878) as copy_dir_to_dir_735_15878:
                            copy_dir_to_dir_735_15878()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=15879) as unwtar_736_15879:
                            unwtar_736_15879()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=15880, recursive=True) as chown_737_15880:
                            chown_737_15880()
            with Stage(r"copy", r"Vocal Rider v16.0.23.24", prog_num=15881):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15882) as should_copy_source_738_15882:
                    should_copy_source_738_15882()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=15883):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=15884) as copy_dir_to_dir_739_15884:
                            copy_dir_to_dir_739_15884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=15885) as unwtar_740_15885:
                            unwtar_740_15885()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=15886, recursive=True) as chown_741_15886:
                            chown_741_15886()
            with Stage(r"copy", r"Voltage Amps Bass v16.0.23.24", prog_num=15887):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15888) as should_copy_source_742_15888:
                    should_copy_source_742_15888()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=15889):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=15890) as copy_dir_to_dir_743_15890:
                            copy_dir_to_dir_743_15890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=15891) as unwtar_744_15891:
                            unwtar_744_15891()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=15892, recursive=True) as chown_745_15892:
                            chown_745_15892()
            with Stage(r"copy", r"Voltage Amps Guitar v16.0.23.24", prog_num=15893):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15894) as should_copy_source_746_15894:
                    should_copy_source_746_15894()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=15895):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=15896) as copy_dir_to_dir_747_15896:
                            copy_dir_to_dir_747_15896()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=15897) as unwtar_748_15897:
                            unwtar_748_15897()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=15898, recursive=True) as chown_749_15898:
                            chown_749_15898()
            with Stage(r"copy", r"WLM v16.0.23.24", prog_num=15899):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15900) as should_copy_source_750_15900:
                    should_copy_source_750_15900()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=15901):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=15902) as copy_dir_to_dir_751_15902:
                            copy_dir_to_dir_751_15902()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=15903) as unwtar_752_15903:
                            unwtar_752_15903()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM.bundle", user_id=-1, group_id=-1, prog_num=15904, recursive=True) as chown_753_15904:
                            chown_753_15904()
            with Stage(r"copy", r"WLM Plus v16.0.23.24", prog_num=15905):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15906) as should_copy_source_754_15906:
                    should_copy_source_754_15906()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=15907):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=15908) as copy_dir_to_dir_755_15908:
                            copy_dir_to_dir_755_15908()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=15909) as unwtar_756_15909:
                            unwtar_756_15909()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=15910, recursive=True) as chown_757_15910:
                            chown_757_15910()
            with Stage(r"copy", r"WavesHeadTracker v16.0.23.24", prog_num=15911):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=5, prog_num=15912) as should_copy_source_758_15912:
                    should_copy_source_758_15912()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=15913):
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=15914) as rm_file_or_dir_759_15914:
                            rm_file_or_dir_759_15914()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=15915) as copy_dir_to_dir_760_15915:
                            copy_dir_to_dir_760_15915()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=15916) as unwtar_761_15916:
                            unwtar_761_15916()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=15917, recursive=True) as chown_762_15917:
                            chown_762_15917()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=15918):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15919) as should_copy_source_763_15919:
                    should_copy_source_763_15919()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=15920):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=15921) as copy_dir_to_dir_764_15921:
                            copy_dir_to_dir_764_15921()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=15922) as unwtar_765_15922:
                            unwtar_765_15922()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=15923, recursive=True) as chown_766_15923:
                            chown_766_15923()
            with Stage(r"copy", r"WavesLib1_16_0_30_31 v16.0.30.31", prog_num=15924):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15925) as should_copy_source_767_15925:
                    should_copy_source_767_15925()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.30.framework", prog_num=15926):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r".", delete_extraneous_files=True, prog_num=15927) as copy_dir_to_dir_768_15927:
                            copy_dir_to_dir_768_15927()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", where_to_unwtar=r".", prog_num=15928) as unwtar_769_15928:
                            unwtar_769_15928()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.30.framework", user_id=-1, group_id=-1, prog_num=15929, recursive=True) as chown_770_15929:
                            chown_770_15929()
            with Stage(r"copy", r"WavesLib1_16_0_64_65 v16.0.64.65", prog_num=15930):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15931) as should_copy_source_771_15931:
                    should_copy_source_771_15931()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.64.framework", prog_num=15932):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", r".", delete_extraneous_files=True, prog_num=15933) as copy_dir_to_dir_772_15933:
                            copy_dir_to_dir_772_15933()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", where_to_unwtar=r".", prog_num=15934) as unwtar_773_15934:
                            unwtar_773_15934()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.64.framework", user_id=-1, group_id=-1, prog_num=15935, recursive=True) as chown_774_15935:
                            chown_774_15935()
            with Stage(r"copy", r"WavesTune v16.0.23.24", prog_num=15936):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15937) as should_copy_source_775_15937:
                    should_copy_source_775_15937()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=15938):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=15939) as copy_dir_to_dir_776_15939:
                            copy_dir_to_dir_776_15939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=15940) as unwtar_777_15940:
                            unwtar_777_15940()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=15941, recursive=True) as chown_778_15941:
                            chown_778_15941()
            with Stage(r"copy", r"WavesTune LT v16.0.23.24", prog_num=15942):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15943) as should_copy_source_779_15943:
                    should_copy_source_779_15943()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=15944):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=15945) as copy_dir_to_dir_780_15945:
                            copy_dir_to_dir_780_15945()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=15946) as unwtar_781_15946:
                            unwtar_781_15946()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=15947, recursive=True) as chown_782_15947:
                            chown_782_15947()
            with Stage(r"copy", r"Waves Harmony v16.0.23.24", prog_num=15948):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15949) as should_copy_source_783_15949:
                    should_copy_source_783_15949()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=15950):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=15951) as copy_dir_to_dir_784_15951:
                            copy_dir_to_dir_784_15951()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=15952) as unwtar_785_15952:
                            unwtar_785_15952()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=15953, recursive=True) as chown_786_15953:
                            chown_786_15953()
            with Stage(r"copy", r"Waves Tune Real-Time v16.0.23.24", prog_num=15954):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15955) as should_copy_source_787_15955:
                    should_copy_source_787_15955()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=15956):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=15957) as copy_dir_to_dir_788_15957:
                            copy_dir_to_dir_788_15957()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=15958) as unwtar_789_15958:
                            unwtar_789_15958()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=15959, recursive=True) as chown_790_15959:
                            chown_790_15959()
            with Stage(r"copy", r"X-Click v16.0.23.24", prog_num=15960):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15961) as should_copy_source_791_15961:
                    should_copy_source_791_15961()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=15962):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=15963) as copy_dir_to_dir_792_15963:
                            copy_dir_to_dir_792_15963()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=15964) as unwtar_793_15964:
                            unwtar_793_15964()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Click.bundle", user_id=-1, group_id=-1, prog_num=15965, recursive=True) as chown_794_15965:
                            chown_794_15965()
            with Stage(r"copy", r"X-Crackle v16.0.23.24", prog_num=15966):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15967) as should_copy_source_795_15967:
                    should_copy_source_795_15967()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=15968):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=15969) as copy_dir_to_dir_796_15969:
                            copy_dir_to_dir_796_15969()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=15970) as unwtar_797_15970:
                            unwtar_797_15970()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=15971, recursive=True) as chown_798_15971:
                            chown_798_15971()
            with Stage(r"copy", r"X-Hum v16.0.23.24", prog_num=15972):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15973) as should_copy_source_799_15973:
                    should_copy_source_799_15973()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=15974):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=15975) as copy_dir_to_dir_800_15975:
                            copy_dir_to_dir_800_15975()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=15976) as unwtar_801_15976:
                            unwtar_801_15976()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=15977, recursive=True) as chown_802_15977:
                            chown_802_15977()
            with Stage(r"copy", r"X-Noise v16.0.23.24", prog_num=15978):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15979) as should_copy_source_803_15979:
                    should_copy_source_803_15979()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=15980):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=15981) as copy_dir_to_dir_804_15981:
                            copy_dir_to_dir_804_15981()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=15982) as unwtar_805_15982:
                            unwtar_805_15982()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=15983, recursive=True) as chown_806_15983:
                            chown_806_15983()
            with Stage(r"copy", r"Z-Noise v16.0.23.24", prog_num=15984):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=15985) as should_copy_source_807_15985:
                    should_copy_source_807_15985()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=15986):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=15987) as copy_dir_to_dir_808_15987:
                            copy_dir_to_dir_808_15987()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=15988) as unwtar_809_15988:
                            unwtar_809_15988()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=15989, recursive=True) as chown_810_15989:
                            chown_810_15989()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=6, prog_num=15995) as resolve_symlink_files_in_folder_811_15995:
                resolve_symlink_files_in_folder_811_15995()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=15996) as shell_command_812_15996:
                shell_command_812_15996()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=15997) as script_command_813_15997:
                script_command_813_15997()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=15998) as shell_command_814_15998:
                shell_command_814_15998()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=15999) as create_symlink_815_15999:
                create_symlink_815_15999()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=16000) as create_symlink_816_16000:
                create_symlink_816_16000()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=16001) as copy_glob_to_dir_817_16001:
                copy_glob_to_dir_817_16001()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=16002) as cd_stage_818_16002:
            cd_stage_818_16002()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=16003):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=16004) as should_copy_source_819_16004:
                    should_copy_source_819_16004()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=16005):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=16006) as copy_file_to_dir_820_16006:
                            copy_file_to_dir_820_16006()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=16007) as chmod_and_chown_821_16007:
                            chmod_and_chown_821_16007()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTR", prog_num=16008) as cd_stage_822_16008:
            cd_stage_822_16008()
            with Stage(r"copy", r"GTR Stomps v16.0.23.24", prog_num=16009):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16010) as should_copy_source_823_16010:
                    should_copy_source_823_16010()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=16011):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=16012) as copy_dir_to_dir_824_16012:
                            copy_dir_to_dir_824_16012()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=16013) as unwtar_825_16013:
                            unwtar_825_16013()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=16014, recursive=True) as chown_826_16014:
                            chown_826_16014()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16015) as should_copy_source_827_16015:
                    should_copy_source_827_16015()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=16016):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=16017) as copy_dir_to_dir_828_16017:
                            copy_dir_to_dir_828_16017()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=16018) as unwtar_829_16018:
                            unwtar_829_16018()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=16019, recursive=True) as chown_830_16019:
                            chown_830_16019()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16020) as should_copy_source_831_16020:
                    should_copy_source_831_16020()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=16021):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=16022) as copy_dir_to_dir_832_16022:
                            copy_dir_to_dir_832_16022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=16023) as unwtar_833_16023:
                            unwtar_833_16023()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=16024, recursive=True) as chown_834_16024:
                            chown_834_16024()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16025) as should_copy_source_835_16025:
                    should_copy_source_835_16025()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=16026):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=16027) as copy_dir_to_dir_836_16027:
                            copy_dir_to_dir_836_16027()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=16028) as unwtar_837_16028:
                            unwtar_837_16028()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=16029, recursive=True) as chown_838_16029:
                            chown_838_16029()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16030) as should_copy_source_839_16030:
                    should_copy_source_839_16030()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=16031):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=16032) as copy_dir_to_dir_840_16032:
                            copy_dir_to_dir_840_16032()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=16033) as unwtar_841_16033:
                            unwtar_841_16033()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=16034, recursive=True) as chown_842_16034:
                            chown_842_16034()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16035) as should_copy_source_843_16035:
                    should_copy_source_843_16035()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=16036):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=16037) as copy_dir_to_dir_844_16037:
                            copy_dir_to_dir_844_16037()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=16038) as unwtar_845_16038:
                            unwtar_845_16038()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=16039, recursive=True) as chown_846_16039:
                            chown_846_16039()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16040) as should_copy_source_847_16040:
                    should_copy_source_847_16040()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=16041):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=16042) as copy_dir_to_dir_848_16042:
                            copy_dir_to_dir_848_16042()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=16043) as unwtar_849_16043:
                            unwtar_849_16043()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=16044, recursive=True) as chown_850_16044:
                            chown_850_16044()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16045) as should_copy_source_851_16045:
                    should_copy_source_851_16045()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=16046):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=16047) as copy_dir_to_dir_852_16047:
                            copy_dir_to_dir_852_16047()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=16048) as unwtar_853_16048:
                            unwtar_853_16048()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=16049, recursive=True) as chown_854_16049:
                            chown_854_16049()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16050) as should_copy_source_855_16050:
                    should_copy_source_855_16050()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=16051):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=16052) as copy_dir_to_dir_856_16052:
                            copy_dir_to_dir_856_16052()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=16053) as unwtar_857_16053:
                            unwtar_857_16053()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=16054, recursive=True) as chown_858_16054:
                            chown_858_16054()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16055) as should_copy_source_859_16055:
                    should_copy_source_859_16055()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=16056):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=16057) as copy_dir_to_dir_860_16057:
                            copy_dir_to_dir_860_16057()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=16058) as unwtar_861_16058:
                            unwtar_861_16058()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=16059, recursive=True) as chown_862_16059:
                            chown_862_16059()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16060) as should_copy_source_863_16060:
                    should_copy_source_863_16060()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=16061):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=16062) as copy_dir_to_dir_864_16062:
                            copy_dir_to_dir_864_16062()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=16063) as unwtar_865_16063:
                            unwtar_865_16063()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=16064, recursive=True) as chown_866_16064:
                            chown_866_16064()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16065) as should_copy_source_867_16065:
                    should_copy_source_867_16065()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=16066):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=16067) as copy_dir_to_dir_868_16067:
                            copy_dir_to_dir_868_16067()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=16068) as unwtar_869_16068:
                            unwtar_869_16068()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=16069, recursive=True) as chown_870_16069:
                            chown_870_16069()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16070) as should_copy_source_871_16070:
                    should_copy_source_871_16070()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=16071):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=16072) as copy_dir_to_dir_872_16072:
                            copy_dir_to_dir_872_16072()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=16073) as unwtar_873_16073:
                            unwtar_873_16073()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=16074, recursive=True) as chown_874_16074:
                            chown_874_16074()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16075) as should_copy_source_875_16075:
                    should_copy_source_875_16075()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=16076):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=16077) as copy_dir_to_dir_876_16077:
                            copy_dir_to_dir_876_16077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=16078) as unwtar_877_16078:
                            unwtar_877_16078()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=16079, recursive=True) as chown_878_16079:
                            chown_878_16079()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16080) as should_copy_source_879_16080:
                    should_copy_source_879_16080()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=16081):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=16082) as copy_dir_to_dir_880_16082:
                            copy_dir_to_dir_880_16082()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=16083) as unwtar_881_16083:
                            unwtar_881_16083()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=16084, recursive=True) as chown_882_16084:
                            chown_882_16084()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16085) as should_copy_source_883_16085:
                    should_copy_source_883_16085()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=16086):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=16087) as copy_dir_to_dir_884_16087:
                            copy_dir_to_dir_884_16087()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=16088) as unwtar_885_16088:
                            unwtar_885_16088()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=16089, recursive=True) as chown_886_16089:
                            chown_886_16089()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16090) as should_copy_source_887_16090:
                    should_copy_source_887_16090()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=16091):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=16092) as copy_dir_to_dir_888_16092:
                            copy_dir_to_dir_888_16092()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=16093) as unwtar_889_16093:
                            unwtar_889_16093()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=16094, recursive=True) as chown_890_16094:
                            chown_890_16094()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16095) as should_copy_source_891_16095:
                    should_copy_source_891_16095()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=16096):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=16097) as copy_dir_to_dir_892_16097:
                            copy_dir_to_dir_892_16097()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=16098) as unwtar_893_16098:
                            unwtar_893_16098()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=16099, recursive=True) as chown_894_16099:
                            chown_894_16099()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16100) as should_copy_source_895_16100:
                    should_copy_source_895_16100()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=16101):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=16102) as copy_dir_to_dir_896_16102:
                            copy_dir_to_dir_896_16102()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=16103) as unwtar_897_16103:
                            unwtar_897_16103()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=16104, recursive=True) as chown_898_16104:
                            chown_898_16104()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16105) as should_copy_source_899_16105:
                    should_copy_source_899_16105()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=16106):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=16107) as copy_dir_to_dir_900_16107:
                            copy_dir_to_dir_900_16107()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=16108) as unwtar_901_16108:
                            unwtar_901_16108()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=16109, recursive=True) as chown_902_16109:
                            chown_902_16109()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16110) as should_copy_source_903_16110:
                    should_copy_source_903_16110()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=16111):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=16112) as copy_dir_to_dir_904_16112:
                            copy_dir_to_dir_904_16112()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=16113) as unwtar_905_16113:
                            unwtar_905_16113()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=16114, recursive=True) as chown_906_16114:
                            chown_906_16114()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16115) as should_copy_source_907_16115:
                    should_copy_source_907_16115()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=16116):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=16117) as copy_dir_to_dir_908_16117:
                            copy_dir_to_dir_908_16117()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=16118) as unwtar_909_16118:
                            unwtar_909_16118()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=16119, recursive=True) as chown_910_16119:
                            chown_910_16119()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16120) as should_copy_source_911_16120:
                    should_copy_source_911_16120()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=16121):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=16122) as copy_dir_to_dir_912_16122:
                            copy_dir_to_dir_912_16122()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=16123) as unwtar_913_16123:
                            unwtar_913_16123()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=16124, recursive=True) as chown_914_16124:
                            chown_914_16124()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16125) as should_copy_source_915_16125:
                    should_copy_source_915_16125()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=16126):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=16127) as copy_dir_to_dir_916_16127:
                            copy_dir_to_dir_916_16127()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=16128) as unwtar_917_16128:
                            unwtar_917_16128()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=16129, recursive=True) as chown_918_16129:
                            chown_918_16129()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=16130) as should_copy_source_919_16130:
                    should_copy_source_919_16130()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=16131):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=16132) as copy_dir_to_dir_920_16132:
                            copy_dir_to_dir_920_16132()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=16133) as unwtar_921_16133:
                            unwtar_921_16133()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=16134, recursive=True) as chown_922_16134:
                            chown_922_16134()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=16135) as shell_command_923_16135:
                shell_command_923_16135()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=16136) as cd_stage_924_16136:
            cd_stage_924_16136()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=16137):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=16138) as should_copy_source_925_16138:
                    should_copy_source_925_16138()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=16139):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=16140) as copy_dir_to_dir_926_16140:
                            copy_dir_to_dir_926_16140()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=16141) as unwtar_927_16141:
                            unwtar_927_16141()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=16142, recursive=True) as chown_928_16142:
                            chown_928_16142()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=16143) as shell_command_929_16143:
                            shell_command_929_16143()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=16144):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=16145) as should_copy_source_930_16145:
                    should_copy_source_930_16145()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=16146):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=16147) as copy_dir_to_dir_931_16147:
                            copy_dir_to_dir_931_16147()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=16148) as unwtar_932_16148:
                            unwtar_932_16148()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=16149, recursive=True) as chown_933_16149:
                            chown_933_16149()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=16150) as break_hard_link_934_16150:
                            break_hard_link_934_16150()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=16151) as shell_command_935_16151:
                            shell_command_935_16151()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=16152, recursive=True) as chown_936_16152:
                            chown_936_16152()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=16153, recursive=True) as chmod_937_16153:
                            chmod_937_16153()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=16154):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=16155) as should_copy_source_938_16155:
                    should_copy_source_938_16155()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=16156):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=16157) as copy_dir_to_dir_939_16157:
                            copy_dir_to_dir_939_16157()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=16158) as unwtar_940_16158:
                            unwtar_940_16158()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=16159, recursive=True) as chown_941_16159:
                            chown_941_16159()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=16160) as shell_command_942_16160:
                            shell_command_942_16160()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=16161):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=16162) as should_copy_source_943_16162:
                    should_copy_source_943_16162()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=16163):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=16164) as copy_dir_to_dir_944_16164:
                            copy_dir_to_dir_944_16164()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=16165) as unwtar_945_16165:
                            unwtar_945_16165()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=16166, recursive=True) as chown_946_16166:
                            chown_946_16166()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=16167) as shell_command_947_16167:
                            shell_command_947_16167()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=16168) as script_command_948_16168:
                            script_command_948_16168()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=16169) as shell_command_949_16169:
                            shell_command_949_16169()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=16170):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=16171) as should_copy_source_950_16171:
                    should_copy_source_950_16171()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=16172):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=16173) as copy_dir_to_dir_951_16173:
                            copy_dir_to_dir_951_16173()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=16174) as unwtar_952_16174:
                            unwtar_952_16174()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=16175, recursive=True) as chown_953_16175:
                            chown_953_16175()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=16176) as shell_command_954_16176:
                shell_command_954_16176()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=16177) as cd_stage_955_16177:
            cd_stage_955_16177()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=16178):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=16179) as should_copy_source_956_16179:
                    should_copy_source_956_16179()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=16180):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=16181) as copy_dir_to_dir_957_16181:
                            copy_dir_to_dir_957_16181()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=16182) as unwtar_958_16182:
                            unwtar_958_16182()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=16183, recursive=True) as chown_959_16183:
                            chown_959_16183()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=16184) as shell_command_960_16184:
                            shell_command_960_16184()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=16185) as cd_stage_961_16185:
            cd_stage_961_16185()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=16186):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16187) as should_copy_source_962_16187:
                    should_copy_source_962_16187()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=16188):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=16189) as copy_file_to_dir_963_16189:
                            copy_file_to_dir_963_16189()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16190) as chmod_and_chown_964_16190:
                            chmod_and_chown_964_16190()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=16191):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16192) as should_copy_source_965_16192:
                    should_copy_source_965_16192()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=16193):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=16194) as copy_file_to_dir_966_16194:
                            copy_file_to_dir_966_16194()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16195) as chmod_and_chown_967_16195:
                            chmod_and_chown_967_16195()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=16196):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16197) as should_copy_source_968_16197:
                    should_copy_source_968_16197()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=16198):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=16199) as copy_file_to_dir_969_16199:
                            copy_file_to_dir_969_16199()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16200) as chmod_and_chown_970_16200:
                            chmod_and_chown_970_16200()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=16201):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16202) as should_copy_source_971_16202:
                    should_copy_source_971_16202()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=16203):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=16204) as copy_file_to_dir_972_16204:
                            copy_file_to_dir_972_16204()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16205) as chmod_and_chown_973_16205:
                            chmod_and_chown_973_16205()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=16206):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16207) as should_copy_source_974_16207:
                    should_copy_source_974_16207()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=16208):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=16209) as copy_file_to_dir_975_16209:
                            copy_file_to_dir_975_16209()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16210) as chmod_and_chown_976_16210:
                            chmod_and_chown_976_16210()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=16211):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16212) as should_copy_source_977_16212:
                    should_copy_source_977_16212()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=16213):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=16214) as copy_file_to_dir_978_16214:
                            copy_file_to_dir_978_16214()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16215) as chmod_and_chown_979_16215:
                            chmod_and_chown_979_16215()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=16216):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16217) as should_copy_source_980_16217:
                    should_copy_source_980_16217()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=16218):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=16219) as copy_file_to_dir_981_16219:
                            copy_file_to_dir_981_16219()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16220) as chmod_and_chown_982_16220:
                            chmod_and_chown_982_16220()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=16221):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16222) as should_copy_source_983_16222:
                    should_copy_source_983_16222()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=16223):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=16224) as copy_file_to_dir_984_16224:
                            copy_file_to_dir_984_16224()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16225) as chmod_and_chown_985_16225:
                            chmod_and_chown_985_16225()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=16226):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16227) as should_copy_source_986_16227:
                    should_copy_source_986_16227()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=16228):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=16229) as copy_file_to_dir_987_16229:
                            copy_file_to_dir_987_16229()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16230) as chmod_and_chown_988_16230:
                            chmod_and_chown_988_16230()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=16231):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16232) as should_copy_source_989_16232:
                    should_copy_source_989_16232()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=16233):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=16234) as copy_file_to_dir_990_16234:
                            copy_file_to_dir_990_16234()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16235) as chmod_and_chown_991_16235:
                            chmod_and_chown_991_16235()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=16236):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16237) as should_copy_source_992_16237:
                    should_copy_source_992_16237()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=16238):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=16239) as copy_file_to_dir_993_16239:
                            copy_file_to_dir_993_16239()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16240) as chmod_and_chown_994_16240:
                            chmod_and_chown_994_16240()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=16241):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16242) as should_copy_source_995_16242:
                    should_copy_source_995_16242()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=16243):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=16244) as copy_file_to_dir_996_16244:
                            copy_file_to_dir_996_16244()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16245) as chmod_and_chown_997_16245:
                            chmod_and_chown_997_16245()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=16246):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16247) as should_copy_source_998_16247:
                    should_copy_source_998_16247()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=16248):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=16249) as copy_file_to_dir_999_16249:
                            copy_file_to_dir_999_16249()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16250) as chmod_and_chown_1000_16250:
                            chmod_and_chown_1000_16250()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=16251):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16252) as should_copy_source_1001_16252:
                    should_copy_source_1001_16252()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=16253):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=16254) as copy_file_to_dir_1002_16254:
                            copy_file_to_dir_1002_16254()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16255) as chmod_and_chown_1003_16255:
                            chmod_and_chown_1003_16255()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=16256):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16257) as should_copy_source_1004_16257:
                    should_copy_source_1004_16257()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=16258):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=16259) as copy_file_to_dir_1005_16259:
                            copy_file_to_dir_1005_16259()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16260) as chmod_and_chown_1006_16260:
                            chmod_and_chown_1006_16260()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=16261):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16262) as should_copy_source_1007_16262:
                    should_copy_source_1007_16262()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=16263):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=16264) as copy_file_to_dir_1008_16264:
                            copy_file_to_dir_1008_16264()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16265) as chmod_and_chown_1009_16265:
                            chmod_and_chown_1009_16265()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=16266):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16267) as should_copy_source_1010_16267:
                    should_copy_source_1010_16267()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=16268):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=16269) as copy_file_to_dir_1011_16269:
                            copy_file_to_dir_1011_16269()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16270) as chmod_and_chown_1012_16270:
                            chmod_and_chown_1012_16270()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=16271):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16272) as should_copy_source_1013_16272:
                    should_copy_source_1013_16272()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=16273):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=16274) as copy_file_to_dir_1014_16274:
                            copy_file_to_dir_1014_16274()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16275) as chmod_and_chown_1015_16275:
                            chmod_and_chown_1015_16275()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=16276):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16277) as should_copy_source_1016_16277:
                    should_copy_source_1016_16277()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=16278):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=16279) as copy_file_to_dir_1017_16279:
                            copy_file_to_dir_1017_16279()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16280) as chmod_and_chown_1018_16280:
                            chmod_and_chown_1018_16280()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=16281):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16282) as should_copy_source_1019_16282:
                    should_copy_source_1019_16282()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=16283):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=16284) as copy_file_to_dir_1020_16284:
                            copy_file_to_dir_1020_16284()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16285) as chmod_and_chown_1021_16285:
                            chmod_and_chown_1021_16285()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=16286):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16287) as should_copy_source_1022_16287:
                    should_copy_source_1022_16287()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=16288):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=16289) as copy_file_to_dir_1023_16289:
                            copy_file_to_dir_1023_16289()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16290) as chmod_and_chown_1024_16290:
                            chmod_and_chown_1024_16290()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=16291):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16292) as should_copy_source_1025_16292:
                    should_copy_source_1025_16292()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=16293):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=16294) as copy_file_to_dir_1026_16294:
                            copy_file_to_dir_1026_16294()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16295) as chmod_and_chown_1027_16295:
                            chmod_and_chown_1027_16295()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=16296):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16297) as should_copy_source_1028_16297:
                    should_copy_source_1028_16297()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=16298):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=16299) as copy_file_to_dir_1029_16299:
                            copy_file_to_dir_1029_16299()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16300) as chmod_and_chown_1030_16300:
                            chmod_and_chown_1030_16300()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=16301):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16302) as should_copy_source_1031_16302:
                    should_copy_source_1031_16302()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=16303):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=16304) as copy_file_to_dir_1032_16304:
                            copy_file_to_dir_1032_16304()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16305) as chmod_and_chown_1033_16305:
                            chmod_and_chown_1033_16305()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=16306):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16307) as should_copy_source_1034_16307:
                    should_copy_source_1034_16307()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=16308):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=16309) as copy_file_to_dir_1035_16309:
                            copy_file_to_dir_1035_16309()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16310) as chmod_and_chown_1036_16310:
                            chmod_and_chown_1036_16310()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=16311):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16312) as should_copy_source_1037_16312:
                    should_copy_source_1037_16312()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=16313):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=16314) as copy_file_to_dir_1038_16314:
                            copy_file_to_dir_1038_16314()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16315) as chmod_and_chown_1039_16315:
                            chmod_and_chown_1039_16315()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=16316):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16317) as should_copy_source_1040_16317:
                    should_copy_source_1040_16317()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=16318):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=16319) as copy_file_to_dir_1041_16319:
                            copy_file_to_dir_1041_16319()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16320) as chmod_and_chown_1042_16320:
                            chmod_and_chown_1042_16320()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=16321):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16322) as should_copy_source_1043_16322:
                    should_copy_source_1043_16322()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=16323):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=16324) as copy_file_to_dir_1044_16324:
                            copy_file_to_dir_1044_16324()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16325) as chmod_and_chown_1045_16325:
                            chmod_and_chown_1045_16325()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=16326):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16327) as should_copy_source_1046_16327:
                    should_copy_source_1046_16327()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=16328):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=16329) as copy_file_to_dir_1047_16329:
                            copy_file_to_dir_1047_16329()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16330) as chmod_and_chown_1048_16330:
                            chmod_and_chown_1048_16330()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=16331):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16332) as should_copy_source_1049_16332:
                    should_copy_source_1049_16332()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=16333):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=16334) as copy_file_to_dir_1050_16334:
                            copy_file_to_dir_1050_16334()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16335) as chmod_and_chown_1051_16335:
                            chmod_and_chown_1051_16335()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=16336):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16337) as should_copy_source_1052_16337:
                    should_copy_source_1052_16337()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=16338):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=16339) as copy_file_to_dir_1053_16339:
                            copy_file_to_dir_1053_16339()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16340) as chmod_and_chown_1054_16340:
                            chmod_and_chown_1054_16340()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=16341):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16342) as should_copy_source_1055_16342:
                    should_copy_source_1055_16342()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=16343):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=16344) as copy_file_to_dir_1056_16344:
                            copy_file_to_dir_1056_16344()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16345) as chmod_and_chown_1057_16345:
                            chmod_and_chown_1057_16345()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=16346):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16347) as should_copy_source_1058_16347:
                    should_copy_source_1058_16347()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=16348):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=16349) as copy_file_to_dir_1059_16349:
                            copy_file_to_dir_1059_16349()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16350) as chmod_and_chown_1060_16350:
                            chmod_and_chown_1060_16350()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=16351):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16352) as should_copy_source_1061_16352:
                    should_copy_source_1061_16352()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=16353):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=16354) as copy_file_to_dir_1062_16354:
                            copy_file_to_dir_1062_16354()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16355) as chmod_and_chown_1063_16355:
                            chmod_and_chown_1063_16355()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=16356):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16357) as should_copy_source_1064_16357:
                    should_copy_source_1064_16357()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=16358):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=16359) as copy_file_to_dir_1065_16359:
                            copy_file_to_dir_1065_16359()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16360) as chmod_and_chown_1066_16360:
                            chmod_and_chown_1066_16360()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=16361):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16362) as should_copy_source_1067_16362:
                    should_copy_source_1067_16362()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=16363):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=16364) as copy_file_to_dir_1068_16364:
                            copy_file_to_dir_1068_16364()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16365) as chmod_and_chown_1069_16365:
                            chmod_and_chown_1069_16365()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=16366):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16367) as should_copy_source_1070_16367:
                    should_copy_source_1070_16367()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=16368):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=16369) as copy_file_to_dir_1071_16369:
                            copy_file_to_dir_1071_16369()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16370) as chmod_and_chown_1072_16370:
                            chmod_and_chown_1072_16370()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=16371):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16372) as should_copy_source_1073_16372:
                    should_copy_source_1073_16372()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=16373):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=16374) as copy_file_to_dir_1074_16374:
                            copy_file_to_dir_1074_16374()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16375) as chmod_and_chown_1075_16375:
                            chmod_and_chown_1075_16375()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=16376):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16377) as should_copy_source_1076_16377:
                    should_copy_source_1076_16377()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=16378):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=16379) as copy_file_to_dir_1077_16379:
                            copy_file_to_dir_1077_16379()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16380) as chmod_and_chown_1078_16380:
                            chmod_and_chown_1078_16380()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=16381):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16382) as should_copy_source_1079_16382:
                    should_copy_source_1079_16382()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=16383):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=16384) as copy_file_to_dir_1080_16384:
                            copy_file_to_dir_1080_16384()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16385) as chmod_and_chown_1081_16385:
                            chmod_and_chown_1081_16385()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=16386):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16387) as should_copy_source_1082_16387:
                    should_copy_source_1082_16387()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=16388):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=16389) as copy_file_to_dir_1083_16389:
                            copy_file_to_dir_1083_16389()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16390) as chmod_and_chown_1084_16390:
                            chmod_and_chown_1084_16390()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=16391):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16392) as should_copy_source_1085_16392:
                    should_copy_source_1085_16392()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=16393):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=16394) as copy_file_to_dir_1086_16394:
                            copy_file_to_dir_1086_16394()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16395) as chmod_and_chown_1087_16395:
                            chmod_and_chown_1087_16395()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=16396):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16397) as should_copy_source_1088_16397:
                    should_copy_source_1088_16397()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=16398):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=16399) as copy_file_to_dir_1089_16399:
                            copy_file_to_dir_1089_16399()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16400) as chmod_and_chown_1090_16400:
                            chmod_and_chown_1090_16400()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=16401):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16402) as should_copy_source_1091_16402:
                    should_copy_source_1091_16402()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=16403):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=16404) as copy_file_to_dir_1092_16404:
                            copy_file_to_dir_1092_16404()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16405) as chmod_and_chown_1093_16405:
                            chmod_and_chown_1093_16405()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=16406):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16407) as should_copy_source_1094_16407:
                    should_copy_source_1094_16407()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=16408):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=16409) as copy_file_to_dir_1095_16409:
                            copy_file_to_dir_1095_16409()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16410) as chmod_and_chown_1096_16410:
                            chmod_and_chown_1096_16410()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=16411):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16412) as should_copy_source_1097_16412:
                    should_copy_source_1097_16412()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=16413):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=16414) as copy_file_to_dir_1098_16414:
                            copy_file_to_dir_1098_16414()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16415) as chmod_and_chown_1099_16415:
                            chmod_and_chown_1099_16415()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=16416):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16417) as should_copy_source_1100_16417:
                    should_copy_source_1100_16417()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=16418):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=16419) as copy_file_to_dir_1101_16419:
                            copy_file_to_dir_1101_16419()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16420) as chmod_and_chown_1102_16420:
                            chmod_and_chown_1102_16420()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=16421):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16422) as should_copy_source_1103_16422:
                    should_copy_source_1103_16422()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=16423):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=16424) as copy_file_to_dir_1104_16424:
                            copy_file_to_dir_1104_16424()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16425) as chmod_and_chown_1105_16425:
                            chmod_and_chown_1105_16425()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16426) as should_copy_source_1106_16426:
                    should_copy_source_1106_16426()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=16427):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=16428) as copy_file_to_dir_1107_16428:
                            copy_file_to_dir_1107_16428()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16429) as chmod_and_chown_1108_16429:
                            chmod_and_chown_1108_16429()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=16430):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16431) as should_copy_source_1109_16431:
                    should_copy_source_1109_16431()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=16432):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=16433) as copy_file_to_dir_1110_16433:
                            copy_file_to_dir_1110_16433()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16434) as chmod_and_chown_1111_16434:
                            chmod_and_chown_1111_16434()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=16435):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16436) as should_copy_source_1112_16436:
                    should_copy_source_1112_16436()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=16437):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=16438) as copy_file_to_dir_1113_16438:
                            copy_file_to_dir_1113_16438()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16439) as chmod_and_chown_1114_16439:
                            chmod_and_chown_1114_16439()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=16440):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16441) as should_copy_source_1115_16441:
                    should_copy_source_1115_16441()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=16442):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=16443) as copy_file_to_dir_1116_16443:
                            copy_file_to_dir_1116_16443()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16444) as chmod_and_chown_1117_16444:
                            chmod_and_chown_1117_16444()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=16445):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16446) as should_copy_source_1118_16446:
                    should_copy_source_1118_16446()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=16447):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=16448) as copy_file_to_dir_1119_16448:
                            copy_file_to_dir_1119_16448()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16449) as chmod_and_chown_1120_16449:
                            chmod_and_chown_1120_16449()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=16450):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16451) as should_copy_source_1121_16451:
                    should_copy_source_1121_16451()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=16452):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=16453) as copy_file_to_dir_1122_16453:
                            copy_file_to_dir_1122_16453()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16454) as chmod_and_chown_1123_16454:
                            chmod_and_chown_1123_16454()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=16455):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16456) as should_copy_source_1124_16456:
                    should_copy_source_1124_16456()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=16457):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=16458) as copy_file_to_dir_1125_16458:
                            copy_file_to_dir_1125_16458()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16459) as chmod_and_chown_1126_16459:
                            chmod_and_chown_1126_16459()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=16460):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16461) as should_copy_source_1127_16461:
                    should_copy_source_1127_16461()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=16462):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=16463) as copy_file_to_dir_1128_16463:
                            copy_file_to_dir_1128_16463()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16464) as chmod_and_chown_1129_16464:
                            chmod_and_chown_1129_16464()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=16465):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16466) as should_copy_source_1130_16466:
                    should_copy_source_1130_16466()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=16467):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=16468) as copy_file_to_dir_1131_16468:
                            copy_file_to_dir_1131_16468()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16469) as chmod_and_chown_1132_16469:
                            chmod_and_chown_1132_16469()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=16470):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16471) as should_copy_source_1133_16471:
                    should_copy_source_1133_16471()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=16472):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=16473) as copy_file_to_dir_1134_16473:
                            copy_file_to_dir_1134_16473()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16474) as chmod_and_chown_1135_16474:
                            chmod_and_chown_1135_16474()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=16475):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16476) as should_copy_source_1136_16476:
                    should_copy_source_1136_16476()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=16477):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=16478) as copy_file_to_dir_1137_16478:
                            copy_file_to_dir_1137_16478()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16479) as chmod_and_chown_1138_16479:
                            chmod_and_chown_1138_16479()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=16480):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16481) as should_copy_source_1139_16481:
                    should_copy_source_1139_16481()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=16482):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=16483) as copy_file_to_dir_1140_16483:
                            copy_file_to_dir_1140_16483()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16484) as chmod_and_chown_1141_16484:
                            chmod_and_chown_1141_16484()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=16485):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16486) as should_copy_source_1142_16486:
                    should_copy_source_1142_16486()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=16487):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=16488) as copy_file_to_dir_1143_16488:
                            copy_file_to_dir_1143_16488()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16489) as chmod_and_chown_1144_16489:
                            chmod_and_chown_1144_16489()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=16490):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16491) as should_copy_source_1145_16491:
                    should_copy_source_1145_16491()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=16492):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=16493) as copy_file_to_dir_1146_16493:
                            copy_file_to_dir_1146_16493()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16494) as chmod_and_chown_1147_16494:
                            chmod_and_chown_1147_16494()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=16495):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16496) as should_copy_source_1148_16496:
                    should_copy_source_1148_16496()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=16497):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=16498) as copy_file_to_dir_1149_16498:
                            copy_file_to_dir_1149_16498()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16499) as chmod_and_chown_1150_16499:
                            chmod_and_chown_1150_16499()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=16500):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16501) as should_copy_source_1151_16501:
                    should_copy_source_1151_16501()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=16502):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=16503) as copy_file_to_dir_1152_16503:
                            copy_file_to_dir_1152_16503()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16504) as chmod_and_chown_1153_16504:
                            chmod_and_chown_1153_16504()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=16505):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16506) as should_copy_source_1154_16506:
                    should_copy_source_1154_16506()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=16507):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=16508) as copy_file_to_dir_1155_16508:
                            copy_file_to_dir_1155_16508()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16509) as chmod_and_chown_1156_16509:
                            chmod_and_chown_1156_16509()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=16510):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16511) as should_copy_source_1157_16511:
                    should_copy_source_1157_16511()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=16512):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=16513) as copy_file_to_dir_1158_16513:
                            copy_file_to_dir_1158_16513()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16514) as chmod_and_chown_1159_16514:
                            chmod_and_chown_1159_16514()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=16515):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16516) as should_copy_source_1160_16516:
                    should_copy_source_1160_16516()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=16517):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=16518) as copy_file_to_dir_1161_16518:
                            copy_file_to_dir_1161_16518()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16519) as chmod_and_chown_1162_16519:
                            chmod_and_chown_1162_16519()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=16520):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16521) as should_copy_source_1163_16521:
                    should_copy_source_1163_16521()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=16522):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=16523) as copy_file_to_dir_1164_16523:
                            copy_file_to_dir_1164_16523()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16524) as chmod_and_chown_1165_16524:
                            chmod_and_chown_1165_16524()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=16525):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16526) as should_copy_source_1166_16526:
                    should_copy_source_1166_16526()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=16527):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=16528) as copy_file_to_dir_1167_16528:
                            copy_file_to_dir_1167_16528()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16529) as chmod_and_chown_1168_16529:
                            chmod_and_chown_1168_16529()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=16530):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16531) as should_copy_source_1169_16531:
                    should_copy_source_1169_16531()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=16532):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=16533) as copy_file_to_dir_1170_16533:
                            copy_file_to_dir_1170_16533()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16534) as chmod_and_chown_1171_16534:
                            chmod_and_chown_1171_16534()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=16535):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16536) as should_copy_source_1172_16536:
                    should_copy_source_1172_16536()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=16537):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=16538) as copy_file_to_dir_1173_16538:
                            copy_file_to_dir_1173_16538()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16539) as chmod_and_chown_1174_16539:
                            chmod_and_chown_1174_16539()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=16540):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16541) as should_copy_source_1175_16541:
                    should_copy_source_1175_16541()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=16542):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=16543) as copy_file_to_dir_1176_16543:
                            copy_file_to_dir_1176_16543()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16544) as chmod_and_chown_1177_16544:
                            chmod_and_chown_1177_16544()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=16545):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16546) as should_copy_source_1178_16546:
                    should_copy_source_1178_16546()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=16547):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=16548) as copy_file_to_dir_1179_16548:
                            copy_file_to_dir_1179_16548()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16549) as chmod_and_chown_1180_16549:
                            chmod_and_chown_1180_16549()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=16550):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16551) as should_copy_source_1181_16551:
                    should_copy_source_1181_16551()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=16552):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=16553) as copy_file_to_dir_1182_16553:
                            copy_file_to_dir_1182_16553()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16554) as chmod_and_chown_1183_16554:
                            chmod_and_chown_1183_16554()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=16555):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16556) as should_copy_source_1184_16556:
                    should_copy_source_1184_16556()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=16557):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=16558) as copy_file_to_dir_1185_16558:
                            copy_file_to_dir_1185_16558()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16559) as chmod_and_chown_1186_16559:
                            chmod_and_chown_1186_16559()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=16560):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16561) as should_copy_source_1187_16561:
                    should_copy_source_1187_16561()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=16562):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=16563) as copy_file_to_dir_1188_16563:
                            copy_file_to_dir_1188_16563()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16564) as chmod_and_chown_1189_16564:
                            chmod_and_chown_1189_16564()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=16565):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16566) as should_copy_source_1190_16566:
                    should_copy_source_1190_16566()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=16567):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=16568) as copy_file_to_dir_1191_16568:
                            copy_file_to_dir_1191_16568()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16569) as chmod_and_chown_1192_16569:
                            chmod_and_chown_1192_16569()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16570) as should_copy_source_1193_16570:
                    should_copy_source_1193_16570()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=16571):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=16572) as copy_file_to_dir_1194_16572:
                            copy_file_to_dir_1194_16572()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16573) as chmod_and_chown_1195_16573:
                            chmod_and_chown_1195_16573()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16574) as should_copy_source_1196_16574:
                    should_copy_source_1196_16574()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=16575):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=16576) as copy_file_to_dir_1197_16576:
                            copy_file_to_dir_1197_16576()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16577) as chmod_and_chown_1198_16577:
                            chmod_and_chown_1198_16577()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=16578):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16579) as should_copy_source_1199_16579:
                    should_copy_source_1199_16579()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=16580):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=16581) as copy_file_to_dir_1200_16581:
                            copy_file_to_dir_1200_16581()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16582) as chmod_and_chown_1201_16582:
                            chmod_and_chown_1201_16582()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=16583):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16584) as should_copy_source_1202_16584:
                    should_copy_source_1202_16584()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=16585):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=16586) as copy_file_to_dir_1203_16586:
                            copy_file_to_dir_1203_16586()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16587) as chmod_and_chown_1204_16587:
                            chmod_and_chown_1204_16587()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=16588):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16589) as should_copy_source_1205_16589:
                    should_copy_source_1205_16589()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=16590):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=16591) as copy_file_to_dir_1206_16591:
                            copy_file_to_dir_1206_16591()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16592) as chmod_and_chown_1207_16592:
                            chmod_and_chown_1207_16592()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=16593):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16594) as should_copy_source_1208_16594:
                    should_copy_source_1208_16594()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=16595):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=16596) as copy_file_to_dir_1209_16596:
                            copy_file_to_dir_1209_16596()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16597) as chmod_and_chown_1210_16597:
                            chmod_and_chown_1210_16597()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=16598):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16599) as should_copy_source_1211_16599:
                    should_copy_source_1211_16599()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=16600):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=16601) as copy_file_to_dir_1212_16601:
                            copy_file_to_dir_1212_16601()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16602) as chmod_and_chown_1213_16602:
                            chmod_and_chown_1213_16602()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=16603):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16604) as should_copy_source_1214_16604:
                    should_copy_source_1214_16604()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=16605):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=16606) as copy_file_to_dir_1215_16606:
                            copy_file_to_dir_1215_16606()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16607) as chmod_and_chown_1216_16607:
                            chmod_and_chown_1216_16607()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=16608):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16609) as should_copy_source_1217_16609:
                    should_copy_source_1217_16609()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=16610):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=16611) as copy_file_to_dir_1218_16611:
                            copy_file_to_dir_1218_16611()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16612) as chmod_and_chown_1219_16612:
                            chmod_and_chown_1219_16612()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=16613):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=16614) as should_copy_source_1220_16614:
                    should_copy_source_1220_16614()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=16615):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=16616) as copy_file_to_dir_1221_16616:
                            copy_file_to_dir_1221_16616()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=16617) as chmod_and_chown_1222_16617:
                            chmod_and_chown_1222_16617()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=16618) as resolve_config_vars_in_file_1223_16618:
                resolve_config_vars_in_file_1223_16618()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=16619) as if_1224_16619:
                if_1224_16619()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=16620) as resolve_config_vars_in_file_1225_16620:
                resolve_config_vars_in_file_1225_16620()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=16621) as if_1226_16621:
                if_1226_16621()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=16622) as resolve_config_vars_in_file_1227_16622:
                resolve_config_vars_in_file_1227_16622()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=16623) as if_1228_16623:
                if_1228_16623()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=16624) as resolve_config_vars_in_file_1229_16624:
                resolve_config_vars_in_file_1229_16624()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=16625) as if_1230_16625:
                if_1230_16625()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=16626) as resolve_config_vars_in_file_1231_16626:
                resolve_config_vars_in_file_1231_16626()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=16627) as if_1232_16627:
                if_1232_16627()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=16628) as resolve_config_vars_in_file_1233_16628:
                resolve_config_vars_in_file_1233_16628()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=16629) as if_1234_16629:
                if_1234_16629()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=16630) as resolve_config_vars_in_file_1235_16630:
                resolve_config_vars_in_file_1235_16630()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=16631) as if_1236_16631:
                if_1236_16631()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=16632) as resolve_config_vars_in_file_1237_16632:
                resolve_config_vars_in_file_1237_16632()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=16633) as if_1238_16633:
                if_1238_16633()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=16634) as resolve_config_vars_in_file_1239_16634:
                resolve_config_vars_in_file_1239_16634()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=16635) as if_1240_16635:
                if_1240_16635()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=16636) as resolve_config_vars_in_file_1241_16636:
                resolve_config_vars_in_file_1241_16636()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=16637) as if_1242_16637:
                if_1242_16637()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=16638) as resolve_config_vars_in_file_1243_16638:
                resolve_config_vars_in_file_1243_16638()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=16639) as if_1244_16639:
                if_1244_16639()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=16640) as resolve_config_vars_in_file_1245_16640:
                resolve_config_vars_in_file_1245_16640()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=16641) as if_1246_16641:
                if_1246_16641()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=16642) as resolve_config_vars_in_file_1247_16642:
                resolve_config_vars_in_file_1247_16642()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=16643) as if_1248_16643:
                if_1248_16643()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=16644) as resolve_config_vars_in_file_1249_16644:
                resolve_config_vars_in_file_1249_16644()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=16645) as if_1250_16645:
                if_1250_16645()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=16646) as resolve_config_vars_in_file_1251_16646:
                resolve_config_vars_in_file_1251_16646()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=16647) as if_1252_16647:
                if_1252_16647()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=16648) as resolve_config_vars_in_file_1253_16648:
                resolve_config_vars_in_file_1253_16648()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=16649) as if_1254_16649:
                if_1254_16649()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=16650) as resolve_config_vars_in_file_1255_16650:
                resolve_config_vars_in_file_1255_16650()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=16651) as if_1256_16651:
                if_1256_16651()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=16652) as resolve_config_vars_in_file_1257_16652:
                resolve_config_vars_in_file_1257_16652()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=16653) as if_1258_16653:
                if_1258_16653()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=16654) as resolve_config_vars_in_file_1259_16654:
                resolve_config_vars_in_file_1259_16654()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=16655) as if_1260_16655:
                if_1260_16655()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=16656) as resolve_config_vars_in_file_1261_16656:
                resolve_config_vars_in_file_1261_16656()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=16657) as if_1262_16657:
                if_1262_16657()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=16658) as resolve_config_vars_in_file_1263_16658:
                resolve_config_vars_in_file_1263_16658()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=16659) as if_1264_16659:
                if_1264_16659()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=16660) as resolve_config_vars_in_file_1265_16660:
                resolve_config_vars_in_file_1265_16660()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=16661) as if_1266_16661:
                if_1266_16661()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=16662) as resolve_config_vars_in_file_1267_16662:
                resolve_config_vars_in_file_1267_16662()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=16663) as if_1268_16663:
                if_1268_16663()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=16664) as resolve_config_vars_in_file_1269_16664:
                resolve_config_vars_in_file_1269_16664()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=16665) as if_1270_16665:
                if_1270_16665()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=16666) as rm_file_or_dir_1271_16666:
                rm_file_or_dir_1271_16666()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=16667) as resolve_config_vars_in_file_1272_16667:
                resolve_config_vars_in_file_1272_16667()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=16668) as if_1273_16668:
                if_1273_16668()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=16669) as rm_file_or_dir_1274_16669:
                rm_file_or_dir_1274_16669()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=16670) as resolve_config_vars_in_file_1275_16670:
                resolve_config_vars_in_file_1275_16670()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=16671) as if_1276_16671:
                if_1276_16671()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=16672) as resolve_config_vars_in_file_1277_16672:
                resolve_config_vars_in_file_1277_16672()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=16673) as if_1278_16673:
                if_1278_16673()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=16674) as resolve_config_vars_in_file_1279_16674:
                resolve_config_vars_in_file_1279_16674()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=16675) as if_1280_16675:
                if_1280_16675()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=16676) as resolve_config_vars_in_file_1281_16676:
                resolve_config_vars_in_file_1281_16676()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=16677) as if_1282_16677:
                if_1282_16677()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=16678) as resolve_config_vars_in_file_1283_16678:
                resolve_config_vars_in_file_1283_16678()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=16679) as if_1284_16679:
                if_1284_16679()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=16680) as resolve_config_vars_in_file_1285_16680:
                resolve_config_vars_in_file_1285_16680()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=16681) as if_1286_16681:
                if_1286_16681()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=16682) as resolve_config_vars_in_file_1287_16682:
                resolve_config_vars_in_file_1287_16682()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=16683) as if_1288_16683:
                if_1288_16683()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=16684) as resolve_config_vars_in_file_1289_16684:
                resolve_config_vars_in_file_1289_16684()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=16685) as if_1290_16685:
                if_1290_16685()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=16686) as resolve_config_vars_in_file_1291_16686:
                resolve_config_vars_in_file_1291_16686()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=16687) as if_1292_16687:
                if_1292_16687()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=16688) as resolve_config_vars_in_file_1293_16688:
                resolve_config_vars_in_file_1293_16688()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=16689) as if_1294_16689:
                if_1294_16689()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=16690) as resolve_config_vars_in_file_1295_16690:
                resolve_config_vars_in_file_1295_16690()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=16691) as if_1296_16691:
                if_1296_16691()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=16692) as resolve_config_vars_in_file_1297_16692:
                resolve_config_vars_in_file_1297_16692()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=16693) as if_1298_16693:
                if_1298_16693()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=16694) as resolve_config_vars_in_file_1299_16694:
                resolve_config_vars_in_file_1299_16694()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=16695) as if_1300_16695:
                if_1300_16695()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=16696) as resolve_config_vars_in_file_1301_16696:
                resolve_config_vars_in_file_1301_16696()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=16697) as if_1302_16697:
                if_1302_16697()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=16698) as resolve_config_vars_in_file_1303_16698:
                resolve_config_vars_in_file_1303_16698()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=16699) as if_1304_16699:
                if_1304_16699()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=16700) as resolve_config_vars_in_file_1305_16700:
                resolve_config_vars_in_file_1305_16700()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=16701) as if_1306_16701:
                if_1306_16701()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=16702) as resolve_config_vars_in_file_1307_16702:
                resolve_config_vars_in_file_1307_16702()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=16703) as if_1308_16703:
                if_1308_16703()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=16704) as resolve_config_vars_in_file_1309_16704:
                resolve_config_vars_in_file_1309_16704()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=16705) as if_1310_16705:
                if_1310_16705()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=16706) as resolve_config_vars_in_file_1311_16706:
                resolve_config_vars_in_file_1311_16706()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=16707) as if_1312_16707:
                if_1312_16707()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=16708) as resolve_config_vars_in_file_1313_16708:
                resolve_config_vars_in_file_1313_16708()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=16709) as if_1314_16709:
                if_1314_16709()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=16710) as resolve_config_vars_in_file_1315_16710:
                resolve_config_vars_in_file_1315_16710()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=16711) as if_1316_16711:
                if_1316_16711()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=16712) as resolve_config_vars_in_file_1317_16712:
                resolve_config_vars_in_file_1317_16712()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=16713) as if_1318_16713:
                if_1318_16713()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=16714) as resolve_config_vars_in_file_1319_16714:
                resolve_config_vars_in_file_1319_16714()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=16715) as if_1320_16715:
                if_1320_16715()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=16716) as move_file_to_file_1321_16716:
                move_file_to_file_1321_16716()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=16717) as resolve_config_vars_in_file_1322_16717:
                resolve_config_vars_in_file_1322_16717()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=16718) as if_1323_16718:
                if_1323_16718()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=16719) as resolve_config_vars_in_file_1324_16719:
                resolve_config_vars_in_file_1324_16719()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=16720) as if_1325_16720:
                if_1325_16720()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=16721) as resolve_config_vars_in_file_1326_16721:
                resolve_config_vars_in_file_1326_16721()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=16722) as if_1327_16722:
                if_1327_16722()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=16723) as resolve_config_vars_in_file_1328_16723:
                resolve_config_vars_in_file_1328_16723()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=16724) as if_1329_16724:
                if_1329_16724()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=16725) as resolve_config_vars_in_file_1330_16725:
                resolve_config_vars_in_file_1330_16725()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=16726) as if_1331_16726:
                if_1331_16726()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=16727) as resolve_config_vars_in_file_1332_16727:
                resolve_config_vars_in_file_1332_16727()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=16728) as if_1333_16728:
                if_1333_16728()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=16729) as resolve_config_vars_in_file_1334_16729:
                resolve_config_vars_in_file_1334_16729()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=16730) as if_1335_16730:
                if_1335_16730()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=16731) as resolve_config_vars_in_file_1336_16731:
                resolve_config_vars_in_file_1336_16731()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=16732) as if_1337_16732:
                if_1337_16732()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=16733) as resolve_config_vars_in_file_1338_16733:
                resolve_config_vars_in_file_1338_16733()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=16734) as if_1339_16734:
                if_1339_16734()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=16735) as resolve_config_vars_in_file_1340_16735:
                resolve_config_vars_in_file_1340_16735()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=16736) as if_1341_16736:
                if_1341_16736()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=16737) as resolve_config_vars_in_file_1342_16737:
                resolve_config_vars_in_file_1342_16737()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=16738) as if_1343_16738:
                if_1343_16738()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=16739) as resolve_config_vars_in_file_1344_16739:
                resolve_config_vars_in_file_1344_16739()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=16740) as if_1345_16740:
                if_1345_16740()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=16741) as resolve_config_vars_in_file_1346_16741:
                resolve_config_vars_in_file_1346_16741()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=16742) as if_1347_16742:
                if_1347_16742()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=16743) as resolve_config_vars_in_file_1348_16743:
                resolve_config_vars_in_file_1348_16743()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=16744) as if_1349_16744:
                if_1349_16744()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=16745) as resolve_config_vars_in_file_1350_16745:
                resolve_config_vars_in_file_1350_16745()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=16746) as if_1351_16746:
                if_1351_16746()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=16747) as resolve_config_vars_in_file_1352_16747:
                resolve_config_vars_in_file_1352_16747()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=16748) as if_1353_16748:
                if_1353_16748()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=16749) as resolve_config_vars_in_file_1354_16749:
                resolve_config_vars_in_file_1354_16749()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=16750) as if_1355_16750:
                if_1355_16750()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=16751) as resolve_config_vars_in_file_1356_16751:
                resolve_config_vars_in_file_1356_16751()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=16752) as if_1357_16752:
                if_1357_16752()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=16753) as resolve_config_vars_in_file_1358_16753:
                resolve_config_vars_in_file_1358_16753()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=16754) as if_1359_16754:
                if_1359_16754()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=16755) as resolve_config_vars_in_file_1360_16755:
                resolve_config_vars_in_file_1360_16755()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=16756) as if_1361_16756:
                if_1361_16756()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=16757) as resolve_config_vars_in_file_1362_16757:
                resolve_config_vars_in_file_1362_16757()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=16758) as if_1363_16758:
                if_1363_16758()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=16759) as resolve_config_vars_in_file_1364_16759:
                resolve_config_vars_in_file_1364_16759()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=16760) as if_1365_16760:
                if_1365_16760()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=16761) as resolve_config_vars_in_file_1366_16761:
                resolve_config_vars_in_file_1366_16761()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=16762) as if_1367_16762:
                if_1367_16762()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=16763) as resolve_config_vars_in_file_1368_16763:
                resolve_config_vars_in_file_1368_16763()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=16764) as if_1369_16764:
                if_1369_16764()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=16765) as resolve_config_vars_in_file_1370_16765:
                resolve_config_vars_in_file_1370_16765()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=16766) as if_1371_16766:
                if_1371_16766()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=16767) as resolve_config_vars_in_file_1372_16767:
                resolve_config_vars_in_file_1372_16767()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=16768) as if_1373_16768:
                if_1373_16768()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=16769) as resolve_config_vars_in_file_1374_16769:
                resolve_config_vars_in_file_1374_16769()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=16770) as if_1375_16770:
                if_1375_16770()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=16771) as resolve_config_vars_in_file_1376_16771:
                resolve_config_vars_in_file_1376_16771()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=16772) as if_1377_16772:
                if_1377_16772()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=16773) as rm_file_or_dir_1378_16773:
                rm_file_or_dir_1378_16773()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=16774) as rm_file_or_dir_1379_16774:
                rm_file_or_dir_1379_16774()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=16775) as rm_file_or_dir_1380_16775:
                rm_file_or_dir_1380_16775()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=16776) as resolve_config_vars_in_file_1381_16776:
                resolve_config_vars_in_file_1381_16776()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=16777) as if_1382_16777:
                if_1382_16777()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=16778) as resolve_config_vars_in_file_1383_16778:
                resolve_config_vars_in_file_1383_16778()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=16779) as if_1384_16779:
                if_1384_16779()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=16780) as resolve_config_vars_in_file_1385_16780:
                resolve_config_vars_in_file_1385_16780()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=16781) as if_1386_16781:
                if_1386_16781()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=16782) as rm_file_or_dir_1387_16782:
                rm_file_or_dir_1387_16782()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=16783) as rm_file_or_dir_1388_16783:
                rm_file_or_dir_1388_16783()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=16784) as rm_file_or_dir_1389_16784:
                rm_file_or_dir_1389_16784()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=16785) as resolve_config_vars_in_file_1390_16785:
                resolve_config_vars_in_file_1390_16785()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=16786) as if_1391_16786:
                if_1391_16786()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=16787) as resolve_config_vars_in_file_1392_16787:
                resolve_config_vars_in_file_1392_16787()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=16788) as if_1393_16788:
                if_1393_16788()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=16789) as resolve_config_vars_in_file_1394_16789:
                resolve_config_vars_in_file_1394_16789()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=16790) as if_1395_16790:
                if_1395_16790()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=16791) as resolve_config_vars_in_file_1396_16791:
                resolve_config_vars_in_file_1396_16791()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=16792) as if_1397_16792:
                if_1397_16792()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=16793) as resolve_config_vars_in_file_1398_16793:
                resolve_config_vars_in_file_1398_16793()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=16794) as if_1399_16794:
                if_1399_16794()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=16795) as resolve_config_vars_in_file_1400_16795:
                resolve_config_vars_in_file_1400_16795()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=16796) as if_1401_16796:
                if_1401_16796()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=16797) as resolve_config_vars_in_file_1402_16797:
                resolve_config_vars_in_file_1402_16797()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=16798) as if_1403_16798:
                if_1403_16798()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=16799) as resolve_config_vars_in_file_1404_16799:
                resolve_config_vars_in_file_1404_16799()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=16800) as if_1405_16800:
                if_1405_16800()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=16801) as cd_stage_1406_16801:
            cd_stage_1406_16801()
            with Stage(r"copy", r"COSMOS_HTML v2.6.6", prog_num=16802):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=16803) as should_copy_source_1407_16803:
                    should_copy_source_1407_16803()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=16804):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=16805) as copy_dir_to_dir_1408_16805:
                            copy_dir_to_dir_1408_16805()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=16806, recursive=True) as chown_1409_16806:
                            chown_1409_16806()
            with Stage(r"copy", r"COSMOS_python v2.7.7", prog_num=16807):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=16808) as should_copy_source_1410_16808:
                    should_copy_source_1410_16808()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=16809):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=16810) as copy_dir_to_dir_1411_16810:
                            copy_dir_to_dir_1411_16810()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=16811) as unwtar_1412_16811:
                            unwtar_1412_16811()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=16812, recursive=True) as chown_1413_16812:
                            chown_1413_16812()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=16813) as cd_stage_1414_16813:
            cd_stage_1414_16813()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=16814):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=16815) as should_copy_source_1415_16815:
                    should_copy_source_1415_16815()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=16816):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=16817) as copy_dir_to_dir_1416_16817:
                            copy_dir_to_dir_1416_16817()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=16818) as unwtar_1417_16818:
                            unwtar_1417_16818()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=16819, recursive=True) as chown_1418_16819:
                            chown_1418_16819()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=16820) as cd_stage_1419_16820:
            cd_stage_1419_16820()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=16821):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=16822) as should_copy_source_1420_16822:
                    should_copy_source_1420_16822()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=16823):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=16824) as copy_dir_to_dir_1421_16824:
                            copy_dir_to_dir_1421_16824()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=16825, recursive=True) as chown_1422_16825:
                            chown_1422_16825()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=16826) as cd_stage_1423_16826:
            cd_stage_1423_16826()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=16827):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=16828) as should_copy_source_1424_16828:
                    should_copy_source_1424_16828()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=16829):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=16830) as copy_dir_to_dir_1425_16830:
                            copy_dir_to_dir_1425_16830()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=16831, recursive=True) as chown_1426_16831:
                            chown_1426_16831()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=16832) as cd_stage_1427_16832:
            cd_stage_1427_16832()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=16833):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=16834) as should_copy_source_1428_16834:
                    should_copy_source_1428_16834()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=16835):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=16836) as copy_dir_to_dir_1429_16836:
                            copy_dir_to_dir_1429_16836()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=16837, recursive=True) as chown_1430_16837:
                            chown_1430_16837()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=16838) as cd_stage_1431_16838:
            cd_stage_1431_16838()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=16839) as rm_file_or_dir_1432_16839:
                rm_file_or_dir_1432_16839()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=16840):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=16841) as should_copy_source_1433_16841:
                    should_copy_source_1433_16841()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=16842):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=16843) as copy_dir_to_dir_1434_16843:
                            copy_dir_to_dir_1434_16843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=16844) as unwtar_1435_16844:
                            unwtar_1435_16844()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=16845, recursive=True) as chown_1436_16845:
                            chown_1436_16845()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=16846):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=16847) as should_copy_source_1437_16847:
                    should_copy_source_1437_16847()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=16848):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=16849) as unwtar_1438_16849:
                            unwtar_1438_16849()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=16850):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=16851) as should_copy_source_1439_16851:
                    should_copy_source_1439_16851()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=16852):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=16853) as copy_dir_to_dir_1440_16853:
                            copy_dir_to_dir_1440_16853()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=16854) as unwtar_1441_16854:
                            unwtar_1441_16854()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=16855, recursive=True) as chown_1442_16855:
                            chown_1442_16855()
            with Stage(r"copy", r"onnxruntime_1.19.0 v1.19.0", prog_num=16856):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=16857) as should_copy_source_1443_16857:
                    should_copy_source_1443_16857()
                    with Stage(r"copy source", r"Mac/Modules/onnxruntime", prog_num=16858):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r".", delete_extraneous_files=True, prog_num=16859) as copy_dir_to_dir_1444_16859:
                            copy_dir_to_dir_1444_16859()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", where_to_unwtar=r".", prog_num=16860) as unwtar_1445_16860:
                            unwtar_1445_16860()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/onnxruntime", user_id=-1, group_id=-1, prog_num=16861, recursive=True) as chown_1446_16861:
                            chown_1446_16861()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=16862):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=16863) as should_copy_source_1447_16863:
                    should_copy_source_1447_16863()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=16864):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=16865) as copy_dir_to_dir_1448_16865:
                            copy_dir_to_dir_1448_16865()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=16866) as chmod_1449_16866:
                            chmod_1449_16866()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=16867) as chmod_1450_16867:
                            chmod_1450_16867()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=16868, recursive=True) as chown_1451_16868:
                            chown_1451_16868()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=16871) as resolve_symlink_files_in_folder_1452_16871:
                resolve_symlink_files_in_folder_1452_16871()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=16872) as shell_command_1453_16872:
                shell_command_1453_16872()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=16873) as cd_stage_1454_16873:
            cd_stage_1454_16873()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=16874):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=16875) as should_copy_source_1455_16875:
                    should_copy_source_1455_16875()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=16876):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=16877) as copy_dir_to_dir_1456_16877:
                            copy_dir_to_dir_1456_16877()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=16878, recursive=True) as chown_1457_16878:
                            chown_1457_16878()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=16879) as cd_stage_1458_16879:
            cd_stage_1458_16879()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=16880):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=16881) as should_copy_source_1459_16881:
                    should_copy_source_1459_16881()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=16882):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=16883) as copy_dir_to_dir_1460_16883:
                            copy_dir_to_dir_1460_16883()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=16884, recursive=True) as chown_1461_16884:
                            chown_1461_16884()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=16885) as cd_stage_1462_16885:
            cd_stage_1462_16885()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=16886):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=16887) as should_copy_source_1463_16887:
                    should_copy_source_1463_16887()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=16888):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=16889, recursive=True) as chmod_1464_16889:
                            chmod_1464_16889()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=16890) as copy_dir_to_dir_1465_16890:
                            copy_dir_to_dir_1465_16890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=16891) as unwtar_1466_16891:
                            unwtar_1466_16891()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=16892, recursive=True) as chown_1467_16892:
                            chown_1467_16892()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=16893) as if_1468_16893:
                            if_1468_16893()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=16894) as cd_stage_1469_16894:
            cd_stage_1469_16894()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=16895):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=16896) as should_copy_source_1470_16896:
                    should_copy_source_1470_16896()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=16897):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=16898, recursive=True) as chmod_1471_16898:
                            chmod_1471_16898()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=16899) as copy_dir_to_dir_1472_16899:
                            copy_dir_to_dir_1472_16899()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=16900) as unwtar_1473_16900:
                            unwtar_1473_16900()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=16901, recursive=True) as chown_1474_16901:
                            chown_1474_16901()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250728102636-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=16902) as if_1475_16902:
                            if_1475_16902()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=16903) as cd_stage_1476_16903:
            cd_stage_1476_16903()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=16904):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=16905) as should_copy_source_1477_16905:
                    should_copy_source_1477_16905()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=16906):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=16907) as copy_dir_to_dir_1478_16907:
                            copy_dir_to_dir_1478_16907()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=16908) as unwtar_1479_16908:
                            unwtar_1479_16908()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=16909, recursive=True) as chown_1480_16909:
                            chown_1480_16909()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=16910) as break_hard_link_1481_16910:
                            break_hard_link_1481_16910()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=16911) as shell_command_1482_16911:
                            shell_command_1482_16911()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=16912, recursive=True) as chown_1483_16912:
                            chown_1483_16912()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=16913, recursive=True) as chmod_1484_16913:
                            chmod_1484_16913()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=16914) as cd_stage_1485_16914:
            cd_stage_1485_16914()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=16915):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=16916) as should_copy_source_1486_16916:
                    should_copy_source_1486_16916()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=16917):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=16918) as copy_dir_to_dir_1487_16918:
                            copy_dir_to_dir_1487_16918()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=16919) as unwtar_1488_16919:
                            unwtar_1488_16919()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=16920, recursive=True) as chown_1489_16920:
                            chown_1489_16920()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=16921) as shell_command_1490_16921:
                            shell_command_1490_16921()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=16922) as cd_stage_1491_16922:
            cd_stage_1491_16922()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=16923):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=16924) as should_copy_source_1492_16924:
                    should_copy_source_1492_16924()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=16925):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=16926) as copy_dir_to_dir_1493_16926:
                            copy_dir_to_dir_1493_16926()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=16927) as unwtar_1494_16927:
                            unwtar_1494_16927()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=16928, recursive=True) as chown_1495_16928:
                            chown_1495_16928()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=16929) as shell_command_1496_16929:
                            shell_command_1496_16929()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=16930) as script_command_1497_16930:
                            script_command_1497_16930()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=16931) as shell_command_1498_16931:
                            shell_command_1498_16931()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=16932) as create_symlink_1499_16932:
                create_symlink_1499_16932()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=16933) as create_symlink_1500_16933:
                create_symlink_1500_16933()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=16934) as cd_stage_1501_16934:
            cd_stage_1501_16934()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=16935) as rm_file_or_dir_1502_16935:
                rm_file_or_dir_1502_16935()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=16936) as cd_stage_1503_16936:
            cd_stage_1503_16936()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=16937) as rm_file_or_dir_1504_16937:
                rm_file_or_dir_1504_16937()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=16938) as rm_file_or_dir_1505_16938:
                rm_file_or_dir_1505_16938()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=16939) as rm_file_or_dir_1506_16939:
                rm_file_or_dir_1506_16939()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=16940) as shell_command_1507_16940:
            shell_command_1507_16940()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=16941) as shell_command_1508_16941:
            shell_command_1508_16941()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=16942) as script_command_1509_16942:
            script_command_1509_16942()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=16943) as rm_file_or_dir_1510_16943:
            rm_file_or_dir_1510_16943()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16944) as move_dir_to_dir_1511_16944:
            move_dir_to_dir_1511_16944()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16945) as move_dir_to_dir_1512_16945:
            move_dir_to_dir_1512_16945()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16946) as move_dir_to_dir_1513_16946:
            move_dir_to_dir_1513_16946()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16947) as move_dir_to_dir_1514_16947:
            move_dir_to_dir_1514_16947()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=16948) as make_dirs_1515_16948:
            make_dirs_1515_16948()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16949) as move_dir_to_dir_1516_16949:
            move_dir_to_dir_1516_16949()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=16950) as move_dir_to_dir_1517_16950:
            move_dir_to_dir_1517_16950()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=16951) as shell_command_1518_16951:
            shell_command_1518_16951()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=16952) as script_command_1519_16952:
            script_command_1519_16952()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=16953) as rm_file_or_dir_1520_16953:
            rm_file_or_dir_1520_16953()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=16954) as glober_1521_16954:
            glober_1521_16954()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=16955) as glober_1522_16955:
            glober_1522_16955()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=16956) as glober_1523_16956:
            glober_1523_16956()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=16957) as shell_command_1524_16957:
            shell_command_1524_16957()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=16958) as shell_command_1525_16958:
            shell_command_1525_16958()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=16959) as shell_command_1526_16959:
            shell_command_1526_16959()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=16960) as shell_command_1527_16960:
            shell_command_1527_16960()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=16961) as shell_command_1528_16961:
            shell_command_1528_16961()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=16962) as script_command_1529_16962:
            script_command_1529_16962()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=16963) as if_1530_16963:
            if_1530_16963()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=16964) as if_1531_16964:
            if_1531_16964()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=16965) as if_1532_16965:
            if_1532_16965()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=16966) as if_1533_16966:
            if_1533_16966()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=16967) as make_dir_1534_16967:
            make_dir_1534_16967()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=16968) as chmod_1535_16968:
            chmod_1535_16968()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=16969) as make_dir_1536_16969:
            make_dir_1536_16969()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=16970) as chmod_1537_16970:
            chmod_1537_16970()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=16971) as chmod_1538_16971:
            chmod_1538_16971()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=16972) as chmod_1539_16972:
            chmod_1539_16972()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=16973) as chmod_1540_16973:
            chmod_1540_16973()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=16974) as shell_command_1541_16974:
            shell_command_1541_16974()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=16975) as script_command_1542_16975:
            script_command_1542_16975()
    with Stage(r"post-copy", prog_num=16976):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=16977) as make_dir_1543_16977:
            make_dir_1543_16977()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=16978) as copy_file_to_file_1544_16978:
            copy_file_to_file_1544_16978()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=16979) as chmod_1545_16979:
            chmod_1545_16979()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=16980) as chmod_1546_16980:
            chmod_1546_16980()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=16981) as copy_file_to_file_1547_16981:
            copy_file_to_file_1547_16981()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=16982) as chmod_1548_16982:
            chmod_1548_16982()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=16983) as copy_file_to_file_1549_16983:
            copy_file_to_file_1549_16983()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=16984) as chmod_1550_16984:
            chmod_1550_16984()
        Progress(r"Done copy", prog_num=16985)()
        Progress(r"Done synccopy", prog_num=16986)()
    with Stage(r"post", prog_num=16987):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=16988) as make_dir_1551_16988:
            make_dir_1551_16988()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=16989) as copy_file_to_file_1552_16989:
            copy_file_to_file_1552_16989()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=16990) as make_dir_1553_16990:
            make_dir_1553_16990()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=16991) as copy_file_to_file_1554_16991:
            copy_file_to_file_1554_16991()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=16992) as make_dir_1555_16992:
            make_dir_1555_16992()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/9/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=16993) as copy_file_to_file_1556_16993:
            copy_file_to_file_1556_16993()

with Stage(r"epilog", prog_num=16994):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250728102636.py", prog_num=16995) as patch_py_batch_with_timings_1557_16995:
        patch_py_batch_with_timings_1557_16995()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


