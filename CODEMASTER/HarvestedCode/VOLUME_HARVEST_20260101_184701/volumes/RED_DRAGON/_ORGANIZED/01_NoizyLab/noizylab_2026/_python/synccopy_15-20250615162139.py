# Creation time: 15-06-25_16-22
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 13603
PythonBatchCommandBase.running_progress = 1226
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1227):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"15-20250615162139"
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
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NDkwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NjAwfX19XX0_;CloudFront-Signature=eEo47m2OwJbNsuelAVRCGSiXKH~nscmDg6~fbF2GY~kLLVG8HbLNFTawibq-Riwrig2sZj0cTel~CxE0Iy8tWQpVivDeL8UbwqgEdlPp9j8xjtghfmV9Va~90e3STS0WgC2s2dLsV3qhIo~CtsOORZset~grRaqdz484ku6I6fawGWi39d3HAKpuCqqghHdleEcDpV-On6y32MDruFqUfwKdAXOywDQd03JsiB7lIRMaGd-WVLWq4Bq~ufJnv4FwBjGF~qwdXfvHaf7rHHOpt~i7rjQeIWdTdKg51uaqaIHKx2kNo0vYVxgahEk9ksVIHU2dyhyJS0yozyee8Xj~wQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MDA1NDkwMH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUwMDE4NjAwfX19XX0_;CloudFront-Signature=eEo47m2OwJbNsuelAVRCGSiXKH~nscmDg6~fbF2GY~kLLVG8HbLNFTawibq-Riwrig2sZj0cTel~CxE0Iy8tWQpVivDeL8UbwqgEdlPp9j8xjtghfmV9Va~90e3STS0WgC2s2dLsV3qhIo~CtsOORZset~grRaqdz484ku6I6fawGWi39d3HAKpuCqqghHdleEcDpV-On6y32MDruFqUfwKdAXOywDQd03JsiB7lIRMaGd-WVLWq4Bq~ufJnv4FwBjGF~qwdXfvHaf7rHHOpt~i7rjQeIWdTdKg51uaqaIHKx2kNo0vYVxgahEk9ksVIHU2dyhyJS0yozyee8Xj~wQ__"
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162139.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V15-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml")
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
    config_vars['REQUIRE_REPO_REV'] = 53
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 12372
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250615162139.log", r"--run")
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
    config_vars['__INVOCATION_RANDOM_ID__'] = r"fkbytenttaxgmbqj"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS__IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-15 16:23:28.542999"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 26353886
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 8
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

