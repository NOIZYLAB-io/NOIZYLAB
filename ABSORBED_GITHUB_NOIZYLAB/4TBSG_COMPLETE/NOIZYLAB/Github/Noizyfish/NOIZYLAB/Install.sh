#!/bin/sh

#  Uninstall.sh
#  Omni
#
#  Created by Betty Wang on 2017/8/15.
#
location, parentFolder, source,

TERGET="$1"
SOURCE="$2"
PARENT="$3"

# 1.delete app
rm -rf "${TERGET}"

# 2.create folder
mkdir -p "${PARENT}"

# 3.move to target
mv "${SOURCE}" "${PARENT}"
