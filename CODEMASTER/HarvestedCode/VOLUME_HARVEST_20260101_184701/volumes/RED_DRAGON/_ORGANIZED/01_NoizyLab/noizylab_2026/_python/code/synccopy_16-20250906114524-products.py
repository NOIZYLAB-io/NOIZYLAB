# Creation time: 06-09-25_11-45
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 26637
PythonBatchCommandBase.running_progress = 1372
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1373):
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac64", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac64")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250906114524-products"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX")
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
    config_vars['MAIN_INSTALL_TARGETS'] = (r"0386f35f-d467-42c1-9aa2-593d4f331cc6", r"1374eaac-1f40-4629-a1bd-7fad36931856", r"1b2e3046-b634-4fc3-92df-100722e72a75", r"1d2e15ad-514e-4894-b13c-087940f2c275", r"215572dc-9c91-4912-a0a9-d68096edc994", r"22195f90-44a7-41aa-8e89-7cd4032a553e", r"239c7584-82a0-420d-bfae-8885b3a52538", r"289510f1-fdf8-45ee-ae8d-4f42cc82ca64", r"29e06aff-907d-4711-a74e-3f8a59d69d79", r"2acada14-94c5-4414-9d64-454da34b0639", r"2d71ad91-bddb-42f2-a652-835830176f9f", r"30917ee9-a700-481d-85d7-2062c35a9802", r"3164b0cb-806c-4bdd-a286-260f9c6eb04c", r"329dbe6a-233e-4f8f-ac70-f5b55036845b", r"34ec8670-67d0-4e60-9e6a-3a3d15146c3c", r"386ca2e5-2636-495f-810e-49eceb953b9f", r"3c217951-f061-42a9-a797-c6ae08355e8d", r"3cc8e3c0-c209-4128-a2f6-32be589badbf", r"3d47fe76-e1f9-4cbf-b155-715460ee749f", r"423381b7-4e7e-41e2-a69a-518aefd4ef13", r"49e069d6-907d-4991-a74e-3f8959d69830", r"51472ece-6f53-4926-8123-64330d6c6852", r"53a2fb95-8424-429f-a2c8-21e86b847f0a", r"558c21cb-b648-48a3-a23b-db455ecc2d55", r"5634fda9-ea28-4316-9476-527b8e7279a9", r"5daf4282-f6c5-4e00-b7d5-cac37ad48604", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"63b0a9f9-a701-4596-acb7-ab671e5addd9", r"6983b49f-2238-4e1e-8828-50ca84f58737", r"6c7cdfec-03f7-4d62-84c3-9ea633067fc9", r"72e4f2f3-cc29-4635-8715-a7977a943920", r"7707a80e-06f0-412a-b2de-baa2c332bb13", r"7c01bd8c-6267-48ce-8707-9df05b786b7b", r"811b0faa-6979-4500-a187-791e07c79138", r"87d5ca54-c659-460d-92ca-d25786210a25", r"8ce7a272-1741-4893-b516-e93ce40db756", r"911c58f1-0b6b-42f7-93dd-a571b29860fc", r"96f2b292-8c3b-49f4-8193-4f7783654547", r"__UPDATE_INSTALLED_ITEMS__", r"aa264888-988b-421c-89c9-629934734f37", r"ab09a527-4793-44f2-9353-c25cc1f4b856", r"ae4b9cc6-a30f-42ad-b4db-28cb21cda94b", r"b158aea5-79f7-4a39-b9b9-f8c5e7c237c2", r"b3964c48-04db-470f-b5b8-fa2b340a6fd4", r"b8a31ecd-5110-4d10-ba3d-ca56215b3745", r"c079789d-12a1-42af-8cf5-53295d4fdf55", r"c19c1d27-90ca-43e3-b503-9c7f2da272bc", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"ca9a4322-a903-43ec-95d7-ccbbb475d2d5", r"d1b17f75-9fbf-4af9-9c8e-ebb7068998b9", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"dfc80d80-ad21-11e0-804c-b7fd7bebd530", r"dfe64476-ad21-11e0-80e3-b7fd7bebd530", r"e0052ccd-ad21-11e0-81d6-b7fd7bebd530", r"e023b7a0-ad21-11e0-80bf-b7fd7bebd530", r"e0427e39-ad21-11e0-832d-b7fd7bebd530", r"e06158e4-ad21-11e0-80ed-b7fd7bebd530", r"e09dd956-ad21-11e0-80a8-b7fd7bebd530", r"e10288b9-ad21-11e0-8381-b7fd7bebd530", r"e1e91460-ad21-11e0-8303-b7fd7bebd530", r"e22cd127-ad21-11e0-822b-b7fd7bebd530", r"e39dce24-16c9-4f4a-bb98-545e10052b75", r"e3a57973-ad21-11e0-818c-b7fd7bebd530", r"e3c605a4-ad21-11e0-8113-b7fd7bebd530", r"e47a4b22-ad21-11e0-80ba-b7fd7bebd530", r"e4b00ec4-ad21-11e0-834b-b7fd7bebd530", r"e4e5fb53-131e-45e0-91c1-d78aa4f5c69f", r"e4e72e7b-ad21-11e0-81a6-b7fd7bebd530", r"e5100b89-ad21-11e0-81a0-b7fd7bebd530", r"e551833a-ad21-11e0-8177-b7fd7bebd530", r"e591e90a-ad21-11e0-83a1-b7fd7bebd530", r"e5ce4a76-ad21-11e0-832b-b7fd7bebd530", r"e5ecb58a-ad21-11e0-820b-b7fd7bebd530", r"e60ab8c6-ad21-11e0-8364-b7fd7bebd530", r"e6281b3c-ad21-11e0-8087-b7fd7bebd530", r"e646beb6-ad21-11e0-83c3-b7fd7bebd530", r"e6675177-ad21-11e0-833e-b7fd7bebd530", r"e686154a-ad21-11e0-806f-b7fd7bebd530", r"e686394e-ad21-11e0-8185-b7fd7bebd530", r"e6a8de66-ad21-11e0-81f4-b7fd7bebd530", r"e6c7625a-ad21-11e0-8262-b7fd7bebd530", r"e6ead714-ad21-11e0-82a6-b7fd7bebd530", r"e7069133-ad21-11e0-82c1-b7fd7bebd530", r"e7223951-ad21-11e0-82d3-b7fd7bebd530", r"e73ed1fb-ad21-11e0-8035-b7fd7bebd530", r"e759bc5f-ad21-11e0-827d-b7fd7bebd530", r"e775f5e1-ad21-11e0-809f-b7fd7bebd530", r"e790fd1a-ad21-11e0-82c3-b7fd7bebd530", r"e7af58a0-ad21-11e0-832f-b7fd7bebd530", r"e7cd30b4-ad21-11e0-8385-b7fd7bebd530", r"e808505c-ad21-11e0-83e8-b7fd7bebd530", r"e8f6b97d-ad21-11e0-8088-b7fd7bebd530", r"e92b2cea-ad21-11e0-8218-b7fd7bebd530", r"e9797602-ad21-11e0-8369-b7fd7bebd530", r"e9ef3ffd-ad21-11e0-83e3-b7fd7bebd530", r"ea1152ba-ad21-11e0-8305-b7fd7bebd530", r"ea4ad51a-ad21-11e0-8137-b7fd7bebd530", r"ea812d41-ad21-11e0-80f3-b7fd7bebd530", r"ea9c2b7e-ad21-11e0-8327-b7fd7bebd530", r"eab8d633-ad21-11e0-81eb-b7fd7bebd530", r"eb0c63ec-ad21-11e0-8288-b7fd7bebd530", r"eb542f98-ad21-11e0-8222-b7fd7bebd530", r"eb621b67-ad21-11e0-8319-b7fd7bebd530", r"ec32123c-ad21-11e0-83d2-b7fd7bebd530", r"ec53f8dd-ad21-11e0-8276-b7fd7bebd530", r"ec541a62-ad21-11e0-8150-b7fd7bebd530", r"ec719e28-ad21-11e0-8100-b7fd7bebd530", r"ec971ad7-ad21-11e0-8359-b7fd7bebd530", r"ec97493f-ad21-11e0-803e-b7fd7bebd530", r"eced4ec6-6f5a-4d23-880a-0e522dd7db8d", r"ed13f26a-ad21-11e0-8216-b7fd7bebd530", r"ed14136b-ad21-11e0-837c-b7fd7bebd530", r"ed748b6e-ad21-11e0-83bb-b7fd7bebd530", r"edff65f4-ad21-11e0-8126-b7fd7bebd530", r"ee3dacf8-ad21-11e0-83ec-b7fd7bebd530", r"ee76f044-ad21-11e0-8170-b7fd7bebd530", r"ee93e582-ad21-11e0-8390-b7fd7bebd530", r"ef202a69-ad21-11e0-839b-b7fd7bebd530", r"ef3b4d52-ad21-11e0-8109-b7fd7bebd530", r"ef6067d8-ad21-11e0-8308-b7fd7bebd530", r"ef7b9575-ad21-11e0-81f1-b7fd7bebd530", r"ef9640eb-ad21-11e0-83ab-b7fd7bebd530", r"efb10934-ad21-11e0-8058-b7fd7bebd530", r"efce20a0-ad21-11e0-8012-b7fd7bebd530", r"efe96c20-ad21-11e0-833c-b7fd7bebd530", r"f00484d0-ad21-11e0-8357-b7fd7bebd530", r"f01f84d6-ad21-11e0-822a-b7fd7bebd530", r"f03a7463-ad21-11e0-830f-b7fd7bebd530", r"f056c254-ad21-11e0-8310-b7fd7bebd530", r"f169fb78-ad21-11e0-8276-b7fd7bebd530", r"f1e2bcde-ad21-11e0-800a-b7fd7bebd530", r"f202b779-ad21-11e0-8344-b7fd7bebd530", r"f2214239-ad21-11e0-82e2-b7fd7bebd530", r"f23de82a-ad21-11e0-803b-b7fd7bebd530", r"f25bce3b-ad21-11e0-8126-b7fd7bebd530", r"f2781703-ad21-11e0-8147-b7fd7bebd530", r"f2a5ad2a-ad21-11e0-8185-b7fd7bebd530", r"f2f168c9-ad21-11e0-803f-b7fd7bebd530", r"f3315154-ad21-11e0-8140-b7fd7bebd530", r"f3513e7f-ad21-11e0-83f7-b7fd7bebd530", r"f3515f5a-ad21-11e0-81da-b7fd7bebd530", r"f4b4c760-76c5-4b08-b2f9-7df547f7bd19", r"fcdbc046-5e44-4d4d-b4ec-049d194c2458")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 19
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
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml")
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
    config_vars['REQUIRE_REPO_REV'] = 15
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 25260
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250906114524.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-08-23 23:57:51.343637"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.6.1"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac64", r"MacArm")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac64"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Q_Clone_Presets_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Effects_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_Data_Folders_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS_Models_Data_Folders_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"CR8_Sampler_Presets_IID", r"CURVES_AQ_IID", r"Center_IID", r"ChainersChildExcludeList_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx__Presets__IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Curves_AQ_Special_Data__IID", r"Curves_AQ__Presets__IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_V16_1_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Enigma_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"Get_General_Icons_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR_360_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InTrigger_Data_Folders_IID", r"InTrigger_IID", r"InTrigger_Live_IID", r"InTrigger_Live_Presets_IID", r"InTrigger_Presets_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LicenseNotifications_V16_1_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"ONNXRUNTIME_IID", r"ORS_Modulators_Data_IID", r"PAZ_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_V16_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"SOC_Presets_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"SuperTap_IID", r"SyncVx_Data_IID", r"SyncVx_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"WLM_IID", r"WLM_Plus_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AAX_16_1_IID", r"WaveShell1_AAX_16_2_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_AU_16_1_IID", r"WaveShell1_AU_16_2_IID", r"WaveShell1_VST3_ARA_V16_0_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_VST3_V16_1_IID", r"WaveShell1_VST_3_V16_2_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell1_WPAPI_2_16_1_IID", r"WaveShell1_WPAPI_2_16_2_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_16_0_23_IID", r"WavesLib1_16_0_30_IID", r"WavesLib1_16_0_64_IID", r"WavesLib1_16_0_78_IID", r"WavesLib1_16_0_91_IID", r"WavesLib1_16_1_99_IID", r"WavesLib1_16_2_30_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V16_1_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.2.1 2025-08-23 23:57:51.343637 bm-mac-ado12"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.2.1"
    config_vars['__INSTL_VERSION__'] = (2, 5, 2, 1)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"rifadwhpipinonon"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"ARPlates_IID", r"ARVinyl_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C4_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Effects_IID", r"CLA_Guitars_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"CURVES_AQ_IID", r"Center_IID", r"Clarity_Vx_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Doubler_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_DR_IID", r"EddieKramer_VC_IID", r"ElectricG80_IID", r"Enigma_IID", r"GTRAmp_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_Reverb_IID", r"IR_L_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InTrigger_IID", r"InTrigger_Live_IID", r"J37_IID", r"JJP-Vocals_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MV2_IID", r"MagmaSprings_IID", r"MannyM-TripleD_IID", r"Maserati_DRM_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"NLS_IID", r"NX_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKPhatter_IID", r"OKPumper_IID", r"PAZ_IID", r"PS22_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"SuperTap_IID", r"SyncVx_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"WLM_IID", r"WLM_Plus_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = (r"IR_360_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_VST3_V16_0_IID")
    config_vars['__NOW__'] = r"2025-09-06 11:47:59.086100"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 209117367
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 1858
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

