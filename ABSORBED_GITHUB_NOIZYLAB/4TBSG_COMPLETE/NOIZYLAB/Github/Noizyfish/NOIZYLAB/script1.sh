#!/bin/sh
volPath=$1
rm "$volPath/System/Installation/Packages"
cp -R "/Volumes/OS X Install ESD/Packages" "$volPath/System/Installation/"
cp "/Volumes/OS X Install ESD/BaseSystem.dmg" "$volPath/"
cp "/Volumes/OS X Install ESD/BaseSystem.chunklist" "$volPath/"