with PythonBatchRuntime(r"synccopy", prog_num=1228):
    with Stage(r"begin", prog_num=1229):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1230):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1231) as copy_file_to_file_001_1231:
            copy_file_to_file_001_1231()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1232) as copy_file_to_file_002_1232:
            copy_file_to_file_002_1232()
    with Stage(r"sync", prog_num=1233):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1234) as shell_command_003_1234:
            shell_command_003_1234()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1235) as shell_command_004_1235:
            shell_command_004_1235()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1236) as shell_command_005_1236:
            shell_command_005_1236()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1237) as shell_command_006_1237:
            shell_command_006_1237()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1238) as shell_command_007_1238:
            shell_command_007_1238()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1239) as shell_command_008_1239:
            shell_command_008_1239()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1240) as shell_command_009_1240:
            shell_command_009_1240()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1241) as shell_command_010_1241:
            shell_command_010_1241()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V15", prog_num=1242):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", chowner=True, prog_num=1243) as make_dir_011_1243:
                make_dir_011_1243()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=1244) as cd_012_1244:
                cd_012_1244()
                Progress(r"10081 files already in cache", own_progress_count=10081, prog_num=11325)()
                with CreateSyncFolders(own_progress_count=5, prog_num=11330) as create_sync_folders_013_11330:
                    create_sync_folders_013_11330()
                Progress(r"Downloading with 50 processes in parallel", prog_num=11331)()
                Progress(r"Downloading with curl parallel", prog_num=11332)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.py_curl/dl-00", total_files_to_download=8, previously_downloaded_files=0, total_bytes_to_download=26353886, own_progress_count=7, prog_num=11339, report_own_progress=False) as curl_with_internal_parallel_014_11339:
                    curl_with_internal_parallel_014_11339()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.py_curl/dl-01", total_files_to_download=8, previously_downloaded_files=7, total_bytes_to_download=26353886, prog_num=11340, report_own_progress=False) as curl_with_internal_parallel_015_11340:
                    curl_with_internal_parallel_015_11340()
                Progress(r"Downloading 8 files done", prog_num=11341)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=11342) as run_in_thread_016_11342:
                    run_in_thread_016_11342()
                Progress(r"Check checksum ...", prog_num=11343)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=8, prog_num=11351) as check_download_folder_checksum_017_11351:
                    check_download_folder_checksum_017_11351()
                with Stage(r"post_sync", prog_num=11352):
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15...", prog_num=11353)()
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=11354, recursive=True) as chmod_and_chown_018_11354:
                        chmod_and_chown_018_11354()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=11355) as copy_file_to_file_019_11355:
                        copy_file_to_file_019_11355()
            Progress(r"Done sync", prog_num=11356)()
    with Stage(r"copy", prog_num=11357):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11358)()
        with Stage(r"create folders", prog_num=11359):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=11360) as make_dir_020_11360:
                make_dir_020_11360()
            with MakeDir(r"/Applications/Waves/Applications V15", chowner=True, prog_num=11361) as make_dir_021_11361:
                make_dir_021_11361()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=11362) as make_dir_022_11362:
                make_dir_022_11362()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=11363) as make_dir_023_11363:
                make_dir_023_11363()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=11364) as make_dir_024_11364:
                make_dir_024_11364()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=11365) as make_dir_025_11365:
                make_dir_025_11365()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=11366) as make_dir_026_11366:
                make_dir_026_11366()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=11367) as make_dir_027_11367:
                make_dir_027_11367()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=11368) as make_dir_028_11368:
                make_dir_028_11368()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=11369) as make_dir_029_11369:
                make_dir_029_11369()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=11370) as make_dir_030_11370:
                make_dir_030_11370()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=11371) as make_dir_031_11371:
                make_dir_031_11371()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=11372) as make_dir_032_11372:
                make_dir_032_11372()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=11373) as make_dir_033_11373:
                make_dir_033_11373()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15", chowner=True, prog_num=11374) as make_dir_034_11374:
                make_dir_034_11374()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/Documents", chowner=True, prog_num=11375) as make_dir_035_11375:
                make_dir_035_11375()
            with MakeDir(r"/Applications/Waves/Plug-Ins V15/GTR", chowner=True, prog_num=11376) as make_dir_036_11376:
                make_dir_036_11376()
            with MakeDir(r"/Applications/Waves/ReWire", chowner=True, prog_num=11377) as make_dir_037_11377:
                make_dir_037_11377()
            with MakeDir(r"/Applications/Waves/WaveShells V15", chowner=True, prog_num=11378) as make_dir_038_11378:
                make_dir_038_11378()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=11379) as make_dir_039_11379:
                make_dir_039_11379()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=11380) as make_dir_040_11380:
                make_dir_040_11380()
            with MakeDir(r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=11381) as make_dir_041_11381:
                make_dir_041_11381()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=11382) as make_dir_042_11382:
                make_dir_042_11382()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=11383) as make_dir_043_11383:
                make_dir_043_11383()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=11384) as make_dir_044_11384:
                make_dir_044_11384()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=11385) as make_dir_045_11385:
                make_dir_045_11385()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V15", chowner=True, prog_num=11386) as make_dir_046_11386:
                make_dir_046_11386()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=11387) as make_dir_047_11387:
                make_dir_047_11387()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=11388) as make_dir_048_11388:
                make_dir_048_11388()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=11389) as make_dir_049_11389:
                make_dir_049_11389()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=11390) as make_dir_050_11390:
                make_dir_050_11390()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=11391) as make_dir_051_11391:
                make_dir_051_11391()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=11392) as make_dir_052_11392:
                make_dir_052_11392()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=11393) as make_dir_053_11393:
                make_dir_053_11393()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=11394) as make_dir_054_11394:
                make_dir_054_11394()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=11395) as make_dir_055_11395:
                make_dir_055_11395()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=11396) as make_dir_056_11396:
                make_dir_056_11396()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=11397) as rm_file_or_dir_057_11397:
            rm_file_or_dir_057_11397()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=11398) as rm_file_or_dir_058_11398:
            rm_file_or_dir_058_11398()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=11399) as shell_command_059_11399:
            shell_command_059_11399()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=11400) as shell_command_060_11400:
            shell_command_060_11400()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=11401) as shell_command_061_11401:
            shell_command_061_11401()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11402) as shell_command_062_11402:
            shell_command_062_11402()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=11403) as shell_command_063_11403:
            shell_command_063_11403()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=11404) as shell_command_064_11404:
            shell_command_064_11404()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=11405) as shell_command_065_11405:
            shell_command_065_11405()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=11406) as shell_command_066_11406:
            shell_command_066_11406()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15", prog_num=11407) as cd_stage_067_11407:
            cd_stage_067_11407()
            with SetExecPermissionsInSyncFolder(prog_num=11408) as set_exec_permissions_in_sync_folder_068_11408:
                set_exec_permissions_in_sync_folder_068_11408()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V15", prog_num=11409) as cd_stage_069_11409:
            cd_stage_069_11409()
            with Stage(r"copy", r"Bass Slapper application v15.5.79.262", prog_num=11410):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11411) as should_copy_source_070_11411:
                    should_copy_source_070_11411()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=11412):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=11413) as copy_dir_to_dir_071_11413:
                            copy_dir_to_dir_071_11413()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=11414) as unwtar_072_11414:
                            unwtar_072_11414()
                        with Chown(path=r"/Applications/Waves/Applications V15/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=11415, recursive=True) as chown_073_11415:
                            chown_073_11415()
            with Stage(r"copy", r"Electric Grand 80 application v15.5.79.262", prog_num=11416):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11417) as should_copy_source_074_11417:
                    should_copy_source_074_11417()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=11418):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=11419) as copy_dir_to_dir_075_11419:
                            copy_dir_to_dir_075_11419()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=11420) as unwtar_076_11420:
                            unwtar_076_11420()
                        with Chown(path=r"/Applications/Waves/Applications V15/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=11421, recursive=True) as chown_077_11421:
                            chown_077_11421()
            with Stage(r"copy", r"GTR application v15.5.79.262", prog_num=11422):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V15", skip_progress_count=4, prog_num=11423) as should_copy_source_078_11423:
                    should_copy_source_078_11423()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=11424):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=11425) as copy_dir_to_dir_079_11425:
                            copy_dir_to_dir_079_11425()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=11426) as unwtar_080_11426:
                            unwtar_080_11426()
                        with Chown(path=r"/Applications/Waves/Applications V15/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=11427, recursive=True) as chown_081_11427:
                            chown_081_11427()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V15" -c', ignore_all_errors=True, prog_num=11428) as shell_command_082_11428:
                shell_command_082_11428()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V15"/Icon?; fi', prog_num=11429) as script_command_083_11429:
                script_command_083_11429()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=11430) as cd_stage_084_11430:
            cd_stage_084_11430()
            with Stage(r"copy", r"COSMOS__Application v15.5.79.262", prog_num=11431):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=11432) as should_copy_source_085_11432:
                    should_copy_source_085_11432()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=11433):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=11434) as copy_dir_to_dir_086_11434:
                            copy_dir_to_dir_086_11434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=11435) as unwtar_087_11435:
                            unwtar_087_11435()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=11436, recursive=True) as chown_088_11436:
                            chown_088_11436()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=11446) as resolve_symlink_files_in_folder_089_11446:
                resolve_symlink_files_in_folder_089_11446()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=11447) as cd_stage_090_11447:
            cd_stage_090_11447()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.0.2", prog_num=11448):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11449) as should_copy_source_091_11449:
                    should_copy_source_091_11449()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=11450):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=11451) as copy_dir_to_dir_092_11451:
                            copy_dir_to_dir_092_11451()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=11452, recursive=True) as chown_093_11452:
                            chown_093_11452()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=11453):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11454) as should_copy_source_094_11454:
                    should_copy_source_094_11454()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=11455):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=11456) as copy_dir_to_dir_095_11456:
                            copy_dir_to_dir_095_11456()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Models", where_to_unwtar=r".", prog_num=11457) as unwtar_096_11457:
                            unwtar_096_11457()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=11458, recursive=True) as chown_097_11458:
                            chown_097_11458()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=11459):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11460) as should_copy_source_098_11460:
                    should_copy_source_098_11460()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=11461):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=11462) as copy_dir_to_dir_099_11462:
                            copy_dir_to_dir_099_11462()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=11463, recursive=True) as chown_100_11463:
                            chown_100_11463()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=11464):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11465) as should_copy_source_101_11465:
                    should_copy_source_101_11465()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=11466):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11467) as copy_dir_to_dir_102_11467:
                            copy_dir_to_dir_102_11467()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=11468, recursive=True) as chown_103_11468:
                            chown_103_11468()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=11469):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11470) as should_copy_source_104_11470:
                    should_copy_source_104_11470()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=11471):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=11472) as copy_dir_to_dir_105_11472:
                            copy_dir_to_dir_105_11472()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=11473, recursive=True) as chown_106_11473:
                            chown_106_11473()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=11474):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=11475) as should_copy_source_107_11475:
                    should_copy_source_107_11475()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=11476):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=11477) as copy_dir_to_dir_108_11477:
                            copy_dir_to_dir_108_11477()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=11478, recursive=True) as chown_109_11478:
                            chown_109_11478()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=11479):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=11480) as should_copy_source_110_11480:
                    should_copy_source_110_11480()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=11481):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=11482) as copy_dir_to_dir_111_11482:
                            copy_dir_to_dir_111_11482()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Harmony", where_to_unwtar=r".", prog_num=11483) as unwtar_112_11483:
                            unwtar_112_11483()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=11484, recursive=True) as chown_113_11484:
                            chown_113_11484()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=11485) as cd_stage_114_11485:
            cd_stage_114_11485()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=11486):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=11487) as should_copy_source_115_11487:
                    should_copy_source_115_11487()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=11488):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/Info.xml", r".", prog_num=11489) as copy_file_to_dir_116_11489:
                            copy_file_to_dir_116_11489()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=11490) as chmod_and_chown_117_11490:
                            chmod_and_chown_117_11490()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=11491) as should_copy_source_118_11491:
                    should_copy_source_118_11491()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=11492):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=11493) as copy_dir_to_dir_119_11493:
                            copy_dir_to_dir_119_11493()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=11494) as unwtar_120_11494:
                            unwtar_120_11494()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=11495, recursive=True) as chown_121_11495:
                            chown_121_11495()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=11496) as cd_stage_122_11496:
            cd_stage_122_11496()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=11497):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11498) as should_copy_source_123_11498:
                    should_copy_source_123_11498()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=11499):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=11500) as copy_dir_to_dir_124_11500:
                            copy_dir_to_dir_124_11500()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=11501, recursive=True) as chown_125_11501:
                            chown_125_11501()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11502) as should_copy_source_126_11502:
                    should_copy_source_126_11502()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=11503):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=11504) as copy_dir_to_dir_127_11504:
                            copy_dir_to_dir_127_11504()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=11505, recursive=True) as chown_128_11505:
                            chown_128_11505()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=11506):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11507) as should_copy_source_129_11507:
                    should_copy_source_129_11507()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=11508):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=11509) as copy_dir_to_dir_130_11509:
                            copy_dir_to_dir_130_11509()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=11510, recursive=True) as chown_131_11510:
                            chown_131_11510()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=11511) as should_copy_source_132_11511:
                    should_copy_source_132_11511()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=11512):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=11513) as copy_dir_to_dir_133_11513:
                            copy_dir_to_dir_133_11513()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=11514, recursive=True) as chown_134_11514:
                            chown_134_11514()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=11515) as cd_stage_135_11515:
            cd_stage_135_11515()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=11516):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=11517) as should_copy_source_136_11517:
                    should_copy_source_136_11517()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=11518):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=11519) as copy_file_to_dir_137_11519:
                            copy_file_to_dir_137_11519()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=11520) as chmod_and_chown_138_11520:
                            chmod_and_chown_138_11520()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=11521) as cd_stage_139_11521:
            cd_stage_139_11521()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=11522):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11523) as should_copy_source_140_11523:
                    should_copy_source_140_11523()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=11524):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=11525) as copy_dir_to_dir_141_11525:
                            copy_dir_to_dir_141_11525()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=11526, recursive=True) as chown_142_11526:
                            chown_142_11526()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=11527):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11528) as should_copy_source_143_11528:
                    should_copy_source_143_11528()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=11529):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=11530) as copy_dir_to_dir_144_11530:
                            copy_dir_to_dir_144_11530()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=11531, recursive=True) as chown_145_11531:
                            chown_145_11531()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=11532):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11533) as should_copy_source_146_11533:
                    should_copy_source_146_11533()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=11534):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=11535) as copy_dir_to_dir_147_11535:
                            copy_dir_to_dir_147_11535()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=11536, recursive=True) as chown_148_11536:
                            chown_148_11536()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=11537):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11538) as should_copy_source_149_11538:
                    should_copy_source_149_11538()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=11539):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=11540) as copy_dir_to_dir_150_11540:
                            copy_dir_to_dir_150_11540()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=11541, recursive=True) as chown_151_11541:
                            chown_151_11541()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=11542):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11543) as should_copy_source_152_11543:
                    should_copy_source_152_11543()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=11544):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=11545) as copy_dir_to_dir_153_11545:
                            copy_dir_to_dir_153_11545()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=11546, recursive=True) as chown_154_11546:
                            chown_154_11546()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=11547):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11548) as should_copy_source_155_11548:
                    should_copy_source_155_11548()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=11549):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=11550) as copy_dir_to_dir_156_11550:
                            copy_dir_to_dir_156_11550()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=11551, recursive=True) as chown_157_11551:
                            chown_157_11551()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=11552):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11553) as should_copy_source_158_11553:
                    should_copy_source_158_11553()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=11554):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=11555) as copy_dir_to_dir_159_11555:
                            copy_dir_to_dir_159_11555()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=11556, recursive=True) as chown_160_11556:
                            chown_160_11556()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=11557):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11558) as should_copy_source_161_11558:
                    should_copy_source_161_11558()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=11559):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=11560) as copy_dir_to_dir_162_11560:
                            copy_dir_to_dir_162_11560()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=11561, recursive=True) as chown_163_11561:
                            chown_163_11561()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=11562):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11563) as should_copy_source_164_11563:
                    should_copy_source_164_11563()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=11564):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=11565) as copy_dir_to_dir_165_11565:
                            copy_dir_to_dir_165_11565()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=11566, recursive=True) as chown_166_11566:
                            chown_166_11566()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=11567):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11568) as should_copy_source_167_11568:
                    should_copy_source_167_11568()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=11569):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=11570) as copy_dir_to_dir_168_11570:
                            copy_dir_to_dir_168_11570()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=11571, recursive=True) as chown_169_11571:
                            chown_169_11571()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=11572):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11573) as should_copy_source_170_11573:
                    should_copy_source_170_11573()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=11574):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=11575) as copy_dir_to_dir_171_11575:
                            copy_dir_to_dir_171_11575()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=11576, recursive=True) as chown_172_11576:
                            chown_172_11576()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=11577):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11578) as should_copy_source_173_11578:
                    should_copy_source_173_11578()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=11579):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=11580) as copy_dir_to_dir_174_11580:
                            copy_dir_to_dir_174_11580()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=11581, recursive=True) as chown_175_11581:
                            chown_175_11581()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=11582):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11583) as should_copy_source_176_11583:
                    should_copy_source_176_11583()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=11584):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=11585) as copy_dir_to_dir_177_11585:
                            copy_dir_to_dir_177_11585()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=11586, recursive=True) as chown_178_11586:
                            chown_178_11586()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=11587):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11588) as should_copy_source_179_11588:
                    should_copy_source_179_11588()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=11589):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=11590) as copy_dir_to_dir_180_11590:
                            copy_dir_to_dir_180_11590()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=11591, recursive=True) as chown_181_11591:
                            chown_181_11591()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=11592):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11593) as should_copy_source_182_11593:
                    should_copy_source_182_11593()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=11594):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=11595) as copy_dir_to_dir_183_11595:
                            copy_dir_to_dir_183_11595()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=11596, recursive=True) as chown_184_11596:
                            chown_184_11596()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=11597):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11598) as should_copy_source_185_11598:
                    should_copy_source_185_11598()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=11599):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=11600) as copy_dir_to_dir_186_11600:
                            copy_dir_to_dir_186_11600()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=11601, recursive=True) as chown_187_11601:
                            chown_187_11601()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=11602):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11603) as should_copy_source_188_11603:
                    should_copy_source_188_11603()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=11604):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11605) as copy_dir_to_dir_189_11605:
                            copy_dir_to_dir_189_11605()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11606, recursive=True) as chown_190_11606:
                            chown_190_11606()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=11607):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11608) as should_copy_source_191_11608:
                    should_copy_source_191_11608()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=11609):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11610) as copy_dir_to_dir_192_11610:
                            copy_dir_to_dir_192_11610()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11611, recursive=True) as chown_193_11611:
                            chown_193_11611()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=11612):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=11613) as should_copy_source_194_11613:
                    should_copy_source_194_11613()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=11614):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=11615) as copy_dir_to_dir_195_11615:
                            copy_dir_to_dir_195_11615()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=11616, recursive=True) as chown_196_11616:
                            chown_196_11616()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=11617) as cd_stage_197_11617:
            cd_stage_197_11617()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=11618):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11619) as should_copy_source_198_11619:
                    should_copy_source_198_11619()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=11620):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=11621) as copy_dir_to_dir_199_11621:
                            copy_dir_to_dir_199_11621()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=11622, recursive=True) as chown_200_11622:
                            chown_200_11622()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=11623):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11624) as should_copy_source_201_11624:
                    should_copy_source_201_11624()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=11625):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=11626) as copy_dir_to_dir_202_11626:
                            copy_dir_to_dir_202_11626()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=11627, recursive=True) as chown_203_11627:
                            chown_203_11627()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=11628):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11629) as should_copy_source_204_11629:
                    should_copy_source_204_11629()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=11630):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=11631) as copy_dir_to_dir_205_11631:
                            copy_dir_to_dir_205_11631()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=11632, recursive=True) as chown_206_11632:
                            chown_206_11632()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=11633):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11634) as should_copy_source_207_11634:
                    should_copy_source_207_11634()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=11635):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=11636) as copy_dir_to_dir_208_11636:
                            copy_dir_to_dir_208_11636()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=11637, recursive=True) as chown_209_11637:
                            chown_209_11637()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=11638):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11639) as should_copy_source_210_11639:
                    should_copy_source_210_11639()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=11640):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=11641) as copy_dir_to_dir_211_11641:
                            copy_dir_to_dir_211_11641()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=11642, recursive=True) as chown_212_11642:
                            chown_212_11642()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=11643):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11644) as should_copy_source_213_11644:
                    should_copy_source_213_11644()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=11645):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=11646) as copy_dir_to_dir_214_11646:
                            copy_dir_to_dir_214_11646()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=11647, recursive=True) as chown_215_11647:
                            chown_215_11647()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=11648):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=11649) as should_copy_source_216_11649:
                    should_copy_source_216_11649()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=11650):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=11651) as copy_dir_to_dir_217_11651:
                            copy_dir_to_dir_217_11651()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=11652, recursive=True) as chown_218_11652:
                            chown_218_11652()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=11653) as cd_stage_219_11653:
            cd_stage_219_11653()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=11654):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11655) as should_copy_source_220_11655:
                    should_copy_source_220_11655()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=11656):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=11657) as copy_dir_to_dir_221_11657:
                            copy_dir_to_dir_221_11657()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=11658, recursive=True) as chown_222_11658:
                            chown_222_11658()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=11659):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=11660) as should_copy_source_223_11660:
                    should_copy_source_223_11660()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=11661):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=11662) as copy_dir_to_dir_224_11662:
                            copy_dir_to_dir_224_11662()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=11663, recursive=True) as chown_225_11663:
                            chown_225_11663()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=11664) as cd_stage_226_11664:
            cd_stage_226_11664()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=11665):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11666) as should_copy_source_227_11666:
                    should_copy_source_227_11666()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=11667):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=11668) as unwtar_228_11668:
                            unwtar_228_11668()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=11669) as should_copy_source_229_11669:
                    should_copy_source_229_11669()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=11670):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=11671) as unwtar_230_11671:
                            unwtar_230_11671()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=11672) as cd_stage_231_11672:
            cd_stage_231_11672()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=11673):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=11674) as should_copy_source_232_11674:
                    should_copy_source_232_11674()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=11675):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=11676) as unwtar_233_11676:
                            unwtar_233_11676()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15", prog_num=11677) as cd_stage_234_11677:
            cd_stage_234_11677()
            with Stage(r"copy", r"ARPlates v15.5.79.262", prog_num=11678):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11679) as should_copy_source_235_11679:
                    should_copy_source_235_11679()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=11680):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=11681) as copy_dir_to_dir_236_11681:
                            copy_dir_to_dir_236_11681()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=11682) as unwtar_237_11682:
                            unwtar_237_11682()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=11683, recursive=True) as chown_238_11683:
                            chown_238_11683()
            with Stage(r"copy", r"Abbey Road Vinyl v15.5.79.262", prog_num=11684):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11685) as should_copy_source_239_11685:
                    should_copy_source_239_11685()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=11686):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=11687) as copy_dir_to_dir_240_11687:
                            copy_dir_to_dir_240_11687()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=11688) as unwtar_241_11688:
                            unwtar_241_11688()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=11689, recursive=True) as chown_242_11689:
                            chown_242_11689()
            with Stage(r"copy", r"Aphex AX v15.5.79.262", prog_num=11690):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11691) as should_copy_source_243_11691:
                    should_copy_source_243_11691()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=11692):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=11693) as copy_dir_to_dir_244_11693:
                            copy_dir_to_dir_244_11693()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=11694) as unwtar_245_11694:
                            unwtar_245_11694()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=11695, recursive=True) as chown_246_11695:
                            chown_246_11695()
            with Stage(r"copy", r"AudioTrack v15.5.79.262", prog_num=11696):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11697) as should_copy_source_247_11697:
                    should_copy_source_247_11697()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=11698):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=11699) as copy_dir_to_dir_248_11699:
                            copy_dir_to_dir_248_11699()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=11700) as unwtar_249_11700:
                            unwtar_249_11700()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=11701, recursive=True) as chown_250_11701:
                            chown_250_11701()
            with Stage(r"copy", r"Bass Rider v15.5.79.262", prog_num=11702):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11703) as should_copy_source_251_11703:
                    should_copy_source_251_11703()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=11704):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=11705) as copy_dir_to_dir_252_11705:
                            copy_dir_to_dir_252_11705()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=11706) as unwtar_253_11706:
                            unwtar_253_11706()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=11707, recursive=True) as chown_254_11707:
                            chown_254_11707()
            with Stage(r"copy", r"Bass Slapper v15.5.79.262", prog_num=11708):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11709) as should_copy_source_255_11709:
                    should_copy_source_255_11709()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=11710):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=11711) as copy_dir_to_dir_256_11711:
                            copy_dir_to_dir_256_11711()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=11712) as unwtar_257_11712:
                            unwtar_257_11712()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=11713, recursive=True) as chown_258_11713:
                            chown_258_11713()
            with Stage(r"copy", r"Brauer Motion v15.5.79.262", prog_num=11714):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11715) as should_copy_source_259_11715:
                    should_copy_source_259_11715()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=11716):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=11717) as copy_dir_to_dir_260_11717:
                            copy_dir_to_dir_260_11717()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=11718) as unwtar_261_11718:
                            unwtar_261_11718()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=11719, recursive=True) as chown_262_11719:
                            chown_262_11719()
            with Stage(r"copy", r"Butch Vig Vocals v15.5.79.262", prog_num=11720):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11721) as should_copy_source_263_11721:
                    should_copy_source_263_11721()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=11722):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11723) as copy_dir_to_dir_264_11723:
                            copy_dir_to_dir_264_11723()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=11724) as unwtar_265_11724:
                            unwtar_265_11724()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=11725, recursive=True) as chown_266_11725:
                            chown_266_11725()
            with Stage(r"copy", r"C1 v15.5.79.262", prog_num=11726):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11727) as should_copy_source_267_11727:
                    should_copy_source_267_11727()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=11728):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=11729) as copy_dir_to_dir_268_11729:
                            copy_dir_to_dir_268_11729()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=11730) as unwtar_269_11730:
                            unwtar_269_11730()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C1.bundle", user_id=-1, group_id=-1, prog_num=11731, recursive=True) as chown_270_11731:
                            chown_270_11731()
            with Stage(r"copy", r"C4 v15.5.79.262", prog_num=11732):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11733) as should_copy_source_271_11733:
                    should_copy_source_271_11733()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=11734):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=11735) as copy_dir_to_dir_272_11735:
                            copy_dir_to_dir_272_11735()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=11736) as unwtar_273_11736:
                            unwtar_273_11736()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/C4.bundle", user_id=-1, group_id=-1, prog_num=11737, recursive=True) as chown_274_11737:
                            chown_274_11737()
            with Stage(r"copy", r"CLA-2A v15.5.79.262", prog_num=11738):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11739) as should_copy_source_275_11739:
                    should_copy_source_275_11739()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=11740):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=11741) as copy_dir_to_dir_276_11741:
                            copy_dir_to_dir_276_11741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=11742) as unwtar_277_11742:
                            unwtar_277_11742()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=11743, recursive=True) as chown_278_11743:
                            chown_278_11743()
            with Stage(r"copy", r"CLA-3A v15.5.79.262", prog_num=11744):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11745) as should_copy_source_279_11745:
                    should_copy_source_279_11745()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=11746):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=11747) as copy_dir_to_dir_280_11747:
                            copy_dir_to_dir_280_11747()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=11748) as unwtar_281_11748:
                            unwtar_281_11748()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=11749, recursive=True) as chown_282_11749:
                            chown_282_11749()
            with Stage(r"copy", r"CLA-76 v15.5.79.262", prog_num=11750):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11751) as should_copy_source_283_11751:
                    should_copy_source_283_11751()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=11752):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=11753) as copy_dir_to_dir_284_11753:
                            copy_dir_to_dir_284_11753()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=11754) as unwtar_285_11754:
                            unwtar_285_11754()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=11755, recursive=True) as chown_286_11755:
                            chown_286_11755()
            with Stage(r"copy", r"CLA Bass v15.5.79.262", prog_num=11756):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11757) as should_copy_source_287_11757:
                    should_copy_source_287_11757()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=11758):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=11759) as copy_dir_to_dir_288_11759:
                            copy_dir_to_dir_288_11759()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=11760) as unwtar_289_11760:
                            unwtar_289_11760()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=11761, recursive=True) as chown_290_11761:
                            chown_290_11761()
            with Stage(r"copy", r"CLA Guitars v15.5.79.262", prog_num=11762):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11763) as should_copy_source_291_11763:
                    should_copy_source_291_11763()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=11764):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=11765) as copy_dir_to_dir_292_11765:
                            copy_dir_to_dir_292_11765()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=11766) as unwtar_293_11766:
                            unwtar_293_11766()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=11767, recursive=True) as chown_294_11767:
                            chown_294_11767()
            with Stage(r"copy", r"CLA Unplugged v15.5.79.262", prog_num=11768):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11769) as should_copy_source_295_11769:
                    should_copy_source_295_11769()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=11770):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=11771) as copy_dir_to_dir_296_11771:
                            copy_dir_to_dir_296_11771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=11772) as unwtar_297_11772:
                            unwtar_297_11772()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=11773, recursive=True) as chown_298_11773:
                            chown_298_11773()
            with Stage(r"copy", r"CLA Vocals v15.5.79.262", prog_num=11774):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11775) as should_copy_source_299_11775:
                    should_copy_source_299_11775()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=11776):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11777) as copy_dir_to_dir_300_11777:
                            copy_dir_to_dir_300_11777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=11778) as unwtar_301_11778:
                            unwtar_301_11778()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=11779, recursive=True) as chown_302_11779:
                            chown_302_11779()
            with Stage(r"copy", r"Center v15.5.79.262", prog_num=11780):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11781) as should_copy_source_303_11781:
                    should_copy_source_303_11781()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=11782):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=11783) as copy_dir_to_dir_304_11783:
                            copy_dir_to_dir_304_11783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=11784) as unwtar_305_11784:
                            unwtar_305_11784()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Center.bundle", user_id=-1, group_id=-1, prog_num=11785, recursive=True) as chown_306_11785:
                            chown_306_11785()
            with Stage(r"copy", r"Clarity Vx v15.5.79.262", prog_num=11786):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11787) as should_copy_source_307_11787:
                    should_copy_source_307_11787()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=11788):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=11789) as copy_dir_to_dir_308_11789:
                            copy_dir_to_dir_308_11789()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=11790) as unwtar_309_11790:
                            unwtar_309_11790()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=11791, recursive=True) as chown_310_11791:
                            chown_310_11791()
            with Stage(r"copy", r"Saphira v15.5.79.262", prog_num=11792):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11793) as should_copy_source_311_11793:
                    should_copy_source_311_11793()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=11794):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=11795) as copy_dir_to_dir_312_11795:
                            copy_dir_to_dir_312_11795()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=11796) as unwtar_313_11796:
                            unwtar_313_11796()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Saphira.bundle", user_id=-1, group_id=-1, prog_num=11797, recursive=True) as chown_314_11797:
                            chown_314_11797()
            with Stage(r"copy", r"Submarine v15.5.79.262", prog_num=11798):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11799) as should_copy_source_315_11799:
                    should_copy_source_315_11799()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=11800):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=11801) as copy_dir_to_dir_316_11801:
                            copy_dir_to_dir_316_11801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=11802) as unwtar_317_11802:
                            unwtar_317_11802()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Submarine.bundle", user_id=-1, group_id=-1, prog_num=11803, recursive=True) as chown_318_11803:
                            chown_318_11803()
            with Stage(r"copy", r"DeBreath v15.5.79.262", prog_num=11804):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11805) as should_copy_source_319_11805:
                    should_copy_source_319_11805()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=11806):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=11807) as copy_dir_to_dir_320_11807:
                            copy_dir_to_dir_320_11807()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=11808) as unwtar_321_11808:
                            unwtar_321_11808()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=11809, recursive=True) as chown_322_11809:
                            chown_322_11809()
            with Stage(r"copy", r"DeEsser v15.5.79.262", prog_num=11810):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11811) as should_copy_source_323_11811:
                    should_copy_source_323_11811()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=11812):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=11813) as copy_dir_to_dir_324_11813:
                            copy_dir_to_dir_324_11813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=11814) as unwtar_325_11814:
                            unwtar_325_11814()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=11815, recursive=True) as chown_326_11815:
                            chown_326_11815()
            with Stage(r"copy", r"Doppler v15.5.79.262", prog_num=11816):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11817) as should_copy_source_327_11817:
                    should_copy_source_327_11817()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=11818):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=11819) as copy_dir_to_dir_328_11819:
                            copy_dir_to_dir_328_11819()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=11820) as unwtar_329_11820:
                            unwtar_329_11820()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doppler.bundle", user_id=-1, group_id=-1, prog_num=11821, recursive=True) as chown_330_11821:
                            chown_330_11821()
            with Stage(r"copy", r"Doubler v15.5.79.262", prog_num=11822):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11823) as should_copy_source_331_11823:
                    should_copy_source_331_11823()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=11824):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=11825) as copy_dir_to_dir_332_11825:
                            copy_dir_to_dir_332_11825()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=11826) as unwtar_333_11826:
                            unwtar_333_11826()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Doubler.bundle", user_id=-1, group_id=-1, prog_num=11827, recursive=True) as chown_334_11827:
                            chown_334_11827()
            with Stage(r"copy", r"EMO-F2 v15.5.79.262", prog_num=11828):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11829) as should_copy_source_335_11829:
                    should_copy_source_335_11829()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=11830):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=11831) as copy_dir_to_dir_336_11831:
                            copy_dir_to_dir_336_11831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=11832) as unwtar_337_11832:
                            unwtar_337_11832()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=11833, recursive=True) as chown_338_11833:
                            chown_338_11833()
            with Stage(r"copy", r"EMO-Q4 v15.5.79.262", prog_num=11834):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11835) as should_copy_source_339_11835:
                    should_copy_source_339_11835()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=11836):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=11837) as copy_dir_to_dir_340_11837:
                            copy_dir_to_dir_340_11837()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=11838) as unwtar_341_11838:
                            unwtar_341_11838()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=11839, recursive=True) as chown_342_11839:
                            chown_342_11839()
            with Stage(r"copy", r"EddieKramer DR v15.5.79.262", prog_num=11840):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11841) as should_copy_source_343_11841:
                    should_copy_source_343_11841()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=11842):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=11843) as copy_dir_to_dir_344_11843:
                            copy_dir_to_dir_344_11843()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=11844) as unwtar_345_11844:
                            unwtar_345_11844()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=11845, recursive=True) as chown_346_11845:
                            chown_346_11845()
            with Stage(r"copy", r"EddieKramer VC v15.5.79.262", prog_num=11846):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11847) as should_copy_source_347_11847:
                    should_copy_source_347_11847()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=11848):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=11849) as copy_dir_to_dir_348_11849:
                            copy_dir_to_dir_348_11849()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=11850) as unwtar_349_11850:
                            unwtar_349_11850()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=11851, recursive=True) as chown_350_11851:
                            chown_350_11851()
            with Stage(r"copy", r"Electric Grand 80 v15.5.79.262", prog_num=11852):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11853) as should_copy_source_351_11853:
                    should_copy_source_351_11853()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=11854):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=11855) as copy_dir_to_dir_352_11855:
                            copy_dir_to_dir_352_11855()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=11856) as unwtar_353_11856:
                            unwtar_353_11856()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=11857, recursive=True) as chown_354_11857:
                            chown_354_11857()
            with Stage(r"copy", r"Enigma v15.5.79.262", prog_num=11858):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11859) as should_copy_source_355_11859:
                    should_copy_source_355_11859()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=11860):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=11861) as copy_dir_to_dir_356_11861:
                            copy_dir_to_dir_356_11861()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=11862) as unwtar_357_11862:
                            unwtar_357_11862()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Enigma.bundle", user_id=-1, group_id=-1, prog_num=11863, recursive=True) as chown_358_11863:
                            chown_358_11863()
            with Stage(r"copy", r"GTRAmp v15.5.79.262", prog_num=11864):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11865) as should_copy_source_359_11865:
                    should_copy_source_359_11865()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=11866):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=11867) as copy_dir_to_dir_360_11867:
                            copy_dir_to_dir_360_11867()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=11868) as unwtar_361_11868:
                            unwtar_361_11868()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=11869, recursive=True) as chown_362_11869:
                            chown_362_11869()
            with Stage(r"copy", r"GTRStomp v15.5.79.262", prog_num=11870):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11871) as should_copy_source_363_11871:
                    should_copy_source_363_11871()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=11872):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=11873) as copy_dir_to_dir_364_11873:
                            copy_dir_to_dir_364_11873()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=11874) as unwtar_365_11874:
                            unwtar_365_11874()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=11875, recursive=True) as chown_366_11875:
                            chown_366_11875()
            with Stage(r"copy", r"GTRToolRack v15.5.79.262", prog_num=11876):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11877) as should_copy_source_367_11877:
                    should_copy_source_367_11877()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=11878):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=11879) as copy_dir_to_dir_368_11879:
                            copy_dir_to_dir_368_11879()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=11880) as unwtar_369_11880:
                            unwtar_369_11880()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=11881, recursive=True) as chown_370_11881:
                            chown_370_11881()
            with Stage(r"copy", r"GTRTuner v15.5.79.262", prog_num=11882):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11883) as should_copy_source_371_11883:
                    should_copy_source_371_11883()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=11884):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=11885) as copy_dir_to_dir_372_11885:
                            copy_dir_to_dir_372_11885()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=11886) as unwtar_373_11886:
                            unwtar_373_11886()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=11887, recursive=True) as chown_374_11887:
                            chown_374_11887()
            with Stage(r"copy", r"Greg Wells MixCentric v15.5.79.262", prog_num=11888):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11889) as should_copy_source_375_11889:
                    should_copy_source_375_11889()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=11890):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=11891) as copy_dir_to_dir_376_11891:
                            copy_dir_to_dir_376_11891()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=11892) as unwtar_377_11892:
                            unwtar_377_11892()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=11893, recursive=True) as chown_378_11893:
                            chown_378_11893()
            with Stage(r"copy", r"Greg Wells PianoCentric v15.5.79.262", prog_num=11894):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11895) as should_copy_source_379_11895:
                    should_copy_source_379_11895()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=11896):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=11897) as copy_dir_to_dir_380_11897:
                            copy_dir_to_dir_380_11897()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=11898) as unwtar_381_11898:
                            unwtar_381_11898()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=11899, recursive=True) as chown_382_11899:
                            chown_382_11899()
            with Stage(r"copy", r"Greg Wells ToneCentric v15.5.79.262", prog_num=11900):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11901) as should_copy_source_383_11901:
                    should_copy_source_383_11901()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=11902):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=11903) as copy_dir_to_dir_384_11903:
                            copy_dir_to_dir_384_11903()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=11904) as unwtar_385_11904:
                            unwtar_385_11904()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=11905, recursive=True) as chown_386_11905:
                            chown_386_11905()
            with Stage(r"copy", r"H-Comp v15.5.79.262", prog_num=11906):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11907) as should_copy_source_387_11907:
                    should_copy_source_387_11907()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=11908):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=11909) as copy_dir_to_dir_388_11909:
                            copy_dir_to_dir_388_11909()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=11910) as unwtar_389_11910:
                            unwtar_389_11910()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=11911, recursive=True) as chown_390_11911:
                            chown_390_11911()
            with Stage(r"copy", r"H-Delay v15.5.79.262", prog_num=11912):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11913) as should_copy_source_391_11913:
                    should_copy_source_391_11913()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=11914):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=11915) as copy_dir_to_dir_392_11915:
                            copy_dir_to_dir_392_11915()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=11916) as unwtar_393_11916:
                            unwtar_393_11916()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=11917, recursive=True) as chown_394_11917:
                            chown_394_11917()
            with Stage(r"copy", r"H-Reverb v15.5.79.262", prog_num=11918):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11919) as should_copy_source_395_11919:
                    should_copy_source_395_11919()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=11920):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=11921) as copy_dir_to_dir_396_11921:
                            copy_dir_to_dir_396_11921()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=11922) as unwtar_397_11922:
                            unwtar_397_11922()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=11923, recursive=True) as chown_398_11923:
                            chown_398_11923()
            with Stage(r"copy", r"IR-L v15.5.79.262", prog_num=11924):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11925) as should_copy_source_399_11925:
                    should_copy_source_399_11925()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=11926):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=11927) as copy_dir_to_dir_400_11927:
                            copy_dir_to_dir_400_11927()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=11928) as unwtar_401_11928:
                            unwtar_401_11928()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/IR-L.bundle", user_id=-1, group_id=-1, prog_num=11929, recursive=True) as chown_402_11929:
                            chown_402_11929()
            with Stage(r"copy", r"InPhase v15.5.79.262", prog_num=11930):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11931) as should_copy_source_403_11931:
                    should_copy_source_403_11931()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=11932):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=11933) as copy_dir_to_dir_404_11933:
                            copy_dir_to_dir_404_11933()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=11934) as unwtar_405_11934:
                            unwtar_405_11934()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase.bundle", user_id=-1, group_id=-1, prog_num=11935, recursive=True) as chown_406_11935:
                            chown_406_11935()
            with Stage(r"copy", r"InPhase LT v15.5.79.262", prog_num=11936):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11937) as should_copy_source_407_11937:
                    should_copy_source_407_11937()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=11938):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=11939) as copy_dir_to_dir_408_11939:
                            copy_dir_to_dir_408_11939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=11940) as unwtar_409_11940:
                            unwtar_409_11940()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=11941, recursive=True) as chown_410_11941:
                            chown_410_11941()
            with Stage(r"copy", r"J37 v15.5.79.262", prog_num=11942):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11943) as should_copy_source_411_11943:
                    should_copy_source_411_11943()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=11944):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=11945) as copy_dir_to_dir_412_11945:
                            copy_dir_to_dir_412_11945()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=11946) as unwtar_413_11946:
                            unwtar_413_11946()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/J37.bundle", user_id=-1, group_id=-1, prog_num=11947, recursive=True) as chown_414_11947:
                            chown_414_11947()
            with Stage(r"copy", r"JJP-Vocals v15.5.79.262", prog_num=11948):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11949) as should_copy_source_415_11949:
                    should_copy_source_415_11949()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=11950):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=11951) as copy_dir_to_dir_416_11951:
                            copy_dir_to_dir_416_11951()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=11952) as unwtar_417_11952:
                            unwtar_417_11952()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=11953, recursive=True) as chown_418_11953:
                            chown_418_11953()
            with Stage(r"copy", r"Key Detector v15.5.79.262", prog_num=11954):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11955) as should_copy_source_419_11955:
                    should_copy_source_419_11955()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=11956):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=11957) as copy_dir_to_dir_420_11957:
                            copy_dir_to_dir_420_11957()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=11958) as unwtar_421_11958:
                            unwtar_421_11958()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=11959, recursive=True) as chown_422_11959:
                            chown_422_11959()
            with Stage(r"copy", r"KingsMic v15.5.79.262", prog_num=11960):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11961) as should_copy_source_423_11961:
                    should_copy_source_423_11961()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=11962):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=11963) as copy_dir_to_dir_424_11963:
                            copy_dir_to_dir_424_11963()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=11964) as unwtar_425_11964:
                            unwtar_425_11964()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=11965, recursive=True) as chown_426_11965:
                            chown_426_11965()
            with Stage(r"copy", r"KramerHLS v15.5.79.262", prog_num=11966):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11967) as should_copy_source_427_11967:
                    should_copy_source_427_11967()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=11968):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=11969) as copy_dir_to_dir_428_11969:
                            copy_dir_to_dir_428_11969()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=11970) as unwtar_429_11970:
                            unwtar_429_11970()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=11971, recursive=True) as chown_430_11971:
                            chown_430_11971()
            with Stage(r"copy", r"KramerPIE v15.5.79.262", prog_num=11972):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11973) as should_copy_source_431_11973:
                    should_copy_source_431_11973()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=11974):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=11975) as copy_dir_to_dir_432_11975:
                            copy_dir_to_dir_432_11975()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=11976) as unwtar_433_11976:
                            unwtar_433_11976()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=11977, recursive=True) as chown_434_11977:
                            chown_434_11977()
            with Stage(r"copy", r"KramerTape v15.5.79.262", prog_num=11978):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11979) as should_copy_source_435_11979:
                    should_copy_source_435_11979()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=11980):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=11981) as copy_dir_to_dir_436_11981:
                            copy_dir_to_dir_436_11981()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=11982) as unwtar_437_11982:
                            unwtar_437_11982()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=11983, recursive=True) as chown_438_11983:
                            chown_438_11983()
            with Stage(r"copy", r"L1 v15.5.79.262", prog_num=11984):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11985) as should_copy_source_439_11985:
                    should_copy_source_439_11985()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=11986):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=11987) as copy_dir_to_dir_440_11987:
                            copy_dir_to_dir_440_11987()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=11988) as unwtar_441_11988:
                            unwtar_441_11988()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L1.bundle", user_id=-1, group_id=-1, prog_num=11989, recursive=True) as chown_442_11989:
                            chown_442_11989()
            with Stage(r"copy", r"L2 v15.5.79.262", prog_num=11990):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11991) as should_copy_source_443_11991:
                    should_copy_source_443_11991()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=11992):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=11993) as copy_dir_to_dir_444_11993:
                            copy_dir_to_dir_444_11993()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=11994) as unwtar_445_11994:
                            unwtar_445_11994()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L2.bundle", user_id=-1, group_id=-1, prog_num=11995, recursive=True) as chown_446_11995:
                            chown_446_11995()
            with Stage(r"copy", r"L3-16 v15.5.79.262", prog_num=11996):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=11997) as should_copy_source_447_11997:
                    should_copy_source_447_11997()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=11998):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=11999) as copy_dir_to_dir_448_11999:
                            copy_dir_to_dir_448_11999()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=12000) as unwtar_449_12000:
                            unwtar_449_12000()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-16.bundle", user_id=-1, group_id=-1, prog_num=12001, recursive=True) as chown_450_12001:
                            chown_450_12001()
            with Stage(r"copy", r"L3-LL Multi v15.5.79.262", prog_num=12002):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12003) as should_copy_source_451_12003:
                    should_copy_source_451_12003()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=12004):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=12005) as copy_dir_to_dir_452_12005:
                            copy_dir_to_dir_452_12005()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=12006) as unwtar_453_12006:
                            unwtar_453_12006()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=12007, recursive=True) as chown_454_12007:
                            chown_454_12007()
            with Stage(r"copy", r"L3-LL Ultra v15.5.79.262", prog_num=12008):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12009) as should_copy_source_455_12009:
                    should_copy_source_455_12009()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=12010):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=12011) as copy_dir_to_dir_456_12011:
                            copy_dir_to_dir_456_12011()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=12012) as unwtar_457_12012:
                            unwtar_457_12012()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=12013, recursive=True) as chown_458_12013:
                            chown_458_12013()
            with Stage(r"copy", r"L3 Multi v15.5.79.262", prog_num=12014):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12015) as should_copy_source_459_12015:
                    should_copy_source_459_12015()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=12016):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=12017) as copy_dir_to_dir_460_12017:
                            copy_dir_to_dir_460_12017()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=12018) as unwtar_461_12018:
                            unwtar_461_12018()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=12019, recursive=True) as chown_462_12019:
                            chown_462_12019()
            with Stage(r"copy", r"L3 Ultra v15.5.79.262", prog_num=12020):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12021) as should_copy_source_463_12021:
                    should_copy_source_463_12021()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=12022):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=12023) as copy_dir_to_dir_464_12023:
                            copy_dir_to_dir_464_12023()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=12024) as unwtar_465_12024:
                            unwtar_465_12024()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=12025, recursive=True) as chown_466_12025:
                            chown_466_12025()
            with Stage(r"copy", r"LinEQ v15.5.79.262", prog_num=12026):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12027) as should_copy_source_467_12027:
                    should_copy_source_467_12027()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=12028):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=12029) as copy_dir_to_dir_468_12029:
                            copy_dir_to_dir_468_12029()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=12030) as unwtar_469_12030:
                            unwtar_469_12030()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=12031, recursive=True) as chown_470_12031:
                            chown_470_12031()
            with Stage(r"copy", r"LinMB v15.5.79.262", prog_num=12032):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12033) as should_copy_source_471_12033:
                    should_copy_source_471_12033()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=12034):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=12035) as copy_dir_to_dir_472_12035:
                            copy_dir_to_dir_472_12035()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=12036) as unwtar_473_12036:
                            unwtar_473_12036()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LinMB.bundle", user_id=-1, group_id=-1, prog_num=12037, recursive=True) as chown_474_12037:
                            chown_474_12037()
            with Stage(r"copy", r"LoAir v15.5.79.262", prog_num=12038):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12039) as should_copy_source_475_12039:
                    should_copy_source_475_12039()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=12040):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=12041) as copy_dir_to_dir_476_12041:
                            copy_dir_to_dir_476_12041()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=12042) as unwtar_477_12042:
                            unwtar_477_12042()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/LoAir.bundle", user_id=-1, group_id=-1, prog_num=12043, recursive=True) as chown_478_12043:
                            chown_478_12043()
            with Stage(r"copy", r"Lofi Space v15.5.79.262", prog_num=12044):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12045) as should_copy_source_479_12045:
                    should_copy_source_479_12045()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=12046):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=12047) as copy_dir_to_dir_480_12047:
                            copy_dir_to_dir_480_12047()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=12048) as unwtar_481_12048:
                            unwtar_481_12048()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=12049, recursive=True) as chown_482_12049:
                            chown_482_12049()
            with Stage(r"copy", r"MV2 v15.5.79.262", prog_num=12050):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12051) as should_copy_source_483_12051:
                    should_copy_source_483_12051()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=12052):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=12053) as copy_dir_to_dir_484_12053:
                            copy_dir_to_dir_484_12053()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=12054) as unwtar_485_12054:
                            unwtar_485_12054()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MV2.bundle", user_id=-1, group_id=-1, prog_num=12055, recursive=True) as chown_486_12055:
                            chown_486_12055()
            with Stage(r"copy", r"Magma Springs v15.5.79.262", prog_num=12056):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12057) as should_copy_source_487_12057:
                    should_copy_source_487_12057()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=12058):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=12059) as copy_dir_to_dir_488_12059:
                            copy_dir_to_dir_488_12059()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=12060) as unwtar_489_12060:
                            unwtar_489_12060()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=12061, recursive=True) as chown_490_12061:
                            chown_490_12061()
            with Stage(r"copy", r"MannyM-TripleD v15.5.79.262", prog_num=12062):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12063) as should_copy_source_491_12063:
                    should_copy_source_491_12063()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=12064):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=12065) as copy_dir_to_dir_492_12065:
                            copy_dir_to_dir_492_12065()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=12066) as unwtar_493_12066:
                            unwtar_493_12066()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=12067, recursive=True) as chown_494_12067:
                            chown_494_12067()
            with Stage(r"copy", r"Maserati DRM v15.5.79.262", prog_num=12068):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12069) as should_copy_source_495_12069:
                    should_copy_source_495_12069()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=12070):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=12071) as copy_dir_to_dir_496_12071:
                            copy_dir_to_dir_496_12071()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=12072) as unwtar_497_12072:
                            unwtar_497_12072()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=12073, recursive=True) as chown_498_12073:
                            chown_498_12073()
            with Stage(r"copy", r"Maserati VX1 v15.5.79.262", prog_num=12074):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12075) as should_copy_source_499_12075:
                    should_copy_source_499_12075()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=12076):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=12077) as copy_dir_to_dir_500_12077:
                            copy_dir_to_dir_500_12077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=12078) as unwtar_501_12078:
                            unwtar_501_12078()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=12079, recursive=True) as chown_502_12079:
                            chown_502_12079()
            with Stage(r"copy", r"MaxxBass v15.5.79.262", prog_num=12080):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12081) as should_copy_source_503_12081:
                    should_copy_source_503_12081()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=12082):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=12083) as copy_dir_to_dir_504_12083:
                            copy_dir_to_dir_504_12083()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=12084) as unwtar_505_12084:
                            unwtar_505_12084()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=12085, recursive=True) as chown_506_12085:
                            chown_506_12085()
            with Stage(r"copy", r"MaxxVolume v15.5.79.262", prog_num=12086):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12087) as should_copy_source_507_12087:
                    should_copy_source_507_12087()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=12088):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=12089) as copy_dir_to_dir_508_12089:
                            copy_dir_to_dir_508_12089()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=12090) as unwtar_509_12090:
                            unwtar_509_12090()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=12091, recursive=True) as chown_510_12091:
                            chown_510_12091()
            with Stage(r"copy", r"MetaFilter v15.5.79.262", prog_num=12092):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12093) as should_copy_source_511_12093:
                    should_copy_source_511_12093()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=12094):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=12095) as copy_dir_to_dir_512_12095:
                            copy_dir_to_dir_512_12095()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=12096) as unwtar_513_12096:
                            unwtar_513_12096()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=12097, recursive=True) as chown_514_12097:
                            chown_514_12097()
            with Stage(r"copy", r"MetaFlanger v15.5.79.262", prog_num=12098):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12099) as should_copy_source_515_12099:
                    should_copy_source_515_12099()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=12100):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12101) as copy_dir_to_dir_516_12101:
                            copy_dir_to_dir_516_12101()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=12102) as unwtar_517_12102:
                            unwtar_517_12102()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=12103, recursive=True) as chown_518_12103:
                            chown_518_12103()
            with Stage(r"copy", r"MondoMod v15.5.79.262", prog_num=12104):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12105) as should_copy_source_519_12105:
                    should_copy_source_519_12105()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=12106):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=12107) as copy_dir_to_dir_520_12107:
                            copy_dir_to_dir_520_12107()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=12108) as unwtar_521_12108:
                            unwtar_521_12108()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=12109, recursive=True) as chown_522_12109:
                            chown_522_12109()
            with Stage(r"copy", r"Morphoder v15.5.79.262", prog_num=12110):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12111) as should_copy_source_523_12111:
                    should_copy_source_523_12111()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=12112):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=12113) as copy_dir_to_dir_524_12113:
                            copy_dir_to_dir_524_12113()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=12114) as unwtar_525_12114:
                            unwtar_525_12114()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=12115, recursive=True) as chown_526_12115:
                            chown_526_12115()
            with Stage(r"copy", r"NLS v15.5.79.262", prog_num=12116):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12117) as should_copy_source_527_12117:
                    should_copy_source_527_12117()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=12118):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=12119) as copy_dir_to_dir_528_12119:
                            copy_dir_to_dir_528_12119()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=12120) as unwtar_529_12120:
                            unwtar_529_12120()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NLS.bundle", user_id=-1, group_id=-1, prog_num=12121, recursive=True) as chown_530_12121:
                            chown_530_12121()
            with Stage(r"copy", r"NX v15.5.79.262", prog_num=12122):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12123) as should_copy_source_531_12123:
                    should_copy_source_531_12123()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=12124):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=12125) as copy_dir_to_dir_532_12125:
                            copy_dir_to_dir_532_12125()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=12126) as unwtar_533_12126:
                            unwtar_533_12126()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/NX.bundle", user_id=-1, group_id=-1, prog_num=12127, recursive=True) as chown_534_12127:
                            chown_534_12127()
            with Stage(r"copy", r"OKDriver v15.5.79.262", prog_num=12128):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12129) as should_copy_source_535_12129:
                    should_copy_source_535_12129()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=12130):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=12131) as copy_dir_to_dir_536_12131:
                            copy_dir_to_dir_536_12131()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=12132) as unwtar_537_12132:
                            unwtar_537_12132()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=12133, recursive=True) as chown_538_12133:
                            chown_538_12133()
            with Stage(r"copy", r"OKFilter v15.5.79.262", prog_num=12134):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12135) as should_copy_source_539_12135:
                    should_copy_source_539_12135()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=12136):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=12137) as copy_dir_to_dir_540_12137:
                            copy_dir_to_dir_540_12137()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=12138) as unwtar_541_12138:
                            unwtar_541_12138()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=12139, recursive=True) as chown_542_12139:
                            chown_542_12139()
            with Stage(r"copy", r"OKPhatter v15.5.79.262", prog_num=12140):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12141) as should_copy_source_543_12141:
                    should_copy_source_543_12141()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=12142):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=12143) as copy_dir_to_dir_544_12143:
                            copy_dir_to_dir_544_12143()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=12144) as unwtar_545_12144:
                            unwtar_545_12144()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=12145, recursive=True) as chown_546_12145:
                            chown_546_12145()
            with Stage(r"copy", r"OKPumper v15.5.79.262", prog_num=12146):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12147) as should_copy_source_547_12147:
                    should_copy_source_547_12147()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=12148):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=12149) as copy_dir_to_dir_548_12149:
                            copy_dir_to_dir_548_12149()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=12150) as unwtar_549_12150:
                            unwtar_549_12150()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=12151, recursive=True) as chown_550_12151:
                            chown_550_12151()
            with Stage(r"copy", r"PAZ v15.5.79.262", prog_num=12152):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12153) as should_copy_source_551_12153:
                    should_copy_source_551_12153()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=12154):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=12155) as copy_dir_to_dir_552_12155:
                            copy_dir_to_dir_552_12155()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=12156) as unwtar_553_12156:
                            unwtar_553_12156()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PAZ.bundle", user_id=-1, group_id=-1, prog_num=12157, recursive=True) as chown_554_12157:
                            chown_554_12157()
            with Stage(r"copy", r"PS22 v15.5.79.262", prog_num=12158):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12159) as should_copy_source_555_12159:
                    should_copy_source_555_12159()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=12160):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=12161) as copy_dir_to_dir_556_12161:
                            copy_dir_to_dir_556_12161()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=12162) as unwtar_557_12162:
                            unwtar_557_12162()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PS22.bundle", user_id=-1, group_id=-1, prog_num=12163, recursive=True) as chown_558_12163:
                            chown_558_12163()
            with Stage(r"copy", r"PuigChild v15.5.79.262", prog_num=12164):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12165) as should_copy_source_559_12165:
                    should_copy_source_559_12165()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=12166):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=12167) as copy_dir_to_dir_560_12167:
                            copy_dir_to_dir_560_12167()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=12168) as unwtar_561_12168:
                            unwtar_561_12168()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=12169, recursive=True) as chown_562_12169:
                            chown_562_12169()
            with Stage(r"copy", r"PuigTec v15.5.79.262", prog_num=12170):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12171) as should_copy_source_563_12171:
                    should_copy_source_563_12171()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=12172):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=12173) as copy_dir_to_dir_564_12173:
                            copy_dir_to_dir_564_12173()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=12174) as unwtar_565_12174:
                            unwtar_565_12174()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=12175, recursive=True) as chown_566_12175:
                            chown_566_12175()
            with Stage(r"copy", r"Q10 v15.5.79.262", prog_num=12176):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12177) as should_copy_source_567_12177:
                    should_copy_source_567_12177()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=12178):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=12179) as copy_dir_to_dir_568_12179:
                            copy_dir_to_dir_568_12179()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=12180) as unwtar_569_12180:
                            unwtar_569_12180()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q10.bundle", user_id=-1, group_id=-1, prog_num=12181, recursive=True) as chown_570_12181:
                            chown_570_12181()
            with Stage(r"copy", r"Q-Clone v15.5.79.262", prog_num=12182):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12183) as should_copy_source_571_12183:
                    should_copy_source_571_12183()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=12184):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=12185) as copy_dir_to_dir_572_12185:
                            copy_dir_to_dir_572_12185()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=12186) as unwtar_573_12186:
                            unwtar_573_12186()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=12187, recursive=True) as chown_574_12187:
                            chown_574_12187()
            with Stage(r"copy", r"RBass v15.5.79.262", prog_num=12188):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12189) as should_copy_source_575_12189:
                    should_copy_source_575_12189()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=12190):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=12191) as copy_dir_to_dir_576_12191:
                            copy_dir_to_dir_576_12191()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=12192) as unwtar_577_12192:
                            unwtar_577_12192()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RBass.bundle", user_id=-1, group_id=-1, prog_num=12193, recursive=True) as chown_578_12193:
                            chown_578_12193()
            with Stage(r"copy", r"RChannel v15.5.79.262", prog_num=12194):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12195) as should_copy_source_579_12195:
                    should_copy_source_579_12195()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=12196):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=12197) as copy_dir_to_dir_580_12197:
                            copy_dir_to_dir_580_12197()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=12198) as unwtar_581_12198:
                            unwtar_581_12198()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RChannel.bundle", user_id=-1, group_id=-1, prog_num=12199, recursive=True) as chown_582_12199:
                            chown_582_12199()
            with Stage(r"copy", r"RComp v15.5.79.262", prog_num=12200):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12201) as should_copy_source_583_12201:
                    should_copy_source_583_12201()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=12202):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=12203) as copy_dir_to_dir_584_12203:
                            copy_dir_to_dir_584_12203()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=12204) as unwtar_585_12204:
                            unwtar_585_12204()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RComp.bundle", user_id=-1, group_id=-1, prog_num=12205, recursive=True) as chown_586_12205:
                            chown_586_12205()
            with Stage(r"copy", r"RDeEsser v15.5.79.262", prog_num=12206):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12207) as should_copy_source_587_12207:
                    should_copy_source_587_12207()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=12208):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=12209) as copy_dir_to_dir_588_12209:
                            copy_dir_to_dir_588_12209()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=12210) as unwtar_589_12210:
                            unwtar_589_12210()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=12211, recursive=True) as chown_590_12211:
                            chown_590_12211()
            with Stage(r"copy", r"REDD17 v15.5.79.262", prog_num=12212):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12213) as should_copy_source_591_12213:
                    should_copy_source_591_12213()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=12214):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=12215) as copy_dir_to_dir_592_12215:
                            copy_dir_to_dir_592_12215()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=12216) as unwtar_593_12216:
                            unwtar_593_12216()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD17.bundle", user_id=-1, group_id=-1, prog_num=12217, recursive=True) as chown_594_12217:
                            chown_594_12217()
            with Stage(r"copy", r"REDD37-51 v15.5.79.262", prog_num=12218):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12219) as should_copy_source_595_12219:
                    should_copy_source_595_12219()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=12220):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=12221) as copy_dir_to_dir_596_12221:
                            copy_dir_to_dir_596_12221()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=12222) as unwtar_597_12222:
                            unwtar_597_12222()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=12223, recursive=True) as chown_598_12223:
                            chown_598_12223()
            with Stage(r"copy", r"REQ v15.5.79.262", prog_num=12224):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12225) as should_copy_source_599_12225:
                    should_copy_source_599_12225()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=12226):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=12227) as copy_dir_to_dir_600_12227:
                            copy_dir_to_dir_600_12227()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=12228) as unwtar_601_12228:
                            unwtar_601_12228()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/REQ.bundle", user_id=-1, group_id=-1, prog_num=12229, recursive=True) as chown_602_12229:
                            chown_602_12229()
            with Stage(r"copy", r"RS56 v15.5.79.262", prog_num=12230):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12231) as should_copy_source_603_12231:
                    should_copy_source_603_12231()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=12232):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=12233) as copy_dir_to_dir_604_12233:
                            copy_dir_to_dir_604_12233()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=12234) as unwtar_605_12234:
                            unwtar_605_12234()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RS56.bundle", user_id=-1, group_id=-1, prog_num=12235, recursive=True) as chown_606_12235:
                            chown_606_12235()
            with Stage(r"copy", r"RVerb v15.5.79.262", prog_num=12236):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12237) as should_copy_source_607_12237:
                    should_copy_source_607_12237()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=12238):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=12239) as copy_dir_to_dir_608_12239:
                            copy_dir_to_dir_608_12239()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=12240) as unwtar_609_12240:
                            unwtar_609_12240()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVerb.bundle", user_id=-1, group_id=-1, prog_num=12241, recursive=True) as chown_610_12241:
                            chown_610_12241()
            with Stage(r"copy", r"RVox v15.5.79.262", prog_num=12242):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12243) as should_copy_source_611_12243:
                    should_copy_source_611_12243()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=12244):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=12245) as copy_dir_to_dir_612_12245:
                            copy_dir_to_dir_612_12245()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=12246) as unwtar_613_12246:
                            unwtar_613_12246()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RVox.bundle", user_id=-1, group_id=-1, prog_num=12247, recursive=True) as chown_614_12247:
                            chown_614_12247()
            with Stage(r"copy", r"Reel ADT v15.5.79.262", prog_num=12248):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12249) as should_copy_source_615_12249:
                    should_copy_source_615_12249()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=12250):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=12251) as copy_dir_to_dir_616_12251:
                            copy_dir_to_dir_616_12251()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=12252) as unwtar_617_12252:
                            unwtar_617_12252()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=12253, recursive=True) as chown_618_12253:
                            chown_618_12253()
            with Stage(r"copy", r"RenAxx v15.5.79.262", prog_num=12254):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12255) as should_copy_source_619_12255:
                    should_copy_source_619_12255()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=12256):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=12257) as copy_dir_to_dir_620_12257:
                            copy_dir_to_dir_620_12257()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=12258) as unwtar_621_12258:
                            unwtar_621_12258()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=12259, recursive=True) as chown_622_12259:
                            chown_622_12259()
            with Stage(r"copy", r"Retro Fi v15.5.79.262", prog_num=12260):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12261) as should_copy_source_623_12261:
                    should_copy_source_623_12261()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=12262):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=12263) as copy_dir_to_dir_624_12263:
                            copy_dir_to_dir_624_12263()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=12264) as unwtar_625_12264:
                            unwtar_625_12264()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=12265, recursive=True) as chown_626_12265:
                            chown_626_12265()
            with Stage(r"copy", r"S1 v15.5.79.262", prog_num=12266):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12267) as should_copy_source_627_12267:
                    should_copy_source_627_12267()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=12268):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=12269) as copy_dir_to_dir_628_12269:
                            copy_dir_to_dir_628_12269()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=12270) as unwtar_629_12270:
                            unwtar_629_12270()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/S1.bundle", user_id=-1, group_id=-1, prog_num=12271, recursive=True) as chown_630_12271:
                            chown_630_12271()
            with Stage(r"copy", r"Scheps 73 v15.5.79.262", prog_num=12272):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12273) as should_copy_source_631_12273:
                    should_copy_source_631_12273()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=12274):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=12275) as copy_dir_to_dir_632_12275:
                            copy_dir_to_dir_632_12275()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=12276) as unwtar_633_12276:
                            unwtar_633_12276()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=12277, recursive=True) as chown_634_12277:
                            chown_634_12277()
            with Stage(r"copy", r"Scheps Omni Channel v15.5.79.262", prog_num=12278):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12279) as should_copy_source_635_12279:
                    should_copy_source_635_12279()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=12280):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=12281) as copy_dir_to_dir_636_12281:
                            copy_dir_to_dir_636_12281()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=12282) as unwtar_637_12282:
                            unwtar_637_12282()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=12283, recursive=True) as chown_638_12283:
                            chown_638_12283()
            with Stage(r"copy", r"Scheps Parallel Particles v15.5.79.262", prog_num=12284):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12285) as should_copy_source_639_12285:
                    should_copy_source_639_12285()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=12286):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=12287) as copy_dir_to_dir_640_12287:
                            copy_dir_to_dir_640_12287()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=12288) as unwtar_641_12288:
                            unwtar_641_12288()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=12289, recursive=True) as chown_642_12289:
                            chown_642_12289()
            with Stage(r"copy", r"Sibilance v15.5.79.262", prog_num=12290):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12291) as should_copy_source_643_12291:
                    should_copy_source_643_12291()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=12292):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=12293) as copy_dir_to_dir_644_12293:
                            copy_dir_to_dir_644_12293()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=12294) as unwtar_645_12294:
                            unwtar_645_12294()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=12295, recursive=True) as chown_646_12295:
                            chown_646_12295()
            with Stage(r"copy", r"Emo Signal Generator v15.5.79.262", prog_num=12296):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12297) as should_copy_source_647_12297:
                    should_copy_source_647_12297()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=12298):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=12299) as copy_dir_to_dir_648_12299:
                            copy_dir_to_dir_648_12299()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=12300) as unwtar_649_12300:
                            unwtar_649_12300()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=12301, recursive=True) as chown_650_12301:
                            chown_650_12301()
            with Stage(r"copy", r"Silk Vocal v15.10.46.293", prog_num=12302):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12303) as should_copy_source_651_12303:
                    should_copy_source_651_12303()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=12304):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=12305) as copy_dir_to_dir_652_12305:
                            copy_dir_to_dir_652_12305()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=12306) as unwtar_653_12306:
                            unwtar_653_12306()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=12307, recursive=True) as chown_654_12307:
                            chown_654_12307()
            with Stage(r"copy", r"Smack Attack v15.5.79.262", prog_num=12308):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12309) as should_copy_source_655_12309:
                    should_copy_source_655_12309()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=12310):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=12311) as copy_dir_to_dir_656_12311:
                            copy_dir_to_dir_656_12311()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=12312) as unwtar_657_12312:
                            unwtar_657_12312()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=12313, recursive=True) as chown_658_12313:
                            chown_658_12313()
            with Stage(r"copy", r"SoundShifter v15.5.79.262", prog_num=12314):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12315) as should_copy_source_659_12315:
                    should_copy_source_659_12315()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=12316):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=12317) as copy_dir_to_dir_660_12317:
                            copy_dir_to_dir_660_12317()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=12318) as unwtar_661_12318:
                            unwtar_661_12318()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=12319, recursive=True) as chown_662_12319:
                            chown_662_12319()
            with Stage(r"copy", r"Spherix Immersive Compressor v15.5.79.262", prog_num=12320):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12321) as should_copy_source_663_12321:
                    should_copy_source_663_12321()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=12322):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=12323) as copy_dir_to_dir_664_12323:
                            copy_dir_to_dir_664_12323()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=12324) as unwtar_665_12324:
                            unwtar_665_12324()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=12325, recursive=True) as chown_666_12325:
                            chown_666_12325()
            with Stage(r"copy", r"Spherix Immersive Limiter v15.5.79.262", prog_num=12326):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12327) as should_copy_source_667_12327:
                    should_copy_source_667_12327()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=12328):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=12329) as copy_dir_to_dir_668_12329:
                            copy_dir_to_dir_668_12329()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=12330) as unwtar_669_12330:
                            unwtar_669_12330()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=12331, recursive=True) as chown_670_12331:
                            chown_670_12331()
            with Stage(r"copy", r"SuperTap v15.5.79.262", prog_num=12332):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12333) as should_copy_source_671_12333:
                    should_copy_source_671_12333()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=12334):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=12335) as copy_dir_to_dir_672_12335:
                            copy_dir_to_dir_672_12335()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=12336) as unwtar_673_12336:
                            unwtar_673_12336()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=12337, recursive=True) as chown_674_12337:
                            chown_674_12337()
            with Stage(r"copy", r"TG12345 v15.5.79.262", prog_num=12338):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12339) as should_copy_source_675_12339:
                    should_copy_source_675_12339()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=12340):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=12341) as copy_dir_to_dir_676_12341:
                            copy_dir_to_dir_676_12341()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=12342) as unwtar_677_12342:
                            unwtar_677_12342()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TG12345.bundle", user_id=-1, group_id=-1, prog_num=12343, recursive=True) as chown_678_12343:
                            chown_678_12343()
            with Stage(r"copy", r"AR TG Meter Bridge v15.5.79.262", prog_num=12344):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12345) as should_copy_source_679_12345:
                    should_copy_source_679_12345()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=12346):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=12347) as copy_dir_to_dir_680_12347:
                            copy_dir_to_dir_680_12347()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=12348) as unwtar_681_12348:
                            unwtar_681_12348()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=12349, recursive=True) as chown_682_12349:
                            chown_682_12349()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v15.5.79.262", prog_num=12350):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12351) as should_copy_source_683_12351:
                    should_copy_source_683_12351()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=12352):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=12353) as copy_dir_to_dir_684_12353:
                            copy_dir_to_dir_684_12353()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=12354) as unwtar_685_12354:
                            unwtar_685_12354()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=12355, recursive=True) as chown_686_12355:
                            chown_686_12355()
            with Stage(r"copy", r"TransX v15.5.79.262", prog_num=12356):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12357) as should_copy_source_687_12357:
                    should_copy_source_687_12357()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=12358):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=12359) as copy_dir_to_dir_688_12359:
                            copy_dir_to_dir_688_12359()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=12360) as unwtar_689_12360:
                            unwtar_689_12360()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TransX.bundle", user_id=-1, group_id=-1, prog_num=12361, recursive=True) as chown_690_12361:
                            chown_690_12361()
            with Stage(r"copy", r"TrueVerb v15.5.79.262", prog_num=12362):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12363) as should_copy_source_691_12363:
                    should_copy_source_691_12363()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=12364):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=12365) as copy_dir_to_dir_692_12365:
                            copy_dir_to_dir_692_12365()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=12366) as unwtar_693_12366:
                            unwtar_693_12366()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=12367, recursive=True) as chown_694_12367:
                            chown_694_12367()
            with Stage(r"copy", r"UM v15.5.79.262", prog_num=12368):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12369) as should_copy_source_695_12369:
                    should_copy_source_695_12369()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=12370):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=12371) as copy_dir_to_dir_696_12371:
                            copy_dir_to_dir_696_12371()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=12372) as unwtar_697_12372:
                            unwtar_697_12372()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UM.bundle", user_id=-1, group_id=-1, prog_num=12373, recursive=True) as chown_698_12373:
                            chown_698_12373()
            with Stage(r"copy", r"UltraPitch v15.5.79.262", prog_num=12374):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12375) as should_copy_source_699_12375:
                    should_copy_source_699_12375()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=12376):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=12377) as copy_dir_to_dir_700_12377:
                            copy_dir_to_dir_700_12377()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=12378) as unwtar_701_12378:
                            unwtar_701_12378()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=12379, recursive=True) as chown_702_12379:
                            chown_702_12379()
            with Stage(r"copy", r"VComp v15.5.79.262", prog_num=12380):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12381) as should_copy_source_703_12381:
                    should_copy_source_703_12381()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=12382):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=12383) as copy_dir_to_dir_704_12383:
                            copy_dir_to_dir_704_12383()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=12384) as unwtar_705_12384:
                            unwtar_705_12384()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VComp.bundle", user_id=-1, group_id=-1, prog_num=12385, recursive=True) as chown_706_12385:
                            chown_706_12385()
            with Stage(r"copy", r"VEQ3 v15.5.79.262", prog_num=12386):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12387) as should_copy_source_707_12387:
                    should_copy_source_707_12387()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=12388):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=12389) as copy_dir_to_dir_708_12389:
                            copy_dir_to_dir_708_12389()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=12390) as unwtar_709_12390:
                            unwtar_709_12390()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=12391, recursive=True) as chown_710_12391:
                            chown_710_12391()
            with Stage(r"copy", r"VEQ4 v15.5.79.262", prog_num=12392):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12393) as should_copy_source_711_12393:
                    should_copy_source_711_12393()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=12394):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=12395) as copy_dir_to_dir_712_12395:
                            copy_dir_to_dir_712_12395()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=12396) as unwtar_713_12396:
                            unwtar_713_12396()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=12397, recursive=True) as chown_714_12397:
                            chown_714_12397()
            with Stage(r"copy", r"VU Meter v15.5.79.262", prog_num=12398):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12399) as should_copy_source_715_12399:
                    should_copy_source_715_12399()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=12400):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=12401) as copy_dir_to_dir_716_12401:
                            copy_dir_to_dir_716_12401()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=12402) as unwtar_717_12402:
                            unwtar_717_12402()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=12403, recursive=True) as chown_718_12403:
                            chown_718_12403()
            with Stage(r"copy", r"Vitamin v15.5.79.262", prog_num=12404):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12405) as should_copy_source_719_12405:
                    should_copy_source_719_12405()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=12406):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=12407) as copy_dir_to_dir_720_12407:
                            copy_dir_to_dir_720_12407()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=12408) as unwtar_721_12408:
                            unwtar_721_12408()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=12409, recursive=True) as chown_722_12409:
                            chown_722_12409()
            with Stage(r"copy", r"Vocal Rider v15.5.79.262", prog_num=12410):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12411) as should_copy_source_723_12411:
                    should_copy_source_723_12411()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=12412):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=12413) as copy_dir_to_dir_724_12413:
                            copy_dir_to_dir_724_12413()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=12414) as unwtar_725_12414:
                            unwtar_725_12414()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=12415, recursive=True) as chown_726_12415:
                            chown_726_12415()
            with Stage(r"copy", r"Voltage Amps Bass v15.5.79.262", prog_num=12416):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12417) as should_copy_source_727_12417:
                    should_copy_source_727_12417()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=12418):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=12419) as copy_dir_to_dir_728_12419:
                            copy_dir_to_dir_728_12419()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=12420) as unwtar_729_12420:
                            unwtar_729_12420()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=12421, recursive=True) as chown_730_12421:
                            chown_730_12421()
            with Stage(r"copy", r"Voltage Amps Guitar v15.5.79.262", prog_num=12422):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12423) as should_copy_source_731_12423:
                    should_copy_source_731_12423()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=12424):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=12425) as copy_dir_to_dir_732_12425:
                            copy_dir_to_dir_732_12425()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=12426) as unwtar_733_12426:
                            unwtar_733_12426()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=12427, recursive=True) as chown_734_12427:
                            chown_734_12427()
            with Stage(r"copy", r"WLM v15.5.79.262", prog_num=12428):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12429) as should_copy_source_735_12429:
                    should_copy_source_735_12429()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=12430):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=12431) as copy_dir_to_dir_736_12431:
                            copy_dir_to_dir_736_12431()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=12432) as unwtar_737_12432:
                            unwtar_737_12432()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM.bundle", user_id=-1, group_id=-1, prog_num=12433, recursive=True) as chown_738_12433:
                            chown_738_12433()
            with Stage(r"copy", r"WLM Plus v15.5.79.262", prog_num=12434):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12435) as should_copy_source_739_12435:
                    should_copy_source_739_12435()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=12436):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=12437) as copy_dir_to_dir_740_12437:
                            copy_dir_to_dir_740_12437()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=12438) as unwtar_741_12438:
                            unwtar_741_12438()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=12439, recursive=True) as chown_742_12439:
                            chown_742_12439()
            with Stage(r"copy", r"WavesHeadTracker v15.5.79.262", prog_num=12440):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=5, prog_num=12441) as should_copy_source_743_12441:
                    should_copy_source_743_12441()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=12442):
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=12443) as rm_file_or_dir_744_12443:
                            rm_file_or_dir_744_12443()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=12444) as copy_dir_to_dir_745_12444:
                            copy_dir_to_dir_745_12444()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=12445) as unwtar_746_12445:
                            unwtar_746_12445()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=12446, recursive=True) as chown_747_12446:
                            chown_747_12446()
            with Stage(r"copy", r"WavesLib1_15_10_46_293 v15.10.46.293", prog_num=12447):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12448) as should_copy_source_748_12448:
                    should_copy_source_748_12448()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.10.46.framework", prog_num=12449):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", r".", delete_extraneous_files=True, prog_num=12450) as copy_dir_to_dir_749_12450:
                            copy_dir_to_dir_749_12450()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.10.46.framework", where_to_unwtar=r".", prog_num=12451) as unwtar_750_12451:
                            unwtar_750_12451()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.10.46.framework", user_id=-1, group_id=-1, prog_num=12452, recursive=True) as chown_751_12452:
                            chown_751_12452()
            with Stage(r"copy", r"WavesLib1_15_5_139_322 v15.5.139.322", prog_num=12453):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12454) as should_copy_source_752_12454:
                    should_copy_source_752_12454()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.139.framework", prog_num=12455):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", r".", delete_extraneous_files=True, prog_num=12456) as copy_dir_to_dir_753_12456:
                            copy_dir_to_dir_753_12456()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.139.framework", where_to_unwtar=r".", prog_num=12457) as unwtar_754_12457:
                            unwtar_754_12457()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.139.framework", user_id=-1, group_id=-1, prog_num=12458, recursive=True) as chown_755_12458:
                            chown_755_12458()
            with Stage(r"copy", r"WavesLib1_15_5_79_262 v15.5.79.262", prog_num=12459):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12460) as should_copy_source_756_12460:
                    should_copy_source_756_12460()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_15.5.79.framework", prog_num=12461):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", r".", delete_extraneous_files=True, prog_num=12462) as copy_dir_to_dir_757_12462:
                            copy_dir_to_dir_757_12462()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesLib1_15.5.79.framework", where_to_unwtar=r".", prog_num=12463) as unwtar_758_12463:
                            unwtar_758_12463()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesLib1_15.5.79.framework", user_id=-1, group_id=-1, prog_num=12464, recursive=True) as chown_759_12464:
                            chown_759_12464()
            with Stage(r"copy", r"WavesTune v15.5.79.262", prog_num=12465):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12466) as should_copy_source_760_12466:
                    should_copy_source_760_12466()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=12467):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=12468) as copy_dir_to_dir_761_12468:
                            copy_dir_to_dir_761_12468()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=12469) as unwtar_762_12469:
                            unwtar_762_12469()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=12470, recursive=True) as chown_763_12470:
                            chown_763_12470()
            with Stage(r"copy", r"WavesTune LT v15.5.79.262", prog_num=12471):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12472) as should_copy_source_764_12472:
                    should_copy_source_764_12472()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=12473):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=12474) as copy_dir_to_dir_765_12474:
                            copy_dir_to_dir_765_12474()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=12475) as unwtar_766_12475:
                            unwtar_766_12475()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=12476, recursive=True) as chown_767_12476:
                            chown_767_12476()
            with Stage(r"copy", r"Waves Harmony v15.5.139.322", prog_num=12477):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12478) as should_copy_source_768_12478:
                    should_copy_source_768_12478()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=12479):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=12480) as copy_dir_to_dir_769_12480:
                            copy_dir_to_dir_769_12480()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=12481) as unwtar_770_12481:
                            unwtar_770_12481()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=12482, recursive=True) as chown_771_12482:
                            chown_771_12482()
            with Stage(r"copy", r"Waves Tune Real-Time v15.5.79.262", prog_num=12483):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12484) as should_copy_source_772_12484:
                    should_copy_source_772_12484()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=12485):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=12486) as copy_dir_to_dir_773_12486:
                            copy_dir_to_dir_773_12486()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=12487) as unwtar_774_12487:
                            unwtar_774_12487()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=12488, recursive=True) as chown_775_12488:
                            chown_775_12488()
            with Stage(r"copy", r"X-Click v15.5.79.262", prog_num=12489):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12490) as should_copy_source_776_12490:
                    should_copy_source_776_12490()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=12491):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=12492) as copy_dir_to_dir_777_12492:
                            copy_dir_to_dir_777_12492()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=12493) as unwtar_778_12493:
                            unwtar_778_12493()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Click.bundle", user_id=-1, group_id=-1, prog_num=12494, recursive=True) as chown_779_12494:
                            chown_779_12494()
            with Stage(r"copy", r"X-Crackle v15.5.79.262", prog_num=12495):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12496) as should_copy_source_780_12496:
                    should_copy_source_780_12496()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=12497):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=12498) as copy_dir_to_dir_781_12498:
                            copy_dir_to_dir_781_12498()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=12499) as unwtar_782_12499:
                            unwtar_782_12499()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=12500, recursive=True) as chown_783_12500:
                            chown_783_12500()
            with Stage(r"copy", r"X-Hum v15.5.79.262", prog_num=12501):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12502) as should_copy_source_784_12502:
                    should_copy_source_784_12502()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=12503):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=12504) as copy_dir_to_dir_785_12504:
                            copy_dir_to_dir_785_12504()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=12505) as unwtar_786_12505:
                            unwtar_786_12505()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=12506, recursive=True) as chown_787_12506:
                            chown_787_12506()
            with Stage(r"copy", r"X-Noise v15.5.79.262", prog_num=12507):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12508) as should_copy_source_788_12508:
                    should_copy_source_788_12508()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=12509):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12510) as copy_dir_to_dir_789_12510:
                            copy_dir_to_dir_789_12510()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=12511) as unwtar_790_12511:
                            unwtar_790_12511()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=12512, recursive=True) as chown_791_12512:
                            chown_791_12512()
            with Stage(r"copy", r"Z-Noise v15.5.79.262", prog_num=12513):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V15", skip_progress_count=4, prog_num=12514) as should_copy_source_792_12514:
                    should_copy_source_792_12514()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=12515):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=12516) as copy_dir_to_dir_793_12516:
                            copy_dir_to_dir_793_12516()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=12517) as unwtar_794_12517:
                            unwtar_794_12517()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=12518, recursive=True) as chown_795_12518:
                            chown_795_12518()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V15", own_progress_count=6, prog_num=12524) as resolve_symlink_files_in_folder_796_12524:
                resolve_symlink_files_in_folder_796_12524()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V15" -c', ignore_all_errors=True, prog_num=12525) as shell_command_797_12525:
                shell_command_797_12525()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V15"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V15"/Icon?; fi', prog_num=12526) as script_command_798_12526:
                script_command_798_12526()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12527) as shell_command_799_12527:
                shell_command_799_12527()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12528) as create_symlink_800_12528:
                create_symlink_800_12528()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V15", r"/Applications/Waves/Plug-Ins V15", prog_num=12529) as create_symlink_801_12529:
                create_symlink_801_12529()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=12530) as copy_glob_to_dir_802_12530:
                copy_glob_to_dir_802_12530()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/Documents", prog_num=12531) as cd_stage_803_12531:
            cd_stage_803_12531()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=12532):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V15/Documents", skip_progress_count=3, prog_num=12533) as should_copy_source_804_12533:
                    should_copy_source_804_12533()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=12534):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=12535) as copy_file_to_dir_805_12535:
                            copy_file_to_dir_805_12535()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=12536) as chmod_and_chown_806_12536:
                            chmod_and_chown_806_12536()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V15/GTR", prog_num=12537) as cd_stage_807_12537:
            cd_stage_807_12537()
            with Stage(r"copy", r"GTR Stomps v15.5.79.262", prog_num=12538):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12539) as should_copy_source_808_12539:
                    should_copy_source_808_12539()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=12540):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=12541) as copy_dir_to_dir_809_12541:
                            copy_dir_to_dir_809_12541()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=12542) as unwtar_810_12542:
                            unwtar_810_12542()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=12543, recursive=True) as chown_811_12543:
                            chown_811_12543()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12544) as should_copy_source_812_12544:
                    should_copy_source_812_12544()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=12545):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=12546) as copy_dir_to_dir_813_12546:
                            copy_dir_to_dir_813_12546()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=12547) as unwtar_814_12547:
                            unwtar_814_12547()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=12548, recursive=True) as chown_815_12548:
                            chown_815_12548()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12549) as should_copy_source_816_12549:
                    should_copy_source_816_12549()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=12550):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=12551) as copy_dir_to_dir_817_12551:
                            copy_dir_to_dir_817_12551()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=12552) as unwtar_818_12552:
                            unwtar_818_12552()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=12553, recursive=True) as chown_819_12553:
                            chown_819_12553()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12554) as should_copy_source_820_12554:
                    should_copy_source_820_12554()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=12555):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=12556) as copy_dir_to_dir_821_12556:
                            copy_dir_to_dir_821_12556()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=12557) as unwtar_822_12557:
                            unwtar_822_12557()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=12558, recursive=True) as chown_823_12558:
                            chown_823_12558()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12559) as should_copy_source_824_12559:
                    should_copy_source_824_12559()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=12560):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=12561) as copy_dir_to_dir_825_12561:
                            copy_dir_to_dir_825_12561()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=12562) as unwtar_826_12562:
                            unwtar_826_12562()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=12563, recursive=True) as chown_827_12563:
                            chown_827_12563()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12564) as should_copy_source_828_12564:
                    should_copy_source_828_12564()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=12565):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=12566) as copy_dir_to_dir_829_12566:
                            copy_dir_to_dir_829_12566()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=12567) as unwtar_830_12567:
                            unwtar_830_12567()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=12568, recursive=True) as chown_831_12568:
                            chown_831_12568()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12569) as should_copy_source_832_12569:
                    should_copy_source_832_12569()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=12570):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=12571) as copy_dir_to_dir_833_12571:
                            copy_dir_to_dir_833_12571()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=12572) as unwtar_834_12572:
                            unwtar_834_12572()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=12573, recursive=True) as chown_835_12573:
                            chown_835_12573()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12574) as should_copy_source_836_12574:
                    should_copy_source_836_12574()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=12575):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=12576) as copy_dir_to_dir_837_12576:
                            copy_dir_to_dir_837_12576()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=12577) as unwtar_838_12577:
                            unwtar_838_12577()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=12578, recursive=True) as chown_839_12578:
                            chown_839_12578()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12579) as should_copy_source_840_12579:
                    should_copy_source_840_12579()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=12580):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=12581) as copy_dir_to_dir_841_12581:
                            copy_dir_to_dir_841_12581()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=12582) as unwtar_842_12582:
                            unwtar_842_12582()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=12583, recursive=True) as chown_843_12583:
                            chown_843_12583()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12584) as should_copy_source_844_12584:
                    should_copy_source_844_12584()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=12585):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=12586) as copy_dir_to_dir_845_12586:
                            copy_dir_to_dir_845_12586()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=12587) as unwtar_846_12587:
                            unwtar_846_12587()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=12588, recursive=True) as chown_847_12588:
                            chown_847_12588()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12589) as should_copy_source_848_12589:
                    should_copy_source_848_12589()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=12590):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=12591) as copy_dir_to_dir_849_12591:
                            copy_dir_to_dir_849_12591()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=12592) as unwtar_850_12592:
                            unwtar_850_12592()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=12593, recursive=True) as chown_851_12593:
                            chown_851_12593()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12594) as should_copy_source_852_12594:
                    should_copy_source_852_12594()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=12595):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=12596) as copy_dir_to_dir_853_12596:
                            copy_dir_to_dir_853_12596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=12597) as unwtar_854_12597:
                            unwtar_854_12597()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=12598, recursive=True) as chown_855_12598:
                            chown_855_12598()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12599) as should_copy_source_856_12599:
                    should_copy_source_856_12599()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=12600):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=12601) as copy_dir_to_dir_857_12601:
                            copy_dir_to_dir_857_12601()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=12602) as unwtar_858_12602:
                            unwtar_858_12602()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=12603, recursive=True) as chown_859_12603:
                            chown_859_12603()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12604) as should_copy_source_860_12604:
                    should_copy_source_860_12604()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=12605):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=12606) as copy_dir_to_dir_861_12606:
                            copy_dir_to_dir_861_12606()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=12607) as unwtar_862_12607:
                            unwtar_862_12607()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=12608, recursive=True) as chown_863_12608:
                            chown_863_12608()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12609) as should_copy_source_864_12609:
                    should_copy_source_864_12609()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=12610):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=12611) as copy_dir_to_dir_865_12611:
                            copy_dir_to_dir_865_12611()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=12612) as unwtar_866_12612:
                            unwtar_866_12612()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=12613, recursive=True) as chown_867_12613:
                            chown_867_12613()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12614) as should_copy_source_868_12614:
                    should_copy_source_868_12614()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=12615):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=12616) as copy_dir_to_dir_869_12616:
                            copy_dir_to_dir_869_12616()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=12617) as unwtar_870_12617:
                            unwtar_870_12617()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=12618, recursive=True) as chown_871_12618:
                            chown_871_12618()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12619) as should_copy_source_872_12619:
                    should_copy_source_872_12619()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=12620):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=12621) as copy_dir_to_dir_873_12621:
                            copy_dir_to_dir_873_12621()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=12622) as unwtar_874_12622:
                            unwtar_874_12622()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=12623, recursive=True) as chown_875_12623:
                            chown_875_12623()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12624) as should_copy_source_876_12624:
                    should_copy_source_876_12624()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=12625):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=12626) as copy_dir_to_dir_877_12626:
                            copy_dir_to_dir_877_12626()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=12627) as unwtar_878_12627:
                            unwtar_878_12627()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=12628, recursive=True) as chown_879_12628:
                            chown_879_12628()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12629) as should_copy_source_880_12629:
                    should_copy_source_880_12629()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=12630):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=12631) as copy_dir_to_dir_881_12631:
                            copy_dir_to_dir_881_12631()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=12632) as unwtar_882_12632:
                            unwtar_882_12632()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=12633, recursive=True) as chown_883_12633:
                            chown_883_12633()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12634) as should_copy_source_884_12634:
                    should_copy_source_884_12634()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=12635):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=12636) as copy_dir_to_dir_885_12636:
                            copy_dir_to_dir_885_12636()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=12637) as unwtar_886_12637:
                            unwtar_886_12637()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=12638, recursive=True) as chown_887_12638:
                            chown_887_12638()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12639) as should_copy_source_888_12639:
                    should_copy_source_888_12639()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=12640):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=12641) as copy_dir_to_dir_889_12641:
                            copy_dir_to_dir_889_12641()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=12642) as unwtar_890_12642:
                            unwtar_890_12642()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=12643, recursive=True) as chown_891_12643:
                            chown_891_12643()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12644) as should_copy_source_892_12644:
                    should_copy_source_892_12644()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=12645):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=12646) as copy_dir_to_dir_893_12646:
                            copy_dir_to_dir_893_12646()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=12647) as unwtar_894_12647:
                            unwtar_894_12647()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=12648, recursive=True) as chown_895_12648:
                            chown_895_12648()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12649) as should_copy_source_896_12649:
                    should_copy_source_896_12649()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=12650):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=12651) as copy_dir_to_dir_897_12651:
                            copy_dir_to_dir_897_12651()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=12652) as unwtar_898_12652:
                            unwtar_898_12652()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=12653, recursive=True) as chown_899_12653:
                            chown_899_12653()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12654) as should_copy_source_900_12654:
                    should_copy_source_900_12654()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=12655):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=12656) as copy_dir_to_dir_901_12656:
                            copy_dir_to_dir_901_12656()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=12657) as unwtar_902_12657:
                            unwtar_902_12657()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=12658, recursive=True) as chown_903_12658:
                            chown_903_12658()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V15/GTR", skip_progress_count=4, prog_num=12659) as should_copy_source_904_12659:
                    should_copy_source_904_12659()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=12660):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=12661) as copy_dir_to_dir_905_12661:
                            copy_dir_to_dir_905_12661()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=12662) as unwtar_906_12662:
                            unwtar_906_12662()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V15/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=12663, recursive=True) as chown_907_12663:
                            chown_907_12663()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12664) as shell_command_908_12664:
                shell_command_908_12664()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/ReWire", prog_num=12665) as cd_stage_909_12665:
            cd_stage_909_12665()
            with Stage(r"copy", r"backup ReWire to Waves folder", prog_num=12666):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12667) as should_copy_source_910_12667:
                    should_copy_source_910_12667()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=12668):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=12669) as copy_dir_to_dir_911_12669:
                            copy_dir_to_dir_911_12669()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=12670) as unwtar_912_12670:
                            unwtar_912_12670()
                        with Chown(path=r"/Applications/Waves/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=12671, recursive=True) as chown_913_12671:
                            chown_913_12671()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Applications/Waves/ReWire", skip_progress_count=4, prog_num=12672) as should_copy_source_914_12672:
                    should_copy_source_914_12672()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=12673):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=12674) as copy_dir_to_dir_915_12674:
                            copy_dir_to_dir_915_12674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=12675) as unwtar_916_12675:
                            unwtar_916_12675()
                        with Chown(path=r"/Applications/Waves/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=12676, recursive=True) as chown_917_12676:
                            chown_917_12676()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/ReWire" -c', ignore_all_errors=True, prog_num=12677) as shell_command_918_12677:
                shell_command_918_12677()
            with ScriptCommand(r'if [ -f "/Applications/Waves/ReWire"/Icon? ]; then chmod a+rw "/Applications/Waves/ReWire"/Icon?; fi', prog_num=12678) as script_command_919_12678:
                script_command_919_12678()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12679) as shell_command_920_12679:
                shell_command_920_12679()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V15", prog_num=12680) as cd_stage_921_12680:
            cd_stage_921_12680()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12681):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12682) as should_copy_source_922_12682:
                    should_copy_source_922_12682()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12683):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12684) as copy_dir_to_dir_923_12684:
                            copy_dir_to_dir_923_12684()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12685) as unwtar_924_12685:
                            unwtar_924_12685()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12686, recursive=True) as chown_925_12686:
                            chown_925_12686()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12687) as shell_command_926_12687:
                            shell_command_926_12687()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12688):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12689) as should_copy_source_927_12689:
                    should_copy_source_927_12689()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12690):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12691) as copy_dir_to_dir_928_12691:
                            copy_dir_to_dir_928_12691()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12692) as unwtar_929_12692:
                            unwtar_929_12692()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12693, recursive=True) as chown_930_12693:
                            chown_930_12693()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12694) as shell_command_931_12694:
                            shell_command_931_12694()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=12695):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12696) as should_copy_source_932_12696:
                    should_copy_source_932_12696()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=12697):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=12698) as copy_dir_to_dir_933_12698:
                            copy_dir_to_dir_933_12698()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=12699) as unwtar_934_12699:
                            unwtar_934_12699()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12700, recursive=True) as chown_935_12700:
                            chown_935_12700()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=12701) as break_hard_link_936_12701:
                            break_hard_link_936_12701()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=12702) as shell_command_937_12702:
                            shell_command_937_12702()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=12703, recursive=True) as chown_938_12703:
                            chown_938_12703()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=12704, recursive=True) as chmod_939_12704:
                            chmod_939_12704()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=12705):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Applications/Waves/WaveShells V15", skip_progress_count=8, prog_num=12706) as should_copy_source_940_12706:
                    should_copy_source_940_12706()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=12707):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=12708) as copy_dir_to_dir_941_12708:
                            copy_dir_to_dir_941_12708()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=12709) as unwtar_942_12709:
                            unwtar_942_12709()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12710, recursive=True) as chown_943_12710:
                            chown_943_12710()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=12711) as break_hard_link_944_12711:
                            break_hard_link_944_12711()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=12712) as shell_command_945_12712:
                            shell_command_945_12712()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=12713, recursive=True) as chown_946_12713:
                            chown_946_12713()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=12714, recursive=True) as chmod_947_12714:
                            chmod_947_12714()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=12715):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12716) as should_copy_source_948_12716:
                    should_copy_source_948_12716()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=12717):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=12718) as copy_dir_to_dir_949_12718:
                            copy_dir_to_dir_949_12718()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=12719) as unwtar_950_12719:
                            unwtar_950_12719()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=12720, recursive=True) as chown_951_12720:
                            chown_951_12720()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=12721) as shell_command_952_12721:
                            shell_command_952_12721()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=12722):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Applications/Waves/WaveShells V15", skip_progress_count=5, prog_num=12723) as should_copy_source_953_12723:
                    should_copy_source_953_12723()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=12724):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=12725) as copy_dir_to_dir_954_12725:
                            copy_dir_to_dir_954_12725()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=12726) as unwtar_955_12726:
                            unwtar_955_12726()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=12727, recursive=True) as chown_956_12727:
                            chown_956_12727()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=12728) as shell_command_957_12728:
                            shell_command_957_12728()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=12729):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12730) as should_copy_source_958_12730:
                    should_copy_source_958_12730()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=12731):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=12732) as copy_dir_to_dir_959_12732:
                            copy_dir_to_dir_959_12732()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=12733) as unwtar_960_12733:
                            unwtar_960_12733()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=12734, recursive=True) as chown_961_12734:
                            chown_961_12734()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12735) as shell_command_962_12735:
                            shell_command_962_12735()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12736) as script_command_963_12736:
                            script_command_963_12736()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12737) as shell_command_964_12737:
                            shell_command_964_12737()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=12738):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Applications/Waves/WaveShells V15", skip_progress_count=7, prog_num=12739) as should_copy_source_965_12739:
                    should_copy_source_965_12739()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=12740):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=12741) as copy_dir_to_dir_966_12741:
                            copy_dir_to_dir_966_12741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=12742) as unwtar_967_12742:
                            unwtar_967_12742()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=12743, recursive=True) as chown_968_12743:
                            chown_968_12743()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=12744) as shell_command_969_12744:
                            shell_command_969_12744()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=12745) as script_command_970_12745:
                            script_command_970_12745()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=12746) as shell_command_971_12746:
                            shell_command_971_12746()
            with Stage(r"copy", r"WaveShell-AU registration utility v15.5.79.262", prog_num=12747):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r"/Applications/Waves/WaveShells V15", skip_progress_count=4, prog_num=12748) as should_copy_source_972_12748:
                    should_copy_source_972_12748()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 15.app", prog_num=12749):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", r".", delete_extraneous_files=True, prog_num=12750) as copy_dir_to_dir_973_12750:
                            copy_dir_to_dir_973_12750()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/Waves AU Reg Utility 15.app", where_to_unwtar=r".", prog_num=12751) as unwtar_974_12751:
                            unwtar_974_12751()
                        with Chown(path=r"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app", user_id=-1, group_id=-1, prog_num=12752, recursive=True) as chown_975_12752:
                            chown_975_12752()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 15.app"', ignore_all_errors=True, prog_num=12753) as shell_command_976_12753:
                shell_command_976_12753()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=12754) as cd_stage_977_12754:
            cd_stage_977_12754()
            with Stage(r"copy", r"WaveShell1-AAX 15.10 v15.10.46.293", prog_num=12755):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12756) as should_copy_source_978_12756:
                    should_copy_source_978_12756()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", prog_num=12757):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", r".", delete_extraneous_files=True, prog_num=12758) as copy_dir_to_dir_979_12758:
                            copy_dir_to_dir_979_12758()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.10.aaxplugin", where_to_unwtar=r".", prog_num=12759) as unwtar_980_12759:
                            unwtar_980_12759()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.10.aaxplugin", user_id=-1, group_id=-1, prog_num=12760, recursive=True) as chown_981_12760:
                            chown_981_12760()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.10.aaxplugin"', ignore_all_errors=True, prog_num=12761) as shell_command_982_12761:
                            shell_command_982_12761()
            with Stage(r"copy", r"WaveShell1-AAX 15.5 v15.5.139.322", prog_num=12762):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=12763) as should_copy_source_983_12763:
                    should_copy_source_983_12763()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", prog_num=12764):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", r".", delete_extraneous_files=True, prog_num=12765) as copy_dir_to_dir_984_12765:
                            copy_dir_to_dir_984_12765()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AAX 15.5.aaxplugin", where_to_unwtar=r".", prog_num=12766) as unwtar_985_12766:
                            unwtar_985_12766()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 15.5.aaxplugin", user_id=-1, group_id=-1, prog_num=12767, recursive=True) as chown_986_12767:
                            chown_986_12767()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 15.5.aaxplugin"', ignore_all_errors=True, prog_num=12768) as shell_command_987_12768:
                            shell_command_987_12768()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=12769) as cd_stage_988_12769:
            cd_stage_988_12769()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=12770):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12771) as should_copy_source_989_12771:
                    should_copy_source_989_12771()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=12772):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=12773) as copy_file_to_dir_990_12773:
                            copy_file_to_dir_990_12773()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12774) as chmod_and_chown_991_12774:
                            chmod_and_chown_991_12774()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=12775):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12776) as should_copy_source_992_12776:
                    should_copy_source_992_12776()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=12777):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=12778) as copy_file_to_dir_993_12778:
                            copy_file_to_dir_993_12778()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12779) as chmod_and_chown_994_12779:
                            chmod_and_chown_994_12779()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=12780):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12781) as should_copy_source_995_12781:
                    should_copy_source_995_12781()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=12782):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=12783) as copy_file_to_dir_996_12783:
                            copy_file_to_dir_996_12783()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12784) as chmod_and_chown_997_12784:
                            chmod_and_chown_997_12784()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=12785):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12786) as should_copy_source_998_12786:
                    should_copy_source_998_12786()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=12787):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=12788) as copy_file_to_dir_999_12788:
                            copy_file_to_dir_999_12788()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12789) as chmod_and_chown_1000_12789:
                            chmod_and_chown_1000_12789()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=12790):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12791) as should_copy_source_1001_12791:
                    should_copy_source_1001_12791()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=12792):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=12793) as copy_file_to_dir_1002_12793:
                            copy_file_to_dir_1002_12793()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12794) as chmod_and_chown_1003_12794:
                            chmod_and_chown_1003_12794()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=12795):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12796) as should_copy_source_1004_12796:
                    should_copy_source_1004_12796()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=12797):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=12798) as copy_file_to_dir_1005_12798:
                            copy_file_to_dir_1005_12798()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12799) as chmod_and_chown_1006_12799:
                            chmod_and_chown_1006_12799()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=12800):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12801) as should_copy_source_1007_12801:
                    should_copy_source_1007_12801()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=12802):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=12803) as copy_file_to_dir_1008_12803:
                            copy_file_to_dir_1008_12803()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12804) as chmod_and_chown_1009_12804:
                            chmod_and_chown_1009_12804()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=12805):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12806) as should_copy_source_1010_12806:
                    should_copy_source_1010_12806()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=12807):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=12808) as copy_file_to_dir_1011_12808:
                            copy_file_to_dir_1011_12808()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12809) as chmod_and_chown_1012_12809:
                            chmod_and_chown_1012_12809()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=12810):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12811) as should_copy_source_1013_12811:
                    should_copy_source_1013_12811()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=12812):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=12813) as copy_file_to_dir_1014_12813:
                            copy_file_to_dir_1014_12813()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12814) as chmod_and_chown_1015_12814:
                            chmod_and_chown_1015_12814()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=12815):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12816) as should_copy_source_1016_12816:
                    should_copy_source_1016_12816()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=12817):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=12818) as copy_file_to_dir_1017_12818:
                            copy_file_to_dir_1017_12818()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12819) as chmod_and_chown_1018_12819:
                            chmod_and_chown_1018_12819()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=12820):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12821) as should_copy_source_1019_12821:
                    should_copy_source_1019_12821()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=12822):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=12823) as copy_file_to_dir_1020_12823:
                            copy_file_to_dir_1020_12823()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12824) as chmod_and_chown_1021_12824:
                            chmod_and_chown_1021_12824()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=12825):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12826) as should_copy_source_1022_12826:
                    should_copy_source_1022_12826()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=12827):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=12828) as copy_file_to_dir_1023_12828:
                            copy_file_to_dir_1023_12828()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12829) as chmod_and_chown_1024_12829:
                            chmod_and_chown_1024_12829()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=12830):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12831) as should_copy_source_1025_12831:
                    should_copy_source_1025_12831()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=12832):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=12833) as copy_file_to_dir_1026_12833:
                            copy_file_to_dir_1026_12833()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12834) as chmod_and_chown_1027_12834:
                            chmod_and_chown_1027_12834()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=12835):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12836) as should_copy_source_1028_12836:
                    should_copy_source_1028_12836()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=12837):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=12838) as copy_file_to_dir_1029_12838:
                            copy_file_to_dir_1029_12838()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12839) as chmod_and_chown_1030_12839:
                            chmod_and_chown_1030_12839()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=12840):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12841) as should_copy_source_1031_12841:
                    should_copy_source_1031_12841()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=12842):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=12843) as copy_file_to_dir_1032_12843:
                            copy_file_to_dir_1032_12843()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12844) as chmod_and_chown_1033_12844:
                            chmod_and_chown_1033_12844()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=12845):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12846) as should_copy_source_1034_12846:
                    should_copy_source_1034_12846()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=12847):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=12848) as copy_file_to_dir_1035_12848:
                            copy_file_to_dir_1035_12848()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12849) as chmod_and_chown_1036_12849:
                            chmod_and_chown_1036_12849()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=12850):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12851) as should_copy_source_1037_12851:
                    should_copy_source_1037_12851()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=12852):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=12853) as copy_file_to_dir_1038_12853:
                            copy_file_to_dir_1038_12853()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12854) as chmod_and_chown_1039_12854:
                            chmod_and_chown_1039_12854()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=12855):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12856) as should_copy_source_1040_12856:
                    should_copy_source_1040_12856()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=12857):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=12858) as copy_file_to_dir_1041_12858:
                            copy_file_to_dir_1041_12858()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12859) as chmod_and_chown_1042_12859:
                            chmod_and_chown_1042_12859()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=12860):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12861) as should_copy_source_1043_12861:
                    should_copy_source_1043_12861()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=12862):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=12863) as copy_file_to_dir_1044_12863:
                            copy_file_to_dir_1044_12863()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12864) as chmod_and_chown_1045_12864:
                            chmod_and_chown_1045_12864()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=12865):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12866) as should_copy_source_1046_12866:
                    should_copy_source_1046_12866()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=12867):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=12868) as copy_file_to_dir_1047_12868:
                            copy_file_to_dir_1047_12868()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12869) as chmod_and_chown_1048_12869:
                            chmod_and_chown_1048_12869()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=12870):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12871) as should_copy_source_1049_12871:
                    should_copy_source_1049_12871()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=12872):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=12873) as copy_file_to_dir_1050_12873:
                            copy_file_to_dir_1050_12873()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12874) as chmod_and_chown_1051_12874:
                            chmod_and_chown_1051_12874()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=12875):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12876) as should_copy_source_1052_12876:
                    should_copy_source_1052_12876()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=12877):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=12878) as copy_file_to_dir_1053_12878:
                            copy_file_to_dir_1053_12878()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12879) as chmod_and_chown_1054_12879:
                            chmod_and_chown_1054_12879()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=12880):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12881) as should_copy_source_1055_12881:
                    should_copy_source_1055_12881()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=12882):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=12883) as copy_file_to_dir_1056_12883:
                            copy_file_to_dir_1056_12883()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12884) as chmod_and_chown_1057_12884:
                            chmod_and_chown_1057_12884()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=12885):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12886) as should_copy_source_1058_12886:
                    should_copy_source_1058_12886()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=12887):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=12888) as copy_file_to_dir_1059_12888:
                            copy_file_to_dir_1059_12888()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12889) as chmod_and_chown_1060_12889:
                            chmod_and_chown_1060_12889()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=12890):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12891) as should_copy_source_1061_12891:
                    should_copy_source_1061_12891()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=12892):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=12893) as copy_file_to_dir_1062_12893:
                            copy_file_to_dir_1062_12893()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12894) as chmod_and_chown_1063_12894:
                            chmod_and_chown_1063_12894()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=12895):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12896) as should_copy_source_1064_12896:
                    should_copy_source_1064_12896()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=12897):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=12898) as copy_file_to_dir_1065_12898:
                            copy_file_to_dir_1065_12898()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12899) as chmod_and_chown_1066_12899:
                            chmod_and_chown_1066_12899()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=12900):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12901) as should_copy_source_1067_12901:
                    should_copy_source_1067_12901()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=12902):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=12903) as copy_file_to_dir_1068_12903:
                            copy_file_to_dir_1068_12903()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12904) as chmod_and_chown_1069_12904:
                            chmod_and_chown_1069_12904()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=12905):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12906) as should_copy_source_1070_12906:
                    should_copy_source_1070_12906()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=12907):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=12908) as copy_file_to_dir_1071_12908:
                            copy_file_to_dir_1071_12908()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12909) as chmod_and_chown_1072_12909:
                            chmod_and_chown_1072_12909()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=12910):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12911) as should_copy_source_1073_12911:
                    should_copy_source_1073_12911()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=12912):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=12913) as copy_file_to_dir_1074_12913:
                            copy_file_to_dir_1074_12913()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12914) as chmod_and_chown_1075_12914:
                            chmod_and_chown_1075_12914()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=12915):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12916) as should_copy_source_1076_12916:
                    should_copy_source_1076_12916()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=12917):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=12918) as copy_file_to_dir_1077_12918:
                            copy_file_to_dir_1077_12918()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12919) as chmod_and_chown_1078_12919:
                            chmod_and_chown_1078_12919()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=12920):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12921) as should_copy_source_1079_12921:
                    should_copy_source_1079_12921()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=12922):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=12923) as copy_file_to_dir_1080_12923:
                            copy_file_to_dir_1080_12923()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12924) as chmod_and_chown_1081_12924:
                            chmod_and_chown_1081_12924()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=12925):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12926) as should_copy_source_1082_12926:
                    should_copy_source_1082_12926()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=12927):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=12928) as copy_file_to_dir_1083_12928:
                            copy_file_to_dir_1083_12928()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12929) as chmod_and_chown_1084_12929:
                            chmod_and_chown_1084_12929()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=12930):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12931) as should_copy_source_1085_12931:
                    should_copy_source_1085_12931()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=12932):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=12933) as copy_file_to_dir_1086_12933:
                            copy_file_to_dir_1086_12933()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12934) as chmod_and_chown_1087_12934:
                            chmod_and_chown_1087_12934()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=12935):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12936) as should_copy_source_1088_12936:
                    should_copy_source_1088_12936()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=12937):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=12938) as copy_file_to_dir_1089_12938:
                            copy_file_to_dir_1089_12938()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12939) as chmod_and_chown_1090_12939:
                            chmod_and_chown_1090_12939()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=12940):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12941) as should_copy_source_1091_12941:
                    should_copy_source_1091_12941()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=12942):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=12943) as copy_file_to_dir_1092_12943:
                            copy_file_to_dir_1092_12943()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12944) as chmod_and_chown_1093_12944:
                            chmod_and_chown_1093_12944()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=12945):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12946) as should_copy_source_1094_12946:
                    should_copy_source_1094_12946()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=12947):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=12948) as copy_file_to_dir_1095_12948:
                            copy_file_to_dir_1095_12948()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12949) as chmod_and_chown_1096_12949:
                            chmod_and_chown_1096_12949()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=12950):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12951) as should_copy_source_1097_12951:
                    should_copy_source_1097_12951()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=12952):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=12953) as copy_file_to_dir_1098_12953:
                            copy_file_to_dir_1098_12953()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12954) as chmod_and_chown_1099_12954:
                            chmod_and_chown_1099_12954()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=12955):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12956) as should_copy_source_1100_12956:
                    should_copy_source_1100_12956()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=12957):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=12958) as copy_file_to_dir_1101_12958:
                            copy_file_to_dir_1101_12958()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12959) as chmod_and_chown_1102_12959:
                            chmod_and_chown_1102_12959()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=12960):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12961) as should_copy_source_1103_12961:
                    should_copy_source_1103_12961()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=12962):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=12963) as copy_file_to_dir_1104_12963:
                            copy_file_to_dir_1104_12963()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12964) as chmod_and_chown_1105_12964:
                            chmod_and_chown_1105_12964()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=12965):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12966) as should_copy_source_1106_12966:
                    should_copy_source_1106_12966()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=12967):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=12968) as copy_file_to_dir_1107_12968:
                            copy_file_to_dir_1107_12968()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12969) as chmod_and_chown_1108_12969:
                            chmod_and_chown_1108_12969()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=12970):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12971) as should_copy_source_1109_12971:
                    should_copy_source_1109_12971()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=12972):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=12973) as copy_file_to_dir_1110_12973:
                            copy_file_to_dir_1110_12973()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12974) as chmod_and_chown_1111_12974:
                            chmod_and_chown_1111_12974()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=12975):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12976) as should_copy_source_1112_12976:
                    should_copy_source_1112_12976()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=12977):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=12978) as copy_file_to_dir_1113_12978:
                            copy_file_to_dir_1113_12978()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12979) as chmod_and_chown_1114_12979:
                            chmod_and_chown_1114_12979()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=12980):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12981) as should_copy_source_1115_12981:
                    should_copy_source_1115_12981()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=12982):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=12983) as copy_file_to_dir_1116_12983:
                            copy_file_to_dir_1116_12983()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12984) as chmod_and_chown_1117_12984:
                            chmod_and_chown_1117_12984()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=12985):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12986) as should_copy_source_1118_12986:
                    should_copy_source_1118_12986()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=12987):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=12988) as copy_file_to_dir_1119_12988:
                            copy_file_to_dir_1119_12988()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12989) as chmod_and_chown_1120_12989:
                            chmod_and_chown_1120_12989()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=12990):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12991) as should_copy_source_1121_12991:
                    should_copy_source_1121_12991()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=12992):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=12993) as copy_file_to_dir_1122_12993:
                            copy_file_to_dir_1122_12993()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12994) as chmod_and_chown_1123_12994:
                            chmod_and_chown_1123_12994()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=12995):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=12996) as should_copy_source_1124_12996:
                    should_copy_source_1124_12996()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=12997):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=12998) as copy_file_to_dir_1125_12998:
                            copy_file_to_dir_1125_12998()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=12999) as chmod_and_chown_1126_12999:
                            chmod_and_chown_1126_12999()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=13000):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13001) as should_copy_source_1127_13001:
                    should_copy_source_1127_13001()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=13002):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=13003) as copy_file_to_dir_1128_13003:
                            copy_file_to_dir_1128_13003()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13004) as chmod_and_chown_1129_13004:
                            chmod_and_chown_1129_13004()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=13005):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13006) as should_copy_source_1130_13006:
                    should_copy_source_1130_13006()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=13007):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=13008) as copy_file_to_dir_1131_13008:
                            copy_file_to_dir_1131_13008()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13009) as chmod_and_chown_1132_13009:
                            chmod_and_chown_1132_13009()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13010) as should_copy_source_1133_13010:
                    should_copy_source_1133_13010()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=13011):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=13012) as copy_file_to_dir_1134_13012:
                            copy_file_to_dir_1134_13012()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13013) as chmod_and_chown_1135_13013:
                            chmod_and_chown_1135_13013()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=13014):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13015) as should_copy_source_1136_13015:
                    should_copy_source_1136_13015()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=13016):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=13017) as copy_file_to_dir_1137_13017:
                            copy_file_to_dir_1137_13017()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13018) as chmod_and_chown_1138_13018:
                            chmod_and_chown_1138_13018()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=13019):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13020) as should_copy_source_1139_13020:
                    should_copy_source_1139_13020()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=13021):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=13022) as copy_file_to_dir_1140_13022:
                            copy_file_to_dir_1140_13022()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13023) as chmod_and_chown_1141_13023:
                            chmod_and_chown_1141_13023()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=13024):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13025) as should_copy_source_1142_13025:
                    should_copy_source_1142_13025()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=13026):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=13027) as copy_file_to_dir_1143_13027:
                            copy_file_to_dir_1143_13027()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13028) as chmod_and_chown_1144_13028:
                            chmod_and_chown_1144_13028()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=13029):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13030) as should_copy_source_1145_13030:
                    should_copy_source_1145_13030()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=13031):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=13032) as copy_file_to_dir_1146_13032:
                            copy_file_to_dir_1146_13032()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13033) as chmod_and_chown_1147_13033:
                            chmod_and_chown_1147_13033()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=13034):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13035) as should_copy_source_1148_13035:
                    should_copy_source_1148_13035()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=13036):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=13037) as copy_file_to_dir_1149_13037:
                            copy_file_to_dir_1149_13037()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13038) as chmod_and_chown_1150_13038:
                            chmod_and_chown_1150_13038()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=13039):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13040) as should_copy_source_1151_13040:
                    should_copy_source_1151_13040()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=13041):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=13042) as copy_file_to_dir_1152_13042:
                            copy_file_to_dir_1152_13042()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13043) as chmod_and_chown_1153_13043:
                            chmod_and_chown_1153_13043()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=13044):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13045) as should_copy_source_1154_13045:
                    should_copy_source_1154_13045()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=13046):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=13047) as copy_file_to_dir_1155_13047:
                            copy_file_to_dir_1155_13047()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13048) as chmod_and_chown_1156_13048:
                            chmod_and_chown_1156_13048()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=13049):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13050) as should_copy_source_1157_13050:
                    should_copy_source_1157_13050()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=13051):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=13052) as copy_file_to_dir_1158_13052:
                            copy_file_to_dir_1158_13052()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13053) as chmod_and_chown_1159_13053:
                            chmod_and_chown_1159_13053()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=13054):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13055) as should_copy_source_1160_13055:
                    should_copy_source_1160_13055()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=13056):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=13057) as copy_file_to_dir_1161_13057:
                            copy_file_to_dir_1161_13057()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13058) as chmod_and_chown_1162_13058:
                            chmod_and_chown_1162_13058()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=13059):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13060) as should_copy_source_1163_13060:
                    should_copy_source_1163_13060()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=13061):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=13062) as copy_file_to_dir_1164_13062:
                            copy_file_to_dir_1164_13062()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13063) as chmod_and_chown_1165_13063:
                            chmod_and_chown_1165_13063()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=13064):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13065) as should_copy_source_1166_13065:
                    should_copy_source_1166_13065()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=13066):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=13067) as copy_file_to_dir_1167_13067:
                            copy_file_to_dir_1167_13067()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13068) as chmod_and_chown_1168_13068:
                            chmod_and_chown_1168_13068()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=13069):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13070) as should_copy_source_1169_13070:
                    should_copy_source_1169_13070()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=13071):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=13072) as copy_file_to_dir_1170_13072:
                            copy_file_to_dir_1170_13072()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13073) as chmod_and_chown_1171_13073:
                            chmod_and_chown_1171_13073()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=13074):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13075) as should_copy_source_1172_13075:
                    should_copy_source_1172_13075()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=13076):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=13077) as copy_file_to_dir_1173_13077:
                            copy_file_to_dir_1173_13077()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13078) as chmod_and_chown_1174_13078:
                            chmod_and_chown_1174_13078()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=13079):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13080) as should_copy_source_1175_13080:
                    should_copy_source_1175_13080()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=13081):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=13082) as copy_file_to_dir_1176_13082:
                            copy_file_to_dir_1176_13082()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13083) as chmod_and_chown_1177_13083:
                            chmod_and_chown_1177_13083()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=13084):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13085) as should_copy_source_1178_13085:
                    should_copy_source_1178_13085()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=13086):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=13087) as copy_file_to_dir_1179_13087:
                            copy_file_to_dir_1179_13087()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13088) as chmod_and_chown_1180_13088:
                            chmod_and_chown_1180_13088()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=13089):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13090) as should_copy_source_1181_13090:
                    should_copy_source_1181_13090()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=13091):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=13092) as copy_file_to_dir_1182_13092:
                            copy_file_to_dir_1182_13092()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13093) as chmod_and_chown_1183_13093:
                            chmod_and_chown_1183_13093()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=13094):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13095) as should_copy_source_1184_13095:
                    should_copy_source_1184_13095()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=13096):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=13097) as copy_file_to_dir_1185_13097:
                            copy_file_to_dir_1185_13097()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13098) as chmod_and_chown_1186_13098:
                            chmod_and_chown_1186_13098()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=13099):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13100) as should_copy_source_1187_13100:
                    should_copy_source_1187_13100()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=13101):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=13102) as copy_file_to_dir_1188_13102:
                            copy_file_to_dir_1188_13102()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13103) as chmod_and_chown_1189_13103:
                            chmod_and_chown_1189_13103()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=13104):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13105) as should_copy_source_1190_13105:
                    should_copy_source_1190_13105()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=13106):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=13107) as copy_file_to_dir_1191_13107:
                            copy_file_to_dir_1191_13107()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13108) as chmod_and_chown_1192_13108:
                            chmod_and_chown_1192_13108()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=13109):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13110) as should_copy_source_1193_13110:
                    should_copy_source_1193_13110()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=13111):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=13112) as copy_file_to_dir_1194_13112:
                            copy_file_to_dir_1194_13112()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13113) as chmod_and_chown_1195_13113:
                            chmod_and_chown_1195_13113()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=13114):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13115) as should_copy_source_1196_13115:
                    should_copy_source_1196_13115()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=13116):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=13117) as copy_file_to_dir_1197_13117:
                            copy_file_to_dir_1197_13117()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13118) as chmod_and_chown_1198_13118:
                            chmod_and_chown_1198_13118()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=13119):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13120) as should_copy_source_1199_13120:
                    should_copy_source_1199_13120()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=13121):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=13122) as copy_file_to_dir_1200_13122:
                            copy_file_to_dir_1200_13122()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13123) as chmod_and_chown_1201_13123:
                            chmod_and_chown_1201_13123()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=13124):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13125) as should_copy_source_1202_13125:
                    should_copy_source_1202_13125()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=13126):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=13127) as copy_file_to_dir_1203_13127:
                            copy_file_to_dir_1203_13127()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13128) as chmod_and_chown_1204_13128:
                            chmod_and_chown_1204_13128()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=13129):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13130) as should_copy_source_1205_13130:
                    should_copy_source_1205_13130()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=13131):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=13132) as copy_file_to_dir_1206_13132:
                            copy_file_to_dir_1206_13132()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13133) as chmod_and_chown_1207_13133:
                            chmod_and_chown_1207_13133()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=13134):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13135) as should_copy_source_1208_13135:
                    should_copy_source_1208_13135()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=13136):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=13137) as copy_file_to_dir_1209_13137:
                            copy_file_to_dir_1209_13137()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13138) as chmod_and_chown_1210_13138:
                            chmod_and_chown_1210_13138()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=13139):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13140) as should_copy_source_1211_13140:
                    should_copy_source_1211_13140()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=13141):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=13142) as copy_file_to_dir_1212_13142:
                            copy_file_to_dir_1212_13142()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13143) as chmod_and_chown_1213_13143:
                            chmod_and_chown_1213_13143()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=13144):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13145) as should_copy_source_1214_13145:
                    should_copy_source_1214_13145()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=13146):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=13147) as copy_file_to_dir_1215_13147:
                            copy_file_to_dir_1215_13147()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13148) as chmod_and_chown_1216_13148:
                            chmod_and_chown_1216_13148()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=13149):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13150) as should_copy_source_1217_13150:
                    should_copy_source_1217_13150()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=13151):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=13152) as copy_file_to_dir_1218_13152:
                            copy_file_to_dir_1218_13152()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13153) as chmod_and_chown_1219_13153:
                            chmod_and_chown_1219_13153()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13154) as should_copy_source_1220_13154:
                    should_copy_source_1220_13154()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=13155):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=13156) as copy_file_to_dir_1221_13156:
                            copy_file_to_dir_1221_13156()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13157) as chmod_and_chown_1222_13157:
                            chmod_and_chown_1222_13157()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13158) as should_copy_source_1223_13158:
                    should_copy_source_1223_13158()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=13159):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=13160) as copy_file_to_dir_1224_13160:
                            copy_file_to_dir_1224_13160()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13161) as chmod_and_chown_1225_13161:
                            chmod_and_chown_1225_13161()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=13162):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13163) as should_copy_source_1226_13163:
                    should_copy_source_1226_13163()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=13164):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=13165) as copy_file_to_dir_1227_13165:
                            copy_file_to_dir_1227_13165()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13166) as chmod_and_chown_1228_13166:
                            chmod_and_chown_1228_13166()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=13167):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13168) as should_copy_source_1229_13168:
                    should_copy_source_1229_13168()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=13169):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=13170) as copy_file_to_dir_1230_13170:
                            copy_file_to_dir_1230_13170()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13171) as chmod_and_chown_1231_13171:
                            chmod_and_chown_1231_13171()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=13172):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13173) as should_copy_source_1232_13173:
                    should_copy_source_1232_13173()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=13174):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=13175) as copy_file_to_dir_1233_13175:
                            copy_file_to_dir_1233_13175()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13176) as chmod_and_chown_1234_13176:
                            chmod_and_chown_1234_13176()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=13177):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13178) as should_copy_source_1235_13178:
                    should_copy_source_1235_13178()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=13179):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=13180) as copy_file_to_dir_1236_13180:
                            copy_file_to_dir_1236_13180()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13181) as chmod_and_chown_1237_13181:
                            chmod_and_chown_1237_13181()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=13182):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13183) as should_copy_source_1238_13183:
                    should_copy_source_1238_13183()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=13184):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=13185) as copy_file_to_dir_1239_13185:
                            copy_file_to_dir_1239_13185()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13186) as chmod_and_chown_1240_13186:
                            chmod_and_chown_1240_13186()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=13187):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13188) as should_copy_source_1241_13188:
                    should_copy_source_1241_13188()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=13189):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=13190) as copy_file_to_dir_1242_13190:
                            copy_file_to_dir_1242_13190()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13191) as chmod_and_chown_1243_13191:
                            chmod_and_chown_1243_13191()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=13192):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13193) as should_copy_source_1244_13193:
                    should_copy_source_1244_13193()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=13194):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=13195) as copy_file_to_dir_1245_13195:
                            copy_file_to_dir_1245_13195()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13196) as chmod_and_chown_1246_13196:
                            chmod_and_chown_1246_13196()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=13197):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=13198) as should_copy_source_1247_13198:
                    should_copy_source_1247_13198()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=13199):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=13200) as copy_file_to_dir_1248_13200:
                            copy_file_to_dir_1248_13200()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=13201) as chmod_and_chown_1249_13201:
                            chmod_and_chown_1249_13201()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=13202) as resolve_config_vars_in_file_1250_13202:
                resolve_config_vars_in_file_1250_13202()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=13203) as if_1251_13203:
                if_1251_13203()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=13204) as resolve_config_vars_in_file_1252_13204:
                resolve_config_vars_in_file_1252_13204()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=13205) as if_1253_13205:
                if_1253_13205()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=13206) as resolve_config_vars_in_file_1254_13206:
                resolve_config_vars_in_file_1254_13206()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=13207) as if_1255_13207:
                if_1255_13207()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=13208) as resolve_config_vars_in_file_1256_13208:
                resolve_config_vars_in_file_1256_13208()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=13209) as if_1257_13209:
                if_1257_13209()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=13210) as resolve_config_vars_in_file_1258_13210:
                resolve_config_vars_in_file_1258_13210()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=13211) as if_1259_13211:
                if_1259_13211()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13212) as resolve_config_vars_in_file_1260_13212:
                resolve_config_vars_in_file_1260_13212()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=13213) as if_1261_13213:
                if_1261_13213()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=13214) as resolve_config_vars_in_file_1262_13214:
                resolve_config_vars_in_file_1262_13214()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=13215) as if_1263_13215:
                if_1263_13215()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=13216) as resolve_config_vars_in_file_1264_13216:
                resolve_config_vars_in_file_1264_13216()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=13217) as if_1265_13217:
                if_1265_13217()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=13218) as resolve_config_vars_in_file_1266_13218:
                resolve_config_vars_in_file_1266_13218()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=13219) as if_1267_13219:
                if_1267_13219()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=13220) as resolve_config_vars_in_file_1268_13220:
                resolve_config_vars_in_file_1268_13220()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=13221) as if_1269_13221:
                if_1269_13221()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=13222) as resolve_config_vars_in_file_1270_13222:
                resolve_config_vars_in_file_1270_13222()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=13223) as if_1271_13223:
                if_1271_13223()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=13224) as resolve_config_vars_in_file_1272_13224:
                resolve_config_vars_in_file_1272_13224()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=13225) as if_1273_13225:
                if_1273_13225()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=13226) as resolve_config_vars_in_file_1274_13226:
                resolve_config_vars_in_file_1274_13226()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=13227) as if_1275_13227:
                if_1275_13227()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=13228) as resolve_config_vars_in_file_1276_13228:
                resolve_config_vars_in_file_1276_13228()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=13229) as if_1277_13229:
                if_1277_13229()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=13230) as resolve_config_vars_in_file_1278_13230:
                resolve_config_vars_in_file_1278_13230()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=13231) as if_1279_13231:
                if_1279_13231()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=13232) as resolve_config_vars_in_file_1280_13232:
                resolve_config_vars_in_file_1280_13232()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=13233) as if_1281_13233:
                if_1281_13233()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13234) as resolve_config_vars_in_file_1282_13234:
                resolve_config_vars_in_file_1282_13234()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=13235) as if_1283_13235:
                if_1283_13235()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13236) as resolve_config_vars_in_file_1284_13236:
                resolve_config_vars_in_file_1284_13236()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=13237) as if_1285_13237:
                if_1285_13237()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=13238) as resolve_config_vars_in_file_1286_13238:
                resolve_config_vars_in_file_1286_13238()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=13239) as if_1287_13239:
                if_1287_13239()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=13240) as resolve_config_vars_in_file_1288_13240:
                resolve_config_vars_in_file_1288_13240()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=13241) as if_1289_13241:
                if_1289_13241()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=13242) as resolve_config_vars_in_file_1290_13242:
                resolve_config_vars_in_file_1290_13242()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=13243) as if_1291_13243:
                if_1291_13243()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=13244) as resolve_config_vars_in_file_1292_13244:
                resolve_config_vars_in_file_1292_13244()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=13245) as if_1293_13245:
                if_1293_13245()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=13246) as resolve_config_vars_in_file_1294_13246:
                resolve_config_vars_in_file_1294_13246()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=13247) as if_1295_13247:
                if_1295_13247()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=13248) as resolve_config_vars_in_file_1296_13248:
                resolve_config_vars_in_file_1296_13248()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=13249) as if_1297_13249:
                if_1297_13249()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=13250) as rm_file_or_dir_1298_13250:
                rm_file_or_dir_1298_13250()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=13251) as resolve_config_vars_in_file_1299_13251:
                resolve_config_vars_in_file_1299_13251()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=13252) as if_1300_13252:
                if_1300_13252()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=13253) as rm_file_or_dir_1301_13253:
                rm_file_or_dir_1301_13253()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=13254) as resolve_config_vars_in_file_1302_13254:
                resolve_config_vars_in_file_1302_13254()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=13255) as if_1303_13255:
                if_1303_13255()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=13256) as resolve_config_vars_in_file_1304_13256:
                resolve_config_vars_in_file_1304_13256()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=13257) as if_1305_13257:
                if_1305_13257()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=13258) as resolve_config_vars_in_file_1306_13258:
                resolve_config_vars_in_file_1306_13258()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=13259) as if_1307_13259:
                if_1307_13259()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=13260) as resolve_config_vars_in_file_1308_13260:
                resolve_config_vars_in_file_1308_13260()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=13261) as if_1309_13261:
                if_1309_13261()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=13262) as resolve_config_vars_in_file_1310_13262:
                resolve_config_vars_in_file_1310_13262()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=13263) as if_1311_13263:
                if_1311_13263()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=13264) as resolve_config_vars_in_file_1312_13264:
                resolve_config_vars_in_file_1312_13264()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=13265) as if_1313_13265:
                if_1313_13265()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13266) as resolve_config_vars_in_file_1314_13266:
                resolve_config_vars_in_file_1314_13266()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=13267) as if_1315_13267:
                if_1315_13267()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13268) as resolve_config_vars_in_file_1316_13268:
                resolve_config_vars_in_file_1316_13268()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=13269) as if_1317_13269:
                if_1317_13269()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=13270) as resolve_config_vars_in_file_1318_13270:
                resolve_config_vars_in_file_1318_13270()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=13271) as if_1319_13271:
                if_1319_13271()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=13272) as resolve_config_vars_in_file_1320_13272:
                resolve_config_vars_in_file_1320_13272()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=13273) as if_1321_13273:
                if_1321_13273()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=13274) as resolve_config_vars_in_file_1322_13274:
                resolve_config_vars_in_file_1322_13274()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=13275) as if_1323_13275:
                if_1323_13275()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13276) as resolve_config_vars_in_file_1324_13276:
                resolve_config_vars_in_file_1324_13276()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=13277) as if_1325_13277:
                if_1325_13277()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=13278) as resolve_config_vars_in_file_1326_13278:
                resolve_config_vars_in_file_1326_13278()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=13279) as if_1327_13279:
                if_1327_13279()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=13280) as resolve_config_vars_in_file_1328_13280:
                resolve_config_vars_in_file_1328_13280()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=13281) as if_1329_13281:
                if_1329_13281()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=13282) as resolve_config_vars_in_file_1330_13282:
                resolve_config_vars_in_file_1330_13282()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=13283) as if_1331_13283:
                if_1331_13283()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=13284) as resolve_config_vars_in_file_1332_13284:
                resolve_config_vars_in_file_1332_13284()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=13285) as if_1333_13285:
                if_1333_13285()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=13286) as resolve_config_vars_in_file_1334_13286:
                resolve_config_vars_in_file_1334_13286()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=13287) as if_1335_13287:
                if_1335_13287()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=13288) as resolve_config_vars_in_file_1336_13288:
                resolve_config_vars_in_file_1336_13288()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=13289) as if_1337_13289:
                if_1337_13289()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=13290) as resolve_config_vars_in_file_1338_13290:
                resolve_config_vars_in_file_1338_13290()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=13291) as if_1339_13291:
                if_1339_13291()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=13292) as resolve_config_vars_in_file_1340_13292:
                resolve_config_vars_in_file_1340_13292()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=13293) as if_1341_13293:
                if_1341_13293()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=13294) as resolve_config_vars_in_file_1342_13294:
                resolve_config_vars_in_file_1342_13294()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=13295) as if_1343_13295:
                if_1343_13295()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=13296) as resolve_config_vars_in_file_1344_13296:
                resolve_config_vars_in_file_1344_13296()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=13297) as if_1345_13297:
                if_1345_13297()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=13298) as resolve_config_vars_in_file_1346_13298:
                resolve_config_vars_in_file_1346_13298()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=13299) as if_1347_13299:
                if_1347_13299()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=13300) as move_file_to_file_1348_13300:
                move_file_to_file_1348_13300()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=13301) as resolve_config_vars_in_file_1349_13301:
                resolve_config_vars_in_file_1349_13301()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=13302) as if_1350_13302:
                if_1350_13302()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=13303) as resolve_config_vars_in_file_1351_13303:
                resolve_config_vars_in_file_1351_13303()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=13304) as if_1352_13304:
                if_1352_13304()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=13305) as resolve_config_vars_in_file_1353_13305:
                resolve_config_vars_in_file_1353_13305()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=13306) as if_1354_13306:
                if_1354_13306()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=13307) as resolve_config_vars_in_file_1355_13307:
                resolve_config_vars_in_file_1355_13307()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=13308) as if_1356_13308:
                if_1356_13308()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=13309) as resolve_config_vars_in_file_1357_13309:
                resolve_config_vars_in_file_1357_13309()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=13310) as if_1358_13310:
                if_1358_13310()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=13311) as resolve_config_vars_in_file_1359_13311:
                resolve_config_vars_in_file_1359_13311()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=13312) as if_1360_13312:
                if_1360_13312()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=13313) as resolve_config_vars_in_file_1361_13313:
                resolve_config_vars_in_file_1361_13313()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=13314) as if_1362_13314:
                if_1362_13314()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=13315) as resolve_config_vars_in_file_1363_13315:
                resolve_config_vars_in_file_1363_13315()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=13316) as if_1364_13316:
                if_1364_13316()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=13317) as resolve_config_vars_in_file_1365_13317:
                resolve_config_vars_in_file_1365_13317()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=13318) as if_1366_13318:
                if_1366_13318()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=13319) as resolve_config_vars_in_file_1367_13319:
                resolve_config_vars_in_file_1367_13319()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=13320) as if_1368_13320:
                if_1368_13320()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=13321) as resolve_config_vars_in_file_1369_13321:
                resolve_config_vars_in_file_1369_13321()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=13322) as if_1370_13322:
                if_1370_13322()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=13323) as resolve_config_vars_in_file_1371_13323:
                resolve_config_vars_in_file_1371_13323()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=13324) as if_1372_13324:
                if_1372_13324()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13325) as resolve_config_vars_in_file_1373_13325:
                resolve_config_vars_in_file_1373_13325()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=13326) as if_1374_13326:
                if_1374_13326()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=13327) as resolve_config_vars_in_file_1375_13327:
                resolve_config_vars_in_file_1375_13327()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=13328) as if_1376_13328:
                if_1376_13328()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=13329) as resolve_config_vars_in_file_1377_13329:
                resolve_config_vars_in_file_1377_13329()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=13330) as if_1378_13330:
                if_1378_13330()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=13331) as resolve_config_vars_in_file_1379_13331:
                resolve_config_vars_in_file_1379_13331()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=13332) as if_1380_13332:
                if_1380_13332()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=13333) as resolve_config_vars_in_file_1381_13333:
                resolve_config_vars_in_file_1381_13333()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=13334) as if_1382_13334:
                if_1382_13334()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=13335) as resolve_config_vars_in_file_1383_13335:
                resolve_config_vars_in_file_1383_13335()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=13336) as if_1384_13336:
                if_1384_13336()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=13337) as resolve_config_vars_in_file_1385_13337:
                resolve_config_vars_in_file_1385_13337()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=13338) as if_1386_13338:
                if_1386_13338()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=13339) as resolve_config_vars_in_file_1387_13339:
                resolve_config_vars_in_file_1387_13339()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=13340) as if_1388_13340:
                if_1388_13340()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=13341) as resolve_config_vars_in_file_1389_13341:
                resolve_config_vars_in_file_1389_13341()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=13342) as if_1390_13342:
                if_1390_13342()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=13343) as resolve_config_vars_in_file_1391_13343:
                resolve_config_vars_in_file_1391_13343()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=13344) as if_1392_13344:
                if_1392_13344()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13345) as resolve_config_vars_in_file_1393_13345:
                resolve_config_vars_in_file_1393_13345()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=13346) as if_1394_13346:
                if_1394_13346()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=13347) as resolve_config_vars_in_file_1395_13347:
                resolve_config_vars_in_file_1395_13347()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=13348) as if_1396_13348:
                if_1396_13348()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=13349) as resolve_config_vars_in_file_1397_13349:
                resolve_config_vars_in_file_1397_13349()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=13350) as if_1398_13350:
                if_1398_13350()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=13351) as resolve_config_vars_in_file_1399_13351:
                resolve_config_vars_in_file_1399_13351()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=13352) as if_1400_13352:
                if_1400_13352()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=13353) as resolve_config_vars_in_file_1401_13353:
                resolve_config_vars_in_file_1401_13353()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=13354) as if_1402_13354:
                if_1402_13354()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=13355) as resolve_config_vars_in_file_1403_13355:
                resolve_config_vars_in_file_1403_13355()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=13356) as if_1404_13356:
                if_1404_13356()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=13357) as rm_file_or_dir_1405_13357:
                rm_file_or_dir_1405_13357()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=13358) as rm_file_or_dir_1406_13358:
                rm_file_or_dir_1406_13358()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=13359) as rm_file_or_dir_1407_13359:
                rm_file_or_dir_1407_13359()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13360) as resolve_config_vars_in_file_1408_13360:
                resolve_config_vars_in_file_1408_13360()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=13361) as if_1409_13361:
                if_1409_13361()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=13362) as resolve_config_vars_in_file_1410_13362:
                resolve_config_vars_in_file_1410_13362()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=13363) as if_1411_13363:
                if_1411_13363()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=13364) as resolve_config_vars_in_file_1412_13364:
                resolve_config_vars_in_file_1412_13364()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=13365) as if_1413_13365:
                if_1413_13365()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=13366) as rm_file_or_dir_1414_13366:
                rm_file_or_dir_1414_13366()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=13367) as rm_file_or_dir_1415_13367:
                rm_file_or_dir_1415_13367()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=13368) as rm_file_or_dir_1416_13368:
                rm_file_or_dir_1416_13368()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=13369) as resolve_config_vars_in_file_1417_13369:
                resolve_config_vars_in_file_1417_13369()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=13370) as if_1418_13370:
                if_1418_13370()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=13371) as resolve_config_vars_in_file_1419_13371:
                resolve_config_vars_in_file_1419_13371()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=13372) as if_1420_13372:
                if_1420_13372()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13373) as resolve_config_vars_in_file_1421_13373:
                resolve_config_vars_in_file_1421_13373()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=13374) as if_1422_13374:
                if_1422_13374()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=13375) as resolve_config_vars_in_file_1423_13375:
                resolve_config_vars_in_file_1423_13375()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=13376) as if_1424_13376:
                if_1424_13376()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=13377) as resolve_config_vars_in_file_1425_13377:
                resolve_config_vars_in_file_1425_13377()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=13378) as if_1426_13378:
                if_1426_13378()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=13379) as resolve_config_vars_in_file_1427_13379:
                resolve_config_vars_in_file_1427_13379()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=13380) as if_1428_13380:
                if_1428_13380()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=13381) as resolve_config_vars_in_file_1429_13381:
                resolve_config_vars_in_file_1429_13381()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=13382) as if_1430_13382:
                if_1430_13382()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=13383) as resolve_config_vars_in_file_1431_13383:
                resolve_config_vars_in_file_1431_13383()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=13384) as if_1432_13384:
                if_1432_13384()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Propellerhead Software/ReWire", prog_num=13385) as cd_stage_1433_13385:
            cd_stage_1433_13385()
            with Stage(r"copy", r"WavesReWireDevice v13.0.0.129", prog_num=13386):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13387) as should_copy_source_1434_13387:
                    should_copy_source_1434_13387()
                    with Stage(r"copy source", r"Mac/Shells/ReWire.bundle", prog_num=13388):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", r".", delete_extraneous_files=True, prog_num=13389) as copy_dir_to_dir_1435_13389:
                            copy_dir_to_dir_1435_13389()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/ReWire.bundle", where_to_unwtar=r".", prog_num=13390) as unwtar_1436_13390:
                            unwtar_1436_13390()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/ReWire.bundle", user_id=-1, group_id=-1, prog_num=13391, recursive=True) as chown_1437_13391:
                            chown_1437_13391()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r"/Library/Application Support/Propellerhead Software/ReWire", skip_progress_count=4, prog_num=13392) as should_copy_source_1438_13392:
                    should_copy_source_1438_13392()
                    with Stage(r"copy source", r"Mac/Shells/WavesReWireDevice.bundle", prog_num=13393):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", r".", delete_extraneous_files=True, prog_num=13394) as copy_dir_to_dir_1439_13394:
                            copy_dir_to_dir_1439_13394()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WavesReWireDevice.bundle", where_to_unwtar=r".", prog_num=13395) as unwtar_1440_13395:
                            unwtar_1440_13395()
                        with Chown(path=r"/Library/Application Support/Propellerhead Software/ReWire/WavesReWireDevice.bundle", user_id=-1, group_id=-1, prog_num=13396, recursive=True) as chown_1441_13396:
                            chown_1441_13396()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13397) as shell_command_1442_13397:
                shell_command_1442_13397()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=13398) as cd_stage_1443_13398:
            cd_stage_1443_13398()
            with Stage(r"copy", r"COSMOS_HTML v2.4", prog_num=13399):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=13400) as should_copy_source_1444_13400:
                    should_copy_source_1444_13400()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=13401):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=13402) as copy_dir_to_dir_1445_13402:
                            copy_dir_to_dir_1445_13402()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=13403, recursive=True) as chown_1446_13403:
                            chown_1446_13403()
            with Stage(r"copy", r"COSMOS_python v2.4", prog_num=13404):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=13405) as should_copy_source_1447_13405:
                    should_copy_source_1447_13405()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=13406):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=13407) as copy_dir_to_dir_1448_13407:
                            copy_dir_to_dir_1448_13407()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=13408) as unwtar_1449_13408:
                            unwtar_1449_13408()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=13409, recursive=True) as chown_1450_13409:
                            chown_1450_13409()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=13410) as cd_stage_1451_13410:
            cd_stage_1451_13410()
            with Stage(r"copy", r"AnalyzeAudio v15.5.79.262", prog_num=13411):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=13412) as should_copy_source_1452_13412:
                    should_copy_source_1452_13412()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=13413):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=13414) as copy_dir_to_dir_1453_13414:
                            copy_dir_to_dir_1453_13414()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=13415) as unwtar_1454_13415:
                            unwtar_1454_13415()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=13416, recursive=True) as chown_1455_13416:
                            chown_1455_13416()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=13417) as cd_stage_1456_13417:
            cd_stage_1456_13417()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=13418):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=13419) as should_copy_source_1457_13419:
                    should_copy_source_1457_13419()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=13420):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=13421) as copy_dir_to_dir_1458_13421:
                            copy_dir_to_dir_1458_13421()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=13422, recursive=True) as chown_1459_13422:
                            chown_1459_13422()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V15", prog_num=13423) as cd_stage_1460_13423:
            cd_stage_1460_13423()
            with Stage(r"copy", r"License Notifications 1.1 v1.1", prog_num=13424):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r"/Library/Application Support/Waves/License Notifications/V15", skip_progress_count=3, prog_num=13425) as should_copy_source_1461_13425:
                    should_copy_source_1461_13425()
                    with Stage(r"copy source", r"Mac/License Notifications/V15/1", prog_num=13426):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/License Notifications/V15/1", r".", delete_extraneous_files=True, prog_num=13427) as copy_dir_to_dir_1462_13427:
                            copy_dir_to_dir_1462_13427()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V15/1", user_id=-1, group_id=-1, prog_num=13428, recursive=True) as chown_1463_13428:
                            chown_1463_13428()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=13429) as cd_stage_1464_13429:
            cd_stage_1464_13429()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=13430) as rm_file_or_dir_1465_13430:
                rm_file_or_dir_1465_13430()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=13431):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=13432) as should_copy_source_1466_13432:
                    should_copy_source_1466_13432()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=13433):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13434) as copy_dir_to_dir_1467_13434:
                            copy_dir_to_dir_1467_13434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=13435) as unwtar_1468_13435:
                            unwtar_1468_13435()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=13436, recursive=True) as chown_1469_13436:
                            chown_1469_13436()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=13437):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=13438) as should_copy_source_1470_13438:
                    should_copy_source_1470_13438()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=13439):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=13440) as unwtar_1471_13440:
                            unwtar_1471_13440()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=13441):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13442) as should_copy_source_1472_13442:
                    should_copy_source_1472_13442()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=13443):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=13444) as copy_dir_to_dir_1473_13444:
                            copy_dir_to_dir_1473_13444()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=13445) as unwtar_1474_13445:
                            unwtar_1474_13445()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=13446, recursive=True) as chown_1475_13446:
                            chown_1475_13446()
            with Stage(r"copy", r"OpenVino_2021.4.689 v2021.4.689", prog_num=13447):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=13448) as should_copy_source_1476_13448:
                    should_copy_source_1476_13448()
                    with Stage(r"copy source", r"Mac/Modules/openvino", prog_num=13449):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", r".", delete_extraneous_files=True, prog_num=13450) as copy_dir_to_dir_1477_13450:
                            copy_dir_to_dir_1477_13450()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/openvino", where_to_unwtar=r".", prog_num=13451) as unwtar_1478_13451:
                            unwtar_1478_13451()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/openvino", user_id=-1, group_id=-1, prog_num=13452, recursive=True) as chown_1479_13452:
                            chown_1479_13452()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=13453):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=13454) as should_copy_source_1480_13454:
                    should_copy_source_1480_13454()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=13455):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13456) as copy_dir_to_dir_1481_13456:
                            copy_dir_to_dir_1481_13456()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=13457) as chmod_1482_13457:
                            chmod_1482_13457()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=13458) as chmod_1483_13458:
                            chmod_1483_13458()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=13459, recursive=True) as chown_1484_13459:
                            chown_1484_13459()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=13462) as resolve_symlink_files_in_folder_1485_13462:
                resolve_symlink_files_in_folder_1485_13462()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13463) as shell_command_1486_13463:
                shell_command_1486_13463()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=13464) as cd_stage_1487_13464:
            cd_stage_1487_13464()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=13465):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=13466) as should_copy_source_1488_13466:
                    should_copy_source_1488_13466()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=13467):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=13468) as copy_dir_to_dir_1489_13468:
                            copy_dir_to_dir_1489_13468()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=13469, recursive=True) as chown_1490_13469:
                            chown_1490_13469()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=13470) as cd_stage_1491_13470:
            cd_stage_1491_13470()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=13471):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=13472) as should_copy_source_1492_13472:
                    should_copy_source_1492_13472()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=13473):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=13474, recursive=True) as chmod_1493_13474:
                            chmod_1493_13474()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13475) as copy_dir_to_dir_1494_13475:
                            copy_dir_to_dir_1494_13475()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=13476) as unwtar_1495_13476:
                            unwtar_1495_13476()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=13477, recursive=True) as chown_1496_13477:
                            chown_1496_13477()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13478) as if_1497_13478:
                            if_1497_13478()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=13479) as cd_stage_1498_13479:
            cd_stage_1498_13479()
            with Stage(r"copy", r"WavesPluginServer_V15_2 v15.2.178.179", prog_num=13480):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=5, prog_num=13481) as should_copy_source_1499_13481:
                    should_copy_source_1499_13481()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", prog_num=13482):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=13483) as copy_dir_to_dir_1500_13483:
                            copy_dir_to_dir_1500_13483()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WavesPluginServer/WavesPluginServerV15.2.bundle", where_to_unwtar=r".", prog_num=13484) as unwtar_1501_13484:
                            unwtar_1501_13484()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle", user_id=-1, group_id=-1, prog_num=13485, recursive=True) as chown_1502_13485:
                            chown_1502_13485()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_14-20250615162139-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/com.waves.wps.V15.2.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V15.2.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=13486) as if_1503_13486:
                            if_1503_13486()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=13487) as cd_stage_1504_13487:
            cd_stage_1504_13487()
            with Stage(r"copy", r"WaveShell1-AU 15.10 v15.10.46.293", prog_num=13488):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13489) as should_copy_source_1505_13489:
                    should_copy_source_1505_13489()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.10.component", prog_num=13490):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", r".", delete_extraneous_files=True, prog_num=13491) as copy_dir_to_dir_1506_13491:
                            copy_dir_to_dir_1506_13491()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.10.component", where_to_unwtar=r".", prog_num=13492) as unwtar_1507_13492:
                            unwtar_1507_13492()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13493, recursive=True) as chown_1508_13493:
                            chown_1508_13493()
                        with BreakHardLink(r"WaveShell1-AU 15.10.component/Contents/Info.plist", prog_num=13494) as break_hard_link_1509_13494:
                            break_hard_link_1509_13494()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.10.component"', ignore_all_errors=True, prog_num=13495) as shell_command_1510_13495:
                            shell_command_1510_13495()
                        with Chown(path=r"WaveShell1-AU 15.10.component", user_id=-1, group_id=-1, prog_num=13496, recursive=True) as chown_1511_13496:
                            chown_1511_13496()
                        with Chmod(path=r"WaveShell1-AU 15.10.component", mode="a+rwX", prog_num=13497, recursive=True) as chmod_1512_13497:
                            chmod_1512_13497()
            with Stage(r"copy", r"WaveShell1-AU 15.5 v15.5.79.262", prog_num=13498):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=13499) as should_copy_source_1513_13499:
                    should_copy_source_1513_13499()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 15.5.component", prog_num=13500):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", r".", delete_extraneous_files=True, prog_num=13501) as copy_dir_to_dir_1514_13501:
                            copy_dir_to_dir_1514_13501()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-AU 15.5.component", where_to_unwtar=r".", prog_num=13502) as unwtar_1515_13502:
                            unwtar_1515_13502()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13503, recursive=True) as chown_1516_13503:
                            chown_1516_13503()
                        with BreakHardLink(r"WaveShell1-AU 15.5.component/Contents/Info.plist", prog_num=13504) as break_hard_link_1517_13504:
                            break_hard_link_1517_13504()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 15.5.component"', ignore_all_errors=True, prog_num=13505) as shell_command_1518_13505:
                            shell_command_1518_13505()
                        with Chown(path=r"WaveShell1-AU 15.5.component", user_id=-1, group_id=-1, prog_num=13506, recursive=True) as chown_1519_13506:
                            chown_1519_13506()
                        with Chmod(path=r"WaveShell1-AU 15.5.component", mode="a+rwX", prog_num=13507, recursive=True) as chmod_1520_13507:
                            chmod_1520_13507()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=13508) as cd_stage_1521_13508:
            cd_stage_1521_13508()
            with Stage(r"copy", r"WaveShell1-VST3 15.10 v15.10.46.293", prog_num=13509):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13510) as should_copy_source_1522_13510:
                    should_copy_source_1522_13510()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.10.vst3", prog_num=13511):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", r".", delete_extraneous_files=True, prog_num=13512) as copy_dir_to_dir_1523_13512:
                            copy_dir_to_dir_1523_13512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.10.vst3", where_to_unwtar=r".", prog_num=13513) as unwtar_1524_13513:
                            unwtar_1524_13513()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.10.vst3", user_id=-1, group_id=-1, prog_num=13514, recursive=True) as chown_1525_13514:
                            chown_1525_13514()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.10.vst3"', ignore_all_errors=True, prog_num=13515) as shell_command_1526_13515:
                            shell_command_1526_13515()
            with Stage(r"copy", r"WaveShell1-VST3 15.5 v15.5.79.262", prog_num=13516):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=13517) as should_copy_source_1527_13517:
                    should_copy_source_1527_13517()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 15.5.vst3", prog_num=13518):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", r".", delete_extraneous_files=True, prog_num=13519) as copy_dir_to_dir_1528_13519:
                            copy_dir_to_dir_1528_13519()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Shells/WaveShell1-VST3 15.5.vst3", where_to_unwtar=r".", prog_num=13520) as unwtar_1529_13520:
                            unwtar_1529_13520()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 15.5.vst3", user_id=-1, group_id=-1, prog_num=13521, recursive=True) as chown_1530_13521:
                            chown_1530_13521()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 15.5.vst3"', ignore_all_errors=True, prog_num=13522) as shell_command_1531_13522:
                            shell_command_1531_13522()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13523) as cd_stage_1532_13523:
            cd_stage_1532_13523()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.10 v15.10.46.293", prog_num=13524):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13525) as should_copy_source_1533_13525:
                    should_copy_source_1533_13525()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", prog_num=13526):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", r".", delete_extraneous_files=True, prog_num=13527) as copy_dir_to_dir_1534_13527:
                            copy_dir_to_dir_1534_13527()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", where_to_unwtar=r".", prog_num=13528) as unwtar_1535_13528:
                            unwtar_1535_13528()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.10.bundle", user_id=-1, group_id=-1, prog_num=13529, recursive=True) as chown_1536_13529:
                            chown_1536_13529()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13530) as shell_command_1537_13530:
                            shell_command_1537_13530()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13531) as script_command_1538_13531:
                            script_command_1538_13531()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13532) as shell_command_1539_13532:
                            shell_command_1539_13532()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 15.5 v15.5.79.262", prog_num=13533):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=13534) as should_copy_source_1540_13534:
                    should_copy_source_1540_13534()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", prog_num=13535):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", r".", delete_extraneous_files=True, prog_num=13536) as copy_dir_to_dir_1541_13536:
                            copy_dir_to_dir_1541_13536()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", where_to_unwtar=r".", prog_num=13537) as unwtar_1542_13537:
                            unwtar_1542_13537()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 15.5.bundle", user_id=-1, group_id=-1, prog_num=13538, recursive=True) as chown_1543_13538:
                            chown_1543_13538()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=13539) as shell_command_1544_13539:
                            shell_command_1544_13539()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=13540) as script_command_1545_13540:
                            script_command_1545_13540()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=13541) as shell_command_1546_13541:
                            shell_command_1546_13541()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13542) as create_symlink_1547_13542:
                create_symlink_1547_13542()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=13543) as create_symlink_1548_13543:
                create_symlink_1548_13543()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=13544) as cd_stage_1549_13544:
            cd_stage_1549_13544()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=13545) as rm_file_or_dir_1550_13545:
                rm_file_or_dir_1550_13545()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=13546) as cd_stage_1551_13546:
            cd_stage_1551_13546()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=13547) as rm_file_or_dir_1552_13547:
                rm_file_or_dir_1552_13547()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=13548) as rm_file_or_dir_1553_13548:
                rm_file_or_dir_1553_13548()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=13549) as rm_file_or_dir_1554_13549:
                rm_file_or_dir_1554_13549()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=13550) as shell_command_1555_13550:
            shell_command_1555_13550()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=13551) as shell_command_1556_13551:
            shell_command_1556_13551()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=13552) as script_command_1557_13552:
            script_command_1557_13552()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=13553) as rm_file_or_dir_1558_13553:
            rm_file_or_dir_1558_13553()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13554) as move_dir_to_dir_1559_13554:
            move_dir_to_dir_1559_13554()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13555) as move_dir_to_dir_1560_13555:
            move_dir_to_dir_1560_13555()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13556) as move_dir_to_dir_1561_13556:
            move_dir_to_dir_1561_13556()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13557) as move_dir_to_dir_1562_13557:
            move_dir_to_dir_1562_13557()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=13558) as make_dirs_1563_13558:
            make_dirs_1563_13558()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13559) as move_dir_to_dir_1564_13559:
            move_dir_to_dir_1564_13559()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=13560) as move_dir_to_dir_1565_13560:
            move_dir_to_dir_1565_13560()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=13561) as shell_command_1566_13561:
            shell_command_1566_13561()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=13562) as script_command_1567_13562:
            script_command_1567_13562()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=13563) as rm_file_or_dir_1568_13563:
            rm_file_or_dir_1568_13563()
        with Glober(r"/Library/Audio/Plug-Ins/VST/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13564) as glober_1569_13564:
            glober_1569_13564()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=13565) as glober_1570_13565:
            glober_1570_13565()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=13566) as glober_1571_13566:
            glober_1571_13566()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=13567) as glober_1572_13567:
            glober_1572_13567()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=13568) as shell_command_1573_13568:
            shell_command_1573_13568()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V15" -c', ignore_all_errors=True, prog_num=13569) as shell_command_1574_13569:
            shell_command_1574_13569()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V15"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V15"/Icon?; fi', prog_num=13570) as script_command_1575_13570:
            script_command_1575_13570()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=13571) as if_1576_13571:
            if_1576_13571()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13572) as if_1577_13572:
            if_1577_13572()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=13573) as if_1578_13573:
            if_1578_13573()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=13574) as if_1579_13574:
            if_1579_13574()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=13575) as make_dir_1580_13575:
            make_dir_1580_13575()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=13576) as chmod_1581_13576:
            chmod_1581_13576()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", prog_num=13577) as make_dir_1582_13577:
            make_dir_1582_13577()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2", mode="a+rwx", ignore_if_not_exist=True, prog_num=13578) as chmod_1583_13578:
            chmod_1583_13578()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13579) as chmod_1584_13579:
            chmod_1584_13579()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V15.2/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=13580) as chmod_1585_13580:
            chmod_1585_13580()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=13581) as chmod_1586_13581:
            chmod_1586_13581()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=13582) as shell_command_1587_13582:
            shell_command_1587_13582()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=13583) as script_command_1588_13583:
            script_command_1588_13583()
    with Stage(r"post-copy", prog_num=13584):
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13585) as make_dir_1589_13585:
            make_dir_1589_13585()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V15/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=13586) as copy_file_to_file_1590_13586:
            copy_file_to_file_1590_13586()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13587) as chmod_1591_13587:
            chmod_1591_13587()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13588) as chmod_1592_13588:
            chmod_1592_13588()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/require.yaml", r"/Library/Application Support/Waves/Central/V15/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=13589) as copy_file_to_file_1593_13589:
            copy_file_to_file_1593_13589()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13590) as chmod_1594_13590:
            chmod_1594_13590()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V15/new_require.yaml", r"/Library/Application Support/Waves/Central/V15/require.yaml", hard_links=False, copy_owner=True, prog_num=13591) as copy_file_to_file_1595_13591:
            copy_file_to_file_1595_13591()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V15/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=13592) as chmod_1596_13592:
            chmod_1596_13592()
        Progress(r"Done copy", prog_num=13593)()
        Progress(r"Done synccopy", prog_num=13594)()
    with Stage(r"post", prog_num=13595):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13596) as make_dir_1597_13596:
            make_dir_1597_13596()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V15_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/V15_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=13597) as copy_file_to_file_1598_13597:
            copy_file_to_file_1598_13597()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping", chowner=True, prog_num=13598) as make_dir_1599_13598:
            make_dir_1599_13598()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=13599) as copy_file_to_file_1600_13599:
            copy_file_to_file_1600_13599()
        with MakeDir(r"/Library/Application Support/Waves/Central/V15", chowner=True, prog_num=13600) as make_dir_1601_13600:
            make_dir_1601_13600()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V15/bookkeeping/59/index.yaml", r"/Library/Application Support/Waves/Central/V15/index.yaml", hard_links=False, copy_owner=True, prog_num=13601) as copy_file_to_file_1602_13601:
            copy_file_to_file_1602_13601()

with Stage(r"epilog", prog_num=13602):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_15-20250615162139.py", prog_num=13603) as patch_py_batch_with_timings_1603_13603:
        patch_py_batch_with_timings_1603_13603()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