with PythonBatchRuntime(r"synccopy", prog_num=1374):
    with Stage(r"begin", prog_num=1375):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1376):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1377) as copy_file_to_file_001_1377:
            copy_file_to_file_001_1377()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1378) as copy_file_to_file_002_1378:
            copy_file_to_file_002_1378()
    with Stage(r"sync", prog_num=1379):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1380) as shell_command_003_1380:
            shell_command_003_1380()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1381) as shell_command_004_1381:
            shell_command_004_1381()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=1382) as shell_command_005_1382:
            shell_command_005_1382()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1383) as shell_command_006_1383:
            shell_command_006_1383()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1384) as shell_command_007_1384:
            shell_command_007_1384()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1385) as shell_command_008_1385:
            shell_command_008_1385()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1386) as shell_command_009_1386:
            shell_command_009_1386()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1387) as shell_command_010_1387:
            shell_command_010_1387()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1388) as shell_command_011_1388:
            shell_command_011_1388()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=1389):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=1390) as make_dir_012_1390:
                make_dir_012_1390()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1391) as cd_013_1391:
                cd_013_1391()
                Progress(r"18989 files already in cache", own_progress_count=18989, prog_num=20380)()
                with CreateSyncFolders(own_progress_count=94, prog_num=20474) as create_sync_folders_014_20474:
                    create_sync_folders_014_20474()
                Progress(r"Downloading with 50 processes in parallel", prog_num=20475)()
                Progress(r"Downloading with curl parallel", prog_num=20476)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.py_curl/dl-00", total_files_to_download=1858, previously_downloaded_files=0, total_bytes_to_download=209117367, own_progress_count=1836, prog_num=22312, report_own_progress=False) as curl_with_internal_parallel_015_22312:
                    curl_with_internal_parallel_015_22312()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.py_curl/dl-01", total_files_to_download=1858, previously_downloaded_files=1836, total_bytes_to_download=209117367, own_progress_count=22, prog_num=22334, report_own_progress=False) as curl_with_internal_parallel_016_22334:
                    curl_with_internal_parallel_016_22334()
                Progress(r"Downloading 1858 files done", prog_num=22335)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=22336) as run_in_thread_017_22336:
                    run_in_thread_017_22336()
                Progress(r"Check checksum ...", prog_num=22337)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=1858, prog_num=24195) as check_download_folder_checksum_018_24195:
                    check_download_folder_checksum_018_24195()
                with Stage(r"post_sync", prog_num=24196):
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16...", prog_num=24197)()
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=24198, recursive=True) as chmod_and_chown_019_24198:
                        chmod_and_chown_019_24198()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=24199) as copy_file_to_file_020_24199:
                        copy_file_to_file_020_24199()
            Progress(r"Done sync", prog_num=24200)()
    with Stage(r"copy", prog_num=24201):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=24202)()
        with Stage(r"create folders", prog_num=24203):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=24204) as make_dir_021_24204:
                make_dir_021_24204()
            with MakeDir(r"/Applications/Waves/Applications V16", chowner=True, prog_num=24205) as make_dir_022_24205:
                make_dir_022_24205()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=24206) as make_dir_023_24206:
                make_dir_023_24206()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=24207) as make_dir_024_24207:
                make_dir_024_24207()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx/onnx/Network", chowner=True, prog_num=24208) as make_dir_025_24208:
                make_dir_025_24208()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=24209) as make_dir_026_24209:
                make_dir_026_24209()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=24210) as make_dir_027_24210:
                make_dir_027_24210()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=24211) as make_dir_028_24211:
                make_dir_028_24211()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=24212) as make_dir_029_24212:
                make_dir_029_24212()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=24213) as make_dir_030_24213:
                make_dir_030_24213()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=24214) as make_dir_031_24214:
                make_dir_031_24214()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=24215) as make_dir_032_24215:
                make_dir_032_24215()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=24216) as make_dir_033_24216:
                make_dir_033_24216()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=24217) as make_dir_034_24217:
                make_dir_034_24217()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=24218) as make_dir_035_24218:
                make_dir_035_24218()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=24219) as make_dir_036_24219:
                make_dir_036_24219()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTR", chowner=True, prog_num=24220) as make_dir_037_24220:
                make_dir_037_24220()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=24221) as make_dir_038_24221:
                make_dir_038_24221()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=24222) as make_dir_039_24222:
                make_dir_039_24222()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=24223) as make_dir_040_24223:
                make_dir_040_24223()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=24224) as make_dir_041_24224:
                make_dir_041_24224()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=24225) as make_dir_042_24225:
                make_dir_042_24225()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=24226) as make_dir_043_24226:
                make_dir_043_24226()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=24227) as make_dir_044_24227:
                make_dir_044_24227()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=24228) as make_dir_045_24228:
                make_dir_045_24228()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=24229) as make_dir_046_24229:
                make_dir_046_24229()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=24230) as make_dir_047_24230:
                make_dir_047_24230()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=24231) as make_dir_048_24231:
                make_dir_048_24231()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=24232) as make_dir_049_24232:
                make_dir_049_24232()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=24233) as make_dir_050_24233:
                make_dir_050_24233()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=24234) as make_dir_051_24234:
                make_dir_051_24234()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=24235) as make_dir_052_24235:
                make_dir_052_24235()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=24236) as make_dir_053_24236:
                make_dir_053_24236()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=24237) as make_dir_054_24237:
                make_dir_054_24237()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=24238) as make_dir_055_24238:
                make_dir_055_24238()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=24239) as rm_file_or_dir_056_24239:
            rm_file_or_dir_056_24239()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=24240) as shell_command_057_24240:
            shell_command_057_24240()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=24241) as shell_command_058_24241:
            shell_command_058_24241()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=24242) as shell_command_059_24242:
            shell_command_059_24242()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=24243) as shell_command_060_24243:
            shell_command_060_24243()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=24244) as shell_command_061_24244:
            shell_command_061_24244()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=24245) as shell_command_062_24245:
            shell_command_062_24245()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=24246) as shell_command_063_24246:
            shell_command_063_24246()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=24247) as shell_command_064_24247:
            shell_command_064_24247()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=24248) as shell_command_065_24248:
            shell_command_065_24248()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=24249) as cd_stage_066_24249:
            cd_stage_066_24249()
            with SetExecPermissionsInSyncFolder(prog_num=24250) as set_exec_permissions_in_sync_folder_067_24250:
                set_exec_permissions_in_sync_folder_067_24250()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V16", prog_num=24251) as cd_stage_068_24251:
            cd_stage_068_24251()
            with Stage(r"copy", r"Bass Slapper application v16.0.23.24", prog_num=24252):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=24253) as should_copy_source_069_24253:
                    should_copy_source_069_24253()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=24254):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=24255) as copy_dir_to_dir_070_24255:
                            copy_dir_to_dir_070_24255()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=24256) as unwtar_071_24256:
                            unwtar_071_24256()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=24257, recursive=True) as chown_072_24257:
                            chown_072_24257()
            with Stage(r"copy", r"Electric Grand 80 application v16.0.23.24", prog_num=24258):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=24259) as should_copy_source_073_24259:
                    should_copy_source_073_24259()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=24260):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=24261) as copy_dir_to_dir_074_24261:
                            copy_dir_to_dir_074_24261()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=24262) as unwtar_075_24262:
                            unwtar_075_24262()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=24263, recursive=True) as chown_076_24263:
                            chown_076_24263()
            with Stage(r"copy", r"GTR application v16.0.23.24", prog_num=24264):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=24265) as should_copy_source_077_24265:
                    should_copy_source_077_24265()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=24266):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=24267) as copy_dir_to_dir_078_24267:
                            copy_dir_to_dir_078_24267()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=24268) as unwtar_079_24268:
                            unwtar_079_24268()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=24269, recursive=True) as chown_080_24269:
                            chown_080_24269()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V16" -c', ignore_all_errors=True, prog_num=24270) as shell_command_081_24270:
                shell_command_081_24270()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V16"/Icon?; fi', prog_num=24271) as script_command_082_24271:
                script_command_082_24271()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=24272) as cd_stage_083_24272:
            cd_stage_083_24272()
            with Stage(r"copy", r"COSMOS__Application v16.0.50.51", prog_num=24273):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=24274) as should_copy_source_084_24274:
                    should_copy_source_084_24274()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=24275):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=24276) as copy_dir_to_dir_085_24276:
                            copy_dir_to_dir_085_24276()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=24277) as unwtar_086_24277:
                            unwtar_086_24277()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=24278, recursive=True) as chown_087_24278:
                            chown_087_24278()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=24288) as resolve_symlink_files_in_folder_088_24288:
                resolve_symlink_files_in_folder_088_24288()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=24289) as cd_stage_089_24289:
            cd_stage_089_24289()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=24290):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24291) as should_copy_source_090_24291:
                    should_copy_source_090_24291()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=24292):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=24293) as copy_dir_to_dir_091_24293:
                            copy_dir_to_dir_091_24293()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=24294, recursive=True) as chown_092_24294:
                            chown_092_24294()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=24295):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=24296) as should_copy_source_093_24296:
                    should_copy_source_093_24296()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=24297):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=24298) as copy_dir_to_dir_094_24298:
                            copy_dir_to_dir_094_24298()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=24299) as unwtar_095_24299:
                            unwtar_095_24299()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=24300, recursive=True) as chown_096_24300:
                            chown_096_24300()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.2", prog_num=24301):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24302) as should_copy_source_097_24302:
                    should_copy_source_097_24302()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=24303):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=24304) as copy_dir_to_dir_098_24304:
                            copy_dir_to_dir_098_24304()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=24305, recursive=True) as chown_099_24305:
                            chown_099_24305()
            with Stage(r"copy", r"Curves_AQ_Special_Data v1.0.0.4", prog_num=24306):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=24307) as should_copy_source_100_24307:
                    should_copy_source_100_24307()
                    with Stage(r"copy source", r"Common/Data/Curves", prog_num=24308):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r".", delete_extraneous_files=True, prog_num=24309) as copy_dir_to_dir_101_24309:
                            copy_dir_to_dir_101_24309()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", where_to_unwtar=r".", prog_num=24310) as unwtar_102_24310:
                            unwtar_102_24310()
                        with Chown(path=r"/Applications/Waves/Data/Curves", user_id=-1, group_id=-1, prog_num=24311, recursive=True) as chown_103_24311:
                            chown_103_24311()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=24312):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24313) as should_copy_source_104_24313:
                    should_copy_source_104_24313()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=24314):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=24315) as copy_dir_to_dir_105_24315:
                            copy_dir_to_dir_105_24315()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=24316, recursive=True) as chown_106_24316:
                            chown_106_24316()
            with Stage(r"copy", r"InTrigger__Data_Folders v1.0.0.3", prog_num=24317):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/InTrigger", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24318) as should_copy_source_107_24318:
                    should_copy_source_107_24318()
                    with Stage(r"copy source", r"Common/Data/InTrigger", prog_num=24319):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/InTrigger", r".", delete_extraneous_files=True, prog_num=24320) as copy_dir_to_dir_108_24320:
                            copy_dir_to_dir_108_24320()
                        with Chown(path=r"/Applications/Waves/Data/InTrigger", user_id=-1, group_id=-1, prog_num=24321, recursive=True) as chown_109_24321:
                            chown_109_24321()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=24322):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24323) as should_copy_source_110_24323:
                    should_copy_source_110_24323()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=24324):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=24325) as copy_dir_to_dir_111_24325:
                            copy_dir_to_dir_111_24325()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=24326, recursive=True) as chown_112_24326:
                            chown_112_24326()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=24327):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24328) as should_copy_source_113_24328:
                    should_copy_source_113_24328()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=24329):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=24330) as copy_dir_to_dir_114_24330:
                            copy_dir_to_dir_114_24330()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=24331, recursive=True) as chown_115_24331:
                            chown_115_24331()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=24332):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=24333) as should_copy_source_116_24333:
                    should_copy_source_116_24333()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=24334):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=24335) as copy_dir_to_dir_117_24335:
                            copy_dir_to_dir_117_24335()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=24336, recursive=True) as chown_118_24336:
                            chown_118_24336()
            with Stage(r"copy", r"SyncVx Data v1.0.0.2", prog_num=24337):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=24338) as should_copy_source_119_24338:
                    should_copy_source_119_24338()
                    with Stage(r"copy source", r"Common/Data/SyncVx", prog_num=24339):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r".", delete_extraneous_files=True, prog_num=24340) as copy_dir_to_dir_120_24340:
                            copy_dir_to_dir_120_24340()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", where_to_unwtar=r".", prog_num=24341) as unwtar_121_24341:
                            unwtar_121_24341()
                        with Chown(path=r"/Applications/Waves/Data/SyncVx", user_id=-1, group_id=-1, prog_num=24342, recursive=True) as chown_122_24342:
                            chown_122_24342()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=24343):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=24344) as should_copy_source_123_24344:
                    should_copy_source_123_24344()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=24345):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=24346) as copy_dir_to_dir_124_24346:
                            copy_dir_to_dir_124_24346()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", where_to_unwtar=r".", prog_num=24347) as unwtar_125_24347:
                            unwtar_125_24347()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=24348, recursive=True) as chown_126_24348:
                            chown_126_24348()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", prog_num=24349) as cd_stage_127_24349:
            cd_stage_127_24349()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.5", prog_num=24350):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=3, prog_num=24351) as should_copy_source_128_24351:
                    should_copy_source_128_24351()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=24352):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r".", prog_num=24353) as copy_file_to_dir_129_24353:
                            copy_file_to_dir_129_24353()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=24354) as chmod_and_chown_130_24354:
                            chmod_and_chown_130_24354()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=24355) as should_copy_source_131_24355:
                    should_copy_source_131_24355()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/A", prog_num=24356):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", r".", delete_extraneous_files=True, prog_num=24357) as copy_dir_to_dir_132_24357:
                            copy_dir_to_dir_132_24357()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/A", where_to_unwtar=r".", prog_num=24358) as unwtar_133_24358:
                            unwtar_133_24358()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/A", user_id=-1, group_id=-1, prog_num=24359, recursive=True) as chown_134_24359:
                            chown_134_24359()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=24360) as should_copy_source_135_24360:
                    should_copy_source_135_24360()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/B", prog_num=24361):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", r".", delete_extraneous_files=True, prog_num=24362) as copy_dir_to_dir_136_24362:
                            copy_dir_to_dir_136_24362()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/B", where_to_unwtar=r".", prog_num=24363) as unwtar_137_24363:
                            unwtar_137_24363()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/B", user_id=-1, group_id=-1, prog_num=24364, recursive=True) as chown_138_24364:
                            chown_138_24364()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=24365) as should_copy_source_139_24365:
                    should_copy_source_139_24365()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/C", prog_num=24366):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", r".", delete_extraneous_files=True, prog_num=24367) as copy_dir_to_dir_140_24367:
                            copy_dir_to_dir_140_24367()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/C", where_to_unwtar=r".", prog_num=24368) as unwtar_141_24368:
                            unwtar_141_24368()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/C", user_id=-1, group_id=-1, prog_num=24369, recursive=True) as chown_142_24369:
                            chown_142_24369()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", r"/Applications/Waves/Data/Clarity Vx/onnx/Network", skip_progress_count=4, prog_num=24370) as should_copy_source_143_24370:
                    should_copy_source_143_24370()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx/Network/F", prog_num=24371):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", r".", delete_extraneous_files=True, prog_num=24372) as copy_dir_to_dir_144_24372:
                            copy_dir_to_dir_144_24372()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx/Network/F", where_to_unwtar=r".", prog_num=24373) as unwtar_145_24373:
                            unwtar_145_24373()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx/Network/F", user_id=-1, group_id=-1, prog_num=24374, recursive=True) as chown_146_24374:
                            chown_146_24374()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=24375) as cd_stage_147_24375:
            cd_stage_147_24375()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=24376):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=24377) as should_copy_source_148_24377:
                    should_copy_source_148_24377()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=24378):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=24379) as copy_dir_to_dir_149_24379:
                            copy_dir_to_dir_149_24379()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=24380, recursive=True) as chown_150_24380:
                            chown_150_24380()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=24381) as should_copy_source_151_24381:
                    should_copy_source_151_24381()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=24382):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=24383) as copy_dir_to_dir_152_24383:
                            copy_dir_to_dir_152_24383()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=24384, recursive=True) as chown_153_24384:
                            chown_153_24384()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=24385):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=24386) as should_copy_source_154_24386:
                    should_copy_source_154_24386()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=24387):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=24388) as copy_dir_to_dir_155_24388:
                            copy_dir_to_dir_155_24388()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=24389, recursive=True) as chown_156_24389:
                            chown_156_24389()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=24390) as should_copy_source_157_24390:
                    should_copy_source_157_24390()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=24391):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=24392) as copy_dir_to_dir_158_24392:
                            copy_dir_to_dir_158_24392()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=24393, recursive=True) as chown_159_24393:
                            chown_159_24393()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=24394) as cd_stage_160_24394:
            cd_stage_160_24394()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=24395):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=24396) as should_copy_source_161_24396:
                    should_copy_source_161_24396()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=24397):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=24398) as copy_file_to_dir_162_24398:
                            copy_file_to_dir_162_24398()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=24399) as chmod_and_chown_163_24399:
                            chmod_and_chown_163_24399()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=24400) as cd_stage_164_24400:
            cd_stage_164_24400()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=24401):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24402) as should_copy_source_165_24402:
                    should_copy_source_165_24402()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=24403):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=24404) as copy_dir_to_dir_166_24404:
                            copy_dir_to_dir_166_24404()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=24405, recursive=True) as chown_167_24405:
                            chown_167_24405()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=24406):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24407) as should_copy_source_168_24407:
                    should_copy_source_168_24407()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=24408):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=24409) as copy_dir_to_dir_169_24409:
                            copy_dir_to_dir_169_24409()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=24410, recursive=True) as chown_170_24410:
                            chown_170_24410()
            with Stage(r"copy", r"Curves_AQ__Presets v1.0.0.1", prog_num=24411):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24412) as should_copy_source_171_24412:
                    should_copy_source_171_24412()
                    with Stage(r"copy source", r"Common/Data/Presets/Curves AQ", prog_num=24413):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r".", delete_extraneous_files=True, prog_num=24414) as copy_dir_to_dir_172_24414:
                            copy_dir_to_dir_172_24414()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Curves AQ", user_id=-1, group_id=-1, prog_num=24415, recursive=True) as chown_173_24415:
                            chown_173_24415()
            with Stage(r"copy", r"InTrigger Live Presets v1.0.0.4", prog_num=24416):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger Live", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24417) as should_copy_source_174_24417:
                    should_copy_source_174_24417()
                    with Stage(r"copy source", r"Common/Data/Presets/InTrigger Live", prog_num=24418):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger Live", r".", delete_extraneous_files=True, prog_num=24419) as copy_dir_to_dir_175_24419:
                            copy_dir_to_dir_175_24419()
                        with Chown(path=r"/Applications/Waves/Data/Presets/InTrigger Live", user_id=-1, group_id=-1, prog_num=24420, recursive=True) as chown_176_24420:
                            chown_176_24420()
            with Stage(r"copy", r"InTrigger Presets v1.0.0.4", prog_num=24421):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24422) as should_copy_source_177_24422:
                    should_copy_source_177_24422()
                    with Stage(r"copy source", r"Common/Data/Presets/InTrigger", prog_num=24423):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/InTrigger", r".", delete_extraneous_files=True, prog_num=24424) as copy_dir_to_dir_178_24424:
                            copy_dir_to_dir_178_24424()
                        with Chown(path=r"/Applications/Waves/Data/Presets/InTrigger", user_id=-1, group_id=-1, prog_num=24425, recursive=True) as chown_179_24425:
                            chown_179_24425()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=24426):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24427) as should_copy_source_180_24427:
                    should_copy_source_180_24427()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=24428):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=24429) as copy_dir_to_dir_181_24429:
                            copy_dir_to_dir_181_24429()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=24430, recursive=True) as chown_182_24430:
                            chown_182_24430()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=24431):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24432) as should_copy_source_183_24432:
                    should_copy_source_183_24432()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=24433):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=24434) as copy_dir_to_dir_184_24434:
                            copy_dir_to_dir_184_24434()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=24435, recursive=True) as chown_185_24435:
                            chown_185_24435()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=24436):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24437) as should_copy_source_186_24437:
                    should_copy_source_186_24437()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=24438):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=24439) as copy_dir_to_dir_187_24439:
                            copy_dir_to_dir_187_24439()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=24440, recursive=True) as chown_188_24440:
                            chown_188_24440()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=24441):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24442) as should_copy_source_189_24442:
                    should_copy_source_189_24442()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=24443):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=24444) as copy_dir_to_dir_190_24444:
                            copy_dir_to_dir_190_24444()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=24445, recursive=True) as chown_191_24445:
                            chown_191_24445()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=24446):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24447) as should_copy_source_192_24447:
                    should_copy_source_192_24447()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=24448):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=24449) as copy_dir_to_dir_193_24449:
                            copy_dir_to_dir_193_24449()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=24450, recursive=True) as chown_194_24450:
                            chown_194_24450()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=24451):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24452) as should_copy_source_195_24452:
                    should_copy_source_195_24452()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=24453):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=24454) as copy_dir_to_dir_196_24454:
                            copy_dir_to_dir_196_24454()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=24455, recursive=True) as chown_197_24455:
                            chown_197_24455()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=24456):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24457) as should_copy_source_198_24457:
                    should_copy_source_198_24457()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=24458):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=24459) as copy_dir_to_dir_199_24459:
                            copy_dir_to_dir_199_24459()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=24460, recursive=True) as chown_200_24460:
                            chown_200_24460()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=24461):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24462) as should_copy_source_201_24462:
                    should_copy_source_201_24462()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=24463):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=24464) as copy_dir_to_dir_202_24464:
                            copy_dir_to_dir_202_24464()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=24465, recursive=True) as chown_203_24465:
                            chown_203_24465()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=24466):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24467) as should_copy_source_204_24467:
                    should_copy_source_204_24467()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=24468):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=24469) as copy_dir_to_dir_205_24469:
                            copy_dir_to_dir_205_24469()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=24470, recursive=True) as chown_206_24470:
                            chown_206_24470()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=24471):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24472) as should_copy_source_207_24472:
                    should_copy_source_207_24472()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=24473):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=24474) as copy_dir_to_dir_208_24474:
                            copy_dir_to_dir_208_24474()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=24475, recursive=True) as chown_209_24475:
                            chown_209_24475()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=24476):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24477) as should_copy_source_210_24477:
                    should_copy_source_210_24477()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=24478):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=24479) as copy_dir_to_dir_211_24479:
                            copy_dir_to_dir_211_24479()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=24480, recursive=True) as chown_212_24480:
                            chown_212_24480()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=24481):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24482) as should_copy_source_213_24482:
                    should_copy_source_213_24482()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=24483):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=24484) as copy_dir_to_dir_214_24484:
                            copy_dir_to_dir_214_24484()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=24485, recursive=True) as chown_215_24485:
                            chown_215_24485()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=24486):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24487) as should_copy_source_216_24487:
                    should_copy_source_216_24487()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=24488):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=24489) as copy_dir_to_dir_217_24489:
                            copy_dir_to_dir_217_24489()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=24490, recursive=True) as chown_218_24490:
                            chown_218_24490()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=24491):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24492) as should_copy_source_219_24492:
                    should_copy_source_219_24492()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=24493):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=24494) as copy_dir_to_dir_220_24494:
                            copy_dir_to_dir_220_24494()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=24495, recursive=True) as chown_221_24495:
                            chown_221_24495()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=24496):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24497) as should_copy_source_222_24497:
                    should_copy_source_222_24497()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=24498):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=24499) as copy_dir_to_dir_223_24499:
                            copy_dir_to_dir_223_24499()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=24500, recursive=True) as chown_224_24500:
                            chown_224_24500()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=24501):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24502) as should_copy_source_225_24502:
                    should_copy_source_225_24502()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=24503):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=24504) as copy_dir_to_dir_226_24504:
                            copy_dir_to_dir_226_24504()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=24505, recursive=True) as chown_227_24505:
                            chown_227_24505()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=24506):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24507) as should_copy_source_228_24507:
                    should_copy_source_228_24507()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=24508):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=24509) as copy_dir_to_dir_229_24509:
                            copy_dir_to_dir_229_24509()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=24510, recursive=True) as chown_230_24510:
                            chown_230_24510()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=24511):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=24512) as should_copy_source_231_24512:
                    should_copy_source_231_24512()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=24513):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=24514) as copy_dir_to_dir_232_24514:
                            copy_dir_to_dir_232_24514()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=24515, recursive=True) as chown_233_24515:
                            chown_233_24515()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=24516) as cd_stage_234_24516:
            cd_stage_234_24516()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=24517):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24518) as should_copy_source_235_24518:
                    should_copy_source_235_24518()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=24519):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=24520) as copy_dir_to_dir_236_24520:
                            copy_dir_to_dir_236_24520()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=24521, recursive=True) as chown_237_24521:
                            chown_237_24521()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=24522):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24523) as should_copy_source_238_24523:
                    should_copy_source_238_24523()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=24524):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=24525) as copy_dir_to_dir_239_24525:
                            copy_dir_to_dir_239_24525()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=24526, recursive=True) as chown_240_24526:
                            chown_240_24526()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=24527):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24528) as should_copy_source_241_24528:
                    should_copy_source_241_24528()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=24529):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=24530) as copy_dir_to_dir_242_24530:
                            copy_dir_to_dir_242_24530()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=24531, recursive=True) as chown_243_24531:
                            chown_243_24531()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=24532):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24533) as should_copy_source_244_24533:
                    should_copy_source_244_24533()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=24534):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=24535) as copy_dir_to_dir_245_24535:
                            copy_dir_to_dir_245_24535()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=24536, recursive=True) as chown_246_24536:
                            chown_246_24536()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=24537):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24538) as should_copy_source_247_24538:
                    should_copy_source_247_24538()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=24539):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=24540) as copy_dir_to_dir_248_24540:
                            copy_dir_to_dir_248_24540()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=24541, recursive=True) as chown_249_24541:
                            chown_249_24541()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=24542):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24543) as should_copy_source_250_24543:
                    should_copy_source_250_24543()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=24544):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=24545) as copy_dir_to_dir_251_24545:
                            copy_dir_to_dir_251_24545()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=24546, recursive=True) as chown_252_24546:
                            chown_252_24546()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=24547):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=24548) as should_copy_source_253_24548:
                    should_copy_source_253_24548()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=24549):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=24550) as copy_dir_to_dir_254_24550:
                            copy_dir_to_dir_254_24550()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=24551, recursive=True) as chown_255_24551:
                            chown_255_24551()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=24552) as cd_stage_256_24552:
            cd_stage_256_24552()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=24553):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=24554) as should_copy_source_257_24554:
                    should_copy_source_257_24554()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=24555):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=24556) as copy_dir_to_dir_258_24556:
                            copy_dir_to_dir_258_24556()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=24557, recursive=True) as chown_259_24557:
                            chown_259_24557()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=24558):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=24559) as should_copy_source_260_24559:
                    should_copy_source_260_24559()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=24560):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=24561) as copy_dir_to_dir_261_24561:
                            copy_dir_to_dir_261_24561()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=24562, recursive=True) as chown_262_24562:
                            chown_262_24562()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=24563) as cd_stage_263_24563:
            cd_stage_263_24563()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=24564):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=24565) as should_copy_source_264_24565:
                    should_copy_source_264_24565()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=24566):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=24567) as unwtar_265_24567:
                            unwtar_265_24567()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=24568) as should_copy_source_266_24568:
                    should_copy_source_266_24568()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=24569):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=24570) as unwtar_267_24570:
                            unwtar_267_24570()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=24571) as cd_stage_268_24571:
            cd_stage_268_24571()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=24572):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=24573) as should_copy_source_269_24573:
                    should_copy_source_269_24573()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=24574):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=24575) as unwtar_270_24575:
                            unwtar_270_24575()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=24576) as cd_stage_271_24576:
            cd_stage_271_24576()
            with Stage(r"copy", r"ARPlates v16.0.23.24", prog_num=24577):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24578) as should_copy_source_272_24578:
                    should_copy_source_272_24578()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=24579):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=24580) as copy_dir_to_dir_273_24580:
                            copy_dir_to_dir_273_24580()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=24581) as unwtar_274_24581:
                            unwtar_274_24581()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=24582, recursive=True) as chown_275_24582:
                            chown_275_24582()
            with Stage(r"copy", r"Abbey Road Vinyl v16.0.23.24", prog_num=24583):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24584) as should_copy_source_276_24584:
                    should_copy_source_276_24584()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=24585):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=24586) as copy_dir_to_dir_277_24586:
                            copy_dir_to_dir_277_24586()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=24587) as unwtar_278_24587:
                            unwtar_278_24587()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=24588, recursive=True) as chown_279_24588:
                            chown_279_24588()
            with Stage(r"copy", r"Aphex AX v16.0.23.24", prog_num=24589):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24590) as should_copy_source_280_24590:
                    should_copy_source_280_24590()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=24591):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=24592) as copy_dir_to_dir_281_24592:
                            copy_dir_to_dir_281_24592()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=24593) as unwtar_282_24593:
                            unwtar_282_24593()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=24594, recursive=True) as chown_283_24594:
                            chown_283_24594()
            with Stage(r"copy", r"AudioTrack v16.0.23.24", prog_num=24595):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24596) as should_copy_source_284_24596:
                    should_copy_source_284_24596()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=24597):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=24598) as copy_dir_to_dir_285_24598:
                            copy_dir_to_dir_285_24598()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=24599) as unwtar_286_24599:
                            unwtar_286_24599()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=24600, recursive=True) as chown_287_24600:
                            chown_287_24600()
            with Stage(r"copy", r"Bass Rider v16.0.23.24", prog_num=24601):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24602) as should_copy_source_288_24602:
                    should_copy_source_288_24602()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=24603):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=24604) as copy_dir_to_dir_289_24604:
                            copy_dir_to_dir_289_24604()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=24605) as unwtar_290_24605:
                            unwtar_290_24605()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=24606, recursive=True) as chown_291_24606:
                            chown_291_24606()
            with Stage(r"copy", r"Bass Slapper v16.0.23.24", prog_num=24607):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24608) as should_copy_source_292_24608:
                    should_copy_source_292_24608()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=24609):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=24610) as copy_dir_to_dir_293_24610:
                            copy_dir_to_dir_293_24610()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=24611) as unwtar_294_24611:
                            unwtar_294_24611()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=24612, recursive=True) as chown_295_24612:
                            chown_295_24612()
            with Stage(r"copy", r"Brauer Motion v16.0.23.24", prog_num=24613):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24614) as should_copy_source_296_24614:
                    should_copy_source_296_24614()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=24615):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=24616) as copy_dir_to_dir_297_24616:
                            copy_dir_to_dir_297_24616()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=24617) as unwtar_298_24617:
                            unwtar_298_24617()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=24618, recursive=True) as chown_299_24618:
                            chown_299_24618()
            with Stage(r"copy", r"Butch Vig Vocals v16.0.23.24", prog_num=24619):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24620) as should_copy_source_300_24620:
                    should_copy_source_300_24620()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=24621):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=24622) as copy_dir_to_dir_301_24622:
                            copy_dir_to_dir_301_24622()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=24623) as unwtar_302_24623:
                            unwtar_302_24623()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=24624, recursive=True) as chown_303_24624:
                            chown_303_24624()
            with Stage(r"copy", r"C1 v16.0.23.24", prog_num=24625):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24626) as should_copy_source_304_24626:
                    should_copy_source_304_24626()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=24627):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=24628) as copy_dir_to_dir_305_24628:
                            copy_dir_to_dir_305_24628()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=24629) as unwtar_306_24629:
                            unwtar_306_24629()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C1.bundle", user_id=-1, group_id=-1, prog_num=24630, recursive=True) as chown_307_24630:
                            chown_307_24630()
            with Stage(r"copy", r"C4 v16.0.23.24", prog_num=24631):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24632) as should_copy_source_308_24632:
                    should_copy_source_308_24632()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=24633):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=24634) as copy_dir_to_dir_309_24634:
                            copy_dir_to_dir_309_24634()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=24635) as unwtar_310_24635:
                            unwtar_310_24635()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C4.bundle", user_id=-1, group_id=-1, prog_num=24636, recursive=True) as chown_311_24636:
                            chown_311_24636()
            with Stage(r"copy", r"CLA-2A v16.0.23.24", prog_num=24637):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24638) as should_copy_source_312_24638:
                    should_copy_source_312_24638()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=24639):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=24640) as copy_dir_to_dir_313_24640:
                            copy_dir_to_dir_313_24640()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=24641) as unwtar_314_24641:
                            unwtar_314_24641()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=24642, recursive=True) as chown_315_24642:
                            chown_315_24642()
            with Stage(r"copy", r"CLA-3A v16.0.23.24", prog_num=24643):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24644) as should_copy_source_316_24644:
                    should_copy_source_316_24644()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=24645):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=24646) as copy_dir_to_dir_317_24646:
                            copy_dir_to_dir_317_24646()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=24647) as unwtar_318_24647:
                            unwtar_318_24647()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=24648, recursive=True) as chown_319_24648:
                            chown_319_24648()
            with Stage(r"copy", r"CLA-76 v16.0.23.24", prog_num=24649):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24650) as should_copy_source_320_24650:
                    should_copy_source_320_24650()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=24651):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=24652) as copy_dir_to_dir_321_24652:
                            copy_dir_to_dir_321_24652()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=24653) as unwtar_322_24653:
                            unwtar_322_24653()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=24654, recursive=True) as chown_323_24654:
                            chown_323_24654()
            with Stage(r"copy", r"CLA Bass v16.0.23.24", prog_num=24655):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24656) as should_copy_source_324_24656:
                    should_copy_source_324_24656()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=24657):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=24658) as copy_dir_to_dir_325_24658:
                            copy_dir_to_dir_325_24658()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=24659) as unwtar_326_24659:
                            unwtar_326_24659()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=24660, recursive=True) as chown_327_24660:
                            chown_327_24660()
            with Stage(r"copy", r"CLA Drums v16.0.23.24", prog_num=24661):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24662) as should_copy_source_328_24662:
                    should_copy_source_328_24662()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Drums.bundle", prog_num=24663):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r".", delete_extraneous_files=True, prog_num=24664) as copy_dir_to_dir_329_24664:
                            copy_dir_to_dir_329_24664()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", where_to_unwtar=r".", prog_num=24665) as unwtar_330_24665:
                            unwtar_330_24665()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Drums.bundle", user_id=-1, group_id=-1, prog_num=24666, recursive=True) as chown_331_24666:
                            chown_331_24666()
            with Stage(r"copy", r"CLA Effects v16.0.23.24", prog_num=24667):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24668) as should_copy_source_332_24668:
                    should_copy_source_332_24668()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Effects.bundle", prog_num=24669):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r".", delete_extraneous_files=True, prog_num=24670) as copy_dir_to_dir_333_24670:
                            copy_dir_to_dir_333_24670()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", where_to_unwtar=r".", prog_num=24671) as unwtar_334_24671:
                            unwtar_334_24671()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Effects.bundle", user_id=-1, group_id=-1, prog_num=24672, recursive=True) as chown_335_24672:
                            chown_335_24672()
            with Stage(r"copy", r"CLA Guitars v16.0.23.24", prog_num=24673):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24674) as should_copy_source_336_24674:
                    should_copy_source_336_24674()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=24675):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=24676) as copy_dir_to_dir_337_24676:
                            copy_dir_to_dir_337_24676()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=24677) as unwtar_338_24677:
                            unwtar_338_24677()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=24678, recursive=True) as chown_339_24678:
                            chown_339_24678()
            with Stage(r"copy", r"CLA Unplugged v16.0.23.24", prog_num=24679):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24680) as should_copy_source_340_24680:
                    should_copy_source_340_24680()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=24681):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=24682) as copy_dir_to_dir_341_24682:
                            copy_dir_to_dir_341_24682()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=24683) as unwtar_342_24683:
                            unwtar_342_24683()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=24684, recursive=True) as chown_343_24684:
                            chown_343_24684()
            with Stage(r"copy", r"CLA Vocals v16.0.23.24", prog_num=24685):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24686) as should_copy_source_344_24686:
                    should_copy_source_344_24686()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=24687):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=24688) as copy_dir_to_dir_345_24688:
                            copy_dir_to_dir_345_24688()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=24689) as unwtar_346_24689:
                            unwtar_346_24689()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=24690, recursive=True) as chown_347_24690:
                            chown_347_24690()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=24691):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24692) as should_copy_source_348_24692:
                    should_copy_source_348_24692()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=24693):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=24694) as copy_dir_to_dir_349_24694:
                            copy_dir_to_dir_349_24694()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=24695) as unwtar_350_24695:
                            unwtar_350_24695()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=24696, recursive=True) as chown_351_24696:
                            chown_351_24696()
            with Stage(r"copy", r"Curves AQ v16.0.23.24", prog_num=24697):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24698) as should_copy_source_352_24698:
                    should_copy_source_352_24698()
                    with Stage(r"copy source", r"Mac/Plugins/Curves AQ.bundle", prog_num=24699):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r".", delete_extraneous_files=True, prog_num=24700) as copy_dir_to_dir_353_24700:
                            copy_dir_to_dir_353_24700()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", where_to_unwtar=r".", prog_num=24701) as unwtar_354_24701:
                            unwtar_354_24701()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Curves AQ.bundle", user_id=-1, group_id=-1, prog_num=24702, recursive=True) as chown_355_24702:
                            chown_355_24702()
            with Stage(r"copy", r"Center v16.0.23.24", prog_num=24703):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24704) as should_copy_source_356_24704:
                    should_copy_source_356_24704()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=24705):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=24706) as copy_dir_to_dir_357_24706:
                            copy_dir_to_dir_357_24706()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=24707) as unwtar_358_24707:
                            unwtar_358_24707()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Center.bundle", user_id=-1, group_id=-1, prog_num=24708, recursive=True) as chown_359_24708:
                            chown_359_24708()
            with Stage(r"copy", r"Clarity Vx v16.2.30.56", prog_num=24709):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24710) as should_copy_source_360_24710:
                    should_copy_source_360_24710()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=24711):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=24712) as copy_dir_to_dir_361_24712:
                            copy_dir_to_dir_361_24712()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=24713) as unwtar_362_24713:
                            unwtar_362_24713()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=24714, recursive=True) as chown_363_24714:
                            chown_363_24714()
            with Stage(r"copy", r"Saphira v16.0.23.24", prog_num=24715):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24716) as should_copy_source_364_24716:
                    should_copy_source_364_24716()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=24717):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=24718) as copy_dir_to_dir_365_24718:
                            copy_dir_to_dir_365_24718()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=24719) as unwtar_366_24719:
                            unwtar_366_24719()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Saphira.bundle", user_id=-1, group_id=-1, prog_num=24720, recursive=True) as chown_367_24720:
                            chown_367_24720()
            with Stage(r"copy", r"Submarine v16.0.23.24", prog_num=24721):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24722) as should_copy_source_368_24722:
                    should_copy_source_368_24722()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=24723):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=24724) as copy_dir_to_dir_369_24724:
                            copy_dir_to_dir_369_24724()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=24725) as unwtar_370_24725:
                            unwtar_370_24725()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Submarine.bundle", user_id=-1, group_id=-1, prog_num=24726, recursive=True) as chown_371_24726:
                            chown_371_24726()
            with Stage(r"copy", r"DeBreath v16.0.23.24", prog_num=24727):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24728) as should_copy_source_372_24728:
                    should_copy_source_372_24728()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=24729):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=24730) as copy_dir_to_dir_373_24730:
                            copy_dir_to_dir_373_24730()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=24731) as unwtar_374_24731:
                            unwtar_374_24731()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=24732, recursive=True) as chown_375_24732:
                            chown_375_24732()
            with Stage(r"copy", r"DeEsser v16.0.23.24", prog_num=24733):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24734) as should_copy_source_376_24734:
                    should_copy_source_376_24734()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=24735):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=24736) as copy_dir_to_dir_377_24736:
                            copy_dir_to_dir_377_24736()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=24737) as unwtar_378_24737:
                            unwtar_378_24737()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=24738, recursive=True) as chown_379_24738:
                            chown_379_24738()
            with Stage(r"copy", r"Doppler v16.0.23.24", prog_num=24739):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24740) as should_copy_source_380_24740:
                    should_copy_source_380_24740()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=24741):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=24742) as copy_dir_to_dir_381_24742:
                            copy_dir_to_dir_381_24742()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=24743) as unwtar_382_24743:
                            unwtar_382_24743()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doppler.bundle", user_id=-1, group_id=-1, prog_num=24744, recursive=True) as chown_383_24744:
                            chown_383_24744()
            with Stage(r"copy", r"Doubler v16.0.23.24", prog_num=24745):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24746) as should_copy_source_384_24746:
                    should_copy_source_384_24746()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=24747):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=24748) as copy_dir_to_dir_385_24748:
                            copy_dir_to_dir_385_24748()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=24749) as unwtar_386_24749:
                            unwtar_386_24749()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doubler.bundle", user_id=-1, group_id=-1, prog_num=24750, recursive=True) as chown_387_24750:
                            chown_387_24750()
            with Stage(r"copy", r"EMO-F2 v16.0.23.24", prog_num=24751):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24752) as should_copy_source_388_24752:
                    should_copy_source_388_24752()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=24753):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=24754) as copy_dir_to_dir_389_24754:
                            copy_dir_to_dir_389_24754()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=24755) as unwtar_390_24755:
                            unwtar_390_24755()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=24756, recursive=True) as chown_391_24756:
                            chown_391_24756()
            with Stage(r"copy", r"EMO-Q4 v16.0.23.24", prog_num=24757):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24758) as should_copy_source_392_24758:
                    should_copy_source_392_24758()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=24759):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=24760) as copy_dir_to_dir_393_24760:
                            copy_dir_to_dir_393_24760()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=24761) as unwtar_394_24761:
                            unwtar_394_24761()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=24762, recursive=True) as chown_395_24762:
                            chown_395_24762()
            with Stage(r"copy", r"EddieKramer DR v16.0.23.24", prog_num=24763):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24764) as should_copy_source_396_24764:
                    should_copy_source_396_24764()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=24765):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=24766) as copy_dir_to_dir_397_24766:
                            copy_dir_to_dir_397_24766()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=24767) as unwtar_398_24767:
                            unwtar_398_24767()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=24768, recursive=True) as chown_399_24768:
                            chown_399_24768()
            with Stage(r"copy", r"EddieKramer VC v16.0.23.24", prog_num=24769):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24770) as should_copy_source_400_24770:
                    should_copy_source_400_24770()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=24771):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=24772) as copy_dir_to_dir_401_24772:
                            copy_dir_to_dir_401_24772()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=24773) as unwtar_402_24773:
                            unwtar_402_24773()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=24774, recursive=True) as chown_403_24774:
                            chown_403_24774()
            with Stage(r"copy", r"Electric Grand 80 v16.0.23.24", prog_num=24775):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24776) as should_copy_source_404_24776:
                    should_copy_source_404_24776()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=24777):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=24778) as copy_dir_to_dir_405_24778:
                            copy_dir_to_dir_405_24778()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=24779) as unwtar_406_24779:
                            unwtar_406_24779()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=24780, recursive=True) as chown_407_24780:
                            chown_407_24780()
            with Stage(r"copy", r"Enigma v16.0.23.24", prog_num=24781):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24782) as should_copy_source_408_24782:
                    should_copy_source_408_24782()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=24783):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=24784) as copy_dir_to_dir_409_24784:
                            copy_dir_to_dir_409_24784()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=24785) as unwtar_410_24785:
                            unwtar_410_24785()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Enigma.bundle", user_id=-1, group_id=-1, prog_num=24786, recursive=True) as chown_411_24786:
                            chown_411_24786()
            with Stage(r"copy", r"GTRAmp v16.0.23.24", prog_num=24787):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24788) as should_copy_source_412_24788:
                    should_copy_source_412_24788()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=24789):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=24790) as copy_dir_to_dir_413_24790:
                            copy_dir_to_dir_413_24790()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=24791) as unwtar_414_24791:
                            unwtar_414_24791()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=24792, recursive=True) as chown_415_24792:
                            chown_415_24792()
            with Stage(r"copy", r"GTRStomp v16.0.23.24", prog_num=24793):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24794) as should_copy_source_416_24794:
                    should_copy_source_416_24794()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=24795):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=24796) as copy_dir_to_dir_417_24796:
                            copy_dir_to_dir_417_24796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=24797) as unwtar_418_24797:
                            unwtar_418_24797()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=24798, recursive=True) as chown_419_24798:
                            chown_419_24798()
            with Stage(r"copy", r"GTRToolRack v16.0.23.24", prog_num=24799):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24800) as should_copy_source_420_24800:
                    should_copy_source_420_24800()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=24801):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=24802) as copy_dir_to_dir_421_24802:
                            copy_dir_to_dir_421_24802()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=24803) as unwtar_422_24803:
                            unwtar_422_24803()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=24804, recursive=True) as chown_423_24804:
                            chown_423_24804()
            with Stage(r"copy", r"GTRTuner v16.0.23.24", prog_num=24805):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24806) as should_copy_source_424_24806:
                    should_copy_source_424_24806()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=24807):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=24808) as copy_dir_to_dir_425_24808:
                            copy_dir_to_dir_425_24808()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=24809) as unwtar_426_24809:
                            unwtar_426_24809()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=24810, recursive=True) as chown_427_24810:
                            chown_427_24810()
            with Stage(r"copy", r"Greg Wells MixCentric v16.0.23.24", prog_num=24811):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24812) as should_copy_source_428_24812:
                    should_copy_source_428_24812()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=24813):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=24814) as copy_dir_to_dir_429_24814:
                            copy_dir_to_dir_429_24814()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=24815) as unwtar_430_24815:
                            unwtar_430_24815()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=24816, recursive=True) as chown_431_24816:
                            chown_431_24816()
            with Stage(r"copy", r"Greg Wells PianoCentric v16.0.23.24", prog_num=24817):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24818) as should_copy_source_432_24818:
                    should_copy_source_432_24818()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=24819):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=24820) as copy_dir_to_dir_433_24820:
                            copy_dir_to_dir_433_24820()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=24821) as unwtar_434_24821:
                            unwtar_434_24821()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=24822, recursive=True) as chown_435_24822:
                            chown_435_24822()
            with Stage(r"copy", r"Greg Wells ToneCentric v16.0.23.24", prog_num=24823):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24824) as should_copy_source_436_24824:
                    should_copy_source_436_24824()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=24825):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=24826) as copy_dir_to_dir_437_24826:
                            copy_dir_to_dir_437_24826()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=24827) as unwtar_438_24827:
                            unwtar_438_24827()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=24828, recursive=True) as chown_439_24828:
                            chown_439_24828()
            with Stage(r"copy", r"H-Comp v16.0.23.24", prog_num=24829):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24830) as should_copy_source_440_24830:
                    should_copy_source_440_24830()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=24831):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=24832) as copy_dir_to_dir_441_24832:
                            copy_dir_to_dir_441_24832()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=24833) as unwtar_442_24833:
                            unwtar_442_24833()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=24834, recursive=True) as chown_443_24834:
                            chown_443_24834()
            with Stage(r"copy", r"H-Delay v16.0.23.24", prog_num=24835):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24836) as should_copy_source_444_24836:
                    should_copy_source_444_24836()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=24837):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=24838) as copy_dir_to_dir_445_24838:
                            copy_dir_to_dir_445_24838()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=24839) as unwtar_446_24839:
                            unwtar_446_24839()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=24840, recursive=True) as chown_447_24840:
                            chown_447_24840()
            with Stage(r"copy", r"H-Reverb v16.0.23.24", prog_num=24841):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24842) as should_copy_source_448_24842:
                    should_copy_source_448_24842()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=24843):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=24844) as copy_dir_to_dir_449_24844:
                            copy_dir_to_dir_449_24844()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=24845) as unwtar_450_24845:
                            unwtar_450_24845()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=24846, recursive=True) as chown_451_24846:
                            chown_451_24846()
            with Stage(r"copy", r"IR-360 v16.0.91.92", prog_num=24847):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24848) as should_copy_source_452_24848:
                    should_copy_source_452_24848()
                    with Stage(r"copy source", r"Mac/Plugins/IR-360.bundle", prog_num=24849):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r".", delete_extraneous_files=True, prog_num=24850) as copy_dir_to_dir_453_24850:
                            copy_dir_to_dir_453_24850()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", where_to_unwtar=r".", prog_num=24851) as unwtar_454_24851:
                            unwtar_454_24851()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-360.bundle", user_id=-1, group_id=-1, prog_num=24852, recursive=True) as chown_455_24852:
                            chown_455_24852()
            with Stage(r"copy", r"IR-L v16.0.23.24", prog_num=24853):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24854) as should_copy_source_456_24854:
                    should_copy_source_456_24854()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=24855):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=24856) as copy_dir_to_dir_457_24856:
                            copy_dir_to_dir_457_24856()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=24857) as unwtar_458_24857:
                            unwtar_458_24857()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-L.bundle", user_id=-1, group_id=-1, prog_num=24858, recursive=True) as chown_459_24858:
                            chown_459_24858()
            with Stage(r"copy", r"InPhase v16.0.23.24", prog_num=24859):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24860) as should_copy_source_460_24860:
                    should_copy_source_460_24860()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=24861):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=24862) as copy_dir_to_dir_461_24862:
                            copy_dir_to_dir_461_24862()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=24863) as unwtar_462_24863:
                            unwtar_462_24863()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase.bundle", user_id=-1, group_id=-1, prog_num=24864, recursive=True) as chown_463_24864:
                            chown_463_24864()
            with Stage(r"copy", r"InPhase LT v16.0.23.24", prog_num=24865):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24866) as should_copy_source_464_24866:
                    should_copy_source_464_24866()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=24867):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=24868) as copy_dir_to_dir_465_24868:
                            copy_dir_to_dir_465_24868()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=24869) as unwtar_466_24869:
                            unwtar_466_24869()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=24870, recursive=True) as chown_467_24870:
                            chown_467_24870()
            with Stage(r"copy", r"InTrigger v16.1.99.101", prog_num=24871):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24872) as should_copy_source_468_24872:
                    should_copy_source_468_24872()
                    with Stage(r"copy source", r"Mac/Plugins/InTrigger.bundle", prog_num=24873):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", r".", delete_extraneous_files=True, prog_num=24874) as copy_dir_to_dir_469_24874:
                            copy_dir_to_dir_469_24874()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger.bundle", where_to_unwtar=r".", prog_num=24875) as unwtar_470_24875:
                            unwtar_470_24875()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InTrigger.bundle", user_id=-1, group_id=-1, prog_num=24876, recursive=True) as chown_471_24876:
                            chown_471_24876()
            with Stage(r"copy", r"InTrigger Live v16.1.99.101", prog_num=24877):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24878) as should_copy_source_472_24878:
                    should_copy_source_472_24878()
                    with Stage(r"copy source", r"Mac/Plugins/InTrigger Live.bundle", prog_num=24879):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", r".", delete_extraneous_files=True, prog_num=24880) as copy_dir_to_dir_473_24880:
                            copy_dir_to_dir_473_24880()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InTrigger Live.bundle", where_to_unwtar=r".", prog_num=24881) as unwtar_474_24881:
                            unwtar_474_24881()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InTrigger Live.bundle", user_id=-1, group_id=-1, prog_num=24882, recursive=True) as chown_475_24882:
                            chown_475_24882()
            with Stage(r"copy", r"J37 v16.0.23.24", prog_num=24883):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24884) as should_copy_source_476_24884:
                    should_copy_source_476_24884()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=24885):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=24886) as copy_dir_to_dir_477_24886:
                            copy_dir_to_dir_477_24886()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=24887) as unwtar_478_24887:
                            unwtar_478_24887()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/J37.bundle", user_id=-1, group_id=-1, prog_num=24888, recursive=True) as chown_479_24888:
                            chown_479_24888()
            with Stage(r"copy", r"JJP-Vocals v16.0.23.24", prog_num=24889):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24890) as should_copy_source_480_24890:
                    should_copy_source_480_24890()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=24891):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=24892) as copy_dir_to_dir_481_24892:
                            copy_dir_to_dir_481_24892()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=24893) as unwtar_482_24893:
                            unwtar_482_24893()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=24894, recursive=True) as chown_483_24894:
                            chown_483_24894()
            with Stage(r"copy", r"Key Detector v16.0.23.24", prog_num=24895):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24896) as should_copy_source_484_24896:
                    should_copy_source_484_24896()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=24897):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=24898) as copy_dir_to_dir_485_24898:
                            copy_dir_to_dir_485_24898()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=24899) as unwtar_486_24899:
                            unwtar_486_24899()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=24900, recursive=True) as chown_487_24900:
                            chown_487_24900()
            with Stage(r"copy", r"KingsMic v16.0.23.24", prog_num=24901):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24902) as should_copy_source_488_24902:
                    should_copy_source_488_24902()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=24903):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=24904) as copy_dir_to_dir_489_24904:
                            copy_dir_to_dir_489_24904()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=24905) as unwtar_490_24905:
                            unwtar_490_24905()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=24906, recursive=True) as chown_491_24906:
                            chown_491_24906()
            with Stage(r"copy", r"KramerHLS v16.0.23.24", prog_num=24907):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24908) as should_copy_source_492_24908:
                    should_copy_source_492_24908()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=24909):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=24910) as copy_dir_to_dir_493_24910:
                            copy_dir_to_dir_493_24910()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=24911) as unwtar_494_24911:
                            unwtar_494_24911()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=24912, recursive=True) as chown_495_24912:
                            chown_495_24912()
            with Stage(r"copy", r"KramerPIE v16.0.23.24", prog_num=24913):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24914) as should_copy_source_496_24914:
                    should_copy_source_496_24914()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=24915):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=24916) as copy_dir_to_dir_497_24916:
                            copy_dir_to_dir_497_24916()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=24917) as unwtar_498_24917:
                            unwtar_498_24917()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=24918, recursive=True) as chown_499_24918:
                            chown_499_24918()
            with Stage(r"copy", r"KramerTape v16.0.23.24", prog_num=24919):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24920) as should_copy_source_500_24920:
                    should_copy_source_500_24920()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=24921):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=24922) as copy_dir_to_dir_501_24922:
                            copy_dir_to_dir_501_24922()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=24923) as unwtar_502_24923:
                            unwtar_502_24923()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=24924, recursive=True) as chown_503_24924:
                            chown_503_24924()
            with Stage(r"copy", r"L1 v16.0.23.24", prog_num=24925):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24926) as should_copy_source_504_24926:
                    should_copy_source_504_24926()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=24927):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=24928) as copy_dir_to_dir_505_24928:
                            copy_dir_to_dir_505_24928()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=24929) as unwtar_506_24929:
                            unwtar_506_24929()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L1.bundle", user_id=-1, group_id=-1, prog_num=24930, recursive=True) as chown_507_24930:
                            chown_507_24930()
            with Stage(r"copy", r"L2 v16.0.23.24", prog_num=24931):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24932) as should_copy_source_508_24932:
                    should_copy_source_508_24932()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=24933):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=24934) as copy_dir_to_dir_509_24934:
                            copy_dir_to_dir_509_24934()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=24935) as unwtar_510_24935:
                            unwtar_510_24935()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L2.bundle", user_id=-1, group_id=-1, prog_num=24936, recursive=True) as chown_511_24936:
                            chown_511_24936()
            with Stage(r"copy", r"L3-16 v16.0.23.24", prog_num=24937):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24938) as should_copy_source_512_24938:
                    should_copy_source_512_24938()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=24939):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=24940) as copy_dir_to_dir_513_24940:
                            copy_dir_to_dir_513_24940()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=24941) as unwtar_514_24941:
                            unwtar_514_24941()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-16.bundle", user_id=-1, group_id=-1, prog_num=24942, recursive=True) as chown_515_24942:
                            chown_515_24942()
            with Stage(r"copy", r"L3-LL Multi v16.0.23.24", prog_num=24943):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24944) as should_copy_source_516_24944:
                    should_copy_source_516_24944()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=24945):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=24946) as copy_dir_to_dir_517_24946:
                            copy_dir_to_dir_517_24946()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=24947) as unwtar_518_24947:
                            unwtar_518_24947()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=24948, recursive=True) as chown_519_24948:
                            chown_519_24948()
            with Stage(r"copy", r"L3-LL Ultra v16.0.23.24", prog_num=24949):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24950) as should_copy_source_520_24950:
                    should_copy_source_520_24950()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=24951):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=24952) as copy_dir_to_dir_521_24952:
                            copy_dir_to_dir_521_24952()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=24953) as unwtar_522_24953:
                            unwtar_522_24953()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=24954, recursive=True) as chown_523_24954:
                            chown_523_24954()
            with Stage(r"copy", r"L3 Multi v16.0.23.24", prog_num=24955):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24956) as should_copy_source_524_24956:
                    should_copy_source_524_24956()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=24957):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=24958) as copy_dir_to_dir_525_24958:
                            copy_dir_to_dir_525_24958()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=24959) as unwtar_526_24959:
                            unwtar_526_24959()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=24960, recursive=True) as chown_527_24960:
                            chown_527_24960()
            with Stage(r"copy", r"L3 Ultra v16.0.23.24", prog_num=24961):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24962) as should_copy_source_528_24962:
                    should_copy_source_528_24962()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=24963):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=24964) as copy_dir_to_dir_529_24964:
                            copy_dir_to_dir_529_24964()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=24965) as unwtar_530_24965:
                            unwtar_530_24965()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=24966, recursive=True) as chown_531_24966:
                            chown_531_24966()
            with Stage(r"copy", r"LinEQ v16.0.23.24", prog_num=24967):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24968) as should_copy_source_532_24968:
                    should_copy_source_532_24968()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=24969):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=24970) as copy_dir_to_dir_533_24970:
                            copy_dir_to_dir_533_24970()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=24971) as unwtar_534_24971:
                            unwtar_534_24971()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=24972, recursive=True) as chown_535_24972:
                            chown_535_24972()
            with Stage(r"copy", r"LinMB v16.0.23.24", prog_num=24973):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24974) as should_copy_source_536_24974:
                    should_copy_source_536_24974()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=24975):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=24976) as copy_dir_to_dir_537_24976:
                            copy_dir_to_dir_537_24976()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=24977) as unwtar_538_24977:
                            unwtar_538_24977()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinMB.bundle", user_id=-1, group_id=-1, prog_num=24978, recursive=True) as chown_539_24978:
                            chown_539_24978()
            with Stage(r"copy", r"LoAir v16.0.91.92", prog_num=24979):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24980) as should_copy_source_540_24980:
                    should_copy_source_540_24980()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=24981):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=24982) as copy_dir_to_dir_541_24982:
                            copy_dir_to_dir_541_24982()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=24983) as unwtar_542_24983:
                            unwtar_542_24983()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LoAir.bundle", user_id=-1, group_id=-1, prog_num=24984, recursive=True) as chown_543_24984:
                            chown_543_24984()
            with Stage(r"copy", r"Lofi Space v16.0.23.24", prog_num=24985):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24986) as should_copy_source_544_24986:
                    should_copy_source_544_24986()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=24987):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=24988) as copy_dir_to_dir_545_24988:
                            copy_dir_to_dir_545_24988()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=24989) as unwtar_546_24989:
                            unwtar_546_24989()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=24990, recursive=True) as chown_547_24990:
                            chown_547_24990()
            with Stage(r"copy", r"MV2 v16.0.23.24", prog_num=24991):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24992) as should_copy_source_548_24992:
                    should_copy_source_548_24992()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=24993):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=24994) as copy_dir_to_dir_549_24994:
                            copy_dir_to_dir_549_24994()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=24995) as unwtar_550_24995:
                            unwtar_550_24995()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV2.bundle", user_id=-1, group_id=-1, prog_num=24996, recursive=True) as chown_551_24996:
                            chown_551_24996()
            with Stage(r"copy", r"Magma Springs v16.0.23.24", prog_num=24997):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=24998) as should_copy_source_552_24998:
                    should_copy_source_552_24998()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=24999):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=25000) as copy_dir_to_dir_553_25000:
                            copy_dir_to_dir_553_25000()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=25001) as unwtar_554_25001:
                            unwtar_554_25001()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=25002, recursive=True) as chown_555_25002:
                            chown_555_25002()
            with Stage(r"copy", r"MannyM-TripleD v16.0.23.24", prog_num=25003):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25004) as should_copy_source_556_25004:
                    should_copy_source_556_25004()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=25005):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=25006) as copy_dir_to_dir_557_25006:
                            copy_dir_to_dir_557_25006()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=25007) as unwtar_558_25007:
                            unwtar_558_25007()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=25008, recursive=True) as chown_559_25008:
                            chown_559_25008()
            with Stage(r"copy", r"Maserati DRM v16.0.23.24", prog_num=25009):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25010) as should_copy_source_560_25010:
                    should_copy_source_560_25010()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=25011):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=25012) as copy_dir_to_dir_561_25012:
                            copy_dir_to_dir_561_25012()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=25013) as unwtar_562_25013:
                            unwtar_562_25013()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=25014, recursive=True) as chown_563_25014:
                            chown_563_25014()
            with Stage(r"copy", r"Maserati VX1 v16.0.23.24", prog_num=25015):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25016) as should_copy_source_564_25016:
                    should_copy_source_564_25016()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=25017):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=25018) as copy_dir_to_dir_565_25018:
                            copy_dir_to_dir_565_25018()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=25019) as unwtar_566_25019:
                            unwtar_566_25019()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=25020, recursive=True) as chown_567_25020:
                            chown_567_25020()
            with Stage(r"copy", r"MaxxBass v16.0.30.31", prog_num=25021):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25022) as should_copy_source_568_25022:
                    should_copy_source_568_25022()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=25023):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=25024) as copy_dir_to_dir_569_25024:
                            copy_dir_to_dir_569_25024()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=25025) as unwtar_570_25025:
                            unwtar_570_25025()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=25026, recursive=True) as chown_571_25026:
                            chown_571_25026()
            with Stage(r"copy", r"MaxxVolume v16.0.23.24", prog_num=25027):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25028) as should_copy_source_572_25028:
                    should_copy_source_572_25028()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=25029):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=25030) as copy_dir_to_dir_573_25030:
                            copy_dir_to_dir_573_25030()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=25031) as unwtar_574_25031:
                            unwtar_574_25031()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=25032, recursive=True) as chown_575_25032:
                            chown_575_25032()
            with Stage(r"copy", r"MetaFilter v16.0.23.24", prog_num=25033):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25034) as should_copy_source_576_25034:
                    should_copy_source_576_25034()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=25035):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=25036) as copy_dir_to_dir_577_25036:
                            copy_dir_to_dir_577_25036()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=25037) as unwtar_578_25037:
                            unwtar_578_25037()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=25038, recursive=True) as chown_579_25038:
                            chown_579_25038()
            with Stage(r"copy", r"MetaFlanger v16.0.23.24", prog_num=25039):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25040) as should_copy_source_580_25040:
                    should_copy_source_580_25040()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=25041):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=25042) as copy_dir_to_dir_581_25042:
                            copy_dir_to_dir_581_25042()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=25043) as unwtar_582_25043:
                            unwtar_582_25043()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=25044, recursive=True) as chown_583_25044:
                            chown_583_25044()
            with Stage(r"copy", r"MondoMod v16.0.23.24", prog_num=25045):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25046) as should_copy_source_584_25046:
                    should_copy_source_584_25046()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=25047):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=25048) as copy_dir_to_dir_585_25048:
                            copy_dir_to_dir_585_25048()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=25049) as unwtar_586_25049:
                            unwtar_586_25049()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=25050, recursive=True) as chown_587_25050:
                            chown_587_25050()
            with Stage(r"copy", r"Morphoder v16.0.23.24", prog_num=25051):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25052) as should_copy_source_588_25052:
                    should_copy_source_588_25052()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=25053):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=25054) as copy_dir_to_dir_589_25054:
                            copy_dir_to_dir_589_25054()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=25055) as unwtar_590_25055:
                            unwtar_590_25055()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=25056, recursive=True) as chown_591_25056:
                            chown_591_25056()
            with Stage(r"copy", r"NLS v16.0.23.24", prog_num=25057):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25058) as should_copy_source_592_25058:
                    should_copy_source_592_25058()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=25059):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=25060) as copy_dir_to_dir_593_25060:
                            copy_dir_to_dir_593_25060()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=25061) as unwtar_594_25061:
                            unwtar_594_25061()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NLS.bundle", user_id=-1, group_id=-1, prog_num=25062, recursive=True) as chown_595_25062:
                            chown_595_25062()
            with Stage(r"copy", r"NX v16.0.91.92", prog_num=25063):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25064) as should_copy_source_596_25064:
                    should_copy_source_596_25064()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=25065):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=25066) as copy_dir_to_dir_597_25066:
                            copy_dir_to_dir_597_25066()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=25067) as unwtar_598_25067:
                            unwtar_598_25067()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NX.bundle", user_id=-1, group_id=-1, prog_num=25068, recursive=True) as chown_599_25068:
                            chown_599_25068()
            with Stage(r"copy", r"OKDriver v16.0.23.24", prog_num=25069):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25070) as should_copy_source_600_25070:
                    should_copy_source_600_25070()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=25071):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=25072) as copy_dir_to_dir_601_25072:
                            copy_dir_to_dir_601_25072()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=25073) as unwtar_602_25073:
                            unwtar_602_25073()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=25074, recursive=True) as chown_603_25074:
                            chown_603_25074()
            with Stage(r"copy", r"OKFilter v16.0.23.24", prog_num=25075):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25076) as should_copy_source_604_25076:
                    should_copy_source_604_25076()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=25077):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=25078) as copy_dir_to_dir_605_25078:
                            copy_dir_to_dir_605_25078()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=25079) as unwtar_606_25079:
                            unwtar_606_25079()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=25080, recursive=True) as chown_607_25080:
                            chown_607_25080()
            with Stage(r"copy", r"OKPhatter v16.0.23.24", prog_num=25081):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25082) as should_copy_source_608_25082:
                    should_copy_source_608_25082()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=25083):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=25084) as copy_dir_to_dir_609_25084:
                            copy_dir_to_dir_609_25084()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=25085) as unwtar_610_25085:
                            unwtar_610_25085()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=25086, recursive=True) as chown_611_25086:
                            chown_611_25086()
            with Stage(r"copy", r"OKPumper v16.0.23.24", prog_num=25087):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25088) as should_copy_source_612_25088:
                    should_copy_source_612_25088()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=25089):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=25090) as copy_dir_to_dir_613_25090:
                            copy_dir_to_dir_613_25090()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=25091) as unwtar_614_25091:
                            unwtar_614_25091()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=25092, recursive=True) as chown_615_25092:
                            chown_615_25092()
            with Stage(r"copy", r"PAZ v16.0.23.24", prog_num=25093):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25094) as should_copy_source_616_25094:
                    should_copy_source_616_25094()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=25095):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=25096) as copy_dir_to_dir_617_25096:
                            copy_dir_to_dir_617_25096()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=25097) as unwtar_618_25097:
                            unwtar_618_25097()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PAZ.bundle", user_id=-1, group_id=-1, prog_num=25098, recursive=True) as chown_619_25098:
                            chown_619_25098()
            with Stage(r"copy", r"PS22 v16.0.23.24", prog_num=25099):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25100) as should_copy_source_620_25100:
                    should_copy_source_620_25100()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=25101):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=25102) as copy_dir_to_dir_621_25102:
                            copy_dir_to_dir_621_25102()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=25103) as unwtar_622_25103:
                            unwtar_622_25103()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PS22.bundle", user_id=-1, group_id=-1, prog_num=25104, recursive=True) as chown_623_25104:
                            chown_623_25104()
            with Stage(r"copy", r"PuigChild v16.0.23.24", prog_num=25105):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25106) as should_copy_source_624_25106:
                    should_copy_source_624_25106()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=25107):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=25108) as copy_dir_to_dir_625_25108:
                            copy_dir_to_dir_625_25108()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=25109) as unwtar_626_25109:
                            unwtar_626_25109()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=25110, recursive=True) as chown_627_25110:
                            chown_627_25110()
            with Stage(r"copy", r"PuigTec v16.0.23.24", prog_num=25111):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25112) as should_copy_source_628_25112:
                    should_copy_source_628_25112()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=25113):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=25114) as copy_dir_to_dir_629_25114:
                            copy_dir_to_dir_629_25114()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=25115) as unwtar_630_25115:
                            unwtar_630_25115()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=25116, recursive=True) as chown_631_25116:
                            chown_631_25116()
            with Stage(r"copy", r"Q10 v16.0.23.24", prog_num=25117):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25118) as should_copy_source_632_25118:
                    should_copy_source_632_25118()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=25119):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=25120) as copy_dir_to_dir_633_25120:
                            copy_dir_to_dir_633_25120()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=25121) as unwtar_634_25121:
                            unwtar_634_25121()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q10.bundle", user_id=-1, group_id=-1, prog_num=25122, recursive=True) as chown_635_25122:
                            chown_635_25122()
            with Stage(r"copy", r"Q-Clone v16.0.23.24", prog_num=25123):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25124) as should_copy_source_636_25124:
                    should_copy_source_636_25124()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=25125):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=25126) as copy_dir_to_dir_637_25126:
                            copy_dir_to_dir_637_25126()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=25127) as unwtar_638_25127:
                            unwtar_638_25127()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=25128, recursive=True) as chown_639_25128:
                            chown_639_25128()
            with Stage(r"copy", r"RBass v16.0.23.24", prog_num=25129):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25130) as should_copy_source_640_25130:
                    should_copy_source_640_25130()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=25131):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=25132) as copy_dir_to_dir_641_25132:
                            copy_dir_to_dir_641_25132()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=25133) as unwtar_642_25133:
                            unwtar_642_25133()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RBass.bundle", user_id=-1, group_id=-1, prog_num=25134, recursive=True) as chown_643_25134:
                            chown_643_25134()
            with Stage(r"copy", r"RChannel v16.0.23.24", prog_num=25135):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25136) as should_copy_source_644_25136:
                    should_copy_source_644_25136()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=25137):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=25138) as copy_dir_to_dir_645_25138:
                            copy_dir_to_dir_645_25138()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=25139) as unwtar_646_25139:
                            unwtar_646_25139()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RChannel.bundle", user_id=-1, group_id=-1, prog_num=25140, recursive=True) as chown_647_25140:
                            chown_647_25140()
            with Stage(r"copy", r"RComp v16.0.23.24", prog_num=25141):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25142) as should_copy_source_648_25142:
                    should_copy_source_648_25142()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=25143):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=25144) as copy_dir_to_dir_649_25144:
                            copy_dir_to_dir_649_25144()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=25145) as unwtar_650_25145:
                            unwtar_650_25145()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RComp.bundle", user_id=-1, group_id=-1, prog_num=25146, recursive=True) as chown_651_25146:
                            chown_651_25146()
            with Stage(r"copy", r"RDeEsser v16.0.23.24", prog_num=25147):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25148) as should_copy_source_652_25148:
                    should_copy_source_652_25148()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=25149):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=25150) as copy_dir_to_dir_653_25150:
                            copy_dir_to_dir_653_25150()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=25151) as unwtar_654_25151:
                            unwtar_654_25151()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=25152, recursive=True) as chown_655_25152:
                            chown_655_25152()
            with Stage(r"copy", r"REDD17 v16.0.23.24", prog_num=25153):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25154) as should_copy_source_656_25154:
                    should_copy_source_656_25154()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=25155):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=25156) as copy_dir_to_dir_657_25156:
                            copy_dir_to_dir_657_25156()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=25157) as unwtar_658_25157:
                            unwtar_658_25157()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD17.bundle", user_id=-1, group_id=-1, prog_num=25158, recursive=True) as chown_659_25158:
                            chown_659_25158()
            with Stage(r"copy", r"REDD37-51 v16.0.23.24", prog_num=25159):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25160) as should_copy_source_660_25160:
                    should_copy_source_660_25160()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=25161):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=25162) as copy_dir_to_dir_661_25162:
                            copy_dir_to_dir_661_25162()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=25163) as unwtar_662_25163:
                            unwtar_662_25163()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=25164, recursive=True) as chown_663_25164:
                            chown_663_25164()
            with Stage(r"copy", r"REQ v16.0.23.24", prog_num=25165):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25166) as should_copy_source_664_25166:
                    should_copy_source_664_25166()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=25167):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=25168) as copy_dir_to_dir_665_25168:
                            copy_dir_to_dir_665_25168()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=25169) as unwtar_666_25169:
                            unwtar_666_25169()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REQ.bundle", user_id=-1, group_id=-1, prog_num=25170, recursive=True) as chown_667_25170:
                            chown_667_25170()
            with Stage(r"copy", r"RS56 v16.0.23.24", prog_num=25171):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25172) as should_copy_source_668_25172:
                    should_copy_source_668_25172()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=25173):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=25174) as copy_dir_to_dir_669_25174:
                            copy_dir_to_dir_669_25174()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=25175) as unwtar_670_25175:
                            unwtar_670_25175()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RS56.bundle", user_id=-1, group_id=-1, prog_num=25176, recursive=True) as chown_671_25176:
                            chown_671_25176()
            with Stage(r"copy", r"RVerb v16.0.23.24", prog_num=25177):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25178) as should_copy_source_672_25178:
                    should_copy_source_672_25178()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=25179):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=25180) as copy_dir_to_dir_673_25180:
                            copy_dir_to_dir_673_25180()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=25181) as unwtar_674_25181:
                            unwtar_674_25181()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVerb.bundle", user_id=-1, group_id=-1, prog_num=25182, recursive=True) as chown_675_25182:
                            chown_675_25182()
            with Stage(r"copy", r"RVox v16.0.23.24", prog_num=25183):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25184) as should_copy_source_676_25184:
                    should_copy_source_676_25184()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=25185):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=25186) as copy_dir_to_dir_677_25186:
                            copy_dir_to_dir_677_25186()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=25187) as unwtar_678_25187:
                            unwtar_678_25187()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVox.bundle", user_id=-1, group_id=-1, prog_num=25188, recursive=True) as chown_679_25188:
                            chown_679_25188()
            with Stage(r"copy", r"Reel ADT v16.0.23.24", prog_num=25189):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25190) as should_copy_source_680_25190:
                    should_copy_source_680_25190()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=25191):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=25192) as copy_dir_to_dir_681_25192:
                            copy_dir_to_dir_681_25192()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=25193) as unwtar_682_25193:
                            unwtar_682_25193()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=25194, recursive=True) as chown_683_25194:
                            chown_683_25194()
            with Stage(r"copy", r"RenAxx v16.0.23.24", prog_num=25195):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25196) as should_copy_source_684_25196:
                    should_copy_source_684_25196()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=25197):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=25198) as copy_dir_to_dir_685_25198:
                            copy_dir_to_dir_685_25198()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=25199) as unwtar_686_25199:
                            unwtar_686_25199()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=25200, recursive=True) as chown_687_25200:
                            chown_687_25200()
            with Stage(r"copy", r"Retro Fi v16.0.23.24", prog_num=25201):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25202) as should_copy_source_688_25202:
                    should_copy_source_688_25202()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=25203):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=25204) as copy_dir_to_dir_689_25204:
                            copy_dir_to_dir_689_25204()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=25205) as unwtar_690_25205:
                            unwtar_690_25205()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=25206, recursive=True) as chown_691_25206:
                            chown_691_25206()
            with Stage(r"copy", r"S1 v16.0.23.24", prog_num=25207):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25208) as should_copy_source_692_25208:
                    should_copy_source_692_25208()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=25209):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=25210) as copy_dir_to_dir_693_25210:
                            copy_dir_to_dir_693_25210()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=25211) as unwtar_694_25211:
                            unwtar_694_25211()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S1.bundle", user_id=-1, group_id=-1, prog_num=25212, recursive=True) as chown_695_25212:
                            chown_695_25212()
            with Stage(r"copy", r"Scheps 73 v16.0.23.24", prog_num=25213):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25214) as should_copy_source_696_25214:
                    should_copy_source_696_25214()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=25215):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=25216) as copy_dir_to_dir_697_25216:
                            copy_dir_to_dir_697_25216()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=25217) as unwtar_698_25217:
                            unwtar_698_25217()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=25218, recursive=True) as chown_699_25218:
                            chown_699_25218()
            with Stage(r"copy", r"Scheps Omni Channel v16.0.64.65", prog_num=25219):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25220) as should_copy_source_700_25220:
                    should_copy_source_700_25220()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=25221):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=25222) as copy_dir_to_dir_701_25222:
                            copy_dir_to_dir_701_25222()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=25223) as unwtar_702_25223:
                            unwtar_702_25223()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=25224, recursive=True) as chown_703_25224:
                            chown_703_25224()
            with Stage(r"copy", r"Scheps Parallel Particles v16.0.23.24", prog_num=25225):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25226) as should_copy_source_704_25226:
                    should_copy_source_704_25226()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=25227):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=25228) as copy_dir_to_dir_705_25228:
                            copy_dir_to_dir_705_25228()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=25229) as unwtar_706_25229:
                            unwtar_706_25229()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=25230, recursive=True) as chown_707_25230:
                            chown_707_25230()
            with Stage(r"copy", r"Sibilance v16.0.23.24", prog_num=25231):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25232) as should_copy_source_708_25232:
                    should_copy_source_708_25232()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=25233):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=25234) as copy_dir_to_dir_709_25234:
                            copy_dir_to_dir_709_25234()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=25235) as unwtar_710_25235:
                            unwtar_710_25235()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=25236, recursive=True) as chown_711_25236:
                            chown_711_25236()
            with Stage(r"copy", r"Emo Signal Generator v16.0.23.24", prog_num=25237):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25238) as should_copy_source_712_25238:
                    should_copy_source_712_25238()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=25239):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=25240) as copy_dir_to_dir_713_25240:
                            copy_dir_to_dir_713_25240()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=25241) as unwtar_714_25241:
                            unwtar_714_25241()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=25242, recursive=True) as chown_715_25242:
                            chown_715_25242()
            with Stage(r"copy", r"Silk Vocal v16.0.23.24", prog_num=25243):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25244) as should_copy_source_716_25244:
                    should_copy_source_716_25244()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=25245):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=25246) as copy_dir_to_dir_717_25246:
                            copy_dir_to_dir_717_25246()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=25247) as unwtar_718_25247:
                            unwtar_718_25247()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=25248, recursive=True) as chown_719_25248:
                            chown_719_25248()
            with Stage(r"copy", r"Smack Attack v16.0.23.24", prog_num=25249):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25250) as should_copy_source_720_25250:
                    should_copy_source_720_25250()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=25251):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=25252) as copy_dir_to_dir_721_25252:
                            copy_dir_to_dir_721_25252()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=25253) as unwtar_722_25253:
                            unwtar_722_25253()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=25254, recursive=True) as chown_723_25254:
                            chown_723_25254()
            with Stage(r"copy", r"SoundShifter v16.0.23.24", prog_num=25255):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25256) as should_copy_source_724_25256:
                    should_copy_source_724_25256()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=25257):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=25258) as copy_dir_to_dir_725_25258:
                            copy_dir_to_dir_725_25258()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=25259) as unwtar_726_25259:
                            unwtar_726_25259()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=25260, recursive=True) as chown_727_25260:
                            chown_727_25260()
            with Stage(r"copy", r"Spherix Immersive Compressor v16.0.23.24", prog_num=25261):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25262) as should_copy_source_728_25262:
                    should_copy_source_728_25262()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=25263):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=25264) as copy_dir_to_dir_729_25264:
                            copy_dir_to_dir_729_25264()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=25265) as unwtar_730_25265:
                            unwtar_730_25265()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=25266, recursive=True) as chown_731_25266:
                            chown_731_25266()
            with Stage(r"copy", r"Spherix Immersive Limiter v16.0.23.24", prog_num=25267):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25268) as should_copy_source_732_25268:
                    should_copy_source_732_25268()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=25269):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=25270) as copy_dir_to_dir_733_25270:
                            copy_dir_to_dir_733_25270()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=25271) as unwtar_734_25271:
                            unwtar_734_25271()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=25272, recursive=True) as chown_735_25272:
                            chown_735_25272()
            with Stage(r"copy", r"SuperTap v16.0.23.24", prog_num=25273):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25274) as should_copy_source_736_25274:
                    should_copy_source_736_25274()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=25275):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=25276) as copy_dir_to_dir_737_25276:
                            copy_dir_to_dir_737_25276()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=25277) as unwtar_738_25277:
                            unwtar_738_25277()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=25278, recursive=True) as chown_739_25278:
                            chown_739_25278()
            with Stage(r"copy", r"Sync Vx v16.0.91.92", prog_num=25279):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25280) as should_copy_source_740_25280:
                    should_copy_source_740_25280()
                    with Stage(r"copy source", r"Mac/Plugins/Sync Vx.bundle", prog_num=25281):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r".", delete_extraneous_files=True, prog_num=25282) as copy_dir_to_dir_741_25282:
                            copy_dir_to_dir_741_25282()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", where_to_unwtar=r".", prog_num=25283) as unwtar_742_25283:
                            unwtar_742_25283()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sync Vx.bundle", user_id=-1, group_id=-1, prog_num=25284, recursive=True) as chown_743_25284:
                            chown_743_25284()
            with Stage(r"copy", r"TG12345 v16.0.23.24", prog_num=25285):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25286) as should_copy_source_744_25286:
                    should_copy_source_744_25286()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=25287):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=25288) as copy_dir_to_dir_745_25288:
                            copy_dir_to_dir_745_25288()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=25289) as unwtar_746_25289:
                            unwtar_746_25289()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TG12345.bundle", user_id=-1, group_id=-1, prog_num=25290, recursive=True) as chown_747_25290:
                            chown_747_25290()
            with Stage(r"copy", r"AR TG Meter Bridge v16.0.23.24", prog_num=25291):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25292) as should_copy_source_748_25292:
                    should_copy_source_748_25292()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=25293):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=25294) as copy_dir_to_dir_749_25294:
                            copy_dir_to_dir_749_25294()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=25295) as unwtar_750_25295:
                            unwtar_750_25295()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=25296, recursive=True) as chown_751_25296:
                            chown_751_25296()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v16.0.23.24", prog_num=25297):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25298) as should_copy_source_752_25298:
                    should_copy_source_752_25298()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=25299):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=25300) as copy_dir_to_dir_753_25300:
                            copy_dir_to_dir_753_25300()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=25301) as unwtar_754_25301:
                            unwtar_754_25301()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=25302, recursive=True) as chown_755_25302:
                            chown_755_25302()
            with Stage(r"copy", r"TransX v16.0.23.24", prog_num=25303):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25304) as should_copy_source_756_25304:
                    should_copy_source_756_25304()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=25305):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=25306) as copy_dir_to_dir_757_25306:
                            copy_dir_to_dir_757_25306()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=25307) as unwtar_758_25307:
                            unwtar_758_25307()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TransX.bundle", user_id=-1, group_id=-1, prog_num=25308, recursive=True) as chown_759_25308:
                            chown_759_25308()
            with Stage(r"copy", r"TrueVerb v16.0.23.24", prog_num=25309):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25310) as should_copy_source_760_25310:
                    should_copy_source_760_25310()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=25311):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=25312) as copy_dir_to_dir_761_25312:
                            copy_dir_to_dir_761_25312()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=25313) as unwtar_762_25313:
                            unwtar_762_25313()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=25314, recursive=True) as chown_763_25314:
                            chown_763_25314()
            with Stage(r"copy", r"UM v16.0.91.92", prog_num=25315):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25316) as should_copy_source_764_25316:
                    should_copy_source_764_25316()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=25317):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=25318) as copy_dir_to_dir_765_25318:
                            copy_dir_to_dir_765_25318()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=25319) as unwtar_766_25319:
                            unwtar_766_25319()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UM.bundle", user_id=-1, group_id=-1, prog_num=25320, recursive=True) as chown_767_25320:
                            chown_767_25320()
            with Stage(r"copy", r"UltraPitch v16.0.23.24", prog_num=25321):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25322) as should_copy_source_768_25322:
                    should_copy_source_768_25322()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=25323):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=25324) as copy_dir_to_dir_769_25324:
                            copy_dir_to_dir_769_25324()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=25325) as unwtar_770_25325:
                            unwtar_770_25325()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=25326, recursive=True) as chown_771_25326:
                            chown_771_25326()
            with Stage(r"copy", r"VComp v16.0.23.24", prog_num=25327):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25328) as should_copy_source_772_25328:
                    should_copy_source_772_25328()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=25329):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=25330) as copy_dir_to_dir_773_25330:
                            copy_dir_to_dir_773_25330()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=25331) as unwtar_774_25331:
                            unwtar_774_25331()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VComp.bundle", user_id=-1, group_id=-1, prog_num=25332, recursive=True) as chown_775_25332:
                            chown_775_25332()
            with Stage(r"copy", r"VEQ3 v16.0.23.24", prog_num=25333):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25334) as should_copy_source_776_25334:
                    should_copy_source_776_25334()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=25335):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=25336) as copy_dir_to_dir_777_25336:
                            copy_dir_to_dir_777_25336()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=25337) as unwtar_778_25337:
                            unwtar_778_25337()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=25338, recursive=True) as chown_779_25338:
                            chown_779_25338()
            with Stage(r"copy", r"VEQ4 v16.0.23.24", prog_num=25339):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25340) as should_copy_source_780_25340:
                    should_copy_source_780_25340()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=25341):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=25342) as copy_dir_to_dir_781_25342:
                            copy_dir_to_dir_781_25342()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=25343) as unwtar_782_25343:
                            unwtar_782_25343()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=25344, recursive=True) as chown_783_25344:
                            chown_783_25344()
            with Stage(r"copy", r"VU Meter v16.0.23.24", prog_num=25345):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25346) as should_copy_source_784_25346:
                    should_copy_source_784_25346()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=25347):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=25348) as copy_dir_to_dir_785_25348:
                            copy_dir_to_dir_785_25348()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=25349) as unwtar_786_25349:
                            unwtar_786_25349()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=25350, recursive=True) as chown_787_25350:
                            chown_787_25350()
            with Stage(r"copy", r"Vitamin v16.0.23.24", prog_num=25351):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25352) as should_copy_source_788_25352:
                    should_copy_source_788_25352()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=25353):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=25354) as copy_dir_to_dir_789_25354:
                            copy_dir_to_dir_789_25354()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=25355) as unwtar_790_25355:
                            unwtar_790_25355()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=25356, recursive=True) as chown_791_25356:
                            chown_791_25356()
            with Stage(r"copy", r"Vocal Rider v16.0.23.24", prog_num=25357):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25358) as should_copy_source_792_25358:
                    should_copy_source_792_25358()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=25359):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=25360) as copy_dir_to_dir_793_25360:
                            copy_dir_to_dir_793_25360()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=25361) as unwtar_794_25361:
                            unwtar_794_25361()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=25362, recursive=True) as chown_795_25362:
                            chown_795_25362()
            with Stage(r"copy", r"Voltage Amps Bass v16.0.23.24", prog_num=25363):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25364) as should_copy_source_796_25364:
                    should_copy_source_796_25364()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=25365):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=25366) as copy_dir_to_dir_797_25366:
                            copy_dir_to_dir_797_25366()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=25367) as unwtar_798_25367:
                            unwtar_798_25367()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=25368, recursive=True) as chown_799_25368:
                            chown_799_25368()
            with Stage(r"copy", r"Voltage Amps Guitar v16.0.23.24", prog_num=25369):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25370) as should_copy_source_800_25370:
                    should_copy_source_800_25370()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=25371):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=25372) as copy_dir_to_dir_801_25372:
                            copy_dir_to_dir_801_25372()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=25373) as unwtar_802_25373:
                            unwtar_802_25373()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=25374, recursive=True) as chown_803_25374:
                            chown_803_25374()
            with Stage(r"copy", r"WLM v16.0.78.79", prog_num=25375):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25376) as should_copy_source_804_25376:
                    should_copy_source_804_25376()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=25377):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=25378) as copy_dir_to_dir_805_25378:
                            copy_dir_to_dir_805_25378()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=25379) as unwtar_806_25379:
                            unwtar_806_25379()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM.bundle", user_id=-1, group_id=-1, prog_num=25380, recursive=True) as chown_807_25380:
                            chown_807_25380()
            with Stage(r"copy", r"WLM Plus v16.0.78.79", prog_num=25381):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25382) as should_copy_source_808_25382:
                    should_copy_source_808_25382()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=25383):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=25384) as copy_dir_to_dir_809_25384:
                            copy_dir_to_dir_809_25384()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=25385) as unwtar_810_25385:
                            unwtar_810_25385()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=25386, recursive=True) as chown_811_25386:
                            chown_811_25386()
            with Stage(r"copy", r"WavesHeadTracker v16.0.23.24", prog_num=25387):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=5, prog_num=25388) as should_copy_source_812_25388:
                    should_copy_source_812_25388()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=25389):
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=25390) as rm_file_or_dir_813_25390:
                            rm_file_or_dir_813_25390()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=25391) as copy_dir_to_dir_814_25391:
                            copy_dir_to_dir_814_25391()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=25392) as unwtar_815_25392:
                            unwtar_815_25392()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=25393, recursive=True) as chown_816_25393:
                            chown_816_25393()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=25394):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25395) as should_copy_source_817_25395:
                    should_copy_source_817_25395()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=25396):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=25397) as copy_dir_to_dir_818_25397:
                            copy_dir_to_dir_818_25397()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=25398) as unwtar_819_25398:
                            unwtar_819_25398()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=25399, recursive=True) as chown_820_25399:
                            chown_820_25399()
            with Stage(r"copy", r"WavesLib1_16_0_30_31 v16.0.30.31", prog_num=25400):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25401) as should_copy_source_821_25401:
                    should_copy_source_821_25401()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.30.framework", prog_num=25402):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r".", delete_extraneous_files=True, prog_num=25403) as copy_dir_to_dir_822_25403:
                            copy_dir_to_dir_822_25403()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", where_to_unwtar=r".", prog_num=25404) as unwtar_823_25404:
                            unwtar_823_25404()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.30.framework", user_id=-1, group_id=-1, prog_num=25405, recursive=True) as chown_824_25405:
                            chown_824_25405()
            with Stage(r"copy", r"WavesLib1_16_0_64_65 v16.0.64.65", prog_num=25406):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25407) as should_copy_source_825_25407:
                    should_copy_source_825_25407()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.64.framework", prog_num=25408):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", r".", delete_extraneous_files=True, prog_num=25409) as copy_dir_to_dir_826_25409:
                            copy_dir_to_dir_826_25409()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.64.framework", where_to_unwtar=r".", prog_num=25410) as unwtar_827_25410:
                            unwtar_827_25410()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.64.framework", user_id=-1, group_id=-1, prog_num=25411, recursive=True) as chown_828_25411:
                            chown_828_25411()
            with Stage(r"copy", r"WavesLib1_16_0_78_79 v16.0.78.79", prog_num=25412):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.78.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25413) as should_copy_source_829_25413:
                    should_copy_source_829_25413()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.78.framework", prog_num=25414):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.78.framework", r".", delete_extraneous_files=True, prog_num=25415) as copy_dir_to_dir_830_25415:
                            copy_dir_to_dir_830_25415()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.78.framework", where_to_unwtar=r".", prog_num=25416) as unwtar_831_25416:
                            unwtar_831_25416()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.78.framework", user_id=-1, group_id=-1, prog_num=25417, recursive=True) as chown_832_25417:
                            chown_832_25417()
            with Stage(r"copy", r"WavesLib1_16_0_91_92 v16.0.91.92", prog_num=25418):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.91.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25419) as should_copy_source_833_25419:
                    should_copy_source_833_25419()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.91.framework", prog_num=25420):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.91.framework", r".", delete_extraneous_files=True, prog_num=25421) as copy_dir_to_dir_834_25421:
                            copy_dir_to_dir_834_25421()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.91.framework", where_to_unwtar=r".", prog_num=25422) as unwtar_835_25422:
                            unwtar_835_25422()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.91.framework", user_id=-1, group_id=-1, prog_num=25423, recursive=True) as chown_836_25423:
                            chown_836_25423()
            with Stage(r"copy", r"WavesLib1_16_1_99_101 v16.1.99.101", prog_num=25424):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25425) as should_copy_source_837_25425:
                    should_copy_source_837_25425()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.1.99.framework", prog_num=25426):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", r".", delete_extraneous_files=True, prog_num=25427) as copy_dir_to_dir_838_25427:
                            copy_dir_to_dir_838_25427()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.1.99.framework", where_to_unwtar=r".", prog_num=25428) as unwtar_839_25428:
                            unwtar_839_25428()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.1.99.framework", user_id=-1, group_id=-1, prog_num=25429, recursive=True) as chown_840_25429:
                            chown_840_25429()
            with Stage(r"copy", r"WavesLib1_16_2_30_56 v16.2.30.56", prog_num=25430):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25431) as should_copy_source_841_25431:
                    should_copy_source_841_25431()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.2.30.framework", prog_num=25432):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", r".", delete_extraneous_files=True, prog_num=25433) as copy_dir_to_dir_842_25433:
                            copy_dir_to_dir_842_25433()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.2.30.framework", where_to_unwtar=r".", prog_num=25434) as unwtar_843_25434:
                            unwtar_843_25434()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.2.30.framework", user_id=-1, group_id=-1, prog_num=25435, recursive=True) as chown_844_25435:
                            chown_844_25435()
            with Stage(r"copy", r"WavesTune v16.0.23.24", prog_num=25436):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25437) as should_copy_source_845_25437:
                    should_copy_source_845_25437()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=25438):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=25439) as copy_dir_to_dir_846_25439:
                            copy_dir_to_dir_846_25439()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=25440) as unwtar_847_25440:
                            unwtar_847_25440()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=25441, recursive=True) as chown_848_25441:
                            chown_848_25441()
            with Stage(r"copy", r"WavesTune LT v16.0.23.24", prog_num=25442):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25443) as should_copy_source_849_25443:
                    should_copy_source_849_25443()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=25444):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=25445) as copy_dir_to_dir_850_25445:
                            copy_dir_to_dir_850_25445()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=25446) as unwtar_851_25446:
                            unwtar_851_25446()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=25447, recursive=True) as chown_852_25447:
                            chown_852_25447()
            with Stage(r"copy", r"Waves Harmony v16.0.23.24", prog_num=25448):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25449) as should_copy_source_853_25449:
                    should_copy_source_853_25449()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=25450):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=25451) as copy_dir_to_dir_854_25451:
                            copy_dir_to_dir_854_25451()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=25452) as unwtar_855_25452:
                            unwtar_855_25452()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=25453, recursive=True) as chown_856_25453:
                            chown_856_25453()
            with Stage(r"copy", r"Waves Tune Real-Time v16.0.23.24", prog_num=25454):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25455) as should_copy_source_857_25455:
                    should_copy_source_857_25455()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=25456):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=25457) as copy_dir_to_dir_858_25457:
                            copy_dir_to_dir_858_25457()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=25458) as unwtar_859_25458:
                            unwtar_859_25458()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=25459, recursive=True) as chown_860_25459:
                            chown_860_25459()
            with Stage(r"copy", r"X-Click v16.0.23.24", prog_num=25460):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25461) as should_copy_source_861_25461:
                    should_copy_source_861_25461()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=25462):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=25463) as copy_dir_to_dir_862_25463:
                            copy_dir_to_dir_862_25463()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=25464) as unwtar_863_25464:
                            unwtar_863_25464()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Click.bundle", user_id=-1, group_id=-1, prog_num=25465, recursive=True) as chown_864_25465:
                            chown_864_25465()
            with Stage(r"copy", r"X-Crackle v16.0.23.24", prog_num=25466):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25467) as should_copy_source_865_25467:
                    should_copy_source_865_25467()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=25468):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=25469) as copy_dir_to_dir_866_25469:
                            copy_dir_to_dir_866_25469()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=25470) as unwtar_867_25470:
                            unwtar_867_25470()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=25471, recursive=True) as chown_868_25471:
                            chown_868_25471()
            with Stage(r"copy", r"X-Hum v16.0.23.24", prog_num=25472):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25473) as should_copy_source_869_25473:
                    should_copy_source_869_25473()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=25474):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=25475) as copy_dir_to_dir_870_25475:
                            copy_dir_to_dir_870_25475()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=25476) as unwtar_871_25476:
                            unwtar_871_25476()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=25477, recursive=True) as chown_872_25477:
                            chown_872_25477()
            with Stage(r"copy", r"X-Noise v16.0.23.24", prog_num=25478):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25479) as should_copy_source_873_25479:
                    should_copy_source_873_25479()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=25480):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=25481) as copy_dir_to_dir_874_25481:
                            copy_dir_to_dir_874_25481()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=25482) as unwtar_875_25482:
                            unwtar_875_25482()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=25483, recursive=True) as chown_876_25483:
                            chown_876_25483()
            with Stage(r"copy", r"Z-Noise v16.0.23.24", prog_num=25484):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=25485) as should_copy_source_877_25485:
                    should_copy_source_877_25485()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=25486):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=25487) as copy_dir_to_dir_878_25487:
                            copy_dir_to_dir_878_25487()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=25488) as unwtar_879_25488:
                            unwtar_879_25488()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=25489, recursive=True) as chown_880_25489:
                            chown_880_25489()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=14, prog_num=25503) as resolve_symlink_files_in_folder_881_25503:
                resolve_symlink_files_in_folder_881_25503()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=25504) as shell_command_882_25504:
                shell_command_882_25504()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=25505) as script_command_883_25505:
                script_command_883_25505()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=25506) as shell_command_884_25506:
                shell_command_884_25506()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=25507) as create_symlink_885_25507:
                create_symlink_885_25507()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=25508) as create_symlink_886_25508:
                create_symlink_886_25508()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=25509) as copy_glob_to_dir_887_25509:
                copy_glob_to_dir_887_25509()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=25510) as cd_stage_888_25510:
            cd_stage_888_25510()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=25511):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=25512) as should_copy_source_889_25512:
                    should_copy_source_889_25512()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=25513):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=25514) as copy_file_to_dir_890_25514:
                            copy_file_to_dir_890_25514()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=25515) as chmod_and_chown_891_25515:
                            chmod_and_chown_891_25515()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTR", prog_num=25516) as cd_stage_892_25516:
            cd_stage_892_25516()
            with Stage(r"copy", r"GTR Stomps v16.0.23.24", prog_num=25517):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25518) as should_copy_source_893_25518:
                    should_copy_source_893_25518()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=25519):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=25520) as copy_dir_to_dir_894_25520:
                            copy_dir_to_dir_894_25520()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=25521) as unwtar_895_25521:
                            unwtar_895_25521()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=25522, recursive=True) as chown_896_25522:
                            chown_896_25522()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25523) as should_copy_source_897_25523:
                    should_copy_source_897_25523()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=25524):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=25525) as copy_dir_to_dir_898_25525:
                            copy_dir_to_dir_898_25525()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=25526) as unwtar_899_25526:
                            unwtar_899_25526()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=25527, recursive=True) as chown_900_25527:
                            chown_900_25527()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25528) as should_copy_source_901_25528:
                    should_copy_source_901_25528()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=25529):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=25530) as copy_dir_to_dir_902_25530:
                            copy_dir_to_dir_902_25530()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=25531) as unwtar_903_25531:
                            unwtar_903_25531()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=25532, recursive=True) as chown_904_25532:
                            chown_904_25532()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25533) as should_copy_source_905_25533:
                    should_copy_source_905_25533()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=25534):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=25535) as copy_dir_to_dir_906_25535:
                            copy_dir_to_dir_906_25535()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=25536) as unwtar_907_25536:
                            unwtar_907_25536()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=25537, recursive=True) as chown_908_25537:
                            chown_908_25537()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25538) as should_copy_source_909_25538:
                    should_copy_source_909_25538()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=25539):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=25540) as copy_dir_to_dir_910_25540:
                            copy_dir_to_dir_910_25540()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=25541) as unwtar_911_25541:
                            unwtar_911_25541()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=25542, recursive=True) as chown_912_25542:
                            chown_912_25542()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25543) as should_copy_source_913_25543:
                    should_copy_source_913_25543()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=25544):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=25545) as copy_dir_to_dir_914_25545:
                            copy_dir_to_dir_914_25545()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=25546) as unwtar_915_25546:
                            unwtar_915_25546()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=25547, recursive=True) as chown_916_25547:
                            chown_916_25547()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25548) as should_copy_source_917_25548:
                    should_copy_source_917_25548()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=25549):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=25550) as copy_dir_to_dir_918_25550:
                            copy_dir_to_dir_918_25550()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=25551) as unwtar_919_25551:
                            unwtar_919_25551()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=25552, recursive=True) as chown_920_25552:
                            chown_920_25552()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25553) as should_copy_source_921_25553:
                    should_copy_source_921_25553()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=25554):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=25555) as copy_dir_to_dir_922_25555:
                            copy_dir_to_dir_922_25555()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=25556) as unwtar_923_25556:
                            unwtar_923_25556()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=25557, recursive=True) as chown_924_25557:
                            chown_924_25557()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25558) as should_copy_source_925_25558:
                    should_copy_source_925_25558()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=25559):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=25560) as copy_dir_to_dir_926_25560:
                            copy_dir_to_dir_926_25560()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=25561) as unwtar_927_25561:
                            unwtar_927_25561()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=25562, recursive=True) as chown_928_25562:
                            chown_928_25562()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25563) as should_copy_source_929_25563:
                    should_copy_source_929_25563()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=25564):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=25565) as copy_dir_to_dir_930_25565:
                            copy_dir_to_dir_930_25565()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=25566) as unwtar_931_25566:
                            unwtar_931_25566()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=25567, recursive=True) as chown_932_25567:
                            chown_932_25567()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25568) as should_copy_source_933_25568:
                    should_copy_source_933_25568()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=25569):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=25570) as copy_dir_to_dir_934_25570:
                            copy_dir_to_dir_934_25570()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=25571) as unwtar_935_25571:
                            unwtar_935_25571()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=25572, recursive=True) as chown_936_25572:
                            chown_936_25572()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25573) as should_copy_source_937_25573:
                    should_copy_source_937_25573()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=25574):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=25575) as copy_dir_to_dir_938_25575:
                            copy_dir_to_dir_938_25575()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=25576) as unwtar_939_25576:
                            unwtar_939_25576()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=25577, recursive=True) as chown_940_25577:
                            chown_940_25577()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25578) as should_copy_source_941_25578:
                    should_copy_source_941_25578()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=25579):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=25580) as copy_dir_to_dir_942_25580:
                            copy_dir_to_dir_942_25580()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=25581) as unwtar_943_25581:
                            unwtar_943_25581()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=25582, recursive=True) as chown_944_25582:
                            chown_944_25582()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25583) as should_copy_source_945_25583:
                    should_copy_source_945_25583()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=25584):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=25585) as copy_dir_to_dir_946_25585:
                            copy_dir_to_dir_946_25585()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=25586) as unwtar_947_25586:
                            unwtar_947_25586()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=25587, recursive=True) as chown_948_25587:
                            chown_948_25587()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25588) as should_copy_source_949_25588:
                    should_copy_source_949_25588()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=25589):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=25590) as copy_dir_to_dir_950_25590:
                            copy_dir_to_dir_950_25590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=25591) as unwtar_951_25591:
                            unwtar_951_25591()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=25592, recursive=True) as chown_952_25592:
                            chown_952_25592()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25593) as should_copy_source_953_25593:
                    should_copy_source_953_25593()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=25594):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=25595) as copy_dir_to_dir_954_25595:
                            copy_dir_to_dir_954_25595()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=25596) as unwtar_955_25596:
                            unwtar_955_25596()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=25597, recursive=True) as chown_956_25597:
                            chown_956_25597()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25598) as should_copy_source_957_25598:
                    should_copy_source_957_25598()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=25599):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=25600) as copy_dir_to_dir_958_25600:
                            copy_dir_to_dir_958_25600()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=25601) as unwtar_959_25601:
                            unwtar_959_25601()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=25602, recursive=True) as chown_960_25602:
                            chown_960_25602()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25603) as should_copy_source_961_25603:
                    should_copy_source_961_25603()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=25604):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=25605) as copy_dir_to_dir_962_25605:
                            copy_dir_to_dir_962_25605()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=25606) as unwtar_963_25606:
                            unwtar_963_25606()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=25607, recursive=True) as chown_964_25607:
                            chown_964_25607()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25608) as should_copy_source_965_25608:
                    should_copy_source_965_25608()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=25609):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=25610) as copy_dir_to_dir_966_25610:
                            copy_dir_to_dir_966_25610()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=25611) as unwtar_967_25611:
                            unwtar_967_25611()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=25612, recursive=True) as chown_968_25612:
                            chown_968_25612()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25613) as should_copy_source_969_25613:
                    should_copy_source_969_25613()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=25614):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=25615) as copy_dir_to_dir_970_25615:
                            copy_dir_to_dir_970_25615()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=25616) as unwtar_971_25616:
                            unwtar_971_25616()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=25617, recursive=True) as chown_972_25617:
                            chown_972_25617()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25618) as should_copy_source_973_25618:
                    should_copy_source_973_25618()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=25619):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=25620) as copy_dir_to_dir_974_25620:
                            copy_dir_to_dir_974_25620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=25621) as unwtar_975_25621:
                            unwtar_975_25621()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=25622, recursive=True) as chown_976_25622:
                            chown_976_25622()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25623) as should_copy_source_977_25623:
                    should_copy_source_977_25623()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=25624):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=25625) as copy_dir_to_dir_978_25625:
                            copy_dir_to_dir_978_25625()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=25626) as unwtar_979_25626:
                            unwtar_979_25626()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=25627, recursive=True) as chown_980_25627:
                            chown_980_25627()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25628) as should_copy_source_981_25628:
                    should_copy_source_981_25628()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=25629):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=25630) as copy_dir_to_dir_982_25630:
                            copy_dir_to_dir_982_25630()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=25631) as unwtar_983_25631:
                            unwtar_983_25631()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=25632, recursive=True) as chown_984_25632:
                            chown_984_25632()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25633) as should_copy_source_985_25633:
                    should_copy_source_985_25633()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=25634):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=25635) as copy_dir_to_dir_986_25635:
                            copy_dir_to_dir_986_25635()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=25636) as unwtar_987_25636:
                            unwtar_987_25636()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=25637, recursive=True) as chown_988_25637:
                            chown_988_25637()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=25638) as should_copy_source_989_25638:
                    should_copy_source_989_25638()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=25639):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=25640) as copy_dir_to_dir_990_25640:
                            copy_dir_to_dir_990_25640()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=25641) as unwtar_991_25641:
                            unwtar_991_25641()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=25642, recursive=True) as chown_992_25642:
                            chown_992_25642()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=25643) as shell_command_993_25643:
                shell_command_993_25643()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=25644) as cd_stage_994_25644:
            cd_stage_994_25644()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.78.79", prog_num=25645):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25646) as should_copy_source_995_25646:
                    should_copy_source_995_25646()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=25647):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=25648) as copy_dir_to_dir_996_25648:
                            copy_dir_to_dir_996_25648()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=25649) as unwtar_997_25649:
                            unwtar_997_25649()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=25650, recursive=True) as chown_998_25650:
                            chown_998_25650()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=25651) as shell_command_999_25651:
                            shell_command_999_25651()
            with Stage(r"copy", r"WaveShell1-AAX 16.1 v16.1.77.79", prog_num=25652):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25653) as should_copy_source_1000_25653:
                    should_copy_source_1000_25653()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", prog_num=25654):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r".", delete_extraneous_files=True, prog_num=25655) as copy_dir_to_dir_1001_25655:
                            copy_dir_to_dir_1001_25655()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", where_to_unwtar=r".", prog_num=25656) as unwtar_1002_25656:
                            unwtar_1002_25656()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.1.aaxplugin", user_id=-1, group_id=-1, prog_num=25657, recursive=True) as chown_1003_25657:
                            chown_1003_25657()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.1.aaxplugin"', ignore_all_errors=True, prog_num=25658) as shell_command_1004_25658:
                            shell_command_1004_25658()
            with Stage(r"copy", r"WaveShell1-AAX 16.2 v16.2.30.56", prog_num=25659):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25660) as should_copy_source_1005_25660:
                    should_copy_source_1005_25660()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", prog_num=25661):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r".", delete_extraneous_files=True, prog_num=25662) as copy_dir_to_dir_1006_25662:
                            copy_dir_to_dir_1006_25662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", where_to_unwtar=r".", prog_num=25663) as unwtar_1007_25663:
                            unwtar_1007_25663()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.2.aaxplugin", user_id=-1, group_id=-1, prog_num=25664, recursive=True) as chown_1008_25664:
                            chown_1008_25664()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.2.aaxplugin"', ignore_all_errors=True, prog_num=25665) as shell_command_1009_25665:
                            shell_command_1009_25665()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=25666):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=25667) as should_copy_source_1010_25667:
                    should_copy_source_1010_25667()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=25668):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=25669) as copy_dir_to_dir_1011_25669:
                            copy_dir_to_dir_1011_25669()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=25670) as unwtar_1012_25670:
                            unwtar_1012_25670()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=25671, recursive=True) as chown_1013_25671:
                            chown_1013_25671()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=25672) as break_hard_link_1014_25672:
                            break_hard_link_1014_25672()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=25673) as shell_command_1015_25673:
                            shell_command_1015_25673()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=25674, recursive=True) as chown_1016_25674:
                            chown_1016_25674()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=25675, recursive=True) as chmod_1017_25675:
                            chmod_1017_25675()
            with Stage(r"copy", r"WaveShell1-AU 16.1 v16.1.77.79", prog_num=25676):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=25677) as should_copy_source_1018_25677:
                    should_copy_source_1018_25677()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.1.component", prog_num=25678):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r".", delete_extraneous_files=True, prog_num=25679) as copy_dir_to_dir_1019_25679:
                            copy_dir_to_dir_1019_25679()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", where_to_unwtar=r".", prog_num=25680) as unwtar_1020_25680:
                            unwtar_1020_25680()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=25681, recursive=True) as chown_1021_25681:
                            chown_1021_25681()
                        with BreakHardLink(r"WaveShell1-AU 16.1.component/Contents/Info.plist", prog_num=25682) as break_hard_link_1022_25682:
                            break_hard_link_1022_25682()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.1.component"', ignore_all_errors=True, prog_num=25683) as shell_command_1023_25683:
                            shell_command_1023_25683()
                        with Chown(path=r"WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=25684, recursive=True) as chown_1024_25684:
                            chown_1024_25684()
                        with Chmod(path=r"WaveShell1-AU 16.1.component", mode="a+rwX", prog_num=25685, recursive=True) as chmod_1025_25685:
                            chmod_1025_25685()
            with Stage(r"copy", r"WaveShell1-AU 16.2.component v16.2.30.56", prog_num=25686):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=25687) as should_copy_source_1026_25687:
                    should_copy_source_1026_25687()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.2.component", prog_num=25688):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r".", delete_extraneous_files=True, prog_num=25689) as copy_dir_to_dir_1027_25689:
                            copy_dir_to_dir_1027_25689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", where_to_unwtar=r".", prog_num=25690) as unwtar_1028_25690:
                            unwtar_1028_25690()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=25691, recursive=True) as chown_1029_25691:
                            chown_1029_25691()
                        with BreakHardLink(r"WaveShell1-AU 16.2.component/Contents/Info.plist", prog_num=25692) as break_hard_link_1030_25692:
                            break_hard_link_1030_25692()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.2.component"', ignore_all_errors=True, prog_num=25693) as shell_command_1031_25693:
                            shell_command_1031_25693()
                        with Chown(path=r"WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=25694, recursive=True) as chown_1032_25694:
                            chown_1032_25694()
                        with Chmod(path=r"WaveShell1-AU 16.2.component", mode="a+rwX", prog_num=25695, recursive=True) as chmod_1033_25695:
                            chmod_1033_25695()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=25696):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25697) as should_copy_source_1034_25697:
                    should_copy_source_1034_25697()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=25698):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=25699) as copy_dir_to_dir_1035_25699:
                            copy_dir_to_dir_1035_25699()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=25700) as unwtar_1036_25700:
                            unwtar_1036_25700()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=25701, recursive=True) as chown_1037_25701:
                            chown_1037_25701()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=25702) as shell_command_1038_25702:
                            shell_command_1038_25702()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.91.92", prog_num=25703):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25704) as should_copy_source_1039_25704:
                    should_copy_source_1039_25704()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=25705):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=25706) as copy_dir_to_dir_1040_25706:
                            copy_dir_to_dir_1040_25706()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=25707) as unwtar_1041_25707:
                            unwtar_1041_25707()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=25708, recursive=True) as chown_1042_25708:
                            chown_1042_25708()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=25709) as shell_command_1043_25709:
                            shell_command_1043_25709()
            with Stage(r"copy", r"WaveShell1-VST3 16.1 v16.1.77.79", prog_num=25710):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25711) as should_copy_source_1044_25711:
                    should_copy_source_1044_25711()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.1.vst3", prog_num=25712):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r".", delete_extraneous_files=True, prog_num=25713) as copy_dir_to_dir_1045_25713:
                            copy_dir_to_dir_1045_25713()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", where_to_unwtar=r".", prog_num=25714) as unwtar_1046_25714:
                            unwtar_1046_25714()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.1.vst3", user_id=-1, group_id=-1, prog_num=25715, recursive=True) as chown_1047_25715:
                            chown_1047_25715()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.1.vst3"', ignore_all_errors=True, prog_num=25716) as shell_command_1048_25716:
                            shell_command_1048_25716()
            with Stage(r"copy", r"WaveShell1-VST3 16.2 v16.2.30.56", prog_num=25717):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=25718) as should_copy_source_1049_25718:
                    should_copy_source_1049_25718()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.2.vst3", prog_num=25719):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r".", delete_extraneous_files=True, prog_num=25720) as copy_dir_to_dir_1050_25720:
                            copy_dir_to_dir_1050_25720()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", where_to_unwtar=r".", prog_num=25721) as unwtar_1051_25721:
                            unwtar_1051_25721()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.2.vst3", user_id=-1, group_id=-1, prog_num=25722, recursive=True) as chown_1052_25722:
                            chown_1052_25722()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.2.vst3"', ignore_all_errors=True, prog_num=25723) as shell_command_1053_25723:
                            shell_command_1053_25723()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=25724):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=25725) as should_copy_source_1054_25725:
                    should_copy_source_1054_25725()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=25726):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=25727) as copy_dir_to_dir_1055_25727:
                            copy_dir_to_dir_1055_25727()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=25728) as unwtar_1056_25728:
                            unwtar_1056_25728()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=25729, recursive=True) as chown_1057_25729:
                            chown_1057_25729()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=25730) as shell_command_1058_25730:
                            shell_command_1058_25730()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=25731) as script_command_1059_25731:
                            script_command_1059_25731()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=25732) as shell_command_1060_25732:
                            shell_command_1060_25732()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.1 v16.1.77.79", prog_num=25733):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=25734) as should_copy_source_1061_25734:
                    should_copy_source_1061_25734()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", prog_num=25735):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r".", delete_extraneous_files=True, prog_num=25736) as copy_dir_to_dir_1062_25736:
                            copy_dir_to_dir_1062_25736()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", where_to_unwtar=r".", prog_num=25737) as unwtar_1063_25737:
                            unwtar_1063_25737()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.1.bundle", user_id=-1, group_id=-1, prog_num=25738, recursive=True) as chown_1064_25738:
                            chown_1064_25738()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=25739) as shell_command_1065_25739:
                            shell_command_1065_25739()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=25740) as script_command_1066_25740:
                            script_command_1066_25740()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=25741) as shell_command_1067_25741:
                            shell_command_1067_25741()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.2 v16.2.30.56", prog_num=25742):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=25743) as should_copy_source_1068_25743:
                    should_copy_source_1068_25743()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", prog_num=25744):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r".", delete_extraneous_files=True, prog_num=25745) as copy_dir_to_dir_1069_25745:
                            copy_dir_to_dir_1069_25745()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", where_to_unwtar=r".", prog_num=25746) as unwtar_1070_25746:
                            unwtar_1070_25746()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.2.bundle", user_id=-1, group_id=-1, prog_num=25747, recursive=True) as chown_1071_25747:
                            chown_1071_25747()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=25748) as shell_command_1072_25748:
                            shell_command_1072_25748()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=25749) as script_command_1073_25749:
                            script_command_1073_25749()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=25750) as shell_command_1074_25750:
                            shell_command_1074_25750()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=25751):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=25752) as should_copy_source_1075_25752:
                    should_copy_source_1075_25752()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=25753):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=25754) as copy_dir_to_dir_1076_25754:
                            copy_dir_to_dir_1076_25754()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=25755) as unwtar_1077_25755:
                            unwtar_1077_25755()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=25756, recursive=True) as chown_1078_25756:
                            chown_1078_25756()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=25757) as shell_command_1079_25757:
                shell_command_1079_25757()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=25758) as cd_stage_1080_25758:
            cd_stage_1080_25758()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.78.79", prog_num=25759):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=25760) as should_copy_source_1081_25760:
                    should_copy_source_1081_25760()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=25761):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=25762) as copy_dir_to_dir_1082_25762:
                            copy_dir_to_dir_1082_25762()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=25763) as unwtar_1083_25763:
                            unwtar_1083_25763()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=25764, recursive=True) as chown_1084_25764:
                            chown_1084_25764()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=25765) as shell_command_1085_25765:
                            shell_command_1085_25765()
            with Stage(r"copy", r"WaveShell1-AAX 16.1 v16.1.77.79", prog_num=25766):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=25767) as should_copy_source_1086_25767:
                    should_copy_source_1086_25767()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", prog_num=25768):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", r".", delete_extraneous_files=True, prog_num=25769) as copy_dir_to_dir_1087_25769:
                            copy_dir_to_dir_1087_25769()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.1.aaxplugin", where_to_unwtar=r".", prog_num=25770) as unwtar_1088_25770:
                            unwtar_1088_25770()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.1.aaxplugin", user_id=-1, group_id=-1, prog_num=25771, recursive=True) as chown_1089_25771:
                            chown_1089_25771()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.1.aaxplugin"', ignore_all_errors=True, prog_num=25772) as shell_command_1090_25772:
                            shell_command_1090_25772()
            with Stage(r"copy", r"WaveShell1-AAX 16.2 v16.2.30.56", prog_num=25773):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=25774) as should_copy_source_1091_25774:
                    should_copy_source_1091_25774()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", prog_num=25775):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", r".", delete_extraneous_files=True, prog_num=25776) as copy_dir_to_dir_1092_25776:
                            copy_dir_to_dir_1092_25776()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.2.aaxplugin", where_to_unwtar=r".", prog_num=25777) as unwtar_1093_25777:
                            unwtar_1093_25777()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.2.aaxplugin", user_id=-1, group_id=-1, prog_num=25778, recursive=True) as chown_1094_25778:
                            chown_1094_25778()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.2.aaxplugin"', ignore_all_errors=True, prog_num=25779) as shell_command_1095_25779:
                            shell_command_1095_25779()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=25780) as cd_stage_1096_25780:
            cd_stage_1096_25780()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=25781):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25782) as should_copy_source_1097_25782:
                    should_copy_source_1097_25782()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=25783):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=25784) as copy_file_to_dir_1098_25784:
                            copy_file_to_dir_1098_25784()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25785) as chmod_and_chown_1099_25785:
                            chmod_and_chown_1099_25785()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=25786):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25787) as should_copy_source_1100_25787:
                    should_copy_source_1100_25787()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=25788):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=25789) as copy_file_to_dir_1101_25789:
                            copy_file_to_dir_1101_25789()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25790) as chmod_and_chown_1102_25790:
                            chmod_and_chown_1102_25790()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=25791):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25792) as should_copy_source_1103_25792:
                    should_copy_source_1103_25792()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=25793):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=25794) as copy_file_to_dir_1104_25794:
                            copy_file_to_dir_1104_25794()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25795) as chmod_and_chown_1105_25795:
                            chmod_and_chown_1105_25795()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=25796):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25797) as should_copy_source_1106_25797:
                    should_copy_source_1106_25797()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=25798):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=25799) as copy_file_to_dir_1107_25799:
                            copy_file_to_dir_1107_25799()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25800) as chmod_and_chown_1108_25800:
                            chmod_and_chown_1108_25800()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=25801):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25802) as should_copy_source_1109_25802:
                    should_copy_source_1109_25802()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=25803):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=25804) as copy_file_to_dir_1110_25804:
                            copy_file_to_dir_1110_25804()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25805) as chmod_and_chown_1111_25805:
                            chmod_and_chown_1111_25805()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=25806):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25807) as should_copy_source_1112_25807:
                    should_copy_source_1112_25807()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=25808):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=25809) as copy_file_to_dir_1113_25809:
                            copy_file_to_dir_1113_25809()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25810) as chmod_and_chown_1114_25810:
                            chmod_and_chown_1114_25810()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=25811):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25812) as should_copy_source_1115_25812:
                    should_copy_source_1115_25812()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=25813):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=25814) as copy_file_to_dir_1116_25814:
                            copy_file_to_dir_1116_25814()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25815) as chmod_and_chown_1117_25815:
                            chmod_and_chown_1117_25815()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=25816):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25817) as should_copy_source_1118_25817:
                    should_copy_source_1118_25817()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=25818):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=25819) as copy_file_to_dir_1119_25819:
                            copy_file_to_dir_1119_25819()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25820) as chmod_and_chown_1120_25820:
                            chmod_and_chown_1120_25820()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=25821):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25822) as should_copy_source_1121_25822:
                    should_copy_source_1121_25822()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=25823):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=25824) as copy_file_to_dir_1122_25824:
                            copy_file_to_dir_1122_25824()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25825) as chmod_and_chown_1123_25825:
                            chmod_and_chown_1123_25825()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=25826):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25827) as should_copy_source_1124_25827:
                    should_copy_source_1124_25827()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=25828):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=25829) as copy_file_to_dir_1125_25829:
                            copy_file_to_dir_1125_25829()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25830) as chmod_and_chown_1126_25830:
                            chmod_and_chown_1126_25830()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=25831):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25832) as should_copy_source_1127_25832:
                    should_copy_source_1127_25832()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=25833):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=25834) as copy_file_to_dir_1128_25834:
                            copy_file_to_dir_1128_25834()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25835) as chmod_and_chown_1129_25835:
                            chmod_and_chown_1129_25835()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=25836):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25837) as should_copy_source_1130_25837:
                    should_copy_source_1130_25837()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=25838):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=25839) as copy_file_to_dir_1131_25839:
                            copy_file_to_dir_1131_25839()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25840) as chmod_and_chown_1132_25840:
                            chmod_and_chown_1132_25840()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=25841):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25842) as should_copy_source_1133_25842:
                    should_copy_source_1133_25842()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=25843):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=25844) as copy_file_to_dir_1134_25844:
                            copy_file_to_dir_1134_25844()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25845) as chmod_and_chown_1135_25845:
                            chmod_and_chown_1135_25845()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=25846):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25847) as should_copy_source_1136_25847:
                    should_copy_source_1136_25847()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=25848):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=25849) as copy_file_to_dir_1137_25849:
                            copy_file_to_dir_1137_25849()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25850) as chmod_and_chown_1138_25850:
                            chmod_and_chown_1138_25850()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=25851):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25852) as should_copy_source_1139_25852:
                    should_copy_source_1139_25852()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=25853):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=25854) as copy_file_to_dir_1140_25854:
                            copy_file_to_dir_1140_25854()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25855) as chmod_and_chown_1141_25855:
                            chmod_and_chown_1141_25855()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=25856):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25857) as should_copy_source_1142_25857:
                    should_copy_source_1142_25857()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=25858):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=25859) as copy_file_to_dir_1143_25859:
                            copy_file_to_dir_1143_25859()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25860) as chmod_and_chown_1144_25860:
                            chmod_and_chown_1144_25860()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=25861):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25862) as should_copy_source_1145_25862:
                    should_copy_source_1145_25862()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=25863):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=25864) as copy_file_to_dir_1146_25864:
                            copy_file_to_dir_1146_25864()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25865) as chmod_and_chown_1147_25865:
                            chmod_and_chown_1147_25865()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=25866):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25867) as should_copy_source_1148_25867:
                    should_copy_source_1148_25867()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=25868):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=25869) as copy_file_to_dir_1149_25869:
                            copy_file_to_dir_1149_25869()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25870) as chmod_and_chown_1150_25870:
                            chmod_and_chown_1150_25870()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=25871):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25872) as should_copy_source_1151_25872:
                    should_copy_source_1151_25872()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=25873):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=25874) as copy_file_to_dir_1152_25874:
                            copy_file_to_dir_1152_25874()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25875) as chmod_and_chown_1153_25875:
                            chmod_and_chown_1153_25875()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=25876):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25877) as should_copy_source_1154_25877:
                    should_copy_source_1154_25877()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=25878):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=25879) as copy_file_to_dir_1155_25879:
                            copy_file_to_dir_1155_25879()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25880) as chmod_and_chown_1156_25880:
                            chmod_and_chown_1156_25880()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=25881):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25882) as should_copy_source_1157_25882:
                    should_copy_source_1157_25882()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=25883):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=25884) as copy_file_to_dir_1158_25884:
                            copy_file_to_dir_1158_25884()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25885) as chmod_and_chown_1159_25885:
                            chmod_and_chown_1159_25885()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=25886):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25887) as should_copy_source_1160_25887:
                    should_copy_source_1160_25887()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=25888):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=25889) as copy_file_to_dir_1161_25889:
                            copy_file_to_dir_1161_25889()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25890) as chmod_and_chown_1162_25890:
                            chmod_and_chown_1162_25890()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=25891):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25892) as should_copy_source_1163_25892:
                    should_copy_source_1163_25892()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=25893):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=25894) as copy_file_to_dir_1164_25894:
                            copy_file_to_dir_1164_25894()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25895) as chmod_and_chown_1165_25895:
                            chmod_and_chown_1165_25895()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=25896):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25897) as should_copy_source_1166_25897:
                    should_copy_source_1166_25897()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=25898):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=25899) as copy_file_to_dir_1167_25899:
                            copy_file_to_dir_1167_25899()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25900) as chmod_and_chown_1168_25900:
                            chmod_and_chown_1168_25900()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=25901):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25902) as should_copy_source_1169_25902:
                    should_copy_source_1169_25902()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=25903):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=25904) as copy_file_to_dir_1170_25904:
                            copy_file_to_dir_1170_25904()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25905) as chmod_and_chown_1171_25905:
                            chmod_and_chown_1171_25905()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=25906):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25907) as should_copy_source_1172_25907:
                    should_copy_source_1172_25907()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=25908):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=25909) as copy_file_to_dir_1173_25909:
                            copy_file_to_dir_1173_25909()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25910) as chmod_and_chown_1174_25910:
                            chmod_and_chown_1174_25910()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=25911):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25912) as should_copy_source_1175_25912:
                    should_copy_source_1175_25912()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=25913):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=25914) as copy_file_to_dir_1176_25914:
                            copy_file_to_dir_1176_25914()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25915) as chmod_and_chown_1177_25915:
                            chmod_and_chown_1177_25915()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=25916):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25917) as should_copy_source_1178_25917:
                    should_copy_source_1178_25917()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=25918):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=25919) as copy_file_to_dir_1179_25919:
                            copy_file_to_dir_1179_25919()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25920) as chmod_and_chown_1180_25920:
                            chmod_and_chown_1180_25920()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=25921):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25922) as should_copy_source_1181_25922:
                    should_copy_source_1181_25922()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=25923):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=25924) as copy_file_to_dir_1182_25924:
                            copy_file_to_dir_1182_25924()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25925) as chmod_and_chown_1183_25925:
                            chmod_and_chown_1183_25925()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=25926):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25927) as should_copy_source_1184_25927:
                    should_copy_source_1184_25927()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=25928):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=25929) as copy_file_to_dir_1185_25929:
                            copy_file_to_dir_1185_25929()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25930) as chmod_and_chown_1186_25930:
                            chmod_and_chown_1186_25930()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=25931):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25932) as should_copy_source_1187_25932:
                    should_copy_source_1187_25932()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=25933):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=25934) as copy_file_to_dir_1188_25934:
                            copy_file_to_dir_1188_25934()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25935) as chmod_and_chown_1189_25935:
                            chmod_and_chown_1189_25935()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=25936):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25937) as should_copy_source_1190_25937:
                    should_copy_source_1190_25937()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=25938):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=25939) as copy_file_to_dir_1191_25939:
                            copy_file_to_dir_1191_25939()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25940) as chmod_and_chown_1192_25940:
                            chmod_and_chown_1192_25940()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=25941):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25942) as should_copy_source_1193_25942:
                    should_copy_source_1193_25942()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=25943):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=25944) as copy_file_to_dir_1194_25944:
                            copy_file_to_dir_1194_25944()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25945) as chmod_and_chown_1195_25945:
                            chmod_and_chown_1195_25945()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=25946):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25947) as should_copy_source_1196_25947:
                    should_copy_source_1196_25947()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=25948):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=25949) as copy_file_to_dir_1197_25949:
                            copy_file_to_dir_1197_25949()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25950) as chmod_and_chown_1198_25950:
                            chmod_and_chown_1198_25950()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=25951):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25952) as should_copy_source_1199_25952:
                    should_copy_source_1199_25952()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=25953):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=25954) as copy_file_to_dir_1200_25954:
                            copy_file_to_dir_1200_25954()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25955) as chmod_and_chown_1201_25955:
                            chmod_and_chown_1201_25955()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=25956):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25957) as should_copy_source_1202_25957:
                    should_copy_source_1202_25957()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=25958):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=25959) as copy_file_to_dir_1203_25959:
                            copy_file_to_dir_1203_25959()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25960) as chmod_and_chown_1204_25960:
                            chmod_and_chown_1204_25960()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=25961):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25962) as should_copy_source_1205_25962:
                    should_copy_source_1205_25962()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=25963):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=25964) as copy_file_to_dir_1206_25964:
                            copy_file_to_dir_1206_25964()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25965) as chmod_and_chown_1207_25965:
                            chmod_and_chown_1207_25965()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=25966):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25967) as should_copy_source_1208_25967:
                    should_copy_source_1208_25967()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=25968):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=25969) as copy_file_to_dir_1209_25969:
                            copy_file_to_dir_1209_25969()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25970) as chmod_and_chown_1210_25970:
                            chmod_and_chown_1210_25970()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=25971):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25972) as should_copy_source_1211_25972:
                    should_copy_source_1211_25972()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=25973):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=25974) as copy_file_to_dir_1212_25974:
                            copy_file_to_dir_1212_25974()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25975) as chmod_and_chown_1213_25975:
                            chmod_and_chown_1213_25975()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=25976):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25977) as should_copy_source_1214_25977:
                    should_copy_source_1214_25977()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=25978):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=25979) as copy_file_to_dir_1215_25979:
                            copy_file_to_dir_1215_25979()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25980) as chmod_and_chown_1216_25980:
                            chmod_and_chown_1216_25980()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=25981):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25982) as should_copy_source_1217_25982:
                    should_copy_source_1217_25982()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=25983):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=25984) as copy_file_to_dir_1218_25984:
                            copy_file_to_dir_1218_25984()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25985) as chmod_and_chown_1219_25985:
                            chmod_and_chown_1219_25985()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=25986):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25987) as should_copy_source_1220_25987:
                    should_copy_source_1220_25987()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=25988):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=25989) as copy_file_to_dir_1221_25989:
                            copy_file_to_dir_1221_25989()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25990) as chmod_and_chown_1222_25990:
                            chmod_and_chown_1222_25990()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=25991):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25992) as should_copy_source_1223_25992:
                    should_copy_source_1223_25992()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=25993):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=25994) as copy_file_to_dir_1224_25994:
                            copy_file_to_dir_1224_25994()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=25995) as chmod_and_chown_1225_25995:
                            chmod_and_chown_1225_25995()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=25996):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=25997) as should_copy_source_1226_25997:
                    should_copy_source_1226_25997()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=25998):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=25999) as copy_file_to_dir_1227_25999:
                            copy_file_to_dir_1227_25999()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26000) as chmod_and_chown_1228_26000:
                            chmod_and_chown_1228_26000()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=26001):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26002) as should_copy_source_1229_26002:
                    should_copy_source_1229_26002()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=26003):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=26004) as copy_file_to_dir_1230_26004:
                            copy_file_to_dir_1230_26004()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26005) as chmod_and_chown_1231_26005:
                            chmod_and_chown_1231_26005()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=26006):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26007) as should_copy_source_1232_26007:
                    should_copy_source_1232_26007()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=26008):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=26009) as copy_file_to_dir_1233_26009:
                            copy_file_to_dir_1233_26009()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26010) as chmod_and_chown_1234_26010:
                            chmod_and_chown_1234_26010()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=26011):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26012) as should_copy_source_1235_26012:
                    should_copy_source_1235_26012()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=26013):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=26014) as copy_file_to_dir_1236_26014:
                            copy_file_to_dir_1236_26014()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26015) as chmod_and_chown_1237_26015:
                            chmod_and_chown_1237_26015()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=26016):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26017) as should_copy_source_1238_26017:
                    should_copy_source_1238_26017()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=26018):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=26019) as copy_file_to_dir_1239_26019:
                            copy_file_to_dir_1239_26019()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26020) as chmod_and_chown_1240_26020:
                            chmod_and_chown_1240_26020()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26021) as should_copy_source_1241_26021:
                    should_copy_source_1241_26021()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=26022):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=26023) as copy_file_to_dir_1242_26023:
                            copy_file_to_dir_1242_26023()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26024) as chmod_and_chown_1243_26024:
                            chmod_and_chown_1243_26024()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=26025):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26026) as should_copy_source_1244_26026:
                    should_copy_source_1244_26026()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=26027):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=26028) as copy_file_to_dir_1245_26028:
                            copy_file_to_dir_1245_26028()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26029) as chmod_and_chown_1246_26029:
                            chmod_and_chown_1246_26029()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=26030):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26031) as should_copy_source_1247_26031:
                    should_copy_source_1247_26031()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=26032):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=26033) as copy_file_to_dir_1248_26033:
                            copy_file_to_dir_1248_26033()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26034) as chmod_and_chown_1249_26034:
                            chmod_and_chown_1249_26034()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=26035):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26036) as should_copy_source_1250_26036:
                    should_copy_source_1250_26036()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=26037):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=26038) as copy_file_to_dir_1251_26038:
                            copy_file_to_dir_1251_26038()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26039) as chmod_and_chown_1252_26039:
                            chmod_and_chown_1252_26039()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=26040):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26041) as should_copy_source_1253_26041:
                    should_copy_source_1253_26041()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=26042):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=26043) as copy_file_to_dir_1254_26043:
                            copy_file_to_dir_1254_26043()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26044) as chmod_and_chown_1255_26044:
                            chmod_and_chown_1255_26044()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=26045):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26046) as should_copy_source_1256_26046:
                    should_copy_source_1256_26046()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=26047):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=26048) as copy_file_to_dir_1257_26048:
                            copy_file_to_dir_1257_26048()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26049) as chmod_and_chown_1258_26049:
                            chmod_and_chown_1258_26049()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=26050):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26051) as should_copy_source_1259_26051:
                    should_copy_source_1259_26051()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=26052):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=26053) as copy_file_to_dir_1260_26053:
                            copy_file_to_dir_1260_26053()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26054) as chmod_and_chown_1261_26054:
                            chmod_and_chown_1261_26054()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=26055):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26056) as should_copy_source_1262_26056:
                    should_copy_source_1262_26056()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=26057):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=26058) as copy_file_to_dir_1263_26058:
                            copy_file_to_dir_1263_26058()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26059) as chmod_and_chown_1264_26059:
                            chmod_and_chown_1264_26059()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=26060):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26061) as should_copy_source_1265_26061:
                    should_copy_source_1265_26061()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=26062):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=26063) as copy_file_to_dir_1266_26063:
                            copy_file_to_dir_1266_26063()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26064) as chmod_and_chown_1267_26064:
                            chmod_and_chown_1267_26064()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=26065):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26066) as should_copy_source_1268_26066:
                    should_copy_source_1268_26066()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=26067):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=26068) as copy_file_to_dir_1269_26068:
                            copy_file_to_dir_1269_26068()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26069) as chmod_and_chown_1270_26069:
                            chmod_and_chown_1270_26069()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=26070):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26071) as should_copy_source_1271_26071:
                    should_copy_source_1271_26071()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=26072):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=26073) as copy_file_to_dir_1272_26073:
                            copy_file_to_dir_1272_26073()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26074) as chmod_and_chown_1273_26074:
                            chmod_and_chown_1273_26074()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=26075):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26076) as should_copy_source_1274_26076:
                    should_copy_source_1274_26076()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=26077):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=26078) as copy_file_to_dir_1275_26078:
                            copy_file_to_dir_1275_26078()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26079) as chmod_and_chown_1276_26079:
                            chmod_and_chown_1276_26079()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=26080):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26081) as should_copy_source_1277_26081:
                    should_copy_source_1277_26081()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=26082):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=26083) as copy_file_to_dir_1278_26083:
                            copy_file_to_dir_1278_26083()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26084) as chmod_and_chown_1279_26084:
                            chmod_and_chown_1279_26084()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=26085):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26086) as should_copy_source_1280_26086:
                    should_copy_source_1280_26086()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=26087):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=26088) as copy_file_to_dir_1281_26088:
                            copy_file_to_dir_1281_26088()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26089) as chmod_and_chown_1282_26089:
                            chmod_and_chown_1282_26089()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=26090):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26091) as should_copy_source_1283_26091:
                    should_copy_source_1283_26091()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=26092):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=26093) as copy_file_to_dir_1284_26093:
                            copy_file_to_dir_1284_26093()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26094) as chmod_and_chown_1285_26094:
                            chmod_and_chown_1285_26094()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=26095):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26096) as should_copy_source_1286_26096:
                    should_copy_source_1286_26096()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=26097):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=26098) as copy_file_to_dir_1287_26098:
                            copy_file_to_dir_1287_26098()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26099) as chmod_and_chown_1288_26099:
                            chmod_and_chown_1288_26099()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=26100):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26101) as should_copy_source_1289_26101:
                    should_copy_source_1289_26101()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=26102):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=26103) as copy_file_to_dir_1290_26103:
                            copy_file_to_dir_1290_26103()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26104) as chmod_and_chown_1291_26104:
                            chmod_and_chown_1291_26104()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=26105):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26106) as should_copy_source_1292_26106:
                    should_copy_source_1292_26106()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=26107):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=26108) as copy_file_to_dir_1293_26108:
                            copy_file_to_dir_1293_26108()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26109) as chmod_and_chown_1294_26109:
                            chmod_and_chown_1294_26109()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=26110):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26111) as should_copy_source_1295_26111:
                    should_copy_source_1295_26111()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=26112):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=26113) as copy_file_to_dir_1296_26113:
                            copy_file_to_dir_1296_26113()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26114) as chmod_and_chown_1297_26114:
                            chmod_and_chown_1297_26114()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=26115):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26116) as should_copy_source_1298_26116:
                    should_copy_source_1298_26116()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=26117):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=26118) as copy_file_to_dir_1299_26118:
                            copy_file_to_dir_1299_26118()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26119) as chmod_and_chown_1300_26119:
                            chmod_and_chown_1300_26119()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=26120):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26121) as should_copy_source_1301_26121:
                    should_copy_source_1301_26121()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=26122):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=26123) as copy_file_to_dir_1302_26123:
                            copy_file_to_dir_1302_26123()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26124) as chmod_and_chown_1303_26124:
                            chmod_and_chown_1303_26124()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=26125):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26126) as should_copy_source_1304_26126:
                    should_copy_source_1304_26126()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=26127):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=26128) as copy_file_to_dir_1305_26128:
                            copy_file_to_dir_1305_26128()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26129) as chmod_and_chown_1306_26129:
                            chmod_and_chown_1306_26129()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=26130):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26131) as should_copy_source_1307_26131:
                    should_copy_source_1307_26131()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=26132):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=26133) as copy_file_to_dir_1308_26133:
                            copy_file_to_dir_1308_26133()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26134) as chmod_and_chown_1309_26134:
                            chmod_and_chown_1309_26134()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=26135):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26136) as should_copy_source_1310_26136:
                    should_copy_source_1310_26136()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=26137):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=26138) as copy_file_to_dir_1311_26138:
                            copy_file_to_dir_1311_26138()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26139) as chmod_and_chown_1312_26139:
                            chmod_and_chown_1312_26139()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=26140):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26141) as should_copy_source_1313_26141:
                    should_copy_source_1313_26141()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=26142):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=26143) as copy_file_to_dir_1314_26143:
                            copy_file_to_dir_1314_26143()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26144) as chmod_and_chown_1315_26144:
                            chmod_and_chown_1315_26144()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=26145):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26146) as should_copy_source_1316_26146:
                    should_copy_source_1316_26146()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=26147):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=26148) as copy_file_to_dir_1317_26148:
                            copy_file_to_dir_1317_26148()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26149) as chmod_and_chown_1318_26149:
                            chmod_and_chown_1318_26149()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=26150):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26151) as should_copy_source_1319_26151:
                    should_copy_source_1319_26151()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=26152):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=26153) as copy_file_to_dir_1320_26153:
                            copy_file_to_dir_1320_26153()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26154) as chmod_and_chown_1321_26154:
                            chmod_and_chown_1321_26154()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=26155):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26156) as should_copy_source_1322_26156:
                    should_copy_source_1322_26156()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=26157):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=26158) as copy_file_to_dir_1323_26158:
                            copy_file_to_dir_1323_26158()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26159) as chmod_and_chown_1324_26159:
                            chmod_and_chown_1324_26159()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=26160):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26161) as should_copy_source_1325_26161:
                    should_copy_source_1325_26161()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=26162):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=26163) as copy_file_to_dir_1326_26163:
                            copy_file_to_dir_1326_26163()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26164) as chmod_and_chown_1327_26164:
                            chmod_and_chown_1327_26164()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26165) as should_copy_source_1328_26165:
                    should_copy_source_1328_26165()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=26166):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=26167) as copy_file_to_dir_1329_26167:
                            copy_file_to_dir_1329_26167()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26168) as chmod_and_chown_1330_26168:
                            chmod_and_chown_1330_26168()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26169) as should_copy_source_1331_26169:
                    should_copy_source_1331_26169()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=26170):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=26171) as copy_file_to_dir_1332_26171:
                            copy_file_to_dir_1332_26171()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26172) as chmod_and_chown_1333_26172:
                            chmod_and_chown_1333_26172()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=26173):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26174) as should_copy_source_1334_26174:
                    should_copy_source_1334_26174()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=26175):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=26176) as copy_file_to_dir_1335_26176:
                            copy_file_to_dir_1335_26176()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26177) as chmod_and_chown_1336_26177:
                            chmod_and_chown_1336_26177()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=26178):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26179) as should_copy_source_1337_26179:
                    should_copy_source_1337_26179()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=26180):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=26181) as copy_file_to_dir_1338_26181:
                            copy_file_to_dir_1338_26181()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26182) as chmod_and_chown_1339_26182:
                            chmod_and_chown_1339_26182()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=26183):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26184) as should_copy_source_1340_26184:
                    should_copy_source_1340_26184()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=26185):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=26186) as copy_file_to_dir_1341_26186:
                            copy_file_to_dir_1341_26186()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26187) as chmod_and_chown_1342_26187:
                            chmod_and_chown_1342_26187()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=26188):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26189) as should_copy_source_1343_26189:
                    should_copy_source_1343_26189()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=26190):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=26191) as copy_file_to_dir_1344_26191:
                            copy_file_to_dir_1344_26191()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26192) as chmod_and_chown_1345_26192:
                            chmod_and_chown_1345_26192()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=26193):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26194) as should_copy_source_1346_26194:
                    should_copy_source_1346_26194()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=26195):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=26196) as copy_file_to_dir_1347_26196:
                            copy_file_to_dir_1347_26196()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26197) as chmod_and_chown_1348_26197:
                            chmod_and_chown_1348_26197()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=26198):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26199) as should_copy_source_1349_26199:
                    should_copy_source_1349_26199()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=26200):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=26201) as copy_file_to_dir_1350_26201:
                            copy_file_to_dir_1350_26201()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26202) as chmod_and_chown_1351_26202:
                            chmod_and_chown_1351_26202()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=26203):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26204) as should_copy_source_1352_26204:
                    should_copy_source_1352_26204()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=26205):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=26206) as copy_file_to_dir_1353_26206:
                            copy_file_to_dir_1353_26206()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26207) as chmod_and_chown_1354_26207:
                            chmod_and_chown_1354_26207()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=26208):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=26209) as should_copy_source_1355_26209:
                    should_copy_source_1355_26209()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=26210):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=26211) as copy_file_to_dir_1356_26211:
                            copy_file_to_dir_1356_26211()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=26212) as chmod_and_chown_1357_26212:
                            chmod_and_chown_1357_26212()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=26213) as resolve_config_vars_in_file_1358_26213:
                resolve_config_vars_in_file_1358_26213()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=26214) as if_1359_26214:
                if_1359_26214()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=26215) as resolve_config_vars_in_file_1360_26215:
                resolve_config_vars_in_file_1360_26215()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=26216) as if_1361_26216:
                if_1361_26216()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=26217) as resolve_config_vars_in_file_1362_26217:
                resolve_config_vars_in_file_1362_26217()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=26218) as if_1363_26218:
                if_1363_26218()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=26219) as resolve_config_vars_in_file_1364_26219:
                resolve_config_vars_in_file_1364_26219()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=26220) as if_1365_26220:
                if_1365_26220()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=26221) as resolve_config_vars_in_file_1366_26221:
                resolve_config_vars_in_file_1366_26221()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=26222) as if_1367_26222:
                if_1367_26222()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=26223) as resolve_config_vars_in_file_1368_26223:
                resolve_config_vars_in_file_1368_26223()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=26224) as if_1369_26224:
                if_1369_26224()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=26225) as resolve_config_vars_in_file_1370_26225:
                resolve_config_vars_in_file_1370_26225()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=26226) as if_1371_26226:
                if_1371_26226()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=26227) as resolve_config_vars_in_file_1372_26227:
                resolve_config_vars_in_file_1372_26227()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=26228) as if_1373_26228:
                if_1373_26228()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=26229) as resolve_config_vars_in_file_1374_26229:
                resolve_config_vars_in_file_1374_26229()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=26230) as if_1375_26230:
                if_1375_26230()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=26231) as resolve_config_vars_in_file_1376_26231:
                resolve_config_vars_in_file_1376_26231()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=26232) as if_1377_26232:
                if_1377_26232()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=26233) as resolve_config_vars_in_file_1378_26233:
                resolve_config_vars_in_file_1378_26233()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=26234) as if_1379_26234:
                if_1379_26234()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=26235) as resolve_config_vars_in_file_1380_26235:
                resolve_config_vars_in_file_1380_26235()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=26236) as if_1381_26236:
                if_1381_26236()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=26237) as resolve_config_vars_in_file_1382_26237:
                resolve_config_vars_in_file_1382_26237()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=26238) as if_1383_26238:
                if_1383_26238()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=26239) as resolve_config_vars_in_file_1384_26239:
                resolve_config_vars_in_file_1384_26239()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=26240) as if_1385_26240:
                if_1385_26240()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=26241) as resolve_config_vars_in_file_1386_26241:
                resolve_config_vars_in_file_1386_26241()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=26242) as if_1387_26242:
                if_1387_26242()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=26243) as resolve_config_vars_in_file_1388_26243:
                resolve_config_vars_in_file_1388_26243()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=26244) as if_1389_26244:
                if_1389_26244()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=26245) as resolve_config_vars_in_file_1390_26245:
                resolve_config_vars_in_file_1390_26245()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=26246) as if_1391_26246:
                if_1391_26246()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=26247) as resolve_config_vars_in_file_1392_26247:
                resolve_config_vars_in_file_1392_26247()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=26248) as if_1393_26248:
                if_1393_26248()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=26249) as resolve_config_vars_in_file_1394_26249:
                resolve_config_vars_in_file_1394_26249()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=26250) as if_1395_26250:
                if_1395_26250()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=26251) as resolve_config_vars_in_file_1396_26251:
                resolve_config_vars_in_file_1396_26251()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=26252) as if_1397_26252:
                if_1397_26252()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=26253) as resolve_config_vars_in_file_1398_26253:
                resolve_config_vars_in_file_1398_26253()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=26254) as if_1399_26254:
                if_1399_26254()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=26255) as resolve_config_vars_in_file_1400_26255:
                resolve_config_vars_in_file_1400_26255()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=26256) as if_1401_26256:
                if_1401_26256()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=26257) as resolve_config_vars_in_file_1402_26257:
                resolve_config_vars_in_file_1402_26257()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=26258) as if_1403_26258:
                if_1403_26258()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=26259) as resolve_config_vars_in_file_1404_26259:
                resolve_config_vars_in_file_1404_26259()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=26260) as if_1405_26260:
                if_1405_26260()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=26261) as rm_file_or_dir_1406_26261:
                rm_file_or_dir_1406_26261()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=26262) as resolve_config_vars_in_file_1407_26262:
                resolve_config_vars_in_file_1407_26262()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=26263) as if_1408_26263:
                if_1408_26263()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=26264) as rm_file_or_dir_1409_26264:
                rm_file_or_dir_1409_26264()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=26265) as resolve_config_vars_in_file_1410_26265:
                resolve_config_vars_in_file_1410_26265()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=26266) as if_1411_26266:
                if_1411_26266()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=26267) as resolve_config_vars_in_file_1412_26267:
                resolve_config_vars_in_file_1412_26267()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=26268) as if_1413_26268:
                if_1413_26268()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=26269) as resolve_config_vars_in_file_1414_26269:
                resolve_config_vars_in_file_1414_26269()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=26270) as if_1415_26270:
                if_1415_26270()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=26271) as resolve_config_vars_in_file_1416_26271:
                resolve_config_vars_in_file_1416_26271()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=26272) as if_1417_26272:
                if_1417_26272()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=26273) as resolve_config_vars_in_file_1418_26273:
                resolve_config_vars_in_file_1418_26273()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=26274) as if_1419_26274:
                if_1419_26274()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=26275) as resolve_config_vars_in_file_1420_26275:
                resolve_config_vars_in_file_1420_26275()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=26276) as if_1421_26276:
                if_1421_26276()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=26277) as resolve_config_vars_in_file_1422_26277:
                resolve_config_vars_in_file_1422_26277()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=26278) as if_1423_26278:
                if_1423_26278()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=26279) as resolve_config_vars_in_file_1424_26279:
                resolve_config_vars_in_file_1424_26279()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=26280) as if_1425_26280:
                if_1425_26280()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=26281) as resolve_config_vars_in_file_1426_26281:
                resolve_config_vars_in_file_1426_26281()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=26282) as if_1427_26282:
                if_1427_26282()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=26283) as resolve_config_vars_in_file_1428_26283:
                resolve_config_vars_in_file_1428_26283()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=26284) as if_1429_26284:
                if_1429_26284()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=26285) as resolve_config_vars_in_file_1430_26285:
                resolve_config_vars_in_file_1430_26285()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=26286) as if_1431_26286:
                if_1431_26286()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=26287) as resolve_config_vars_in_file_1432_26287:
                resolve_config_vars_in_file_1432_26287()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=26288) as if_1433_26288:
                if_1433_26288()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=26289) as resolve_config_vars_in_file_1434_26289:
                resolve_config_vars_in_file_1434_26289()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=26290) as if_1435_26290:
                if_1435_26290()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=26291) as resolve_config_vars_in_file_1436_26291:
                resolve_config_vars_in_file_1436_26291()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=26292) as if_1437_26292:
                if_1437_26292()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=26293) as resolve_config_vars_in_file_1438_26293:
                resolve_config_vars_in_file_1438_26293()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=26294) as if_1439_26294:
                if_1439_26294()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=26295) as resolve_config_vars_in_file_1440_26295:
                resolve_config_vars_in_file_1440_26295()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=26296) as if_1441_26296:
                if_1441_26296()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=26297) as resolve_config_vars_in_file_1442_26297:
                resolve_config_vars_in_file_1442_26297()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=26298) as if_1443_26298:
                if_1443_26298()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=26299) as resolve_config_vars_in_file_1444_26299:
                resolve_config_vars_in_file_1444_26299()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=26300) as if_1445_26300:
                if_1445_26300()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=26301) as resolve_config_vars_in_file_1446_26301:
                resolve_config_vars_in_file_1446_26301()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=26302) as if_1447_26302:
                if_1447_26302()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=26303) as resolve_config_vars_in_file_1448_26303:
                resolve_config_vars_in_file_1448_26303()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=26304) as if_1449_26304:
                if_1449_26304()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=26305) as resolve_config_vars_in_file_1450_26305:
                resolve_config_vars_in_file_1450_26305()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=26306) as if_1451_26306:
                if_1451_26306()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=26307) as resolve_config_vars_in_file_1452_26307:
                resolve_config_vars_in_file_1452_26307()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=26308) as if_1453_26308:
                if_1453_26308()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=26309) as resolve_config_vars_in_file_1454_26309:
                resolve_config_vars_in_file_1454_26309()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=26310) as if_1455_26310:
                if_1455_26310()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=26311) as move_file_to_file_1456_26311:
                move_file_to_file_1456_26311()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=26312) as resolve_config_vars_in_file_1457_26312:
                resolve_config_vars_in_file_1457_26312()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=26313) as if_1458_26313:
                if_1458_26313()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=26314) as resolve_config_vars_in_file_1459_26314:
                resolve_config_vars_in_file_1459_26314()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=26315) as if_1460_26315:
                if_1460_26315()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=26316) as resolve_config_vars_in_file_1461_26316:
                resolve_config_vars_in_file_1461_26316()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=26317) as if_1462_26317:
                if_1462_26317()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=26318) as resolve_config_vars_in_file_1463_26318:
                resolve_config_vars_in_file_1463_26318()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=26319) as if_1464_26319:
                if_1464_26319()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=26320) as resolve_config_vars_in_file_1465_26320:
                resolve_config_vars_in_file_1465_26320()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=26321) as if_1466_26321:
                if_1466_26321()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=26322) as resolve_config_vars_in_file_1467_26322:
                resolve_config_vars_in_file_1467_26322()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=26323) as if_1468_26323:
                if_1468_26323()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=26324) as resolve_config_vars_in_file_1469_26324:
                resolve_config_vars_in_file_1469_26324()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=26325) as if_1470_26325:
                if_1470_26325()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=26326) as resolve_config_vars_in_file_1471_26326:
                resolve_config_vars_in_file_1471_26326()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=26327) as if_1472_26327:
                if_1472_26327()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=26328) as resolve_config_vars_in_file_1473_26328:
                resolve_config_vars_in_file_1473_26328()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=26329) as if_1474_26329:
                if_1474_26329()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=26330) as resolve_config_vars_in_file_1475_26330:
                resolve_config_vars_in_file_1475_26330()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=26331) as if_1476_26331:
                if_1476_26331()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=26332) as resolve_config_vars_in_file_1477_26332:
                resolve_config_vars_in_file_1477_26332()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=26333) as if_1478_26333:
                if_1478_26333()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=26334) as resolve_config_vars_in_file_1479_26334:
                resolve_config_vars_in_file_1479_26334()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=26335) as if_1480_26335:
                if_1480_26335()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=26336) as resolve_config_vars_in_file_1481_26336:
                resolve_config_vars_in_file_1481_26336()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=26337) as if_1482_26337:
                if_1482_26337()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=26338) as resolve_config_vars_in_file_1483_26338:
                resolve_config_vars_in_file_1483_26338()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=26339) as if_1484_26339:
                if_1484_26339()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=26340) as resolve_config_vars_in_file_1485_26340:
                resolve_config_vars_in_file_1485_26340()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=26341) as if_1486_26341:
                if_1486_26341()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=26342) as resolve_config_vars_in_file_1487_26342:
                resolve_config_vars_in_file_1487_26342()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=26343) as if_1488_26343:
                if_1488_26343()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=26344) as resolve_config_vars_in_file_1489_26344:
                resolve_config_vars_in_file_1489_26344()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=26345) as if_1490_26345:
                if_1490_26345()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=26346) as resolve_config_vars_in_file_1491_26346:
                resolve_config_vars_in_file_1491_26346()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=26347) as if_1492_26347:
                if_1492_26347()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=26348) as resolve_config_vars_in_file_1493_26348:
                resolve_config_vars_in_file_1493_26348()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=26349) as if_1494_26349:
                if_1494_26349()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=26350) as resolve_config_vars_in_file_1495_26350:
                resolve_config_vars_in_file_1495_26350()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=26351) as if_1496_26351:
                if_1496_26351()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=26352) as resolve_config_vars_in_file_1497_26352:
                resolve_config_vars_in_file_1497_26352()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=26353) as if_1498_26353:
                if_1498_26353()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=26354) as resolve_config_vars_in_file_1499_26354:
                resolve_config_vars_in_file_1499_26354()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=26355) as if_1500_26355:
                if_1500_26355()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=26356) as resolve_config_vars_in_file_1501_26356:
                resolve_config_vars_in_file_1501_26356()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=26357) as if_1502_26357:
                if_1502_26357()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=26358) as resolve_config_vars_in_file_1503_26358:
                resolve_config_vars_in_file_1503_26358()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=26359) as if_1504_26359:
                if_1504_26359()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=26360) as resolve_config_vars_in_file_1505_26360:
                resolve_config_vars_in_file_1505_26360()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=26361) as if_1506_26361:
                if_1506_26361()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=26362) as resolve_config_vars_in_file_1507_26362:
                resolve_config_vars_in_file_1507_26362()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=26363) as if_1508_26363:
                if_1508_26363()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=26364) as resolve_config_vars_in_file_1509_26364:
                resolve_config_vars_in_file_1509_26364()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=26365) as if_1510_26365:
                if_1510_26365()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=26366) as resolve_config_vars_in_file_1511_26366:
                resolve_config_vars_in_file_1511_26366()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=26367) as if_1512_26367:
                if_1512_26367()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=26368) as rm_file_or_dir_1513_26368:
                rm_file_or_dir_1513_26368()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=26369) as rm_file_or_dir_1514_26369:
                rm_file_or_dir_1514_26369()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=26370) as rm_file_or_dir_1515_26370:
                rm_file_or_dir_1515_26370()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=26371) as resolve_config_vars_in_file_1516_26371:
                resolve_config_vars_in_file_1516_26371()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=26372) as if_1517_26372:
                if_1517_26372()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=26373) as resolve_config_vars_in_file_1518_26373:
                resolve_config_vars_in_file_1518_26373()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=26374) as if_1519_26374:
                if_1519_26374()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=26375) as resolve_config_vars_in_file_1520_26375:
                resolve_config_vars_in_file_1520_26375()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=26376) as if_1521_26376:
                if_1521_26376()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=26377) as rm_file_or_dir_1522_26377:
                rm_file_or_dir_1522_26377()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=26378) as rm_file_or_dir_1523_26378:
                rm_file_or_dir_1523_26378()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=26379) as rm_file_or_dir_1524_26379:
                rm_file_or_dir_1524_26379()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=26380) as resolve_config_vars_in_file_1525_26380:
                resolve_config_vars_in_file_1525_26380()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=26381) as if_1526_26381:
                if_1526_26381()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=26382) as resolve_config_vars_in_file_1527_26382:
                resolve_config_vars_in_file_1527_26382()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=26383) as if_1528_26383:
                if_1528_26383()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=26384) as resolve_config_vars_in_file_1529_26384:
                resolve_config_vars_in_file_1529_26384()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=26385) as if_1530_26385:
                if_1530_26385()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=26386) as resolve_config_vars_in_file_1531_26386:
                resolve_config_vars_in_file_1531_26386()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=26387) as if_1532_26387:
                if_1532_26387()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=26388) as resolve_config_vars_in_file_1533_26388:
                resolve_config_vars_in_file_1533_26388()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=26389) as if_1534_26389:
                if_1534_26389()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=26390) as resolve_config_vars_in_file_1535_26390:
                resolve_config_vars_in_file_1535_26390()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=26391) as if_1536_26391:
                if_1536_26391()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=26392) as resolve_config_vars_in_file_1537_26392:
                resolve_config_vars_in_file_1537_26392()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=26393) as if_1538_26393:
                if_1538_26393()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=26394) as resolve_config_vars_in_file_1539_26394:
                resolve_config_vars_in_file_1539_26394()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=26395) as if_1540_26395:
                if_1540_26395()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=26396) as cd_stage_1541_26396:
            cd_stage_1541_26396()
            with Stage(r"copy", r"COSMOS_HTML v2.6.6", prog_num=26397):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=26398) as should_copy_source_1542_26398:
                    should_copy_source_1542_26398()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=26399):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=26400) as copy_dir_to_dir_1543_26400:
                            copy_dir_to_dir_1543_26400()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=26401, recursive=True) as chown_1544_26401:
                            chown_1544_26401()
            with Stage(r"copy", r"COSMOS_python v2.7.7", prog_num=26402):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=26403) as should_copy_source_1545_26403:
                    should_copy_source_1545_26403()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=26404):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=26405) as copy_dir_to_dir_1546_26405:
                            copy_dir_to_dir_1546_26405()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=26406) as unwtar_1547_26406:
                            unwtar_1547_26406()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=26407, recursive=True) as chown_1548_26407:
                            chown_1548_26407()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=26408) as cd_stage_1549_26408:
            cd_stage_1549_26408()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=26409):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=26410) as should_copy_source_1550_26410:
                    should_copy_source_1550_26410()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=26411):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=26412) as copy_dir_to_dir_1551_26412:
                            copy_dir_to_dir_1551_26412()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=26413) as unwtar_1552_26413:
                            unwtar_1552_26413()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=26414, recursive=True) as chown_1553_26414:
                            chown_1553_26414()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=26415) as cd_stage_1554_26415:
            cd_stage_1554_26415()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=26416):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=26417) as should_copy_source_1555_26417:
                    should_copy_source_1555_26417()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=26418):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=26419) as copy_dir_to_dir_1556_26419:
                            copy_dir_to_dir_1556_26419()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=26420, recursive=True) as chown_1557_26420:
                            chown_1557_26420()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=26421) as cd_stage_1558_26421:
            cd_stage_1558_26421()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=26422):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=26423) as should_copy_source_1559_26423:
                    should_copy_source_1559_26423()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=26424):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=26425) as copy_dir_to_dir_1560_26425:
                            copy_dir_to_dir_1560_26425()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=26426, recursive=True) as chown_1561_26426:
                            chown_1561_26426()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=26427) as cd_stage_1562_26427:
            cd_stage_1562_26427()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=26428) as rm_file_or_dir_1563_26428:
                rm_file_or_dir_1563_26428()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=26429):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=26430) as should_copy_source_1564_26430:
                    should_copy_source_1564_26430()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=26431):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=26432) as copy_dir_to_dir_1565_26432:
                            copy_dir_to_dir_1565_26432()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=26433) as unwtar_1566_26433:
                            unwtar_1566_26433()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=26434, recursive=True) as chown_1567_26434:
                            chown_1567_26434()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=26435):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=26436) as should_copy_source_1568_26436:
                    should_copy_source_1568_26436()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=26437):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=26438) as unwtar_1569_26438:
                            unwtar_1569_26438()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=26439):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=26440) as should_copy_source_1570_26440:
                    should_copy_source_1570_26440()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=26441):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=26442) as copy_dir_to_dir_1571_26442:
                            copy_dir_to_dir_1571_26442()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=26443) as unwtar_1572_26443:
                            unwtar_1572_26443()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=26444, recursive=True) as chown_1573_26444:
                            chown_1573_26444()
            with Stage(r"copy", r"onnxruntime_1.19.0 v1.19.0", prog_num=26445):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=26446) as should_copy_source_1574_26446:
                    should_copy_source_1574_26446()
                    with Stage(r"copy source", r"Mac/Modules/onnxruntime", prog_num=26447):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r".", delete_extraneous_files=True, prog_num=26448) as copy_dir_to_dir_1575_26448:
                            copy_dir_to_dir_1575_26448()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", where_to_unwtar=r".", prog_num=26449) as unwtar_1576_26449:
                            unwtar_1576_26449()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/onnxruntime", user_id=-1, group_id=-1, prog_num=26450, recursive=True) as chown_1577_26450:
                            chown_1577_26450()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=26451):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=26452) as should_copy_source_1578_26452:
                    should_copy_source_1578_26452()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=26453):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=26454) as copy_dir_to_dir_1579_26454:
                            copy_dir_to_dir_1579_26454()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=26455) as chmod_1580_26455:
                            chmod_1580_26455()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=26456) as chmod_1581_26456:
                            chmod_1581_26456()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=26457, recursive=True) as chown_1582_26457:
                            chown_1582_26457()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=26460) as resolve_symlink_files_in_folder_1583_26460:
                resolve_symlink_files_in_folder_1583_26460()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=26461) as shell_command_1584_26461:
                shell_command_1584_26461()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=26462) as cd_stage_1585_26462:
            cd_stage_1585_26462()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=26463):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=26464) as should_copy_source_1586_26464:
                    should_copy_source_1586_26464()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=26465):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=26466) as copy_dir_to_dir_1587_26466:
                            copy_dir_to_dir_1587_26466()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=26467, recursive=True) as chown_1588_26467:
                            chown_1588_26467()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=26468) as cd_stage_1589_26468:
            cd_stage_1589_26468()
            with Stage(r"copy", r"Waves Local Server v12.16.44.45", prog_num=26469):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=26470) as should_copy_source_1590_26470:
                    should_copy_source_1590_26470()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=26471):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=26472, recursive=True) as chmod_1591_26472:
                            chmod_1591_26472()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=26473) as copy_dir_to_dir_1592_26473:
                            copy_dir_to_dir_1592_26473()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=26474) as unwtar_1593_26474:
                            unwtar_1593_26474()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=26475, recursive=True) as chown_1594_26475:
                            chown_1594_26475()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=26476) as if_1595_26476:
                            if_1595_26476()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=26477) as cd_stage_1596_26477:
            cd_stage_1596_26477()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=26478):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=26479) as should_copy_source_1597_26479:
                    should_copy_source_1597_26479()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=26480):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=26481, recursive=True) as chmod_1598_26481:
                            chmod_1598_26481()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=26482) as copy_dir_to_dir_1599_26482:
                            copy_dir_to_dir_1599_26482()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=26483) as unwtar_1600_26483:
                            unwtar_1600_26483()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=26484, recursive=True) as chown_1601_26484:
                            chown_1601_26484()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=26485) as if_1602_26485:
                            if_1602_26485()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=26486) as cd_stage_1603_26486:
            cd_stage_1603_26486()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=26487):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=26488) as should_copy_source_1604_26488:
                    should_copy_source_1604_26488()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=26489):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=26490) as copy_dir_to_dir_1605_26490:
                            copy_dir_to_dir_1605_26490()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=26491) as unwtar_1606_26491:
                            unwtar_1606_26491()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=26492, recursive=True) as chown_1607_26492:
                            chown_1607_26492()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=26493) as break_hard_link_1608_26493:
                            break_hard_link_1608_26493()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=26494) as shell_command_1609_26494:
                            shell_command_1609_26494()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=26495, recursive=True) as chown_1610_26495:
                            chown_1610_26495()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=26496, recursive=True) as chmod_1611_26496:
                            chmod_1611_26496()
            with Stage(r"copy", r"WaveShell1-AU 16.1 v16.1.77.79", prog_num=26497):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=26498) as should_copy_source_1612_26498:
                    should_copy_source_1612_26498()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.1.component", prog_num=26499):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", r".", delete_extraneous_files=True, prog_num=26500) as copy_dir_to_dir_1613_26500:
                            copy_dir_to_dir_1613_26500()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.1.component", where_to_unwtar=r".", prog_num=26501) as unwtar_1614_26501:
                            unwtar_1614_26501()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=26502, recursive=True) as chown_1615_26502:
                            chown_1615_26502()
                        with BreakHardLink(r"WaveShell1-AU 16.1.component/Contents/Info.plist", prog_num=26503) as break_hard_link_1616_26503:
                            break_hard_link_1616_26503()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.1.component"', ignore_all_errors=True, prog_num=26504) as shell_command_1617_26504:
                            shell_command_1617_26504()
                        with Chown(path=r"WaveShell1-AU 16.1.component", user_id=-1, group_id=-1, prog_num=26505, recursive=True) as chown_1618_26505:
                            chown_1618_26505()
                        with Chmod(path=r"WaveShell1-AU 16.1.component", mode="a+rwX", prog_num=26506, recursive=True) as chmod_1619_26506:
                            chmod_1619_26506()
            with Stage(r"copy", r"WaveShell1-AU 16.2.component v16.2.30.56", prog_num=26507):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=26508) as should_copy_source_1620_26508:
                    should_copy_source_1620_26508()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.2.component", prog_num=26509):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", r".", delete_extraneous_files=True, prog_num=26510) as copy_dir_to_dir_1621_26510:
                            copy_dir_to_dir_1621_26510()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.2.component", where_to_unwtar=r".", prog_num=26511) as unwtar_1622_26511:
                            unwtar_1622_26511()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=26512, recursive=True) as chown_1623_26512:
                            chown_1623_26512()
                        with BreakHardLink(r"WaveShell1-AU 16.2.component/Contents/Info.plist", prog_num=26513) as break_hard_link_1624_26513:
                            break_hard_link_1624_26513()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.2.component"', ignore_all_errors=True, prog_num=26514) as shell_command_1625_26514:
                            shell_command_1625_26514()
                        with Chown(path=r"WaveShell1-AU 16.2.component", user_id=-1, group_id=-1, prog_num=26515, recursive=True) as chown_1626_26515:
                            chown_1626_26515()
                        with Chmod(path=r"WaveShell1-AU 16.2.component", mode="a+rwX", prog_num=26516, recursive=True) as chmod_1627_26516:
                            chmod_1627_26516()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=26517) as cd_stage_1628_26517:
            cd_stage_1628_26517()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=26518):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=26519) as should_copy_source_1629_26519:
                    should_copy_source_1629_26519()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=26520):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=26521) as copy_dir_to_dir_1630_26521:
                            copy_dir_to_dir_1630_26521()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=26522) as unwtar_1631_26522:
                            unwtar_1631_26522()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=26523, recursive=True) as chown_1632_26523:
                            chown_1632_26523()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=26524) as shell_command_1633_26524:
                            shell_command_1633_26524()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.91.92", prog_num=26525):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=26526) as should_copy_source_1634_26526:
                    should_copy_source_1634_26526()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=26527):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=26528) as copy_dir_to_dir_1635_26528:
                            copy_dir_to_dir_1635_26528()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=26529) as unwtar_1636_26529:
                            unwtar_1636_26529()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=26530, recursive=True) as chown_1637_26530:
                            chown_1637_26530()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=26531) as shell_command_1638_26531:
                            shell_command_1638_26531()
            with Stage(r"copy", r"WaveShell1-VST3 16.1 v16.1.77.79", prog_num=26532):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=26533) as should_copy_source_1639_26533:
                    should_copy_source_1639_26533()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.1.vst3", prog_num=26534):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", r".", delete_extraneous_files=True, prog_num=26535) as copy_dir_to_dir_1640_26535:
                            copy_dir_to_dir_1640_26535()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.1.vst3", where_to_unwtar=r".", prog_num=26536) as unwtar_1641_26536:
                            unwtar_1641_26536()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.1.vst3", user_id=-1, group_id=-1, prog_num=26537, recursive=True) as chown_1642_26537:
                            chown_1642_26537()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.1.vst3"', ignore_all_errors=True, prog_num=26538) as shell_command_1643_26538:
                            shell_command_1643_26538()
            with Stage(r"copy", r"WaveShell1-VST3 16.2 v16.2.30.56", prog_num=26539):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=26540) as should_copy_source_1644_26540:
                    should_copy_source_1644_26540()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.2.vst3", prog_num=26541):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", r".", delete_extraneous_files=True, prog_num=26542) as copy_dir_to_dir_1645_26542:
                            copy_dir_to_dir_1645_26542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.2.vst3", where_to_unwtar=r".", prog_num=26543) as unwtar_1646_26543:
                            unwtar_1646_26543()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.2.vst3", user_id=-1, group_id=-1, prog_num=26544, recursive=True) as chown_1647_26544:
                            chown_1647_26544()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.2.vst3"', ignore_all_errors=True, prog_num=26545) as shell_command_1648_26545:
                            shell_command_1648_26545()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=26546) as cd_stage_1649_26546:
            cd_stage_1649_26546()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=26547):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=26548) as should_copy_source_1650_26548:
                    should_copy_source_1650_26548()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=26549):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=26550) as copy_dir_to_dir_1651_26550:
                            copy_dir_to_dir_1651_26550()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=26551) as unwtar_1652_26551:
                            unwtar_1652_26551()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=26552, recursive=True) as chown_1653_26552:
                            chown_1653_26552()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=26553) as shell_command_1654_26553:
                            shell_command_1654_26553()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=26554) as script_command_1655_26554:
                            script_command_1655_26554()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=26555) as shell_command_1656_26555:
                            shell_command_1656_26555()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.1 v16.1.77.79", prog_num=26556):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=26557) as should_copy_source_1657_26557:
                    should_copy_source_1657_26557()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", prog_num=26558):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", r".", delete_extraneous_files=True, prog_num=26559) as copy_dir_to_dir_1658_26559:
                            copy_dir_to_dir_1658_26559()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", where_to_unwtar=r".", prog_num=26560) as unwtar_1659_26560:
                            unwtar_1659_26560()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.1.bundle", user_id=-1, group_id=-1, prog_num=26561, recursive=True) as chown_1660_26561:
                            chown_1660_26561()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=26562) as shell_command_1661_26562:
                            shell_command_1661_26562()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=26563) as script_command_1662_26563:
                            script_command_1662_26563()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=26564) as shell_command_1663_26564:
                            shell_command_1663_26564()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.2 v16.2.30.56", prog_num=26565):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=26566) as should_copy_source_1664_26566:
                    should_copy_source_1664_26566()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", prog_num=26567):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", r".", delete_extraneous_files=True, prog_num=26568) as copy_dir_to_dir_1665_26568:
                            copy_dir_to_dir_1665_26568()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", where_to_unwtar=r".", prog_num=26569) as unwtar_1666_26569:
                            unwtar_1666_26569()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.2.bundle", user_id=-1, group_id=-1, prog_num=26570, recursive=True) as chown_1667_26570:
                            chown_1667_26570()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=26571) as shell_command_1668_26571:
                            shell_command_1668_26571()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=26572) as script_command_1669_26572:
                            script_command_1669_26572()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=26573) as shell_command_1670_26573:
                            shell_command_1670_26573()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=26574) as create_symlink_1671_26574:
                create_symlink_1671_26574()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=26575) as create_symlink_1672_26575:
                create_symlink_1672_26575()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=26576) as cd_stage_1673_26576:
            cd_stage_1673_26576()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=26577) as rm_file_or_dir_1674_26577:
                rm_file_or_dir_1674_26577()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=26578) as cd_stage_1675_26578:
            cd_stage_1675_26578()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=26579) as rm_file_or_dir_1676_26579:
                rm_file_or_dir_1676_26579()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=26580) as rm_file_or_dir_1677_26580:
                rm_file_or_dir_1677_26580()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=26581) as rm_file_or_dir_1678_26581:
                rm_file_or_dir_1678_26581()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=26582) as shell_command_1679_26582:
            shell_command_1679_26582()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=26583) as shell_command_1680_26583:
            shell_command_1680_26583()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=26584) as script_command_1681_26584:
            script_command_1681_26584()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=26585) as rm_file_or_dir_1682_26585:
            rm_file_or_dir_1682_26585()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26586) as move_dir_to_dir_1683_26586:
            move_dir_to_dir_1683_26586()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26587) as move_dir_to_dir_1684_26587:
            move_dir_to_dir_1684_26587()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26588) as move_dir_to_dir_1685_26588:
            move_dir_to_dir_1685_26588()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26589) as move_dir_to_dir_1686_26589:
            move_dir_to_dir_1686_26589()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=26590) as make_dirs_1687_26590:
            make_dirs_1687_26590()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26591) as move_dir_to_dir_1688_26591:
            move_dir_to_dir_1688_26591()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=26592) as move_dir_to_dir_1689_26592:
            move_dir_to_dir_1689_26592()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=26593) as shell_command_1690_26593:
            shell_command_1690_26593()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=26594) as script_command_1691_26594:
            script_command_1691_26594()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=26595) as rm_file_or_dir_1692_26595:
            rm_file_or_dir_1692_26595()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=26596) as glober_1693_26596:
            glober_1693_26596()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=26597) as glober_1694_26597:
            glober_1694_26597()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=26598) as glober_1695_26598:
            glober_1695_26598()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=26599) as shell_command_1696_26599:
            shell_command_1696_26599()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=26600) as shell_command_1697_26600:
            shell_command_1697_26600()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=26601) as shell_command_1698_26601:
            shell_command_1698_26601()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=26602) as shell_command_1699_26602:
            shell_command_1699_26602()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=26603) as shell_command_1700_26603:
            shell_command_1700_26603()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=26604) as script_command_1701_26604:
            script_command_1701_26604()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=26605) as if_1702_26605:
            if_1702_26605()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=26606) as if_1703_26606:
            if_1703_26606()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=26607) as if_1704_26607:
            if_1704_26607()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=26608) as if_1705_26608:
            if_1705_26608()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=26609) as make_dir_1706_26609:
            make_dir_1706_26609()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=26610) as chmod_1707_26610:
            chmod_1707_26610()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=26611) as make_dir_1708_26611:
            make_dir_1708_26611()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=26612) as chmod_1709_26612:
            chmod_1709_26612()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=26613) as chmod_1710_26613:
            chmod_1710_26613()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=26614) as chmod_1711_26614:
            chmod_1711_26614()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=26615) as chmod_1712_26615:
            chmod_1712_26615()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=26616) as shell_command_1713_26616:
            shell_command_1713_26616()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=26617) as script_command_1714_26617:
            script_command_1714_26617()
    with Stage(r"post-copy", prog_num=26618):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=26619) as make_dir_1715_26619:
            make_dir_1715_26619()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=26620) as copy_file_to_file_1716_26620:
            copy_file_to_file_1716_26620()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=26621) as chmod_1717_26621:
            chmod_1717_26621()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=26622) as chmod_1718_26622:
            chmod_1718_26622()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=26623) as copy_file_to_file_1719_26623:
            copy_file_to_file_1719_26623()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=26624) as chmod_1720_26624:
            chmod_1720_26624()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=26625) as copy_file_to_file_1721_26625:
            copy_file_to_file_1721_26625()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=26626) as chmod_1722_26626:
            chmod_1722_26626()
        Progress(r"Done copy", prog_num=26627)()
        Progress(r"Done synccopy", prog_num=26628)()
    with Stage(r"post", prog_num=26629):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=26630) as make_dir_1723_26630:
            make_dir_1723_26630()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=26631) as copy_file_to_file_1724_26631:
            copy_file_to_file_1724_26631()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=26632) as make_dir_1725_26632:
            make_dir_1725_26632()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=26633) as copy_file_to_file_1726_26633:
            copy_file_to_file_1726_26633()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=26634) as make_dir_1727_26634:
            make_dir_1727_26634()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/19/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=26635) as copy_file_to_file_1728_26635:
            copy_file_to_file_1728_26635()

with Stage(r"epilog", prog_num=26636):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250906114524-products.py", prog_num=26637) as patch_py_batch_with_timings_1729_26637:
        patch_py_batch_with_timings_1729_26637()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


