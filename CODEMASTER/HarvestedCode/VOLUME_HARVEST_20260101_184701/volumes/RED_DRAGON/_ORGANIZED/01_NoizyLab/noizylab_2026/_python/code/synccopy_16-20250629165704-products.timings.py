# Creation time: 29-06-25_16-57
import os
import sys
sys.path.append(r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/_internal")
import logging
log = logging.getLogger(__name__)
import utils
from configVar import config_vars
utils.set_acting_ids(config_vars.get("ACTING_UID", -1).int(), config_vars.get("ACTING_GID", -1).int())
from pybatch import *
PythonBatchCommandBase.total_progress = 66300
PythonBatchCommandBase.running_progress = 1764
if __name__ == '__main__':
    from utils import log_utils
    log_utils.config_logger()

with Stage(r"assign", prog_num=1765):  # 0m:0.001s
    config_vars['ACCEPTABLE_YAML_DOC_TAGS'] = (r"define_Mac", r"define_Mac32", r"define_if_not_exist_Mac", r"define_if_not_exist_Mac32")
    config_vars['ACTING_GID'] = -1
    config_vars['ACTING_HOME_DIR'] = r"/Users/rsp_ms"
    config_vars['ACTING_SHELL'] = r"/bin/zsh"
    config_vars['ACTING_UID'] = -1
    config_vars['ACTING_UNAME'] = r"rsp_ms"
    config_vars['ACTION_ID'] = r"16-20250629165704-products"
    config_vars['ALL_SYNC_DIRS'] = (r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/NKS FX", r"/Applications/Waves/Data/Video Sound Suite Impulses", r"/Applications/Waves/Data/Video Sound Suite Impulses")
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
    config_vars['CHECK_BINARIES_VERSION_MAXIMAL_REPO_REV'] = 6
    config_vars['COMPANY_NAME'] = r"Waves Audio"
    config_vars['CONFIG_VARS_FOR_ERROR_REPORT'] = (r"REPO_REV", r"REQUIRE_REPO_REV", r"BASE_LINKS_URL", r"S3_BUCKET_NAME", r"REPO_NAME", r"CENTRAL_VERSION")
    config_vars['CONFIG_VAR_NAME_ENDING_DENOTING_PATH'] = (r"/_DIR", r"/_PATH")
    config_vars['COOKIE_FOR_SYNC_URLS'] = r"CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MTI2NjYyNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUxMjMwMzI0fX19XX0_;CloudFront-Signature=VPkeZNaEgWAZ~BodijNxNhFwnftuXIuqUn4YyEKFJQHa1M5whMFxr0kworF3ZULW3dE0EBh82J0~NUPbslGA6ejAar8UIP67H01ag-wXuoC32Otog53Re1zMbo7A01uZ0ui6USAhGPrcXkIDNAFmGYhgqshvm4mYgxVsdaeF5GIjTGbjnOe0oZfEkHhrLS8JNmrXvm113ONqtYSNvzX8jcrlAVUwAEIL~53B6g0yv44e0NhwGUTb8PqIbjNk30q9OHDnc0ZRoDSSH7edSV9~ODi36t7lLGKa8IK4-enT3bT811WLiSPRmdQCzyV6xmwOBn5~G27gDQHiOmFAPwjhRQ__"
    config_vars['COOKIE_JAR'] = r"d36wza55md4dee.cloudfront.net:CloudFront-Key-Pair-Id=APKAI3XDGLX25XNO6R5Q;CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM2d3phNTVtZDRkZWUuY2xvdWRmcm9udC5uZXQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1MTI2NjYyNH0sIkRhdGVHcmVhdGVyVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzUxMjMwMzI0fX19XX0_;CloudFront-Signature=VPkeZNaEgWAZ~BodijNxNhFwnftuXIuqUn4YyEKFJQHa1M5whMFxr0kworF3ZULW3dE0EBh82J0~NUPbslGA6ejAar8UIP67H01ag-wXuoC32Otog53Re1zMbo7A01uZ0ui6USAhGPrcXkIDNAFmGYhgqshvm4mYgxVsdaeF5GIjTGbjnOe0oZfEkHhrLS8JNmrXvm113ONqtYSNvzX8jcrlAVUwAEIL~53B6g0yv44e0NhwGUTb8PqIbjNk30q9OHDnc0ZRoDSSH7edSV9~ODi36t7lLGKa8IK4-enT3bT811WLiSPRmdQCzyV6xmwOBn5~G27gDQHiOmFAPwjhRQ__"
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
    config_vars['INDEX_CHECKSUM'] = r"d116cfee4d3b8ba823ca77d73db949cd9f5332df"
    config_vars['INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/index.yaml.wzip"
    config_vars['INFO_MAP_CHECKSUM'] = r"63d9fef14341cb4766d5c3d12c3578eca2a2385e"
    config_vars['INFO_MAP_FILE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/info_map.txt.wzip"
    config_vars['INSTL_EXEC_DISPLAY_NAME'] = r"instl"
    config_vars['INSTL_FOLDER_BASE_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl"
    config_vars['INSTL_MINIMAL_VERSION'] = (2, 5, 0)
    config_vars['INSTL_VERSION_CHANGE_REASON'] = r'limit setuptools==68.2.2, to avoid "pkg_resources is deprecated" warning'
    config_vars['LAST_PROGRESS'] = 0
    config_vars['LOCAL_COPY_OF_REMOTE_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/remote_info_map.txt"
    config_vars['LOCAL_REPO_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping"
    config_vars['LOCAL_REPO_REV_BOOKKEEPING_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6"
    config_vars['LOCAL_REPO_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16"
    config_vars['LOCAL_SYNC_DIR'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl"
    config_vars['MACOS_APPLICATIONSUPPORT_DIR'] = r"/Library/Application Support"
    config_vars['MACOS_WAVESHELL_AU_DIR'] = r"/Library/Audio/Plug-Ins/Components"
    config_vars['MACOS_WAVESHELL_DAE_DIR'] = r"/Library/Application Support/Digidesign/Plug-Ins"
    config_vars['MACOS_WAVESHELL_VST3_DIR'] = r"/Library/Audio/Plug-Ins/VST3"
    config_vars['MACOS_WAVESHELL_VST_DIR'] = r"/Library/Audio/Plug-Ins/VST"
    config_vars['MAC_DOCK_TOOL'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['MAIN_IGNORED_TARGETS'] = r"Remove_9_6_leftovers_IID"
    config_vars['MAIN_INSTALL_TARGETS'] = (r"017b82a7-89aa-42ae-8fde-0ad5b83d249c", r"07850c39-be4a-4a50-8723-9be368efa831", r"0dd61f49-26d3-4ef3-8e61-630977075891", r"11aa65c2-9605-4b66-852a-19c00a8cad0a", r"1374eaac-1f40-4629-a1bd-7fad36931856", r"174305d5-4b34-45d6-8856-31464b6bdc1a", r"1ae02c29-eb06-46d8-933f-44dc29cae2f4", r"1b278f8c-b11e-45f7-9e6c-52daf5603529", r"1b2e3046-b634-4fc3-92df-100722e72a75", r"1d2e15ad-514e-4894-b13c-087940f2c275", r"1f35a6df-cfcc-4588-9e39-9c2b446dffe6", r"215572dc-9c91-4912-a0a9-d68096edc994", r"22195f90-44a7-41aa-8e89-7cd4032a553e", r"239c7584-82a0-420d-bfae-8885b3a52538", r"289510f1-fdf8-45ee-ae8d-4f42cc82ca64", r"29e06aff-907d-4711-a74e-3f8a59d69d79", r"2acada14-94c5-4414-9d64-454da34b0639", r"2d71ad91-bddb-42f2-a652-835830176f9f", r"2f139c88-eef0-46e0-aa4c-a64d89569da5", r"2f8f4c91-26ba-4be8-8310-d0d605b4eab8", r"2fca9f9c-44b8-499e-9ea6-59b9a95aed82", r"30917ee9-a700-481d-85d7-2062c35a9802", r"31278582-0282-4f7d-97b4-b44c7ec46dc2", r"3164b0cb-806c-4bdd-a286-260f9c6eb04c", r"329dbe6a-233e-4f8f-ac70-f5b55036845b", r"3398c0b1-9a1a-43b4-aba4-ac4264d6530c", r"33d7dcb8-cfb9-4647-9338-9ad15b619bb9", r"3466f9b8-bbb8-4717-96fb-25ab0e7c76bc", r"34ec8670-67d0-4e60-9e6a-3a3d15146c3c", r"35ec36e5-ddcb-451a-b1f3-9d0737e82c60", r"386ca2e5-2636-495f-810e-49eceb953b9f", r"397d345c-cb28-4ac3-9802-cf21d9a13e1a", r"3ba44abc-09c9-4ca5-9a1d-f4ac797ed633", r"3c217951-f061-42a9-a797-c6ae08355e8d", r"3cc8e3c0-c209-4128-a2f6-32be589badbf", r"3d47fe76-e1f9-4cbf-b155-715460ee749f", r"3ddd87ba-616d-4b2e-b4ec-71dfee0e0230", r"3ea2b316-c6c6-49f7-9f90-814c8cc34993", r"423381b7-4e7e-41e2-a69a-518aefd4ef13", r"45197058-00f3-4e1e-9381-cd0d545356b5", r"45a63c82-a4d3-43cb-926b-1daea4ffc4cc", r"49e069d6-907d-4991-a74e-3f8959d69830", r"4b221595-fbb4-46a0-8827-1e07b139a0bd", r"4cb5b3a8-8997-4828-9f05-cc46b141f7b9", r"507d025d-2709-4049-908f-7f9ae0a26e84", r"51472ece-6f53-4926-8123-64330d6c6852", r"51ba20e4-fa7e-4a85-bde9-b837c0c1d479", r"53a2fb95-8424-429f-a2c8-21e86b847f0a", r"558c21cb-b648-48a3-a23b-db455ecc2d55", r"5634fda9-ea28-4316-9476-527b8e7279a9", r"597fd39c-dc58-4d40-9a73-1bdc07a11e85", r"5d73b443-5698-4ab2-90e4-94e263aa9def", r"5daf4282-f6c5-4e00-b7d5-cac37ad48604", r"611c341d-39b7-43f1-a44d-5310bb283eeb", r"63b0a9f9-a701-4596-acb7-ab671e5addd9", r"6983b49f-2238-4e1e-8828-50ca84f58737", r"6b26e76e-10cf-44f9-88a1-d72c1eb242b0", r"6c7cdfec-03f7-4d62-84c3-9ea633067fc9", r"72e4f2f3-cc29-4635-8715-a7977a943920", r"7707a80e-06f0-412a-b2de-baa2c332bb13", r"783c2ffe-7eb8-4624-9fea-ae2c8f9c0ab1", r"7a2dfe16-a53f-4d65-8666-a0783b88887b", r"7c01bd8c-6267-48ce-8707-9df05b786b7b", r"7d186a7d-aa1c-493f-b969-f1a3dff4ce38", r"809ee9bf-24fe-44ff-968d-ef0199d798fc", r"811b0faa-6979-4500-a187-791e07c79138", r"823a2ad5-6a52-4cfe-8926-c016b63f4e17", r"84212e63-dffc-41b7-8249-1689a9c35fe0", r"87d5ca54-c659-460d-92ca-d25786210a25", r"891d818c-d046-420b-9602-ce7f5ee73c87", r"892c8a73-64c0-4929-956f-1fd68577f6cc", r"89e8ebe9-e72f-48a9-938b-bec5a9ec639e", r"8ce7a272-1741-4893-b516-e93ce40db756", r"8f96ad1e-814a-429b-97a7-2759ccb71191", r"911c58f1-0b6b-42f7-93dd-a571b29860fc", r"93b76aed-2b4e-46bc-8108-dabb326f6510", r"9502905b-ec62-4822-8dc7-874768aa8f3f", r"95c4284b-2d5d-400e-bbbb-e7b73ba236ad", r"96f2b292-8c3b-49f4-8193-4f7783654547", r"99ffe133-e637-4c37-9876-11e0ac55c125", r"a2c080f4-dc5c-4f63-88a2-a856d8f2d737", r"a9a2da9e-4feb-4f8e-b816-ccc743f3ead0", r"aa264888-988b-421c-89c9-629934734f37", r"ab09a527-4793-44f2-9353-c25cc1f4b856", r"ae4b9cc6-a30f-42ad-b4db-28cb21cda94b", r"b158aea5-79f7-4a39-b9b9-f8c5e7c237c2", r"b216adf9-77d5-4361-a210-d68d6a3d11bc", r"b3964c48-04db-470f-b5b8-fa2b340a6fd4", r"b5cd1675-b663-4a0b-aecc-ca9fe0e573fe", r"b8a31ecd-5110-4d10-ba3d-ca56215b3745", r"bd481d1c-7793-4c63-ac7e-bb88f5c13267", r"be8463eb-cba5-43d5-b591-e729549c8a1c", r"bf8f294e-2389-4ce6-8868-5f5aa1efaf66", r"c079789d-12a1-42af-8cf5-53295d4fdf55", r"c19c1d27-90ca-43e3-b503-9c7f2da272bc", r"c4283f8a-9ca9-4c54-bc11-77e6b61f2f5e", r"c4fb99f7-fc70-4b1f-999a-9920272bce03", r"c5f61b15-cd46-4fe8-8307-9a3065ca9d6e", r"c93e0e0e-c552-46d1-9dd1-3a8ea700ba3a", r"ca9a4322-a903-43ec-95d7-ccbbb475d2d5", r"cc3766ad-3e2c-4247-9adb-d28031b569af", r"cdbc077d-8945-429b-9a97-2cce4bdb0de4", r"d1b17f75-9fbf-4af9-9c8e-ebb7068998b9", r"d24276f9-7710-4c47-9935-c58d20c8b237", r"daac8463-5aa5-446c-9a3e-23ef92b7cca3", r"df43d3a6-ad21-11e0-836f-b7fd7bebd530", r"df76732e-ad21-11e0-81a3-b7fd7bebd530", r"df9b6bc1-ad21-11e0-8286-b7fd7bebd530", r"dfc80d80-ad21-11e0-804c-b7fd7bebd530", r"dfe64476-ad21-11e0-80e3-b7fd7bebd530", r"e0052ccd-ad21-11e0-81d6-b7fd7bebd530", r"e023b7a0-ad21-11e0-80bf-b7fd7bebd530", r"e0427e39-ad21-11e0-832d-b7fd7bebd530", r"e06158e4-ad21-11e0-80ed-b7fd7bebd530", r"e07f8a94-ad21-11e0-821f-b7fd7bebd530", r"e09dd956-ad21-11e0-80a8-b7fd7bebd530", r"e0bf0ba7-ad21-11e0-8147-b7fd7bebd530", r"e0e0ba8c-ad21-11e0-8153-b7fd7bebd530", r"e10288b9-ad21-11e0-8381-b7fd7bebd530", r"e124ade4-ad21-11e0-811f-b7fd7bebd530", r"e143b292-29ba-4885-aae7-c7f52a22ffc9", r"e161d7ab-ad21-11e0-818c-b7fd7bebd530", r"e184357b-ad21-11e0-82f9-b7fd7bebd530", r"e1a6881e-ad21-11e0-825a-b7fd7bebd530", r"e1c73d2a-ad21-11e0-8082-b7fd7bebd530", r"e1e91460-ad21-11e0-8303-b7fd7bebd530", r"e20c014e-ad21-11e0-83e6-b7fd7bebd530", r"e22cd127-ad21-11e0-822b-b7fd7bebd530", r"e2521210-ad21-11e0-838c-b7fd7bebd530", r"e2818ac3-ad21-11e0-80d6-b7fd7bebd530", r"e2a675c7-ad21-11e0-8023-b7fd7bebd530", r"e2cb5832-ad21-11e0-8125-b7fd7bebd530", r"e2edb329-ad21-11e0-8202-b7fd7bebd530", r"e30f737a-ad21-11e0-83dd-b7fd7bebd530", r"e3331e4b-ad21-11e0-829b-b7fd7bebd530", r"e352d399-ad21-11e0-8316-b7fd7bebd530", r"e37c8ff0-ad21-11e0-810d-b7fd7bebd530", r"e39dce24-16c9-4f4a-bb98-545e10052b75", r"e3a57973-ad21-11e0-818c-b7fd7bebd530", r"e3c605a4-ad21-11e0-8113-b7fd7bebd530", r"e47a4b22-ad21-11e0-80ba-b7fd7bebd530", r"e4b00ec4-ad21-11e0-834b-b7fd7bebd530", r"e4e5fb53-131e-45e0-91c1-d78aa4f5c69f", r"e4e72e7b-ad21-11e0-81a6-b7fd7bebd530", r"e5100b89-ad21-11e0-81a0-b7fd7bebd530", r"e551833a-ad21-11e0-8177-b7fd7bebd530", r"e591e90a-ad21-11e0-83a1-b7fd7bebd530", r"e5ce4a76-ad21-11e0-832b-b7fd7bebd530", r"e5ecb58a-ad21-11e0-820b-b7fd7bebd530", r"e60ab8c6-ad21-11e0-8364-b7fd7bebd530", r"e6281b3c-ad21-11e0-8087-b7fd7bebd530", r"e646beb6-ad21-11e0-83c3-b7fd7bebd530", r"e6675177-ad21-11e0-833e-b7fd7bebd530", r"e686154a-ad21-11e0-806f-b7fd7bebd530", r"e686394e-ad21-11e0-8185-b7fd7bebd530", r"e6a8de66-ad21-11e0-81f4-b7fd7bebd530", r"e6c7625a-ad21-11e0-8262-b7fd7bebd530", r"e6ead714-ad21-11e0-82a6-b7fd7bebd530", r"e7069133-ad21-11e0-82c1-b7fd7bebd530", r"e7223951-ad21-11e0-82d3-b7fd7bebd530", r"e73ed1fb-ad21-11e0-8035-b7fd7bebd530", r"e759bc5f-ad21-11e0-827d-b7fd7bebd530", r"e775f5e1-ad21-11e0-809f-b7fd7bebd530", r"e790fd1a-ad21-11e0-82c3-b7fd7bebd530", r"e7af58a0-ad21-11e0-832f-b7fd7bebd530", r"e7cd30b4-ad21-11e0-8385-b7fd7bebd530", r"e808505c-ad21-11e0-83e8-b7fd7bebd530", r"e8f6b97d-ad21-11e0-8088-b7fd7bebd530", r"e8f6df11-ad21-11e0-81f9-b7fd7bebd530", r"e92b2cea-ad21-11e0-8218-b7fd7bebd530", r"e9797602-ad21-11e0-8369-b7fd7bebd530", r"e9a3b6c2-ad21-11e0-823c-b7fd7bebd530", r"e9ef3ffd-ad21-11e0-83e3-b7fd7bebd530", r"ea1152ba-ad21-11e0-8305-b7fd7bebd530", r"ea4ad51a-ad21-11e0-8137-b7fd7bebd530", r"ea812d41-ad21-11e0-80f3-b7fd7bebd530", r"ea9c2b7e-ad21-11e0-8327-b7fd7bebd530", r"eab8d633-ad21-11e0-81eb-b7fd7bebd530", r"eb0c63ec-ad21-11e0-8288-b7fd7bebd530", r"eb442f99-ad21-11e0-8219-b7fd7bebd530", r"eb542f98-ad21-11e0-8222-b7fd7bebd530", r"eb621b67-ad21-11e0-8319-b7fd7bebd530", r"eba516c8-ad21-11e0-8377-b7fd7bebd530", r"eba53bd0-ad21-11e0-809f-b7fd7bebd530", r"ec31edd4-ad21-11e0-8215-b7fd7bebd530", r"ec32123c-ad21-11e0-83d2-b7fd7bebd530", r"ec323077-ad21-11e0-8335-b7fd7bebd530", r"ec53f8dd-ad21-11e0-8276-b7fd7bebd530", r"ec541a62-ad21-11e0-8150-b7fd7bebd530", r"ec719e28-ad21-11e0-8100-b7fd7bebd530", r"ec971ad7-ad21-11e0-8359-b7fd7bebd530", r"ec97493f-ad21-11e0-803e-b7fd7bebd530", r"eced4ec6-6f5a-4d23-880a-0e522dd7db8d", r"ed13f26a-ad21-11e0-8216-b7fd7bebd530", r"ed14136b-ad21-11e0-837c-b7fd7bebd530", r"ed143318-ad21-11e0-821a-b7fd7bebd530", r"ed748b6e-ad21-11e0-83bb-b7fd7bebd530", r"edff65f4-ad21-11e0-8126-b7fd7bebd530", r"ee3dacf8-ad21-11e0-83ec-b7fd7bebd530", r"ee5af8ce-ad21-11e0-8200-b7fd7bebd530", r"ee66500c-c66c-4e3d-8b59-d6d8bb07e29a", r"ee76f044-ad21-11e0-8170-b7fd7bebd530", r"ee93e582-ad21-11e0-8390-b7fd7bebd530", r"eecca8c2-ad21-11e0-8250-b7fd7bebd530", r"eee933a0-ad21-11e0-80e0-b7fd7bebd530", r"ef03fc08-ad21-11e0-8353-b7fd7bebd530", r"ef202a69-ad21-11e0-839b-b7fd7bebd530", r"ef3b4d52-ad21-11e0-8109-b7fd7bebd530", r"ef6067d8-ad21-11e0-8308-b7fd7bebd530", r"ef7b9575-ad21-11e0-81f1-b7fd7bebd530", r"ef9640eb-ad21-11e0-83ab-b7fd7bebd530", r"efb10934-ad21-11e0-8058-b7fd7bebd530", r"efce20a0-ad21-11e0-8012-b7fd7bebd530", r"efe96c20-ad21-11e0-833c-b7fd7bebd530", r"f00484d0-ad21-11e0-8357-b7fd7bebd530", r"f01f84d6-ad21-11e0-822a-b7fd7bebd530", r"f03a7463-ad21-11e0-830f-b7fd7bebd530", r"f056c254-ad21-11e0-8310-b7fd7bebd530", r"f07779d5-ad21-11e0-8252-b7fd7bebd530", r"f0b21870-ad21-11e0-811e-b7fd7bebd530", r"f0db846b-ad21-11e0-801f-b7fd7bebd530", r"f0dba8a1-ad21-11e0-82d9-b7fd7bebd530", r"f1174573-ad21-11e0-817b-b7fd7bebd530", r"f13344fe-ad21-11e0-82b1-b7fd7bebd530", r"f14f750c-ad21-11e0-8124-b7fd7bebd530", r"f169fb78-ad21-11e0-8276-b7fd7bebd530", r"f1896c6a-ad21-11e0-82f7-b7fd7bebd530", r"f1a67d84-ad21-11e0-8380-b7fd7bebd530", r"f1c3685d-ad21-11e0-8256-b7fd7bebd530", r"f1e2bcde-ad21-11e0-800a-b7fd7bebd530", r"f202b779-ad21-11e0-8344-b7fd7bebd530", r"f2214239-ad21-11e0-82e2-b7fd7bebd530", r"f23de82a-ad21-11e0-803b-b7fd7bebd530", r"f25bce3b-ad21-11e0-8126-b7fd7bebd530", r"f2781703-ad21-11e0-8147-b7fd7bebd530", r"f2a5ad2a-ad21-11e0-8185-b7fd7bebd530", r"f2f168c9-ad21-11e0-803f-b7fd7bebd530", r"f3315154-ad21-11e0-8140-b7fd7bebd530", r"f3513e7f-ad21-11e0-83f7-b7fd7bebd530", r"f3515f5a-ad21-11e0-81da-b7fd7bebd530", r"f64f3b3a-ca96-4bd0-a0e7-7c4283fefc69", r"fc52bedf-6e86-4353-bb34-0847d8e9e78a", r"fcdbc046-5e44-4d4d-b4ec-049d194c2458")
    config_vars['MAX_BAD_FILES_TO_REDOWNLOAD'] = 32
    config_vars['MAX_REPO_REV'] = 6
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
    config_vars['OPEN_LOG_FILES'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165704.log"
    config_vars['OUTPUT_FORMAT'] = r"$(__OUTPUT_FORMAT__)"
    config_vars['PARALLEL_DOWNLOAD_METHOD'] = r"internal"
    config_vars['PARALLEL_SYNC'] = 50
    config_vars['PATHS_TO_RESOLVE'] = (r"DOWNLOAD_TOOL_PATH", r"SET_ICON_TOOL_PATH")
    config_vars['POST_INSTALL_SCRIPT_FILE'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"
    config_vars['PRINT_COMMAND_TIME'] = r"yes"
    config_vars['PROPELLERHEAD_SOFTWARE_REWIRE'] = r"/Library/Application Support/Propellerhead Software/ReWire"
    config_vars['PYTHON_BATCH_LOG_LEVEL'] = 20
    config_vars['Plist_for_NI_Instrument_Data_NKS'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_Instrument_Data_NKS_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_Instrument_Data_NKS_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_Instrument_Data_NKS_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Plist_for_NI_NKS_FX'] = (r'''ResolveConfigVarsInFile(r"""/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template""", r"""/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist""",temp_config_vars={'NKS_NAME':r"$(__Plist_for_NI_NKS_FX_1__)",'NKS_DATA_VERSION':r"$(__Plist_for_NI_NKS_FX_2__)"} )''', r'If(IsConfigVarDefined("POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", output_script="/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh", hard_links=True, ignore_all_errors=True), if_false=CopyFileToFile("/tmp/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", "/Library/Preferences/com.native-instruments.Waves-$(__Plist_for_NI_NKS_FX_1__) Stereo.plist", hard_links=True, ignore_all_errors=True))')
    config_vars['Pre_Set_Bundles_Icon'] = ""
    config_vars['READ_YAML_FILES'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/main.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/compile-info.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClient.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults/InstlClientSync.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-synccopy.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16.yaml", r"/Applications/Waves Central.app/Contents/Resources/res/external/data/V16-online-common.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml")
    config_vars['REMOVE_EMPTY_FOLDERS_IGNORE_FILES'] = (r".DS_Store", r"Icon.*")
    config_vars['REMOVE_PREVIOUS_SOURCES'] = r"yes"
    config_vars['REPO_MAJOR_VERSION'] = 16
    config_vars['REPO_NAME'] = r"V16"
    config_vars['REPO_REV'] = 6
    config_vars['REPO_REV_EXT'] = ""
    config_vars['REPO_REV_FILE_BASE_NAME'] = r"V16_repo_rev.yaml"
    config_vars['REPO_REV_FILE_CREATED_BY'] = r"instl version 2.5.0.1 (not compiled) Stout"
    config_vars['REPO_REV_FILE_CREATE_TIME'] = r"2025-06-18 18:39:08.575155"
    config_vars['REPO_REV_FILE_SPECIFIC_NAME'] = r"V16_repo_rev.yaml.$(TARGET_REPO_REV)"
    config_vars['REPO_REV_FOLDER_HIERARCHY'] = r"00/06"
    config_vars['REPO_TYPE'] = r"URL"
    config_vars['REQUIRED_INFO_MAP_PATH'] = r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/required_info_map.txt"
    config_vars['REQUIRE_REPO_REV'] = 0
    config_vars['RSYNC_PERM_OPTIONS'] = r"a+rw,+X"
    config_vars['S3_BUCKET_NAME'] = r"instl"
    config_vars['S3_SECURE_URL_EXPIRATION'] = 86400
    config_vars['SAMPLE_LIBRARIES_LOCATIONS_DIR'] = r"/Users/Shared/Waves/Sample Libraries Locations"
    config_vars['SEARCH_PATHS'] = ""
    config_vars['SET_ICON_TOOL_PATH'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon"
    config_vars['SEVER_HARD_LINK'] = r'ScriptCommand(r"""tmpfile="$(__SEVER_HARD_LINK_1__)$(date +%s)"; cp -a "$(__SEVER_HARD_LINK_1__)" "$tmpfile"; mv "$tmpfile" "$(__SEVER_HARD_LINK_1__)" """)'
    config_vars['SHORT_INDEX_CHECKSUM'] = r"34e29ead85a33957b970d8d3096a8857e036390a"
    config_vars['SHORT_INDEX_URL'] = r"https://d36wza55md4dee.cloudfront.net/V16/00/06/instl/short-index.yaml"
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
    config_vars['TOTAL_ITEMS_FOR_PROGRESS_REPORT'] = 64531
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
    config_vars['__ARGV__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl", r"synccopy", r"--in", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.yaml", r"--out", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py", r"--log", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy-output-20250629165704.log", r"--run")
    config_vars['__COMMAND_NAMES__'] = (r"copy", r"read-yaml", r"remove", r"report-versions", r"sync", r"synccopy", r"uninstall")
    config_vars['__COMPILATION_TIME__'] = r"2025-06-23 13:34:46.784918"
    config_vars['__CURRENT_OS_DESCRIPTION__'] = r"macOS 15.5"
    config_vars['__CURRENT_OS_NAMES__'] = (r"Mac", r"Mac32")
    config_vars['__CURRENT_OS_SECOND_NAME__'] = r"Mac32"
    config_vars['__CURRENT_OS__'] = r"Mac"
    config_vars['__CURR_WORKING_DIR__'] = r"/"
    config_vars['__DATABASE_URL__'] = r":memory:"
    config_vars['__FULL_LIST_OF_DIRECT_SYNC_TARGETS__'] = (r"ARPlates_PlatePositions_IID", r"Artist_MM_IID", r"Data_AR_ST3_IID", r"Data_CLA_Nx_IID", r"Data_Chambers_IID", r"Data_Nx_Germano_Studios_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"PRS_Supermodels_Data_IID", r"AR_RS124_Presets_IID", r"Bass_Fingers_Presets_IID", r"FlowMotion_Presets_IID", r"Q_Clone_Presets_IID", r"SV_Instruments_Presets_IID", r"StudioRack_Presets_IID", r"SSL_EV2__PresetsPluginSetup__IID", r"StudioRack_Video_Impulses_IID", r"Instrument_Data_NKS_BFingers_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_CODEX_IID", r"Instrument_Data_NKS_Clavinet_IID", r"Instrument_Data_NKS_Electric200_IID", r"Instrument_Data_NKS_Electric88_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_Element_IID", r"Instrument_Data_NKS_FlowMotion_IID", r"Instrument_Data_NKS_GrandRhapsody_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_C6_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_DPR-402_IID", r"Instrument_Data_NKS_FX_Dorrough_IID", r"Instrument_Data_NKS_FX_EMO_D5_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_F6_IID", r"Instrument_Data_NKS_FX_GEQ_Classic_IID", r"Instrument_Data_NKS_FX_GEQ_Modern_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_VoiceCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_EQ_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_IMPusher_IID", r"Instrument_Data_NKS_FX_IRLive_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Bass_IID", r"Instrument_Data_NKS_FX_JJP-Cymb-Perc_IID", r"Instrument_Data_NKS_FX_JJP-Drums_IID", r"Instrument_Data_NKS_FX_JJP-Guitars_IID", r"Instrument_Data_NKS_FX_JJP-Strings-Keys_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MannyM-Delay_IID", r"Instrument_Data_NKS_FX_MannyM-Distortion_IID", r"Instrument_Data_NKS_FX_MannyM-EQ_IID", r"Instrument_Data_NKS_FX_MannyM-Reverb_IID", r"Instrument_Data_NKS_FX_MannyM-ToneShaper_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKBrighter_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKLouder_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPressure_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_OKWetter_IID", r"Instrument_Data_NKS_FX_OVox_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_Archon_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_Dallas_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_V9_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_SSLComp_IID", r"Instrument_Data_NKS_FX_SSLEQ_IID", r"Instrument_Data_NKS_FX_SSL_E-Channel_IID", r"Instrument_Data_NKS_FX_SSL_G-Channel_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_Torque_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_W43_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_WNS_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"Instrument_Data_NKS_FX_dbx-160_IID")
    config_vars['__FULL_LIST_OF_INSTALL_TARGETS__'] = (r"API_2500_IID", r"API_550_IID", r"API_560_IID", r"ARChambers_IID", r"ARPlates_IID", r"ARPlates_PlatePositions_IID", r"ARVinyl_IID", r"AR_RS124_IID", r"AR_RS124_Presets_IID", r"AR_ST3_IID", r"AR_Saturator_IID", r"Abbey_Road_Saturator_Presets_IID", r"AnalyzeAudioBundle_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"Artist_MM_IID", r"AudioTrack_IID", r"AudioTrack_Setups_library_IID", r"B360_IID", r"BB_Tubes_IID", r"BB_Tubes__Presets_IID", r"Bass_FingersApp_IID", r"Bass_Fingers_IID", r"Bass_Fingers_Presets_IID", r"Bass_Rider_IID", r"Bass_SlapperApp_IID", r"Bass_Slapper_IID", r"Berzerk_Distortion_IID", r"Berzerk_Distortion_Presets_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C1_Setups_Library_IID", r"C360_IID", r"C4_IID", r"C6_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Echosphere_IID", r"CLA_Echosphere_Presets_IID", r"CLA_Effects_IID", r"CLA_Epic_IID", r"CLA_Epic_Presets_IID", r"CLA_Guitars_IID", r"CLA_MixDown_IID", r"CLA_MixHub_IID", r"CLA_MixHub_Presets_IID", r"CLA_Nx_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"CODEXApp_IID", r"CODEX_IID", r"COMMON_PLUGIN_DEPENDS_IID", r"COSMOS_Application_IID", r"COSMOS_Common_Resources_IID", r"COSMOS_Data_Folders_IID", r"COSMOS_DelOldCommonResources_IID", r"COSMOS_HTML_IID", r"COSMOS_Models_Data_Folders_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"COSMOS_python_IID", r"CR8App_IID", r"CR8_Sampler_IID", r"CR8_Sampler_Presets_IID", r"CURVES_AQ_IID", r"CURVES_EQUATOR_IID", r"Center_IID", r"ChainersChildExcludeList_IID", r"Character_Filters_Data_IID", r"Clarity_Vx_DeReverb_IID", r"Clarity_Vx_DeReverb_Network__Data_Folders__IID", r"Clarity_Vx_DeReverb_Pro_IID", r"Clarity_Vx_DeReverb_Pro__Presets__IID", r"Clarity_Vx_DeReverb__Presets__IID", r"Clarity_Vx_IID", r"Clarity_Vx_Onnx__Data_Folders__IID", r"Clarity_Vx_Pro_IID", r"Clarity_Vx_Pro__Presets__IID", r"Clarity_Vx__Presets__IID", r"ClavinetApp_IID", r"Clavinet_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"Curves_AQ_Special_Data__IID", r"Curves_AQ__Presets__IID", r"Curves_Equator__Presets__IID", r"DPR-402_IID", r"Data_AR_ST3_IID", r"Data_CLA_Nx_IID", r"Data_Chambers_IID", r"Data_Nx_Germano_Studios_IID", r"Data_Nx_Headphone_EQ_IID", r"Data_Vinyl_IID", r"Data_Waves_Gems_IID", r"DeBreath_IID", r"DeEsser_IID", r"Delete_Waves_Caches_IID", r"DemoMode_1_IID", r"DemoMode_V16_1_IID", r"Doppler_IID", r"Dorrough_IID", r"Dorrough_Surround_5_0_IID", r"Dorrough_Surround_5_1_IID", r"Doubler_IID", r"EMO_D5_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_BA_IID", r"EddieKramer_DR_IID", r"EddieKramer_FX_IID", r"EddieKramer_GT_IID", r"EddieKramer_VC_IID", r"Electric200App_IID", r"Electric200_IID", r"Electric88App_IID", r"Electric88_IID", r"ElectricG80App_IID", r"ElectricG80_IID", r"Element2_IID", r"ElementApp_IID", r"Enigma_IID", r"F6_IID", r"FFmpeg_IID", r"Feedback_Hunter_IID", r"FlowMotionApp_IID", r"FlowMotion_IID", r"FlowMotion_Presets_IID", r"GEQ_IID", r"GET_FILES_FOR_CREATE_PLIST_IID", r"GTRAmp_IID", r"GTRSolo_App_IID", r"GTRSolo_Stomps_IID", r"GTRSolo_ToolRack_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GTR_App_IID", r"GTR_Stomps_IID", r"GemPlayer_IID", r"Get_General_Icons_IID", r"GrandRhapsodyApp_IID", r"GrandRhapsody_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"Greg_Wells_VoiceCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_EQ_IID", r"H_Reverb_IID", r"IDX_Intelligent_Dynamics_RMS_IID", r"IMPusher_IID", r"IR1IMPULSES_IID", r"IR1IMPULSES_V2_IID", r"IR1Impulses_Folder_IID", r"IR_1_IID", r"IR_360_IID", r"IR_LIVE_IMPULSES_IID", r"IR_L_IID", r"IR_Live_IID", r"Immersive_Wrapper_IID", r"InPhase_IID", r"InPhase_LT_IID", r"InnerProcess2_IID", r"InnerProcess_IID", r"Instrument_Data_Clavinet_IID", r"Instrument_Data_Electric200_IID", r"Instrument_Data_Electric88_IID", r"Instrument_Data_ElectricG80_IID", r"Instrument_Data_Folder_IID", r"Instrument_Data_Misc_ElectricG80_IID", r"Instrument_Data_Misc_GrandRhapsody_IID", r"Instrument_Data_NKS_BFingers_IID", r"Instrument_Data_NKS_BSlapper_IID", r"Instrument_Data_NKS_CODEX_IID", r"Instrument_Data_NKS_Clavinet_IID", r"Instrument_Data_NKS_Electric200_IID", r"Instrument_Data_NKS_Electric88_IID", r"Instrument_Data_NKS_ElectricG80_IID", r"Instrument_Data_NKS_Element_IID", r"Instrument_Data_NKS_FX_Aphex_AX_IID", r"Instrument_Data_NKS_FX_AudioTrack_IID", r"Instrument_Data_NKS_FX_Bass_Rider_IID", r"Instrument_Data_NKS_FX_Brauer_Motion_IID", r"Instrument_Data_NKS_FX_Butch_Vig_Vocals_IID", r"Instrument_Data_NKS_FX_C1_comp-gate_IID", r"Instrument_Data_NKS_FX_C4_IID", r"Instrument_Data_NKS_FX_C6_IID", r"Instrument_Data_NKS_FX_CLA-2A_IID", r"Instrument_Data_NKS_FX_CLA-3A_IID", r"Instrument_Data_NKS_FX_CLA-76_IID", r"Instrument_Data_NKS_FX_Center_IID", r"Instrument_Data_NKS_FX_DPR-402_IID", r"Instrument_Data_NKS_FX_Dorrough_IID", r"Instrument_Data_NKS_FX_EMO_D5_IID", r"Instrument_Data_NKS_FX_EMO_F2_IID", r"Instrument_Data_NKS_FX_EMO_Q4_IID", r"Instrument_Data_NKS_FX_Enigma_IID", r"Instrument_Data_NKS_FX_F6_IID", r"Instrument_Data_NKS_FX_Folders_IID", r"Instrument_Data_NKS_FX_GEQ_Classic_IID", r"Instrument_Data_NKS_FX_GEQ_Modern_IID", r"Instrument_Data_NKS_FX_Greg_Wells_MixCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_PianoCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_ToneCentric_IID", r"Instrument_Data_NKS_FX_Greg_Wells_VoiceCentric_IID", r"Instrument_Data_NKS_FX_H_Delay_IID", r"Instrument_Data_NKS_FX_H_EQ_IID", r"Instrument_Data_NKS_FX_H_Reverb_IID", r"Instrument_Data_NKS_FX_IMPusher_IID", r"Instrument_Data_NKS_FX_IRLive_IID", r"Instrument_Data_NKS_FX_InPhase_LT_Live_IID", r"Instrument_Data_NKS_FX_J37_IID", r"Instrument_Data_NKS_FX_JJP-Bass_IID", r"Instrument_Data_NKS_FX_JJP-Cymb-Perc_IID", r"Instrument_Data_NKS_FX_JJP-Drums_IID", r"Instrument_Data_NKS_FX_JJP-Guitars_IID", r"Instrument_Data_NKS_FX_JJP-Strings-Keys_IID", r"Instrument_Data_NKS_FX_JJP-Vocals_IID", r"Instrument_Data_NKS_FX_KingsMic_IID", r"Instrument_Data_NKS_FX_KramerHLS_IID", r"Instrument_Data_NKS_FX_KramerPIE_IID", r"Instrument_Data_NKS_FX_KramerTape_IID", r"Instrument_Data_NKS_FX_L1_IID", r"Instrument_Data_NKS_FX_L2_IID", r"Instrument_Data_NKS_FX_L3_16_IID", r"Instrument_Data_NKS_FX_L3_LL_Multi_IID", r"Instrument_Data_NKS_FX_L3_Multi_IID", r"Instrument_Data_NKS_FX_L3_Ultra_IID", r"Instrument_Data_NKS_FX_LinMB_IID", r"Instrument_Data_NKS_FX_LoAir_IID", r"Instrument_Data_NKS_FX_MannyM-Delay_IID", r"Instrument_Data_NKS_FX_MannyM-Distortion_IID", r"Instrument_Data_NKS_FX_MannyM-EQ_IID", r"Instrument_Data_NKS_FX_MannyM-Reverb_IID", r"Instrument_Data_NKS_FX_MannyM-ToneShaper_IID", r"Instrument_Data_NKS_FX_MaxxBass_IID", r"Instrument_Data_NKS_FX_MaxxVolume_IID", r"Instrument_Data_NKS_FX_MetaFilter_IID", r"Instrument_Data_NKS_FX_MondoMod_IID", r"Instrument_Data_NKS_FX_Morphoder_IID", r"Instrument_Data_NKS_FX_OKBrighter_IID", r"Instrument_Data_NKS_FX_OKDriver_IID", r"Instrument_Data_NKS_FX_OKFilter_IID", r"Instrument_Data_NKS_FX_OKLouder_IID", r"Instrument_Data_NKS_FX_OKPhatter_IID", r"Instrument_Data_NKS_FX_OKPressure_IID", r"Instrument_Data_NKS_FX_OKPumper_IID", r"Instrument_Data_NKS_FX_OKWetter_IID", r"Instrument_Data_NKS_FX_OVox_IID", r"Instrument_Data_NKS_FX_PAZ_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_Archon_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_Dallas_IID", r"Instrument_Data_NKS_FX_PRS_Supermodels_V9_IID", r"Instrument_Data_NKS_FX_PS22_IID", r"Instrument_Data_NKS_FX_PuigChild_660_IID", r"Instrument_Data_NKS_FX_PuigChild_670_IID", r"Instrument_Data_NKS_FX_PuigTec_EQP1A_IID", r"Instrument_Data_NKS_FX_PuigTec_MEQ5_IID", r"Instrument_Data_NKS_FX_Q10_IID", r"Instrument_Data_NKS_FX_Q_Clone_IID", r"Instrument_Data_NKS_FX_RBass_IID", r"Instrument_Data_NKS_FX_RChannel_IID", r"Instrument_Data_NKS_FX_RCompressor_IID", r"Instrument_Data_NKS_FX_REDD17_IID", r"Instrument_Data_NKS_FX_REDD37-51_IID", r"Instrument_Data_NKS_FX_REQ_6_IID", r"Instrument_Data_NKS_FX_RS56_IID", r"Instrument_Data_NKS_FX_RVerb_IID", r"Instrument_Data_NKS_FX_RVox_IID", r"Instrument_Data_NKS_FX_Reel_ADT_IID", r"Instrument_Data_NKS_FX_S1_Imager_IID", r"Instrument_Data_NKS_FX_S1_Shuffler_IID", r"Instrument_Data_NKS_FX_SSLComp_IID", r"Instrument_Data_NKS_FX_SSLEQ_IID", r"Instrument_Data_NKS_FX_SSL_E-Channel_IID", r"Instrument_Data_NKS_FX_SSL_G-Channel_IID", r"Instrument_Data_NKS_FX_Scheps_73_IID", r"Instrument_Data_NKS_FX_Scheps_Parallel_Particles_IID", r"Instrument_Data_NKS_FX_Smack_Attack_IID", r"Instrument_Data_NKS_FX_SoundShifter_IID", r"Instrument_Data_NKS_FX_Submarine_IID", r"Instrument_Data_NKS_FX_SuperTap_2_IID", r"Instrument_Data_NKS_FX_SuperTap_6_IID", r"Instrument_Data_NKS_FX_TG12345_IID", r"Instrument_Data_NKS_FX_Torque_IID", r"Instrument_Data_NKS_FX_TransX_Multi_IID", r"Instrument_Data_NKS_FX_TransX_Wide_IID", r"Instrument_Data_NKS_FX_TrueVerb_IID", r"Instrument_Data_NKS_FX_UltraPitch_IID", r"Instrument_Data_NKS_FX_VComp_IID", r"Instrument_Data_NKS_FX_VEQ4_IID", r"Instrument_Data_NKS_FX_VUMeter_IID", r"Instrument_Data_NKS_FX_Vitamin_IID", r"Instrument_Data_NKS_FX_W43_IID", r"Instrument_Data_NKS_FX_WLM_Meter_IID", r"Instrument_Data_NKS_FX_WNS_IID", r"Instrument_Data_NKS_FX_Waves_Tune_Real-Time_IID", r"Instrument_Data_NKS_FX_X_Crackle_IID", r"Instrument_Data_NKS_FX_X_Hum_IID", r"Instrument_Data_NKS_FX_dbx-160_IID", r"Instrument_Data_NKS_FlowMotion_IID", r"Instrument_Data_NKS_GrandRhapsody_IID", r"IntelDlls_IID", r"J37_IID", r"JJP-Bass_IID", r"JJP-Cymb-Perc_IID", r"JJP-Drums_IID", r"JJP-Guitars_IID", r"JJP-Strings-Keys_IID", r"JJP-Vocals_IID", r"Kaleidoscopes_IID", r"Kaleidoscopes_Presets_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L360_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LFE360_IID", r"LicenseNotifications_V16_1_IID", r"Lil_Tube_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"Lofi_Space__Presets__IID", r"MDMX_Distortion_IID", r"MDMX_Fuzz_Presets_IID", r"MDMX_OverDrive_Presets_IID", r"MDMX_Screamer_Presets_IID", r"MIDIArpSeq_IID", r"MIDIChords_IID", r"MIDIKeyboard_IID", r"MIDIMonitor_IID", r"MIDIRange_IID", r"MIDITranspose_IID", r"MIDIVelocity_IID", r"MIDIVoicing_IID", r"MIDI_PLUGINS_IID", r"MKL_Optimization_IID", r"MKL_Waves_IID", r"MV2_IID", r"MV360_IID", r"MagmaChannelStrip_IID", r"MagmaChannelStrip__Presets__IID", r"MagmaSprings_IID", r"MagmaSprings__Data_Folders__IID", r"MagmaSprings__Presets__IID", r"Main_Waves_folder_IID", r"MannyM-Delay_IID", r"MannyM-Distortion_IID", r"MannyM-EQ_IID", r"MannyM-Reverb_IID", r"MannyM-ToneShaper_IID", r"MannyM-TripleD_IID", r"Maserati_ACG_IID", r"Maserati_B72_IID", r"Maserati_DRM_IID", r"Maserati_GRP_IID", r"Maserati_GTi_IID", r"Maserati_HMX_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MetaFlanger_Setups_library_IID", r"Minimum_Requirements_IID", r"ModFX_Autopan_IID", r"ModFX_Chorus_IID", r"ModFX_Compressor_IID", r"ModFX_Delay_IID", r"ModFX_Distortion_IID", r"ModFX_IID", r"ModFX_Limiter_IID", r"ModFX_Reverb_IID", r"MondoMod_IID", r"Morphoder_IID", r"MultiMod_Presets_IID", r"MultiMod_Rack_IID", r"MultiMod_Shapes_folder_IID", r"MusicRack_IID", r"MusicRack_app_IID", r"NLS_IID", r"NS1_IID", r"NX_IID", r"NX_Ocean_Data_IID", r"NX_Ocean_IID", r"Note_Mapping_Data_IID", r"Nx_Germano_Studios_IID", r"OKBrighter_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKLouder_IID", r"OKPhatter_IID", r"OKPressure_IID", r"OKPumper_IID", r"OKWetter_IID", r"ONNXRUNTIME_IID", r"ORS_Modulators_Data_IID", r"OVox_Instrument_Presets_IID", r"OVox_Presets_IID", r"OVox_Vocal_ReSynthesis_IID", r"OVox_app_IID", r"PAZ_IID", r"PRS_Archon_IID", r"PRS_Dallas_IID", r"PRS_Supermodels_Data_IID", r"PRS_Supermodels_IID", r"PRS_V9_IID", r"PS22_DLA_Setups_library_IID", r"PS22_IID", r"PSE_IID", r"PlaylistRider_IID", r"Plugin_folder_registry_IID", r"Plugins_Documents_Folder_IID", r"Plugins_Settings_Folder_IID", r"Plugins_folder_IID", r"PresetBrowser_1_IID", r"PresetBrowser_V16_1_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q10_Setups_library_IID", r"Q_Clone_IID", r"Q_Clone_Presets_IID", r"R360_IID", r"RBass_IID", r"RBass_Presets_IID", r"RChannel_IID", r"RChannel_Presets_IID", r"RComp_IID", r"RComp_Presets_IID", r"RDeEsser_IID", r"RDeEsser_Presets_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"REQ_Presets_IID", r"RS56_IID", r"RVerb_IID", r"RVerb_Presets_IID", r"RVox_IID", r"RVox_Presets_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"RenAxx_Presets_IID", r"Renaissance_EQ_Setups_library_IID", r"Retro_Fi_IID", r"Retro_Fi__Data_Folders__IID", r"Retro_Fi__Presets__IID", r"S1_IID", r"S360_IID", r"SOC_Presets_IID", r"SSLChannel_IID", r"SSLComp_IID", r"SSLEQ_IID", r"SSL_EV2_IID", r"SSL_EV2__PresetsPluginSetup__IID", r"SSL_EV2__Presets__IID", r"SSL_G_Channel_IID", r"SV_Instruments_Presets_IID", r"Sample_Libraries_Locations_Folder_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Shutdown_Servers_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Silk_Vocal__Presets__IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Space_Rider_IID", r"Space_Rider__Presets__IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Compressor__Presets__IID", r"Spherix_Immersive_Limiter_IID", r"Spherix_Immersive_Limiter__Presets__IID", r"StudioRack_Data_IID", r"StudioRack_IID", r"StudioRack_Impulses_IID", r"StudioRack_Presets_Compatibility_IID", r"StudioRack_Presets_IID", r"StudioRack_Video_Impulses_IID", r"Sub_Align_IID", r"SuperTap_IID", r"SyncVx_Data_IID", r"SyncVx_IID", r"TG12345_IID", r"TG_MeterBridge_IID", r"TG_TransferDesk_IID", r"TRACT_IID", r"Torque_IID", r"TransX_IID", r"TrueVerb_IID", r"TrueVerb_Setups_library_IID", r"UM_IID", r"UltraPitch_IID", r"V9_V10_Organizer_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Bender_IID", r"Vocal_Bender_Presets_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsBass__Data_Folders__IID", r"VoltageAmpsBass__Presets__IID", r"VoltageAmpsGuitar_IID", r"VoltageAmpsGuitar__Data_Folders__IID", r"VoltageAmpsGuitar__Presets__IID", r"W43_IID", r"WLM_IID", r"WLM_Plus_IID", r"WNS_IID", r"WPAPI_folder_IID", r"WaveShell1_AAX_16_0_IID", r"WaveShell1_AU_16_0_IID", r"WaveShell1_OBS_V16_0_IID", r"WaveShell1_VST3_ARA_V16_0_IID", r"WaveShell1_VST3_V16_0_IID", r"WaveShell1_WPAPI_2_16_0_IID", r"WaveShell_AU_Reg_Util_IID", r"WaveShell_AU_Reg_Util_RUN_IID", r"WaveShells_Dir_IID", r"WavesGTRSolo_Presets_IID", r"WavesGTR_IID", r"WavesGTR_Presets_IID", r"WavesHeadTracker_IID", r"WavesLib1_16_0_23_IID", r"WavesLib1_16_0_30_IID", r"WavesLicenseEngine_IID", r"WavesLocalServer_IID", r"WavesPluginServer_V16_1_IID", r"WavesStream_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Data_folder_IID", r"Waves_Harmony_IID", r"Waves_Harmony_Note_Mapping_Data_IID", r"Waves_Harmony_Presets_IID", r"Waves_Preferences_folder_Mac_IID", r"Waves_Shared_folder_Mac_IID", r"Waves_Tune_Real-Time_IID", r"WebViewRuntimeInstaller_Offline_Requirement_IID", r"XML_and_Registry_for_Native_Instruments_Aphex_AX_IID", r"XML_and_Registry_for_Native_Instruments_AudioTrack_IID", r"XML_and_Registry_for_Native_Instruments_BFingers_IID", r"XML_and_Registry_for_Native_Instruments_BSlapper_IID", r"XML_and_Registry_for_Native_Instruments_Bass_Rider_IID", r"XML_and_Registry_for_Native_Instruments_Brauer_Motion_IID", r"XML_and_Registry_for_Native_Instruments_Butch_Vig_Vocals_IID", r"XML_and_Registry_for_Native_Instruments_C1_comp-gate_IID", r"XML_and_Registry_for_Native_Instruments_C4_IID", r"XML_and_Registry_for_Native_Instruments_C6_IID", r"XML_and_Registry_for_Native_Instruments_CLA-2A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-3A_IID", r"XML_and_Registry_for_Native_Instruments_CLA-76_IID", r"XML_and_Registry_for_Native_Instruments_CODEX_IID", r"XML_and_Registry_for_Native_Instruments_Center_IID", r"XML_and_Registry_for_Native_Instruments_Clavinet_IID", r"XML_and_Registry_for_Native_Instruments_DPR-402_IID", r"XML_and_Registry_for_Native_Instruments_Dorrough_IID", r"XML_and_Registry_for_Native_Instruments_EMO_D5_IID", r"XML_and_Registry_for_Native_Instruments_EMO_F2_IID", r"XML_and_Registry_for_Native_Instruments_EMO_Q4_IID", r"XML_and_Registry_for_Native_Instruments_Electric200_IID", r"XML_and_Registry_for_Native_Instruments_Electric88_IID", r"XML_and_Registry_for_Native_Instruments_ElectricG80_IID", r"XML_and_Registry_for_Native_Instruments_Element_IID", r"XML_and_Registry_for_Native_Instruments_Enigma_IID", r"XML_and_Registry_for_Native_Instruments_F6_IID", r"XML_and_Registry_for_Native_Instruments_FlowMotion_IID", r"XML_and_Registry_for_Native_Instruments_GEQ_Classic_IID", r"XML_and_Registry_for_Native_Instruments_GEQ_Modern_IID", r"XML_and_Registry_for_Native_Instruments_GrandRhapsody_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_MixCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_PianoCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_ToneCentric_IID", r"XML_and_Registry_for_Native_Instruments_Greg_Wells_VoiceCentric_IID", r"XML_and_Registry_for_Native_Instruments_H_Delay_IID", r"XML_and_Registry_for_Native_Instruments_H_EQ_IID", r"XML_and_Registry_for_Native_Instruments_H_Reverb_IID", r"XML_and_Registry_for_Native_Instruments_IMPusher_IID", r"XML_and_Registry_for_Native_Instruments_IRLive_IID", r"XML_and_Registry_for_Native_Instruments_InPhase_LT_Live_IID", r"XML_and_Registry_for_Native_Instruments_J37_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Bass_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Cymb-Perc_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Drums_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Guitars_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Strings-Keys_IID", r"XML_and_Registry_for_Native_Instruments_JJP-Vocals_IID", r"XML_and_Registry_for_Native_Instruments_KingsMic_IID", r"XML_and_Registry_for_Native_Instruments_KramerHLS_IID", r"XML_and_Registry_for_Native_Instruments_KramerPIE_IID", r"XML_and_Registry_for_Native_Instruments_KramerTape_IID", r"XML_and_Registry_for_Native_Instruments_L1_IID", r"XML_and_Registry_for_Native_Instruments_L2_IID", r"XML_and_Registry_for_Native_Instruments_L3_16_IID", r"XML_and_Registry_for_Native_Instruments_L3_LL_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Multi_IID", r"XML_and_Registry_for_Native_Instruments_L3_Ultra_IID", r"XML_and_Registry_for_Native_Instruments_LinMB_IID", r"XML_and_Registry_for_Native_Instruments_LoAir_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-Delay_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-Distortion_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-EQ_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-Reverb_IID", r"XML_and_Registry_for_Native_Instruments_MannyM-ToneShaper_IID", r"XML_and_Registry_for_Native_Instruments_MaxxBass_IID", r"XML_and_Registry_for_Native_Instruments_MaxxVolume_IID", r"XML_and_Registry_for_Native_Instruments_MetaFilter_IID", r"XML_and_Registry_for_Native_Instruments_MondoMod_IID", r"XML_and_Registry_for_Native_Instruments_Morphoder_IID", r"XML_and_Registry_for_Native_Instruments_OKBrighter_IID", r"XML_and_Registry_for_Native_Instruments_OKDriver_IID", r"XML_and_Registry_for_Native_Instruments_OKFilter_IID", r"XML_and_Registry_for_Native_Instruments_OKLouder_IID", r"XML_and_Registry_for_Native_Instruments_OKPhatter_IID", r"XML_and_Registry_for_Native_Instruments_OKPressure_IID", r"XML_and_Registry_for_Native_Instruments_OKPumper_IID", r"XML_and_Registry_for_Native_Instruments_OKWetter_IID", r"XML_and_Registry_for_Native_Instruments_OVox_IID", r"XML_and_Registry_for_Native_Instruments_PAZ_IID", r"XML_and_Registry_for_Native_Instruments_PRS_Supermodels_Archon_IID", r"XML_and_Registry_for_Native_Instruments_PRS_Supermodels_Dallas_IID", r"XML_and_Registry_for_Native_Instruments_PRS_Supermodels_V9_IID", r"XML_and_Registry_for_Native_Instruments_PS22_IID", r"XML_and_Registry_for_Native_Instruments_PuigChild_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_EQP1A_IID", r"XML_and_Registry_for_Native_Instruments_PuigTec_MEQ5_IID", r"XML_and_Registry_for_Native_Instruments_Q10_IID", r"XML_and_Registry_for_Native_Instruments_Q_Clone_IID", r"XML_and_Registry_for_Native_Instruments_RBass_IID", r"XML_and_Registry_for_Native_Instruments_RChannel_IID", r"XML_and_Registry_for_Native_Instruments_RCompressor_IID", r"XML_and_Registry_for_Native_Instruments_REDD17_IID", r"XML_and_Registry_for_Native_Instruments_REDD37-51_IID", r"XML_and_Registry_for_Native_Instruments_REQ_6_IID", r"XML_and_Registry_for_Native_Instruments_RS56_IID", r"XML_and_Registry_for_Native_Instruments_RVerb_IID", r"XML_and_Registry_for_Native_Instruments_RVox_IID", r"XML_and_Registry_for_Native_Instruments_Reel_ADT_IID", r"XML_and_Registry_for_Native_Instruments_S1_Imager_IID", r"XML_and_Registry_for_Native_Instruments_S1_Shuffler_IID", r"XML_and_Registry_for_Native_Instruments_SSLComp_IID", r"XML_and_Registry_for_Native_Instruments_SSLEQ_IID", r"XML_and_Registry_for_Native_Instruments_SSL_E-Channel_IID", r"XML_and_Registry_for_Native_Instruments_SSL_G-Channel_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_73_IID", r"XML_and_Registry_for_Native_Instruments_Scheps_Parallel_Particles_IID", r"XML_and_Registry_for_Native_Instruments_Smack_Attack_IID", r"XML_and_Registry_for_Native_Instruments_SoundShifter_IID", r"XML_and_Registry_for_Native_Instruments_Submarine_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_2_IID", r"XML_and_Registry_for_Native_Instruments_SuperTap_6_IID", r"XML_and_Registry_for_Native_Instruments_TG12345_IID", r"XML_and_Registry_for_Native_Instruments_Torque_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Multi_IID", r"XML_and_Registry_for_Native_Instruments_TransX_Wide_IID", r"XML_and_Registry_for_Native_Instruments_TrueVerb_IID", r"XML_and_Registry_for_Native_Instruments_UltraPitch_IID", r"XML_and_Registry_for_Native_Instruments_VComp_IID", r"XML_and_Registry_for_Native_Instruments_VEQ4_IID", r"XML_and_Registry_for_Native_Instruments_VUMeter_IID", r"XML_and_Registry_for_Native_Instruments_Vitamin_IID", r"XML_and_Registry_for_Native_Instruments_W43_IID", r"XML_and_Registry_for_Native_Instruments_WLM_Meter_IID", r"XML_and_Registry_for_Native_Instruments_WNS_IID", r"XML_and_Registry_for_Native_Instruments_Waves_Tune_Real-Time_IID", r"XML_and_Registry_for_Native_Instruments_X_Crackle_IID", r"XML_and_Registry_for_Native_Instruments_X_Hum_IID", r"XML_and_Registry_for_Native_Instruments_dbx-160_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_FDBK_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID", r"dbx-160_IID")
    config_vars['__GITHUB_BRANCH__'] = r"master"
    config_vars['__GROUP_ID__'] = 20
    config_vars['__INSTL_COMPILED__'] = r"True"
    config_vars['__INSTL_EXE_PATH__'] = r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"
    config_vars['__INSTL_LAUNCH_COMMAND__'] = r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/MacOS/instl"'
    config_vars['__INSTL_VERSION_STR_LONG__'] = r"instl version 2.5.1.8 2025-06-23 13:34:46.784918 BM-MAC-ADO6"
    config_vars['__INSTL_VERSION_STR_SHORT__'] = r"2.5.1.8"
    config_vars['__INSTL_VERSION__'] = (2, 5, 1, 8)
    config_vars['__INVOCATION_RANDOM_ID__'] = r"uhbtmhgfijuuvime"
    config_vars['__JUST_WITH_NUMBER__'] = 0
    config_vars['__MAIN_COMMAND__'] = r"synccopy"
    config_vars['__MAIN_DB_FILE__'] = r":memory:"
    config_vars['__MAIN_DRIVE_NAME__'] = r"Mission Control"
    config_vars['__MAIN_INPUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.yaml"
    config_vars['__MAIN_INSTALL_IIDS__'] = (r"API_2500_IID", r"API_550_IID", r"API_560_IID", r"ARChambers_IID", r"ARPlates_IID", r"ARVinyl_IID", r"AR_RS124_IID", r"AR_ST3_IID", r"AR_Saturator_IID", r"Aphex_AX_IID", r"Artist_DLLs_Common_Guid_IID", r"AudioTrack_IID", r"B360_IID", r"BB_Tubes_IID", r"Bass_Fingers_IID", r"Bass_Rider_IID", r"Bass_Slapper_IID", r"Berzerk_Distortion_IID", r"Brauer_Motion_IID", r"Butch_Vig_Vocals_IID", r"C1_IID", r"C360_IID", r"C4_IID", r"C6_IID", r"CLA_2A_IID", r"CLA_3A_IID", r"CLA_76_IID", r"CLA_Bass_IID", r"CLA_Drums_IID", r"CLA_Echosphere_IID", r"CLA_Effects_IID", r"CLA_Epic_IID", r"CLA_Guitars_IID", r"CLA_MixDown_IID", r"CLA_MixHub_IID", r"CLA_Nx_IID", r"CLA_Unplugged_IID", r"CLA_Vocals_IID", r"CODEX_IID", r"COSMOS_Plugin_IID", r"COSMOS__IID", r"CR8_Sampler_IID", r"CURVES_AQ_IID", r"CURVES_EQUATOR_IID", r"Center_IID", r"Clarity_Vx_DeReverb_IID", r"Clarity_Vx_DeReverb_Pro_IID", r"Clarity_Vx_IID", r"Clarity_Vx_Pro_IID", r"Clavinet_IID", r"Cobalt_Saphira_IID", r"Cobalt_Submarine_IID", r"DPR-402_IID", r"DeBreath_IID", r"DeEsser_IID", r"Doppler_IID", r"Dorrough_IID", r"Dorrough_Surround_5_0_IID", r"Dorrough_Surround_5_1_IID", r"Doubler_IID", r"EMO_D5_IID", r"EMO_F2_IID", r"EMO_Q4_IID", r"EddieKramer_BA_IID", r"EddieKramer_DR_IID", r"EddieKramer_FX_IID", r"EddieKramer_GT_IID", r"EddieKramer_VC_IID", r"Electric200_IID", r"Electric88_IID", r"ElectricG80_IID", r"Element2_IID", r"Enigma_IID", r"F6_IID", r"Feedback_Hunter_IID", r"FlowMotion_IID", r"GEQ_IID", r"GTRAmp_IID", r"GTRSolo_ToolRack_IID", r"GTRStomp_IID", r"GTRToolRack_IID", r"GTRTuner_IID", r"GemPlayer_IID", r"GrandRhapsody_IID", r"Greg_Wells_MixCentric_IID", r"Greg_Wells_PianoCentric_IID", r"Greg_Wells_ToneCentric_IID", r"Greg_Wells_VoiceCentric_IID", r"H_Comp_IID", r"H_Delay_IID", r"H_EQ_IID", r"H_Reverb_IID", r"IDX_Intelligent_Dynamics_RMS_IID", r"IMPusher_IID", r"IR_1_IID", r"IR_360_IID", r"IR_L_IID", r"IR_Live_IID", r"Immersive_Wrapper_IID", r"InPhase_IID", r"InPhase_LT_IID", r"J37_IID", r"JJP-Bass_IID", r"JJP-Cymb-Perc_IID", r"JJP-Drums_IID", r"JJP-Guitars_IID", r"JJP-Strings-Keys_IID", r"JJP-Vocals_IID", r"Kaleidoscopes_IID", r"KeyDetector_IID", r"KingsMic_IID", r"KramerHLS_IID", r"KramerPIE_IID", r"KramerTape_IID", r"L1_IID", r"L2_IID", r"L360_IID", r"L3_16_IID", r"L3_LL_Multi_IID", r"L3_LL_Ultra_IID", r"L3_Multi_IID", r"L3_Ultra_IID", r"LFE360_IID", r"Lil_Tube_IID", r"LinEQ_IID", r"LinMB_IID", r"LoAir_IID", r"Lofi_Space__IID", r"MDMX_Distortion_IID", r"MV2_IID", r"MV360_IID", r"MagmaChannelStrip_IID", r"MagmaSprings_IID", r"MannyM-Delay_IID", r"MannyM-Distortion_IID", r"MannyM-EQ_IID", r"MannyM-Reverb_IID", r"MannyM-ToneShaper_IID", r"MannyM-TripleD_IID", r"Maserati_ACG_IID", r"Maserati_B72_IID", r"Maserati_DRM_IID", r"Maserati_GRP_IID", r"Maserati_GTi_IID", r"Maserati_HMX_IID", r"Maserati_VX1_IID", r"MaxxBass_IID", r"MaxxVolume_IID", r"MetaFilter_IID", r"MetaFlanger_IID", r"MondoMod_IID", r"Morphoder_IID", r"MultiMod_Rack_IID", r"MusicRack_IID", r"NLS_IID", r"NS1_IID", r"NX_IID", r"NX_Ocean_IID", r"Nx_Germano_Studios_IID", r"OKBrighter_IID", r"OKDriver_IID", r"OKFilter_IID", r"OKLouder_IID", r"OKPhatter_IID", r"OKPressure_IID", r"OKPumper_IID", r"OKWetter_IID", r"OVox_Vocal_ReSynthesis_IID", r"PAZ_IID", r"PRS_Supermodels_IID", r"PS22_IID", r"PSE_IID", r"PlaylistRider_IID", r"PuigChild_IID", r"PuigTec_IID", r"Q10_IID", r"Q_Clone_IID", r"R360_IID", r"RBass_IID", r"RChannel_IID", r"RComp_IID", r"RDeEsser_IID", r"REDD17_IID", r"REDD3751_IID", r"REQ_IID", r"RS56_IID", r"RVerb_IID", r"RVox_IID", r"Reel_ADT_IID", r"RenAxx_IID", r"Retro_Fi_IID", r"S1_IID", r"S360_IID", r"SSLChannel_IID", r"SSLComp_IID", r"SSLEQ_IID", r"SSL_EV2_IID", r"SSL_G_Channel_IID", r"Scheps_73_IID", r"Scheps_Omni_Channel_IID", r"Scheps_Parallel_Particles_IID", r"Sibilance_IID", r"SignalGenerator_IID", r"Silk_Vocal_IID", r"Smack_Attack_IID", r"SoundShifter_IID", r"Space_Rider_IID", r"Spherix_Immersive_Compressor_IID", r"Spherix_Immersive_Limiter_IID", r"StudioRack_IID", r"Sub_Align_IID", r"SuperTap_IID", r"SyncVx_IID", r"TG12345_IID", r"TG_TransferDesk_IID", r"TRACT_IID", r"Torque_IID", r"TransX_IID", r"TrueVerb_IID", r"UM_IID", r"UltraPitch_IID", r"VComp_IID", r"VEQ3_IID", r"VEQ4_IID", r"VUMeter_IID", r"Vitamin_IID", r"Vocal_Bender_IID", r"Vocal_Rider_IID", r"VoltageAmpsBass_IID", r"VoltageAmpsGuitar_IID", r"W43_IID", r"WLM_IID", r"WLM_Plus_IID", r"WNS_IID", r"WavesStream_IID", r"WavesTune_IID", r"WavesTune_LT_IID", r"Waves_Harmony_IID", r"Waves_Tune_Real-Time_IID", r"X_Click_IID", r"X_Crackle_IID", r"X_FDBK_IID", r"X_Hum_IID", r"X_Noise_IID", r"Z_Noise_IID", r"dbx-160_IID")
    config_vars['__MAIN_OUT_FILE__'] = r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py"
    config_vars['__MAIN_UPDATE_IIDS__'] = ""
    config_vars['__NOW__'] = r"2025-06-29 16:57:26.368543"
    config_vars['__NUM_BYTES_TO_DOWNLOAD__'] = 5679397181
    config_vars['__NUM_FILES_TO_DOWNLOAD__'] = 22524
    config_vars['__ORPHAN_INSTALL_TARGETS__'] = ""
    config_vars['__PLATFORM_NODE__'] = r"BM-MAC-ADO6"
    config_vars['__PYSQLITE3_VERSION__'] = r"2.6.0"
    config_vars['__PYTHON_VERSION__'] = (3, 12, 3, r"final", 0)
    config_vars['__RUN_BATCH__'] = r"True"
    config_vars['__SEARCH_PATHS__'] = (r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin/instl.bundle/Contents/Resources/defaults", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Applications/Waves Central.app/Contents/Resources/res/external/data", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6", r"/Applications/Waves Central.app/Contents/Resources/res/external/bin")
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

with PythonBatchRuntime(r"synccopy", prog_num=1766):  # 7m:1.247s
    with Stage(r"begin", prog_num=1767):  # 0m:0.000s
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1768):  # 0m:0.007s
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1769) as copy_file_to_file_001_1769:  # 0m:0.000s
            copy_file_to_file_001_1769()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1770) as copy_file_to_file_002_1770:  # 0m:0.006s
            copy_file_to_file_002_1770()
    with Stage(r"sync", prog_num=1771):  # 1m:24.255s
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1772) as shell_command_003_1772:  # 0m:0.008s
            shell_command_003_1772()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1773) as shell_command_004_1773:  # 0m:0.010s
            shell_command_004_1773()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=1774) as shell_command_005_1774:  # 0m:0.005s
            shell_command_005_1774()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1775) as shell_command_006_1775:  # 0m:0.960s
            shell_command_006_1775()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1776) as shell_command_007_1776:  # 0m:0.008s
            shell_command_007_1776()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1777) as shell_command_008_1777:  # 0m:0.958s
            shell_command_008_1777()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1778) as shell_command_009_1778:  # 0m:0.008s
            shell_command_009_1778()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1779) as shell_command_010_1779:  # 0m:0.005s
            shell_command_010_1779()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1780) as shell_command_011_1780:  # 0m:0.140s
            shell_command_011_1780()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=1781):  # 1m:22.153s
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=1782) as make_dir_012_1782:  # 0m:0.006s
                make_dir_012_1782()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1783) as cd_013_1783:  # 1m:22.146s
                cd_013_1783()
                Progress(r"11308 files already in cache", own_progress_count=11308, prog_num=13091)()  # 0m:0.000s
                with CreateSyncFolders(own_progress_count=4513, prog_num=17604) as create_sync_folders_014_17604:  # 0m:0.471s
                    create_sync_folders_014_17604()
                Progress(r"Downloading with 50 processes in parallel", prog_num=17605)()  # 0m:0.000s
                Progress(r"Downloading with curl parallel", prog_num=17606)()  # 0m:0.000s
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py_curl/dl-00", total_files_to_download=22524, previously_downloaded_files=0, total_bytes_to_download=5679397181, own_progress_count=21671, prog_num=39277, report_own_progress=False) as curl_with_internal_parallel_015_39277:  # 1m:12.323s
                    curl_with_internal_parallel_015_39277()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py_curl/dl-01", total_files_to_download=22524, previously_downloaded_files=21671, total_bytes_to_download=5679397181, own_progress_count=853, prog_num=40130, report_own_progress=False) as curl_with_internal_parallel_016_40130:  # 0m:1.224s
                    curl_with_internal_parallel_016_40130()
                Progress(r"Downloading 22524 files done", prog_num=40131)()  # 0m:0.000s
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=40132) as run_in_thread_017_40132:  # 0m:0.000s
                    run_in_thread_017_40132()
                Progress(r"Check checksum ...", prog_num=40133)()  # 0m:0.000s
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=22524, prog_num=62657) as check_download_folder_checksum_018_62657:  # 0m:7.473s
                    check_download_folder_checksum_018_62657()
                with Stage(r"post_sync", prog_num=62658):  # 0m:0.653s
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16...", prog_num=62659)()  # 0m:0.000s
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=62660, recursive=True) as chmod_and_chown_019_62660:  # 0m:0.636s
                        chmod_and_chown_019_62660()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=62661) as copy_file_to_file_020_62661:  # 0m:0.017s
                        copy_file_to_file_020_62661()
            Progress(r"Done sync", prog_num=62662)()  # 0m:0.000s
    with Stage(r"copy", prog_num=62663):  # 5m:36.904s
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=62664)()  # 0m:0.000s
        with Stage(r"create folders", prog_num=62665):  # 0m:0.316s
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=62666) as make_dir_021_62666:  # 0m:0.009s
                make_dir_021_62666()
            with MakeDir(r"/Applications/Waves/Applications V16", chowner=True, prog_num=62667) as make_dir_022_62667:  # 0m:0.001s
                make_dir_022_62667()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=62668) as make_dir_023_62668:  # 0m:0.006s
                make_dir_023_62668()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=62669) as make_dir_024_62669:  # 0m:0.008s
                make_dir_024_62669()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=62670) as make_dir_025_62670:  # 0m:0.010s
                make_dir_025_62670()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses", chowner=True, prog_num=62671) as make_dir_026_62671:  # 0m:0.009s
                make_dir_026_62671()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=62672) as make_dir_027_62672:  # 0m:0.010s
                make_dir_027_62672()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=62673) as make_dir_028_62673:  # 0m:0.009s
                make_dir_028_62673()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=62674) as make_dir_029_62674:  # 0m:0.009s
                make_dir_029_62674()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=62675) as make_dir_030_62675:  # 0m:0.010s
                make_dir_030_62675()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=62676) as make_dir_031_62676:  # 0m:0.010s
                make_dir_031_62676()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=62677) as make_dir_032_62677:  # 0m:0.010s
                make_dir_032_62677()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=62678) as make_dir_033_62678:  # 0m:0.009s
                make_dir_033_62678()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=62679) as make_dir_034_62679:  # 0m:0.010s
                make_dir_034_62679()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=62680) as make_dir_035_62680:  # 0m:0.009s
                make_dir_035_62680()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=62681) as make_dir_036_62681:  # 0m:0.000s
                make_dir_036_62681()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=62682) as make_dir_037_62682:  # 0m:0.000s
                make_dir_037_62682()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTR", chowner=True, prog_num=62683) as make_dir_038_62683:  # 0m:0.000s
                make_dir_038_62683()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTRSolo", chowner=True, prog_num=62684) as make_dir_039_62684:  # 0m:0.000s
                make_dir_039_62684()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/MIDI", chowner=True, prog_num=62685) as make_dir_040_62685:  # 0m:0.000s
                make_dir_040_62685()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/ModFX", chowner=True, prog_num=62686) as make_dir_041_62686:  # 0m:0.000s
                make_dir_041_62686()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=62687) as make_dir_042_62687:  # 0m:0.000s
                make_dir_042_62687()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=62688) as make_dir_043_62688:  # 0m:0.009s
                make_dir_043_62688()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=62689) as make_dir_044_62689:  # 0m:0.010s
                make_dir_044_62689()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=62690) as make_dir_045_62690:  # 0m:0.009s
                make_dir_045_62690()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=62691) as make_dir_046_62691:  # 0m:0.010s
                make_dir_046_62691()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=62692) as make_dir_047_62692:  # 0m:0.009s
                make_dir_047_62692()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=62693) as make_dir_048_62693:  # 0m:0.011s
                make_dir_048_62693()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=62694) as make_dir_049_62694:  # 0m:0.000s
                make_dir_049_62694()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=62695) as make_dir_050_62695:  # 0m:0.000s
                make_dir_050_62695()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=62696) as make_dir_051_62696:  # 0m:0.010s
                make_dir_051_62696()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=62697) as make_dir_052_62697:  # 0m:0.010s
                make_dir_052_62697()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=62698) as make_dir_053_62698:  # 0m:0.000s
                make_dir_053_62698()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=62699) as make_dir_054_62699:  # 0m:0.009s
                make_dir_054_62699()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=62700) as make_dir_055_62700:  # 0m:0.009s
                make_dir_055_62700()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=62701) as make_dir_056_62701:  # 0m:0.015s
                make_dir_056_62701()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=62702) as make_dir_057_62702:  # 0m:0.010s
                make_dir_057_62702()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=62703) as make_dir_058_62703:  # 0m:0.014s
                make_dir_058_62703()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=62704) as make_dir_059_62704:  # 0m:0.009s
                make_dir_059_62704()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=62705) as make_dir_060_62705:  # 0m:0.010s
                make_dir_060_62705()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=62706) as make_dir_061_62706:  # 0m:0.010s
                make_dir_061_62706()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings/MMod", chowner=True, prog_num=62707) as make_dir_062_62707:  # 0m:0.000s
                make_dir_062_62707()
            with MakeDir(r"/Users/Shared/Waves/Sample Libraries Locations", chowner=True, prog_num=62708) as make_dir_063_62708:  # 0m:0.009s
                make_dir_063_62708()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=62709) as make_dir_064_62709:  # 0m:0.010s
                make_dir_064_62709()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=62710) as rm_file_or_dir_065_62710:  # 0m:0.010s
            rm_file_or_dir_065_62710()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=62711) as rm_file_or_dir_066_62711:  # 0m:0.000s
            rm_file_or_dir_066_62711()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=62712) as shell_command_067_62712:  # 0m:0.010s
            shell_command_067_62712()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=62713) as shell_command_068_62713:  # 0m:0.013s
            shell_command_068_62713()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=62714) as shell_command_069_62714:  # 0m:0.009s
            shell_command_069_62714()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=62715) as shell_command_070_62715:  # 0m:1.042s
            shell_command_070_62715()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=62716) as shell_command_071_62716:  # 0m:0.010s
            shell_command_071_62716()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=62717) as shell_command_072_62717:  # 0m:1.056s
            shell_command_072_62717()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=62718) as shell_command_073_62718:  # 0m:0.010s
            shell_command_073_62718()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=62719) as shell_command_074_62719:  # 0m:0.011s
            shell_command_074_62719()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=62720) as shell_command_075_62720:  # 0m:0.166s
            shell_command_075_62720()
        with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/NKS/Grand Rhapsody/Grand Rhapsody Piano Stereo", prog_num=62721) as rm_file_or_dir_076_62721:  # 0m:0.001s
            rm_file_or_dir_076_62721()
        with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Grand Rhapsody Piano Stereo.xml", prog_num=62722) as rm_file_or_dir_077_62722:  # 0m:0.000s
            rm_file_or_dir_077_62722()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=62723) as cd_stage_078_62723:  # 0m:0.013s
            cd_stage_078_62723()
            with SetExecPermissionsInSyncFolder(prog_num=62724) as set_exec_permissions_in_sync_folder_079_62724:  # 0m:0.013s
                set_exec_permissions_in_sync_folder_079_62724()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V16", prog_num=62725) as cd_stage_080_62725:  # 0m:5.938s
            cd_stage_080_62725()
            with Stage(r"copy", r"Bass Fingers application v16.0.23.24", prog_num=62726):  # 0m:0.325s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62727) as should_copy_source_081_62727:  # 0m:0.325s
                    should_copy_source_081_62727()
                    with Stage(r"copy source", r"Mac/Apps/Bass Fingers.app", prog_num=62728):  # 0m:0.325s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", r".", delete_extraneous_files=True, prog_num=62729) as copy_dir_to_dir_082_62729:  # 0m:0.008s
                            copy_dir_to_dir_082_62729()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", where_to_unwtar=r".", prog_num=62730) as unwtar_083_62730:  # 0m:0.316s
                            unwtar_083_62730()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Fingers.app", user_id=-1, group_id=-1, prog_num=62731, recursive=True) as chown_084_62731:  # 0m:0.000s
                            chown_084_62731()
            with Stage(r"copy", r"Bass Slapper application v16.0.23.24", prog_num=62732):  # 0m:0.323s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62733) as should_copy_source_085_62733:  # 0m:0.323s
                    should_copy_source_085_62733()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=62734):  # 0m:0.323s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=62735) as copy_dir_to_dir_086_62735:  # 0m:0.002s
                            copy_dir_to_dir_086_62735()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=62736) as unwtar_087_62736:  # 0m:0.320s
                            unwtar_087_62736()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=62737, recursive=True) as chown_088_62737:  # 0m:0.000s
                            chown_088_62737()
            with Stage(r"copy", r"Codex Wavetable Synth application v16.0.23.24", prog_num=62738):  # 0m:0.316s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62739) as should_copy_source_089_62739:  # 0m:0.316s
                    should_copy_source_089_62739()
                    with Stage(r"copy source", r"Mac/Apps/CODEX.app", prog_num=62740):  # 0m:0.315s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", r".", delete_extraneous_files=True, prog_num=62741) as copy_dir_to_dir_090_62741:  # 0m:0.002s
                            copy_dir_to_dir_090_62741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", where_to_unwtar=r".", prog_num=62742) as unwtar_091_62742:  # 0m:0.313s
                            unwtar_091_62742()
                        with Chown(path=r"/Applications/Waves/Applications V16/CODEX.app", user_id=-1, group_id=-1, prog_num=62743, recursive=True) as chown_092_62743:  # 0m:0.000s
                            chown_092_62743()
            with Stage(r"copy", r"CR8 Sampler application v16.0.23.24", prog_num=62744):  # 0m:0.312s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62745) as should_copy_source_093_62745:  # 0m:0.307s
                    should_copy_source_093_62745()
                    with Stage(r"copy source", r"Mac/Apps/CR8 Sampler.app", prog_num=62746):  # 0m:0.307s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", r".", delete_extraneous_files=True, prog_num=62747) as copy_dir_to_dir_094_62747:  # 0m:0.002s
                            copy_dir_to_dir_094_62747()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", where_to_unwtar=r".", prog_num=62748) as unwtar_095_62748:  # 0m:0.304s
                            unwtar_095_62748()
                        with Chown(path=r"/Applications/Waves/Applications V16/CR8 Sampler.app", user_id=-1, group_id=-1, prog_num=62749, recursive=True) as chown_096_62749:  # 0m:0.000s
                            chown_096_62749()
            with Stage(r"copy", r"Clavinet application v16.0.23.24", prog_num=62750):  # 0m:0.327s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62751) as should_copy_source_097_62751:  # 0m:0.327s
                    should_copy_source_097_62751()
                    with Stage(r"copy source", r"Mac/Apps/Clavinet.app", prog_num=62752):  # 0m:0.327s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", r".", delete_extraneous_files=True, prog_num=62753) as copy_dir_to_dir_098_62753:  # 0m:0.002s
                            copy_dir_to_dir_098_62753()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", where_to_unwtar=r".", prog_num=62754) as unwtar_099_62754:  # 0m:0.324s
                            unwtar_099_62754()
                        with Chown(path=r"/Applications/Waves/Applications V16/Clavinet.app", user_id=-1, group_id=-1, prog_num=62755, recursive=True) as chown_100_62755:  # 0m:0.000s
                            chown_100_62755()
            with Stage(r"copy", r"Electric 200 Piano application v16.0.23.24", prog_num=62756):  # 0m:0.326s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62757) as should_copy_source_101_62757:  # 0m:0.326s
                    should_copy_source_101_62757()
                    with Stage(r"copy source", r"Mac/Apps/Electric200.app", prog_num=62758):  # 0m:0.326s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", r".", delete_extraneous_files=True, prog_num=62759) as copy_dir_to_dir_102_62759:  # 0m:0.002s
                            copy_dir_to_dir_102_62759()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", where_to_unwtar=r".", prog_num=62760) as unwtar_103_62760:  # 0m:0.323s
                            unwtar_103_62760()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric200.app", user_id=-1, group_id=-1, prog_num=62761, recursive=True) as chown_104_62761:  # 0m:0.000s
                            chown_104_62761()
            with Stage(r"copy", r"Electric 88 Piano application v16.0.23.24", prog_num=62762):  # 0m:0.293s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62763) as should_copy_source_105_62763:  # 0m:0.293s
                    should_copy_source_105_62763()
                    with Stage(r"copy source", r"Mac/Apps/Electric88.app", prog_num=62764):  # 0m:0.293s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", r".", delete_extraneous_files=True, prog_num=62765) as copy_dir_to_dir_106_62765:  # 0m:0.007s
                            copy_dir_to_dir_106_62765()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", where_to_unwtar=r".", prog_num=62766) as unwtar_107_62766:  # 0m:0.285s
                            unwtar_107_62766()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric88.app", user_id=-1, group_id=-1, prog_num=62767, recursive=True) as chown_108_62767:  # 0m:0.000s
                            chown_108_62767()
            with Stage(r"copy", r"Electric Grand 80 application v16.0.23.24", prog_num=62768):  # 0m:0.352s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62769) as should_copy_source_109_62769:  # 0m:0.352s
                    should_copy_source_109_62769()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=62770):  # 0m:0.352s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=62771) as copy_dir_to_dir_110_62771:  # 0m:0.002s
                            copy_dir_to_dir_110_62771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=62772) as unwtar_111_62772:  # 0m:0.349s
                            unwtar_111_62772()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=62773, recursive=True) as chown_112_62773:  # 0m:0.000s
                            chown_112_62773()
            with Stage(r"copy", r"Element Virtual Analog Synth application v16.0.23.24", prog_num=62774):  # 0m:0.328s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62775) as should_copy_source_113_62775:  # 0m:0.328s
                    should_copy_source_113_62775()
                    with Stage(r"copy source", r"Mac/Apps/Element.app", prog_num=62776):  # 0m:0.328s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", r".", delete_extraneous_files=True, prog_num=62777) as copy_dir_to_dir_114_62777:  # 0m:0.002s
                            copy_dir_to_dir_114_62777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", where_to_unwtar=r".", prog_num=62778) as unwtar_115_62778:  # 0m:0.325s
                            unwtar_115_62778()
                        with Chown(path=r"/Applications/Waves/Applications V16/Element.app", user_id=-1, group_id=-1, prog_num=62779, recursive=True) as chown_116_62779:  # 0m:0.000s
                            chown_116_62779()
            with Stage(r"copy", r"Flow Motion application v16.0.23.24", prog_num=62780):  # 0m:0.349s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62781) as should_copy_source_117_62781:  # 0m:0.349s
                    should_copy_source_117_62781()
                    with Stage(r"copy source", r"Mac/Apps/Flow Motion.app", prog_num=62782):  # 0m:0.349s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", r".", delete_extraneous_files=True, prog_num=62783) as copy_dir_to_dir_118_62783:  # 0m:0.002s
                            copy_dir_to_dir_118_62783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", where_to_unwtar=r".", prog_num=62784) as unwtar_119_62784:  # 0m:0.346s
                            unwtar_119_62784()
                        with Chown(path=r"/Applications/Waves/Applications V16/Flow Motion.app", user_id=-1, group_id=-1, prog_num=62785, recursive=True) as chown_120_62785:  # 0m:0.000s
                            chown_120_62785()
            with Stage(r"copy", r"GTR Solo application v16.0.23.24", prog_num=62786):  # 0m:0.319s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62787) as should_copy_source_121_62787:  # 0m:0.319s
                    should_copy_source_121_62787()
                    with Stage(r"copy source", r"Mac/Apps/GTRSolo 3.5.app", prog_num=62788):  # 0m:0.318s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", r".", delete_extraneous_files=True, prog_num=62789) as copy_dir_to_dir_122_62789:  # 0m:0.002s
                            copy_dir_to_dir_122_62789()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", where_to_unwtar=r".", prog_num=62790) as unwtar_123_62790:  # 0m:0.316s
                            unwtar_123_62790()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTRSolo 3.5.app", user_id=-1, group_id=-1, prog_num=62791, recursive=True) as chown_124_62791:  # 0m:0.000s
                            chown_124_62791()
            with Stage(r"copy", r"GTR application v16.0.23.24", prog_num=62792):  # 0m:0.323s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62793) as should_copy_source_125_62793:  # 0m:0.323s
                    should_copy_source_125_62793()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=62794):  # 0m:0.322s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=62795) as copy_dir_to_dir_126_62795:  # 0m:0.002s
                            copy_dir_to_dir_126_62795()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=62796) as unwtar_127_62796:  # 0m:0.320s
                            unwtar_127_62796()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=62797, recursive=True) as chown_128_62797:  # 0m:0.000s
                            chown_128_62797()
            with Stage(r"copy", r"Grand Rhapsody application v16.0.23.24", prog_num=62798):  # 0m:0.317s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62799) as should_copy_source_129_62799:  # 0m:0.316s
                    should_copy_source_129_62799()
                    with Stage(r"copy source", r"Mac/Apps/Grand Rhapsody.app", prog_num=62800):  # 0m:0.316s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", r".", delete_extraneous_files=True, prog_num=62801) as copy_dir_to_dir_130_62801:  # 0m:0.002s
                            copy_dir_to_dir_130_62801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", where_to_unwtar=r".", prog_num=62802) as unwtar_131_62802:  # 0m:0.314s
                            unwtar_131_62802()
                        with Chown(path=r"/Applications/Waves/Applications V16/Grand Rhapsody.app", user_id=-1, group_id=-1, prog_num=62803, recursive=True) as chown_132_62803:  # 0m:0.000s
                            chown_132_62803()
            with Stage(r"copy", r"StudioVerse Instruments App v16.0.23.24", prog_num=62804):  # 0m:0.302s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62805) as should_copy_source_133_62805:  # 0m:0.302s
                    should_copy_source_133_62805()
                    with Stage(r"copy source", r"Mac/Apps/StudioVerse Instruments.app", prog_num=62806):  # 0m:0.302s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", r".", delete_extraneous_files=True, prog_num=62807) as copy_dir_to_dir_134_62807:  # 0m:0.002s
                            copy_dir_to_dir_134_62807()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", where_to_unwtar=r".", prog_num=62808) as unwtar_135_62808:  # 0m:0.299s
                            unwtar_135_62808()
                        with Chown(path=r"/Applications/Waves/Applications V16/StudioVerse Instruments.app", user_id=-1, group_id=-1, prog_num=62809, recursive=True) as chown_136_62809:  # 0m:0.000s
                            chown_136_62809()
            with Stage(r"copy", r"OVox Vocal ReSynthesis application v16.0.23.24", prog_num=62810):  # 0m:0.315s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62811) as should_copy_source_137_62811:  # 0m:0.315s
                    should_copy_source_137_62811()
                    with Stage(r"copy source", r"Mac/Apps/OVox.app", prog_num=62812):  # 0m:0.315s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", r".", delete_extraneous_files=True, prog_num=62813) as copy_dir_to_dir_138_62813:  # 0m:0.002s
                            copy_dir_to_dir_138_62813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", where_to_unwtar=r".", prog_num=62814) as unwtar_139_62814:  # 0m:0.312s
                            unwtar_139_62814()
                        with Chown(path=r"/Applications/Waves/Applications V16/OVox.app", user_id=-1, group_id=-1, prog_num=62815, recursive=True) as chown_140_62815:  # 0m:0.000s
                            chown_140_62815()
            with Stage(r"copy", r"PRS Archon application v16.0.23.24", prog_num=62816):  # 0m:0.338s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62817) as should_copy_source_141_62817:  # 0m:0.338s
                    should_copy_source_141_62817()
                    with Stage(r"copy source", r"Mac/Apps/PRS Archon.app", prog_num=62818):  # 0m:0.338s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", r".", delete_extraneous_files=True, prog_num=62819) as copy_dir_to_dir_142_62819:  # 0m:0.002s
                            copy_dir_to_dir_142_62819()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", where_to_unwtar=r".", prog_num=62820) as unwtar_143_62820:  # 0m:0.335s
                            unwtar_143_62820()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS Archon.app", user_id=-1, group_id=-1, prog_num=62821, recursive=True) as chown_144_62821:  # 0m:0.000s
                            chown_144_62821()
            with Stage(r"copy", r"PRS Dallas application v16.0.23.24", prog_num=62822):  # 0m:0.340s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62823) as should_copy_source_145_62823:  # 0m:0.339s
                    should_copy_source_145_62823()
                    with Stage(r"copy source", r"Mac/Apps/PRS Dallas.app", prog_num=62824):  # 0m:0.339s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", r".", delete_extraneous_files=True, prog_num=62825) as copy_dir_to_dir_146_62825:  # 0m:0.002s
                            copy_dir_to_dir_146_62825()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", where_to_unwtar=r".", prog_num=62826) as unwtar_147_62826:  # 0m:0.337s
                            unwtar_147_62826()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS Dallas.app", user_id=-1, group_id=-1, prog_num=62827, recursive=True) as chown_148_62827:  # 0m:0.000s
                            chown_148_62827()
            with Stage(r"copy", r"PRS V9 application v16.0.23.24", prog_num=62828):  # 0m:0.326s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62829) as should_copy_source_149_62829:  # 0m:0.326s
                    should_copy_source_149_62829()
                    with Stage(r"copy source", r"Mac/Apps/PRS V9.app", prog_num=62830):  # 0m:0.326s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", r".", delete_extraneous_files=True, prog_num=62831) as copy_dir_to_dir_150_62831:  # 0m:0.007s
                            copy_dir_to_dir_150_62831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", where_to_unwtar=r".", prog_num=62832) as unwtar_151_62832:  # 0m:0.319s
                            unwtar_151_62832()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS V9.app", user_id=-1, group_id=-1, prog_num=62833, recursive=True) as chown_152_62833:  # 0m:0.000s
                            chown_152_62833()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V16" -c', ignore_all_errors=True, prog_num=62834) as shell_command_153_62834:  # 0m:0.096s
                shell_command_153_62834()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V16"/Icon?; fi', prog_num=62835) as script_command_154_62835:  # 0m:0.010s
                script_command_154_62835()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=62836) as cd_stage_155_62836:  # 0m:15.143s
            cd_stage_155_62836()
            with Stage(r"copy", r"COSMOS__Application v16.0.30.31", prog_num=62837):  # 0m:15.131s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=62838) as should_copy_source_156_62838:  # 0m:15.131s
                    should_copy_source_156_62838()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=62839):  # 0m:15.130s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=62840) as copy_dir_to_dir_157_62840:  # 0m:0.274s
                            copy_dir_to_dir_157_62840()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=62841) as unwtar_158_62841:  # 0m:14.855s
                            unwtar_158_62841()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=62842, recursive=True) as chown_159_62842:  # 0m:0.000s
                            chown_159_62842()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=62852) as resolve_symlink_files_in_folder_160_62852:  # 0m:0.011s
                resolve_symlink_files_in_folder_160_62852()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=62853) as cd_stage_161_62853:  # 0m:24.801s
            cd_stage_161_62853()
            with RmFileOrDir(r"/Applications/Waves/Data/Waves Gems", prog_num=62854) as rm_file_or_dir_162_62854:  # 0m:0.019s
                rm_file_or_dir_162_62854()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=62855):  # 0m:1.355s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62856) as should_copy_source_163_62856:  # 0m:1.355s
                    should_copy_source_163_62856()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=62857):  # 0m:1.354s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=62858) as copy_dir_to_dir_164_62858:  # 0m:1.354s
                            copy_dir_to_dir_164_62858()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=62859, recursive=True) as chown_165_62859:  # 0m:0.000s
                            chown_165_62859()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=62860):  # 0m:5.141s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62861) as should_copy_source_166_62861:  # 0m:5.140s
                    should_copy_source_166_62861()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=62862):  # 0m:5.139s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=62863) as copy_dir_to_dir_167_62863:  # 0m:0.054s
                            copy_dir_to_dir_167_62863()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=62864) as unwtar_168_62864:  # 0m:5.085s
                            unwtar_168_62864()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=62865, recursive=True) as chown_169_62865:  # 0m:0.000s
                            chown_169_62865()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.1", prog_num=62866):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62867) as should_copy_source_170_62867:  # ?
                    should_copy_source_170_62867()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=62868):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=62869) as copy_dir_to_dir_171_62869:  # ?
                            copy_dir_to_dir_171_62869()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=62870, recursive=True) as chown_172_62870:  # 0m:0.001s
                            chown_172_62870()
            with Stage(r"copy", r"Character Filters Data v1.0.0.9", prog_num=62871):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Character Filters", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62872) as should_copy_source_173_62872:  # ?
                    should_copy_source_173_62872()
                    with Stage(r"copy source", r"Common/Data/Character Filters", prog_num=62873):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Character Filters", r".", delete_extraneous_files=True, prog_num=62874) as copy_dir_to_dir_174_62874:  # ?
                            copy_dir_to_dir_174_62874()
                        with Chown(path=r"/Applications/Waves/Data/Character Filters", user_id=-1, group_id=-1, prog_num=62875, recursive=True) as chown_175_62875:  # 0m:0.001s
                            chown_175_62875()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Network__Data_Folders v1.0.1.6", prog_num=62876):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62877) as should_copy_source_176_62877:  # ?
                    should_copy_source_176_62877()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx DeReverb", prog_num=62878):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=62879) as copy_dir_to_dir_177_62879:  # ?
                            copy_dir_to_dir_177_62879()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", where_to_unwtar=r".", prog_num=62880) as unwtar_178_62880:  # ?
                            unwtar_178_62880()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=62881, recursive=True) as chown_179_62881:  # 0m:0.001s
                            chown_179_62881()
            with Stage(r"copy", r"Curves_AQ_Special_Data v1.0.0.4", prog_num=62882):  # 0m:8.147s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62883) as should_copy_source_180_62883:  # 0m:8.146s
                    should_copy_source_180_62883()
                    with Stage(r"copy source", r"Common/Data/Curves", prog_num=62884):  # 0m:8.146s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r".", delete_extraneous_files=True, prog_num=62885) as copy_dir_to_dir_181_62885:  # 0m:3.789s
                            copy_dir_to_dir_181_62885()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", where_to_unwtar=r".", prog_num=62886) as unwtar_182_62886:  # 0m:4.357s
                            unwtar_182_62886()
                        with Chown(path=r"/Applications/Waves/Data/Curves", user_id=-1, group_id=-1, prog_num=62887, recursive=True) as chown_183_62887:  # 0m:0.000s
                            chown_183_62887()
            with Stage(r"copy", r"Waves Gems Data v1.1.0.2", prog_num=62888):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Waves Gems", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62889) as should_copy_source_184_62889:  # 0m:0.101s
                    should_copy_source_184_62889()
                    with Stage(r"copy source", r"Common/Data/Waves Gems", prog_num=62890):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Waves Gems", r".", delete_extraneous_files=True, prog_num=62891) as copy_dir_to_dir_185_62891:  # 0m:0.100s
                            copy_dir_to_dir_185_62891()
                        with Chown(path=r"/Applications/Waves/Data/Waves Gems", user_id=-1, group_id=-1, prog_num=62892, recursive=True) as chown_186_62892:  # 0m:0.000s
                            chown_186_62892()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=62893):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62894) as should_copy_source_187_62894:  # ?
                    should_copy_source_187_62894()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=62895):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=62896) as copy_dir_to_dir_188_62896:  # ?
                            copy_dir_to_dir_188_62896()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=62897, recursive=True) as chown_189_62897:  # 0m:0.001s
                            chown_189_62897()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=62898):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62899) as should_copy_source_190_62899:  # ?
                    should_copy_source_190_62899()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=62900):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=62901) as copy_dir_to_dir_191_62901:  # ?
                            copy_dir_to_dir_191_62901()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=62902, recursive=True) as chown_192_62902:  # 0m:0.000s
                            chown_192_62902()
            with Stage(r"copy", r"Nx Ocean Way Nashville Data v1.0.0.0", prog_num=62903):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Nx Ocean Way Nashville", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62904) as should_copy_source_193_62904:  # ?
                    should_copy_source_193_62904()
                    with Stage(r"copy source", r"Common/Data/Nx Ocean Way Nashville", prog_num=62905):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Nx Ocean Way Nashville", r".", delete_extraneous_files=True, prog_num=62906) as copy_dir_to_dir_194_62906:  # ?
                            copy_dir_to_dir_194_62906()
                        with Chown(path=r"/Applications/Waves/Data/Nx Ocean Way Nashville", user_id=-1, group_id=-1, prog_num=62907, recursive=True) as chown_195_62907:  # 0m:0.000s
                            chown_195_62907()
            with Stage(r"copy", r"Note Mapping Data v1.0.0.10", prog_num=62908):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62909) as should_copy_source_196_62909:  # ?
                    should_copy_source_196_62909()
                    with Stage(r"copy source", r"Common/Data/Note Mapping", prog_num=62910):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", r".", delete_extraneous_files=True, prog_num=62911) as copy_dir_to_dir_197_62911:  # ?
                            copy_dir_to_dir_197_62911()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", where_to_unwtar=r".", prog_num=62912) as unwtar_198_62912:  # ?
                            unwtar_198_62912()
                        with Chown(path=r"/Applications/Waves/Data/Note Mapping", user_id=-1, group_id=-1, prog_num=62913, recursive=True) as chown_199_62913:  # 0m:0.000s
                            chown_199_62913()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=62914):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62915) as should_copy_source_200_62915:  # 0m:0.115s
                    should_copy_source_200_62915()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=62916):  # 0m:0.115s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=62917) as copy_dir_to_dir_201_62917:  # 0m:0.115s
                            copy_dir_to_dir_201_62917()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=62918, recursive=True) as chown_202_62918:  # 0m:0.000s
                            chown_202_62918()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=62919):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62920) as should_copy_source_203_62920:  # ?
                    should_copy_source_203_62920()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=62921):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=62922) as copy_dir_to_dir_204_62922:  # ?
                            copy_dir_to_dir_204_62922()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=62923, recursive=True) as chown_205_62923:  # 0m:0.001s
                            chown_205_62923()
            with Stage(r"copy", r"StudioRack Data v1.0.0.6", prog_num=62924):  # 0m:9.733s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62925) as should_copy_source_206_62925:  # 0m:9.732s
                    should_copy_source_206_62925()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=62926):  # 0m:9.732s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=62927) as copy_dir_to_dir_207_62927:  # 0m:0.026s
                            copy_dir_to_dir_207_62927()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=62928) as unwtar_208_62928:  # 0m:9.705s
                            unwtar_208_62928()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=62929, recursive=True) as chown_209_62929:  # 0m:0.000s
                            chown_209_62929()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.2.0", prog_num=62930):  # 0m:0.161s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62931) as should_copy_source_210_62931:  # 0m:0.161s
                    should_copy_source_210_62931()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=62932):  # 0m:0.160s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=62933) as copy_dir_to_dir_211_62933:  # 0m:0.160s
                            copy_dir_to_dir_211_62933()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=62934, recursive=True) as chown_212_62934:  # 0m:0.000s
                            chown_212_62934()
            with Stage(r"copy", r"SyncVx Data v1.0.0.2", prog_num=62935):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62936) as should_copy_source_213_62936:  # ?
                    should_copy_source_213_62936()
                    with Stage(r"copy source", r"Common/Data/SyncVx", prog_num=62937):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r".", delete_extraneous_files=True, prog_num=62938) as copy_dir_to_dir_214_62938:  # ?
                            copy_dir_to_dir_214_62938()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", where_to_unwtar=r".", prog_num=62939) as unwtar_215_62939:  # ?
                            unwtar_215_62939()
                        with Chown(path=r"/Applications/Waves/Data/SyncVx", user_id=-1, group_id=-1, prog_num=62940, recursive=True) as chown_216_62940:  # 0m:0.001s
                            chown_216_62940()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=62941):  # 0m:0.022s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62942) as should_copy_source_217_62942:  # 0m:0.021s
                    should_copy_source_217_62942()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=62943):  # 0m:0.021s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=62944) as copy_dir_to_dir_218_62944:  # 0m:0.010s
                            copy_dir_to_dir_218_62944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", where_to_unwtar=r".", prog_num=62945) as unwtar_219_62945:  # 0m:0.011s
                            unwtar_219_62945()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=62946, recursive=True) as chown_220_62946:  # 0m:0.000s
                            chown_220_62946()
            with RmFileOrDir(r"/Applications/Waves/Data/Nx Ocean Way Nashville/44.1", prog_num=62947) as rm_file_or_dir_221_62947:  # 0m:0.000s
                rm_file_or_dir_221_62947()
            with RmFileOrDir(r"/Applications/Waves/Data/Nx Ocean Way Nashville/48", prog_num=62948) as rm_file_or_dir_222_62948:  # 0m:0.000s
                rm_file_or_dir_222_62948()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Chromatic.scale", prog_num=62949) as rm_file_or_dir_223_62949:  # 0m:0.000s
                rm_file_or_dir_223_62949()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Major.scale", prog_num=62950) as rm_file_or_dir_224_62950:  # 0m:0.000s
                rm_file_or_dir_224_62950()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Natural Minor.scale", prog_num=62951) as rm_file_or_dir_225_62951:  # 0m:0.000s
                rm_file_or_dir_225_62951()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=62952) as rm_globs_226_62952:  # 0m:0.000s
                rm_globs_226_62952()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=62953) as cd_stage_227_62953:  # 0m:7.217s
            cd_stage_227_62953()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=62954):  # 0m:7.217s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=62955) as should_copy_source_228_62955:  # 0m:0.001s
                    should_copy_source_228_62955()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=62956):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r".", prog_num=62957) as copy_file_to_dir_229_62957:  # 0m:0.001s
                            copy_file_to_dir_229_62957()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=62958) as chmod_and_chown_230_62958:  # 0m:0.000s
                            chmod_and_chown_230_62958()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=62959) as should_copy_source_231_62959:  # 0m:7.216s
                    should_copy_source_231_62959()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=62960):  # 0m:7.216s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=62961) as copy_dir_to_dir_232_62961:  # 0m:0.017s
                            copy_dir_to_dir_232_62961()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=62962) as unwtar_233_62962:  # 0m:7.198s
                            unwtar_233_62962()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=62963, recursive=True) as chown_234_62963:  # 0m:0.000s
                            chown_234_62963()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=62964) as cd_stage_235_62964:  # 0m:0.161s
            cd_stage_235_62964()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=62965):  # 0m:0.036s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62966) as should_copy_source_236_62966:  # 0m:0.025s
                    should_copy_source_236_62966()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=62967):  # 0m:0.024s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=62968) as copy_dir_to_dir_237_62968:  # 0m:0.024s
                            copy_dir_to_dir_237_62968()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=62969, recursive=True) as chown_238_62969:  # 0m:0.000s
                            chown_238_62969()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62970) as should_copy_source_239_62970:  # 0m:0.011s
                    should_copy_source_239_62970()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=62971):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=62972) as copy_dir_to_dir_240_62972:  # 0m:0.011s
                            copy_dir_to_dir_240_62972()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=62973, recursive=True) as chown_241_62973:  # 0m:0.000s
                            chown_241_62973()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=62974):  # 0m:0.082s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62975) as should_copy_source_242_62975:  # 0m:0.011s
                    should_copy_source_242_62975()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=62976):  # 0m:0.011s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=62977) as copy_dir_to_dir_243_62977:  # 0m:0.011s
                            copy_dir_to_dir_243_62977()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=62978, recursive=True) as chown_244_62978:  # 0m:0.000s
                            chown_244_62978()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62979) as should_copy_source_245_62979:  # 0m:0.070s
                    should_copy_source_245_62979()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=62980):  # 0m:0.070s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=62981) as copy_dir_to_dir_246_62981:  # 0m:0.070s
                            copy_dir_to_dir_246_62981()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=62982, recursive=True) as chown_247_62982:  # 0m:0.000s
                            chown_247_62982()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=62983):  # 0m:0.043s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62984) as should_copy_source_248_62984:  # 0m:0.021s
                    should_copy_source_248_62984()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=62985):  # 0m:0.020s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=62986) as copy_dir_to_dir_249_62986:  # 0m:0.020s
                            copy_dir_to_dir_249_62986()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=62987, recursive=True) as chown_250_62987:  # 0m:0.000s
                            chown_250_62987()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62988) as should_copy_source_251_62988:  # 0m:0.022s
                    should_copy_source_251_62988()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=62989):  # 0m:0.022s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=62990) as copy_dir_to_dir_252_62990:  # 0m:0.021s
                            copy_dir_to_dir_252_62990()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=62991, recursive=True) as chown_253_62991:  # 0m:0.000s
                            chown_253_62991()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=62992) as cd_stage_254_62992:  # 0m:0.003s
            cd_stage_254_62992()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=62993):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=62994) as should_copy_source_255_62994:  # 0m:0.001s
                    should_copy_source_255_62994()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=62995):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=62996) as copy_file_to_dir_256_62996:  # 0m:0.001s
                            copy_file_to_dir_256_62996()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=62997) as chmod_and_chown_257_62997:  # 0m:0.000s
                            chmod_and_chown_257_62997()
            with Stage(r"copy", r"Grand Rhapsody Misc Data", prog_num=62998):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=62999) as should_copy_source_258_62999:  # 0m:0.001s
                    should_copy_source_258_62999()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", prog_num=63000):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", r".", prog_num=63001) as copy_file_to_dir_259_63001:  # 0m:0.000s
                            copy_file_to_dir_259_63001()
                        with ChmodAndChown(path=r"Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=63002) as chmod_and_chown_260_63002:  # 0m:0.000s
                            chmod_and_chown_260_63002()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", prog_num=63003) as rm_file_or_dir_261_63003:  # 0m:0.000s
                rm_file_or_dir_261_63003()
            with RemoveEmptyFolders(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody", prog_num=63004) as remove_empty_folders_262_63004:  # 0m:0.000s
                remove_empty_folders_262_63004()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=63005) as cd_stage_263_63005:  # 0m:0.122s
            cd_stage_263_63005()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Echosphere/Artist", prog_num=63006) as rm_file_or_dir_264_63006:  # 0m:0.000s
                rm_file_or_dir_264_63006()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Echosphere", prog_num=63007) as rm_file_or_dir_265_63007:  # 0m:0.017s
                rm_file_or_dir_265_63007()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Epic/Artist", prog_num=63008) as rm_file_or_dir_266_63008:  # 0m:0.000s
                rm_file_or_dir_266_63008()
            with Stage(r"copy", r"Abbey Road Saturator Presets v1.0.0.6", prog_num=63009):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Abbey Road Saturator", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63010) as should_copy_source_267_63010:  # ?
                    should_copy_source_267_63010()
                    with Stage(r"copy source", r"Common/Data/Presets/Abbey Road Saturator", prog_num=63011):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Abbey Road Saturator", r".", delete_extraneous_files=True, prog_num=63012) as copy_dir_to_dir_268_63012:  # ?
                            copy_dir_to_dir_268_63012()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Abbey Road Saturator", user_id=-1, group_id=-1, prog_num=63013, recursive=True) as chown_269_63013:  # 0m:0.001s
                            chown_269_63013()
            with Stage(r"copy", r"BB Tubes Presets v1.0.0.6", prog_num=63014):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/BB Tubes", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63015) as should_copy_source_270_63015:  # ?
                    should_copy_source_270_63015()
                    with Stage(r"copy source", r"Common/Data/Presets/BB Tubes", prog_num=63016):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/BB Tubes", r".", delete_extraneous_files=True, prog_num=63017) as copy_dir_to_dir_271_63017:  # ?
                            copy_dir_to_dir_271_63017()
                        with Chown(path=r"/Applications/Waves/Data/Presets/BB Tubes", user_id=-1, group_id=-1, prog_num=63018, recursive=True) as chown_272_63018:  # 0m:0.001s
                            chown_272_63018()
            with Stage(r"copy", r"Berzerk Distortion Presets v1.0.0.5", prog_num=63019):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Berzerk Distortion", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63020) as should_copy_source_273_63020:  # ?
                    should_copy_source_273_63020()
                    with Stage(r"copy source", r"Common/Data/Presets/Berzerk Distortion", prog_num=63021):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Berzerk Distortion", r".", delete_extraneous_files=True, prog_num=63022) as copy_dir_to_dir_274_63022:  # ?
                            copy_dir_to_dir_274_63022()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Berzerk Distortion", user_id=-1, group_id=-1, prog_num=63023, recursive=True) as chown_275_63023:  # 0m:0.000s
                            chown_275_63023()
            with Stage(r"copy", r"CLA EchoSphere Presets v1.0.0.9", prog_num=63024):  # 0m:0.063s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA EchoSphere", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63025) as should_copy_source_276_63025:  # 0m:0.063s
                    should_copy_source_276_63025()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA EchoSphere", prog_num=63026):  # 0m:0.063s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA EchoSphere", r".", delete_extraneous_files=True, prog_num=63027) as copy_dir_to_dir_277_63027:  # 0m:0.062s
                            copy_dir_to_dir_277_63027()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA EchoSphere", user_id=-1, group_id=-1, prog_num=63028, recursive=True) as chown_278_63028:  # 0m:0.000s
                            chown_278_63028()
            with Stage(r"copy", r"CLA Epic Presets v1.0.0.15", prog_num=63029):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA Epic", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63030) as should_copy_source_279_63030:  # ?
                    should_copy_source_279_63030()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA Epic", prog_num=63031):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA Epic", r".", delete_extraneous_files=True, prog_num=63032) as copy_dir_to_dir_280_63032:  # ?
                            copy_dir_to_dir_280_63032()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA Epic", user_id=-1, group_id=-1, prog_num=63033, recursive=True) as chown_281_63033:  # 0m:0.000s
                            chown_281_63033()
            with Stage(r"copy", r"CLA MixHub Presets v1.0.0.8", prog_num=63034):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA MixHub", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63035) as should_copy_source_282_63035:  # ?
                    should_copy_source_282_63035()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA MixHub", prog_num=63036):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA MixHub", r".", delete_extraneous_files=True, prog_num=63037) as copy_dir_to_dir_283_63037:  # ?
                            copy_dir_to_dir_283_63037()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA MixHub", user_id=-1, group_id=-1, prog_num=63038, recursive=True) as chown_284_63038:  # 0m:0.000s
                            chown_284_63038()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=63039):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63040) as should_copy_source_285_63040:  # ?
                    should_copy_source_285_63040()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=63041):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=63042) as copy_dir_to_dir_286_63042:  # ?
                            copy_dir_to_dir_286_63042()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=63043, recursive=True) as chown_287_63043:  # 0m:0.000s
                            chown_287_63043()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Pro__Presets v1.0.2.1", prog_num=63044):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63045) as should_copy_source_288_63045:  # ?
                    should_copy_source_288_63045()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb Pro", prog_num=63046):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r".", delete_extraneous_files=True, prog_num=63047) as copy_dir_to_dir_289_63047:  # ?
                            copy_dir_to_dir_289_63047()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb Pro", user_id=-1, group_id=-1, prog_num=63048, recursive=True) as chown_290_63048:  # 0m:0.000s
                            chown_290_63048()
            with Stage(r"copy", r"Clarity_Vx_DeReverb__Presets v1.0.2.1", prog_num=63049):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63050) as should_copy_source_291_63050:  # ?
                    should_copy_source_291_63050()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb", prog_num=63051):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=63052) as copy_dir_to_dir_292_63052:  # ?
                            copy_dir_to_dir_292_63052()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=63053, recursive=True) as chown_293_63053:  # 0m:0.000s
                            chown_293_63053()
            with Stage(r"copy", r"Clarity_Vx_Pro__Presets v1.0.1.8", prog_num=63054):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63055) as should_copy_source_294_63055:  # ?
                    should_copy_source_294_63055()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx Pro", prog_num=63056):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r".", delete_extraneous_files=True, prog_num=63057) as copy_dir_to_dir_295_63057:  # ?
                            copy_dir_to_dir_295_63057()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx Pro", user_id=-1, group_id=-1, prog_num=63058, recursive=True) as chown_296_63058:  # 0m:0.000s
                            chown_296_63058()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=63059):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63060) as should_copy_source_297_63060:  # ?
                    should_copy_source_297_63060()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=63061):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=63062) as copy_dir_to_dir_298_63062:  # ?
                            copy_dir_to_dir_298_63062()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=63063, recursive=True) as chown_299_63063:  # 0m:0.001s
                            chown_299_63063()
            with Stage(r"copy", r"Curves_AQ__Presets v1.0.0.1", prog_num=63064):  # 0m:0.008s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63065) as should_copy_source_300_63065:  # 0m:0.008s
                    should_copy_source_300_63065()
                    with Stage(r"copy source", r"Common/Data/Presets/Curves AQ", prog_num=63066):  # 0m:0.008s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r".", delete_extraneous_files=True, prog_num=63067) as copy_dir_to_dir_301_63067:  # 0m:0.007s
                            copy_dir_to_dir_301_63067()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Curves AQ", user_id=-1, group_id=-1, prog_num=63068, recursive=True) as chown_302_63068:  # 0m:0.000s
                            chown_302_63068()
            with Stage(r"copy", r"Curves_Equator__Presets v1.0.0.8", prog_num=63069):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves Equator", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63070) as should_copy_source_303_63070:  # ?
                    should_copy_source_303_63070()
                    with Stage(r"copy source", r"Common/Data/Presets/Curves Equator", prog_num=63071):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves Equator", r".", delete_extraneous_files=True, prog_num=63072) as copy_dir_to_dir_304_63072:  # ?
                            copy_dir_to_dir_304_63072()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Curves Equator", user_id=-1, group_id=-1, prog_num=63073, recursive=True) as chown_305_63073:  # 0m:0.000s
                            chown_305_63073()
            with Stage(r"copy", r"Kaleidoscopes Presets v1.1.0.0", prog_num=63074):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Kaleidoscopes", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63075) as should_copy_source_306_63075:  # ?
                    should_copy_source_306_63075()
                    with Stage(r"copy source", r"Common/Data/Presets/Kaleidoscopes", prog_num=63076):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Kaleidoscopes", r".", delete_extraneous_files=True, prog_num=63077) as copy_dir_to_dir_307_63077:  # ?
                            copy_dir_to_dir_307_63077()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Kaleidoscopes", user_id=-1, group_id=-1, prog_num=63078, recursive=True) as chown_308_63078:  # 0m:0.000s
                            chown_308_63078()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=63079):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63080) as should_copy_source_309_63080:  # ?
                    should_copy_source_309_63080()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=63081):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=63082) as copy_dir_to_dir_310_63082:  # ?
                            copy_dir_to_dir_310_63082()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=63083, recursive=True) as chown_311_63083:  # 0m:0.000s
                            chown_311_63083()
            with Stage(r"copy", r"MDMX Fuzz Presets v1.0.0.4", prog_num=63084):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Fuzz", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63085) as should_copy_source_312_63085:  # ?
                    should_copy_source_312_63085()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Fuzz", prog_num=63086):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Fuzz", r".", delete_extraneous_files=True, prog_num=63087) as copy_dir_to_dir_313_63087:  # ?
                            copy_dir_to_dir_313_63087()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Fuzz", user_id=-1, group_id=-1, prog_num=63088, recursive=True) as chown_314_63088:  # 0m:0.000s
                            chown_314_63088()
            with Stage(r"copy", r"MDMX OverDrive Presets v1.0.0.4", prog_num=63089):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX OverDrive", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63090) as should_copy_source_315_63090:  # ?
                    should_copy_source_315_63090()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX OverDrive", prog_num=63091):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX OverDrive", r".", delete_extraneous_files=True, prog_num=63092) as copy_dir_to_dir_316_63092:  # ?
                            copy_dir_to_dir_316_63092()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX OverDrive", user_id=-1, group_id=-1, prog_num=63093, recursive=True) as chown_317_63093:  # 0m:0.000s
                            chown_317_63093()
            with Stage(r"copy", r"MDMX Screamer Presets v1.0.0.4", prog_num=63094):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Screamer", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63095) as should_copy_source_318_63095:  # ?
                    should_copy_source_318_63095()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Screamer", prog_num=63096):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Screamer", r".", delete_extraneous_files=True, prog_num=63097) as copy_dir_to_dir_319_63097:  # ?
                            copy_dir_to_dir_319_63097()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Screamer", user_id=-1, group_id=-1, prog_num=63098, recursive=True) as chown_320_63098:  # 0m:0.000s
                            chown_320_63098()
            with Stage(r"copy", r"MagmaChannelStrip__Presets v1.0.0.4", prog_num=63099):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaChannelStrip", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63100) as should_copy_source_321_63100:  # ?
                    should_copy_source_321_63100()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaChannelStrip", prog_num=63101):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaChannelStrip", r".", delete_extraneous_files=True, prog_num=63102) as copy_dir_to_dir_322_63102:  # ?
                            copy_dir_to_dir_322_63102()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaChannelStrip", user_id=-1, group_id=-1, prog_num=63103, recursive=True) as chown_323_63103:  # 0m:0.000s
                            chown_323_63103()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=63104):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63105) as should_copy_source_324_63105:  # ?
                    should_copy_source_324_63105()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=63106):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=63107) as copy_dir_to_dir_325_63107:  # ?
                            copy_dir_to_dir_325_63107()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=63108, recursive=True) as chown_326_63108:  # 0m:0.000s
                            chown_326_63108()
            with Stage(r"copy", r"MultiMod Distortion Rack Presets v1.0.0.11", prog_num=63109):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MultiMod Rack", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63110) as should_copy_source_327_63110:  # ?
                    should_copy_source_327_63110()
                    with Stage(r"copy source", r"Common/Data/Presets/MultiMod Rack", prog_num=63111):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MultiMod Rack", r".", delete_extraneous_files=True, prog_num=63112) as copy_dir_to_dir_328_63112:  # ?
                            copy_dir_to_dir_328_63112()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MultiMod Rack", user_id=-1, group_id=-1, prog_num=63113, recursive=True) as chown_329_63113:  # 0m:0.000s
                            chown_329_63113()
            with Stage(r"copy", r"OVox Instrument Presets v1.0.0.1", prog_num=63114):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Instrument", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63115) as should_copy_source_330_63115:  # ?
                    should_copy_source_330_63115()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Instrument", prog_num=63116):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Instrument", r".", delete_extraneous_files=True, prog_num=63117) as copy_dir_to_dir_331_63117:  # ?
                            copy_dir_to_dir_331_63117()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Instrument", user_id=-1, group_id=-1, prog_num=63118, recursive=True) as chown_332_63118:  # 0m:0.000s
                            chown_332_63118()
            with Stage(r"copy", r"OVox Vocal ReSynthesis Presets v1.1.0.2", prog_num=63119):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Vocal ReSynthesis", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63120) as should_copy_source_333_63120:  # ?
                    should_copy_source_333_63120()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Vocal ReSynthesis", prog_num=63121):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Vocal ReSynthesis", r".", delete_extraneous_files=True, prog_num=63122) as copy_dir_to_dir_334_63122:  # ?
                            copy_dir_to_dir_334_63122()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Vocal ReSynthesis", user_id=-1, group_id=-1, prog_num=63123, recursive=True) as chown_335_63123:  # 0m:0.000s
                            chown_335_63123()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=63124):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63125) as should_copy_source_336_63125:  # ?
                    should_copy_source_336_63125()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=63126):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=63127) as copy_dir_to_dir_337_63127:  # ?
                            copy_dir_to_dir_337_63127()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=63128, recursive=True) as chown_338_63128:  # 0m:0.007s
                            chown_338_63128()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=63129):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63130) as should_copy_source_339_63130:  # ?
                    should_copy_source_339_63130()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=63131):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=63132) as copy_dir_to_dir_340_63132:  # ?
                            copy_dir_to_dir_340_63132()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=63133, recursive=True) as chown_341_63133:  # 0m:0.000s
                            chown_341_63133()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=63134):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63135) as should_copy_source_342_63135:  # ?
                    should_copy_source_342_63135()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=63136):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=63137) as copy_dir_to_dir_343_63137:  # ?
                            copy_dir_to_dir_343_63137()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=63138, recursive=True) as chown_344_63138:  # 0m:0.000s
                            chown_344_63138()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=63139):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63140) as should_copy_source_345_63140:  # ?
                    should_copy_source_345_63140()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=63141):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=63142) as copy_dir_to_dir_346_63142:  # ?
                            copy_dir_to_dir_346_63142()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=63143, recursive=True) as chown_347_63143:  # 0m:0.001s
                            chown_347_63143()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=63144):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63145) as should_copy_source_348_63145:  # ?
                    should_copy_source_348_63145()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=63146):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=63147) as copy_dir_to_dir_349_63147:  # ?
                            copy_dir_to_dir_349_63147()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=63148, recursive=True) as chown_350_63148:  # 0m:0.000s
                            chown_350_63148()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=63149):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63150) as should_copy_source_351_63150:  # ?
                    should_copy_source_351_63150()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=63151):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=63152) as copy_dir_to_dir_352_63152:  # ?
                            copy_dir_to_dir_352_63152()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=63153, recursive=True) as chown_353_63153:  # 0m:0.001s
                            chown_353_63153()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=63154):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63155) as should_copy_source_354_63155:  # ?
                    should_copy_source_354_63155()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=63156):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=63157) as copy_dir_to_dir_355_63157:  # ?
                            copy_dir_to_dir_355_63157()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=63158, recursive=True) as chown_356_63158:  # 0m:0.000s
                            chown_356_63158()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=63159):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63160) as should_copy_source_357_63160:  # ?
                    should_copy_source_357_63160()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=63161):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=63162) as copy_dir_to_dir_358_63162:  # ?
                            copy_dir_to_dir_358_63162()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=63163, recursive=True) as chown_359_63163:  # 0m:0.000s
                            chown_359_63163()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=63164):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63165) as should_copy_source_360_63165:  # ?
                    should_copy_source_360_63165()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=63166):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=63167) as copy_dir_to_dir_361_63167:  # ?
                            copy_dir_to_dir_361_63167()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=63168, recursive=True) as chown_362_63168:  # 0m:0.000s
                            chown_362_63168()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=63169):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63170) as should_copy_source_363_63170:  # ?
                    should_copy_source_363_63170()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=63171):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=63172) as copy_dir_to_dir_364_63172:  # ?
                            copy_dir_to_dir_364_63172()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=63173, recursive=True) as chown_365_63173:  # 0m:0.000s
                            chown_365_63173()
            with Stage(r"copy", r"SSL_EV2__Presets v1.0.0.7", prog_num=63174):  # 0m:0.007s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/SSL EV2 Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63175) as should_copy_source_366_63175:  # ?
                    should_copy_source_366_63175()
                    with Stage(r"copy source", r"Common/Data/Presets/SSL EV2 Channel", prog_num=63176):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/SSL EV2 Channel", r".", delete_extraneous_files=True, prog_num=63177) as copy_dir_to_dir_367_63177:  # ?
                            copy_dir_to_dir_367_63177()
                        with Chown(path=r"/Applications/Waves/Data/Presets/SSL EV2 Channel", user_id=-1, group_id=-1, prog_num=63178, recursive=True) as chown_368_63178:  # 0m:0.007s
                            chown_368_63178()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=63179):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63180) as should_copy_source_369_63180:  # ?
                    should_copy_source_369_63180()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=63181):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=63182) as copy_dir_to_dir_370_63182:  # ?
                            copy_dir_to_dir_370_63182()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=63183, recursive=True) as chown_371_63183:  # 0m:0.000s
                            chown_371_63183()
            with Stage(r"copy", r"Space_Rider__Presets v1.0.0.4", prog_num=63184):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Space Rider", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63185) as should_copy_source_372_63185:  # ?
                    should_copy_source_372_63185()
                    with Stage(r"copy source", r"Common/Data/Presets/Space Rider", prog_num=63186):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Space Rider", r".", delete_extraneous_files=True, prog_num=63187) as copy_dir_to_dir_373_63187:  # ?
                            copy_dir_to_dir_373_63187()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Space Rider", user_id=-1, group_id=-1, prog_num=63188, recursive=True) as chown_374_63188:  # 0m:0.000s
                            chown_374_63188()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=63189):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63190) as should_copy_source_375_63190:  # ?
                    should_copy_source_375_63190()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=63191):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=63192) as copy_dir_to_dir_376_63192:  # ?
                            copy_dir_to_dir_376_63192()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=63193, recursive=True) as chown_377_63193:  # 0m:0.000s
                            chown_377_63193()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=63194):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63195) as should_copy_source_378_63195:  # ?
                    should_copy_source_378_63195()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=63196):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=63197) as copy_dir_to_dir_379_63197:  # ?
                            copy_dir_to_dir_379_63197()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=63198, recursive=True) as chown_380_63198:  # 0m:0.000s
                            chown_380_63198()
            with Stage(r"copy", r"Vocal Bender Presets v1.0.0.10", prog_num=63199):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Vocal Bender", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63200) as should_copy_source_381_63200:  # ?
                    should_copy_source_381_63200()
                    with Stage(r"copy source", r"Common/Data/Presets/Vocal Bender", prog_num=63201):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Vocal Bender", r".", delete_extraneous_files=True, prog_num=63202) as copy_dir_to_dir_382_63202:  # ?
                            copy_dir_to_dir_382_63202()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Vocal Bender", user_id=-1, group_id=-1, prog_num=63203, recursive=True) as chown_383_63203:  # 0m:0.000s
                            chown_383_63203()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=63204):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63205) as should_copy_source_384_63205:  # ?
                    should_copy_source_384_63205()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=63206):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=63207) as copy_dir_to_dir_385_63207:  # ?
                            copy_dir_to_dir_385_63207()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=63208, recursive=True) as chown_386_63208:  # 0m:0.000s
                            chown_386_63208()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=63209):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63210) as should_copy_source_387_63210:  # ?
                    should_copy_source_387_63210()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=63211):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=63212) as copy_dir_to_dir_388_63212:  # ?
                            copy_dir_to_dir_388_63212()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=63213, recursive=True) as chown_389_63213:  # 0m:0.000s
                            chown_389_63213()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=63214):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63215) as should_copy_source_390_63215:  # ?
                    should_copy_source_390_63215()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=63216):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=63217) as copy_dir_to_dir_391_63217:  # ?
                            copy_dir_to_dir_391_63217()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=63218, recursive=True) as chown_392_63218:  # 0m:0.001s
                            chown_392_63218()
            with RmFileOrDir(r"/Applications/Waves/Data/CLA MixHub Data", prog_num=63219) as rm_file_or_dir_393_63219:  # 0m:0.000s
                rm_file_or_dir_393_63219()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/Vocal Bender", prog_num=63220) as rm_file_or_dir_394_63220:  # 0m:0.000s
                rm_file_or_dir_394_63220()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Vocal Bender Stereo.xml", prog_num=63221) as rm_file_or_dir_395_63221:  # 0m:0.000s
                rm_file_or_dir_395_63221()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=63222) as cd_stage_396_63222:  # 0m:0.008s
            cd_stage_396_63222()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=63223):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63224) as should_copy_source_397_63224:  # ?
                    should_copy_source_397_63224()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=63225):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=63226) as copy_dir_to_dir_398_63226:  # ?
                            copy_dir_to_dir_398_63226()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=63227, recursive=True) as chown_399_63227:  # 0m:0.000s
                            chown_399_63227()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=63228):  # 0m:0.006s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63229) as should_copy_source_400_63229:  # ?
                    should_copy_source_400_63229()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=63230):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=63231) as copy_dir_to_dir_401_63231:  # ?
                            copy_dir_to_dir_401_63231()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=63232, recursive=True) as chown_402_63232:  # 0m:0.006s
                            chown_402_63232()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=63233):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63234) as should_copy_source_403_63234:  # ?
                    should_copy_source_403_63234()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=63235):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=63236) as copy_dir_to_dir_404_63236:  # ?
                            copy_dir_to_dir_404_63236()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=63237, recursive=True) as chown_405_63237:  # 0m:0.000s
                            chown_405_63237()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=63238):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63239) as should_copy_source_406_63239:  # ?
                    should_copy_source_406_63239()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=63240):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=63241) as copy_dir_to_dir_407_63241:  # ?
                            copy_dir_to_dir_407_63241()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=63242, recursive=True) as chown_408_63242:  # 0m:0.000s
                            chown_408_63242()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=63243):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63244) as should_copy_source_409_63244:  # ?
                    should_copy_source_409_63244()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=63245):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=63246) as copy_dir_to_dir_410_63246:  # ?
                            copy_dir_to_dir_410_63246()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=63247, recursive=True) as chown_411_63247:  # 0m:0.000s
                            chown_411_63247()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=63248):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63249) as should_copy_source_412_63249:  # ?
                    should_copy_source_412_63249()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=63250):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=63251) as copy_dir_to_dir_413_63251:  # ?
                            copy_dir_to_dir_413_63251()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=63252, recursive=True) as chown_414_63252:  # 0m:0.000s
                            chown_414_63252()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=63253):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63254) as should_copy_source_415_63254:  # ?
                    should_copy_source_415_63254()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=63255):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=63256) as copy_dir_to_dir_416_63256:  # ?
                            copy_dir_to_dir_416_63256()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=63257, recursive=True) as chown_417_63257:  # 0m:0.000s
                            chown_417_63257()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=63258) as cd_stage_418_63258:  # 0m:0.001s
            cd_stage_418_63258()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=63259):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=63260) as should_copy_source_419_63260:  # ?
                    should_copy_source_419_63260()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=63261):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=63262) as copy_dir_to_dir_420_63262:  # ?
                            copy_dir_to_dir_420_63262()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=63263, recursive=True) as chown_421_63263:  # 0m:0.000s
                            chown_421_63263()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=63264):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=63265) as should_copy_source_422_63265:  # ?
                    should_copy_source_422_63265()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=63266):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=63267) as copy_dir_to_dir_423_63267:  # ?
                            copy_dir_to_dir_423_63267()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=63268, recursive=True) as chown_424_63268:  # 0m:0.000s
                            chown_424_63268()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=63269) as cd_stage_425_63269:  # 0m:0.137s
            cd_stage_425_63269()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=63270):  # 0m:0.137s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=63271) as should_copy_source_426_63271:  # 0m:0.013s
                    should_copy_source_426_63271()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=63272):  # 0m:0.012s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=63273) as unwtar_427_63273:  # 0m:0.012s
                            unwtar_427_63273()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=63274) as should_copy_source_428_63274:  # 0m:0.124s
                    should_copy_source_428_63274()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=63275):  # 0m:0.119s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=63276) as unwtar_429_63276:  # 0m:0.118s
                            unwtar_429_63276()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=63277) as cd_stage_430_63277:  # 0m:0.033s
            cd_stage_430_63277()
            with Stage(r"copy", r"GTR Solo Presets v1.1.0.0", prog_num=63278):  # 0m:0.012s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR-Solo", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=63279) as should_copy_source_431_63279:  # 0m:0.012s
                    should_copy_source_431_63279()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR-Solo", prog_num=63280):  # 0m:0.011s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR-Solo.wtar.aa", where_to_unwtar=r".", prog_num=63281) as unwtar_432_63281:  # 0m:0.011s
                            unwtar_432_63281()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=63282):  # 0m:0.021s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=63283) as should_copy_source_433_63283:  # 0m:0.021s
                    should_copy_source_433_63283()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=63284):  # 0m:0.021s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=63285) as unwtar_434_63285:  # 0m:0.021s
                            unwtar_434_63285()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=63286) as cd_stage_435_63286:  # 4m:16.067s
            cd_stage_435_63286()
            with Stage(r"copy", r"API-2500 v16.0.23.24", prog_num=63287):  # 0m:0.432s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63288) as should_copy_source_436_63288:  # 0m:0.432s
                    should_copy_source_436_63288()
                    with Stage(r"copy source", r"Mac/Plugins/API-2500.bundle", prog_num=63289):  # 0m:0.431s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", r".", delete_extraneous_files=True, prog_num=63290) as copy_dir_to_dir_437_63290:  # 0m:0.008s
                            copy_dir_to_dir_437_63290()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", where_to_unwtar=r".", prog_num=63291) as unwtar_438_63291:  # 0m:0.422s
                            unwtar_438_63291()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-2500.bundle", user_id=-1, group_id=-1, prog_num=63292, recursive=True) as chown_439_63292:  # 0m:0.000s
                            chown_439_63292()
            with Stage(r"copy", r"API-550 v16.0.23.24", prog_num=63293):  # 0m:0.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63294) as should_copy_source_440_63294:  # 0m:0.172s
                    should_copy_source_440_63294()
                    with Stage(r"copy source", r"Mac/Plugins/API-550.bundle", prog_num=63295):  # 0m:0.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", r".", delete_extraneous_files=True, prog_num=63296) as copy_dir_to_dir_441_63296:  # 0m:0.002s
                            copy_dir_to_dir_441_63296()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", where_to_unwtar=r".", prog_num=63297) as unwtar_442_63297:  # 0m:0.169s
                            unwtar_442_63297()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-550.bundle", user_id=-1, group_id=-1, prog_num=63298, recursive=True) as chown_443_63298:  # 0m:0.000s
                            chown_443_63298()
            with Stage(r"copy", r"API-560 v16.0.23.24", prog_num=63299):  # 0m:0.141s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63300) as should_copy_source_444_63300:  # 0m:0.141s
                    should_copy_source_444_63300()
                    with Stage(r"copy source", r"Mac/Plugins/API-560.bundle", prog_num=63301):  # 0m:0.141s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", r".", delete_extraneous_files=True, prog_num=63302) as copy_dir_to_dir_445_63302:  # 0m:0.002s
                            copy_dir_to_dir_445_63302()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", where_to_unwtar=r".", prog_num=63303) as unwtar_446_63303:  # 0m:0.138s
                            unwtar_446_63303()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-560.bundle", user_id=-1, group_id=-1, prog_num=63304, recursive=True) as chown_447_63304:  # 0m:0.000s
                            chown_447_63304()
            with Stage(r"copy", r"Abbey Road Chambers v16.0.23.24", prog_num=63305):  # 0m:2.816s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63306) as should_copy_source_448_63306:  # 0m:2.816s
                    should_copy_source_448_63306()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Chambers.bundle", prog_num=63307):  # 0m:2.816s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", r".", delete_extraneous_files=True, prog_num=63308) as copy_dir_to_dir_449_63308:  # 0m:0.003s
                            copy_dir_to_dir_449_63308()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", where_to_unwtar=r".", prog_num=63309) as unwtar_450_63309:  # 0m:2.813s
                            unwtar_450_63309()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Chambers.bundle", user_id=-1, group_id=-1, prog_num=63310, recursive=True) as chown_451_63310:  # 0m:0.000s
                            chown_451_63310()
            with Stage(r"copy", r"ARPlates v16.0.23.24", prog_num=63311):  # 0m:1.339s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63312) as should_copy_source_452_63312:  # 0m:1.338s
                    should_copy_source_452_63312()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=63313):  # 0m:1.338s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=63314) as copy_dir_to_dir_453_63314:  # 0m:0.002s
                            copy_dir_to_dir_453_63314()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=63315) as unwtar_454_63315:  # 0m:1.336s
                            unwtar_454_63315()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=63316, recursive=True) as chown_455_63316:  # 0m:0.000s
                            chown_455_63316()
            with Stage(r"copy", r"Abbey Road Vinyl v16.0.23.24", prog_num=63317):  # 0m:2.811s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63318) as should_copy_source_456_63318:  # 0m:2.810s
                    should_copy_source_456_63318()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=63319):  # 0m:2.810s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=63320) as copy_dir_to_dir_457_63320:  # 0m:0.002s
                            copy_dir_to_dir_457_63320()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=63321) as unwtar_458_63321:  # 0m:2.807s
                            unwtar_458_63321()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=63322, recursive=True) as chown_459_63322:  # 0m:0.000s
                            chown_459_63322()
            with Stage(r"copy", r"Abbey Road RS124 v16.0.23.24", prog_num=63323):  # 0m:0.572s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63324) as should_copy_source_460_63324:  # 0m:0.572s
                    should_copy_source_460_63324()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road RS124.bundle", prog_num=63325):  # 0m:0.572s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", r".", delete_extraneous_files=True, prog_num=63326) as copy_dir_to_dir_461_63326:  # 0m:0.003s
                            copy_dir_to_dir_461_63326()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", where_to_unwtar=r".", prog_num=63327) as unwtar_462_63327:  # 0m:0.568s
                            unwtar_462_63327()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road RS124.bundle", user_id=-1, group_id=-1, prog_num=63328, recursive=True) as chown_463_63328:  # 0m:0.000s
                            chown_463_63328()
            with Stage(r"copy", r"Abbey Road Studio 3 v16.0.23.24", prog_num=63329):  # 0m:24.212s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63330) as should_copy_source_464_63330:  # 0m:24.212s
                    should_copy_source_464_63330()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Studio 3.bundle", prog_num=63331):  # 0m:24.212s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", r".", delete_extraneous_files=True, prog_num=63332) as copy_dir_to_dir_465_63332:  # 0m:0.024s
                            copy_dir_to_dir_465_63332()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", where_to_unwtar=r".", prog_num=63333) as unwtar_466_63333:  # 0m:24.188s
                            unwtar_466_63333()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Studio 3.bundle", user_id=-1, group_id=-1, prog_num=63334, recursive=True) as chown_467_63334:  # 0m:0.000s
                            chown_467_63334()
            with Stage(r"copy", r"Abbey Road Saturator v16.0.23.24", prog_num=63335):  # 0m:0.315s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63336) as should_copy_source_468_63336:  # 0m:0.315s
                    should_copy_source_468_63336()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Saturator.bundle", prog_num=63337):  # 0m:0.315s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", r".", delete_extraneous_files=True, prog_num=63338) as copy_dir_to_dir_469_63338:  # 0m:0.003s
                            copy_dir_to_dir_469_63338()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", where_to_unwtar=r".", prog_num=63339) as unwtar_470_63339:  # 0m:0.312s
                            unwtar_470_63339()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Saturator.bundle", user_id=-1, group_id=-1, prog_num=63340, recursive=True) as chown_471_63340:  # 0m:0.000s
                            chown_471_63340()
            with Stage(r"copy", r"Aphex AX v16.0.23.24", prog_num=63341):  # 0m:0.142s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63342) as should_copy_source_472_63342:  # 0m:0.142s
                    should_copy_source_472_63342()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=63343):  # 0m:0.141s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=63344) as copy_dir_to_dir_473_63344:  # 0m:0.004s
                            copy_dir_to_dir_473_63344()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=63345) as unwtar_474_63345:  # 0m:0.137s
                            unwtar_474_63345()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=63346, recursive=True) as chown_475_63346:  # 0m:0.000s
                            chown_475_63346()
            with Stage(r"copy", r"AudioTrack v16.0.23.24", prog_num=63347):  # 0m:0.264s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63348) as should_copy_source_476_63348:  # 0m:0.264s
                    should_copy_source_476_63348()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=63349):  # 0m:0.264s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=63350) as copy_dir_to_dir_477_63350:  # 0m:0.003s
                            copy_dir_to_dir_477_63350()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=63351) as unwtar_478_63351:  # 0m:0.260s
                            unwtar_478_63351()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=63352, recursive=True) as chown_479_63352:  # 0m:0.000s
                            chown_479_63352()
            with Stage(r"copy", r"B360 v16.0.23.24", prog_num=63353):  # 0m:0.445s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63354) as should_copy_source_480_63354:  # 0m:0.445s
                    should_copy_source_480_63354()
                    with Stage(r"copy source", r"Mac/Plugins/B360.bundle", prog_num=63355):  # 0m:0.445s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", r".", delete_extraneous_files=True, prog_num=63356) as copy_dir_to_dir_481_63356:  # 0m:0.003s
                            copy_dir_to_dir_481_63356()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", where_to_unwtar=r".", prog_num=63357) as unwtar_482_63357:  # 0m:0.441s
                            unwtar_482_63357()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/B360.bundle", user_id=-1, group_id=-1, prog_num=63358, recursive=True) as chown_483_63358:  # 0m:0.000s
                            chown_483_63358()
            with Stage(r"copy", r"BB Tubes v16.0.23.24", prog_num=63359):  # 0m:1.251s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63360) as should_copy_source_484_63360:  # 0m:1.251s
                    should_copy_source_484_63360()
                    with Stage(r"copy source", r"Mac/Plugins/BB Tubes.bundle", prog_num=63361):  # 0m:1.251s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", r".", delete_extraneous_files=True, prog_num=63362) as copy_dir_to_dir_485_63362:  # 0m:0.003s
                            copy_dir_to_dir_485_63362()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", where_to_unwtar=r".", prog_num=63363) as unwtar_486_63363:  # 0m:1.247s
                            unwtar_486_63363()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/BB Tubes.bundle", user_id=-1, group_id=-1, prog_num=63364, recursive=True) as chown_487_63364:  # 0m:0.000s
                            chown_487_63364()
            with Stage(r"copy", r"Bass Fingers v16.0.23.24", prog_num=63365):  # 0m:5.669s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63366) as should_copy_source_488_63366:  # 0m:5.669s
                    should_copy_source_488_63366()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Fingers.bundle", prog_num=63367):  # 0m:5.668s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", r".", delete_extraneous_files=True, prog_num=63368) as copy_dir_to_dir_489_63368:  # 0m:0.014s
                            copy_dir_to_dir_489_63368()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", where_to_unwtar=r".", prog_num=63369) as unwtar_490_63369:  # 0m:5.654s
                            unwtar_490_63369()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Fingers.bundle", user_id=-1, group_id=-1, prog_num=63370, recursive=True) as chown_491_63370:  # 0m:0.000s
                            chown_491_63370()
            with Stage(r"copy", r"Bass Rider v16.0.23.24", prog_num=63371):  # 0m:0.114s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63372) as should_copy_source_492_63372:  # 0m:0.113s
                    should_copy_source_492_63372()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=63373):  # 0m:0.113s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=63374) as copy_dir_to_dir_493_63374:  # 0m:0.002s
                            copy_dir_to_dir_493_63374()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=63375) as unwtar_494_63375:  # 0m:0.110s
                            unwtar_494_63375()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=63376, recursive=True) as chown_495_63376:  # 0m:0.000s
                            chown_495_63376()
            with Stage(r"copy", r"Bass Slapper v16.0.23.24", prog_num=63377):  # 0m:5.338s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63378) as should_copy_source_496_63378:  # 0m:5.338s
                    should_copy_source_496_63378()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=63379):  # 0m:5.338s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=63380) as copy_dir_to_dir_497_63380:  # 0m:0.013s
                            copy_dir_to_dir_497_63380()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=63381) as unwtar_498_63381:  # 0m:5.324s
                            unwtar_498_63381()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=63382, recursive=True) as chown_499_63382:  # 0m:0.000s
                            chown_499_63382()
            with Stage(r"copy", r"Berzerk Distortion v16.0.23.24", prog_num=63383):  # 0m:0.301s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63384) as should_copy_source_500_63384:  # 0m:0.301s
                    should_copy_source_500_63384()
                    with Stage(r"copy source", r"Mac/Plugins/Berzerk Distortion.bundle", prog_num=63385):  # 0m:0.301s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", r".", delete_extraneous_files=True, prog_num=63386) as copy_dir_to_dir_501_63386:  # 0m:0.002s
                            copy_dir_to_dir_501_63386()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", where_to_unwtar=r".", prog_num=63387) as unwtar_502_63387:  # 0m:0.298s
                            unwtar_502_63387()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Berzerk Distortion.bundle", user_id=-1, group_id=-1, prog_num=63388, recursive=True) as chown_503_63388:  # 0m:0.000s
                            chown_503_63388()
            with Stage(r"copy", r"Brauer Motion v16.0.23.24", prog_num=63389):  # 0m:0.324s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63390) as should_copy_source_504_63390:  # 0m:0.324s
                    should_copy_source_504_63390()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=63391):  # 0m:0.324s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=63392) as copy_dir_to_dir_505_63392:  # 0m:0.002s
                            copy_dir_to_dir_505_63392()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=63393) as unwtar_506_63393:  # 0m:0.321s
                            unwtar_506_63393()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=63394, recursive=True) as chown_507_63394:  # 0m:0.000s
                            chown_507_63394()
            with Stage(r"copy", r"Butch Vig Vocals v16.0.23.24", prog_num=63395):  # 0m:2.599s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63396) as should_copy_source_508_63396:  # 0m:2.599s
                    should_copy_source_508_63396()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=63397):  # 0m:2.599s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63398) as copy_dir_to_dir_509_63398:  # 0m:0.033s
                            copy_dir_to_dir_509_63398()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=63399) as unwtar_510_63399:  # 0m:2.565s
                            unwtar_510_63399()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=63400, recursive=True) as chown_511_63400:  # 0m:0.000s
                            chown_511_63400()
            with Stage(r"copy", r"C1 v16.0.23.24", prog_num=63401):  # 0m:0.489s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63402) as should_copy_source_512_63402:  # 0m:0.488s
                    should_copy_source_512_63402()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=63403):  # 0m:0.488s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=63404) as copy_dir_to_dir_513_63404:  # 0m:0.002s
                            copy_dir_to_dir_513_63404()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=63405) as unwtar_514_63405:  # 0m:0.485s
                            unwtar_514_63405()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C1.bundle", user_id=-1, group_id=-1, prog_num=63406, recursive=True) as chown_515_63406:  # 0m:0.000s
                            chown_515_63406()
            with Stage(r"copy", r"C360 v16.0.23.24", prog_num=63407):  # 0m:0.130s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63408) as should_copy_source_516_63408:  # 0m:0.130s
                    should_copy_source_516_63408()
                    with Stage(r"copy source", r"Mac/Plugins/C360.bundle", prog_num=63409):  # 0m:0.130s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", r".", delete_extraneous_files=True, prog_num=63410) as copy_dir_to_dir_517_63410:  # 0m:0.002s
                            copy_dir_to_dir_517_63410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", where_to_unwtar=r".", prog_num=63411) as unwtar_518_63411:  # 0m:0.127s
                            unwtar_518_63411()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C360.bundle", user_id=-1, group_id=-1, prog_num=63412, recursive=True) as chown_519_63412:  # 0m:0.000s
                            chown_519_63412()
            with Stage(r"copy", r"C4 v16.0.23.24", prog_num=63413):  # 0m:0.129s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63414) as should_copy_source_520_63414:  # 0m:0.129s
                    should_copy_source_520_63414()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=63415):  # 0m:0.129s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=63416) as copy_dir_to_dir_521_63416:  # 0m:0.002s
                            copy_dir_to_dir_521_63416()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=63417) as unwtar_522_63417:  # 0m:0.126s
                            unwtar_522_63417()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C4.bundle", user_id=-1, group_id=-1, prog_num=63418, recursive=True) as chown_523_63418:  # 0m:0.000s
                            chown_523_63418()
            with Stage(r"copy", r"C6 v16.0.23.24", prog_num=63419):  # 0m:0.150s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63420) as should_copy_source_524_63420:  # 0m:0.150s
                    should_copy_source_524_63420()
                    with Stage(r"copy source", r"Mac/Plugins/C6.bundle", prog_num=63421):  # 0m:0.149s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", r".", delete_extraneous_files=True, prog_num=63422) as copy_dir_to_dir_525_63422:  # 0m:0.002s
                            copy_dir_to_dir_525_63422()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", where_to_unwtar=r".", prog_num=63423) as unwtar_526_63423:  # 0m:0.147s
                            unwtar_526_63423()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C6.bundle", user_id=-1, group_id=-1, prog_num=63424, recursive=True) as chown_527_63424:  # 0m:0.000s
                            chown_527_63424()
            with Stage(r"copy", r"CLA-2A v16.0.23.24", prog_num=63425):  # 0m:0.299s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63426) as should_copy_source_528_63426:  # 0m:0.299s
                    should_copy_source_528_63426()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=63427):  # 0m:0.299s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=63428) as copy_dir_to_dir_529_63428:  # 0m:0.002s
                            copy_dir_to_dir_529_63428()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=63429) as unwtar_530_63429:  # 0m:0.296s
                            unwtar_530_63429()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=63430, recursive=True) as chown_531_63430:  # 0m:0.001s
                            chown_531_63430()
            with Stage(r"copy", r"CLA-3A v16.0.23.24", prog_num=63431):  # 0m:0.309s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63432) as should_copy_source_532_63432:  # 0m:0.309s
                    should_copy_source_532_63432()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=63433):  # 0m:0.309s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=63434) as copy_dir_to_dir_533_63434:  # 0m:0.002s
                            copy_dir_to_dir_533_63434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=63435) as unwtar_534_63435:  # 0m:0.306s
                            unwtar_534_63435()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=63436, recursive=True) as chown_535_63436:  # 0m:0.000s
                            chown_535_63436()
            with Stage(r"copy", r"CLA-76 v16.0.23.24", prog_num=63437):  # 0m:0.551s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63438) as should_copy_source_536_63438:  # 0m:0.551s
                    should_copy_source_536_63438()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=63439):  # 0m:0.551s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=63440) as copy_dir_to_dir_537_63440:  # 0m:0.002s
                            copy_dir_to_dir_537_63440()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=63441) as unwtar_538_63441:  # 0m:0.548s
                            unwtar_538_63441()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=63442, recursive=True) as chown_539_63442:  # 0m:0.000s
                            chown_539_63442()
            with Stage(r"copy", r"CLA Bass v16.0.23.24", prog_num=63443):  # 0m:0.951s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63444) as should_copy_source_540_63444:  # 0m:0.951s
                    should_copy_source_540_63444()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=63445):  # 0m:0.951s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=63446) as copy_dir_to_dir_541_63446:  # 0m:0.045s
                            copy_dir_to_dir_541_63446()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=63447) as unwtar_542_63447:  # 0m:0.905s
                            unwtar_542_63447()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=63448, recursive=True) as chown_543_63448:  # 0m:0.000s
                            chown_543_63448()
            with Stage(r"copy", r"CLA Drums v16.0.23.24", prog_num=63449):  # 0m:0.712s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63450) as should_copy_source_544_63450:  # 0m:0.712s
                    should_copy_source_544_63450()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Drums.bundle", prog_num=63451):  # 0m:0.711s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r".", delete_extraneous_files=True, prog_num=63452) as copy_dir_to_dir_545_63452:  # 0m:0.032s
                            copy_dir_to_dir_545_63452()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", where_to_unwtar=r".", prog_num=63453) as unwtar_546_63453:  # 0m:0.679s
                            unwtar_546_63453()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Drums.bundle", user_id=-1, group_id=-1, prog_num=63454, recursive=True) as chown_547_63454:  # 0m:0.000s
                            chown_547_63454()
            with Stage(r"copy", r"CLA EchoSphere v16.0.23.24", prog_num=63455):  # 0m:1.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63456) as should_copy_source_548_63456:  # 0m:1.000s
                    should_copy_source_548_63456()
                    with Stage(r"copy source", r"Mac/Plugins/CLA EchoSphere.bundle", prog_num=63457):  # 0m:0.1000s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", r".", delete_extraneous_files=True, prog_num=63458) as copy_dir_to_dir_549_63458:  # 0m:0.025s
                            copy_dir_to_dir_549_63458()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", where_to_unwtar=r".", prog_num=63459) as unwtar_550_63459:  # 0m:0.974s
                            unwtar_550_63459()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA EchoSphere.bundle", user_id=-1, group_id=-1, prog_num=63460, recursive=True) as chown_551_63460:  # 0m:0.000s
                            chown_551_63460()
            with Stage(r"copy", r"CLA Effects v16.0.23.24", prog_num=63461):  # 0m:0.763s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63462) as should_copy_source_552_63462:  # 0m:0.763s
                    should_copy_source_552_63462()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Effects.bundle", prog_num=63463):  # 0m:0.762s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r".", delete_extraneous_files=True, prog_num=63464) as copy_dir_to_dir_553_63464:  # 0m:0.036s
                            copy_dir_to_dir_553_63464()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", where_to_unwtar=r".", prog_num=63465) as unwtar_554_63465:  # 0m:0.726s
                            unwtar_554_63465()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Effects.bundle", user_id=-1, group_id=-1, prog_num=63466, recursive=True) as chown_555_63466:  # 0m:0.000s
                            chown_555_63466()
            with Stage(r"copy", r"CLA Epic v16.0.23.24", prog_num=63467):  # 0m:1.121s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63468) as should_copy_source_556_63468:  # 0m:1.121s
                    should_copy_source_556_63468()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Epic.bundle", prog_num=63469):  # 0m:1.121s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", r".", delete_extraneous_files=True, prog_num=63470) as copy_dir_to_dir_557_63470:  # 0m:0.020s
                            copy_dir_to_dir_557_63470()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", where_to_unwtar=r".", prog_num=63471) as unwtar_558_63471:  # 0m:1.100s
                            unwtar_558_63471()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Epic.bundle", user_id=-1, group_id=-1, prog_num=63472, recursive=True) as chown_559_63472:  # 0m:0.000s
                            chown_559_63472()
            with Stage(r"copy", r"CLA Guitars v16.0.23.24", prog_num=63473):  # 0m:0.821s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63474) as should_copy_source_560_63474:  # 0m:0.821s
                    should_copy_source_560_63474()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=63475):  # 0m:0.820s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=63476) as copy_dir_to_dir_561_63476:  # 0m:0.036s
                            copy_dir_to_dir_561_63476()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=63477) as unwtar_562_63477:  # 0m:0.784s
                            unwtar_562_63477()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=63478, recursive=True) as chown_563_63478:  # 0m:0.000s
                            chown_563_63478()
            with Stage(r"copy", r"CLA MixDown v16.0.23.24", prog_num=63479):  # 0m:0.758s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63480) as should_copy_source_564_63480:  # 0m:0.758s
                    should_copy_source_564_63480()
                    with Stage(r"copy source", r"Mac/Plugins/CLA MixDown.bundle", prog_num=63481):  # 0m:0.757s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", r".", delete_extraneous_files=True, prog_num=63482) as copy_dir_to_dir_565_63482:  # 0m:0.025s
                            copy_dir_to_dir_565_63482()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", where_to_unwtar=r".", prog_num=63483) as unwtar_566_63483:  # 0m:0.732s
                            unwtar_566_63483()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA MixDown.bundle", user_id=-1, group_id=-1, prog_num=63484, recursive=True) as chown_567_63484:  # 0m:0.000s
                            chown_567_63484()
            with Stage(r"copy", r"CLA MixHub v16.0.30.31", prog_num=63485):  # 0m:6.600s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63486) as should_copy_source_568_63486:  # 0m:6.600s
                    should_copy_source_568_63486()
                    with Stage(r"copy source", r"Mac/Plugins/CLA MixHub.bundle", prog_num=63487):  # 0m:6.600s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", r".", delete_extraneous_files=True, prog_num=63488) as copy_dir_to_dir_569_63488:  # 0m:0.028s
                            copy_dir_to_dir_569_63488()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", where_to_unwtar=r".", prog_num=63489) as unwtar_570_63489:  # 0m:6.571s
                            unwtar_570_63489()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA MixHub.bundle", user_id=-1, group_id=-1, prog_num=63490, recursive=True) as chown_571_63490:  # 0m:0.000s
                            chown_571_63490()
            with Stage(r"copy", r"CLA Nx v16.0.23.24", prog_num=63491):  # 0m:8.451s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63492) as should_copy_source_572_63492:  # 0m:8.451s
                    should_copy_source_572_63492()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Nx.bundle", prog_num=63493):  # 0m:8.451s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", r".", delete_extraneous_files=True, prog_num=63494) as copy_dir_to_dir_573_63494:  # 0m:0.023s
                            copy_dir_to_dir_573_63494()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", where_to_unwtar=r".", prog_num=63495) as unwtar_574_63495:  # 0m:8.428s
                            unwtar_574_63495()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Nx.bundle", user_id=-1, group_id=-1, prog_num=63496, recursive=True) as chown_575_63496:  # 0m:0.000s
                            chown_575_63496()
            with Stage(r"copy", r"CLA Unplugged v16.0.23.24", prog_num=63497):  # 0m:0.686s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63498) as should_copy_source_576_63498:  # 0m:0.686s
                    should_copy_source_576_63498()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=63499):  # 0m:0.686s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=63500) as copy_dir_to_dir_577_63500:  # 0m:0.033s
                            copy_dir_to_dir_577_63500()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=63501) as unwtar_578_63501:  # 0m:0.653s
                            unwtar_578_63501()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=63502, recursive=True) as chown_579_63502:  # 0m:0.000s
                            chown_579_63502()
            with Stage(r"copy", r"CLA Vocals v16.0.23.24", prog_num=63503):  # 0m:0.769s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63504) as should_copy_source_580_63504:  # 0m:0.769s
                    should_copy_source_580_63504()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=63505):  # 0m:0.768s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63506) as copy_dir_to_dir_581_63506:  # 0m:0.034s
                            copy_dir_to_dir_581_63506()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=63507) as unwtar_582_63507:  # 0m:0.734s
                            unwtar_582_63507()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=63508, recursive=True) as chown_583_63508:  # 0m:0.000s
                            chown_583_63508()
            with Stage(r"copy", r"CODEX v16.0.23.24", prog_num=63509):  # 0m:1.121s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63510) as should_copy_source_584_63510:  # 0m:1.121s
                    should_copy_source_584_63510()
                    with Stage(r"copy source", r"Mac/Plugins/CODEX.bundle", prog_num=63511):  # 0m:1.121s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", r".", delete_extraneous_files=True, prog_num=63512) as copy_dir_to_dir_585_63512:  # 0m:0.002s
                            copy_dir_to_dir_585_63512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", where_to_unwtar=r".", prog_num=63513) as unwtar_586_63513:  # 0m:1.118s
                            unwtar_586_63513()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CODEX.bundle", user_id=-1, group_id=-1, prog_num=63514, recursive=True) as chown_587_63514:  # 0m:0.000s
                            chown_587_63514()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=63515):  # 0m:1.842s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63516) as should_copy_source_588_63516:  # 0m:1.841s
                    should_copy_source_588_63516()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=63517):  # 0m:1.841s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=63518) as copy_dir_to_dir_589_63518:  # 0m:0.010s
                            copy_dir_to_dir_589_63518()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=63519) as unwtar_590_63519:  # 0m:1.831s
                            unwtar_590_63519()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=63520, recursive=True) as chown_591_63520:  # 0m:0.000s
                            chown_591_63520()
            with Stage(r"copy", r"CR8_Sampler v16.0.30.31", prog_num=63521):  # 0m:2.124s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63522) as should_copy_source_592_63522:  # 0m:2.124s
                    should_copy_source_592_63522()
                    with Stage(r"copy source", r"Mac/Plugins/CR8 Sampler.bundle", prog_num=63523):  # 0m:2.124s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", r".", delete_extraneous_files=True, prog_num=63524) as copy_dir_to_dir_593_63524:  # 0m:0.010s
                            copy_dir_to_dir_593_63524()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", where_to_unwtar=r".", prog_num=63525) as unwtar_594_63525:  # 0m:2.113s
                            unwtar_594_63525()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CR8 Sampler.bundle", user_id=-1, group_id=-1, prog_num=63526, recursive=True) as chown_595_63526:  # 0m:0.000s
                            chown_595_63526()
            with Stage(r"copy", r"Curves AQ v16.0.23.24", prog_num=63527):  # 0m:2.272s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63528) as should_copy_source_596_63528:  # 0m:2.271s
                    should_copy_source_596_63528()
                    with Stage(r"copy source", r"Mac/Plugins/Curves AQ.bundle", prog_num=63529):  # 0m:2.271s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r".", delete_extraneous_files=True, prog_num=63530) as copy_dir_to_dir_597_63530:  # 0m:0.002s
                            copy_dir_to_dir_597_63530()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", where_to_unwtar=r".", prog_num=63531) as unwtar_598_63531:  # 0m:2.268s
                            unwtar_598_63531()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Curves AQ.bundle", user_id=-1, group_id=-1, prog_num=63532, recursive=True) as chown_599_63532:  # 0m:0.000s
                            chown_599_63532()
            with Stage(r"copy", r"Curves Equator v16.0.23.24", prog_num=63533):  # 0m:2.184s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63534) as should_copy_source_600_63534:  # 0m:2.184s
                    should_copy_source_600_63534()
                    with Stage(r"copy source", r"Mac/Plugins/Curves Equator.bundle", prog_num=63535):  # 0m:2.184s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", r".", delete_extraneous_files=True, prog_num=63536) as copy_dir_to_dir_601_63536:  # 0m:0.003s
                            copy_dir_to_dir_601_63536()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", where_to_unwtar=r".", prog_num=63537) as unwtar_602_63537:  # 0m:2.181s
                            unwtar_602_63537()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Curves Equator.bundle", user_id=-1, group_id=-1, prog_num=63538, recursive=True) as chown_603_63538:  # 0m:0.000s
                            chown_603_63538()
            with Stage(r"copy", r"Center v16.0.23.24", prog_num=63539):  # 0m:0.108s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63540) as should_copy_source_604_63540:  # 0m:0.108s
                    should_copy_source_604_63540()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=63541):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=63542) as copy_dir_to_dir_605_63542:  # 0m:0.002s
                            copy_dir_to_dir_605_63542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=63543) as unwtar_606_63543:  # 0m:0.105s
                            unwtar_606_63543()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Center.bundle", user_id=-1, group_id=-1, prog_num=63544, recursive=True) as chown_607_63544:  # 0m:0.000s
                            chown_607_63544()
            with Stage(r"copy", r"Clarity Vx DeReverb v16.0.23.24", prog_num=63545):  # 0m:5.127s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63546) as should_copy_source_608_63546:  # 0m:5.127s
                    should_copy_source_608_63546()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb.bundle", prog_num=63547):  # 0m:5.127s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r".", delete_extraneous_files=True, prog_num=63548) as copy_dir_to_dir_609_63548:  # 0m:0.001s
                            copy_dir_to_dir_609_63548()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", where_to_unwtar=r".", prog_num=63549) as unwtar_610_63549:  # 0m:5.125s
                            unwtar_610_63549()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb.bundle", user_id=-1, group_id=-1, prog_num=63550, recursive=True) as chown_611_63550:  # 0m:0.000s
                            chown_611_63550()
            with Stage(r"copy", r"Clarity Vx DeReverb Pro v16.0.23.24", prog_num=63551):  # 0m:5.637s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63552) as should_copy_source_612_63552:  # 0m:5.637s
                    should_copy_source_612_63552()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb Pro.bundle", prog_num=63553):  # 0m:5.637s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r".", delete_extraneous_files=True, prog_num=63554) as copy_dir_to_dir_613_63554:  # 0m:0.002s
                            copy_dir_to_dir_613_63554()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", where_to_unwtar=r".", prog_num=63555) as unwtar_614_63555:  # 0m:5.634s
                            unwtar_614_63555()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb Pro.bundle", user_id=-1, group_id=-1, prog_num=63556, recursive=True) as chown_615_63556:  # 0m:0.000s
                            chown_615_63556()
            with Stage(r"copy", r"Clarity Vx v16.0.23.24", prog_num=63557):  # 0m:1.828s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63558) as should_copy_source_616_63558:  # 0m:1.828s
                    should_copy_source_616_63558()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=63559):  # 0m:1.827s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=63560) as copy_dir_to_dir_617_63560:  # 0m:0.002s
                            copy_dir_to_dir_617_63560()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=63561) as unwtar_618_63561:  # 0m:1.825s
                            unwtar_618_63561()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=63562, recursive=True) as chown_619_63562:  # 0m:0.000s
                            chown_619_63562()
            with Stage(r"copy", r"Clarity Vx Pro v16.0.23.24", prog_num=63563):  # 0m:1.743s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63564) as should_copy_source_620_63564:  # 0m:1.743s
                    should_copy_source_620_63564()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx Pro.bundle", prog_num=63565):  # 0m:1.742s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r".", delete_extraneous_files=True, prog_num=63566) as copy_dir_to_dir_621_63566:  # 0m:0.002s
                            copy_dir_to_dir_621_63566()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", where_to_unwtar=r".", prog_num=63567) as unwtar_622_63567:  # 0m:1.740s
                            unwtar_622_63567()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx Pro.bundle", user_id=-1, group_id=-1, prog_num=63568, recursive=True) as chown_623_63568:  # 0m:0.000s
                            chown_623_63568()
            with Stage(r"copy", r"Clavinet v16.0.23.24", prog_num=63569):  # 0m:3.786s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63570) as should_copy_source_624_63570:  # 0m:3.786s
                    should_copy_source_624_63570()
                    with Stage(r"copy source", r"Mac/Plugins/Clavinet.bundle", prog_num=63571):  # 0m:3.785s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", r".", delete_extraneous_files=True, prog_num=63572) as copy_dir_to_dir_625_63572:  # 0m:0.020s
                            copy_dir_to_dir_625_63572()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", where_to_unwtar=r".", prog_num=63573) as unwtar_626_63573:  # 0m:3.765s
                            unwtar_626_63573()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clavinet.bundle", user_id=-1, group_id=-1, prog_num=63574, recursive=True) as chown_627_63574:  # 0m:0.000s
                            chown_627_63574()
            with Stage(r"copy", r"Saphira v16.0.23.24", prog_num=63575):  # 0m:0.581s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63576) as should_copy_source_628_63576:  # 0m:0.581s
                    should_copy_source_628_63576()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=63577):  # 0m:0.581s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=63578) as copy_dir_to_dir_629_63578:  # 0m:0.015s
                            copy_dir_to_dir_629_63578()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=63579) as unwtar_630_63579:  # 0m:0.565s
                            unwtar_630_63579()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Saphira.bundle", user_id=-1, group_id=-1, prog_num=63580, recursive=True) as chown_631_63580:  # 0m:0.000s
                            chown_631_63580()
            with Stage(r"copy", r"Submarine v16.0.23.24", prog_num=63581):  # 0m:0.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63582) as should_copy_source_632_63582:  # 0m:0.172s
                    should_copy_source_632_63582()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=63583):  # 0m:0.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=63584) as copy_dir_to_dir_633_63584:  # 0m:0.003s
                            copy_dir_to_dir_633_63584()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=63585) as unwtar_634_63585:  # 0m:0.169s
                            unwtar_634_63585()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Submarine.bundle", user_id=-1, group_id=-1, prog_num=63586, recursive=True) as chown_635_63586:  # 0m:0.000s
                            chown_635_63586()
            with Stage(r"copy", r"DPR-402 v16.0.23.24", prog_num=63587):  # 0m:0.350s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63588) as should_copy_source_636_63588:  # 0m:0.350s
                    should_copy_source_636_63588()
                    with Stage(r"copy source", r"Mac/Plugins/DPR-402.bundle", prog_num=63589):  # 0m:0.350s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", r".", delete_extraneous_files=True, prog_num=63590) as copy_dir_to_dir_637_63590:  # 0m:0.002s
                            copy_dir_to_dir_637_63590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", where_to_unwtar=r".", prog_num=63591) as unwtar_638_63591:  # 0m:0.347s
                            unwtar_638_63591()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DPR-402.bundle", user_id=-1, group_id=-1, prog_num=63592, recursive=True) as chown_639_63592:  # 0m:0.000s
                            chown_639_63592()
            with Stage(r"copy", r"DeBreath v16.0.23.24", prog_num=63593):  # 0m:0.144s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63594) as should_copy_source_640_63594:  # 0m:0.144s
                    should_copy_source_640_63594()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=63595):  # 0m:0.144s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=63596) as copy_dir_to_dir_641_63596:  # 0m:0.002s
                            copy_dir_to_dir_641_63596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=63597) as unwtar_642_63597:  # 0m:0.142s
                            unwtar_642_63597()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=63598, recursive=True) as chown_643_63598:  # 0m:0.000s
                            chown_643_63598()
            with Stage(r"copy", r"DeEsser v16.0.23.24", prog_num=63599):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63600) as should_copy_source_644_63600:  # 0m:0.111s
                    should_copy_source_644_63600()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=63601):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=63602) as copy_dir_to_dir_645_63602:  # 0m:0.002s
                            copy_dir_to_dir_645_63602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=63603) as unwtar_646_63603:  # 0m:0.109s
                            unwtar_646_63603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=63604, recursive=True) as chown_647_63604:  # 0m:0.000s
                            chown_647_63604()
            with Stage(r"copy", r"Doppler v16.0.23.24", prog_num=63605):  # 0m:0.113s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63606) as should_copy_source_648_63606:  # 0m:0.112s
                    should_copy_source_648_63606()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=63607):  # 0m:0.112s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=63608) as copy_dir_to_dir_649_63608:  # 0m:0.002s
                            copy_dir_to_dir_649_63608()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=63609) as unwtar_650_63609:  # 0m:0.110s
                            unwtar_650_63609()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doppler.bundle", user_id=-1, group_id=-1, prog_num=63610, recursive=True) as chown_651_63610:  # 0m:0.000s
                            chown_651_63610()
            with Stage(r"copy", r"Dorrough v16.0.23.24", prog_num=63611):  # 0m:1.247s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63612) as should_copy_source_652_63612:  # 0m:1.247s
                    should_copy_source_652_63612()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough.bundle", prog_num=63613):  # 0m:1.247s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", r".", delete_extraneous_files=True, prog_num=63614) as copy_dir_to_dir_653_63614:  # 0m:0.002s
                            copy_dir_to_dir_653_63614()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", where_to_unwtar=r".", prog_num=63615) as unwtar_654_63615:  # 0m:1.245s
                            unwtar_654_63615()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough.bundle", user_id=-1, group_id=-1, prog_num=63616, recursive=True) as chown_655_63616:  # 0m:0.000s
                            chown_655_63616()
            with Stage(r"copy", r"Dorrough Surround 5.0 v16.0.23.24", prog_num=63617):  # 0m:0.169s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63618) as should_copy_source_656_63618:  # 0m:0.169s
                    should_copy_source_656_63618()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough Surround 5.0.bundle", prog_num=63619):  # 0m:0.168s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", r".", delete_extraneous_files=True, prog_num=63620) as copy_dir_to_dir_657_63620:  # 0m:0.002s
                            copy_dir_to_dir_657_63620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", where_to_unwtar=r".", prog_num=63621) as unwtar_658_63621:  # 0m:0.166s
                            unwtar_658_63621()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough Surround 5.0.bundle", user_id=-1, group_id=-1, prog_num=63622, recursive=True) as chown_659_63622:  # 0m:0.000s
                            chown_659_63622()
            with Stage(r"copy", r"Dorrough Surround 5.1 v16.0.23.24", prog_num=63623):  # 0m:0.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63624) as should_copy_source_660_63624:  # 0m:0.171s
                    should_copy_source_660_63624()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough Surround 5.1.bundle", prog_num=63625):  # 0m:0.171s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", r".", delete_extraneous_files=True, prog_num=63626) as copy_dir_to_dir_661_63626:  # 0m:0.002s
                            copy_dir_to_dir_661_63626()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", where_to_unwtar=r".", prog_num=63627) as unwtar_662_63627:  # 0m:0.169s
                            unwtar_662_63627()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough Surround 5.1.bundle", user_id=-1, group_id=-1, prog_num=63628, recursive=True) as chown_663_63628:  # 0m:0.000s
                            chown_663_63628()
            with Stage(r"copy", r"Doubler v16.0.23.24", prog_num=63629):  # 0m:0.370s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63630) as should_copy_source_664_63630:  # 0m:0.370s
                    should_copy_source_664_63630()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=63631):  # 0m:0.369s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=63632) as copy_dir_to_dir_665_63632:  # 0m:0.003s
                            copy_dir_to_dir_665_63632()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=63633) as unwtar_666_63633:  # 0m:0.366s
                            unwtar_666_63633()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doubler.bundle", user_id=-1, group_id=-1, prog_num=63634, recursive=True) as chown_667_63634:  # 0m:0.000s
                            chown_667_63634()
            with Stage(r"copy", r"EMO-D5 v16.0.23.24", prog_num=63635):  # 0m:0.395s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63636) as should_copy_source_668_63636:  # 0m:0.395s
                    should_copy_source_668_63636()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-D5.bundle", prog_num=63637):  # 0m:0.395s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", r".", delete_extraneous_files=True, prog_num=63638) as copy_dir_to_dir_669_63638:  # 0m:0.003s
                            copy_dir_to_dir_669_63638()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", where_to_unwtar=r".", prog_num=63639) as unwtar_670_63639:  # 0m:0.392s
                            unwtar_670_63639()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-D5.bundle", user_id=-1, group_id=-1, prog_num=63640, recursive=True) as chown_671_63640:  # 0m:0.000s
                            chown_671_63640()
            with Stage(r"copy", r"EMO-F2 v16.0.23.24", prog_num=63641):  # 0m:0.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63642) as should_copy_source_672_63642:  # 0m:0.172s
                    should_copy_source_672_63642()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=63643):  # 0m:0.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=63644) as copy_dir_to_dir_673_63644:  # 0m:0.002s
                            copy_dir_to_dir_673_63644()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=63645) as unwtar_674_63645:  # 0m:0.169s
                            unwtar_674_63645()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=63646, recursive=True) as chown_675_63646:  # 0m:0.000s
                            chown_675_63646()
            with Stage(r"copy", r"EMO-Q4 v16.0.23.24", prog_num=63647):  # 0m:0.251s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63648) as should_copy_source_676_63648:  # 0m:0.251s
                    should_copy_source_676_63648()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=63649):  # 0m:0.251s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=63650) as copy_dir_to_dir_677_63650:  # 0m:0.002s
                            copy_dir_to_dir_677_63650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=63651) as unwtar_678_63651:  # 0m:0.249s
                            unwtar_678_63651()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=63652, recursive=True) as chown_679_63652:  # 0m:0.000s
                            chown_679_63652()
            with Stage(r"copy", r"EddieKramer BA v16.0.23.24", prog_num=63653):  # 0m:0.865s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63654) as should_copy_source_680_63654:  # 0m:0.865s
                    should_copy_source_680_63654()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer BA.bundle", prog_num=63655):  # 0m:0.865s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", r".", delete_extraneous_files=True, prog_num=63656) as copy_dir_to_dir_681_63656:  # 0m:0.025s
                            copy_dir_to_dir_681_63656()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", where_to_unwtar=r".", prog_num=63657) as unwtar_682_63657:  # 0m:0.839s
                            unwtar_682_63657()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer BA.bundle", user_id=-1, group_id=-1, prog_num=63658, recursive=True) as chown_683_63658:  # 0m:0.000s
                            chown_683_63658()
            with Stage(r"copy", r"EddieKramer DR v16.0.23.24", prog_num=63659):  # 0m:0.813s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63660) as should_copy_source_684_63660:  # 0m:0.813s
                    should_copy_source_684_63660()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=63661):  # 0m:0.813s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=63662) as copy_dir_to_dir_685_63662:  # 0m:0.023s
                            copy_dir_to_dir_685_63662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=63663) as unwtar_686_63663:  # 0m:0.790s
                            unwtar_686_63663()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=63664, recursive=True) as chown_687_63664:  # 0m:0.000s
                            chown_687_63664()
            with Stage(r"copy", r"EddieKramer FX v16.0.23.24", prog_num=63665):  # 0m:0.349s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63666) as should_copy_source_688_63666:  # 0m:0.349s
                    should_copy_source_688_63666()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer FX.bundle", prog_num=63667):  # 0m:0.348s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", r".", delete_extraneous_files=True, prog_num=63668) as copy_dir_to_dir_689_63668:  # 0m:0.013s
                            copy_dir_to_dir_689_63668()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", where_to_unwtar=r".", prog_num=63669) as unwtar_690_63669:  # 0m:0.334s
                            unwtar_690_63669()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer FX.bundle", user_id=-1, group_id=-1, prog_num=63670, recursive=True) as chown_691_63670:  # 0m:0.000s
                            chown_691_63670()
            with Stage(r"copy", r"EddieKramer GT v16.0.23.24", prog_num=63671):  # 0m:0.950s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63672) as should_copy_source_692_63672:  # 0m:0.950s
                    should_copy_source_692_63672()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer GT.bundle", prog_num=63673):  # 0m:0.949s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", r".", delete_extraneous_files=True, prog_num=63674) as copy_dir_to_dir_693_63674:  # 0m:0.038s
                            copy_dir_to_dir_693_63674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", where_to_unwtar=r".", prog_num=63675) as unwtar_694_63675:  # 0m:0.911s
                            unwtar_694_63675()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer GT.bundle", user_id=-1, group_id=-1, prog_num=63676, recursive=True) as chown_695_63676:  # 0m:0.000s
                            chown_695_63676()
            with Stage(r"copy", r"EddieKramer VC v16.0.23.24", prog_num=63677):  # 0m:0.871s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63678) as should_copy_source_696_63678:  # 0m:0.871s
                    should_copy_source_696_63678()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=63679):  # 0m:0.870s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=63680) as copy_dir_to_dir_697_63680:  # 0m:0.024s
                            copy_dir_to_dir_697_63680()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=63681) as unwtar_698_63681:  # 0m:0.846s
                            unwtar_698_63681()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=63682, recursive=True) as chown_699_63682:  # 0m:0.000s
                            chown_699_63682()
            with Stage(r"copy", r"Electric 200 v16.0.23.24", prog_num=63683):  # 0m:3.615s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63684) as should_copy_source_700_63684:  # 0m:3.615s
                    should_copy_source_700_63684()
                    with Stage(r"copy source", r"Mac/Plugins/Electric200.bundle", prog_num=63685):  # 0m:3.615s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", r".", delete_extraneous_files=True, prog_num=63686) as copy_dir_to_dir_701_63686:  # 0m:0.013s
                            copy_dir_to_dir_701_63686()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", where_to_unwtar=r".", prog_num=63687) as unwtar_702_63687:  # 0m:3.601s
                            unwtar_702_63687()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric200.bundle", user_id=-1, group_id=-1, prog_num=63688, recursive=True) as chown_703_63688:  # 0m:0.000s
                            chown_703_63688()
            with Stage(r"copy", r"Electric 88 v16.0.23.24", prog_num=63689):  # 0m:3.473s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63690) as should_copy_source_704_63690:  # 0m:3.473s
                    should_copy_source_704_63690()
                    with Stage(r"copy source", r"Mac/Plugins/Electric88.bundle", prog_num=63691):  # 0m:3.472s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", r".", delete_extraneous_files=True, prog_num=63692) as copy_dir_to_dir_705_63692:  # 0m:0.014s
                            copy_dir_to_dir_705_63692()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", where_to_unwtar=r".", prog_num=63693) as unwtar_706_63693:  # 0m:3.458s
                            unwtar_706_63693()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric88.bundle", user_id=-1, group_id=-1, prog_num=63694, recursive=True) as chown_707_63694:  # 0m:0.000s
                            chown_707_63694()
            with Stage(r"copy", r"Electric Grand 80 v16.0.23.24", prog_num=63695):  # 0m:3.546s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63696) as should_copy_source_708_63696:  # 0m:3.546s
                    should_copy_source_708_63696()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=63697):  # 0m:3.546s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=63698) as copy_dir_to_dir_709_63698:  # 0m:0.014s
                            copy_dir_to_dir_709_63698()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=63699) as unwtar_710_63699:  # 0m:3.532s
                            unwtar_710_63699()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=63700, recursive=True) as chown_711_63700:  # 0m:0.000s
                            chown_711_63700()
            with Stage(r"copy", r"Element2 v16.0.23.24", prog_num=63701):  # 0m:0.546s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63702) as should_copy_source_712_63702:  # 0m:0.545s
                    should_copy_source_712_63702()
                    with Stage(r"copy source", r"Mac/Plugins/Element2.bundle", prog_num=63703):  # 0m:0.545s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", r".", delete_extraneous_files=True, prog_num=63704) as copy_dir_to_dir_713_63704:  # 0m:0.002s
                            copy_dir_to_dir_713_63704()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", where_to_unwtar=r".", prog_num=63705) as unwtar_714_63705:  # 0m:0.543s
                            unwtar_714_63705()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Element2.bundle", user_id=-1, group_id=-1, prog_num=63706, recursive=True) as chown_715_63706:  # 0m:0.000s
                            chown_715_63706()
            with Stage(r"copy", r"Enigma v16.0.23.24", prog_num=63707):  # 0m:0.309s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63708) as should_copy_source_716_63708:  # 0m:0.309s
                    should_copy_source_716_63708()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=63709):  # 0m:0.309s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=63710) as copy_dir_to_dir_717_63710:  # 0m:0.002s
                            copy_dir_to_dir_717_63710()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=63711) as unwtar_718_63711:  # 0m:0.306s
                            unwtar_718_63711()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Enigma.bundle", user_id=-1, group_id=-1, prog_num=63712, recursive=True) as chown_719_63712:  # 0m:0.000s
                            chown_719_63712()
            with Stage(r"copy", r"F6 v16.0.23.24", prog_num=63713):  # 0m:0.242s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63714) as should_copy_source_720_63714:  # 0m:0.242s
                    should_copy_source_720_63714()
                    with Stage(r"copy source", r"Mac/Plugins/F6.bundle", prog_num=63715):  # 0m:0.242s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", r".", delete_extraneous_files=True, prog_num=63716) as copy_dir_to_dir_721_63716:  # 0m:0.003s
                            copy_dir_to_dir_721_63716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", where_to_unwtar=r".", prog_num=63717) as unwtar_722_63717:  # 0m:0.239s
                            unwtar_722_63717()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/F6.bundle", user_id=-1, group_id=-1, prog_num=63718, recursive=True) as chown_723_63718:  # 0m:0.000s
                            chown_723_63718()
            with Stage(r"copy", r"Feedback Hunter v16.0.23.24", prog_num=63719):  # 0m:0.216s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63720) as should_copy_source_724_63720:  # 0m:0.216s
                    should_copy_source_724_63720()
                    with Stage(r"copy source", r"Mac/Plugins/Feedback Hunter.bundle", prog_num=63721):  # 0m:0.216s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", r".", delete_extraneous_files=True, prog_num=63722) as copy_dir_to_dir_725_63722:  # 0m:0.003s
                            copy_dir_to_dir_725_63722()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", where_to_unwtar=r".", prog_num=63723) as unwtar_726_63723:  # 0m:0.212s
                            unwtar_726_63723()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Feedback Hunter.bundle", user_id=-1, group_id=-1, prog_num=63724, recursive=True) as chown_727_63724:  # 0m:0.000s
                            chown_727_63724()
            with Stage(r"copy", r"Flow Motion v16.0.23.24", prog_num=63725):  # 0m:1.072s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63726) as should_copy_source_728_63726:  # 0m:1.072s
                    should_copy_source_728_63726()
                    with Stage(r"copy source", r"Mac/Plugins/Flow Motion.bundle", prog_num=63727):  # 0m:1.071s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", r".", delete_extraneous_files=True, prog_num=63728) as copy_dir_to_dir_729_63728:  # 0m:0.002s
                            copy_dir_to_dir_729_63728()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", where_to_unwtar=r".", prog_num=63729) as unwtar_730_63729:  # 0m:1.069s
                            unwtar_730_63729()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Flow Motion.bundle", user_id=-1, group_id=-1, prog_num=63730, recursive=True) as chown_731_63730:  # 0m:0.000s
                            chown_731_63730()
            with Stage(r"copy", r"GEQ v16.0.23.24", prog_num=63731):  # 0m:0.359s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63732) as should_copy_source_732_63732:  # 0m:0.358s
                    should_copy_source_732_63732()
                    with Stage(r"copy source", r"Mac/Plugins/GEQ.bundle", prog_num=63733):  # 0m:0.358s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", r".", delete_extraneous_files=True, prog_num=63734) as copy_dir_to_dir_733_63734:  # 0m:0.002s
                            copy_dir_to_dir_733_63734()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", where_to_unwtar=r".", prog_num=63735) as unwtar_734_63735:  # 0m:0.355s
                            unwtar_734_63735()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GEQ.bundle", user_id=-1, group_id=-1, prog_num=63736, recursive=True) as chown_735_63736:  # 0m:0.000s
                            chown_735_63736()
            with Stage(r"copy", r"GTRAmp v16.0.23.24", prog_num=63737):  # 0m:1.173s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63738) as should_copy_source_736_63738:  # 0m:1.173s
                    should_copy_source_736_63738()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=63739):  # 0m:1.173s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=63740) as copy_dir_to_dir_737_63740:  # 0m:0.002s
                            copy_dir_to_dir_737_63740()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=63741) as unwtar_738_63741:  # 0m:1.170s
                            unwtar_738_63741()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=63742, recursive=True) as chown_739_63742:  # 0m:0.000s
                            chown_739_63742()
            with Stage(r"copy", r"GTR Solo ToolRack v16.0.23.24", prog_num=63743):  # 0m:0.496s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63744) as should_copy_source_740_63744:  # 0m:0.496s
                    should_copy_source_740_63744()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSoloToolRack.bundle", prog_num=63745):  # 0m:0.496s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", r".", delete_extraneous_files=True, prog_num=63746) as copy_dir_to_dir_741_63746:  # 0m:0.013s
                            copy_dir_to_dir_741_63746()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", where_to_unwtar=r".", prog_num=63747) as unwtar_742_63747:  # 0m:0.482s
                            unwtar_742_63747()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSoloToolRack.bundle", user_id=-1, group_id=-1, prog_num=63748, recursive=True) as chown_743_63748:  # 0m:0.000s
                            chown_743_63748()
            with Stage(r"copy", r"GTRStomp v16.0.23.24", prog_num=63749):  # 0m:0.221s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63750) as should_copy_source_744_63750:  # 0m:0.221s
                    should_copy_source_744_63750()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=63751):  # 0m:0.221s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=63752) as copy_dir_to_dir_745_63752:  # 0m:0.003s
                            copy_dir_to_dir_745_63752()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=63753) as unwtar_746_63753:  # 0m:0.218s
                            unwtar_746_63753()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=63754, recursive=True) as chown_747_63754:  # 0m:0.001s
                            chown_747_63754()
            with Stage(r"copy", r"GTRToolRack v16.0.23.24", prog_num=63755):  # 0m:1.253s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63756) as should_copy_source_748_63756:  # 0m:1.253s
                    should_copy_source_748_63756()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=63757):  # 0m:1.253s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=63758) as copy_dir_to_dir_749_63758:  # 0m:0.016s
                            copy_dir_to_dir_749_63758()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=63759) as unwtar_750_63759:  # 0m:1.236s
                            unwtar_750_63759()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=63760, recursive=True) as chown_751_63760:  # 0m:0.000s
                            chown_751_63760()
            with Stage(r"copy", r"GTRTuner v16.0.23.24", prog_num=63761):  # 0m:0.079s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63762) as should_copy_source_752_63762:  # 0m:0.079s
                    should_copy_source_752_63762()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=63763):  # 0m:0.079s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=63764) as copy_dir_to_dir_753_63764:  # 0m:0.002s
                            copy_dir_to_dir_753_63764()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=63765) as unwtar_754_63765:  # 0m:0.077s
                            unwtar_754_63765()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=63766, recursive=True) as chown_755_63766:  # 0m:0.000s
                            chown_755_63766()
            with Stage(r"copy", r"Waves Gemstones v16.0.23.24", prog_num=63767):  # 0m:2.597s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63768) as should_copy_source_756_63768:  # 0m:2.597s
                    should_copy_source_756_63768()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Gemstones.bundle", prog_num=63769):  # 0m:2.597s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", r".", delete_extraneous_files=True, prog_num=63770) as copy_dir_to_dir_757_63770:  # 0m:0.021s
                            copy_dir_to_dir_757_63770()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", where_to_unwtar=r".", prog_num=63771) as unwtar_758_63771:  # 0m:2.575s
                            unwtar_758_63771()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Gemstones.bundle", user_id=-1, group_id=-1, prog_num=63772, recursive=True) as chown_759_63772:  # 0m:0.000s
                            chown_759_63772()
            with Stage(r"copy", r"Grand Rhapsody v16.0.23.24", prog_num=63773):  # 0m:3.803s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63774) as should_copy_source_760_63774:  # 0m:3.803s
                    should_copy_source_760_63774()
                    with Stage(r"copy source", r"Mac/Plugins/GrandRhapsody.bundle", prog_num=63775):  # 0m:3.802s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", r".", delete_extraneous_files=True, prog_num=63776) as copy_dir_to_dir_761_63776:  # 0m:0.022s
                            copy_dir_to_dir_761_63776()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", where_to_unwtar=r".", prog_num=63777) as unwtar_762_63777:  # 0m:3.779s
                            unwtar_762_63777()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GrandRhapsody.bundle", user_id=-1, group_id=-1, prog_num=63778, recursive=True) as chown_763_63778:  # 0m:0.000s
                            chown_763_63778()
            with Stage(r"copy", r"Greg Wells MixCentric v16.0.23.24", prog_num=63779):  # 0m:1.487s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63780) as should_copy_source_764_63780:  # 0m:1.487s
                    should_copy_source_764_63780()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=63781):  # 0m:1.487s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=63782) as copy_dir_to_dir_765_63782:  # 0m:0.021s
                            copy_dir_to_dir_765_63782()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=63783) as unwtar_766_63783:  # 0m:1.465s
                            unwtar_766_63783()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=63784, recursive=True) as chown_767_63784:  # 0m:0.000s
                            chown_767_63784()
            with Stage(r"copy", r"Greg Wells PianoCentric v16.0.23.24", prog_num=63785):  # 0m:1.506s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63786) as should_copy_source_768_63786:  # 0m:1.505s
                    should_copy_source_768_63786()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=63787):  # 0m:1.505s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=63788) as copy_dir_to_dir_769_63788:  # 0m:0.022s
                            copy_dir_to_dir_769_63788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=63789) as unwtar_770_63789:  # 0m:1.483s
                            unwtar_770_63789()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=63790, recursive=True) as chown_771_63790:  # 0m:0.000s
                            chown_771_63790()
            with Stage(r"copy", r"Greg Wells ToneCentric v16.0.23.24", prog_num=63791):  # 0m:1.518s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63792) as should_copy_source_772_63792:  # 0m:1.518s
                    should_copy_source_772_63792()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=63793):  # 0m:1.517s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=63794) as copy_dir_to_dir_773_63794:  # 0m:0.022s
                            copy_dir_to_dir_773_63794()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=63795) as unwtar_774_63795:  # 0m:1.495s
                            unwtar_774_63795()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=63796, recursive=True) as chown_775_63796:  # 0m:0.000s
                            chown_775_63796()
            with Stage(r"copy", r"Greg Wells VoiceCentric v16.0.23.24", prog_num=63797):  # 0m:1.628s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63798) as should_copy_source_776_63798:  # 0m:1.628s
                    should_copy_source_776_63798()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells VoiceCentric.bundle", prog_num=63799):  # 0m:1.628s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", r".", delete_extraneous_files=True, prog_num=63800) as copy_dir_to_dir_777_63800:  # 0m:0.034s
                            copy_dir_to_dir_777_63800()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", where_to_unwtar=r".", prog_num=63801) as unwtar_778_63801:  # 0m:1.593s
                            unwtar_778_63801()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells VoiceCentric.bundle", user_id=-1, group_id=-1, prog_num=63802, recursive=True) as chown_779_63802:  # 0m:0.000s
                            chown_779_63802()
            with Stage(r"copy", r"H-Comp v16.0.23.24", prog_num=63803):  # 0m:1.026s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63804) as should_copy_source_780_63804:  # 0m:1.026s
                    should_copy_source_780_63804()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=63805):  # 0m:1.026s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=63806) as copy_dir_to_dir_781_63806:  # 0m:0.002s
                            copy_dir_to_dir_781_63806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=63807) as unwtar_782_63807:  # 0m:1.023s
                            unwtar_782_63807()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=63808, recursive=True) as chown_783_63808:  # 0m:0.000s
                            chown_783_63808()
            with Stage(r"copy", r"H-Delay v16.0.23.24", prog_num=63809):  # 0m:0.139s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63810) as should_copy_source_784_63810:  # 0m:0.139s
                    should_copy_source_784_63810()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=63811):  # 0m:0.139s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=63812) as copy_dir_to_dir_785_63812:  # 0m:0.002s
                            copy_dir_to_dir_785_63812()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=63813) as unwtar_786_63813:  # 0m:0.136s
                            unwtar_786_63813()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=63814, recursive=True) as chown_787_63814:  # 0m:0.000s
                            chown_787_63814()
            with Stage(r"copy", r"H-EQ v16.0.23.24", prog_num=63815):  # 0m:0.240s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63816) as should_copy_source_788_63816:  # 0m:0.240s
                    should_copy_source_788_63816()
                    with Stage(r"copy source", r"Mac/Plugins/H-EQ.bundle", prog_num=63817):  # 0m:0.240s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", r".", delete_extraneous_files=True, prog_num=63818) as copy_dir_to_dir_789_63818:  # 0m:0.002s
                            copy_dir_to_dir_789_63818()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", where_to_unwtar=r".", prog_num=63819) as unwtar_790_63819:  # 0m:0.237s
                            unwtar_790_63819()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-EQ.bundle", user_id=-1, group_id=-1, prog_num=63820, recursive=True) as chown_791_63820:  # 0m:0.000s
                            chown_791_63820()
            with Stage(r"copy", r"H-Reverb v16.0.23.24", prog_num=63821):  # 0m:0.299s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63822) as should_copy_source_792_63822:  # 0m:0.299s
                    should_copy_source_792_63822()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=63823):  # 0m:0.298s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=63824) as copy_dir_to_dir_793_63824:  # 0m:0.002s
                            copy_dir_to_dir_793_63824()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=63825) as unwtar_794_63825:  # 0m:0.296s
                            unwtar_794_63825()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=63826, recursive=True) as chown_795_63826:  # 0m:0.000s
                            chown_795_63826()
            with Stage(r"copy", r"IDX Intelligent Dynamics v16.0.23.24", prog_num=63827):  # 0m:2.779s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63828) as should_copy_source_796_63828:  # 0m:2.779s
                    should_copy_source_796_63828()
                    with Stage(r"copy source", r"Mac/Plugins/IDX Intelligent Dynamics.bundle", prog_num=63829):  # 0m:2.779s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", r".", delete_extraneous_files=True, prog_num=63830) as copy_dir_to_dir_797_63830:  # 0m:0.003s
                            copy_dir_to_dir_797_63830()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", where_to_unwtar=r".", prog_num=63831) as unwtar_798_63831:  # 0m:2.776s
                            unwtar_798_63831()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IDX Intelligent Dynamics.bundle", user_id=-1, group_id=-1, prog_num=63832, recursive=True) as chown_799_63832:  # 0m:0.000s
                            chown_799_63832()
            with Stage(r"copy", r"IMPusher v16.0.23.24", prog_num=63833):  # 0m:0.750s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63834) as should_copy_source_800_63834:  # 0m:0.750s
                    should_copy_source_800_63834()
                    with Stage(r"copy source", r"Mac/Plugins/IMPusher.bundle", prog_num=63835):  # 0m:0.749s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", r".", delete_extraneous_files=True, prog_num=63836) as copy_dir_to_dir_801_63836:  # 0m:0.025s
                            copy_dir_to_dir_801_63836()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", where_to_unwtar=r".", prog_num=63837) as unwtar_802_63837:  # 0m:0.724s
                            unwtar_802_63837()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IMPusher.bundle", user_id=-1, group_id=-1, prog_num=63838, recursive=True) as chown_803_63838:  # 0m:0.000s
                            chown_803_63838()
            with Stage(r"copy", r"IR-1 v16.0.23.24", prog_num=63839):  # 0m:0.224s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63840) as should_copy_source_804_63840:  # 0m:0.224s
                    should_copy_source_804_63840()
                    with Stage(r"copy source", r"Mac/Plugins/IR-1.bundle", prog_num=63841):  # 0m:0.224s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", r".", delete_extraneous_files=True, prog_num=63842) as copy_dir_to_dir_805_63842:  # 0m:0.002s
                            copy_dir_to_dir_805_63842()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", where_to_unwtar=r".", prog_num=63843) as unwtar_806_63843:  # 0m:0.221s
                            unwtar_806_63843()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-1.bundle", user_id=-1, group_id=-1, prog_num=63844, recursive=True) as chown_807_63844:  # 0m:0.000s
                            chown_807_63844()
            with Stage(r"copy", r"IR-360 v16.0.23.24", prog_num=63845):  # 0m:0.220s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63846) as should_copy_source_808_63846:  # 0m:0.219s
                    should_copy_source_808_63846()
                    with Stage(r"copy source", r"Mac/Plugins/IR-360.bundle", prog_num=63847):  # 0m:0.219s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r".", delete_extraneous_files=True, prog_num=63848) as copy_dir_to_dir_809_63848:  # 0m:0.002s
                            copy_dir_to_dir_809_63848()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", where_to_unwtar=r".", prog_num=63849) as unwtar_810_63849:  # 0m:0.216s
                            unwtar_810_63849()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-360.bundle", user_id=-1, group_id=-1, prog_num=63850, recursive=True) as chown_811_63850:  # 0m:0.000s
                            chown_811_63850()
            with Stage(r"copy", r"IR-L v16.0.23.24", prog_num=63851):  # 0m:0.218s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63852) as should_copy_source_812_63852:  # 0m:0.218s
                    should_copy_source_812_63852()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=63853):  # 0m:0.217s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=63854) as copy_dir_to_dir_813_63854:  # 0m:0.002s
                            copy_dir_to_dir_813_63854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=63855) as unwtar_814_63855:  # 0m:0.215s
                            unwtar_814_63855()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-L.bundle", user_id=-1, group_id=-1, prog_num=63856, recursive=True) as chown_815_63856:  # 0m:0.000s
                            chown_815_63856()
            with Stage(r"copy", r"IRLive v16.0.23.24", prog_num=63857):  # 0m:0.286s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63858) as should_copy_source_816_63858:  # 0m:0.286s
                    should_copy_source_816_63858()
                    with Stage(r"copy source", r"Mac/Plugins/IRLive.bundle", prog_num=63859):  # 0m:0.286s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", r".", delete_extraneous_files=True, prog_num=63860) as copy_dir_to_dir_817_63860:  # 0m:0.003s
                            copy_dir_to_dir_817_63860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", where_to_unwtar=r".", prog_num=63861) as unwtar_818_63861:  # 0m:0.283s
                            unwtar_818_63861()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IRLive.bundle", user_id=-1, group_id=-1, prog_num=63862, recursive=True) as chown_819_63862:  # 0m:0.000s
                            chown_819_63862()
            with Stage(r"copy", r"Immersive Wrapper v16.0.23.24", prog_num=63863):  # 0m:0.412s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63864) as should_copy_source_820_63864:  # 0m:0.412s
                    should_copy_source_820_63864()
                    with Stage(r"copy source", r"Mac/Plugins/Immersive Wrapper.bundle", prog_num=63865):  # 0m:0.412s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r".", delete_extraneous_files=True, prog_num=63866) as copy_dir_to_dir_821_63866:  # 0m:0.003s
                            copy_dir_to_dir_821_63866()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", where_to_unwtar=r".", prog_num=63867) as unwtar_822_63867:  # 0m:0.409s
                            unwtar_822_63867()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Immersive Wrapper.bundle", user_id=-1, group_id=-1, prog_num=63868, recursive=True) as chown_823_63868:  # 0m:0.000s
                            chown_823_63868()
            with Stage(r"copy", r"InPhase v16.0.23.24", prog_num=63869):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63870) as should_copy_source_824_63870:  # 0m:0.116s
                    should_copy_source_824_63870()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=63871):  # 0m:0.116s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=63872) as copy_dir_to_dir_825_63872:  # 0m:0.002s
                            copy_dir_to_dir_825_63872()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=63873) as unwtar_826_63873:  # 0m:0.113s
                            unwtar_826_63873()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase.bundle", user_id=-1, group_id=-1, prog_num=63874, recursive=True) as chown_827_63874:  # 0m:0.000s
                            chown_827_63874()
            with Stage(r"copy", r"InPhase LT v16.0.23.24", prog_num=63875):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63876) as should_copy_source_828_63876:  # 0m:0.116s
                    should_copy_source_828_63876()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=63877):  # 0m:0.116s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=63878) as copy_dir_to_dir_829_63878:  # 0m:0.002s
                            copy_dir_to_dir_829_63878()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=63879) as unwtar_830_63879:  # 0m:0.113s
                            unwtar_830_63879()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=63880, recursive=True) as chown_831_63880:  # 0m:0.000s
                            chown_831_63880()
            with Stage(r"copy", r"J37 v16.0.23.24", prog_num=63881):  # 0m:1.584s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63882) as should_copy_source_832_63882:  # 0m:1.584s
                    should_copy_source_832_63882()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=63883):  # 0m:1.583s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=63884) as copy_dir_to_dir_833_63884:  # 0m:0.002s
                            copy_dir_to_dir_833_63884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=63885) as unwtar_834_63885:  # 0m:1.581s
                            unwtar_834_63885()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/J37.bundle", user_id=-1, group_id=-1, prog_num=63886, recursive=True) as chown_835_63886:  # 0m:0.000s
                            chown_835_63886()
            with Stage(r"copy", r"JJP-Bass v16.0.23.24", prog_num=63887):  # 0m:0.994s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63888) as should_copy_source_836_63888:  # 0m:0.994s
                    should_copy_source_836_63888()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Bass.bundle", prog_num=63889):  # 0m:0.994s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", r".", delete_extraneous_files=True, prog_num=63890) as copy_dir_to_dir_837_63890:  # 0m:0.042s
                            copy_dir_to_dir_837_63890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", where_to_unwtar=r".", prog_num=63891) as unwtar_838_63891:  # 0m:0.952s
                            unwtar_838_63891()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Bass.bundle", user_id=-1, group_id=-1, prog_num=63892, recursive=True) as chown_839_63892:  # 0m:0.000s
                            chown_839_63892()
            with Stage(r"copy", r"JJP-Cymb-Perc v16.0.23.24", prog_num=63893):  # 0m:0.891s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63894) as should_copy_source_840_63894:  # 0m:0.890s
                    should_copy_source_840_63894()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Cymb-Perc.bundle", prog_num=63895):  # 0m:0.890s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", r".", delete_extraneous_files=True, prog_num=63896) as copy_dir_to_dir_841_63896:  # 0m:0.033s
                            copy_dir_to_dir_841_63896()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", where_to_unwtar=r".", prog_num=63897) as unwtar_842_63897:  # 0m:0.857s
                            unwtar_842_63897()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Cymb-Perc.bundle", user_id=-1, group_id=-1, prog_num=63898, recursive=True) as chown_843_63898:  # 0m:0.000s
                            chown_843_63898()
            with Stage(r"copy", r"JJP-Drums v16.0.23.24", prog_num=63899):  # 0m:1.076s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63900) as should_copy_source_844_63900:  # 0m:1.076s
                    should_copy_source_844_63900()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Drums.bundle", prog_num=63901):  # 0m:1.075s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", r".", delete_extraneous_files=True, prog_num=63902) as copy_dir_to_dir_845_63902:  # 0m:0.042s
                            copy_dir_to_dir_845_63902()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", where_to_unwtar=r".", prog_num=63903) as unwtar_846_63903:  # 0m:1.033s
                            unwtar_846_63903()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Drums.bundle", user_id=-1, group_id=-1, prog_num=63904, recursive=True) as chown_847_63904:  # 0m:0.000s
                            chown_847_63904()
            with Stage(r"copy", r"JJP-Guitars v16.0.23.24", prog_num=63905):  # 0m:1.045s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63906) as should_copy_source_848_63906:  # 0m:1.045s
                    should_copy_source_848_63906()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Guitars.bundle", prog_num=63907):  # 0m:1.044s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", r".", delete_extraneous_files=True, prog_num=63908) as copy_dir_to_dir_849_63908:  # 0m:0.043s
                            copy_dir_to_dir_849_63908()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", where_to_unwtar=r".", prog_num=63909) as unwtar_850_63909:  # 0m:1.001s
                            unwtar_850_63909()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Guitars.bundle", user_id=-1, group_id=-1, prog_num=63910, recursive=True) as chown_851_63910:  # 0m:0.000s
                            chown_851_63910()
            with Stage(r"copy", r"JJP-Strings-Keys v16.0.23.24", prog_num=63911):  # 0m:0.961s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63912) as should_copy_source_852_63912:  # 0m:0.961s
                    should_copy_source_852_63912()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Strings-Keys.bundle", prog_num=63913):  # 0m:0.961s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", r".", delete_extraneous_files=True, prog_num=63914) as copy_dir_to_dir_853_63914:  # 0m:0.045s
                            copy_dir_to_dir_853_63914()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", where_to_unwtar=r".", prog_num=63915) as unwtar_854_63915:  # 0m:0.915s
                            unwtar_854_63915()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Strings-Keys.bundle", user_id=-1, group_id=-1, prog_num=63916, recursive=True) as chown_855_63916:  # 0m:0.000s
                            chown_855_63916()
            with Stage(r"copy", r"JJP-Vocals v16.0.23.24", prog_num=63917):  # 0m:1.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63918) as should_copy_source_856_63918:  # 0m:1.101s
                    should_copy_source_856_63918()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=63919):  # 0m:1.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63920) as copy_dir_to_dir_857_63920:  # 0m:0.043s
                            copy_dir_to_dir_857_63920()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=63921) as unwtar_858_63921:  # 0m:1.057s
                            unwtar_858_63921()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=63922, recursive=True) as chown_859_63922:  # 0m:0.000s
                            chown_859_63922()
            with Stage(r"copy", r"Kaleidoscopes v16.0.23.24", prog_num=63923):  # 0m:1.832s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63924) as should_copy_source_860_63924:  # 0m:1.832s
                    should_copy_source_860_63924()
                    with Stage(r"copy source", r"Mac/Plugins/Kaleidoscopes.bundle", prog_num=63925):  # 0m:1.831s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", r".", delete_extraneous_files=True, prog_num=63926) as copy_dir_to_dir_861_63926:  # 0m:0.002s
                            copy_dir_to_dir_861_63926()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", where_to_unwtar=r".", prog_num=63927) as unwtar_862_63927:  # 0m:1.829s
                            unwtar_862_63927()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Kaleidoscopes.bundle", user_id=-1, group_id=-1, prog_num=63928, recursive=True) as chown_863_63928:  # 0m:0.000s
                            chown_863_63928()
            with Stage(r"copy", r"Key Detector v16.0.23.24", prog_num=63929):  # 0m:0.238s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63930) as should_copy_source_864_63930:  # 0m:0.238s
                    should_copy_source_864_63930()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=63931):  # 0m:0.238s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=63932) as copy_dir_to_dir_865_63932:  # 0m:0.002s
                            copy_dir_to_dir_865_63932()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=63933) as unwtar_866_63933:  # 0m:0.235s
                            unwtar_866_63933()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=63934, recursive=True) as chown_867_63934:  # 0m:0.000s
                            chown_867_63934()
            with Stage(r"copy", r"KingsMic v16.0.23.24", prog_num=63935):  # 0m:0.224s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63936) as should_copy_source_868_63936:  # 0m:0.223s
                    should_copy_source_868_63936()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=63937):  # 0m:0.223s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=63938) as copy_dir_to_dir_869_63938:  # 0m:0.002s
                            copy_dir_to_dir_869_63938()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=63939) as unwtar_870_63939:  # 0m:0.221s
                            unwtar_870_63939()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=63940, recursive=True) as chown_871_63940:  # 0m:0.000s
                            chown_871_63940()
            with Stage(r"copy", r"KramerHLS v16.0.23.24", prog_num=63941):  # 0m:0.173s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63942) as should_copy_source_872_63942:  # 0m:0.173s
                    should_copy_source_872_63942()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=63943):  # 0m:0.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=63944) as copy_dir_to_dir_873_63944:  # 0m:0.002s
                            copy_dir_to_dir_873_63944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=63945) as unwtar_874_63945:  # 0m:0.170s
                            unwtar_874_63945()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=63946, recursive=True) as chown_875_63946:  # 0m:0.000s
                            chown_875_63946()
            with Stage(r"copy", r"KramerPIE v16.0.23.24", prog_num=63947):  # 0m:0.132s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63948) as should_copy_source_876_63948:  # 0m:0.132s
                    should_copy_source_876_63948()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=63949):  # 0m:0.132s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=63950) as copy_dir_to_dir_877_63950:  # 0m:0.002s
                            copy_dir_to_dir_877_63950()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=63951) as unwtar_878_63951:  # 0m:0.130s
                            unwtar_878_63951()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=63952, recursive=True) as chown_879_63952:  # 0m:0.000s
                            chown_879_63952()
            with Stage(r"copy", r"KramerTape v16.0.23.24", prog_num=63953):  # 0m:1.084s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63954) as should_copy_source_880_63954:  # 0m:1.084s
                    should_copy_source_880_63954()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=63955):  # 0m:1.083s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=63956) as copy_dir_to_dir_881_63956:  # 0m:0.002s
                            copy_dir_to_dir_881_63956()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=63957) as unwtar_882_63957:  # 0m:1.081s
                            unwtar_882_63957()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=63958, recursive=True) as chown_883_63958:  # 0m:0.000s
                            chown_883_63958()
            with Stage(r"copy", r"L1 v16.0.23.24", prog_num=63959):  # 0m:0.251s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63960) as should_copy_source_884_63960:  # 0m:0.251s
                    should_copy_source_884_63960()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=63961):  # 0m:0.251s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=63962) as copy_dir_to_dir_885_63962:  # 0m:0.002s
                            copy_dir_to_dir_885_63962()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=63963) as unwtar_886_63963:  # 0m:0.248s
                            unwtar_886_63963()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L1.bundle", user_id=-1, group_id=-1, prog_num=63964, recursive=True) as chown_887_63964:  # 0m:0.000s
                            chown_887_63964()
            with Stage(r"copy", r"L2 v16.0.23.24", prog_num=63965):  # 0m:0.098s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63966) as should_copy_source_888_63966:  # 0m:0.098s
                    should_copy_source_888_63966()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=63967):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=63968) as copy_dir_to_dir_889_63968:  # 0m:0.002s
                            copy_dir_to_dir_889_63968()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=63969) as unwtar_890_63969:  # 0m:0.095s
                            unwtar_890_63969()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L2.bundle", user_id=-1, group_id=-1, prog_num=63970, recursive=True) as chown_891_63970:  # 0m:0.000s
                            chown_891_63970()
            with Stage(r"copy", r"L360 v16.0.23.24", prog_num=63971):  # 0m:0.129s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63972) as should_copy_source_892_63972:  # 0m:0.129s
                    should_copy_source_892_63972()
                    with Stage(r"copy source", r"Mac/Plugins/L360.bundle", prog_num=63973):  # 0m:0.129s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", r".", delete_extraneous_files=True, prog_num=63974) as copy_dir_to_dir_893_63974:  # 0m:0.002s
                            copy_dir_to_dir_893_63974()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", where_to_unwtar=r".", prog_num=63975) as unwtar_894_63975:  # 0m:0.127s
                            unwtar_894_63975()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L360.bundle", user_id=-1, group_id=-1, prog_num=63976, recursive=True) as chown_895_63976:  # 0m:0.000s
                            chown_895_63976()
            with Stage(r"copy", r"L3-16 v16.0.23.24", prog_num=63977):  # 0m:1.576s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63978) as should_copy_source_896_63978:  # 0m:1.576s
                    should_copy_source_896_63978()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=63979):  # 0m:1.576s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=63980) as copy_dir_to_dir_897_63980:  # 0m:0.002s
                            copy_dir_to_dir_897_63980()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=63981) as unwtar_898_63981:  # 0m:1.573s
                            unwtar_898_63981()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-16.bundle", user_id=-1, group_id=-1, prog_num=63982, recursive=True) as chown_899_63982:  # 0m:0.000s
                            chown_899_63982()
            with Stage(r"copy", r"L3-LL Multi v16.0.23.24", prog_num=63983):  # 0m:0.149s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63984) as should_copy_source_900_63984:  # 0m:0.149s
                    should_copy_source_900_63984()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=63985):  # 0m:0.149s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=63986) as copy_dir_to_dir_901_63986:  # 0m:0.002s
                            copy_dir_to_dir_901_63986()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=63987) as unwtar_902_63987:  # 0m:0.146s
                            unwtar_902_63987()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=63988, recursive=True) as chown_903_63988:  # 0m:0.001s
                            chown_903_63988()
            with Stage(r"copy", r"L3-LL Ultra v16.0.23.24", prog_num=63989):  # 0m:0.166s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63990) as should_copy_source_904_63990:  # 0m:0.165s
                    should_copy_source_904_63990()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=63991):  # 0m:0.165s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=63992) as copy_dir_to_dir_905_63992:  # 0m:0.002s
                            copy_dir_to_dir_905_63992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=63993) as unwtar_906_63993:  # 0m:0.163s
                            unwtar_906_63993()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=63994, recursive=True) as chown_907_63994:  # 0m:0.000s
                            chown_907_63994()
            with Stage(r"copy", r"L3 Multi v16.0.23.24", prog_num=63995):  # 0m:0.131s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63996) as should_copy_source_908_63996:  # 0m:0.131s
                    should_copy_source_908_63996()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=63997):  # 0m:0.131s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=63998) as copy_dir_to_dir_909_63998:  # 0m:0.002s
                            copy_dir_to_dir_909_63998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=63999) as unwtar_910_63999:  # 0m:0.128s
                            unwtar_910_63999()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=64000, recursive=True) as chown_911_64000:  # 0m:0.000s
                            chown_911_64000()
            with Stage(r"copy", r"L3 Ultra v16.0.23.24", prog_num=64001):  # 0m:0.120s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64002) as should_copy_source_912_64002:  # 0m:0.120s
                    should_copy_source_912_64002()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=64003):  # 0m:0.120s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=64004) as copy_dir_to_dir_913_64004:  # 0m:0.002s
                            copy_dir_to_dir_913_64004()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=64005) as unwtar_914_64005:  # 0m:0.117s
                            unwtar_914_64005()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=64006, recursive=True) as chown_915_64006:  # 0m:0.000s
                            chown_915_64006()
            with Stage(r"copy", r"LFE360 v16.0.23.24", prog_num=64007):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64008) as should_copy_source_916_64008:  # 0m:0.100s
                    should_copy_source_916_64008()
                    with Stage(r"copy source", r"Mac/Plugins/LFE360.bundle", prog_num=64009):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", r".", delete_extraneous_files=True, prog_num=64010) as copy_dir_to_dir_917_64010:  # 0m:0.002s
                            copy_dir_to_dir_917_64010()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", where_to_unwtar=r".", prog_num=64011) as unwtar_918_64011:  # 0m:0.097s
                            unwtar_918_64011()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LFE360.bundle", user_id=-1, group_id=-1, prog_num=64012, recursive=True) as chown_919_64012:  # 0m:0.000s
                            chown_919_64012()
            with Stage(r"copy", r"Lil Tube v16.0.23.24", prog_num=64013):  # 0m:0.252s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64014) as should_copy_source_920_64014:  # 0m:0.252s
                    should_copy_source_920_64014()
                    with Stage(r"copy source", r"Mac/Plugins/Lil Tube.bundle", prog_num=64015):  # 0m:0.251s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", r".", delete_extraneous_files=True, prog_num=64016) as copy_dir_to_dir_921_64016:  # 0m:0.003s
                            copy_dir_to_dir_921_64016()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", where_to_unwtar=r".", prog_num=64017) as unwtar_922_64017:  # 0m:0.248s
                            unwtar_922_64017()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lil Tube.bundle", user_id=-1, group_id=-1, prog_num=64018, recursive=True) as chown_923_64018:  # 0m:0.000s
                            chown_923_64018()
            with Stage(r"copy", r"LinEQ v16.0.23.24", prog_num=64019):  # 0m:0.228s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64020) as should_copy_source_924_64020:  # 0m:0.227s
                    should_copy_source_924_64020()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=64021):  # 0m:0.227s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=64022) as copy_dir_to_dir_925_64022:  # 0m:0.002s
                            copy_dir_to_dir_925_64022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=64023) as unwtar_926_64023:  # 0m:0.224s
                            unwtar_926_64023()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=64024, recursive=True) as chown_927_64024:  # 0m:0.000s
                            chown_927_64024()
            with Stage(r"copy", r"LinMB v16.0.23.24", prog_num=64025):  # 0m:0.150s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64026) as should_copy_source_928_64026:  # 0m:0.150s
                    should_copy_source_928_64026()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=64027):  # 0m:0.149s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=64028) as copy_dir_to_dir_929_64028:  # 0m:0.002s
                            copy_dir_to_dir_929_64028()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=64029) as unwtar_930_64029:  # 0m:0.147s
                            unwtar_930_64029()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinMB.bundle", user_id=-1, group_id=-1, prog_num=64030, recursive=True) as chown_931_64030:  # 0m:0.000s
                            chown_931_64030()
            with Stage(r"copy", r"LoAir v16.0.23.24", prog_num=64031):  # 0m:0.110s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64032) as should_copy_source_932_64032:  # 0m:0.110s
                    should_copy_source_932_64032()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=64033):  # 0m:0.110s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=64034) as copy_dir_to_dir_933_64034:  # 0m:0.002s
                            copy_dir_to_dir_933_64034()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=64035) as unwtar_934_64035:  # 0m:0.107s
                            unwtar_934_64035()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LoAir.bundle", user_id=-1, group_id=-1, prog_num=64036, recursive=True) as chown_935_64036:  # 0m:0.000s
                            chown_935_64036()
            with Stage(r"copy", r"Lofi Space v16.0.23.24", prog_num=64037):  # 0m:1.138s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64038) as should_copy_source_936_64038:  # 0m:1.138s
                    should_copy_source_936_64038()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=64039):  # 0m:1.138s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=64040) as copy_dir_to_dir_937_64040:  # 0m:0.041s
                            copy_dir_to_dir_937_64040()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=64041) as unwtar_938_64041:  # 0m:1.096s
                            unwtar_938_64041()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=64042, recursive=True) as chown_939_64042:  # 0m:0.000s
                            chown_939_64042()
            with Stage(r"copy", r"MDMX Distortion v16.0.23.24", prog_num=64043):  # 0m:1.709s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64044) as should_copy_source_940_64044:  # 0m:1.709s
                    should_copy_source_940_64044()
                    with Stage(r"copy source", r"Mac/Plugins/MDMX Distortion.bundle", prog_num=64045):  # 0m:1.708s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", r".", delete_extraneous_files=True, prog_num=64046) as copy_dir_to_dir_941_64046:  # 0m:0.002s
                            copy_dir_to_dir_941_64046()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", where_to_unwtar=r".", prog_num=64047) as unwtar_942_64047:  # 0m:1.706s
                            unwtar_942_64047()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MDMX Distortion.bundle", user_id=-1, group_id=-1, prog_num=64048, recursive=True) as chown_943_64048:  # 0m:0.000s
                            chown_943_64048()
            with Stage(r"copy", r"MV2 v16.0.23.24", prog_num=64049):  # 0m:0.095s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64050) as should_copy_source_944_64050:  # 0m:0.095s
                    should_copy_source_944_64050()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=64051):  # 0m:0.095s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=64052) as copy_dir_to_dir_945_64052:  # 0m:0.002s
                            copy_dir_to_dir_945_64052()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=64053) as unwtar_946_64053:  # 0m:0.092s
                            unwtar_946_64053()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV2.bundle", user_id=-1, group_id=-1, prog_num=64054, recursive=True) as chown_947_64054:  # 0m:0.000s
                            chown_947_64054()
            with Stage(r"copy", r"MV360 v16.0.23.24", prog_num=64055):  # 0m:0.116s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64056) as should_copy_source_948_64056:  # 0m:0.116s
                    should_copy_source_948_64056()
                    with Stage(r"copy source", r"Mac/Plugins/MV360.bundle", prog_num=64057):  # 0m:0.116s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", r".", delete_extraneous_files=True, prog_num=64058) as copy_dir_to_dir_949_64058:  # 0m:0.002s
                            copy_dir_to_dir_949_64058()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", where_to_unwtar=r".", prog_num=64059) as unwtar_950_64059:  # 0m:0.113s
                            unwtar_950_64059()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV360.bundle", user_id=-1, group_id=-1, prog_num=64060, recursive=True) as chown_951_64060:  # 0m:0.000s
                            chown_951_64060()
            with Stage(r"copy", r"Magma Channel Strip v16.0.23.24", prog_num=64061):  # 0m:0.903s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64062) as should_copy_source_952_64062:  # 0m:0.903s
                    should_copy_source_952_64062()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaChannelStrip.bundle", prog_num=64063):  # 0m:0.903s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", r".", delete_extraneous_files=True, prog_num=64064) as copy_dir_to_dir_953_64064:  # 0m:0.024s
                            copy_dir_to_dir_953_64064()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", where_to_unwtar=r".", prog_num=64065) as unwtar_954_64065:  # 0m:0.878s
                            unwtar_954_64065()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaChannelStrip.bundle", user_id=-1, group_id=-1, prog_num=64066, recursive=True) as chown_955_64066:  # 0m:0.000s
                            chown_955_64066()
            with Stage(r"copy", r"Magma Springs v16.0.23.24", prog_num=64067):  # 0m:0.917s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64068) as should_copy_source_956_64068:  # 0m:0.917s
                    should_copy_source_956_64068()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=64069):  # 0m:0.917s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=64070) as copy_dir_to_dir_957_64070:  # 0m:0.021s
                            copy_dir_to_dir_957_64070()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=64071) as unwtar_958_64071:  # 0m:0.895s
                            unwtar_958_64071()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=64072, recursive=True) as chown_959_64072:  # 0m:0.000s
                            chown_959_64072()
            with Stage(r"copy", r"MannyM-Delay v16.0.23.24", prog_num=64073):  # 0m:0.953s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64074) as should_copy_source_960_64074:  # 0m:0.953s
                    should_copy_source_960_64074()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Delay.bundle", prog_num=64075):  # 0m:0.953s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", r".", delete_extraneous_files=True, prog_num=64076) as copy_dir_to_dir_961_64076:  # 0m:0.037s
                            copy_dir_to_dir_961_64076()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", where_to_unwtar=r".", prog_num=64077) as unwtar_962_64077:  # 0m:0.916s
                            unwtar_962_64077()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Delay.bundle", user_id=-1, group_id=-1, prog_num=64078, recursive=True) as chown_963_64078:  # 0m:0.000s
                            chown_963_64078()
            with Stage(r"copy", r"MannyM-Distortion v16.0.23.24", prog_num=64079):  # 0m:0.610s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64080) as should_copy_source_964_64080:  # 0m:0.610s
                    should_copy_source_964_64080()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Distortion.bundle", prog_num=64081):  # 0m:0.610s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", r".", delete_extraneous_files=True, prog_num=64082) as copy_dir_to_dir_965_64082:  # 0m:0.020s
                            copy_dir_to_dir_965_64082()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", where_to_unwtar=r".", prog_num=64083) as unwtar_966_64083:  # 0m:0.589s
                            unwtar_966_64083()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Distortion.bundle", user_id=-1, group_id=-1, prog_num=64084, recursive=True) as chown_967_64084:  # 0m:0.000s
                            chown_967_64084()
            with Stage(r"copy", r"MannyM-EQ v16.0.23.24", prog_num=64085):  # 0m:0.405s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64086) as should_copy_source_968_64086:  # 0m:0.404s
                    should_copy_source_968_64086()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-EQ.bundle", prog_num=64087):  # 0m:0.404s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", r".", delete_extraneous_files=True, prog_num=64088) as copy_dir_to_dir_969_64088:  # 0m:0.011s
                            copy_dir_to_dir_969_64088()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", where_to_unwtar=r".", prog_num=64089) as unwtar_970_64089:  # 0m:0.393s
                            unwtar_970_64089()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-EQ.bundle", user_id=-1, group_id=-1, prog_num=64090, recursive=True) as chown_971_64090:  # 0m:0.000s
                            chown_971_64090()
            with Stage(r"copy", r"MannyM-Reverb v16.0.23.24", prog_num=64091):  # 0m:0.695s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64092) as should_copy_source_972_64092:  # 0m:0.695s
                    should_copy_source_972_64092()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Reverb.bundle", prog_num=64093):  # 0m:0.694s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=64094) as copy_dir_to_dir_973_64094:  # 0m:0.020s
                            copy_dir_to_dir_973_64094()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", where_to_unwtar=r".", prog_num=64095) as unwtar_974_64095:  # 0m:0.674s
                            unwtar_974_64095()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Reverb.bundle", user_id=-1, group_id=-1, prog_num=64096, recursive=True) as chown_975_64096:  # 0m:0.000s
                            chown_975_64096()
            with Stage(r"copy", r"MannyM-ToneShaper v16.0.23.24", prog_num=64097):  # 0m:0.802s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64098) as should_copy_source_976_64098:  # 0m:0.802s
                    should_copy_source_976_64098()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-ToneShaper.bundle", prog_num=64099):  # 0m:0.802s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", r".", delete_extraneous_files=True, prog_num=64100) as copy_dir_to_dir_977_64100:  # 0m:0.025s
                            copy_dir_to_dir_977_64100()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", where_to_unwtar=r".", prog_num=64101) as unwtar_978_64101:  # 0m:0.776s
                            unwtar_978_64101()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-ToneShaper.bundle", user_id=-1, group_id=-1, prog_num=64102, recursive=True) as chown_979_64102:  # 0m:0.000s
                            chown_979_64102()
            with Stage(r"copy", r"MannyM-TripleD v16.0.23.24", prog_num=64103):  # 0m:0.505s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64104) as should_copy_source_980_64104:  # 0m:0.505s
                    should_copy_source_980_64104()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=64105):  # 0m:0.505s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=64106) as copy_dir_to_dir_981_64106:  # 0m:0.014s
                            copy_dir_to_dir_981_64106()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=64107) as unwtar_982_64107:  # 0m:0.491s
                            unwtar_982_64107()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=64108, recursive=True) as chown_983_64108:  # 0m:0.000s
                            chown_983_64108()
            with Stage(r"copy", r"Maserati ACG v16.0.23.24", prog_num=64109):  # 0m:0.449s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64110) as should_copy_source_984_64110:  # 0m:0.449s
                    should_copy_source_984_64110()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati ACG.bundle", prog_num=64111):  # 0m:0.448s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", r".", delete_extraneous_files=True, prog_num=64112) as copy_dir_to_dir_985_64112:  # 0m:0.015s
                            copy_dir_to_dir_985_64112()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", where_to_unwtar=r".", prog_num=64113) as unwtar_986_64113:  # 0m:0.433s
                            unwtar_986_64113()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati ACG.bundle", user_id=-1, group_id=-1, prog_num=64114, recursive=True) as chown_987_64114:  # 0m:0.000s
                            chown_987_64114()
            with Stage(r"copy", r"Maserati B72 v16.0.23.24", prog_num=64115):  # 0m:0.731s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64116) as should_copy_source_988_64116:  # 0m:0.731s
                    should_copy_source_988_64116()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati B72.bundle", prog_num=64117):  # 0m:0.731s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", r".", delete_extraneous_files=True, prog_num=64118) as copy_dir_to_dir_989_64118:  # 0m:0.024s
                            copy_dir_to_dir_989_64118()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", where_to_unwtar=r".", prog_num=64119) as unwtar_990_64119:  # 0m:0.706s
                            unwtar_990_64119()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati B72.bundle", user_id=-1, group_id=-1, prog_num=64120, recursive=True) as chown_991_64120:  # 0m:0.000s
                            chown_991_64120()
            with Stage(r"copy", r"Maserati DRM v16.0.23.24", prog_num=64121):  # 0m:0.189s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64122) as should_copy_source_992_64122:  # 0m:0.189s
                    should_copy_source_992_64122()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=64123):  # 0m:0.189s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=64124) as copy_dir_to_dir_993_64124:  # 0m:0.004s
                            copy_dir_to_dir_993_64124()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=64125) as unwtar_994_64125:  # 0m:0.184s
                            unwtar_994_64125()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=64126, recursive=True) as chown_995_64126:  # 0m:0.000s
                            chown_995_64126()
            with Stage(r"copy", r"Maserati GRP v16.0.23.24", prog_num=64127):  # 0m:1.172s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64128) as should_copy_source_996_64128:  # 0m:1.172s
                    should_copy_source_996_64128()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati GRP.bundle", prog_num=64129):  # 0m:1.172s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", r".", delete_extraneous_files=True, prog_num=64130) as copy_dir_to_dir_997_64130:  # 0m:0.042s
                            copy_dir_to_dir_997_64130()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", where_to_unwtar=r".", prog_num=64131) as unwtar_998_64131:  # 0m:1.130s
                            unwtar_998_64131()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati GRP.bundle", user_id=-1, group_id=-1, prog_num=64132, recursive=True) as chown_999_64132:  # 0m:0.000s
                            chown_999_64132()
            with Stage(r"copy", r"Maserati GTi v16.0.23.24", prog_num=64133):  # 0m:1.994s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64134) as should_copy_source_1000_64134:  # 0m:1.994s
                    should_copy_source_1000_64134()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati GTi.bundle", prog_num=64135):  # 0m:1.994s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", r".", delete_extraneous_files=True, prog_num=64136) as copy_dir_to_dir_1001_64136:  # 0m:0.039s
                            copy_dir_to_dir_1001_64136()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", where_to_unwtar=r".", prog_num=64137) as unwtar_1002_64137:  # 0m:1.954s
                            unwtar_1002_64137()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati GTi.bundle", user_id=-1, group_id=-1, prog_num=64138, recursive=True) as chown_1003_64138:  # 0m:0.000s
                            chown_1003_64138()
            with Stage(r"copy", r"Maserati HMX v16.0.23.24", prog_num=64139):  # 0m:1.449s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64140) as should_copy_source_1004_64140:  # 0m:1.449s
                    should_copy_source_1004_64140()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati HMX.bundle", prog_num=64141):  # 0m:1.448s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", r".", delete_extraneous_files=True, prog_num=64142) as copy_dir_to_dir_1005_64142:  # 0m:0.025s
                            copy_dir_to_dir_1005_64142()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", where_to_unwtar=r".", prog_num=64143) as unwtar_1006_64143:  # 0m:1.423s
                            unwtar_1006_64143()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati HMX.bundle", user_id=-1, group_id=-1, prog_num=64144, recursive=True) as chown_1007_64144:  # 0m:0.000s
                            chown_1007_64144()
            with Stage(r"copy", r"Maserati VX1 v16.0.23.24", prog_num=64145):  # 0m:1.046s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64146) as should_copy_source_1008_64146:  # 0m:1.046s
                    should_copy_source_1008_64146()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=64147):  # 0m:1.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=64148) as copy_dir_to_dir_1009_64148:  # 0m:0.030s
                            copy_dir_to_dir_1009_64148()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=64149) as unwtar_1010_64149:  # 0m:1.016s
                            unwtar_1010_64149()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=64150, recursive=True) as chown_1011_64150:  # 0m:0.000s
                            chown_1011_64150()
            with Stage(r"copy", r"MaxxBass v16.0.30.31", prog_num=64151):  # 0m:0.234s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64152) as should_copy_source_1012_64152:  # 0m:0.233s
                    should_copy_source_1012_64152()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=64153):  # 0m:0.233s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=64154) as copy_dir_to_dir_1013_64154:  # 0m:0.002s
                            copy_dir_to_dir_1013_64154()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=64155) as unwtar_1014_64155:  # 0m:0.230s
                            unwtar_1014_64155()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=64156, recursive=True) as chown_1015_64156:  # 0m:0.000s
                            chown_1015_64156()
            with Stage(r"copy", r"MaxxVolume v16.0.23.24", prog_num=64157):  # 0m:0.142s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64158) as should_copy_source_1016_64158:  # 0m:0.142s
                    should_copy_source_1016_64158()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=64159):  # 0m:0.142s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=64160) as copy_dir_to_dir_1017_64160:  # 0m:0.002s
                            copy_dir_to_dir_1017_64160()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=64161) as unwtar_1018_64161:  # 0m:0.139s
                            unwtar_1018_64161()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=64162, recursive=True) as chown_1019_64162:  # 0m:0.000s
                            chown_1019_64162()
            with Stage(r"copy", r"MetaFilter v16.0.23.24", prog_num=64163):  # 0m:0.441s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64164) as should_copy_source_1020_64164:  # 0m:0.440s
                    should_copy_source_1020_64164()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=64165):  # 0m:0.440s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=64166) as copy_dir_to_dir_1021_64166:  # 0m:0.002s
                            copy_dir_to_dir_1021_64166()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=64167) as unwtar_1022_64167:  # 0m:0.438s
                            unwtar_1022_64167()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=64168, recursive=True) as chown_1023_64168:  # 0m:0.000s
                            chown_1023_64168()
            with Stage(r"copy", r"MetaFlanger v16.0.23.24", prog_num=64169):  # 0m:0.101s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64170) as should_copy_source_1024_64170:  # 0m:0.101s
                    should_copy_source_1024_64170()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=64171):  # 0m:0.101s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64172) as copy_dir_to_dir_1025_64172:  # 0m:0.002s
                            copy_dir_to_dir_1025_64172()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=64173) as unwtar_1026_64173:  # 0m:0.098s
                            unwtar_1026_64173()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=64174, recursive=True) as chown_1027_64174:  # 0m:0.000s
                            chown_1027_64174()
            with Stage(r"copy", r"MondoMod v16.0.23.24", prog_num=64175):  # 0m:0.112s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64176) as should_copy_source_1028_64176:  # 0m:0.112s
                    should_copy_source_1028_64176()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=64177):  # 0m:0.112s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=64178) as copy_dir_to_dir_1029_64178:  # 0m:0.002s
                            copy_dir_to_dir_1029_64178()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=64179) as unwtar_1030_64179:  # 0m:0.109s
                            unwtar_1030_64179()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=64180, recursive=True) as chown_1031_64180:  # 0m:0.000s
                            chown_1031_64180()
            with Stage(r"copy", r"Morphoder v16.0.23.24", prog_num=64181):  # 0m:0.461s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64182) as should_copy_source_1032_64182:  # 0m:0.461s
                    should_copy_source_1032_64182()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=64183):  # 0m:0.461s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=64184) as copy_dir_to_dir_1033_64184:  # 0m:0.002s
                            copy_dir_to_dir_1033_64184()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=64185) as unwtar_1034_64185:  # 0m:0.459s
                            unwtar_1034_64185()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=64186, recursive=True) as chown_1035_64186:  # 0m:0.000s
                            chown_1035_64186()
            with Stage(r"copy", r"MultiMod Rack v16.0.23.24", prog_num=64187):  # 0m:2.797s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64188) as should_copy_source_1036_64188:  # 0m:2.797s
                    should_copy_source_1036_64188()
                    with Stage(r"copy source", r"Mac/Plugins/MultiMod Rack.bundle", prog_num=64189):  # 0m:2.797s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", r".", delete_extraneous_files=True, prog_num=64190) as copy_dir_to_dir_1037_64190:  # 0m:0.027s
                            copy_dir_to_dir_1037_64190()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", where_to_unwtar=r".", prog_num=64191) as unwtar_1038_64191:  # 0m:2.769s
                            unwtar_1038_64191()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MultiMod Rack.bundle", user_id=-1, group_id=-1, prog_num=64192, recursive=True) as chown_1039_64192:  # 0m:0.000s
                            chown_1039_64192()
            with Stage(r"copy", r"StudioVerse Instruments v16.0.30.31", prog_num=64193):  # 0m:4.137s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64194) as should_copy_source_1040_64194:  # 0m:4.137s
                    should_copy_source_1040_64194()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Instruments.bundle", prog_num=64195):  # 0m:4.136s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", r".", delete_extraneous_files=True, prog_num=64196) as copy_dir_to_dir_1041_64196:  # 0m:0.030s
                            copy_dir_to_dir_1041_64196()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", where_to_unwtar=r".", prog_num=64197) as unwtar_1042_64197:  # 0m:4.106s
                            unwtar_1042_64197()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/StudioVerse Instruments.bundle", user_id=-1, group_id=-1, prog_num=64198, recursive=True) as chown_1043_64198:  # 0m:0.000s
                            chown_1043_64198()
            with Stage(r"copy", r"NLS v16.0.23.24", prog_num=64199):  # 0m:1.187s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64200) as should_copy_source_1044_64200:  # 0m:1.187s
                    should_copy_source_1044_64200()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=64201):  # 0m:1.186s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=64202) as copy_dir_to_dir_1045_64202:  # 0m:0.002s
                            copy_dir_to_dir_1045_64202()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=64203) as unwtar_1046_64203:  # 0m:1.184s
                            unwtar_1046_64203()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NLS.bundle", user_id=-1, group_id=-1, prog_num=64204, recursive=True) as chown_1047_64204:  # 0m:0.000s
                            chown_1047_64204()
            with Stage(r"copy", r"NS1 v16.0.23.24", prog_num=64205):  # 0m:0.102s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64206) as should_copy_source_1048_64206:  # 0m:0.102s
                    should_copy_source_1048_64206()
                    with Stage(r"copy source", r"Mac/Plugins/NS1.bundle", prog_num=64207):  # 0m:0.101s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", r".", delete_extraneous_files=True, prog_num=64208) as copy_dir_to_dir_1049_64208:  # 0m:0.002s
                            copy_dir_to_dir_1049_64208()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", where_to_unwtar=r".", prog_num=64209) as unwtar_1050_64209:  # 0m:0.099s
                            unwtar_1050_64209()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NS1.bundle", user_id=-1, group_id=-1, prog_num=64210, recursive=True) as chown_1051_64210:  # 0m:0.000s
                            chown_1051_64210()
            with Stage(r"copy", r"NX v16.0.23.24", prog_num=64211):  # 0m:0.930s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64212) as should_copy_source_1052_64212:  # 0m:0.930s
                    should_copy_source_1052_64212()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=64213):  # 0m:0.930s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=64214) as copy_dir_to_dir_1053_64214:  # 0m:0.002s
                            copy_dir_to_dir_1053_64214()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=64215) as unwtar_1054_64215:  # 0m:0.927s
                            unwtar_1054_64215()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NX.bundle", user_id=-1, group_id=-1, prog_num=64216, recursive=True) as chown_1055_64216:  # 0m:0.000s
                            chown_1055_64216()
            with Stage(r"copy", r"Nx Ocean Way Nashville v16.0.23.24", prog_num=64217):  # 0m:13.909s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64218) as should_copy_source_1056_64218:  # 0m:13.909s
                    should_copy_source_1056_64218()
                    with Stage(r"copy source", r"Mac/Plugins/Nx Ocean Way Nashville.bundle", prog_num=64219):  # 0m:13.909s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", r".", delete_extraneous_files=True, prog_num=64220) as copy_dir_to_dir_1057_64220:  # 0m:0.023s
                            copy_dir_to_dir_1057_64220()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", where_to_unwtar=r".", prog_num=64221) as unwtar_1058_64221:  # 0m:13.885s
                            unwtar_1058_64221()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Nx Ocean Way Nashville.bundle", user_id=-1, group_id=-1, prog_num=64222, recursive=True) as chown_1059_64222:  # 0m:0.000s
                            chown_1059_64222()
            with Stage(r"copy", r"Nx Germano Studios v16.0.23.24", prog_num=64223):  # 0m:12.701s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64224) as should_copy_source_1060_64224:  # 0m:12.701s
                    should_copy_source_1060_64224()
                    with Stage(r"copy source", r"Mac/Plugins/Nx Germano Studios.bundle", prog_num=64225):  # 0m:12.700s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", r".", delete_extraneous_files=True, prog_num=64226) as copy_dir_to_dir_1061_64226:  # 0m:0.033s
                            copy_dir_to_dir_1061_64226()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", where_to_unwtar=r".", prog_num=64227) as unwtar_1062_64227:  # 0m:12.667s
                            unwtar_1062_64227()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Nx Germano Studios.bundle", user_id=-1, group_id=-1, prog_num=64228, recursive=True) as chown_1063_64228:  # 0m:0.000s
                            chown_1063_64228()
            with Stage(r"copy", r"OKBrighter v16.0.23.24", prog_num=64229):  # 0m:0.112s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64230) as should_copy_source_1064_64230:  # 0m:0.112s
                    should_copy_source_1064_64230()
                    with Stage(r"copy source", r"Mac/Plugins/OKBrighter.bundle", prog_num=64231):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", r".", delete_extraneous_files=True, prog_num=64232) as copy_dir_to_dir_1065_64232:  # 0m:0.002s
                            copy_dir_to_dir_1065_64232()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", where_to_unwtar=r".", prog_num=64233) as unwtar_1066_64233:  # 0m:0.109s
                            unwtar_1066_64233()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKBrighter.bundle", user_id=-1, group_id=-1, prog_num=64234, recursive=True) as chown_1067_64234:  # 0m:0.000s
                            chown_1067_64234()
            with Stage(r"copy", r"OKDriver v16.0.23.24", prog_num=64235):  # 0m:0.117s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64236) as should_copy_source_1068_64236:  # 0m:0.117s
                    should_copy_source_1068_64236()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=64237):  # 0m:0.117s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=64238) as copy_dir_to_dir_1069_64238:  # 0m:0.002s
                            copy_dir_to_dir_1069_64238()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=64239) as unwtar_1070_64239:  # 0m:0.114s
                            unwtar_1070_64239()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=64240, recursive=True) as chown_1071_64240:  # 0m:0.000s
                            chown_1071_64240()
            with Stage(r"copy", r"OKFilter v16.0.23.24", prog_num=64241):  # 0m:0.118s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64242) as should_copy_source_1072_64242:  # 0m:0.118s
                    should_copy_source_1072_64242()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=64243):  # 0m:0.118s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=64244) as copy_dir_to_dir_1073_64244:  # 0m:0.002s
                            copy_dir_to_dir_1073_64244()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=64245) as unwtar_1074_64245:  # 0m:0.115s
                            unwtar_1074_64245()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=64246, recursive=True) as chown_1075_64246:  # 0m:0.000s
                            chown_1075_64246()
            with Stage(r"copy", r"OKLouder v16.0.23.24", prog_num=64247):  # 0m:0.121s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64248) as should_copy_source_1076_64248:  # 0m:0.121s
                    should_copy_source_1076_64248()
                    with Stage(r"copy source", r"Mac/Plugins/OKLouder.bundle", prog_num=64249):  # 0m:0.121s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", r".", delete_extraneous_files=True, prog_num=64250) as copy_dir_to_dir_1077_64250:  # 0m:0.002s
                            copy_dir_to_dir_1077_64250()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", where_to_unwtar=r".", prog_num=64251) as unwtar_1078_64251:  # 0m:0.118s
                            unwtar_1078_64251()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKLouder.bundle", user_id=-1, group_id=-1, prog_num=64252, recursive=True) as chown_1079_64252:  # 0m:0.000s
                            chown_1079_64252()
            with Stage(r"copy", r"OKPhatter v16.0.23.24", prog_num=64253):  # 0m:0.115s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64254) as should_copy_source_1080_64254:  # 0m:0.115s
                    should_copy_source_1080_64254()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=64255):  # 0m:0.114s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=64256) as copy_dir_to_dir_1081_64256:  # 0m:0.002s
                            copy_dir_to_dir_1081_64256()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=64257) as unwtar_1082_64257:  # 0m:0.112s
                            unwtar_1082_64257()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=64258, recursive=True) as chown_1083_64258:  # 0m:0.000s
                            chown_1083_64258()
            with Stage(r"copy", r"OKPressure v16.0.23.24", prog_num=64259):  # 0m:0.131s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64260) as should_copy_source_1084_64260:  # 0m:0.131s
                    should_copy_source_1084_64260()
                    with Stage(r"copy source", r"Mac/Plugins/OKPressure.bundle", prog_num=64261):  # 0m:0.130s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", r".", delete_extraneous_files=True, prog_num=64262) as copy_dir_to_dir_1085_64262:  # 0m:0.007s
                            copy_dir_to_dir_1085_64262()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", where_to_unwtar=r".", prog_num=64263) as unwtar_1086_64263:  # 0m:0.122s
                            unwtar_1086_64263()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPressure.bundle", user_id=-1, group_id=-1, prog_num=64264, recursive=True) as chown_1087_64264:  # 0m:0.000s
                            chown_1087_64264()
            with Stage(r"copy", r"OKPumper v16.0.23.24", prog_num=64265):  # 0m:0.098s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64266) as should_copy_source_1088_64266:  # 0m:0.098s
                    should_copy_source_1088_64266()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=64267):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=64268) as copy_dir_to_dir_1089_64268:  # 0m:0.002s
                            copy_dir_to_dir_1089_64268()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=64269) as unwtar_1090_64269:  # 0m:0.095s
                            unwtar_1090_64269()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=64270, recursive=True) as chown_1091_64270:  # 0m:0.000s
                            chown_1091_64270()
            with Stage(r"copy", r"OKWetter v16.0.23.24", prog_num=64271):  # 0m:0.271s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64272) as should_copy_source_1092_64272:  # 0m:0.271s
                    should_copy_source_1092_64272()
                    with Stage(r"copy source", r"Mac/Plugins/OKWetter.bundle", prog_num=64273):  # 0m:0.271s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", r".", delete_extraneous_files=True, prog_num=64274) as copy_dir_to_dir_1093_64274:  # 0m:0.011s
                            copy_dir_to_dir_1093_64274()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", where_to_unwtar=r".", prog_num=64275) as unwtar_1094_64275:  # 0m:0.259s
                            unwtar_1094_64275()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKWetter.bundle", user_id=-1, group_id=-1, prog_num=64276, recursive=True) as chown_1095_64276:  # 0m:0.000s
                            chown_1095_64276()
            with Stage(r"copy", r"OVox v16.0.23.24", prog_num=64277):  # 0m:0.814s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64278) as should_copy_source_1096_64278:  # 0m:0.814s
                    should_copy_source_1096_64278()
                    with Stage(r"copy source", r"Mac/Plugins/OVox.bundle", prog_num=64279):  # 0m:0.814s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", r".", delete_extraneous_files=True, prog_num=64280) as copy_dir_to_dir_1097_64280:  # 0m:0.003s
                            copy_dir_to_dir_1097_64280()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", where_to_unwtar=r".", prog_num=64281) as unwtar_1098_64281:  # 0m:0.811s
                            unwtar_1098_64281()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OVox.bundle", user_id=-1, group_id=-1, prog_num=64282, recursive=True) as chown_1099_64282:  # 0m:0.000s
                            chown_1099_64282()
            with Stage(r"copy", r"PAZ v16.0.23.24", prog_num=64283):  # 0m:0.100s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64284) as should_copy_source_1100_64284:  # 0m:0.100s
                    should_copy_source_1100_64284()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=64285):  # 0m:0.100s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=64286) as copy_dir_to_dir_1101_64286:  # 0m:0.002s
                            copy_dir_to_dir_1101_64286()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=64287) as unwtar_1102_64287:  # 0m:0.097s
                            unwtar_1102_64287()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PAZ.bundle", user_id=-1, group_id=-1, prog_num=64288, recursive=True) as chown_1103_64288:  # 0m:0.000s
                            chown_1103_64288()
            with Stage(r"copy", r"PRS Supermodels v16.0.23.24", prog_num=64289):  # 0m:2.638s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64290) as should_copy_source_1104_64290:  # 0m:2.638s
                    should_copy_source_1104_64290()
                    with Stage(r"copy source", r"Mac/Plugins/PRS Supermodels.bundle", prog_num=64291):  # 0m:2.638s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", r".", delete_extraneous_files=True, prog_num=64292) as copy_dir_to_dir_1105_64292:  # 0m:0.025s
                            copy_dir_to_dir_1105_64292()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", where_to_unwtar=r".", prog_num=64293) as unwtar_1106_64293:  # 0m:2.612s
                            unwtar_1106_64293()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PRS Supermodels.bundle", user_id=-1, group_id=-1, prog_num=64294, recursive=True) as chown_1107_64294:  # 0m:0.000s
                            chown_1107_64294()
            with Stage(r"copy", r"PS22 v16.0.23.24", prog_num=64295):  # 0m:0.113s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64296) as should_copy_source_1108_64296:  # 0m:0.113s
                    should_copy_source_1108_64296()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=64297):  # 0m:0.113s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=64298) as copy_dir_to_dir_1109_64298:  # 0m:0.002s
                            copy_dir_to_dir_1109_64298()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=64299) as unwtar_1110_64299:  # 0m:0.110s
                            unwtar_1110_64299()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PS22.bundle", user_id=-1, group_id=-1, prog_num=64300, recursive=True) as chown_1111_64300:  # 0m:0.000s
                            chown_1111_64300()
            with Stage(r"copy", r"Primary Source Expander v16.0.23.24", prog_num=64301):  # 0m:0.181s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64302) as should_copy_source_1112_64302:  # 0m:0.181s
                    should_copy_source_1112_64302()
                    with Stage(r"copy source", r"Mac/Plugins/Primary Source Expander.bundle", prog_num=64303):  # 0m:0.180s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", r".", delete_extraneous_files=True, prog_num=64304) as copy_dir_to_dir_1113_64304:  # 0m:0.003s
                            copy_dir_to_dir_1113_64304()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", where_to_unwtar=r".", prog_num=64305) as unwtar_1114_64305:  # 0m:0.178s
                            unwtar_1114_64305()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Primary Source Expander.bundle", user_id=-1, group_id=-1, prog_num=64306, recursive=True) as chown_1115_64306:  # 0m:0.000s
                            chown_1115_64306()
            with Stage(r"copy", r"PlaylistRider v16.0.23.24", prog_num=64307):  # 0m:0.150s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64308) as should_copy_source_1116_64308:  # 0m:0.150s
                    should_copy_source_1116_64308()
                    with Stage(r"copy source", r"Mac/Plugins/PlaylistRider.bundle", prog_num=64309):  # 0m:0.150s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", r".", delete_extraneous_files=True, prog_num=64310) as copy_dir_to_dir_1117_64310:  # 0m:0.002s
                            copy_dir_to_dir_1117_64310()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", where_to_unwtar=r".", prog_num=64311) as unwtar_1118_64311:  # 0m:0.147s
                            unwtar_1118_64311()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PlaylistRider.bundle", user_id=-1, group_id=-1, prog_num=64312, recursive=True) as chown_1119_64312:  # 0m:0.000s
                            chown_1119_64312()
            with Stage(r"copy", r"PuigChild v16.0.23.24", prog_num=64313):  # 0m:1.751s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64314) as should_copy_source_1120_64314:  # 0m:1.751s
                    should_copy_source_1120_64314()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=64315):  # 0m:1.751s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=64316) as copy_dir_to_dir_1121_64316:  # 0m:0.002s
                            copy_dir_to_dir_1121_64316()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=64317) as unwtar_1122_64317:  # 0m:1.748s
                            unwtar_1122_64317()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=64318, recursive=True) as chown_1123_64318:  # 0m:0.000s
                            chown_1123_64318()
            with Stage(r"copy", r"PuigTec v16.0.23.24", prog_num=64319):  # 0m:1.902s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64320) as should_copy_source_1124_64320:  # 0m:1.902s
                    should_copy_source_1124_64320()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=64321):  # 0m:1.902s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=64322) as copy_dir_to_dir_1125_64322:  # 0m:0.002s
                            copy_dir_to_dir_1125_64322()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=64323) as unwtar_1126_64323:  # 0m:1.899s
                            unwtar_1126_64323()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=64324, recursive=True) as chown_1127_64324:  # 0m:0.000s
                            chown_1127_64324()
            with Stage(r"copy", r"Q10 v16.0.23.24", prog_num=64325):  # 0m:0.288s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64326) as should_copy_source_1128_64326:  # 0m:0.288s
                    should_copy_source_1128_64326()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=64327):  # 0m:0.288s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=64328) as copy_dir_to_dir_1129_64328:  # 0m:0.003s
                            copy_dir_to_dir_1129_64328()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=64329) as unwtar_1130_64329:  # 0m:0.285s
                            unwtar_1130_64329()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q10.bundle", user_id=-1, group_id=-1, prog_num=64330, recursive=True) as chown_1131_64330:  # 0m:0.000s
                            chown_1131_64330()
            with Stage(r"copy", r"Q-Clone v16.0.23.24", prog_num=64331):  # 0m:0.282s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64332) as should_copy_source_1132_64332:  # 0m:0.282s
                    should_copy_source_1132_64332()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=64333):  # 0m:0.281s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=64334) as copy_dir_to_dir_1133_64334:  # 0m:0.002s
                            copy_dir_to_dir_1133_64334()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=64335) as unwtar_1134_64335:  # 0m:0.279s
                            unwtar_1134_64335()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=64336, recursive=True) as chown_1135_64336:  # 0m:0.000s
                            chown_1135_64336()
            with Stage(r"copy", r"R360 v16.0.23.24", prog_num=64337):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64338) as should_copy_source_1136_64338:  # 0m:0.111s
                    should_copy_source_1136_64338()
                    with Stage(r"copy source", r"Mac/Plugins/R360.bundle", prog_num=64339):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", r".", delete_extraneous_files=True, prog_num=64340) as copy_dir_to_dir_1137_64340:  # 0m:0.002s
                            copy_dir_to_dir_1137_64340()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", where_to_unwtar=r".", prog_num=64341) as unwtar_1138_64341:  # 0m:0.109s
                            unwtar_1138_64341()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/R360.bundle", user_id=-1, group_id=-1, prog_num=64342, recursive=True) as chown_1139_64342:  # 0m:0.000s
                            chown_1139_64342()
            with Stage(r"copy", r"RBass v16.0.23.24", prog_num=64343):  # 0m:0.159s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64344) as should_copy_source_1140_64344:  # 0m:0.159s
                    should_copy_source_1140_64344()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=64345):  # 0m:0.159s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=64346) as copy_dir_to_dir_1141_64346:  # 0m:0.002s
                            copy_dir_to_dir_1141_64346()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=64347) as unwtar_1142_64347:  # 0m:0.156s
                            unwtar_1142_64347()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RBass.bundle", user_id=-1, group_id=-1, prog_num=64348, recursive=True) as chown_1143_64348:  # 0m:0.000s
                            chown_1143_64348()
            with Stage(r"copy", r"RChannel v16.0.23.24", prog_num=64349):  # 0m:0.277s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64350) as should_copy_source_1144_64350:  # 0m:0.277s
                    should_copy_source_1144_64350()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=64351):  # 0m:0.277s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=64352) as copy_dir_to_dir_1145_64352:  # 0m:0.002s
                            copy_dir_to_dir_1145_64352()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=64353) as unwtar_1146_64353:  # 0m:0.274s
                            unwtar_1146_64353()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RChannel.bundle", user_id=-1, group_id=-1, prog_num=64354, recursive=True) as chown_1147_64354:  # 0m:0.000s
                            chown_1147_64354()
            with Stage(r"copy", r"RComp v16.0.23.24", prog_num=64355):  # 0m:0.127s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64356) as should_copy_source_1148_64356:  # 0m:0.127s
                    should_copy_source_1148_64356()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=64357):  # 0m:0.127s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=64358) as copy_dir_to_dir_1149_64358:  # 0m:0.002s
                            copy_dir_to_dir_1149_64358()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=64359) as unwtar_1150_64359:  # 0m:0.125s
                            unwtar_1150_64359()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RComp.bundle", user_id=-1, group_id=-1, prog_num=64360, recursive=True) as chown_1151_64360:  # 0m:0.000s
                            chown_1151_64360()
            with Stage(r"copy", r"RDeEsser v16.0.23.24", prog_num=64361):  # 0m:0.346s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64362) as should_copy_source_1152_64362:  # 0m:0.346s
                    should_copy_source_1152_64362()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=64363):  # 0m:0.346s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=64364) as copy_dir_to_dir_1153_64364:  # 0m:0.002s
                            copy_dir_to_dir_1153_64364()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=64365) as unwtar_1154_64365:  # 0m:0.343s
                            unwtar_1154_64365()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=64366, recursive=True) as chown_1155_64366:  # 0m:0.000s
                            chown_1155_64366()
            with Stage(r"copy", r"REDD17 v16.0.23.24", prog_num=64367):  # 0m:0.168s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64368) as should_copy_source_1156_64368:  # 0m:0.167s
                    should_copy_source_1156_64368()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=64369):  # 0m:0.167s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=64370) as copy_dir_to_dir_1157_64370:  # 0m:0.002s
                            copy_dir_to_dir_1157_64370()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=64371) as unwtar_1158_64371:  # 0m:0.164s
                            unwtar_1158_64371()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD17.bundle", user_id=-1, group_id=-1, prog_num=64372, recursive=True) as chown_1159_64372:  # 0m:0.000s
                            chown_1159_64372()
            with Stage(r"copy", r"REDD37-51 v16.0.23.24", prog_num=64373):  # 0m:0.167s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64374) as should_copy_source_1160_64374:  # 0m:0.167s
                    should_copy_source_1160_64374()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=64375):  # 0m:0.166s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=64376) as copy_dir_to_dir_1161_64376:  # 0m:0.002s
                            copy_dir_to_dir_1161_64376()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=64377) as unwtar_1162_64377:  # 0m:0.164s
                            unwtar_1162_64377()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=64378, recursive=True) as chown_1163_64378:  # 0m:0.000s
                            chown_1163_64378()
            with Stage(r"copy", r"REQ v16.0.23.24", prog_num=64379):  # 0m:0.286s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64380) as should_copy_source_1164_64380:  # 0m:0.286s
                    should_copy_source_1164_64380()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=64381):  # 0m:0.286s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=64382) as copy_dir_to_dir_1165_64382:  # 0m:0.002s
                            copy_dir_to_dir_1165_64382()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=64383) as unwtar_1166_64383:  # 0m:0.284s
                            unwtar_1166_64383()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REQ.bundle", user_id=-1, group_id=-1, prog_num=64384, recursive=True) as chown_1167_64384:  # 0m:0.000s
                            chown_1167_64384()
            with Stage(r"copy", r"RS56 v16.0.23.24", prog_num=64385):  # 0m:0.910s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64386) as should_copy_source_1168_64386:  # 0m:0.910s
                    should_copy_source_1168_64386()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=64387):  # 0m:0.910s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=64388) as copy_dir_to_dir_1169_64388:  # 0m:0.002s
                            copy_dir_to_dir_1169_64388()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=64389) as unwtar_1170_64389:  # 0m:0.907s
                            unwtar_1170_64389()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RS56.bundle", user_id=-1, group_id=-1, prog_num=64390, recursive=True) as chown_1171_64390:  # 0m:0.000s
                            chown_1171_64390()
            with Stage(r"copy", r"RVerb v16.0.23.24", prog_num=64391):  # 0m:0.207s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64392) as should_copy_source_1172_64392:  # 0m:0.207s
                    should_copy_source_1172_64392()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=64393):  # 0m:0.207s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=64394) as copy_dir_to_dir_1173_64394:  # 0m:0.003s
                            copy_dir_to_dir_1173_64394()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=64395) as unwtar_1174_64395:  # 0m:0.204s
                            unwtar_1174_64395()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVerb.bundle", user_id=-1, group_id=-1, prog_num=64396, recursive=True) as chown_1175_64396:  # 0m:0.000s
                            chown_1175_64396()
            with Stage(r"copy", r"RVox v16.0.23.24", prog_num=64397):  # 0m:0.162s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64398) as should_copy_source_1176_64398:  # 0m:0.162s
                    should_copy_source_1176_64398()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=64399):  # 0m:0.161s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=64400) as copy_dir_to_dir_1177_64400:  # 0m:0.002s
                            copy_dir_to_dir_1177_64400()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=64401) as unwtar_1178_64401:  # 0m:0.159s
                            unwtar_1178_64401()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVox.bundle", user_id=-1, group_id=-1, prog_num=64402, recursive=True) as chown_1179_64402:  # 0m:0.000s
                            chown_1179_64402()
            with Stage(r"copy", r"Reel ADT v16.0.23.24", prog_num=64403):  # 0m:0.914s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64404) as should_copy_source_1180_64404:  # 0m:0.914s
                    should_copy_source_1180_64404()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=64405):  # 0m:0.914s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=64406) as copy_dir_to_dir_1181_64406:  # 0m:0.002s
                            copy_dir_to_dir_1181_64406()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=64407) as unwtar_1182_64407:  # 0m:0.910s
                            unwtar_1182_64407()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=64408, recursive=True) as chown_1183_64408:  # 0m:0.002s
                            chown_1183_64408()
            with Stage(r"copy", r"RenAxx v16.0.23.24", prog_num=64409):  # 0m:0.105s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64410) as should_copy_source_1184_64410:  # 0m:0.104s
                    should_copy_source_1184_64410()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=64411):  # 0m:0.104s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=64412) as copy_dir_to_dir_1185_64412:  # 0m:0.002s
                            copy_dir_to_dir_1185_64412()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=64413) as unwtar_1186_64413:  # 0m:0.101s
                            unwtar_1186_64413()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=64414, recursive=True) as chown_1187_64414:  # 0m:0.000s
                            chown_1187_64414()
            with Stage(r"copy", r"Retro Fi v16.0.23.24", prog_num=64415):  # 0m:1.364s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64416) as should_copy_source_1188_64416:  # 0m:1.364s
                    should_copy_source_1188_64416()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=64417):  # 0m:1.364s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=64418) as copy_dir_to_dir_1189_64418:  # 0m:0.021s
                            copy_dir_to_dir_1189_64418()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=64419) as unwtar_1190_64419:  # 0m:1.342s
                            unwtar_1190_64419()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=64420, recursive=True) as chown_1191_64420:  # 0m:0.000s
                            chown_1191_64420()
            with Stage(r"copy", r"S1 v16.0.23.24", prog_num=64421):  # 0m:0.084s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64422) as should_copy_source_1192_64422:  # 0m:0.084s
                    should_copy_source_1192_64422()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=64423):  # 0m:0.084s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=64424) as copy_dir_to_dir_1193_64424:  # 0m:0.002s
                            copy_dir_to_dir_1193_64424()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=64425) as unwtar_1194_64425:  # 0m:0.082s
                            unwtar_1194_64425()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S1.bundle", user_id=-1, group_id=-1, prog_num=64426, recursive=True) as chown_1195_64426:  # 0m:0.000s
                            chown_1195_64426()
            with Stage(r"copy", r"S360 v16.0.23.24", prog_num=64427):  # 0m:0.081s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64428) as should_copy_source_1196_64428:  # 0m:0.081s
                    should_copy_source_1196_64428()
                    with Stage(r"copy source", r"Mac/Plugins/S360.bundle", prog_num=64429):  # 0m:0.081s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", r".", delete_extraneous_files=True, prog_num=64430) as copy_dir_to_dir_1197_64430:  # 0m:0.002s
                            copy_dir_to_dir_1197_64430()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", where_to_unwtar=r".", prog_num=64431) as unwtar_1198_64431:  # 0m:0.078s
                            unwtar_1198_64431()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S360.bundle", user_id=-1, group_id=-1, prog_num=64432, recursive=True) as chown_1199_64432:  # 0m:0.000s
                            chown_1199_64432()
            with Stage(r"copy", r"SSL E-Channel v16.0.23.24", prog_num=64433):  # 0m:0.095s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64434) as should_copy_source_1200_64434:  # 0m:0.095s
                    should_copy_source_1200_64434()
                    with Stage(r"copy source", r"Mac/Plugins/SSL E-Channel.bundle", prog_num=64435):  # 0m:0.094s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", r".", delete_extraneous_files=True, prog_num=64436) as copy_dir_to_dir_1201_64436:  # 0m:0.002s
                            copy_dir_to_dir_1201_64436()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", where_to_unwtar=r".", prog_num=64437) as unwtar_1202_64437:  # 0m:0.092s
                            unwtar_1202_64437()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL E-Channel.bundle", user_id=-1, group_id=-1, prog_num=64438, recursive=True) as chown_1203_64438:  # 0m:0.000s
                            chown_1203_64438()
            with Stage(r"copy", r"SSLComp v16.0.23.24", prog_num=64439):  # 0m:0.084s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64440) as should_copy_source_1204_64440:  # 0m:0.083s
                    should_copy_source_1204_64440()
                    with Stage(r"copy source", r"Mac/Plugins/SSLComp.bundle", prog_num=64441):  # 0m:0.083s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", r".", delete_extraneous_files=True, prog_num=64442) as copy_dir_to_dir_1205_64442:  # 0m:0.002s
                            copy_dir_to_dir_1205_64442()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", where_to_unwtar=r".", prog_num=64443) as unwtar_1206_64443:  # 0m:0.081s
                            unwtar_1206_64443()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSLComp.bundle", user_id=-1, group_id=-1, prog_num=64444, recursive=True) as chown_1207_64444:  # 0m:0.000s
                            chown_1207_64444()
            with Stage(r"copy", r"SSLEQ v16.0.23.24", prog_num=64445):  # 0m:0.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64446) as should_copy_source_1208_64446:  # 0m:0.074s
                    should_copy_source_1208_64446()
                    with Stage(r"copy source", r"Mac/Plugins/SSLEQ.bundle", prog_num=64447):  # 0m:0.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", r".", delete_extraneous_files=True, prog_num=64448) as copy_dir_to_dir_1209_64448:  # 0m:0.002s
                            copy_dir_to_dir_1209_64448()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", where_to_unwtar=r".", prog_num=64449) as unwtar_1210_64449:  # 0m:0.071s
                            unwtar_1210_64449()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSLEQ.bundle", user_id=-1, group_id=-1, prog_num=64450, recursive=True) as chown_1211_64450:  # 0m:0.000s
                            chown_1211_64450()
            with Stage(r"copy", r"SSL EV2 Channel v16.0.23.24", prog_num=64451):  # 0m:0.572s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64452) as should_copy_source_1212_64452:  # 0m:0.572s
                    should_copy_source_1212_64452()
                    with Stage(r"copy source", r"Mac/Plugins/SSL EV2 Channel.bundle", prog_num=64453):  # 0m:0.571s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", r".", delete_extraneous_files=True, prog_num=64454) as copy_dir_to_dir_1213_64454:  # 0m:0.011s
                            copy_dir_to_dir_1213_64454()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", where_to_unwtar=r".", prog_num=64455) as unwtar_1214_64455:  # 0m:0.560s
                            unwtar_1214_64455()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL EV2 Channel.bundle", user_id=-1, group_id=-1, prog_num=64456, recursive=True) as chown_1215_64456:  # 0m:0.000s
                            chown_1215_64456()
            with Stage(r"copy", r"SSL G-Channel v16.0.23.24", prog_num=64457):  # 0m:0.097s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64458) as should_copy_source_1216_64458:  # 0m:0.097s
                    should_copy_source_1216_64458()
                    with Stage(r"copy source", r"Mac/Plugins/SSL G-Channel.bundle", prog_num=64459):  # 0m:0.097s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", r".", delete_extraneous_files=True, prog_num=64460) as copy_dir_to_dir_1217_64460:  # 0m:0.002s
                            copy_dir_to_dir_1217_64460()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", where_to_unwtar=r".", prog_num=64461) as unwtar_1218_64461:  # 0m:0.094s
                            unwtar_1218_64461()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL G-Channel.bundle", user_id=-1, group_id=-1, prog_num=64462, recursive=True) as chown_1219_64462:  # 0m:0.000s
                            chown_1219_64462()
            with Stage(r"copy", r"Scheps 73 v16.0.23.24", prog_num=64463):  # 0m:0.683s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64464) as should_copy_source_1220_64464:  # 0m:0.683s
                    should_copy_source_1220_64464()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=64465):  # 0m:0.682s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=64466) as copy_dir_to_dir_1221_64466:  # 0m:0.002s
                            copy_dir_to_dir_1221_64466()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=64467) as unwtar_1222_64467:  # 0m:0.680s
                            unwtar_1222_64467()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=64468, recursive=True) as chown_1223_64468:  # 0m:0.000s
                            chown_1223_64468()
            with Stage(r"copy", r"Scheps Omni Channel v16.0.30.31", prog_num=64469):  # 0m:0.857s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64470) as should_copy_source_1224_64470:  # 0m:0.857s
                    should_copy_source_1224_64470()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=64471):  # 0m:0.857s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=64472) as copy_dir_to_dir_1225_64472:  # 0m:0.020s
                            copy_dir_to_dir_1225_64472()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=64473) as unwtar_1226_64473:  # 0m:0.836s
                            unwtar_1226_64473()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=64474, recursive=True) as chown_1227_64474:  # 0m:0.000s
                            chown_1227_64474()
            with Stage(r"copy", r"Scheps Parallel Particles v16.0.23.24", prog_num=64475):  # 0m:1.206s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64476) as should_copy_source_1228_64476:  # 0m:1.206s
                    should_copy_source_1228_64476()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=64477):  # 0m:1.206s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=64478) as copy_dir_to_dir_1229_64478:  # 0m:0.010s
                            copy_dir_to_dir_1229_64478()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=64479) as unwtar_1230_64479:  # 0m:1.196s
                            unwtar_1230_64479()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=64480, recursive=True) as chown_1231_64480:  # 0m:0.000s
                            chown_1231_64480()
            with Stage(r"copy", r"Sibilance v16.0.23.24", prog_num=64481):  # 0m:0.486s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64482) as should_copy_source_1232_64482:  # 0m:0.486s
                    should_copy_source_1232_64482()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=64483):  # 0m:0.486s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=64484) as copy_dir_to_dir_1233_64484:  # 0m:0.002s
                            copy_dir_to_dir_1233_64484()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=64485) as unwtar_1234_64485:  # 0m:0.483s
                            unwtar_1234_64485()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=64486, recursive=True) as chown_1235_64486:  # 0m:0.000s
                            chown_1235_64486()
            with Stage(r"copy", r"Emo Signal Generator v16.0.23.24", prog_num=64487):  # 0m:0.066s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64488) as should_copy_source_1236_64488:  # 0m:0.066s
                    should_copy_source_1236_64488()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=64489):  # 0m:0.065s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=64490) as copy_dir_to_dir_1237_64490:  # 0m:0.002s
                            copy_dir_to_dir_1237_64490()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=64491) as unwtar_1238_64491:  # 0m:0.063s
                            unwtar_1238_64491()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=64492, recursive=True) as chown_1239_64492:  # 0m:0.000s
                            chown_1239_64492()
            with Stage(r"copy", r"Silk Vocal v16.0.23.24", prog_num=64493):  # 0m:0.283s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64494) as should_copy_source_1240_64494:  # 0m:0.283s
                    should_copy_source_1240_64494()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=64495):  # 0m:0.283s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=64496) as copy_dir_to_dir_1241_64496:  # 0m:0.002s
                            copy_dir_to_dir_1241_64496()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=64497) as unwtar_1242_64497:  # 0m:0.280s
                            unwtar_1242_64497()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=64498, recursive=True) as chown_1243_64498:  # 0m:0.000s
                            chown_1243_64498()
            with Stage(r"copy", r"Smack Attack v16.0.23.24", prog_num=64499):  # 0m:0.159s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64500) as should_copy_source_1244_64500:  # 0m:0.159s
                    should_copy_source_1244_64500()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=64501):  # 0m:0.159s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=64502) as copy_dir_to_dir_1245_64502:  # 0m:0.002s
                            copy_dir_to_dir_1245_64502()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=64503) as unwtar_1246_64503:  # 0m:0.156s
                            unwtar_1246_64503()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=64504, recursive=True) as chown_1247_64504:  # 0m:0.000s
                            chown_1247_64504()
            with Stage(r"copy", r"SoundShifter v16.0.23.24", prog_num=64505):  # 0m:0.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64506) as should_copy_source_1248_64506:  # 0m:0.074s
                    should_copy_source_1248_64506()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=64507):  # 0m:0.073s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=64508) as copy_dir_to_dir_1249_64508:  # 0m:0.002s
                            copy_dir_to_dir_1249_64508()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=64509) as unwtar_1250_64509:  # 0m:0.071s
                            unwtar_1250_64509()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=64510, recursive=True) as chown_1251_64510:  # 0m:0.000s
                            chown_1251_64510()
            with Stage(r"copy", r"Space Rider v16.0.23.24", prog_num=64511):  # 0m:0.143s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64512) as should_copy_source_1252_64512:  # 0m:0.143s
                    should_copy_source_1252_64512()
                    with Stage(r"copy source", r"Mac/Plugins/Space Rider.bundle", prog_num=64513):  # 0m:0.143s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", r".", delete_extraneous_files=True, prog_num=64514) as copy_dir_to_dir_1253_64514:  # 0m:0.002s
                            copy_dir_to_dir_1253_64514()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", where_to_unwtar=r".", prog_num=64515) as unwtar_1254_64515:  # 0m:0.140s
                            unwtar_1254_64515()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Space Rider.bundle", user_id=-1, group_id=-1, prog_num=64516, recursive=True) as chown_1255_64516:  # 0m:0.000s
                            chown_1255_64516()
            with Stage(r"copy", r"Spherix Immersive Compressor v16.0.23.24", prog_num=64517):  # 0m:0.111s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64518) as should_copy_source_1256_64518:  # 0m:0.111s
                    should_copy_source_1256_64518()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=64519):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=64520) as copy_dir_to_dir_1257_64520:  # 0m:0.003s
                            copy_dir_to_dir_1257_64520()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=64521) as unwtar_1258_64521:  # 0m:0.108s
                            unwtar_1258_64521()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=64522, recursive=True) as chown_1259_64522:  # 0m:0.000s
                            chown_1259_64522()
            with Stage(r"copy", r"Spherix Immersive Limiter v16.0.23.24", prog_num=64523):  # 0m:0.108s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64524) as should_copy_source_1260_64524:  # 0m:0.108s
                    should_copy_source_1260_64524()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=64525):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=64526) as copy_dir_to_dir_1261_64526:  # 0m:0.002s
                            copy_dir_to_dir_1261_64526()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=64527) as unwtar_1262_64527:  # 0m:0.105s
                            unwtar_1262_64527()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=64528, recursive=True) as chown_1263_64528:  # 0m:0.000s
                            chown_1263_64528()
            with Stage(r"copy", r"StudioVerse Audio Effects v16.0.30.31", prog_num=64529):  # 0m:1.349s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64530) as should_copy_source_1264_64530:  # 0m:1.349s
                    should_copy_source_1264_64530()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Audio Effects.bundle", prog_num=64531):  # 0m:1.349s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", r".", delete_extraneous_files=True, prog_num=64532) as copy_dir_to_dir_1265_64532:  # 0m:0.009s
                            copy_dir_to_dir_1265_64532()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", where_to_unwtar=r".", prog_num=64533) as unwtar_1266_64533:  # 0m:1.339s
                            unwtar_1266_64533()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/StudioVerse Audio Effects.bundle", user_id=-1, group_id=-1, prog_num=64534, recursive=True) as chown_1267_64534:  # 0m:0.000s
                            chown_1267_64534()
            with Stage(r"copy", r"Sub Align v16.0.23.24", prog_num=64535):  # 0m:0.099s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64536) as should_copy_source_1268_64536:  # 0m:0.098s
                    should_copy_source_1268_64536()
                    with Stage(r"copy source", r"Mac/Plugins/Sub Align.bundle", prog_num=64537):  # 0m:0.098s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", r".", delete_extraneous_files=True, prog_num=64538) as copy_dir_to_dir_1269_64538:  # 0m:0.002s
                            copy_dir_to_dir_1269_64538()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", where_to_unwtar=r".", prog_num=64539) as unwtar_1270_64539:  # 0m:0.096s
                            unwtar_1270_64539()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sub Align.bundle", user_id=-1, group_id=-1, prog_num=64540, recursive=True) as chown_1271_64540:  # 0m:0.000s
                            chown_1271_64540()
            with Stage(r"copy", r"SuperTap v16.0.23.24", prog_num=64541):  # 0m:0.223s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64542) as should_copy_source_1272_64542:  # 0m:0.223s
                    should_copy_source_1272_64542()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=64543):  # 0m:0.223s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=64544) as copy_dir_to_dir_1273_64544:  # 0m:0.003s
                            copy_dir_to_dir_1273_64544()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=64545) as unwtar_1274_64545:  # 0m:0.220s
                            unwtar_1274_64545()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=64546, recursive=True) as chown_1275_64546:  # 0m:0.000s
                            chown_1275_64546()
            with Stage(r"copy", r"Sync Vx v16.0.23.24", prog_num=64547):  # 0m:0.849s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64548) as should_copy_source_1276_64548:  # 0m:0.849s
                    should_copy_source_1276_64548()
                    with Stage(r"copy source", r"Mac/Plugins/Sync Vx.bundle", prog_num=64549):  # 0m:0.849s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r".", delete_extraneous_files=True, prog_num=64550) as copy_dir_to_dir_1277_64550:  # 0m:0.004s
                            copy_dir_to_dir_1277_64550()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", where_to_unwtar=r".", prog_num=64551) as unwtar_1278_64551:  # 0m:0.844s
                            unwtar_1278_64551()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sync Vx.bundle", user_id=-1, group_id=-1, prog_num=64552, recursive=True) as chown_1279_64552:  # 0m:0.000s
                            chown_1279_64552()
            with Stage(r"copy", r"TG12345 v16.0.23.24", prog_num=64553):  # 0m:0.684s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64554) as should_copy_source_1280_64554:  # 0m:0.684s
                    should_copy_source_1280_64554()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=64555):  # 0m:0.684s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=64556) as copy_dir_to_dir_1281_64556:  # 0m:0.002s
                            copy_dir_to_dir_1281_64556()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=64557) as unwtar_1282_64557:  # 0m:0.681s
                            unwtar_1282_64557()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TG12345.bundle", user_id=-1, group_id=-1, prog_num=64558, recursive=True) as chown_1283_64558:  # 0m:0.000s
                            chown_1283_64558()
            with Stage(r"copy", r"AR TG Meter Bridge v16.0.23.24", prog_num=64559):  # 0m:0.135s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64560) as should_copy_source_1284_64560:  # 0m:0.134s
                    should_copy_source_1284_64560()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=64561):  # 0m:0.134s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=64562) as copy_dir_to_dir_1285_64562:  # 0m:0.002s
                            copy_dir_to_dir_1285_64562()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=64563) as unwtar_1286_64563:  # 0m:0.132s
                            unwtar_1286_64563()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=64564, recursive=True) as chown_1287_64564:  # 0m:0.000s
                            chown_1287_64564()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v16.0.23.24", prog_num=64565):  # 0m:0.922s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64566) as should_copy_source_1288_64566:  # 0m:0.921s
                    should_copy_source_1288_64566()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=64567):  # 0m:0.921s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=64568) as copy_dir_to_dir_1289_64568:  # 0m:0.016s
                            copy_dir_to_dir_1289_64568()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=64569) as unwtar_1290_64569:  # 0m:0.905s
                            unwtar_1290_64569()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=64570, recursive=True) as chown_1291_64570:  # 0m:0.000s
                            chown_1291_64570()
            with Stage(r"copy", r"TRACT v16.0.23.24", prog_num=64571):  # 0m:0.212s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64572) as should_copy_source_1292_64572:  # 0m:0.212s
                    should_copy_source_1292_64572()
                    with Stage(r"copy source", r"Mac/Plugins/TRACT.bundle", prog_num=64573):  # 0m:0.212s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", r".", delete_extraneous_files=True, prog_num=64574) as copy_dir_to_dir_1293_64574:  # 0m:0.002s
                            copy_dir_to_dir_1293_64574()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", where_to_unwtar=r".", prog_num=64575) as unwtar_1294_64575:  # 0m:0.209s
                            unwtar_1294_64575()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TRACT.bundle", user_id=-1, group_id=-1, prog_num=64576, recursive=True) as chown_1295_64576:  # 0m:0.000s
                            chown_1295_64576()
            with Stage(r"copy", r"Torque v16.0.23.24", prog_num=64577):  # 0m:0.132s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64578) as should_copy_source_1296_64578:  # 0m:0.132s
                    should_copy_source_1296_64578()
                    with Stage(r"copy source", r"Mac/Plugins/Torque.bundle", prog_num=64579):  # 0m:0.131s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", r".", delete_extraneous_files=True, prog_num=64580) as copy_dir_to_dir_1297_64580:  # 0m:0.002s
                            copy_dir_to_dir_1297_64580()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", where_to_unwtar=r".", prog_num=64581) as unwtar_1298_64581:  # 0m:0.129s
                            unwtar_1298_64581()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Torque.bundle", user_id=-1, group_id=-1, prog_num=64582, recursive=True) as chown_1299_64582:  # 0m:0.000s
                            chown_1299_64582()
            with Stage(r"copy", r"TransX v16.0.23.24", prog_num=64583):  # 0m:0.068s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64584) as should_copy_source_1300_64584:  # 0m:0.068s
                    should_copy_source_1300_64584()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=64585):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=64586) as copy_dir_to_dir_1301_64586:  # 0m:0.002s
                            copy_dir_to_dir_1301_64586()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=64587) as unwtar_1302_64587:  # 0m:0.066s
                            unwtar_1302_64587()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TransX.bundle", user_id=-1, group_id=-1, prog_num=64588, recursive=True) as chown_1303_64588:  # 0m:0.000s
                            chown_1303_64588()
            with Stage(r"copy", r"TrueVerb v16.0.23.24", prog_num=64589):  # 0m:0.076s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64590) as should_copy_source_1304_64590:  # 0m:0.076s
                    should_copy_source_1304_64590()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=64591):  # 0m:0.076s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=64592) as copy_dir_to_dir_1305_64592:  # 0m:0.002s
                            copy_dir_to_dir_1305_64592()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=64593) as unwtar_1306_64593:  # 0m:0.073s
                            unwtar_1306_64593()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=64594, recursive=True) as chown_1307_64594:  # 0m:0.000s
                            chown_1307_64594()
            with Stage(r"copy", r"UM v16.0.23.24", prog_num=64595):  # 0m:0.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64596) as should_copy_source_1308_64596:  # 0m:0.074s
                    should_copy_source_1308_64596()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=64597):  # 0m:0.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=64598) as copy_dir_to_dir_1309_64598:  # 0m:0.002s
                            copy_dir_to_dir_1309_64598()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=64599) as unwtar_1310_64599:  # 0m:0.072s
                            unwtar_1310_64599()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UM.bundle", user_id=-1, group_id=-1, prog_num=64600, recursive=True) as chown_1311_64600:  # 0m:0.000s
                            chown_1311_64600()
            with Stage(r"copy", r"UltraPitch v16.0.23.24", prog_num=64601):  # 0m:0.087s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64602) as should_copy_source_1312_64602:  # 0m:0.087s
                    should_copy_source_1312_64602()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=64603):  # 0m:0.087s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=64604) as copy_dir_to_dir_1313_64604:  # 0m:0.002s
                            copy_dir_to_dir_1313_64604()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=64605) as unwtar_1314_64605:  # 0m:0.085s
                            unwtar_1314_64605()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=64606, recursive=True) as chown_1315_64606:  # 0m:0.000s
                            chown_1315_64606()
            with Stage(r"copy", r"VComp v16.0.23.24", prog_num=64607):  # 0m:0.515s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64608) as should_copy_source_1316_64608:  # 0m:0.515s
                    should_copy_source_1316_64608()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=64609):  # 0m:0.515s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=64610) as copy_dir_to_dir_1317_64610:  # 0m:0.003s
                            copy_dir_to_dir_1317_64610()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=64611) as unwtar_1318_64611:  # 0m:0.512s
                            unwtar_1318_64611()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VComp.bundle", user_id=-1, group_id=-1, prog_num=64612, recursive=True) as chown_1319_64612:  # 0m:0.000s
                            chown_1319_64612()
            with Stage(r"copy", r"VEQ3 v16.0.23.24", prog_num=64613):  # 0m:0.377s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64614) as should_copy_source_1320_64614:  # 0m:0.376s
                    should_copy_source_1320_64614()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=64615):  # 0m:0.376s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=64616) as copy_dir_to_dir_1321_64616:  # 0m:0.002s
                            copy_dir_to_dir_1321_64616()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=64617) as unwtar_1322_64617:  # 0m:0.374s
                            unwtar_1322_64617()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=64618, recursive=True) as chown_1323_64618:  # 0m:0.000s
                            chown_1323_64618()
            with Stage(r"copy", r"VEQ4 v16.0.23.24", prog_num=64619):  # 0m:0.382s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64620) as should_copy_source_1324_64620:  # 0m:0.382s
                    should_copy_source_1324_64620()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=64621):  # 0m:0.382s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=64622) as copy_dir_to_dir_1325_64622:  # 0m:0.002s
                            copy_dir_to_dir_1325_64622()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=64623) as unwtar_1326_64623:  # 0m:0.379s
                            unwtar_1326_64623()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=64624, recursive=True) as chown_1327_64624:  # 0m:0.000s
                            chown_1327_64624()
            with Stage(r"copy", r"VU Meter v16.0.23.24", prog_num=64625):  # 0m:1.892s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64626) as should_copy_source_1328_64626:  # 0m:1.892s
                    should_copy_source_1328_64626()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=64627):  # 0m:1.892s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=64628) as copy_dir_to_dir_1329_64628:  # 0m:0.002s
                            copy_dir_to_dir_1329_64628()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=64629) as unwtar_1330_64629:  # 0m:1.890s
                            unwtar_1330_64629()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=64630, recursive=True) as chown_1331_64630:  # 0m:0.000s
                            chown_1331_64630()
            with Stage(r"copy", r"Vitamin v16.0.23.24", prog_num=64631):  # 0m:0.068s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64632) as should_copy_source_1332_64632:  # 0m:0.068s
                    should_copy_source_1332_64632()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=64633):  # 0m:0.068s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=64634) as copy_dir_to_dir_1333_64634:  # 0m:0.002s
                            copy_dir_to_dir_1333_64634()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=64635) as unwtar_1334_64635:  # 0m:0.065s
                            unwtar_1334_64635()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=64636, recursive=True) as chown_1335_64636:  # 0m:0.000s
                            chown_1335_64636()
            with Stage(r"copy", r"Vocal Bender v16.0.23.24", prog_num=64637):  # 0m:0.294s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64638) as should_copy_source_1336_64638:  # 0m:0.294s
                    should_copy_source_1336_64638()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Bender.bundle", prog_num=64639):  # 0m:0.294s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", r".", delete_extraneous_files=True, prog_num=64640) as copy_dir_to_dir_1337_64640:  # 0m:0.003s
                            copy_dir_to_dir_1337_64640()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", where_to_unwtar=r".", prog_num=64641) as unwtar_1338_64641:  # 0m:0.291s
                            unwtar_1338_64641()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Bender.bundle", user_id=-1, group_id=-1, prog_num=64642, recursive=True) as chown_1339_64642:  # 0m:0.000s
                            chown_1339_64642()
            with Stage(r"copy", r"Vocal Rider v16.0.23.24", prog_num=64643):  # 0m:0.066s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64644) as should_copy_source_1340_64644:  # 0m:0.066s
                    should_copy_source_1340_64644()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=64645):  # 0m:0.065s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=64646) as copy_dir_to_dir_1341_64646:  # 0m:0.002s
                            copy_dir_to_dir_1341_64646()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=64647) as unwtar_1342_64647:  # 0m:0.063s
                            unwtar_1342_64647()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=64648, recursive=True) as chown_1343_64648:  # 0m:0.000s
                            chown_1343_64648()
            with Stage(r"copy", r"Voltage Amps Bass v16.0.23.24", prog_num=64649):  # 0m:0.815s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64650) as should_copy_source_1344_64650:  # 0m:0.815s
                    should_copy_source_1344_64650()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=64651):  # 0m:0.815s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=64652) as copy_dir_to_dir_1345_64652:  # 0m:0.018s
                            copy_dir_to_dir_1345_64652()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=64653) as unwtar_1346_64653:  # 0m:0.797s
                            unwtar_1346_64653()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=64654, recursive=True) as chown_1347_64654:  # 0m:0.000s
                            chown_1347_64654()
            with Stage(r"copy", r"Voltage Amps Guitar v16.0.23.24", prog_num=64655):  # 0m:0.917s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64656) as should_copy_source_1348_64656:  # 0m:0.917s
                    should_copy_source_1348_64656()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=64657):  # 0m:0.917s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=64658) as copy_dir_to_dir_1349_64658:  # 0m:0.017s
                            copy_dir_to_dir_1349_64658()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=64659) as unwtar_1350_64659:  # 0m:0.899s
                            unwtar_1350_64659()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=64660, recursive=True) as chown_1351_64660:  # 0m:0.000s
                            chown_1351_64660()
            with Stage(r"copy", r"W43 v16.0.23.24", prog_num=64661):  # 0m:0.071s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64662) as should_copy_source_1352_64662:  # 0m:0.071s
                    should_copy_source_1352_64662()
                    with Stage(r"copy source", r"Mac/Plugins/W43.bundle", prog_num=64663):  # 0m:0.071s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", r".", delete_extraneous_files=True, prog_num=64664) as copy_dir_to_dir_1353_64664:  # 0m:0.002s
                            copy_dir_to_dir_1353_64664()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", where_to_unwtar=r".", prog_num=64665) as unwtar_1354_64665:  # 0m:0.068s
                            unwtar_1354_64665()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/W43.bundle", user_id=-1, group_id=-1, prog_num=64666, recursive=True) as chown_1355_64666:  # 0m:0.000s
                            chown_1355_64666()
            with Stage(r"copy", r"WLM v16.0.23.24", prog_num=64667):  # 0m:0.143s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64668) as should_copy_source_1356_64668:  # 0m:0.143s
                    should_copy_source_1356_64668()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=64669):  # 0m:0.143s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=64670) as copy_dir_to_dir_1357_64670:  # 0m:0.002s
                            copy_dir_to_dir_1357_64670()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=64671) as unwtar_1358_64671:  # 0m:0.140s
                            unwtar_1358_64671()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM.bundle", user_id=-1, group_id=-1, prog_num=64672, recursive=True) as chown_1359_64672:  # 0m:0.000s
                            chown_1359_64672()
            with Stage(r"copy", r"WLM Plus v16.0.23.24", prog_num=64673):  # 0m:0.140s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64674) as should_copy_source_1360_64674:  # 0m:0.140s
                    should_copy_source_1360_64674()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=64675):  # 0m:0.140s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=64676) as copy_dir_to_dir_1361_64676:  # 0m:0.002s
                            copy_dir_to_dir_1361_64676()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=64677) as unwtar_1362_64677:  # 0m:0.137s
                            unwtar_1362_64677()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=64678, recursive=True) as chown_1363_64678:  # 0m:0.000s
                            chown_1363_64678()
            with Stage(r"copy", r"WNS v16.0.23.24", prog_num=64679):  # 0m:0.093s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64680) as should_copy_source_1364_64680:  # 0m:0.093s
                    should_copy_source_1364_64680()
                    with Stage(r"copy source", r"Mac/Plugins/WNS.bundle", prog_num=64681):  # 0m:0.093s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", r".", delete_extraneous_files=True, prog_num=64682) as copy_dir_to_dir_1365_64682:  # 0m:0.008s
                            copy_dir_to_dir_1365_64682()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", where_to_unwtar=r".", prog_num=64683) as unwtar_1366_64683:  # 0m:0.084s
                            unwtar_1366_64683()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WNS.bundle", user_id=-1, group_id=-1, prog_num=64684, recursive=True) as chown_1367_64684:  # 0m:0.000s
                            chown_1367_64684()
            with Stage(r"copy", r"WavesHeadTracker v16.0.23.24", prog_num=64685):  # 0m:2.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=5, prog_num=64686) as should_copy_source_1368_64686:  # 0m:2.009s
                    should_copy_source_1368_64686()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=64687):  # 0m:2.009s
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=64688) as rm_file_or_dir_1369_64688:  # 0m:0.000s
                            rm_file_or_dir_1369_64688()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=64689) as copy_dir_to_dir_1370_64689:  # 0m:0.003s
                            copy_dir_to_dir_1370_64689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=64690) as unwtar_1371_64690:  # 0m:2.006s
                            unwtar_1371_64690()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=64691, recursive=True) as chown_1372_64691:  # 0m:0.000s
                            chown_1372_64691()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=64692):  # 0m:0.327s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64693) as should_copy_source_1373_64693:  # 0m:0.327s
                    should_copy_source_1373_64693()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=64694):  # 0m:0.327s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=64695) as copy_dir_to_dir_1374_64695:  # 0m:0.001s
                            copy_dir_to_dir_1374_64695()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=64696) as unwtar_1375_64696:  # 0m:0.325s
                            unwtar_1375_64696()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=64697, recursive=True) as chown_1376_64697:  # 0m:0.000s
                            chown_1376_64697()
            with Stage(r"copy", r"WavesLib1_16_0_30_31 v16.0.30.31", prog_num=64698):  # 0m:0.324s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64699) as should_copy_source_1377_64699:  # 0m:0.324s
                    should_copy_source_1377_64699()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.30.framework", prog_num=64700):  # 0m:0.324s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r".", delete_extraneous_files=True, prog_num=64701) as copy_dir_to_dir_1378_64701:  # 0m:0.002s
                            copy_dir_to_dir_1378_64701()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", where_to_unwtar=r".", prog_num=64702) as unwtar_1379_64702:  # 0m:0.322s
                            unwtar_1379_64702()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.30.framework", user_id=-1, group_id=-1, prog_num=64703, recursive=True) as chown_1380_64703:  # 0m:0.000s
                            chown_1380_64703()
            with Stage(r"copy", r"Waves Stream v16.0.23.24", prog_num=64704):  # 0m:0.756s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64705) as should_copy_source_1381_64705:  # 0m:0.756s
                    should_copy_source_1381_64705()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Stream.bundle", prog_num=64706):  # 0m:0.756s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", r".", delete_extraneous_files=True, prog_num=64707) as copy_dir_to_dir_1382_64707:  # 0m:0.002s
                            copy_dir_to_dir_1382_64707()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", where_to_unwtar=r".", prog_num=64708) as unwtar_1383_64708:  # 0m:0.753s
                            unwtar_1383_64708()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Stream.bundle", user_id=-1, group_id=-1, prog_num=64709, recursive=True) as chown_1384_64709:  # 0m:0.000s
                            chown_1384_64709()
            with Stage(r"copy", r"WavesTune v16.0.23.24", prog_num=64710):  # 0m:0.108s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64711) as should_copy_source_1385_64711:  # 0m:0.108s
                    should_copy_source_1385_64711()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=64712):  # 0m:0.108s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=64713) as copy_dir_to_dir_1386_64713:  # 0m:0.003s
                            copy_dir_to_dir_1386_64713()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=64714) as unwtar_1387_64714:  # 0m:0.105s
                            unwtar_1387_64714()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=64715, recursive=True) as chown_1388_64715:  # 0m:0.000s
                            chown_1388_64715()
            with Stage(r"copy", r"WavesTune LT v16.0.23.24", prog_num=64716):  # 0m:0.106s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64717) as should_copy_source_1389_64717:  # 0m:0.106s
                    should_copy_source_1389_64717()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=64718):  # 0m:0.106s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=64719) as copy_dir_to_dir_1390_64719:  # 0m:0.002s
                            copy_dir_to_dir_1390_64719()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=64720) as unwtar_1391_64720:  # 0m:0.103s
                            unwtar_1391_64720()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=64721, recursive=True) as chown_1392_64721:  # 0m:0.000s
                            chown_1392_64721()
            with Stage(r"copy", r"Waves Harmony v16.0.23.24", prog_num=64722):  # 0m:0.348s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64723) as should_copy_source_1393_64723:  # 0m:0.347s
                    should_copy_source_1393_64723()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=64724):  # 0m:0.347s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=64725) as copy_dir_to_dir_1394_64725:  # 0m:0.003s
                            copy_dir_to_dir_1394_64725()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=64726) as unwtar_1395_64726:  # 0m:0.344s
                            unwtar_1395_64726()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=64727, recursive=True) as chown_1396_64727:  # 0m:0.000s
                            chown_1396_64727()
            with Stage(r"copy", r"Waves Tune Real-Time v16.0.23.24", prog_num=64728):  # 0m:0.240s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64729) as should_copy_source_1397_64729:  # 0m:0.240s
                    should_copy_source_1397_64729()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=64730):  # 0m:0.239s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=64731) as copy_dir_to_dir_1398_64731:  # 0m:0.003s
                            copy_dir_to_dir_1398_64731()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=64732) as unwtar_1399_64732:  # 0m:0.236s
                            unwtar_1399_64732()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=64733, recursive=True) as chown_1400_64733:  # 0m:0.000s
                            chown_1400_64733()
            with Stage(r"copy", r"X-Click v16.0.23.24", prog_num=64734):  # 0m:0.062s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64735) as should_copy_source_1401_64735:  # 0m:0.062s
                    should_copy_source_1401_64735()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=64736):  # 0m:0.062s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=64737) as copy_dir_to_dir_1402_64737:  # 0m:0.002s
                            copy_dir_to_dir_1402_64737()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=64738) as unwtar_1403_64738:  # 0m:0.060s
                            unwtar_1403_64738()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Click.bundle", user_id=-1, group_id=-1, prog_num=64739, recursive=True) as chown_1404_64739:  # 0m:0.000s
                            chown_1404_64739()
            with Stage(r"copy", r"X-Crackle v16.0.23.24", prog_num=64740):  # 0m:0.059s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64741) as should_copy_source_1405_64741:  # 0m:0.059s
                    should_copy_source_1405_64741()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=64742):  # 0m:0.059s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=64743) as copy_dir_to_dir_1406_64743:  # 0m:0.002s
                            copy_dir_to_dir_1406_64743()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=64744) as unwtar_1407_64744:  # 0m:0.056s
                            unwtar_1407_64744()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=64745, recursive=True) as chown_1408_64745:  # 0m:0.000s
                            chown_1408_64745()
            with Stage(r"copy", r"X-FDBK v16.0.23.24", prog_num=64746):  # 0m:0.088s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64747) as should_copy_source_1409_64747:  # 0m:0.087s
                    should_copy_source_1409_64747()
                    with Stage(r"copy source", r"Mac/Plugins/X-FDBK.bundle", prog_num=64748):  # 0m:0.087s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", r".", delete_extraneous_files=True, prog_num=64749) as copy_dir_to_dir_1410_64749:  # 0m:0.002s
                            copy_dir_to_dir_1410_64749()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", where_to_unwtar=r".", prog_num=64750) as unwtar_1411_64750:  # 0m:0.084s
                            unwtar_1411_64750()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-FDBK.bundle", user_id=-1, group_id=-1, prog_num=64751, recursive=True) as chown_1412_64751:  # 0m:0.000s
                            chown_1412_64751()
            with Stage(r"copy", r"X-Hum v16.0.23.24", prog_num=64752):  # 0m:0.059s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64753) as should_copy_source_1413_64753:  # 0m:0.059s
                    should_copy_source_1413_64753()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=64754):  # 0m:0.058s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=64755) as copy_dir_to_dir_1414_64755:  # 0m:0.002s
                            copy_dir_to_dir_1414_64755()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=64756) as unwtar_1415_64756:  # 0m:0.056s
                            unwtar_1415_64756()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=64757, recursive=True) as chown_1416_64757:  # 0m:0.000s
                            chown_1416_64757()
            with Stage(r"copy", r"X-Noise v16.0.23.24", prog_num=64758):  # 0m:0.073s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64759) as should_copy_source_1417_64759:  # 0m:0.073s
                    should_copy_source_1417_64759()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=64760):  # 0m:0.073s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=64761) as copy_dir_to_dir_1418_64761:  # 0m:0.002s
                            copy_dir_to_dir_1418_64761()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=64762) as unwtar_1419_64762:  # 0m:0.070s
                            unwtar_1419_64762()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=64763, recursive=True) as chown_1420_64763:  # 0m:0.000s
                            chown_1420_64763()
            with Stage(r"copy", r"Z-Noise v16.0.23.24", prog_num=64764):  # 0m:0.074s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64765) as should_copy_source_1421_64765:  # 0m:0.074s
                    should_copy_source_1421_64765()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=64766):  # 0m:0.074s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=64767) as copy_dir_to_dir_1422_64767:  # 0m:0.002s
                            copy_dir_to_dir_1422_64767()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=64768) as unwtar_1423_64768:  # 0m:0.072s
                            unwtar_1423_64768()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=64769, recursive=True) as chown_1424_64769:  # 0m:0.000s
                            chown_1424_64769()
            with Stage(r"copy", r"dbx-160 v16.0.23.24", prog_num=64770):  # 0m:0.082s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64771) as should_copy_source_1425_64771:  # 0m:0.082s
                    should_copy_source_1425_64771()
                    with Stage(r"copy source", r"Mac/Plugins/dbx-160.bundle", prog_num=64772):  # 0m:0.082s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", r".", delete_extraneous_files=True, prog_num=64773) as copy_dir_to_dir_1426_64773:  # 0m:0.002s
                            copy_dir_to_dir_1426_64773()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", where_to_unwtar=r".", prog_num=64774) as unwtar_1427_64774:  # 0m:0.079s
                            unwtar_1427_64774()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/dbx-160.bundle", user_id=-1, group_id=-1, prog_num=64775, recursive=True) as chown_1428_64775:  # 0m:0.000s
                            chown_1428_64775()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=4, prog_num=64779) as resolve_symlink_files_in_folder_1429_64779:  # 0m:0.309s
                resolve_symlink_files_in_folder_1429_64779()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=64780) as shell_command_1430_64780:  # 0m:0.097s
                shell_command_1430_64780()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=64781) as script_command_1431_64781:  # 0m:0.013s
                script_command_1431_64781()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64782) as shell_command_1432_64782:  # 0m:6.474s
                shell_command_1432_64782()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=64783) as create_symlink_1433_64783:  # 0m:0.001s
                create_symlink_1433_64783()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=64784) as create_symlink_1434_64784:  # 0m:0.001s
                create_symlink_1434_64784()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=64785) as copy_glob_to_dir_1435_64785:  # 0m:0.182s
                copy_glob_to_dir_1435_64785()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=64786) as cd_stage_1436_64786:  # 0m:0.001s
            cd_stage_1436_64786()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=64787):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=64788) as should_copy_source_1437_64788:  # 0m:0.001s
                    should_copy_source_1437_64788()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=64789):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=64790) as copy_file_to_dir_1438_64790:  # 0m:0.001s
                            copy_file_to_dir_1438_64790()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=64791) as chmod_and_chown_1439_64791:  # 0m:0.000s
                            chmod_and_chown_1439_64791()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTR", prog_num=64792) as cd_stage_1440_64792:  # 0m:2.012s
            cd_stage_1440_64792()
            with Stage(r"copy", r"GTR Stomps v16.0.23.24", prog_num=64793):  # 0m:1.286s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64794) as should_copy_source_1441_64794:  # 0m:0.055s
                    should_copy_source_1441_64794()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=64795):  # 0m:0.055s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=64796) as copy_dir_to_dir_1442_64796:  # 0m:0.002s
                            copy_dir_to_dir_1442_64796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=64797) as unwtar_1443_64797:  # 0m:0.053s
                            unwtar_1443_64797()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=64798, recursive=True) as chown_1444_64798:  # 0m:0.000s
                            chown_1444_64798()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64799) as should_copy_source_1445_64799:  # 0m:0.056s
                    should_copy_source_1445_64799()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=64800):  # 0m:0.056s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=64801) as copy_dir_to_dir_1446_64801:  # 0m:0.002s
                            copy_dir_to_dir_1446_64801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=64802) as unwtar_1447_64802:  # 0m:0.053s
                            unwtar_1447_64802()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=64803, recursive=True) as chown_1448_64803:  # 0m:0.000s
                            chown_1448_64803()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64804) as should_copy_source_1449_64804:  # 0m:0.105s
                    should_copy_source_1449_64804()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=64805):  # 0m:0.104s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=64806) as copy_dir_to_dir_1450_64806:  # 0m:0.002s
                            copy_dir_to_dir_1450_64806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=64807) as unwtar_1451_64807:  # 0m:0.102s
                            unwtar_1451_64807()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=64808, recursive=True) as chown_1452_64808:  # 0m:0.000s
                            chown_1452_64808()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64809) as should_copy_source_1453_64809:  # 0m:0.048s
                    should_copy_source_1453_64809()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=64810):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=64811) as copy_dir_to_dir_1454_64811:  # 0m:0.002s
                            copy_dir_to_dir_1454_64811()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=64812) as unwtar_1455_64812:  # 0m:0.046s
                            unwtar_1455_64812()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=64813, recursive=True) as chown_1456_64813:  # 0m:0.000s
                            chown_1456_64813()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64814) as should_copy_source_1457_64814:  # 0m:0.059s
                    should_copy_source_1457_64814()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=64815):  # 0m:0.059s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=64816) as copy_dir_to_dir_1458_64816:  # 0m:0.002s
                            copy_dir_to_dir_1458_64816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=64817) as unwtar_1459_64817:  # 0m:0.057s
                            unwtar_1459_64817()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=64818, recursive=True) as chown_1460_64818:  # 0m:0.000s
                            chown_1460_64818()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64819) as should_copy_source_1461_64819:  # 0m:0.048s
                    should_copy_source_1461_64819()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=64820):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=64821) as copy_dir_to_dir_1462_64821:  # 0m:0.002s
                            copy_dir_to_dir_1462_64821()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=64822) as unwtar_1463_64822:  # 0m:0.046s
                            unwtar_1463_64822()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=64823, recursive=True) as chown_1464_64823:  # 0m:0.000s
                            chown_1464_64823()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64824) as should_copy_source_1465_64824:  # 0m:0.050s
                    should_copy_source_1465_64824()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=64825):  # 0m:0.050s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=64826) as copy_dir_to_dir_1466_64826:  # 0m:0.002s
                            copy_dir_to_dir_1466_64826()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=64827) as unwtar_1467_64827:  # 0m:0.048s
                            unwtar_1467_64827()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=64828, recursive=True) as chown_1468_64828:  # 0m:0.000s
                            chown_1468_64828()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64829) as should_copy_source_1469_64829:  # 0m:0.047s
                    should_copy_source_1469_64829()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=64830):  # 0m:0.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=64831) as copy_dir_to_dir_1470_64831:  # 0m:0.002s
                            copy_dir_to_dir_1470_64831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=64832) as unwtar_1471_64832:  # 0m:0.044s
                            unwtar_1471_64832()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=64833, recursive=True) as chown_1472_64833:  # 0m:0.000s
                            chown_1472_64833()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64834) as should_copy_source_1473_64834:  # 0m:0.048s
                    should_copy_source_1473_64834()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=64835):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64836) as copy_dir_to_dir_1474_64836:  # 0m:0.002s
                            copy_dir_to_dir_1474_64836()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=64837) as unwtar_1475_64837:  # 0m:0.046s
                            unwtar_1475_64837()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=64838, recursive=True) as chown_1476_64838:  # 0m:0.000s
                            chown_1476_64838()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64839) as should_copy_source_1477_64839:  # 0m:0.047s
                    should_copy_source_1477_64839()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=64840):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=64841) as copy_dir_to_dir_1478_64841:  # 0m:0.002s
                            copy_dir_to_dir_1478_64841()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=64842) as unwtar_1479_64842:  # 0m:0.045s
                            unwtar_1479_64842()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=64843, recursive=True) as chown_1480_64843:  # 0m:0.000s
                            chown_1480_64843()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64844) as should_copy_source_1481_64844:  # 0m:0.052s
                    should_copy_source_1481_64844()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=64845):  # 0m:0.051s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=64846) as copy_dir_to_dir_1482_64846:  # 0m:0.002s
                            copy_dir_to_dir_1482_64846()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=64847) as unwtar_1483_64847:  # 0m:0.049s
                            unwtar_1483_64847()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=64848, recursive=True) as chown_1484_64848:  # 0m:0.000s
                            chown_1484_64848()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64849) as should_copy_source_1485_64849:  # 0m:0.047s
                    should_copy_source_1485_64849()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=64850):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=64851) as copy_dir_to_dir_1486_64851:  # 0m:0.002s
                            copy_dir_to_dir_1486_64851()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=64852) as unwtar_1487_64852:  # 0m:0.044s
                            unwtar_1487_64852()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=64853, recursive=True) as chown_1488_64853:  # 0m:0.000s
                            chown_1488_64853()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64854) as should_copy_source_1489_64854:  # 0m:0.050s
                    should_copy_source_1489_64854()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=64855):  # 0m:0.050s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=64856) as copy_dir_to_dir_1490_64856:  # 0m:0.002s
                            copy_dir_to_dir_1490_64856()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=64857) as unwtar_1491_64857:  # 0m:0.047s
                            unwtar_1491_64857()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=64858, recursive=True) as chown_1492_64858:  # 0m:0.000s
                            chown_1492_64858()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64859) as should_copy_source_1493_64859:  # 0m:0.045s
                    should_copy_source_1493_64859()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=64860):  # 0m:0.045s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=64861) as copy_dir_to_dir_1494_64861:  # 0m:0.002s
                            copy_dir_to_dir_1494_64861()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=64862) as unwtar_1495_64862:  # 0m:0.043s
                            unwtar_1495_64862()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=64863, recursive=True) as chown_1496_64863:  # 0m:0.000s
                            chown_1496_64863()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64864) as should_copy_source_1497_64864:  # 0m:0.046s
                    should_copy_source_1497_64864()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=64865):  # 0m:0.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=64866) as copy_dir_to_dir_1498_64866:  # 0m:0.002s
                            copy_dir_to_dir_1498_64866()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=64867) as unwtar_1499_64867:  # 0m:0.044s
                            unwtar_1499_64867()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=64868, recursive=True) as chown_1500_64868:  # 0m:0.000s
                            chown_1500_64868()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64869) as should_copy_source_1501_64869:  # 0m:0.047s
                    should_copy_source_1501_64869()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=64870):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=64871) as copy_dir_to_dir_1502_64871:  # 0m:0.002s
                            copy_dir_to_dir_1502_64871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=64872) as unwtar_1503_64872:  # 0m:0.045s
                            unwtar_1503_64872()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=64873, recursive=True) as chown_1504_64873:  # 0m:0.000s
                            chown_1504_64873()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64874) as should_copy_source_1505_64874:  # 0m:0.050s
                    should_copy_source_1505_64874()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=64875):  # 0m:0.050s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=64876) as copy_dir_to_dir_1506_64876:  # 0m:0.002s
                            copy_dir_to_dir_1506_64876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=64877) as unwtar_1507_64877:  # 0m:0.048s
                            unwtar_1507_64877()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=64878, recursive=True) as chown_1508_64878:  # 0m:0.000s
                            chown_1508_64878()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64879) as should_copy_source_1509_64879:  # 0m:0.045s
                    should_copy_source_1509_64879()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=64880):  # 0m:0.045s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=64881) as copy_dir_to_dir_1510_64881:  # 0m:0.002s
                            copy_dir_to_dir_1510_64881()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=64882) as unwtar_1511_64882:  # 0m:0.042s
                            unwtar_1511_64882()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=64883, recursive=True) as chown_1512_64883:  # 0m:0.000s
                            chown_1512_64883()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64884) as should_copy_source_1513_64884:  # 0m:0.047s
                    should_copy_source_1513_64884()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=64885):  # 0m:0.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=64886) as copy_dir_to_dir_1514_64886:  # 0m:0.002s
                            copy_dir_to_dir_1514_64886()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=64887) as unwtar_1515_64887:  # 0m:0.044s
                            unwtar_1515_64887()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=64888, recursive=True) as chown_1516_64888:  # 0m:0.000s
                            chown_1516_64888()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64889) as should_copy_source_1517_64889:  # 0m:0.048s
                    should_copy_source_1517_64889()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=64890):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=64891) as copy_dir_to_dir_1518_64891:  # 0m:0.002s
                            copy_dir_to_dir_1518_64891()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=64892) as unwtar_1519_64892:  # 0m:0.045s
                            unwtar_1519_64892()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=64893, recursive=True) as chown_1520_64893:  # 0m:0.000s
                            chown_1520_64893()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64894) as should_copy_source_1521_64894:  # 0m:0.048s
                    should_copy_source_1521_64894()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=64895):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=64896) as copy_dir_to_dir_1522_64896:  # 0m:0.002s
                            copy_dir_to_dir_1522_64896()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=64897) as unwtar_1523_64897:  # 0m:0.045s
                            unwtar_1523_64897()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=64898, recursive=True) as chown_1524_64898:  # 0m:0.000s
                            chown_1524_64898()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64899) as should_copy_source_1525_64899:  # 0m:0.050s
                    should_copy_source_1525_64899()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=64900):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=64901) as copy_dir_to_dir_1526_64901:  # 0m:0.002s
                            copy_dir_to_dir_1526_64901()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=64902) as unwtar_1527_64902:  # 0m:0.047s
                            unwtar_1527_64902()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=64903, recursive=True) as chown_1528_64903:  # 0m:0.000s
                            chown_1528_64903()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64904) as should_copy_source_1529_64904:  # 0m:0.050s
                    should_copy_source_1529_64904()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=64905):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=64906) as copy_dir_to_dir_1530_64906:  # 0m:0.002s
                            copy_dir_to_dir_1530_64906()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=64907) as unwtar_1531_64907:  # 0m:0.047s
                            unwtar_1531_64907()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=64908, recursive=True) as chown_1532_64908:  # 0m:0.000s
                            chown_1532_64908()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64909) as should_copy_source_1533_64909:  # 0m:0.049s
                    should_copy_source_1533_64909()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=64910):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=64911) as copy_dir_to_dir_1534_64911:  # 0m:0.002s
                            copy_dir_to_dir_1534_64911()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=64912) as unwtar_1535_64912:  # 0m:0.047s
                            unwtar_1535_64912()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=64913, recursive=True) as chown_1536_64913:  # 0m:0.000s
                            chown_1536_64913()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64914) as should_copy_source_1537_64914:  # 0m:0.049s
                    should_copy_source_1537_64914()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=64915):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=64916) as copy_dir_to_dir_1538_64916:  # 0m:0.002s
                            copy_dir_to_dir_1538_64916()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=64917) as unwtar_1539_64917:  # 0m:0.046s
                            unwtar_1539_64917()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=64918, recursive=True) as chown_1540_64918:  # 0m:0.000s
                            chown_1540_64918()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64919) as shell_command_1541_64919:  # 0m:0.726s
                shell_command_1541_64919()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTRSolo", prog_num=64920) as cd_stage_1542_64920:  # 0m:1.057s
            cd_stage_1542_64920()
            with Stage(r"copy", r"GTR Solo Stomps v16.0.23.24", prog_num=64921):  # 0m:0.673s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64922) as should_copy_source_1543_64922:  # 0m:0.051s
                    should_copy_source_1543_64922()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLChorus.bundle", prog_num=64923):  # 0m:0.051s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", r".", delete_extraneous_files=True, prog_num=64924) as copy_dir_to_dir_1544_64924:  # 0m:0.002s
                            copy_dir_to_dir_1544_64924()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", where_to_unwtar=r".", prog_num=64925) as unwtar_1545_64925:  # 0m:0.048s
                            unwtar_1545_64925()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLChorus.bundle", user_id=-1, group_id=-1, prog_num=64926, recursive=True) as chown_1546_64926:  # 0m:0.000s
                            chown_1546_64926()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64927) as should_copy_source_1547_64927:  # 0m:0.070s
                    should_copy_source_1547_64927()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLDelay.bundle", prog_num=64928):  # 0m:0.070s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", r".", delete_extraneous_files=True, prog_num=64929) as copy_dir_to_dir_1548_64929:  # 0m:0.002s
                            copy_dir_to_dir_1548_64929()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", where_to_unwtar=r".", prog_num=64930) as unwtar_1549_64930:  # 0m:0.068s
                            unwtar_1549_64930()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLDelay.bundle", user_id=-1, group_id=-1, prog_num=64931, recursive=True) as chown_1550_64931:  # 0m:0.000s
                            chown_1550_64931()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64932) as should_copy_source_1551_64932:  # 0m:0.052s
                    should_copy_source_1551_64932()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLDistortion.bundle", prog_num=64933):  # 0m:0.052s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", r".", delete_extraneous_files=True, prog_num=64934) as copy_dir_to_dir_1552_64934:  # 0m:0.002s
                            copy_dir_to_dir_1552_64934()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", where_to_unwtar=r".", prog_num=64935) as unwtar_1553_64935:  # 0m:0.049s
                            unwtar_1553_64935()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLDistortion.bundle", user_id=-1, group_id=-1, prog_num=64936, recursive=True) as chown_1554_64936:  # 0m:0.000s
                            chown_1554_64936()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64937) as should_copy_source_1555_64937:  # 0m:0.050s
                    should_copy_source_1555_64937()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLEQ.bundle", prog_num=64938):  # 0m:0.050s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", r".", delete_extraneous_files=True, prog_num=64939) as copy_dir_to_dir_1556_64939:  # 0m:0.002s
                            copy_dir_to_dir_1556_64939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", where_to_unwtar=r".", prog_num=64940) as unwtar_1557_64940:  # 0m:0.048s
                            unwtar_1557_64940()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLEQ.bundle", user_id=-1, group_id=-1, prog_num=64941, recursive=True) as chown_1558_64941:  # 0m:0.000s
                            chown_1558_64941()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64942) as should_copy_source_1559_64942:  # 0m:0.052s
                    should_copy_source_1559_64942()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLFlanger.bundle", prog_num=64943):  # 0m:0.052s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64944) as copy_dir_to_dir_1560_64944:  # 0m:0.002s
                            copy_dir_to_dir_1560_64944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", where_to_unwtar=r".", prog_num=64945) as unwtar_1561_64945:  # 0m:0.050s
                            unwtar_1561_64945()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLFlanger.bundle", user_id=-1, group_id=-1, prog_num=64946, recursive=True) as chown_1562_64946:  # 0m:0.000s
                            chown_1562_64946()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64947) as should_copy_source_1563_64947:  # 0m:0.048s
                    should_copy_source_1563_64947()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLGateComp.bundle", prog_num=64948):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", r".", delete_extraneous_files=True, prog_num=64949) as copy_dir_to_dir_1564_64949:  # 0m:0.002s
                            copy_dir_to_dir_1564_64949()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", where_to_unwtar=r".", prog_num=64950) as unwtar_1565_64950:  # 0m:0.046s
                            unwtar_1565_64950()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLGateComp.bundle", user_id=-1, group_id=-1, prog_num=64951, recursive=True) as chown_1566_64951:  # 0m:0.000s
                            chown_1566_64951()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64952) as should_copy_source_1567_64952:  # 0m:0.058s
                    should_copy_source_1567_64952()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", prog_num=64953):  # 0m:0.057s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=64954) as copy_dir_to_dir_1568_64954:  # 0m:0.002s
                            copy_dir_to_dir_1568_64954()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", where_to_unwtar=r".", prog_num=64955) as unwtar_1569_64955:  # 0m:0.055s
                            unwtar_1569_64955()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLOverDrive.bundle", user_id=-1, group_id=-1, prog_num=64956, recursive=True) as chown_1570_64956:  # 0m:0.000s
                            chown_1570_64956()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64957) as should_copy_source_1571_64957:  # 0m:0.051s
                    should_copy_source_1571_64957()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLPhaser.bundle", prog_num=64958):  # 0m:0.051s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", r".", delete_extraneous_files=True, prog_num=64959) as copy_dir_to_dir_1572_64959:  # 0m:0.002s
                            copy_dir_to_dir_1572_64959()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", where_to_unwtar=r".", prog_num=64960) as unwtar_1573_64960:  # 0m:0.048s
                            unwtar_1573_64960()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLPhaser.bundle", user_id=-1, group_id=-1, prog_num=64961, recursive=True) as chown_1574_64961:  # 0m:0.000s
                            chown_1574_64961()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64962) as should_copy_source_1575_64962:  # 0m:0.052s
                    should_copy_source_1575_64962()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLPitcher.bundle", prog_num=64963):  # 0m:0.051s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", r".", delete_extraneous_files=True, prog_num=64964) as copy_dir_to_dir_1576_64964:  # 0m:0.002s
                            copy_dir_to_dir_1576_64964()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", where_to_unwtar=r".", prog_num=64965) as unwtar_1577_64965:  # 0m:0.049s
                            unwtar_1577_64965()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLPitcher.bundle", user_id=-1, group_id=-1, prog_num=64966, recursive=True) as chown_1578_64966:  # 0m:0.000s
                            chown_1578_64966()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64967) as should_copy_source_1579_64967:  # 0m:0.049s
                    should_copy_source_1579_64967()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLSpring.bundle", prog_num=64968):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", r".", delete_extraneous_files=True, prog_num=64969) as copy_dir_to_dir_1580_64969:  # 0m:0.002s
                            copy_dir_to_dir_1580_64969()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", where_to_unwtar=r".", prog_num=64970) as unwtar_1581_64970:  # 0m:0.046s
                            unwtar_1581_64970()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLSpring.bundle", user_id=-1, group_id=-1, prog_num=64971, recursive=True) as chown_1582_64971:  # 0m:0.000s
                            chown_1582_64971()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64972) as should_copy_source_1583_64972:  # 0m:0.048s
                    should_copy_source_1583_64972()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", prog_num=64973):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=64974) as copy_dir_to_dir_1584_64974:  # 0m:0.002s
                            copy_dir_to_dir_1584_64974()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", where_to_unwtar=r".", prog_num=64975) as unwtar_1585_64975:  # 0m:0.046s
                            unwtar_1585_64975()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLVibrolo.bundle", user_id=-1, group_id=-1, prog_num=64976, recursive=True) as chown_1586_64976:  # 0m:0.000s
                            chown_1586_64976()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64977) as should_copy_source_1587_64977:  # 0m:0.044s
                    should_copy_source_1587_64977()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLVolume.bundle", prog_num=64978):  # 0m:0.044s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", r".", delete_extraneous_files=True, prog_num=64979) as copy_dir_to_dir_1588_64979:  # 0m:0.002s
                            copy_dir_to_dir_1588_64979()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", where_to_unwtar=r".", prog_num=64980) as unwtar_1589_64980:  # 0m:0.042s
                            unwtar_1589_64980()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLVolume.bundle", user_id=-1, group_id=-1, prog_num=64981, recursive=True) as chown_1590_64981:  # 0m:0.000s
                            chown_1590_64981()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64982) as should_copy_source_1591_64982:  # 0m:0.047s
                    should_copy_source_1591_64982()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLWahWah.bundle", prog_num=64983):  # 0m:0.046s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", r".", delete_extraneous_files=True, prog_num=64984) as copy_dir_to_dir_1592_64984:  # 0m:0.002s
                            copy_dir_to_dir_1592_64984()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", where_to_unwtar=r".", prog_num=64985) as unwtar_1593_64985:  # 0m:0.044s
                            unwtar_1593_64985()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLWahWah.bundle", user_id=-1, group_id=-1, prog_num=64986, recursive=True) as chown_1594_64986:  # 0m:0.000s
                            chown_1594_64986()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64987) as shell_command_1595_64987:  # 0m:0.383s
                shell_command_1595_64987()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/MIDI", prog_num=64988) as cd_stage_1596_64988:  # 0m:0.425s
            cd_stage_1596_64988()
            with Stage(r"copy", r"MidiArpSeq v16.0.23.24", prog_num=64989):  # 0m:0.064s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=64990) as should_copy_source_1597_64990:  # 0m:0.064s
                    should_copy_source_1597_64990()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIArpSeq.bundle", prog_num=64991):  # 0m:0.064s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r".", delete_extraneous_files=True, prog_num=64992) as copy_dir_to_dir_1598_64992:  # 0m:0.003s
                            copy_dir_to_dir_1598_64992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", where_to_unwtar=r".", prog_num=64993) as unwtar_1599_64993:  # 0m:0.060s
                            unwtar_1599_64993()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIArpSeq.bundle", user_id=-1, group_id=-1, prog_num=64994, recursive=True) as chown_1600_64994:  # 0m:0.000s
                            chown_1600_64994()
            with Stage(r"copy", r"MIDIChords v16.0.23.24", prog_num=64995):  # 0m:0.070s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=64996) as should_copy_source_1601_64996:  # 0m:0.069s
                    should_copy_source_1601_64996()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIChords.bundle", prog_num=64997):  # 0m:0.069s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", r".", delete_extraneous_files=True, prog_num=64998) as copy_dir_to_dir_1602_64998:  # 0m:0.002s
                            copy_dir_to_dir_1602_64998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", where_to_unwtar=r".", prog_num=64999) as unwtar_1603_64999:  # 0m:0.067s
                            unwtar_1603_64999()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIChords.bundle", user_id=-1, group_id=-1, prog_num=65000, recursive=True) as chown_1604_65000:  # 0m:0.000s
                            chown_1604_65000()
            with Stage(r"copy", r"MIDIKeyboard v16.0.30.31", prog_num=65001):  # 0m:0.048s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65002) as should_copy_source_1605_65002:  # 0m:0.048s
                    should_copy_source_1605_65002()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIKeyboard.bundle", prog_num=65003):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r".", delete_extraneous_files=True, prog_num=65004) as copy_dir_to_dir_1606_65004:  # 0m:0.002s
                            copy_dir_to_dir_1606_65004()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", where_to_unwtar=r".", prog_num=65005) as unwtar_1607_65005:  # 0m:0.045s
                            unwtar_1607_65005()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIKeyboard.bundle", user_id=-1, group_id=-1, prog_num=65006, recursive=True) as chown_1608_65006:  # 0m:0.000s
                            chown_1608_65006()
            with Stage(r"copy", r"MIDIMonitor v16.0.23.24", prog_num=65007):  # 0m:0.051s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65008) as should_copy_source_1609_65008:  # 0m:0.051s
                    should_copy_source_1609_65008()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIMonitor.bundle", prog_num=65009):  # 0m:0.051s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", r".", delete_extraneous_files=True, prog_num=65010) as copy_dir_to_dir_1610_65010:  # 0m:0.002s
                            copy_dir_to_dir_1610_65010()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", where_to_unwtar=r".", prog_num=65011) as unwtar_1611_65011:  # 0m:0.048s
                            unwtar_1611_65011()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIMonitor.bundle", user_id=-1, group_id=-1, prog_num=65012, recursive=True) as chown_1612_65012:  # 0m:0.000s
                            chown_1612_65012()
            with Stage(r"copy", r"MIDIRange v16.0.23.24", prog_num=65013):  # 0m:0.047s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65014) as should_copy_source_1613_65014:  # 0m:0.047s
                    should_copy_source_1613_65014()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIRange.bundle", prog_num=65015):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", r".", delete_extraneous_files=True, prog_num=65016) as copy_dir_to_dir_1614_65016:  # 0m:0.002s
                            copy_dir_to_dir_1614_65016()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", where_to_unwtar=r".", prog_num=65017) as unwtar_1615_65017:  # 0m:0.045s
                            unwtar_1615_65017()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIRange.bundle", user_id=-1, group_id=-1, prog_num=65018, recursive=True) as chown_1616_65018:  # 0m:0.000s
                            chown_1616_65018()
            with Stage(r"copy", r"MIDITranspose v16.0.23.24", prog_num=65019):  # 0m:0.047s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65020) as should_copy_source_1617_65020:  # 0m:0.047s
                    should_copy_source_1617_65020()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDITranspose.bundle", prog_num=65021):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", r".", delete_extraneous_files=True, prog_num=65022) as copy_dir_to_dir_1618_65022:  # 0m:0.003s
                            copy_dir_to_dir_1618_65022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", where_to_unwtar=r".", prog_num=65023) as unwtar_1619_65023:  # 0m:0.044s
                            unwtar_1619_65023()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDITranspose.bundle", user_id=-1, group_id=-1, prog_num=65024, recursive=True) as chown_1620_65024:  # 0m:0.000s
                            chown_1620_65024()
            with Stage(r"copy", r"MIDIVelocity v16.0.23.24", prog_num=65025):  # 0m:0.049s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65026) as should_copy_source_1621_65026:  # 0m:0.049s
                    should_copy_source_1621_65026()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVelocity.bundle", prog_num=65027):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", r".", delete_extraneous_files=True, prog_num=65028) as copy_dir_to_dir_1622_65028:  # 0m:0.002s
                            copy_dir_to_dir_1622_65028()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", where_to_unwtar=r".", prog_num=65029) as unwtar_1623_65029:  # 0m:0.047s
                            unwtar_1623_65029()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIVelocity.bundle", user_id=-1, group_id=-1, prog_num=65030, recursive=True) as chown_1624_65030:  # 0m:0.000s
                            chown_1624_65030()
            with Stage(r"copy", r"MIDIVoicing v16.0.23.24", prog_num=65031):  # 0m:0.049s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65032) as should_copy_source_1625_65032:  # 0m:0.049s
                    should_copy_source_1625_65032()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVoicing.bundle", prog_num=65033):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", r".", delete_extraneous_files=True, prog_num=65034) as copy_dir_to_dir_1626_65034:  # 0m:0.003s
                            copy_dir_to_dir_1626_65034()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", where_to_unwtar=r".", prog_num=65035) as unwtar_1627_65035:  # 0m:0.045s
                            unwtar_1627_65035()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIVoicing.bundle", user_id=-1, group_id=-1, prog_num=65036, recursive=True) as chown_1628_65036:  # 0m:0.000s
                            chown_1628_65036()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/ModFX", prog_num=65037) as cd_stage_1629_65037:  # 0m:0.423s
            cd_stage_1629_65037()
            with Stage(r"copy", r"ModFX Autopan v16.0.23.24", prog_num=65038):  # 0m:0.050s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65039) as should_copy_source_1630_65039:  # 0m:0.050s
                    should_copy_source_1630_65039()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Autopan.bundle", prog_num=65040):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r".", delete_extraneous_files=True, prog_num=65041) as copy_dir_to_dir_1631_65041:  # 0m:0.003s
                            copy_dir_to_dir_1631_65041()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", where_to_unwtar=r".", prog_num=65042) as unwtar_1632_65042:  # 0m:0.047s
                            unwtar_1632_65042()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Autopan.bundle", user_id=-1, group_id=-1, prog_num=65043, recursive=True) as chown_1633_65043:  # 0m:0.000s
                            chown_1633_65043()
            with Stage(r"copy", r"ModFX Chorus v16.0.23.24", prog_num=65044):  # 0m:0.050s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65045) as should_copy_source_1634_65045:  # 0m:0.050s
                    should_copy_source_1634_65045()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Chorus.bundle", prog_num=65046):  # 0m:0.049s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r".", delete_extraneous_files=True, prog_num=65047) as copy_dir_to_dir_1635_65047:  # 0m:0.003s
                            copy_dir_to_dir_1635_65047()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", where_to_unwtar=r".", prog_num=65048) as unwtar_1636_65048:  # 0m:0.046s
                            unwtar_1636_65048()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Chorus.bundle", user_id=-1, group_id=-1, prog_num=65049, recursive=True) as chown_1637_65049:  # 0m:0.000s
                            chown_1637_65049()
            with Stage(r"copy", r"ModFX Compressor v16.0.23.24", prog_num=65050):  # 0m:0.049s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65051) as should_copy_source_1638_65051:  # 0m:0.049s
                    should_copy_source_1638_65051()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Compressor.bundle", prog_num=65052):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r".", delete_extraneous_files=True, prog_num=65053) as copy_dir_to_dir_1639_65053:  # 0m:0.002s
                            copy_dir_to_dir_1639_65053()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", where_to_unwtar=r".", prog_num=65054) as unwtar_1640_65054:  # 0m:0.046s
                            unwtar_1640_65054()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Compressor.bundle", user_id=-1, group_id=-1, prog_num=65055, recursive=True) as chown_1641_65055:  # 0m:0.000s
                            chown_1641_65055()
            with Stage(r"copy", r"ModFX Delay v16.0.23.24", prog_num=65056):  # 0m:0.049s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65057) as should_copy_source_1642_65057:  # 0m:0.049s
                    should_copy_source_1642_65057()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Delay.bundle", prog_num=65058):  # 0m:0.048s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", r".", delete_extraneous_files=True, prog_num=65059) as copy_dir_to_dir_1643_65059:  # 0m:0.003s
                            copy_dir_to_dir_1643_65059()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", where_to_unwtar=r".", prog_num=65060) as unwtar_1644_65060:  # 0m:0.045s
                            unwtar_1644_65060()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Delay.bundle", user_id=-1, group_id=-1, prog_num=65061, recursive=True) as chown_1645_65061:  # 0m:0.000s
                            chown_1645_65061()
            with Stage(r"copy", r"ModFX Distortion v16.0.23.24", prog_num=65062):  # 0m:0.067s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65063) as should_copy_source_1646_65063:  # 0m:0.067s
                    should_copy_source_1646_65063()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Distortion.bundle", prog_num=65064):  # 0m:0.067s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r".", delete_extraneous_files=True, prog_num=65065) as copy_dir_to_dir_1647_65065:  # 0m:0.002s
                            copy_dir_to_dir_1647_65065()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", where_to_unwtar=r".", prog_num=65066) as unwtar_1648_65066:  # 0m:0.065s
                            unwtar_1648_65066()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Distortion.bundle", user_id=-1, group_id=-1, prog_num=65067, recursive=True) as chown_1649_65067:  # 0m:0.000s
                            chown_1649_65067()
            with Stage(r"copy", r"ModFX Limiter v16.0.23.24", prog_num=65068):  # 0m:0.047s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65069) as should_copy_source_1650_65069:  # 0m:0.047s
                    should_copy_source_1650_65069()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Limiter.bundle", prog_num=65070):  # 0m:0.047s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r".", delete_extraneous_files=True, prog_num=65071) as copy_dir_to_dir_1651_65071:  # 0m:0.002s
                            copy_dir_to_dir_1651_65071()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", where_to_unwtar=r".", prog_num=65072) as unwtar_1652_65072:  # 0m:0.044s
                            unwtar_1652_65072()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Limiter.bundle", user_id=-1, group_id=-1, prog_num=65073, recursive=True) as chown_1653_65073:  # 0m:0.000s
                            chown_1653_65073()
            with Stage(r"copy", r"ModFX Reverb v16.0.23.24", prog_num=65074):  # 0m:0.112s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65075) as should_copy_source_1654_65075:  # 0m:0.111s
                    should_copy_source_1654_65075()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Reverb.bundle", prog_num=65076):  # 0m:0.111s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r".", delete_extraneous_files=True, prog_num=65077) as copy_dir_to_dir_1655_65077:  # 0m:0.003s
                            copy_dir_to_dir_1655_65077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", where_to_unwtar=r".", prog_num=65078) as unwtar_1656_65078:  # 0m:0.108s
                            unwtar_1656_65078()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Reverb.bundle", user_id=-1, group_id=-1, prog_num=65079, recursive=True) as chown_1657_65079:  # 0m:0.000s
                            chown_1657_65079()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=65080) as cd_stage_1658_65080:  # 0m:3.711s
            cd_stage_1658_65080()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=65081):  # 0m:0.682s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65082) as should_copy_source_1659_65082:  # 0m:0.682s
                    should_copy_source_1659_65082()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=65083):  # 0m:0.682s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=65084) as copy_dir_to_dir_1660_65084:  # 0m:0.004s
                            copy_dir_to_dir_1660_65084()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=65085) as unwtar_1661_65085:  # 0m:0.633s
                            unwtar_1661_65085()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=65086, recursive=True) as chown_1662_65086:  # 0m:0.000s
                            chown_1662_65086()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=65087) as shell_command_1663_65087:  # 0m:0.044s
                            shell_command_1663_65087()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=65088):  # 0m:0.654s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=65089) as should_copy_source_1664_65089:  # 0m:0.654s
                    should_copy_source_1664_65089()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=65090):  # 0m:0.653s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=65091) as copy_dir_to_dir_1665_65091:  # 0m:0.001s
                            copy_dir_to_dir_1665_65091()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=65092) as unwtar_1666_65092:  # 0m:0.586s
                            unwtar_1666_65092()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=65093, recursive=True) as chown_1667_65093:  # 0m:0.000s
                            chown_1667_65093()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=65094) as break_hard_link_1668_65094:  # 0m:0.014s
                            break_hard_link_1668_65094()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=65095) as shell_command_1669_65095:  # 0m:0.043s
                            shell_command_1669_65095()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=65096, recursive=True) as chown_1670_65096:  # 0m:0.000s
                            chown_1670_65096()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=65097, recursive=True) as chmod_1671_65097:  # 0m:0.009s
                            chmod_1671_65097()
            with Stage(r"copy", r"WaveShell1-OBS 16.0 v16.0.23.24", prog_num=65098):  # 0m:0.410s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65099) as should_copy_source_1672_65099:  # 0m:0.409s
                    should_copy_source_1672_65099()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=65100):  # 0m:0.409s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=65101) as copy_dir_to_dir_1673_65101:  # 0m:0.001s
                            copy_dir_to_dir_1673_65101()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=65102) as unwtar_1674_65102:  # 0m:0.360s
                            unwtar_1674_65102()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=65103, recursive=True) as chown_1675_65103:  # 0m:0.000s
                            chown_1675_65103()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=65104) as shell_command_1676_65104:  # 0m:0.047s
                            shell_command_1676_65104()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=65105):  # 0m:0.687s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65106) as should_copy_source_1677_65106:  # 0m:0.686s
                    should_copy_source_1677_65106()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=65107):  # 0m:0.686s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=65108) as copy_dir_to_dir_1678_65108:  # 0m:0.002s
                            copy_dir_to_dir_1678_65108()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=65109) as unwtar_1679_65109:  # 0m:0.638s
                            unwtar_1679_65109()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=65110, recursive=True) as chown_1680_65110:  # 0m:0.000s
                            chown_1680_65110()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=65111) as shell_command_1681_65111:  # 0m:0.046s
                            shell_command_1681_65111()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=65112):  # 0m:0.675s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65113) as should_copy_source_1682_65113:  # 0m:0.675s
                    should_copy_source_1682_65113()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=65114):  # 0m:0.674s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=65115) as copy_dir_to_dir_1683_65115:  # 0m:0.001s
                            copy_dir_to_dir_1683_65115()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=65116) as unwtar_1684_65116:  # 0m:0.628s
                            unwtar_1684_65116()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=65117, recursive=True) as chown_1685_65117:  # 0m:0.000s
                            chown_1685_65117()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=65118) as shell_command_1686_65118:  # 0m:0.044s
                            shell_command_1686_65118()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=65119):  # 0m:0.341s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=65120) as should_copy_source_1687_65120:  # 0m:0.341s
                    should_copy_source_1687_65120()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=65121):  # 0m:0.341s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=65122) as copy_dir_to_dir_1688_65122:  # 0m:0.001s
                            copy_dir_to_dir_1688_65122()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=65123) as unwtar_1689_65123:  # 0m:0.179s
                            unwtar_1689_65123()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=65124, recursive=True) as chown_1690_65124:  # 0m:0.000s
                            chown_1690_65124()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=65125) as shell_command_1691_65125:  # 0m:0.096s
                            shell_command_1691_65125()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=65126) as script_command_1692_65126:  # 0m:0.013s
                            script_command_1692_65126()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=65127) as shell_command_1693_65127:  # 0m:0.051s
                            shell_command_1693_65127()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=65128):  # 0m:0.154s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=65129) as should_copy_source_1694_65129:  # 0m:0.154s
                    should_copy_source_1694_65129()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=65130):  # 0m:0.153s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=65131) as copy_dir_to_dir_1695_65131:  # 0m:0.002s
                            copy_dir_to_dir_1695_65131()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=65132) as unwtar_1696_65132:  # 0m:0.151s
                            unwtar_1696_65132()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=65133, recursive=True) as chown_1697_65133:  # 0m:0.000s
                            chown_1697_65133()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=65134) as shell_command_1698_65134:  # 0m:0.107s
                shell_command_1698_65134()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=65135) as cd_stage_1699_65135:  # 0m:0.670s
            cd_stage_1699_65135()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=65136):  # 0m:0.669s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=65137) as should_copy_source_1700_65137:  # 0m:0.669s
                    should_copy_source_1700_65137()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=65138):  # 0m:0.669s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=65139) as copy_dir_to_dir_1701_65139:  # 0m:0.003s
                            copy_dir_to_dir_1701_65139()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=65140) as unwtar_1702_65140:  # 0m:0.621s
                            unwtar_1702_65140()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=65141, recursive=True) as chown_1703_65141:  # 0m:0.000s
                            chown_1703_65141()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=65142) as shell_command_1704_65142:  # 0m:0.044s
                            shell_command_1704_65142()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=65143) as cd_stage_1705_65143:  # 0m:0.186s
            cd_stage_1705_65143()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=65144):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65145) as should_copy_source_1706_65145:  # 0m:0.002s
                    should_copy_source_1706_65145()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=65146):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=65147) as copy_file_to_dir_1707_65147:  # 0m:0.001s
                            copy_file_to_dir_1707_65147()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65148) as chmod_and_chown_1708_65148:  # 0m:0.000s
                            chmod_and_chown_1708_65148()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=65149):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65150) as should_copy_source_1709_65150:  # 0m:0.001s
                    should_copy_source_1709_65150()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=65151):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=65152) as copy_file_to_dir_1710_65152:  # 0m:0.000s
                            copy_file_to_dir_1710_65152()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65153) as chmod_and_chown_1711_65153:  # 0m:0.000s
                            chmod_and_chown_1711_65153()
            with Stage(r"copy", r"Bass Fingers XML and Registry for Native Instruments", prog_num=65154):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65155) as should_copy_source_1712_65155:  # 0m:0.001s
                    should_copy_source_1712_65155()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", prog_num=65156):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", r".", prog_num=65157) as copy_file_to_dir_1713_65157:  # 0m:0.000s
                            copy_file_to_dir_1713_65157()
                        with ChmodAndChown(path=r"Waves-Bass Fingers Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65158) as chmod_and_chown_1714_65158:  # 0m:0.000s
                            chmod_and_chown_1714_65158()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=65159):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65160) as should_copy_source_1715_65160:  # 0m:0.001s
                    should_copy_source_1715_65160()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=65161):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=65162) as copy_file_to_dir_1716_65162:  # 0m:0.000s
                            copy_file_to_dir_1716_65162()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65163) as chmod_and_chown_1717_65163:  # 0m:0.000s
                            chmod_and_chown_1717_65163()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=65164):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65165) as should_copy_source_1718_65165:  # 0m:0.001s
                    should_copy_source_1718_65165()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=65166):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=65167) as copy_file_to_dir_1719_65167:  # 0m:0.000s
                            copy_file_to_dir_1719_65167()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65168) as chmod_and_chown_1720_65168:  # 0m:0.000s
                            chmod_and_chown_1720_65168()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=65169):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65170) as should_copy_source_1721_65170:  # 0m:0.001s
                    should_copy_source_1721_65170()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=65171):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=65172) as copy_file_to_dir_1722_65172:  # 0m:0.000s
                            copy_file_to_dir_1722_65172()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65173) as chmod_and_chown_1723_65173:  # 0m:0.000s
                            chmod_and_chown_1723_65173()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=65174):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65175) as should_copy_source_1724_65175:  # 0m:0.001s
                    should_copy_source_1724_65175()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=65176):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=65177) as copy_file_to_dir_1725_65177:  # 0m:0.000s
                            copy_file_to_dir_1725_65177()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65178) as chmod_and_chown_1726_65178:  # 0m:0.000s
                            chmod_and_chown_1726_65178()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=65179):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65180) as should_copy_source_1727_65180:  # 0m:0.001s
                    should_copy_source_1727_65180()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=65181):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=65182) as copy_file_to_dir_1728_65182:  # 0m:0.000s
                            copy_file_to_dir_1728_65182()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65183) as chmod_and_chown_1729_65183:  # 0m:0.000s
                            chmod_and_chown_1729_65183()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=65184):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65185) as should_copy_source_1730_65185:  # 0m:0.001s
                    should_copy_source_1730_65185()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=65186):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=65187) as copy_file_to_dir_1731_65187:  # 0m:0.000s
                            copy_file_to_dir_1731_65187()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65188) as chmod_and_chown_1732_65188:  # 0m:0.000s
                            chmod_and_chown_1732_65188()
            with Stage(r"copy", r"C6 XML and Registry for Native Instruments", prog_num=65189):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65190) as should_copy_source_1733_65190:  # 0m:0.001s
                    should_copy_source_1733_65190()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", prog_num=65191):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", r".", prog_num=65192) as copy_file_to_dir_1734_65192:  # 0m:0.000s
                            copy_file_to_dir_1734_65192()
                        with ChmodAndChown(path=r"Waves-C6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65193) as chmod_and_chown_1735_65193:  # 0m:0.000s
                            chmod_and_chown_1735_65193()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=65194):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65195) as should_copy_source_1736_65195:  # 0m:0.001s
                    should_copy_source_1736_65195()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=65196):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=65197) as copy_file_to_dir_1737_65197:  # 0m:0.000s
                            copy_file_to_dir_1737_65197()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65198) as chmod_and_chown_1738_65198:  # 0m:0.000s
                            chmod_and_chown_1738_65198()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=65199):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65200) as should_copy_source_1739_65200:  # 0m:0.001s
                    should_copy_source_1739_65200()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=65201):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=65202) as copy_file_to_dir_1740_65202:  # 0m:0.001s
                            copy_file_to_dir_1740_65202()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65203) as chmod_and_chown_1741_65203:  # 0m:0.000s
                            chmod_and_chown_1741_65203()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=65204):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65205) as should_copy_source_1742_65205:  # 0m:0.001s
                    should_copy_source_1742_65205()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=65206):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=65207) as copy_file_to_dir_1743_65207:  # 0m:0.000s
                            copy_file_to_dir_1743_65207()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65208) as chmod_and_chown_1744_65208:  # 0m:0.000s
                            chmod_and_chown_1744_65208()
            with Stage(r"copy", r"CODEX XML and Registry for Native Instruments", prog_num=65209):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65210) as should_copy_source_1745_65210:  # 0m:0.001s
                    should_copy_source_1745_65210()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", prog_num=65211):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", r".", prog_num=65212) as copy_file_to_dir_1746_65212:  # 0m:0.000s
                            copy_file_to_dir_1746_65212()
                        with ChmodAndChown(path=r"Waves-CODEX Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65213) as chmod_and_chown_1747_65213:  # 0m:0.000s
                            chmod_and_chown_1747_65213()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=65214):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65215) as should_copy_source_1748_65215:  # 0m:0.001s
                    should_copy_source_1748_65215()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=65216):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=65217) as copy_file_to_dir_1749_65217:  # 0m:0.000s
                            copy_file_to_dir_1749_65217()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65218) as chmod_and_chown_1750_65218:  # 0m:0.000s
                            chmod_and_chown_1750_65218()
            with Stage(r"copy", r"Clavinet XML and Registry for Native Instruments", prog_num=65219):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65220) as should_copy_source_1751_65220:  # 0m:0.001s
                    should_copy_source_1751_65220()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", prog_num=65221):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", r".", prog_num=65222) as copy_file_to_dir_1752_65222:  # 0m:0.000s
                            copy_file_to_dir_1752_65222()
                        with ChmodAndChown(path=r"Waves-Clavinet Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65223) as chmod_and_chown_1753_65223:  # 0m:0.000s
                            chmod_and_chown_1753_65223()
            with Stage(r"copy", r"DPR-402 XML and Registry for Native Instruments", prog_num=65224):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65225) as should_copy_source_1754_65225:  # 0m:0.001s
                    should_copy_source_1754_65225()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", prog_num=65226):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", r".", prog_num=65227) as copy_file_to_dir_1755_65227:  # 0m:0.000s
                            copy_file_to_dir_1755_65227()
                        with ChmodAndChown(path=r"Waves-DPR-402 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65228) as chmod_and_chown_1756_65228:  # 0m:0.000s
                            chmod_and_chown_1756_65228()
            with Stage(r"copy", r"Dorrough XML and Registry for Native Instruments", prog_num=65229):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65230) as should_copy_source_1757_65230:  # 0m:0.001s
                    should_copy_source_1757_65230()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", prog_num=65231):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", r".", prog_num=65232) as copy_file_to_dir_1758_65232:  # 0m:0.000s
                            copy_file_to_dir_1758_65232()
                        with ChmodAndChown(path=r"Waves-Dorrough Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65233) as chmod_and_chown_1759_65233:  # 0m:0.000s
                            chmod_and_chown_1759_65233()
            with Stage(r"copy", r"EMO-D5 XML and Registry for Native Instruments", prog_num=65234):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65235) as should_copy_source_1760_65235:  # 0m:0.001s
                    should_copy_source_1760_65235()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", prog_num=65236):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r".", prog_num=65237) as copy_file_to_dir_1761_65237:  # 0m:0.001s
                            copy_file_to_dir_1761_65237()
                        with ChmodAndChown(path=r"Waves-EMO-D5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65238) as chmod_and_chown_1762_65238:  # 0m:0.000s
                            chmod_and_chown_1762_65238()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=65239):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65240) as should_copy_source_1763_65240:  # 0m:0.001s
                    should_copy_source_1763_65240()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=65241):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=65242) as copy_file_to_dir_1764_65242:  # 0m:0.000s
                            copy_file_to_dir_1764_65242()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65243) as chmod_and_chown_1765_65243:  # 0m:0.000s
                            chmod_and_chown_1765_65243()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=65244):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65245) as should_copy_source_1766_65245:  # 0m:0.001s
                    should_copy_source_1766_65245()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=65246):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=65247) as copy_file_to_dir_1767_65247:  # 0m:0.000s
                            copy_file_to_dir_1767_65247()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65248) as chmod_and_chown_1768_65248:  # 0m:0.000s
                            chmod_and_chown_1768_65248()
            with Stage(r"copy", r"Electric200 XML and Registry for Native Instruments", prog_num=65249):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65250) as should_copy_source_1769_65250:  # 0m:0.001s
                    should_copy_source_1769_65250()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", prog_num=65251):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", r".", prog_num=65252) as copy_file_to_dir_1770_65252:  # 0m:0.000s
                            copy_file_to_dir_1770_65252()
                        with ChmodAndChown(path=r"Waves-Electric200 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65253) as chmod_and_chown_1771_65253:  # 0m:0.000s
                            chmod_and_chown_1771_65253()
            with Stage(r"copy", r"Electric88 XML and Registry for Native Instruments", prog_num=65254):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65255) as should_copy_source_1772_65255:  # 0m:0.001s
                    should_copy_source_1772_65255()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", prog_num=65256):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", r".", prog_num=65257) as copy_file_to_dir_1773_65257:  # 0m:0.000s
                            copy_file_to_dir_1773_65257()
                        with ChmodAndChown(path=r"Waves-Electric88 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65258) as chmod_and_chown_1774_65258:  # 0m:0.000s
                            chmod_and_chown_1774_65258()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=65259):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65260) as should_copy_source_1775_65260:  # 0m:0.001s
                    should_copy_source_1775_65260()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=65261):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=65262) as copy_file_to_dir_1776_65262:  # 0m:0.000s
                            copy_file_to_dir_1776_65262()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65263) as chmod_and_chown_1777_65263:  # 0m:0.000s
                            chmod_and_chown_1777_65263()
            with Stage(r"copy", r"Element XML and Registry for Native Instruments", prog_num=65264):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65265) as should_copy_source_1778_65265:  # 0m:0.001s
                    should_copy_source_1778_65265()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", prog_num=65266):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", r".", prog_num=65267) as copy_file_to_dir_1779_65267:  # 0m:0.000s
                            copy_file_to_dir_1779_65267()
                        with ChmodAndChown(path=r"Waves-Element Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65268) as chmod_and_chown_1780_65268:  # 0m:0.000s
                            chmod_and_chown_1780_65268()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=65269):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65270) as should_copy_source_1781_65270:  # 0m:0.001s
                    should_copy_source_1781_65270()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=65271):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=65272) as copy_file_to_dir_1782_65272:  # 0m:0.000s
                            copy_file_to_dir_1782_65272()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65273) as chmod_and_chown_1783_65273:  # 0m:0.000s
                            chmod_and_chown_1783_65273()
            with Stage(r"copy", r"F6 XML and Registry for Native Instruments", prog_num=65274):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65275) as should_copy_source_1784_65275:  # 0m:0.001s
                    should_copy_source_1784_65275()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", prog_num=65276):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", r".", prog_num=65277) as copy_file_to_dir_1785_65277:  # 0m:0.000s
                            copy_file_to_dir_1785_65277()
                        with ChmodAndChown(path=r"Waves-F6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65278) as chmod_and_chown_1786_65278:  # 0m:0.000s
                            chmod_and_chown_1786_65278()
            with Stage(r"copy", r"Flow Motion XML and Registry for Native Instruments", prog_num=65279):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65280) as should_copy_source_1787_65280:  # 0m:0.001s
                    should_copy_source_1787_65280()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", prog_num=65281):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", r".", prog_num=65282) as copy_file_to_dir_1788_65282:  # 0m:0.000s
                            copy_file_to_dir_1788_65282()
                        with ChmodAndChown(path=r"Waves-Flow Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65283) as chmod_and_chown_1789_65283:  # 0m:0.000s
                            chmod_and_chown_1789_65283()
            with Stage(r"copy", r"GEQ Classic XML and Registry for Native Instruments", prog_num=65284):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65285) as should_copy_source_1790_65285:  # 0m:0.001s
                    should_copy_source_1790_65285()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", prog_num=65286):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", r".", prog_num=65287) as copy_file_to_dir_1791_65287:  # 0m:0.000s
                            copy_file_to_dir_1791_65287()
                        with ChmodAndChown(path=r"Waves-GEQ Classic Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65288) as chmod_and_chown_1792_65288:  # 0m:0.000s
                            chmod_and_chown_1792_65288()
            with Stage(r"copy", r"GEQ Modern XML and Registry for Native Instruments", prog_num=65289):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65290) as should_copy_source_1793_65290:  # 0m:0.001s
                    should_copy_source_1793_65290()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", prog_num=65291):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", r".", prog_num=65292) as copy_file_to_dir_1794_65292:  # 0m:0.000s
                            copy_file_to_dir_1794_65292()
                        with ChmodAndChown(path=r"Waves-GEQ Modern Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65293) as chmod_and_chown_1795_65293:  # 0m:0.000s
                            chmod_and_chown_1795_65293()
            with Stage(r"copy", r"Grand Rhapsody XML and Registry for Native Instruments", prog_num=65294):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65295) as should_copy_source_1796_65295:  # 0m:0.001s
                    should_copy_source_1796_65295()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", prog_num=65296):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", r".", prog_num=65297) as copy_file_to_dir_1797_65297:  # 0m:0.001s
                            copy_file_to_dir_1797_65297()
                        with ChmodAndChown(path=r"Waves-Grand Rhapsody Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65298) as chmod_and_chown_1798_65298:  # 0m:0.000s
                            chmod_and_chown_1798_65298()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=65299):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65300) as should_copy_source_1799_65300:  # 0m:0.001s
                    should_copy_source_1799_65300()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=65301):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=65302) as copy_file_to_dir_1800_65302:  # 0m:0.000s
                            copy_file_to_dir_1800_65302()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65303) as chmod_and_chown_1801_65303:  # 0m:0.000s
                            chmod_and_chown_1801_65303()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=65304):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65305) as should_copy_source_1802_65305:  # 0m:0.001s
                    should_copy_source_1802_65305()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=65306):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=65307) as copy_file_to_dir_1803_65307:  # 0m:0.000s
                            copy_file_to_dir_1803_65307()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65308) as chmod_and_chown_1804_65308:  # 0m:0.000s
                            chmod_and_chown_1804_65308()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=65309):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65310) as should_copy_source_1805_65310:  # 0m:0.001s
                    should_copy_source_1805_65310()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=65311):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=65312) as copy_file_to_dir_1806_65312:  # 0m:0.000s
                            copy_file_to_dir_1806_65312()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65313) as chmod_and_chown_1807_65313:  # 0m:0.000s
                            chmod_and_chown_1807_65313()
            with Stage(r"copy", r"GW VoiceCentric XML and Registry for Native Instruments", prog_num=65314):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65315) as should_copy_source_1808_65315:  # 0m:0.001s
                    should_copy_source_1808_65315()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", prog_num=65316):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", r".", prog_num=65317) as copy_file_to_dir_1809_65317:  # 0m:0.000s
                            copy_file_to_dir_1809_65317()
                        with ChmodAndChown(path=r"Waves-GW VoiceCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65318) as chmod_and_chown_1810_65318:  # 0m:0.000s
                            chmod_and_chown_1810_65318()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=65319):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65320) as should_copy_source_1811_65320:  # 0m:0.001s
                    should_copy_source_1811_65320()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=65321):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=65322) as copy_file_to_dir_1812_65322:  # 0m:0.000s
                            copy_file_to_dir_1812_65322()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65323) as chmod_and_chown_1813_65323:  # 0m:0.000s
                            chmod_and_chown_1813_65323()
            with Stage(r"copy", r"H-EQ XML and Registry for Native Instruments", prog_num=65324):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65325) as should_copy_source_1814_65325:  # 0m:0.001s
                    should_copy_source_1814_65325()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", prog_num=65326):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", r".", prog_num=65327) as copy_file_to_dir_1815_65327:  # 0m:0.000s
                            copy_file_to_dir_1815_65327()
                        with ChmodAndChown(path=r"Waves-H-EQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65328) as chmod_and_chown_1816_65328:  # 0m:0.000s
                            chmod_and_chown_1816_65328()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=65329):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65330) as should_copy_source_1817_65330:  # 0m:0.001s
                    should_copy_source_1817_65330()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=65331):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=65332) as copy_file_to_dir_1818_65332:  # 0m:0.000s
                            copy_file_to_dir_1818_65332()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65333) as chmod_and_chown_1819_65333:  # 0m:0.000s
                            chmod_and_chown_1819_65333()
            with Stage(r"copy", r"IMPusher XML and Registry for Native Instruments", prog_num=65334):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65335) as should_copy_source_1820_65335:  # 0m:0.001s
                    should_copy_source_1820_65335()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", prog_num=65336):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", r".", prog_num=65337) as copy_file_to_dir_1821_65337:  # 0m:0.000s
                            copy_file_to_dir_1821_65337()
                        with ChmodAndChown(path=r"Waves-IMPusher Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65338) as chmod_and_chown_1822_65338:  # 0m:0.000s
                            chmod_and_chown_1822_65338()
            with Stage(r"copy", r"IRLive XML and Registry for Native Instruments", prog_num=65339):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65340) as should_copy_source_1823_65340:  # 0m:0.001s
                    should_copy_source_1823_65340()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", prog_num=65341):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", r".", prog_num=65342) as copy_file_to_dir_1824_65342:  # 0m:0.000s
                            copy_file_to_dir_1824_65342()
                        with ChmodAndChown(path=r"Waves-IRLive Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65343) as chmod_and_chown_1825_65343:  # 0m:0.000s
                            chmod_and_chown_1825_65343()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=65344):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65345) as should_copy_source_1826_65345:  # 0m:0.001s
                    should_copy_source_1826_65345()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=65346):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=65347) as copy_file_to_dir_1827_65347:  # 0m:0.000s
                            copy_file_to_dir_1827_65347()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65348) as chmod_and_chown_1828_65348:  # 0m:0.000s
                            chmod_and_chown_1828_65348()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=65349):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65350) as should_copy_source_1829_65350:  # 0m:0.001s
                    should_copy_source_1829_65350()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=65351):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=65352) as copy_file_to_dir_1830_65352:  # 0m:0.000s
                            copy_file_to_dir_1830_65352()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65353) as chmod_and_chown_1831_65353:  # 0m:0.000s
                            chmod_and_chown_1831_65353()
            with Stage(r"copy", r"JJP-Bass XML and Registry for Native Instruments", prog_num=65354):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65355) as should_copy_source_1832_65355:  # 0m:0.001s
                    should_copy_source_1832_65355()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", prog_num=65356):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", r".", prog_num=65357) as copy_file_to_dir_1833_65357:  # 0m:0.000s
                            copy_file_to_dir_1833_65357()
                        with ChmodAndChown(path=r"Waves-JJP-Bass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65358) as chmod_and_chown_1834_65358:  # 0m:0.000s
                            chmod_and_chown_1834_65358()
            with Stage(r"copy", r"JJP-Cymb-Perc XML and Registry for Native Instruments", prog_num=65359):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65360) as should_copy_source_1835_65360:  # 0m:0.001s
                    should_copy_source_1835_65360()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", prog_num=65361):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", r".", prog_num=65362) as copy_file_to_dir_1836_65362:  # 0m:0.000s
                            copy_file_to_dir_1836_65362()
                        with ChmodAndChown(path=r"Waves-JJP-Cymb-Perc Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65363) as chmod_and_chown_1837_65363:  # 0m:0.000s
                            chmod_and_chown_1837_65363()
            with Stage(r"copy", r"JJP-Drums XML and Registry for Native Instruments", prog_num=65364):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65365) as should_copy_source_1838_65365:  # 0m:0.001s
                    should_copy_source_1838_65365()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", prog_num=65366):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", r".", prog_num=65367) as copy_file_to_dir_1839_65367:  # 0m:0.000s
                            copy_file_to_dir_1839_65367()
                        with ChmodAndChown(path=r"Waves-JJP-Drums Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65368) as chmod_and_chown_1840_65368:  # 0m:0.000s
                            chmod_and_chown_1840_65368()
            with Stage(r"copy", r"JJP-Guitars XML and Registry for Native Instruments", prog_num=65369):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65370) as should_copy_source_1841_65370:  # 0m:0.001s
                    should_copy_source_1841_65370()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", prog_num=65371):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", r".", prog_num=65372) as copy_file_to_dir_1842_65372:  # 0m:0.000s
                            copy_file_to_dir_1842_65372()
                        with ChmodAndChown(path=r"Waves-JJP-Guitars Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65373) as chmod_and_chown_1843_65373:  # 0m:0.000s
                            chmod_and_chown_1843_65373()
            with Stage(r"copy", r"JJP-Strings-Keys XML and Registry for Native Instruments", prog_num=65374):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65375) as should_copy_source_1844_65375:  # 0m:0.001s
                    should_copy_source_1844_65375()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", prog_num=65376):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", r".", prog_num=65377) as copy_file_to_dir_1845_65377:  # 0m:0.000s
                            copy_file_to_dir_1845_65377()
                        with ChmodAndChown(path=r"Waves-JJP-Strings-Keys Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65378) as chmod_and_chown_1846_65378:  # 0m:0.000s
                            chmod_and_chown_1846_65378()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=65379):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65380) as should_copy_source_1847_65380:  # 0m:0.001s
                    should_copy_source_1847_65380()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=65381):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=65382) as copy_file_to_dir_1848_65382:  # 0m:0.000s
                            copy_file_to_dir_1848_65382()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65383) as chmod_and_chown_1849_65383:  # 0m:0.000s
                            chmod_and_chown_1849_65383()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=65384):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65385) as should_copy_source_1850_65385:  # 0m:0.001s
                    should_copy_source_1850_65385()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=65386):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=65387) as copy_file_to_dir_1851_65387:  # 0m:0.000s
                            copy_file_to_dir_1851_65387()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65388) as chmod_and_chown_1852_65388:  # 0m:0.000s
                            chmod_and_chown_1852_65388()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=65389):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65390) as should_copy_source_1853_65390:  # 0m:0.001s
                    should_copy_source_1853_65390()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=65391):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=65392) as copy_file_to_dir_1854_65392:  # 0m:0.000s
                            copy_file_to_dir_1854_65392()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65393) as chmod_and_chown_1855_65393:  # 0m:0.000s
                            chmod_and_chown_1855_65393()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=65394):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65395) as should_copy_source_1856_65395:  # 0m:0.001s
                    should_copy_source_1856_65395()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=65396):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=65397) as copy_file_to_dir_1857_65397:  # 0m:0.000s
                            copy_file_to_dir_1857_65397()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65398) as chmod_and_chown_1858_65398:  # 0m:0.000s
                            chmod_and_chown_1858_65398()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=65399):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65400) as should_copy_source_1859_65400:  # 0m:0.001s
                    should_copy_source_1859_65400()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=65401):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=65402) as copy_file_to_dir_1860_65402:  # 0m:0.001s
                            copy_file_to_dir_1860_65402()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65403) as chmod_and_chown_1861_65403:  # 0m:0.000s
                            chmod_and_chown_1861_65403()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=65404):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65405) as should_copy_source_1862_65405:  # 0m:0.001s
                    should_copy_source_1862_65405()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=65406):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=65407) as copy_file_to_dir_1863_65407:  # 0m:0.000s
                            copy_file_to_dir_1863_65407()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65408) as chmod_and_chown_1864_65408:  # 0m:0.000s
                            chmod_and_chown_1864_65408()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=65409):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65410) as should_copy_source_1865_65410:  # 0m:0.001s
                    should_copy_source_1865_65410()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=65411):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=65412) as copy_file_to_dir_1866_65412:  # 0m:0.000s
                            copy_file_to_dir_1866_65412()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65413) as chmod_and_chown_1867_65413:  # 0m:0.000s
                            chmod_and_chown_1867_65413()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=65414):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65415) as should_copy_source_1868_65415:  # 0m:0.001s
                    should_copy_source_1868_65415()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=65416):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=65417) as copy_file_to_dir_1869_65417:  # 0m:0.000s
                            copy_file_to_dir_1869_65417()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65418) as chmod_and_chown_1870_65418:  # 0m:0.000s
                            chmod_and_chown_1870_65418()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=65419):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65420) as should_copy_source_1871_65420:  # 0m:0.001s
                    should_copy_source_1871_65420()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=65421):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=65422) as copy_file_to_dir_1872_65422:  # 0m:0.000s
                            copy_file_to_dir_1872_65422()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65423) as chmod_and_chown_1873_65423:  # 0m:0.000s
                            chmod_and_chown_1873_65423()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=65424):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65425) as should_copy_source_1874_65425:  # 0m:0.001s
                    should_copy_source_1874_65425()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=65426):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=65427) as copy_file_to_dir_1875_65427:  # 0m:0.000s
                            copy_file_to_dir_1875_65427()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65428) as chmod_and_chown_1876_65428:  # 0m:0.000s
                            chmod_and_chown_1876_65428()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=65429):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65430) as should_copy_source_1877_65430:  # 0m:0.001s
                    should_copy_source_1877_65430()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=65431):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=65432) as copy_file_to_dir_1878_65432:  # 0m:0.000s
                            copy_file_to_dir_1878_65432()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65433) as chmod_and_chown_1879_65433:  # 0m:0.000s
                            chmod_and_chown_1879_65433()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=65434):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65435) as should_copy_source_1880_65435:  # 0m:0.001s
                    should_copy_source_1880_65435()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=65436):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=65437) as copy_file_to_dir_1881_65437:  # 0m:0.000s
                            copy_file_to_dir_1881_65437()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65438) as chmod_and_chown_1882_65438:  # 0m:0.000s
                            chmod_and_chown_1882_65438()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=65439):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65440) as should_copy_source_1883_65440:  # 0m:0.001s
                    should_copy_source_1883_65440()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=65441):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=65442) as copy_file_to_dir_1884_65442:  # 0m:0.000s
                            copy_file_to_dir_1884_65442()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65443) as chmod_and_chown_1885_65443:  # 0m:0.000s
                            chmod_and_chown_1885_65443()
            with Stage(r"copy", r"MannyM-Delay XML and Registry for Native Instruments", prog_num=65444):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65445) as should_copy_source_1886_65445:  # 0m:0.001s
                    should_copy_source_1886_65445()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", prog_num=65446):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r".", prog_num=65447) as copy_file_to_dir_1887_65447:  # 0m:0.000s
                            copy_file_to_dir_1887_65447()
                        with ChmodAndChown(path=r"Waves-MannyM-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65448) as chmod_and_chown_1888_65448:  # 0m:0.000s
                            chmod_and_chown_1888_65448()
            with Stage(r"copy", r"MannyM Distortion XML and Registry for Native Instruments", prog_num=65449):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65450) as should_copy_source_1889_65450:  # 0m:0.001s
                    should_copy_source_1889_65450()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", prog_num=65451):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", r".", prog_num=65452) as copy_file_to_dir_1890_65452:  # 0m:0.000s
                            copy_file_to_dir_1890_65452()
                        with ChmodAndChown(path=r"Waves-MannyM Distortion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65453) as chmod_and_chown_1891_65453:  # 0m:0.000s
                            chmod_and_chown_1891_65453()
            with Stage(r"copy", r"MannyM-EQ XML and Registry for Native Instruments", prog_num=65454):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65455) as should_copy_source_1892_65455:  # 0m:0.001s
                    should_copy_source_1892_65455()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", prog_num=65456):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", r".", prog_num=65457) as copy_file_to_dir_1893_65457:  # 0m:0.000s
                            copy_file_to_dir_1893_65457()
                        with ChmodAndChown(path=r"Waves-MannyM-EQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65458) as chmod_and_chown_1894_65458:  # 0m:0.000s
                            chmod_and_chown_1894_65458()
            with Stage(r"copy", r"Manny Marroquin Reverb XML and Registry for Native Instruments", prog_num=65459):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65460) as should_copy_source_1895_65460:  # 0m:0.001s
                    should_copy_source_1895_65460()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", prog_num=65461):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", r".", prog_num=65462) as copy_file_to_dir_1896_65462:  # 0m:0.000s
                            copy_file_to_dir_1896_65462()
                        with ChmodAndChown(path=r"Waves-MannyM-Reverb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65463) as chmod_and_chown_1897_65463:  # 0m:0.000s
                            chmod_and_chown_1897_65463()
            with Stage(r"copy", r"Manny Marroquin Tone Shaper XML and Registry for Native Instruments", prog_num=65464):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65465) as should_copy_source_1898_65465:  # 0m:0.001s
                    should_copy_source_1898_65465()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", prog_num=65466):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", r".", prog_num=65467) as copy_file_to_dir_1899_65467:  # 0m:0.000s
                            copy_file_to_dir_1899_65467()
                        with ChmodAndChown(path=r"Waves-MannyM-ToneShaper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65468) as chmod_and_chown_1900_65468:  # 0m:0.000s
                            chmod_and_chown_1900_65468()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=65469):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65470) as should_copy_source_1901_65470:  # 0m:0.001s
                    should_copy_source_1901_65470()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=65471):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=65472) as copy_file_to_dir_1902_65472:  # 0m:0.000s
                            copy_file_to_dir_1902_65472()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65473) as chmod_and_chown_1903_65473:  # 0m:0.000s
                            chmod_and_chown_1903_65473()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=65474):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65475) as should_copy_source_1904_65475:  # 0m:0.001s
                    should_copy_source_1904_65475()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=65476):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=65477) as copy_file_to_dir_1905_65477:  # 0m:0.000s
                            copy_file_to_dir_1905_65477()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65478) as chmod_and_chown_1906_65478:  # 0m:0.000s
                            chmod_and_chown_1906_65478()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=65479):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65480) as should_copy_source_1907_65480:  # 0m:0.001s
                    should_copy_source_1907_65480()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=65481):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=65482) as copy_file_to_dir_1908_65482:  # 0m:0.000s
                            copy_file_to_dir_1908_65482()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65483) as chmod_and_chown_1909_65483:  # 0m:0.000s
                            chmod_and_chown_1909_65483()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=65484):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65485) as should_copy_source_1910_65485:  # 0m:0.001s
                    should_copy_source_1910_65485()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=65486):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=65487) as copy_file_to_dir_1911_65487:  # 0m:0.000s
                            copy_file_to_dir_1911_65487()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65488) as chmod_and_chown_1912_65488:  # 0m:0.000s
                            chmod_and_chown_1912_65488()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=65489):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65490) as should_copy_source_1913_65490:  # 0m:0.001s
                    should_copy_source_1913_65490()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=65491):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=65492) as copy_file_to_dir_1914_65492:  # 0m:0.000s
                            copy_file_to_dir_1914_65492()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65493) as chmod_and_chown_1915_65493:  # 0m:0.000s
                            chmod_and_chown_1915_65493()
            with Stage(r"copy", r"OneKnob Brighter XML and Registry for Native Instruments", prog_num=65494):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65495) as should_copy_source_1916_65495:  # 0m:0.001s
                    should_copy_source_1916_65495()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", prog_num=65496):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", r".", prog_num=65497) as copy_file_to_dir_1917_65497:  # 0m:0.000s
                            copy_file_to_dir_1917_65497()
                        with ChmodAndChown(path=r"Waves-OneKnob Brighter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65498) as chmod_and_chown_1918_65498:  # 0m:0.000s
                            chmod_and_chown_1918_65498()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=65499):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65500) as should_copy_source_1919_65500:  # 0m:0.001s
                    should_copy_source_1919_65500()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=65501):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=65502) as copy_file_to_dir_1920_65502:  # 0m:0.000s
                            copy_file_to_dir_1920_65502()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65503) as chmod_and_chown_1921_65503:  # 0m:0.000s
                            chmod_and_chown_1921_65503()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=65504):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65505) as should_copy_source_1922_65505:  # 0m:0.001s
                    should_copy_source_1922_65505()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=65506):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=65507) as copy_file_to_dir_1923_65507:  # 0m:0.000s
                            copy_file_to_dir_1923_65507()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65508) as chmod_and_chown_1924_65508:  # 0m:0.000s
                            chmod_and_chown_1924_65508()
            with Stage(r"copy", r"OneKnob Louder XML and Registry for Native Instruments", prog_num=65509):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65510) as should_copy_source_1925_65510:  # 0m:0.001s
                    should_copy_source_1925_65510()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", prog_num=65511):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", r".", prog_num=65512) as copy_file_to_dir_1926_65512:  # 0m:0.000s
                            copy_file_to_dir_1926_65512()
                        with ChmodAndChown(path=r"Waves-OneKnob Louder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65513) as chmod_and_chown_1927_65513:  # 0m:0.000s
                            chmod_and_chown_1927_65513()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=65514):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65515) as should_copy_source_1928_65515:  # 0m:0.001s
                    should_copy_source_1928_65515()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=65516):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=65517) as copy_file_to_dir_1929_65517:  # 0m:0.000s
                            copy_file_to_dir_1929_65517()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65518) as chmod_and_chown_1930_65518:  # 0m:0.000s
                            chmod_and_chown_1930_65518()
            with Stage(r"copy", r"OneKnob Pressure XML and Registry for Native Instruments", prog_num=65519):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65520) as should_copy_source_1931_65520:  # 0m:0.001s
                    should_copy_source_1931_65520()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", prog_num=65521):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", r".", prog_num=65522) as copy_file_to_dir_1932_65522:  # 0m:0.000s
                            copy_file_to_dir_1932_65522()
                        with ChmodAndChown(path=r"Waves-OneKnob Pressure Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65523) as chmod_and_chown_1933_65523:  # 0m:0.000s
                            chmod_and_chown_1933_65523()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=65524):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65525) as should_copy_source_1934_65525:  # 0m:0.001s
                    should_copy_source_1934_65525()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=65526):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=65527) as copy_file_to_dir_1935_65527:  # 0m:0.000s
                            copy_file_to_dir_1935_65527()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65528) as chmod_and_chown_1936_65528:  # 0m:0.000s
                            chmod_and_chown_1936_65528()
            with Stage(r"copy", r"OneKnob Wetter XML and Registry for Native Instruments", prog_num=65529):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65530) as should_copy_source_1937_65530:  # 0m:0.001s
                    should_copy_source_1937_65530()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", prog_num=65531):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", r".", prog_num=65532) as copy_file_to_dir_1938_65532:  # 0m:0.000s
                            copy_file_to_dir_1938_65532()
                        with ChmodAndChown(path=r"Waves-OneKnob Wetter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65533) as chmod_and_chown_1939_65533:  # 0m:0.000s
                            chmod_and_chown_1939_65533()
            with Stage(r"copy", r"OVox XML and Registry for Native Instruments", prog_num=65534):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65535) as should_copy_source_1940_65535:  # 0m:0.001s
                    should_copy_source_1940_65535()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", prog_num=65536):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r".", prog_num=65537) as copy_file_to_dir_1941_65537:  # 0m:0.000s
                            copy_file_to_dir_1941_65537()
                        with ChmodAndChown(path=r"Waves-OVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65538) as chmod_and_chown_1942_65538:  # 0m:0.000s
                            chmod_and_chown_1942_65538()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=65539):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65540) as should_copy_source_1943_65540:  # 0m:0.001s
                    should_copy_source_1943_65540()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=65541):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=65542) as copy_file_to_dir_1944_65542:  # 0m:0.000s
                            copy_file_to_dir_1944_65542()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65543) as chmod_and_chown_1945_65543:  # 0m:0.000s
                            chmod_and_chown_1945_65543()
            with Stage(r"copy", r"PRS Archon XML and Registry for Native Instruments", prog_num=65544):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65545) as should_copy_source_1946_65545:  # 0m:0.001s
                    should_copy_source_1946_65545()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", prog_num=65546):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", r".", prog_num=65547) as copy_file_to_dir_1947_65547:  # 0m:0.000s
                            copy_file_to_dir_1947_65547()
                        with ChmodAndChown(path=r"Waves-PRS Archon Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65548) as chmod_and_chown_1948_65548:  # 0m:0.000s
                            chmod_and_chown_1948_65548()
            with Stage(r"copy", r"PRS Dallas XML and Registry for Native Instruments", prog_num=65549):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65550) as should_copy_source_1949_65550:  # 0m:0.001s
                    should_copy_source_1949_65550()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", prog_num=65551):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", r".", prog_num=65552) as copy_file_to_dir_1950_65552:  # 0m:0.000s
                            copy_file_to_dir_1950_65552()
                        with ChmodAndChown(path=r"Waves-PRS Dallas Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65553) as chmod_and_chown_1951_65553:  # 0m:0.000s
                            chmod_and_chown_1951_65553()
            with Stage(r"copy", r"PRS V9 XML and Registry for Native Instruments", prog_num=65554):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65555) as should_copy_source_1952_65555:  # 0m:0.001s
                    should_copy_source_1952_65555()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", prog_num=65556):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", r".", prog_num=65557) as copy_file_to_dir_1953_65557:  # 0m:0.000s
                            copy_file_to_dir_1953_65557()
                        with ChmodAndChown(path=r"Waves-PRS V9 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65558) as chmod_and_chown_1954_65558:  # 0m:0.000s
                            chmod_and_chown_1954_65558()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=65559):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65560) as should_copy_source_1955_65560:  # 0m:0.001s
                    should_copy_source_1955_65560()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=65561):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=65562) as copy_file_to_dir_1956_65562:  # 0m:0.000s
                            copy_file_to_dir_1956_65562()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65563) as chmod_and_chown_1957_65563:  # 0m:0.000s
                            chmod_and_chown_1957_65563()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=65564):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65565) as should_copy_source_1958_65565:  # 0m:0.001s
                    should_copy_source_1958_65565()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=65566):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=65567) as copy_file_to_dir_1959_65567:  # 0m:0.000s
                            copy_file_to_dir_1959_65567()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65568) as chmod_and_chown_1960_65568:  # 0m:0.000s
                            chmod_and_chown_1960_65568()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65569) as should_copy_source_1961_65569:  # 0m:0.001s
                    should_copy_source_1961_65569()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=65570):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=65571) as copy_file_to_dir_1962_65571:  # 0m:0.001s
                            copy_file_to_dir_1962_65571()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65572) as chmod_and_chown_1963_65572:  # 0m:0.000s
                            chmod_and_chown_1963_65572()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=65573):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65574) as should_copy_source_1964_65574:  # 0m:0.001s
                    should_copy_source_1964_65574()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=65575):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=65576) as copy_file_to_dir_1965_65576:  # 0m:0.000s
                            copy_file_to_dir_1965_65576()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65577) as chmod_and_chown_1966_65577:  # 0m:0.000s
                            chmod_and_chown_1966_65577()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=65578):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65579) as should_copy_source_1967_65579:  # 0m:0.001s
                    should_copy_source_1967_65579()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=65580):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=65581) as copy_file_to_dir_1968_65581:  # 0m:0.000s
                            copy_file_to_dir_1968_65581()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65582) as chmod_and_chown_1969_65582:  # 0m:0.000s
                            chmod_and_chown_1969_65582()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=65583):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65584) as should_copy_source_1970_65584:  # 0m:0.001s
                    should_copy_source_1970_65584()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=65585):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=65586) as copy_file_to_dir_1971_65586:  # 0m:0.000s
                            copy_file_to_dir_1971_65586()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65587) as chmod_and_chown_1972_65587:  # 0m:0.000s
                            chmod_and_chown_1972_65587()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=65588):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65589) as should_copy_source_1973_65589:  # 0m:0.001s
                    should_copy_source_1973_65589()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=65590):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=65591) as copy_file_to_dir_1974_65591:  # 0m:0.000s
                            copy_file_to_dir_1974_65591()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65592) as chmod_and_chown_1975_65592:  # 0m:0.000s
                            chmod_and_chown_1975_65592()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=65593):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65594) as should_copy_source_1976_65594:  # 0m:0.001s
                    should_copy_source_1976_65594()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=65595):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=65596) as copy_file_to_dir_1977_65596:  # 0m:0.000s
                            copy_file_to_dir_1977_65596()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65597) as chmod_and_chown_1978_65597:  # 0m:0.000s
                            chmod_and_chown_1978_65597()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=65598):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65599) as should_copy_source_1979_65599:  # 0m:0.001s
                    should_copy_source_1979_65599()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=65600):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=65601) as copy_file_to_dir_1980_65601:  # 0m:0.000s
                            copy_file_to_dir_1980_65601()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65602) as chmod_and_chown_1981_65602:  # 0m:0.000s
                            chmod_and_chown_1981_65602()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=65603):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65604) as should_copy_source_1982_65604:  # 0m:0.001s
                    should_copy_source_1982_65604()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=65605):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=65606) as copy_file_to_dir_1983_65606:  # 0m:0.000s
                            copy_file_to_dir_1983_65606()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65607) as chmod_and_chown_1984_65607:  # 0m:0.000s
                            chmod_and_chown_1984_65607()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=65608):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65609) as should_copy_source_1985_65609:  # 0m:0.001s
                    should_copy_source_1985_65609()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=65610):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=65611) as copy_file_to_dir_1986_65611:  # 0m:0.000s
                            copy_file_to_dir_1986_65611()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65612) as chmod_and_chown_1987_65612:  # 0m:0.000s
                            chmod_and_chown_1987_65612()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=65613):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65614) as should_copy_source_1988_65614:  # 0m:0.001s
                    should_copy_source_1988_65614()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=65615):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=65616) as copy_file_to_dir_1989_65616:  # 0m:0.000s
                            copy_file_to_dir_1989_65616()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65617) as chmod_and_chown_1990_65617:  # 0m:0.000s
                            chmod_and_chown_1990_65617()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=65618):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65619) as should_copy_source_1991_65619:  # 0m:0.001s
                    should_copy_source_1991_65619()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=65620):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=65621) as copy_file_to_dir_1992_65621:  # 0m:0.000s
                            copy_file_to_dir_1992_65621()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65622) as chmod_and_chown_1993_65622:  # 0m:0.000s
                            chmod_and_chown_1993_65622()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=65623):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65624) as should_copy_source_1994_65624:  # 0m:0.001s
                    should_copy_source_1994_65624()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=65625):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=65626) as copy_file_to_dir_1995_65626:  # 0m:0.000s
                            copy_file_to_dir_1995_65626()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65627) as chmod_and_chown_1996_65627:  # 0m:0.000s
                            chmod_and_chown_1996_65627()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=65628):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65629) as should_copy_source_1997_65629:  # 0m:0.001s
                    should_copy_source_1997_65629()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=65630):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=65631) as copy_file_to_dir_1998_65631:  # 0m:0.000s
                            copy_file_to_dir_1998_65631()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65632) as chmod_and_chown_1999_65632:  # 0m:0.000s
                            chmod_and_chown_1999_65632()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=65633):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65634) as should_copy_source_2000_65634:  # 0m:0.001s
                    should_copy_source_2000_65634()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=65635):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=65636) as copy_file_to_dir_2001_65636:  # 0m:0.000s
                            copy_file_to_dir_2001_65636()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65637) as chmod_and_chown_2002_65637:  # 0m:0.000s
                            chmod_and_chown_2002_65637()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=65638):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65639) as should_copy_source_2003_65639:  # 0m:0.001s
                    should_copy_source_2003_65639()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=65640):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=65641) as copy_file_to_dir_2004_65641:  # 0m:0.000s
                            copy_file_to_dir_2004_65641()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65642) as chmod_and_chown_2005_65642:  # 0m:0.000s
                            chmod_and_chown_2005_65642()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=65643):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65644) as should_copy_source_2006_65644:  # 0m:0.001s
                    should_copy_source_2006_65644()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=65645):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=65646) as copy_file_to_dir_2007_65646:  # 0m:0.001s
                            copy_file_to_dir_2007_65646()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65647) as chmod_and_chown_2008_65647:  # 0m:0.000s
                            chmod_and_chown_2008_65647()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=65648):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65649) as should_copy_source_2009_65649:  # 0m:0.001s
                    should_copy_source_2009_65649()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=65650):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=65651) as copy_file_to_dir_2010_65651:  # 0m:0.000s
                            copy_file_to_dir_2010_65651()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65652) as chmod_and_chown_2011_65652:  # 0m:0.000s
                            chmod_and_chown_2011_65652()
            with Stage(r"copy", r"SSLComp XML and Registry for Native Instruments", prog_num=65653):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65654) as should_copy_source_2012_65654:  # 0m:0.001s
                    should_copy_source_2012_65654()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", prog_num=65655):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", r".", prog_num=65656) as copy_file_to_dir_2013_65656:  # 0m:0.000s
                            copy_file_to_dir_2013_65656()
                        with ChmodAndChown(path=r"Waves-SSLComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65657) as chmod_and_chown_2014_65657:  # 0m:0.000s
                            chmod_and_chown_2014_65657()
            with Stage(r"copy", r"SSLEQ XML and Registry for Native Instruments", prog_num=65658):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65659) as should_copy_source_2015_65659:  # 0m:0.001s
                    should_copy_source_2015_65659()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", prog_num=65660):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", r".", prog_num=65661) as copy_file_to_dir_2016_65661:  # 0m:0.000s
                            copy_file_to_dir_2016_65661()
                        with ChmodAndChown(path=r"Waves-SSLEQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65662) as chmod_and_chown_2017_65662:  # 0m:0.000s
                            chmod_and_chown_2017_65662()
            with Stage(r"copy", r"SSL E-Channel XML and Registry for Native Instruments", prog_num=65663):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65664) as should_copy_source_2018_65664:  # 0m:0.001s
                    should_copy_source_2018_65664()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", prog_num=65665):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", r".", prog_num=65666) as copy_file_to_dir_2019_65666:  # 0m:0.000s
                            copy_file_to_dir_2019_65666()
                        with ChmodAndChown(path=r"Waves-SSL E-Channel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65667) as chmod_and_chown_2020_65667:  # 0m:0.000s
                            chmod_and_chown_2020_65667()
            with Stage(r"copy", r"SSL G-Channel XML and Registry for Native Instruments", prog_num=65668):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65669) as should_copy_source_2021_65669:  # 0m:0.001s
                    should_copy_source_2021_65669()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", prog_num=65670):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", r".", prog_num=65671) as copy_file_to_dir_2022_65671:  # 0m:0.000s
                            copy_file_to_dir_2022_65671()
                        with ChmodAndChown(path=r"Waves-SSL G-Channel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65672) as chmod_and_chown_2023_65672:  # 0m:0.000s
                            chmod_and_chown_2023_65672()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=65673):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65674) as should_copy_source_2024_65674:  # 0m:0.001s
                    should_copy_source_2024_65674()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=65675):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=65676) as copy_file_to_dir_2025_65676:  # 0m:0.000s
                            copy_file_to_dir_2025_65676()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65677) as chmod_and_chown_2026_65677:  # 0m:0.000s
                            chmod_and_chown_2026_65677()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=65678):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65679) as should_copy_source_2027_65679:  # 0m:0.001s
                    should_copy_source_2027_65679()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=65680):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=65681) as copy_file_to_dir_2028_65681:  # 0m:0.000s
                            copy_file_to_dir_2028_65681()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65682) as chmod_and_chown_2029_65682:  # 0m:0.000s
                            chmod_and_chown_2029_65682()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=65683):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65684) as should_copy_source_2030_65684:  # 0m:0.001s
                    should_copy_source_2030_65684()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=65685):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=65686) as copy_file_to_dir_2031_65686:  # 0m:0.000s
                            copy_file_to_dir_2031_65686()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65687) as chmod_and_chown_2032_65687:  # 0m:0.000s
                            chmod_and_chown_2032_65687()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=65688):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65689) as should_copy_source_2033_65689:  # 0m:0.001s
                    should_copy_source_2033_65689()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=65690):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=65691) as copy_file_to_dir_2034_65691:  # 0m:0.000s
                            copy_file_to_dir_2034_65691()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65692) as chmod_and_chown_2035_65692:  # 0m:0.000s
                            chmod_and_chown_2035_65692()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=65693):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65694) as should_copy_source_2036_65694:  # 0m:0.001s
                    should_copy_source_2036_65694()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=65695):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=65696) as copy_file_to_dir_2037_65696:  # 0m:0.000s
                            copy_file_to_dir_2037_65696()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65697) as chmod_and_chown_2038_65697:  # 0m:0.000s
                            chmod_and_chown_2038_65697()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=65698):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65699) as should_copy_source_2039_65699:  # 0m:0.001s
                    should_copy_source_2039_65699()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=65700):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=65701) as copy_file_to_dir_2040_65701:  # 0m:0.000s
                            copy_file_to_dir_2040_65701()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65702) as chmod_and_chown_2041_65702:  # 0m:0.000s
                            chmod_and_chown_2041_65702()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=65703):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65704) as should_copy_source_2042_65704:  # 0m:0.001s
                    should_copy_source_2042_65704()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=65705):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=65706) as copy_file_to_dir_2043_65706:  # 0m:0.000s
                            copy_file_to_dir_2043_65706()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65707) as chmod_and_chown_2044_65707:  # 0m:0.000s
                            chmod_and_chown_2044_65707()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=65708):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65709) as should_copy_source_2045_65709:  # 0m:0.001s
                    should_copy_source_2045_65709()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=65710):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=65711) as copy_file_to_dir_2046_65711:  # 0m:0.000s
                            copy_file_to_dir_2046_65711()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65712) as chmod_and_chown_2047_65712:  # 0m:0.000s
                            chmod_and_chown_2047_65712()
            with Stage(r"copy", r"Torque XML and Registry for Native Instruments", prog_num=65713):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65714) as should_copy_source_2048_65714:  # 0m:0.001s
                    should_copy_source_2048_65714()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", prog_num=65715):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", r".", prog_num=65716) as copy_file_to_dir_2049_65716:  # 0m:0.000s
                            copy_file_to_dir_2049_65716()
                        with ChmodAndChown(path=r"Waves-Torque Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65717) as chmod_and_chown_2050_65717:  # 0m:0.000s
                            chmod_and_chown_2050_65717()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=65718):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65719) as should_copy_source_2051_65719:  # 0m:0.001s
                    should_copy_source_2051_65719()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=65720):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=65721) as copy_file_to_dir_2052_65721:  # 0m:0.000s
                            copy_file_to_dir_2052_65721()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65722) as chmod_and_chown_2053_65722:  # 0m:0.000s
                            chmod_and_chown_2053_65722()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=65723):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65724) as should_copy_source_2054_65724:  # 0m:0.001s
                    should_copy_source_2054_65724()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=65725):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=65726) as copy_file_to_dir_2055_65726:  # 0m:0.000s
                            copy_file_to_dir_2055_65726()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65727) as chmod_and_chown_2056_65727:  # 0m:0.000s
                            chmod_and_chown_2056_65727()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=65728):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65729) as should_copy_source_2057_65729:  # 0m:0.001s
                    should_copy_source_2057_65729()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=65730):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=65731) as copy_file_to_dir_2058_65731:  # 0m:0.000s
                            copy_file_to_dir_2058_65731()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65732) as chmod_and_chown_2059_65732:  # 0m:0.000s
                            chmod_and_chown_2059_65732()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=65733):  # 0m:0.002s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65734) as should_copy_source_2060_65734:  # 0m:0.001s
                    should_copy_source_2060_65734()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=65735):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=65736) as copy_file_to_dir_2061_65736:  # 0m:0.000s
                            copy_file_to_dir_2061_65736()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65737) as chmod_and_chown_2062_65737:  # 0m:0.000s
                            chmod_and_chown_2062_65737()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65738) as should_copy_source_2063_65738:  # 0m:0.001s
                    should_copy_source_2063_65738()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=65739):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=65740) as copy_file_to_dir_2064_65740:  # 0m:0.000s
                            copy_file_to_dir_2064_65740()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65741) as chmod_and_chown_2065_65741:  # 0m:0.000s
                            chmod_and_chown_2065_65741()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65742) as should_copy_source_2066_65742:  # 0m:0.001s
                    should_copy_source_2066_65742()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=65743):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=65744) as copy_file_to_dir_2067_65744:  # 0m:0.000s
                            copy_file_to_dir_2067_65744()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65745) as chmod_and_chown_2068_65745:  # 0m:0.000s
                            chmod_and_chown_2068_65745()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=65746):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65747) as should_copy_source_2069_65747:  # 0m:0.001s
                    should_copy_source_2069_65747()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=65748):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=65749) as copy_file_to_dir_2070_65749:  # 0m:0.000s
                            copy_file_to_dir_2070_65749()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65750) as chmod_and_chown_2071_65750:  # 0m:0.000s
                            chmod_and_chown_2071_65750()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=65751):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65752) as should_copy_source_2072_65752:  # 0m:0.001s
                    should_copy_source_2072_65752()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=65753):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=65754) as copy_file_to_dir_2073_65754:  # 0m:0.000s
                            copy_file_to_dir_2073_65754()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65755) as chmod_and_chown_2074_65755:  # 0m:0.000s
                            chmod_and_chown_2074_65755()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=65756):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65757) as should_copy_source_2075_65757:  # 0m:0.001s
                    should_copy_source_2075_65757()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=65758):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=65759) as copy_file_to_dir_2076_65759:  # 0m:0.000s
                            copy_file_to_dir_2076_65759()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65760) as chmod_and_chown_2077_65760:  # 0m:0.000s
                            chmod_and_chown_2077_65760()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=65761):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65762) as should_copy_source_2078_65762:  # 0m:0.001s
                    should_copy_source_2078_65762()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=65763):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=65764) as copy_file_to_dir_2079_65764:  # 0m:0.000s
                            copy_file_to_dir_2079_65764()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65765) as chmod_and_chown_2080_65765:  # 0m:0.000s
                            chmod_and_chown_2080_65765()
            with Stage(r"copy", r"W43 XML and Registry for Native Instruments", prog_num=65766):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65767) as should_copy_source_2081_65767:  # 0m:0.001s
                    should_copy_source_2081_65767()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", prog_num=65768):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", r".", prog_num=65769) as copy_file_to_dir_2082_65769:  # 0m:0.000s
                            copy_file_to_dir_2082_65769()
                        with ChmodAndChown(path=r"Waves-W43 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65770) as chmod_and_chown_2083_65770:  # 0m:0.000s
                            chmod_and_chown_2083_65770()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=65771):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65772) as should_copy_source_2084_65772:  # 0m:0.001s
                    should_copy_source_2084_65772()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=65773):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=65774) as copy_file_to_dir_2085_65774:  # 0m:0.000s
                            copy_file_to_dir_2085_65774()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65775) as chmod_and_chown_2086_65775:  # 0m:0.000s
                            chmod_and_chown_2086_65775()
            with Stage(r"copy", r"WNS XML and Registry for Native Instruments", prog_num=65776):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65777) as should_copy_source_2087_65777:  # 0m:0.001s
                    should_copy_source_2087_65777()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", prog_num=65778):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", r".", prog_num=65779) as copy_file_to_dir_2088_65779:  # 0m:0.000s
                            copy_file_to_dir_2088_65779()
                        with ChmodAndChown(path=r"Waves-WNS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65780) as chmod_and_chown_2089_65780:  # 0m:0.000s
                            chmod_and_chown_2089_65780()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=65781):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65782) as should_copy_source_2090_65782:  # 0m:0.001s
                    should_copy_source_2090_65782()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=65783):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=65784) as copy_file_to_dir_2091_65784:  # 0m:0.000s
                            copy_file_to_dir_2091_65784()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65785) as chmod_and_chown_2092_65785:  # 0m:0.000s
                            chmod_and_chown_2092_65785()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=65786):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65787) as should_copy_source_2093_65787:  # 0m:0.001s
                    should_copy_source_2093_65787()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=65788):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=65789) as copy_file_to_dir_2094_65789:  # 0m:0.000s
                            copy_file_to_dir_2094_65789()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65790) as chmod_and_chown_2095_65790:  # 0m:0.000s
                            chmod_and_chown_2095_65790()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=65791):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65792) as should_copy_source_2096_65792:  # 0m:0.001s
                    should_copy_source_2096_65792()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=65793):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=65794) as copy_file_to_dir_2097_65794:  # 0m:0.000s
                            copy_file_to_dir_2097_65794()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65795) as chmod_and_chown_2098_65795:  # 0m:0.000s
                            chmod_and_chown_2098_65795()
            with Stage(r"copy", r"dbx-160 XML and Registry for Native Instruments", prog_num=65796):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65797) as should_copy_source_2099_65797:  # 0m:0.001s
                    should_copy_source_2099_65797()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", prog_num=65798):  # 0m:0.001s
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", r".", prog_num=65799) as copy_file_to_dir_2100_65799:  # 0m:0.000s
                            copy_file_to_dir_2100_65799()
                        with ChmodAndChown(path=r"Waves-dbx-160 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65800) as chmod_and_chown_2101_65800:  # 0m:0.000s
                            chmod_and_chown_2101_65800()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=65801) as resolve_config_vars_in_file_2102_65801:  # 0m:0.001s
                resolve_config_vars_in_file_2102_65801()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=65802) as if_2103_65802:  # 0m:0.000s
                if_2103_65802()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=65803) as resolve_config_vars_in_file_2104_65803:  # 0m:0.000s
                resolve_config_vars_in_file_2104_65803()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=65804) as if_2105_65804:  # 0m:0.000s
                if_2105_65804()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Fingers", "NKS_DATA_VERSION": "1.0"}, prog_num=65805) as resolve_config_vars_in_file_2106_65805:  # 0m:0.000s
                resolve_config_vars_in_file_2106_65805()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Fingers Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Fingers Stereo.plist", ignore_all_errors=True), prog_num=65806) as if_2107_65806:  # 0m:0.000s
                if_2107_65806()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=65807) as resolve_config_vars_in_file_2108_65807:  # 0m:0.000s
                resolve_config_vars_in_file_2108_65807()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=65808) as if_2109_65808:  # 0m:0.000s
                if_2109_65808()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=65809) as resolve_config_vars_in_file_2110_65809:  # 0m:0.000s
                resolve_config_vars_in_file_2110_65809()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=65810) as if_2111_65810:  # 0m:0.000s
                if_2111_65810()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=65811) as resolve_config_vars_in_file_2112_65811:  # 0m:0.000s
                resolve_config_vars_in_file_2112_65811()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=65812) as if_2113_65812:  # 0m:0.000s
                if_2113_65812()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=65813) as resolve_config_vars_in_file_2114_65813:  # 0m:0.000s
                resolve_config_vars_in_file_2114_65813()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=65814) as if_2115_65814:  # 0m:0.000s
                if_2115_65814()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=65815) as resolve_config_vars_in_file_2116_65815:  # 0m:0.000s
                resolve_config_vars_in_file_2116_65815()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=65816) as if_2117_65816:  # 0m:0.000s
                if_2117_65816()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=65817) as resolve_config_vars_in_file_2118_65817:  # 0m:0.000s
                resolve_config_vars_in_file_2118_65817()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=65818) as if_2119_65818:  # 0m:0.000s
                if_2119_65818()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C6", "NKS_DATA_VERSION": "1.0"}, prog_num=65819) as resolve_config_vars_in_file_2120_65819:  # 0m:0.000s
                resolve_config_vars_in_file_2120_65819()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C6 Stereo.plist", ignore_all_errors=True), prog_num=65820) as if_2121_65820:  # 0m:0.000s
                if_2121_65820()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=65821) as resolve_config_vars_in_file_2122_65821:  # 0m:0.000s
                resolve_config_vars_in_file_2122_65821()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=65822) as if_2123_65822:  # 0m:0.000s
                if_2123_65822()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=65823) as resolve_config_vars_in_file_2124_65823:  # 0m:0.000s
                resolve_config_vars_in_file_2124_65823()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=65824) as if_2125_65824:  # 0m:0.000s
                if_2125_65824()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=65825) as resolve_config_vars_in_file_2126_65825:  # 0m:0.000s
                resolve_config_vars_in_file_2126_65825()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=65826) as if_2127_65826:  # 0m:0.000s
                if_2127_65826()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CODEX", "NKS_DATA_VERSION": "1.0"}, prog_num=65827) as resolve_config_vars_in_file_2128_65827:  # 0m:0.000s
                resolve_config_vars_in_file_2128_65827()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CODEX Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CODEX Stereo.plist", ignore_all_errors=True), prog_num=65828) as if_2129_65828:  # 0m:0.000s
                if_2129_65828()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=65829) as resolve_config_vars_in_file_2130_65829:  # 0m:0.000s
                resolve_config_vars_in_file_2130_65829()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=65830) as if_2131_65830:  # 0m:0.000s
                if_2131_65830()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Clavinet", "NKS_DATA_VERSION": "1.0"}, prog_num=65831) as resolve_config_vars_in_file_2132_65831:  # 0m:0.000s
                resolve_config_vars_in_file_2132_65831()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Clavinet Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Clavinet Stereo.plist", ignore_all_errors=True), prog_num=65832) as if_2133_65832:  # 0m:0.000s
                if_2133_65832()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "DPR-402", "NKS_DATA_VERSION": "1.0"}, prog_num=65833) as resolve_config_vars_in_file_2134_65833:  # 0m:0.000s
                resolve_config_vars_in_file_2134_65833()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-DPR-402 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-DPR-402 Stereo.plist", ignore_all_errors=True), prog_num=65834) as if_2135_65834:  # 0m:0.000s
                if_2135_65834()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Dorrough", "NKS_DATA_VERSION": "1.0"}, prog_num=65835) as resolve_config_vars_in_file_2136_65835:  # 0m:0.000s
                resolve_config_vars_in_file_2136_65835()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Dorrough Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Dorrough Stereo.plist", ignore_all_errors=True), prog_num=65836) as if_2137_65836:  # 0m:0.000s
                if_2137_65836()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-D5", "NKS_DATA_VERSION": "1.0"}, prog_num=65837) as resolve_config_vars_in_file_2138_65837:  # 0m:0.000s
                resolve_config_vars_in_file_2138_65837()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True), prog_num=65838) as if_2139_65838:  # 0m:0.000s
                if_2139_65838()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=65839) as resolve_config_vars_in_file_2140_65839:  # 0m:0.000s
                resolve_config_vars_in_file_2140_65839()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=65840) as if_2141_65840:  # 0m:0.000s
                if_2141_65840()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=65841) as resolve_config_vars_in_file_2142_65841:  # 0m:0.000s
                resolve_config_vars_in_file_2142_65841()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=65842) as if_2143_65842:  # 0m:0.000s
                if_2143_65842()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric200", "NKS_DATA_VERSION": "1.0"}, prog_num=65843) as resolve_config_vars_in_file_2144_65843:  # 0m:0.000s
                resolve_config_vars_in_file_2144_65843()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric200 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric200 Stereo.plist", ignore_all_errors=True), prog_num=65844) as if_2145_65844:  # 0m:0.000s
                if_2145_65844()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric88", "NKS_DATA_VERSION": "1.0"}, prog_num=65845) as resolve_config_vars_in_file_2146_65845:  # 0m:0.000s
                resolve_config_vars_in_file_2146_65845()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric88 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric88 Stereo.plist", ignore_all_errors=True), prog_num=65846) as if_2147_65846:  # 0m:0.000s
                if_2147_65846()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=65847) as resolve_config_vars_in_file_2148_65847:  # 0m:0.000s
                resolve_config_vars_in_file_2148_65847()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=65848) as if_2149_65848:  # 0m:0.000s
                if_2149_65848()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Element", "NKS_DATA_VERSION": "1.0"}, prog_num=65849) as resolve_config_vars_in_file_2150_65849:  # 0m:0.000s
                resolve_config_vars_in_file_2150_65849()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Element Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Element Stereo.plist", ignore_all_errors=True), prog_num=65850) as if_2151_65850:  # 0m:0.000s
                if_2151_65850()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=65851) as resolve_config_vars_in_file_2152_65851:  # 0m:0.000s
                resolve_config_vars_in_file_2152_65851()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=65852) as if_2153_65852:  # 0m:0.000s
                if_2153_65852()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "F6", "NKS_DATA_VERSION": "1.0"}, prog_num=65853) as resolve_config_vars_in_file_2154_65853:  # 0m:0.000s
                resolve_config_vars_in_file_2154_65853()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-F6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-F6 Stereo.plist", ignore_all_errors=True), prog_num=65854) as if_2155_65854:  # 0m:0.000s
                if_2155_65854()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Flow Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=65855) as resolve_config_vars_in_file_2156_65855:  # 0m:0.000s
                resolve_config_vars_in_file_2156_65855()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Flow Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Flow Motion Stereo.plist", ignore_all_errors=True), prog_num=65856) as if_2157_65856:  # 0m:0.000s
                if_2157_65856()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GEQ Classic", "NKS_DATA_VERSION": "1.0"}, prog_num=65857) as resolve_config_vars_in_file_2158_65857:  # 0m:0.000s
                resolve_config_vars_in_file_2158_65857()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Classic Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Classic Stereo.plist", ignore_all_errors=True), prog_num=65858) as if_2159_65858:  # 0m:0.000s
                if_2159_65858()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GEQ Modern", "NKS_DATA_VERSION": "1.0"}, prog_num=65859) as resolve_config_vars_in_file_2160_65859:  # 0m:0.000s
                resolve_config_vars_in_file_2160_65859()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Modern Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Modern Stereo.plist", ignore_all_errors=True), prog_num=65860) as if_2161_65860:  # 0m:0.000s
                if_2161_65860()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Grand Rhapsody", "NKS_DATA_VERSION": "1.0"}, prog_num=65861) as resolve_config_vars_in_file_2162_65861:  # 0m:0.000s
                resolve_config_vars_in_file_2162_65861()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", ignore_all_errors=True), prog_num=65862) as if_2163_65862:  # 0m:0.000s
                if_2163_65862()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Piano Stereo.plist", prog_num=65863) as rm_file_or_dir_2164_65863:  # 0m:0.000s
                rm_file_or_dir_2164_65863()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65864) as resolve_config_vars_in_file_2165_65864:  # 0m:0.000s
                resolve_config_vars_in_file_2165_65864()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=65865) as if_2166_65865:  # 0m:0.000s
                if_2166_65865()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65866) as resolve_config_vars_in_file_2167_65866:  # 0m:0.001s
                resolve_config_vars_in_file_2167_65866()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=65867) as if_2168_65867:  # 0m:0.000s
                if_2168_65867()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65868) as resolve_config_vars_in_file_2169_65868:  # 0m:0.000s
                resolve_config_vars_in_file_2169_65868()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=65869) as if_2170_65869:  # 0m:0.000s
                if_2170_65869()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW VoiceCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65870) as resolve_config_vars_in_file_2171_65870:  # 0m:0.000s
                resolve_config_vars_in_file_2171_65870()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", ignore_all_errors=True), prog_num=65871) as if_2172_65871:  # 0m:0.000s
                if_2172_65871()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=65872) as resolve_config_vars_in_file_2173_65872:  # 0m:0.000s
                resolve_config_vars_in_file_2173_65872()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=65873) as if_2174_65873:  # 0m:0.000s
                if_2174_65873()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-EQ", "NKS_DATA_VERSION": "1.0"}, prog_num=65874) as resolve_config_vars_in_file_2175_65874:  # 0m:0.000s
                resolve_config_vars_in_file_2175_65874()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-EQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-EQ Stereo.plist", ignore_all_errors=True), prog_num=65875) as if_2176_65875:  # 0m:0.000s
                if_2176_65875()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=65876) as resolve_config_vars_in_file_2177_65876:  # 0m:0.000s
                resolve_config_vars_in_file_2177_65876()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=65877) as if_2178_65877:  # 0m:0.000s
                if_2178_65877()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "IMPusher", "NKS_DATA_VERSION": "1.0"}, prog_num=65878) as resolve_config_vars_in_file_2179_65878:  # 0m:0.000s
                resolve_config_vars_in_file_2179_65878()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IMPusher Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IMPusher Stereo.plist", ignore_all_errors=True), prog_num=65879) as if_2180_65879:  # 0m:0.000s
                if_2180_65879()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "IRLive", "NKS_DATA_VERSION": "1.0"}, prog_num=65880) as resolve_config_vars_in_file_2181_65880:  # 0m:0.000s
                resolve_config_vars_in_file_2181_65880()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IRLive Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IRLive Stereo.plist", ignore_all_errors=True), prog_num=65881) as if_2182_65881:  # 0m:0.000s
                if_2182_65881()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=65882) as resolve_config_vars_in_file_2183_65882:  # 0m:0.000s
                resolve_config_vars_in_file_2183_65882()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=65883) as if_2184_65883:  # 0m:0.000s
                if_2184_65883()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=65884) as resolve_config_vars_in_file_2185_65884:  # 0m:0.000s
                resolve_config_vars_in_file_2185_65884()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=65885) as if_2186_65885:  # 0m:0.000s
                if_2186_65885()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Bass", "NKS_DATA_VERSION": "1.0"}, prog_num=65886) as resolve_config_vars_in_file_2187_65886:  # 0m:0.000s
                resolve_config_vars_in_file_2187_65886()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Bass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Bass Stereo.plist", ignore_all_errors=True), prog_num=65887) as if_2188_65887:  # 0m:0.000s
                if_2188_65887()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Cymb-Perc", "NKS_DATA_VERSION": "1.0"}, prog_num=65888) as resolve_config_vars_in_file_2189_65888:  # 0m:0.000s
                resolve_config_vars_in_file_2189_65888()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", ignore_all_errors=True), prog_num=65889) as if_2190_65889:  # 0m:0.000s
                if_2190_65889()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Drums", "NKS_DATA_VERSION": "1.0"}, prog_num=65890) as resolve_config_vars_in_file_2191_65890:  # 0m:0.000s
                resolve_config_vars_in_file_2191_65890()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Drums Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Drums Stereo.plist", ignore_all_errors=True), prog_num=65891) as if_2192_65891:  # 0m:0.000s
                if_2192_65891()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Guitars", "NKS_DATA_VERSION": "1.0"}, prog_num=65892) as resolve_config_vars_in_file_2193_65892:  # 0m:0.000s
                resolve_config_vars_in_file_2193_65892()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Guitars Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Guitars Stereo.plist", ignore_all_errors=True), prog_num=65893) as if_2194_65893:  # 0m:0.000s
                if_2194_65893()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Strings-Keys", "NKS_DATA_VERSION": "1.0"}, prog_num=65894) as resolve_config_vars_in_file_2195_65894:  # 0m:0.000s
                resolve_config_vars_in_file_2195_65894()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", ignore_all_errors=True), prog_num=65895) as if_2196_65895:  # 0m:0.000s
                if_2196_65895()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=65896) as resolve_config_vars_in_file_2197_65896:  # 0m:0.000s
                resolve_config_vars_in_file_2197_65896()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=65897) as if_2198_65897:  # 0m:0.000s
                if_2198_65897()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=65898) as rm_file_or_dir_2199_65898:  # 0m:0.000s
                rm_file_or_dir_2199_65898()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=65899) as resolve_config_vars_in_file_2200_65899:  # 0m:0.000s
                resolve_config_vars_in_file_2200_65899()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=65900) as if_2201_65900:  # 0m:0.000s
                if_2201_65900()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=65901) as rm_file_or_dir_2202_65901:  # 0m:0.000s
                rm_file_or_dir_2202_65901()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=65902) as resolve_config_vars_in_file_2203_65902:  # 0m:0.000s
                resolve_config_vars_in_file_2203_65902()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=65903) as if_2204_65903:  # 0m:0.000s
                if_2204_65903()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=65904) as resolve_config_vars_in_file_2205_65904:  # 0m:0.000s
                resolve_config_vars_in_file_2205_65904()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=65905) as if_2206_65905:  # 0m:0.000s
                if_2206_65905()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=65906) as resolve_config_vars_in_file_2207_65906:  # 0m:0.000s
                resolve_config_vars_in_file_2207_65906()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=65907) as if_2208_65907:  # 0m:0.000s
                if_2208_65907()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=65908) as resolve_config_vars_in_file_2209_65908:  # 0m:0.000s
                resolve_config_vars_in_file_2209_65908()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=65909) as if_2210_65909:  # 0m:0.000s
                if_2210_65909()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=65910) as resolve_config_vars_in_file_2211_65910:  # 0m:0.000s
                resolve_config_vars_in_file_2211_65910()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=65911) as if_2212_65911:  # 0m:0.000s
                if_2212_65911()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=65912) as resolve_config_vars_in_file_2213_65912:  # 0m:0.000s
                resolve_config_vars_in_file_2213_65912()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=65913) as if_2214_65913:  # 0m:0.000s
                if_2214_65913()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=65914) as resolve_config_vars_in_file_2215_65914:  # 0m:0.000s
                resolve_config_vars_in_file_2215_65914()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=65915) as if_2216_65915:  # 0m:0.000s
                if_2216_65915()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=65916) as resolve_config_vars_in_file_2217_65916:  # 0m:0.000s
                resolve_config_vars_in_file_2217_65916()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=65917) as if_2218_65917:  # 0m:0.000s
                if_2218_65917()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=65918) as resolve_config_vars_in_file_2219_65918:  # 0m:0.000s
                resolve_config_vars_in_file_2219_65918()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=65919) as if_2220_65919:  # 0m:0.000s
                if_2220_65919()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=65920) as resolve_config_vars_in_file_2221_65920:  # 0m:0.000s
                resolve_config_vars_in_file_2221_65920()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=65921) as if_2222_65921:  # 0m:0.000s
                if_2222_65921()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=65922) as resolve_config_vars_in_file_2223_65922:  # 0m:0.000s
                resolve_config_vars_in_file_2223_65922()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=65923) as if_2224_65923:  # 0m:0.000s
                if_2224_65923()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=65924) as resolve_config_vars_in_file_2225_65924:  # 0m:0.000s
                resolve_config_vars_in_file_2225_65924()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True), prog_num=65925) as if_2226_65925:  # 0m:0.000s
                if_2226_65925()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM Distortion", "NKS_DATA_VERSION": "1.0"}, prog_num=65926) as resolve_config_vars_in_file_2227_65926:  # 0m:0.000s
                resolve_config_vars_in_file_2227_65926()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM Distortion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM Distortion Stereo.plist", ignore_all_errors=True), prog_num=65927) as if_2228_65927:  # 0m:0.000s
                if_2228_65927()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-EQ", "NKS_DATA_VERSION": "1.0"}, prog_num=65928) as resolve_config_vars_in_file_2229_65928:  # 0m:0.000s
                resolve_config_vars_in_file_2229_65928()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-EQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-EQ Stereo.plist", ignore_all_errors=True), prog_num=65929) as if_2230_65929:  # 0m:0.000s
                if_2230_65929()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMReverb Stereo.xml", prog_num=65930) as rm_file_or_dir_2231_65930:  # 0m:0.000s
                rm_file_or_dir_2231_65930()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MannyM Reverb Stereo.xml", prog_num=65931) as rm_file_or_dir_2232_65931:  # 0m:0.000s
                rm_file_or_dir_2232_65931()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-Reverb", "NKS_DATA_VERSION": "1.0"}, prog_num=65932) as resolve_config_vars_in_file_2233_65932:  # 0m:0.000s
                resolve_config_vars_in_file_2233_65932()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", ignore_all_errors=True), prog_num=65933) as if_2234_65933:  # 0m:0.000s
                if_2234_65933()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMReverb Stereo.plist", prog_num=65934) as rm_file_or_dir_2235_65934:  # 0m:0.000s
                rm_file_or_dir_2235_65934()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MannyM Reverb Stereo.plist", prog_num=65935) as rm_file_or_dir_2236_65935:  # 0m:0.000s
                rm_file_or_dir_2236_65935()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMToneShaper Stereo.xml", prog_num=65936) as rm_file_or_dir_2237_65936:  # 0m:0.000s
                rm_file_or_dir_2237_65936()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMTShaper Stereo.xml", prog_num=65937) as rm_file_or_dir_2238_65937:  # 0m:0.000s
                rm_file_or_dir_2238_65937()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-ToneShaper", "NKS_DATA_VERSION": "1.0"}, prog_num=65938) as resolve_config_vars_in_file_2239_65938:  # 0m:0.000s
                resolve_config_vars_in_file_2239_65938()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", ignore_all_errors=True), prog_num=65939) as if_2240_65939:  # 0m:0.000s
                if_2240_65939()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMToneShaper Stereo.plist", prog_num=65940) as rm_file_or_dir_2241_65940:  # 0m:0.000s
                rm_file_or_dir_2241_65940()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMTShaper Stereo.plist", prog_num=65941) as rm_file_or_dir_2242_65941:  # 0m:0.000s
                rm_file_or_dir_2242_65941()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=65942) as resolve_config_vars_in_file_2243_65942:  # 0m:0.000s
                resolve_config_vars_in_file_2243_65942()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=65943) as if_2244_65943:  # 0m:0.000s
                if_2244_65943()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=65944) as resolve_config_vars_in_file_2245_65944:  # 0m:0.000s
                resolve_config_vars_in_file_2245_65944()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=65945) as if_2246_65945:  # 0m:0.000s
                if_2246_65945()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=65946) as resolve_config_vars_in_file_2247_65946:  # 0m:0.000s
                resolve_config_vars_in_file_2247_65946()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=65947) as if_2248_65947:  # 0m:0.000s
                if_2248_65947()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=65948) as resolve_config_vars_in_file_2249_65948:  # 0m:0.000s
                resolve_config_vars_in_file_2249_65948()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=65949) as if_2250_65949:  # 0m:0.000s
                if_2250_65949()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=65950) as resolve_config_vars_in_file_2251_65950:  # 0m:0.000s
                resolve_config_vars_in_file_2251_65950()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=65951) as if_2252_65951:  # 0m:0.000s
                if_2252_65951()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Brighter", "NKS_DATA_VERSION": "1.0"}, prog_num=65952) as resolve_config_vars_in_file_2253_65952:  # 0m:0.000s
                resolve_config_vars_in_file_2253_65952()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", ignore_all_errors=True), prog_num=65953) as if_2254_65953:  # 0m:0.000s
                if_2254_65953()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=65954) as resolve_config_vars_in_file_2255_65954:  # 0m:0.000s
                resolve_config_vars_in_file_2255_65954()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=65955) as if_2256_65955:  # 0m:0.000s
                if_2256_65955()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=65956) as resolve_config_vars_in_file_2257_65956:  # 0m:0.000s
                resolve_config_vars_in_file_2257_65956()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=65957) as if_2258_65957:  # 0m:0.000s
                if_2258_65957()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Louder", "NKS_DATA_VERSION": "1.0"}, prog_num=65958) as resolve_config_vars_in_file_2259_65958:  # 0m:0.000s
                resolve_config_vars_in_file_2259_65958()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Louder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Louder Stereo.plist", ignore_all_errors=True), prog_num=65959) as if_2260_65959:  # 0m:0.000s
                if_2260_65959()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=65960) as resolve_config_vars_in_file_2261_65960:  # 0m:0.000s
                resolve_config_vars_in_file_2261_65960()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=65961) as if_2262_65961:  # 0m:0.000s
                if_2262_65961()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pressure", "NKS_DATA_VERSION": "1.0"}, prog_num=65962) as resolve_config_vars_in_file_2263_65962:  # 0m:0.000s
                resolve_config_vars_in_file_2263_65962()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", ignore_all_errors=True), prog_num=65963) as if_2264_65963:  # 0m:0.000s
                if_2264_65963()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=65964) as resolve_config_vars_in_file_2265_65964:  # 0m:0.000s
                resolve_config_vars_in_file_2265_65964()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=65965) as if_2266_65965:  # 0m:0.000s
                if_2266_65965()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Wetter", "NKS_DATA_VERSION": "1.0"}, prog_num=65966) as resolve_config_vars_in_file_2267_65966:  # 0m:0.000s
                resolve_config_vars_in_file_2267_65966()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", ignore_all_errors=True), prog_num=65967) as if_2268_65967:  # 0m:0.000s
                if_2268_65967()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OVox", "NKS_DATA_VERSION": "1.0"}, prog_num=65968) as resolve_config_vars_in_file_2269_65968:  # 0m:0.000s
                resolve_config_vars_in_file_2269_65968()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True), prog_num=65969) as if_2270_65969:  # 0m:0.000s
                if_2270_65969()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=65970) as resolve_config_vars_in_file_2271_65970:  # 0m:0.000s
                resolve_config_vars_in_file_2271_65970()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=65971) as if_2272_65971:  # 0m:0.000s
                if_2272_65971()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS Archon", "NKS_DATA_VERSION": "1.0"}, prog_num=65972) as resolve_config_vars_in_file_2273_65972:  # 0m:0.000s
                resolve_config_vars_in_file_2273_65972()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Archon Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Archon Stereo.plist", ignore_all_errors=True), prog_num=65973) as if_2274_65973:  # 0m:0.000s
                if_2274_65973()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS Dallas", "NKS_DATA_VERSION": "1.0"}, prog_num=65974) as resolve_config_vars_in_file_2275_65974:  # 0m:0.000s
                resolve_config_vars_in_file_2275_65974()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Dallas Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Dallas Stereo.plist", ignore_all_errors=True), prog_num=65975) as if_2276_65975:  # 0m:0.000s
                if_2276_65975()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS V9", "NKS_DATA_VERSION": "1.0"}, prog_num=65976) as resolve_config_vars_in_file_2277_65976:  # 0m:0.000s
                resolve_config_vars_in_file_2277_65976()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS V9 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS V9 Stereo.plist", ignore_all_errors=True), prog_num=65977) as if_2278_65977:  # 0m:0.000s
                if_2278_65977()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=65978) as resolve_config_vars_in_file_2279_65978:  # 0m:0.000s
                resolve_config_vars_in_file_2279_65978()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=65979) as if_2280_65979:  # 0m:0.000s
                if_2280_65979()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=65980) as resolve_config_vars_in_file_2281_65980:  # 0m:0.000s
                resolve_config_vars_in_file_2281_65980()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=65981) as if_2282_65981:  # 0m:0.000s
                if_2282_65981()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=65982) as move_file_to_file_2283_65982:  # 0m:0.011s
                move_file_to_file_2283_65982()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=65983) as resolve_config_vars_in_file_2284_65983:  # 0m:0.001s
                resolve_config_vars_in_file_2284_65983()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=65984) as if_2285_65984:  # 0m:0.000s
                if_2285_65984()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=65985) as resolve_config_vars_in_file_2286_65985:  # 0m:0.000s
                resolve_config_vars_in_file_2286_65985()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=65986) as if_2287_65986:  # 0m:0.000s
                if_2287_65986()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=65987) as resolve_config_vars_in_file_2288_65987:  # 0m:0.000s
                resolve_config_vars_in_file_2288_65987()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=65988) as if_2289_65988:  # 0m:0.000s
                if_2289_65988()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=65989) as resolve_config_vars_in_file_2290_65989:  # 0m:0.000s
                resolve_config_vars_in_file_2290_65989()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=65990) as if_2291_65990:  # 0m:0.000s
                if_2291_65990()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=65991) as resolve_config_vars_in_file_2292_65991:  # 0m:0.000s
                resolve_config_vars_in_file_2292_65991()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=65992) as if_2293_65992:  # 0m:0.000s
                if_2293_65992()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=65993) as resolve_config_vars_in_file_2294_65993:  # 0m:0.000s
                resolve_config_vars_in_file_2294_65993()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=65994) as if_2295_65994:  # 0m:0.000s
                if_2295_65994()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=65995) as resolve_config_vars_in_file_2296_65995:  # 0m:0.000s
                resolve_config_vars_in_file_2296_65995()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=65996) as if_2297_65996:  # 0m:0.000s
                if_2297_65996()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=65997) as resolve_config_vars_in_file_2298_65997:  # 0m:0.000s
                resolve_config_vars_in_file_2298_65997()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=65998) as if_2299_65998:  # 0m:0.000s
                if_2299_65998()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=65999) as resolve_config_vars_in_file_2300_65999:  # 0m:0.000s
                resolve_config_vars_in_file_2300_65999()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=66000) as if_2301_66000:  # 0m:0.000s
                if_2301_66000()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=66001) as resolve_config_vars_in_file_2302_66001:  # 0m:0.000s
                resolve_config_vars_in_file_2302_66001()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=66002) as if_2303_66002:  # 0m:0.000s
                if_2303_66002()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=66003) as resolve_config_vars_in_file_2304_66003:  # 0m:0.000s
                resolve_config_vars_in_file_2304_66003()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=66004) as if_2305_66004:  # 0m:0.000s
                if_2305_66004()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=66005) as resolve_config_vars_in_file_2306_66005:  # 0m:0.000s
                resolve_config_vars_in_file_2306_66005()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=66006) as if_2307_66006:  # 0m:0.000s
                if_2307_66006()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=66007) as resolve_config_vars_in_file_2308_66007:  # 0m:0.000s
                resolve_config_vars_in_file_2308_66007()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=66008) as if_2309_66008:  # 0m:0.000s
                if_2309_66008()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=66009) as resolve_config_vars_in_file_2310_66009:  # 0m:0.000s
                resolve_config_vars_in_file_2310_66009()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=66010) as if_2311_66010:  # 0m:0.000s
                if_2311_66010()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=66011) as resolve_config_vars_in_file_2312_66011:  # 0m:0.000s
                resolve_config_vars_in_file_2312_66011()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=66012) as if_2313_66012:  # 0m:0.000s
                if_2313_66012()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=66013) as resolve_config_vars_in_file_2314_66013:  # 0m:0.000s
                resolve_config_vars_in_file_2314_66013()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=66014) as if_2315_66014:  # 0m:0.000s
                if_2315_66014()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=66015) as resolve_config_vars_in_file_2316_66015:  # 0m:0.000s
                resolve_config_vars_in_file_2316_66015()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=66016) as if_2317_66016:  # 0m:0.000s
                if_2317_66016()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSLComp", "NKS_DATA_VERSION": "1.0"}, prog_num=66017) as resolve_config_vars_in_file_2318_66017:  # 0m:0.000s
                resolve_config_vars_in_file_2318_66017()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLComp Stereo.plist", ignore_all_errors=True), prog_num=66018) as if_2319_66018:  # 0m:0.000s
                if_2319_66018()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSLEQ", "NKS_DATA_VERSION": "1.0"}, prog_num=66019) as resolve_config_vars_in_file_2320_66019:  # 0m:0.000s
                resolve_config_vars_in_file_2320_66019()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLEQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLEQ Stereo.plist", ignore_all_errors=True), prog_num=66020) as if_2321_66020:  # 0m:0.000s
                if_2321_66020()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSL E-Channel", "NKS_DATA_VERSION": "1.0"}, prog_num=66021) as resolve_config_vars_in_file_2322_66021:  # 0m:0.000s
                resolve_config_vars_in_file_2322_66021()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL E-Channel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL E-Channel Stereo.plist", ignore_all_errors=True), prog_num=66022) as if_2323_66022:  # 0m:0.000s
                if_2323_66022()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSL G-Channel", "NKS_DATA_VERSION": "1.0"}, prog_num=66023) as resolve_config_vars_in_file_2324_66023:  # 0m:0.000s
                resolve_config_vars_in_file_2324_66023()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL G-Channel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL G-Channel Stereo.plist", ignore_all_errors=True), prog_num=66024) as if_2325_66024:  # 0m:0.000s
                if_2325_66024()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=66025) as resolve_config_vars_in_file_2326_66025:  # 0m:0.000s
                resolve_config_vars_in_file_2326_66025()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=66026) as if_2327_66026:  # 0m:0.000s
                if_2327_66026()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=66027) as resolve_config_vars_in_file_2328_66027:  # 0m:0.000s
                resolve_config_vars_in_file_2328_66027()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=66028) as if_2329_66028:  # 0m:0.000s
                if_2329_66028()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=66029) as resolve_config_vars_in_file_2330_66029:  # 0m:0.000s
                resolve_config_vars_in_file_2330_66029()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=66030) as if_2331_66030:  # 0m:0.000s
                if_2331_66030()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=66031) as resolve_config_vars_in_file_2332_66031:  # 0m:0.000s
                resolve_config_vars_in_file_2332_66031()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=66032) as if_2333_66032:  # 0m:0.000s
                if_2333_66032()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=66033) as resolve_config_vars_in_file_2334_66033:  # 0m:0.000s
                resolve_config_vars_in_file_2334_66033()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=66034) as if_2335_66034:  # 0m:0.000s
                if_2335_66034()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=66035) as resolve_config_vars_in_file_2336_66035:  # 0m:0.000s
                resolve_config_vars_in_file_2336_66035()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=66036) as if_2337_66036:  # 0m:0.000s
                if_2337_66036()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=66037) as resolve_config_vars_in_file_2338_66037:  # 0m:0.000s
                resolve_config_vars_in_file_2338_66037()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=66038) as if_2339_66038:  # 0m:0.000s
                if_2339_66038()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=66039) as resolve_config_vars_in_file_2340_66039:  # 0m:0.000s
                resolve_config_vars_in_file_2340_66039()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=66040) as if_2341_66040:  # 0m:0.000s
                if_2341_66040()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Torque", "NKS_DATA_VERSION": "1.0"}, prog_num=66041) as resolve_config_vars_in_file_2342_66041:  # 0m:0.000s
                resolve_config_vars_in_file_2342_66041()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Torque Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Torque Stereo.plist", ignore_all_errors=True), prog_num=66042) as if_2343_66042:  # 0m:0.000s
                if_2343_66042()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=66043) as resolve_config_vars_in_file_2344_66043:  # 0m:0.000s
                resolve_config_vars_in_file_2344_66043()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=66044) as if_2345_66044:  # 0m:0.000s
                if_2345_66044()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=66045) as resolve_config_vars_in_file_2346_66045:  # 0m:0.000s
                resolve_config_vars_in_file_2346_66045()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=66046) as if_2347_66046:  # 0m:0.000s
                if_2347_66046()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=66047) as resolve_config_vars_in_file_2348_66047:  # 0m:0.000s
                resolve_config_vars_in_file_2348_66047()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=66048) as if_2349_66048:  # 0m:0.000s
                if_2349_66048()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=66049) as rm_file_or_dir_2350_66049:  # 0m:0.000s
                rm_file_or_dir_2350_66049()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=66050) as rm_file_or_dir_2351_66050:  # 0m:0.000s
                rm_file_or_dir_2351_66050()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=66051) as rm_file_or_dir_2352_66051:  # 0m:0.000s
                rm_file_or_dir_2352_66051()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=66052) as resolve_config_vars_in_file_2353_66052:  # 0m:0.000s
                resolve_config_vars_in_file_2353_66052()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=66053) as if_2354_66053:  # 0m:0.000s
                if_2354_66053()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=66054) as resolve_config_vars_in_file_2355_66054:  # 0m:0.000s
                resolve_config_vars_in_file_2355_66054()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=66055) as if_2356_66055:  # 0m:0.000s
                if_2356_66055()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=66056) as resolve_config_vars_in_file_2357_66056:  # 0m:0.000s
                resolve_config_vars_in_file_2357_66056()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=66057) as if_2358_66057:  # 0m:0.000s
                if_2358_66057()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=66058) as rm_file_or_dir_2359_66058:  # 0m:0.000s
                rm_file_or_dir_2359_66058()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=66059) as rm_file_or_dir_2360_66059:  # 0m:0.000s
                rm_file_or_dir_2360_66059()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=66060) as rm_file_or_dir_2361_66060:  # 0m:0.000s
                rm_file_or_dir_2361_66060()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=66061) as resolve_config_vars_in_file_2362_66061:  # 0m:0.000s
                resolve_config_vars_in_file_2362_66061()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=66062) as if_2363_66062:  # 0m:0.000s
                if_2363_66062()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=66063) as resolve_config_vars_in_file_2364_66063:  # 0m:0.000s
                resolve_config_vars_in_file_2364_66063()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=66064) as if_2365_66064:  # 0m:0.000s
                if_2365_66064()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=66065) as resolve_config_vars_in_file_2366_66065:  # 0m:0.000s
                resolve_config_vars_in_file_2366_66065()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=66066) as if_2367_66066:  # 0m:0.000s
                if_2367_66066()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=66067) as resolve_config_vars_in_file_2368_66067:  # 0m:0.000s
                resolve_config_vars_in_file_2368_66067()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=66068) as if_2369_66068:  # 0m:0.000s
                if_2369_66068()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "W43", "NKS_DATA_VERSION": "1.0"}, prog_num=66069) as resolve_config_vars_in_file_2370_66069:  # 0m:0.000s
                resolve_config_vars_in_file_2370_66069()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-W43 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-W43 Stereo.plist", ignore_all_errors=True), prog_num=66070) as if_2371_66070:  # 0m:0.000s
                if_2371_66070()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=66071) as resolve_config_vars_in_file_2372_66071:  # 0m:0.000s
                resolve_config_vars_in_file_2372_66071()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=66072) as if_2373_66072:  # 0m:0.000s
                if_2373_66072()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WNS", "NKS_DATA_VERSION": "1.0"}, prog_num=66073) as resolve_config_vars_in_file_2374_66073:  # 0m:0.000s
                resolve_config_vars_in_file_2374_66073()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WNS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WNS Stereo.plist", ignore_all_errors=True), prog_num=66074) as if_2375_66074:  # 0m:0.000s
                if_2375_66074()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=66075) as resolve_config_vars_in_file_2376_66075:  # 0m:0.000s
                resolve_config_vars_in_file_2376_66075()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=66076) as if_2377_66076:  # 0m:0.000s
                if_2377_66076()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=66077) as resolve_config_vars_in_file_2378_66077:  # 0m:0.000s
                resolve_config_vars_in_file_2378_66077()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=66078) as if_2379_66078:  # 0m:0.000s
                if_2379_66078()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=66079) as resolve_config_vars_in_file_2380_66079:  # 0m:0.000s
                resolve_config_vars_in_file_2380_66079()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=66080) as if_2381_66080:  # 0m:0.000s
                if_2381_66080()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "dbx-160", "NKS_DATA_VERSION": "1.0"}, prog_num=66081) as resolve_config_vars_in_file_2382_66081:  # 0m:0.000s
                resolve_config_vars_in_file_2382_66081()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-dbx-160 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-dbx-160 Stereo.plist", ignore_all_errors=True), prog_num=66082) as if_2383_66082:  # 0m:0.000s
                if_2383_66082()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=66083) as cd_stage_2384_66083:  # 0m:0.190s
            cd_stage_2384_66083()
            with Stage(r"copy", r"COSMOS_HTML v2.6.5", prog_num=66084):  # 0m:0.027s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=66085) as should_copy_source_2385_66085:  # 0m:0.027s
                    should_copy_source_2385_66085()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=66086):  # 0m:0.026s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=66087) as copy_dir_to_dir_2386_66087:  # 0m:0.026s
                            copy_dir_to_dir_2386_66087()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=66088, recursive=True) as chown_2387_66088:  # 0m:0.000s
                            chown_2387_66088()
            with Stage(r"copy", r"COSMOS_python v2.7.6", prog_num=66089):  # 0m:0.163s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=66090) as should_copy_source_2388_66090:  # 0m:0.163s
                    should_copy_source_2388_66090()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=66091):  # 0m:0.162s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=66092) as copy_dir_to_dir_2389_66092:  # 0m:0.126s
                            copy_dir_to_dir_2389_66092()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=66093) as unwtar_2390_66093:  # 0m:0.036s
                            unwtar_2390_66093()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=66094, recursive=True) as chown_2391_66094:  # 0m:0.000s
                            chown_2391_66094()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=66095) as cd_stage_2392_66095:  # 0m:0.082s
            cd_stage_2392_66095()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=66096):  # 0m:0.082s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=66097) as should_copy_source_2393_66097:  # 0m:0.082s
                    should_copy_source_2393_66097()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=66098):  # 0m:0.081s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=66099) as copy_dir_to_dir_2394_66099:  # 0m:0.024s
                            copy_dir_to_dir_2394_66099()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=66100) as unwtar_2395_66100:  # 0m:0.057s
                            unwtar_2395_66100()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=66101, recursive=True) as chown_2396_66101:  # 0m:0.000s
                            chown_2396_66101()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=66102) as cd_stage_2397_66102:  # 0m:0.001s
            cd_stage_2397_66102()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=66103):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=66104) as should_copy_source_2398_66104:  # ?
                    should_copy_source_2398_66104()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=66105):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=66106) as copy_dir_to_dir_2399_66106:  # ?
                            copy_dir_to_dir_2399_66106()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=66107, recursive=True) as chown_2400_66107:  # 0m:0.000s
                            chown_2400_66107()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=66108) as cd_stage_2401_66108:  # 0m:0.005s
            cd_stage_2401_66108()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=66109):  # 0m:0.005s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=66110) as should_copy_source_2402_66110:  # 0m:0.005s
                    should_copy_source_2402_66110()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=66111):  # 0m:0.004s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=66112) as copy_dir_to_dir_2403_66112:  # 0m:0.004s
                            copy_dir_to_dir_2403_66112()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=66113, recursive=True) as chown_2404_66113:  # 0m:0.000s
                            chown_2404_66113()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=66114) as cd_stage_2405_66114:  # 0m:0.001s
            cd_stage_2405_66114()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=66115):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=66116) as should_copy_source_2406_66116:  # 0m:0.001s
                    should_copy_source_2406_66116()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=66117):  # 0m:0.001s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=66118) as copy_dir_to_dir_2407_66118:  # 0m:0.001s
                            copy_dir_to_dir_2407_66118()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=66119, recursive=True) as chown_2408_66119:  # 0m:0.000s
                            chown_2408_66119()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=66120) as cd_stage_2409_66120:  # 0m:3.867s
            cd_stage_2409_66120()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=66121) as rm_file_or_dir_2410_66121:  # 0m:0.000s
                rm_file_or_dir_2410_66121()
            with Stage(r"copy", r"ffmpeg v6.1.1", prog_num=66122):  # 0m:0.044s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/ffmpeg", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=66123) as should_copy_source_2411_66123:  # 0m:0.044s
                    should_copy_source_2411_66123()
                    with Stage(r"copy source", r"Mac/Modules/ffmpeg", prog_num=66124):  # 0m:0.044s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/ffmpeg.wtar.aa", where_to_unwtar=r".", prog_num=66125) as unwtar_2412_66125:  # 0m:0.044s
                            unwtar_2412_66125()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=66126):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=66127) as should_copy_source_2413_66127:  # ?
                    should_copy_source_2413_66127()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=66128):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66129) as copy_dir_to_dir_2414_66129:  # ?
                            copy_dir_to_dir_2414_66129()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=66130) as unwtar_2415_66130:  # ?
                            unwtar_2415_66130()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=66131, recursive=True) as chown_2416_66131:  # 0m:0.000s
                            chown_2416_66131()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=66132):  # 0m:0.003s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=66133) as should_copy_source_2417_66133:  # 0m:0.003s
                    should_copy_source_2417_66133()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=66134):  # 0m:0.003s
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=66135) as unwtar_2418_66135:  # 0m:0.003s
                            unwtar_2418_66135()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=66136):  # 0m:2.932s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=66137) as should_copy_source_2419_66137:  # 0m:2.932s
                    should_copy_source_2419_66137()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=66138):  # 0m:2.931s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=66139) as copy_dir_to_dir_2420_66139:  # 0m:0.016s
                            copy_dir_to_dir_2420_66139()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=66140) as unwtar_2421_66140:  # 0m:2.914s
                            unwtar_2421_66140()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=66141, recursive=True) as chown_2422_66141:  # 0m:0.000s
                            chown_2422_66141()
            with Stage(r"copy", r"onnxruntime_1.19.0 v1.19.0", prog_num=66142):  # 0m:0.872s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=66143) as should_copy_source_2423_66143:  # 0m:0.871s
                    should_copy_source_2423_66143()
                    with Stage(r"copy source", r"Mac/Modules/onnxruntime", prog_num=66144):  # 0m:0.871s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r".", delete_extraneous_files=True, prog_num=66145) as copy_dir_to_dir_2424_66145:  # 0m:0.001s
                            copy_dir_to_dir_2424_66145()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", where_to_unwtar=r".", prog_num=66146) as unwtar_2425_66146:  # 0m:0.870s
                            unwtar_2425_66146()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/onnxruntime", user_id=-1, group_id=-1, prog_num=66147, recursive=True) as chown_2426_66147:  # 0m:0.000s
                            chown_2426_66147()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=66148):  # 0m:0.001s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=66149) as should_copy_source_2427_66149:  # ?
                    should_copy_source_2427_66149()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=66150):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66151) as copy_dir_to_dir_2428_66151:  # ?
                            copy_dir_to_dir_2428_66151()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=66152) as chmod_2429_66152:  # ?
                            chmod_2429_66152()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=66153) as chmod_2430_66153:  # ?
                            chmod_2430_66153()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=66154, recursive=True) as chown_2431_66154:  # 0m:0.000s
                            chown_2431_66154()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=66157) as resolve_symlink_files_in_folder_2432_66157:  # 0m:0.003s
                resolve_symlink_files_in_folder_2432_66157()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=66158) as shell_command_2433_66158:  # 0m:0.012s
                shell_command_2433_66158()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=66159) as cd_stage_2434_66159:  # 0m:0.001s
            cd_stage_2434_66159()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=66160):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=66161) as should_copy_source_2435_66161:  # ?
                    should_copy_source_2435_66161()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=66162):  # ?
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=66163) as copy_dir_to_dir_2436_66163:  # ?
                            copy_dir_to_dir_2436_66163()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=66164, recursive=True) as chown_2437_66164:  # 0m:0.000s
                            chown_2437_66164()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=66165) as cd_stage_2438_66165:  # 0m:0.009s
            cd_stage_2438_66165()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=66166):  # 0m:0.009s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=66167) as should_copy_source_2439_66167:  # 0m:0.009s
                    should_copy_source_2439_66167()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=66168):  # 0m:0.009s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=66169) as copy_dir_to_dir_2440_66169:  # 0m:0.009s
                            copy_dir_to_dir_2440_66169()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=66170, recursive=True) as chown_2441_66170:  # 0m:0.000s
                            chown_2441_66170()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=66171) as cd_stage_2442_66171:  # 0m:0.001s
            cd_stage_2442_66171()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=66172):  # 0m:0.000s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=66173) as should_copy_source_2443_66173:  # ?
                    should_copy_source_2443_66173()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=66174):  # ?
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=66175, recursive=True) as chmod_2444_66175:  # ?
                            chmod_2444_66175()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66176) as copy_dir_to_dir_2445_66176:  # ?
                            copy_dir_to_dir_2445_66176()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=66177) as unwtar_2446_66177:  # ?
                            unwtar_2446_66177()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=66178, recursive=True) as chown_2447_66178:  # ?
                            chown_2447_66178()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=66179) as if_2448_66179:  # 0m:0.000s
                            if_2448_66179()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=66180) as cd_stage_2449_66180:  # 0m:4.937s
            cd_stage_2449_66180()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=66181):  # 0m:4.937s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=66182) as should_copy_source_2450_66182:  # 0m:4.937s
                    should_copy_source_2450_66182()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=66183):  # 0m:4.936s
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=66184, recursive=True) as chmod_2451_66184:  # 0m:0.008s
                            chmod_2451_66184()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66185) as copy_dir_to_dir_2452_66185:  # 0m:0.003s
                            copy_dir_to_dir_2452_66185()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=66186) as unwtar_2453_66186:  # 0m:4.924s
                            unwtar_2453_66186()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=66187, recursive=True) as chown_2454_66187:  # 0m:0.000s
                            chown_2454_66187()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=66188) as if_2455_66188:  # 0m:0.001s
                            if_2455_66188()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=66189) as cd_stage_2456_66189:  # 0m:0.686s
            cd_stage_2456_66189()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=66190):  # 0m:0.686s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=66191) as should_copy_source_2457_66191:  # 0m:0.686s
                    should_copy_source_2457_66191()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=66192):  # 0m:0.686s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=66193) as copy_dir_to_dir_2458_66193:  # 0m:0.001s
                            copy_dir_to_dir_2458_66193()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=66194) as unwtar_2459_66194:  # 0m:0.615s
                            unwtar_2459_66194()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=66195, recursive=True) as chown_2460_66195:  # 0m:0.000s
                            chown_2460_66195()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=66196) as break_hard_link_2461_66196:  # 0m:0.015s
                            break_hard_link_2461_66196()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=66197) as shell_command_2462_66197:  # 0m:0.044s
                            shell_command_2462_66197()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=66198, recursive=True) as chown_2463_66198:  # 0m:0.000s
                            chown_2463_66198()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=66199, recursive=True) as chmod_2464_66199:  # 0m:0.009s
                            chmod_2464_66199()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=66200) as cd_stage_2465_66200:  # 0m:0.412s
            cd_stage_2465_66200()
            with Stage(r"copy", r"WaveShell1-OBS 16.0 v16.0.23.24", prog_num=66201):  # 0m:0.412s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=66202) as should_copy_source_2466_66202:  # 0m:0.412s
                    should_copy_source_2466_66202()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=66203):  # 0m:0.411s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=66204) as copy_dir_to_dir_2467_66204:  # 0m:0.017s
                            copy_dir_to_dir_2467_66204()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=66205) as unwtar_2468_66205:  # 0m:0.349s
                            unwtar_2468_66205()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=66206, recursive=True) as chown_2469_66206:  # 0m:0.000s
                            chown_2469_66206()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=66207) as shell_command_2470_66207:  # 0m:0.045s
                            shell_command_2470_66207()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=66208) as cd_stage_2471_66208:  # 0m:1.403s
            cd_stage_2471_66208()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=66209):  # 0m:0.675s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=66210) as should_copy_source_2472_66210:  # 0m:0.675s
                    should_copy_source_2472_66210()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=66211):  # 0m:0.675s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=66212) as copy_dir_to_dir_2473_66212:  # 0m:0.002s
                            copy_dir_to_dir_2473_66212()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=66213) as unwtar_2474_66213:  # 0m:0.629s
                            unwtar_2474_66213()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=66214, recursive=True) as chown_2475_66214:  # 0m:0.000s
                            chown_2475_66214()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=66215) as shell_command_2476_66215:  # 0m:0.044s
                            shell_command_2476_66215()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=66216):  # 0m:0.727s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=66217) as should_copy_source_2477_66217:  # 0m:0.727s
                    should_copy_source_2477_66217()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=66218):  # 0m:0.726s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=66219) as copy_dir_to_dir_2478_66219:  # 0m:0.002s
                            copy_dir_to_dir_2478_66219()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=66220) as unwtar_2479_66220:  # 0m:0.674s
                            unwtar_2479_66220()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=66221, recursive=True) as chown_2480_66221:  # 0m:0.000s
                            chown_2480_66221()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=66222) as shell_command_2481_66222:  # 0m:0.050s
                            shell_command_2481_66222()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66223) as cd_stage_2482_66223:  # 0m:0.388s
            cd_stage_2482_66223()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=66224):  # 0m:0.386s
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=66225) as should_copy_source_2483_66225:  # 0m:0.386s
                    should_copy_source_2483_66225()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=66226):  # 0m:0.386s
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=66227) as copy_dir_to_dir_2484_66227:  # 0m:0.001s
                            copy_dir_to_dir_2484_66227()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=66228) as unwtar_2485_66228:  # 0m:0.198s
                            unwtar_2485_66228()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=66229, recursive=True) as chown_2486_66229:  # 0m:0.000s
                            chown_2486_66229()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=66230) as shell_command_2487_66230:  # 0m:0.109s
                            shell_command_2487_66230()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=66231) as script_command_2488_66231:  # 0m:0.017s
                            script_command_2488_66231()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=66232) as shell_command_2489_66232:  # 0m:0.061s
                            shell_command_2489_66232()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66233) as create_symlink_2490_66233:  # 0m:0.001s
                create_symlink_2490_66233()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66234) as create_symlink_2491_66234:  # 0m:0.000s
                create_symlink_2491_66234()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=66235) as cd_stage_2492_66235:  # 0m:0.000s
            cd_stage_2492_66235()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Bass Fingers Presets", prog_num=66236) as rm_file_or_dir_2493_66236:  # 0m:0.000s
                rm_file_or_dir_2493_66236()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Flow Motion Presets", prog_num=66237) as rm_file_or_dir_2494_66237:  # 0m:0.000s
                rm_file_or_dir_2494_66237()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=66238) as rm_file_or_dir_2495_66238:  # 0m:0.000s
                rm_file_or_dir_2495_66238()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=66239) as cd_stage_2496_66239:  # 0m:0.000s
            cd_stage_2496_66239()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/MMToneShaper", prog_num=66240) as rm_file_or_dir_2497_66240:  # 0m:0.000s
                rm_file_or_dir_2497_66240()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=66241) as rm_file_or_dir_2498_66241:  # 0m:0.000s
                rm_file_or_dir_2498_66241()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=66242) as rm_file_or_dir_2499_66242:  # 0m:0.000s
                rm_file_or_dir_2499_66242()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=66243) as rm_file_or_dir_2500_66243:  # 0m:0.000s
                rm_file_or_dir_2500_66243()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=66244) as shell_command_2501_66244:  # 0m:0.014s
            shell_command_2501_66244()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=66245) as shell_command_2502_66245:  # 0m:0.108s
            shell_command_2502_66245()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=66246) as script_command_2503_66246:  # 0m:0.014s
            script_command_2503_66246()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=66247) as rm_file_or_dir_2504_66247:  # 0m:0.002s
            rm_file_or_dir_2504_66247()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66248) as move_dir_to_dir_2505_66248:  # 0m:0.000s
            move_dir_to_dir_2505_66248()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66249) as move_dir_to_dir_2506_66249:  # 0m:0.000s
            move_dir_to_dir_2506_66249()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66250) as move_dir_to_dir_2507_66250:  # 0m:0.000s
            move_dir_to_dir_2507_66250()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66251) as move_dir_to_dir_2508_66251:  # 0m:0.000s
            move_dir_to_dir_2508_66251()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=66252) as make_dirs_2509_66252:  # 0m:0.030s
            make_dirs_2509_66252()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66253) as move_dir_to_dir_2510_66253:  # 0m:0.001s
            move_dir_to_dir_2510_66253()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66254) as move_dir_to_dir_2511_66254:  # 0m:0.000s
            move_dir_to_dir_2511_66254()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=66255) as shell_command_2512_66255:  # 0m:0.258s
            shell_command_2512_66255()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=66256) as script_command_2513_66256:  # 0m:0.015s
            script_command_2513_66256()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=66257) as rm_file_or_dir_2514_66257:  # 0m:0.001s
            rm_file_or_dir_2514_66257()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=66258) as touch_2515_66258:  # 0m:0.000s
            touch_2515_66258()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=66259) as glober_2516_66259:  # 0m:0.004s
            glober_2516_66259()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=66260) as glober_2517_66260:  # 0m:0.002s
            glober_2517_66260()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=66261) as glober_2518_66261:  # 0m:0.002s
            glober_2518_66261()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66262) as shell_command_2519_66262:  # 0m:0.012s
            shell_command_2519_66262()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66263) as shell_command_2520_66263:  # 0m:2.540s
            shell_command_2520_66263()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66264) as shell_command_2521_66264:  # 0m:0.574s
            shell_command_2521_66264()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66265) as shell_command_2522_66265:  # 0m:0.317s
            shell_command_2522_66265()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=66266) as shell_command_2523_66266:  # 0m:0.102s
            shell_command_2523_66266()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=66267) as script_command_2524_66267:  # 0m:0.013s
            script_command_2524_66267()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=66268) as if_2525_66268:  # 0m:0.000s
            if_2525_66268()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=66269) as if_2526_66269:  # 0m:0.000s
            if_2526_66269()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=66270) as if_2527_66270:  # 0m:0.000s
            if_2527_66270()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=66271) as if_2528_66271:  # 0m:0.000s
            if_2528_66271()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=66272) as make_dir_2529_66272:  # 0m:0.008s
            make_dir_2529_66272()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=66273) as chmod_2530_66273:  # 0m:0.000s
            chmod_2530_66273()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=66274) as make_dir_2531_66274:  # 0m:0.000s
            make_dir_2531_66274()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=66275) as chmod_2532_66275:  # 0m:0.000s
            chmod_2532_66275()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=66276) as chmod_2533_66276:  # 0m:0.000s
            chmod_2533_66276()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=66277) as chmod_2534_66277:  # 0m:0.000s
            chmod_2534_66277()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=66278) as chmod_2535_66278:  # 0m:0.000s
            chmod_2535_66278()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=66279) as shell_command_2536_66279:  # 0m:0.098s
            shell_command_2536_66279()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=66280) as script_command_2537_66280:  # 0m:0.014s
            script_command_2537_66280()
    with Stage(r"post-copy", prog_num=66281):  # 0m:0.026s
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=66282) as make_dir_2538_66282:  # 0m:0.008s
            make_dir_2538_66282()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=66283) as copy_file_to_file_2539_66283:  # 0m:0.009s
            copy_file_to_file_2539_66283()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66284) as chmod_2540_66284:  # 0m:0.000s
            chmod_2540_66284()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66285) as chmod_2541_66285:  # 0m:0.000s
            chmod_2541_66285()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=66286) as copy_file_to_file_2542_66286:  # 0m:0.000s
            copy_file_to_file_2542_66286()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66287) as chmod_2543_66287:  # 0m:0.000s
            chmod_2543_66287()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=66288) as copy_file_to_file_2544_66288:  # 0m:0.008s
            copy_file_to_file_2544_66288()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66289) as chmod_2545_66289:  # 0m:0.000s
            chmod_2545_66289()
        Progress(r"Done copy", prog_num=66290)()  # 0m:0.000s
        Progress(r"Done synccopy", prog_num=66291)()  # 0m:0.000s
    with Stage(r"post", prog_num=66292):  # 0m:0.055s
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=66293) as make_dir_2546_66293:  # 0m:0.007s
            make_dir_2546_66293()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=66294) as copy_file_to_file_2547_66294:  # 0m:0.007s
            copy_file_to_file_2547_66294()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=66295) as make_dir_2548_66295:  # 0m:0.007s
            make_dir_2548_66295()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=66296) as copy_file_to_file_2549_66296:  # 0m:0.010s
            copy_file_to_file_2549_66296()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=66297) as make_dir_2550_66297:  # 0m:0.013s
            make_dir_2550_66297()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=66298) as copy_file_to_file_2551_66298:  # 0m:0.010s
            copy_file_to_file_2551_66298()

with Stage(r"epilog", prog_num=66299):  # ?
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py", prog_num=66300) as patch_py_batch_with_timings_2552_66300:  # ?
        patch_py_batch_with_timings_2552_66300()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


# downloaded 5679397181 bytes in 1m:24.255s, 67406949 bytes per second
# copy time 5m:36.904s
