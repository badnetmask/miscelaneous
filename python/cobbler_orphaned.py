#!/usr/bin/python
#
# $id: cobbler_orphaned.py,v 1.0.0 2017/10/30 14:01:02 mteixeir Exp $
# Copyright (C) 2017
#
# Last Modified: 2017/10/31 15:20:31
#
# Helps finding orphaned distros and profiles in a Cobbler server.

import argparse
import sys
import os
import json

def find_distros():
    all_distros = []

    # find all configured distros
    distpath = os.path.join(args.conf_dir, 'config/distros.d')
    for jsonfile in os.listdir(distpath):
        if os.path.isfile(os.path.join(distpath,jsonfile)):
            data = json.load(open(os.path.join(distpath, jsonfile), 'r'))
            all_distros.append(data['name'])

    return sorted(all_distros)

def find_profiles(and_distros=False):
    all_profiles = []
    used_distros = []

    # find all configured profiles
    profpath = os.path.join(args.conf_dir, 'config/profiles.d')
    for jsonfile in os.listdir(profpath):
        if os.path.isfile(os.path.join(profpath, jsonfile)):
            data = json.load(open(os.path.join(profpath, jsonfile), 'r'))
            all_profiles.append(data['name'])
            if and_distros:
                # we also want to know the distros
                if data['parent'] not in used_distros:
                    used_distros.append(data['parent'])

    if and_distros:
        return sorted(all_profiles), sorted(used_distros)
    else:
        return sorted(all_profiles)

def find_orphaned_profiles():
    all_profiles = find_profiles()
    all_profiles_from_systems = []
    orphaned_profiles = []

    # extract all profiles from all systems
    syspath = os.path.join(args.conf_dir, 'config/systems.d')
    for jsonfile in os.listdir(syspath):
        if os.path.isfile(os.path.join(syspath, jsonfile)):
            data = json.load(open(os.path.join(syspath, jsonfile), 'r'))
            if data['profile'] not in all_profiles_from_systems:
                all_profiles_from_systems.append(data['profile'])

    # now we find the orphaned profiles
    for profile in all_profiles:
        if profile not in all_profiles_from_systems:
            orphaned_profiles.append(profile)

    return sorted(orphaned_profiles)

def find_orphaned_distros():
    all_profiles, used_distros = find_profiles(and_distros=True)
    orphaned_distros = []

    # find all distros that are not used by any profiles
    for distro in find_distros():
        if (distro not in used_distros) and (distro not in orphaned_distros):
            orphaned_distros.append(distro)

    return sorted(orphaned_distros)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cobbler_orphaned.py is used to find orphaned things in Cobbler')
    parser.add_argument('-c', '--conf_dir', default='/var/lib/cobbler', help='Path wher Cobbler store config files')
    parser.add_argument('-p', '--profiles', action='store_true', help='(action) Find orphaned profiles')
    parser.add_argument('-d', '--distros', action='store_true', help='(action) Find orphaned distros')
    args = parser.parse_args()
    if not (args.profiles or args.distros):
        print("At least one action is required!\n")
        parser.print_help()
        sys.exit(1)

    if not os.path.isdir(args.conf_dir):
        print("Can't read configs from %s (is it valid?)\n" % args.conf_dir)
        parser.print_help()
        sys.exit(1)

    if args.profiles:
        orphaned_profiles = find_orphaned_profiles()
        for profile in orphaned_profiles:
            print(profile)

    if args.distros:
        orphaned_distros = find_orphaned_distros()
        for distro in orphaned_distros:
            print(distro)
