# Creation time: 15-06-25_16-25
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 13579
PythonBatchCommandBase.running_progress = 1221
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1222):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250615162416"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX")
    config_vars['AUXILIARY_IIDS'] = (r"UNINSTALL_AS_APPLICATION", r"UNINSTALL_AS_PLUGIN")
    config_vars['AVOID_COPY_MARKERS'] = (r"Info.xml", r"Info.plist")
    config_vars['BASE_LINKS_URL'] = r"https://d36wza55md4dee.cloudfront.net"
    config_vars['BASE_REPO_REV'] = 1
    config_vars['BATCH_EXT'] = r"py"
    config_vars['CENTRAL_VERSION'] = r"15.5.5"
    config_vars['CHECK_BINARIES_VERSION_FILE_EXCLUDE_REGEX'] = (r"\.DS_Store", r"Icon")
    config_vars['CHECK_BINARIES_VERSION_FOLDERS'] = (r"/Applications/Waves/Applications V15", r"/Applications/Waves/Applications V10", r"/Applications/Waves/Applications V11", r"/Applications/Waves/Applications V12", r"/Applications/Waves/Applications V13", r"/Applications/Waves/Applications V14", r"/Applications/Waves/eMotion LV1", r"/Library/Application Support/Waves/Modules", r"/Applications/Waves/MultiRack", r"/Applications/Waves/MultiRack for Kramer", r"/Applications/Waves/Plug-Ins V15", r"/Applications/Waves/WaveShells V15", r"/Applications/Waves/WaveShells V10", r"/Applications/Waves/WaveShells V11", r"/Applications/Waves/WaveShells V12", r"/Applications/Waves/WaveShells V13", r"/Applications/Waves/WaveShells V14", r"/Applications/Waves/SoundGrid", r"/Library/Application Support/Waves/SoundGrid Firmware", r"/Library/Application Support/Waves/SoundGrid IO Modules", r"/Applications/Waves/SoundGrid Studio", r"/Applications/Waves/SuperRack Performer", r"/Library/Application Support/Waves/MyMon", r"/Library/Application Support/Waves/RemoteServices")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX'] = (r"(eMotion LV1|SoundGrid Studio|MultiRack|MultiRack for Kramer|SoundGrid|SoundGrid for Venue|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS'] = (r"(eMotion LV1|MultiRack|MultiRack for Kramer|SoundGrid|SuperRack).(Modules|Documents)", r"Session Templates", r"\.app/Contents", r"WavesQtLibs")
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 59
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NTA1Nn0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NzU2fX19XX0_;CloudFront-Signature=JkhiBwwGY4QW8-2GttlMdWx0JJ0GJqOTNxFufVWppasIBanqFZH-kLOs33-O12EqTbNhQ7pFAtmkeKB9ToW3AUHj4b35lSL4JHKVD38oueZpTP9SPsT6dPipODJ4GQulnX-R4FAYXzmikrjkXbU6ZukJ6mD4jujt6HmxN1HXXiJMRvMkSRoCLxUVeFxt9s4WyuB0BB0GqHRp7bGUvphXBgZg23FGHPgs3Rcg~kB2LiHukuBUvEP47os6PUGKfJqUqr4fKsuJFf~hL7syE9vqfuQj7afubRPu5quaORceIEfK-E8fnke6feEJs9KPDXXIACF7Q63b7LooxG-TxGruOg__"
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
    config_vars['INDEX_CHECKSUM'] = r"f92abdecad4a6427c158f4ca0302ab5be6a6de94"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"085814c5e8648b4cf8579f15da7e845477bd3c7f"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 4, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r"fixed create_venc.sh to not update pip itself with the global python"
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59"
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
    config_vars['MAX_REPO_REV'] = 59
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162416.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 15
    config_vars['REPO_NAME'] = r"V15"
    config_vars['REPO_REV'] = 59
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V15_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-05-30 10:29:38.857115"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V15_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/59"
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
    config_vars['SHORT_INDEX_CHECKSUM'] = r"52074f48d72fd4ac2fa9f1f7e661cd948b2e8653"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V15/00/59/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 12353
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
    config_vars['WLE_EXEC_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/WavesLicenseEngine.bundle/Contents/MacOS/exec/wle"
    config_vars['WRITE_CONFIG_VARS_READ_FROM_ENVIRON_TO_BATCH_FILE'] = r"no"
    config_vars['WTAR_RATIO'] = r"1.3"
    config_vars['WZLIB_EXTENSION'] = r".wzip"
    config_vars['Win_ALL_OS_NAMES'] = (r"Win", r"Win32", r"Win64")
    config_vars['ZLIB_COMPRESSION_LEVEL'] = 8
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162416.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-05-22 15:27:15.823473"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Q_Clone_Presets_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS__Data_Folders__IID", r"COSMOS__IID", r"COSMOS__Models_Data_Folders__IID", r"COSMOS_python_IID", r"Center_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Enigma_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"Get_General_Icons_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LicenseNotifications_1_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"ORS_Modulators_Data_IID", r"OpenVino_IID", r"PAZ_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"ReWire_IID", r"ReWire_backup_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"SOC_Presets_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"SuperTap_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"WLM_IID", r"WLM_Plus_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_15_10_IID", r"WaveShell1_AAX_15_5_IID", r"WaveShell1_AU_15_10_IID", r"WaveShell1_AU_15_5_IID", r"WaveShell1_VST_3_V15_10_IID", r"WaveShell1_VST_3_V15_5_IID", r"WaveShell1_WPAPI_2_15_10_IID", r"WaveShell1_WPAPI_2_15_5_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShells_Dir_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_15_10_46_IID", r"WavesLib1_15_5_139_IID", r"WavesLib1_15_5_79_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V15_2_IID", r"WavesReWireDevice_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.7 2025-05-22 15:27:15.823473 BM-MAC-ADO5"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.7"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 7)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"cgajimwldogmvzdt"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS__IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-15 16:26:37.199670"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 0
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 0
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO5"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59", r"/Library/Application Support/Waves/Central/V15", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=1223):  # 1m:14.982s
    with Stage(r"begin", prog_num=1224):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1225):  # 0m:0.014s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1226) as copy_file_to_file_001_1226:  # 0m:0.008s
            copy_file_to_file_001_1226()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1227) as copy_file_to_file_002_1227:  # 0m:0.006s
            copy_file_to_file_002_1227()
    with Stage(r"sync", prog_num=1228):  # 0m:42.303s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1229) as shell_command_003_1229:  # 0m:0.009s
            shell_command_003_1229()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1230) as shell_command_004_1230:  # 0m:0.011s
            shell_command_004_1230()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1231) as shell_command_005_1231:  # 0m:41.044s
            shell_command_005_1231()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1232) as shell_command_006_1232:  # 0m:0.009s
            shell_command_006_1232()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1233) as shell_command_007_1233:  # 0m:1.033s
            shell_command_007_1233()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1234) as shell_command_008_1234:  # 0m:0.009s
            shell_command_008_1234()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1235) as shell_command_009_1235:  # 0m:0.008s
            shell_command_009_1235()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1236) as shell_command_010_1236:  # 0m:0.161s
            shell_command_010_1236()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=1237):  # 0m:0.018s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=1238) as make_dir_011_1238:  # 0m:0.008s
                make_dir_011_1238()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=1239) as cd_012_1239:  # 0m:0.009s
                cd_012_1239()
                Progress(r"10089 files already in cache", own_progress_count=10089, prog_num=11328)()  # 0m:0.000s
                with Stage(r"post_sync", prog_num=11329):  # 0m:0.009s
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=11330) as copy_file_to_file_013_11330:  # 0m:0.009s
                        copy_file_to_file_013_11330()
            Progress(r"Done sync", prog_num=11331)()  # 0m:0.000s
    with Stage(r"copy", prog_num=11332):  # 0m:32.558s
        with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/before-copy-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=11333) as run_in_thread_014_11333:  # 0m:0.000s
            run_in_thread_014_11333()
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11334)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=11335):  # 0m:0.278s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=11336) as make_dir_015_11336:  # 0m:0.009s
                make_dir_015_11336()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=11337) as make_dir_016_11337:  # 0m:0.010s
                make_dir_016_11337()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=11338) as make_dir_017_11338:  # 0m:0.006s
                make_dir_017_11338()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=11339) as make_dir_018_11339:  # 0m:0.007s
                make_dir_018_11339()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=11340) as make_dir_019_11340:  # 0m:0.009s
                make_dir_019_11340()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=11341) as make_dir_020_11341:  # 0m:0.012s
                make_dir_020_11341()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=11342) as make_dir_021_11342:  # 0m:0.006s
                make_dir_021_11342()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=11343) as make_dir_022_11343:  # 0m:0.005s
                make_dir_022_11343()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=11344) as make_dir_023_11344:  # 0m:0.006s
                make_dir_023_11344()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=11345) as make_dir_024_11345:  # 0m:0.006s
                make_dir_024_11345()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=11346) as make_dir_025_11346:  # 0m:0.009s
                make_dir_025_11346()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=11347) as make_dir_026_11347:  # 0m:0.007s
                make_dir_026_11347()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=11348) as make_dir_027_11348:  # 0m:0.010s
                make_dir_027_11348()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=11349) as make_dir_028_11349:  # 0m:0.006s
                make_dir_028_11349()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=11350) as make_dir_029_11350:  # 0m:0.007s
                make_dir_029_11350()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=11351) as make_dir_030_11351:  # 0m:0.005s
                make_dir_030_11351()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/GTR", chowner=True, prog_num=11352) as make_dir_031_11352:  # 0m:0.011s
                make_dir_031_11352()
            with MakeDir(r"/Applications/Waves/ReWire", chowner=True, prog_num=11353) as make_dir_032_11353:  # 0m:0.013s
                make_dir_032_11353()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=11354) as make_dir_033_11354:  # 0m:0.006s
                make_dir_033_11354()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=11355) as make_dir_034_11355:  # 0m:0.005s
                make_dir_034_11355()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=11356) as make_dir_035_11356:  # 0m:0.008s
                make_dir_035_11356()
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=11357) as make_dir_036_11357:  # 0m:0.008s
                make_dir_036_11357()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=11358) as make_dir_037_11358:  # 0m:0.010s
                make_dir_037_11358()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=11359) as make_dir_038_11359:  # 0m:0.006s
                make_dir_038_11359()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=11360) as make_dir_039_11360:  # 0m:0.011s
                make_dir_039_11360()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=11361) as make_dir_040_11361:  # 0m:0.005s
                make_dir_040_11361()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=11362) as make_dir_041_11362:  # 0m:0.005s
                make_dir_041_11362()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=11363) as make_dir_042_11363:  # 0m:0.007s
                make_dir_042_11363()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=11364) as make_dir_043_11364:  # 0m:0.007s
                make_dir_043_11364()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=11365) as make_dir_044_11365:  # 0m:0.005s
                make_dir_044_11365()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=11366) as make_dir_045_11366:  # 0m:0.009s
                make_dir_045_11366()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=11367) as make_dir_046_11367:  # 0m:0.009s
                make_dir_046_11367()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=11368) as make_dir_047_11368:  # 0m:0.005s
                make_dir_047_11368()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=11369) as make_dir_048_11369:  # 0m:0.009s
                make_dir_048_11369()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=11370) as make_dir_049_11370:  # 0m:0.006s
                make_dir_049_11370()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=11371) as make_dir_050_11371:  # 0m:0.009s
                make_dir_050_11371()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=11372) as make_dir_051_11372:  # 0m:0.006s
                make_dir_051_11372()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=11373) as rm_file_or_dir_052_11373:  # 0m:0.015s
            rm_file_or_dir_052_11373()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=11374) as rm_file_or_dir_053_11374:  # 0m:0.001s
            rm_file_or_dir_053_11374()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=11375) as shell_command_054_11375:  # 0m:0.011s
            shell_command_054_11375()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=11376) as shell_command_055_11376:  # 0m:0.011s
            shell_command_055_11376()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=11377) as shell_command_056_11377:  # 0m:1.069s
            shell_command_056_11377()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11378) as shell_command_057_11378:  # 0m:0.007s
            shell_command_057_11378()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11379) as shell_command_058_11379:  # 0m:1.083s
            shell_command_058_11379()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=11380) as shell_command_059_11380:  # 0m:0.011s
            shell_command_059_11380()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=11381) as shell_command_060_11381:  # 0m:0.009s
            shell_command_060_11381()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=11382) as shell_command_061_11382:  # 0m:0.166s
            shell_command_061_11382()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11383) as cd_stage_062_11383:  # 0m:0.011s
            cd_stage_062_11383()
            with SetExecPermissionsInSyncFolder(prog_num=11384) as set_exec_permissions_in_sync_folder_063_11384:  # 0m:0.011s
                set_exec_permissions_in_sync_folder_063_11384()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=11385) as cd_stage_064_11385:  # 0m:0.114s
            cd_stage_064_11385()
            with Stage(r"copy", r"Bass Slapper application v15.5.79.262", prog_num=11386):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11387) as should_copy_source_065_11387:  # ?
                    should_copy_source_065_11387()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=11388):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=11389) as copy_dir_to_dir_066_11389:  # ?
                            copy_dir_to_dir_066_11389()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=11390) as unwtar_067_11390:  # ?
                            unwtar_067_11390()
                        with Chown(path=r"/Applications/Waves/Applications V15/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=11391, recursive=True) as chown_068_11391:  # 0m:0.001s
                            chown_068_11391()
            with Stage(r"copy", r"Electric Grand 80 application v15.5.79.262", prog_num=11392):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11393) as should_copy_source_069_11393:  # ?
                    should_copy_source_069_11393()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=11394):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=11395) as copy_dir_to_dir_070_11395:  # ?
                            copy_dir_to_dir_070_11395()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=11396) as unwtar_071_11396:  # ?
                            unwtar_071_11396()
                        with Chown(path=r"/Applications/Waves/Applications V15/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=11397, recursive=True) as chown_072_11397:  # 0m:0.005s
                            chown_072_11397()
            with Stage(r"copy", r"GTR application v15.5.79.262", prog_num=11398):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11399) as should_copy_source_073_11399:  # ?
                    should_copy_source_073_11399()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=11400):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=11401) as copy_dir_to_dir_074_11401:  # ?
                            copy_dir_to_dir_074_11401()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=11402) as unwtar_075_11402:  # ?
                            unwtar_075_11402()
                        with Chown(path=r"/Applications/Waves/Applications V15/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=11403, recursive=True) as chown_076_11403:  # 0m:0.000s
                            chown_076_11403()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=11404) as shell_command_077_11404:  # 0m:0.099s
                shell_command_077_11404()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=11405) as script_command_078_11405:  # 0m:0.008s
                script_command_078_11405()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=11406) as cd_stage_079_11406:  # 0m:0.014s
            cd_stage_079_11406()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=11407):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=11408) as should_copy_source_080_11408:  # ?
                    should_copy_source_080_11408()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=11409):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=11410) as copy_dir_to_dir_081_11410:  # ?
                            copy_dir_to_dir_081_11410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=11411) as unwtar_082_11411:  # ?
                            unwtar_082_11411()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=11412, recursive=True) as chown_083_11412:  # 0m:0.000s
                            chown_083_11412()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=11422) as resolve_symlink_files_in_folder_084_11422:  # 0m:0.013s
                resolve_symlink_files_in_folder_084_11422()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=11423) as cd_stage_085_11423:  # 0m:0.046s
            cd_stage_085_11423()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=11424):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11425) as should_copy_source_086_11425:  # ?
                    should_copy_source_086_11425()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=11426):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=11427) as copy_dir_to_dir_087_11427:  # ?
                            copy_dir_to_dir_087_11427()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=11428, recursive=True) as chown_088_11428:  # 0m:0.000s
                            chown_088_11428()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=11429):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11430) as should_copy_source_089_11430:  # ?
                    should_copy_source_089_11430()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=11431):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=11432) as copy_dir_to_dir_090_11432:  # ?
                            copy_dir_to_dir_090_11432()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=11433) as unwtar_091_11433:  # ?
                            unwtar_091_11433()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=11434, recursive=True) as chown_092_11434:  # 0m:0.001s
                            chown_092_11434()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=11435):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11436) as should_copy_source_093_11436:  # ?
                    should_copy_source_093_11436()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=11437):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=11438) as copy_dir_to_dir_094_11438:  # ?
                            copy_dir_to_dir_094_11438()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=11439, recursive=True) as chown_095_11439:  # 0m:0.001s
                            chown_095_11439()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=11440):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11441) as should_copy_source_096_11441:  # ?
                    should_copy_source_096_11441()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=11442):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11443) as copy_dir_to_dir_097_11443:  # ?
                            copy_dir_to_dir_097_11443()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=11444, recursive=True) as chown_098_11444:  # 0m:0.000s
                            chown_098_11444()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=11445):  # 0m:0.027s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11446) as should_copy_source_099_11446:  # 0m:0.027s
                    should_copy_source_099_11446()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=11447):  # 0m:0.027s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=11448) as copy_dir_to_dir_100_11448:  # 0m:0.026s
                            copy_dir_to_dir_100_11448()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=11449, recursive=True) as chown_101_11449:  # 0m:0.000s
                            chown_101_11449()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=11450):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11451) as should_copy_source_102_11451:  # ?
                    should_copy_source_102_11451()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=11452):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=11453) as copy_dir_to_dir_103_11453:  # ?
                            copy_dir_to_dir_103_11453()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=11454, recursive=True) as chown_104_11454:  # 0m:0.000s
                            chown_104_11454()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=11455):  # 0m:0.011s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11456) as should_copy_source_105_11456:  # 0m:0.011s
                    should_copy_source_105_11456()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=11457):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=11458) as copy_dir_to_dir_106_11458:  # 0m:0.007s
                            copy_dir_to_dir_106_11458()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=11459) as unwtar_107_11459:  # 0m:0.004s
                            unwtar_107_11459()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=11460, recursive=True) as chown_108_11460:  # 0m:0.000s
                            chown_108_11460()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=11461) as cd_stage_109_11461:  # 0m:8.373s
            cd_stage_109_11461()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=11462):  # 0m:8.373s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=11463) as should_copy_source_110_11463:  # 0m:0.007s
                    should_copy_source_110_11463()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=11464):  # 0m:0.006s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r".", prog_num=11465) as copy_file_to_dir_111_11465:  # 0m:0.006s
                            copy_file_to_dir_111_11465()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=11466) as chmod_and_chown_112_11466:  # 0m:0.000s
                            chmod_and_chown_112_11466()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=11467) as should_copy_source_113_11467:  # 0m:8.366s
                    should_copy_source_113_11467()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=11468):  # 0m:8.366s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=11469) as copy_dir_to_dir_114_11469:  # 0m:0.010s
                            copy_dir_to_dir_114_11469()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=11470) as unwtar_115_11470:  # 0m:8.355s
                            unwtar_115_11470()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=11471, recursive=True) as chown_116_11471:  # 0m:0.000s
                            chown_116_11471()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=11472) as cd_stage_117_11472:  # 0m:0.090s
            cd_stage_117_11472()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=11473):  # 0m:0.024s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11474) as should_copy_source_118_11474:  # 0m:0.013s
                    should_copy_source_118_11474()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=11475):  # 0m:0.013s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=11476) as copy_dir_to_dir_119_11476:  # 0m:0.012s
                            copy_dir_to_dir_119_11476()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=11477, recursive=True) as chown_120_11477:  # 0m:0.000s
                            chown_120_11477()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11478) as should_copy_source_121_11478:  # 0m:0.011s
                    should_copy_source_121_11478()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=11479):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=11480) as copy_dir_to_dir_122_11480:  # 0m:0.011s
                            copy_dir_to_dir_122_11480()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=11481, recursive=True) as chown_123_11481:  # 0m:0.000s
                            chown_123_11481()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=11482):  # 0m:0.066s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11483) as should_copy_source_124_11483:  # 0m:0.011s
                    should_copy_source_124_11483()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=11484):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=11485) as copy_dir_to_dir_125_11485:  # 0m:0.011s
                            copy_dir_to_dir_125_11485()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=11486, recursive=True) as chown_126_11486:  # 0m:0.000s
                            chown_126_11486()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11487) as should_copy_source_127_11487:  # 0m:0.054s
                    should_copy_source_127_11487()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=11488):  # 0m:0.054s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=11489) as copy_dir_to_dir_128_11489:  # 0m:0.054s
                            copy_dir_to_dir_128_11489()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=11490, recursive=True) as chown_129_11490:  # 0m:0.000s
                            chown_129_11490()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=11491) as cd_stage_130_11491:  # 0m:0.001s
            cd_stage_130_11491()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=11492):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=11493) as should_copy_source_131_11493:  # ?
                    should_copy_source_131_11493()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=11494):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=11495) as copy_file_to_dir_132_11495:  # ?
                            copy_file_to_dir_132_11495()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=11496) as chmod_and_chown_133_11496:  # 0m:0.000s
                            chmod_and_chown_133_11496()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=11497) as cd_stage_134_11497:  # 0m:0.013s
            cd_stage_134_11497()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=11498):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11499) as should_copy_source_135_11499:  # ?
                    should_copy_source_135_11499()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=11500):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=11501) as copy_dir_to_dir_136_11501:  # ?
                            copy_dir_to_dir_136_11501()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=11502, recursive=True) as chown_137_11502:  # 0m:0.000s
                            chown_137_11502()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=11503):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11504) as should_copy_source_138_11504:  # ?
                    should_copy_source_138_11504()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=11505):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=11506) as copy_dir_to_dir_139_11506:  # ?
                            copy_dir_to_dir_139_11506()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=11507, recursive=True) as chown_140_11507:  # 0m:0.001s
                            chown_140_11507()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=11508):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11509) as should_copy_source_141_11509:  # ?
                    should_copy_source_141_11509()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=11510):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11511) as copy_dir_to_dir_142_11511:  # ?
                            copy_dir_to_dir_142_11511()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=11512, recursive=True) as chown_143_11512:  # 0m:0.000s
                            chown_143_11512()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=11513):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11514) as should_copy_source_144_11514:  # ?
                    should_copy_source_144_11514()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=11515):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=11516) as copy_dir_to_dir_145_11516:  # ?
                            copy_dir_to_dir_145_11516()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=11517, recursive=True) as chown_146_11517:  # 0m:0.000s
                            chown_146_11517()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=11518):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11519) as should_copy_source_147_11519:  # ?
                    should_copy_source_147_11519()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=11520):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=11521) as copy_dir_to_dir_148_11521:  # ?
                            copy_dir_to_dir_148_11521()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=11522, recursive=True) as chown_149_11522:  # 0m:0.000s
                            chown_149_11522()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=11523):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11524) as should_copy_source_150_11524:  # ?
                    should_copy_source_150_11524()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=11525):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=11526) as copy_dir_to_dir_151_11526:  # ?
                            copy_dir_to_dir_151_11526()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=11527, recursive=True) as chown_152_11527:  # 0m:0.000s
                            chown_152_11527()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=11528):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11529) as should_copy_source_153_11529:  # ?
                    should_copy_source_153_11529()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=11530):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=11531) as copy_dir_to_dir_154_11531:  # ?
                            copy_dir_to_dir_154_11531()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=11532, recursive=True) as chown_155_11532:  # 0m:0.000s
                            chown_155_11532()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=11533):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11534) as should_copy_source_156_11534:  # ?
                    should_copy_source_156_11534()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=11535):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=11536) as copy_dir_to_dir_157_11536:  # ?
                            copy_dir_to_dir_157_11536()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=11537, recursive=True) as chown_158_11537:  # 0m:0.000s
                            chown_158_11537()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=11538):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11539) as should_copy_source_159_11539:  # ?
                    should_copy_source_159_11539()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=11540):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=11541) as copy_dir_to_dir_160_11541:  # ?
                            copy_dir_to_dir_160_11541()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=11542, recursive=True) as chown_161_11542:  # 0m:0.000s
                            chown_161_11542()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=11543):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11544) as should_copy_source_162_11544:  # ?
                    should_copy_source_162_11544()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=11545):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=11546) as copy_dir_to_dir_163_11546:  # ?
                            copy_dir_to_dir_163_11546()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=11547, recursive=True) as chown_164_11547:  # 0m:0.001s
                            chown_164_11547()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=11548):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11549) as should_copy_source_165_11549:  # ?
                    should_copy_source_165_11549()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=11550):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=11551) as copy_dir_to_dir_166_11551:  # ?
                            copy_dir_to_dir_166_11551()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=11552, recursive=True) as chown_167_11552:  # 0m:0.005s
                            chown_167_11552()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=11553):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11554) as should_copy_source_168_11554:  # ?
                    should_copy_source_168_11554()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=11555):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=11556) as copy_dir_to_dir_169_11556:  # ?
                            copy_dir_to_dir_169_11556()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=11557, recursive=True) as chown_170_11557:  # 0m:0.000s
                            chown_170_11557()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=11558):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11559) as should_copy_source_171_11559:  # ?
                    should_copy_source_171_11559()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=11560):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=11561) as copy_dir_to_dir_172_11561:  # ?
                            copy_dir_to_dir_172_11561()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=11562, recursive=True) as chown_173_11562:  # 0m:0.000s
                            chown_173_11562()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=11563):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11564) as should_copy_source_174_11564:  # ?
                    should_copy_source_174_11564()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=11565):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=11566) as copy_dir_to_dir_175_11566:  # ?
                            copy_dir_to_dir_175_11566()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=11567, recursive=True) as chown_176_11567:  # 0m:0.000s
                            chown_176_11567()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=11568):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11569) as should_copy_source_177_11569:  # ?
                    should_copy_source_177_11569()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=11570):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=11571) as copy_dir_to_dir_178_11571:  # ?
                            copy_dir_to_dir_178_11571()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=11572, recursive=True) as chown_179_11572:  # 0m:0.001s
                            chown_179_11572()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=11573):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11574) as should_copy_source_180_11574:  # ?
                    should_copy_source_180_11574()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=11575):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=11576) as copy_dir_to_dir_181_11576:  # ?
                            copy_dir_to_dir_181_11576()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=11577, recursive=True) as chown_182_11577:  # 0m:0.000s
                            chown_182_11577()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=11578):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11579) as should_copy_source_183_11579:  # ?
                    should_copy_source_183_11579()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=11580):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11581) as copy_dir_to_dir_184_11581:  # ?
                            copy_dir_to_dir_184_11581()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11582, recursive=True) as chown_185_11582:  # 0m:0.000s
                            chown_185_11582()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=11583):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11584) as should_copy_source_186_11584:  # ?
                    should_copy_source_186_11584()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=11585):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11586) as copy_dir_to_dir_187_11586:  # ?
                            copy_dir_to_dir_187_11586()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11587, recursive=True) as chown_188_11587:  # 0m:0.000s
                            chown_188_11587()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=11588):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11589) as should_copy_source_189_11589:  # ?
                    should_copy_source_189_11589()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=11590):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=11591) as copy_dir_to_dir_190_11591:  # ?
                            copy_dir_to_dir_190_11591()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=11592, recursive=True) as chown_191_11592:  # 0m:0.000s
                            chown_191_11592()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=11593) as cd_stage_192_11593:  # 0m:0.008s
            cd_stage_192_11593()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=11594):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11595) as should_copy_source_193_11595:  # ?
                    should_copy_source_193_11595()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=11596):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=11597) as copy_dir_to_dir_194_11597:  # ?
                            copy_dir_to_dir_194_11597()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=11598, recursive=True) as chown_195_11598:  # 0m:0.001s
                            chown_195_11598()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=11599):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11600) as should_copy_source_196_11600:  # ?
                    should_copy_source_196_11600()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=11601):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=11602) as copy_dir_to_dir_197_11602:  # ?
                            copy_dir_to_dir_197_11602()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=11603, recursive=True) as chown_198_11603:  # 0m:0.000s
                            chown_198_11603()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=11604):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11605) as should_copy_source_199_11605:  # ?
                    should_copy_source_199_11605()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=11606):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=11607) as copy_dir_to_dir_200_11607:  # ?
                            copy_dir_to_dir_200_11607()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=11608, recursive=True) as chown_201_11608:  # 0m:0.001s
                            chown_201_11608()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=11609):  # 0m:0.004s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11610) as should_copy_source_202_11610:  # ?
                    should_copy_source_202_11610()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=11611):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=11612) as copy_dir_to_dir_203_11612:  # ?
                            copy_dir_to_dir_203_11612()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=11613, recursive=True) as chown_204_11613:  # 0m:0.004s
                            chown_204_11613()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=11614):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11615) as should_copy_source_205_11615:  # ?
                    should_copy_source_205_11615()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=11616):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=11617) as copy_dir_to_dir_206_11617:  # ?
                            copy_dir_to_dir_206_11617()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=11618, recursive=True) as chown_207_11618:  # 0m:0.001s
                            chown_207_11618()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=11619):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11620) as should_copy_source_208_11620:  # ?
                    should_copy_source_208_11620()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=11621):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=11622) as copy_dir_to_dir_209_11622:  # ?
                            copy_dir_to_dir_209_11622()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=11623, recursive=True) as chown_210_11623:  # 0m:0.000s
                            chown_210_11623()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=11624):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11625) as should_copy_source_211_11625:  # ?
                    should_copy_source_211_11625()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=11626):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=11627) as copy_dir_to_dir_212_11627:  # ?
                            copy_dir_to_dir_212_11627()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=11628, recursive=True) as chown_213_11628:  # 0m:0.000s
                            chown_213_11628()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=11629) as cd_stage_214_11629:  # 0m:0.001s
            cd_stage_214_11629()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=11630):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11631) as should_copy_source_215_11631:  # ?
                    should_copy_source_215_11631()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=11632):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11633) as copy_dir_to_dir_216_11633:  # ?
                            copy_dir_to_dir_216_11633()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11634, recursive=True) as chown_217_11634:  # 0m:0.000s
                            chown_217_11634()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=11635):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11636) as should_copy_source_218_11636:  # ?
                    should_copy_source_218_11636()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=11637):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11638) as copy_dir_to_dir_219_11638:  # ?
                            copy_dir_to_dir_219_11638()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11639, recursive=True) as chown_220_11639:  # 0m:0.000s
                            chown_220_11639()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=11640) as cd_stage_221_11640:  # 0m:0.065s
            cd_stage_221_11640()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=11641):  # 0m:0.064s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11642) as should_copy_source_222_11642:  # 0m:0.009s
                    should_copy_source_222_11642()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=11643):  # 0m:0.009s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=11644) as unwtar_223_11644:  # 0m:0.009s
                            unwtar_223_11644()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11645) as should_copy_source_224_11645:  # 0m:0.055s
                    should_copy_source_224_11645()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=11646):  # 0m:0.055s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=11647) as unwtar_225_11647:  # 0m:0.055s
                            unwtar_225_11647()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=11648) as cd_stage_226_11648:  # 0m:0.010s
            cd_stage_226_11648()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=11649):  # 0m:0.010s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=11650) as should_copy_source_227_11650:  # 0m:0.010s
                    should_copy_source_227_11650()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=11651):  # 0m:0.009s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=11652) as unwtar_228_11652:  # 0m:0.009s
                            unwtar_228_11652()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=11653) as cd_stage_229_11653:  # 0m:5.065s
            cd_stage_229_11653()
            with Stage(r"copy", r"ARPlates v15.5.79.262", prog_num=11654):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11655) as should_copy_source_230_11655:  # ?
                    should_copy_source_230_11655()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=11656):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=11657) as copy_dir_to_dir_231_11657:  # ?
                            copy_dir_to_dir_231_11657()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=11658) as unwtar_232_11658:  # ?
                            unwtar_232_11658()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=11659, recursive=True) as chown_233_11659:  # 0m:0.000s
                            chown_233_11659()
            with Stage(r"copy", r"Abbey Road Vinyl v15.5.79.262", prog_num=11660):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11661) as should_copy_source_234_11661:  # ?
                    should_copy_source_234_11661()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=11662):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=11663) as copy_dir_to_dir_235_11663:  # ?
                            copy_dir_to_dir_235_11663()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=11664) as unwtar_236_11664:  # ?
                            unwtar_236_11664()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=11665, recursive=True) as chown_237_11665:  # 0m:0.000s
                            chown_237_11665()
            with Stage(r"copy", r"Aphex AX v15.5.79.262", prog_num=11666):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11667) as should_copy_source_238_11667:  # ?
                    should_copy_source_238_11667()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=11668):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=11669) as copy_dir_to_dir_239_11669:  # ?
                            copy_dir_to_dir_239_11669()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=11670) as unwtar_240_11670:  # ?
                            unwtar_240_11670()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=11671, recursive=True) as chown_241_11671:  # 0m:0.000s
                            chown_241_11671()
            with Stage(r"copy", r"AudioTrack v15.5.79.262", prog_num=11672):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11673) as should_copy_source_242_11673:  # ?
                    should_copy_source_242_11673()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=11674):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=11675) as copy_dir_to_dir_243_11675:  # ?
                            copy_dir_to_dir_243_11675()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=11676) as unwtar_244_11676:  # ?
                            unwtar_244_11676()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=11677, recursive=True) as chown_245_11677:  # 0m:0.000s
                            chown_245_11677()
            with Stage(r"copy", r"Bass Rider v15.5.79.262", prog_num=11678):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11679) as should_copy_source_246_11679:  # ?
                    should_copy_source_246_11679()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=11680):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=11681) as copy_dir_to_dir_247_11681:  # ?
                            copy_dir_to_dir_247_11681()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=11682) as unwtar_248_11682:  # ?
                            unwtar_248_11682()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=11683, recursive=True) as chown_249_11683:  # 0m:0.000s
                            chown_249_11683()
            with Stage(r"copy", r"Bass Slapper v15.5.79.262", prog_num=11684):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11685) as should_copy_source_250_11685:  # ?
                    should_copy_source_250_11685()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=11686):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=11687) as copy_dir_to_dir_251_11687:  # ?
                            copy_dir_to_dir_251_11687()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=11688) as unwtar_252_11688:  # ?
                            unwtar_252_11688()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=11689, recursive=True) as chown_253_11689:  # 0m:0.000s
                            chown_253_11689()
            with Stage(r"copy", r"Brauer Motion v15.5.79.262", prog_num=11690):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11691) as should_copy_source_254_11691:  # ?
                    should_copy_source_254_11691()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=11692):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=11693) as copy_dir_to_dir_255_11693:  # ?
                            copy_dir_to_dir_255_11693()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=11694) as unwtar_256_11694:  # ?
                            unwtar_256_11694()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=11695, recursive=True) as chown_257_11695:  # 0m:0.000s
                            chown_257_11695()
            with Stage(r"copy", r"Butch Vig Vocals v15.5.79.262", prog_num=11696):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11697) as should_copy_source_258_11697:  # ?
                    should_copy_source_258_11697()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=11698):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11699) as copy_dir_to_dir_259_11699:  # ?
                            copy_dir_to_dir_259_11699()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=11700) as unwtar_260_11700:  # ?
                            unwtar_260_11700()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=11701, recursive=True) as chown_261_11701:  # 0m:0.000s
                            chown_261_11701()
            with Stage(r"copy", r"C1 v15.5.79.262", prog_num=11702):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11703) as should_copy_source_262_11703:  # ?
                    should_copy_source_262_11703()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=11704):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=11705) as copy_dir_to_dir_263_11705:  # ?
                            copy_dir_to_dir_263_11705()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=11706) as unwtar_264_11706:  # ?
                            unwtar_264_11706()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C1.bundle", user_id=-1, group_id=-1, prog_num=11707, recursive=True) as chown_265_11707:  # 0m:0.000s
                            chown_265_11707()
            with Stage(r"copy", r"C4 v15.5.79.262", prog_num=11708):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11709) as should_copy_source_266_11709:  # ?
                    should_copy_source_266_11709()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=11710):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=11711) as copy_dir_to_dir_267_11711:  # ?
                            copy_dir_to_dir_267_11711()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=11712) as unwtar_268_11712:  # ?
                            unwtar_268_11712()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C4.bundle", user_id=-1, group_id=-1, prog_num=11713, recursive=True) as chown_269_11713:  # 0m:0.001s
                            chown_269_11713()
            with Stage(r"copy", r"CLA-2A v15.5.79.262", prog_num=11714):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11715) as should_copy_source_270_11715:  # ?
                    should_copy_source_270_11715()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=11716):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=11717) as copy_dir_to_dir_271_11717:  # ?
                            copy_dir_to_dir_271_11717()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=11718) as unwtar_272_11718:  # ?
                            unwtar_272_11718()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=11719, recursive=True) as chown_273_11719:  # 0m:0.004s
                            chown_273_11719()
            with Stage(r"copy", r"CLA-3A v15.5.79.262", prog_num=11720):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11721) as should_copy_source_274_11721:  # ?
                    should_copy_source_274_11721()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=11722):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=11723) as copy_dir_to_dir_275_11723:  # ?
                            copy_dir_to_dir_275_11723()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=11724) as unwtar_276_11724:  # ?
                            unwtar_276_11724()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=11725, recursive=True) as chown_277_11725:  # 0m:0.000s
                            chown_277_11725()
            with Stage(r"copy", r"CLA-76 v15.5.79.262", prog_num=11726):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11727) as should_copy_source_278_11727:  # ?
                    should_copy_source_278_11727()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=11728):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=11729) as copy_dir_to_dir_279_11729:  # ?
                            copy_dir_to_dir_279_11729()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=11730) as unwtar_280_11730:  # ?
                            unwtar_280_11730()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=11731, recursive=True) as chown_281_11731:  # 0m:0.000s
                            chown_281_11731()
            with Stage(r"copy", r"CLA Bass v15.5.79.262", prog_num=11732):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11733) as should_copy_source_282_11733:  # ?
                    should_copy_source_282_11733()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=11734):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=11735) as copy_dir_to_dir_283_11735:  # ?
                            copy_dir_to_dir_283_11735()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=11736) as unwtar_284_11736:  # ?
                            unwtar_284_11736()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=11737, recursive=True) as chown_285_11737:  # 0m:0.000s
                            chown_285_11737()
            with Stage(r"copy", r"CLA Guitars v15.5.79.262", prog_num=11738):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11739) as should_copy_source_286_11739:  # ?
                    should_copy_source_286_11739()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=11740):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=11741) as copy_dir_to_dir_287_11741:  # ?
                            copy_dir_to_dir_287_11741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=11742) as unwtar_288_11742:  # ?
                            unwtar_288_11742()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=11743, recursive=True) as chown_289_11743:  # 0m:0.000s
                            chown_289_11743()
            with Stage(r"copy", r"CLA Unplugged v15.5.79.262", prog_num=11744):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11745) as should_copy_source_290_11745:  # ?
                    should_copy_source_290_11745()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=11746):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=11747) as copy_dir_to_dir_291_11747:  # ?
                            copy_dir_to_dir_291_11747()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=11748) as unwtar_292_11748:  # ?
                            unwtar_292_11748()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=11749, recursive=True) as chown_293_11749:  # 0m:0.000s
                            chown_293_11749()
            with Stage(r"copy", r"CLA Vocals v15.5.79.262", prog_num=11750):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11751) as should_copy_source_294_11751:  # ?
                    should_copy_source_294_11751()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=11752):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11753) as copy_dir_to_dir_295_11753:  # ?
                            copy_dir_to_dir_295_11753()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=11754) as unwtar_296_11754:  # ?
                            unwtar_296_11754()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=11755, recursive=True) as chown_297_11755:  # 0m:0.000s
                            chown_297_11755()
            with Stage(r"copy", r"Center v15.5.79.262", prog_num=11756):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11757) as should_copy_source_298_11757:  # ?
                    should_copy_source_298_11757()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=11758):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=11759) as copy_dir_to_dir_299_11759:  # ?
                            copy_dir_to_dir_299_11759()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=11760) as unwtar_300_11760:  # ?
                            unwtar_300_11760()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Center.bundle", user_id=-1, group_id=-1, prog_num=11761, recursive=True) as chown_301_11761:  # 0m:0.000s
                            chown_301_11761()
            with Stage(r"copy", r"Clarity Vx v15.5.79.262", prog_num=11762):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11763) as should_copy_source_302_11763:  # ?
                    should_copy_source_302_11763()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=11764):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=11765) as copy_dir_to_dir_303_11765:  # ?
                            copy_dir_to_dir_303_11765()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=11766) as unwtar_304_11766:  # ?
                            unwtar_304_11766()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=11767, recursive=True) as chown_305_11767:  # 0m:0.000s
                            chown_305_11767()
            with Stage(r"copy", r"Saphira v15.5.79.262", prog_num=11768):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11769) as should_copy_source_306_11769:  # ?
                    should_copy_source_306_11769()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=11770):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=11771) as copy_dir_to_dir_307_11771:  # ?
                            copy_dir_to_dir_307_11771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=11772) as unwtar_308_11772:  # ?
                            unwtar_308_11772()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Saphira.bundle", user_id=-1, group_id=-1, prog_num=11773, recursive=True) as chown_309_11773:  # 0m:0.000s
                            chown_309_11773()
            with Stage(r"copy", r"Submarine v15.5.79.262", prog_num=11774):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11775) as should_copy_source_310_11775:  # ?
                    should_copy_source_310_11775()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=11776):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=11777) as copy_dir_to_dir_311_11777:  # ?
                            copy_dir_to_dir_311_11777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=11778) as unwtar_312_11778:  # ?
                            unwtar_312_11778()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Submarine.bundle", user_id=-1, group_id=-1, prog_num=11779, recursive=True) as chown_313_11779:  # 0m:0.000s
                            chown_313_11779()
            with Stage(r"copy", r"DeBreath v15.5.79.262", prog_num=11780):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11781) as should_copy_source_314_11781:  # ?
                    should_copy_source_314_11781()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=11782):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=11783) as copy_dir_to_dir_315_11783:  # ?
                            copy_dir_to_dir_315_11783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=11784) as unwtar_316_11784:  # ?
                            unwtar_316_11784()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=11785, recursive=True) as chown_317_11785:  # 0m:0.000s
                            chown_317_11785()
            with Stage(r"copy", r"DeEsser v15.5.79.262", prog_num=11786):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11787) as should_copy_source_318_11787:  # ?
                    should_copy_source_318_11787()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=11788):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=11789) as copy_dir_to_dir_319_11789:  # ?
                            copy_dir_to_dir_319_11789()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=11790) as unwtar_320_11790:  # ?
                            unwtar_320_11790()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=11791, recursive=True) as chown_321_11791:  # 0m:0.000s
                            chown_321_11791()
            with Stage(r"copy", r"Doppler v15.5.79.262", prog_num=11792):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11793) as should_copy_source_322_11793:  # ?
                    should_copy_source_322_11793()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=11794):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=11795) as copy_dir_to_dir_323_11795:  # ?
                            copy_dir_to_dir_323_11795()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=11796) as unwtar_324_11796:  # ?
                            unwtar_324_11796()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doppler.bundle", user_id=-1, group_id=-1, prog_num=11797, recursive=True) as chown_325_11797:  # 0m:0.000s
                            chown_325_11797()
            with Stage(r"copy", r"Doubler v15.5.79.262", prog_num=11798):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11799) as should_copy_source_326_11799:  # ?
                    should_copy_source_326_11799()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=11800):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=11801) as copy_dir_to_dir_327_11801:  # ?
                            copy_dir_to_dir_327_11801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=11802) as unwtar_328_11802:  # ?
                            unwtar_328_11802()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doubler.bundle", user_id=-1, group_id=-1, prog_num=11803, recursive=True) as chown_329_11803:  # 0m:0.000s
                            chown_329_11803()
            with Stage(r"copy", r"EMO-F2 v15.5.79.262", prog_num=11804):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11805) as should_copy_source_330_11805:  # ?
                    should_copy_source_330_11805()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=11806):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=11807) as copy_dir_to_dir_331_11807:  # ?
                            copy_dir_to_dir_331_11807()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=11808) as unwtar_332_11808:  # ?
                            unwtar_332_11808()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=11809, recursive=True) as chown_333_11809:  # 0m:0.000s
                            chown_333_11809()
            with Stage(r"copy", r"EMO-Q4 v15.5.79.262", prog_num=11810):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11811) as should_copy_source_334_11811:  # ?
                    should_copy_source_334_11811()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=11812):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=11813) as copy_dir_to_dir_335_11813:  # ?
                            copy_dir_to_dir_335_11813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=11814) as unwtar_336_11814:  # ?
                            unwtar_336_11814()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=11815, recursive=True) as chown_337_11815:  # 0m:0.004s
                            chown_337_11815()
            with Stage(r"copy", r"EddieKramer DR v15.5.79.262", prog_num=11816):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11817) as should_copy_source_338_11817:  # ?
                    should_copy_source_338_11817()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=11818):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=11819) as copy_dir_to_dir_339_11819:  # ?
                            copy_dir_to_dir_339_11819()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=11820) as unwtar_340_11820:  # ?
                            unwtar_340_11820()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=11821, recursive=True) as chown_341_11821:  # 0m:0.000s
                            chown_341_11821()
            with Stage(r"copy", r"EddieKramer VC v15.5.79.262", prog_num=11822):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11823) as should_copy_source_342_11823:  # ?
                    should_copy_source_342_11823()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=11824):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=11825) as copy_dir_to_dir_343_11825:  # ?
                            copy_dir_to_dir_343_11825()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=11826) as unwtar_344_11826:  # ?
                            unwtar_344_11826()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=11827, recursive=True) as chown_345_11827:  # 0m:0.000s
                            chown_345_11827()
            with Stage(r"copy", r"Electric Grand 80 v15.5.79.262", prog_num=11828):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11829) as should_copy_source_346_11829:  # ?
                    should_copy_source_346_11829()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=11830):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=11831) as copy_dir_to_dir_347_11831:  # ?
                            copy_dir_to_dir_347_11831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=11832) as unwtar_348_11832:  # ?
                            unwtar_348_11832()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=11833, recursive=True) as chown_349_11833:  # 0m:0.000s
                            chown_349_11833()
            with Stage(r"copy", r"Enigma v15.5.79.262", prog_num=11834):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11835) as should_copy_source_350_11835:  # ?
                    should_copy_source_350_11835()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=11836):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=11837) as copy_dir_to_dir_351_11837:  # ?
                            copy_dir_to_dir_351_11837()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=11838) as unwtar_352_11838:  # ?
                            unwtar_352_11838()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Enigma.bundle", user_id=-1, group_id=-1, prog_num=11839, recursive=True) as chown_353_11839:  # 0m:0.000s
                            chown_353_11839()
            with Stage(r"copy", r"GTRAmp v15.5.79.262", prog_num=11840):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11841) as should_copy_source_354_11841:  # ?
                    should_copy_source_354_11841()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=11842):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=11843) as copy_dir_to_dir_355_11843:  # ?
                            copy_dir_to_dir_355_11843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=11844) as unwtar_356_11844:  # ?
                            unwtar_356_11844()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=11845, recursive=True) as chown_357_11845:  # 0m:0.000s
                            chown_357_11845()
            with Stage(r"copy", r"GTRStomp v15.5.79.262", prog_num=11846):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11847) as should_copy_source_358_11847:  # ?
                    should_copy_source_358_11847()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=11848):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=11849) as copy_dir_to_dir_359_11849:  # ?
                            copy_dir_to_dir_359_11849()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=11850) as unwtar_360_11850:  # ?
                            unwtar_360_11850()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=11851, recursive=True) as chown_361_11851:  # 0m:0.000s
                            chown_361_11851()
            with Stage(r"copy", r"GTRToolRack v15.5.79.262", prog_num=11852):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11853) as should_copy_source_362_11853:  # ?
                    should_copy_source_362_11853()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=11854):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=11855) as copy_dir_to_dir_363_11855:  # ?
                            copy_dir_to_dir_363_11855()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=11856) as unwtar_364_11856:  # ?
                            unwtar_364_11856()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=11857, recursive=True) as chown_365_11857:  # 0m:0.000s
                            chown_365_11857()
            with Stage(r"copy", r"GTRTuner v15.5.79.262", prog_num=11858):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11859) as should_copy_source_366_11859:  # ?
                    should_copy_source_366_11859()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=11860):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=11861) as copy_dir_to_dir_367_11861:  # ?
                            copy_dir_to_dir_367_11861()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=11862) as unwtar_368_11862:  # ?
                            unwtar_368_11862()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=11863, recursive=True) as chown_369_11863:  # 0m:0.000s
                            chown_369_11863()
            with Stage(r"copy", r"Greg Wells MixCentric v15.5.79.262", prog_num=11864):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11865) as should_copy_source_370_11865:  # ?
                    should_copy_source_370_11865()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=11866):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=11867) as copy_dir_to_dir_371_11867:  # ?
                            copy_dir_to_dir_371_11867()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=11868) as unwtar_372_11868:  # ?
                            unwtar_372_11868()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=11869, recursive=True) as chown_373_11869:  # 0m:0.000s
                            chown_373_11869()
            with Stage(r"copy", r"Greg Wells PianoCentric v15.5.79.262", prog_num=11870):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11871) as should_copy_source_374_11871:  # ?
                    should_copy_source_374_11871()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=11872):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=11873) as copy_dir_to_dir_375_11873:  # ?
                            copy_dir_to_dir_375_11873()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=11874) as unwtar_376_11874:  # ?
                            unwtar_376_11874()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=11875, recursive=True) as chown_377_11875:  # 0m:0.000s
                            chown_377_11875()
            with Stage(r"copy", r"Greg Wells ToneCentric v15.5.79.262", prog_num=11876):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11877) as should_copy_source_378_11877:  # ?
                    should_copy_source_378_11877()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=11878):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=11879) as copy_dir_to_dir_379_11879:  # ?
                            copy_dir_to_dir_379_11879()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=11880) as unwtar_380_11880:  # ?
                            unwtar_380_11880()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=11881, recursive=True) as chown_381_11881:  # 0m:0.000s
                            chown_381_11881()
            with Stage(r"copy", r"H-Comp v15.5.79.262", prog_num=11882):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11883) as should_copy_source_382_11883:  # ?
                    should_copy_source_382_11883()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=11884):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=11885) as copy_dir_to_dir_383_11885:  # ?
                            copy_dir_to_dir_383_11885()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=11886) as unwtar_384_11886:  # ?
                            unwtar_384_11886()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=11887, recursive=True) as chown_385_11887:  # 0m:0.000s
                            chown_385_11887()
            with Stage(r"copy", r"H-Delay v15.5.79.262", prog_num=11888):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11889) as should_copy_source_386_11889:  # ?
                    should_copy_source_386_11889()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=11890):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=11891) as copy_dir_to_dir_387_11891:  # ?
                            copy_dir_to_dir_387_11891()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=11892) as unwtar_388_11892:  # ?
                            unwtar_388_11892()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=11893, recursive=True) as chown_389_11893:  # 0m:0.000s
                            chown_389_11893()
            with Stage(r"copy", r"H-Reverb v15.5.79.262", prog_num=11894):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11895) as should_copy_source_390_11895:  # ?
                    should_copy_source_390_11895()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=11896):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=11897) as copy_dir_to_dir_391_11897:  # ?
                            copy_dir_to_dir_391_11897()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=11898) as unwtar_392_11898:  # ?
                            unwtar_392_11898()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=11899, recursive=True) as chown_393_11899:  # 0m:0.000s
                            chown_393_11899()
            with Stage(r"copy", r"IR-L v15.5.79.262", prog_num=11900):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11901) as should_copy_source_394_11901:  # ?
                    should_copy_source_394_11901()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=11902):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=11903) as copy_dir_to_dir_395_11903:  # ?
                            copy_dir_to_dir_395_11903()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=11904) as unwtar_396_11904:  # ?
                            unwtar_396_11904()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/IR-L.bundle", user_id=-1, group_id=-1, prog_num=11905, recursive=True) as chown_397_11905:  # 0m:0.000s
                            chown_397_11905()
            with Stage(r"copy", r"InPhase v15.5.79.262", prog_num=11906):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11907) as should_copy_source_398_11907:  # ?
                    should_copy_source_398_11907()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=11908):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=11909) as copy_dir_to_dir_399_11909:  # ?
                            copy_dir_to_dir_399_11909()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=11910) as unwtar_400_11910:  # ?
                            unwtar_400_11910()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase.bundle", user_id=-1, group_id=-1, prog_num=11911, recursive=True) as chown_401_11911:  # 0m:0.000s
                            chown_401_11911()
            with Stage(r"copy", r"InPhase LT v15.5.79.262", prog_num=11912):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11913) as should_copy_source_402_11913:  # ?
                    should_copy_source_402_11913()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=11914):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=11915) as copy_dir_to_dir_403_11915:  # ?
                            copy_dir_to_dir_403_11915()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=11916) as unwtar_404_11916:  # ?
                            unwtar_404_11916()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=11917, recursive=True) as chown_405_11917:  # 0m:0.000s
                            chown_405_11917()
            with Stage(r"copy", r"J37 v15.5.79.262", prog_num=11918):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11919) as should_copy_source_406_11919:  # ?
                    should_copy_source_406_11919()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=11920):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=11921) as copy_dir_to_dir_407_11921:  # ?
                            copy_dir_to_dir_407_11921()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=11922) as unwtar_408_11922:  # ?
                            unwtar_408_11922()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/J37.bundle", user_id=-1, group_id=-1, prog_num=11923, recursive=True) as chown_409_11923:  # 0m:0.006s
                            chown_409_11923()
            with Stage(r"copy", r"JJP-Vocals v15.5.79.262", prog_num=11924):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11925) as should_copy_source_410_11925:  # ?
                    should_copy_source_410_11925()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=11926):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11927) as copy_dir_to_dir_411_11927:  # ?
                            copy_dir_to_dir_411_11927()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=11928) as unwtar_412_11928:  # ?
                            unwtar_412_11928()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=11929, recursive=True) as chown_413_11929:  # 0m:0.000s
                            chown_413_11929()
            with Stage(r"copy", r"Key Detector v15.5.79.262", prog_num=11930):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11931) as should_copy_source_414_11931:  # ?
                    should_copy_source_414_11931()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=11932):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=11933) as copy_dir_to_dir_415_11933:  # ?
                            copy_dir_to_dir_415_11933()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=11934) as unwtar_416_11934:  # ?
                            unwtar_416_11934()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=11935, recursive=True) as chown_417_11935:  # 0m:0.000s
                            chown_417_11935()
            with Stage(r"copy", r"KingsMic v15.5.79.262", prog_num=11936):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11937) as should_copy_source_418_11937:  # ?
                    should_copy_source_418_11937()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=11938):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=11939) as copy_dir_to_dir_419_11939:  # ?
                            copy_dir_to_dir_419_11939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=11940) as unwtar_420_11940:  # ?
                            unwtar_420_11940()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=11941, recursive=True) as chown_421_11941:  # 0m:0.000s
                            chown_421_11941()
            with Stage(r"copy", r"KramerHLS v15.5.79.262", prog_num=11942):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11943) as should_copy_source_422_11943:  # ?
                    should_copy_source_422_11943()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=11944):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=11945) as copy_dir_to_dir_423_11945:  # ?
                            copy_dir_to_dir_423_11945()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=11946) as unwtar_424_11946:  # ?
                            unwtar_424_11946()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=11947, recursive=True) as chown_425_11947:  # 0m:0.000s
                            chown_425_11947()
            with Stage(r"copy", r"KramerPIE v15.5.79.262", prog_num=11948):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11949) as should_copy_source_426_11949:  # ?
                    should_copy_source_426_11949()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=11950):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=11951) as copy_dir_to_dir_427_11951:  # ?
                            copy_dir_to_dir_427_11951()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=11952) as unwtar_428_11952:  # ?
                            unwtar_428_11952()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=11953, recursive=True) as chown_429_11953:  # 0m:0.000s
                            chown_429_11953()
            with Stage(r"copy", r"KramerTape v15.5.79.262", prog_num=11954):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11955) as should_copy_source_430_11955:  # ?
                    should_copy_source_430_11955()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=11956):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=11957) as copy_dir_to_dir_431_11957:  # ?
                            copy_dir_to_dir_431_11957()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=11958) as unwtar_432_11958:  # ?
                            unwtar_432_11958()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=11959, recursive=True) as chown_433_11959:  # 0m:0.000s
                            chown_433_11959()
            with Stage(r"copy", r"L1 v15.5.79.262", prog_num=11960):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11961) as should_copy_source_434_11961:  # ?
                    should_copy_source_434_11961()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=11962):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=11963) as copy_dir_to_dir_435_11963:  # ?
                            copy_dir_to_dir_435_11963()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=11964) as unwtar_436_11964:  # ?
                            unwtar_436_11964()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L1.bundle", user_id=-1, group_id=-1, prog_num=11965, recursive=True) as chown_437_11965:  # 0m:0.000s
                            chown_437_11965()
            with Stage(r"copy", r"L2 v15.5.79.262", prog_num=11966):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11967) as should_copy_source_438_11967:  # ?
                    should_copy_source_438_11967()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=11968):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=11969) as copy_dir_to_dir_439_11969:  # ?
                            copy_dir_to_dir_439_11969()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=11970) as unwtar_440_11970:  # ?
                            unwtar_440_11970()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L2.bundle", user_id=-1, group_id=-1, prog_num=11971, recursive=True) as chown_441_11971:  # 0m:0.000s
                            chown_441_11971()
            with Stage(r"copy", r"L3-16 v15.5.79.262", prog_num=11972):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11973) as should_copy_source_442_11973:  # ?
                    should_copy_source_442_11973()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=11974):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=11975) as copy_dir_to_dir_443_11975:  # ?
                            copy_dir_to_dir_443_11975()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=11976) as unwtar_444_11976:  # ?
                            unwtar_444_11976()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-16.bundle", user_id=-1, group_id=-1, prog_num=11977, recursive=True) as chown_445_11977:  # 0m:0.000s
                            chown_445_11977()
            with Stage(r"copy", r"L3-LL Multi v15.5.79.262", prog_num=11978):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11979) as should_copy_source_446_11979:  # ?
                    should_copy_source_446_11979()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=11980):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=11981) as copy_dir_to_dir_447_11981:  # ?
                            copy_dir_to_dir_447_11981()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=11982) as unwtar_448_11982:  # ?
                            unwtar_448_11982()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=11983, recursive=True) as chown_449_11983:  # 0m:0.000s
                            chown_449_11983()
            with Stage(r"copy", r"L3-LL Ultra v15.5.79.262", prog_num=11984):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11985) as should_copy_source_450_11985:  # ?
                    should_copy_source_450_11985()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=11986):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=11987) as copy_dir_to_dir_451_11987:  # ?
                            copy_dir_to_dir_451_11987()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=11988) as unwtar_452_11988:  # ?
                            unwtar_452_11988()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=11989, recursive=True) as chown_453_11989:  # 0m:0.000s
                            chown_453_11989()
            with Stage(r"copy", r"L3 Multi v15.5.79.262", prog_num=11990):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11991) as should_copy_source_454_11991:  # ?
                    should_copy_source_454_11991()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=11992):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=11993) as copy_dir_to_dir_455_11993:  # ?
                            copy_dir_to_dir_455_11993()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=11994) as unwtar_456_11994:  # ?
                            unwtar_456_11994()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=11995, recursive=True) as chown_457_11995:  # 0m:0.000s
                            chown_457_11995()
            with Stage(r"copy", r"L3 Ultra v15.5.79.262", prog_num=11996):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11997) as should_copy_source_458_11997:  # ?
                    should_copy_source_458_11997()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=11998):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=11999) as copy_dir_to_dir_459_11999:  # ?
                            copy_dir_to_dir_459_11999()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=12000) as unwtar_460_12000:  # ?
                            unwtar_460_12000()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=12001, recursive=True) as chown_461_12001:  # 0m:0.000s
                            chown_461_12001()
            with Stage(r"copy", r"LinEQ v15.5.79.262", prog_num=12002):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12003) as should_copy_source_462_12003:  # ?
                    should_copy_source_462_12003()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=12004):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=12005) as copy_dir_to_dir_463_12005:  # ?
                            copy_dir_to_dir_463_12005()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=12006) as unwtar_464_12006:  # ?
                            unwtar_464_12006()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=12007, recursive=True) as chown_465_12007:  # 0m:0.000s
                            chown_465_12007()
            with Stage(r"copy", r"LinMB v15.5.79.262", prog_num=12008):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12009) as should_copy_source_466_12009:  # ?
                    should_copy_source_466_12009()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=12010):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=12011) as copy_dir_to_dir_467_12011:  # ?
                            copy_dir_to_dir_467_12011()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=12012) as unwtar_468_12012:  # ?
                            unwtar_468_12012()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinMB.bundle", user_id=-1, group_id=-1, prog_num=12013, recursive=True) as chown_469_12013:  # 0m:0.000s
                            chown_469_12013()
            with Stage(r"copy", r"LoAir v15.5.79.262", prog_num=12014):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12015) as should_copy_source_470_12015:  # ?
                    should_copy_source_470_12015()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=12016):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=12017) as copy_dir_to_dir_471_12017:  # ?
                            copy_dir_to_dir_471_12017()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=12018) as unwtar_472_12018:  # ?
                            unwtar_472_12018()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LoAir.bundle", user_id=-1, group_id=-1, prog_num=12019, recursive=True) as chown_473_12019:  # 0m:0.000s
                            chown_473_12019()
            with Stage(r"copy", r"Lofi Space v15.5.79.262", prog_num=12020):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12021) as should_copy_source_474_12021:  # ?
                    should_copy_source_474_12021()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=12022):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=12023) as copy_dir_to_dir_475_12023:  # ?
                            copy_dir_to_dir_475_12023()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=12024) as unwtar_476_12024:  # ?
                            unwtar_476_12024()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=12025, recursive=True) as chown_477_12025:  # 0m:0.000s
                            chown_477_12025()
            with Stage(r"copy", r"MV2 v15.5.79.262", prog_num=12026):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12027) as should_copy_source_478_12027:  # ?
                    should_copy_source_478_12027()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=12028):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=12029) as copy_dir_to_dir_479_12029:  # ?
                            copy_dir_to_dir_479_12029()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=12030) as unwtar_480_12030:  # ?
                            unwtar_480_12030()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MV2.bundle", user_id=-1, group_id=-1, prog_num=12031, recursive=True) as chown_481_12031:  # 0m:0.004s
                            chown_481_12031()
            with Stage(r"copy", r"Magma Springs v15.5.79.262", prog_num=12032):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12033) as should_copy_source_482_12033:  # ?
                    should_copy_source_482_12033()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=12034):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=12035) as copy_dir_to_dir_483_12035:  # ?
                            copy_dir_to_dir_483_12035()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=12036) as unwtar_484_12036:  # ?
                            unwtar_484_12036()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=12037, recursive=True) as chown_485_12037:  # 0m:0.000s
                            chown_485_12037()
            with Stage(r"copy", r"MannyM-TripleD v15.5.79.262", prog_num=12038):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12039) as should_copy_source_486_12039:  # ?
                    should_copy_source_486_12039()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=12040):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=12041) as copy_dir_to_dir_487_12041:  # ?
                            copy_dir_to_dir_487_12041()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=12042) as unwtar_488_12042:  # ?
                            unwtar_488_12042()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=12043, recursive=True) as chown_489_12043:  # 0m:0.000s
                            chown_489_12043()
            with Stage(r"copy", r"Maserati DRM v15.5.79.262", prog_num=12044):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12045) as should_copy_source_490_12045:  # ?
                    should_copy_source_490_12045()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=12046):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=12047) as copy_dir_to_dir_491_12047:  # ?
                            copy_dir_to_dir_491_12047()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=12048) as unwtar_492_12048:  # ?
                            unwtar_492_12048()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=12049, recursive=True) as chown_493_12049:  # 0m:0.000s
                            chown_493_12049()
            with Stage(r"copy", r"Maserati VX1 v15.5.79.262", prog_num=12050):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12051) as should_copy_source_494_12051:  # ?
                    should_copy_source_494_12051()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=12052):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=12053) as copy_dir_to_dir_495_12053:  # ?
                            copy_dir_to_dir_495_12053()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=12054) as unwtar_496_12054:  # ?
                            unwtar_496_12054()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=12055, recursive=True) as chown_497_12055:  # 0m:0.000s
                            chown_497_12055()
            with Stage(r"copy", r"MaxxBass v15.5.79.262", prog_num=12056):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12057) as should_copy_source_498_12057:  # ?
                    should_copy_source_498_12057()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=12058):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=12059) as copy_dir_to_dir_499_12059:  # ?
                            copy_dir_to_dir_499_12059()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=12060) as unwtar_500_12060:  # ?
                            unwtar_500_12060()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=12061, recursive=True) as chown_501_12061:  # 0m:0.000s
                            chown_501_12061()
            with Stage(r"copy", r"MaxxVolume v15.5.79.262", prog_num=12062):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12063) as should_copy_source_502_12063:  # ?
                    should_copy_source_502_12063()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=12064):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=12065) as copy_dir_to_dir_503_12065:  # ?
                            copy_dir_to_dir_503_12065()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=12066) as unwtar_504_12066:  # ?
                            unwtar_504_12066()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=12067, recursive=True) as chown_505_12067:  # 0m:0.000s
                            chown_505_12067()
            with Stage(r"copy", r"MetaFilter v15.5.79.262", prog_num=12068):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12069) as should_copy_source_506_12069:  # ?
                    should_copy_source_506_12069()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=12070):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=12071) as copy_dir_to_dir_507_12071:  # ?
                            copy_dir_to_dir_507_12071()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=12072) as unwtar_508_12072:  # ?
                            unwtar_508_12072()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=12073, recursive=True) as chown_509_12073:  # 0m:0.000s
                            chown_509_12073()
            with Stage(r"copy", r"MetaFlanger v15.5.79.262", prog_num=12074):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12075) as should_copy_source_510_12075:  # ?
                    should_copy_source_510_12075()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=12076):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12077) as copy_dir_to_dir_511_12077:  # ?
                            copy_dir_to_dir_511_12077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=12078) as unwtar_512_12078:  # ?
                            unwtar_512_12078()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=12079, recursive=True) as chown_513_12079:  # 0m:0.000s
                            chown_513_12079()
            with Stage(r"copy", r"MondoMod v15.5.79.262", prog_num=12080):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12081) as should_copy_source_514_12081:  # ?
                    should_copy_source_514_12081()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=12082):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=12083) as copy_dir_to_dir_515_12083:  # ?
                            copy_dir_to_dir_515_12083()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=12084) as unwtar_516_12084:  # ?
                            unwtar_516_12084()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=12085, recursive=True) as chown_517_12085:  # 0m:0.000s
                            chown_517_12085()
            with Stage(r"copy", r"Morphoder v15.5.79.262", prog_num=12086):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12087) as should_copy_source_518_12087:  # ?
                    should_copy_source_518_12087()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=12088):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=12089) as copy_dir_to_dir_519_12089:  # ?
                            copy_dir_to_dir_519_12089()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=12090) as unwtar_520_12090:  # ?
                            unwtar_520_12090()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=12091, recursive=True) as chown_521_12091:  # 0m:0.000s
                            chown_521_12091()
            with Stage(r"copy", r"NLS v15.5.79.262", prog_num=12092):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12093) as should_copy_source_522_12093:  # ?
                    should_copy_source_522_12093()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=12094):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=12095) as copy_dir_to_dir_523_12095:  # ?
                            copy_dir_to_dir_523_12095()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=12096) as unwtar_524_12096:  # ?
                            unwtar_524_12096()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NLS.bundle", user_id=-1, group_id=-1, prog_num=12097, recursive=True) as chown_525_12097:  # 0m:0.000s
                            chown_525_12097()
            with Stage(r"copy", r"NX v15.5.79.262", prog_num=12098):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12099) as should_copy_source_526_12099:  # ?
                    should_copy_source_526_12099()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=12100):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=12101) as copy_dir_to_dir_527_12101:  # ?
                            copy_dir_to_dir_527_12101()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=12102) as unwtar_528_12102:  # ?
                            unwtar_528_12102()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NX.bundle", user_id=-1, group_id=-1, prog_num=12103, recursive=True) as chown_529_12103:  # 0m:0.000s
                            chown_529_12103()
            with Stage(r"copy", r"OKDriver v15.5.79.262", prog_num=12104):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12105) as should_copy_source_530_12105:  # ?
                    should_copy_source_530_12105()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=12106):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=12107) as copy_dir_to_dir_531_12107:  # ?
                            copy_dir_to_dir_531_12107()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=12108) as unwtar_532_12108:  # ?
                            unwtar_532_12108()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=12109, recursive=True) as chown_533_12109:  # 0m:0.000s
                            chown_533_12109()
            with Stage(r"copy", r"OKFilter v15.5.79.262", prog_num=12110):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12111) as should_copy_source_534_12111:  # ?
                    should_copy_source_534_12111()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=12112):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=12113) as copy_dir_to_dir_535_12113:  # ?
                            copy_dir_to_dir_535_12113()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=12114) as unwtar_536_12114:  # ?
                            unwtar_536_12114()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=12115, recursive=True) as chown_537_12115:  # 0m:0.000s
                            chown_537_12115()
            with Stage(r"copy", r"OKPhatter v15.5.79.262", prog_num=12116):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12117) as should_copy_source_538_12117:  # ?
                    should_copy_source_538_12117()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=12118):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=12119) as copy_dir_to_dir_539_12119:  # ?
                            copy_dir_to_dir_539_12119()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=12120) as unwtar_540_12120:  # ?
                            unwtar_540_12120()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=12121, recursive=True) as chown_541_12121:  # 0m:0.004s
                            chown_541_12121()
            with Stage(r"copy", r"OKPumper v15.5.79.262", prog_num=12122):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12123) as should_copy_source_542_12123:  # ?
                    should_copy_source_542_12123()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=12124):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=12125) as copy_dir_to_dir_543_12125:  # ?
                            copy_dir_to_dir_543_12125()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=12126) as unwtar_544_12126:  # ?
                            unwtar_544_12126()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=12127, recursive=True) as chown_545_12127:  # 0m:0.000s
                            chown_545_12127()
            with Stage(r"copy", r"PAZ v15.5.79.262", prog_num=12128):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12129) as should_copy_source_546_12129:  # ?
                    should_copy_source_546_12129()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=12130):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=12131) as copy_dir_to_dir_547_12131:  # ?
                            copy_dir_to_dir_547_12131()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=12132) as unwtar_548_12132:  # ?
                            unwtar_548_12132()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PAZ.bundle", user_id=-1, group_id=-1, prog_num=12133, recursive=True) as chown_549_12133:  # 0m:0.000s
                            chown_549_12133()
            with Stage(r"copy", r"PS22 v15.5.79.262", prog_num=12134):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12135) as should_copy_source_550_12135:  # ?
                    should_copy_source_550_12135()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=12136):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=12137) as copy_dir_to_dir_551_12137:  # ?
                            copy_dir_to_dir_551_12137()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=12138) as unwtar_552_12138:  # ?
                            unwtar_552_12138()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PS22.bundle", user_id=-1, group_id=-1, prog_num=12139, recursive=True) as chown_553_12139:  # 0m:0.000s
                            chown_553_12139()
            with Stage(r"copy", r"PuigChild v15.5.79.262", prog_num=12140):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12141) as should_copy_source_554_12141:  # ?
                    should_copy_source_554_12141()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=12142):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=12143) as copy_dir_to_dir_555_12143:  # ?
                            copy_dir_to_dir_555_12143()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=12144) as unwtar_556_12144:  # ?
                            unwtar_556_12144()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=12145, recursive=True) as chown_557_12145:  # 0m:0.000s
                            chown_557_12145()
            with Stage(r"copy", r"PuigTec v15.5.79.262", prog_num=12146):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12147) as should_copy_source_558_12147:  # ?
                    should_copy_source_558_12147()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=12148):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=12149) as copy_dir_to_dir_559_12149:  # ?
                            copy_dir_to_dir_559_12149()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=12150) as unwtar_560_12150:  # ?
                            unwtar_560_12150()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=12151, recursive=True) as chown_561_12151:  # 0m:0.000s
                            chown_561_12151()
            with Stage(r"copy", r"Q10 v15.5.79.262", prog_num=12152):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12153) as should_copy_source_562_12153:  # ?
                    should_copy_source_562_12153()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=12154):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=12155) as copy_dir_to_dir_563_12155:  # ?
                            copy_dir_to_dir_563_12155()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=12156) as unwtar_564_12156:  # ?
                            unwtar_564_12156()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q10.bundle", user_id=-1, group_id=-1, prog_num=12157, recursive=True) as chown_565_12157:  # 0m:0.000s
                            chown_565_12157()
            with Stage(r"copy", r"Q-Clone v15.5.79.262", prog_num=12158):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12159) as should_copy_source_566_12159:  # ?
                    should_copy_source_566_12159()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=12160):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=12161) as copy_dir_to_dir_567_12161:  # ?
                            copy_dir_to_dir_567_12161()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=12162) as unwtar_568_12162:  # ?
                            unwtar_568_12162()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=12163, recursive=True) as chown_569_12163:  # 0m:0.000s
                            chown_569_12163()
            with Stage(r"copy", r"RBass v15.5.79.262", prog_num=12164):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12165) as should_copy_source_570_12165:  # ?
                    should_copy_source_570_12165()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=12166):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=12167) as copy_dir_to_dir_571_12167:  # ?
                            copy_dir_to_dir_571_12167()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=12168) as unwtar_572_12168:  # ?
                            unwtar_572_12168()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RBass.bundle", user_id=-1, group_id=-1, prog_num=12169, recursive=True) as chown_573_12169:  # 0m:0.000s
                            chown_573_12169()
            with Stage(r"copy", r"RChannel v15.5.79.262", prog_num=12170):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12171) as should_copy_source_574_12171:  # ?
                    should_copy_source_574_12171()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=12172):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=12173) as copy_dir_to_dir_575_12173:  # ?
                            copy_dir_to_dir_575_12173()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=12174) as unwtar_576_12174:  # ?
                            unwtar_576_12174()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RChannel.bundle", user_id=-1, group_id=-1, prog_num=12175, recursive=True) as chown_577_12175:  # 0m:0.000s
                            chown_577_12175()
            with Stage(r"copy", r"RComp v15.5.79.262", prog_num=12176):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12177) as should_copy_source_578_12177:  # ?
                    should_copy_source_578_12177()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=12178):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=12179) as copy_dir_to_dir_579_12179:  # ?
                            copy_dir_to_dir_579_12179()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=12180) as unwtar_580_12180:  # ?
                            unwtar_580_12180()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RComp.bundle", user_id=-1, group_id=-1, prog_num=12181, recursive=True) as chown_581_12181:  # 0m:0.000s
                            chown_581_12181()
            with Stage(r"copy", r"RDeEsser v15.5.79.262", prog_num=12182):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12183) as should_copy_source_582_12183:  # ?
                    should_copy_source_582_12183()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=12184):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=12185) as copy_dir_to_dir_583_12185:  # ?
                            copy_dir_to_dir_583_12185()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=12186) as unwtar_584_12186:  # ?
                            unwtar_584_12186()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=12187, recursive=True) as chown_585_12187:  # 0m:0.000s
                            chown_585_12187()
            with Stage(r"copy", r"REDD17 v15.5.79.262", prog_num=12188):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12189) as should_copy_source_586_12189:  # ?
                    should_copy_source_586_12189()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=12190):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=12191) as copy_dir_to_dir_587_12191:  # ?
                            copy_dir_to_dir_587_12191()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=12192) as unwtar_588_12192:  # ?
                            unwtar_588_12192()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD17.bundle", user_id=-1, group_id=-1, prog_num=12193, recursive=True) as chown_589_12193:  # 0m:0.000s
                            chown_589_12193()
            with Stage(r"copy", r"REDD37-51 v15.5.79.262", prog_num=12194):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12195) as should_copy_source_590_12195:  # ?
                    should_copy_source_590_12195()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=12196):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=12197) as copy_dir_to_dir_591_12197:  # ?
                            copy_dir_to_dir_591_12197()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=12198) as unwtar_592_12198:  # ?
                            unwtar_592_12198()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=12199, recursive=True) as chown_593_12199:  # 0m:0.000s
                            chown_593_12199()
            with Stage(r"copy", r"REQ v15.5.79.262", prog_num=12200):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12201) as should_copy_source_594_12201:  # ?
                    should_copy_source_594_12201()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=12202):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=12203) as copy_dir_to_dir_595_12203:  # ?
                            copy_dir_to_dir_595_12203()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=12204) as unwtar_596_12204:  # ?
                            unwtar_596_12204()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REQ.bundle", user_id=-1, group_id=-1, prog_num=12205, recursive=True) as chown_597_12205:  # 0m:0.000s
                            chown_597_12205()
            with Stage(r"copy", r"RS56 v15.5.79.262", prog_num=12206):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12207) as should_copy_source_598_12207:  # ?
                    should_copy_source_598_12207()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=12208):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=12209) as copy_dir_to_dir_599_12209:  # ?
                            copy_dir_to_dir_599_12209()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=12210) as unwtar_600_12210:  # ?
                            unwtar_600_12210()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RS56.bundle", user_id=-1, group_id=-1, prog_num=12211, recursive=True) as chown_601_12211:  # 0m:0.000s
                            chown_601_12211()
            with Stage(r"copy", r"RVerb v15.5.79.262", prog_num=12212):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12213) as should_copy_source_602_12213:  # ?
                    should_copy_source_602_12213()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=12214):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=12215) as copy_dir_to_dir_603_12215:  # ?
                            copy_dir_to_dir_603_12215()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=12216) as unwtar_604_12216:  # ?
                            unwtar_604_12216()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVerb.bundle", user_id=-1, group_id=-1, prog_num=12217, recursive=True) as chown_605_12217:  # 0m:0.000s
                            chown_605_12217()
            with Stage(r"copy", r"RVox v15.5.79.262", prog_num=12218):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12219) as should_copy_source_606_12219:  # ?
                    should_copy_source_606_12219()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=12220):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=12221) as copy_dir_to_dir_607_12221:  # ?
                            copy_dir_to_dir_607_12221()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=12222) as unwtar_608_12222:  # ?
                            unwtar_608_12222()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVox.bundle", user_id=-1, group_id=-1, prog_num=12223, recursive=True) as chown_609_12223:  # 0m:0.000s
                            chown_609_12223()
            with Stage(r"copy", r"Reel ADT v15.5.79.262", prog_num=12224):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12225) as should_copy_source_610_12225:  # ?
                    should_copy_source_610_12225()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=12226):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=12227) as copy_dir_to_dir_611_12227:  # ?
                            copy_dir_to_dir_611_12227()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=12228) as unwtar_612_12228:  # ?
                            unwtar_612_12228()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=12229, recursive=True) as chown_613_12229:  # 0m:0.001s
                            chown_613_12229()
            with Stage(r"copy", r"RenAxx v15.5.79.262", prog_num=12230):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12231) as should_copy_source_614_12231:  # ?
                    should_copy_source_614_12231()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=12232):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=12233) as copy_dir_to_dir_615_12233:  # ?
                            copy_dir_to_dir_615_12233()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=12234) as unwtar_616_12234:  # ?
                            unwtar_616_12234()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=12235, recursive=True) as chown_617_12235:  # 0m:0.001s
                            chown_617_12235()
            with Stage(r"copy", r"Retro Fi v15.5.79.262", prog_num=12236):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12237) as should_copy_source_618_12237:  # ?
                    should_copy_source_618_12237()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=12238):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=12239) as copy_dir_to_dir_619_12239:  # ?
                            copy_dir_to_dir_619_12239()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=12240) as unwtar_620_12240:  # ?
                            unwtar_620_12240()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=12241, recursive=True) as chown_621_12241:  # 0m:0.000s
                            chown_621_12241()
            with Stage(r"copy", r"S1 v15.5.79.262", prog_num=12242):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12243) as should_copy_source_622_12243:  # ?
                    should_copy_source_622_12243()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=12244):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=12245) as copy_dir_to_dir_623_12245:  # ?
                            copy_dir_to_dir_623_12245()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=12246) as unwtar_624_12246:  # ?
                            unwtar_624_12246()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/S1.bundle", user_id=-1, group_id=-1, prog_num=12247, recursive=True) as chown_625_12247:  # 0m:0.000s
                            chown_625_12247()
            with Stage(r"copy", r"Scheps 73 v15.5.79.262", prog_num=12248):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12249) as should_copy_source_626_12249:  # ?
                    should_copy_source_626_12249()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=12250):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=12251) as copy_dir_to_dir_627_12251:  # ?
                            copy_dir_to_dir_627_12251()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=12252) as unwtar_628_12252:  # ?
                            unwtar_628_12252()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=12253, recursive=True) as chown_629_12253:  # 0m:0.000s
                            chown_629_12253()
            with Stage(r"copy", r"Scheps Omni Channel v15.5.79.262", prog_num=12254):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12255) as should_copy_source_630_12255:  # ?
                    should_copy_source_630_12255()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=12256):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=12257) as copy_dir_to_dir_631_12257:  # ?
                            copy_dir_to_dir_631_12257()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=12258) as unwtar_632_12258:  # ?
                            unwtar_632_12258()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=12259, recursive=True) as chown_633_12259:  # 0m:0.000s
                            chown_633_12259()
            with Stage(r"copy", r"Scheps Parallel Particles v15.5.79.262", prog_num=12260):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12261) as should_copy_source_634_12261:  # ?
                    should_copy_source_634_12261()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=12262):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=12263) as copy_dir_to_dir_635_12263:  # ?
                            copy_dir_to_dir_635_12263()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=12264) as unwtar_636_12264:  # ?
                            unwtar_636_12264()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=12265, recursive=True) as chown_637_12265:  # 0m:0.000s
                            chown_637_12265()
            with Stage(r"copy", r"Sibilance v15.5.79.262", prog_num=12266):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12267) as should_copy_source_638_12267:  # ?
                    should_copy_source_638_12267()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=12268):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=12269) as copy_dir_to_dir_639_12269:  # ?
                            copy_dir_to_dir_639_12269()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=12270) as unwtar_640_12270:  # ?
                            unwtar_640_12270()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=12271, recursive=True) as chown_641_12271:  # 0m:0.000s
                            chown_641_12271()
            with Stage(r"copy", r"Emo Signal Generator v15.5.79.262", prog_num=12272):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12273) as should_copy_source_642_12273:  # ?
                    should_copy_source_642_12273()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=12274):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=12275) as copy_dir_to_dir_643_12275:  # ?
                            copy_dir_to_dir_643_12275()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=12276) as unwtar_644_12276:  # ?
                            unwtar_644_12276()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=12277, recursive=True) as chown_645_12277:  # 0m:0.000s
                            chown_645_12277()
            with Stage(r"copy", r"Silk Vocal v15.10.46.293", prog_num=12278):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12279) as should_copy_source_646_12279:  # ?
                    should_copy_source_646_12279()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=12280):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=12281) as copy_dir_to_dir_647_12281:  # ?
                            copy_dir_to_dir_647_12281()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=12282) as unwtar_648_12282:  # ?
                            unwtar_648_12282()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=12283, recursive=True) as chown_649_12283:  # 0m:0.000s
                            chown_649_12283()
            with Stage(r"copy", r"Smack Attack v15.5.79.262", prog_num=12284):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12285) as should_copy_source_650_12285:  # ?
                    should_copy_source_650_12285()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=12286):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=12287) as copy_dir_to_dir_651_12287:  # ?
                            copy_dir_to_dir_651_12287()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=12288) as unwtar_652_12288:  # ?
                            unwtar_652_12288()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=12289, recursive=True) as chown_653_12289:  # 0m:0.000s
                            chown_653_12289()
            with Stage(r"copy", r"SoundShifter v15.5.79.262", prog_num=12290):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12291) as should_copy_source_654_12291:  # ?
                    should_copy_source_654_12291()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=12292):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=12293) as copy_dir_to_dir_655_12293:  # ?
                            copy_dir_to_dir_655_12293()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=12294) as unwtar_656_12294:  # ?
                            unwtar_656_12294()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=12295, recursive=True) as chown_657_12295:  # 0m:0.000s
                            chown_657_12295()
            with Stage(r"copy", r"Spherix Immersive Compressor v15.5.79.262", prog_num=12296):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12297) as should_copy_source_658_12297:  # ?
                    should_copy_source_658_12297()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=12298):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=12299) as copy_dir_to_dir_659_12299:  # ?
                            copy_dir_to_dir_659_12299()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=12300) as unwtar_660_12300:  # ?
                            unwtar_660_12300()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=12301, recursive=True) as chown_661_12301:  # 0m:0.000s
                            chown_661_12301()
            with Stage(r"copy", r"Spherix Immersive Limiter v15.5.79.262", prog_num=12302):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12303) as should_copy_source_662_12303:  # ?
                    should_copy_source_662_12303()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=12304):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=12305) as copy_dir_to_dir_663_12305:  # ?
                            copy_dir_to_dir_663_12305()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=12306) as unwtar_664_12306:  # ?
                            unwtar_664_12306()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=12307, recursive=True) as chown_665_12307:  # 0m:0.000s
                            chown_665_12307()
            with Stage(r"copy", r"SuperTap v15.5.79.262", prog_num=12308):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12309) as should_copy_source_666_12309:  # ?
                    should_copy_source_666_12309()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=12310):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=12311) as copy_dir_to_dir_667_12311:  # ?
                            copy_dir_to_dir_667_12311()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=12312) as unwtar_668_12312:  # ?
                            unwtar_668_12312()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=12313, recursive=True) as chown_669_12313:  # 0m:0.000s
                            chown_669_12313()
            with Stage(r"copy", r"TG12345 v15.5.79.262", prog_num=12314):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12315) as should_copy_source_670_12315:  # ?
                    should_copy_source_670_12315()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=12316):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=12317) as copy_dir_to_dir_671_12317:  # ?
                            copy_dir_to_dir_671_12317()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=12318) as unwtar_672_12318:  # ?
                            unwtar_672_12318()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TG12345.bundle", user_id=-1, group_id=-1, prog_num=12319, recursive=True) as chown_673_12319:  # 0m:0.000s
                            chown_673_12319()
            with Stage(r"copy", r"AR TG Meter Bridge v15.5.79.262", prog_num=12320):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12321) as should_copy_source_674_12321:  # ?
                    should_copy_source_674_12321()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=12322):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=12323) as copy_dir_to_dir_675_12323:  # ?
                            copy_dir_to_dir_675_12323()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=12324) as unwtar_676_12324:  # ?
                            unwtar_676_12324()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=12325, recursive=True) as chown_677_12325:  # 0m:0.000s
                            chown_677_12325()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v15.5.79.262", prog_num=12326):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12327) as should_copy_source_678_12327:  # ?
                    should_copy_source_678_12327()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=12328):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=12329) as copy_dir_to_dir_679_12329:  # ?
                            copy_dir_to_dir_679_12329()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=12330) as unwtar_680_12330:  # ?
                            unwtar_680_12330()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=12331, recursive=True) as chown_681_12331:  # 0m:0.008s
                            chown_681_12331()
            with Stage(r"copy", r"TransX v15.5.79.262", prog_num=12332):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12333) as should_copy_source_682_12333:  # ?
                    should_copy_source_682_12333()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=12334):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=12335) as copy_dir_to_dir_683_12335:  # ?
                            copy_dir_to_dir_683_12335()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=12336) as unwtar_684_12336:  # ?
                            unwtar_684_12336()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TransX.bundle", user_id=-1, group_id=-1, prog_num=12337, recursive=True) as chown_685_12337:  # 0m:0.000s
                            chown_685_12337()
            with Stage(r"copy", r"TrueVerb v15.5.79.262", prog_num=12338):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12339) as should_copy_source_686_12339:  # ?
                    should_copy_source_686_12339()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=12340):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=12341) as copy_dir_to_dir_687_12341:  # ?
                            copy_dir_to_dir_687_12341()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=12342) as unwtar_688_12342:  # ?
                            unwtar_688_12342()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=12343, recursive=True) as chown_689_12343:  # 0m:0.000s
                            chown_689_12343()
            with Stage(r"copy", r"UM v15.5.79.262", prog_num=12344):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12345) as should_copy_source_690_12345:  # ?
                    should_copy_source_690_12345()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=12346):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=12347) as copy_dir_to_dir_691_12347:  # ?
                            copy_dir_to_dir_691_12347()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=12348) as unwtar_692_12348:  # ?
                            unwtar_692_12348()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UM.bundle", user_id=-1, group_id=-1, prog_num=12349, recursive=True) as chown_693_12349:  # 0m:0.000s
                            chown_693_12349()
            with Stage(r"copy", r"UltraPitch v15.5.79.262", prog_num=12350):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12351) as should_copy_source_694_12351:  # ?
                    should_copy_source_694_12351()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=12352):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=12353) as copy_dir_to_dir_695_12353:  # ?
                            copy_dir_to_dir_695_12353()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=12354) as unwtar_696_12354:  # ?
                            unwtar_696_12354()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=12355, recursive=True) as chown_697_12355:  # 0m:0.000s
                            chown_697_12355()
            with Stage(r"copy", r"VComp v15.5.79.262", prog_num=12356):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12357) as should_copy_source_698_12357:  # ?
                    should_copy_source_698_12357()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=12358):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=12359) as copy_dir_to_dir_699_12359:  # ?
                            copy_dir_to_dir_699_12359()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=12360) as unwtar_700_12360:  # ?
                            unwtar_700_12360()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VComp.bundle", user_id=-1, group_id=-1, prog_num=12361, recursive=True) as chown_701_12361:  # 0m:0.000s
                            chown_701_12361()
            with Stage(r"copy", r"VEQ3 v15.5.79.262", prog_num=12362):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12363) as should_copy_source_702_12363:  # ?
                    should_copy_source_702_12363()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=12364):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=12365) as copy_dir_to_dir_703_12365:  # ?
                            copy_dir_to_dir_703_12365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=12366) as unwtar_704_12366:  # ?
                            unwtar_704_12366()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=12367, recursive=True) as chown_705_12367:  # 0m:0.000s
                            chown_705_12367()
            with Stage(r"copy", r"VEQ4 v15.5.79.262", prog_num=12368):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12369) as should_copy_source_706_12369:  # ?
                    should_copy_source_706_12369()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=12370):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=12371) as copy_dir_to_dir_707_12371:  # ?
                            copy_dir_to_dir_707_12371()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=12372) as unwtar_708_12372:  # ?
                            unwtar_708_12372()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=12373, recursive=True) as chown_709_12373:  # 0m:0.000s
                            chown_709_12373()
            with Stage(r"copy", r"VU Meter v15.5.79.262", prog_num=12374):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12375) as should_copy_source_710_12375:  # ?
                    should_copy_source_710_12375()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=12376):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=12377) as copy_dir_to_dir_711_12377:  # ?
                            copy_dir_to_dir_711_12377()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=12378) as unwtar_712_12378:  # ?
                            unwtar_712_12378()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=12379, recursive=True) as chown_713_12379:  # 0m:0.000s
                            chown_713_12379()
            with Stage(r"copy", r"Vitamin v15.5.79.262", prog_num=12380):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12381) as should_copy_source_714_12381:  # ?
                    should_copy_source_714_12381()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=12382):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=12383) as copy_dir_to_dir_715_12383:  # ?
                            copy_dir_to_dir_715_12383()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=12384) as unwtar_716_12384:  # ?
                            unwtar_716_12384()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=12385, recursive=True) as chown_717_12385:  # 0m:0.000s
                            chown_717_12385()
            with Stage(r"copy", r"Vocal Rider v15.5.79.262", prog_num=12386):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12387) as should_copy_source_718_12387:  # ?
                    should_copy_source_718_12387()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=12388):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=12389) as copy_dir_to_dir_719_12389:  # ?
                            copy_dir_to_dir_719_12389()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=12390) as unwtar_720_12390:  # ?
                            unwtar_720_12390()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=12391, recursive=True) as chown_721_12391:  # 0m:0.000s
                            chown_721_12391()
            with Stage(r"copy", r"Voltage Amps Bass v15.5.79.262", prog_num=12392):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12393) as should_copy_source_722_12393:  # ?
                    should_copy_source_722_12393()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=12394):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=12395) as copy_dir_to_dir_723_12395:  # ?
                            copy_dir_to_dir_723_12395()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=12396) as unwtar_724_12396:  # ?
                            unwtar_724_12396()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=12397, recursive=True) as chown_725_12397:  # 0m:0.000s
                            chown_725_12397()
            with Stage(r"copy", r"Voltage Amps Guitar v15.5.79.262", prog_num=12398):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12399) as should_copy_source_726_12399:  # ?
                    should_copy_source_726_12399()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=12400):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=12401) as copy_dir_to_dir_727_12401:  # ?
                            copy_dir_to_dir_727_12401()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=12402) as unwtar_728_12402:  # ?
                            unwtar_728_12402()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=12403, recursive=True) as chown_729_12403:  # 0m:0.000s
                            chown_729_12403()
            with Stage(r"copy", r"WLM v15.5.79.262", prog_num=12404):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12405) as should_copy_source_730_12405:  # ?
                    should_copy_source_730_12405()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=12406):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=12407) as copy_dir_to_dir_731_12407:  # ?
                            copy_dir_to_dir_731_12407()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=12408) as unwtar_732_12408:  # ?
                            unwtar_732_12408()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM.bundle", user_id=-1, group_id=-1, prog_num=12409, recursive=True) as chown_733_12409:  # 0m:0.000s
                            chown_733_12409()
            with Stage(r"copy", r"WLM Plus v15.5.79.262", prog_num=12410):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12411) as should_copy_source_734_12411:  # ?
                    should_copy_source_734_12411()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=12412):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=12413) as copy_dir_to_dir_735_12413:  # ?
                            copy_dir_to_dir_735_12413()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=12414) as unwtar_736_12414:  # ?
                            unwtar_736_12414()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=12415, recursive=True) as chown_737_12415:  # 0m:0.000s
                            chown_737_12415()
            with Stage(r"copy", r"WavesHeadTracker v15.5.79.262", prog_num=12416):  # 0m:3.395s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=5, prog_num=12417) as should_copy_source_738_12417:  # 0m:3.395s
                    should_copy_source_738_12417()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=12418):  # 0m:3.395s
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=12419) as rm_file_or_dir_739_12419:  # 0m:0.007s
                            rm_file_or_dir_739_12419()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=12420) as copy_dir_to_dir_740_12420:  # 0m:0.003s
                            copy_dir_to_dir_740_12420()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=12421) as unwtar_741_12421:  # 0m:3.384s
                            unwtar_741_12421()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=12422, recursive=True) as chown_742_12422:  # 0m:0.000s
                            chown_742_12422()
            with Stage(r"copy", r"WavesLib1_15_10_46_293 v15.10.46.293", prog_num=12423):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12424) as should_copy_source_743_12424:  # ?
                    should_copy_source_743_12424()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.10.46.framework", prog_num=12425):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r".", delete_extraneous_files=True, prog_num=12426) as copy_dir_to_dir_744_12426:  # ?
                            copy_dir_to_dir_744_12426()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", where_to_unwtar=r".", prog_num=12427) as unwtar_745_12427:  # ?
                            unwtar_745_12427()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.10.46.framework", user_id=-1, group_id=-1, prog_num=12428, recursive=True) as chown_746_12428:  # 0m:0.001s
                            chown_746_12428()
            with Stage(r"copy", r"WavesLib1_15_5_139_322 v15.5.139.322", prog_num=12429):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12430) as should_copy_source_747_12430:  # ?
                    should_copy_source_747_12430()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.139.framework", prog_num=12431):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r".", delete_extraneous_files=True, prog_num=12432) as copy_dir_to_dir_748_12432:  # ?
                            copy_dir_to_dir_748_12432()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", where_to_unwtar=r".", prog_num=12433) as unwtar_749_12433:  # ?
                            unwtar_749_12433()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.139.framework", user_id=-1, group_id=-1, prog_num=12434, recursive=True) as chown_750_12434:  # 0m:0.000s
                            chown_750_12434()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=12435):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12436) as should_copy_source_751_12436:  # ?
                    should_copy_source_751_12436()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=12437):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=12438) as copy_dir_to_dir_752_12438:  # ?
                            copy_dir_to_dir_752_12438()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=12439) as unwtar_753_12439:  # ?
                            unwtar_753_12439()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=12440, recursive=True) as chown_754_12440:  # 0m:0.000s
                            chown_754_12440()
            with Stage(r"copy", r"WavesTune v15.5.79.262", prog_num=12441):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12442) as should_copy_source_755_12442:  # ?
                    should_copy_source_755_12442()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=12443):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=12444) as copy_dir_to_dir_756_12444:  # ?
                            copy_dir_to_dir_756_12444()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=12445) as unwtar_757_12445:  # ?
                            unwtar_757_12445()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=12446, recursive=True) as chown_758_12446:  # 0m:0.000s
                            chown_758_12446()
            with Stage(r"copy", r"WavesTune LT v15.5.79.262", prog_num=12447):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12448) as should_copy_source_759_12448:  # ?
                    should_copy_source_759_12448()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=12449):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=12450) as copy_dir_to_dir_760_12450:  # ?
                            copy_dir_to_dir_760_12450()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=12451) as unwtar_761_12451:  # ?
                            unwtar_761_12451()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=12452, recursive=True) as chown_762_12452:  # 0m:0.000s
                            chown_762_12452()
            with Stage(r"copy", r"Waves Harmony v15.5.139.322", prog_num=12453):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12454) as should_copy_source_763_12454:  # ?
                    should_copy_source_763_12454()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=12455):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=12456) as copy_dir_to_dir_764_12456:  # ?
                            copy_dir_to_dir_764_12456()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=12457) as unwtar_765_12457:  # ?
                            unwtar_765_12457()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=12458, recursive=True) as chown_766_12458:  # 0m:0.000s
                            chown_766_12458()
            with Stage(r"copy", r"Waves Tune Real-Time v15.5.79.262", prog_num=12459):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12460) as should_copy_source_767_12460:  # ?
                    should_copy_source_767_12460()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=12461):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=12462) as copy_dir_to_dir_768_12462:  # ?
                            copy_dir_to_dir_768_12462()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=12463) as unwtar_769_12463:  # ?
                            unwtar_769_12463()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=12464, recursive=True) as chown_770_12464:  # 0m:0.000s
                            chown_770_12464()
            with Stage(r"copy", r"X-Click v15.5.79.262", prog_num=12465):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12466) as should_copy_source_771_12466:  # ?
                    should_copy_source_771_12466()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=12467):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=12468) as copy_dir_to_dir_772_12468:  # ?
                            copy_dir_to_dir_772_12468()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=12469) as unwtar_773_12469:  # ?
                            unwtar_773_12469()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Click.bundle", user_id=-1, group_id=-1, prog_num=12470, recursive=True) as chown_774_12470:  # 0m:0.000s
                            chown_774_12470()
            with Stage(r"copy", r"X-Crackle v15.5.79.262", prog_num=12471):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12472) as should_copy_source_775_12472:  # ?
                    should_copy_source_775_12472()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=12473):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=12474) as copy_dir_to_dir_776_12474:  # ?
                            copy_dir_to_dir_776_12474()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=12475) as unwtar_777_12475:  # ?
                            unwtar_777_12475()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=12476, recursive=True) as chown_778_12476:  # 0m:0.000s
                            chown_778_12476()
            with Stage(r"copy", r"X-Hum v15.5.79.262", prog_num=12477):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12478) as should_copy_source_779_12478:  # ?
                    should_copy_source_779_12478()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=12479):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=12480) as copy_dir_to_dir_780_12480:  # ?
                            copy_dir_to_dir_780_12480()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=12481) as unwtar_781_12481:  # ?
                            unwtar_781_12481()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=12482, recursive=True) as chown_782_12482:  # 0m:0.000s
                            chown_782_12482()
            with Stage(r"copy", r"X-Noise v15.5.79.262", prog_num=12483):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12484) as should_copy_source_783_12484:  # ?
                    should_copy_source_783_12484()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=12485):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12486) as copy_dir_to_dir_784_12486:  # ?
                            copy_dir_to_dir_784_12486()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=12487) as unwtar_785_12487:  # ?
                            unwtar_785_12487()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=12488, recursive=True) as chown_786_12488:  # 0m:0.000s
                            chown_786_12488()
            with Stage(r"copy", r"Z-Noise v15.5.79.262", prog_num=12489):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12490) as should_copy_source_787_12490:  # ?
                    should_copy_source_787_12490()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=12491):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12492) as copy_dir_to_dir_788_12492:  # ?
                            copy_dir_to_dir_788_12492()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=12493) as unwtar_789_12493:  # ?
                            unwtar_789_12493()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=12494, recursive=True) as chown_790_12494:  # 0m:0.000s
                            chown_790_12494()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=6, prog_num=12500) as resolve_symlink_files_in_folder_791_12500:  # 0m:1.302s
                resolve_symlink_files_in_folder_791_12500()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=12501) as shell_command_792_12501:  # 0m:0.097s
                shell_command_792_12501()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=12502) as script_command_793_12502:  # 0m:0.011s
                script_command_793_12502()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12503) as shell_command_794_12503:  # 0m:0.024s
                shell_command_794_12503()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12504) as create_symlink_795_12504:  # 0m:0.001s
                create_symlink_795_12504()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12505) as create_symlink_796_12505:  # 0m:0.000s
                create_symlink_796_12505()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=12506) as copy_glob_to_dir_797_12506:  # 0m:0.154s
                copy_glob_to_dir_797_12506()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=12507) as cd_stage_798_12507:  # 0m:0.001s
            cd_stage_798_12507()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=12508):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=12509) as should_copy_source_799_12509:  # ?
                    should_copy_source_799_12509()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=12510):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=12511) as copy_file_to_dir_800_12511:  # ?
                            copy_file_to_dir_800_12511()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=12512) as chmod_and_chown_801_12512:  # 0m:0.000s
                            chmod_and_chown_801_12512()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/GTR", prog_num=12513) as cd_stage_802_12513:  # 0m:0.035s
            cd_stage_802_12513()
            with Stage(r"copy", r"GTR Stomps v15.5.79.262", prog_num=12514):  # 0m:0.012s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12515) as should_copy_source_803_12515:  # ?
                    should_copy_source_803_12515()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=12516):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=12517) as copy_dir_to_dir_804_12517:  # ?
                            copy_dir_to_dir_804_12517()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=12518) as unwtar_805_12518:  # ?
                            unwtar_805_12518()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=12519, recursive=True) as chown_806_12519:  # 0m:0.000s
                            chown_806_12519()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12520) as should_copy_source_807_12520:  # ?
                    should_copy_source_807_12520()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=12521):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=12522) as copy_dir_to_dir_808_12522:  # ?
                            copy_dir_to_dir_808_12522()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=12523) as unwtar_809_12523:  # ?
                            unwtar_809_12523()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=12524, recursive=True) as chown_810_12524:  # 0m:0.000s
                            chown_810_12524()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12525) as should_copy_source_811_12525:  # ?
                    should_copy_source_811_12525()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=12526):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=12527) as copy_dir_to_dir_812_12527:  # ?
                            copy_dir_to_dir_812_12527()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=12528) as unwtar_813_12528:  # ?
                            unwtar_813_12528()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=12529, recursive=True) as chown_814_12529:  # 0m:0.000s
                            chown_814_12529()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12530) as should_copy_source_815_12530:  # ?
                    should_copy_source_815_12530()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=12531):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=12532) as copy_dir_to_dir_816_12532:  # ?
                            copy_dir_to_dir_816_12532()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=12533) as unwtar_817_12533:  # ?
                            unwtar_817_12533()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=12534, recursive=True) as chown_818_12534:  # 0m:0.000s
                            chown_818_12534()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12535) as should_copy_source_819_12535:  # ?
                    should_copy_source_819_12535()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=12536):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=12537) as copy_dir_to_dir_820_12537:  # ?
                            copy_dir_to_dir_820_12537()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=12538) as unwtar_821_12538:  # ?
                            unwtar_821_12538()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=12539, recursive=True) as chown_822_12539:  # 0m:0.000s
                            chown_822_12539()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12540) as should_copy_source_823_12540:  # ?
                    should_copy_source_823_12540()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=12541):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=12542) as copy_dir_to_dir_824_12542:  # ?
                            copy_dir_to_dir_824_12542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=12543) as unwtar_825_12543:  # ?
                            unwtar_825_12543()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=12544, recursive=True) as chown_826_12544:  # 0m:0.000s
                            chown_826_12544()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12545) as should_copy_source_827_12545:  # ?
                    should_copy_source_827_12545()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=12546):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=12547) as copy_dir_to_dir_828_12547:  # ?
                            copy_dir_to_dir_828_12547()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=12548) as unwtar_829_12548:  # ?
                            unwtar_829_12548()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=12549, recursive=True) as chown_830_12549:  # 0m:0.000s
                            chown_830_12549()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12550) as should_copy_source_831_12550:  # ?
                    should_copy_source_831_12550()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=12551):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=12552) as copy_dir_to_dir_832_12552:  # ?
                            copy_dir_to_dir_832_12552()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=12553) as unwtar_833_12553:  # ?
                            unwtar_833_12553()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=12554, recursive=True) as chown_834_12554:  # 0m:0.000s
                            chown_834_12554()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12555) as should_copy_source_835_12555:  # ?
                    should_copy_source_835_12555()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=12556):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12557) as copy_dir_to_dir_836_12557:  # ?
                            copy_dir_to_dir_836_12557()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=12558) as unwtar_837_12558:  # ?
                            unwtar_837_12558()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=12559, recursive=True) as chown_838_12559:  # 0m:0.000s
                            chown_838_12559()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12560) as should_copy_source_839_12560:  # ?
                    should_copy_source_839_12560()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=12561):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=12562) as copy_dir_to_dir_840_12562:  # ?
                            copy_dir_to_dir_840_12562()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=12563) as unwtar_841_12563:  # ?
                            unwtar_841_12563()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=12564, recursive=True) as chown_842_12564:  # 0m:0.000s
                            chown_842_12564()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12565) as should_copy_source_843_12565:  # ?
                    should_copy_source_843_12565()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=12566):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=12567) as copy_dir_to_dir_844_12567:  # ?
                            copy_dir_to_dir_844_12567()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=12568) as unwtar_845_12568:  # ?
                            unwtar_845_12568()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=12569, recursive=True) as chown_846_12569:  # 0m:0.000s
                            chown_846_12569()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12570) as should_copy_source_847_12570:  # ?
                    should_copy_source_847_12570()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=12571):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=12572) as copy_dir_to_dir_848_12572:  # ?
                            copy_dir_to_dir_848_12572()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=12573) as unwtar_849_12573:  # ?
                            unwtar_849_12573()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=12574, recursive=True) as chown_850_12574:  # 0m:0.000s
                            chown_850_12574()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12575) as should_copy_source_851_12575:  # ?
                    should_copy_source_851_12575()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=12576):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=12577) as copy_dir_to_dir_852_12577:  # ?
                            copy_dir_to_dir_852_12577()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=12578) as unwtar_853_12578:  # ?
                            unwtar_853_12578()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=12579, recursive=True) as chown_854_12579:  # 0m:0.000s
                            chown_854_12579()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12580) as should_copy_source_855_12580:  # ?
                    should_copy_source_855_12580()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=12581):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=12582) as copy_dir_to_dir_856_12582:  # ?
                            copy_dir_to_dir_856_12582()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=12583) as unwtar_857_12583:  # ?
                            unwtar_857_12583()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=12584, recursive=True) as chown_858_12584:  # 0m:0.000s
                            chown_858_12584()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12585) as should_copy_source_859_12585:  # ?
                    should_copy_source_859_12585()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=12586):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=12587) as copy_dir_to_dir_860_12587:  # ?
                            copy_dir_to_dir_860_12587()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=12588) as unwtar_861_12588:  # ?
                            unwtar_861_12588()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=12589, recursive=True) as chown_862_12589:  # 0m:0.000s
                            chown_862_12589()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12590) as should_copy_source_863_12590:  # ?
                    should_copy_source_863_12590()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=12591):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=12592) as copy_dir_to_dir_864_12592:  # ?
                            copy_dir_to_dir_864_12592()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=12593) as unwtar_865_12593:  # ?
                            unwtar_865_12593()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=12594, recursive=True) as chown_866_12594:  # 0m:0.005s
                            chown_866_12594()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12595) as should_copy_source_867_12595:  # ?
                    should_copy_source_867_12595()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=12596):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=12597) as copy_dir_to_dir_868_12597:  # ?
                            copy_dir_to_dir_868_12597()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=12598) as unwtar_869_12598:  # ?
                            unwtar_869_12598()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=12599, recursive=True) as chown_870_12599:  # 0m:0.000s
                            chown_870_12599()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12600) as should_copy_source_871_12600:  # ?
                    should_copy_source_871_12600()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=12601):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=12602) as copy_dir_to_dir_872_12602:  # ?
                            copy_dir_to_dir_872_12602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=12603) as unwtar_873_12603:  # ?
                            unwtar_873_12603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=12604, recursive=True) as chown_874_12604:  # 0m:0.000s
                            chown_874_12604()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12605) as should_copy_source_875_12605:  # ?
                    should_copy_source_875_12605()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=12606):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=12607) as copy_dir_to_dir_876_12607:  # ?
                            copy_dir_to_dir_876_12607()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=12608) as unwtar_877_12608:  # ?
                            unwtar_877_12608()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=12609, recursive=True) as chown_878_12609:  # 0m:0.000s
                            chown_878_12609()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12610) as should_copy_source_879_12610:  # ?
                    should_copy_source_879_12610()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=12611):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=12612) as copy_dir_to_dir_880_12612:  # ?
                            copy_dir_to_dir_880_12612()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=12613) as unwtar_881_12613:  # ?
                            unwtar_881_12613()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=12614, recursive=True) as chown_882_12614:  # 0m:0.000s
                            chown_882_12614()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12615) as should_copy_source_883_12615:  # ?
                    should_copy_source_883_12615()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=12616):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=12617) as copy_dir_to_dir_884_12617:  # ?
                            copy_dir_to_dir_884_12617()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=12618) as unwtar_885_12618:  # ?
                            unwtar_885_12618()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=12619, recursive=True) as chown_886_12619:  # 0m:0.000s
                            chown_886_12619()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12620) as should_copy_source_887_12620:  # ?
                    should_copy_source_887_12620()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=12621):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=12622) as copy_dir_to_dir_888_12622:  # ?
                            copy_dir_to_dir_888_12622()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=12623) as unwtar_889_12623:  # ?
                            unwtar_889_12623()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=12624, recursive=True) as chown_890_12624:  # 0m:0.000s
                            chown_890_12624()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12625) as should_copy_source_891_12625:  # ?
                    should_copy_source_891_12625()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=12626):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=12627) as copy_dir_to_dir_892_12627:  # ?
                            copy_dir_to_dir_892_12627()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=12628) as unwtar_893_12628:  # ?
                            unwtar_893_12628()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=12629, recursive=True) as chown_894_12629:  # 0m:0.000s
                            chown_894_12629()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12630) as should_copy_source_895_12630:  # ?
                    should_copy_source_895_12630()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=12631):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=12632) as copy_dir_to_dir_896_12632:  # ?
                            copy_dir_to_dir_896_12632()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=12633) as unwtar_897_12633:  # ?
                            unwtar_897_12633()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=12634, recursive=True) as chown_898_12634:  # 0m:0.000s
                            chown_898_12634()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12635) as should_copy_source_899_12635:  # ?
                    should_copy_source_899_12635()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=12636):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=12637) as copy_dir_to_dir_900_12637:  # ?
                            copy_dir_to_dir_900_12637()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=12638) as unwtar_901_12638:  # ?
                            unwtar_901_12638()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=12639, recursive=True) as chown_902_12639:  # 0m:0.000s
                            chown_902_12639()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12640) as shell_command_903_12640:  # 0m:0.023s
                shell_command_903_12640()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/ReWire", prog_num=12641) as cd_stage_904_12641:  # 0m:0.123s
            cd_stage_904_12641()
            with Stage(r"copy", r"backup ReWire to Waves folder", prog_num=12642):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12643) as should_copy_source_905_12643:  # ?
                    should_copy_source_905_12643()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=12644):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=12645) as copy_dir_to_dir_906_12645:  # ?
                            copy_dir_to_dir_906_12645()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=12646) as unwtar_907_12646:  # ?
                            unwtar_907_12646()
                        with Chown(path=r"/Applications/Waves/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=12647, recursive=True) as chown_908_12647:  # 0m:0.001s
                            chown_908_12647()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12648) as should_copy_source_909_12648:  # ?
                    should_copy_source_909_12648()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=12649):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=12650) as copy_dir_to_dir_910_12650:  # ?
                            copy_dir_to_dir_910_12650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=12651) as unwtar_911_12651:  # ?
                            unwtar_911_12651()
                        with Chown(path=r"/Applications/Waves/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=12652, recursive=True) as chown_912_12652:  # 0m:0.001s
                            chown_912_12652()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/ReWire" -c', ignore_all_errors=True, prog_num=12653) as shell_command_913_12653:  # 0m:0.096s
                shell_command_913_12653()
            with ScriptCommand(r'if [ -f "/Applications/Waves/ReWire"/Icon? ]; then chmod a+rw "/Applications/Waves/ReWire"/Icon?; fi', prog_num=12654) as script_command_914_12654:  # 0m:0.011s
                script_command_914_12654()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12655) as shell_command_915_12655:  # 0m:0.014s
                shell_command_915_12655()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=12656) as cd_stage_916_12656:  # 0m:0.022s
            cd_stage_916_12656()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12657):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12658) as should_copy_source_917_12658:  # ?
                    should_copy_source_917_12658()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12659):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12660) as copy_dir_to_dir_918_12660:  # ?
                            copy_dir_to_dir_918_12660()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12661) as unwtar_919_12661:  # ?
                            unwtar_919_12661()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12662, recursive=True) as chown_920_12662:  # ?
                            chown_920_12662()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12663) as shell_command_921_12663:  # 0m:0.001s
                            shell_command_921_12663()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12664):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12665) as should_copy_source_922_12665:  # ?
                    should_copy_source_922_12665()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12666):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12667) as copy_dir_to_dir_923_12667:  # ?
                            copy_dir_to_dir_923_12667()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12668) as unwtar_924_12668:  # ?
                            unwtar_924_12668()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12669, recursive=True) as chown_925_12669:  # ?
                            chown_925_12669()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12670) as shell_command_926_12670:  # 0m:0.001s
                            shell_command_926_12670()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=12671):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12672) as should_copy_source_927_12672:  # ?
                    should_copy_source_927_12672()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=12673):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=12674) as copy_dir_to_dir_928_12674:  # ?
                            copy_dir_to_dir_928_12674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=12675) as unwtar_929_12675:  # ?
                            unwtar_929_12675()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12676, recursive=True) as chown_930_12676:  # ?
                            chown_930_12676()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=12677) as break_hard_link_931_12677:  # ?
                            break_hard_link_931_12677()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=12678) as shell_command_932_12678:  # ?
                            shell_command_932_12678()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12679, recursive=True) as chown_933_12679:  # ?
                            chown_933_12679()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=12680, recursive=True) as chmod_934_12680:  # 0m:0.000s
                            chmod_934_12680()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=12681):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12682) as should_copy_source_935_12682:  # ?
                    should_copy_source_935_12682()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=12683):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=12684) as copy_dir_to_dir_936_12684:  # ?
                            copy_dir_to_dir_936_12684()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=12685) as unwtar_937_12685:  # ?
                            unwtar_937_12685()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12686, recursive=True) as chown_938_12686:  # ?
                            chown_938_12686()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=12687) as break_hard_link_939_12687:  # ?
                            break_hard_link_939_12687()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=12688) as shell_command_940_12688:  # ?
                            shell_command_940_12688()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12689, recursive=True) as chown_941_12689:  # ?
                            chown_941_12689()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=12690, recursive=True) as chmod_942_12690:  # 0m:0.000s
                            chmod_942_12690()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=12691):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12692) as should_copy_source_943_12692:  # ?
                    should_copy_source_943_12692()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=12693):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=12694) as copy_dir_to_dir_944_12694:  # ?
                            copy_dir_to_dir_944_12694()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=12695) as unwtar_945_12695:  # ?
                            unwtar_945_12695()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=12696, recursive=True) as chown_946_12696:  # ?
                            chown_946_12696()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=12697) as shell_command_947_12697:  # 0m:0.000s
                            shell_command_947_12697()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=12698):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12699) as should_copy_source_948_12699:  # ?
                    should_copy_source_948_12699()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=12700):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=12701) as copy_dir_to_dir_949_12701:  # ?
                            copy_dir_to_dir_949_12701()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=12702) as unwtar_950_12702:  # ?
                            unwtar_950_12702()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=12703, recursive=True) as chown_951_12703:  # ?
                            chown_951_12703()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=12704) as shell_command_952_12704:  # 0m:0.000s
                            shell_command_952_12704()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=12705):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12706) as should_copy_source_953_12706:  # ?
                    should_copy_source_953_12706()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=12707):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=12708) as copy_dir_to_dir_954_12708:  # ?
                            copy_dir_to_dir_954_12708()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=12709) as unwtar_955_12709:  # ?
                            unwtar_955_12709()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=12710, recursive=True) as chown_956_12710:  # ?
                            chown_956_12710()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12711) as shell_command_957_12711:  # ?
                            shell_command_957_12711()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12712) as script_command_958_12712:  # ?
                            script_command_958_12712()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12713) as shell_command_959_12713:  # 0m:0.001s
                            shell_command_959_12713()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=12714):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12715) as should_copy_source_960_12715:  # ?
                    should_copy_source_960_12715()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=12716):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=12717) as copy_dir_to_dir_961_12717:  # ?
                            copy_dir_to_dir_961_12717()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=12718) as unwtar_962_12718:  # ?
                            unwtar_962_12718()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=12719, recursive=True) as chown_963_12719:  # ?
                            chown_963_12719()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12720) as shell_command_964_12720:  # ?
                            shell_command_964_12720()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12721) as script_command_965_12721:  # ?
                            script_command_965_12721()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12722) as shell_command_966_12722:  # 0m:0.001s
                            shell_command_966_12722()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=12723):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=12724) as should_copy_source_967_12724:  # ?
                    should_copy_source_967_12724()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=12725):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=12726) as copy_dir_to_dir_968_12726:  # ?
                            copy_dir_to_dir_968_12726()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=12727) as unwtar_969_12727:  # ?
                            unwtar_969_12727()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=12728, recursive=True) as chown_970_12728:  # 0m:0.001s
                            chown_970_12728()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=12729) as shell_command_971_12729:  # 0m:0.012s
                shell_command_971_12729()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=12730) as cd_stage_972_12730:  # 0m:0.005s
            cd_stage_972_12730()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12731):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12732) as should_copy_source_973_12732:  # ?
                    should_copy_source_973_12732()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12733):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12734) as copy_dir_to_dir_974_12734:  # ?
                            copy_dir_to_dir_974_12734()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12735) as unwtar_975_12735:  # ?
                            unwtar_975_12735()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12736, recursive=True) as chown_976_12736:  # ?
                            chown_976_12736()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12737) as shell_command_977_12737:  # 0m:0.001s
                            shell_command_977_12737()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12738):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12739) as should_copy_source_978_12739:  # ?
                    should_copy_source_978_12739()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12740):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12741) as copy_dir_to_dir_979_12741:  # ?
                            copy_dir_to_dir_979_12741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12742) as unwtar_980_12742:  # ?
                            unwtar_980_12742()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12743, recursive=True) as chown_981_12743:  # ?
                            chown_981_12743()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12744) as shell_command_982_12744:  # 0m:0.001s
                            shell_command_982_12744()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=12745) as cd_stage_983_12745:  # 0m:0.170s
            cd_stage_983_12745()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=12746):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12747) as should_copy_source_984_12747:  # ?
                    should_copy_source_984_12747()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=12748):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=12749) as copy_file_to_dir_985_12749:  # ?
                            copy_file_to_dir_985_12749()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12750) as chmod_and_chown_986_12750:  # 0m:0.001s
                            chmod_and_chown_986_12750()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=12751):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12752) as should_copy_source_987_12752:  # ?
                    should_copy_source_987_12752()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=12753):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=12754) as copy_file_to_dir_988_12754:  # ?
                            copy_file_to_dir_988_12754()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12755) as chmod_and_chown_989_12755:  # 0m:0.000s
                            chmod_and_chown_989_12755()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=12756):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12757) as should_copy_source_990_12757:  # ?
                    should_copy_source_990_12757()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=12758):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=12759) as copy_file_to_dir_991_12759:  # ?
                            copy_file_to_dir_991_12759()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12760) as chmod_and_chown_992_12760:  # 0m:0.000s
                            chmod_and_chown_992_12760()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=12761):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12762) as should_copy_source_993_12762:  # ?
                    should_copy_source_993_12762()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=12763):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=12764) as copy_file_to_dir_994_12764:  # ?
                            copy_file_to_dir_994_12764()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12765) as chmod_and_chown_995_12765:  # 0m:0.000s
                            chmod_and_chown_995_12765()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=12766):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12767) as should_copy_source_996_12767:  # ?
                    should_copy_source_996_12767()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=12768):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=12769) as copy_file_to_dir_997_12769:  # ?
                            copy_file_to_dir_997_12769()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12770) as chmod_and_chown_998_12770:  # 0m:0.000s
                            chmod_and_chown_998_12770()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=12771):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12772) as should_copy_source_999_12772:  # ?
                    should_copy_source_999_12772()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=12773):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=12774) as copy_file_to_dir_1000_12774:  # ?
                            copy_file_to_dir_1000_12774()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12775) as chmod_and_chown_1001_12775:  # 0m:0.000s
                            chmod_and_chown_1001_12775()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=12776):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12777) as should_copy_source_1002_12777:  # ?
                    should_copy_source_1002_12777()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=12778):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=12779) as copy_file_to_dir_1003_12779:  # ?
                            copy_file_to_dir_1003_12779()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12780) as chmod_and_chown_1004_12780:  # 0m:0.000s
                            chmod_and_chown_1004_12780()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=12781):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12782) as should_copy_source_1005_12782:  # ?
                    should_copy_source_1005_12782()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=12783):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=12784) as copy_file_to_dir_1006_12784:  # ?
                            copy_file_to_dir_1006_12784()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12785) as chmod_and_chown_1007_12785:  # 0m:0.000s
                            chmod_and_chown_1007_12785()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=12786):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12787) as should_copy_source_1008_12787:  # ?
                    should_copy_source_1008_12787()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=12788):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=12789) as copy_file_to_dir_1009_12789:  # ?
                            copy_file_to_dir_1009_12789()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12790) as chmod_and_chown_1010_12790:  # 0m:0.006s
                            chmod_and_chown_1010_12790()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=12791):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12792) as should_copy_source_1011_12792:  # ?
                    should_copy_source_1011_12792()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=12793):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=12794) as copy_file_to_dir_1012_12794:  # ?
                            copy_file_to_dir_1012_12794()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12795) as chmod_and_chown_1013_12795:  # 0m:0.000s
                            chmod_and_chown_1013_12795()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=12796):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12797) as should_copy_source_1014_12797:  # ?
                    should_copy_source_1014_12797()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=12798):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=12799) as copy_file_to_dir_1015_12799:  # ?
                            copy_file_to_dir_1015_12799()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12800) as chmod_and_chown_1016_12800:  # 0m:0.000s
                            chmod_and_chown_1016_12800()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=12801):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12802) as should_copy_source_1017_12802:  # ?
                    should_copy_source_1017_12802()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=12803):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=12804) as copy_file_to_dir_1018_12804:  # ?
                            copy_file_to_dir_1018_12804()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12805) as chmod_and_chown_1019_12805:  # 0m:0.000s
                            chmod_and_chown_1019_12805()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=12806):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12807) as should_copy_source_1020_12807:  # ?
                    should_copy_source_1020_12807()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=12808):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=12809) as copy_file_to_dir_1021_12809:  # ?
                            copy_file_to_dir_1021_12809()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12810) as chmod_and_chown_1022_12810:  # 0m:0.000s
                            chmod_and_chown_1022_12810()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=12811):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12812) as should_copy_source_1023_12812:  # ?
                    should_copy_source_1023_12812()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=12813):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=12814) as copy_file_to_dir_1024_12814:  # ?
                            copy_file_to_dir_1024_12814()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12815) as chmod_and_chown_1025_12815:  # 0m:0.000s
                            chmod_and_chown_1025_12815()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=12816):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12817) as should_copy_source_1026_12817:  # ?
                    should_copy_source_1026_12817()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=12818):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=12819) as copy_file_to_dir_1027_12819:  # ?
                            copy_file_to_dir_1027_12819()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12820) as chmod_and_chown_1028_12820:  # 0m:0.000s
                            chmod_and_chown_1028_12820()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=12821):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12822) as should_copy_source_1029_12822:  # ?
                    should_copy_source_1029_12822()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=12823):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=12824) as copy_file_to_dir_1030_12824:  # ?
                            copy_file_to_dir_1030_12824()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12825) as chmod_and_chown_1031_12825:  # 0m:0.000s
                            chmod_and_chown_1031_12825()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=12826):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12827) as should_copy_source_1032_12827:  # ?
                    should_copy_source_1032_12827()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=12828):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=12829) as copy_file_to_dir_1033_12829:  # ?
                            copy_file_to_dir_1033_12829()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12830) as chmod_and_chown_1034_12830:  # 0m:0.000s
                            chmod_and_chown_1034_12830()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=12831):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12832) as should_copy_source_1035_12832:  # ?
                    should_copy_source_1035_12832()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=12833):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=12834) as copy_file_to_dir_1036_12834:  # ?
                            copy_file_to_dir_1036_12834()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12835) as chmod_and_chown_1037_12835:  # 0m:0.000s
                            chmod_and_chown_1037_12835()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=12836):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12837) as should_copy_source_1038_12837:  # ?
                    should_copy_source_1038_12837()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=12838):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=12839) as copy_file_to_dir_1039_12839:  # ?
                            copy_file_to_dir_1039_12839()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12840) as chmod_and_chown_1040_12840:  # 0m:0.000s
                            chmod_and_chown_1040_12840()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=12841):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12842) as should_copy_source_1041_12842:  # ?
                    should_copy_source_1041_12842()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=12843):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=12844) as copy_file_to_dir_1042_12844:  # ?
                            copy_file_to_dir_1042_12844()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12845) as chmod_and_chown_1043_12845:  # 0m:0.000s
                            chmod_and_chown_1043_12845()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=12846):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12847) as should_copy_source_1044_12847:  # ?
                    should_copy_source_1044_12847()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=12848):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=12849) as copy_file_to_dir_1045_12849:  # ?
                            copy_file_to_dir_1045_12849()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12850) as chmod_and_chown_1046_12850:  # 0m:0.000s
                            chmod_and_chown_1046_12850()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=12851):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12852) as should_copy_source_1047_12852:  # ?
                    should_copy_source_1047_12852()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=12853):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=12854) as copy_file_to_dir_1048_12854:  # ?
                            copy_file_to_dir_1048_12854()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12855) as chmod_and_chown_1049_12855:  # 0m:0.000s
                            chmod_and_chown_1049_12855()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=12856):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12857) as should_copy_source_1050_12857:  # ?
                    should_copy_source_1050_12857()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=12858):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=12859) as copy_file_to_dir_1051_12859:  # ?
                            copy_file_to_dir_1051_12859()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12860) as chmod_and_chown_1052_12860:  # 0m:0.000s
                            chmod_and_chown_1052_12860()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=12861):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12862) as should_copy_source_1053_12862:  # ?
                    should_copy_source_1053_12862()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=12863):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=12864) as copy_file_to_dir_1054_12864:  # ?
                            copy_file_to_dir_1054_12864()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12865) as chmod_and_chown_1055_12865:  # 0m:0.000s
                            chmod_and_chown_1055_12865()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=12866):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12867) as should_copy_source_1056_12867:  # ?
                    should_copy_source_1056_12867()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=12868):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=12869) as copy_file_to_dir_1057_12869:  # ?
                            copy_file_to_dir_1057_12869()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12870) as chmod_and_chown_1058_12870:  # 0m:0.000s
                            chmod_and_chown_1058_12870()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=12871):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12872) as should_copy_source_1059_12872:  # ?
                    should_copy_source_1059_12872()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=12873):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=12874) as copy_file_to_dir_1060_12874:  # ?
                            copy_file_to_dir_1060_12874()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12875) as chmod_and_chown_1061_12875:  # 0m:0.000s
                            chmod_and_chown_1061_12875()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=12876):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12877) as should_copy_source_1062_12877:  # ?
                    should_copy_source_1062_12877()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=12878):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=12879) as copy_file_to_dir_1063_12879:  # ?
                            copy_file_to_dir_1063_12879()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12880) as chmod_and_chown_1064_12880:  # 0m:0.000s
                            chmod_and_chown_1064_12880()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=12881):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12882) as should_copy_source_1065_12882:  # ?
                    should_copy_source_1065_12882()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=12883):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=12884) as copy_file_to_dir_1066_12884:  # ?
                            copy_file_to_dir_1066_12884()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12885) as chmod_and_chown_1067_12885:  # 0m:0.005s
                            chmod_and_chown_1067_12885()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=12886):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12887) as should_copy_source_1068_12887:  # ?
                    should_copy_source_1068_12887()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=12888):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=12889) as copy_file_to_dir_1069_12889:  # ?
                            copy_file_to_dir_1069_12889()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12890) as chmod_and_chown_1070_12890:  # 0m:0.000s
                            chmod_and_chown_1070_12890()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=12891):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12892) as should_copy_source_1071_12892:  # ?
                    should_copy_source_1071_12892()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=12893):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=12894) as copy_file_to_dir_1072_12894:  # ?
                            copy_file_to_dir_1072_12894()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12895) as chmod_and_chown_1073_12895:  # 0m:0.000s
                            chmod_and_chown_1073_12895()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=12896):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12897) as should_copy_source_1074_12897:  # ?
                    should_copy_source_1074_12897()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=12898):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=12899) as copy_file_to_dir_1075_12899:  # ?
                            copy_file_to_dir_1075_12899()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12900) as chmod_and_chown_1076_12900:  # 0m:0.000s
                            chmod_and_chown_1076_12900()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=12901):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12902) as should_copy_source_1077_12902:  # ?
                    should_copy_source_1077_12902()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=12903):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=12904) as copy_file_to_dir_1078_12904:  # ?
                            copy_file_to_dir_1078_12904()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12905) as chmod_and_chown_1079_12905:  # 0m:0.000s
                            chmod_and_chown_1079_12905()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=12906):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12907) as should_copy_source_1080_12907:  # ?
                    should_copy_source_1080_12907()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=12908):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=12909) as copy_file_to_dir_1081_12909:  # ?
                            copy_file_to_dir_1081_12909()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12910) as chmod_and_chown_1082_12910:  # 0m:0.000s
                            chmod_and_chown_1082_12910()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=12911):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12912) as should_copy_source_1083_12912:  # ?
                    should_copy_source_1083_12912()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=12913):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=12914) as copy_file_to_dir_1084_12914:  # ?
                            copy_file_to_dir_1084_12914()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12915) as chmod_and_chown_1085_12915:  # 0m:0.000s
                            chmod_and_chown_1085_12915()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=12916):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12917) as should_copy_source_1086_12917:  # ?
                    should_copy_source_1086_12917()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=12918):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=12919) as copy_file_to_dir_1087_12919:  # ?
                            copy_file_to_dir_1087_12919()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12920) as chmod_and_chown_1088_12920:  # 0m:0.000s
                            chmod_and_chown_1088_12920()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=12921):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12922) as should_copy_source_1089_12922:  # ?
                    should_copy_source_1089_12922()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=12923):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=12924) as copy_file_to_dir_1090_12924:  # ?
                            copy_file_to_dir_1090_12924()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12925) as chmod_and_chown_1091_12925:  # 0m:0.000s
                            chmod_and_chown_1091_12925()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=12926):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12927) as should_copy_source_1092_12927:  # ?
                    should_copy_source_1092_12927()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=12928):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=12929) as copy_file_to_dir_1093_12929:  # ?
                            copy_file_to_dir_1093_12929()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12930) as chmod_and_chown_1094_12930:  # 0m:0.000s
                            chmod_and_chown_1094_12930()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=12931):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12932) as should_copy_source_1095_12932:  # ?
                    should_copy_source_1095_12932()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=12933):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=12934) as copy_file_to_dir_1096_12934:  # ?
                            copy_file_to_dir_1096_12934()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12935) as chmod_and_chown_1097_12935:  # 0m:0.000s
                            chmod_and_chown_1097_12935()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=12936):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12937) as should_copy_source_1098_12937:  # ?
                    should_copy_source_1098_12937()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=12938):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=12939) as copy_file_to_dir_1099_12939:  # ?
                            copy_file_to_dir_1099_12939()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12940) as chmod_and_chown_1100_12940:  # 0m:0.000s
                            chmod_and_chown_1100_12940()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=12941):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12942) as should_copy_source_1101_12942:  # ?
                    should_copy_source_1101_12942()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=12943):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=12944) as copy_file_to_dir_1102_12944:  # ?
                            copy_file_to_dir_1102_12944()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12945) as chmod_and_chown_1103_12945:  # 0m:0.000s
                            chmod_and_chown_1103_12945()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=12946):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12947) as should_copy_source_1104_12947:  # ?
                    should_copy_source_1104_12947()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=12948):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=12949) as copy_file_to_dir_1105_12949:  # ?
                            copy_file_to_dir_1105_12949()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12950) as chmod_and_chown_1106_12950:  # 0m:0.000s
                            chmod_and_chown_1106_12950()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=12951):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12952) as should_copy_source_1107_12952:  # ?
                    should_copy_source_1107_12952()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=12953):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=12954) as copy_file_to_dir_1108_12954:  # ?
                            copy_file_to_dir_1108_12954()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12955) as chmod_and_chown_1109_12955:  # 0m:0.000s
                            chmod_and_chown_1109_12955()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=12956):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12957) as should_copy_source_1110_12957:  # ?
                    should_copy_source_1110_12957()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=12958):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=12959) as copy_file_to_dir_1111_12959:  # ?
                            copy_file_to_dir_1111_12959()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12960) as chmod_and_chown_1112_12960:  # 0m:0.000s
                            chmod_and_chown_1112_12960()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=12961):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12962) as should_copy_source_1113_12962:  # ?
                    should_copy_source_1113_12962()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=12963):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=12964) as copy_file_to_dir_1114_12964:  # ?
                            copy_file_to_dir_1114_12964()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12965) as chmod_and_chown_1115_12965:  # 0m:0.000s
                            chmod_and_chown_1115_12965()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=12966):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12967) as should_copy_source_1116_12967:  # ?
                    should_copy_source_1116_12967()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=12968):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=12969) as copy_file_to_dir_1117_12969:  # ?
                            copy_file_to_dir_1117_12969()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12970) as chmod_and_chown_1118_12970:  # 0m:0.000s
                            chmod_and_chown_1118_12970()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=12971):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12972) as should_copy_source_1119_12972:  # ?
                    should_copy_source_1119_12972()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=12973):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=12974) as copy_file_to_dir_1120_12974:  # ?
                            copy_file_to_dir_1120_12974()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12975) as chmod_and_chown_1121_12975:  # 0m:0.000s
                            chmod_and_chown_1121_12975()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=12976):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12977) as should_copy_source_1122_12977:  # ?
                    should_copy_source_1122_12977()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=12978):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=12979) as copy_file_to_dir_1123_12979:  # ?
                            copy_file_to_dir_1123_12979()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12980) as chmod_and_chown_1124_12980:  # 0m:0.000s
                            chmod_and_chown_1124_12980()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=12981):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12982) as should_copy_source_1125_12982:  # ?
                    should_copy_source_1125_12982()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=12983):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=12984) as copy_file_to_dir_1126_12984:  # ?
                            copy_file_to_dir_1126_12984()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12985) as chmod_and_chown_1127_12985:  # 0m:0.004s
                            chmod_and_chown_1127_12985()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12986) as should_copy_source_1128_12986:  # ?
                    should_copy_source_1128_12986()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=12987):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=12988) as copy_file_to_dir_1129_12988:  # ?
                            copy_file_to_dir_1129_12988()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12989) as chmod_and_chown_1130_12989:  # 0m:0.000s
                            chmod_and_chown_1130_12989()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=12990):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12991) as should_copy_source_1131_12991:  # ?
                    should_copy_source_1131_12991()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=12992):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=12993) as copy_file_to_dir_1132_12993:  # ?
                            copy_file_to_dir_1132_12993()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12994) as chmod_and_chown_1133_12994:  # 0m:0.000s
                            chmod_and_chown_1133_12994()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=12995):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12996) as should_copy_source_1134_12996:  # ?
                    should_copy_source_1134_12996()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=12997):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=12998) as copy_file_to_dir_1135_12998:  # ?
                            copy_file_to_dir_1135_12998()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12999) as chmod_and_chown_1136_12999:  # 0m:0.000s
                            chmod_and_chown_1136_12999()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=13000):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13001) as should_copy_source_1137_13001:  # ?
                    should_copy_source_1137_13001()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=13002):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=13003) as copy_file_to_dir_1138_13003:  # ?
                            copy_file_to_dir_1138_13003()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13004) as chmod_and_chown_1139_13004:  # 0m:0.000s
                            chmod_and_chown_1139_13004()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=13005):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13006) as should_copy_source_1140_13006:  # ?
                    should_copy_source_1140_13006()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=13007):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=13008) as copy_file_to_dir_1141_13008:  # ?
                            copy_file_to_dir_1141_13008()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13009) as chmod_and_chown_1142_13009:  # 0m:0.000s
                            chmod_and_chown_1142_13009()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=13010):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13011) as should_copy_source_1143_13011:  # ?
                    should_copy_source_1143_13011()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=13012):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=13013) as copy_file_to_dir_1144_13013:  # ?
                            copy_file_to_dir_1144_13013()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13014) as chmod_and_chown_1145_13014:  # 0m:0.000s
                            chmod_and_chown_1145_13014()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=13015):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13016) as should_copy_source_1146_13016:  # ?
                    should_copy_source_1146_13016()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=13017):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=13018) as copy_file_to_dir_1147_13018:  # ?
                            copy_file_to_dir_1147_13018()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13019) as chmod_and_chown_1148_13019:  # 0m:0.000s
                            chmod_and_chown_1148_13019()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=13020):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13021) as should_copy_source_1149_13021:  # ?
                    should_copy_source_1149_13021()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=13022):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=13023) as copy_file_to_dir_1150_13023:  # ?
                            copy_file_to_dir_1150_13023()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13024) as chmod_and_chown_1151_13024:  # 0m:0.000s
                            chmod_and_chown_1151_13024()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=13025):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13026) as should_copy_source_1152_13026:  # ?
                    should_copy_source_1152_13026()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=13027):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=13028) as copy_file_to_dir_1153_13028:  # ?
                            copy_file_to_dir_1153_13028()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13029) as chmod_and_chown_1154_13029:  # 0m:0.000s
                            chmod_and_chown_1154_13029()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=13030):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13031) as should_copy_source_1155_13031:  # ?
                    should_copy_source_1155_13031()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=13032):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=13033) as copy_file_to_dir_1156_13033:  # ?
                            copy_file_to_dir_1156_13033()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13034) as chmod_and_chown_1157_13034:  # 0m:0.000s
                            chmod_and_chown_1157_13034()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=13035):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13036) as should_copy_source_1158_13036:  # ?
                    should_copy_source_1158_13036()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=13037):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=13038) as copy_file_to_dir_1159_13038:  # ?
                            copy_file_to_dir_1159_13038()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13039) as chmod_and_chown_1160_13039:  # 0m:0.000s
                            chmod_and_chown_1160_13039()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=13040):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13041) as should_copy_source_1161_13041:  # ?
                    should_copy_source_1161_13041()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=13042):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=13043) as copy_file_to_dir_1162_13043:  # ?
                            copy_file_to_dir_1162_13043()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13044) as chmod_and_chown_1163_13044:  # 0m:0.000s
                            chmod_and_chown_1163_13044()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=13045):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13046) as should_copy_source_1164_13046:  # ?
                    should_copy_source_1164_13046()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=13047):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=13048) as copy_file_to_dir_1165_13048:  # ?
                            copy_file_to_dir_1165_13048()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13049) as chmod_and_chown_1166_13049:  # 0m:0.000s
                            chmod_and_chown_1166_13049()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=13050):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13051) as should_copy_source_1167_13051:  # ?
                    should_copy_source_1167_13051()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=13052):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=13053) as copy_file_to_dir_1168_13053:  # ?
                            copy_file_to_dir_1168_13053()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13054) as chmod_and_chown_1169_13054:  # 0m:0.000s
                            chmod_and_chown_1169_13054()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=13055):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13056) as should_copy_source_1170_13056:  # ?
                    should_copy_source_1170_13056()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=13057):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=13058) as copy_file_to_dir_1171_13058:  # ?
                            copy_file_to_dir_1171_13058()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13059) as chmod_and_chown_1172_13059:  # 0m:0.000s
                            chmod_and_chown_1172_13059()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=13060):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13061) as should_copy_source_1173_13061:  # ?
                    should_copy_source_1173_13061()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=13062):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=13063) as copy_file_to_dir_1174_13063:  # ?
                            copy_file_to_dir_1174_13063()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13064) as chmod_and_chown_1175_13064:  # 0m:0.000s
                            chmod_and_chown_1175_13064()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=13065):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13066) as should_copy_source_1176_13066:  # ?
                    should_copy_source_1176_13066()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=13067):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=13068) as copy_file_to_dir_1177_13068:  # ?
                            copy_file_to_dir_1177_13068()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13069) as chmod_and_chown_1178_13069:  # 0m:0.000s
                            chmod_and_chown_1178_13069()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=13070):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13071) as should_copy_source_1179_13071:  # ?
                    should_copy_source_1179_13071()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=13072):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=13073) as copy_file_to_dir_1180_13073:  # ?
                            copy_file_to_dir_1180_13073()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13074) as chmod_and_chown_1181_13074:  # 0m:0.000s
                            chmod_and_chown_1181_13074()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=13075):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13076) as should_copy_source_1182_13076:  # ?
                    should_copy_source_1182_13076()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=13077):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=13078) as copy_file_to_dir_1183_13078:  # ?
                            copy_file_to_dir_1183_13078()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13079) as chmod_and_chown_1184_13079:  # 0m:0.000s
                            chmod_and_chown_1184_13079()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=13080):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13081) as should_copy_source_1185_13081:  # ?
                    should_copy_source_1185_13081()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=13082):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=13083) as copy_file_to_dir_1186_13083:  # ?
                            copy_file_to_dir_1186_13083()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13084) as chmod_and_chown_1187_13084:  # 0m:0.000s
                            chmod_and_chown_1187_13084()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=13085):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13086) as should_copy_source_1188_13086:  # ?
                    should_copy_source_1188_13086()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=13087):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=13088) as copy_file_to_dir_1189_13088:  # ?
                            copy_file_to_dir_1189_13088()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13089) as chmod_and_chown_1190_13089:  # 0m:0.000s
                            chmod_and_chown_1190_13089()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=13090):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13091) as should_copy_source_1191_13091:  # ?
                    should_copy_source_1191_13091()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=13092):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=13093) as copy_file_to_dir_1192_13093:  # ?
                            copy_file_to_dir_1192_13093()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13094) as chmod_and_chown_1193_13094:  # 0m:0.000s
                            chmod_and_chown_1193_13094()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=13095):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13096) as should_copy_source_1194_13096:  # ?
                    should_copy_source_1194_13096()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=13097):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=13098) as copy_file_to_dir_1195_13098:  # ?
                            copy_file_to_dir_1195_13098()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13099) as chmod_and_chown_1196_13099:  # 0m:0.000s
                            chmod_and_chown_1196_13099()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=13100):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13101) as should_copy_source_1197_13101:  # ?
                    should_copy_source_1197_13101()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=13102):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=13103) as copy_file_to_dir_1198_13103:  # ?
                            copy_file_to_dir_1198_13103()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13104) as chmod_and_chown_1199_13104:  # 0m:0.005s
                            chmod_and_chown_1199_13104()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=13105):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13106) as should_copy_source_1200_13106:  # ?
                    should_copy_source_1200_13106()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=13107):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=13108) as copy_file_to_dir_1201_13108:  # ?
                            copy_file_to_dir_1201_13108()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13109) as chmod_and_chown_1202_13109:  # 0m:0.000s
                            chmod_and_chown_1202_13109()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=13110):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13111) as should_copy_source_1203_13111:  # ?
                    should_copy_source_1203_13111()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=13112):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=13113) as copy_file_to_dir_1204_13113:  # ?
                            copy_file_to_dir_1204_13113()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13114) as chmod_and_chown_1205_13114:  # 0m:0.000s
                            chmod_and_chown_1205_13114()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=13115):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13116) as should_copy_source_1206_13116:  # ?
                    should_copy_source_1206_13116()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=13117):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=13118) as copy_file_to_dir_1207_13118:  # ?
                            copy_file_to_dir_1207_13118()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13119) as chmod_and_chown_1208_13119:  # 0m:0.000s
                            chmod_and_chown_1208_13119()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=13120):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13121) as should_copy_source_1209_13121:  # ?
                    should_copy_source_1209_13121()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=13122):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=13123) as copy_file_to_dir_1210_13123:  # ?
                            copy_file_to_dir_1210_13123()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13124) as chmod_and_chown_1211_13124:  # 0m:0.000s
                            chmod_and_chown_1211_13124()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=13125):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13126) as should_copy_source_1212_13126:  # ?
                    should_copy_source_1212_13126()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=13127):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=13128) as copy_file_to_dir_1213_13128:  # ?
                            copy_file_to_dir_1213_13128()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13129) as chmod_and_chown_1214_13129:  # 0m:0.000s
                            chmod_and_chown_1214_13129()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13130) as should_copy_source_1215_13130:  # ?
                    should_copy_source_1215_13130()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=13131):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=13132) as copy_file_to_dir_1216_13132:  # ?
                            copy_file_to_dir_1216_13132()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13133) as chmod_and_chown_1217_13133:  # 0m:0.000s
                            chmod_and_chown_1217_13133()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13134) as should_copy_source_1218_13134:  # ?
                    should_copy_source_1218_13134()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=13135):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=13136) as copy_file_to_dir_1219_13136:  # ?
                            copy_file_to_dir_1219_13136()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13137) as chmod_and_chown_1220_13137:  # 0m:0.000s
                            chmod_and_chown_1220_13137()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=13138):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13139) as should_copy_source_1221_13139:  # ?
                    should_copy_source_1221_13139()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=13140):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=13141) as copy_file_to_dir_1222_13141:  # ?
                            copy_file_to_dir_1222_13141()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13142) as chmod_and_chown_1223_13142:  # 0m:0.000s
                            chmod_and_chown_1223_13142()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=13143):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13144) as should_copy_source_1224_13144:  # ?
                    should_copy_source_1224_13144()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=13145):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=13146) as copy_file_to_dir_1225_13146:  # ?
                            copy_file_to_dir_1225_13146()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13147) as chmod_and_chown_1226_13147:  # 0m:0.000s
                            chmod_and_chown_1226_13147()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=13148):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13149) as should_copy_source_1227_13149:  # ?
                    should_copy_source_1227_13149()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=13150):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=13151) as copy_file_to_dir_1228_13151:  # ?
                            copy_file_to_dir_1228_13151()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13152) as chmod_and_chown_1229_13152:  # 0m:0.000s
                            chmod_and_chown_1229_13152()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=13153):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13154) as should_copy_source_1230_13154:  # ?
                    should_copy_source_1230_13154()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=13155):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=13156) as copy_file_to_dir_1231_13156:  # ?
                            copy_file_to_dir_1231_13156()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13157) as chmod_and_chown_1232_13157:  # 0m:0.000s
                            chmod_and_chown_1232_13157()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=13158):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13159) as should_copy_source_1233_13159:  # ?
                    should_copy_source_1233_13159()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=13160):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=13161) as copy_file_to_dir_1234_13161:  # ?
                            copy_file_to_dir_1234_13161()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13162) as chmod_and_chown_1235_13162:  # 0m:0.000s
                            chmod_and_chown_1235_13162()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=13163):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13164) as should_copy_source_1236_13164:  # ?
                    should_copy_source_1236_13164()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=13165):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=13166) as copy_file_to_dir_1237_13166:  # ?
                            copy_file_to_dir_1237_13166()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13167) as chmod_and_chown_1238_13167:  # 0m:0.000s
                            chmod_and_chown_1238_13167()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=13168):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13169) as should_copy_source_1239_13169:  # ?
                    should_copy_source_1239_13169()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=13170):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=13171) as copy_file_to_dir_1240_13171:  # ?
                            copy_file_to_dir_1240_13171()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13172) as chmod_and_chown_1241_13172:  # 0m:0.000s
                            chmod_and_chown_1241_13172()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=13173):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13174) as should_copy_source_1242_13174:  # ?
                    should_copy_source_1242_13174()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=13175):  # ?
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=13176) as copy_file_to_dir_1243_13176:  # ?
                            copy_file_to_dir_1243_13176()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13177) as chmod_and_chown_1244_13177:  # 0m:0.000s
                            chmod_and_chown_1244_13177()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=13178) as resolve_config_vars_in_file_1245_13178:  # 0m:0.001s
                resolve_config_vars_in_file_1245_13178()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=13179) as if_1246_13179:  # 0m:0.006s
                if_1246_13179()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=13180) as resolve_config_vars_in_file_1247_13180:  # 0m:0.001s
                resolve_config_vars_in_file_1247_13180()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=13181) as if_1248_13181:  # 0m:0.000s
                if_1248_13181()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=13182) as resolve_config_vars_in_file_1249_13182:  # 0m:0.000s
                resolve_config_vars_in_file_1249_13182()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=13183) as if_1250_13183:  # 0m:0.000s
                if_1250_13183()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=13184) as resolve_config_vars_in_file_1251_13184:  # 0m:0.000s
                resolve_config_vars_in_file_1251_13184()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=13185) as if_1252_13185:  # 0m:0.000s
                if_1252_13185()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=13186) as resolve_config_vars_in_file_1253_13186:  # 0m:0.000s
                resolve_config_vars_in_file_1253_13186()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=13187) as if_1254_13187:  # 0m:0.000s
                if_1254_13187()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13188) as resolve_config_vars_in_file_1255_13188:  # 0m:0.000s
                resolve_config_vars_in_file_1255_13188()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=13189) as if_1256_13189:  # 0m:0.000s
                if_1256_13189()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=13190) as resolve_config_vars_in_file_1257_13190:  # 0m:0.000s
                resolve_config_vars_in_file_1257_13190()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=13191) as if_1258_13191:  # 0m:0.000s
                if_1258_13191()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=13192) as resolve_config_vars_in_file_1259_13192:  # 0m:0.000s
                resolve_config_vars_in_file_1259_13192()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=13193) as if_1260_13193:  # 0m:0.001s
                if_1260_13193()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=13194) as resolve_config_vars_in_file_1261_13194:  # 0m:0.005s
                resolve_config_vars_in_file_1261_13194()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=13195) as if_1262_13195:  # 0m:0.001s
                if_1262_13195()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=13196) as resolve_config_vars_in_file_1263_13196:  # 0m:0.000s
                resolve_config_vars_in_file_1263_13196()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=13197) as if_1264_13197:  # 0m:0.000s
                if_1264_13197()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=13198) as resolve_config_vars_in_file_1265_13198:  # 0m:0.000s
                resolve_config_vars_in_file_1265_13198()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=13199) as if_1266_13199:  # 0m:0.000s
                if_1266_13199()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=13200) as resolve_config_vars_in_file_1267_13200:  # 0m:0.000s
                resolve_config_vars_in_file_1267_13200()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=13201) as if_1268_13201:  # 0m:0.000s
                if_1268_13201()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=13202) as resolve_config_vars_in_file_1269_13202:  # 0m:0.000s
                resolve_config_vars_in_file_1269_13202()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=13203) as if_1270_13203:  # 0m:0.000s
                if_1270_13203()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=13204) as resolve_config_vars_in_file_1271_13204:  # 0m:0.000s
                resolve_config_vars_in_file_1271_13204()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=13205) as if_1272_13205:  # 0m:0.000s
                if_1272_13205()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=13206) as resolve_config_vars_in_file_1273_13206:  # 0m:0.000s
                resolve_config_vars_in_file_1273_13206()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=13207) as if_1274_13207:  # 0m:0.004s
                if_1274_13207()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=13208) as resolve_config_vars_in_file_1275_13208:  # 0m:0.001s
                resolve_config_vars_in_file_1275_13208()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=13209) as if_1276_13209:  # 0m:0.000s
                if_1276_13209()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13210) as resolve_config_vars_in_file_1277_13210:  # 0m:0.000s
                resolve_config_vars_in_file_1277_13210()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=13211) as if_1278_13211:  # 0m:0.000s
                if_1278_13211()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13212) as resolve_config_vars_in_file_1279_13212:  # 0m:0.000s
                resolve_config_vars_in_file_1279_13212()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=13213) as if_1280_13213:  # 0m:0.000s
                if_1280_13213()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13214) as resolve_config_vars_in_file_1281_13214:  # 0m:0.000s
                resolve_config_vars_in_file_1281_13214()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=13215) as if_1282_13215:  # 0m:0.000s
                if_1282_13215()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=13216) as resolve_config_vars_in_file_1283_13216:  # 0m:0.000s
                resolve_config_vars_in_file_1283_13216()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=13217) as if_1284_13217:  # 0m:0.000s
                if_1284_13217()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=13218) as resolve_config_vars_in_file_1285_13218:  # 0m:0.000s
                resolve_config_vars_in_file_1285_13218()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=13219) as if_1286_13219:  # 0m:0.000s
                if_1286_13219()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=13220) as resolve_config_vars_in_file_1287_13220:  # 0m:0.001s
                resolve_config_vars_in_file_1287_13220()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=13221) as if_1288_13221:  # 0m:0.005s
                if_1288_13221()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=13222) as resolve_config_vars_in_file_1289_13222:  # 0m:0.001s
                resolve_config_vars_in_file_1289_13222()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=13223) as if_1290_13223:  # 0m:0.001s
                if_1290_13223()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13224) as resolve_config_vars_in_file_1291_13224:  # 0m:0.000s
                resolve_config_vars_in_file_1291_13224()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=13225) as if_1292_13225:  # 0m:0.000s
                if_1292_13225()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=13226) as rm_file_or_dir_1293_13226:  # 0m:0.000s
                rm_file_or_dir_1293_13226()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=13227) as resolve_config_vars_in_file_1294_13227:  # 0m:0.000s
                resolve_config_vars_in_file_1294_13227()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=13228) as if_1295_13228:  # 0m:0.000s
                if_1295_13228()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=13229) as rm_file_or_dir_1296_13229:  # 0m:0.000s
                rm_file_or_dir_1296_13229()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=13230) as resolve_config_vars_in_file_1297_13230:  # 0m:0.000s
                resolve_config_vars_in_file_1297_13230()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=13231) as if_1298_13231:  # 0m:0.000s
                if_1298_13231()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=13232) as resolve_config_vars_in_file_1299_13232:  # 0m:0.000s
                resolve_config_vars_in_file_1299_13232()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=13233) as if_1300_13233:  # 0m:0.000s
                if_1300_13233()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=13234) as resolve_config_vars_in_file_1301_13234:  # 0m:0.000s
                resolve_config_vars_in_file_1301_13234()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=13235) as if_1302_13235:  # 0m:0.000s
                if_1302_13235()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=13236) as resolve_config_vars_in_file_1303_13236:  # 0m:0.000s
                resolve_config_vars_in_file_1303_13236()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=13237) as if_1304_13237:  # 0m:0.001s
                if_1304_13237()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=13238) as resolve_config_vars_in_file_1305_13238:  # 0m:0.000s
                resolve_config_vars_in_file_1305_13238()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=13239) as if_1306_13239:  # 0m:0.006s
                if_1306_13239()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=13240) as resolve_config_vars_in_file_1307_13240:  # 0m:0.001s
                resolve_config_vars_in_file_1307_13240()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=13241) as if_1308_13241:  # 0m:0.000s
                if_1308_13241()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13242) as resolve_config_vars_in_file_1309_13242:  # 0m:0.000s
                resolve_config_vars_in_file_1309_13242()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=13243) as if_1310_13243:  # 0m:0.000s
                if_1310_13243()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13244) as resolve_config_vars_in_file_1311_13244:  # 0m:0.000s
                resolve_config_vars_in_file_1311_13244()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=13245) as if_1312_13245:  # 0m:0.000s
                if_1312_13245()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=13246) as resolve_config_vars_in_file_1313_13246:  # 0m:0.000s
                resolve_config_vars_in_file_1313_13246()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=13247) as if_1314_13247:  # 0m:0.000s
                if_1314_13247()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=13248) as resolve_config_vars_in_file_1315_13248:  # 0m:0.000s
                resolve_config_vars_in_file_1315_13248()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=13249) as if_1316_13249:  # 0m:0.000s
                if_1316_13249()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=13250) as resolve_config_vars_in_file_1317_13250:  # 0m:0.000s
                resolve_config_vars_in_file_1317_13250()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=13251) as if_1318_13251:  # 0m:0.001s
                if_1318_13251()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13252) as resolve_config_vars_in_file_1319_13252:  # 0m:0.000s
                resolve_config_vars_in_file_1319_13252()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=13253) as if_1320_13253:  # 0m:0.005s
                if_1320_13253()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=13254) as resolve_config_vars_in_file_1321_13254:  # 0m:0.000s
                resolve_config_vars_in_file_1321_13254()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=13255) as if_1322_13255:  # 0m:0.000s
                if_1322_13255()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=13256) as resolve_config_vars_in_file_1323_13256:  # 0m:0.000s
                resolve_config_vars_in_file_1323_13256()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=13257) as if_1324_13257:  # 0m:0.000s
                if_1324_13257()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=13258) as resolve_config_vars_in_file_1325_13258:  # 0m:0.002s
                resolve_config_vars_in_file_1325_13258()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=13259) as if_1326_13259:  # 0m:0.000s
                if_1326_13259()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=13260) as resolve_config_vars_in_file_1327_13260:  # 0m:0.000s
                resolve_config_vars_in_file_1327_13260()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=13261) as if_1328_13261:  # 0m:0.001s
                if_1328_13261()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=13262) as resolve_config_vars_in_file_1329_13262:  # 0m:0.004s
                resolve_config_vars_in_file_1329_13262()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=13263) as if_1330_13263:  # 0m:0.001s
                if_1330_13263()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=13264) as resolve_config_vars_in_file_1331_13264:  # 0m:0.000s
                resolve_config_vars_in_file_1331_13264()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=13265) as if_1332_13265:  # 0m:0.000s
                if_1332_13265()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=13266) as resolve_config_vars_in_file_1333_13266:  # 0m:0.000s
                resolve_config_vars_in_file_1333_13266()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=13267) as if_1334_13267:  # 0m:0.000s
                if_1334_13267()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=13268) as resolve_config_vars_in_file_1335_13268:  # 0m:0.000s
                resolve_config_vars_in_file_1335_13268()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=13269) as if_1336_13269:  # 0m:0.000s
                if_1336_13269()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=13270) as resolve_config_vars_in_file_1337_13270:  # 0m:0.001s
                resolve_config_vars_in_file_1337_13270()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=13271) as if_1338_13271:  # 0m:0.000s
                if_1338_13271()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=13272) as resolve_config_vars_in_file_1339_13272:  # 0m:0.000s
                resolve_config_vars_in_file_1339_13272()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=13273) as if_1340_13273:  # 0m:0.000s
                if_1340_13273()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=13274) as resolve_config_vars_in_file_1341_13274:  # 0m:0.000s
                resolve_config_vars_in_file_1341_13274()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=13275) as if_1342_13275:  # 0m:0.000s
                if_1342_13275()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=13276) as move_file_to_file_1343_13276:  # 0m:0.012s
                move_file_to_file_1343_13276()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=13277) as resolve_config_vars_in_file_1344_13277:  # 0m:0.001s
                resolve_config_vars_in_file_1344_13277()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=13278) as if_1345_13278:  # 0m:0.000s
                if_1345_13278()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=13279) as resolve_config_vars_in_file_1346_13279:  # 0m:0.000s
                resolve_config_vars_in_file_1346_13279()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=13280) as if_1347_13280:  # 0m:0.000s
                if_1347_13280()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=13281) as resolve_config_vars_in_file_1348_13281:  # 0m:0.000s
                resolve_config_vars_in_file_1348_13281()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=13282) as if_1349_13282:  # 0m:0.000s
                if_1349_13282()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=13283) as resolve_config_vars_in_file_1350_13283:  # 0m:0.000s
                resolve_config_vars_in_file_1350_13283()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=13284) as if_1351_13284:  # 0m:0.000s
                if_1351_13284()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=13285) as resolve_config_vars_in_file_1352_13285:  # 0m:0.000s
                resolve_config_vars_in_file_1352_13285()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=13286) as if_1353_13286:  # 0m:0.000s
                if_1353_13286()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13287) as resolve_config_vars_in_file_1354_13287:  # 0m:0.000s
                resolve_config_vars_in_file_1354_13287()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=13288) as if_1355_13288:  # 0m:0.000s
                if_1355_13288()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=13289) as resolve_config_vars_in_file_1356_13289:  # 0m:0.004s
                resolve_config_vars_in_file_1356_13289()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=13290) as if_1357_13290:  # 0m:0.001s
                if_1357_13290()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=13291) as resolve_config_vars_in_file_1358_13291:  # 0m:0.001s
                resolve_config_vars_in_file_1358_13291()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=13292) as if_1359_13292:  # 0m:0.000s
                if_1359_13292()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=13293) as resolve_config_vars_in_file_1360_13293:  # 0m:0.000s
                resolve_config_vars_in_file_1360_13293()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=13294) as if_1361_13294:  # 0m:0.000s
                if_1361_13294()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=13295) as resolve_config_vars_in_file_1362_13295:  # 0m:0.000s
                resolve_config_vars_in_file_1362_13295()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=13296) as if_1363_13296:  # 0m:0.000s
                if_1363_13296()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=13297) as resolve_config_vars_in_file_1364_13297:  # 0m:0.000s
                resolve_config_vars_in_file_1364_13297()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=13298) as if_1365_13298:  # 0m:0.000s
                if_1365_13298()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=13299) as resolve_config_vars_in_file_1366_13299:  # 0m:0.000s
                resolve_config_vars_in_file_1366_13299()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=13300) as if_1367_13300:  # 0m:0.000s
                if_1367_13300()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13301) as resolve_config_vars_in_file_1368_13301:  # 0m:0.000s
                resolve_config_vars_in_file_1368_13301()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=13302) as if_1369_13302:  # 0m:0.006s
                if_1369_13302()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=13303) as resolve_config_vars_in_file_1370_13303:  # 0m:0.001s
                resolve_config_vars_in_file_1370_13303()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=13304) as if_1371_13304:  # 0m:0.000s
                if_1371_13304()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=13305) as resolve_config_vars_in_file_1372_13305:  # 0m:0.000s
                resolve_config_vars_in_file_1372_13305()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=13306) as if_1373_13306:  # 0m:0.000s
                if_1373_13306()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=13307) as resolve_config_vars_in_file_1374_13307:  # 0m:0.000s
                resolve_config_vars_in_file_1374_13307()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=13308) as if_1375_13308:  # 0m:0.000s
                if_1375_13308()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=13309) as resolve_config_vars_in_file_1376_13309:  # 0m:0.000s
                resolve_config_vars_in_file_1376_13309()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=13310) as if_1377_13310:  # 0m:0.000s
                if_1377_13310()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=13311) as resolve_config_vars_in_file_1378_13311:  # 0m:0.000s
                resolve_config_vars_in_file_1378_13311()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=13312) as if_1379_13312:  # 0m:0.000s
                if_1379_13312()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=13313) as resolve_config_vars_in_file_1380_13313:  # 0m:0.000s
                resolve_config_vars_in_file_1380_13313()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=13314) as if_1381_13314:  # 0m:0.000s
                if_1381_13314()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=13315) as resolve_config_vars_in_file_1382_13315:  # 0m:0.000s
                resolve_config_vars_in_file_1382_13315()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=13316) as if_1383_13316:  # 0m:0.000s
                if_1383_13316()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=13317) as resolve_config_vars_in_file_1384_13317:  # 0m:0.000s
                resolve_config_vars_in_file_1384_13317()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=13318) as if_1385_13318:  # 0m:0.000s
                if_1385_13318()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=13319) as resolve_config_vars_in_file_1386_13319:  # 0m:0.000s
                resolve_config_vars_in_file_1386_13319()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=13320) as if_1387_13320:  # 0m:0.004s
                if_1387_13320()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13321) as resolve_config_vars_in_file_1388_13321:  # 0m:0.001s
                resolve_config_vars_in_file_1388_13321()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=13322) as if_1389_13322:  # 0m:0.000s
                if_1389_13322()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13323) as resolve_config_vars_in_file_1390_13323:  # 0m:0.000s
                resolve_config_vars_in_file_1390_13323()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=13324) as if_1391_13324:  # 0m:0.000s
                if_1391_13324()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=13325) as resolve_config_vars_in_file_1392_13325:  # 0m:0.000s
                resolve_config_vars_in_file_1392_13325()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=13326) as if_1393_13326:  # 0m:0.000s
                if_1393_13326()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13327) as resolve_config_vars_in_file_1394_13327:  # 0m:0.000s
                resolve_config_vars_in_file_1394_13327()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=13328) as if_1395_13328:  # 0m:0.000s
                if_1395_13328()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=13329) as resolve_config_vars_in_file_1396_13329:  # 0m:0.000s
                resolve_config_vars_in_file_1396_13329()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=13330) as if_1397_13330:  # 0m:0.000s
                if_1397_13330()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13331) as resolve_config_vars_in_file_1398_13331:  # 0m:0.000s
                resolve_config_vars_in_file_1398_13331()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=13332) as if_1399_13332:  # 0m:0.000s
                if_1399_13332()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=13333) as rm_file_or_dir_1400_13333:  # 0m:0.000s
                rm_file_or_dir_1400_13333()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=13334) as rm_file_or_dir_1401_13334:  # 0m:0.000s
                rm_file_or_dir_1401_13334()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=13335) as rm_file_or_dir_1402_13335:  # 0m:0.000s
                rm_file_or_dir_1402_13335()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13336) as resolve_config_vars_in_file_1403_13336:  # 0m:0.000s
                resolve_config_vars_in_file_1403_13336()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=13337) as if_1404_13337:  # 0m:0.000s
                if_1404_13337()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13338) as resolve_config_vars_in_file_1405_13338:  # 0m:0.000s
                resolve_config_vars_in_file_1405_13338()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=13339) as if_1406_13339:  # 0m:0.000s
                if_1406_13339()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=13340) as resolve_config_vars_in_file_1407_13340:  # 0m:0.000s
                resolve_config_vars_in_file_1407_13340()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=13341) as if_1408_13341:  # 0m:0.000s
                if_1408_13341()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=13342) as rm_file_or_dir_1409_13342:  # 0m:0.000s
                rm_file_or_dir_1409_13342()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=13343) as rm_file_or_dir_1410_13343:  # 0m:0.000s
                rm_file_or_dir_1410_13343()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=13344) as rm_file_or_dir_1411_13344:  # 0m:0.000s
                rm_file_or_dir_1411_13344()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=13345) as resolve_config_vars_in_file_1412_13345:  # 0m:0.000s
                resolve_config_vars_in_file_1412_13345()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=13346) as if_1413_13346:  # 0m:0.000s
                if_1413_13346()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=13347) as resolve_config_vars_in_file_1414_13347:  # 0m:0.000s
                resolve_config_vars_in_file_1414_13347()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=13348) as if_1415_13348:  # 0m:0.000s
                if_1415_13348()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13349) as resolve_config_vars_in_file_1416_13349:  # 0m:0.001s
                resolve_config_vars_in_file_1416_13349()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=13350) as if_1417_13350:  # 0m:0.000s
                if_1417_13350()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=13351) as resolve_config_vars_in_file_1418_13351:  # 0m:0.000s
                resolve_config_vars_in_file_1418_13351()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=13352) as if_1419_13352:  # 0m:0.000s
                if_1419_13352()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13353) as resolve_config_vars_in_file_1420_13353:  # 0m:0.000s
                resolve_config_vars_in_file_1420_13353()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=13354) as if_1421_13354:  # 0m:0.000s
                if_1421_13354()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=13355) as resolve_config_vars_in_file_1422_13355:  # 0m:0.000s
                resolve_config_vars_in_file_1422_13355()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=13356) as if_1423_13356:  # 0m:0.000s
                if_1423_13356()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=13357) as resolve_config_vars_in_file_1424_13357:  # 0m:0.000s
                resolve_config_vars_in_file_1424_13357()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=13358) as if_1425_13358:  # 0m:0.000s
                if_1425_13358()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=13359) as resolve_config_vars_in_file_1426_13359:  # 0m:0.000s
                resolve_config_vars_in_file_1426_13359()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=13360) as if_1427_13360:  # 0m:0.001s
                if_1427_13360()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=13361) as cd_stage_1428_13361:  # 0m:0.021s
            cd_stage_1428_13361()
            with Stage(r"copy", r"WavesReWireDevice v13.0.0.129", prog_num=13362):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13363) as should_copy_source_1429_13363:  # ?
                    should_copy_source_1429_13363()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=13364):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=13365) as copy_dir_to_dir_1430_13365:  # ?
                            copy_dir_to_dir_1430_13365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=13366) as unwtar_1431_13366:  # ?
                            unwtar_1431_13366()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=13367, recursive=True) as chown_1432_13367:  # 0m:0.000s
                            chown_1432_13367()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13368) as should_copy_source_1433_13368:  # ?
                    should_copy_source_1433_13368()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=13369):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=13370) as copy_dir_to_dir_1434_13370:  # ?
                            copy_dir_to_dir_1434_13370()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=13371) as unwtar_1435_13371:  # ?
                            unwtar_1435_13371()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=13372, recursive=True) as chown_1436_13372:  # 0m:0.001s
                            chown_1436_13372()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13373) as shell_command_1437_13373:  # 0m:0.015s
                shell_command_1437_13373()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=13374) as cd_stage_1438_13374:  # 0m:0.006s
            cd_stage_1438_13374()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=13375):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=13376) as should_copy_source_1439_13376:  # ?
                    should_copy_source_1439_13376()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=13377):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=13378) as copy_dir_to_dir_1440_13378:  # ?
                            copy_dir_to_dir_1440_13378()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=13379, recursive=True) as chown_1441_13379:  # 0m:0.001s
                            chown_1441_13379()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=13380):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=13381) as should_copy_source_1442_13381:  # ?
                    should_copy_source_1442_13381()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=13382):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=13383) as copy_dir_to_dir_1443_13383:  # ?
                            copy_dir_to_dir_1443_13383()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=13384) as unwtar_1444_13384:  # ?
                            unwtar_1444_13384()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=13385, recursive=True) as chown_1445_13385:  # 0m:0.005s
                            chown_1445_13385()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=13386) as cd_stage_1446_13386:  # 0m:0.001s
            cd_stage_1446_13386()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=13387):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=13388) as should_copy_source_1447_13388:  # ?
                    should_copy_source_1447_13388()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=13389):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=13390) as copy_dir_to_dir_1448_13390:  # ?
                            copy_dir_to_dir_1448_13390()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=13391) as unwtar_1449_13391:  # ?
                            unwtar_1449_13391()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=13392, recursive=True) as chown_1450_13392:  # 0m:0.000s
                            chown_1450_13392()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=13393) as cd_stage_1451_13393:  # 0m:0.001s
            cd_stage_1451_13393()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=13394):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=13395) as should_copy_source_1452_13395:  # ?
                    should_copy_source_1452_13395()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=13396):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=13397) as copy_dir_to_dir_1453_13397:  # ?
                            copy_dir_to_dir_1453_13397()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=13398, recursive=True) as chown_1454_13398:  # 0m:0.000s
                            chown_1454_13398()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=13399) as cd_stage_1455_13399:  # 0m:0.001s
            cd_stage_1455_13399()
            with Stage(r"copy", r"License Notifications 1.1 v1.1", prog_num=13400):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=13401) as should_copy_source_1456_13401:  # ?
                    should_copy_source_1456_13401()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=13402):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=13403) as copy_dir_to_dir_1457_13403:  # ?
                            copy_dir_to_dir_1457_13403()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=13404, recursive=True) as chown_1458_13404:  # 0m:0.000s
                            chown_1458_13404()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=13405) as cd_stage_1459_13405:  # 0m:9.669s
            cd_stage_1459_13405()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=13406) as rm_file_or_dir_1460_13406:  # 0m:0.000s
                rm_file_or_dir_1460_13406()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=13407):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=13408) as should_copy_source_1461_13408:  # ?
                    should_copy_source_1461_13408()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=13409):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13410) as copy_dir_to_dir_1462_13410:  # ?
                            copy_dir_to_dir_1462_13410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=13411) as unwtar_1463_13411:  # ?
                            unwtar_1463_13411()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=13412, recursive=True) as chown_1464_13412:  # 0m:0.000s
                            chown_1464_13412()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=13413):  # 0m:0.016s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=13414) as should_copy_source_1465_13414:  # 0m:0.016s
                    should_copy_source_1465_13414()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=13415):  # 0m:0.016s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=13416) as unwtar_1466_13416:  # 0m:0.016s
                            unwtar_1466_13416()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=13417):  # 0m:5.298s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13418) as should_copy_source_1467_13418:  # 0m:5.298s
                    should_copy_source_1467_13418()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=13419):  # 0m:5.298s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=13420) as copy_dir_to_dir_1468_13420:  # 0m:0.016s
                            copy_dir_to_dir_1468_13420()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=13421) as unwtar_1469_13421:  # 0m:5.282s
                            unwtar_1469_13421()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=13422, recursive=True) as chown_1470_13422:  # 0m:0.000s
                            chown_1470_13422()
            with Stage(r"copy", r"OpenVino_2021.4.689 v2021.4.689", prog_num=13423):  # 0m:4.334s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13424) as should_copy_source_1471_13424:  # 0m:4.333s
                    should_copy_source_1471_13424()
                    with Stage(r"copy source", r"Mac/Modules/openvino", prog_num=13425):  # 0m:4.333s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r".", delete_extraneous_files=True, prog_num=13426) as copy_dir_to_dir_1472_13426:  # 0m:0.228s
                            copy_dir_to_dir_1472_13426()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", where_to_unwtar=r".", prog_num=13427) as unwtar_1473_13427:  # 0m:4.105s
                            unwtar_1473_13427()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/openvino", user_id=-1, group_id=-1, prog_num=13428, recursive=True) as chown_1474_13428:  # 0m:0.000s
                            chown_1474_13428()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=13429):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=13430) as should_copy_source_1475_13430:  # ?
                    should_copy_source_1475_13430()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=13431):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13432) as copy_dir_to_dir_1476_13432:  # ?
                            copy_dir_to_dir_1476_13432()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=13433) as chmod_1477_13433:  # ?
                            chmod_1477_13433()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=13434) as chmod_1478_13434:  # ?
                            chmod_1478_13434()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=13435, recursive=True) as chown_1479_13435:  # 0m:0.000s
                            chown_1479_13435()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=13438) as resolve_symlink_files_in_folder_1480_13438:  # 0m:0.002s
                resolve_symlink_files_in_folder_1480_13438()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13439) as shell_command_1481_13439:  # 0m:0.017s
                shell_command_1481_13439()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=13440) as cd_stage_1482_13440:  # 0m:0.002s
            cd_stage_1482_13440()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=13441):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=13442) as should_copy_source_1483_13442:  # ?
                    should_copy_source_1483_13442()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=13443):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=13444) as copy_dir_to_dir_1484_13444:  # ?
                            copy_dir_to_dir_1484_13444()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=13445, recursive=True) as chown_1485_13445:  # 0m:0.001s
                            chown_1485_13445()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=13446) as cd_stage_1486_13446:  # 0m:0.001s
            cd_stage_1486_13446()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=13447):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=13448) as should_copy_source_1487_13448:  # ?
                    should_copy_source_1487_13448()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=13449):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=13450, recursive=True) as chmod_1488_13450:  # ?
                            chmod_1488_13450()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13451) as copy_dir_to_dir_1489_13451:  # ?
                            copy_dir_to_dir_1489_13451()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=13452) as unwtar_1490_13452:  # ?
                            unwtar_1490_13452()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=13453, recursive=True) as chown_1491_13453:  # ?
                            chown_1491_13453()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13454) as if_1492_13454:  # 0m:0.000s
                            if_1492_13454()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=13455) as cd_stage_1493_13455:  # 0m:0.001s
            cd_stage_1493_13455()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.178.179", prog_num=13456):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=13457) as should_copy_source_1494_13457:  # ?
                    should_copy_source_1494_13457()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=13458):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13459) as copy_dir_to_dir_1495_13459:  # ?
                            copy_dir_to_dir_1495_13459()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=13460) as unwtar_1496_13460:  # ?
                            unwtar_1496_13460()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=13461, recursive=True) as chown_1497_13461:  # ?
                            chown_1497_13461()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162416-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13462) as if_1498_13462:  # 0m:0.001s
                            if_1498_13462()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=13463) as cd_stage_1499_13463:  # 0m:2.411s
            cd_stage_1499_13463()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=13464):  # 0m:1.162s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13465) as should_copy_source_1500_13465:  # 0m:1.162s
                    should_copy_source_1500_13465()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=13466):  # 0m:1.161s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=13467) as copy_dir_to_dir_1501_13467:  # 0m:0.022s
                            copy_dir_to_dir_1501_13467()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=13468) as unwtar_1502_13468:  # 0m:1.066s
                            unwtar_1502_13468()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13469, recursive=True) as chown_1503_13469:  # 0m:0.000s
                            chown_1503_13469()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=13470) as break_hard_link_1504_13470:  # 0m:0.017s
                            break_hard_link_1504_13470()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=13471) as shell_command_1505_13471:  # 0m:0.048s
                            shell_command_1505_13471()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13472, recursive=True) as chown_1506_13472:  # 0m:0.000s
                            chown_1506_13472()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=13473, recursive=True) as chmod_1507_13473:  # 0m:0.008s
                            chmod_1507_13473()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=13474):  # 0m:1.248s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13475) as should_copy_source_1508_13475:  # 0m:1.248s
                    should_copy_source_1508_13475()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=13476):  # 0m:1.247s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=13477) as copy_dir_to_dir_1509_13477:  # 0m:0.100s
                            copy_dir_to_dir_1509_13477()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=13478) as unwtar_1510_13478:  # 0m:1.073s
                            unwtar_1510_13478()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13479, recursive=True) as chown_1511_13479:  # 0m:0.001s
                            chown_1511_13479()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=13480) as break_hard_link_1512_13480:  # 0m:0.015s
                            break_hard_link_1512_13480()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=13481) as shell_command_1513_13481:  # 0m:0.050s
                            shell_command_1513_13481()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13482, recursive=True) as chown_1514_13482:  # 0m:0.000s
                            chown_1514_13482()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=13483, recursive=True) as chmod_1515_13483:  # 0m:0.007s
                            chmod_1515_13483()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=13484) as cd_stage_1516_13484:  # 0m:0.002s
            cd_stage_1516_13484()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=13485):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13486) as should_copy_source_1517_13486:  # ?
                    should_copy_source_1517_13486()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=13487):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=13488) as copy_dir_to_dir_1518_13488:  # ?
                            copy_dir_to_dir_1518_13488()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=13489) as unwtar_1519_13489:  # ?
                            unwtar_1519_13489()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=13490, recursive=True) as chown_1520_13490:  # ?
                            chown_1520_13490()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=13491) as shell_command_1521_13491:  # 0m:0.000s
                            shell_command_1521_13491()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=13492):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13493) as should_copy_source_1522_13493:  # ?
                    should_copy_source_1522_13493()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=13494):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=13495) as copy_dir_to_dir_1523_13495:  # ?
                            copy_dir_to_dir_1523_13495()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=13496) as unwtar_1524_13496:  # ?
                            unwtar_1524_13496()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=13497, recursive=True) as chown_1525_13497:  # ?
                            chown_1525_13497()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=13498) as shell_command_1526_13498:  # 0m:0.000s
                            shell_command_1526_13498()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13499) as cd_stage_1527_13499:  # 0m:0.002s
            cd_stage_1527_13499()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=13500):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13501) as should_copy_source_1528_13501:  # ?
                    should_copy_source_1528_13501()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=13502):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=13503) as copy_dir_to_dir_1529_13503:  # ?
                            copy_dir_to_dir_1529_13503()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=13504) as unwtar_1530_13504:  # ?
                            unwtar_1530_13504()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=13505, recursive=True) as chown_1531_13505:  # ?
                            chown_1531_13505()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13506) as shell_command_1532_13506:  # ?
                            shell_command_1532_13506()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13507) as script_command_1533_13507:  # ?
                            script_command_1533_13507()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13508) as shell_command_1534_13508:  # 0m:0.001s
                            shell_command_1534_13508()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=13509):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13510) as should_copy_source_1535_13510:  # ?
                    should_copy_source_1535_13510()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=13511):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=13512) as copy_dir_to_dir_1536_13512:  # ?
                            copy_dir_to_dir_1536_13512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=13513) as unwtar_1537_13513:  # ?
                            unwtar_1537_13513()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=13514, recursive=True) as chown_1538_13514:  # ?
                            chown_1538_13514()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13515) as shell_command_1539_13515:  # ?
                            shell_command_1539_13515()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13516) as script_command_1540_13516:  # ?
                            script_command_1540_13516()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13517) as shell_command_1541_13517:  # 0m:0.001s
                            shell_command_1541_13517()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13518) as create_symlink_1542_13518:  # 0m:0.000s
                create_symlink_1542_13518()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13519) as create_symlink_1543_13519:  # 0m:0.000s
                create_symlink_1543_13519()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=13520) as cd_stage_1544_13520:  # 0m:0.000s
            cd_stage_1544_13520()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=13521) as rm_file_or_dir_1545_13521:  # 0m:0.000s
                rm_file_or_dir_1545_13521()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=13522) as cd_stage_1546_13522:  # 0m:0.000s
            cd_stage_1546_13522()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=13523) as rm_file_or_dir_1547_13523:  # 0m:0.000s
                rm_file_or_dir_1547_13523()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=13524) as rm_file_or_dir_1548_13524:  # 0m:0.000s
                rm_file_or_dir_1548_13524()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=13525) as rm_file_or_dir_1549_13525:  # 0m:0.000s
                rm_file_or_dir_1549_13525()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=13526) as shell_command_1550_13526:  # 0m:0.009s
            shell_command_1550_13526()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=13527) as shell_command_1551_13527:  # 0m:0.101s
            shell_command_1551_13527()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=13528) as script_command_1552_13528:  # 0m:0.010s
            script_command_1552_13528()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=13529) as rm_file_or_dir_1553_13529:  # 0m:0.001s
            rm_file_or_dir_1553_13529()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13530) as move_dir_to_dir_1554_13530:  # 0m:0.000s
            move_dir_to_dir_1554_13530()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13531) as move_dir_to_dir_1555_13531:  # 0m:0.000s
            move_dir_to_dir_1555_13531()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13532) as move_dir_to_dir_1556_13532:  # 0m:0.000s
            move_dir_to_dir_1556_13532()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13533) as move_dir_to_dir_1557_13533:  # 0m:0.000s
            move_dir_to_dir_1557_13533()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=13534) as make_dirs_1558_13534:  # 0m:0.012s
            make_dirs_1558_13534()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13535) as move_dir_to_dir_1559_13535:  # 0m:0.000s
            move_dir_to_dir_1559_13535()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13536) as move_dir_to_dir_1560_13536:  # 0m:0.000s
            move_dir_to_dir_1560_13536()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=13537) as shell_command_1561_13537:  # 0m:0.102s
            shell_command_1561_13537()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=13538) as script_command_1562_13538:  # 0m:0.011s
            script_command_1562_13538()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=13539) as rm_file_or_dir_1563_13539:  # 0m:0.001s
            rm_file_or_dir_1563_13539()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13540) as glober_1564_13540:  # 0m:0.001s
            glober_1564_13540()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=13541) as glober_1565_13541:  # 0m:0.001s
            glober_1565_13541()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13542) as glober_1566_13542:  # 0m:0.001s
            glober_1566_13542()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=13543) as glober_1567_13543:  # 0m:0.001s
            glober_1567_13543()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=13544) as shell_command_1568_13544:  # 0m:3.120s
            shell_command_1568_13544()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=13545) as shell_command_1569_13545:  # 0m:0.100s
            shell_command_1569_13545()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=13546) as script_command_1570_13546:  # 0m:0.012s
            script_command_1570_13546()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=13547) as if_1571_13547:  # 0m:0.001s
            if_1571_13547()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13548) as if_1572_13548:  # 0m:0.000s
            if_1572_13548()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=13549) as if_1573_13549:  # 0m:0.000s
            if_1573_13549()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13550) as if_1574_13550:  # 0m:0.000s
            if_1574_13550()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=13551) as make_dir_1575_13551:  # 0m:0.009s
            make_dir_1575_13551()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=13552) as chmod_1576_13552:  # 0m:0.000s
            chmod_1576_13552()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=13553) as make_dir_1577_13553:  # 0m:0.011s
            make_dir_1577_13553()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=13554) as chmod_1578_13554:  # 0m:0.000s
            chmod_1578_13554()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13555) as chmod_1579_13555:  # 0m:0.000s
            chmod_1579_13555()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13556) as chmod_1580_13556:  # 0m:0.000s
            chmod_1580_13556()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=13557) as chmod_1581_13557:  # 0m:0.000s
            chmod_1581_13557()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=13558) as shell_command_1582_13558:  # 0m:0.097s
            shell_command_1582_13558()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=13559) as script_command_1583_13559:  # 0m:0.010s
            script_command_1583_13559()
    with Stage(r"post-copy", prog_num=13560):  # 0m:0.044s
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13561) as make_dir_1584_13561:  # 0m:0.012s
            make_dir_1584_13561()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=13562) as copy_file_to_file_1585_13562:  # 0m:0.011s
            copy_file_to_file_1585_13562()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13563) as chmod_1586_13563:  # 0m:0.000s
            chmod_1586_13563()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13564) as chmod_1587_13564:  # 0m:0.000s
            chmod_1587_13564()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=13565) as copy_file_to_file_1588_13565:  # 0m:0.010s
            copy_file_to_file_1588_13565()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13566) as chmod_1589_13566:  # 0m:0.000s
            chmod_1589_13566()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=13567) as copy_file_to_file_1590_13567:  # 0m:0.009s
            copy_file_to_file_1590_13567()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13568) as chmod_1591_13568:  # 0m:0.000s
            chmod_1591_13568()
        Progress(r"Done copy", prog_num=13569)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=13570)()  # 0m:0.000s
    with Stage(r"post", prog_num=13571):  # 0m:0.061s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13572) as make_dir_1592_13572:  # 0m:0.010s
            make_dir_1592_13572()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=13573) as copy_file_to_file_1593_13573:  # 0m:0.010s
            copy_file_to_file_1593_13573()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13574) as make_dir_1594_13574:  # 0m:0.009s
            make_dir_1594_13574()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=13575) as copy_file_to_file_1595_13575:  # 0m:0.013s
            copy_file_to_file_1595_13575()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13576) as make_dir_1596_13576:  # 0m:0.009s
            make_dir_1596_13576()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=13577) as copy_file_to_file_1597_13577:  # 0m:0.010s
            copy_file_to_file_1597_13577()

with Stage(r"epilog", prog_num=13578):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162416.py", prog_num=13579) as patch_py_batch_with_timings_1598_13579:  # ?
        patch_py_batch_with_timings_1598_13579()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# copy time 0m:32.558s
