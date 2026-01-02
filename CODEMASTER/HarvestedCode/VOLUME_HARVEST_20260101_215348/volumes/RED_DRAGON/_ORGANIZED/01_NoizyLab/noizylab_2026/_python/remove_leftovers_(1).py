#!/usr/bin/env python3

import os
import re
import utils
import pyinstl
from configVar import var_stack

the_current_os = var_stack.ResolveVarToStr("__CURRENT_OS__")
if the_current_os == "Mac":
    waveslib_extension = ".framework"
elif the_current_os == "Win":
    waveslib_extension = ".dll"

if not 'get_info_from_plugin' in dir(utils):
    print('Not supported instl version')
    sys.exit(0)

def main():
    var_stack.read_environment(['ProgramFiles(x86)', 'ProgramW6432', 'CommonProgramW6432', 'CommonProgramFiles(x86)'])
    plugin_path = var_stack.ResolveVarToStr("WAVES_PLUGINS_DIR")
    venue_path = var_stack.ResolveVarToStr("WAVES_SOUNDGRID_FOR_VENUE_DIR")
    studio_path = var_stack.ResolveVarToStr("WAVES_SOUNDGRID_STUDIO_DIR")

    if 'V9' in plugin_path:
        plugin_ver = "9."
    elif 'V10' in plugin_path:
        plugin_ver = "10."
    else:
        plugin_ver = "Unknow version"

    ignore_regexes_filter = utils.check_binaries_versions_filter_with_ignore_regexes()
    ignore_folder_regex_list = var_stack.ResolveVarToList("CHECK_BINARIES_VERSION_FOLDER_EXCLUDE_REGEX_FOR_REMOVE_LEFTOVERS")
    ignore_regexes_filter.set_folder_ignore_regexes(ignore_folder_regex_list)

    #build list of plugin dictionaries and list of waveslib's
    binaries_version_from_plugin_folder = utils.check_binaries_versions_in_folder(the_current_os, plugin_path, ignore_regexes_filter)
    plugin_info_list = list()
    waveslib_list = list()
    for a_item in binaries_version_from_plugin_folder:
        if 'ArtistDlls' not in a_item[0]:
            if 'bundle' in a_item[0]:
                plugin_info_list.append(utils.get_info_from_plugin(None,a_item[0]))
            elif 'WavesLib' in a_item[0]:
                waveslib_list.append(a_item)

    for waveslib_item in waveslib_list:
        remove_item = True
        for plugin_item in plugin_info_list:
             for waveslib_name in plugin_item['DynamicPluginLibName']:
                if os.path.split(waveslib_item[0])[1] in waveslib_name:
                    remove_item = False
                    break
             if not remove_item:
                break
        if remove_item:
            print('Removing left over - '+waveslib_item[0],flush=True)
            utils.safe_remove_file_system_object(waveslib_item[0])
            if 'WavesLib_9.6' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls1',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls1')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls1',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls1')
            if 'WavesLib_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls2',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls2')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls2',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls2')
            if 'WavesLib3_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls3',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls3')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls3',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls3')
            if 'WavesLib4_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls4',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls4')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls4',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls4')
            if 'WavesLib5_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls5',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls5')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls5',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls5')
            if 'WavesLib6_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls6',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls6')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls6',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls6')
            if 'WavesLib7_9.91' in waveslib_item[0]:
                if the_current_os == "Mac":
                    print('Removing left over - /Applications/Waves/Plug-Ins V9/ArtistDlls7',flush=True)
                    utils.safe_remove_file_system_object('/Applications/Waves/Plug-Ins V9/ArtistDlls7')
                if the_current_os == "Win":
                    print('Removing left over - C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls7',flush=True)
                    utils.safe_remove_file_system_object('C:\Program Files (x86)\Waves\Plug-Ins V9\ArtistDlls7')

    binaries_version_from_venue_folder = utils.check_binaries_versions_in_folder(the_current_os, venue_path, ignore_regexes_filter)
    for a_item in binaries_version_from_venue_folder:
        if 'SoundGridRack.bundle' in a_item[0]:
            plugin_info_list.append(utils.get_info_from_plugin(None,a_item[0]))

    binaries_version_from_studio_folder = utils.check_binaries_versions_in_folder(the_current_os, studio_path, ignore_regexes_filter)
    for a_item in binaries_version_from_studio_folder:
        if 'StudioRack.bundle' in a_item[0]:
            plugin_info_list.append(utils.get_info_from_plugin(None,a_item[0]))

    #list all shells
    shell_list = list()
    shells_dirs = var_stack.ResolveVarToList("WAVES_SHELL_DIRS")
    for shell_dir in shells_dirs:
        shell_list.append(utils.check_binaries_versions_in_folder(the_current_os, shell_dir, ignore_regexes_filter))

    for shell_group in shell_list:
        for shell_item in shell_group:
            if 'WaveShell' in shell_item[0] and 'Waves AU Reg Utility' not in shell_item[0]:
                remove_item = True
                remove_WPAPI = True
                for plugin_item in plugin_info_list:
                    #for Insert plugin do not scan shells
                    if 'a39d317a-5e89-4dd2-949a-7b2c15836a10' not in plugin_item['LicenseGUID']:
                        shell_base_name = plugin_item.get('WaveShellsBaseName', None)
                        if shell_base_name:
                            if plugin_item['WaveShellsBaseName'] in shell_item[0]:
                                remove_item = False
                                break
                        else:
                            major, minor, *other = shell_item[1].split('.', 3)
                            major_from_dict, minor_from_dict, *other_from_dict = plugin_item['PluginExternalVersion'].split('.', 3)
                            if major+'.'+minor == major_from_dict+'.'+minor_from_dict:
                                remove_item = False
                                break
                    #for Insert plugin keep WPAPI
                    else:
                        remove_WPAPI = False
                if remove_item and plugin_ver in shell_item[0]:
                    if 'WPAPI' not in shell_item[0]:
                        print('Removing left over - '+shell_item[0],flush=True)
                        utils.safe_remove_file_system_object(shell_item[0])
                    elif remove_WPAPI:
                        print('Removing left over - '+shell_item[0],flush=True)
                        utils.safe_remove_file_system_object(shell_item[0])
                    if the_current_os == "Mac":
                        if '-AU ' in shell_item[0] and '/Applications/Waves/WaveShells' in shell_item[0]:
                            p0, p1, p2, p3, *other = shell_item[0].split('/')
                            waveshell_path = '/'+p1+'/'+p2+'/'+p3+'/'
                            infra = shell_item[0].split(waveshell_path+'WaveShell')[1].split('-AU')[0]
                            major, minor, *other = shell_item[1].split('.', 3)
                            print('Removing left over - '+waveshell_path+'Waves AU Reg Utility'+infra+' '+major+'.'+minor+'.app',flush=True)
                            utils.safe_remove_file_system_object(waveshell_path+'Waves AU Reg Utility'+infra+' '+major+'.'+minor+'.app')

main()
