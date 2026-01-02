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

with Stage(r"assign", prog_num=1765):
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

with PythonBatchRuntime(r"synccopy", prog_num=1766):
    with Stage(r"begin", prog_num=1767):
        RsyncClone.add_global_ignore_patterns(config_vars.get("COPY_IGNORE_PATTERNS", []).list())
        RsyncClone.add_global_no_hard_link_patterns(config_vars.get("NO_HARD_LINK_PATTERNS", []).list())
        RsyncClone.add_global_no_flags_patterns(config_vars.get("NO_FLAGS_PATTERNS", []).list())
        RsyncClone.add_global_avoid_copy_markers(config_vars.get("AVOID_COPY_MARKERS", []).list())
        RemoveEmptyFolders.set_a_kwargs_default("files_to_ignore", config_vars.get("REMOVE_EMPTY_FOLDERS_IGNORE_FILES", []).list())
        log.setLevel(20)
    with Stage(r"pre", prog_num=1768):
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products_require_before.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1769) as copy_file_to_file_001_1769:
            copy_file_to_file_001_1769()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products_require_after.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=1770) as copy_file_to_file_002_1770:
            copy_file_to_file_002_1770()
    with Stage(r"sync", prog_num=1771):
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=1772) as shell_command_003_1772:
            shell_command_003_1772()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=1773) as shell_command_004_1773:
            shell_command_004_1773()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=1774) as shell_command_005_1774:
            shell_command_005_1774()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=1775) as shell_command_006_1775:
            shell_command_006_1775()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1776) as shell_command_007_1776:
            shell_command_007_1776()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=1777) as shell_command_008_1777:
            shell_command_008_1777()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=1778) as shell_command_009_1778:
            shell_command_009_1778()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=1779) as shell_command_010_1779:
            shell_command_010_1779()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=1780) as shell_command_011_1780:
            shell_command_011_1780()
        with Stage(r"download", r"https://d36wza55md4dee.cloudfront.net/V16", prog_num=1781):
            with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", chowner=True, prog_num=1782) as make_dir_012_1782:
                make_dir_012_1782()
            with Cd(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=1783) as cd_013_1783:
                cd_013_1783()
                Progress(r"11308 files already in cache", own_progress_count=11308, prog_num=13091)()
                with CreateSyncFolders(own_progress_count=4513, prog_num=17604) as create_sync_folders_014_17604:
                    create_sync_folders_014_17604()
                Progress(r"Downloading with 50 processes in parallel", prog_num=17605)()
                Progress(r"Downloading with curl parallel", prog_num=17606)()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py_curl/dl-00", total_files_to_download=22524, previously_downloaded_files=0, total_bytes_to_download=5679397181, own_progress_count=21671, prog_num=39277, report_own_progress=False) as curl_with_internal_parallel_015_39277:
                    curl_with_internal_parallel_015_39277()
                with CurlWithInternalParallel(curl_path=r"curl", config_file_path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py_curl/dl-01", total_files_to_download=22524, previously_downloaded_files=21671, total_bytes_to_download=5679397181, own_progress_count=853, prog_num=40130, report_own_progress=False) as curl_with_internal_parallel_016_40130:
                    curl_with_internal_parallel_016_40130()
                Progress(r"Downloading 22524 files done", prog_num=40131)()
                with RunInThread(Ls(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", out_file=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/after-sync-sync-folder-manifest.txt"), thread_name=r"list_sync_folder", daemon=True, ignore_all_errors=True, prog_num=40132) as run_in_thread_017_40132:
                    run_in_thread_017_40132()
                Progress(r"Check checksum ...", prog_num=40133)()
                with CheckDownloadFolderChecksum(print_report=True, raise_on_bad_checksum=True, max_bad_files_to_redownload=32, own_progress_count=22524, prog_num=62657) as check_download_folder_checksum_018_62657:
                    check_download_folder_checksum_018_62657()
                with Stage(r"post_sync", prog_num=62658):
                    Progress(r"Adjust ownership and permissions /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16...", prog_num=62659)()
                    with ChmodAndChown(path=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", mode="a+rwX", user_id=-1, group_id=-1, ignore_all_errors=True, prog_num=62660, recursive=True) as chmod_and_chown_019_62660:
                        chmod_and_chown_019_62660()
                    with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/new_have_info_map.txt", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=62661) as copy_file_to_file_020_62661:
                        copy_file_to_file_020_62661()
            Progress(r"Done sync", prog_num=62662)()
    with Stage(r"copy", prog_num=62663):
        Progress(r"Start copy from /Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=62664)()
        with Stage(r"create folders", prog_num=62665):
            with MakeDir(r"/Applications/Waves", chowner=True, prog_num=62666) as make_dir_021_62666:
                make_dir_021_62666()
            with MakeDir(r"/Applications/Waves/Applications V16", chowner=True, prog_num=62667) as make_dir_022_62667:
                make_dir_022_62667()
            with MakeDir(r"/Applications/Waves/COSMOS", chowner=True, prog_num=62668) as make_dir_023_62668:
                make_dir_023_62668()
            with MakeDir(r"/Applications/Waves/Data", chowner=True, prog_num=62669) as make_dir_024_62669:
                make_dir_024_62669()
            with MakeDir(r"/Applications/Waves/Data/Clarity Vx", chowner=True, prog_num=62670) as make_dir_025_62670:
                make_dir_025_62670()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses", chowner=True, prog_num=62671) as make_dir_026_62671:
                make_dir_026_62671()
            with MakeDir(r"/Applications/Waves/Data/IR1Impulses V2", chowner=True, prog_num=62672) as make_dir_027_62672:
                make_dir_027_62672()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Misc", chowner=True, prog_num=62673) as make_dir_028_62673:
                make_dir_028_62673()
            with MakeDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries", chowner=True, prog_num=62674) as make_dir_029_62674:
                make_dir_029_62674()
            with MakeDir(r"/Applications/Waves/Data/NKS FX", chowner=True, prog_num=62675) as make_dir_030_62675:
                make_dir_030_62675()
            with MakeDir(r"/Applications/Waves/Data/Presets", chowner=True, prog_num=62676) as make_dir_031_62676:
                make_dir_031_62676()
            with MakeDir(r"/Applications/Waves/Data/Setup Libraries", chowner=True, prog_num=62677) as make_dir_032_62677:
                make_dir_032_62677()
            with MakeDir(r"/Applications/Waves/Data/Voltage Amps IR", chowner=True, prog_num=62678) as make_dir_033_62678:
                make_dir_033_62678()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR", chowner=True, prog_num=62679) as make_dir_034_62679:
                make_dir_034_62679()
            with MakeDir(r"/Applications/Waves/Data/WavesGTR/Presets", chowner=True, prog_num=62680) as make_dir_035_62680:
                make_dir_035_62680()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16", chowner=True, prog_num=62681) as make_dir_036_62681:
                make_dir_036_62681()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/Documents", chowner=True, prog_num=62682) as make_dir_037_62682:
                make_dir_037_62682()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTR", chowner=True, prog_num=62683) as make_dir_038_62683:
                make_dir_038_62683()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/GTRSolo", chowner=True, prog_num=62684) as make_dir_039_62684:
                make_dir_039_62684()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/MIDI", chowner=True, prog_num=62685) as make_dir_040_62685:
                make_dir_040_62685()
            with MakeDir(r"/Applications/Waves/Plug-Ins V16/ModFX", chowner=True, prog_num=62686) as make_dir_041_62686:
                make_dir_041_62686()
            with MakeDir(r"/Applications/Waves/WaveShells V16", chowner=True, prog_num=62687) as make_dir_042_62687:
                make_dir_042_62687()
            with MakeDir(r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=62688) as make_dir_043_62688:
                make_dir_043_62688()
            with MakeDir(r"/Library/Application Support/Native Instruments/Service Center", prog_num=62689) as make_dir_044_62689:
                make_dir_044_62689()
            with MakeDir(r"/Library/Application Support/Waves", chowner=True, prog_num=62690) as make_dir_045_62690:
                make_dir_045_62690()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS", chowner=True, prog_num=62691) as make_dir_046_62691:
                make_dir_046_62691()
            with MakeDir(r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", chowner=True, prog_num=62692) as make_dir_047_62692:
                make_dir_047_62692()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V15", chowner=True, prog_num=62693) as make_dir_048_62693:
                make_dir_048_62693()
            with MakeDir(r"/Library/Application Support/Waves/Demo Mode/V16", chowner=True, prog_num=62694) as make_dir_049_62694:
                make_dir_049_62694()
            with MakeDir(r"/Library/Application Support/Waves/License Notifications/V16", chowner=True, prog_num=62695) as make_dir_050_62695:
                make_dir_050_62695()
            with MakeDir(r"/Library/Application Support/Waves/Modules", chowner=True, prog_num=62696) as make_dir_051_62696:
                make_dir_051_62696()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V15", chowner=True, prog_num=62697) as make_dir_052_62697:
                make_dir_052_62697()
            with MakeDir(r"/Library/Application Support/Waves/Preset Browser/V16", chowner=True, prog_num=62698) as make_dir_053_62698:
                make_dir_053_62698()
            with MakeDir(r"/Library/Application Support/Waves/WavesLocalServer", chowner=True, prog_num=62699) as make_dir_054_62699:
                make_dir_054_62699()
            with MakeDir(r"/Library/Application Support/Waves/WavesPluginServer", chowner=True, prog_num=62700) as make_dir_055_62700:
                make_dir_055_62700()
            with MakeDir(r"/Library/Audio/Plug-Ins/Components", prog_num=62701) as make_dir_056_62701:
                make_dir_056_62701()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST", prog_num=62702) as make_dir_057_62702:
                make_dir_057_62702()
            with MakeDir(r"/Library/Audio/Plug-Ins/VST3", prog_num=62703) as make_dir_058_62703:
                make_dir_058_62703()
            with MakeDir(r"/Library/Audio/Plug-Ins/WPAPI", chowner=True, prog_num=62704) as make_dir_059_62704:
                make_dir_059_62704()
            with MakeDir(r"/Users/Shared/Waves", chowner=True, prog_num=62705) as make_dir_060_62705:
                make_dir_060_62705()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings", chowner=True, prog_num=62706) as make_dir_061_62706:
                make_dir_061_62706()
            with MakeDir(r"/Users/Shared/Waves/Plug-In Settings/MMod", chowner=True, prog_num=62707) as make_dir_062_62707:
                make_dir_062_62707()
            with MakeDir(r"/Users/Shared/Waves/Sample Libraries Locations", chowner=True, prog_num=62708) as make_dir_063_62708:
                make_dir_063_62708()
            with MakeDir(r"/Users/rsp_ms/Library/Preferences/Waves Preferences", chowner=True, prog_num=62709) as make_dir_064_62709:
                make_dir_064_62709()
        with RmFileOrDir(r"/Applications/Waves/Data/Clarity Vx/onnx", prog_num=62710) as rm_file_or_dir_065_62710:
            rm_file_or_dir_065_62710()
        with RmFileOrDir(r"/Applications/Waves/.IKB", prog_num=62711) as rm_file_or_dir_066_62711:
            rm_file_or_dir_066_62711()
        with ShellCommand(r'launchctl unload "${HOME}/Library/LaunchAgents/com.WavesAudio.Cosmos.plist"', ignore_all_errors=True, prog_num=62712) as shell_command_067_62712:
            shell_command_067_62712()
        with ShellCommand(r"killall COSMOS", message=r"Closing COSMOS", ignore_all_errors=True, prog_num=62713) as shell_command_068_62713:
            shell_command_068_62713()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V16.1", ignore_all_errors=True, prog_num=62714) as shell_command_069_62714:
            shell_command_069_62714()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V15.2", ignore_all_errors=True, prog_num=62715) as shell_command_070_62715:
            shell_command_070_62715()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV15.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=62716) as shell_command_071_62716:
            shell_command_071_62716()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.2.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.2", ignore_all_errors=True, prog_num=62717) as shell_command_072_62717:
            shell_command_072_62717()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV14.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V14.1", ignore_all_errors=True, prog_num=62718) as shell_command_073_62718:
            shell_command_073_62718()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV13.1.bundle/Contents/MacOS/WavesPluginClient" wps.shutdown', message=r"Stop WavesPluginServer V13.1", ignore_all_errors=True, prog_num=62719) as shell_command_074_62719:
            shell_command_074_62719()
        with ShellCommand(r'"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/MacOS/WavesLocalClient" wpivot.shutdown', message=r"Stop WavesLocalServer", ignore_all_errors=True, prog_num=62720) as shell_command_075_62720:
            shell_command_075_62720()
        with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/NKS/Grand Rhapsody/Grand Rhapsody Piano Stereo", prog_num=62721) as rm_file_or_dir_076_62721:
            rm_file_or_dir_076_62721()
        with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Grand Rhapsody Piano Stereo.xml", prog_num=62722) as rm_file_or_dir_077_62722:
            rm_file_or_dir_077_62722()
        with CdStage(r"SetExecPermissionsInSyncFolder", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16", prog_num=62723) as cd_stage_078_62723:
            cd_stage_078_62723()
            with SetExecPermissionsInSyncFolder(prog_num=62724) as set_exec_permissions_in_sync_folder_079_62724:
                set_exec_permissions_in_sync_folder_079_62724()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Applications V16", prog_num=62725) as cd_stage_080_62725:
            cd_stage_080_62725()
            with Stage(r"copy", r"Bass Fingers application v16.0.23.24", prog_num=62726):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62727) as should_copy_source_081_62727:
                    should_copy_source_081_62727()
                    with Stage(r"copy source", r"Mac/Apps/Bass Fingers.app", prog_num=62728):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", r".", delete_extraneous_files=True, prog_num=62729) as copy_dir_to_dir_082_62729:
                            copy_dir_to_dir_082_62729()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Fingers.app", where_to_unwtar=r".", prog_num=62730) as unwtar_083_62730:
                            unwtar_083_62730()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Fingers.app", user_id=-1, group_id=-1, prog_num=62731, recursive=True) as chown_084_62731:
                            chown_084_62731()
            with Stage(r"copy", r"Bass Slapper application v16.0.23.24", prog_num=62732):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62733) as should_copy_source_085_62733:
                    should_copy_source_085_62733()
                    with Stage(r"copy source", r"Mac/Apps/Bass Slapper.app", prog_num=62734):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", r".", delete_extraneous_files=True, prog_num=62735) as copy_dir_to_dir_086_62735:
                            copy_dir_to_dir_086_62735()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Bass Slapper.app", where_to_unwtar=r".", prog_num=62736) as unwtar_087_62736:
                            unwtar_087_62736()
                        with Chown(path=r"/Applications/Waves/Applications V16/Bass Slapper.app", user_id=-1, group_id=-1, prog_num=62737, recursive=True) as chown_088_62737:
                            chown_088_62737()
            with Stage(r"copy", r"Codex Wavetable Synth application v16.0.23.24", prog_num=62738):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62739) as should_copy_source_089_62739:
                    should_copy_source_089_62739()
                    with Stage(r"copy source", r"Mac/Apps/CODEX.app", prog_num=62740):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", r".", delete_extraneous_files=True, prog_num=62741) as copy_dir_to_dir_090_62741:
                            copy_dir_to_dir_090_62741()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CODEX.app", where_to_unwtar=r".", prog_num=62742) as unwtar_091_62742:
                            unwtar_091_62742()
                        with Chown(path=r"/Applications/Waves/Applications V16/CODEX.app", user_id=-1, group_id=-1, prog_num=62743, recursive=True) as chown_092_62743:
                            chown_092_62743()
            with Stage(r"copy", r"CR8 Sampler application v16.0.23.24", prog_num=62744):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62745) as should_copy_source_093_62745:
                    should_copy_source_093_62745()
                    with Stage(r"copy source", r"Mac/Apps/CR8 Sampler.app", prog_num=62746):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", r".", delete_extraneous_files=True, prog_num=62747) as copy_dir_to_dir_094_62747:
                            copy_dir_to_dir_094_62747()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/CR8 Sampler.app", where_to_unwtar=r".", prog_num=62748) as unwtar_095_62748:
                            unwtar_095_62748()
                        with Chown(path=r"/Applications/Waves/Applications V16/CR8 Sampler.app", user_id=-1, group_id=-1, prog_num=62749, recursive=True) as chown_096_62749:
                            chown_096_62749()
            with Stage(r"copy", r"Clavinet application v16.0.23.24", prog_num=62750):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62751) as should_copy_source_097_62751:
                    should_copy_source_097_62751()
                    with Stage(r"copy source", r"Mac/Apps/Clavinet.app", prog_num=62752):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", r".", delete_extraneous_files=True, prog_num=62753) as copy_dir_to_dir_098_62753:
                            copy_dir_to_dir_098_62753()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Clavinet.app", where_to_unwtar=r".", prog_num=62754) as unwtar_099_62754:
                            unwtar_099_62754()
                        with Chown(path=r"/Applications/Waves/Applications V16/Clavinet.app", user_id=-1, group_id=-1, prog_num=62755, recursive=True) as chown_100_62755:
                            chown_100_62755()
            with Stage(r"copy", r"Electric 200 Piano application v16.0.23.24", prog_num=62756):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62757) as should_copy_source_101_62757:
                    should_copy_source_101_62757()
                    with Stage(r"copy source", r"Mac/Apps/Electric200.app", prog_num=62758):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", r".", delete_extraneous_files=True, prog_num=62759) as copy_dir_to_dir_102_62759:
                            copy_dir_to_dir_102_62759()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric200.app", where_to_unwtar=r".", prog_num=62760) as unwtar_103_62760:
                            unwtar_103_62760()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric200.app", user_id=-1, group_id=-1, prog_num=62761, recursive=True) as chown_104_62761:
                            chown_104_62761()
            with Stage(r"copy", r"Electric 88 Piano application v16.0.23.24", prog_num=62762):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62763) as should_copy_source_105_62763:
                    should_copy_source_105_62763()
                    with Stage(r"copy source", r"Mac/Apps/Electric88.app", prog_num=62764):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", r".", delete_extraneous_files=True, prog_num=62765) as copy_dir_to_dir_106_62765:
                            copy_dir_to_dir_106_62765()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric88.app", where_to_unwtar=r".", prog_num=62766) as unwtar_107_62766:
                            unwtar_107_62766()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric88.app", user_id=-1, group_id=-1, prog_num=62767, recursive=True) as chown_108_62767:
                            chown_108_62767()
            with Stage(r"copy", r"Electric Grand 80 application v16.0.23.24", prog_num=62768):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62769) as should_copy_source_109_62769:
                    should_copy_source_109_62769()
                    with Stage(r"copy source", r"Mac/Apps/Electric Grand 80.app", prog_num=62770):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", r".", delete_extraneous_files=True, prog_num=62771) as copy_dir_to_dir_110_62771:
                            copy_dir_to_dir_110_62771()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Electric Grand 80.app", where_to_unwtar=r".", prog_num=62772) as unwtar_111_62772:
                            unwtar_111_62772()
                        with Chown(path=r"/Applications/Waves/Applications V16/Electric Grand 80.app", user_id=-1, group_id=-1, prog_num=62773, recursive=True) as chown_112_62773:
                            chown_112_62773()
            with Stage(r"copy", r"Element Virtual Analog Synth application v16.0.23.24", prog_num=62774):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62775) as should_copy_source_113_62775:
                    should_copy_source_113_62775()
                    with Stage(r"copy source", r"Mac/Apps/Element.app", prog_num=62776):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", r".", delete_extraneous_files=True, prog_num=62777) as copy_dir_to_dir_114_62777:
                            copy_dir_to_dir_114_62777()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Element.app", where_to_unwtar=r".", prog_num=62778) as unwtar_115_62778:
                            unwtar_115_62778()
                        with Chown(path=r"/Applications/Waves/Applications V16/Element.app", user_id=-1, group_id=-1, prog_num=62779, recursive=True) as chown_116_62779:
                            chown_116_62779()
            with Stage(r"copy", r"Flow Motion application v16.0.23.24", prog_num=62780):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62781) as should_copy_source_117_62781:
                    should_copy_source_117_62781()
                    with Stage(r"copy source", r"Mac/Apps/Flow Motion.app", prog_num=62782):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", r".", delete_extraneous_files=True, prog_num=62783) as copy_dir_to_dir_118_62783:
                            copy_dir_to_dir_118_62783()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Flow Motion.app", where_to_unwtar=r".", prog_num=62784) as unwtar_119_62784:
                            unwtar_119_62784()
                        with Chown(path=r"/Applications/Waves/Applications V16/Flow Motion.app", user_id=-1, group_id=-1, prog_num=62785, recursive=True) as chown_120_62785:
                            chown_120_62785()
            with Stage(r"copy", r"GTR Solo application v16.0.23.24", prog_num=62786):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62787) as should_copy_source_121_62787:
                    should_copy_source_121_62787()
                    with Stage(r"copy source", r"Mac/Apps/GTRSolo 3.5.app", prog_num=62788):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", r".", delete_extraneous_files=True, prog_num=62789) as copy_dir_to_dir_122_62789:
                            copy_dir_to_dir_122_62789()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTRSolo 3.5.app", where_to_unwtar=r".", prog_num=62790) as unwtar_123_62790:
                            unwtar_123_62790()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTRSolo 3.5.app", user_id=-1, group_id=-1, prog_num=62791, recursive=True) as chown_124_62791:
                            chown_124_62791()
            with Stage(r"copy", r"GTR application v16.0.23.24", prog_num=62792):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62793) as should_copy_source_125_62793:
                    should_copy_source_125_62793()
                    with Stage(r"copy source", r"Mac/Apps/GTR 3.5.app", prog_num=62794):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", r".", delete_extraneous_files=True, prog_num=62795) as copy_dir_to_dir_126_62795:
                            copy_dir_to_dir_126_62795()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/GTR 3.5.app", where_to_unwtar=r".", prog_num=62796) as unwtar_127_62796:
                            unwtar_127_62796()
                        with Chown(path=r"/Applications/Waves/Applications V16/GTR 3.5.app", user_id=-1, group_id=-1, prog_num=62797, recursive=True) as chown_128_62797:
                            chown_128_62797()
            with Stage(r"copy", r"Grand Rhapsody application v16.0.23.24", prog_num=62798):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62799) as should_copy_source_129_62799:
                    should_copy_source_129_62799()
                    with Stage(r"copy source", r"Mac/Apps/Grand Rhapsody.app", prog_num=62800):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", r".", delete_extraneous_files=True, prog_num=62801) as copy_dir_to_dir_130_62801:
                            copy_dir_to_dir_130_62801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/Grand Rhapsody.app", where_to_unwtar=r".", prog_num=62802) as unwtar_131_62802:
                            unwtar_131_62802()
                        with Chown(path=r"/Applications/Waves/Applications V16/Grand Rhapsody.app", user_id=-1, group_id=-1, prog_num=62803, recursive=True) as chown_132_62803:
                            chown_132_62803()
            with Stage(r"copy", r"StudioVerse Instruments App v16.0.23.24", prog_num=62804):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62805) as should_copy_source_133_62805:
                    should_copy_source_133_62805()
                    with Stage(r"copy source", r"Mac/Apps/StudioVerse Instruments.app", prog_num=62806):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", r".", delete_extraneous_files=True, prog_num=62807) as copy_dir_to_dir_134_62807:
                            copy_dir_to_dir_134_62807()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/StudioVerse Instruments.app", where_to_unwtar=r".", prog_num=62808) as unwtar_135_62808:
                            unwtar_135_62808()
                        with Chown(path=r"/Applications/Waves/Applications V16/StudioVerse Instruments.app", user_id=-1, group_id=-1, prog_num=62809, recursive=True) as chown_136_62809:
                            chown_136_62809()
            with Stage(r"copy", r"OVox Vocal ReSynthesis application v16.0.23.24", prog_num=62810):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62811) as should_copy_source_137_62811:
                    should_copy_source_137_62811()
                    with Stage(r"copy source", r"Mac/Apps/OVox.app", prog_num=62812):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", r".", delete_extraneous_files=True, prog_num=62813) as copy_dir_to_dir_138_62813:
                            copy_dir_to_dir_138_62813()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/OVox.app", where_to_unwtar=r".", prog_num=62814) as unwtar_139_62814:
                            unwtar_139_62814()
                        with Chown(path=r"/Applications/Waves/Applications V16/OVox.app", user_id=-1, group_id=-1, prog_num=62815, recursive=True) as chown_140_62815:
                            chown_140_62815()
            with Stage(r"copy", r"PRS Archon application v16.0.23.24", prog_num=62816):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62817) as should_copy_source_141_62817:
                    should_copy_source_141_62817()
                    with Stage(r"copy source", r"Mac/Apps/PRS Archon.app", prog_num=62818):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", r".", delete_extraneous_files=True, prog_num=62819) as copy_dir_to_dir_142_62819:
                            copy_dir_to_dir_142_62819()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Archon.app", where_to_unwtar=r".", prog_num=62820) as unwtar_143_62820:
                            unwtar_143_62820()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS Archon.app", user_id=-1, group_id=-1, prog_num=62821, recursive=True) as chown_144_62821:
                            chown_144_62821()
            with Stage(r"copy", r"PRS Dallas application v16.0.23.24", prog_num=62822):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62823) as should_copy_source_145_62823:
                    should_copy_source_145_62823()
                    with Stage(r"copy source", r"Mac/Apps/PRS Dallas.app", prog_num=62824):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", r".", delete_extraneous_files=True, prog_num=62825) as copy_dir_to_dir_146_62825:
                            copy_dir_to_dir_146_62825()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS Dallas.app", where_to_unwtar=r".", prog_num=62826) as unwtar_147_62826:
                            unwtar_147_62826()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS Dallas.app", user_id=-1, group_id=-1, prog_num=62827, recursive=True) as chown_148_62827:
                            chown_148_62827()
            with Stage(r"copy", r"PRS V9 application v16.0.23.24", prog_num=62828):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", r"/Applications/Waves/Applications V16", skip_progress_count=4, prog_num=62829) as should_copy_source_149_62829:
                    should_copy_source_149_62829()
                    with Stage(r"copy source", r"Mac/Apps/PRS V9.app", prog_num=62830):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", r".", delete_extraneous_files=True, prog_num=62831) as copy_dir_to_dir_150_62831:
                            copy_dir_to_dir_150_62831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/PRS V9.app", where_to_unwtar=r".", prog_num=62832) as unwtar_151_62832:
                            unwtar_151_62832()
                        with Chown(path=r"/Applications/Waves/Applications V16/PRS V9.app", user_id=-1, group_id=-1, prog_num=62833, recursive=True) as chown_152_62833:
                            chown_152_62833()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Applications V16" -c', ignore_all_errors=True, prog_num=62834) as shell_command_153_62834:
                shell_command_153_62834()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Applications V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Applications V16"/Icon?; fi', prog_num=62835) as script_command_154_62835:
                script_command_154_62835()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/COSMOS", prog_num=62836) as cd_stage_155_62836:
            cd_stage_155_62836()
            with Stage(r"copy", r"COSMOS__Application v16.0.30.31", prog_num=62837):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r"/Applications/Waves/COSMOS", skip_progress_count=4, prog_num=62838) as should_copy_source_156_62838:
                    should_copy_source_156_62838()
                    with Stage(r"copy source", r"Mac/Apps/COSMOS.app", prog_num=62839):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", r".", hard_links=False, delete_extraneous_files=True, prog_num=62840) as copy_dir_to_dir_157_62840:
                            copy_dir_to_dir_157_62840()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Apps/COSMOS.app", where_to_unwtar=r".", prog_num=62841) as unwtar_158_62841:
                            unwtar_158_62841()
                        with Chown(path=r"/Applications/Waves/COSMOS/COSMOS.app", user_id=-1, group_id=-1, prog_num=62842, recursive=True) as chown_159_62842:
                            chown_159_62842()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/COSMOS", own_progress_count=10, prog_num=62852) as resolve_symlink_files_in_folder_160_62852:
                resolve_symlink_files_in_folder_160_62852()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data", prog_num=62853) as cd_stage_161_62853:
            cd_stage_161_62853()
            with RmFileOrDir(r"/Applications/Waves/Data/Waves Gems", prog_num=62854) as rm_file_or_dir_162_62854:
                rm_file_or_dir_162_62854()
            with Stage(r"copy", r"COSMOS__Data_Folders v2.0.2.2", prog_num=62855):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62856) as should_copy_source_163_62856:
                    should_copy_source_163_62856()
                    with Stage(r"copy source", r"Common/Data/COSMOS", prog_num=62857):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/COSMOS", r".", delete_extraneous_files=True, prog_num=62858) as copy_dir_to_dir_164_62858:
                            copy_dir_to_dir_164_62858()
                        with Chown(path=r"/Applications/Waves/Data/COSMOS", user_id=-1, group_id=-1, prog_num=62859, recursive=True) as chown_165_62859:
                            chown_165_62859()
            with Stage(r"copy", r"COSMOS__Models_Data_Folders v2.0.0.4", prog_num=62860):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62861) as should_copy_source_166_62861:
                    should_copy_source_166_62861()
                    with Stage(r"copy source", r"Common/Data/Models", prog_num=62862):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", r".", delete_extraneous_files=True, prog_num=62863) as copy_dir_to_dir_167_62863:
                            copy_dir_to_dir_167_62863()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Models", where_to_unwtar=r".", prog_num=62864) as unwtar_168_62864:
                            unwtar_168_62864()
                        with Chown(path=r"/Applications/Waves/Data/Models", user_id=-1, group_id=-1, prog_num=62865, recursive=True) as chown_169_62865:
                            chown_169_62865()
            with Stage(r"copy", r"ChainersChildExcludeList v1.0.0.1", prog_num=62866):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62867) as should_copy_source_170_62867:
                    should_copy_source_170_62867()
                    with Stage(r"copy source", r"Common/Data/ChainersChildExcludeList", prog_num=62868):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ChainersChildExcludeList", r".", delete_extraneous_files=True, prog_num=62869) as copy_dir_to_dir_171_62869:
                            copy_dir_to_dir_171_62869()
                        with Chown(path=r"/Applications/Waves/Data/ChainersChildExcludeList", user_id=-1, group_id=-1, prog_num=62870, recursive=True) as chown_172_62870:
                            chown_172_62870()
            with Stage(r"copy", r"Character Filters Data v1.0.0.9", prog_num=62871):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Character Filters", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62872) as should_copy_source_173_62872:
                    should_copy_source_173_62872()
                    with Stage(r"copy source", r"Common/Data/Character Filters", prog_num=62873):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Character Filters", r".", delete_extraneous_files=True, prog_num=62874) as copy_dir_to_dir_174_62874:
                            copy_dir_to_dir_174_62874()
                        with Chown(path=r"/Applications/Waves/Data/Character Filters", user_id=-1, group_id=-1, prog_num=62875, recursive=True) as chown_175_62875:
                            chown_175_62875()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Network__Data_Folders v1.0.1.6", prog_num=62876):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62877) as should_copy_source_176_62877:
                    should_copy_source_176_62877()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx DeReverb", prog_num=62878):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=62879) as copy_dir_to_dir_177_62879:
                            copy_dir_to_dir_177_62879()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx DeReverb", where_to_unwtar=r".", prog_num=62880) as unwtar_178_62880:
                            unwtar_178_62880()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=62881, recursive=True) as chown_179_62881:
                            chown_179_62881()
            with Stage(r"copy", r"Curves_AQ_Special_Data v1.0.0.4", prog_num=62882):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62883) as should_copy_source_180_62883:
                    should_copy_source_180_62883()
                    with Stage(r"copy source", r"Common/Data/Curves", prog_num=62884):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", r".", delete_extraneous_files=True, prog_num=62885) as copy_dir_to_dir_181_62885:
                            copy_dir_to_dir_181_62885()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Curves", where_to_unwtar=r".", prog_num=62886) as unwtar_182_62886:
                            unwtar_182_62886()
                        with Chown(path=r"/Applications/Waves/Data/Curves", user_id=-1, group_id=-1, prog_num=62887, recursive=True) as chown_183_62887:
                            chown_183_62887()
            with Stage(r"copy", r"Waves Gems Data v1.1.0.2", prog_num=62888):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Waves Gems", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62889) as should_copy_source_184_62889:
                    should_copy_source_184_62889()
                    with Stage(r"copy source", r"Common/Data/Waves Gems", prog_num=62890):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Waves Gems", r".", delete_extraneous_files=True, prog_num=62891) as copy_dir_to_dir_185_62891:
                            copy_dir_to_dir_185_62891()
                        with Chown(path=r"/Applications/Waves/Data/Waves Gems", user_id=-1, group_id=-1, prog_num=62892, recursive=True) as chown_186_62892:
                            chown_186_62892()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses v1.0.0.1", prog_num=62893):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62894) as should_copy_source_187_62894:
                    should_copy_source_187_62894()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses", prog_num=62895):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses", r".", delete_extraneous_files=True, prog_num=62896) as copy_dir_to_dir_188_62896:
                            copy_dir_to_dir_188_62896()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses", user_id=-1, group_id=-1, prog_num=62897, recursive=True) as chown_189_62897:
                            chown_189_62897()
            with Stage(r"copy", r"MagmaSprings__Data_Folders v1.0.0.4", prog_num=62898):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62899) as should_copy_source_190_62899:
                    should_copy_source_190_62899()
                    with Stage(r"copy source", r"Common/Data/MagmaSprings", prog_num=62900):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/MagmaSprings", r".", delete_extraneous_files=True, prog_num=62901) as copy_dir_to_dir_191_62901:
                            copy_dir_to_dir_191_62901()
                        with Chown(path=r"/Applications/Waves/Data/MagmaSprings", user_id=-1, group_id=-1, prog_num=62902, recursive=True) as chown_192_62902:
                            chown_192_62902()
            with Stage(r"copy", r"Nx Ocean Way Nashville Data v1.0.0.0", prog_num=62903):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Nx Ocean Way Nashville", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62904) as should_copy_source_193_62904:
                    should_copy_source_193_62904()
                    with Stage(r"copy source", r"Common/Data/Nx Ocean Way Nashville", prog_num=62905):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Nx Ocean Way Nashville", r".", delete_extraneous_files=True, prog_num=62906) as copy_dir_to_dir_194_62906:
                            copy_dir_to_dir_194_62906()
                        with Chown(path=r"/Applications/Waves/Data/Nx Ocean Way Nashville", user_id=-1, group_id=-1, prog_num=62907, recursive=True) as chown_195_62907:
                            chown_195_62907()
            with Stage(r"copy", r"Note Mapping Data v1.0.0.10", prog_num=62908):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62909) as should_copy_source_196_62909:
                    should_copy_source_196_62909()
                    with Stage(r"copy source", r"Common/Data/Note Mapping", prog_num=62910):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", r".", delete_extraneous_files=True, prog_num=62911) as copy_dir_to_dir_197_62911:
                            copy_dir_to_dir_197_62911()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Note Mapping", where_to_unwtar=r".", prog_num=62912) as unwtar_198_62912:
                            unwtar_198_62912()
                        with Chown(path=r"/Applications/Waves/Data/Note Mapping", user_id=-1, group_id=-1, prog_num=62913, recursive=True) as chown_199_62913:
                            chown_199_62913()
            with Stage(r"copy", r"ORS Modulators Data v1.0.0.4", prog_num=62914):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62915) as should_copy_source_200_62915:
                    should_copy_source_200_62915()
                    with Stage(r"copy source", r"Common/Data/ORS Modulators", prog_num=62916):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/ORS Modulators", r".", delete_extraneous_files=True, prog_num=62917) as copy_dir_to_dir_201_62917:
                            copy_dir_to_dir_201_62917()
                        with Chown(path=r"/Applications/Waves/Data/ORS Modulators", user_id=-1, group_id=-1, prog_num=62918, recursive=True) as chown_202_62918:
                            chown_202_62918()
            with Stage(r"copy", r"Retro_Fi__Data_Folders v1.0.0.0", prog_num=62919):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62920) as should_copy_source_203_62920:
                    should_copy_source_203_62920()
                    with Stage(r"copy source", r"Common/Data/Retro Fi", prog_num=62921):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Retro Fi", r".", delete_extraneous_files=True, prog_num=62922) as copy_dir_to_dir_204_62922:
                            copy_dir_to_dir_204_62922()
                        with Chown(path=r"/Applications/Waves/Data/Retro Fi", user_id=-1, group_id=-1, prog_num=62923, recursive=True) as chown_205_62923:
                            chown_205_62923()
            with Stage(r"copy", r"StudioRack Data v1.0.0.6", prog_num=62924):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62925) as should_copy_source_206_62925:
                    should_copy_source_206_62925()
                    with Stage(r"copy source", r"Common/Data/StudioRack", prog_num=62926):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", r".", delete_extraneous_files=True, prog_num=62927) as copy_dir_to_dir_207_62927:
                            copy_dir_to_dir_207_62927()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/StudioRack", where_to_unwtar=r".", prog_num=62928) as unwtar_208_62928:
                            unwtar_208_62928()
                        with Chown(path=r"/Applications/Waves/Data/StudioRack", user_id=-1, group_id=-1, prog_num=62929, recursive=True) as chown_209_62929:
                            chown_209_62929()
            with Stage(r"copy", r"StudioRack Presets Compatibility v1.0.2.0", prog_num=62930):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Automation ID Mappings", r"/Applications/Waves/Data", skip_progress_count=3, prog_num=62931) as should_copy_source_210_62931:
                    should_copy_source_210_62931()
                    with Stage(r"copy source", r"Common/Data/Automation ID Mappings", prog_num=62932):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Automation ID Mappings", r".", delete_extraneous_files=True, prog_num=62933) as copy_dir_to_dir_211_62933:
                            copy_dir_to_dir_211_62933()
                        with Chown(path=r"/Applications/Waves/Data/Automation ID Mappings", user_id=-1, group_id=-1, prog_num=62934, recursive=True) as chown_212_62934:
                            chown_212_62934()
            with Stage(r"copy", r"SyncVx Data v1.0.0.2", prog_num=62935):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62936) as should_copy_source_213_62936:
                    should_copy_source_213_62936()
                    with Stage(r"copy source", r"Common/Data/SyncVx", prog_num=62937):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", r".", delete_extraneous_files=True, prog_num=62938) as copy_dir_to_dir_214_62938:
                            copy_dir_to_dir_214_62938()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/SyncVx", where_to_unwtar=r".", prog_num=62939) as unwtar_215_62939:
                            unwtar_215_62939()
                        with Chown(path=r"/Applications/Waves/Data/SyncVx", user_id=-1, group_id=-1, prog_num=62940, recursive=True) as chown_216_62940:
                            chown_216_62940()
            with Stage(r"copy", r"Waves Harmony Note Mapping Data v1.0.0.13", prog_num=62941):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r"/Applications/Waves/Data", skip_progress_count=4, prog_num=62942) as should_copy_source_217_62942:
                    should_copy_source_217_62942()
                    with Stage(r"copy source", r"Common/Data/Harmony", prog_num=62943):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", r".", delete_extraneous_files=True, prog_num=62944) as copy_dir_to_dir_218_62944:
                            copy_dir_to_dir_218_62944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Harmony", where_to_unwtar=r".", prog_num=62945) as unwtar_219_62945:
                            unwtar_219_62945()
                        with Chown(path=r"/Applications/Waves/Data/Harmony", user_id=-1, group_id=-1, prog_num=62946, recursive=True) as chown_220_62946:
                            chown_220_62946()
            with RmFileOrDir(r"/Applications/Waves/Data/Nx Ocean Way Nashville/44.1", prog_num=62947) as rm_file_or_dir_221_62947:
                rm_file_or_dir_221_62947()
            with RmFileOrDir(r"/Applications/Waves/Data/Nx Ocean Way Nashville/48", prog_num=62948) as rm_file_or_dir_222_62948:
                rm_file_or_dir_222_62948()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Chromatic.scale", prog_num=62949) as rm_file_or_dir_223_62949:
                rm_file_or_dir_223_62949()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Major.scale", prog_num=62950) as rm_file_or_dir_224_62950:
                rm_file_or_dir_224_62950()
            with RmFileOrDir(r"/Applications/Waves/Data/Note Mapping/Scales/ Natural Minor.scale", prog_num=62951) as rm_file_or_dir_225_62951:
                rm_file_or_dir_225_62951()
            with RmGlobs(r'"/Applications/Waves/Data/Automation ID Mappings"', r"B3XX.json", r"C360.json", r"DXMT.json", r"L360.json", r"MV36.json", r"R360.json", r"S360.json", r"UMPT.json", r"UPMX.json", ignore_all_errors=True, prog_num=62952) as rm_globs_226_62952:
                rm_globs_226_62952()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Clarity Vx", prog_num=62953) as cd_stage_227_62953:
            cd_stage_227_62953()
            with Stage(r"copy", r"Clarity_Vx_Onnx__Data_Folders v1.0.1.4", prog_num=62954):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=3, prog_num=62955) as should_copy_source_228_62955:
                    should_copy_source_228_62955()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/Info.xml", prog_num=62956):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/Info.xml", r".", prog_num=62957) as copy_file_to_dir_229_62957:
                            copy_file_to_dir_229_62957()
                        with ChmodAndChown(path=r"Info.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=62958) as chmod_and_chown_230_62958:
                            chmod_and_chown_230_62958()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r"/Applications/Waves/Data/Clarity Vx", skip_progress_count=4, prog_num=62959) as should_copy_source_231_62959:
                    should_copy_source_231_62959()
                    with Stage(r"copy source", r"Common/Data/Clarity Vx/onnx", prog_num=62960):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", r".", delete_extraneous_files=True, prog_num=62961) as copy_dir_to_dir_232_62961:
                            copy_dir_to_dir_232_62961()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Clarity Vx/onnx", where_to_unwtar=r".", prog_num=62962) as unwtar_233_62962:
                            unwtar_233_62962()
                        with Chown(path=r"/Applications/Waves/Data/Clarity Vx/onnx", user_id=-1, group_id=-1, prog_num=62963, recursive=True) as chown_234_62963:
                            chown_234_62963()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/IR1Impulses V2", prog_num=62964) as cd_stage_235_62964:
            cd_stage_235_62964()
            with Stage(r"copy", r"IR1 Convolution Reverb Impulses V2 v1.0.0.1", prog_num=62965):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62966) as should_copy_source_236_62966:
                    should_copy_source_236_62966()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic", prog_num=62967):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic", r".", delete_extraneous_files=True, prog_num=62968) as copy_dir_to_dir_237_62968:
                            copy_dir_to_dir_237_62968()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic", user_id=-1, group_id=-1, prog_num=62969, recursive=True) as chown_238_62969:
                            chown_238_62969()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62970) as should_copy_source_239_62970:
                    should_copy_source_239_62970()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Inverse Sweeps", prog_num=62971):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Inverse Sweeps", r".", delete_extraneous_files=True, prog_num=62972) as copy_dir_to_dir_240_62972:
                            copy_dir_to_dir_240_62972()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Inverse Sweeps", user_id=-1, group_id=-1, prog_num=62973, recursive=True) as chown_241_62973:
                            chown_241_62973()
            with Stage(r"copy", r"IR-Live Convolution Reverb Impulses v1.0.0.2", prog_num=62974):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62975) as should_copy_source_242_62975:
                    should_copy_source_242_62975()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Basic Live", prog_num=62976):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Basic Live", r".", delete_extraneous_files=True, prog_num=62977) as copy_dir_to_dir_243_62977:
                            copy_dir_to_dir_243_62977()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Basic Live", user_id=-1, group_id=-1, prog_num=62978, recursive=True) as chown_244_62978:
                            chown_244_62978()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62979) as should_copy_source_245_62979:
                    should_copy_source_245_62979()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/IR-Live Impulses", prog_num=62980):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/IR-Live Impulses", r".", delete_extraneous_files=True, prog_num=62981) as copy_dir_to_dir_246_62981:
                            copy_dir_to_dir_246_62981()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/IR-Live Impulses", user_id=-1, group_id=-1, prog_num=62982, recursive=True) as chown_247_62982:
                            chown_247_62982()
            with Stage(r"copy", r"StudioRack Impulses", prog_num=62983):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Stairwells", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62984) as should_copy_source_248_62984:
                    should_copy_source_248_62984()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Stairwells", prog_num=62985):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Stairwells", r".", delete_extraneous_files=True, prog_num=62986) as copy_dir_to_dir_249_62986:
                            copy_dir_to_dir_249_62986()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Stairwells", user_id=-1, group_id=-1, prog_num=62987, recursive=True) as chown_250_62987:
                            chown_250_62987()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Synagogues", r"/Applications/Waves/Data/IR1Impulses V2", skip_progress_count=3, prog_num=62988) as should_copy_source_251_62988:
                    should_copy_source_251_62988()
                    with Stage(r"copy source", r"Common/Data/IR1Impulses V2/Synagogues", prog_num=62989):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/IR1Impulses V2/Synagogues", r".", delete_extraneous_files=True, prog_num=62990) as copy_dir_to_dir_252_62990:
                            copy_dir_to_dir_252_62990()
                        with Chown(path=r"/Applications/Waves/Data/IR1Impulses V2/Synagogues", user_id=-1, group_id=-1, prog_num=62991, recursive=True) as chown_253_62991:
                            chown_253_62991()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Instrument Data/Misc", prog_num=62992) as cd_stage_254_62992:
            cd_stage_254_62992()
            with Stage(r"copy", r"Electric Grand 80 Misc Data", prog_num=62993):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=62994) as should_copy_source_255_62994:
                    should_copy_source_255_62994()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", prog_num=62995):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", r".", prog_num=62996) as copy_file_to_dir_256_62996:
                            copy_file_to_dir_256_62996()
                        with ChmodAndChown(path=r"rtshdjucbelairmc4pOgdTrqgankJ63HnsgetcI.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=62997) as chmod_and_chown_257_62997:
                            chmod_and_chown_257_62997()
            with Stage(r"copy", r"Grand Rhapsody Misc Data", prog_num=62998):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", r"/Applications/Waves/Data/Instrument Data/Misc", skip_progress_count=3, prog_num=62999) as should_copy_source_258_62999:
                    should_copy_source_258_62999()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", prog_num=63000):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/Misc/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", r".", prog_num=63001) as copy_file_to_dir_259_63001:
                            copy_file_to_dir_259_63001()
                        with ChmodAndChown(path=r"Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", mode="a+rw", user_id=-1, group_id=-1, prog_num=63002) as chmod_and_chown_260_63002:
                            chmod_and_chown_260_63002()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody/Grtshdjucbelairmc4pOgdTrqgankJ63HnsgetP.wir", prog_num=63003) as rm_file_or_dir_261_63003:
                rm_file_or_dir_261_63003()
            with RemoveEmptyFolders(r"/Applications/Waves/Data/Instrument Data/Waves Sample Libraries/Grand Rhapsody", prog_num=63004) as remove_empty_folders_262_63004:
                remove_empty_folders_262_63004()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Presets", prog_num=63005) as cd_stage_263_63005:
            cd_stage_263_63005()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Echosphere/Artist", prog_num=63006) as rm_file_or_dir_264_63006:
                rm_file_or_dir_264_63006()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Echosphere", prog_num=63007) as rm_file_or_dir_265_63007:
                rm_file_or_dir_265_63007()
            with RmFileOrDir(r"/Applications/Waves/Data/Presets/CLA Epic/Artist", prog_num=63008) as rm_file_or_dir_266_63008:
                rm_file_or_dir_266_63008()
            with Stage(r"copy", r"Abbey Road Saturator Presets v1.0.0.6", prog_num=63009):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Abbey Road Saturator", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63010) as should_copy_source_267_63010:
                    should_copy_source_267_63010()
                    with Stage(r"copy source", r"Common/Data/Presets/Abbey Road Saturator", prog_num=63011):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Abbey Road Saturator", r".", delete_extraneous_files=True, prog_num=63012) as copy_dir_to_dir_268_63012:
                            copy_dir_to_dir_268_63012()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Abbey Road Saturator", user_id=-1, group_id=-1, prog_num=63013, recursive=True) as chown_269_63013:
                            chown_269_63013()
            with Stage(r"copy", r"BB Tubes Presets v1.0.0.6", prog_num=63014):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/BB Tubes", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63015) as should_copy_source_270_63015:
                    should_copy_source_270_63015()
                    with Stage(r"copy source", r"Common/Data/Presets/BB Tubes", prog_num=63016):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/BB Tubes", r".", delete_extraneous_files=True, prog_num=63017) as copy_dir_to_dir_271_63017:
                            copy_dir_to_dir_271_63017()
                        with Chown(path=r"/Applications/Waves/Data/Presets/BB Tubes", user_id=-1, group_id=-1, prog_num=63018, recursive=True) as chown_272_63018:
                            chown_272_63018()
            with Stage(r"copy", r"Berzerk Distortion Presets v1.0.0.5", prog_num=63019):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Berzerk Distortion", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63020) as should_copy_source_273_63020:
                    should_copy_source_273_63020()
                    with Stage(r"copy source", r"Common/Data/Presets/Berzerk Distortion", prog_num=63021):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Berzerk Distortion", r".", delete_extraneous_files=True, prog_num=63022) as copy_dir_to_dir_274_63022:
                            copy_dir_to_dir_274_63022()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Berzerk Distortion", user_id=-1, group_id=-1, prog_num=63023, recursive=True) as chown_275_63023:
                            chown_275_63023()
            with Stage(r"copy", r"CLA EchoSphere Presets v1.0.0.9", prog_num=63024):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA EchoSphere", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63025) as should_copy_source_276_63025:
                    should_copy_source_276_63025()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA EchoSphere", prog_num=63026):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA EchoSphere", r".", delete_extraneous_files=True, prog_num=63027) as copy_dir_to_dir_277_63027:
                            copy_dir_to_dir_277_63027()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA EchoSphere", user_id=-1, group_id=-1, prog_num=63028, recursive=True) as chown_278_63028:
                            chown_278_63028()
            with Stage(r"copy", r"CLA Epic Presets v1.0.0.15", prog_num=63029):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA Epic", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63030) as should_copy_source_279_63030:
                    should_copy_source_279_63030()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA Epic", prog_num=63031):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA Epic", r".", delete_extraneous_files=True, prog_num=63032) as copy_dir_to_dir_280_63032:
                            copy_dir_to_dir_280_63032()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA Epic", user_id=-1, group_id=-1, prog_num=63033, recursive=True) as chown_281_63033:
                            chown_281_63033()
            with Stage(r"copy", r"CLA MixHub Presets v1.0.0.8", prog_num=63034):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA MixHub", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63035) as should_copy_source_282_63035:
                    should_copy_source_282_63035()
                    with Stage(r"copy source", r"Common/Data/Presets/CLA MixHub", prog_num=63036):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CLA MixHub", r".", delete_extraneous_files=True, prog_num=63037) as copy_dir_to_dir_283_63037:
                            copy_dir_to_dir_283_63037()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CLA MixHub", user_id=-1, group_id=-1, prog_num=63038, recursive=True) as chown_284_63038:
                            chown_284_63038()
            with Stage(r"copy", r"CR8 Sampler_Presets v1.0.6.10", prog_num=63039):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63040) as should_copy_source_285_63040:
                    should_copy_source_285_63040()
                    with Stage(r"copy source", r"Common/Data/Presets/CR8 Sampler", prog_num=63041):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/CR8 Sampler", r".", delete_extraneous_files=True, prog_num=63042) as copy_dir_to_dir_286_63042:
                            copy_dir_to_dir_286_63042()
                        with Chown(path=r"/Applications/Waves/Data/Presets/CR8 Sampler", user_id=-1, group_id=-1, prog_num=63043, recursive=True) as chown_287_63043:
                            chown_287_63043()
            with Stage(r"copy", r"Clarity_Vx_DeReverb_Pro__Presets v1.0.2.1", prog_num=63044):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63045) as should_copy_source_288_63045:
                    should_copy_source_288_63045()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb Pro", prog_num=63046):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb Pro", r".", delete_extraneous_files=True, prog_num=63047) as copy_dir_to_dir_289_63047:
                            copy_dir_to_dir_289_63047()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb Pro", user_id=-1, group_id=-1, prog_num=63048, recursive=True) as chown_290_63048:
                            chown_290_63048()
            with Stage(r"copy", r"Clarity_Vx_DeReverb__Presets v1.0.2.1", prog_num=63049):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63050) as should_copy_source_291_63050:
                    should_copy_source_291_63050()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx DeReverb", prog_num=63051):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx DeReverb", r".", delete_extraneous_files=True, prog_num=63052) as copy_dir_to_dir_292_63052:
                            copy_dir_to_dir_292_63052()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx DeReverb", user_id=-1, group_id=-1, prog_num=63053, recursive=True) as chown_293_63053:
                            chown_293_63053()
            with Stage(r"copy", r"Clarity_Vx_Pro__Presets v1.0.1.8", prog_num=63054):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63055) as should_copy_source_294_63055:
                    should_copy_source_294_63055()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx Pro", prog_num=63056):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx Pro", r".", delete_extraneous_files=True, prog_num=63057) as copy_dir_to_dir_295_63057:
                            copy_dir_to_dir_295_63057()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx Pro", user_id=-1, group_id=-1, prog_num=63058, recursive=True) as chown_296_63058:
                            chown_296_63058()
            with Stage(r"copy", r"Clarity_Vx__Presets v1.0.1.3", prog_num=63059):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63060) as should_copy_source_297_63060:
                    should_copy_source_297_63060()
                    with Stage(r"copy source", r"Common/Data/Presets/Clarity Vx", prog_num=63061):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Clarity Vx", r".", delete_extraneous_files=True, prog_num=63062) as copy_dir_to_dir_298_63062:
                            copy_dir_to_dir_298_63062()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Clarity Vx", user_id=-1, group_id=-1, prog_num=63063, recursive=True) as chown_299_63063:
                            chown_299_63063()
            with Stage(r"copy", r"Curves_AQ__Presets v1.0.0.1", prog_num=63064):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63065) as should_copy_source_300_63065:
                    should_copy_source_300_63065()
                    with Stage(r"copy source", r"Common/Data/Presets/Curves AQ", prog_num=63066):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves AQ", r".", delete_extraneous_files=True, prog_num=63067) as copy_dir_to_dir_301_63067:
                            copy_dir_to_dir_301_63067()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Curves AQ", user_id=-1, group_id=-1, prog_num=63068, recursive=True) as chown_302_63068:
                            chown_302_63068()
            with Stage(r"copy", r"Curves_Equator__Presets v1.0.0.8", prog_num=63069):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves Equator", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63070) as should_copy_source_303_63070:
                    should_copy_source_303_63070()
                    with Stage(r"copy source", r"Common/Data/Presets/Curves Equator", prog_num=63071):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Curves Equator", r".", delete_extraneous_files=True, prog_num=63072) as copy_dir_to_dir_304_63072:
                            copy_dir_to_dir_304_63072()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Curves Equator", user_id=-1, group_id=-1, prog_num=63073, recursive=True) as chown_305_63073:
                            chown_305_63073()
            with Stage(r"copy", r"Kaleidoscopes Presets v1.1.0.0", prog_num=63074):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Kaleidoscopes", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63075) as should_copy_source_306_63075:
                    should_copy_source_306_63075()
                    with Stage(r"copy source", r"Common/Data/Presets/Kaleidoscopes", prog_num=63076):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Kaleidoscopes", r".", delete_extraneous_files=True, prog_num=63077) as copy_dir_to_dir_307_63077:
                            copy_dir_to_dir_307_63077()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Kaleidoscopes", user_id=-1, group_id=-1, prog_num=63078, recursive=True) as chown_308_63078:
                            chown_308_63078()
            with Stage(r"copy", r"Lofi_Space__Presets v1.0.0.5", prog_num=63079):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63080) as should_copy_source_309_63080:
                    should_copy_source_309_63080()
                    with Stage(r"copy source", r"Common/Data/Presets/Lofi Space", prog_num=63081):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Lofi Space", r".", delete_extraneous_files=True, prog_num=63082) as copy_dir_to_dir_310_63082:
                            copy_dir_to_dir_310_63082()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Lofi Space", user_id=-1, group_id=-1, prog_num=63083, recursive=True) as chown_311_63083:
                            chown_311_63083()
            with Stage(r"copy", r"MDMX Fuzz Presets v1.0.0.4", prog_num=63084):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Fuzz", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63085) as should_copy_source_312_63085:
                    should_copy_source_312_63085()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Fuzz", prog_num=63086):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Fuzz", r".", delete_extraneous_files=True, prog_num=63087) as copy_dir_to_dir_313_63087:
                            copy_dir_to_dir_313_63087()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Fuzz", user_id=-1, group_id=-1, prog_num=63088, recursive=True) as chown_314_63088:
                            chown_314_63088()
            with Stage(r"copy", r"MDMX OverDrive Presets v1.0.0.4", prog_num=63089):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX OverDrive", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63090) as should_copy_source_315_63090:
                    should_copy_source_315_63090()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX OverDrive", prog_num=63091):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX OverDrive", r".", delete_extraneous_files=True, prog_num=63092) as copy_dir_to_dir_316_63092:
                            copy_dir_to_dir_316_63092()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX OverDrive", user_id=-1, group_id=-1, prog_num=63093, recursive=True) as chown_317_63093:
                            chown_317_63093()
            with Stage(r"copy", r"MDMX Screamer Presets v1.0.0.4", prog_num=63094):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Screamer", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63095) as should_copy_source_318_63095:
                    should_copy_source_318_63095()
                    with Stage(r"copy source", r"Common/Data/Presets/MDMX Screamer", prog_num=63096):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MDMX Screamer", r".", delete_extraneous_files=True, prog_num=63097) as copy_dir_to_dir_319_63097:
                            copy_dir_to_dir_319_63097()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MDMX Screamer", user_id=-1, group_id=-1, prog_num=63098, recursive=True) as chown_320_63098:
                            chown_320_63098()
            with Stage(r"copy", r"MagmaChannelStrip__Presets v1.0.0.4", prog_num=63099):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaChannelStrip", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63100) as should_copy_source_321_63100:
                    should_copy_source_321_63100()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaChannelStrip", prog_num=63101):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaChannelStrip", r".", delete_extraneous_files=True, prog_num=63102) as copy_dir_to_dir_322_63102:
                            copy_dir_to_dir_322_63102()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaChannelStrip", user_id=-1, group_id=-1, prog_num=63103, recursive=True) as chown_323_63103:
                            chown_323_63103()
            with Stage(r"copy", r"MagmaSprings__Presets v1.0.0.3", prog_num=63104):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63105) as should_copy_source_324_63105:
                    should_copy_source_324_63105()
                    with Stage(r"copy source", r"Common/Data/Presets/MagmaSprings", prog_num=63106):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MagmaSprings", r".", delete_extraneous_files=True, prog_num=63107) as copy_dir_to_dir_325_63107:
                            copy_dir_to_dir_325_63107()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MagmaSprings", user_id=-1, group_id=-1, prog_num=63108, recursive=True) as chown_326_63108:
                            chown_326_63108()
            with Stage(r"copy", r"MultiMod Distortion Rack Presets v1.0.0.11", prog_num=63109):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MultiMod Rack", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63110) as should_copy_source_327_63110:
                    should_copy_source_327_63110()
                    with Stage(r"copy source", r"Common/Data/Presets/MultiMod Rack", prog_num=63111):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/MultiMod Rack", r".", delete_extraneous_files=True, prog_num=63112) as copy_dir_to_dir_328_63112:
                            copy_dir_to_dir_328_63112()
                        with Chown(path=r"/Applications/Waves/Data/Presets/MultiMod Rack", user_id=-1, group_id=-1, prog_num=63113, recursive=True) as chown_329_63113:
                            chown_329_63113()
            with Stage(r"copy", r"OVox Instrument Presets v1.0.0.1", prog_num=63114):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Instrument", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63115) as should_copy_source_330_63115:
                    should_copy_source_330_63115()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Instrument", prog_num=63116):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Instrument", r".", delete_extraneous_files=True, prog_num=63117) as copy_dir_to_dir_331_63117:
                            copy_dir_to_dir_331_63117()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Instrument", user_id=-1, group_id=-1, prog_num=63118, recursive=True) as chown_332_63118:
                            chown_332_63118()
            with Stage(r"copy", r"OVox Vocal ReSynthesis Presets v1.1.0.2", prog_num=63119):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Vocal ReSynthesis", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63120) as should_copy_source_333_63120:
                    should_copy_source_333_63120()
                    with Stage(r"copy source", r"Common/Data/Presets/OVox Vocal ReSynthesis", prog_num=63121):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/OVox Vocal ReSynthesis", r".", delete_extraneous_files=True, prog_num=63122) as copy_dir_to_dir_334_63122:
                            copy_dir_to_dir_334_63122()
                        with Chown(path=r"/Applications/Waves/Data/Presets/OVox Vocal ReSynthesis", user_id=-1, group_id=-1, prog_num=63123, recursive=True) as chown_335_63123:
                            chown_335_63123()
            with Stage(r"copy", r"Renaissance Bass Presets v1.0.0.5", prog_num=63124):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63125) as should_copy_source_336_63125:
                    should_copy_source_336_63125()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Bass", prog_num=63126):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Bass", r".", delete_extraneous_files=True, prog_num=63127) as copy_dir_to_dir_337_63127:
                            copy_dir_to_dir_337_63127()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Bass", user_id=-1, group_id=-1, prog_num=63128, recursive=True) as chown_338_63128:
                            chown_338_63128()
            with Stage(r"copy", r"Renaissance Channel Presets v1.0.0.4", prog_num=63129):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63130) as should_copy_source_339_63130:
                    should_copy_source_339_63130()
                    with Stage(r"copy source", r"Common/Data/Presets/RChannel", prog_num=63131):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RChannel", r".", delete_extraneous_files=True, prog_num=63132) as copy_dir_to_dir_340_63132:
                            copy_dir_to_dir_340_63132()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RChannel", user_id=-1, group_id=-1, prog_num=63133, recursive=True) as chown_341_63133:
                            chown_341_63133()
            with Stage(r"copy", r"Renaissance Compressor Presets v1.0.0.4", prog_num=63134):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63135) as should_copy_source_342_63135:
                    should_copy_source_342_63135()
                    with Stage(r"copy source", r"Common/Data/Presets/RComp", prog_num=63136):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RComp", r".", delete_extraneous_files=True, prog_num=63137) as copy_dir_to_dir_343_63137:
                            copy_dir_to_dir_343_63137()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RComp", user_id=-1, group_id=-1, prog_num=63138, recursive=True) as chown_344_63138:
                            chown_344_63138()
            with Stage(r"copy", r"Renaissance DeEsser Presets v1.0.0.2", prog_num=63139):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63140) as should_copy_source_345_63140:
                    should_copy_source_345_63140()
                    with Stage(r"copy source", r"Common/Data/Presets/RDeesser", prog_num=63141):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RDeesser", r".", delete_extraneous_files=True, prog_num=63142) as copy_dir_to_dir_346_63142:
                            copy_dir_to_dir_346_63142()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RDeesser", user_id=-1, group_id=-1, prog_num=63143, recursive=True) as chown_347_63143:
                            chown_347_63143()
            with Stage(r"copy", r"Renaissance Equalizer Presets v1.0.0.4", prog_num=63144):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63145) as should_copy_source_348_63145:
                    should_copy_source_348_63145()
                    with Stage(r"copy source", r"Common/Data/Presets/REQ", prog_num=63146):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/REQ", r".", delete_extraneous_files=True, prog_num=63147) as copy_dir_to_dir_349_63147:
                            copy_dir_to_dir_349_63147()
                        with Chown(path=r"/Applications/Waves/Data/Presets/REQ", user_id=-1, group_id=-1, prog_num=63148, recursive=True) as chown_350_63148:
                            chown_350_63148()
            with Stage(r"copy", r"Renaissance Reverb Presets v1.0.0.6", prog_num=63149):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63150) as should_copy_source_351_63150:
                    should_copy_source_351_63150()
                    with Stage(r"copy source", r"Common/Data/Presets/RVerb", prog_num=63151):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RVerb", r".", delete_extraneous_files=True, prog_num=63152) as copy_dir_to_dir_352_63152:
                            copy_dir_to_dir_352_63152()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RVerb", user_id=-1, group_id=-1, prog_num=63153, recursive=True) as chown_353_63153:
                            chown_353_63153()
            with Stage(r"copy", r"Renaissance Vox Presets v1.0.0.3", prog_num=63154):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63155) as should_copy_source_354_63155:
                    should_copy_source_354_63155()
                    with Stage(r"copy source", r"Common/Data/Presets/Renaissance Vox", prog_num=63156):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Renaissance Vox", r".", delete_extraneous_files=True, prog_num=63157) as copy_dir_to_dir_355_63157:
                            copy_dir_to_dir_355_63157()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Renaissance Vox", user_id=-1, group_id=-1, prog_num=63158, recursive=True) as chown_356_63158:
                            chown_356_63158()
            with Stage(r"copy", r"Renaissance Axx Presets v1.0.0.5", prog_num=63159):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63160) as should_copy_source_357_63160:
                    should_copy_source_357_63160()
                    with Stage(r"copy source", r"Common/Data/Presets/RenAxx", prog_num=63161):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/RenAxx", r".", delete_extraneous_files=True, prog_num=63162) as copy_dir_to_dir_358_63162:
                            copy_dir_to_dir_358_63162()
                        with Chown(path=r"/Applications/Waves/Data/Presets/RenAxx", user_id=-1, group_id=-1, prog_num=63163, recursive=True) as chown_359_63163:
                            chown_359_63163()
            with Stage(r"copy", r"Retro_Fi__Presets v1.0.0.9", prog_num=63164):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63165) as should_copy_source_360_63165:
                    should_copy_source_360_63165()
                    with Stage(r"copy source", r"Common/Data/Presets/Retro Fi", prog_num=63166):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Retro Fi", r".", delete_extraneous_files=True, prog_num=63167) as copy_dir_to_dir_361_63167:
                            copy_dir_to_dir_361_63167()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Retro Fi", user_id=-1, group_id=-1, prog_num=63168, recursive=True) as chown_362_63168:
                            chown_362_63168()
            with Stage(r"copy", r"Scheps Omni Channel Presets v1.0.0.6", prog_num=63169):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63170) as should_copy_source_363_63170:
                    should_copy_source_363_63170()
                    with Stage(r"copy source", r"Common/Data/Presets/Scheps Omni Channel", prog_num=63171):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Scheps Omni Channel", r".", delete_extraneous_files=True, prog_num=63172) as copy_dir_to_dir_364_63172:
                            copy_dir_to_dir_364_63172()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Scheps Omni Channel", user_id=-1, group_id=-1, prog_num=63173, recursive=True) as chown_365_63173:
                            chown_365_63173()
            with Stage(r"copy", r"SSL_EV2__Presets v1.0.0.7", prog_num=63174):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/SSL EV2 Channel", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63175) as should_copy_source_366_63175:
                    should_copy_source_366_63175()
                    with Stage(r"copy source", r"Common/Data/Presets/SSL EV2 Channel", prog_num=63176):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/SSL EV2 Channel", r".", delete_extraneous_files=True, prog_num=63177) as copy_dir_to_dir_367_63177:
                            copy_dir_to_dir_367_63177()
                        with Chown(path=r"/Applications/Waves/Data/Presets/SSL EV2 Channel", user_id=-1, group_id=-1, prog_num=63178, recursive=True) as chown_368_63178:
                            chown_368_63178()
            with Stage(r"copy", r"Silk_Vocal__Presets v1.0.0.4", prog_num=63179):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63180) as should_copy_source_369_63180:
                    should_copy_source_369_63180()
                    with Stage(r"copy source", r"Common/Data/Presets/Silk Vocal", prog_num=63181):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Silk Vocal", r".", delete_extraneous_files=True, prog_num=63182) as copy_dir_to_dir_370_63182:
                            copy_dir_to_dir_370_63182()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Silk Vocal", user_id=-1, group_id=-1, prog_num=63183, recursive=True) as chown_371_63183:
                            chown_371_63183()
            with Stage(r"copy", r"Space_Rider__Presets v1.0.0.4", prog_num=63184):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Space Rider", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63185) as should_copy_source_372_63185:
                    should_copy_source_372_63185()
                    with Stage(r"copy source", r"Common/Data/Presets/Space Rider", prog_num=63186):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Space Rider", r".", delete_extraneous_files=True, prog_num=63187) as copy_dir_to_dir_373_63187:
                            copy_dir_to_dir_373_63187()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Space Rider", user_id=-1, group_id=-1, prog_num=63188, recursive=True) as chown_374_63188:
                            chown_374_63188()
            with Stage(r"copy", r"Spherix_Immersive_Compressor__Presets v1.0.0.2", prog_num=63189):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63190) as should_copy_source_375_63190:
                    should_copy_source_375_63190()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Compressor", prog_num=63191):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Compressor", r".", delete_extraneous_files=True, prog_num=63192) as copy_dir_to_dir_376_63192:
                            copy_dir_to_dir_376_63192()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Compressor", user_id=-1, group_id=-1, prog_num=63193, recursive=True) as chown_377_63193:
                            chown_377_63193()
            with Stage(r"copy", r"Spherix_Immersive_Limiter__Presets v1.0.0.1", prog_num=63194):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63195) as should_copy_source_378_63195:
                    should_copy_source_378_63195()
                    with Stage(r"copy source", r"Common/Data/Presets/Spherix Immersive Limiter", prog_num=63196):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Spherix Immersive Limiter", r".", delete_extraneous_files=True, prog_num=63197) as copy_dir_to_dir_379_63197:
                            copy_dir_to_dir_379_63197()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Spherix Immersive Limiter", user_id=-1, group_id=-1, prog_num=63198, recursive=True) as chown_380_63198:
                            chown_380_63198()
            with Stage(r"copy", r"Vocal Bender Presets v1.0.0.10", prog_num=63199):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Vocal Bender", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63200) as should_copy_source_381_63200:
                    should_copy_source_381_63200()
                    with Stage(r"copy source", r"Common/Data/Presets/Vocal Bender", prog_num=63201):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Vocal Bender", r".", delete_extraneous_files=True, prog_num=63202) as copy_dir_to_dir_382_63202:
                            copy_dir_to_dir_382_63202()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Vocal Bender", user_id=-1, group_id=-1, prog_num=63203, recursive=True) as chown_383_63203:
                            chown_383_63203()
            with Stage(r"copy", r"VoltageAmpsBass__Presets v1.0.0.6", prog_num=63204):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63205) as should_copy_source_384_63205:
                    should_copy_source_384_63205()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Bass", prog_num=63206):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=63207) as copy_dir_to_dir_385_63207:
                            copy_dir_to_dir_385_63207()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=63208, recursive=True) as chown_386_63208:
                            chown_386_63208()
            with Stage(r"copy", r"VoltageAmpsGuitar__Presets v1.0.0.7", prog_num=63209):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63210) as should_copy_source_387_63210:
                    should_copy_source_387_63210()
                    with Stage(r"copy source", r"Common/Data/Presets/Voltage Amps Guitar", prog_num=63211):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=63212) as copy_dir_to_dir_388_63212:
                            copy_dir_to_dir_388_63212()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=63213, recursive=True) as chown_389_63213:
                            chown_389_63213()
            with Stage(r"copy", r"Waves Harmony Presets v1.0.0.18", prog_num=63214):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r"/Applications/Waves/Data/Presets", skip_progress_count=3, prog_num=63215) as should_copy_source_390_63215:
                    should_copy_source_390_63215()
                    with Stage(r"copy source", r"Common/Data/Presets/Waves Harmony", prog_num=63216):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Presets/Waves Harmony", r".", delete_extraneous_files=True, prog_num=63217) as copy_dir_to_dir_391_63217:
                            copy_dir_to_dir_391_63217()
                        with Chown(path=r"/Applications/Waves/Data/Presets/Waves Harmony", user_id=-1, group_id=-1, prog_num=63218, recursive=True) as chown_392_63218:
                            chown_392_63218()
            with RmFileOrDir(r"/Applications/Waves/Data/CLA MixHub Data", prog_num=63219) as rm_file_or_dir_393_63219:
                rm_file_or_dir_393_63219()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/Vocal Bender", prog_num=63220) as rm_file_or_dir_394_63220:
                rm_file_or_dir_394_63220()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Vocal Bender Stereo.xml", prog_num=63221) as rm_file_or_dir_395_63221:
                rm_file_or_dir_395_63221()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Setup Libraries", prog_num=63222) as cd_stage_396_63222:
            cd_stage_396_63222()
            with Stage(r"copy", r"AudioTrack Setups library v1.0.0.1", prog_num=63223):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63224) as should_copy_source_397_63224:
                    should_copy_source_397_63224()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/AudioTrack Setups library", prog_num=63225):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/AudioTrack Setups library", r".", delete_extraneous_files=True, prog_num=63226) as copy_dir_to_dir_398_63226:
                            copy_dir_to_dir_398_63226()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/AudioTrack Setups library", user_id=-1, group_id=-1, prog_num=63227, recursive=True) as chown_399_63227:
                            chown_399_63227()
            with Stage(r"copy", r"C1 Compressor Setups Library v1.0.0.1", prog_num=63228):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63229) as should_copy_source_400_63229:
                    should_copy_source_400_63229()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/C1 Setups Library", prog_num=63230):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/C1 Setups Library", r".", delete_extraneous_files=True, prog_num=63231) as copy_dir_to_dir_401_63231:
                            copy_dir_to_dir_401_63231()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/C1 Setups Library", user_id=-1, group_id=-1, prog_num=63232, recursive=True) as chown_402_63232:
                            chown_402_63232()
            with Stage(r"copy", r"MetaFlanger Setups Library v1.0.0.1", prog_num=63233):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63234) as should_copy_source_403_63234:
                    should_copy_source_403_63234()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/MetaFlanger Setup Library", prog_num=63235):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/MetaFlanger Setup Library", r".", delete_extraneous_files=True, prog_num=63236) as copy_dir_to_dir_404_63236:
                            copy_dir_to_dir_404_63236()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/MetaFlanger Setup Library", user_id=-1, group_id=-1, prog_num=63237, recursive=True) as chown_405_63237:
                            chown_405_63237()
            with Stage(r"copy", r"PS22_DLA SetupLibrary v1.0.0.1", prog_num=63238):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63239) as should_copy_source_406_63239:
                    should_copy_source_406_63239()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/PS22_DLA SetupLibrary", prog_num=63240):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/PS22_DLA SetupLibrary", r".", delete_extraneous_files=True, prog_num=63241) as copy_dir_to_dir_407_63241:
                            copy_dir_to_dir_407_63241()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/PS22_DLA SetupLibrary", user_id=-1, group_id=-1, prog_num=63242, recursive=True) as chown_408_63242:
                            chown_408_63242()
            with Stage(r"copy", r"Q10 Setups Library v1.0.0.1", prog_num=63243):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63244) as should_copy_source_409_63244:
                    should_copy_source_409_63244()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Q10 Setups Library", prog_num=63245):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Q10 Setups Library", r".", delete_extraneous_files=True, prog_num=63246) as copy_dir_to_dir_410_63246:
                            copy_dir_to_dir_410_63246()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Q10 Setups Library", user_id=-1, group_id=-1, prog_num=63247, recursive=True) as chown_411_63247:
                            chown_411_63247()
            with Stage(r"copy", r"Renaissance EQ Setup Lib v1.0.0.0", prog_num=63248):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63249) as should_copy_source_412_63249:
                    should_copy_source_412_63249()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/Renaissance EQ Setup Lib", prog_num=63250):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/Renaissance EQ Setup Lib", r".", delete_extraneous_files=True, prog_num=63251) as copy_dir_to_dir_413_63251:
                            copy_dir_to_dir_413_63251()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/Renaissance EQ Setup Lib", user_id=-1, group_id=-1, prog_num=63252, recursive=True) as chown_414_63252:
                            chown_414_63252()
            with Stage(r"copy", r"TrueVerb Setups Library v1.0.0.1", prog_num=63253):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r"/Applications/Waves/Data/Setup Libraries", skip_progress_count=3, prog_num=63254) as should_copy_source_415_63254:
                    should_copy_source_415_63254()
                    with Stage(r"copy source", r"Common/Data/Setup Libraries/TrueVerb Setups Library", prog_num=63255):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Setup Libraries/TrueVerb Setups Library", r".", delete_extraneous_files=True, prog_num=63256) as copy_dir_to_dir_416_63256:
                            copy_dir_to_dir_416_63256()
                        with Chown(path=r"/Applications/Waves/Data/Setup Libraries/TrueVerb Setups Library", user_id=-1, group_id=-1, prog_num=63257, recursive=True) as chown_417_63257:
                            chown_417_63257()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/Voltage Amps IR", prog_num=63258) as cd_stage_418_63258:
            cd_stage_418_63258()
            with Stage(r"copy", r"VoltageAmpsBass__Data_Folders v1.0.0.2", prog_num=63259):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=63260) as should_copy_source_419_63260:
                    should_copy_source_419_63260()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Bass", prog_num=63261):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Bass", r".", delete_extraneous_files=True, prog_num=63262) as copy_dir_to_dir_420_63262:
                            copy_dir_to_dir_420_63262()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Bass", user_id=-1, group_id=-1, prog_num=63263, recursive=True) as chown_421_63263:
                            chown_421_63263()
            with Stage(r"copy", r"VoltageAmpsGuitar__Data_Folders v1.0.0.1", prog_num=63264):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r"/Applications/Waves/Data/Voltage Amps IR", skip_progress_count=3, prog_num=63265) as should_copy_source_422_63265:
                    should_copy_source_422_63265()
                    with Stage(r"copy source", r"Common/Data/Voltage Amps IR/Voltage Amps Guitar", prog_num=63266):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Voltage Amps IR/Voltage Amps Guitar", r".", delete_extraneous_files=True, prog_num=63267) as copy_dir_to_dir_423_63267:
                            copy_dir_to_dir_423_63267()
                        with Chown(path=r"/Applications/Waves/Data/Voltage Amps IR/Voltage Amps Guitar", user_id=-1, group_id=-1, prog_num=63268, recursive=True) as chown_424_63268:
                            chown_424_63268()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR", prog_num=63269) as cd_stage_425_63269:
            cd_stage_425_63269()
            with Stage(r"copy", r"GTR Amps and Cabinets v2.0.0.0", prog_num=63270):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=63271) as should_copy_source_426_63271:
                    should_copy_source_426_63271()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Amps", prog_num=63272):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Amps.wtar.aa", where_to_unwtar=r".", prog_num=63273) as unwtar_427_63273:
                            unwtar_427_63273()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets", r"/Applications/Waves/Data/WavesGTR", skip_progress_count=2, prog_num=63274) as should_copy_source_428_63274:
                    should_copy_source_428_63274()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Cabinets", prog_num=63275):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Cabinets.wtar.aa", where_to_unwtar=r".", prog_num=63276) as unwtar_429_63276:
                            unwtar_429_63276()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Data/WavesGTR/Presets", prog_num=63277) as cd_stage_430_63277:
            cd_stage_430_63277()
            with Stage(r"copy", r"GTR Solo Presets v1.1.0.0", prog_num=63278):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR-Solo", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=63279) as should_copy_source_431_63279:
                    should_copy_source_431_63279()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR-Solo", prog_num=63280):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR-Solo.wtar.aa", where_to_unwtar=r".", prog_num=63281) as unwtar_432_63281:
                            unwtar_432_63281()
            with Stage(r"copy", r"GTR Presets v1.0.0.3", prog_num=63282):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR", r"/Applications/Waves/Data/WavesGTR/Presets", skip_progress_count=2, prog_num=63283) as should_copy_source_433_63283:
                    should_copy_source_433_63283()
                    with Stage(r"copy source", r"Common/Data/WavesGTR/Presets/GTR", prog_num=63284):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/WavesGTR/Presets/GTR.wtar.aa", where_to_unwtar=r".", prog_num=63285) as unwtar_434_63285:
                            unwtar_434_63285()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16", prog_num=63286) as cd_stage_435_63286:
            cd_stage_435_63286()
            with Stage(r"copy", r"API-2500 v16.0.23.24", prog_num=63287):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63288) as should_copy_source_436_63288:
                    should_copy_source_436_63288()
                    with Stage(r"copy source", r"Mac/Plugins/API-2500.bundle", prog_num=63289):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", r".", delete_extraneous_files=True, prog_num=63290) as copy_dir_to_dir_437_63290:
                            copy_dir_to_dir_437_63290()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-2500.bundle", where_to_unwtar=r".", prog_num=63291) as unwtar_438_63291:
                            unwtar_438_63291()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-2500.bundle", user_id=-1, group_id=-1, prog_num=63292, recursive=True) as chown_439_63292:
                            chown_439_63292()
            with Stage(r"copy", r"API-550 v16.0.23.24", prog_num=63293):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63294) as should_copy_source_440_63294:
                    should_copy_source_440_63294()
                    with Stage(r"copy source", r"Mac/Plugins/API-550.bundle", prog_num=63295):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", r".", delete_extraneous_files=True, prog_num=63296) as copy_dir_to_dir_441_63296:
                            copy_dir_to_dir_441_63296()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-550.bundle", where_to_unwtar=r".", prog_num=63297) as unwtar_442_63297:
                            unwtar_442_63297()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-550.bundle", user_id=-1, group_id=-1, prog_num=63298, recursive=True) as chown_443_63298:
                            chown_443_63298()
            with Stage(r"copy", r"API-560 v16.0.23.24", prog_num=63299):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63300) as should_copy_source_444_63300:
                    should_copy_source_444_63300()
                    with Stage(r"copy source", r"Mac/Plugins/API-560.bundle", prog_num=63301):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", r".", delete_extraneous_files=True, prog_num=63302) as copy_dir_to_dir_445_63302:
                            copy_dir_to_dir_445_63302()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/API-560.bundle", where_to_unwtar=r".", prog_num=63303) as unwtar_446_63303:
                            unwtar_446_63303()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/API-560.bundle", user_id=-1, group_id=-1, prog_num=63304, recursive=True) as chown_447_63304:
                            chown_447_63304()
            with Stage(r"copy", r"Abbey Road Chambers v16.0.23.24", prog_num=63305):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63306) as should_copy_source_448_63306:
                    should_copy_source_448_63306()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Chambers.bundle", prog_num=63307):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", r".", delete_extraneous_files=True, prog_num=63308) as copy_dir_to_dir_449_63308:
                            copy_dir_to_dir_449_63308()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Chambers.bundle", where_to_unwtar=r".", prog_num=63309) as unwtar_450_63309:
                            unwtar_450_63309()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Chambers.bundle", user_id=-1, group_id=-1, prog_num=63310, recursive=True) as chown_451_63310:
                            chown_451_63310()
            with Stage(r"copy", r"ARPlates v16.0.23.24", prog_num=63311):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63312) as should_copy_source_452_63312:
                    should_copy_source_452_63312()
                    with Stage(r"copy source", r"Mac/Plugins/ARPlates.bundle", prog_num=63313):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", r".", delete_extraneous_files=True, prog_num=63314) as copy_dir_to_dir_453_63314:
                            copy_dir_to_dir_453_63314()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ARPlates.bundle", where_to_unwtar=r".", prog_num=63315) as unwtar_454_63315:
                            unwtar_454_63315()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ARPlates.bundle", user_id=-1, group_id=-1, prog_num=63316, recursive=True) as chown_455_63316:
                            chown_455_63316()
            with Stage(r"copy", r"Abbey Road Vinyl v16.0.23.24", prog_num=63317):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63318) as should_copy_source_456_63318:
                    should_copy_source_456_63318()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Vinyl.bundle", prog_num=63319):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", r".", delete_extraneous_files=True, prog_num=63320) as copy_dir_to_dir_457_63320:
                            copy_dir_to_dir_457_63320()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Vinyl.bundle", where_to_unwtar=r".", prog_num=63321) as unwtar_458_63321:
                            unwtar_458_63321()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Vinyl.bundle", user_id=-1, group_id=-1, prog_num=63322, recursive=True) as chown_459_63322:
                            chown_459_63322()
            with Stage(r"copy", r"Abbey Road RS124 v16.0.23.24", prog_num=63323):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63324) as should_copy_source_460_63324:
                    should_copy_source_460_63324()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road RS124.bundle", prog_num=63325):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", r".", delete_extraneous_files=True, prog_num=63326) as copy_dir_to_dir_461_63326:
                            copy_dir_to_dir_461_63326()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road RS124.bundle", where_to_unwtar=r".", prog_num=63327) as unwtar_462_63327:
                            unwtar_462_63327()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road RS124.bundle", user_id=-1, group_id=-1, prog_num=63328, recursive=True) as chown_463_63328:
                            chown_463_63328()
            with Stage(r"copy", r"Abbey Road Studio 3 v16.0.23.24", prog_num=63329):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63330) as should_copy_source_464_63330:
                    should_copy_source_464_63330()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Studio 3.bundle", prog_num=63331):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", r".", delete_extraneous_files=True, prog_num=63332) as copy_dir_to_dir_465_63332:
                            copy_dir_to_dir_465_63332()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Studio 3.bundle", where_to_unwtar=r".", prog_num=63333) as unwtar_466_63333:
                            unwtar_466_63333()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Studio 3.bundle", user_id=-1, group_id=-1, prog_num=63334, recursive=True) as chown_467_63334:
                            chown_467_63334()
            with Stage(r"copy", r"Abbey Road Saturator v16.0.23.24", prog_num=63335):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63336) as should_copy_source_468_63336:
                    should_copy_source_468_63336()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road Saturator.bundle", prog_num=63337):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", r".", delete_extraneous_files=True, prog_num=63338) as copy_dir_to_dir_469_63338:
                            copy_dir_to_dir_469_63338()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road Saturator.bundle", where_to_unwtar=r".", prog_num=63339) as unwtar_470_63339:
                            unwtar_470_63339()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road Saturator.bundle", user_id=-1, group_id=-1, prog_num=63340, recursive=True) as chown_471_63340:
                            chown_471_63340()
            with Stage(r"copy", r"Aphex AX v16.0.23.24", prog_num=63341):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63342) as should_copy_source_472_63342:
                    should_copy_source_472_63342()
                    with Stage(r"copy source", r"Mac/Plugins/Aphex AX.bundle", prog_num=63343):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", r".", delete_extraneous_files=True, prog_num=63344) as copy_dir_to_dir_473_63344:
                            copy_dir_to_dir_473_63344()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Aphex AX.bundle", where_to_unwtar=r".", prog_num=63345) as unwtar_474_63345:
                            unwtar_474_63345()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Aphex AX.bundle", user_id=-1, group_id=-1, prog_num=63346, recursive=True) as chown_475_63346:
                            chown_475_63346()
            with Stage(r"copy", r"AudioTrack v16.0.23.24", prog_num=63347):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63348) as should_copy_source_476_63348:
                    should_copy_source_476_63348()
                    with Stage(r"copy source", r"Mac/Plugins/AudioTrack.bundle", prog_num=63349):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", r".", delete_extraneous_files=True, prog_num=63350) as copy_dir_to_dir_477_63350:
                            copy_dir_to_dir_477_63350()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AudioTrack.bundle", where_to_unwtar=r".", prog_num=63351) as unwtar_478_63351:
                            unwtar_478_63351()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AudioTrack.bundle", user_id=-1, group_id=-1, prog_num=63352, recursive=True) as chown_479_63352:
                            chown_479_63352()
            with Stage(r"copy", r"B360 v16.0.23.24", prog_num=63353):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63354) as should_copy_source_480_63354:
                    should_copy_source_480_63354()
                    with Stage(r"copy source", r"Mac/Plugins/B360.bundle", prog_num=63355):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", r".", delete_extraneous_files=True, prog_num=63356) as copy_dir_to_dir_481_63356:
                            copy_dir_to_dir_481_63356()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/B360.bundle", where_to_unwtar=r".", prog_num=63357) as unwtar_482_63357:
                            unwtar_482_63357()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/B360.bundle", user_id=-1, group_id=-1, prog_num=63358, recursive=True) as chown_483_63358:
                            chown_483_63358()
            with Stage(r"copy", r"BB Tubes v16.0.23.24", prog_num=63359):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63360) as should_copy_source_484_63360:
                    should_copy_source_484_63360()
                    with Stage(r"copy source", r"Mac/Plugins/BB Tubes.bundle", prog_num=63361):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", r".", delete_extraneous_files=True, prog_num=63362) as copy_dir_to_dir_485_63362:
                            copy_dir_to_dir_485_63362()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/BB Tubes.bundle", where_to_unwtar=r".", prog_num=63363) as unwtar_486_63363:
                            unwtar_486_63363()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/BB Tubes.bundle", user_id=-1, group_id=-1, prog_num=63364, recursive=True) as chown_487_63364:
                            chown_487_63364()
            with Stage(r"copy", r"Bass Fingers v16.0.23.24", prog_num=63365):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63366) as should_copy_source_488_63366:
                    should_copy_source_488_63366()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Fingers.bundle", prog_num=63367):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", r".", delete_extraneous_files=True, prog_num=63368) as copy_dir_to_dir_489_63368:
                            copy_dir_to_dir_489_63368()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Fingers.bundle", where_to_unwtar=r".", prog_num=63369) as unwtar_490_63369:
                            unwtar_490_63369()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Fingers.bundle", user_id=-1, group_id=-1, prog_num=63370, recursive=True) as chown_491_63370:
                            chown_491_63370()
            with Stage(r"copy", r"Bass Rider v16.0.23.24", prog_num=63371):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63372) as should_copy_source_492_63372:
                    should_copy_source_492_63372()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Rider.bundle", prog_num=63373):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", r".", delete_extraneous_files=True, prog_num=63374) as copy_dir_to_dir_493_63374:
                            copy_dir_to_dir_493_63374()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Rider.bundle", where_to_unwtar=r".", prog_num=63375) as unwtar_494_63375:
                            unwtar_494_63375()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Rider.bundle", user_id=-1, group_id=-1, prog_num=63376, recursive=True) as chown_495_63376:
                            chown_495_63376()
            with Stage(r"copy", r"Bass Slapper v16.0.23.24", prog_num=63377):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63378) as should_copy_source_496_63378:
                    should_copy_source_496_63378()
                    with Stage(r"copy source", r"Mac/Plugins/Bass Slapper.bundle", prog_num=63379):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", r".", delete_extraneous_files=True, prog_num=63380) as copy_dir_to_dir_497_63380:
                            copy_dir_to_dir_497_63380()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Bass Slapper.bundle", where_to_unwtar=r".", prog_num=63381) as unwtar_498_63381:
                            unwtar_498_63381()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Bass Slapper.bundle", user_id=-1, group_id=-1, prog_num=63382, recursive=True) as chown_499_63382:
                            chown_499_63382()
            with Stage(r"copy", r"Berzerk Distortion v16.0.23.24", prog_num=63383):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63384) as should_copy_source_500_63384:
                    should_copy_source_500_63384()
                    with Stage(r"copy source", r"Mac/Plugins/Berzerk Distortion.bundle", prog_num=63385):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", r".", delete_extraneous_files=True, prog_num=63386) as copy_dir_to_dir_501_63386:
                            copy_dir_to_dir_501_63386()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Berzerk Distortion.bundle", where_to_unwtar=r".", prog_num=63387) as unwtar_502_63387:
                            unwtar_502_63387()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Berzerk Distortion.bundle", user_id=-1, group_id=-1, prog_num=63388, recursive=True) as chown_503_63388:
                            chown_503_63388()
            with Stage(r"copy", r"Brauer Motion v16.0.23.24", prog_num=63389):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63390) as should_copy_source_504_63390:
                    should_copy_source_504_63390()
                    with Stage(r"copy source", r"Mac/Plugins/Brauer Motion.bundle", prog_num=63391):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", r".", delete_extraneous_files=True, prog_num=63392) as copy_dir_to_dir_505_63392:
                            copy_dir_to_dir_505_63392()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Brauer Motion.bundle", where_to_unwtar=r".", prog_num=63393) as unwtar_506_63393:
                            unwtar_506_63393()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Brauer Motion.bundle", user_id=-1, group_id=-1, prog_num=63394, recursive=True) as chown_507_63394:
                            chown_507_63394()
            with Stage(r"copy", r"Butch Vig Vocals v16.0.23.24", prog_num=63395):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63396) as should_copy_source_508_63396:
                    should_copy_source_508_63396()
                    with Stage(r"copy source", r"Mac/Plugins/Butch Vig Vocals.bundle", prog_num=63397):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63398) as copy_dir_to_dir_509_63398:
                            copy_dir_to_dir_509_63398()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Butch Vig Vocals.bundle", where_to_unwtar=r".", prog_num=63399) as unwtar_510_63399:
                            unwtar_510_63399()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Butch Vig Vocals.bundle", user_id=-1, group_id=-1, prog_num=63400, recursive=True) as chown_511_63400:
                            chown_511_63400()
            with Stage(r"copy", r"C1 v16.0.23.24", prog_num=63401):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63402) as should_copy_source_512_63402:
                    should_copy_source_512_63402()
                    with Stage(r"copy source", r"Mac/Plugins/C1.bundle", prog_num=63403):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", r".", delete_extraneous_files=True, prog_num=63404) as copy_dir_to_dir_513_63404:
                            copy_dir_to_dir_513_63404()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C1.bundle", where_to_unwtar=r".", prog_num=63405) as unwtar_514_63405:
                            unwtar_514_63405()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C1.bundle", user_id=-1, group_id=-1, prog_num=63406, recursive=True) as chown_515_63406:
                            chown_515_63406()
            with Stage(r"copy", r"C360 v16.0.23.24", prog_num=63407):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63408) as should_copy_source_516_63408:
                    should_copy_source_516_63408()
                    with Stage(r"copy source", r"Mac/Plugins/C360.bundle", prog_num=63409):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", r".", delete_extraneous_files=True, prog_num=63410) as copy_dir_to_dir_517_63410:
                            copy_dir_to_dir_517_63410()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C360.bundle", where_to_unwtar=r".", prog_num=63411) as unwtar_518_63411:
                            unwtar_518_63411()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C360.bundle", user_id=-1, group_id=-1, prog_num=63412, recursive=True) as chown_519_63412:
                            chown_519_63412()
            with Stage(r"copy", r"C4 v16.0.23.24", prog_num=63413):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63414) as should_copy_source_520_63414:
                    should_copy_source_520_63414()
                    with Stage(r"copy source", r"Mac/Plugins/C4.bundle", prog_num=63415):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", r".", delete_extraneous_files=True, prog_num=63416) as copy_dir_to_dir_521_63416:
                            copy_dir_to_dir_521_63416()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C4.bundle", where_to_unwtar=r".", prog_num=63417) as unwtar_522_63417:
                            unwtar_522_63417()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C4.bundle", user_id=-1, group_id=-1, prog_num=63418, recursive=True) as chown_523_63418:
                            chown_523_63418()
            with Stage(r"copy", r"C6 v16.0.23.24", prog_num=63419):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63420) as should_copy_source_524_63420:
                    should_copy_source_524_63420()
                    with Stage(r"copy source", r"Mac/Plugins/C6.bundle", prog_num=63421):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", r".", delete_extraneous_files=True, prog_num=63422) as copy_dir_to_dir_525_63422:
                            copy_dir_to_dir_525_63422()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/C6.bundle", where_to_unwtar=r".", prog_num=63423) as unwtar_526_63423:
                            unwtar_526_63423()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/C6.bundle", user_id=-1, group_id=-1, prog_num=63424, recursive=True) as chown_527_63424:
                            chown_527_63424()
            with Stage(r"copy", r"CLA-2A v16.0.23.24", prog_num=63425):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63426) as should_copy_source_528_63426:
                    should_copy_source_528_63426()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-2A.bundle", prog_num=63427):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", r".", delete_extraneous_files=True, prog_num=63428) as copy_dir_to_dir_529_63428:
                            copy_dir_to_dir_529_63428()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-2A.bundle", where_to_unwtar=r".", prog_num=63429) as unwtar_530_63429:
                            unwtar_530_63429()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-2A.bundle", user_id=-1, group_id=-1, prog_num=63430, recursive=True) as chown_531_63430:
                            chown_531_63430()
            with Stage(r"copy", r"CLA-3A v16.0.23.24", prog_num=63431):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63432) as should_copy_source_532_63432:
                    should_copy_source_532_63432()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-3A.bundle", prog_num=63433):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", r".", delete_extraneous_files=True, prog_num=63434) as copy_dir_to_dir_533_63434:
                            copy_dir_to_dir_533_63434()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-3A.bundle", where_to_unwtar=r".", prog_num=63435) as unwtar_534_63435:
                            unwtar_534_63435()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-3A.bundle", user_id=-1, group_id=-1, prog_num=63436, recursive=True) as chown_535_63436:
                            chown_535_63436()
            with Stage(r"copy", r"CLA-76 v16.0.23.24", prog_num=63437):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63438) as should_copy_source_536_63438:
                    should_copy_source_536_63438()
                    with Stage(r"copy source", r"Mac/Plugins/CLA-76.bundle", prog_num=63439):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", r".", delete_extraneous_files=True, prog_num=63440) as copy_dir_to_dir_537_63440:
                            copy_dir_to_dir_537_63440()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA-76.bundle", where_to_unwtar=r".", prog_num=63441) as unwtar_538_63441:
                            unwtar_538_63441()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA-76.bundle", user_id=-1, group_id=-1, prog_num=63442, recursive=True) as chown_539_63442:
                            chown_539_63442()
            with Stage(r"copy", r"CLA Bass v16.0.23.24", prog_num=63443):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63444) as should_copy_source_540_63444:
                    should_copy_source_540_63444()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Bass.bundle", prog_num=63445):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", r".", delete_extraneous_files=True, prog_num=63446) as copy_dir_to_dir_541_63446:
                            copy_dir_to_dir_541_63446()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Bass.bundle", where_to_unwtar=r".", prog_num=63447) as unwtar_542_63447:
                            unwtar_542_63447()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Bass.bundle", user_id=-1, group_id=-1, prog_num=63448, recursive=True) as chown_543_63448:
                            chown_543_63448()
            with Stage(r"copy", r"CLA Drums v16.0.23.24", prog_num=63449):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63450) as should_copy_source_544_63450:
                    should_copy_source_544_63450()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Drums.bundle", prog_num=63451):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", r".", delete_extraneous_files=True, prog_num=63452) as copy_dir_to_dir_545_63452:
                            copy_dir_to_dir_545_63452()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Drums.bundle", where_to_unwtar=r".", prog_num=63453) as unwtar_546_63453:
                            unwtar_546_63453()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Drums.bundle", user_id=-1, group_id=-1, prog_num=63454, recursive=True) as chown_547_63454:
                            chown_547_63454()
            with Stage(r"copy", r"CLA EchoSphere v16.0.23.24", prog_num=63455):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63456) as should_copy_source_548_63456:
                    should_copy_source_548_63456()
                    with Stage(r"copy source", r"Mac/Plugins/CLA EchoSphere.bundle", prog_num=63457):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", r".", delete_extraneous_files=True, prog_num=63458) as copy_dir_to_dir_549_63458:
                            copy_dir_to_dir_549_63458()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA EchoSphere.bundle", where_to_unwtar=r".", prog_num=63459) as unwtar_550_63459:
                            unwtar_550_63459()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA EchoSphere.bundle", user_id=-1, group_id=-1, prog_num=63460, recursive=True) as chown_551_63460:
                            chown_551_63460()
            with Stage(r"copy", r"CLA Effects v16.0.23.24", prog_num=63461):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63462) as should_copy_source_552_63462:
                    should_copy_source_552_63462()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Effects.bundle", prog_num=63463):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", r".", delete_extraneous_files=True, prog_num=63464) as copy_dir_to_dir_553_63464:
                            copy_dir_to_dir_553_63464()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Effects.bundle", where_to_unwtar=r".", prog_num=63465) as unwtar_554_63465:
                            unwtar_554_63465()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Effects.bundle", user_id=-1, group_id=-1, prog_num=63466, recursive=True) as chown_555_63466:
                            chown_555_63466()
            with Stage(r"copy", r"CLA Epic v16.0.23.24", prog_num=63467):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63468) as should_copy_source_556_63468:
                    should_copy_source_556_63468()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Epic.bundle", prog_num=63469):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", r".", delete_extraneous_files=True, prog_num=63470) as copy_dir_to_dir_557_63470:
                            copy_dir_to_dir_557_63470()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Epic.bundle", where_to_unwtar=r".", prog_num=63471) as unwtar_558_63471:
                            unwtar_558_63471()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Epic.bundle", user_id=-1, group_id=-1, prog_num=63472, recursive=True) as chown_559_63472:
                            chown_559_63472()
            with Stage(r"copy", r"CLA Guitars v16.0.23.24", prog_num=63473):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63474) as should_copy_source_560_63474:
                    should_copy_source_560_63474()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Guitars.bundle", prog_num=63475):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", r".", delete_extraneous_files=True, prog_num=63476) as copy_dir_to_dir_561_63476:
                            copy_dir_to_dir_561_63476()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Guitars.bundle", where_to_unwtar=r".", prog_num=63477) as unwtar_562_63477:
                            unwtar_562_63477()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Guitars.bundle", user_id=-1, group_id=-1, prog_num=63478, recursive=True) as chown_563_63478:
                            chown_563_63478()
            with Stage(r"copy", r"CLA MixDown v16.0.23.24", prog_num=63479):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63480) as should_copy_source_564_63480:
                    should_copy_source_564_63480()
                    with Stage(r"copy source", r"Mac/Plugins/CLA MixDown.bundle", prog_num=63481):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", r".", delete_extraneous_files=True, prog_num=63482) as copy_dir_to_dir_565_63482:
                            copy_dir_to_dir_565_63482()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixDown.bundle", where_to_unwtar=r".", prog_num=63483) as unwtar_566_63483:
                            unwtar_566_63483()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA MixDown.bundle", user_id=-1, group_id=-1, prog_num=63484, recursive=True) as chown_567_63484:
                            chown_567_63484()
            with Stage(r"copy", r"CLA MixHub v16.0.30.31", prog_num=63485):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63486) as should_copy_source_568_63486:
                    should_copy_source_568_63486()
                    with Stage(r"copy source", r"Mac/Plugins/CLA MixHub.bundle", prog_num=63487):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", r".", delete_extraneous_files=True, prog_num=63488) as copy_dir_to_dir_569_63488:
                            copy_dir_to_dir_569_63488()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA MixHub.bundle", where_to_unwtar=r".", prog_num=63489) as unwtar_570_63489:
                            unwtar_570_63489()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA MixHub.bundle", user_id=-1, group_id=-1, prog_num=63490, recursive=True) as chown_571_63490:
                            chown_571_63490()
            with Stage(r"copy", r"CLA Nx v16.0.23.24", prog_num=63491):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63492) as should_copy_source_572_63492:
                    should_copy_source_572_63492()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Nx.bundle", prog_num=63493):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", r".", delete_extraneous_files=True, prog_num=63494) as copy_dir_to_dir_573_63494:
                            copy_dir_to_dir_573_63494()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Nx.bundle", where_to_unwtar=r".", prog_num=63495) as unwtar_574_63495:
                            unwtar_574_63495()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Nx.bundle", user_id=-1, group_id=-1, prog_num=63496, recursive=True) as chown_575_63496:
                            chown_575_63496()
            with Stage(r"copy", r"CLA Unplugged v16.0.23.24", prog_num=63497):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63498) as should_copy_source_576_63498:
                    should_copy_source_576_63498()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Unplugged.bundle", prog_num=63499):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", r".", delete_extraneous_files=True, prog_num=63500) as copy_dir_to_dir_577_63500:
                            copy_dir_to_dir_577_63500()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Unplugged.bundle", where_to_unwtar=r".", prog_num=63501) as unwtar_578_63501:
                            unwtar_578_63501()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Unplugged.bundle", user_id=-1, group_id=-1, prog_num=63502, recursive=True) as chown_579_63502:
                            chown_579_63502()
            with Stage(r"copy", r"CLA Vocals v16.0.23.24", prog_num=63503):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63504) as should_copy_source_580_63504:
                    should_copy_source_580_63504()
                    with Stage(r"copy source", r"Mac/Plugins/CLA Vocals.bundle", prog_num=63505):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63506) as copy_dir_to_dir_581_63506:
                            copy_dir_to_dir_581_63506()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CLA Vocals.bundle", where_to_unwtar=r".", prog_num=63507) as unwtar_582_63507:
                            unwtar_582_63507()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CLA Vocals.bundle", user_id=-1, group_id=-1, prog_num=63508, recursive=True) as chown_583_63508:
                            chown_583_63508()
            with Stage(r"copy", r"CODEX v16.0.23.24", prog_num=63509):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63510) as should_copy_source_584_63510:
                    should_copy_source_584_63510()
                    with Stage(r"copy source", r"Mac/Plugins/CODEX.bundle", prog_num=63511):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", r".", delete_extraneous_files=True, prog_num=63512) as copy_dir_to_dir_585_63512:
                            copy_dir_to_dir_585_63512()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CODEX.bundle", where_to_unwtar=r".", prog_num=63513) as unwtar_586_63513:
                            unwtar_586_63513()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CODEX.bundle", user_id=-1, group_id=-1, prog_num=63514, recursive=True) as chown_587_63514:
                            chown_587_63514()
            with Stage(r"copy", r"COSMOS_Plugin v16.0.23.24", prog_num=63515):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63516) as should_copy_source_588_63516:
                    should_copy_source_588_63516()
                    with Stage(r"copy source", r"Mac/Plugins/COSMOS.bundle", prog_num=63517):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", r".", delete_extraneous_files=True, prog_num=63518) as copy_dir_to_dir_589_63518:
                            copy_dir_to_dir_589_63518()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/COSMOS.bundle", where_to_unwtar=r".", prog_num=63519) as unwtar_590_63519:
                            unwtar_590_63519()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/COSMOS.bundle", user_id=-1, group_id=-1, prog_num=63520, recursive=True) as chown_591_63520:
                            chown_591_63520()
            with Stage(r"copy", r"CR8_Sampler v16.0.30.31", prog_num=63521):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63522) as should_copy_source_592_63522:
                    should_copy_source_592_63522()
                    with Stage(r"copy source", r"Mac/Plugins/CR8 Sampler.bundle", prog_num=63523):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", r".", delete_extraneous_files=True, prog_num=63524) as copy_dir_to_dir_593_63524:
                            copy_dir_to_dir_593_63524()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/CR8 Sampler.bundle", where_to_unwtar=r".", prog_num=63525) as unwtar_594_63525:
                            unwtar_594_63525()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/CR8 Sampler.bundle", user_id=-1, group_id=-1, prog_num=63526, recursive=True) as chown_595_63526:
                            chown_595_63526()
            with Stage(r"copy", r"Curves AQ v16.0.23.24", prog_num=63527):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63528) as should_copy_source_596_63528:
                    should_copy_source_596_63528()
                    with Stage(r"copy source", r"Mac/Plugins/Curves AQ.bundle", prog_num=63529):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", r".", delete_extraneous_files=True, prog_num=63530) as copy_dir_to_dir_597_63530:
                            copy_dir_to_dir_597_63530()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves AQ.bundle", where_to_unwtar=r".", prog_num=63531) as unwtar_598_63531:
                            unwtar_598_63531()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Curves AQ.bundle", user_id=-1, group_id=-1, prog_num=63532, recursive=True) as chown_599_63532:
                            chown_599_63532()
            with Stage(r"copy", r"Curves Equator v16.0.23.24", prog_num=63533):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63534) as should_copy_source_600_63534:
                    should_copy_source_600_63534()
                    with Stage(r"copy source", r"Mac/Plugins/Curves Equator.bundle", prog_num=63535):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", r".", delete_extraneous_files=True, prog_num=63536) as copy_dir_to_dir_601_63536:
                            copy_dir_to_dir_601_63536()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Curves Equator.bundle", where_to_unwtar=r".", prog_num=63537) as unwtar_602_63537:
                            unwtar_602_63537()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Curves Equator.bundle", user_id=-1, group_id=-1, prog_num=63538, recursive=True) as chown_603_63538:
                            chown_603_63538()
            with Stage(r"copy", r"Center v16.0.23.24", prog_num=63539):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63540) as should_copy_source_604_63540:
                    should_copy_source_604_63540()
                    with Stage(r"copy source", r"Mac/Plugins/Center.bundle", prog_num=63541):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", r".", delete_extraneous_files=True, prog_num=63542) as copy_dir_to_dir_605_63542:
                            copy_dir_to_dir_605_63542()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Center.bundle", where_to_unwtar=r".", prog_num=63543) as unwtar_606_63543:
                            unwtar_606_63543()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Center.bundle", user_id=-1, group_id=-1, prog_num=63544, recursive=True) as chown_607_63544:
                            chown_607_63544()
            with Stage(r"copy", r"Clarity Vx DeReverb v16.0.23.24", prog_num=63545):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63546) as should_copy_source_608_63546:
                    should_copy_source_608_63546()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb.bundle", prog_num=63547):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", r".", delete_extraneous_files=True, prog_num=63548) as copy_dir_to_dir_609_63548:
                            copy_dir_to_dir_609_63548()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb.bundle", where_to_unwtar=r".", prog_num=63549) as unwtar_610_63549:
                            unwtar_610_63549()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb.bundle", user_id=-1, group_id=-1, prog_num=63550, recursive=True) as chown_611_63550:
                            chown_611_63550()
            with Stage(r"copy", r"Clarity Vx DeReverb Pro v16.0.23.24", prog_num=63551):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63552) as should_copy_source_612_63552:
                    should_copy_source_612_63552()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx DeReverb Pro.bundle", prog_num=63553):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", r".", delete_extraneous_files=True, prog_num=63554) as copy_dir_to_dir_613_63554:
                            copy_dir_to_dir_613_63554()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx DeReverb Pro.bundle", where_to_unwtar=r".", prog_num=63555) as unwtar_614_63555:
                            unwtar_614_63555()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx DeReverb Pro.bundle", user_id=-1, group_id=-1, prog_num=63556, recursive=True) as chown_615_63556:
                            chown_615_63556()
            with Stage(r"copy", r"Clarity Vx v16.0.23.24", prog_num=63557):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63558) as should_copy_source_616_63558:
                    should_copy_source_616_63558()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx.bundle", prog_num=63559):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", r".", delete_extraneous_files=True, prog_num=63560) as copy_dir_to_dir_617_63560:
                            copy_dir_to_dir_617_63560()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx.bundle", where_to_unwtar=r".", prog_num=63561) as unwtar_618_63561:
                            unwtar_618_63561()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx.bundle", user_id=-1, group_id=-1, prog_num=63562, recursive=True) as chown_619_63562:
                            chown_619_63562()
            with Stage(r"copy", r"Clarity Vx Pro v16.0.23.24", prog_num=63563):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63564) as should_copy_source_620_63564:
                    should_copy_source_620_63564()
                    with Stage(r"copy source", r"Mac/Plugins/Clarity Vx Pro.bundle", prog_num=63565):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", r".", delete_extraneous_files=True, prog_num=63566) as copy_dir_to_dir_621_63566:
                            copy_dir_to_dir_621_63566()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clarity Vx Pro.bundle", where_to_unwtar=r".", prog_num=63567) as unwtar_622_63567:
                            unwtar_622_63567()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clarity Vx Pro.bundle", user_id=-1, group_id=-1, prog_num=63568, recursive=True) as chown_623_63568:
                            chown_623_63568()
            with Stage(r"copy", r"Clavinet v16.0.23.24", prog_num=63569):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63570) as should_copy_source_624_63570:
                    should_copy_source_624_63570()
                    with Stage(r"copy source", r"Mac/Plugins/Clavinet.bundle", prog_num=63571):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", r".", delete_extraneous_files=True, prog_num=63572) as copy_dir_to_dir_625_63572:
                            copy_dir_to_dir_625_63572()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Clavinet.bundle", where_to_unwtar=r".", prog_num=63573) as unwtar_626_63573:
                            unwtar_626_63573()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Clavinet.bundle", user_id=-1, group_id=-1, prog_num=63574, recursive=True) as chown_627_63574:
                            chown_627_63574()
            with Stage(r"copy", r"Saphira v16.0.23.24", prog_num=63575):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63576) as should_copy_source_628_63576:
                    should_copy_source_628_63576()
                    with Stage(r"copy source", r"Mac/Plugins/Saphira.bundle", prog_num=63577):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", r".", delete_extraneous_files=True, prog_num=63578) as copy_dir_to_dir_629_63578:
                            copy_dir_to_dir_629_63578()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Saphira.bundle", where_to_unwtar=r".", prog_num=63579) as unwtar_630_63579:
                            unwtar_630_63579()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Saphira.bundle", user_id=-1, group_id=-1, prog_num=63580, recursive=True) as chown_631_63580:
                            chown_631_63580()
            with Stage(r"copy", r"Submarine v16.0.23.24", prog_num=63581):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63582) as should_copy_source_632_63582:
                    should_copy_source_632_63582()
                    with Stage(r"copy source", r"Mac/Plugins/Submarine.bundle", prog_num=63583):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", r".", delete_extraneous_files=True, prog_num=63584) as copy_dir_to_dir_633_63584:
                            copy_dir_to_dir_633_63584()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Submarine.bundle", where_to_unwtar=r".", prog_num=63585) as unwtar_634_63585:
                            unwtar_634_63585()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Submarine.bundle", user_id=-1, group_id=-1, prog_num=63586, recursive=True) as chown_635_63586:
                            chown_635_63586()
            with Stage(r"copy", r"DPR-402 v16.0.23.24", prog_num=63587):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63588) as should_copy_source_636_63588:
                    should_copy_source_636_63588()
                    with Stage(r"copy source", r"Mac/Plugins/DPR-402.bundle", prog_num=63589):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", r".", delete_extraneous_files=True, prog_num=63590) as copy_dir_to_dir_637_63590:
                            copy_dir_to_dir_637_63590()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DPR-402.bundle", where_to_unwtar=r".", prog_num=63591) as unwtar_638_63591:
                            unwtar_638_63591()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DPR-402.bundle", user_id=-1, group_id=-1, prog_num=63592, recursive=True) as chown_639_63592:
                            chown_639_63592()
            with Stage(r"copy", r"DeBreath v16.0.23.24", prog_num=63593):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63594) as should_copy_source_640_63594:
                    should_copy_source_640_63594()
                    with Stage(r"copy source", r"Mac/Plugins/DeBreath.bundle", prog_num=63595):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", r".", delete_extraneous_files=True, prog_num=63596) as copy_dir_to_dir_641_63596:
                            copy_dir_to_dir_641_63596()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeBreath.bundle", where_to_unwtar=r".", prog_num=63597) as unwtar_642_63597:
                            unwtar_642_63597()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeBreath.bundle", user_id=-1, group_id=-1, prog_num=63598, recursive=True) as chown_643_63598:
                            chown_643_63598()
            with Stage(r"copy", r"DeEsser v16.0.23.24", prog_num=63599):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63600) as should_copy_source_644_63600:
                    should_copy_source_644_63600()
                    with Stage(r"copy source", r"Mac/Plugins/DeEsser.bundle", prog_num=63601):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", r".", delete_extraneous_files=True, prog_num=63602) as copy_dir_to_dir_645_63602:
                            copy_dir_to_dir_645_63602()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/DeEsser.bundle", where_to_unwtar=r".", prog_num=63603) as unwtar_646_63603:
                            unwtar_646_63603()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/DeEsser.bundle", user_id=-1, group_id=-1, prog_num=63604, recursive=True) as chown_647_63604:
                            chown_647_63604()
            with Stage(r"copy", r"Doppler v16.0.23.24", prog_num=63605):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63606) as should_copy_source_648_63606:
                    should_copy_source_648_63606()
                    with Stage(r"copy source", r"Mac/Plugins/Doppler.bundle", prog_num=63607):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", r".", delete_extraneous_files=True, prog_num=63608) as copy_dir_to_dir_649_63608:
                            copy_dir_to_dir_649_63608()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doppler.bundle", where_to_unwtar=r".", prog_num=63609) as unwtar_650_63609:
                            unwtar_650_63609()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doppler.bundle", user_id=-1, group_id=-1, prog_num=63610, recursive=True) as chown_651_63610:
                            chown_651_63610()
            with Stage(r"copy", r"Dorrough v16.0.23.24", prog_num=63611):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63612) as should_copy_source_652_63612:
                    should_copy_source_652_63612()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough.bundle", prog_num=63613):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", r".", delete_extraneous_files=True, prog_num=63614) as copy_dir_to_dir_653_63614:
                            copy_dir_to_dir_653_63614()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough.bundle", where_to_unwtar=r".", prog_num=63615) as unwtar_654_63615:
                            unwtar_654_63615()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough.bundle", user_id=-1, group_id=-1, prog_num=63616, recursive=True) as chown_655_63616:
                            chown_655_63616()
            with Stage(r"copy", r"Dorrough Surround 5.0 v16.0.23.24", prog_num=63617):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63618) as should_copy_source_656_63618:
                    should_copy_source_656_63618()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough Surround 5.0.bundle", prog_num=63619):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", r".", delete_extraneous_files=True, prog_num=63620) as copy_dir_to_dir_657_63620:
                            copy_dir_to_dir_657_63620()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.0.bundle", where_to_unwtar=r".", prog_num=63621) as unwtar_658_63621:
                            unwtar_658_63621()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough Surround 5.0.bundle", user_id=-1, group_id=-1, prog_num=63622, recursive=True) as chown_659_63622:
                            chown_659_63622()
            with Stage(r"copy", r"Dorrough Surround 5.1 v16.0.23.24", prog_num=63623):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63624) as should_copy_source_660_63624:
                    should_copy_source_660_63624()
                    with Stage(r"copy source", r"Mac/Plugins/Dorrough Surround 5.1.bundle", prog_num=63625):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", r".", delete_extraneous_files=True, prog_num=63626) as copy_dir_to_dir_661_63626:
                            copy_dir_to_dir_661_63626()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Dorrough Surround 5.1.bundle", where_to_unwtar=r".", prog_num=63627) as unwtar_662_63627:
                            unwtar_662_63627()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Dorrough Surround 5.1.bundle", user_id=-1, group_id=-1, prog_num=63628, recursive=True) as chown_663_63628:
                            chown_663_63628()
            with Stage(r"copy", r"Doubler v16.0.23.24", prog_num=63629):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63630) as should_copy_source_664_63630:
                    should_copy_source_664_63630()
                    with Stage(r"copy source", r"Mac/Plugins/Doubler.bundle", prog_num=63631):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", r".", delete_extraneous_files=True, prog_num=63632) as copy_dir_to_dir_665_63632:
                            copy_dir_to_dir_665_63632()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Doubler.bundle", where_to_unwtar=r".", prog_num=63633) as unwtar_666_63633:
                            unwtar_666_63633()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Doubler.bundle", user_id=-1, group_id=-1, prog_num=63634, recursive=True) as chown_667_63634:
                            chown_667_63634()
            with Stage(r"copy", r"EMO-D5 v16.0.23.24", prog_num=63635):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63636) as should_copy_source_668_63636:
                    should_copy_source_668_63636()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-D5.bundle", prog_num=63637):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", r".", delete_extraneous_files=True, prog_num=63638) as copy_dir_to_dir_669_63638:
                            copy_dir_to_dir_669_63638()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-D5.bundle", where_to_unwtar=r".", prog_num=63639) as unwtar_670_63639:
                            unwtar_670_63639()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-D5.bundle", user_id=-1, group_id=-1, prog_num=63640, recursive=True) as chown_671_63640:
                            chown_671_63640()
            with Stage(r"copy", r"EMO-F2 v16.0.23.24", prog_num=63641):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63642) as should_copy_source_672_63642:
                    should_copy_source_672_63642()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-F2.bundle", prog_num=63643):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", r".", delete_extraneous_files=True, prog_num=63644) as copy_dir_to_dir_673_63644:
                            copy_dir_to_dir_673_63644()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-F2.bundle", where_to_unwtar=r".", prog_num=63645) as unwtar_674_63645:
                            unwtar_674_63645()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-F2.bundle", user_id=-1, group_id=-1, prog_num=63646, recursive=True) as chown_675_63646:
                            chown_675_63646()
            with Stage(r"copy", r"EMO-Q4 v16.0.23.24", prog_num=63647):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63648) as should_copy_source_676_63648:
                    should_copy_source_676_63648()
                    with Stage(r"copy source", r"Mac/Plugins/EMO-Q4.bundle", prog_num=63649):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", r".", delete_extraneous_files=True, prog_num=63650) as copy_dir_to_dir_677_63650:
                            copy_dir_to_dir_677_63650()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EMO-Q4.bundle", where_to_unwtar=r".", prog_num=63651) as unwtar_678_63651:
                            unwtar_678_63651()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EMO-Q4.bundle", user_id=-1, group_id=-1, prog_num=63652, recursive=True) as chown_679_63652:
                            chown_679_63652()
            with Stage(r"copy", r"EddieKramer BA v16.0.23.24", prog_num=63653):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63654) as should_copy_source_680_63654:
                    should_copy_source_680_63654()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer BA.bundle", prog_num=63655):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", r".", delete_extraneous_files=True, prog_num=63656) as copy_dir_to_dir_681_63656:
                            copy_dir_to_dir_681_63656()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer BA.bundle", where_to_unwtar=r".", prog_num=63657) as unwtar_682_63657:
                            unwtar_682_63657()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer BA.bundle", user_id=-1, group_id=-1, prog_num=63658, recursive=True) as chown_683_63658:
                            chown_683_63658()
            with Stage(r"copy", r"EddieKramer DR v16.0.23.24", prog_num=63659):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63660) as should_copy_source_684_63660:
                    should_copy_source_684_63660()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer DR.bundle", prog_num=63661):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", r".", delete_extraneous_files=True, prog_num=63662) as copy_dir_to_dir_685_63662:
                            copy_dir_to_dir_685_63662()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer DR.bundle", where_to_unwtar=r".", prog_num=63663) as unwtar_686_63663:
                            unwtar_686_63663()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer DR.bundle", user_id=-1, group_id=-1, prog_num=63664, recursive=True) as chown_687_63664:
                            chown_687_63664()
            with Stage(r"copy", r"EddieKramer FX v16.0.23.24", prog_num=63665):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63666) as should_copy_source_688_63666:
                    should_copy_source_688_63666()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer FX.bundle", prog_num=63667):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", r".", delete_extraneous_files=True, prog_num=63668) as copy_dir_to_dir_689_63668:
                            copy_dir_to_dir_689_63668()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer FX.bundle", where_to_unwtar=r".", prog_num=63669) as unwtar_690_63669:
                            unwtar_690_63669()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer FX.bundle", user_id=-1, group_id=-1, prog_num=63670, recursive=True) as chown_691_63670:
                            chown_691_63670()
            with Stage(r"copy", r"EddieKramer GT v16.0.23.24", prog_num=63671):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63672) as should_copy_source_692_63672:
                    should_copy_source_692_63672()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer GT.bundle", prog_num=63673):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", r".", delete_extraneous_files=True, prog_num=63674) as copy_dir_to_dir_693_63674:
                            copy_dir_to_dir_693_63674()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer GT.bundle", where_to_unwtar=r".", prog_num=63675) as unwtar_694_63675:
                            unwtar_694_63675()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer GT.bundle", user_id=-1, group_id=-1, prog_num=63676, recursive=True) as chown_695_63676:
                            chown_695_63676()
            with Stage(r"copy", r"EddieKramer VC v16.0.23.24", prog_num=63677):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63678) as should_copy_source_696_63678:
                    should_copy_source_696_63678()
                    with Stage(r"copy source", r"Mac/Plugins/EddieKramer VC.bundle", prog_num=63679):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", r".", delete_extraneous_files=True, prog_num=63680) as copy_dir_to_dir_697_63680:
                            copy_dir_to_dir_697_63680()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/EddieKramer VC.bundle", where_to_unwtar=r".", prog_num=63681) as unwtar_698_63681:
                            unwtar_698_63681()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/EddieKramer VC.bundle", user_id=-1, group_id=-1, prog_num=63682, recursive=True) as chown_699_63682:
                            chown_699_63682()
            with Stage(r"copy", r"Electric 200 v16.0.23.24", prog_num=63683):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63684) as should_copy_source_700_63684:
                    should_copy_source_700_63684()
                    with Stage(r"copy source", r"Mac/Plugins/Electric200.bundle", prog_num=63685):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", r".", delete_extraneous_files=True, prog_num=63686) as copy_dir_to_dir_701_63686:
                            copy_dir_to_dir_701_63686()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric200.bundle", where_to_unwtar=r".", prog_num=63687) as unwtar_702_63687:
                            unwtar_702_63687()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric200.bundle", user_id=-1, group_id=-1, prog_num=63688, recursive=True) as chown_703_63688:
                            chown_703_63688()
            with Stage(r"copy", r"Electric 88 v16.0.23.24", prog_num=63689):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63690) as should_copy_source_704_63690:
                    should_copy_source_704_63690()
                    with Stage(r"copy source", r"Mac/Plugins/Electric88.bundle", prog_num=63691):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", r".", delete_extraneous_files=True, prog_num=63692) as copy_dir_to_dir_705_63692:
                            copy_dir_to_dir_705_63692()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric88.bundle", where_to_unwtar=r".", prog_num=63693) as unwtar_706_63693:
                            unwtar_706_63693()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric88.bundle", user_id=-1, group_id=-1, prog_num=63694, recursive=True) as chown_707_63694:
                            chown_707_63694()
            with Stage(r"copy", r"Electric Grand 80 v16.0.23.24", prog_num=63695):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63696) as should_copy_source_708_63696:
                    should_copy_source_708_63696()
                    with Stage(r"copy source", r"Mac/Plugins/Electric Grand 80.bundle", prog_num=63697):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", r".", delete_extraneous_files=True, prog_num=63698) as copy_dir_to_dir_709_63698:
                            copy_dir_to_dir_709_63698()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Electric Grand 80.bundle", where_to_unwtar=r".", prog_num=63699) as unwtar_710_63699:
                            unwtar_710_63699()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Electric Grand 80.bundle", user_id=-1, group_id=-1, prog_num=63700, recursive=True) as chown_711_63700:
                            chown_711_63700()
            with Stage(r"copy", r"Element2 v16.0.23.24", prog_num=63701):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63702) as should_copy_source_712_63702:
                    should_copy_source_712_63702()
                    with Stage(r"copy source", r"Mac/Plugins/Element2.bundle", prog_num=63703):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", r".", delete_extraneous_files=True, prog_num=63704) as copy_dir_to_dir_713_63704:
                            copy_dir_to_dir_713_63704()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Element2.bundle", where_to_unwtar=r".", prog_num=63705) as unwtar_714_63705:
                            unwtar_714_63705()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Element2.bundle", user_id=-1, group_id=-1, prog_num=63706, recursive=True) as chown_715_63706:
                            chown_715_63706()
            with Stage(r"copy", r"Enigma v16.0.23.24", prog_num=63707):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63708) as should_copy_source_716_63708:
                    should_copy_source_716_63708()
                    with Stage(r"copy source", r"Mac/Plugins/Enigma.bundle", prog_num=63709):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", r".", delete_extraneous_files=True, prog_num=63710) as copy_dir_to_dir_717_63710:
                            copy_dir_to_dir_717_63710()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Enigma.bundle", where_to_unwtar=r".", prog_num=63711) as unwtar_718_63711:
                            unwtar_718_63711()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Enigma.bundle", user_id=-1, group_id=-1, prog_num=63712, recursive=True) as chown_719_63712:
                            chown_719_63712()
            with Stage(r"copy", r"F6 v16.0.23.24", prog_num=63713):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63714) as should_copy_source_720_63714:
                    should_copy_source_720_63714()
                    with Stage(r"copy source", r"Mac/Plugins/F6.bundle", prog_num=63715):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", r".", delete_extraneous_files=True, prog_num=63716) as copy_dir_to_dir_721_63716:
                            copy_dir_to_dir_721_63716()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/F6.bundle", where_to_unwtar=r".", prog_num=63717) as unwtar_722_63717:
                            unwtar_722_63717()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/F6.bundle", user_id=-1, group_id=-1, prog_num=63718, recursive=True) as chown_723_63718:
                            chown_723_63718()
            with Stage(r"copy", r"Feedback Hunter v16.0.23.24", prog_num=63719):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63720) as should_copy_source_724_63720:
                    should_copy_source_724_63720()
                    with Stage(r"copy source", r"Mac/Plugins/Feedback Hunter.bundle", prog_num=63721):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", r".", delete_extraneous_files=True, prog_num=63722) as copy_dir_to_dir_725_63722:
                            copy_dir_to_dir_725_63722()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Feedback Hunter.bundle", where_to_unwtar=r".", prog_num=63723) as unwtar_726_63723:
                            unwtar_726_63723()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Feedback Hunter.bundle", user_id=-1, group_id=-1, prog_num=63724, recursive=True) as chown_727_63724:
                            chown_727_63724()
            with Stage(r"copy", r"Flow Motion v16.0.23.24", prog_num=63725):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63726) as should_copy_source_728_63726:
                    should_copy_source_728_63726()
                    with Stage(r"copy source", r"Mac/Plugins/Flow Motion.bundle", prog_num=63727):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", r".", delete_extraneous_files=True, prog_num=63728) as copy_dir_to_dir_729_63728:
                            copy_dir_to_dir_729_63728()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Flow Motion.bundle", where_to_unwtar=r".", prog_num=63729) as unwtar_730_63729:
                            unwtar_730_63729()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Flow Motion.bundle", user_id=-1, group_id=-1, prog_num=63730, recursive=True) as chown_731_63730:
                            chown_731_63730()
            with Stage(r"copy", r"GEQ v16.0.23.24", prog_num=63731):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63732) as should_copy_source_732_63732:
                    should_copy_source_732_63732()
                    with Stage(r"copy source", r"Mac/Plugins/GEQ.bundle", prog_num=63733):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", r".", delete_extraneous_files=True, prog_num=63734) as copy_dir_to_dir_733_63734:
                            copy_dir_to_dir_733_63734()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GEQ.bundle", where_to_unwtar=r".", prog_num=63735) as unwtar_734_63735:
                            unwtar_734_63735()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GEQ.bundle", user_id=-1, group_id=-1, prog_num=63736, recursive=True) as chown_735_63736:
                            chown_735_63736()
            with Stage(r"copy", r"GTRAmp v16.0.23.24", prog_num=63737):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63738) as should_copy_source_736_63738:
                    should_copy_source_736_63738()
                    with Stage(r"copy source", r"Mac/Plugins/GTRAmp.bundle", prog_num=63739):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", r".", delete_extraneous_files=True, prog_num=63740) as copy_dir_to_dir_737_63740:
                            copy_dir_to_dir_737_63740()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRAmp.bundle", where_to_unwtar=r".", prog_num=63741) as unwtar_738_63741:
                            unwtar_738_63741()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRAmp.bundle", user_id=-1, group_id=-1, prog_num=63742, recursive=True) as chown_739_63742:
                            chown_739_63742()
            with Stage(r"copy", r"GTR Solo ToolRack v16.0.23.24", prog_num=63743):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63744) as should_copy_source_740_63744:
                    should_copy_source_740_63744()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSoloToolRack.bundle", prog_num=63745):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", r".", delete_extraneous_files=True, prog_num=63746) as copy_dir_to_dir_741_63746:
                            copy_dir_to_dir_741_63746()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSoloToolRack.bundle", where_to_unwtar=r".", prog_num=63747) as unwtar_742_63747:
                            unwtar_742_63747()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSoloToolRack.bundle", user_id=-1, group_id=-1, prog_num=63748, recursive=True) as chown_743_63748:
                            chown_743_63748()
            with Stage(r"copy", r"GTRStomp v16.0.23.24", prog_num=63749):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63750) as should_copy_source_744_63750:
                    should_copy_source_744_63750()
                    with Stage(r"copy source", r"Mac/Plugins/GTRStomp.bundle", prog_num=63751):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", r".", delete_extraneous_files=True, prog_num=63752) as copy_dir_to_dir_745_63752:
                            copy_dir_to_dir_745_63752()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRStomp.bundle", where_to_unwtar=r".", prog_num=63753) as unwtar_746_63753:
                            unwtar_746_63753()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRStomp.bundle", user_id=-1, group_id=-1, prog_num=63754, recursive=True) as chown_747_63754:
                            chown_747_63754()
            with Stage(r"copy", r"GTRToolRack v16.0.23.24", prog_num=63755):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63756) as should_copy_source_748_63756:
                    should_copy_source_748_63756()
                    with Stage(r"copy source", r"Mac/Plugins/GTRToolRack.bundle", prog_num=63757):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", r".", delete_extraneous_files=True, prog_num=63758) as copy_dir_to_dir_749_63758:
                            copy_dir_to_dir_749_63758()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRToolRack.bundle", where_to_unwtar=r".", prog_num=63759) as unwtar_750_63759:
                            unwtar_750_63759()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRToolRack.bundle", user_id=-1, group_id=-1, prog_num=63760, recursive=True) as chown_751_63760:
                            chown_751_63760()
            with Stage(r"copy", r"GTRTuner v16.0.23.24", prog_num=63761):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63762) as should_copy_source_752_63762:
                    should_copy_source_752_63762()
                    with Stage(r"copy source", r"Mac/Plugins/GTRTuner.bundle", prog_num=63763):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", r".", delete_extraneous_files=True, prog_num=63764) as copy_dir_to_dir_753_63764:
                            copy_dir_to_dir_753_63764()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRTuner.bundle", where_to_unwtar=r".", prog_num=63765) as unwtar_754_63765:
                            unwtar_754_63765()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRTuner.bundle", user_id=-1, group_id=-1, prog_num=63766, recursive=True) as chown_755_63766:
                            chown_755_63766()
            with Stage(r"copy", r"Waves Gemstones v16.0.23.24", prog_num=63767):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63768) as should_copy_source_756_63768:
                    should_copy_source_756_63768()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Gemstones.bundle", prog_num=63769):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", r".", delete_extraneous_files=True, prog_num=63770) as copy_dir_to_dir_757_63770:
                            copy_dir_to_dir_757_63770()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Gemstones.bundle", where_to_unwtar=r".", prog_num=63771) as unwtar_758_63771:
                            unwtar_758_63771()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Gemstones.bundle", user_id=-1, group_id=-1, prog_num=63772, recursive=True) as chown_759_63772:
                            chown_759_63772()
            with Stage(r"copy", r"Grand Rhapsody v16.0.23.24", prog_num=63773):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63774) as should_copy_source_760_63774:
                    should_copy_source_760_63774()
                    with Stage(r"copy source", r"Mac/Plugins/GrandRhapsody.bundle", prog_num=63775):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", r".", delete_extraneous_files=True, prog_num=63776) as copy_dir_to_dir_761_63776:
                            copy_dir_to_dir_761_63776()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GrandRhapsody.bundle", where_to_unwtar=r".", prog_num=63777) as unwtar_762_63777:
                            unwtar_762_63777()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GrandRhapsody.bundle", user_id=-1, group_id=-1, prog_num=63778, recursive=True) as chown_763_63778:
                            chown_763_63778()
            with Stage(r"copy", r"Greg Wells MixCentric v16.0.23.24", prog_num=63779):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63780) as should_copy_source_764_63780:
                    should_copy_source_764_63780()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells MixCentric.bundle", prog_num=63781):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", r".", delete_extraneous_files=True, prog_num=63782) as copy_dir_to_dir_765_63782:
                            copy_dir_to_dir_765_63782()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells MixCentric.bundle", where_to_unwtar=r".", prog_num=63783) as unwtar_766_63783:
                            unwtar_766_63783()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells MixCentric.bundle", user_id=-1, group_id=-1, prog_num=63784, recursive=True) as chown_767_63784:
                            chown_767_63784()
            with Stage(r"copy", r"Greg Wells PianoCentric v16.0.23.24", prog_num=63785):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63786) as should_copy_source_768_63786:
                    should_copy_source_768_63786()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells PianoCentric.bundle", prog_num=63787):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", r".", delete_extraneous_files=True, prog_num=63788) as copy_dir_to_dir_769_63788:
                            copy_dir_to_dir_769_63788()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells PianoCentric.bundle", where_to_unwtar=r".", prog_num=63789) as unwtar_770_63789:
                            unwtar_770_63789()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells PianoCentric.bundle", user_id=-1, group_id=-1, prog_num=63790, recursive=True) as chown_771_63790:
                            chown_771_63790()
            with Stage(r"copy", r"Greg Wells ToneCentric v16.0.23.24", prog_num=63791):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63792) as should_copy_source_772_63792:
                    should_copy_source_772_63792()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells ToneCentric.bundle", prog_num=63793):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", r".", delete_extraneous_files=True, prog_num=63794) as copy_dir_to_dir_773_63794:
                            copy_dir_to_dir_773_63794()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells ToneCentric.bundle", where_to_unwtar=r".", prog_num=63795) as unwtar_774_63795:
                            unwtar_774_63795()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells ToneCentric.bundle", user_id=-1, group_id=-1, prog_num=63796, recursive=True) as chown_775_63796:
                            chown_775_63796()
            with Stage(r"copy", r"Greg Wells VoiceCentric v16.0.23.24", prog_num=63797):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63798) as should_copy_source_776_63798:
                    should_copy_source_776_63798()
                    with Stage(r"copy source", r"Mac/Plugins/Greg Wells VoiceCentric.bundle", prog_num=63799):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", r".", delete_extraneous_files=True, prog_num=63800) as copy_dir_to_dir_777_63800:
                            copy_dir_to_dir_777_63800()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Greg Wells VoiceCentric.bundle", where_to_unwtar=r".", prog_num=63801) as unwtar_778_63801:
                            unwtar_778_63801()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Greg Wells VoiceCentric.bundle", user_id=-1, group_id=-1, prog_num=63802, recursive=True) as chown_779_63802:
                            chown_779_63802()
            with Stage(r"copy", r"H-Comp v16.0.23.24", prog_num=63803):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63804) as should_copy_source_780_63804:
                    should_copy_source_780_63804()
                    with Stage(r"copy source", r"Mac/Plugins/H-Comp.bundle", prog_num=63805):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", r".", delete_extraneous_files=True, prog_num=63806) as copy_dir_to_dir_781_63806:
                            copy_dir_to_dir_781_63806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Comp.bundle", where_to_unwtar=r".", prog_num=63807) as unwtar_782_63807:
                            unwtar_782_63807()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Comp.bundle", user_id=-1, group_id=-1, prog_num=63808, recursive=True) as chown_783_63808:
                            chown_783_63808()
            with Stage(r"copy", r"H-Delay v16.0.23.24", prog_num=63809):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63810) as should_copy_source_784_63810:
                    should_copy_source_784_63810()
                    with Stage(r"copy source", r"Mac/Plugins/H-Delay.bundle", prog_num=63811):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", r".", delete_extraneous_files=True, prog_num=63812) as copy_dir_to_dir_785_63812:
                            copy_dir_to_dir_785_63812()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Delay.bundle", where_to_unwtar=r".", prog_num=63813) as unwtar_786_63813:
                            unwtar_786_63813()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Delay.bundle", user_id=-1, group_id=-1, prog_num=63814, recursive=True) as chown_787_63814:
                            chown_787_63814()
            with Stage(r"copy", r"H-EQ v16.0.23.24", prog_num=63815):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63816) as should_copy_source_788_63816:
                    should_copy_source_788_63816()
                    with Stage(r"copy source", r"Mac/Plugins/H-EQ.bundle", prog_num=63817):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", r".", delete_extraneous_files=True, prog_num=63818) as copy_dir_to_dir_789_63818:
                            copy_dir_to_dir_789_63818()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-EQ.bundle", where_to_unwtar=r".", prog_num=63819) as unwtar_790_63819:
                            unwtar_790_63819()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-EQ.bundle", user_id=-1, group_id=-1, prog_num=63820, recursive=True) as chown_791_63820:
                            chown_791_63820()
            with Stage(r"copy", r"H-Reverb v16.0.23.24", prog_num=63821):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63822) as should_copy_source_792_63822:
                    should_copy_source_792_63822()
                    with Stage(r"copy source", r"Mac/Plugins/H-Reverb.bundle", prog_num=63823):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=63824) as copy_dir_to_dir_793_63824:
                            copy_dir_to_dir_793_63824()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/H-Reverb.bundle", where_to_unwtar=r".", prog_num=63825) as unwtar_794_63825:
                            unwtar_794_63825()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/H-Reverb.bundle", user_id=-1, group_id=-1, prog_num=63826, recursive=True) as chown_795_63826:
                            chown_795_63826()
            with Stage(r"copy", r"IDX Intelligent Dynamics v16.0.23.24", prog_num=63827):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63828) as should_copy_source_796_63828:
                    should_copy_source_796_63828()
                    with Stage(r"copy source", r"Mac/Plugins/IDX Intelligent Dynamics.bundle", prog_num=63829):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", r".", delete_extraneous_files=True, prog_num=63830) as copy_dir_to_dir_797_63830:
                            copy_dir_to_dir_797_63830()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IDX Intelligent Dynamics.bundle", where_to_unwtar=r".", prog_num=63831) as unwtar_798_63831:
                            unwtar_798_63831()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IDX Intelligent Dynamics.bundle", user_id=-1, group_id=-1, prog_num=63832, recursive=True) as chown_799_63832:
                            chown_799_63832()
            with Stage(r"copy", r"IMPusher v16.0.23.24", prog_num=63833):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63834) as should_copy_source_800_63834:
                    should_copy_source_800_63834()
                    with Stage(r"copy source", r"Mac/Plugins/IMPusher.bundle", prog_num=63835):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", r".", delete_extraneous_files=True, prog_num=63836) as copy_dir_to_dir_801_63836:
                            copy_dir_to_dir_801_63836()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IMPusher.bundle", where_to_unwtar=r".", prog_num=63837) as unwtar_802_63837:
                            unwtar_802_63837()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IMPusher.bundle", user_id=-1, group_id=-1, prog_num=63838, recursive=True) as chown_803_63838:
                            chown_803_63838()
            with Stage(r"copy", r"IR-1 v16.0.23.24", prog_num=63839):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63840) as should_copy_source_804_63840:
                    should_copy_source_804_63840()
                    with Stage(r"copy source", r"Mac/Plugins/IR-1.bundle", prog_num=63841):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", r".", delete_extraneous_files=True, prog_num=63842) as copy_dir_to_dir_805_63842:
                            copy_dir_to_dir_805_63842()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-1.bundle", where_to_unwtar=r".", prog_num=63843) as unwtar_806_63843:
                            unwtar_806_63843()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-1.bundle", user_id=-1, group_id=-1, prog_num=63844, recursive=True) as chown_807_63844:
                            chown_807_63844()
            with Stage(r"copy", r"IR-360 v16.0.23.24", prog_num=63845):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63846) as should_copy_source_808_63846:
                    should_copy_source_808_63846()
                    with Stage(r"copy source", r"Mac/Plugins/IR-360.bundle", prog_num=63847):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", r".", delete_extraneous_files=True, prog_num=63848) as copy_dir_to_dir_809_63848:
                            copy_dir_to_dir_809_63848()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-360.bundle", where_to_unwtar=r".", prog_num=63849) as unwtar_810_63849:
                            unwtar_810_63849()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-360.bundle", user_id=-1, group_id=-1, prog_num=63850, recursive=True) as chown_811_63850:
                            chown_811_63850()
            with Stage(r"copy", r"IR-L v16.0.23.24", prog_num=63851):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63852) as should_copy_source_812_63852:
                    should_copy_source_812_63852()
                    with Stage(r"copy source", r"Mac/Plugins/IR-L.bundle", prog_num=63853):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", r".", delete_extraneous_files=True, prog_num=63854) as copy_dir_to_dir_813_63854:
                            copy_dir_to_dir_813_63854()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IR-L.bundle", where_to_unwtar=r".", prog_num=63855) as unwtar_814_63855:
                            unwtar_814_63855()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IR-L.bundle", user_id=-1, group_id=-1, prog_num=63856, recursive=True) as chown_815_63856:
                            chown_815_63856()
            with Stage(r"copy", r"IRLive v16.0.23.24", prog_num=63857):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63858) as should_copy_source_816_63858:
                    should_copy_source_816_63858()
                    with Stage(r"copy source", r"Mac/Plugins/IRLive.bundle", prog_num=63859):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", r".", delete_extraneous_files=True, prog_num=63860) as copy_dir_to_dir_817_63860:
                            copy_dir_to_dir_817_63860()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/IRLive.bundle", where_to_unwtar=r".", prog_num=63861) as unwtar_818_63861:
                            unwtar_818_63861()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/IRLive.bundle", user_id=-1, group_id=-1, prog_num=63862, recursive=True) as chown_819_63862:
                            chown_819_63862()
            with Stage(r"copy", r"Immersive Wrapper v16.0.23.24", prog_num=63863):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63864) as should_copy_source_820_63864:
                    should_copy_source_820_63864()
                    with Stage(r"copy source", r"Mac/Plugins/Immersive Wrapper.bundle", prog_num=63865):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", r".", delete_extraneous_files=True, prog_num=63866) as copy_dir_to_dir_821_63866:
                            copy_dir_to_dir_821_63866()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Immersive Wrapper.bundle", where_to_unwtar=r".", prog_num=63867) as unwtar_822_63867:
                            unwtar_822_63867()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Immersive Wrapper.bundle", user_id=-1, group_id=-1, prog_num=63868, recursive=True) as chown_823_63868:
                            chown_823_63868()
            with Stage(r"copy", r"InPhase v16.0.23.24", prog_num=63869):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63870) as should_copy_source_824_63870:
                    should_copy_source_824_63870()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase.bundle", prog_num=63871):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", r".", delete_extraneous_files=True, prog_num=63872) as copy_dir_to_dir_825_63872:
                            copy_dir_to_dir_825_63872()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase.bundle", where_to_unwtar=r".", prog_num=63873) as unwtar_826_63873:
                            unwtar_826_63873()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase.bundle", user_id=-1, group_id=-1, prog_num=63874, recursive=True) as chown_827_63874:
                            chown_827_63874()
            with Stage(r"copy", r"InPhase LT v16.0.23.24", prog_num=63875):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63876) as should_copy_source_828_63876:
                    should_copy_source_828_63876()
                    with Stage(r"copy source", r"Mac/Plugins/InPhase LT.bundle", prog_num=63877):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", r".", delete_extraneous_files=True, prog_num=63878) as copy_dir_to_dir_829_63878:
                            copy_dir_to_dir_829_63878()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/InPhase LT.bundle", where_to_unwtar=r".", prog_num=63879) as unwtar_830_63879:
                            unwtar_830_63879()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/InPhase LT.bundle", user_id=-1, group_id=-1, prog_num=63880, recursive=True) as chown_831_63880:
                            chown_831_63880()
            with Stage(r"copy", r"J37 v16.0.23.24", prog_num=63881):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63882) as should_copy_source_832_63882:
                    should_copy_source_832_63882()
                    with Stage(r"copy source", r"Mac/Plugins/J37.bundle", prog_num=63883):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", r".", delete_extraneous_files=True, prog_num=63884) as copy_dir_to_dir_833_63884:
                            copy_dir_to_dir_833_63884()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/J37.bundle", where_to_unwtar=r".", prog_num=63885) as unwtar_834_63885:
                            unwtar_834_63885()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/J37.bundle", user_id=-1, group_id=-1, prog_num=63886, recursive=True) as chown_835_63886:
                            chown_835_63886()
            with Stage(r"copy", r"JJP-Bass v16.0.23.24", prog_num=63887):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63888) as should_copy_source_836_63888:
                    should_copy_source_836_63888()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Bass.bundle", prog_num=63889):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", r".", delete_extraneous_files=True, prog_num=63890) as copy_dir_to_dir_837_63890:
                            copy_dir_to_dir_837_63890()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Bass.bundle", where_to_unwtar=r".", prog_num=63891) as unwtar_838_63891:
                            unwtar_838_63891()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Bass.bundle", user_id=-1, group_id=-1, prog_num=63892, recursive=True) as chown_839_63892:
                            chown_839_63892()
            with Stage(r"copy", r"JJP-Cymb-Perc v16.0.23.24", prog_num=63893):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63894) as should_copy_source_840_63894:
                    should_copy_source_840_63894()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Cymb-Perc.bundle", prog_num=63895):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", r".", delete_extraneous_files=True, prog_num=63896) as copy_dir_to_dir_841_63896:
                            copy_dir_to_dir_841_63896()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Cymb-Perc.bundle", where_to_unwtar=r".", prog_num=63897) as unwtar_842_63897:
                            unwtar_842_63897()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Cymb-Perc.bundle", user_id=-1, group_id=-1, prog_num=63898, recursive=True) as chown_843_63898:
                            chown_843_63898()
            with Stage(r"copy", r"JJP-Drums v16.0.23.24", prog_num=63899):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63900) as should_copy_source_844_63900:
                    should_copy_source_844_63900()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Drums.bundle", prog_num=63901):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", r".", delete_extraneous_files=True, prog_num=63902) as copy_dir_to_dir_845_63902:
                            copy_dir_to_dir_845_63902()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Drums.bundle", where_to_unwtar=r".", prog_num=63903) as unwtar_846_63903:
                            unwtar_846_63903()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Drums.bundle", user_id=-1, group_id=-1, prog_num=63904, recursive=True) as chown_847_63904:
                            chown_847_63904()
            with Stage(r"copy", r"JJP-Guitars v16.0.23.24", prog_num=63905):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63906) as should_copy_source_848_63906:
                    should_copy_source_848_63906()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Guitars.bundle", prog_num=63907):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", r".", delete_extraneous_files=True, prog_num=63908) as copy_dir_to_dir_849_63908:
                            copy_dir_to_dir_849_63908()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Guitars.bundle", where_to_unwtar=r".", prog_num=63909) as unwtar_850_63909:
                            unwtar_850_63909()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Guitars.bundle", user_id=-1, group_id=-1, prog_num=63910, recursive=True) as chown_851_63910:
                            chown_851_63910()
            with Stage(r"copy", r"JJP-Strings-Keys v16.0.23.24", prog_num=63911):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63912) as should_copy_source_852_63912:
                    should_copy_source_852_63912()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Strings-Keys.bundle", prog_num=63913):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", r".", delete_extraneous_files=True, prog_num=63914) as copy_dir_to_dir_853_63914:
                            copy_dir_to_dir_853_63914()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Strings-Keys.bundle", where_to_unwtar=r".", prog_num=63915) as unwtar_854_63915:
                            unwtar_854_63915()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Strings-Keys.bundle", user_id=-1, group_id=-1, prog_num=63916, recursive=True) as chown_855_63916:
                            chown_855_63916()
            with Stage(r"copy", r"JJP-Vocals v16.0.23.24", prog_num=63917):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63918) as should_copy_source_856_63918:
                    should_copy_source_856_63918()
                    with Stage(r"copy source", r"Mac/Plugins/JJP-Vocals.bundle", prog_num=63919):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", r".", delete_extraneous_files=True, prog_num=63920) as copy_dir_to_dir_857_63920:
                            copy_dir_to_dir_857_63920()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/JJP-Vocals.bundle", where_to_unwtar=r".", prog_num=63921) as unwtar_858_63921:
                            unwtar_858_63921()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/JJP-Vocals.bundle", user_id=-1, group_id=-1, prog_num=63922, recursive=True) as chown_859_63922:
                            chown_859_63922()
            with Stage(r"copy", r"Kaleidoscopes v16.0.23.24", prog_num=63923):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63924) as should_copy_source_860_63924:
                    should_copy_source_860_63924()
                    with Stage(r"copy source", r"Mac/Plugins/Kaleidoscopes.bundle", prog_num=63925):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", r".", delete_extraneous_files=True, prog_num=63926) as copy_dir_to_dir_861_63926:
                            copy_dir_to_dir_861_63926()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Kaleidoscopes.bundle", where_to_unwtar=r".", prog_num=63927) as unwtar_862_63927:
                            unwtar_862_63927()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Kaleidoscopes.bundle", user_id=-1, group_id=-1, prog_num=63928, recursive=True) as chown_863_63928:
                            chown_863_63928()
            with Stage(r"copy", r"Key Detector v16.0.23.24", prog_num=63929):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63930) as should_copy_source_864_63930:
                    should_copy_source_864_63930()
                    with Stage(r"copy source", r"Mac/Plugins/Key Detector.bundle", prog_num=63931):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", r".", delete_extraneous_files=True, prog_num=63932) as copy_dir_to_dir_865_63932:
                            copy_dir_to_dir_865_63932()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Key Detector.bundle", where_to_unwtar=r".", prog_num=63933) as unwtar_866_63933:
                            unwtar_866_63933()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Key Detector.bundle", user_id=-1, group_id=-1, prog_num=63934, recursive=True) as chown_867_63934:
                            chown_867_63934()
            with Stage(r"copy", r"KingsMic v16.0.23.24", prog_num=63935):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63936) as should_copy_source_868_63936:
                    should_copy_source_868_63936()
                    with Stage(r"copy source", r"Mac/Plugins/KingsMic.bundle", prog_num=63937):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", r".", delete_extraneous_files=True, prog_num=63938) as copy_dir_to_dir_869_63938:
                            copy_dir_to_dir_869_63938()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KingsMic.bundle", where_to_unwtar=r".", prog_num=63939) as unwtar_870_63939:
                            unwtar_870_63939()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KingsMic.bundle", user_id=-1, group_id=-1, prog_num=63940, recursive=True) as chown_871_63940:
                            chown_871_63940()
            with Stage(r"copy", r"KramerHLS v16.0.23.24", prog_num=63941):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63942) as should_copy_source_872_63942:
                    should_copy_source_872_63942()
                    with Stage(r"copy source", r"Mac/Plugins/KramerHLS.bundle", prog_num=63943):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", r".", delete_extraneous_files=True, prog_num=63944) as copy_dir_to_dir_873_63944:
                            copy_dir_to_dir_873_63944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerHLS.bundle", where_to_unwtar=r".", prog_num=63945) as unwtar_874_63945:
                            unwtar_874_63945()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerHLS.bundle", user_id=-1, group_id=-1, prog_num=63946, recursive=True) as chown_875_63946:
                            chown_875_63946()
            with Stage(r"copy", r"KramerPIE v16.0.23.24", prog_num=63947):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63948) as should_copy_source_876_63948:
                    should_copy_source_876_63948()
                    with Stage(r"copy source", r"Mac/Plugins/KramerPIE.bundle", prog_num=63949):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", r".", delete_extraneous_files=True, prog_num=63950) as copy_dir_to_dir_877_63950:
                            copy_dir_to_dir_877_63950()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerPIE.bundle", where_to_unwtar=r".", prog_num=63951) as unwtar_878_63951:
                            unwtar_878_63951()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerPIE.bundle", user_id=-1, group_id=-1, prog_num=63952, recursive=True) as chown_879_63952:
                            chown_879_63952()
            with Stage(r"copy", r"KramerTape v16.0.23.24", prog_num=63953):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63954) as should_copy_source_880_63954:
                    should_copy_source_880_63954()
                    with Stage(r"copy source", r"Mac/Plugins/KramerTape.bundle", prog_num=63955):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", r".", delete_extraneous_files=True, prog_num=63956) as copy_dir_to_dir_881_63956:
                            copy_dir_to_dir_881_63956()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/KramerTape.bundle", where_to_unwtar=r".", prog_num=63957) as unwtar_882_63957:
                            unwtar_882_63957()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/KramerTape.bundle", user_id=-1, group_id=-1, prog_num=63958, recursive=True) as chown_883_63958:
                            chown_883_63958()
            with Stage(r"copy", r"L1 v16.0.23.24", prog_num=63959):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63960) as should_copy_source_884_63960:
                    should_copy_source_884_63960()
                    with Stage(r"copy source", r"Mac/Plugins/L1.bundle", prog_num=63961):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", r".", delete_extraneous_files=True, prog_num=63962) as copy_dir_to_dir_885_63962:
                            copy_dir_to_dir_885_63962()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L1.bundle", where_to_unwtar=r".", prog_num=63963) as unwtar_886_63963:
                            unwtar_886_63963()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L1.bundle", user_id=-1, group_id=-1, prog_num=63964, recursive=True) as chown_887_63964:
                            chown_887_63964()
            with Stage(r"copy", r"L2 v16.0.23.24", prog_num=63965):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63966) as should_copy_source_888_63966:
                    should_copy_source_888_63966()
                    with Stage(r"copy source", r"Mac/Plugins/L2.bundle", prog_num=63967):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", r".", delete_extraneous_files=True, prog_num=63968) as copy_dir_to_dir_889_63968:
                            copy_dir_to_dir_889_63968()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L2.bundle", where_to_unwtar=r".", prog_num=63969) as unwtar_890_63969:
                            unwtar_890_63969()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L2.bundle", user_id=-1, group_id=-1, prog_num=63970, recursive=True) as chown_891_63970:
                            chown_891_63970()
            with Stage(r"copy", r"L360 v16.0.23.24", prog_num=63971):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63972) as should_copy_source_892_63972:
                    should_copy_source_892_63972()
                    with Stage(r"copy source", r"Mac/Plugins/L360.bundle", prog_num=63973):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", r".", delete_extraneous_files=True, prog_num=63974) as copy_dir_to_dir_893_63974:
                            copy_dir_to_dir_893_63974()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L360.bundle", where_to_unwtar=r".", prog_num=63975) as unwtar_894_63975:
                            unwtar_894_63975()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L360.bundle", user_id=-1, group_id=-1, prog_num=63976, recursive=True) as chown_895_63976:
                            chown_895_63976()
            with Stage(r"copy", r"L3-16 v16.0.23.24", prog_num=63977):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63978) as should_copy_source_896_63978:
                    should_copy_source_896_63978()
                    with Stage(r"copy source", r"Mac/Plugins/L3-16.bundle", prog_num=63979):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", r".", delete_extraneous_files=True, prog_num=63980) as copy_dir_to_dir_897_63980:
                            copy_dir_to_dir_897_63980()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-16.bundle", where_to_unwtar=r".", prog_num=63981) as unwtar_898_63981:
                            unwtar_898_63981()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-16.bundle", user_id=-1, group_id=-1, prog_num=63982, recursive=True) as chown_899_63982:
                            chown_899_63982()
            with Stage(r"copy", r"L3-LL Multi v16.0.23.24", prog_num=63983):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63984) as should_copy_source_900_63984:
                    should_copy_source_900_63984()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Multi.bundle", prog_num=63985):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", r".", delete_extraneous_files=True, prog_num=63986) as copy_dir_to_dir_901_63986:
                            copy_dir_to_dir_901_63986()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Multi.bundle", where_to_unwtar=r".", prog_num=63987) as unwtar_902_63987:
                            unwtar_902_63987()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Multi.bundle", user_id=-1, group_id=-1, prog_num=63988, recursive=True) as chown_903_63988:
                            chown_903_63988()
            with Stage(r"copy", r"L3-LL Ultra v16.0.23.24", prog_num=63989):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63990) as should_copy_source_904_63990:
                    should_copy_source_904_63990()
                    with Stage(r"copy source", r"Mac/Plugins/L3-LL Ultra.bundle", prog_num=63991):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", r".", delete_extraneous_files=True, prog_num=63992) as copy_dir_to_dir_905_63992:
                            copy_dir_to_dir_905_63992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3-LL Ultra.bundle", where_to_unwtar=r".", prog_num=63993) as unwtar_906_63993:
                            unwtar_906_63993()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3-LL Ultra.bundle", user_id=-1, group_id=-1, prog_num=63994, recursive=True) as chown_907_63994:
                            chown_907_63994()
            with Stage(r"copy", r"L3 Multi v16.0.23.24", prog_num=63995):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=63996) as should_copy_source_908_63996:
                    should_copy_source_908_63996()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Multi.bundle", prog_num=63997):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", r".", delete_extraneous_files=True, prog_num=63998) as copy_dir_to_dir_909_63998:
                            copy_dir_to_dir_909_63998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Multi.bundle", where_to_unwtar=r".", prog_num=63999) as unwtar_910_63999:
                            unwtar_910_63999()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Multi.bundle", user_id=-1, group_id=-1, prog_num=64000, recursive=True) as chown_911_64000:
                            chown_911_64000()
            with Stage(r"copy", r"L3 Ultra v16.0.23.24", prog_num=64001):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64002) as should_copy_source_912_64002:
                    should_copy_source_912_64002()
                    with Stage(r"copy source", r"Mac/Plugins/L3 Ultra.bundle", prog_num=64003):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", r".", delete_extraneous_files=True, prog_num=64004) as copy_dir_to_dir_913_64004:
                            copy_dir_to_dir_913_64004()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/L3 Ultra.bundle", where_to_unwtar=r".", prog_num=64005) as unwtar_914_64005:
                            unwtar_914_64005()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/L3 Ultra.bundle", user_id=-1, group_id=-1, prog_num=64006, recursive=True) as chown_915_64006:
                            chown_915_64006()
            with Stage(r"copy", r"LFE360 v16.0.23.24", prog_num=64007):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64008) as should_copy_source_916_64008:
                    should_copy_source_916_64008()
                    with Stage(r"copy source", r"Mac/Plugins/LFE360.bundle", prog_num=64009):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", r".", delete_extraneous_files=True, prog_num=64010) as copy_dir_to_dir_917_64010:
                            copy_dir_to_dir_917_64010()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LFE360.bundle", where_to_unwtar=r".", prog_num=64011) as unwtar_918_64011:
                            unwtar_918_64011()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LFE360.bundle", user_id=-1, group_id=-1, prog_num=64012, recursive=True) as chown_919_64012:
                            chown_919_64012()
            with Stage(r"copy", r"Lil Tube v16.0.23.24", prog_num=64013):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64014) as should_copy_source_920_64014:
                    should_copy_source_920_64014()
                    with Stage(r"copy source", r"Mac/Plugins/Lil Tube.bundle", prog_num=64015):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", r".", delete_extraneous_files=True, prog_num=64016) as copy_dir_to_dir_921_64016:
                            copy_dir_to_dir_921_64016()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lil Tube.bundle", where_to_unwtar=r".", prog_num=64017) as unwtar_922_64017:
                            unwtar_922_64017()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lil Tube.bundle", user_id=-1, group_id=-1, prog_num=64018, recursive=True) as chown_923_64018:
                            chown_923_64018()
            with Stage(r"copy", r"LinEQ v16.0.23.24", prog_num=64019):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64020) as should_copy_source_924_64020:
                    should_copy_source_924_64020()
                    with Stage(r"copy source", r"Mac/Plugins/LinEQ.bundle", prog_num=64021):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", r".", delete_extraneous_files=True, prog_num=64022) as copy_dir_to_dir_925_64022:
                            copy_dir_to_dir_925_64022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinEQ.bundle", where_to_unwtar=r".", prog_num=64023) as unwtar_926_64023:
                            unwtar_926_64023()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinEQ.bundle", user_id=-1, group_id=-1, prog_num=64024, recursive=True) as chown_927_64024:
                            chown_927_64024()
            with Stage(r"copy", r"LinMB v16.0.23.24", prog_num=64025):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64026) as should_copy_source_928_64026:
                    should_copy_source_928_64026()
                    with Stage(r"copy source", r"Mac/Plugins/LinMB.bundle", prog_num=64027):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", r".", delete_extraneous_files=True, prog_num=64028) as copy_dir_to_dir_929_64028:
                            copy_dir_to_dir_929_64028()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LinMB.bundle", where_to_unwtar=r".", prog_num=64029) as unwtar_930_64029:
                            unwtar_930_64029()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LinMB.bundle", user_id=-1, group_id=-1, prog_num=64030, recursive=True) as chown_931_64030:
                            chown_931_64030()
            with Stage(r"copy", r"LoAir v16.0.23.24", prog_num=64031):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64032) as should_copy_source_932_64032:
                    should_copy_source_932_64032()
                    with Stage(r"copy source", r"Mac/Plugins/LoAir.bundle", prog_num=64033):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", r".", delete_extraneous_files=True, prog_num=64034) as copy_dir_to_dir_933_64034:
                            copy_dir_to_dir_933_64034()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/LoAir.bundle", where_to_unwtar=r".", prog_num=64035) as unwtar_934_64035:
                            unwtar_934_64035()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/LoAir.bundle", user_id=-1, group_id=-1, prog_num=64036, recursive=True) as chown_935_64036:
                            chown_935_64036()
            with Stage(r"copy", r"Lofi Space v16.0.23.24", prog_num=64037):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64038) as should_copy_source_936_64038:
                    should_copy_source_936_64038()
                    with Stage(r"copy source", r"Mac/Plugins/Lofi Space.bundle", prog_num=64039):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", r".", delete_extraneous_files=True, prog_num=64040) as copy_dir_to_dir_937_64040:
                            copy_dir_to_dir_937_64040()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Lofi Space.bundle", where_to_unwtar=r".", prog_num=64041) as unwtar_938_64041:
                            unwtar_938_64041()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Lofi Space.bundle", user_id=-1, group_id=-1, prog_num=64042, recursive=True) as chown_939_64042:
                            chown_939_64042()
            with Stage(r"copy", r"MDMX Distortion v16.0.23.24", prog_num=64043):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64044) as should_copy_source_940_64044:
                    should_copy_source_940_64044()
                    with Stage(r"copy source", r"Mac/Plugins/MDMX Distortion.bundle", prog_num=64045):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", r".", delete_extraneous_files=True, prog_num=64046) as copy_dir_to_dir_941_64046:
                            copy_dir_to_dir_941_64046()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MDMX Distortion.bundle", where_to_unwtar=r".", prog_num=64047) as unwtar_942_64047:
                            unwtar_942_64047()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MDMX Distortion.bundle", user_id=-1, group_id=-1, prog_num=64048, recursive=True) as chown_943_64048:
                            chown_943_64048()
            with Stage(r"copy", r"MV2 v16.0.23.24", prog_num=64049):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64050) as should_copy_source_944_64050:
                    should_copy_source_944_64050()
                    with Stage(r"copy source", r"Mac/Plugins/MV2.bundle", prog_num=64051):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", r".", delete_extraneous_files=True, prog_num=64052) as copy_dir_to_dir_945_64052:
                            copy_dir_to_dir_945_64052()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV2.bundle", where_to_unwtar=r".", prog_num=64053) as unwtar_946_64053:
                            unwtar_946_64053()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV2.bundle", user_id=-1, group_id=-1, prog_num=64054, recursive=True) as chown_947_64054:
                            chown_947_64054()
            with Stage(r"copy", r"MV360 v16.0.23.24", prog_num=64055):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64056) as should_copy_source_948_64056:
                    should_copy_source_948_64056()
                    with Stage(r"copy source", r"Mac/Plugins/MV360.bundle", prog_num=64057):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", r".", delete_extraneous_files=True, prog_num=64058) as copy_dir_to_dir_949_64058:
                            copy_dir_to_dir_949_64058()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MV360.bundle", where_to_unwtar=r".", prog_num=64059) as unwtar_950_64059:
                            unwtar_950_64059()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MV360.bundle", user_id=-1, group_id=-1, prog_num=64060, recursive=True) as chown_951_64060:
                            chown_951_64060()
            with Stage(r"copy", r"Magma Channel Strip v16.0.23.24", prog_num=64061):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64062) as should_copy_source_952_64062:
                    should_copy_source_952_64062()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaChannelStrip.bundle", prog_num=64063):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", r".", delete_extraneous_files=True, prog_num=64064) as copy_dir_to_dir_953_64064:
                            copy_dir_to_dir_953_64064()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaChannelStrip.bundle", where_to_unwtar=r".", prog_num=64065) as unwtar_954_64065:
                            unwtar_954_64065()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaChannelStrip.bundle", user_id=-1, group_id=-1, prog_num=64066, recursive=True) as chown_955_64066:
                            chown_955_64066()
            with Stage(r"copy", r"Magma Springs v16.0.23.24", prog_num=64067):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64068) as should_copy_source_956_64068:
                    should_copy_source_956_64068()
                    with Stage(r"copy source", r"Mac/Plugins/MagmaSprings.bundle", prog_num=64069):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", r".", delete_extraneous_files=True, prog_num=64070) as copy_dir_to_dir_957_64070:
                            copy_dir_to_dir_957_64070()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MagmaSprings.bundle", where_to_unwtar=r".", prog_num=64071) as unwtar_958_64071:
                            unwtar_958_64071()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MagmaSprings.bundle", user_id=-1, group_id=-1, prog_num=64072, recursive=True) as chown_959_64072:
                            chown_959_64072()
            with Stage(r"copy", r"MannyM-Delay v16.0.23.24", prog_num=64073):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64074) as should_copy_source_960_64074:
                    should_copy_source_960_64074()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Delay.bundle", prog_num=64075):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", r".", delete_extraneous_files=True, prog_num=64076) as copy_dir_to_dir_961_64076:
                            copy_dir_to_dir_961_64076()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Delay.bundle", where_to_unwtar=r".", prog_num=64077) as unwtar_962_64077:
                            unwtar_962_64077()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Delay.bundle", user_id=-1, group_id=-1, prog_num=64078, recursive=True) as chown_963_64078:
                            chown_963_64078()
            with Stage(r"copy", r"MannyM-Distortion v16.0.23.24", prog_num=64079):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64080) as should_copy_source_964_64080:
                    should_copy_source_964_64080()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Distortion.bundle", prog_num=64081):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", r".", delete_extraneous_files=True, prog_num=64082) as copy_dir_to_dir_965_64082:
                            copy_dir_to_dir_965_64082()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Distortion.bundle", where_to_unwtar=r".", prog_num=64083) as unwtar_966_64083:
                            unwtar_966_64083()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Distortion.bundle", user_id=-1, group_id=-1, prog_num=64084, recursive=True) as chown_967_64084:
                            chown_967_64084()
            with Stage(r"copy", r"MannyM-EQ v16.0.23.24", prog_num=64085):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64086) as should_copy_source_968_64086:
                    should_copy_source_968_64086()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-EQ.bundle", prog_num=64087):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", r".", delete_extraneous_files=True, prog_num=64088) as copy_dir_to_dir_969_64088:
                            copy_dir_to_dir_969_64088()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-EQ.bundle", where_to_unwtar=r".", prog_num=64089) as unwtar_970_64089:
                            unwtar_970_64089()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-EQ.bundle", user_id=-1, group_id=-1, prog_num=64090, recursive=True) as chown_971_64090:
                            chown_971_64090()
            with Stage(r"copy", r"MannyM-Reverb v16.0.23.24", prog_num=64091):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64092) as should_copy_source_972_64092:
                    should_copy_source_972_64092()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-Reverb.bundle", prog_num=64093):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", r".", delete_extraneous_files=True, prog_num=64094) as copy_dir_to_dir_973_64094:
                            copy_dir_to_dir_973_64094()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-Reverb.bundle", where_to_unwtar=r".", prog_num=64095) as unwtar_974_64095:
                            unwtar_974_64095()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-Reverb.bundle", user_id=-1, group_id=-1, prog_num=64096, recursive=True) as chown_975_64096:
                            chown_975_64096()
            with Stage(r"copy", r"MannyM-ToneShaper v16.0.23.24", prog_num=64097):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64098) as should_copy_source_976_64098:
                    should_copy_source_976_64098()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-ToneShaper.bundle", prog_num=64099):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", r".", delete_extraneous_files=True, prog_num=64100) as copy_dir_to_dir_977_64100:
                            copy_dir_to_dir_977_64100()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-ToneShaper.bundle", where_to_unwtar=r".", prog_num=64101) as unwtar_978_64101:
                            unwtar_978_64101()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-ToneShaper.bundle", user_id=-1, group_id=-1, prog_num=64102, recursive=True) as chown_979_64102:
                            chown_979_64102()
            with Stage(r"copy", r"MannyM-TripleD v16.0.23.24", prog_num=64103):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64104) as should_copy_source_980_64104:
                    should_copy_source_980_64104()
                    with Stage(r"copy source", r"Mac/Plugins/MannyM-TripleD.bundle", prog_num=64105):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", r".", delete_extraneous_files=True, prog_num=64106) as copy_dir_to_dir_981_64106:
                            copy_dir_to_dir_981_64106()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MannyM-TripleD.bundle", where_to_unwtar=r".", prog_num=64107) as unwtar_982_64107:
                            unwtar_982_64107()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MannyM-TripleD.bundle", user_id=-1, group_id=-1, prog_num=64108, recursive=True) as chown_983_64108:
                            chown_983_64108()
            with Stage(r"copy", r"Maserati ACG v16.0.23.24", prog_num=64109):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64110) as should_copy_source_984_64110:
                    should_copy_source_984_64110()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati ACG.bundle", prog_num=64111):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", r".", delete_extraneous_files=True, prog_num=64112) as copy_dir_to_dir_985_64112:
                            copy_dir_to_dir_985_64112()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati ACG.bundle", where_to_unwtar=r".", prog_num=64113) as unwtar_986_64113:
                            unwtar_986_64113()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati ACG.bundle", user_id=-1, group_id=-1, prog_num=64114, recursive=True) as chown_987_64114:
                            chown_987_64114()
            with Stage(r"copy", r"Maserati B72 v16.0.23.24", prog_num=64115):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64116) as should_copy_source_988_64116:
                    should_copy_source_988_64116()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati B72.bundle", prog_num=64117):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", r".", delete_extraneous_files=True, prog_num=64118) as copy_dir_to_dir_989_64118:
                            copy_dir_to_dir_989_64118()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati B72.bundle", where_to_unwtar=r".", prog_num=64119) as unwtar_990_64119:
                            unwtar_990_64119()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati B72.bundle", user_id=-1, group_id=-1, prog_num=64120, recursive=True) as chown_991_64120:
                            chown_991_64120()
            with Stage(r"copy", r"Maserati DRM v16.0.23.24", prog_num=64121):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64122) as should_copy_source_992_64122:
                    should_copy_source_992_64122()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati DRM.bundle", prog_num=64123):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", r".", delete_extraneous_files=True, prog_num=64124) as copy_dir_to_dir_993_64124:
                            copy_dir_to_dir_993_64124()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati DRM.bundle", where_to_unwtar=r".", prog_num=64125) as unwtar_994_64125:
                            unwtar_994_64125()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati DRM.bundle", user_id=-1, group_id=-1, prog_num=64126, recursive=True) as chown_995_64126:
                            chown_995_64126()
            with Stage(r"copy", r"Maserati GRP v16.0.23.24", prog_num=64127):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64128) as should_copy_source_996_64128:
                    should_copy_source_996_64128()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati GRP.bundle", prog_num=64129):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", r".", delete_extraneous_files=True, prog_num=64130) as copy_dir_to_dir_997_64130:
                            copy_dir_to_dir_997_64130()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GRP.bundle", where_to_unwtar=r".", prog_num=64131) as unwtar_998_64131:
                            unwtar_998_64131()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati GRP.bundle", user_id=-1, group_id=-1, prog_num=64132, recursive=True) as chown_999_64132:
                            chown_999_64132()
            with Stage(r"copy", r"Maserati GTi v16.0.23.24", prog_num=64133):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64134) as should_copy_source_1000_64134:
                    should_copy_source_1000_64134()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati GTi.bundle", prog_num=64135):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", r".", delete_extraneous_files=True, prog_num=64136) as copy_dir_to_dir_1001_64136:
                            copy_dir_to_dir_1001_64136()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati GTi.bundle", where_to_unwtar=r".", prog_num=64137) as unwtar_1002_64137:
                            unwtar_1002_64137()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati GTi.bundle", user_id=-1, group_id=-1, prog_num=64138, recursive=True) as chown_1003_64138:
                            chown_1003_64138()
            with Stage(r"copy", r"Maserati HMX v16.0.23.24", prog_num=64139):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64140) as should_copy_source_1004_64140:
                    should_copy_source_1004_64140()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati HMX.bundle", prog_num=64141):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", r".", delete_extraneous_files=True, prog_num=64142) as copy_dir_to_dir_1005_64142:
                            copy_dir_to_dir_1005_64142()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati HMX.bundle", where_to_unwtar=r".", prog_num=64143) as unwtar_1006_64143:
                            unwtar_1006_64143()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati HMX.bundle", user_id=-1, group_id=-1, prog_num=64144, recursive=True) as chown_1007_64144:
                            chown_1007_64144()
            with Stage(r"copy", r"Maserati VX1 v16.0.23.24", prog_num=64145):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64146) as should_copy_source_1008_64146:
                    should_copy_source_1008_64146()
                    with Stage(r"copy source", r"Mac/Plugins/Maserati VX1.bundle", prog_num=64147):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", r".", delete_extraneous_files=True, prog_num=64148) as copy_dir_to_dir_1009_64148:
                            copy_dir_to_dir_1009_64148()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Maserati VX1.bundle", where_to_unwtar=r".", prog_num=64149) as unwtar_1010_64149:
                            unwtar_1010_64149()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Maserati VX1.bundle", user_id=-1, group_id=-1, prog_num=64150, recursive=True) as chown_1011_64150:
                            chown_1011_64150()
            with Stage(r"copy", r"MaxxBass v16.0.30.31", prog_num=64151):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64152) as should_copy_source_1012_64152:
                    should_copy_source_1012_64152()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxBass.bundle", prog_num=64153):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", r".", delete_extraneous_files=True, prog_num=64154) as copy_dir_to_dir_1013_64154:
                            copy_dir_to_dir_1013_64154()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxBass.bundle", where_to_unwtar=r".", prog_num=64155) as unwtar_1014_64155:
                            unwtar_1014_64155()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxBass.bundle", user_id=-1, group_id=-1, prog_num=64156, recursive=True) as chown_1015_64156:
                            chown_1015_64156()
            with Stage(r"copy", r"MaxxVolume v16.0.23.24", prog_num=64157):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64158) as should_copy_source_1016_64158:
                    should_copy_source_1016_64158()
                    with Stage(r"copy source", r"Mac/Plugins/MaxxVolume.bundle", prog_num=64159):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", r".", delete_extraneous_files=True, prog_num=64160) as copy_dir_to_dir_1017_64160:
                            copy_dir_to_dir_1017_64160()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MaxxVolume.bundle", where_to_unwtar=r".", prog_num=64161) as unwtar_1018_64161:
                            unwtar_1018_64161()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MaxxVolume.bundle", user_id=-1, group_id=-1, prog_num=64162, recursive=True) as chown_1019_64162:
                            chown_1019_64162()
            with Stage(r"copy", r"MetaFilter v16.0.23.24", prog_num=64163):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64164) as should_copy_source_1020_64164:
                    should_copy_source_1020_64164()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFilter.bundle", prog_num=64165):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", r".", delete_extraneous_files=True, prog_num=64166) as copy_dir_to_dir_1021_64166:
                            copy_dir_to_dir_1021_64166()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFilter.bundle", where_to_unwtar=r".", prog_num=64167) as unwtar_1022_64167:
                            unwtar_1022_64167()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFilter.bundle", user_id=-1, group_id=-1, prog_num=64168, recursive=True) as chown_1023_64168:
                            chown_1023_64168()
            with Stage(r"copy", r"MetaFlanger v16.0.23.24", prog_num=64169):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64170) as should_copy_source_1024_64170:
                    should_copy_source_1024_64170()
                    with Stage(r"copy source", r"Mac/Plugins/MetaFlanger.bundle", prog_num=64171):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64172) as copy_dir_to_dir_1025_64172:
                            copy_dir_to_dir_1025_64172()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MetaFlanger.bundle", where_to_unwtar=r".", prog_num=64173) as unwtar_1026_64173:
                            unwtar_1026_64173()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MetaFlanger.bundle", user_id=-1, group_id=-1, prog_num=64174, recursive=True) as chown_1027_64174:
                            chown_1027_64174()
            with Stage(r"copy", r"MondoMod v16.0.23.24", prog_num=64175):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64176) as should_copy_source_1028_64176:
                    should_copy_source_1028_64176()
                    with Stage(r"copy source", r"Mac/Plugins/MondoMod.bundle", prog_num=64177):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", r".", delete_extraneous_files=True, prog_num=64178) as copy_dir_to_dir_1029_64178:
                            copy_dir_to_dir_1029_64178()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MondoMod.bundle", where_to_unwtar=r".", prog_num=64179) as unwtar_1030_64179:
                            unwtar_1030_64179()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MondoMod.bundle", user_id=-1, group_id=-1, prog_num=64180, recursive=True) as chown_1031_64180:
                            chown_1031_64180()
            with Stage(r"copy", r"Morphoder v16.0.23.24", prog_num=64181):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64182) as should_copy_source_1032_64182:
                    should_copy_source_1032_64182()
                    with Stage(r"copy source", r"Mac/Plugins/Morphoder.bundle", prog_num=64183):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", r".", delete_extraneous_files=True, prog_num=64184) as copy_dir_to_dir_1033_64184:
                            copy_dir_to_dir_1033_64184()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Morphoder.bundle", where_to_unwtar=r".", prog_num=64185) as unwtar_1034_64185:
                            unwtar_1034_64185()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Morphoder.bundle", user_id=-1, group_id=-1, prog_num=64186, recursive=True) as chown_1035_64186:
                            chown_1035_64186()
            with Stage(r"copy", r"MultiMod Rack v16.0.23.24", prog_num=64187):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64188) as should_copy_source_1036_64188:
                    should_copy_source_1036_64188()
                    with Stage(r"copy source", r"Mac/Plugins/MultiMod Rack.bundle", prog_num=64189):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", r".", delete_extraneous_files=True, prog_num=64190) as copy_dir_to_dir_1037_64190:
                            copy_dir_to_dir_1037_64190()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MultiMod Rack.bundle", where_to_unwtar=r".", prog_num=64191) as unwtar_1038_64191:
                            unwtar_1038_64191()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MultiMod Rack.bundle", user_id=-1, group_id=-1, prog_num=64192, recursive=True) as chown_1039_64192:
                            chown_1039_64192()
            with Stage(r"copy", r"StudioVerse Instruments v16.0.30.31", prog_num=64193):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64194) as should_copy_source_1040_64194:
                    should_copy_source_1040_64194()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Instruments.bundle", prog_num=64195):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", r".", delete_extraneous_files=True, prog_num=64196) as copy_dir_to_dir_1041_64196:
                            copy_dir_to_dir_1041_64196()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Instruments.bundle", where_to_unwtar=r".", prog_num=64197) as unwtar_1042_64197:
                            unwtar_1042_64197()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/StudioVerse Instruments.bundle", user_id=-1, group_id=-1, prog_num=64198, recursive=True) as chown_1043_64198:
                            chown_1043_64198()
            with Stage(r"copy", r"NLS v16.0.23.24", prog_num=64199):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64200) as should_copy_source_1044_64200:
                    should_copy_source_1044_64200()
                    with Stage(r"copy source", r"Mac/Plugins/NLS.bundle", prog_num=64201):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", r".", delete_extraneous_files=True, prog_num=64202) as copy_dir_to_dir_1045_64202:
                            copy_dir_to_dir_1045_64202()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NLS.bundle", where_to_unwtar=r".", prog_num=64203) as unwtar_1046_64203:
                            unwtar_1046_64203()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NLS.bundle", user_id=-1, group_id=-1, prog_num=64204, recursive=True) as chown_1047_64204:
                            chown_1047_64204()
            with Stage(r"copy", r"NS1 v16.0.23.24", prog_num=64205):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64206) as should_copy_source_1048_64206:
                    should_copy_source_1048_64206()
                    with Stage(r"copy source", r"Mac/Plugins/NS1.bundle", prog_num=64207):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", r".", delete_extraneous_files=True, prog_num=64208) as copy_dir_to_dir_1049_64208:
                            copy_dir_to_dir_1049_64208()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NS1.bundle", where_to_unwtar=r".", prog_num=64209) as unwtar_1050_64209:
                            unwtar_1050_64209()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NS1.bundle", user_id=-1, group_id=-1, prog_num=64210, recursive=True) as chown_1051_64210:
                            chown_1051_64210()
            with Stage(r"copy", r"NX v16.0.23.24", prog_num=64211):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64212) as should_copy_source_1052_64212:
                    should_copy_source_1052_64212()
                    with Stage(r"copy source", r"Mac/Plugins/NX.bundle", prog_num=64213):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", r".", delete_extraneous_files=True, prog_num=64214) as copy_dir_to_dir_1053_64214:
                            copy_dir_to_dir_1053_64214()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/NX.bundle", where_to_unwtar=r".", prog_num=64215) as unwtar_1054_64215:
                            unwtar_1054_64215()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/NX.bundle", user_id=-1, group_id=-1, prog_num=64216, recursive=True) as chown_1055_64216:
                            chown_1055_64216()
            with Stage(r"copy", r"Nx Ocean Way Nashville v16.0.23.24", prog_num=64217):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64218) as should_copy_source_1056_64218:
                    should_copy_source_1056_64218()
                    with Stage(r"copy source", r"Mac/Plugins/Nx Ocean Way Nashville.bundle", prog_num=64219):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", r".", delete_extraneous_files=True, prog_num=64220) as copy_dir_to_dir_1057_64220:
                            copy_dir_to_dir_1057_64220()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Ocean Way Nashville.bundle", where_to_unwtar=r".", prog_num=64221) as unwtar_1058_64221:
                            unwtar_1058_64221()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Nx Ocean Way Nashville.bundle", user_id=-1, group_id=-1, prog_num=64222, recursive=True) as chown_1059_64222:
                            chown_1059_64222()
            with Stage(r"copy", r"Nx Germano Studios v16.0.23.24", prog_num=64223):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64224) as should_copy_source_1060_64224:
                    should_copy_source_1060_64224()
                    with Stage(r"copy source", r"Mac/Plugins/Nx Germano Studios.bundle", prog_num=64225):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", r".", delete_extraneous_files=True, prog_num=64226) as copy_dir_to_dir_1061_64226:
                            copy_dir_to_dir_1061_64226()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Nx Germano Studios.bundle", where_to_unwtar=r".", prog_num=64227) as unwtar_1062_64227:
                            unwtar_1062_64227()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Nx Germano Studios.bundle", user_id=-1, group_id=-1, prog_num=64228, recursive=True) as chown_1063_64228:
                            chown_1063_64228()
            with Stage(r"copy", r"OKBrighter v16.0.23.24", prog_num=64229):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64230) as should_copy_source_1064_64230:
                    should_copy_source_1064_64230()
                    with Stage(r"copy source", r"Mac/Plugins/OKBrighter.bundle", prog_num=64231):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", r".", delete_extraneous_files=True, prog_num=64232) as copy_dir_to_dir_1065_64232:
                            copy_dir_to_dir_1065_64232()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKBrighter.bundle", where_to_unwtar=r".", prog_num=64233) as unwtar_1066_64233:
                            unwtar_1066_64233()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKBrighter.bundle", user_id=-1, group_id=-1, prog_num=64234, recursive=True) as chown_1067_64234:
                            chown_1067_64234()
            with Stage(r"copy", r"OKDriver v16.0.23.24", prog_num=64235):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64236) as should_copy_source_1068_64236:
                    should_copy_source_1068_64236()
                    with Stage(r"copy source", r"Mac/Plugins/OKDriver.bundle", prog_num=64237):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", r".", delete_extraneous_files=True, prog_num=64238) as copy_dir_to_dir_1069_64238:
                            copy_dir_to_dir_1069_64238()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKDriver.bundle", where_to_unwtar=r".", prog_num=64239) as unwtar_1070_64239:
                            unwtar_1070_64239()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKDriver.bundle", user_id=-1, group_id=-1, prog_num=64240, recursive=True) as chown_1071_64240:
                            chown_1071_64240()
            with Stage(r"copy", r"OKFilter v16.0.23.24", prog_num=64241):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64242) as should_copy_source_1072_64242:
                    should_copy_source_1072_64242()
                    with Stage(r"copy source", r"Mac/Plugins/OKFilter.bundle", prog_num=64243):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", r".", delete_extraneous_files=True, prog_num=64244) as copy_dir_to_dir_1073_64244:
                            copy_dir_to_dir_1073_64244()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKFilter.bundle", where_to_unwtar=r".", prog_num=64245) as unwtar_1074_64245:
                            unwtar_1074_64245()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKFilter.bundle", user_id=-1, group_id=-1, prog_num=64246, recursive=True) as chown_1075_64246:
                            chown_1075_64246()
            with Stage(r"copy", r"OKLouder v16.0.23.24", prog_num=64247):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64248) as should_copy_source_1076_64248:
                    should_copy_source_1076_64248()
                    with Stage(r"copy source", r"Mac/Plugins/OKLouder.bundle", prog_num=64249):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", r".", delete_extraneous_files=True, prog_num=64250) as copy_dir_to_dir_1077_64250:
                            copy_dir_to_dir_1077_64250()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKLouder.bundle", where_to_unwtar=r".", prog_num=64251) as unwtar_1078_64251:
                            unwtar_1078_64251()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKLouder.bundle", user_id=-1, group_id=-1, prog_num=64252, recursive=True) as chown_1079_64252:
                            chown_1079_64252()
            with Stage(r"copy", r"OKPhatter v16.0.23.24", prog_num=64253):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64254) as should_copy_source_1080_64254:
                    should_copy_source_1080_64254()
                    with Stage(r"copy source", r"Mac/Plugins/OKPhatter.bundle", prog_num=64255):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", r".", delete_extraneous_files=True, prog_num=64256) as copy_dir_to_dir_1081_64256:
                            copy_dir_to_dir_1081_64256()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPhatter.bundle", where_to_unwtar=r".", prog_num=64257) as unwtar_1082_64257:
                            unwtar_1082_64257()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPhatter.bundle", user_id=-1, group_id=-1, prog_num=64258, recursive=True) as chown_1083_64258:
                            chown_1083_64258()
            with Stage(r"copy", r"OKPressure v16.0.23.24", prog_num=64259):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64260) as should_copy_source_1084_64260:
                    should_copy_source_1084_64260()
                    with Stage(r"copy source", r"Mac/Plugins/OKPressure.bundle", prog_num=64261):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", r".", delete_extraneous_files=True, prog_num=64262) as copy_dir_to_dir_1085_64262:
                            copy_dir_to_dir_1085_64262()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPressure.bundle", where_to_unwtar=r".", prog_num=64263) as unwtar_1086_64263:
                            unwtar_1086_64263()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPressure.bundle", user_id=-1, group_id=-1, prog_num=64264, recursive=True) as chown_1087_64264:
                            chown_1087_64264()
            with Stage(r"copy", r"OKPumper v16.0.23.24", prog_num=64265):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64266) as should_copy_source_1088_64266:
                    should_copy_source_1088_64266()
                    with Stage(r"copy source", r"Mac/Plugins/OKPumper.bundle", prog_num=64267):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", r".", delete_extraneous_files=True, prog_num=64268) as copy_dir_to_dir_1089_64268:
                            copy_dir_to_dir_1089_64268()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKPumper.bundle", where_to_unwtar=r".", prog_num=64269) as unwtar_1090_64269:
                            unwtar_1090_64269()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKPumper.bundle", user_id=-1, group_id=-1, prog_num=64270, recursive=True) as chown_1091_64270:
                            chown_1091_64270()
            with Stage(r"copy", r"OKWetter v16.0.23.24", prog_num=64271):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64272) as should_copy_source_1092_64272:
                    should_copy_source_1092_64272()
                    with Stage(r"copy source", r"Mac/Plugins/OKWetter.bundle", prog_num=64273):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", r".", delete_extraneous_files=True, prog_num=64274) as copy_dir_to_dir_1093_64274:
                            copy_dir_to_dir_1093_64274()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OKWetter.bundle", where_to_unwtar=r".", prog_num=64275) as unwtar_1094_64275:
                            unwtar_1094_64275()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OKWetter.bundle", user_id=-1, group_id=-1, prog_num=64276, recursive=True) as chown_1095_64276:
                            chown_1095_64276()
            with Stage(r"copy", r"OVox v16.0.23.24", prog_num=64277):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64278) as should_copy_source_1096_64278:
                    should_copy_source_1096_64278()
                    with Stage(r"copy source", r"Mac/Plugins/OVox.bundle", prog_num=64279):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", r".", delete_extraneous_files=True, prog_num=64280) as copy_dir_to_dir_1097_64280:
                            copy_dir_to_dir_1097_64280()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/OVox.bundle", where_to_unwtar=r".", prog_num=64281) as unwtar_1098_64281:
                            unwtar_1098_64281()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/OVox.bundle", user_id=-1, group_id=-1, prog_num=64282, recursive=True) as chown_1099_64282:
                            chown_1099_64282()
            with Stage(r"copy", r"PAZ v16.0.23.24", prog_num=64283):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64284) as should_copy_source_1100_64284:
                    should_copy_source_1100_64284()
                    with Stage(r"copy source", r"Mac/Plugins/PAZ.bundle", prog_num=64285):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", r".", delete_extraneous_files=True, prog_num=64286) as copy_dir_to_dir_1101_64286:
                            copy_dir_to_dir_1101_64286()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PAZ.bundle", where_to_unwtar=r".", prog_num=64287) as unwtar_1102_64287:
                            unwtar_1102_64287()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PAZ.bundle", user_id=-1, group_id=-1, prog_num=64288, recursive=True) as chown_1103_64288:
                            chown_1103_64288()
            with Stage(r"copy", r"PRS Supermodels v16.0.23.24", prog_num=64289):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64290) as should_copy_source_1104_64290:
                    should_copy_source_1104_64290()
                    with Stage(r"copy source", r"Mac/Plugins/PRS Supermodels.bundle", prog_num=64291):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", r".", delete_extraneous_files=True, prog_num=64292) as copy_dir_to_dir_1105_64292:
                            copy_dir_to_dir_1105_64292()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PRS Supermodels.bundle", where_to_unwtar=r".", prog_num=64293) as unwtar_1106_64293:
                            unwtar_1106_64293()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PRS Supermodels.bundle", user_id=-1, group_id=-1, prog_num=64294, recursive=True) as chown_1107_64294:
                            chown_1107_64294()
            with Stage(r"copy", r"PS22 v16.0.23.24", prog_num=64295):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64296) as should_copy_source_1108_64296:
                    should_copy_source_1108_64296()
                    with Stage(r"copy source", r"Mac/Plugins/PS22.bundle", prog_num=64297):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", r".", delete_extraneous_files=True, prog_num=64298) as copy_dir_to_dir_1109_64298:
                            copy_dir_to_dir_1109_64298()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PS22.bundle", where_to_unwtar=r".", prog_num=64299) as unwtar_1110_64299:
                            unwtar_1110_64299()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PS22.bundle", user_id=-1, group_id=-1, prog_num=64300, recursive=True) as chown_1111_64300:
                            chown_1111_64300()
            with Stage(r"copy", r"Primary Source Expander v16.0.23.24", prog_num=64301):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64302) as should_copy_source_1112_64302:
                    should_copy_source_1112_64302()
                    with Stage(r"copy source", r"Mac/Plugins/Primary Source Expander.bundle", prog_num=64303):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", r".", delete_extraneous_files=True, prog_num=64304) as copy_dir_to_dir_1113_64304:
                            copy_dir_to_dir_1113_64304()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Primary Source Expander.bundle", where_to_unwtar=r".", prog_num=64305) as unwtar_1114_64305:
                            unwtar_1114_64305()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Primary Source Expander.bundle", user_id=-1, group_id=-1, prog_num=64306, recursive=True) as chown_1115_64306:
                            chown_1115_64306()
            with Stage(r"copy", r"PlaylistRider v16.0.23.24", prog_num=64307):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64308) as should_copy_source_1116_64308:
                    should_copy_source_1116_64308()
                    with Stage(r"copy source", r"Mac/Plugins/PlaylistRider.bundle", prog_num=64309):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", r".", delete_extraneous_files=True, prog_num=64310) as copy_dir_to_dir_1117_64310:
                            copy_dir_to_dir_1117_64310()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PlaylistRider.bundle", where_to_unwtar=r".", prog_num=64311) as unwtar_1118_64311:
                            unwtar_1118_64311()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PlaylistRider.bundle", user_id=-1, group_id=-1, prog_num=64312, recursive=True) as chown_1119_64312:
                            chown_1119_64312()
            with Stage(r"copy", r"PuigChild v16.0.23.24", prog_num=64313):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64314) as should_copy_source_1120_64314:
                    should_copy_source_1120_64314()
                    with Stage(r"copy source", r"Mac/Plugins/PuigChild.bundle", prog_num=64315):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", r".", delete_extraneous_files=True, prog_num=64316) as copy_dir_to_dir_1121_64316:
                            copy_dir_to_dir_1121_64316()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigChild.bundle", where_to_unwtar=r".", prog_num=64317) as unwtar_1122_64317:
                            unwtar_1122_64317()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigChild.bundle", user_id=-1, group_id=-1, prog_num=64318, recursive=True) as chown_1123_64318:
                            chown_1123_64318()
            with Stage(r"copy", r"PuigTec v16.0.23.24", prog_num=64319):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64320) as should_copy_source_1124_64320:
                    should_copy_source_1124_64320()
                    with Stage(r"copy source", r"Mac/Plugins/PuigTec.bundle", prog_num=64321):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", r".", delete_extraneous_files=True, prog_num=64322) as copy_dir_to_dir_1125_64322:
                            copy_dir_to_dir_1125_64322()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/PuigTec.bundle", where_to_unwtar=r".", prog_num=64323) as unwtar_1126_64323:
                            unwtar_1126_64323()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/PuigTec.bundle", user_id=-1, group_id=-1, prog_num=64324, recursive=True) as chown_1127_64324:
                            chown_1127_64324()
            with Stage(r"copy", r"Q10 v16.0.23.24", prog_num=64325):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64326) as should_copy_source_1128_64326:
                    should_copy_source_1128_64326()
                    with Stage(r"copy source", r"Mac/Plugins/Q10.bundle", prog_num=64327):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", r".", delete_extraneous_files=True, prog_num=64328) as copy_dir_to_dir_1129_64328:
                            copy_dir_to_dir_1129_64328()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q10.bundle", where_to_unwtar=r".", prog_num=64329) as unwtar_1130_64329:
                            unwtar_1130_64329()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q10.bundle", user_id=-1, group_id=-1, prog_num=64330, recursive=True) as chown_1131_64330:
                            chown_1131_64330()
            with Stage(r"copy", r"Q-Clone v16.0.23.24", prog_num=64331):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64332) as should_copy_source_1132_64332:
                    should_copy_source_1132_64332()
                    with Stage(r"copy source", r"Mac/Plugins/Q-Clone.bundle", prog_num=64333):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", r".", delete_extraneous_files=True, prog_num=64334) as copy_dir_to_dir_1133_64334:
                            copy_dir_to_dir_1133_64334()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Q-Clone.bundle", where_to_unwtar=r".", prog_num=64335) as unwtar_1134_64335:
                            unwtar_1134_64335()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Q-Clone.bundle", user_id=-1, group_id=-1, prog_num=64336, recursive=True) as chown_1135_64336:
                            chown_1135_64336()
            with Stage(r"copy", r"R360 v16.0.23.24", prog_num=64337):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64338) as should_copy_source_1136_64338:
                    should_copy_source_1136_64338()
                    with Stage(r"copy source", r"Mac/Plugins/R360.bundle", prog_num=64339):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", r".", delete_extraneous_files=True, prog_num=64340) as copy_dir_to_dir_1137_64340:
                            copy_dir_to_dir_1137_64340()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/R360.bundle", where_to_unwtar=r".", prog_num=64341) as unwtar_1138_64341:
                            unwtar_1138_64341()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/R360.bundle", user_id=-1, group_id=-1, prog_num=64342, recursive=True) as chown_1139_64342:
                            chown_1139_64342()
            with Stage(r"copy", r"RBass v16.0.23.24", prog_num=64343):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64344) as should_copy_source_1140_64344:
                    should_copy_source_1140_64344()
                    with Stage(r"copy source", r"Mac/Plugins/RBass.bundle", prog_num=64345):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", r".", delete_extraneous_files=True, prog_num=64346) as copy_dir_to_dir_1141_64346:
                            copy_dir_to_dir_1141_64346()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RBass.bundle", where_to_unwtar=r".", prog_num=64347) as unwtar_1142_64347:
                            unwtar_1142_64347()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RBass.bundle", user_id=-1, group_id=-1, prog_num=64348, recursive=True) as chown_1143_64348:
                            chown_1143_64348()
            with Stage(r"copy", r"RChannel v16.0.23.24", prog_num=64349):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64350) as should_copy_source_1144_64350:
                    should_copy_source_1144_64350()
                    with Stage(r"copy source", r"Mac/Plugins/RChannel.bundle", prog_num=64351):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", r".", delete_extraneous_files=True, prog_num=64352) as copy_dir_to_dir_1145_64352:
                            copy_dir_to_dir_1145_64352()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RChannel.bundle", where_to_unwtar=r".", prog_num=64353) as unwtar_1146_64353:
                            unwtar_1146_64353()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RChannel.bundle", user_id=-1, group_id=-1, prog_num=64354, recursive=True) as chown_1147_64354:
                            chown_1147_64354()
            with Stage(r"copy", r"RComp v16.0.23.24", prog_num=64355):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64356) as should_copy_source_1148_64356:
                    should_copy_source_1148_64356()
                    with Stage(r"copy source", r"Mac/Plugins/RComp.bundle", prog_num=64357):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", r".", delete_extraneous_files=True, prog_num=64358) as copy_dir_to_dir_1149_64358:
                            copy_dir_to_dir_1149_64358()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RComp.bundle", where_to_unwtar=r".", prog_num=64359) as unwtar_1150_64359:
                            unwtar_1150_64359()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RComp.bundle", user_id=-1, group_id=-1, prog_num=64360, recursive=True) as chown_1151_64360:
                            chown_1151_64360()
            with Stage(r"copy", r"RDeEsser v16.0.23.24", prog_num=64361):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64362) as should_copy_source_1152_64362:
                    should_copy_source_1152_64362()
                    with Stage(r"copy source", r"Mac/Plugins/RDeEsser.bundle", prog_num=64363):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", r".", delete_extraneous_files=True, prog_num=64364) as copy_dir_to_dir_1153_64364:
                            copy_dir_to_dir_1153_64364()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RDeEsser.bundle", where_to_unwtar=r".", prog_num=64365) as unwtar_1154_64365:
                            unwtar_1154_64365()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RDeEsser.bundle", user_id=-1, group_id=-1, prog_num=64366, recursive=True) as chown_1155_64366:
                            chown_1155_64366()
            with Stage(r"copy", r"REDD17 v16.0.23.24", prog_num=64367):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64368) as should_copy_source_1156_64368:
                    should_copy_source_1156_64368()
                    with Stage(r"copy source", r"Mac/Plugins/REDD17.bundle", prog_num=64369):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", r".", delete_extraneous_files=True, prog_num=64370) as copy_dir_to_dir_1157_64370:
                            copy_dir_to_dir_1157_64370()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD17.bundle", where_to_unwtar=r".", prog_num=64371) as unwtar_1158_64371:
                            unwtar_1158_64371()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD17.bundle", user_id=-1, group_id=-1, prog_num=64372, recursive=True) as chown_1159_64372:
                            chown_1159_64372()
            with Stage(r"copy", r"REDD37-51 v16.0.23.24", prog_num=64373):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64374) as should_copy_source_1160_64374:
                    should_copy_source_1160_64374()
                    with Stage(r"copy source", r"Mac/Plugins/REDD37-51.bundle", prog_num=64375):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", r".", delete_extraneous_files=True, prog_num=64376) as copy_dir_to_dir_1161_64376:
                            copy_dir_to_dir_1161_64376()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REDD37-51.bundle", where_to_unwtar=r".", prog_num=64377) as unwtar_1162_64377:
                            unwtar_1162_64377()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REDD37-51.bundle", user_id=-1, group_id=-1, prog_num=64378, recursive=True) as chown_1163_64378:
                            chown_1163_64378()
            with Stage(r"copy", r"REQ v16.0.23.24", prog_num=64379):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64380) as should_copy_source_1164_64380:
                    should_copy_source_1164_64380()
                    with Stage(r"copy source", r"Mac/Plugins/REQ.bundle", prog_num=64381):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", r".", delete_extraneous_files=True, prog_num=64382) as copy_dir_to_dir_1165_64382:
                            copy_dir_to_dir_1165_64382()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/REQ.bundle", where_to_unwtar=r".", prog_num=64383) as unwtar_1166_64383:
                            unwtar_1166_64383()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/REQ.bundle", user_id=-1, group_id=-1, prog_num=64384, recursive=True) as chown_1167_64384:
                            chown_1167_64384()
            with Stage(r"copy", r"RS56 v16.0.23.24", prog_num=64385):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64386) as should_copy_source_1168_64386:
                    should_copy_source_1168_64386()
                    with Stage(r"copy source", r"Mac/Plugins/RS56.bundle", prog_num=64387):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", r".", delete_extraneous_files=True, prog_num=64388) as copy_dir_to_dir_1169_64388:
                            copy_dir_to_dir_1169_64388()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RS56.bundle", where_to_unwtar=r".", prog_num=64389) as unwtar_1170_64389:
                            unwtar_1170_64389()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RS56.bundle", user_id=-1, group_id=-1, prog_num=64390, recursive=True) as chown_1171_64390:
                            chown_1171_64390()
            with Stage(r"copy", r"RVerb v16.0.23.24", prog_num=64391):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64392) as should_copy_source_1172_64392:
                    should_copy_source_1172_64392()
                    with Stage(r"copy source", r"Mac/Plugins/RVerb.bundle", prog_num=64393):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", r".", delete_extraneous_files=True, prog_num=64394) as copy_dir_to_dir_1173_64394:
                            copy_dir_to_dir_1173_64394()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVerb.bundle", where_to_unwtar=r".", prog_num=64395) as unwtar_1174_64395:
                            unwtar_1174_64395()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVerb.bundle", user_id=-1, group_id=-1, prog_num=64396, recursive=True) as chown_1175_64396:
                            chown_1175_64396()
            with Stage(r"copy", r"RVox v16.0.23.24", prog_num=64397):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64398) as should_copy_source_1176_64398:
                    should_copy_source_1176_64398()
                    with Stage(r"copy source", r"Mac/Plugins/RVox.bundle", prog_num=64399):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", r".", delete_extraneous_files=True, prog_num=64400) as copy_dir_to_dir_1177_64400:
                            copy_dir_to_dir_1177_64400()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RVox.bundle", where_to_unwtar=r".", prog_num=64401) as unwtar_1178_64401:
                            unwtar_1178_64401()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RVox.bundle", user_id=-1, group_id=-1, prog_num=64402, recursive=True) as chown_1179_64402:
                            chown_1179_64402()
            with Stage(r"copy", r"Reel ADT v16.0.23.24", prog_num=64403):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64404) as should_copy_source_1180_64404:
                    should_copy_source_1180_64404()
                    with Stage(r"copy source", r"Mac/Plugins/Reel ADT.bundle", prog_num=64405):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", r".", delete_extraneous_files=True, prog_num=64406) as copy_dir_to_dir_1181_64406:
                            copy_dir_to_dir_1181_64406()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Reel ADT.bundle", where_to_unwtar=r".", prog_num=64407) as unwtar_1182_64407:
                            unwtar_1182_64407()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Reel ADT.bundle", user_id=-1, group_id=-1, prog_num=64408, recursive=True) as chown_1183_64408:
                            chown_1183_64408()
            with Stage(r"copy", r"RenAxx v16.0.23.24", prog_num=64409):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64410) as should_copy_source_1184_64410:
                    should_copy_source_1184_64410()
                    with Stage(r"copy source", r"Mac/Plugins/RenAxx.bundle", prog_num=64411):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", r".", delete_extraneous_files=True, prog_num=64412) as copy_dir_to_dir_1185_64412:
                            copy_dir_to_dir_1185_64412()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/RenAxx.bundle", where_to_unwtar=r".", prog_num=64413) as unwtar_1186_64413:
                            unwtar_1186_64413()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/RenAxx.bundle", user_id=-1, group_id=-1, prog_num=64414, recursive=True) as chown_1187_64414:
                            chown_1187_64414()
            with Stage(r"copy", r"Retro Fi v16.0.23.24", prog_num=64415):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64416) as should_copy_source_1188_64416:
                    should_copy_source_1188_64416()
                    with Stage(r"copy source", r"Mac/Plugins/Retro Fi.bundle", prog_num=64417):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", r".", delete_extraneous_files=True, prog_num=64418) as copy_dir_to_dir_1189_64418:
                            copy_dir_to_dir_1189_64418()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Retro Fi.bundle", where_to_unwtar=r".", prog_num=64419) as unwtar_1190_64419:
                            unwtar_1190_64419()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Retro Fi.bundle", user_id=-1, group_id=-1, prog_num=64420, recursive=True) as chown_1191_64420:
                            chown_1191_64420()
            with Stage(r"copy", r"S1 v16.0.23.24", prog_num=64421):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64422) as should_copy_source_1192_64422:
                    should_copy_source_1192_64422()
                    with Stage(r"copy source", r"Mac/Plugins/S1.bundle", prog_num=64423):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", r".", delete_extraneous_files=True, prog_num=64424) as copy_dir_to_dir_1193_64424:
                            copy_dir_to_dir_1193_64424()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S1.bundle", where_to_unwtar=r".", prog_num=64425) as unwtar_1194_64425:
                            unwtar_1194_64425()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S1.bundle", user_id=-1, group_id=-1, prog_num=64426, recursive=True) as chown_1195_64426:
                            chown_1195_64426()
            with Stage(r"copy", r"S360 v16.0.23.24", prog_num=64427):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64428) as should_copy_source_1196_64428:
                    should_copy_source_1196_64428()
                    with Stage(r"copy source", r"Mac/Plugins/S360.bundle", prog_num=64429):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", r".", delete_extraneous_files=True, prog_num=64430) as copy_dir_to_dir_1197_64430:
                            copy_dir_to_dir_1197_64430()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/S360.bundle", where_to_unwtar=r".", prog_num=64431) as unwtar_1198_64431:
                            unwtar_1198_64431()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/S360.bundle", user_id=-1, group_id=-1, prog_num=64432, recursive=True) as chown_1199_64432:
                            chown_1199_64432()
            with Stage(r"copy", r"SSL E-Channel v16.0.23.24", prog_num=64433):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64434) as should_copy_source_1200_64434:
                    should_copy_source_1200_64434()
                    with Stage(r"copy source", r"Mac/Plugins/SSL E-Channel.bundle", prog_num=64435):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", r".", delete_extraneous_files=True, prog_num=64436) as copy_dir_to_dir_1201_64436:
                            copy_dir_to_dir_1201_64436()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL E-Channel.bundle", where_to_unwtar=r".", prog_num=64437) as unwtar_1202_64437:
                            unwtar_1202_64437()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL E-Channel.bundle", user_id=-1, group_id=-1, prog_num=64438, recursive=True) as chown_1203_64438:
                            chown_1203_64438()
            with Stage(r"copy", r"SSLComp v16.0.23.24", prog_num=64439):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64440) as should_copy_source_1204_64440:
                    should_copy_source_1204_64440()
                    with Stage(r"copy source", r"Mac/Plugins/SSLComp.bundle", prog_num=64441):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", r".", delete_extraneous_files=True, prog_num=64442) as copy_dir_to_dir_1205_64442:
                            copy_dir_to_dir_1205_64442()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLComp.bundle", where_to_unwtar=r".", prog_num=64443) as unwtar_1206_64443:
                            unwtar_1206_64443()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSLComp.bundle", user_id=-1, group_id=-1, prog_num=64444, recursive=True) as chown_1207_64444:
                            chown_1207_64444()
            with Stage(r"copy", r"SSLEQ v16.0.23.24", prog_num=64445):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64446) as should_copy_source_1208_64446:
                    should_copy_source_1208_64446()
                    with Stage(r"copy source", r"Mac/Plugins/SSLEQ.bundle", prog_num=64447):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", r".", delete_extraneous_files=True, prog_num=64448) as copy_dir_to_dir_1209_64448:
                            copy_dir_to_dir_1209_64448()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSLEQ.bundle", where_to_unwtar=r".", prog_num=64449) as unwtar_1210_64449:
                            unwtar_1210_64449()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSLEQ.bundle", user_id=-1, group_id=-1, prog_num=64450, recursive=True) as chown_1211_64450:
                            chown_1211_64450()
            with Stage(r"copy", r"SSL EV2 Channel v16.0.23.24", prog_num=64451):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64452) as should_copy_source_1212_64452:
                    should_copy_source_1212_64452()
                    with Stage(r"copy source", r"Mac/Plugins/SSL EV2 Channel.bundle", prog_num=64453):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", r".", delete_extraneous_files=True, prog_num=64454) as copy_dir_to_dir_1213_64454:
                            copy_dir_to_dir_1213_64454()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL EV2 Channel.bundle", where_to_unwtar=r".", prog_num=64455) as unwtar_1214_64455:
                            unwtar_1214_64455()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL EV2 Channel.bundle", user_id=-1, group_id=-1, prog_num=64456, recursive=True) as chown_1215_64456:
                            chown_1215_64456()
            with Stage(r"copy", r"SSL G-Channel v16.0.23.24", prog_num=64457):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64458) as should_copy_source_1216_64458:
                    should_copy_source_1216_64458()
                    with Stage(r"copy source", r"Mac/Plugins/SSL G-Channel.bundle", prog_num=64459):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", r".", delete_extraneous_files=True, prog_num=64460) as copy_dir_to_dir_1217_64460:
                            copy_dir_to_dir_1217_64460()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SSL G-Channel.bundle", where_to_unwtar=r".", prog_num=64461) as unwtar_1218_64461:
                            unwtar_1218_64461()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SSL G-Channel.bundle", user_id=-1, group_id=-1, prog_num=64462, recursive=True) as chown_1219_64462:
                            chown_1219_64462()
            with Stage(r"copy", r"Scheps 73 v16.0.23.24", prog_num=64463):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64464) as should_copy_source_1220_64464:
                    should_copy_source_1220_64464()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps 73.bundle", prog_num=64465):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", r".", delete_extraneous_files=True, prog_num=64466) as copy_dir_to_dir_1221_64466:
                            copy_dir_to_dir_1221_64466()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps 73.bundle", where_to_unwtar=r".", prog_num=64467) as unwtar_1222_64467:
                            unwtar_1222_64467()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps 73.bundle", user_id=-1, group_id=-1, prog_num=64468, recursive=True) as chown_1223_64468:
                            chown_1223_64468()
            with Stage(r"copy", r"Scheps Omni Channel v16.0.30.31", prog_num=64469):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64470) as should_copy_source_1224_64470:
                    should_copy_source_1224_64470()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Omni Channel.bundle", prog_num=64471):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", r".", delete_extraneous_files=True, prog_num=64472) as copy_dir_to_dir_1225_64472:
                            copy_dir_to_dir_1225_64472()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Omni Channel.bundle", where_to_unwtar=r".", prog_num=64473) as unwtar_1226_64473:
                            unwtar_1226_64473()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Omni Channel.bundle", user_id=-1, group_id=-1, prog_num=64474, recursive=True) as chown_1227_64474:
                            chown_1227_64474()
            with Stage(r"copy", r"Scheps Parallel Particles v16.0.23.24", prog_num=64475):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64476) as should_copy_source_1228_64476:
                    should_copy_source_1228_64476()
                    with Stage(r"copy source", r"Mac/Plugins/Scheps Parallel Particles.bundle", prog_num=64477):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", r".", delete_extraneous_files=True, prog_num=64478) as copy_dir_to_dir_1229_64478:
                            copy_dir_to_dir_1229_64478()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Scheps Parallel Particles.bundle", where_to_unwtar=r".", prog_num=64479) as unwtar_1230_64479:
                            unwtar_1230_64479()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Scheps Parallel Particles.bundle", user_id=-1, group_id=-1, prog_num=64480, recursive=True) as chown_1231_64480:
                            chown_1231_64480()
            with Stage(r"copy", r"Sibilance v16.0.23.24", prog_num=64481):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64482) as should_copy_source_1232_64482:
                    should_copy_source_1232_64482()
                    with Stage(r"copy source", r"Mac/Plugins/Sibilance.bundle", prog_num=64483):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", r".", delete_extraneous_files=True, prog_num=64484) as copy_dir_to_dir_1233_64484:
                            copy_dir_to_dir_1233_64484()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sibilance.bundle", where_to_unwtar=r".", prog_num=64485) as unwtar_1234_64485:
                            unwtar_1234_64485()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sibilance.bundle", user_id=-1, group_id=-1, prog_num=64486, recursive=True) as chown_1235_64486:
                            chown_1235_64486()
            with Stage(r"copy", r"Emo Signal Generator v16.0.23.24", prog_num=64487):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64488) as should_copy_source_1236_64488:
                    should_copy_source_1236_64488()
                    with Stage(r"copy source", r"Mac/Plugins/SignalGenerator.bundle", prog_num=64489):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", r".", delete_extraneous_files=True, prog_num=64490) as copy_dir_to_dir_1237_64490:
                            copy_dir_to_dir_1237_64490()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SignalGenerator.bundle", where_to_unwtar=r".", prog_num=64491) as unwtar_1238_64491:
                            unwtar_1238_64491()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SignalGenerator.bundle", user_id=-1, group_id=-1, prog_num=64492, recursive=True) as chown_1239_64492:
                            chown_1239_64492()
            with Stage(r"copy", r"Silk Vocal v16.0.23.24", prog_num=64493):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64494) as should_copy_source_1240_64494:
                    should_copy_source_1240_64494()
                    with Stage(r"copy source", r"Mac/Plugins/Silk Vocal.bundle", prog_num=64495):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", r".", delete_extraneous_files=True, prog_num=64496) as copy_dir_to_dir_1241_64496:
                            copy_dir_to_dir_1241_64496()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Silk Vocal.bundle", where_to_unwtar=r".", prog_num=64497) as unwtar_1242_64497:
                            unwtar_1242_64497()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Silk Vocal.bundle", user_id=-1, group_id=-1, prog_num=64498, recursive=True) as chown_1243_64498:
                            chown_1243_64498()
            with Stage(r"copy", r"Smack Attack v16.0.23.24", prog_num=64499):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64500) as should_copy_source_1244_64500:
                    should_copy_source_1244_64500()
                    with Stage(r"copy source", r"Mac/Plugins/Smack Attack.bundle", prog_num=64501):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", r".", delete_extraneous_files=True, prog_num=64502) as copy_dir_to_dir_1245_64502:
                            copy_dir_to_dir_1245_64502()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Smack Attack.bundle", where_to_unwtar=r".", prog_num=64503) as unwtar_1246_64503:
                            unwtar_1246_64503()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Smack Attack.bundle", user_id=-1, group_id=-1, prog_num=64504, recursive=True) as chown_1247_64504:
                            chown_1247_64504()
            with Stage(r"copy", r"SoundShifter v16.0.23.24", prog_num=64505):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64506) as should_copy_source_1248_64506:
                    should_copy_source_1248_64506()
                    with Stage(r"copy source", r"Mac/Plugins/SoundShifter.bundle", prog_num=64507):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", r".", delete_extraneous_files=True, prog_num=64508) as copy_dir_to_dir_1249_64508:
                            copy_dir_to_dir_1249_64508()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SoundShifter.bundle", where_to_unwtar=r".", prog_num=64509) as unwtar_1250_64509:
                            unwtar_1250_64509()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SoundShifter.bundle", user_id=-1, group_id=-1, prog_num=64510, recursive=True) as chown_1251_64510:
                            chown_1251_64510()
            with Stage(r"copy", r"Space Rider v16.0.23.24", prog_num=64511):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64512) as should_copy_source_1252_64512:
                    should_copy_source_1252_64512()
                    with Stage(r"copy source", r"Mac/Plugins/Space Rider.bundle", prog_num=64513):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", r".", delete_extraneous_files=True, prog_num=64514) as copy_dir_to_dir_1253_64514:
                            copy_dir_to_dir_1253_64514()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Space Rider.bundle", where_to_unwtar=r".", prog_num=64515) as unwtar_1254_64515:
                            unwtar_1254_64515()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Space Rider.bundle", user_id=-1, group_id=-1, prog_num=64516, recursive=True) as chown_1255_64516:
                            chown_1255_64516()
            with Stage(r"copy", r"Spherix Immersive Compressor v16.0.23.24", prog_num=64517):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64518) as should_copy_source_1256_64518:
                    should_copy_source_1256_64518()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Compressor.bundle", prog_num=64519):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", r".", delete_extraneous_files=True, prog_num=64520) as copy_dir_to_dir_1257_64520:
                            copy_dir_to_dir_1257_64520()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Compressor.bundle", where_to_unwtar=r".", prog_num=64521) as unwtar_1258_64521:
                            unwtar_1258_64521()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Compressor.bundle", user_id=-1, group_id=-1, prog_num=64522, recursive=True) as chown_1259_64522:
                            chown_1259_64522()
            with Stage(r"copy", r"Spherix Immersive Limiter v16.0.23.24", prog_num=64523):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64524) as should_copy_source_1260_64524:
                    should_copy_source_1260_64524()
                    with Stage(r"copy source", r"Mac/Plugins/Spherix Immersive Limiter.bundle", prog_num=64525):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", r".", delete_extraneous_files=True, prog_num=64526) as copy_dir_to_dir_1261_64526:
                            copy_dir_to_dir_1261_64526()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Spherix Immersive Limiter.bundle", where_to_unwtar=r".", prog_num=64527) as unwtar_1262_64527:
                            unwtar_1262_64527()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Spherix Immersive Limiter.bundle", user_id=-1, group_id=-1, prog_num=64528, recursive=True) as chown_1263_64528:
                            chown_1263_64528()
            with Stage(r"copy", r"StudioVerse Audio Effects v16.0.30.31", prog_num=64529):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64530) as should_copy_source_1264_64530:
                    should_copy_source_1264_64530()
                    with Stage(r"copy source", r"Mac/Plugins/StudioVerse Audio Effects.bundle", prog_num=64531):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", r".", delete_extraneous_files=True, prog_num=64532) as copy_dir_to_dir_1265_64532:
                            copy_dir_to_dir_1265_64532()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/StudioVerse Audio Effects.bundle", where_to_unwtar=r".", prog_num=64533) as unwtar_1266_64533:
                            unwtar_1266_64533()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/StudioVerse Audio Effects.bundle", user_id=-1, group_id=-1, prog_num=64534, recursive=True) as chown_1267_64534:
                            chown_1267_64534()
            with Stage(r"copy", r"Sub Align v16.0.23.24", prog_num=64535):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64536) as should_copy_source_1268_64536:
                    should_copy_source_1268_64536()
                    with Stage(r"copy source", r"Mac/Plugins/Sub Align.bundle", prog_num=64537):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", r".", delete_extraneous_files=True, prog_num=64538) as copy_dir_to_dir_1269_64538:
                            copy_dir_to_dir_1269_64538()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sub Align.bundle", where_to_unwtar=r".", prog_num=64539) as unwtar_1270_64539:
                            unwtar_1270_64539()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sub Align.bundle", user_id=-1, group_id=-1, prog_num=64540, recursive=True) as chown_1271_64540:
                            chown_1271_64540()
            with Stage(r"copy", r"SuperTap v16.0.23.24", prog_num=64541):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64542) as should_copy_source_1272_64542:
                    should_copy_source_1272_64542()
                    with Stage(r"copy source", r"Mac/Plugins/SuperTap.bundle", prog_num=64543):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", r".", delete_extraneous_files=True, prog_num=64544) as copy_dir_to_dir_1273_64544:
                            copy_dir_to_dir_1273_64544()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/SuperTap.bundle", where_to_unwtar=r".", prog_num=64545) as unwtar_1274_64545:
                            unwtar_1274_64545()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/SuperTap.bundle", user_id=-1, group_id=-1, prog_num=64546, recursive=True) as chown_1275_64546:
                            chown_1275_64546()
            with Stage(r"copy", r"Sync Vx v16.0.23.24", prog_num=64547):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64548) as should_copy_source_1276_64548:
                    should_copy_source_1276_64548()
                    with Stage(r"copy source", r"Mac/Plugins/Sync Vx.bundle", prog_num=64549):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", r".", delete_extraneous_files=True, prog_num=64550) as copy_dir_to_dir_1277_64550:
                            copy_dir_to_dir_1277_64550()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Sync Vx.bundle", where_to_unwtar=r".", prog_num=64551) as unwtar_1278_64551:
                            unwtar_1278_64551()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Sync Vx.bundle", user_id=-1, group_id=-1, prog_num=64552, recursive=True) as chown_1279_64552:
                            chown_1279_64552()
            with Stage(r"copy", r"TG12345 v16.0.23.24", prog_num=64553):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64554) as should_copy_source_1280_64554:
                    should_copy_source_1280_64554()
                    with Stage(r"copy source", r"Mac/Plugins/TG12345.bundle", prog_num=64555):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", r".", delete_extraneous_files=True, prog_num=64556) as copy_dir_to_dir_1281_64556:
                            copy_dir_to_dir_1281_64556()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TG12345.bundle", where_to_unwtar=r".", prog_num=64557) as unwtar_1282_64557:
                            unwtar_1282_64557()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TG12345.bundle", user_id=-1, group_id=-1, prog_num=64558, recursive=True) as chown_1283_64558:
                            chown_1283_64558()
            with Stage(r"copy", r"AR TG Meter Bridge v16.0.23.24", prog_num=64559):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64560) as should_copy_source_1284_64560:
                    should_copy_source_1284_64560()
                    with Stage(r"copy source", r"Mac/Plugins/AR TG Meter Bridge.bundle", prog_num=64561):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", r".", delete_extraneous_files=True, prog_num=64562) as copy_dir_to_dir_1285_64562:
                            copy_dir_to_dir_1285_64562()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/AR TG Meter Bridge.bundle", where_to_unwtar=r".", prog_num=64563) as unwtar_1286_64563:
                            unwtar_1286_64563()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/AR TG Meter Bridge.bundle", user_id=-1, group_id=-1, prog_num=64564, recursive=True) as chown_1287_64564:
                            chown_1287_64564()
            with Stage(r"copy", r"Abbey Road TG Mastering Chain v16.0.23.24", prog_num=64565):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64566) as should_copy_source_1288_64566:
                    should_copy_source_1288_64566()
                    with Stage(r"copy source", r"Mac/Plugins/Abbey Road TG Mastering Chain.bundle", prog_num=64567):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", r".", delete_extraneous_files=True, prog_num=64568) as copy_dir_to_dir_1289_64568:
                            copy_dir_to_dir_1289_64568()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Abbey Road TG Mastering Chain.bundle", where_to_unwtar=r".", prog_num=64569) as unwtar_1290_64569:
                            unwtar_1290_64569()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Abbey Road TG Mastering Chain.bundle", user_id=-1, group_id=-1, prog_num=64570, recursive=True) as chown_1291_64570:
                            chown_1291_64570()
            with Stage(r"copy", r"TRACT v16.0.23.24", prog_num=64571):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64572) as should_copy_source_1292_64572:
                    should_copy_source_1292_64572()
                    with Stage(r"copy source", r"Mac/Plugins/TRACT.bundle", prog_num=64573):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", r".", delete_extraneous_files=True, prog_num=64574) as copy_dir_to_dir_1293_64574:
                            copy_dir_to_dir_1293_64574()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TRACT.bundle", where_to_unwtar=r".", prog_num=64575) as unwtar_1294_64575:
                            unwtar_1294_64575()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TRACT.bundle", user_id=-1, group_id=-1, prog_num=64576, recursive=True) as chown_1295_64576:
                            chown_1295_64576()
            with Stage(r"copy", r"Torque v16.0.23.24", prog_num=64577):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64578) as should_copy_source_1296_64578:
                    should_copy_source_1296_64578()
                    with Stage(r"copy source", r"Mac/Plugins/Torque.bundle", prog_num=64579):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", r".", delete_extraneous_files=True, prog_num=64580) as copy_dir_to_dir_1297_64580:
                            copy_dir_to_dir_1297_64580()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Torque.bundle", where_to_unwtar=r".", prog_num=64581) as unwtar_1298_64581:
                            unwtar_1298_64581()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Torque.bundle", user_id=-1, group_id=-1, prog_num=64582, recursive=True) as chown_1299_64582:
                            chown_1299_64582()
            with Stage(r"copy", r"TransX v16.0.23.24", prog_num=64583):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64584) as should_copy_source_1300_64584:
                    should_copy_source_1300_64584()
                    with Stage(r"copy source", r"Mac/Plugins/TransX.bundle", prog_num=64585):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", r".", delete_extraneous_files=True, prog_num=64586) as copy_dir_to_dir_1301_64586:
                            copy_dir_to_dir_1301_64586()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TransX.bundle", where_to_unwtar=r".", prog_num=64587) as unwtar_1302_64587:
                            unwtar_1302_64587()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TransX.bundle", user_id=-1, group_id=-1, prog_num=64588, recursive=True) as chown_1303_64588:
                            chown_1303_64588()
            with Stage(r"copy", r"TrueVerb v16.0.23.24", prog_num=64589):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64590) as should_copy_source_1304_64590:
                    should_copy_source_1304_64590()
                    with Stage(r"copy source", r"Mac/Plugins/TrueVerb.bundle", prog_num=64591):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", r".", delete_extraneous_files=True, prog_num=64592) as copy_dir_to_dir_1305_64592:
                            copy_dir_to_dir_1305_64592()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/TrueVerb.bundle", where_to_unwtar=r".", prog_num=64593) as unwtar_1306_64593:
                            unwtar_1306_64593()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/TrueVerb.bundle", user_id=-1, group_id=-1, prog_num=64594, recursive=True) as chown_1307_64594:
                            chown_1307_64594()
            with Stage(r"copy", r"UM v16.0.23.24", prog_num=64595):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64596) as should_copy_source_1308_64596:
                    should_copy_source_1308_64596()
                    with Stage(r"copy source", r"Mac/Plugins/UM.bundle", prog_num=64597):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", r".", delete_extraneous_files=True, prog_num=64598) as copy_dir_to_dir_1309_64598:
                            copy_dir_to_dir_1309_64598()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UM.bundle", where_to_unwtar=r".", prog_num=64599) as unwtar_1310_64599:
                            unwtar_1310_64599()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UM.bundle", user_id=-1, group_id=-1, prog_num=64600, recursive=True) as chown_1311_64600:
                            chown_1311_64600()
            with Stage(r"copy", r"UltraPitch v16.0.23.24", prog_num=64601):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64602) as should_copy_source_1312_64602:
                    should_copy_source_1312_64602()
                    with Stage(r"copy source", r"Mac/Plugins/UltraPitch.bundle", prog_num=64603):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", r".", delete_extraneous_files=True, prog_num=64604) as copy_dir_to_dir_1313_64604:
                            copy_dir_to_dir_1313_64604()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/UltraPitch.bundle", where_to_unwtar=r".", prog_num=64605) as unwtar_1314_64605:
                            unwtar_1314_64605()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/UltraPitch.bundle", user_id=-1, group_id=-1, prog_num=64606, recursive=True) as chown_1315_64606:
                            chown_1315_64606()
            with Stage(r"copy", r"VComp v16.0.23.24", prog_num=64607):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64608) as should_copy_source_1316_64608:
                    should_copy_source_1316_64608()
                    with Stage(r"copy source", r"Mac/Plugins/VComp.bundle", prog_num=64609):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", r".", delete_extraneous_files=True, prog_num=64610) as copy_dir_to_dir_1317_64610:
                            copy_dir_to_dir_1317_64610()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VComp.bundle", where_to_unwtar=r".", prog_num=64611) as unwtar_1318_64611:
                            unwtar_1318_64611()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VComp.bundle", user_id=-1, group_id=-1, prog_num=64612, recursive=True) as chown_1319_64612:
                            chown_1319_64612()
            with Stage(r"copy", r"VEQ3 v16.0.23.24", prog_num=64613):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64614) as should_copy_source_1320_64614:
                    should_copy_source_1320_64614()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ3.bundle", prog_num=64615):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", r".", delete_extraneous_files=True, prog_num=64616) as copy_dir_to_dir_1321_64616:
                            copy_dir_to_dir_1321_64616()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ3.bundle", where_to_unwtar=r".", prog_num=64617) as unwtar_1322_64617:
                            unwtar_1322_64617()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ3.bundle", user_id=-1, group_id=-1, prog_num=64618, recursive=True) as chown_1323_64618:
                            chown_1323_64618()
            with Stage(r"copy", r"VEQ4 v16.0.23.24", prog_num=64619):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64620) as should_copy_source_1324_64620:
                    should_copy_source_1324_64620()
                    with Stage(r"copy source", r"Mac/Plugins/VEQ4.bundle", prog_num=64621):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", r".", delete_extraneous_files=True, prog_num=64622) as copy_dir_to_dir_1325_64622:
                            copy_dir_to_dir_1325_64622()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VEQ4.bundle", where_to_unwtar=r".", prog_num=64623) as unwtar_1326_64623:
                            unwtar_1326_64623()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VEQ4.bundle", user_id=-1, group_id=-1, prog_num=64624, recursive=True) as chown_1327_64624:
                            chown_1327_64624()
            with Stage(r"copy", r"VU Meter v16.0.23.24", prog_num=64625):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64626) as should_copy_source_1328_64626:
                    should_copy_source_1328_64626()
                    with Stage(r"copy source", r"Mac/Plugins/VU Meter.bundle", prog_num=64627):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", r".", delete_extraneous_files=True, prog_num=64628) as copy_dir_to_dir_1329_64628:
                            copy_dir_to_dir_1329_64628()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/VU Meter.bundle", where_to_unwtar=r".", prog_num=64629) as unwtar_1330_64629:
                            unwtar_1330_64629()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/VU Meter.bundle", user_id=-1, group_id=-1, prog_num=64630, recursive=True) as chown_1331_64630:
                            chown_1331_64630()
            with Stage(r"copy", r"Vitamin v16.0.23.24", prog_num=64631):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64632) as should_copy_source_1332_64632:
                    should_copy_source_1332_64632()
                    with Stage(r"copy source", r"Mac/Plugins/Vitamin.bundle", prog_num=64633):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", r".", delete_extraneous_files=True, prog_num=64634) as copy_dir_to_dir_1333_64634:
                            copy_dir_to_dir_1333_64634()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vitamin.bundle", where_to_unwtar=r".", prog_num=64635) as unwtar_1334_64635:
                            unwtar_1334_64635()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vitamin.bundle", user_id=-1, group_id=-1, prog_num=64636, recursive=True) as chown_1335_64636:
                            chown_1335_64636()
            with Stage(r"copy", r"Vocal Bender v16.0.23.24", prog_num=64637):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64638) as should_copy_source_1336_64638:
                    should_copy_source_1336_64638()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Bender.bundle", prog_num=64639):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", r".", delete_extraneous_files=True, prog_num=64640) as copy_dir_to_dir_1337_64640:
                            copy_dir_to_dir_1337_64640()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Bender.bundle", where_to_unwtar=r".", prog_num=64641) as unwtar_1338_64641:
                            unwtar_1338_64641()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Bender.bundle", user_id=-1, group_id=-1, prog_num=64642, recursive=True) as chown_1339_64642:
                            chown_1339_64642()
            with Stage(r"copy", r"Vocal Rider v16.0.23.24", prog_num=64643):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64644) as should_copy_source_1340_64644:
                    should_copy_source_1340_64644()
                    with Stage(r"copy source", r"Mac/Plugins/Vocal Rider.bundle", prog_num=64645):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", r".", delete_extraneous_files=True, prog_num=64646) as copy_dir_to_dir_1341_64646:
                            copy_dir_to_dir_1341_64646()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Vocal Rider.bundle", where_to_unwtar=r".", prog_num=64647) as unwtar_1342_64647:
                            unwtar_1342_64647()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Vocal Rider.bundle", user_id=-1, group_id=-1, prog_num=64648, recursive=True) as chown_1343_64648:
                            chown_1343_64648()
            with Stage(r"copy", r"Voltage Amps Bass v16.0.23.24", prog_num=64649):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64650) as should_copy_source_1344_64650:
                    should_copy_source_1344_64650()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Bass.bundle", prog_num=64651):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", r".", delete_extraneous_files=True, prog_num=64652) as copy_dir_to_dir_1345_64652:
                            copy_dir_to_dir_1345_64652()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Bass.bundle", where_to_unwtar=r".", prog_num=64653) as unwtar_1346_64653:
                            unwtar_1346_64653()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Bass.bundle", user_id=-1, group_id=-1, prog_num=64654, recursive=True) as chown_1347_64654:
                            chown_1347_64654()
            with Stage(r"copy", r"Voltage Amps Guitar v16.0.23.24", prog_num=64655):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64656) as should_copy_source_1348_64656:
                    should_copy_source_1348_64656()
                    with Stage(r"copy source", r"Mac/Plugins/Voltage Amps Guitar.bundle", prog_num=64657):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", r".", delete_extraneous_files=True, prog_num=64658) as copy_dir_to_dir_1349_64658:
                            copy_dir_to_dir_1349_64658()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Voltage Amps Guitar.bundle", where_to_unwtar=r".", prog_num=64659) as unwtar_1350_64659:
                            unwtar_1350_64659()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Voltage Amps Guitar.bundle", user_id=-1, group_id=-1, prog_num=64660, recursive=True) as chown_1351_64660:
                            chown_1351_64660()
            with Stage(r"copy", r"W43 v16.0.23.24", prog_num=64661):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64662) as should_copy_source_1352_64662:
                    should_copy_source_1352_64662()
                    with Stage(r"copy source", r"Mac/Plugins/W43.bundle", prog_num=64663):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", r".", delete_extraneous_files=True, prog_num=64664) as copy_dir_to_dir_1353_64664:
                            copy_dir_to_dir_1353_64664()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/W43.bundle", where_to_unwtar=r".", prog_num=64665) as unwtar_1354_64665:
                            unwtar_1354_64665()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/W43.bundle", user_id=-1, group_id=-1, prog_num=64666, recursive=True) as chown_1355_64666:
                            chown_1355_64666()
            with Stage(r"copy", r"WLM v16.0.23.24", prog_num=64667):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64668) as should_copy_source_1356_64668:
                    should_copy_source_1356_64668()
                    with Stage(r"copy source", r"Mac/Plugins/WLM.bundle", prog_num=64669):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", r".", delete_extraneous_files=True, prog_num=64670) as copy_dir_to_dir_1357_64670:
                            copy_dir_to_dir_1357_64670()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM.bundle", where_to_unwtar=r".", prog_num=64671) as unwtar_1358_64671:
                            unwtar_1358_64671()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM.bundle", user_id=-1, group_id=-1, prog_num=64672, recursive=True) as chown_1359_64672:
                            chown_1359_64672()
            with Stage(r"copy", r"WLM Plus v16.0.23.24", prog_num=64673):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64674) as should_copy_source_1360_64674:
                    should_copy_source_1360_64674()
                    with Stage(r"copy source", r"Mac/Plugins/WLM Plus.bundle", prog_num=64675):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", r".", delete_extraneous_files=True, prog_num=64676) as copy_dir_to_dir_1361_64676:
                            copy_dir_to_dir_1361_64676()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WLM Plus.bundle", where_to_unwtar=r".", prog_num=64677) as unwtar_1362_64677:
                            unwtar_1362_64677()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WLM Plus.bundle", user_id=-1, group_id=-1, prog_num=64678, recursive=True) as chown_1363_64678:
                            chown_1363_64678()
            with Stage(r"copy", r"WNS v16.0.23.24", prog_num=64679):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64680) as should_copy_source_1364_64680:
                    should_copy_source_1364_64680()
                    with Stage(r"copy source", r"Mac/Plugins/WNS.bundle", prog_num=64681):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", r".", delete_extraneous_files=True, prog_num=64682) as copy_dir_to_dir_1365_64682:
                            copy_dir_to_dir_1365_64682()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WNS.bundle", where_to_unwtar=r".", prog_num=64683) as unwtar_1366_64683:
                            unwtar_1366_64683()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WNS.bundle", user_id=-1, group_id=-1, prog_num=64684, recursive=True) as chown_1367_64684:
                            chown_1367_64684()
            with Stage(r"copy", r"WavesHeadTracker v16.0.23.24", prog_num=64685):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=5, prog_num=64686) as should_copy_source_1368_64686:
                    should_copy_source_1368_64686()
                    with Stage(r"copy source", r"Mac/Plugins/WavesHeadTracker", prog_num=64687):
                        with RmFileOrDir(r"WavesHeadTracker", prog_num=64688) as rm_file_or_dir_1369_64688:
                            rm_file_or_dir_1369_64688()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", r".", delete_extraneous_files=True, prog_num=64689) as copy_dir_to_dir_1370_64689:
                            copy_dir_to_dir_1370_64689()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesHeadTracker", where_to_unwtar=r".", prog_num=64690) as unwtar_1371_64690:
                            unwtar_1371_64690()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesHeadTracker", user_id=-1, group_id=-1, prog_num=64691, recursive=True) as chown_1372_64691:
                            chown_1372_64691()
            with Stage(r"copy", r"WavesLib1_16_0_23_24 v16.0.23.24", prog_num=64692):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64693) as should_copy_source_1373_64693:
                    should_copy_source_1373_64693()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.23.framework", prog_num=64694):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", r".", delete_extraneous_files=True, prog_num=64695) as copy_dir_to_dir_1374_64695:
                            copy_dir_to_dir_1374_64695()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.23.framework", where_to_unwtar=r".", prog_num=64696) as unwtar_1375_64696:
                            unwtar_1375_64696()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.23.framework", user_id=-1, group_id=-1, prog_num=64697, recursive=True) as chown_1376_64697:
                            chown_1376_64697()
            with Stage(r"copy", r"WavesLib1_16_0_30_31 v16.0.30.31", prog_num=64698):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64699) as should_copy_source_1377_64699:
                    should_copy_source_1377_64699()
                    with Stage(r"copy source", r"Mac/Plugins/WavesLib1_16.0.30.framework", prog_num=64700):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", r".", delete_extraneous_files=True, prog_num=64701) as copy_dir_to_dir_1378_64701:
                            copy_dir_to_dir_1378_64701()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesLib1_16.0.30.framework", where_to_unwtar=r".", prog_num=64702) as unwtar_1379_64702:
                            unwtar_1379_64702()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesLib1_16.0.30.framework", user_id=-1, group_id=-1, prog_num=64703, recursive=True) as chown_1380_64703:
                            chown_1380_64703()
            with Stage(r"copy", r"Waves Stream v16.0.23.24", prog_num=64704):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64705) as should_copy_source_1381_64705:
                    should_copy_source_1381_64705()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Stream.bundle", prog_num=64706):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", r".", delete_extraneous_files=True, prog_num=64707) as copy_dir_to_dir_1382_64707:
                            copy_dir_to_dir_1382_64707()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Stream.bundle", where_to_unwtar=r".", prog_num=64708) as unwtar_1383_64708:
                            unwtar_1383_64708()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Stream.bundle", user_id=-1, group_id=-1, prog_num=64709, recursive=True) as chown_1384_64709:
                            chown_1384_64709()
            with Stage(r"copy", r"WavesTune v16.0.23.24", prog_num=64710):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64711) as should_copy_source_1385_64711:
                    should_copy_source_1385_64711()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune.bundle", prog_num=64712):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", r".", delete_extraneous_files=True, prog_num=64713) as copy_dir_to_dir_1386_64713:
                            copy_dir_to_dir_1386_64713()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune.bundle", where_to_unwtar=r".", prog_num=64714) as unwtar_1387_64714:
                            unwtar_1387_64714()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune.bundle", user_id=-1, group_id=-1, prog_num=64715, recursive=True) as chown_1388_64715:
                            chown_1388_64715()
            with Stage(r"copy", r"WavesTune LT v16.0.23.24", prog_num=64716):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64717) as should_copy_source_1389_64717:
                    should_copy_source_1389_64717()
                    with Stage(r"copy source", r"Mac/Plugins/WavesTune LT.bundle", prog_num=64718):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", r".", delete_extraneous_files=True, prog_num=64719) as copy_dir_to_dir_1390_64719:
                            copy_dir_to_dir_1390_64719()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/WavesTune LT.bundle", where_to_unwtar=r".", prog_num=64720) as unwtar_1391_64720:
                            unwtar_1391_64720()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/WavesTune LT.bundle", user_id=-1, group_id=-1, prog_num=64721, recursive=True) as chown_1392_64721:
                            chown_1392_64721()
            with Stage(r"copy", r"Waves Harmony v16.0.23.24", prog_num=64722):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64723) as should_copy_source_1393_64723:
                    should_copy_source_1393_64723()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Harmony.bundle", prog_num=64724):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", r".", delete_extraneous_files=True, prog_num=64725) as copy_dir_to_dir_1394_64725:
                            copy_dir_to_dir_1394_64725()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Harmony.bundle", where_to_unwtar=r".", prog_num=64726) as unwtar_1395_64726:
                            unwtar_1395_64726()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Harmony.bundle", user_id=-1, group_id=-1, prog_num=64727, recursive=True) as chown_1396_64727:
                            chown_1396_64727()
            with Stage(r"copy", r"Waves Tune Real-Time v16.0.23.24", prog_num=64728):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64729) as should_copy_source_1397_64729:
                    should_copy_source_1397_64729()
                    with Stage(r"copy source", r"Mac/Plugins/Waves Tune Real-Time.bundle", prog_num=64730):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", r".", delete_extraneous_files=True, prog_num=64731) as copy_dir_to_dir_1398_64731:
                            copy_dir_to_dir_1398_64731()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Waves Tune Real-Time.bundle", where_to_unwtar=r".", prog_num=64732) as unwtar_1399_64732:
                            unwtar_1399_64732()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Waves Tune Real-Time.bundle", user_id=-1, group_id=-1, prog_num=64733, recursive=True) as chown_1400_64733:
                            chown_1400_64733()
            with Stage(r"copy", r"X-Click v16.0.23.24", prog_num=64734):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64735) as should_copy_source_1401_64735:
                    should_copy_source_1401_64735()
                    with Stage(r"copy source", r"Mac/Plugins/X-Click.bundle", prog_num=64736):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", r".", delete_extraneous_files=True, prog_num=64737) as copy_dir_to_dir_1402_64737:
                            copy_dir_to_dir_1402_64737()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Click.bundle", where_to_unwtar=r".", prog_num=64738) as unwtar_1403_64738:
                            unwtar_1403_64738()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Click.bundle", user_id=-1, group_id=-1, prog_num=64739, recursive=True) as chown_1404_64739:
                            chown_1404_64739()
            with Stage(r"copy", r"X-Crackle v16.0.23.24", prog_num=64740):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64741) as should_copy_source_1405_64741:
                    should_copy_source_1405_64741()
                    with Stage(r"copy source", r"Mac/Plugins/X-Crackle.bundle", prog_num=64742):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", r".", delete_extraneous_files=True, prog_num=64743) as copy_dir_to_dir_1406_64743:
                            copy_dir_to_dir_1406_64743()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Crackle.bundle", where_to_unwtar=r".", prog_num=64744) as unwtar_1407_64744:
                            unwtar_1407_64744()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Crackle.bundle", user_id=-1, group_id=-1, prog_num=64745, recursive=True) as chown_1408_64745:
                            chown_1408_64745()
            with Stage(r"copy", r"X-FDBK v16.0.23.24", prog_num=64746):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64747) as should_copy_source_1409_64747:
                    should_copy_source_1409_64747()
                    with Stage(r"copy source", r"Mac/Plugins/X-FDBK.bundle", prog_num=64748):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", r".", delete_extraneous_files=True, prog_num=64749) as copy_dir_to_dir_1410_64749:
                            copy_dir_to_dir_1410_64749()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-FDBK.bundle", where_to_unwtar=r".", prog_num=64750) as unwtar_1411_64750:
                            unwtar_1411_64750()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-FDBK.bundle", user_id=-1, group_id=-1, prog_num=64751, recursive=True) as chown_1412_64751:
                            chown_1412_64751()
            with Stage(r"copy", r"X-Hum v16.0.23.24", prog_num=64752):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64753) as should_copy_source_1413_64753:
                    should_copy_source_1413_64753()
                    with Stage(r"copy source", r"Mac/Plugins/X-Hum.bundle", prog_num=64754):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", r".", delete_extraneous_files=True, prog_num=64755) as copy_dir_to_dir_1414_64755:
                            copy_dir_to_dir_1414_64755()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Hum.bundle", where_to_unwtar=r".", prog_num=64756) as unwtar_1415_64756:
                            unwtar_1415_64756()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Hum.bundle", user_id=-1, group_id=-1, prog_num=64757, recursive=True) as chown_1416_64757:
                            chown_1416_64757()
            with Stage(r"copy", r"X-Noise v16.0.23.24", prog_num=64758):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64759) as should_copy_source_1417_64759:
                    should_copy_source_1417_64759()
                    with Stage(r"copy source", r"Mac/Plugins/X-Noise.bundle", prog_num=64760):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", r".", delete_extraneous_files=True, prog_num=64761) as copy_dir_to_dir_1418_64761:
                            copy_dir_to_dir_1418_64761()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/X-Noise.bundle", where_to_unwtar=r".", prog_num=64762) as unwtar_1419_64762:
                            unwtar_1419_64762()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/X-Noise.bundle", user_id=-1, group_id=-1, prog_num=64763, recursive=True) as chown_1420_64763:
                            chown_1420_64763()
            with Stage(r"copy", r"Z-Noise v16.0.23.24", prog_num=64764):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64765) as should_copy_source_1421_64765:
                    should_copy_source_1421_64765()
                    with Stage(r"copy source", r"Mac/Plugins/Z-Noise.bundle", prog_num=64766):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", r".", delete_extraneous_files=True, prog_num=64767) as copy_dir_to_dir_1422_64767:
                            copy_dir_to_dir_1422_64767()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/Z-Noise.bundle", where_to_unwtar=r".", prog_num=64768) as unwtar_1423_64768:
                            unwtar_1423_64768()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/Z-Noise.bundle", user_id=-1, group_id=-1, prog_num=64769, recursive=True) as chown_1424_64769:
                            chown_1424_64769()
            with Stage(r"copy", r"dbx-160 v16.0.23.24", prog_num=64770):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", r"/Applications/Waves/Plug-Ins V16", skip_progress_count=4, prog_num=64771) as should_copy_source_1425_64771:
                    should_copy_source_1425_64771()
                    with Stage(r"copy source", r"Mac/Plugins/dbx-160.bundle", prog_num=64772):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", r".", delete_extraneous_files=True, prog_num=64773) as copy_dir_to_dir_1426_64773:
                            copy_dir_to_dir_1426_64773()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/dbx-160.bundle", where_to_unwtar=r".", prog_num=64774) as unwtar_1427_64774:
                            unwtar_1427_64774()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/dbx-160.bundle", user_id=-1, group_id=-1, prog_num=64775, recursive=True) as chown_1428_64775:
                            chown_1428_64775()
            with ResolveSymlinkFilesInFolder(r"/Applications/Waves/Plug-Ins V16", own_progress_count=4, prog_num=64779) as resolve_symlink_files_in_folder_1429_64779:
                resolve_symlink_files_in_folder_1429_64779()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Plug-Ins V16" -c', ignore_all_errors=True, prog_num=64780) as shell_command_1430_64780:
                shell_command_1430_64780()
            with ScriptCommand(r'if [ -f "/Applications/Waves/Plug-Ins V16"/Icon? ]; then chmod a+rw "/Applications/Waves/Plug-Ins V16"/Icon?; fi', prog_num=64781) as script_command_1431_64781:
                script_command_1431_64781()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64782) as shell_command_1432_64782:
                shell_command_1432_64782()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=64783) as create_symlink_1433_64783:
                create_symlink_1433_64783()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins V16", r"/Applications/Waves/Plug-Ins V16", prog_num=64784) as create_symlink_1434_64784:
                create_symlink_1434_64784()
            with CopyGlobToDir(r"*/*/*/*.pdf", r".", r"./Documents", prog_num=64785) as copy_glob_to_dir_1435_64785:
                copy_glob_to_dir_1435_64785()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/Documents", prog_num=64786) as cd_stage_1436_64786:
            cd_stage_1436_64786()
            with Stage(r"copy", r"Plugins Documents Folder", prog_num=64787):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r"/Applications/Waves/Plug-Ins V16/Documents", skip_progress_count=3, prog_num=64788) as should_copy_source_1437_64788:
                    should_copy_source_1437_64788()
                    with Stage(r"copy source", r"Common/Plugins/Documents/Waves System Guide.pdf", prog_num=64789):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Plugins/Documents/Waves System Guide.pdf", r".", prog_num=64790) as copy_file_to_dir_1438_64790:
                            copy_file_to_dir_1438_64790()
                        with ChmodAndChown(path=r"Waves System Guide.pdf", mode="a+rw", user_id=-1, group_id=-1, prog_num=64791) as chmod_and_chown_1439_64791:
                            chmod_and_chown_1439_64791()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTR", prog_num=64792) as cd_stage_1440_64792:
            cd_stage_1440_64792()
            with Stage(r"copy", r"GTR Stomps v16.0.23.24", prog_num=64793):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64794) as should_copy_source_1441_64794:
                    should_copy_source_1441_64794()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompAxxPress.bundle", prog_num=64795):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", r".", delete_extraneous_files=True, prog_num=64796) as copy_dir_to_dir_1442_64796:
                            copy_dir_to_dir_1442_64796()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompAxxPress.bundle", where_to_unwtar=r".", prog_num=64797) as unwtar_1443_64797:
                            unwtar_1443_64797()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompAxxPress.bundle", user_id=-1, group_id=-1, prog_num=64798, recursive=True) as chown_1444_64798:
                            chown_1444_64798()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64799) as should_copy_source_1445_64799:
                    should_copy_source_1445_64799()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompBuzz.bundle", prog_num=64800):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", r".", delete_extraneous_files=True, prog_num=64801) as copy_dir_to_dir_1446_64801:
                            copy_dir_to_dir_1446_64801()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompBuzz.bundle", where_to_unwtar=r".", prog_num=64802) as unwtar_1447_64802:
                            unwtar_1447_64802()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompBuzz.bundle", user_id=-1, group_id=-1, prog_num=64803, recursive=True) as chown_1448_64803:
                            chown_1448_64803()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64804) as should_copy_source_1449_64804:
                    should_copy_source_1449_64804()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompChorus.bundle", prog_num=64805):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", r".", delete_extraneous_files=True, prog_num=64806) as copy_dir_to_dir_1450_64806:
                            copy_dir_to_dir_1450_64806()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompChorus.bundle", where_to_unwtar=r".", prog_num=64807) as unwtar_1451_64807:
                            unwtar_1451_64807()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompChorus.bundle", user_id=-1, group_id=-1, prog_num=64808, recursive=True) as chown_1452_64808:
                            chown_1452_64808()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64809) as should_copy_source_1453_64809:
                    should_copy_source_1453_64809()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompComp.bundle", prog_num=64810):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", r".", delete_extraneous_files=True, prog_num=64811) as copy_dir_to_dir_1454_64811:
                            copy_dir_to_dir_1454_64811()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompComp.bundle", where_to_unwtar=r".", prog_num=64812) as unwtar_1455_64812:
                            unwtar_1455_64812()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompComp.bundle", user_id=-1, group_id=-1, prog_num=64813, recursive=True) as chown_1456_64813:
                            chown_1456_64813()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64814) as should_copy_source_1457_64814:
                    should_copy_source_1457_64814()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDelay.bundle", prog_num=64815):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", r".", delete_extraneous_files=True, prog_num=64816) as copy_dir_to_dir_1458_64816:
                            copy_dir_to_dir_1458_64816()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDelay.bundle", where_to_unwtar=r".", prog_num=64817) as unwtar_1459_64817:
                            unwtar_1459_64817()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDelay.bundle", user_id=-1, group_id=-1, prog_num=64818, recursive=True) as chown_1460_64818:
                            chown_1460_64818()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64819) as should_copy_source_1461_64819:
                    should_copy_source_1461_64819()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDistortion.bundle", prog_num=64820):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", r".", delete_extraneous_files=True, prog_num=64821) as copy_dir_to_dir_1462_64821:
                            copy_dir_to_dir_1462_64821()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDistortion.bundle", where_to_unwtar=r".", prog_num=64822) as unwtar_1463_64822:
                            unwtar_1463_64822()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDistortion.bundle", user_id=-1, group_id=-1, prog_num=64823, recursive=True) as chown_1464_64823:
                            chown_1464_64823()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64824) as should_copy_source_1465_64824:
                    should_copy_source_1465_64824()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompDoubler.bundle", prog_num=64825):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", r".", delete_extraneous_files=True, prog_num=64826) as copy_dir_to_dir_1466_64826:
                            copy_dir_to_dir_1466_64826()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompDoubler.bundle", where_to_unwtar=r".", prog_num=64827) as unwtar_1467_64827:
                            unwtar_1467_64827()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompDoubler.bundle", user_id=-1, group_id=-1, prog_num=64828, recursive=True) as chown_1468_64828:
                            chown_1468_64828()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64829) as should_copy_source_1469_64829:
                    should_copy_source_1469_64829()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompEQ.bundle", prog_num=64830):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", r".", delete_extraneous_files=True, prog_num=64831) as copy_dir_to_dir_1470_64831:
                            copy_dir_to_dir_1470_64831()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompEQ.bundle", where_to_unwtar=r".", prog_num=64832) as unwtar_1471_64832:
                            unwtar_1471_64832()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompEQ.bundle", user_id=-1, group_id=-1, prog_num=64833, recursive=True) as chown_1472_64833:
                            chown_1472_64833()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64834) as should_copy_source_1473_64834:
                    should_copy_source_1473_64834()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFlanger.bundle", prog_num=64835):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64836) as copy_dir_to_dir_1474_64836:
                            copy_dir_to_dir_1474_64836()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFlanger.bundle", where_to_unwtar=r".", prog_num=64837) as unwtar_1475_64837:
                            unwtar_1475_64837()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFlanger.bundle", user_id=-1, group_id=-1, prog_num=64838, recursive=True) as chown_1476_64838:
                            chown_1476_64838()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64839) as should_copy_source_1477_64839:
                    should_copy_source_1477_64839()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompFuzz.bundle", prog_num=64840):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", r".", delete_extraneous_files=True, prog_num=64841) as copy_dir_to_dir_1478_64841:
                            copy_dir_to_dir_1478_64841()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompFuzz.bundle", where_to_unwtar=r".", prog_num=64842) as unwtar_1479_64842:
                            unwtar_1479_64842()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompFuzz.bundle", user_id=-1, group_id=-1, prog_num=64843, recursive=True) as chown_1480_64843:
                            chown_1480_64843()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64844) as should_copy_source_1481_64844:
                    should_copy_source_1481_64844()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGate.bundle", prog_num=64845):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", r".", delete_extraneous_files=True, prog_num=64846) as copy_dir_to_dir_1482_64846:
                            copy_dir_to_dir_1482_64846()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGate.bundle", where_to_unwtar=r".", prog_num=64847) as unwtar_1483_64847:
                            unwtar_1483_64847()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGate.bundle", user_id=-1, group_id=-1, prog_num=64848, recursive=True) as chown_1484_64848:
                            chown_1484_64848()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64849) as should_copy_source_1485_64849:
                    should_copy_source_1485_64849()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompGateComp.bundle", prog_num=64850):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", r".", delete_extraneous_files=True, prog_num=64851) as copy_dir_to_dir_1486_64851:
                            copy_dir_to_dir_1486_64851()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompGateComp.bundle", where_to_unwtar=r".", prog_num=64852) as unwtar_1487_64852:
                            unwtar_1487_64852()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompGateComp.bundle", user_id=-1, group_id=-1, prog_num=64853, recursive=True) as chown_1488_64853:
                            chown_1488_64853()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64854) as should_copy_source_1489_64854:
                    should_copy_source_1489_64854()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompLayD.bundle", prog_num=64855):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", r".", delete_extraneous_files=True, prog_num=64856) as copy_dir_to_dir_1490_64856:
                            copy_dir_to_dir_1490_64856()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompLayD.bundle", where_to_unwtar=r".", prog_num=64857) as unwtar_1491_64857:
                            unwtar_1491_64857()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompLayD.bundle", user_id=-1, group_id=-1, prog_num=64858, recursive=True) as chown_1492_64858:
                            chown_1492_64858()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64859) as should_copy_source_1493_64859:
                    should_copy_source_1493_64859()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompMetal.bundle", prog_num=64860):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", r".", delete_extraneous_files=True, prog_num=64861) as copy_dir_to_dir_1494_64861:
                            copy_dir_to_dir_1494_64861()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompMetal.bundle", where_to_unwtar=r".", prog_num=64862) as unwtar_1495_64862:
                            unwtar_1495_64862()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompMetal.bundle", user_id=-1, group_id=-1, prog_num=64863, recursive=True) as chown_1496_64863:
                            chown_1496_64863()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64864) as should_copy_source_1497_64864:
                    should_copy_source_1497_64864()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOctaver.bundle", prog_num=64865):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", r".", delete_extraneous_files=True, prog_num=64866) as copy_dir_to_dir_1498_64866:
                            copy_dir_to_dir_1498_64866()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOctaver.bundle", where_to_unwtar=r".", prog_num=64867) as unwtar_1499_64867:
                            unwtar_1499_64867()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOctaver.bundle", user_id=-1, group_id=-1, prog_num=64868, recursive=True) as chown_1500_64868:
                            chown_1500_64868()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64869) as should_copy_source_1501_64869:
                    should_copy_source_1501_64869()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompOverDrive.bundle", prog_num=64870):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=64871) as copy_dir_to_dir_1502_64871:
                            copy_dir_to_dir_1502_64871()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompOverDrive.bundle", where_to_unwtar=r".", prog_num=64872) as unwtar_1503_64872:
                            unwtar_1503_64872()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompOverDrive.bundle", user_id=-1, group_id=-1, prog_num=64873, recursive=True) as chown_1504_64873:
                            chown_1504_64873()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64874) as should_copy_source_1505_64874:
                    should_copy_source_1505_64874()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPanner.bundle", prog_num=64875):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", r".", delete_extraneous_files=True, prog_num=64876) as copy_dir_to_dir_1506_64876:
                            copy_dir_to_dir_1506_64876()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPanner.bundle", where_to_unwtar=r".", prog_num=64877) as unwtar_1507_64877:
                            unwtar_1507_64877()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPanner.bundle", user_id=-1, group_id=-1, prog_num=64878, recursive=True) as chown_1508_64878:
                            chown_1508_64878()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64879) as should_copy_source_1509_64879:
                    should_copy_source_1509_64879()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPhaser.bundle", prog_num=64880):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", r".", delete_extraneous_files=True, prog_num=64881) as copy_dir_to_dir_1510_64881:
                            copy_dir_to_dir_1510_64881()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPhaser.bundle", where_to_unwtar=r".", prog_num=64882) as unwtar_1511_64882:
                            unwtar_1511_64882()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPhaser.bundle", user_id=-1, group_id=-1, prog_num=64883, recursive=True) as chown_1512_64883:
                            chown_1512_64883()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64884) as should_copy_source_1513_64884:
                    should_copy_source_1513_64884()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompPitcher.bundle", prog_num=64885):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", r".", delete_extraneous_files=True, prog_num=64886) as copy_dir_to_dir_1514_64886:
                            copy_dir_to_dir_1514_64886()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompPitcher.bundle", where_to_unwtar=r".", prog_num=64887) as unwtar_1515_64887:
                            unwtar_1515_64887()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompPitcher.bundle", user_id=-1, group_id=-1, prog_num=64888, recursive=True) as chown_1516_64888:
                            chown_1516_64888()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64889) as should_copy_source_1517_64889:
                    should_copy_source_1517_64889()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompReverb.bundle", prog_num=64890):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", r".", delete_extraneous_files=True, prog_num=64891) as copy_dir_to_dir_1518_64891:
                            copy_dir_to_dir_1518_64891()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompReverb.bundle", where_to_unwtar=r".", prog_num=64892) as unwtar_1519_64892:
                            unwtar_1519_64892()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompReverb.bundle", user_id=-1, group_id=-1, prog_num=64893, recursive=True) as chown_1520_64893:
                            chown_1520_64893()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64894) as should_copy_source_1521_64894:
                    should_copy_source_1521_64894()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompSpring.bundle", prog_num=64895):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", r".", delete_extraneous_files=True, prog_num=64896) as copy_dir_to_dir_1522_64896:
                            copy_dir_to_dir_1522_64896()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompSpring.bundle", where_to_unwtar=r".", prog_num=64897) as unwtar_1523_64897:
                            unwtar_1523_64897()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompSpring.bundle", user_id=-1, group_id=-1, prog_num=64898, recursive=True) as chown_1524_64898:
                            chown_1524_64898()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64899) as should_copy_source_1525_64899:
                    should_copy_source_1525_64899()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompTone.bundle", prog_num=64900):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", r".", delete_extraneous_files=True, prog_num=64901) as copy_dir_to_dir_1526_64901:
                            copy_dir_to_dir_1526_64901()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompTone.bundle", where_to_unwtar=r".", prog_num=64902) as unwtar_1527_64902:
                            unwtar_1527_64902()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompTone.bundle", user_id=-1, group_id=-1, prog_num=64903, recursive=True) as chown_1528_64903:
                            chown_1528_64903()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64904) as should_copy_source_1529_64904:
                    should_copy_source_1529_64904()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVibrolo.bundle", prog_num=64905):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=64906) as copy_dir_to_dir_1530_64906:
                            copy_dir_to_dir_1530_64906()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVibrolo.bundle", where_to_unwtar=r".", prog_num=64907) as unwtar_1531_64907:
                            unwtar_1531_64907()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVibrolo.bundle", user_id=-1, group_id=-1, prog_num=64908, recursive=True) as chown_1532_64908:
                            chown_1532_64908()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64909) as should_copy_source_1533_64909:
                    should_copy_source_1533_64909()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompVolume.bundle", prog_num=64910):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", r".", delete_extraneous_files=True, prog_num=64911) as copy_dir_to_dir_1534_64911:
                            copy_dir_to_dir_1534_64911()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompVolume.bundle", where_to_unwtar=r".", prog_num=64912) as unwtar_1535_64912:
                            unwtar_1535_64912()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompVolume.bundle", user_id=-1, group_id=-1, prog_num=64913, recursive=True) as chown_1536_64913:
                            chown_1536_64913()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTR", skip_progress_count=4, prog_num=64914) as should_copy_source_1537_64914:
                    should_copy_source_1537_64914()
                    with Stage(r"copy source", r"Mac/Plugins/GTR/StompWahWah.bundle", prog_num=64915):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", r".", delete_extraneous_files=True, prog_num=64916) as copy_dir_to_dir_1538_64916:
                            copy_dir_to_dir_1538_64916()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTR/StompWahWah.bundle", where_to_unwtar=r".", prog_num=64917) as unwtar_1539_64917:
                            unwtar_1539_64917()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTR/StompWahWah.bundle", user_id=-1, group_id=-1, prog_num=64918, recursive=True) as chown_1540_64918:
                            chown_1540_64918()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64919) as shell_command_1541_64919:
                shell_command_1541_64919()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/GTRSolo", prog_num=64920) as cd_stage_1542_64920:
            cd_stage_1542_64920()
            with Stage(r"copy", r"GTR Solo Stomps v16.0.23.24", prog_num=64921):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64922) as should_copy_source_1543_64922:
                    should_copy_source_1543_64922()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLChorus.bundle", prog_num=64923):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", r".", delete_extraneous_files=True, prog_num=64924) as copy_dir_to_dir_1544_64924:
                            copy_dir_to_dir_1544_64924()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLChorus.bundle", where_to_unwtar=r".", prog_num=64925) as unwtar_1545_64925:
                            unwtar_1545_64925()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLChorus.bundle", user_id=-1, group_id=-1, prog_num=64926, recursive=True) as chown_1546_64926:
                            chown_1546_64926()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64927) as should_copy_source_1547_64927:
                    should_copy_source_1547_64927()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLDelay.bundle", prog_num=64928):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", r".", delete_extraneous_files=True, prog_num=64929) as copy_dir_to_dir_1548_64929:
                            copy_dir_to_dir_1548_64929()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDelay.bundle", where_to_unwtar=r".", prog_num=64930) as unwtar_1549_64930:
                            unwtar_1549_64930()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLDelay.bundle", user_id=-1, group_id=-1, prog_num=64931, recursive=True) as chown_1550_64931:
                            chown_1550_64931()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64932) as should_copy_source_1551_64932:
                    should_copy_source_1551_64932()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLDistortion.bundle", prog_num=64933):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", r".", delete_extraneous_files=True, prog_num=64934) as copy_dir_to_dir_1552_64934:
                            copy_dir_to_dir_1552_64934()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLDistortion.bundle", where_to_unwtar=r".", prog_num=64935) as unwtar_1553_64935:
                            unwtar_1553_64935()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLDistortion.bundle", user_id=-1, group_id=-1, prog_num=64936, recursive=True) as chown_1554_64936:
                            chown_1554_64936()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64937) as should_copy_source_1555_64937:
                    should_copy_source_1555_64937()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLEQ.bundle", prog_num=64938):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", r".", delete_extraneous_files=True, prog_num=64939) as copy_dir_to_dir_1556_64939:
                            copy_dir_to_dir_1556_64939()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLEQ.bundle", where_to_unwtar=r".", prog_num=64940) as unwtar_1557_64940:
                            unwtar_1557_64940()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLEQ.bundle", user_id=-1, group_id=-1, prog_num=64941, recursive=True) as chown_1558_64941:
                            chown_1558_64941()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64942) as should_copy_source_1559_64942:
                    should_copy_source_1559_64942()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLFlanger.bundle", prog_num=64943):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", r".", delete_extraneous_files=True, prog_num=64944) as copy_dir_to_dir_1560_64944:
                            copy_dir_to_dir_1560_64944()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLFlanger.bundle", where_to_unwtar=r".", prog_num=64945) as unwtar_1561_64945:
                            unwtar_1561_64945()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLFlanger.bundle", user_id=-1, group_id=-1, prog_num=64946, recursive=True) as chown_1562_64946:
                            chown_1562_64946()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64947) as should_copy_source_1563_64947:
                    should_copy_source_1563_64947()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLGateComp.bundle", prog_num=64948):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", r".", delete_extraneous_files=True, prog_num=64949) as copy_dir_to_dir_1564_64949:
                            copy_dir_to_dir_1564_64949()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLGateComp.bundle", where_to_unwtar=r".", prog_num=64950) as unwtar_1565_64950:
                            unwtar_1565_64950()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLGateComp.bundle", user_id=-1, group_id=-1, prog_num=64951, recursive=True) as chown_1566_64951:
                            chown_1566_64951()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64952) as should_copy_source_1567_64952:
                    should_copy_source_1567_64952()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", prog_num=64953):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", r".", delete_extraneous_files=True, prog_num=64954) as copy_dir_to_dir_1568_64954:
                            copy_dir_to_dir_1568_64954()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLOverDrive.bundle", where_to_unwtar=r".", prog_num=64955) as unwtar_1569_64955:
                            unwtar_1569_64955()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLOverDrive.bundle", user_id=-1, group_id=-1, prog_num=64956, recursive=True) as chown_1570_64956:
                            chown_1570_64956()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64957) as should_copy_source_1571_64957:
                    should_copy_source_1571_64957()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLPhaser.bundle", prog_num=64958):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", r".", delete_extraneous_files=True, prog_num=64959) as copy_dir_to_dir_1572_64959:
                            copy_dir_to_dir_1572_64959()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPhaser.bundle", where_to_unwtar=r".", prog_num=64960) as unwtar_1573_64960:
                            unwtar_1573_64960()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLPhaser.bundle", user_id=-1, group_id=-1, prog_num=64961, recursive=True) as chown_1574_64961:
                            chown_1574_64961()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64962) as should_copy_source_1575_64962:
                    should_copy_source_1575_64962()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLPitcher.bundle", prog_num=64963):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", r".", delete_extraneous_files=True, prog_num=64964) as copy_dir_to_dir_1576_64964:
                            copy_dir_to_dir_1576_64964()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLPitcher.bundle", where_to_unwtar=r".", prog_num=64965) as unwtar_1577_64965:
                            unwtar_1577_64965()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLPitcher.bundle", user_id=-1, group_id=-1, prog_num=64966, recursive=True) as chown_1578_64966:
                            chown_1578_64966()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64967) as should_copy_source_1579_64967:
                    should_copy_source_1579_64967()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLSpring.bundle", prog_num=64968):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", r".", delete_extraneous_files=True, prog_num=64969) as copy_dir_to_dir_1580_64969:
                            copy_dir_to_dir_1580_64969()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLSpring.bundle", where_to_unwtar=r".", prog_num=64970) as unwtar_1581_64970:
                            unwtar_1581_64970()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLSpring.bundle", user_id=-1, group_id=-1, prog_num=64971, recursive=True) as chown_1582_64971:
                            chown_1582_64971()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64972) as should_copy_source_1583_64972:
                    should_copy_source_1583_64972()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", prog_num=64973):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", r".", delete_extraneous_files=True, prog_num=64974) as copy_dir_to_dir_1584_64974:
                            copy_dir_to_dir_1584_64974()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVibrolo.bundle", where_to_unwtar=r".", prog_num=64975) as unwtar_1585_64975:
                            unwtar_1585_64975()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLVibrolo.bundle", user_id=-1, group_id=-1, prog_num=64976, recursive=True) as chown_1586_64976:
                            chown_1586_64976()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64977) as should_copy_source_1587_64977:
                    should_copy_source_1587_64977()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLVolume.bundle", prog_num=64978):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", r".", delete_extraneous_files=True, prog_num=64979) as copy_dir_to_dir_1588_64979:
                            copy_dir_to_dir_1588_64979()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLVolume.bundle", where_to_unwtar=r".", prog_num=64980) as unwtar_1589_64980:
                            unwtar_1589_64980()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLVolume.bundle", user_id=-1, group_id=-1, prog_num=64981, recursive=True) as chown_1590_64981:
                            chown_1590_64981()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", r"/Applications/Waves/Plug-Ins V16/GTRSolo", skip_progress_count=4, prog_num=64982) as should_copy_source_1591_64982:
                    should_copy_source_1591_64982()
                    with Stage(r"copy source", r"Mac/Plugins/GTRSolo/StompSLWahWah.bundle", prog_num=64983):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", r".", delete_extraneous_files=True, prog_num=64984) as copy_dir_to_dir_1592_64984:
                            copy_dir_to_dir_1592_64984()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/GTRSolo/StompSLWahWah.bundle", where_to_unwtar=r".", prog_num=64985) as unwtar_1593_64985:
                            unwtar_1593_64985()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/GTRSolo/StompSLWahWah.bundle", user_id=-1, group_id=-1, prog_num=64986, recursive=True) as chown_1594_64986:
                            chown_1594_64986()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=64987) as shell_command_1595_64987:
                shell_command_1595_64987()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/MIDI", prog_num=64988) as cd_stage_1596_64988:
            cd_stage_1596_64988()
            with Stage(r"copy", r"MidiArpSeq v16.0.23.24", prog_num=64989):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=64990) as should_copy_source_1597_64990:
                    should_copy_source_1597_64990()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIArpSeq.bundle", prog_num=64991):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", r".", delete_extraneous_files=True, prog_num=64992) as copy_dir_to_dir_1598_64992:
                            copy_dir_to_dir_1598_64992()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIArpSeq.bundle", where_to_unwtar=r".", prog_num=64993) as unwtar_1599_64993:
                            unwtar_1599_64993()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIArpSeq.bundle", user_id=-1, group_id=-1, prog_num=64994, recursive=True) as chown_1600_64994:
                            chown_1600_64994()
            with Stage(r"copy", r"MIDIChords v16.0.23.24", prog_num=64995):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=64996) as should_copy_source_1601_64996:
                    should_copy_source_1601_64996()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIChords.bundle", prog_num=64997):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", r".", delete_extraneous_files=True, prog_num=64998) as copy_dir_to_dir_1602_64998:
                            copy_dir_to_dir_1602_64998()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIChords.bundle", where_to_unwtar=r".", prog_num=64999) as unwtar_1603_64999:
                            unwtar_1603_64999()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIChords.bundle", user_id=-1, group_id=-1, prog_num=65000, recursive=True) as chown_1604_65000:
                            chown_1604_65000()
            with Stage(r"copy", r"MIDIKeyboard v16.0.30.31", prog_num=65001):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65002) as should_copy_source_1605_65002:
                    should_copy_source_1605_65002()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIKeyboard.bundle", prog_num=65003):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", r".", delete_extraneous_files=True, prog_num=65004) as copy_dir_to_dir_1606_65004:
                            copy_dir_to_dir_1606_65004()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIKeyboard.bundle", where_to_unwtar=r".", prog_num=65005) as unwtar_1607_65005:
                            unwtar_1607_65005()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIKeyboard.bundle", user_id=-1, group_id=-1, prog_num=65006, recursive=True) as chown_1608_65006:
                            chown_1608_65006()
            with Stage(r"copy", r"MIDIMonitor v16.0.23.24", prog_num=65007):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65008) as should_copy_source_1609_65008:
                    should_copy_source_1609_65008()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIMonitor.bundle", prog_num=65009):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", r".", delete_extraneous_files=True, prog_num=65010) as copy_dir_to_dir_1610_65010:
                            copy_dir_to_dir_1610_65010()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIMonitor.bundle", where_to_unwtar=r".", prog_num=65011) as unwtar_1611_65011:
                            unwtar_1611_65011()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIMonitor.bundle", user_id=-1, group_id=-1, prog_num=65012, recursive=True) as chown_1612_65012:
                            chown_1612_65012()
            with Stage(r"copy", r"MIDIRange v16.0.23.24", prog_num=65013):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65014) as should_copy_source_1613_65014:
                    should_copy_source_1613_65014()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIRange.bundle", prog_num=65015):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", r".", delete_extraneous_files=True, prog_num=65016) as copy_dir_to_dir_1614_65016:
                            copy_dir_to_dir_1614_65016()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIRange.bundle", where_to_unwtar=r".", prog_num=65017) as unwtar_1615_65017:
                            unwtar_1615_65017()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIRange.bundle", user_id=-1, group_id=-1, prog_num=65018, recursive=True) as chown_1616_65018:
                            chown_1616_65018()
            with Stage(r"copy", r"MIDITranspose v16.0.23.24", prog_num=65019):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65020) as should_copy_source_1617_65020:
                    should_copy_source_1617_65020()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDITranspose.bundle", prog_num=65021):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", r".", delete_extraneous_files=True, prog_num=65022) as copy_dir_to_dir_1618_65022:
                            copy_dir_to_dir_1618_65022()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDITranspose.bundle", where_to_unwtar=r".", prog_num=65023) as unwtar_1619_65023:
                            unwtar_1619_65023()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDITranspose.bundle", user_id=-1, group_id=-1, prog_num=65024, recursive=True) as chown_1620_65024:
                            chown_1620_65024()
            with Stage(r"copy", r"MIDIVelocity v16.0.23.24", prog_num=65025):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65026) as should_copy_source_1621_65026:
                    should_copy_source_1621_65026()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVelocity.bundle", prog_num=65027):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", r".", delete_extraneous_files=True, prog_num=65028) as copy_dir_to_dir_1622_65028:
                            copy_dir_to_dir_1622_65028()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVelocity.bundle", where_to_unwtar=r".", prog_num=65029) as unwtar_1623_65029:
                            unwtar_1623_65029()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIVelocity.bundle", user_id=-1, group_id=-1, prog_num=65030, recursive=True) as chown_1624_65030:
                            chown_1624_65030()
            with Stage(r"copy", r"MIDIVoicing v16.0.23.24", prog_num=65031):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", r"/Applications/Waves/Plug-Ins V16/MIDI", skip_progress_count=4, prog_num=65032) as should_copy_source_1625_65032:
                    should_copy_source_1625_65032()
                    with Stage(r"copy source", r"Mac/Plugins/MIDI/MIDIVoicing.bundle", prog_num=65033):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", r".", delete_extraneous_files=True, prog_num=65034) as copy_dir_to_dir_1626_65034:
                            copy_dir_to_dir_1626_65034()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/MIDI/MIDIVoicing.bundle", where_to_unwtar=r".", prog_num=65035) as unwtar_1627_65035:
                            unwtar_1627_65035()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/MIDI/MIDIVoicing.bundle", user_id=-1, group_id=-1, prog_num=65036, recursive=True) as chown_1628_65036:
                            chown_1628_65036()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/Plug-Ins V16/ModFX", prog_num=65037) as cd_stage_1629_65037:
            cd_stage_1629_65037()
            with Stage(r"copy", r"ModFX Autopan v16.0.23.24", prog_num=65038):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65039) as should_copy_source_1630_65039:
                    should_copy_source_1630_65039()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Autopan.bundle", prog_num=65040):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", r".", delete_extraneous_files=True, prog_num=65041) as copy_dir_to_dir_1631_65041:
                            copy_dir_to_dir_1631_65041()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Autopan.bundle", where_to_unwtar=r".", prog_num=65042) as unwtar_1632_65042:
                            unwtar_1632_65042()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Autopan.bundle", user_id=-1, group_id=-1, prog_num=65043, recursive=True) as chown_1633_65043:
                            chown_1633_65043()
            with Stage(r"copy", r"ModFX Chorus v16.0.23.24", prog_num=65044):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65045) as should_copy_source_1634_65045:
                    should_copy_source_1634_65045()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Chorus.bundle", prog_num=65046):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", r".", delete_extraneous_files=True, prog_num=65047) as copy_dir_to_dir_1635_65047:
                            copy_dir_to_dir_1635_65047()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Chorus.bundle", where_to_unwtar=r".", prog_num=65048) as unwtar_1636_65048:
                            unwtar_1636_65048()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Chorus.bundle", user_id=-1, group_id=-1, prog_num=65049, recursive=True) as chown_1637_65049:
                            chown_1637_65049()
            with Stage(r"copy", r"ModFX Compressor v16.0.23.24", prog_num=65050):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65051) as should_copy_source_1638_65051:
                    should_copy_source_1638_65051()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Compressor.bundle", prog_num=65052):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", r".", delete_extraneous_files=True, prog_num=65053) as copy_dir_to_dir_1639_65053:
                            copy_dir_to_dir_1639_65053()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Compressor.bundle", where_to_unwtar=r".", prog_num=65054) as unwtar_1640_65054:
                            unwtar_1640_65054()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Compressor.bundle", user_id=-1, group_id=-1, prog_num=65055, recursive=True) as chown_1641_65055:
                            chown_1641_65055()
            with Stage(r"copy", r"ModFX Delay v16.0.23.24", prog_num=65056):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65057) as should_copy_source_1642_65057:
                    should_copy_source_1642_65057()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Delay.bundle", prog_num=65058):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", r".", delete_extraneous_files=True, prog_num=65059) as copy_dir_to_dir_1643_65059:
                            copy_dir_to_dir_1643_65059()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Delay.bundle", where_to_unwtar=r".", prog_num=65060) as unwtar_1644_65060:
                            unwtar_1644_65060()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Delay.bundle", user_id=-1, group_id=-1, prog_num=65061, recursive=True) as chown_1645_65061:
                            chown_1645_65061()
            with Stage(r"copy", r"ModFX Distortion v16.0.23.24", prog_num=65062):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65063) as should_copy_source_1646_65063:
                    should_copy_source_1646_65063()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Distortion.bundle", prog_num=65064):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", r".", delete_extraneous_files=True, prog_num=65065) as copy_dir_to_dir_1647_65065:
                            copy_dir_to_dir_1647_65065()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Distortion.bundle", where_to_unwtar=r".", prog_num=65066) as unwtar_1648_65066:
                            unwtar_1648_65066()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Distortion.bundle", user_id=-1, group_id=-1, prog_num=65067, recursive=True) as chown_1649_65067:
                            chown_1649_65067()
            with Stage(r"copy", r"ModFX Limiter v16.0.23.24", prog_num=65068):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65069) as should_copy_source_1650_65069:
                    should_copy_source_1650_65069()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Limiter.bundle", prog_num=65070):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", r".", delete_extraneous_files=True, prog_num=65071) as copy_dir_to_dir_1651_65071:
                            copy_dir_to_dir_1651_65071()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Limiter.bundle", where_to_unwtar=r".", prog_num=65072) as unwtar_1652_65072:
                            unwtar_1652_65072()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Limiter.bundle", user_id=-1, group_id=-1, prog_num=65073, recursive=True) as chown_1653_65073:
                            chown_1653_65073()
            with Stage(r"copy", r"ModFX Reverb v16.0.23.24", prog_num=65074):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r"/Applications/Waves/Plug-Ins V16/ModFX", skip_progress_count=4, prog_num=65075) as should_copy_source_1654_65075:
                    should_copy_source_1654_65075()
                    with Stage(r"copy source", r"Mac/Plugins/ModFX/ModFX_Reverb.bundle", prog_num=65076):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", r".", delete_extraneous_files=True, prog_num=65077) as copy_dir_to_dir_1655_65077:
                            copy_dir_to_dir_1655_65077()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Plugins/ModFX/ModFX_Reverb.bundle", where_to_unwtar=r".", prog_num=65078) as unwtar_1656_65078:
                            unwtar_1656_65078()
                        with Chown(path=r"/Applications/Waves/Plug-Ins V16/ModFX/ModFX_Reverb.bundle", user_id=-1, group_id=-1, prog_num=65079, recursive=True) as chown_1657_65079:
                            chown_1657_65079()
        with CdStage(r"copy_to_folder", r"/Applications/Waves/WaveShells V16", prog_num=65080) as cd_stage_1658_65080:
            cd_stage_1658_65080()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=65081):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65082) as should_copy_source_1659_65082:
                    should_copy_source_1659_65082()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=65083):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=65084) as copy_dir_to_dir_1660_65084:
                            copy_dir_to_dir_1660_65084()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=65085) as unwtar_1661_65085:
                            unwtar_1661_65085()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=65086, recursive=True) as chown_1662_65086:
                            chown_1662_65086()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=65087) as shell_command_1663_65087:
                            shell_command_1663_65087()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=65088):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Applications/Waves/WaveShells V16", skip_progress_count=8, prog_num=65089) as should_copy_source_1664_65089:
                    should_copy_source_1664_65089()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=65090):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=65091) as copy_dir_to_dir_1665_65091:
                            copy_dir_to_dir_1665_65091()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=65092) as unwtar_1666_65092:
                            unwtar_1666_65092()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=65093, recursive=True) as chown_1667_65093:
                            chown_1667_65093()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=65094) as break_hard_link_1668_65094:
                            break_hard_link_1668_65094()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=65095) as shell_command_1669_65095:
                            shell_command_1669_65095()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=65096, recursive=True) as chown_1670_65096:
                            chown_1670_65096()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=65097, recursive=True) as chmod_1671_65097:
                            chmod_1671_65097()
            with Stage(r"copy", r"WaveShell1-OBS 16.0 v16.0.23.24", prog_num=65098):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65099) as should_copy_source_1672_65099:
                    should_copy_source_1672_65099()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=65100):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=65101) as copy_dir_to_dir_1673_65101:
                            copy_dir_to_dir_1673_65101()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=65102) as unwtar_1674_65102:
                            unwtar_1674_65102()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=65103, recursive=True) as chown_1675_65103:
                            chown_1675_65103()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=65104) as shell_command_1676_65104:
                            shell_command_1676_65104()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=65105):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65106) as should_copy_source_1677_65106:
                    should_copy_source_1677_65106()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=65107):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=65108) as copy_dir_to_dir_1678_65108:
                            copy_dir_to_dir_1678_65108()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=65109) as unwtar_1679_65109:
                            unwtar_1679_65109()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=65110, recursive=True) as chown_1680_65110:
                            chown_1680_65110()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=65111) as shell_command_1681_65111:
                            shell_command_1681_65111()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=65112):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Applications/Waves/WaveShells V16", skip_progress_count=5, prog_num=65113) as should_copy_source_1682_65113:
                    should_copy_source_1682_65113()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=65114):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=65115) as copy_dir_to_dir_1683_65115:
                            copy_dir_to_dir_1683_65115()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=65116) as unwtar_1684_65116:
                            unwtar_1684_65116()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=65117, recursive=True) as chown_1685_65117:
                            chown_1685_65117()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=65118) as shell_command_1686_65118:
                            shell_command_1686_65118()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=65119):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Applications/Waves/WaveShells V16", skip_progress_count=7, prog_num=65120) as should_copy_source_1687_65120:
                    should_copy_source_1687_65120()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=65121):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=65122) as copy_dir_to_dir_1688_65122:
                            copy_dir_to_dir_1688_65122()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=65123) as unwtar_1689_65123:
                            unwtar_1689_65123()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=65124, recursive=True) as chown_1690_65124:
                            chown_1690_65124()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=65125) as shell_command_1691_65125:
                            shell_command_1691_65125()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=65126) as script_command_1692_65126:
                            script_command_1692_65126()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=65127) as shell_command_1693_65127:
                            shell_command_1693_65127()
            with Stage(r"copy", r"WaveShell-AU registration utility v16.0.23.24", prog_num=65128):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r"/Applications/Waves/WaveShells V16", skip_progress_count=4, prog_num=65129) as should_copy_source_1694_65129:
                    should_copy_source_1694_65129()
                    with Stage(r"copy source", r"Mac/Shells/Waves AU Reg Utility 16.app", prog_num=65130):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", r".", delete_extraneous_files=True, prog_num=65131) as copy_dir_to_dir_1695_65131:
                            copy_dir_to_dir_1695_65131()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves AU Reg Utility 16.app", where_to_unwtar=r".", prog_num=65132) as unwtar_1696_65132:
                            unwtar_1696_65132()
                        with Chown(path=r"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app", user_id=-1, group_id=-1, prog_num=65133, recursive=True) as chown_1697_65133:
                            chown_1697_65133()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves AU Reg Utility 16.app"', ignore_all_errors=True, prog_num=65134) as shell_command_1698_65134:
                shell_command_1698_65134()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Avid/Audio/Plug-Ins", prog_num=65135) as cd_stage_1699_65135:
            cd_stage_1699_65135()
            with Stage(r"copy", r"WaveShell1-AAX 16.0 v16.0.23.24", prog_num=65136):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r"/Library/Application Support/Avid/Audio/Plug-Ins", skip_progress_count=5, prog_num=65137) as should_copy_source_1700_65137:
                    should_copy_source_1700_65137()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", prog_num=65138):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", r".", delete_extraneous_files=True, prog_num=65139) as copy_dir_to_dir_1701_65139:
                            copy_dir_to_dir_1701_65139()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AAX 16.0.aaxplugin", where_to_unwtar=r".", prog_num=65140) as unwtar_1702_65140:
                            unwtar_1702_65140()
                        with Chown(path=r"/Library/Application Support/Avid/Audio/Plug-Ins/WaveShell1-AAX 16.0.aaxplugin", user_id=-1, group_id=-1, prog_num=65141, recursive=True) as chown_1703_65141:
                            chown_1703_65141()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AAX 16.0.aaxplugin"', ignore_all_errors=True, prog_num=65142) as shell_command_1704_65142:
                            shell_command_1704_65142()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Native Instruments/Service Center", prog_num=65143) as cd_stage_1705_65143:
            cd_stage_1705_65143()
            with Stage(r"copy", r"Aphex Vintage Exciter XML and Registry for Native Instruments", prog_num=65144):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65145) as should_copy_source_1706_65145:
                    should_copy_source_1706_65145()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", prog_num=65146):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Aphex Vintage Exciter Stereo.xml", r".", prog_num=65147) as copy_file_to_dir_1707_65147:
                            copy_file_to_dir_1707_65147()
                        with ChmodAndChown(path=r"Waves-Aphex Vintage Exciter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65148) as chmod_and_chown_1708_65148:
                            chmod_and_chown_1708_65148()
            with Stage(r"copy", r"AudioTrack XML and Registry for Native Instruments", prog_num=65149):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65150) as should_copy_source_1709_65150:
                    should_copy_source_1709_65150()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", prog_num=65151):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-AudioTrack Stereo.xml", r".", prog_num=65152) as copy_file_to_dir_1710_65152:
                            copy_file_to_dir_1710_65152()
                        with ChmodAndChown(path=r"Waves-AudioTrack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65153) as chmod_and_chown_1711_65153:
                            chmod_and_chown_1711_65153()
            with Stage(r"copy", r"Bass Fingers XML and Registry for Native Instruments", prog_num=65154):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65155) as should_copy_source_1712_65155:
                    should_copy_source_1712_65155()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", prog_num=65156):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Fingers Stereo.xml", r".", prog_num=65157) as copy_file_to_dir_1713_65157:
                            copy_file_to_dir_1713_65157()
                        with ChmodAndChown(path=r"Waves-Bass Fingers Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65158) as chmod_and_chown_1714_65158:
                            chmod_and_chown_1714_65158()
            with Stage(r"copy", r"Bass Slapper XML and Registry for Native Instruments", prog_num=65159):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65160) as should_copy_source_1715_65160:
                    should_copy_source_1715_65160()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", prog_num=65161):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Bass Slapper Stereo.xml", r".", prog_num=65162) as copy_file_to_dir_1716_65162:
                            copy_file_to_dir_1716_65162()
                        with ChmodAndChown(path=r"Waves-Bass Slapper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65163) as chmod_and_chown_1717_65163:
                            chmod_and_chown_1717_65163()
            with Stage(r"copy", r"Bass Rider XML and Registry for Native Instruments", prog_num=65164):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65165) as should_copy_source_1718_65165:
                    should_copy_source_1718_65165()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", prog_num=65166):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Bass Rider Stereo.xml", r".", prog_num=65167) as copy_file_to_dir_1719_65167:
                            copy_file_to_dir_1719_65167()
                        with ChmodAndChown(path=r"Waves-Bass Rider Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65168) as chmod_and_chown_1720_65168:
                            chmod_and_chown_1720_65168()
            with Stage(r"copy", r"Brauer Motion XML and Registry for Native Instruments", prog_num=65169):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65170) as should_copy_source_1721_65170:
                    should_copy_source_1721_65170()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", prog_num=65171):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Brauer Motion Stereo.xml", r".", prog_num=65172) as copy_file_to_dir_1722_65172:
                            copy_file_to_dir_1722_65172()
                        with ChmodAndChown(path=r"Waves-Brauer Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65173) as chmod_and_chown_1723_65173:
                            chmod_and_chown_1723_65173()
            with Stage(r"copy", r"Butch Vig Vocals XML and Registry for Native Instruments", prog_num=65174):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65175) as should_copy_source_1724_65175:
                    should_copy_source_1724_65175()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", prog_num=65176):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Butch Vig Vocals Stereo.xml", r".", prog_num=65177) as copy_file_to_dir_1725_65177:
                            copy_file_to_dir_1725_65177()
                        with ChmodAndChown(path=r"Waves-Butch Vig Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65178) as chmod_and_chown_1726_65178:
                            chmod_and_chown_1726_65178()
            with Stage(r"copy", r"C1 comp-gate XML and Registry for Native Instruments", prog_num=65179):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65180) as should_copy_source_1727_65180:
                    should_copy_source_1727_65180()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", prog_num=65181):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C1 comp-gate Stereo.xml", r".", prog_num=65182) as copy_file_to_dir_1728_65182:
                            copy_file_to_dir_1728_65182()
                        with ChmodAndChown(path=r"Waves-C1 comp-gate Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65183) as chmod_and_chown_1729_65183:
                            chmod_and_chown_1729_65183()
            with Stage(r"copy", r"C4 XML and Registry for Native Instruments", prog_num=65184):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65185) as should_copy_source_1730_65185:
                    should_copy_source_1730_65185()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", prog_num=65186):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C4 Stereo.xml", r".", prog_num=65187) as copy_file_to_dir_1731_65187:
                            copy_file_to_dir_1731_65187()
                        with ChmodAndChown(path=r"Waves-C4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65188) as chmod_and_chown_1732_65188:
                            chmod_and_chown_1732_65188()
            with Stage(r"copy", r"C6 XML and Registry for Native Instruments", prog_num=65189):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65190) as should_copy_source_1733_65190:
                    should_copy_source_1733_65190()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", prog_num=65191):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-C6 Stereo.xml", r".", prog_num=65192) as copy_file_to_dir_1734_65192:
                            copy_file_to_dir_1734_65192()
                        with ChmodAndChown(path=r"Waves-C6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65193) as chmod_and_chown_1735_65193:
                            chmod_and_chown_1735_65193()
            with Stage(r"copy", r"CLA-2A XML and Registry for Native Instruments", prog_num=65194):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65195) as should_copy_source_1736_65195:
                    should_copy_source_1736_65195()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", prog_num=65196):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-2A Stereo.xml", r".", prog_num=65197) as copy_file_to_dir_1737_65197:
                            copy_file_to_dir_1737_65197()
                        with ChmodAndChown(path=r"Waves-CLA-2A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65198) as chmod_and_chown_1738_65198:
                            chmod_and_chown_1738_65198()
            with Stage(r"copy", r"CLA-3A XML and Registry for Native Instruments", prog_num=65199):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65200) as should_copy_source_1739_65200:
                    should_copy_source_1739_65200()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", prog_num=65201):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-3A Stereo.xml", r".", prog_num=65202) as copy_file_to_dir_1740_65202:
                            copy_file_to_dir_1740_65202()
                        with ChmodAndChown(path=r"Waves-CLA-3A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65203) as chmod_and_chown_1741_65203:
                            chmod_and_chown_1741_65203()
            with Stage(r"copy", r"CLA-76 XML and Registry for Native Instruments", prog_num=65204):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65205) as should_copy_source_1742_65205:
                    should_copy_source_1742_65205()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", prog_num=65206):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-CLA-76 Stereo.xml", r".", prog_num=65207) as copy_file_to_dir_1743_65207:
                            copy_file_to_dir_1743_65207()
                        with ChmodAndChown(path=r"Waves-CLA-76 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65208) as chmod_and_chown_1744_65208:
                            chmod_and_chown_1744_65208()
            with Stage(r"copy", r"CODEX XML and Registry for Native Instruments", prog_num=65209):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65210) as should_copy_source_1745_65210:
                    should_copy_source_1745_65210()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", prog_num=65211):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-CODEX Stereo.xml", r".", prog_num=65212) as copy_file_to_dir_1746_65212:
                            copy_file_to_dir_1746_65212()
                        with ChmodAndChown(path=r"Waves-CODEX Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65213) as chmod_and_chown_1747_65213:
                            chmod_and_chown_1747_65213()
            with Stage(r"copy", r"Center XML and Registry for Native Instruments", prog_num=65214):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65215) as should_copy_source_1748_65215:
                    should_copy_source_1748_65215()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Center Stereo.xml", prog_num=65216):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Center Stereo.xml", r".", prog_num=65217) as copy_file_to_dir_1749_65217:
                            copy_file_to_dir_1749_65217()
                        with ChmodAndChown(path=r"Waves-Center Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65218) as chmod_and_chown_1750_65218:
                            chmod_and_chown_1750_65218()
            with Stage(r"copy", r"Clavinet XML and Registry for Native Instruments", prog_num=65219):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65220) as should_copy_source_1751_65220:
                    should_copy_source_1751_65220()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", prog_num=65221):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Clavinet Stereo.xml", r".", prog_num=65222) as copy_file_to_dir_1752_65222:
                            copy_file_to_dir_1752_65222()
                        with ChmodAndChown(path=r"Waves-Clavinet Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65223) as chmod_and_chown_1753_65223:
                            chmod_and_chown_1753_65223()
            with Stage(r"copy", r"DPR-402 XML and Registry for Native Instruments", prog_num=65224):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65225) as should_copy_source_1754_65225:
                    should_copy_source_1754_65225()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", prog_num=65226):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-DPR-402 Stereo.xml", r".", prog_num=65227) as copy_file_to_dir_1755_65227:
                            copy_file_to_dir_1755_65227()
                        with ChmodAndChown(path=r"Waves-DPR-402 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65228) as chmod_and_chown_1756_65228:
                            chmod_and_chown_1756_65228()
            with Stage(r"copy", r"Dorrough XML and Registry for Native Instruments", prog_num=65229):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65230) as should_copy_source_1757_65230:
                    should_copy_source_1757_65230()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", prog_num=65231):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Dorrough Stereo.xml", r".", prog_num=65232) as copy_file_to_dir_1758_65232:
                            copy_file_to_dir_1758_65232()
                        with ChmodAndChown(path=r"Waves-Dorrough Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65233) as chmod_and_chown_1759_65233:
                            chmod_and_chown_1759_65233()
            with Stage(r"copy", r"EMO-D5 XML and Registry for Native Instruments", prog_num=65234):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65235) as should_copy_source_1760_65235:
                    should_copy_source_1760_65235()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", prog_num=65236):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-D5 Stereo.xml", r".", prog_num=65237) as copy_file_to_dir_1761_65237:
                            copy_file_to_dir_1761_65237()
                        with ChmodAndChown(path=r"Waves-EMO-D5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65238) as chmod_and_chown_1762_65238:
                            chmod_and_chown_1762_65238()
            with Stage(r"copy", r"EMO-F2 XML and Registry for Native Instruments", prog_num=65239):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65240) as should_copy_source_1763_65240:
                    should_copy_source_1763_65240()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", prog_num=65241):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-F2 Stereo.xml", r".", prog_num=65242) as copy_file_to_dir_1764_65242:
                            copy_file_to_dir_1764_65242()
                        with ChmodAndChown(path=r"Waves-EMO-F2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65243) as chmod_and_chown_1765_65243:
                            chmod_and_chown_1765_65243()
            with Stage(r"copy", r"EMO-Q4 XML and Registry for Native Instruments", prog_num=65244):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65245) as should_copy_source_1766_65245:
                    should_copy_source_1766_65245()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", prog_num=65246):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-EMO-Q4 Stereo.xml", r".", prog_num=65247) as copy_file_to_dir_1767_65247:
                            copy_file_to_dir_1767_65247()
                        with ChmodAndChown(path=r"Waves-EMO-Q4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65248) as chmod_and_chown_1768_65248:
                            chmod_and_chown_1768_65248()
            with Stage(r"copy", r"Electric200 XML and Registry for Native Instruments", prog_num=65249):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65250) as should_copy_source_1769_65250:
                    should_copy_source_1769_65250()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", prog_num=65251):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric200 Stereo.xml", r".", prog_num=65252) as copy_file_to_dir_1770_65252:
                            copy_file_to_dir_1770_65252()
                        with ChmodAndChown(path=r"Waves-Electric200 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65253) as chmod_and_chown_1771_65253:
                            chmod_and_chown_1771_65253()
            with Stage(r"copy", r"Electric88 XML and Registry for Native Instruments", prog_num=65254):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65255) as should_copy_source_1772_65255:
                    should_copy_source_1772_65255()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", prog_num=65256):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric88 Stereo.xml", r".", prog_num=65257) as copy_file_to_dir_1773_65257:
                            copy_file_to_dir_1773_65257()
                        with ChmodAndChown(path=r"Waves-Electric88 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65258) as chmod_and_chown_1774_65258:
                            chmod_and_chown_1774_65258()
            with Stage(r"copy", r"Electric Grand 80 XML and Registry for Native Instruments", prog_num=65259):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65260) as should_copy_source_1775_65260:
                    should_copy_source_1775_65260()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", prog_num=65261):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Electric Grand 80 Stereo.xml", r".", prog_num=65262) as copy_file_to_dir_1776_65262:
                            copy_file_to_dir_1776_65262()
                        with ChmodAndChown(path=r"Waves-Electric Grand 80 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65263) as chmod_and_chown_1777_65263:
                            chmod_and_chown_1777_65263()
            with Stage(r"copy", r"Element XML and Registry for Native Instruments", prog_num=65264):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65265) as should_copy_source_1778_65265:
                    should_copy_source_1778_65265()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", prog_num=65266):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Element Stereo.xml", r".", prog_num=65267) as copy_file_to_dir_1779_65267:
                            copy_file_to_dir_1779_65267()
                        with ChmodAndChown(path=r"Waves-Element Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65268) as chmod_and_chown_1780_65268:
                            chmod_and_chown_1780_65268()
            with Stage(r"copy", r"Enigma XML and Registry for Native Instruments", prog_num=65269):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65270) as should_copy_source_1781_65270:
                    should_copy_source_1781_65270()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", prog_num=65271):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Enigma Stereo.xml", r".", prog_num=65272) as copy_file_to_dir_1782_65272:
                            copy_file_to_dir_1782_65272()
                        with ChmodAndChown(path=r"Waves-Enigma Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65273) as chmod_and_chown_1783_65273:
                            chmod_and_chown_1783_65273()
            with Stage(r"copy", r"F6 XML and Registry for Native Instruments", prog_num=65274):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65275) as should_copy_source_1784_65275:
                    should_copy_source_1784_65275()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", prog_num=65276):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-F6 Stereo.xml", r".", prog_num=65277) as copy_file_to_dir_1785_65277:
                            copy_file_to_dir_1785_65277()
                        with ChmodAndChown(path=r"Waves-F6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65278) as chmod_and_chown_1786_65278:
                            chmod_and_chown_1786_65278()
            with Stage(r"copy", r"Flow Motion XML and Registry for Native Instruments", prog_num=65279):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65280) as should_copy_source_1787_65280:
                    should_copy_source_1787_65280()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", prog_num=65281):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Flow Motion Stereo.xml", r".", prog_num=65282) as copy_file_to_dir_1788_65282:
                            copy_file_to_dir_1788_65282()
                        with ChmodAndChown(path=r"Waves-Flow Motion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65283) as chmod_and_chown_1789_65283:
                            chmod_and_chown_1789_65283()
            with Stage(r"copy", r"GEQ Classic XML and Registry for Native Instruments", prog_num=65284):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65285) as should_copy_source_1790_65285:
                    should_copy_source_1790_65285()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", prog_num=65286):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Classic Stereo.xml", r".", prog_num=65287) as copy_file_to_dir_1791_65287:
                            copy_file_to_dir_1791_65287()
                        with ChmodAndChown(path=r"Waves-GEQ Classic Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65288) as chmod_and_chown_1792_65288:
                            chmod_and_chown_1792_65288()
            with Stage(r"copy", r"GEQ Modern XML and Registry for Native Instruments", prog_num=65289):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65290) as should_copy_source_1793_65290:
                    should_copy_source_1793_65290()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", prog_num=65291):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GEQ Modern Stereo.xml", r".", prog_num=65292) as copy_file_to_dir_1794_65292:
                            copy_file_to_dir_1794_65292()
                        with ChmodAndChown(path=r"Waves-GEQ Modern Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65293) as chmod_and_chown_1795_65293:
                            chmod_and_chown_1795_65293()
            with Stage(r"copy", r"Grand Rhapsody XML and Registry for Native Instruments", prog_num=65294):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65295) as should_copy_source_1796_65295:
                    should_copy_source_1796_65295()
                    with Stage(r"copy source", r"Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", prog_num=65296):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/Instrument Data/NKS/XML/Waves-Grand Rhapsody Stereo.xml", r".", prog_num=65297) as copy_file_to_dir_1797_65297:
                            copy_file_to_dir_1797_65297()
                        with ChmodAndChown(path=r"Waves-Grand Rhapsody Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65298) as chmod_and_chown_1798_65298:
                            chmod_and_chown_1798_65298()
            with Stage(r"copy", r"Greg Wells MixCentric XML and Registry for Native Instruments", prog_num=65299):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65300) as should_copy_source_1799_65300:
                    should_copy_source_1799_65300()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", prog_num=65301):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells MixCentric Stereo.xml", r".", prog_num=65302) as copy_file_to_dir_1800_65302:
                            copy_file_to_dir_1800_65302()
                        with ChmodAndChown(path=r"Waves-Greg Wells MixCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65303) as chmod_and_chown_1801_65303:
                            chmod_and_chown_1801_65303()
            with Stage(r"copy", r"Greg Wells PianoCentric XML and Registry for Native Instruments", prog_num=65304):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65305) as should_copy_source_1802_65305:
                    should_copy_source_1802_65305()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", prog_num=65306):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Greg Wells PianoCentric Stereo.xml", r".", prog_num=65307) as copy_file_to_dir_1803_65307:
                            copy_file_to_dir_1803_65307()
                        with ChmodAndChown(path=r"Waves-Greg Wells PianoCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65308) as chmod_and_chown_1804_65308:
                            chmod_and_chown_1804_65308()
            with Stage(r"copy", r"GW ToneCentric XML and Registry for Native Instruments", prog_num=65309):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65310) as should_copy_source_1805_65310:
                    should_copy_source_1805_65310()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", prog_num=65311):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW ToneCentric Stereo.xml", r".", prog_num=65312) as copy_file_to_dir_1806_65312:
                            copy_file_to_dir_1806_65312()
                        with ChmodAndChown(path=r"Waves-GW ToneCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65313) as chmod_and_chown_1807_65313:
                            chmod_and_chown_1807_65313()
            with Stage(r"copy", r"GW VoiceCentric XML and Registry for Native Instruments", prog_num=65314):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65315) as should_copy_source_1808_65315:
                    should_copy_source_1808_65315()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", prog_num=65316):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-GW VoiceCentric Stereo.xml", r".", prog_num=65317) as copy_file_to_dir_1809_65317:
                            copy_file_to_dir_1809_65317()
                        with ChmodAndChown(path=r"Waves-GW VoiceCentric Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65318) as chmod_and_chown_1810_65318:
                            chmod_and_chown_1810_65318()
            with Stage(r"copy", r"H-Delay XML and Registry for Native Instruments", prog_num=65319):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65320) as should_copy_source_1811_65320:
                    should_copy_source_1811_65320()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", prog_num=65321):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Delay Stereo.xml", r".", prog_num=65322) as copy_file_to_dir_1812_65322:
                            copy_file_to_dir_1812_65322()
                        with ChmodAndChown(path=r"Waves-H-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65323) as chmod_and_chown_1813_65323:
                            chmod_and_chown_1813_65323()
            with Stage(r"copy", r"H-EQ XML and Registry for Native Instruments", prog_num=65324):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65325) as should_copy_source_1814_65325:
                    should_copy_source_1814_65325()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", prog_num=65326):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-EQ Stereo.xml", r".", prog_num=65327) as copy_file_to_dir_1815_65327:
                            copy_file_to_dir_1815_65327()
                        with ChmodAndChown(path=r"Waves-H-EQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65328) as chmod_and_chown_1816_65328:
                            chmod_and_chown_1816_65328()
            with Stage(r"copy", r"H-Reverb long XML and Registry for Native Instruments", prog_num=65329):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65330) as should_copy_source_1817_65330:
                    should_copy_source_1817_65330()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", prog_num=65331):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-H-Reverb long Stereo.xml", r".", prog_num=65332) as copy_file_to_dir_1818_65332:
                            copy_file_to_dir_1818_65332()
                        with ChmodAndChown(path=r"Waves-H-Reverb long Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65333) as chmod_and_chown_1819_65333:
                            chmod_and_chown_1819_65333()
            with Stage(r"copy", r"IMPusher XML and Registry for Native Instruments", prog_num=65334):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65335) as should_copy_source_1820_65335:
                    should_copy_source_1820_65335()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", prog_num=65336):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IMPusher Stereo.xml", r".", prog_num=65337) as copy_file_to_dir_1821_65337:
                            copy_file_to_dir_1821_65337()
                        with ChmodAndChown(path=r"Waves-IMPusher Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65338) as chmod_and_chown_1822_65338:
                            chmod_and_chown_1822_65338()
            with Stage(r"copy", r"IRLive XML and Registry for Native Instruments", prog_num=65339):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65340) as should_copy_source_1823_65340:
                    should_copy_source_1823_65340()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", prog_num=65341):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-IRLive Stereo.xml", r".", prog_num=65342) as copy_file_to_dir_1824_65342:
                            copy_file_to_dir_1824_65342()
                        with ChmodAndChown(path=r"Waves-IRLive Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65343) as chmod_and_chown_1825_65343:
                            chmod_and_chown_1825_65343()
            with Stage(r"copy", r"InPhase LT Live XML and Registry for Native Instruments", prog_num=65344):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65345) as should_copy_source_1826_65345:
                    should_copy_source_1826_65345()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", prog_num=65346):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-InPhase LT Live Stereo.xml", r".", prog_num=65347) as copy_file_to_dir_1827_65347:
                            copy_file_to_dir_1827_65347()
                        with ChmodAndChown(path=r"Waves-InPhase LT Live Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65348) as chmod_and_chown_1828_65348:
                            chmod_and_chown_1828_65348()
            with Stage(r"copy", r"J37 XML and Registry for Native Instruments", prog_num=65349):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65350) as should_copy_source_1829_65350:
                    should_copy_source_1829_65350()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", prog_num=65351):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-J37 Stereo.xml", r".", prog_num=65352) as copy_file_to_dir_1830_65352:
                            copy_file_to_dir_1830_65352()
                        with ChmodAndChown(path=r"Waves-J37 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65353) as chmod_and_chown_1831_65353:
                            chmod_and_chown_1831_65353()
            with Stage(r"copy", r"JJP-Bass XML and Registry for Native Instruments", prog_num=65354):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65355) as should_copy_source_1832_65355:
                    should_copy_source_1832_65355()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", prog_num=65356):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Bass Stereo.xml", r".", prog_num=65357) as copy_file_to_dir_1833_65357:
                            copy_file_to_dir_1833_65357()
                        with ChmodAndChown(path=r"Waves-JJP-Bass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65358) as chmod_and_chown_1834_65358:
                            chmod_and_chown_1834_65358()
            with Stage(r"copy", r"JJP-Cymb-Perc XML and Registry for Native Instruments", prog_num=65359):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65360) as should_copy_source_1835_65360:
                    should_copy_source_1835_65360()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", prog_num=65361):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Cymb-Perc Stereo.xml", r".", prog_num=65362) as copy_file_to_dir_1836_65362:
                            copy_file_to_dir_1836_65362()
                        with ChmodAndChown(path=r"Waves-JJP-Cymb-Perc Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65363) as chmod_and_chown_1837_65363:
                            chmod_and_chown_1837_65363()
            with Stage(r"copy", r"JJP-Drums XML and Registry for Native Instruments", prog_num=65364):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65365) as should_copy_source_1838_65365:
                    should_copy_source_1838_65365()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", prog_num=65366):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Drums Stereo.xml", r".", prog_num=65367) as copy_file_to_dir_1839_65367:
                            copy_file_to_dir_1839_65367()
                        with ChmodAndChown(path=r"Waves-JJP-Drums Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65368) as chmod_and_chown_1840_65368:
                            chmod_and_chown_1840_65368()
            with Stage(r"copy", r"JJP-Guitars XML and Registry for Native Instruments", prog_num=65369):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65370) as should_copy_source_1841_65370:
                    should_copy_source_1841_65370()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", prog_num=65371):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Guitars Stereo.xml", r".", prog_num=65372) as copy_file_to_dir_1842_65372:
                            copy_file_to_dir_1842_65372()
                        with ChmodAndChown(path=r"Waves-JJP-Guitars Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65373) as chmod_and_chown_1843_65373:
                            chmod_and_chown_1843_65373()
            with Stage(r"copy", r"JJP-Strings-Keys XML and Registry for Native Instruments", prog_num=65374):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65375) as should_copy_source_1844_65375:
                    should_copy_source_1844_65375()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", prog_num=65376):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Strings-Keys Stereo.xml", r".", prog_num=65377) as copy_file_to_dir_1845_65377:
                            copy_file_to_dir_1845_65377()
                        with ChmodAndChown(path=r"Waves-JJP-Strings-Keys Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65378) as chmod_and_chown_1846_65378:
                            chmod_and_chown_1846_65378()
            with Stage(r"copy", r"JJP-Vocals XML and Registry for Native Instruments", prog_num=65379):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65380) as should_copy_source_1847_65380:
                    should_copy_source_1847_65380()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", prog_num=65381):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-JJP-Vocals Stereo.xml", r".", prog_num=65382) as copy_file_to_dir_1848_65382:
                            copy_file_to_dir_1848_65382()
                        with ChmodAndChown(path=r"Waves-JJP-Vocals Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65383) as chmod_and_chown_1849_65383:
                            chmod_and_chown_1849_65383()
            with Stage(r"copy", r"The King's Microphones XML and Registry for Native Instruments", prog_num=65384):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65385) as should_copy_source_1850_65385:
                    should_copy_source_1850_65385()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", prog_num=65386):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-The Kings Microphones Stereo.xml", r".", prog_num=65387) as copy_file_to_dir_1851_65387:
                            copy_file_to_dir_1851_65387()
                        with ChmodAndChown(path=r"Waves-The Kings Microphones Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65388) as chmod_and_chown_1852_65388:
                            chmod_and_chown_1852_65388()
            with Stage(r"copy", r"KramerHLS XML and Registry for Native Instruments", prog_num=65389):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65390) as should_copy_source_1853_65390:
                    should_copy_source_1853_65390()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", prog_num=65391):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerHLS Stereo.xml", r".", prog_num=65392) as copy_file_to_dir_1854_65392:
                            copy_file_to_dir_1854_65392()
                        with ChmodAndChown(path=r"Waves-KramerHLS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65393) as chmod_and_chown_1855_65393:
                            chmod_and_chown_1855_65393()
            with Stage(r"copy", r"KramerPIE XML and Registry for Native Instruments", prog_num=65394):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65395) as should_copy_source_1856_65395:
                    should_copy_source_1856_65395()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", prog_num=65396):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-KramerPIE Stereo.xml", r".", prog_num=65397) as copy_file_to_dir_1857_65397:
                            copy_file_to_dir_1857_65397()
                        with ChmodAndChown(path=r"Waves-KramerPIE Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65398) as chmod_and_chown_1858_65398:
                            chmod_and_chown_1858_65398()
            with Stage(r"copy", r"Kramer Tape XML and Registry for Native Instruments", prog_num=65399):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65400) as should_copy_source_1859_65400:
                    should_copy_source_1859_65400()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", prog_num=65401):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Kramer Tape Stereo.xml", r".", prog_num=65402) as copy_file_to_dir_1860_65402:
                            copy_file_to_dir_1860_65402()
                        with ChmodAndChown(path=r"Waves-Kramer Tape Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65403) as chmod_and_chown_1861_65403:
                            chmod_and_chown_1861_65403()
            with Stage(r"copy", r"L1 XML and Registry for Native Instruments", prog_num=65404):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65405) as should_copy_source_1862_65405:
                    should_copy_source_1862_65405()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", prog_num=65406):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L1 Stereo.xml", r".", prog_num=65407) as copy_file_to_dir_1863_65407:
                            copy_file_to_dir_1863_65407()
                        with ChmodAndChown(path=r"Waves-L1 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65408) as chmod_and_chown_1864_65408:
                            chmod_and_chown_1864_65408()
            with Stage(r"copy", r"L2 XML and Registry for Native Instruments", prog_num=65409):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65410) as should_copy_source_1865_65410:
                    should_copy_source_1865_65410()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", prog_num=65411):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L2 Stereo.xml", r".", prog_num=65412) as copy_file_to_dir_1866_65412:
                            copy_file_to_dir_1866_65412()
                        with ChmodAndChown(path=r"Waves-L2 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65413) as chmod_and_chown_1867_65413:
                            chmod_and_chown_1867_65413()
            with Stage(r"copy", r"L3-16 XML and Registry for Native Instruments", prog_num=65414):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65415) as should_copy_source_1868_65415:
                    should_copy_source_1868_65415()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", prog_num=65416):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-16 Stereo.xml", r".", prog_num=65417) as copy_file_to_dir_1869_65417:
                            copy_file_to_dir_1869_65417()
                        with ChmodAndChown(path=r"Waves-L3-16 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65418) as chmod_and_chown_1870_65418:
                            chmod_and_chown_1870_65418()
            with Stage(r"copy", r"L3-LL Multi XML and Registry for Native Instruments", prog_num=65419):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65420) as should_copy_source_1871_65420:
                    should_copy_source_1871_65420()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", prog_num=65421):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3-LL Multi Stereo.xml", r".", prog_num=65422) as copy_file_to_dir_1872_65422:
                            copy_file_to_dir_1872_65422()
                        with ChmodAndChown(path=r"Waves-L3-LL Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65423) as chmod_and_chown_1873_65423:
                            chmod_and_chown_1873_65423()
            with Stage(r"copy", r"L3 Multi XML and Registry for Native Instruments", prog_num=65424):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65425) as should_copy_source_1874_65425:
                    should_copy_source_1874_65425()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", prog_num=65426):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Multi Stereo.xml", r".", prog_num=65427) as copy_file_to_dir_1875_65427:
                            copy_file_to_dir_1875_65427()
                        with ChmodAndChown(path=r"Waves-L3 Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65428) as chmod_and_chown_1876_65428:
                            chmod_and_chown_1876_65428()
            with Stage(r"copy", r"L3 Ultra XML and Registry for Native Instruments", prog_num=65429):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65430) as should_copy_source_1877_65430:
                    should_copy_source_1877_65430()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", prog_num=65431):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-L3 Ultra Stereo.xml", r".", prog_num=65432) as copy_file_to_dir_1878_65432:
                            copy_file_to_dir_1878_65432()
                        with ChmodAndChown(path=r"Waves-L3 Ultra Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65433) as chmod_and_chown_1879_65433:
                            chmod_and_chown_1879_65433()
            with Stage(r"copy", r"LinMB XML and Registry for Native Instruments", prog_num=65434):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65435) as should_copy_source_1880_65435:
                    should_copy_source_1880_65435()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", prog_num=65436):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LinMB Stereo.xml", r".", prog_num=65437) as copy_file_to_dir_1881_65437:
                            copy_file_to_dir_1881_65437()
                        with ChmodAndChown(path=r"Waves-LinMB Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65438) as chmod_and_chown_1882_65438:
                            chmod_and_chown_1882_65438()
            with Stage(r"copy", r"LoAir XML and Registry for Native Instruments", prog_num=65439):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65440) as should_copy_source_1883_65440:
                    should_copy_source_1883_65440()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", prog_num=65441):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-LoAir Stereo.xml", r".", prog_num=65442) as copy_file_to_dir_1884_65442:
                            copy_file_to_dir_1884_65442()
                        with ChmodAndChown(path=r"Waves-LoAir Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65443) as chmod_and_chown_1885_65443:
                            chmod_and_chown_1885_65443()
            with Stage(r"copy", r"MannyM-Delay XML and Registry for Native Instruments", prog_num=65444):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65445) as should_copy_source_1886_65445:
                    should_copy_source_1886_65445()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", prog_num=65446):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Delay Stereo.xml", r".", prog_num=65447) as copy_file_to_dir_1887_65447:
                            copy_file_to_dir_1887_65447()
                        with ChmodAndChown(path=r"Waves-MannyM-Delay Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65448) as chmod_and_chown_1888_65448:
                            chmod_and_chown_1888_65448()
            with Stage(r"copy", r"MannyM Distortion XML and Registry for Native Instruments", prog_num=65449):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65450) as should_copy_source_1889_65450:
                    should_copy_source_1889_65450()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", prog_num=65451):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM Distortion Stereo.xml", r".", prog_num=65452) as copy_file_to_dir_1890_65452:
                            copy_file_to_dir_1890_65452()
                        with ChmodAndChown(path=r"Waves-MannyM Distortion Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65453) as chmod_and_chown_1891_65453:
                            chmod_and_chown_1891_65453()
            with Stage(r"copy", r"MannyM-EQ XML and Registry for Native Instruments", prog_num=65454):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65455) as should_copy_source_1892_65455:
                    should_copy_source_1892_65455()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", prog_num=65456):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-EQ Stereo.xml", r".", prog_num=65457) as copy_file_to_dir_1893_65457:
                            copy_file_to_dir_1893_65457()
                        with ChmodAndChown(path=r"Waves-MannyM-EQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65458) as chmod_and_chown_1894_65458:
                            chmod_and_chown_1894_65458()
            with Stage(r"copy", r"Manny Marroquin Reverb XML and Registry for Native Instruments", prog_num=65459):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65460) as should_copy_source_1895_65460:
                    should_copy_source_1895_65460()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", prog_num=65461):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-Reverb Stereo.xml", r".", prog_num=65462) as copy_file_to_dir_1896_65462:
                            copy_file_to_dir_1896_65462()
                        with ChmodAndChown(path=r"Waves-MannyM-Reverb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65463) as chmod_and_chown_1897_65463:
                            chmod_and_chown_1897_65463()
            with Stage(r"copy", r"Manny Marroquin Tone Shaper XML and Registry for Native Instruments", prog_num=65464):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65465) as should_copy_source_1898_65465:
                    should_copy_source_1898_65465()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", prog_num=65466):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MannyM-ToneShaper Stereo.xml", r".", prog_num=65467) as copy_file_to_dir_1899_65467:
                            copy_file_to_dir_1899_65467()
                        with ChmodAndChown(path=r"Waves-MannyM-ToneShaper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65468) as chmod_and_chown_1900_65468:
                            chmod_and_chown_1900_65468()
            with Stage(r"copy", r"MaxxBass XML and Registry for Native Instruments", prog_num=65469):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65470) as should_copy_source_1901_65470:
                    should_copy_source_1901_65470()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", prog_num=65471):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxBass Stereo.xml", r".", prog_num=65472) as copy_file_to_dir_1902_65472:
                            copy_file_to_dir_1902_65472()
                        with ChmodAndChown(path=r"Waves-MaxxBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65473) as chmod_and_chown_1903_65473:
                            chmod_and_chown_1903_65473()
            with Stage(r"copy", r"MaxxVolume XML and Registry for Native Instruments", prog_num=65474):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65475) as should_copy_source_1904_65475:
                    should_copy_source_1904_65475()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", prog_num=65476):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MaxxVolume Stereo.xml", r".", prog_num=65477) as copy_file_to_dir_1905_65477:
                            copy_file_to_dir_1905_65477()
                        with ChmodAndChown(path=r"Waves-MaxxVolume Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65478) as chmod_and_chown_1906_65478:
                            chmod_and_chown_1906_65478()
            with Stage(r"copy", r"MetaFilter XML and Registry for Native Instruments", prog_num=65479):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65480) as should_copy_source_1907_65480:
                    should_copy_source_1907_65480()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", prog_num=65481):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MetaFilter Stereo.xml", r".", prog_num=65482) as copy_file_to_dir_1908_65482:
                            copy_file_to_dir_1908_65482()
                        with ChmodAndChown(path=r"Waves-MetaFilter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65483) as chmod_and_chown_1909_65483:
                            chmod_and_chown_1909_65483()
            with Stage(r"copy", r"MondoMod XML and Registry for Native Instruments", prog_num=65484):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65485) as should_copy_source_1910_65485:
                    should_copy_source_1910_65485()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", prog_num=65486):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-MondoMod Stereo.xml", r".", prog_num=65487) as copy_file_to_dir_1911_65487:
                            copy_file_to_dir_1911_65487()
                        with ChmodAndChown(path=r"Waves-MondoMod Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65488) as chmod_and_chown_1912_65488:
                            chmod_and_chown_1912_65488()
            with Stage(r"copy", r"Morphoder XML and Registry for Native Instruments", prog_num=65489):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65490) as should_copy_source_1913_65490:
                    should_copy_source_1913_65490()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", prog_num=65491):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Morphoder Stereo.xml", r".", prog_num=65492) as copy_file_to_dir_1914_65492:
                            copy_file_to_dir_1914_65492()
                        with ChmodAndChown(path=r"Waves-Morphoder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65493) as chmod_and_chown_1915_65493:
                            chmod_and_chown_1915_65493()
            with Stage(r"copy", r"OneKnob Brighter XML and Registry for Native Instruments", prog_num=65494):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65495) as should_copy_source_1916_65495:
                    should_copy_source_1916_65495()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", prog_num=65496):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Brighter Stereo.xml", r".", prog_num=65497) as copy_file_to_dir_1917_65497:
                            copy_file_to_dir_1917_65497()
                        with ChmodAndChown(path=r"Waves-OneKnob Brighter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65498) as chmod_and_chown_1918_65498:
                            chmod_and_chown_1918_65498()
            with Stage(r"copy", r"OneKnob Driver XML and Registry for Native Instruments", prog_num=65499):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65500) as should_copy_source_1919_65500:
                    should_copy_source_1919_65500()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", prog_num=65501):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Driver Stereo.xml", r".", prog_num=65502) as copy_file_to_dir_1920_65502:
                            copy_file_to_dir_1920_65502()
                        with ChmodAndChown(path=r"Waves-OneKnob Driver Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65503) as chmod_and_chown_1921_65503:
                            chmod_and_chown_1921_65503()
            with Stage(r"copy", r"OneKnob Filter XML and Registry for Native Instruments", prog_num=65504):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65505) as should_copy_source_1922_65505:
                    should_copy_source_1922_65505()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", prog_num=65506):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Filter Stereo.xml", r".", prog_num=65507) as copy_file_to_dir_1923_65507:
                            copy_file_to_dir_1923_65507()
                        with ChmodAndChown(path=r"Waves-OneKnob Filter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65508) as chmod_and_chown_1924_65508:
                            chmod_and_chown_1924_65508()
            with Stage(r"copy", r"OneKnob Louder XML and Registry for Native Instruments", prog_num=65509):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65510) as should_copy_source_1925_65510:
                    should_copy_source_1925_65510()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", prog_num=65511):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Louder Stereo.xml", r".", prog_num=65512) as copy_file_to_dir_1926_65512:
                            copy_file_to_dir_1926_65512()
                        with ChmodAndChown(path=r"Waves-OneKnob Louder Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65513) as chmod_and_chown_1927_65513:
                            chmod_and_chown_1927_65513()
            with Stage(r"copy", r"OneKnob Phatter XML and Registry for Native Instruments", prog_num=65514):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65515) as should_copy_source_1928_65515:
                    should_copy_source_1928_65515()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", prog_num=65516):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Phatter Stereo.xml", r".", prog_num=65517) as copy_file_to_dir_1929_65517:
                            copy_file_to_dir_1929_65517()
                        with ChmodAndChown(path=r"Waves-OneKnob Phatter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65518) as chmod_and_chown_1930_65518:
                            chmod_and_chown_1930_65518()
            with Stage(r"copy", r"OneKnob Pressure XML and Registry for Native Instruments", prog_num=65519):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65520) as should_copy_source_1931_65520:
                    should_copy_source_1931_65520()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", prog_num=65521):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pressure Stereo.xml", r".", prog_num=65522) as copy_file_to_dir_1932_65522:
                            copy_file_to_dir_1932_65522()
                        with ChmodAndChown(path=r"Waves-OneKnob Pressure Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65523) as chmod_and_chown_1933_65523:
                            chmod_and_chown_1933_65523()
            with Stage(r"copy", r"OneKnob Pumper XML and Registry for Native Instruments", prog_num=65524):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65525) as should_copy_source_1934_65525:
                    should_copy_source_1934_65525()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", prog_num=65526):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Pumper Stereo.xml", r".", prog_num=65527) as copy_file_to_dir_1935_65527:
                            copy_file_to_dir_1935_65527()
                        with ChmodAndChown(path=r"Waves-OneKnob Pumper Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65528) as chmod_and_chown_1936_65528:
                            chmod_and_chown_1936_65528()
            with Stage(r"copy", r"OneKnob Wetter XML and Registry for Native Instruments", prog_num=65529):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65530) as should_copy_source_1937_65530:
                    should_copy_source_1937_65530()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", prog_num=65531):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OneKnob Wetter Stereo.xml", r".", prog_num=65532) as copy_file_to_dir_1938_65532:
                            copy_file_to_dir_1938_65532()
                        with ChmodAndChown(path=r"Waves-OneKnob Wetter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65533) as chmod_and_chown_1939_65533:
                            chmod_and_chown_1939_65533()
            with Stage(r"copy", r"OVox XML and Registry for Native Instruments", prog_num=65534):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65535) as should_copy_source_1940_65535:
                    should_copy_source_1940_65535()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", prog_num=65536):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-OVox Stereo.xml", r".", prog_num=65537) as copy_file_to_dir_1941_65537:
                            copy_file_to_dir_1941_65537()
                        with ChmodAndChown(path=r"Waves-OVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65538) as chmod_and_chown_1942_65538:
                            chmod_and_chown_1942_65538()
            with Stage(r"copy", r"PAZ XML and Registry for Native Instruments", prog_num=65539):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65540) as should_copy_source_1943_65540:
                    should_copy_source_1943_65540()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", prog_num=65541):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PAZ Stereo.xml", r".", prog_num=65542) as copy_file_to_dir_1944_65542:
                            copy_file_to_dir_1944_65542()
                        with ChmodAndChown(path=r"Waves-PAZ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65543) as chmod_and_chown_1945_65543:
                            chmod_and_chown_1945_65543()
            with Stage(r"copy", r"PRS Archon XML and Registry for Native Instruments", prog_num=65544):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65545) as should_copy_source_1946_65545:
                    should_copy_source_1946_65545()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", prog_num=65546):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Archon Stereo.xml", r".", prog_num=65547) as copy_file_to_dir_1947_65547:
                            copy_file_to_dir_1947_65547()
                        with ChmodAndChown(path=r"Waves-PRS Archon Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65548) as chmod_and_chown_1948_65548:
                            chmod_and_chown_1948_65548()
            with Stage(r"copy", r"PRS Dallas XML and Registry for Native Instruments", prog_num=65549):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65550) as should_copy_source_1949_65550:
                    should_copy_source_1949_65550()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", prog_num=65551):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS Dallas Stereo.xml", r".", prog_num=65552) as copy_file_to_dir_1950_65552:
                            copy_file_to_dir_1950_65552()
                        with ChmodAndChown(path=r"Waves-PRS Dallas Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65553) as chmod_and_chown_1951_65553:
                            chmod_and_chown_1951_65553()
            with Stage(r"copy", r"PRS V9 XML and Registry for Native Instruments", prog_num=65554):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65555) as should_copy_source_1952_65555:
                    should_copy_source_1952_65555()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", prog_num=65556):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PRS V9 Stereo.xml", r".", prog_num=65557) as copy_file_to_dir_1953_65557:
                            copy_file_to_dir_1953_65557()
                        with ChmodAndChown(path=r"Waves-PRS V9 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65558) as chmod_and_chown_1954_65558:
                            chmod_and_chown_1954_65558()
            with Stage(r"copy", r"PS22 XML and Registry for Native Instruments", prog_num=65559):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65560) as should_copy_source_1955_65560:
                    should_copy_source_1955_65560()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", prog_num=65561):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PS22 Stereo.xml", r".", prog_num=65562) as copy_file_to_dir_1956_65562:
                            copy_file_to_dir_1956_65562()
                        with ChmodAndChown(path=r"Waves-PS22 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65563) as chmod_and_chown_1957_65563:
                            chmod_and_chown_1957_65563()
            with Stage(r"copy", r"PuigChild Compressor XML and Registry for Native Instruments", prog_num=65564):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65565) as should_copy_source_1958_65565:
                    should_copy_source_1958_65565()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", prog_num=65566):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 660 Mono.xml", r".", prog_num=65567) as copy_file_to_dir_1959_65567:
                            copy_file_to_dir_1959_65567()
                        with ChmodAndChown(path=r"Waves-PuigChild 660 Mono.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65568) as chmod_and_chown_1960_65568:
                            chmod_and_chown_1960_65568()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65569) as should_copy_source_1961_65569:
                    should_copy_source_1961_65569()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", prog_num=65570):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigChild 670 Stereo.xml", r".", prog_num=65571) as copy_file_to_dir_1962_65571:
                            copy_file_to_dir_1962_65571()
                        with ChmodAndChown(path=r"Waves-PuigChild 670 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65572) as chmod_and_chown_1963_65572:
                            chmod_and_chown_1963_65572()
            with Stage(r"copy", r"PuigTec EQP1A XML and Registry for Native Instruments", prog_num=65573):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65574) as should_copy_source_1964_65574:
                    should_copy_source_1964_65574()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", prog_num=65575):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec EQP1A Stereo.xml", r".", prog_num=65576) as copy_file_to_dir_1965_65576:
                            copy_file_to_dir_1965_65576()
                        with ChmodAndChown(path=r"Waves-PuigTec EQP1A Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65577) as chmod_and_chown_1966_65577:
                            chmod_and_chown_1966_65577()
            with Stage(r"copy", r"PuigTec MEQ5 XML and Registry for Native Instruments", prog_num=65578):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65579) as should_copy_source_1967_65579:
                    should_copy_source_1967_65579()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", prog_num=65580):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-PuigTec MEQ5 Stereo.xml", r".", prog_num=65581) as copy_file_to_dir_1968_65581:
                            copy_file_to_dir_1968_65581()
                        with ChmodAndChown(path=r"Waves-PuigTec MEQ5 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65582) as chmod_and_chown_1969_65582:
                            chmod_and_chown_1969_65582()
            with Stage(r"copy", r"Q10 XML and Registry for Native Instruments", prog_num=65583):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65584) as should_copy_source_1970_65584:
                    should_copy_source_1970_65584()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", prog_num=65585):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q10 Stereo.xml", r".", prog_num=65586) as copy_file_to_dir_1971_65586:
                            copy_file_to_dir_1971_65586()
                        with ChmodAndChown(path=r"Waves-Q10 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65587) as chmod_and_chown_1972_65587:
                            chmod_and_chown_1972_65587()
            with Stage(r"copy", r"Q-Clone XML and Registry for Native Instruments", prog_num=65588):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65589) as should_copy_source_1973_65589:
                    should_copy_source_1973_65589()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", prog_num=65590):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Q-Clone Stereo.xml", r".", prog_num=65591) as copy_file_to_dir_1974_65591:
                            copy_file_to_dir_1974_65591()
                        with ChmodAndChown(path=r"Waves-Q-Clone Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65592) as chmod_and_chown_1975_65592:
                            chmod_and_chown_1975_65592()
            with Stage(r"copy", r"RBass XML and Registry for Native Instruments", prog_num=65593):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65594) as should_copy_source_1976_65594:
                    should_copy_source_1976_65594()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", prog_num=65595):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RBass Stereo.xml", r".", prog_num=65596) as copy_file_to_dir_1977_65596:
                            copy_file_to_dir_1977_65596()
                        with ChmodAndChown(path=r"Waves-RBass Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65597) as chmod_and_chown_1978_65597:
                            chmod_and_chown_1978_65597()
            with Stage(r"copy", r"RChannel XML and Registry for Native Instruments", prog_num=65598):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65599) as should_copy_source_1979_65599:
                    should_copy_source_1979_65599()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", prog_num=65600):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RChannel Stereo.xml", r".", prog_num=65601) as copy_file_to_dir_1980_65601:
                            copy_file_to_dir_1980_65601()
                        with ChmodAndChown(path=r"Waves-RChannel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65602) as chmod_and_chown_1981_65602:
                            chmod_and_chown_1981_65602()
            with Stage(r"copy", r"RCompressor XML and Registry for Native Instruments", prog_num=65603):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65604) as should_copy_source_1982_65604:
                    should_copy_source_1982_65604()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", prog_num=65605):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RCompressor Stereo.xml", r".", prog_num=65606) as copy_file_to_dir_1983_65606:
                            copy_file_to_dir_1983_65606()
                        with ChmodAndChown(path=r"Waves-RCompressor Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65607) as chmod_and_chown_1984_65607:
                            chmod_and_chown_1984_65607()
            with Stage(r"copy", r"REDD17 XML and Registry for Native Instruments", prog_num=65608):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65609) as should_copy_source_1985_65609:
                    should_copy_source_1985_65609()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", prog_num=65610):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD17 Stereo.xml", r".", prog_num=65611) as copy_file_to_dir_1986_65611:
                            copy_file_to_dir_1986_65611()
                        with ChmodAndChown(path=r"Waves-REDD17 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65612) as chmod_and_chown_1987_65612:
                            chmod_and_chown_1987_65612()
            with Stage(r"copy", r"REDD37-51 XML and Registry for Native Instruments", prog_num=65613):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65614) as should_copy_source_1988_65614:
                    should_copy_source_1988_65614()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", prog_num=65615):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REDD37-51 Stereo.xml", r".", prog_num=65616) as copy_file_to_dir_1989_65616:
                            copy_file_to_dir_1989_65616()
                        with ChmodAndChown(path=r"Waves-REDD37-51 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65617) as chmod_and_chown_1990_65617:
                            chmod_and_chown_1990_65617()
            with Stage(r"copy", r"REQ 6 XML and Registry for Native Instruments", prog_num=65618):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65619) as should_copy_source_1991_65619:
                    should_copy_source_1991_65619()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", prog_num=65620):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-REQ 6 Stereo.xml", r".", prog_num=65621) as copy_file_to_dir_1992_65621:
                            copy_file_to_dir_1992_65621()
                        with ChmodAndChown(path=r"Waves-REQ 6 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65622) as chmod_and_chown_1993_65622:
                            chmod_and_chown_1993_65622()
            with Stage(r"copy", r"RS56 XML and Registry for Native Instruments", prog_num=65623):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65624) as should_copy_source_1994_65624:
                    should_copy_source_1994_65624()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", prog_num=65625):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RS56 Stereo.xml", r".", prog_num=65626) as copy_file_to_dir_1995_65626:
                            copy_file_to_dir_1995_65626()
                        with ChmodAndChown(path=r"Waves-RS56 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65627) as chmod_and_chown_1996_65627:
                            chmod_and_chown_1996_65627()
            with Stage(r"copy", r"RVerb XML and Registry for Native Instruments", prog_num=65628):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65629) as should_copy_source_1997_65629:
                    should_copy_source_1997_65629()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", prog_num=65630):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVerb Stereo.xml", r".", prog_num=65631) as copy_file_to_dir_1998_65631:
                            copy_file_to_dir_1998_65631()
                        with ChmodAndChown(path=r"Waves-RVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65632) as chmod_and_chown_1999_65632:
                            chmod_and_chown_1999_65632()
            with Stage(r"copy", r"RVox XML and Registry for Native Instruments", prog_num=65633):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65634) as should_copy_source_2000_65634:
                    should_copy_source_2000_65634()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", prog_num=65635):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-RVox Stereo.xml", r".", prog_num=65636) as copy_file_to_dir_2001_65636:
                            copy_file_to_dir_2001_65636()
                        with ChmodAndChown(path=r"Waves-RVox Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65637) as chmod_and_chown_2002_65637:
                            chmod_and_chown_2002_65637()
            with Stage(r"copy", r"Reel ADT XML and Registry for Native Instruments", prog_num=65638):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65639) as should_copy_source_2003_65639:
                    should_copy_source_2003_65639()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", prog_num=65640):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Reel ADT Stereo.xml", r".", prog_num=65641) as copy_file_to_dir_2004_65641:
                            copy_file_to_dir_2004_65641()
                        with ChmodAndChown(path=r"Waves-Reel ADT Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65642) as chmod_and_chown_2005_65642:
                            chmod_and_chown_2005_65642()
            with Stage(r"copy", r"S1 Imager XML and Registry for Native Instruments", prog_num=65643):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65644) as should_copy_source_2006_65644:
                    should_copy_source_2006_65644()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", prog_num=65645):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Imager Stereo.xml", r".", prog_num=65646) as copy_file_to_dir_2007_65646:
                            copy_file_to_dir_2007_65646()
                        with ChmodAndChown(path=r"Waves-S1 Imager Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65647) as chmod_and_chown_2008_65647:
                            chmod_and_chown_2008_65647()
            with Stage(r"copy", r"S1 Shuffler XML and Registry for Native Instruments", prog_num=65648):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65649) as should_copy_source_2009_65649:
                    should_copy_source_2009_65649()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", prog_num=65650):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-S1 Shuffler Stereo.xml", r".", prog_num=65651) as copy_file_to_dir_2010_65651:
                            copy_file_to_dir_2010_65651()
                        with ChmodAndChown(path=r"Waves-S1 Shuffler Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65652) as chmod_and_chown_2011_65652:
                            chmod_and_chown_2011_65652()
            with Stage(r"copy", r"SSLComp XML and Registry for Native Instruments", prog_num=65653):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65654) as should_copy_source_2012_65654:
                    should_copy_source_2012_65654()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", prog_num=65655):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLComp Stereo.xml", r".", prog_num=65656) as copy_file_to_dir_2013_65656:
                            copy_file_to_dir_2013_65656()
                        with ChmodAndChown(path=r"Waves-SSLComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65657) as chmod_and_chown_2014_65657:
                            chmod_and_chown_2014_65657()
            with Stage(r"copy", r"SSLEQ XML and Registry for Native Instruments", prog_num=65658):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65659) as should_copy_source_2015_65659:
                    should_copy_source_2015_65659()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", prog_num=65660):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSLEQ Stereo.xml", r".", prog_num=65661) as copy_file_to_dir_2016_65661:
                            copy_file_to_dir_2016_65661()
                        with ChmodAndChown(path=r"Waves-SSLEQ Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65662) as chmod_and_chown_2017_65662:
                            chmod_and_chown_2017_65662()
            with Stage(r"copy", r"SSL E-Channel XML and Registry for Native Instruments", prog_num=65663):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65664) as should_copy_source_2018_65664:
                    should_copy_source_2018_65664()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", prog_num=65665):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL E-Channel Stereo.xml", r".", prog_num=65666) as copy_file_to_dir_2019_65666:
                            copy_file_to_dir_2019_65666()
                        with ChmodAndChown(path=r"Waves-SSL E-Channel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65667) as chmod_and_chown_2020_65667:
                            chmod_and_chown_2020_65667()
            with Stage(r"copy", r"SSL G-Channel XML and Registry for Native Instruments", prog_num=65668):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65669) as should_copy_source_2021_65669:
                    should_copy_source_2021_65669()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", prog_num=65670):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SSL G-Channel Stereo.xml", r".", prog_num=65671) as copy_file_to_dir_2022_65671:
                            copy_file_to_dir_2022_65671()
                        with ChmodAndChown(path=r"Waves-SSL G-Channel Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65672) as chmod_and_chown_2023_65672:
                            chmod_and_chown_2023_65672()
            with Stage(r"copy", r"Scheps 73 XML and Registry for Native Instruments", prog_num=65673):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65674) as should_copy_source_2024_65674:
                    should_copy_source_2024_65674()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", prog_num=65675):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps 73 Stereo.xml", r".", prog_num=65676) as copy_file_to_dir_2025_65676:
                            copy_file_to_dir_2025_65676()
                        with ChmodAndChown(path=r"Waves-Scheps 73 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65677) as chmod_and_chown_2026_65677:
                            chmod_and_chown_2026_65677()
            with Stage(r"copy", r"Scheps Parallel Particles XML and Registry for Native Instruments", prog_num=65678):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65679) as should_copy_source_2027_65679:
                    should_copy_source_2027_65679()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", prog_num=65680):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Scheps Parallel Particles Stereo.xml", r".", prog_num=65681) as copy_file_to_dir_2028_65681:
                            copy_file_to_dir_2028_65681()
                        with ChmodAndChown(path=r"Waves-Scheps Parallel Particles Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65682) as chmod_and_chown_2029_65682:
                            chmod_and_chown_2029_65682()
            with Stage(r"copy", r"Smack Attack XML and Registry for Native Instruments", prog_num=65683):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65684) as should_copy_source_2030_65684:
                    should_copy_source_2030_65684()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", prog_num=65685):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Smack Attack Stereo.xml", r".", prog_num=65686) as copy_file_to_dir_2031_65686:
                            copy_file_to_dir_2031_65686()
                        with ChmodAndChown(path=r"Waves-Smack Attack Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65687) as chmod_and_chown_2032_65687:
                            chmod_and_chown_2032_65687()
            with Stage(r"copy", r"SoundShifter XML and Registry for Native Instruments", prog_num=65688):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65689) as should_copy_source_2033_65689:
                    should_copy_source_2033_65689()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", prog_num=65690):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SoundShifter Stereo.xml", r".", prog_num=65691) as copy_file_to_dir_2034_65691:
                            copy_file_to_dir_2034_65691()
                        with ChmodAndChown(path=r"Waves-SoundShifter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65692) as chmod_and_chown_2035_65692:
                            chmod_and_chown_2035_65692()
            with Stage(r"copy", r"Submarine XML and Registry for Native Instruments", prog_num=65693):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65694) as should_copy_source_2036_65694:
                    should_copy_source_2036_65694()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", prog_num=65695):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Submarine Stereo.xml", r".", prog_num=65696) as copy_file_to_dir_2037_65696:
                            copy_file_to_dir_2037_65696()
                        with ChmodAndChown(path=r"Waves-Submarine Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65697) as chmod_and_chown_2038_65697:
                            chmod_and_chown_2038_65697()
            with Stage(r"copy", r"SuperTap 2-Taps XML and Registry for Native Instruments", prog_num=65698):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65699) as should_copy_source_2039_65699:
                    should_copy_source_2039_65699()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", prog_num=65700):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 2-Taps Stereo.xml", r".", prog_num=65701) as copy_file_to_dir_2040_65701:
                            copy_file_to_dir_2040_65701()
                        with ChmodAndChown(path=r"Waves-SuperTap 2-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65702) as chmod_and_chown_2041_65702:
                            chmod_and_chown_2041_65702()
            with Stage(r"copy", r"SuperTap 6-Taps XML and Registry for Native Instruments", prog_num=65703):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65704) as should_copy_source_2042_65704:
                    should_copy_source_2042_65704()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", prog_num=65705):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-SuperTap 6-Taps Stereo.xml", r".", prog_num=65706) as copy_file_to_dir_2043_65706:
                            copy_file_to_dir_2043_65706()
                        with ChmodAndChown(path=r"Waves-SuperTap 6-Taps Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65707) as chmod_and_chown_2044_65707:
                            chmod_and_chown_2044_65707()
            with Stage(r"copy", r"TG12345 XML and Registry for Native Instruments", prog_num=65708):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65709) as should_copy_source_2045_65709:
                    should_copy_source_2045_65709()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", prog_num=65710):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TG12345 Stereo.xml", r".", prog_num=65711) as copy_file_to_dir_2046_65711:
                            copy_file_to_dir_2046_65711()
                        with ChmodAndChown(path=r"Waves-TG12345 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65712) as chmod_and_chown_2047_65712:
                            chmod_and_chown_2047_65712()
            with Stage(r"copy", r"Torque XML and Registry for Native Instruments", prog_num=65713):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65714) as should_copy_source_2048_65714:
                    should_copy_source_2048_65714()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", prog_num=65715):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Torque Stereo.xml", r".", prog_num=65716) as copy_file_to_dir_2049_65716:
                            copy_file_to_dir_2049_65716()
                        with ChmodAndChown(path=r"Waves-Torque Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65717) as chmod_and_chown_2050_65717:
                            chmod_and_chown_2050_65717()
            with Stage(r"copy", r"TransX Multi XML and Registry for Native Instruments", prog_num=65718):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65719) as should_copy_source_2051_65719:
                    should_copy_source_2051_65719()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", prog_num=65720):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Multi Stereo.xml", r".", prog_num=65721) as copy_file_to_dir_2052_65721:
                            copy_file_to_dir_2052_65721()
                        with ChmodAndChown(path=r"Waves-TransX Multi Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65722) as chmod_and_chown_2053_65722:
                            chmod_and_chown_2053_65722()
            with Stage(r"copy", r"TransX Wide XML and Registry for Native Instruments", prog_num=65723):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65724) as should_copy_source_2054_65724:
                    should_copy_source_2054_65724()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", prog_num=65725):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TransX Wide Stereo.xml", r".", prog_num=65726) as copy_file_to_dir_2055_65726:
                            copy_file_to_dir_2055_65726()
                        with ChmodAndChown(path=r"Waves-TransX Wide Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65727) as chmod_and_chown_2056_65727:
                            chmod_and_chown_2056_65727()
            with Stage(r"copy", r"TrueVerb XML and Registry for Native Instruments", prog_num=65728):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65729) as should_copy_source_2057_65729:
                    should_copy_source_2057_65729()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", prog_num=65730):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-TrueVerb Stereo.xml", r".", prog_num=65731) as copy_file_to_dir_2058_65731:
                            copy_file_to_dir_2058_65731()
                        with ChmodAndChown(path=r"Waves-TrueVerb Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65732) as chmod_and_chown_2059_65732:
                            chmod_and_chown_2059_65732()
            with Stage(r"copy", r"UltraPitch XML and Registry for Native Instruments", prog_num=65733):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65734) as should_copy_source_2060_65734:
                    should_copy_source_2060_65734()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", prog_num=65735):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 3 Voices Stereo.xml", r".", prog_num=65736) as copy_file_to_dir_2061_65736:
                            copy_file_to_dir_2061_65736()
                        with ChmodAndChown(path=r"Waves-UltraPitch 3 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65737) as chmod_and_chown_2062_65737:
                            chmod_and_chown_2062_65737()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65738) as should_copy_source_2063_65738:
                    should_copy_source_2063_65738()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", prog_num=65739):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch 6 Voices Stereo.xml", r".", prog_num=65740) as copy_file_to_dir_2064_65740:
                            copy_file_to_dir_2064_65740()
                        with ChmodAndChown(path=r"Waves-UltraPitch 6 Voices Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65741) as chmod_and_chown_2065_65741:
                            chmod_and_chown_2065_65741()
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65742) as should_copy_source_2066_65742:
                    should_copy_source_2066_65742()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", prog_num=65743):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-UltraPitch Shift Stereo.xml", r".", prog_num=65744) as copy_file_to_dir_2067_65744:
                            copy_file_to_dir_2067_65744()
                        with ChmodAndChown(path=r"Waves-UltraPitch Shift Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65745) as chmod_and_chown_2068_65745:
                            chmod_and_chown_2068_65745()
            with Stage(r"copy", r"VComp XML and Registry for Native Instruments", prog_num=65746):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65747) as should_copy_source_2069_65747:
                    should_copy_source_2069_65747()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", prog_num=65748):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VComp Stereo.xml", r".", prog_num=65749) as copy_file_to_dir_2070_65749:
                            copy_file_to_dir_2070_65749()
                        with ChmodAndChown(path=r"Waves-VComp Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65750) as chmod_and_chown_2071_65750:
                            chmod_and_chown_2071_65750()
            with Stage(r"copy", r"VEQ4 XML and Registry for Native Instruments", prog_num=65751):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65752) as should_copy_source_2072_65752:
                    should_copy_source_2072_65752()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", prog_num=65753):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VEQ4 Stereo.xml", r".", prog_num=65754) as copy_file_to_dir_2073_65754:
                            copy_file_to_dir_2073_65754()
                        with ChmodAndChown(path=r"Waves-VEQ4 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65755) as chmod_and_chown_2074_65755:
                            chmod_and_chown_2074_65755()
            with Stage(r"copy", r"VU Meter XML and Registry for Native Instruments", prog_num=65756):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65757) as should_copy_source_2075_65757:
                    should_copy_source_2075_65757()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", prog_num=65758):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-VU Meter Stereo.xml", r".", prog_num=65759) as copy_file_to_dir_2076_65759:
                            copy_file_to_dir_2076_65759()
                        with ChmodAndChown(path=r"Waves-VU Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65760) as chmod_and_chown_2077_65760:
                            chmod_and_chown_2077_65760()
            with Stage(r"copy", r"Vitamin XML and Registry for Native Instruments", prog_num=65761):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65762) as should_copy_source_2078_65762:
                    should_copy_source_2078_65762()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", prog_num=65763):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Vitamin Stereo.xml", r".", prog_num=65764) as copy_file_to_dir_2079_65764:
                            copy_file_to_dir_2079_65764()
                        with ChmodAndChown(path=r"Waves-Vitamin Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65765) as chmod_and_chown_2080_65765:
                            chmod_and_chown_2080_65765()
            with Stage(r"copy", r"W43 XML and Registry for Native Instruments", prog_num=65766):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65767) as should_copy_source_2081_65767:
                    should_copy_source_2081_65767()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", prog_num=65768):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-W43 Stereo.xml", r".", prog_num=65769) as copy_file_to_dir_2082_65769:
                            copy_file_to_dir_2082_65769()
                        with ChmodAndChown(path=r"Waves-W43 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65770) as chmod_and_chown_2083_65770:
                            chmod_and_chown_2083_65770()
            with Stage(r"copy", r"WLM Meter XML and Registry for Native Instruments", prog_num=65771):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65772) as should_copy_source_2084_65772:
                    should_copy_source_2084_65772()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", prog_num=65773):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WLM Meter Stereo.xml", r".", prog_num=65774) as copy_file_to_dir_2085_65774:
                            copy_file_to_dir_2085_65774()
                        with ChmodAndChown(path=r"Waves-WLM Meter Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65775) as chmod_and_chown_2086_65775:
                            chmod_and_chown_2086_65775()
            with Stage(r"copy", r"WNS XML and Registry for Native Instruments", prog_num=65776):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65777) as should_copy_source_2087_65777:
                    should_copy_source_2087_65777()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", prog_num=65778):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-WNS Stereo.xml", r".", prog_num=65779) as copy_file_to_dir_2088_65779:
                            copy_file_to_dir_2088_65779()
                        with ChmodAndChown(path=r"Waves-WNS Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65780) as chmod_and_chown_2089_65780:
                            chmod_and_chown_2089_65780()
            with Stage(r"copy", r"Waves Tune Real-Time XML and Registry for Native Instruments", prog_num=65781):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65782) as should_copy_source_2090_65782:
                    should_copy_source_2090_65782()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", prog_num=65783):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-Waves Tune Real-Time Stereo.xml", r".", prog_num=65784) as copy_file_to_dir_2091_65784:
                            copy_file_to_dir_2091_65784()
                        with ChmodAndChown(path=r"Waves-Waves Tune Real-Time Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65785) as chmod_and_chown_2092_65785:
                            chmod_and_chown_2092_65785()
            with Stage(r"copy", r"X-Crackle XML and Registry for Native Instruments", prog_num=65786):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65787) as should_copy_source_2093_65787:
                    should_copy_source_2093_65787()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", prog_num=65788):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Crackle Stereo.xml", r".", prog_num=65789) as copy_file_to_dir_2094_65789:
                            copy_file_to_dir_2094_65789()
                        with ChmodAndChown(path=r"Waves-X-Crackle Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65790) as chmod_and_chown_2095_65790:
                            chmod_and_chown_2095_65790()
            with Stage(r"copy", r"X-Hum XML and Registry for Native Instruments", prog_num=65791):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65792) as should_copy_source_2096_65792:
                    should_copy_source_2096_65792()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", prog_num=65793):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-X-Hum Stereo.xml", r".", prog_num=65794) as copy_file_to_dir_2097_65794:
                            copy_file_to_dir_2097_65794()
                        with ChmodAndChown(path=r"Waves-X-Hum Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65795) as chmod_and_chown_2098_65795:
                            chmod_and_chown_2098_65795()
            with Stage(r"copy", r"dbx-160 XML and Registry for Native Instruments", prog_num=65796):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", r"/Library/Application Support/Native Instruments/Service Center", skip_progress_count=3, prog_num=65797) as should_copy_source_2099_65797:
                    should_copy_source_2099_65797()
                    with Stage(r"copy source", r"Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", prog_num=65798):
                        with CopyFileToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Common/Data/NKS FX/XML/Waves-dbx-160 Stereo.xml", r".", prog_num=65799) as copy_file_to_dir_2100_65799:
                            copy_file_to_dir_2100_65799()
                        with ChmodAndChown(path=r"Waves-dbx-160 Stereo.xml", mode="a+rw", user_id=-1, group_id=-1, prog_num=65800) as chmod_and_chown_2101_65800:
                            chmod_and_chown_2101_65800()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Aphex Vintage Exciter", "NKS_DATA_VERSION": "1.0"}, prog_num=65801) as resolve_config_vars_in_file_2102_65801:
                resolve_config_vars_in_file_2102_65801()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Aphex Vintage Exciter Stereo.plist", ignore_all_errors=True), prog_num=65802) as if_2103_65802:
                if_2103_65802()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "AudioTrack", "NKS_DATA_VERSION": "1.0"}, prog_num=65803) as resolve_config_vars_in_file_2104_65803:
                resolve_config_vars_in_file_2104_65803()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-AudioTrack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-AudioTrack Stereo.plist", ignore_all_errors=True), prog_num=65804) as if_2105_65804:
                if_2105_65804()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Fingers", "NKS_DATA_VERSION": "1.0"}, prog_num=65805) as resolve_config_vars_in_file_2106_65805:
                resolve_config_vars_in_file_2106_65805()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Fingers Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Fingers Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Fingers Stereo.plist", ignore_all_errors=True), prog_num=65806) as if_2107_65806:
                if_2107_65806()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Slapper", "NKS_DATA_VERSION": "2.0"}, prog_num=65807) as resolve_config_vars_in_file_2108_65807:
                resolve_config_vars_in_file_2108_65807()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Slapper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Slapper Stereo.plist", ignore_all_errors=True), prog_num=65808) as if_2109_65808:
                if_2109_65808()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Bass Rider", "NKS_DATA_VERSION": "1.0"}, prog_num=65809) as resolve_config_vars_in_file_2110_65809:
                resolve_config_vars_in_file_2110_65809()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Bass Rider Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Bass Rider Stereo.plist", ignore_all_errors=True), prog_num=65810) as if_2111_65810:
                if_2111_65810()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Brauer Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=65811) as resolve_config_vars_in_file_2112_65811:
                resolve_config_vars_in_file_2112_65811()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Brauer Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Brauer Motion Stereo.plist", ignore_all_errors=True), prog_num=65812) as if_2113_65812:
                if_2113_65812()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Butch Vig Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=65813) as resolve_config_vars_in_file_2114_65813:
                resolve_config_vars_in_file_2114_65813()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Butch Vig Vocals Stereo.plist", ignore_all_errors=True), prog_num=65814) as if_2115_65814:
                if_2115_65814()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C1 comp-gate", "NKS_DATA_VERSION": "1.0"}, prog_num=65815) as resolve_config_vars_in_file_2116_65815:
                resolve_config_vars_in_file_2116_65815()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C1 comp-gate Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C1 comp-gate Stereo.plist", ignore_all_errors=True), prog_num=65816) as if_2117_65816:
                if_2117_65816()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C4", "NKS_DATA_VERSION": "1.0"}, prog_num=65817) as resolve_config_vars_in_file_2118_65817:
                resolve_config_vars_in_file_2118_65817()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C4 Stereo.plist", ignore_all_errors=True), prog_num=65818) as if_2119_65818:
                if_2119_65818()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "C6", "NKS_DATA_VERSION": "1.0"}, prog_num=65819) as resolve_config_vars_in_file_2120_65819:
                resolve_config_vars_in_file_2120_65819()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-C6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-C6 Stereo.plist", ignore_all_errors=True), prog_num=65820) as if_2121_65820:
                if_2121_65820()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-2A", "NKS_DATA_VERSION": "1.0"}, prog_num=65821) as resolve_config_vars_in_file_2122_65821:
                resolve_config_vars_in_file_2122_65821()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-2A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-2A Stereo.plist", ignore_all_errors=True), prog_num=65822) as if_2123_65822:
                if_2123_65822()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-3A", "NKS_DATA_VERSION": "1.0"}, prog_num=65823) as resolve_config_vars_in_file_2124_65823:
                resolve_config_vars_in_file_2124_65823()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-3A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-3A Stereo.plist", ignore_all_errors=True), prog_num=65824) as if_2125_65824:
                if_2125_65824()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CLA-76", "NKS_DATA_VERSION": "1.0"}, prog_num=65825) as resolve_config_vars_in_file_2126_65825:
                resolve_config_vars_in_file_2126_65825()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CLA-76 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CLA-76 Stereo.plist", ignore_all_errors=True), prog_num=65826) as if_2127_65826:
                if_2127_65826()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "CODEX", "NKS_DATA_VERSION": "1.0"}, prog_num=65827) as resolve_config_vars_in_file_2128_65827:
                resolve_config_vars_in_file_2128_65827()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CODEX Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-CODEX Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-CODEX Stereo.plist", ignore_all_errors=True), prog_num=65828) as if_2129_65828:
                if_2129_65828()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Center", "NKS_DATA_VERSION": "1.0"}, prog_num=65829) as resolve_config_vars_in_file_2130_65829:
                resolve_config_vars_in_file_2130_65829()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Center Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Center Stereo.plist", ignore_all_errors=True), prog_num=65830) as if_2131_65830:
                if_2131_65830()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Clavinet", "NKS_DATA_VERSION": "1.0"}, prog_num=65831) as resolve_config_vars_in_file_2132_65831:
                resolve_config_vars_in_file_2132_65831()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Clavinet Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Clavinet Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Clavinet Stereo.plist", ignore_all_errors=True), prog_num=65832) as if_2133_65832:
                if_2133_65832()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "DPR-402", "NKS_DATA_VERSION": "1.0"}, prog_num=65833) as resolve_config_vars_in_file_2134_65833:
                resolve_config_vars_in_file_2134_65833()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-DPR-402 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-DPR-402 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-DPR-402 Stereo.plist", ignore_all_errors=True), prog_num=65834) as if_2135_65834:
                if_2135_65834()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Dorrough", "NKS_DATA_VERSION": "1.0"}, prog_num=65835) as resolve_config_vars_in_file_2136_65835:
                resolve_config_vars_in_file_2136_65835()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Dorrough Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Dorrough Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Dorrough Stereo.plist", ignore_all_errors=True), prog_num=65836) as if_2137_65836:
                if_2137_65836()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-D5", "NKS_DATA_VERSION": "1.0"}, prog_num=65837) as resolve_config_vars_in_file_2138_65837:
                resolve_config_vars_in_file_2138_65837()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-D5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-D5 Stereo.plist", ignore_all_errors=True), prog_num=65838) as if_2139_65838:
                if_2139_65838()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-F2", "NKS_DATA_VERSION": "1.0"}, prog_num=65839) as resolve_config_vars_in_file_2140_65839:
                resolve_config_vars_in_file_2140_65839()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-F2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-F2 Stereo.plist", ignore_all_errors=True), prog_num=65840) as if_2141_65840:
                if_2141_65840()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "EMO-Q4", "NKS_DATA_VERSION": "1.0"}, prog_num=65841) as resolve_config_vars_in_file_2142_65841:
                resolve_config_vars_in_file_2142_65841()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-EMO-Q4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-EMO-Q4 Stereo.plist", ignore_all_errors=True), prog_num=65842) as if_2143_65842:
                if_2143_65842()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric200", "NKS_DATA_VERSION": "1.0"}, prog_num=65843) as resolve_config_vars_in_file_2144_65843:
                resolve_config_vars_in_file_2144_65843()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric200 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric200 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric200 Stereo.plist", ignore_all_errors=True), prog_num=65844) as if_2145_65844:
                if_2145_65844()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric88", "NKS_DATA_VERSION": "1.0"}, prog_num=65845) as resolve_config_vars_in_file_2146_65845:
                resolve_config_vars_in_file_2146_65845()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric88 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric88 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric88 Stereo.plist", ignore_all_errors=True), prog_num=65846) as if_2147_65846:
                if_2147_65846()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Electric Grand 80", "NKS_DATA_VERSION": "1.0"}, prog_num=65847) as resolve_config_vars_in_file_2148_65847:
                resolve_config_vars_in_file_2148_65847()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Electric Grand 80 Stereo.plist", ignore_all_errors=True), prog_num=65848) as if_2149_65848:
                if_2149_65848()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Element", "NKS_DATA_VERSION": "1.0"}, prog_num=65849) as resolve_config_vars_in_file_2150_65849:
                resolve_config_vars_in_file_2150_65849()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Element Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Element Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Element Stereo.plist", ignore_all_errors=True), prog_num=65850) as if_2151_65850:
                if_2151_65850()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Enigma", "NKS_DATA_VERSION": "1.0"}, prog_num=65851) as resolve_config_vars_in_file_2152_65851:
                resolve_config_vars_in_file_2152_65851()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Enigma Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Enigma Stereo.plist", ignore_all_errors=True), prog_num=65852) as if_2153_65852:
                if_2153_65852()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "F6", "NKS_DATA_VERSION": "1.0"}, prog_num=65853) as resolve_config_vars_in_file_2154_65853:
                resolve_config_vars_in_file_2154_65853()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-F6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-F6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-F6 Stereo.plist", ignore_all_errors=True), prog_num=65854) as if_2155_65854:
                if_2155_65854()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Flow Motion", "NKS_DATA_VERSION": "1.0"}, prog_num=65855) as resolve_config_vars_in_file_2156_65855:
                resolve_config_vars_in_file_2156_65855()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Flow Motion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Flow Motion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Flow Motion Stereo.plist", ignore_all_errors=True), prog_num=65856) as if_2157_65856:
                if_2157_65856()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GEQ Classic", "NKS_DATA_VERSION": "1.0"}, prog_num=65857) as resolve_config_vars_in_file_2158_65857:
                resolve_config_vars_in_file_2158_65857()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Classic Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Classic Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Classic Stereo.plist", ignore_all_errors=True), prog_num=65858) as if_2159_65858:
                if_2159_65858()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GEQ Modern", "NKS_DATA_VERSION": "1.0"}, prog_num=65859) as resolve_config_vars_in_file_2160_65859:
                resolve_config_vars_in_file_2160_65859()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Modern Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GEQ Modern Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GEQ Modern Stereo.plist", ignore_all_errors=True), prog_num=65860) as if_2161_65860:
                if_2161_65860()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.Instrument_Data_NKS.plist.template", r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Grand Rhapsody", "NKS_DATA_VERSION": "1.0"}, prog_num=65861) as resolve_config_vars_in_file_2162_65861:
                resolve_config_vars_in_file_2162_65861()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Stereo.plist", ignore_all_errors=True), prog_num=65862) as if_2163_65862:
                if_2163_65862()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Grand Rhapsody Piano Stereo.plist", prog_num=65863) as rm_file_or_dir_2164_65863:
                rm_file_or_dir_2164_65863()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells MixCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65864) as resolve_config_vars_in_file_2165_65864:
                resolve_config_vars_in_file_2165_65864()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells MixCentric Stereo.plist", ignore_all_errors=True), prog_num=65865) as if_2166_65865:
                if_2166_65865()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Greg Wells PianoCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65866) as resolve_config_vars_in_file_2167_65866:
                resolve_config_vars_in_file_2167_65866()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Greg Wells PianoCentric Stereo.plist", ignore_all_errors=True), prog_num=65867) as if_2168_65867:
                if_2168_65867()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW ToneCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65868) as resolve_config_vars_in_file_2169_65868:
                resolve_config_vars_in_file_2169_65868()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW ToneCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW ToneCentric Stereo.plist", ignore_all_errors=True), prog_num=65869) as if_2170_65869:
                if_2170_65869()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "GW VoiceCentric", "NKS_DATA_VERSION": "1.0"}, prog_num=65870) as resolve_config_vars_in_file_2171_65870:
                resolve_config_vars_in_file_2171_65870()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-GW VoiceCentric Stereo.plist", ignore_all_errors=True), prog_num=65871) as if_2172_65871:
                if_2172_65871()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=65872) as resolve_config_vars_in_file_2173_65872:
                resolve_config_vars_in_file_2173_65872()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Delay Stereo.plist", ignore_all_errors=True), prog_num=65873) as if_2174_65873:
                if_2174_65873()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-EQ", "NKS_DATA_VERSION": "1.0"}, prog_num=65874) as resolve_config_vars_in_file_2175_65874:
                resolve_config_vars_in_file_2175_65874()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-EQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-EQ Stereo.plist", ignore_all_errors=True), prog_num=65875) as if_2176_65875:
                if_2176_65875()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "H-Reverb long", "NKS_DATA_VERSION": "1.0"}, prog_num=65876) as resolve_config_vars_in_file_2177_65876:
                resolve_config_vars_in_file_2177_65876()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-H-Reverb long Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-H-Reverb long Stereo.plist", ignore_all_errors=True), prog_num=65877) as if_2178_65877:
                if_2178_65877()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "IMPusher", "NKS_DATA_VERSION": "1.0"}, prog_num=65878) as resolve_config_vars_in_file_2179_65878:
                resolve_config_vars_in_file_2179_65878()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IMPusher Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IMPusher Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IMPusher Stereo.plist", ignore_all_errors=True), prog_num=65879) as if_2180_65879:
                if_2180_65879()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "IRLive", "NKS_DATA_VERSION": "1.0"}, prog_num=65880) as resolve_config_vars_in_file_2181_65880:
                resolve_config_vars_in_file_2181_65880()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IRLive Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-IRLive Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-IRLive Stereo.plist", ignore_all_errors=True), prog_num=65881) as if_2182_65881:
                if_2182_65881()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "InPhase LT Live", "NKS_DATA_VERSION": "1.0"}, prog_num=65882) as resolve_config_vars_in_file_2183_65882:
                resolve_config_vars_in_file_2183_65882()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-InPhase LT Live Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-InPhase LT Live Stereo.plist", ignore_all_errors=True), prog_num=65883) as if_2184_65883:
                if_2184_65883()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "J37", "NKS_DATA_VERSION": "1.0"}, prog_num=65884) as resolve_config_vars_in_file_2185_65884:
                resolve_config_vars_in_file_2185_65884()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-J37 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-J37 Stereo.plist", ignore_all_errors=True), prog_num=65885) as if_2186_65885:
                if_2186_65885()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Bass", "NKS_DATA_VERSION": "1.0"}, prog_num=65886) as resolve_config_vars_in_file_2187_65886:
                resolve_config_vars_in_file_2187_65886()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Bass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Bass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Bass Stereo.plist", ignore_all_errors=True), prog_num=65887) as if_2188_65887:
                if_2188_65887()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Cymb-Perc", "NKS_DATA_VERSION": "1.0"}, prog_num=65888) as resolve_config_vars_in_file_2189_65888:
                resolve_config_vars_in_file_2189_65888()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Cymb-Perc Stereo.plist", ignore_all_errors=True), prog_num=65889) as if_2190_65889:
                if_2190_65889()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Drums", "NKS_DATA_VERSION": "1.0"}, prog_num=65890) as resolve_config_vars_in_file_2191_65890:
                resolve_config_vars_in_file_2191_65890()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Drums Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Drums Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Drums Stereo.plist", ignore_all_errors=True), prog_num=65891) as if_2192_65891:
                if_2192_65891()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Guitars", "NKS_DATA_VERSION": "1.0"}, prog_num=65892) as resolve_config_vars_in_file_2193_65892:
                resolve_config_vars_in_file_2193_65892()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Guitars Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Guitars Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Guitars Stereo.plist", ignore_all_errors=True), prog_num=65893) as if_2194_65893:
                if_2194_65893()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Strings-Keys", "NKS_DATA_VERSION": "1.0"}, prog_num=65894) as resolve_config_vars_in_file_2195_65894:
                resolve_config_vars_in_file_2195_65894()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Strings-Keys Stereo.plist", ignore_all_errors=True), prog_num=65895) as if_2196_65895:
                if_2196_65895()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "JJP-Vocals", "NKS_DATA_VERSION": "1.0"}, prog_num=65896) as resolve_config_vars_in_file_2197_65896:
                resolve_config_vars_in_file_2197_65896()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-JJP-Vocals Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-JJP-Vocals Stereo.plist", ignore_all_errors=True), prog_num=65897) as if_2198_65897:
                if_2198_65897()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-Kings Mics Stereo.xml", prog_num=65898) as rm_file_or_dir_2199_65898:
                rm_file_or_dir_2199_65898()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "The Kings Microphones", "NKS_DATA_VERSION": "1.0"}, prog_num=65899) as resolve_config_vars_in_file_2200_65899:
                resolve_config_vars_in_file_2200_65899()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-The Kings Microphones Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-The Kings Microphones Stereo.plist", ignore_all_errors=True), prog_num=65900) as if_2201_65900:
                if_2201_65900()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-Kings Mics Stereo.plist", prog_num=65901) as rm_file_or_dir_2202_65901:
                rm_file_or_dir_2202_65901()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerHLS", "NKS_DATA_VERSION": "1.0"}, prog_num=65902) as resolve_config_vars_in_file_2203_65902:
                resolve_config_vars_in_file_2203_65902()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerHLS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerHLS Stereo.plist", ignore_all_errors=True), prog_num=65903) as if_2204_65903:
                if_2204_65903()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "KramerPIE", "NKS_DATA_VERSION": "1.0"}, prog_num=65904) as resolve_config_vars_in_file_2205_65904:
                resolve_config_vars_in_file_2205_65904()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-KramerPIE Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-KramerPIE Stereo.plist", ignore_all_errors=True), prog_num=65905) as if_2206_65905:
                if_2206_65905()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Kramer Tape", "NKS_DATA_VERSION": "1.0"}, prog_num=65906) as resolve_config_vars_in_file_2207_65906:
                resolve_config_vars_in_file_2207_65906()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Kramer Tape Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Kramer Tape Stereo.plist", ignore_all_errors=True), prog_num=65907) as if_2208_65907:
                if_2208_65907()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L1", "NKS_DATA_VERSION": "1.0"}, prog_num=65908) as resolve_config_vars_in_file_2209_65908:
                resolve_config_vars_in_file_2209_65908()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L1 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L1 Stereo.plist", ignore_all_errors=True), prog_num=65909) as if_2210_65909:
                if_2210_65909()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L2", "NKS_DATA_VERSION": "1.0"}, prog_num=65910) as resolve_config_vars_in_file_2211_65910:
                resolve_config_vars_in_file_2211_65910()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L2 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L2 Stereo.plist", ignore_all_errors=True), prog_num=65911) as if_2212_65911:
                if_2212_65911()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-16", "NKS_DATA_VERSION": "1.0"}, prog_num=65912) as resolve_config_vars_in_file_2213_65912:
                resolve_config_vars_in_file_2213_65912()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-16 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-16 Stereo.plist", ignore_all_errors=True), prog_num=65913) as if_2214_65913:
                if_2214_65913()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3-LL Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=65914) as resolve_config_vars_in_file_2215_65914:
                resolve_config_vars_in_file_2215_65914()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3-LL Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3-LL Multi Stereo.plist", ignore_all_errors=True), prog_num=65915) as if_2216_65915:
                if_2216_65915()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=65916) as resolve_config_vars_in_file_2217_65916:
                resolve_config_vars_in_file_2217_65916()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Multi Stereo.plist", ignore_all_errors=True), prog_num=65917) as if_2218_65917:
                if_2218_65917()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "L3 Ultra", "NKS_DATA_VERSION": "1.0"}, prog_num=65918) as resolve_config_vars_in_file_2219_65918:
                resolve_config_vars_in_file_2219_65918()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-L3 Ultra Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-L3 Ultra Stereo.plist", ignore_all_errors=True), prog_num=65919) as if_2220_65919:
                if_2220_65919()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LinMB", "NKS_DATA_VERSION": "1.0"}, prog_num=65920) as resolve_config_vars_in_file_2221_65920:
                resolve_config_vars_in_file_2221_65920()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LinMB Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LinMB Stereo.plist", ignore_all_errors=True), prog_num=65921) as if_2222_65921:
                if_2222_65921()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "LoAir", "NKS_DATA_VERSION": "1.0"}, prog_num=65922) as resolve_config_vars_in_file_2223_65922:
                resolve_config_vars_in_file_2223_65922()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-LoAir Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-LoAir Stereo.plist", ignore_all_errors=True), prog_num=65923) as if_2224_65923:
                if_2224_65923()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-Delay", "NKS_DATA_VERSION": "1.0"}, prog_num=65924) as resolve_config_vars_in_file_2225_65924:
                resolve_config_vars_in_file_2225_65924()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Delay Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Delay Stereo.plist", ignore_all_errors=True), prog_num=65925) as if_2226_65925:
                if_2226_65925()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM Distortion", "NKS_DATA_VERSION": "1.0"}, prog_num=65926) as resolve_config_vars_in_file_2227_65926:
                resolve_config_vars_in_file_2227_65926()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM Distortion Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM Distortion Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM Distortion Stereo.plist", ignore_all_errors=True), prog_num=65927) as if_2228_65927:
                if_2228_65927()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-EQ", "NKS_DATA_VERSION": "1.0"}, prog_num=65928) as resolve_config_vars_in_file_2229_65928:
                resolve_config_vars_in_file_2229_65928()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-EQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-EQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-EQ Stereo.plist", ignore_all_errors=True), prog_num=65929) as if_2230_65929:
                if_2230_65929()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMReverb Stereo.xml", prog_num=65930) as rm_file_or_dir_2231_65930:
                rm_file_or_dir_2231_65930()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MannyM Reverb Stereo.xml", prog_num=65931) as rm_file_or_dir_2232_65931:
                rm_file_or_dir_2232_65931()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-Reverb", "NKS_DATA_VERSION": "1.0"}, prog_num=65932) as resolve_config_vars_in_file_2233_65932:
                resolve_config_vars_in_file_2233_65932()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-Reverb Stereo.plist", ignore_all_errors=True), prog_num=65933) as if_2234_65933:
                if_2234_65933()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMReverb Stereo.plist", prog_num=65934) as rm_file_or_dir_2235_65934:
                rm_file_or_dir_2235_65934()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MannyM Reverb Stereo.plist", prog_num=65935) as rm_file_or_dir_2236_65935:
                rm_file_or_dir_2236_65935()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMToneShaper Stereo.xml", prog_num=65936) as rm_file_or_dir_2237_65936:
                rm_file_or_dir_2237_65936()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-MMTShaper Stereo.xml", prog_num=65937) as rm_file_or_dir_2238_65937:
                rm_file_or_dir_2238_65937()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MannyM-ToneShaper", "NKS_DATA_VERSION": "1.0"}, prog_num=65938) as resolve_config_vars_in_file_2239_65938:
                resolve_config_vars_in_file_2239_65938()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MannyM-ToneShaper Stereo.plist", ignore_all_errors=True), prog_num=65939) as if_2240_65939:
                if_2240_65939()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMToneShaper Stereo.plist", prog_num=65940) as rm_file_or_dir_2241_65940:
                rm_file_or_dir_2241_65940()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-MMTShaper Stereo.plist", prog_num=65941) as rm_file_or_dir_2242_65941:
                rm_file_or_dir_2242_65941()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxBass", "NKS_DATA_VERSION": "1.0"}, prog_num=65942) as resolve_config_vars_in_file_2243_65942:
                resolve_config_vars_in_file_2243_65942()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxBass Stereo.plist", ignore_all_errors=True), prog_num=65943) as if_2244_65943:
                if_2244_65943()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MaxxVolume", "NKS_DATA_VERSION": "1.0"}, prog_num=65944) as resolve_config_vars_in_file_2245_65944:
                resolve_config_vars_in_file_2245_65944()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MaxxVolume Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MaxxVolume Stereo.plist", ignore_all_errors=True), prog_num=65945) as if_2246_65945:
                if_2246_65945()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MetaFilter", "NKS_DATA_VERSION": "1.0"}, prog_num=65946) as resolve_config_vars_in_file_2247_65946:
                resolve_config_vars_in_file_2247_65946()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MetaFilter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MetaFilter Stereo.plist", ignore_all_errors=True), prog_num=65947) as if_2248_65947:
                if_2248_65947()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "MondoMod", "NKS_DATA_VERSION": "1.0"}, prog_num=65948) as resolve_config_vars_in_file_2249_65948:
                resolve_config_vars_in_file_2249_65948()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-MondoMod Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-MondoMod Stereo.plist", ignore_all_errors=True), prog_num=65949) as if_2250_65949:
                if_2250_65949()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Morphoder", "NKS_DATA_VERSION": "1.0"}, prog_num=65950) as resolve_config_vars_in_file_2251_65950:
                resolve_config_vars_in_file_2251_65950()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Morphoder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Morphoder Stereo.plist", ignore_all_errors=True), prog_num=65951) as if_2252_65951:
                if_2252_65951()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Brighter", "NKS_DATA_VERSION": "1.0"}, prog_num=65952) as resolve_config_vars_in_file_2253_65952:
                resolve_config_vars_in_file_2253_65952()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Brighter Stereo.plist", ignore_all_errors=True), prog_num=65953) as if_2254_65953:
                if_2254_65953()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Driver", "NKS_DATA_VERSION": "1.0"}, prog_num=65954) as resolve_config_vars_in_file_2255_65954:
                resolve_config_vars_in_file_2255_65954()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Driver Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Driver Stereo.plist", ignore_all_errors=True), prog_num=65955) as if_2256_65955:
                if_2256_65955()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Filter", "NKS_DATA_VERSION": "1.0"}, prog_num=65956) as resolve_config_vars_in_file_2257_65956:
                resolve_config_vars_in_file_2257_65956()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Filter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Filter Stereo.plist", ignore_all_errors=True), prog_num=65957) as if_2258_65957:
                if_2258_65957()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Louder", "NKS_DATA_VERSION": "1.0"}, prog_num=65958) as resolve_config_vars_in_file_2259_65958:
                resolve_config_vars_in_file_2259_65958()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Louder Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Louder Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Louder Stereo.plist", ignore_all_errors=True), prog_num=65959) as if_2260_65959:
                if_2260_65959()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Phatter", "NKS_DATA_VERSION": "1.0"}, prog_num=65960) as resolve_config_vars_in_file_2261_65960:
                resolve_config_vars_in_file_2261_65960()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Phatter Stereo.plist", ignore_all_errors=True), prog_num=65961) as if_2262_65961:
                if_2262_65961()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pressure", "NKS_DATA_VERSION": "1.0"}, prog_num=65962) as resolve_config_vars_in_file_2263_65962:
                resolve_config_vars_in_file_2263_65962()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pressure Stereo.plist", ignore_all_errors=True), prog_num=65963) as if_2264_65963:
                if_2264_65963()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Pumper", "NKS_DATA_VERSION": "1.0"}, prog_num=65964) as resolve_config_vars_in_file_2265_65964:
                resolve_config_vars_in_file_2265_65964()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Pumper Stereo.plist", ignore_all_errors=True), prog_num=65965) as if_2266_65965:
                if_2266_65965()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OneKnob Wetter", "NKS_DATA_VERSION": "1.0"}, prog_num=65966) as resolve_config_vars_in_file_2267_65966:
                resolve_config_vars_in_file_2267_65966()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OneKnob Wetter Stereo.plist", ignore_all_errors=True), prog_num=65967) as if_2268_65967:
                if_2268_65967()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "OVox", "NKS_DATA_VERSION": "1.0"}, prog_num=65968) as resolve_config_vars_in_file_2269_65968:
                resolve_config_vars_in_file_2269_65968()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-OVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-OVox Stereo.plist", ignore_all_errors=True), prog_num=65969) as if_2270_65969:
                if_2270_65969()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PAZ", "NKS_DATA_VERSION": "1.0"}, prog_num=65970) as resolve_config_vars_in_file_2271_65970:
                resolve_config_vars_in_file_2271_65970()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PAZ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PAZ Stereo.plist", ignore_all_errors=True), prog_num=65971) as if_2272_65971:
                if_2272_65971()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS Archon", "NKS_DATA_VERSION": "1.0"}, prog_num=65972) as resolve_config_vars_in_file_2273_65972:
                resolve_config_vars_in_file_2273_65972()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Archon Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Archon Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Archon Stereo.plist", ignore_all_errors=True), prog_num=65973) as if_2274_65973:
                if_2274_65973()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS Dallas", "NKS_DATA_VERSION": "1.0"}, prog_num=65974) as resolve_config_vars_in_file_2275_65974:
                resolve_config_vars_in_file_2275_65974()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Dallas Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS Dallas Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS Dallas Stereo.plist", ignore_all_errors=True), prog_num=65975) as if_2276_65975:
                if_2276_65975()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PRS V9", "NKS_DATA_VERSION": "1.0"}, prog_num=65976) as resolve_config_vars_in_file_2277_65976:
                resolve_config_vars_in_file_2277_65976()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS V9 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PRS V9 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PRS V9 Stereo.plist", ignore_all_errors=True), prog_num=65977) as if_2278_65977:
                if_2278_65977()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PS22", "NKS_DATA_VERSION": "1.0"}, prog_num=65978) as resolve_config_vars_in_file_2279_65978:
                resolve_config_vars_in_file_2279_65978()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PS22 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PS22 Stereo.plist", ignore_all_errors=True), prog_num=65979) as if_2280_65979:
                if_2280_65979()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 660", "NKS_DATA_VERSION": "1.0"}, prog_num=65980) as resolve_config_vars_in_file_2281_65980:
                resolve_config_vars_in_file_2281_65980()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", ignore_all_errors=True), prog_num=65981) as if_2282_65981:
                if_2282_65981()
            with MoveFileToFile(r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 660 Mono.plist", ignore_all_errors=True, prog_num=65982) as move_file_to_file_2283_65982:
                move_file_to_file_2283_65982()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigChild 670", "NKS_DATA_VERSION": "1.0"}, prog_num=65983) as resolve_config_vars_in_file_2284_65983:
                resolve_config_vars_in_file_2284_65983()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigChild 670 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigChild 670 Stereo.plist", ignore_all_errors=True), prog_num=65984) as if_2285_65984:
                if_2285_65984()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec EQP1A", "NKS_DATA_VERSION": "1.0"}, prog_num=65985) as resolve_config_vars_in_file_2286_65985:
                resolve_config_vars_in_file_2286_65985()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec EQP1A Stereo.plist", ignore_all_errors=True), prog_num=65986) as if_2287_65986:
                if_2287_65986()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "PuigTec MEQ5", "NKS_DATA_VERSION": "1.0"}, prog_num=65987) as resolve_config_vars_in_file_2288_65987:
                resolve_config_vars_in_file_2288_65987()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-PuigTec MEQ5 Stereo.plist", ignore_all_errors=True), prog_num=65988) as if_2289_65988:
                if_2289_65988()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q10", "NKS_DATA_VERSION": "1.0"}, prog_num=65989) as resolve_config_vars_in_file_2290_65989:
                resolve_config_vars_in_file_2290_65989()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q10 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q10 Stereo.plist", ignore_all_errors=True), prog_num=65990) as if_2291_65990:
                if_2291_65990()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Q-Clone", "NKS_DATA_VERSION": "1.0"}, prog_num=65991) as resolve_config_vars_in_file_2292_65991:
                resolve_config_vars_in_file_2292_65991()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Q-Clone Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Q-Clone Stereo.plist", ignore_all_errors=True), prog_num=65992) as if_2293_65992:
                if_2293_65992()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RBass", "NKS_DATA_VERSION": "1.0"}, prog_num=65993) as resolve_config_vars_in_file_2294_65993:
                resolve_config_vars_in_file_2294_65993()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RBass Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RBass Stereo.plist", ignore_all_errors=True), prog_num=65994) as if_2295_65994:
                if_2295_65994()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RChannel", "NKS_DATA_VERSION": "1.0"}, prog_num=65995) as resolve_config_vars_in_file_2296_65995:
                resolve_config_vars_in_file_2296_65995()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RChannel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RChannel Stereo.plist", ignore_all_errors=True), prog_num=65996) as if_2297_65996:
                if_2297_65996()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RCompressor", "NKS_DATA_VERSION": "1.0"}, prog_num=65997) as resolve_config_vars_in_file_2298_65997:
                resolve_config_vars_in_file_2298_65997()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RCompressor Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RCompressor Stereo.plist", ignore_all_errors=True), prog_num=65998) as if_2299_65998:
                if_2299_65998()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD17", "NKS_DATA_VERSION": "1.0"}, prog_num=65999) as resolve_config_vars_in_file_2300_65999:
                resolve_config_vars_in_file_2300_65999()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD17 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD17 Stereo.plist", ignore_all_errors=True), prog_num=66000) as if_2301_66000:
                if_2301_66000()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REDD37-51", "NKS_DATA_VERSION": "1.0"}, prog_num=66001) as resolve_config_vars_in_file_2302_66001:
                resolve_config_vars_in_file_2302_66001()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REDD37-51 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REDD37-51 Stereo.plist", ignore_all_errors=True), prog_num=66002) as if_2303_66002:
                if_2303_66002()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "REQ 6", "NKS_DATA_VERSION": "1.0"}, prog_num=66003) as resolve_config_vars_in_file_2304_66003:
                resolve_config_vars_in_file_2304_66003()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-REQ 6 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-REQ 6 Stereo.plist", ignore_all_errors=True), prog_num=66004) as if_2305_66004:
                if_2305_66004()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RS56", "NKS_DATA_VERSION": "1.0"}, prog_num=66005) as resolve_config_vars_in_file_2306_66005:
                resolve_config_vars_in_file_2306_66005()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RS56 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RS56 Stereo.plist", ignore_all_errors=True), prog_num=66006) as if_2307_66006:
                if_2307_66006()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=66007) as resolve_config_vars_in_file_2308_66007:
                resolve_config_vars_in_file_2308_66007()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVerb Stereo.plist", ignore_all_errors=True), prog_num=66008) as if_2309_66008:
                if_2309_66008()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "RVox", "NKS_DATA_VERSION": "1.0"}, prog_num=66009) as resolve_config_vars_in_file_2310_66009:
                resolve_config_vars_in_file_2310_66009()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-RVox Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-RVox Stereo.plist", ignore_all_errors=True), prog_num=66010) as if_2311_66010:
                if_2311_66010()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Reel ADT", "NKS_DATA_VERSION": "1.0"}, prog_num=66011) as resolve_config_vars_in_file_2312_66011:
                resolve_config_vars_in_file_2312_66011()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Reel ADT Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Reel ADT Stereo.plist", ignore_all_errors=True), prog_num=66012) as if_2313_66012:
                if_2313_66012()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Imager", "NKS_DATA_VERSION": "1.0"}, prog_num=66013) as resolve_config_vars_in_file_2314_66013:
                resolve_config_vars_in_file_2314_66013()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Imager Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Imager Stereo.plist", ignore_all_errors=True), prog_num=66014) as if_2315_66014:
                if_2315_66014()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "S1 Shuffler", "NKS_DATA_VERSION": "1.0"}, prog_num=66015) as resolve_config_vars_in_file_2316_66015:
                resolve_config_vars_in_file_2316_66015()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-S1 Shuffler Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-S1 Shuffler Stereo.plist", ignore_all_errors=True), prog_num=66016) as if_2317_66016:
                if_2317_66016()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSLComp", "NKS_DATA_VERSION": "1.0"}, prog_num=66017) as resolve_config_vars_in_file_2318_66017:
                resolve_config_vars_in_file_2318_66017()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLComp Stereo.plist", ignore_all_errors=True), prog_num=66018) as if_2319_66018:
                if_2319_66018()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSLEQ", "NKS_DATA_VERSION": "1.0"}, prog_num=66019) as resolve_config_vars_in_file_2320_66019:
                resolve_config_vars_in_file_2320_66019()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLEQ Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSLEQ Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSLEQ Stereo.plist", ignore_all_errors=True), prog_num=66020) as if_2321_66020:
                if_2321_66020()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSL E-Channel", "NKS_DATA_VERSION": "1.0"}, prog_num=66021) as resolve_config_vars_in_file_2322_66021:
                resolve_config_vars_in_file_2322_66021()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL E-Channel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL E-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL E-Channel Stereo.plist", ignore_all_errors=True), prog_num=66022) as if_2323_66022:
                if_2323_66022()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SSL G-Channel", "NKS_DATA_VERSION": "1.0"}, prog_num=66023) as resolve_config_vars_in_file_2324_66023:
                resolve_config_vars_in_file_2324_66023()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL G-Channel Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SSL G-Channel Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SSL G-Channel Stereo.plist", ignore_all_errors=True), prog_num=66024) as if_2325_66024:
                if_2325_66024()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps 73", "NKS_DATA_VERSION": "1.0"}, prog_num=66025) as resolve_config_vars_in_file_2326_66025:
                resolve_config_vars_in_file_2326_66025()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps 73 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps 73 Stereo.plist", ignore_all_errors=True), prog_num=66026) as if_2327_66026:
                if_2327_66026()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Scheps Parallel Particles", "NKS_DATA_VERSION": "1.0"}, prog_num=66027) as resolve_config_vars_in_file_2328_66027:
                resolve_config_vars_in_file_2328_66027()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Scheps Parallel Particles Stereo.plist", ignore_all_errors=True), prog_num=66028) as if_2329_66028:
                if_2329_66028()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Smack Attack", "NKS_DATA_VERSION": "1.0"}, prog_num=66029) as resolve_config_vars_in_file_2330_66029:
                resolve_config_vars_in_file_2330_66029()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Smack Attack Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Smack Attack Stereo.plist", ignore_all_errors=True), prog_num=66030) as if_2331_66030:
                if_2331_66030()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SoundShifter", "NKS_DATA_VERSION": "1.0"}, prog_num=66031) as resolve_config_vars_in_file_2332_66031:
                resolve_config_vars_in_file_2332_66031()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SoundShifter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SoundShifter Stereo.plist", ignore_all_errors=True), prog_num=66032) as if_2333_66032:
                if_2333_66032()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Submarine", "NKS_DATA_VERSION": "1.0"}, prog_num=66033) as resolve_config_vars_in_file_2334_66033:
                resolve_config_vars_in_file_2334_66033()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Submarine Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Submarine Stereo.plist", ignore_all_errors=True), prog_num=66034) as if_2335_66034:
                if_2335_66034()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 2-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=66035) as resolve_config_vars_in_file_2336_66035:
                resolve_config_vars_in_file_2336_66035()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 2-Taps Stereo.plist", ignore_all_errors=True), prog_num=66036) as if_2337_66036:
                if_2337_66036()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "SuperTap 6-Taps", "NKS_DATA_VERSION": "1.0"}, prog_num=66037) as resolve_config_vars_in_file_2338_66037:
                resolve_config_vars_in_file_2338_66037()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-SuperTap 6-Taps Stereo.plist", ignore_all_errors=True), prog_num=66038) as if_2339_66038:
                if_2339_66038()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TG12345", "NKS_DATA_VERSION": "1.0"}, prog_num=66039) as resolve_config_vars_in_file_2340_66039:
                resolve_config_vars_in_file_2340_66039()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TG12345 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TG12345 Stereo.plist", ignore_all_errors=True), prog_num=66040) as if_2341_66040:
                if_2341_66040()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Torque", "NKS_DATA_VERSION": "1.0"}, prog_num=66041) as resolve_config_vars_in_file_2342_66041:
                resolve_config_vars_in_file_2342_66041()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Torque Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Torque Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Torque Stereo.plist", ignore_all_errors=True), prog_num=66042) as if_2343_66042:
                if_2343_66042()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Multi", "NKS_DATA_VERSION": "1.0"}, prog_num=66043) as resolve_config_vars_in_file_2344_66043:
                resolve_config_vars_in_file_2344_66043()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Multi Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Multi Stereo.plist", ignore_all_errors=True), prog_num=66044) as if_2345_66044:
                if_2345_66044()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TransX Wide", "NKS_DATA_VERSION": "1.0"}, prog_num=66045) as resolve_config_vars_in_file_2346_66045:
                resolve_config_vars_in_file_2346_66045()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TransX Wide Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TransX Wide Stereo.plist", ignore_all_errors=True), prog_num=66046) as if_2347_66046:
                if_2347_66046()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "TrueVerb", "NKS_DATA_VERSION": "1.0"}, prog_num=66047) as resolve_config_vars_in_file_2348_66047:
                resolve_config_vars_in_file_2348_66047()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-TrueVerb Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-TrueVerb Stereo.plist", ignore_all_errors=True), prog_num=66048) as if_2349_66048:
                if_2349_66048()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch Stereo.xml", prog_num=66049) as rm_file_or_dir_2350_66049:
                rm_file_or_dir_2350_66049()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 3 Stereo.xml", prog_num=66050) as rm_file_or_dir_2351_66050:
                rm_file_or_dir_2351_66050()
            with RmFileOrDir(r"/Library/Application Support/Native Instruments/Service Center/Waves-UPitch 6 Stereo.xml", prog_num=66051) as rm_file_or_dir_2352_66051:
                rm_file_or_dir_2352_66051()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 3 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=66052) as resolve_config_vars_in_file_2353_66052:
                resolve_config_vars_in_file_2353_66052()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 3 Voices Stereo.plist", ignore_all_errors=True), prog_num=66053) as if_2354_66053:
                if_2354_66053()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch 6 Voices", "NKS_DATA_VERSION": "1.0"}, prog_num=66054) as resolve_config_vars_in_file_2355_66054:
                resolve_config_vars_in_file_2355_66054()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch 6 Voices Stereo.plist", ignore_all_errors=True), prog_num=66055) as if_2356_66055:
                if_2356_66055()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "UltraPitch Shift", "NKS_DATA_VERSION": "1.0"}, prog_num=66056) as resolve_config_vars_in_file_2357_66056:
                resolve_config_vars_in_file_2357_66056()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-UltraPitch Shift Stereo.plist", ignore_all_errors=True), prog_num=66057) as if_2358_66057:
                if_2358_66057()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch Stereo.plist", prog_num=66058) as rm_file_or_dir_2359_66058:
                rm_file_or_dir_2359_66058()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 3 Stereo.plist", prog_num=66059) as rm_file_or_dir_2360_66059:
                rm_file_or_dir_2360_66059()
            with RmFileOrDir(r"/Library/Preferences/com.native-instruments.Waves-UPitch 6 Stereo.plist", prog_num=66060) as rm_file_or_dir_2361_66060:
                rm_file_or_dir_2361_66060()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VComp", "NKS_DATA_VERSION": "1.0"}, prog_num=66061) as resolve_config_vars_in_file_2362_66061:
                resolve_config_vars_in_file_2362_66061()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VComp Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VComp Stereo.plist", ignore_all_errors=True), prog_num=66062) as if_2363_66062:
                if_2363_66062()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VEQ4", "NKS_DATA_VERSION": "1.0"}, prog_num=66063) as resolve_config_vars_in_file_2364_66063:
                resolve_config_vars_in_file_2364_66063()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VEQ4 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VEQ4 Stereo.plist", ignore_all_errors=True), prog_num=66064) as if_2365_66064:
                if_2365_66064()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "VU Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=66065) as resolve_config_vars_in_file_2366_66065:
                resolve_config_vars_in_file_2366_66065()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-VU Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-VU Meter Stereo.plist", ignore_all_errors=True), prog_num=66066) as if_2367_66066:
                if_2367_66066()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Vitamin", "NKS_DATA_VERSION": "1.0"}, prog_num=66067) as resolve_config_vars_in_file_2368_66067:
                resolve_config_vars_in_file_2368_66067()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Vitamin Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Vitamin Stereo.plist", ignore_all_errors=True), prog_num=66068) as if_2369_66068:
                if_2369_66068()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "W43", "NKS_DATA_VERSION": "1.0"}, prog_num=66069) as resolve_config_vars_in_file_2370_66069:
                resolve_config_vars_in_file_2370_66069()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-W43 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-W43 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-W43 Stereo.plist", ignore_all_errors=True), prog_num=66070) as if_2371_66070:
                if_2371_66070()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WLM Meter", "NKS_DATA_VERSION": "1.0"}, prog_num=66071) as resolve_config_vars_in_file_2372_66071:
                resolve_config_vars_in_file_2372_66071()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WLM Meter Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WLM Meter Stereo.plist", ignore_all_errors=True), prog_num=66072) as if_2373_66072:
                if_2373_66072()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "WNS", "NKS_DATA_VERSION": "1.0"}, prog_num=66073) as resolve_config_vars_in_file_2374_66073:
                resolve_config_vars_in_file_2374_66073()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WNS Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-WNS Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-WNS Stereo.plist", ignore_all_errors=True), prog_num=66074) as if_2375_66074:
                if_2375_66074()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "Waves Tune Real-Time", "NKS_DATA_VERSION": "1.0"}, prog_num=66075) as resolve_config_vars_in_file_2376_66075:
                resolve_config_vars_in_file_2376_66075()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-Waves Tune Real-Time Stereo.plist", ignore_all_errors=True), prog_num=66076) as if_2377_66076:
                if_2377_66076()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Crackle", "NKS_DATA_VERSION": "1.0"}, prog_num=66077) as resolve_config_vars_in_file_2378_66077:
                resolve_config_vars_in_file_2378_66077()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Crackle Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Crackle Stereo.plist", ignore_all_errors=True), prog_num=66078) as if_2379_66078:
                if_2379_66078()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "X-Hum", "NKS_DATA_VERSION": "1.0"}, prog_num=66079) as resolve_config_vars_in_file_2380_66079:
                resolve_config_vars_in_file_2380_66079()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-X-Hum Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-X-Hum Stereo.plist", ignore_all_errors=True), prog_num=66080) as if_2381_66080:
                if_2381_66080()
            with ResolveConfigVarsInFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Utilities/plist/com.NI.Waves.NKS_FX.plist.template", r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", config_files=[], temp_config_vars={"NKS_NAME": "dbx-160", "NKS_DATA_VERSION": "1.0"}, prog_num=66081) as resolve_config_vars_in_file_2382_66081:
                resolve_config_vars_in_file_2382_66081()
            with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-dbx-160 Stereo.plist", ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/private/tmp/com.native-instruments.Waves-dbx-160 Stereo.plist", r"/Library/Preferences/com.native-instruments.Waves-dbx-160 Stereo.plist", ignore_all_errors=True), prog_num=66082) as if_2383_66082:
                if_2383_66082()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS", prog_num=66083) as cd_stage_2384_66083:
            cd_stage_2384_66083()
            with Stage(r"copy", r"COSMOS_HTML v2.6.5", prog_num=66084):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=3, prog_num=66085) as should_copy_source_2385_66085:
                    should_copy_source_2385_66085()
                    with Stage(r"copy source", r"Mac/COSMOS/HTML", prog_num=66086):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/HTML", r".", delete_extraneous_files=True, prog_num=66087) as copy_dir_to_dir_2386_66087:
                            copy_dir_to_dir_2386_66087()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/HTML", user_id=-1, group_id=-1, prog_num=66088, recursive=True) as chown_2387_66088:
                            chown_2387_66088()
            with Stage(r"copy", r"COSMOS_python v2.7.6", prog_num=66089):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r"/Library/Application Support/Waves/COSMOS", skip_progress_count=4, prog_num=66090) as should_copy_source_2388_66090:
                    should_copy_source_2388_66090()
                    with Stage(r"copy source", r"Mac/COSMOS/python", prog_num=66091):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", r".", delete_extraneous_files=True, prog_num=66092) as copy_dir_to_dir_2389_66092:
                            copy_dir_to_dir_2389_66092()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/COSMOS/python", where_to_unwtar=r".", prog_num=66093) as unwtar_2390_66093:
                            unwtar_2390_66093()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/python", user_id=-1, group_id=-1, prog_num=66094, recursive=True) as chown_2391_66094:
                            chown_2391_66094()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", prog_num=66095) as cd_stage_2392_66095:
            cd_stage_2392_66095()
            with Stage(r"copy", r"AnalyzeAudio v16.0.23.24", prog_num=66096):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio", skip_progress_count=4, prog_num=66097) as should_copy_source_2393_66097:
                    should_copy_source_2393_66097()
                    with Stage(r"copy source", r"Mac/Tools/AnalyzeAudio.bundle", prog_num=66098):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", r".", delete_extraneous_files=True, prog_num=66099) as copy_dir_to_dir_2394_66099:
                            copy_dir_to_dir_2394_66099()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Tools/AnalyzeAudio.bundle", where_to_unwtar=r".", prog_num=66100) as unwtar_2395_66100:
                            unwtar_2395_66100()
                        with Chown(path=r"/Library/Application Support/Waves/COSMOS/AnalyzeAudio/AnalyzeAudio.bundle", user_id=-1, group_id=-1, prog_num=66101, recursive=True) as chown_2396_66101:
                            chown_2396_66101()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V15", prog_num=66102) as cd_stage_2397_66102:
            cd_stage_2397_66102()
            with Stage(r"copy", r"Demo Mode 1.1 v1.1", prog_num=66103):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r"/Library/Application Support/Waves/Demo Mode/V15", skip_progress_count=3, prog_num=66104) as should_copy_source_2398_66104:
                    should_copy_source_2398_66104()
                    with Stage(r"copy source", r"Mac/Demo Mode/V15/1", prog_num=66105):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V15/1", r".", delete_extraneous_files=True, prog_num=66106) as copy_dir_to_dir_2399_66106:
                            copy_dir_to_dir_2399_66106()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V15/1", user_id=-1, group_id=-1, prog_num=66107, recursive=True) as chown_2400_66107:
                            chown_2400_66107()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Demo Mode/V16", prog_num=66108) as cd_stage_2401_66108:
            cd_stage_2401_66108()
            with Stage(r"copy", r"Demo Mode V16 1.1 v1.1", prog_num=66109):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r"/Library/Application Support/Waves/Demo Mode/V16", skip_progress_count=3, prog_num=66110) as should_copy_source_2402_66110:
                    should_copy_source_2402_66110()
                    with Stage(r"copy source", r"Mac/Demo Mode/V16/1", prog_num=66111):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Demo Mode/V16/1", r".", delete_extraneous_files=True, prog_num=66112) as copy_dir_to_dir_2403_66112:
                            copy_dir_to_dir_2403_66112()
                        with Chown(path=r"/Library/Application Support/Waves/Demo Mode/V16/1", user_id=-1, group_id=-1, prog_num=66113, recursive=True) as chown_2404_66113:
                            chown_2404_66113()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/License Notifications/V16", prog_num=66114) as cd_stage_2405_66114:
            cd_stage_2405_66114()
            with Stage(r"copy", r"License Notifications V16 1.1 v1.1", prog_num=66115):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r"/Library/Application Support/Waves/License Notifications/V16", skip_progress_count=3, prog_num=66116) as should_copy_source_2406_66116:
                    should_copy_source_2406_66116()
                    with Stage(r"copy source", r"Mac/License Notifications/V16/1", prog_num=66117):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/License Notifications/V16/1", r".", delete_extraneous_files=True, prog_num=66118) as copy_dir_to_dir_2407_66118:
                            copy_dir_to_dir_2407_66118()
                        with Chown(path=r"/Library/Application Support/Waves/License Notifications/V16/1", user_id=-1, group_id=-1, prog_num=66119, recursive=True) as chown_2408_66119:
                            chown_2408_66119()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Modules", prog_num=66120) as cd_stage_2409_66120:
            cd_stage_2409_66120()
            with RmFileOrDir(r"/Library/Application Support/Waves/Modules/libmkl_waves.dylib", prog_num=66121) as rm_file_or_dir_2410_66121:
                rm_file_or_dir_2410_66121()
            with Stage(r"copy", r"ffmpeg v6.1.1", prog_num=66122):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/ffmpeg", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=66123) as should_copy_source_2411_66123:
                    should_copy_source_2411_66123()
                    with Stage(r"copy source", r"Mac/Modules/ffmpeg", prog_num=66124):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/ffmpeg.wtar.aa", where_to_unwtar=r".", prog_num=66125) as unwtar_2412_66125:
                            unwtar_2412_66125()
            with Stage(r"copy", r"InnerProcessDictionary2 v2.4.0.1", prog_num=66126):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=4, prog_num=66127) as should_copy_source_2413_66127:
                    should_copy_source_2413_66127()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary2.bundle", prog_num=66128):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66129) as copy_dir_to_dir_2414_66129:
                            copy_dir_to_dir_2414_66129()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary2.bundle", where_to_unwtar=r".", prog_num=66130) as unwtar_2415_66130:
                            unwtar_2415_66130()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/InnerProcessDictionary2.bundle", user_id=-1, group_id=-1, prog_num=66131, recursive=True) as chown_2416_66131:
                            chown_2416_66131()
            with Stage(r"copy", r"InnerProcessDictionary v1.4.1", prog_num=66132):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib", r"/Library/Application Support/Waves/Modules", skip_progress_count=2, prog_num=66133) as should_copy_source_2417_66133:
                    should_copy_source_2417_66133()
                    with Stage(r"copy source", r"Mac/Modules/InnerProcessDictionary.dylib", prog_num=66134):
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/InnerProcessDictionary.dylib.wtar.aa", where_to_unwtar=r".", prog_num=66135) as unwtar_2418_66135:
                            unwtar_2418_66135()
            with Stage(r"copy", r"mkl_waves library v1.0.1.1", prog_num=66136):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=66137) as should_copy_source_2419_66137:
                    should_copy_source_2419_66137()
                    with Stage(r"copy source", r"Mac/Modules/MklWaves.framework", prog_num=66138):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", r".", delete_extraneous_files=True, prog_num=66139) as copy_dir_to_dir_2420_66139:
                            copy_dir_to_dir_2420_66139()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/MklWaves.framework", where_to_unwtar=r".", prog_num=66140) as unwtar_2421_66140:
                            unwtar_2421_66140()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/MklWaves.framework", user_id=-1, group_id=-1, prog_num=66141, recursive=True) as chown_2422_66141:
                            chown_2422_66141()
            with Stage(r"copy", r"onnxruntime_1.19.0 v1.19.0", prog_num=66142):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r"/Library/Application Support/Waves/Modules", skip_progress_count=4, prog_num=66143) as should_copy_source_2423_66143:
                    should_copy_source_2423_66143()
                    with Stage(r"copy source", r"Mac/Modules/onnxruntime", prog_num=66144):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", r".", delete_extraneous_files=True, prog_num=66145) as copy_dir_to_dir_2424_66145:
                            copy_dir_to_dir_2424_66145()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/onnxruntime", where_to_unwtar=r".", prog_num=66146) as unwtar_2425_66146:
                            unwtar_2425_66146()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/onnxruntime", user_id=-1, group_id=-1, prog_num=66147, recursive=True) as chown_2426_66147:
                            chown_2426_66147()
            with Stage(r"copy", r"WavesLicenseEngine v3.0.0.3", prog_num=66148):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r"/Library/Application Support/Waves/Modules", dont_downgrade=True, skip_progress_count=5, prog_num=66149) as should_copy_source_2427_66149:
                    should_copy_source_2427_66149()
                    with Stage(r"copy source", r"Mac/Modules/WavesLicenseEngine.bundle", prog_num=66150):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Modules/WavesLicenseEngine.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66151) as copy_dir_to_dir_2428_66151:
                            copy_dir_to_dir_2428_66151()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/WavesLicenseEngine", mode="a+rwx", prog_num=66152) as chmod_2429_66152:
                            chmod_2429_66152()
                        with Chmod(path=r"WavesLicenseEngine.bundle/Contents/MacOS/exec/wle", mode="a+rwx", prog_num=66153) as chmod_2430_66153:
                            chmod_2430_66153()
                        with Chown(path=r"/Library/Application Support/Waves/Modules/WavesLicenseEngine.bundle", user_id=-1, group_id=-1, prog_num=66154, recursive=True) as chown_2431_66154:
                            chown_2431_66154()
            with ResolveSymlinkFilesInFolder(r"/Library/Application Support/Waves/Modules", own_progress_count=3, prog_num=66157) as resolve_symlink_files_in_folder_2432_66157:
                resolve_symlink_files_in_folder_2432_66157()
            with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=66158) as shell_command_2433_66158:
                shell_command_2433_66158()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V15", prog_num=66159) as cd_stage_2434_66159:
            cd_stage_2434_66159()
            with Stage(r"copy", r"Preset Browser V15 1.2 v1.2", prog_num=66160):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r"/Library/Application Support/Waves/Preset Browser/V15", skip_progress_count=3, prog_num=66161) as should_copy_source_2435_66161:
                    should_copy_source_2435_66161()
                    with Stage(r"copy source", r"Mac/Preset Browser/V15/1", prog_num=66162):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V15/1", r".", delete_extraneous_files=True, prog_num=66163) as copy_dir_to_dir_2436_66163:
                            copy_dir_to_dir_2436_66163()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V15/1", user_id=-1, group_id=-1, prog_num=66164, recursive=True) as chown_2437_66164:
                            chown_2437_66164()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/Preset Browser/V16", prog_num=66165) as cd_stage_2438_66165:
            cd_stage_2438_66165()
            with Stage(r"copy", r"Preset Browser V16 1.1 v1.1", prog_num=66166):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r"/Library/Application Support/Waves/Preset Browser/V16", skip_progress_count=3, prog_num=66167) as should_copy_source_2439_66167:
                    should_copy_source_2439_66167()
                    with Stage(r"copy source", r"Mac/Preset Browser/V16/1", prog_num=66168):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Preset Browser/V16/1", r".", delete_extraneous_files=True, prog_num=66169) as copy_dir_to_dir_2440_66169:
                            copy_dir_to_dir_2440_66169()
                        with Chown(path=r"/Library/Application Support/Waves/Preset Browser/V16/1", user_id=-1, group_id=-1, prog_num=66170, recursive=True) as chown_2441_66170:
                            chown_2441_66170()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesLocalServer", prog_num=66171) as cd_stage_2442_66171:
            cd_stage_2442_66171()
            with Stage(r"copy", r"Waves Local Server v12.16.0.1", prog_num=66172):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r"/Library/Application Support/Waves/WavesLocalServer", dont_downgrade=True, skip_progress_count=6, prog_num=66173) as should_copy_source_2443_66173:
                    should_copy_source_2443_66173()
                    with Stage(r"copy source", r"Mac/WavesLocalServer/WavesLocalServer.bundle", prog_num=66174):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=66175, recursive=True) as chmod_2444_66175:
                            chmod_2444_66175()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66176) as copy_dir_to_dir_2445_66176:
                            copy_dir_to_dir_2445_66176()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesLocalServer/WavesLocalServer.bundle", where_to_unwtar=r".", prog_num=66177) as unwtar_2446_66177:
                            unwtar_2446_66177()
                        with Chown(path=r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle", user_id=-1, group_id=-1, prog_num=66178, recursive=True) as chown_2447_66178:
                            chown_2447_66178()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesLocalServer/WavesLocalServer.bundle/Contents/com.waves.wls.agent.plist", r"/Library/LaunchAgents/com.waves.wls.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=66179) as if_2448_66179:
                            if_2448_66179()
        with CdStage(r"copy_to_folder", r"/Library/Application Support/Waves/WavesPluginServer", prog_num=66180) as cd_stage_2449_66180:
            cd_stage_2449_66180()
            with Stage(r"copy", r"WavesPluginServer_V16_1 v16.1.1.2", prog_num=66181):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r"/Library/Application Support/Waves/WavesPluginServer", skip_progress_count=6, prog_num=66182) as should_copy_source_2450_66182:
                    should_copy_source_2450_66182()
                    with Stage(r"copy source", r"Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", prog_num=66183):
                        with Chmod(path=r"${HOME}/Library/Caches/numba", mode="a+rwX", ignore_if_not_exist=True, ignore_all_errors=True, prog_num=66184, recursive=True) as chmod_2451_66184:
                            chmod_2451_66184()
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", r".", hard_links=False, delete_extraneous_files=True, prog_num=66185) as copy_dir_to_dir_2452_66185:
                            copy_dir_to_dir_2452_66185()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WavesPluginServer/WavesPluginServerV16.1.bundle", where_to_unwtar=r".", prog_num=66186) as unwtar_2453_66186:
                            unwtar_2453_66186()
                        with Chown(path=r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle", user_id=-1, group_id=-1, prog_num=66187, recursive=True) as chown_2454_66187:
                            chown_2454_66187()
                        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_true=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", hard_links=False, ignore_all_errors=True, output_script=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products-post-script.sh"), if_false=CopyFileToFile(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/com.waves.wps.V16.1.agent.plist", r"/Library/LaunchAgents/com.waves.wps.V16.1.agent.plist", ignore_if_not_exist=True, hard_links=False), prog_num=66188) as if_2455_66188:
                            if_2455_66188()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/Components", prog_num=66189) as cd_stage_2456_66189:
            cd_stage_2456_66189()
            with Stage(r"copy", r"WaveShell1-AU 16.0 v16.0.23.24", prog_num=66190):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r"/Library/Audio/Plug-Ins/Components", skip_progress_count=8, prog_num=66191) as should_copy_source_2457_66191:
                    should_copy_source_2457_66191()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-AU 16.0.component", prog_num=66192):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", r".", delete_extraneous_files=True, prog_num=66193) as copy_dir_to_dir_2458_66193:
                            copy_dir_to_dir_2458_66193()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-AU 16.0.component", where_to_unwtar=r".", prog_num=66194) as unwtar_2459_66194:
                            unwtar_2459_66194()
                        with Chown(path=r"/Library/Audio/Plug-Ins/Components/WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=66195, recursive=True) as chown_2460_66195:
                            chown_2460_66195()
                        with BreakHardLink(r"WaveShell1-AU 16.0.component/Contents/Info.plist", prog_num=66196) as break_hard_link_2461_66196:
                            break_hard_link_2461_66196()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-AU 16.0.component"', ignore_all_errors=True, prog_num=66197) as shell_command_2462_66197:
                            shell_command_2462_66197()
                        with Chown(path=r"WaveShell1-AU 16.0.component", user_id=-1, group_id=-1, prog_num=66198, recursive=True) as chown_2463_66198:
                            chown_2463_66198()
                        with Chmod(path=r"WaveShell1-AU 16.0.component", mode="a+rwX", prog_num=66199, recursive=True) as chmod_2464_66199:
                            chmod_2464_66199()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST", prog_num=66200) as cd_stage_2465_66200:
            cd_stage_2465_66200()
            with Stage(r"copy", r"WaveShell1-OBS 16.0 v16.0.23.24", prog_num=66201):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r"/Library/Audio/Plug-Ins/VST", skip_progress_count=5, prog_num=66202) as should_copy_source_2466_66202:
                    should_copy_source_2466_66202()
                    with Stage(r"copy source", r"Mac/Shells/Waves StudioRack for OBS.vst", prog_num=66203):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", r".", delete_extraneous_files=True, prog_num=66204) as copy_dir_to_dir_2467_66204:
                            copy_dir_to_dir_2467_66204()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/Waves StudioRack for OBS.vst", where_to_unwtar=r".", prog_num=66205) as unwtar_2468_66205:
                            unwtar_2468_66205()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst", user_id=-1, group_id=-1, prog_num=66206, recursive=True) as chown_2469_66206:
                            chown_2469_66206()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "Waves StudioRack for OBS.vst"', ignore_all_errors=True, prog_num=66207) as shell_command_2470_66207:
                            shell_command_2470_66207()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/VST3", prog_num=66208) as cd_stage_2471_66208:
            cd_stage_2471_66208()
            with Stage(r"copy", r"WaveShell1-VST3-ARA 16.0 v16.0.23.24", prog_num=66209):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=66210) as should_copy_source_2472_66210:
                    should_copy_source_2472_66210()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", prog_num=66211):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", r".", delete_extraneous_files=True, prog_num=66212) as copy_dir_to_dir_2473_66212:
                            copy_dir_to_dir_2473_66212()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3-ARA 16.0.vst3", where_to_unwtar=r".", prog_num=66213) as unwtar_2474_66213:
                            unwtar_2474_66213()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3-ARA 16.0.vst3", user_id=-1, group_id=-1, prog_num=66214, recursive=True) as chown_2475_66214:
                            chown_2475_66214()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3-ARA 16.0.vst3"', ignore_all_errors=True, prog_num=66215) as shell_command_2476_66215:
                            shell_command_2476_66215()
            with Stage(r"copy", r"WaveShell1-VST3 16.0 v16.0.23.24", prog_num=66216):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r"/Library/Audio/Plug-Ins/VST3", skip_progress_count=5, prog_num=66217) as should_copy_source_2477_66217:
                    should_copy_source_2477_66217()
                    with Stage(r"copy source", r"Mac/Shells/WaveShell1-VST3 16.0.vst3", prog_num=66218):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", r".", delete_extraneous_files=True, prog_num=66219) as copy_dir_to_dir_2478_66219:
                            copy_dir_to_dir_2478_66219()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Shells/WaveShell1-VST3 16.0.vst3", where_to_unwtar=r".", prog_num=66220) as unwtar_2479_66220:
                            unwtar_2479_66220()
                        with Chown(path=r"/Library/Audio/Plug-Ins/VST3/WaveShell1-VST3 16.0.vst3", user_id=-1, group_id=-1, prog_num=66221, recursive=True) as chown_2480_66221:
                            chown_2480_66221()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" "WaveShell1-VST3 16.0.vst3"', ignore_all_errors=True, prog_num=66222) as shell_command_2481_66222:
                            shell_command_2481_66222()
        with CdStage(r"copy_to_folder", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66223) as cd_stage_2482_66223:
            cd_stage_2482_66223()
            with Stage(r"copy", r"WaveShell1-WPAPI_2 16.0 v16.0.23.24", prog_num=66224):
                with ShouldCopySource(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r"/Library/Audio/Plug-Ins/WPAPI", skip_progress_count=7, prog_num=66225) as should_copy_source_2483_66225:
                    should_copy_source_2483_66225()
                    with Stage(r"copy source", r"Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", prog_num=66226):
                        with CopyDirToDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", r".", delete_extraneous_files=True, prog_num=66227) as copy_dir_to_dir_2484_66227:
                            copy_dir_to_dir_2484_66227()
                        with Unwtar(what_to_unwtar=r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", where_to_unwtar=r".", prog_num=66228) as unwtar_2485_66228:
                            unwtar_2485_66228()
                        with Chown(path=r"/Library/Audio/Plug-Ins/WPAPI/WaveShell1-WPAPI_2 16.0.bundle", user_id=-1, group_id=-1, prog_num=66229, recursive=True) as chown_2486_66229:
                            chown_2486_66229()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Library/Audio/Plug-Ins/WPAPI" -c', ignore_all_errors=True, prog_num=66230) as shell_command_2487_66230:
                            shell_command_2487_66230()
                        with ScriptCommand(r'if [ -f "/Library/Audio/Plug-Ins/WPAPI"/Icon? ]; then chmod a+rw "/Library/Audio/Plug-Ins/WPAPI"/Icon?; fi', prog_num=66231) as script_command_2488_66231:
                            script_command_2488_66231()
                        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" --extension bundle --folder . -c', ignore_all_errors=True, prog_num=66232) as shell_command_2489_66232:
                            shell_command_2489_66232()
            with CreateSymlink(r"/Users/rsp_ms/Library/Preferences/Waves Preferences/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66233) as create_symlink_2490_66233:
                create_symlink_2490_66233()
            with CreateSymlink(r"/Users/Shared/Waves/Waves Plugins WPAPI", r"/Library/Audio/Plug-Ins/WPAPI", prog_num=66234) as create_symlink_2491_66234:
                create_symlink_2491_66234()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/Presets", prog_num=66235) as cd_stage_2492_66235:
            cd_stage_2492_66235()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Bass Fingers Presets", prog_num=66236) as rm_file_or_dir_2493_66236:
                rm_file_or_dir_2493_66236()
            with RmFileOrDir(r"/Applications/Waves/Data/Instrument Data/Flow Motion Presets", prog_num=66237) as rm_file_or_dir_2494_66237:
                rm_file_or_dir_2494_66237()
            with RmFileOrDir(r"/Applications/Waves/Data/Q-Clone presets", prog_num=66238) as rm_file_or_dir_2495_66238:
                rm_file_or_dir_2495_66238()
        with CdStage(r"create_copy_instructions_for_no_copy_folder", r"/Applications/Waves/Data/NKS FX", prog_num=66239) as cd_stage_2496_66239:
            cd_stage_2496_66239()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/MMToneShaper", prog_num=66240) as rm_file_or_dir_2497_66240:
                rm_file_or_dir_2497_66240()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch", prog_num=66241) as rm_file_or_dir_2498_66241:
                rm_file_or_dir_2498_66241()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 3", prog_num=66242) as rm_file_or_dir_2499_66242:
                rm_file_or_dir_2499_66242()
            with RmFileOrDir(r"/Applications/Waves/Data/NKS FX/UPitch 6", prog_num=66243) as rm_file_or_dir_2500_66243:
                rm_file_or_dir_2500_66243()
        with ShellCommand(r"/Library/Application Support/Waves/WavesPluginServer/WavesPluginServerV16.1.bundle/Contents/MacOS/WavesPluginServer", message=r"Start WavesPluginServer", detach=True, prog_num=66244) as shell_command_2501_66244:
            shell_command_2501_66244()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/COSMOS" -c', ignore_all_errors=True, prog_num=66245) as shell_command_2502_66245:
            shell_command_2502_66245()
        with ScriptCommand(r'if [ -f "/Applications/Waves/COSMOS"/Icon? ]; then chmod a+rw "/Applications/Waves/COSMOS"/Icon?; fi', prog_num=66246) as script_command_2503_66246:
            script_command_2503_66246()
        with RmFileOrDir(r"/Users/rsp_ms/Library/Caches/Waves", prog_num=66247) as rm_file_or_dir_2504_66247:
            rm_file_or_dir_2504_66247()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66248) as move_dir_to_dir_2505_66248:
            move_dir_to_dir_2505_66248()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66249) as move_dir_to_dir_2506_66249:
            move_dir_to_dir_2506_66249()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66250) as move_dir_to_dir_2507_66250:
            move_dir_to_dir_2507_66250()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/Acoustics.net Impulses", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66251) as move_dir_to_dir_2508_66251:
            move_dir_to_dir_2508_66251()
        with MakeDirs(r"/Applications/Waves/Data/IR1Impulses/Library Presets", prog_num=66252) as make_dirs_2509_66252:
            make_dirs_2509_66252()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66253) as move_dir_to_dir_2510_66253:
            move_dir_to_dir_2510_66253()
        with MoveDirToDir(r"/Applications/Waves/Plug-Ins V9/IR1Impulses V2", r"/Applications/Waves/Data", ignore_all_errors=True, prog_num=66254) as move_dir_to_dir_2511_66254:
            move_dir_to_dir_2511_66254()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves" -c', ignore_all_errors=True, prog_num=66255) as shell_command_2512_66255:
            shell_command_2512_66255()
        with ScriptCommand(r'if [ -f "/Applications/Waves"/Icon? ]; then chmod a+rw "/Applications/Waves"/Icon?; fi', prog_num=66256) as script_command_2513_66256:
            script_command_2513_66256()
        with RmFileOrDir(r"/Applications/Waves/Utilities", prog_num=66257) as rm_file_or_dir_2514_66257:
            rm_file_or_dir_2514_66257()
        with Touch(r"/Library/Audio/Plug-Ins/VST/Waves StudioRack for OBS.vst/Contents/Info.plist", prog_num=66258) as touch_2515_66258:
            touch_2515_66258()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3", Touch, r"path", prog_num=66259) as glober_2516_66259:
            glober_2516_66259()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/Info.plist", Touch, r"path", prog_num=66260) as glober_2517_66260:
            glober_2517_66260()
        with Glober(r"/Library/Audio/Plug-Ins/VST3/WaveShell*.vst3/Contents/MacOS/WaveShell*-VST3", Touch, r"path", prog_num=66261) as glober_2518_66261:
            glober_2518_66261()
        with ShellCommand(r'"/Applications/Waves/WaveShells V13/Waves AU Reg Utility 13.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66262) as shell_command_2519_66262:
            shell_command_2519_66262()
        with ShellCommand(r'"/Applications/Waves/WaveShells V14/Waves AU Reg Utility 14.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66263) as shell_command_2520_66263:
            shell_command_2520_66263()
        with ShellCommand(r'"/Applications/Waves/WaveShells V15/Waves AU Reg Utility 15.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66264) as shell_command_2521_66264:
            shell_command_2521_66264()
        with ShellCommand(r'"/Applications/Waves/WaveShells V16/Waves AU Reg Utility 16.app/Contents/MacOS/Waves AU Reg Utility" -s --log "${HOME}/Library/Application Support/Waves Audio/Waves Central/Logs/AURegUtility.log"', ignore_all_errors=True, prog_num=66265) as shell_command_2522_66265:
            shell_command_2522_66265()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/WaveShells V16" -c', ignore_all_errors=True, prog_num=66266) as shell_command_2523_66266:
            shell_command_2523_66266()
        with ScriptCommand(r'if [ -f "/Applications/Waves/WaveShells V16"/Icon? ]; then chmod a+rw "/Applications/Waves/WaveShells V16"/Icon?; fi', prog_num=66267) as script_command_2524_66267:
            script_command_2524_66267()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log"), prog_num=66268) as if_2525_66268:
            if_2525_66268()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesLocalServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=66269) as if_2526_66269:
            if_2526_66269()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Touch(r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log"), prog_num=66270) as if_2527_66270:
            if_2527_66270()
        with If(IsConfigVarDefined(r"POST_INSTALL_SCRIPT_FILE"), if_false=Chmod(path=r"/Users/rsp_ms/Library/Logs/Waves Audio/WavesPluginServer.log", mode="a+rw", ignore_if_not_exist=True), prog_num=66271) as if_2528_66271:
            if_2528_66271()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", prog_num=66272) as make_dir_2529_66272:
            make_dir_2529_66272()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server", mode="a+rwx", ignore_if_not_exist=True, prog_num=66273) as chmod_2530_66273:
            chmod_2530_66273()
        with MakeDir(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", prog_num=66274) as make_dir_2531_66274:
            make_dir_2531_66274()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1", mode="a+rwx", ignore_if_not_exist=True, prog_num=66275) as chmod_2532_66275:
            chmod_2532_66275()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/.settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=66276) as chmod_2533_66276:
            chmod_2533_66276()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/V16.1/settings.txt", mode="a+rw", ignore_if_not_exist=True, prog_num=66277) as chmod_2534_66277:
            chmod_2534_66277()
        with Chmod(path=r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Plugin Server/wps.sqlite", mode="a+rw", ignore_if_not_exist=True, prog_num=66278) as chmod_2535_66278:
            chmod_2535_66278()
        with ShellCommand(r'"/Applications/Waves Central.app/Contents/Resources/res/external/bin/setIcon" -f -i "/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/Mac/Icons/Folder.icns" --folder "/Applications/Waves/Data" -c', ignore_all_errors=True, prog_num=66279) as shell_command_2536_66279:
            shell_command_2536_66279()
        with ScriptCommand(r'if [ -f "/Applications/Waves/Data"/Icon? ]; then chmod a+rw "/Applications/Waves/Data"/Icon?; fi', prog_num=66280) as script_command_2537_66280:
            script_command_2537_66280()
    with Stage(r"post-copy", prog_num=66281):
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=66282) as make_dir_2538_66282:
            make_dir_2538_66282()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/have_info_map.txt", r"/Library/Application Support/Waves/Central/V16/have_info_map.txt", hard_links=False, copy_owner=True, prog_num=66283) as copy_file_to_file_2539_66283:
            copy_file_to_file_2539_66283()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/old_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66284) as chmod_2540_66284:
            chmod_2540_66284()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66285) as chmod_2541_66285:
            chmod_2541_66285()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/require.yaml", r"/Library/Application Support/Waves/Central/V16/old_require.yaml", ignore_if_not_exist=True, hard_links=False, copy_owner=True, prog_num=66286) as copy_file_to_file_2542_66286:
            copy_file_to_file_2542_66286()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/new_require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66287) as chmod_2543_66287:
            chmod_2543_66287()
        with CopyFileToFile(r"/Library/Application Support/Waves/Central/V16/new_require.yaml", r"/Library/Application Support/Waves/Central/V16/require.yaml", hard_links=False, copy_owner=True, prog_num=66288) as copy_file_to_file_2544_66288:
            copy_file_to_file_2544_66288()
        with Chmod(path=r"/Library/Application Support/Waves/Central/V16/require.yaml", mode="a+rw", ignore_all_errors=True, prog_num=66289) as chmod_2545_66289:
            chmod_2545_66289()
        Progress(r"Done copy", prog_num=66290)()
        Progress(r"Done synccopy", prog_num=66291)()
    with Stage(r"post", prog_num=66292):
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=66293) as make_dir_2546_66293:
            make_dir_2546_66293()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/cache/V16_repo_rev.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/V16_repo_rev.yaml", hard_links=False, copy_owner=True, prog_num=66294) as copy_file_to_file_2547_66294:
            copy_file_to_file_2547_66294()
        with MakeDir(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping", chowner=True, prog_num=66295) as make_dir_2548_66295:
            make_dir_2548_66295()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/index.yaml", hard_links=False, copy_owner=True, prog_num=66296) as copy_file_to_file_2549_66296:
            copy_file_to_file_2549_66296()
        with MakeDir(r"/Library/Application Support/Waves/Central/V16", chowner=True, prog_num=66297) as make_dir_2550_66297:
            make_dir_2550_66297()
        with CopyFileToFile(r"/Users/rsp_ms/Library/Caches/Waves Audio/instl/instl/V16/bookkeeping/6/index.yaml", r"/Library/Application Support/Waves/Central/V16/index.yaml", hard_links=False, copy_owner=True, prog_num=66298) as copy_file_to_file_2551_66298:
            copy_file_to_file_2551_66298()

with Stage(r"epilog", prog_num=66299):
    with PatchPyBatchWithTimings(r"/Users/rsp_ms/Library/Application Support/Waves Audio/Waves Central/Logs/install/synccopy_16-20250629165704-products.py", prog_num=66300) as patch_py_batch_with_timings_2552_66300:
        patch_py_batch_with_timings_2552_66300()

log.info("Shakespeare says: All's Well That Ends Well")
# eof


