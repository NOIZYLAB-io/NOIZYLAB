#!/usr/bin/env python3
"""
Requirements:
- Python Python 3
- fastboot build artifact
"""
import argparse
import glob
import os
import platform
import re
import struct
import subprocess
import sys
from collections import namedtuple
from distutils.spawn import find_executable
from time import sleep

fastboot_vars = {}
staging_location = None
fastboot_path = None
adb_path = None

try:
    # python2 support
    input = raw_input
except NameError:
    pass


class FlashAllException(Exception):
    pass


class BatteryLevelException(Exception):
    pass


def is_windows():
    return platform.system() == "Windows"


def init_staging_location():
    global staging_location
    # Always use the image files from the update package if available
    if os.path.exists(os.path.join(sys.path[0], "android-info.txt")):
        return
    if "OUT" in os.environ:
        staging_location = os.path.join(os.environ["OUT"], "flash_all")
    if staging_location and not os.path.isdir(staging_location):
        staging_location = None


def init_android_tools(toolspath=None):
    global adb_path
    global fastboot_path

    if toolspath:
        # Look in tools path
        adb_path = find_executable("adb", toolspath)
        if adb_path is None:
            raise OSError("adb not found in {}".format(toolspath))
        fastboot_path = find_executable("fastboot", toolspath)
        if fastboot_path is None:
            raise OSError("fastboot not found in {}".format(toolspath))
    else:
        # Look in PATH
        adb_path = find_executable("adb")
        if adb_path is None:
            raise OSError("adb not found in PATH")
        fastboot_path = find_executable("fastboot")
        if fastboot_path is None:
            raise OSError("fastboot not found in PATH")

    print(" [ADB]                : {}".format(adb_path))
    print(" [FASTBOOT]           : {}".format(fastboot_path))
    check_fastboot_version()
    check_adb_version()


def img_path(filename):
    """Returns the full path of files relative to the script location."""
    if staging_location:
        return os.path.join(staging_location, filename)
    return os.path.join(sys.path[0], filename)


def extract_system_image_metadata(filename):
    with open(filename, "rb") as system_image:
        header_bin = system_image.read(28)
        header = struct.unpack("<I4H4I", header_bin)

        magic = header[0]
        major_version = header[1]
        minor_version = header[2]
        file_hdr_sz = header[3]
        chunk_hdr_sz = header[4]
        blk_sz = header[5]
        total_chunks = header[7]

        assert magic == 0xED26FF3A, "Incorrect magic"
        assert major_version == 1 and minor_version == 0, "Incorrect version number"
        assert file_hdr_sz == 28, "Incorrect file header size"

        for i in range(1, total_chunks + 1):
            header_bin = system_image.read(chunk_hdr_sz)
            chunk_type, _, chunk_sz, total_sz = struct.unpack("<2H2I", header_bin)
            data_sz = total_sz - chunk_hdr_sz

            if chunk_type == 0xCAC1:
                assert data_sz == (
                    chunk_sz * blk_sz
                ), "Chunk #{} - Invalid data size".format(i)

                data_start = system_image.tell()
                data = system_image.read(32)
                try:
                    data = data.decode("ascii")
                    if data.lstrip().startswith("# begin build properties"):
                        data += system_image.read(data_sz - 32).decode("ascii")
                        return dict(
                            re.findall(r"(ro\.build\.[^#=\s]+?)=([^#=\s]+?)\n", data)
                        )
                except Exception:
                    continue
                finally:
                    # Not an ASCII file chunk -OR- not the one we're looking for.
                    system_image.seek(data_start + data_sz)

    # If we get here that's bad news... we couldn't find the build props in system.img
    raise Exception("No build properties found in system.img")


def parse_package_metadata():
    with open(img_path("android-info.txt")) as f:
        lines = f.readlines()

    return dict(line.rstrip().split("=") for line in lines)


def get_this_firmware_arb_version():
    with open(img_path("android-info.txt")) as f:
        lines = f.readlines()
        for line in lines:
            if "current_firmware_image_anti_rollback_version" in line:
                metadata = line.rstrip().split("=")
                return int(metadata[1])
        # If there is no "current_firmware_image_anti_rollback_version" in
        # android-info.txt file , return None .
        return None


def get_min_required_firmware_arb_version_for_device():
    device_info = fastboot_device_info()

    try:
        print(
            "Required Non-HLOS/Firmware Min anti-rollback version {}".format(
                device_info["Required Non-HLOS/Firmware Min anti-rollback version"]
            )
        )
        return int(device_info["Required Non-HLOS/Firmware Min anti-rollback version"])
    except KeyError:
        # Device Info on some products might not populate
        # "Required Non-HLOS/Firmware Min anti-rollback version"
        # Hence,when the device info does not have the field
        # "Required Non-HLOS/Firmware Min anti-rollback version",just return None
        return None


def is_firmware_of_sufficient_arb_version():
    this_arb_version = get_this_firmware_arb_version()
    required_arb_version = get_min_required_firmware_arb_version_for_device()
    if this_arb_version is None:
        # This package does not explicitly identify an ARB version; assume it is zero
        this_arb_version = 0
    if required_arb_version is None:
        # The bootloader is too old. Assume it is zero also
        required_arb_version = 0
    return this_arb_version >= required_arb_version


def fastboot_getvar(v, default=""):
    """Returns value of the specified fastboot variable. Empty string if not found."""

    # check if we've already gotten the variables
    if len(fastboot_vars) == 0:
        try:
            response = fastboot_output(["getvar", "all"])
        except subprocess.CalledProcessError:
            raise OSError("fastboot getvar all failed")

        prefix = b"(bootloader) "
        for line in response.splitlines():
            if prefix in line:
                suffix = line.split(prefix, 1)[1]
                suffix_split = suffix.rsplit(b":", 1)
                key = suffix_split[0].strip().decode("utf-8")
                value = suffix_split[1].strip().decode("utf-8")
                fastboot_vars[key] = value

    # return requested variable
    try:
        value = fastboot_vars[v]
        return value
    except KeyError:
        return default


def adb_args(cmd, no_serial=False):
    if args.serial is not None and not no_serial:
        cmd = ["-s", args.serial] + cmd

    cmd = [adb_path] + cmd
    if args.trace:
        print(" [Exec] : {}".format(" ".join(cmd)))
    return cmd


def adb_output(command):
    """Issues the specified ADB command."""
    return subprocess.check_output(adb_args(command))


def adb(command, check_error=True):
    """Issues the specified adb command and returns its output."""

    success = subprocess.call(adb_args(command)) == 0
    if check_error and not success:
        raise ValueError("fastboot command {} failed".format(command))

    return success


def fastboot_args(cmd, no_serial=False):
    if args.serial is not None and not no_serial:
        cmd = ["-s", args.serial] + cmd

    cmd = [fastboot_path] + cmd
    if args.trace:
        print(" [Exec] : {}".format(" ".join(cmd)))
    return cmd


def fastboot_output(command, universal_newlines=False, no_serial=False):
    """Issues the specified fastboot command and returns its output."""
    return subprocess.check_output(
        fastboot_args(command, no_serial=no_serial),
        stderr=subprocess.STDOUT,
        universal_newlines=universal_newlines,
    )


def fastboot(command, check_error=True):
    """Issues the specified fastboot command."""

    success = subprocess.call(fastboot_args(command)) == 0
    if check_error and not success:
        raise ValueError("fastboot command {} failed".format(command))

    return success


def fastboot_device_present():
    """Returns true if a fastboot device is present"""
    serial = args.serial
    response = fastboot_output(["devices"], universal_newlines=True, no_serial=True)

    if serial is None:
        return "fastboot" in response
    else:
        return serial in response


def fastboot_device_info():
    """Returns a dict of attributes from `oem device-info`"""
    try:
        response = fastboot_output(["oem", "device-info"])
    except subprocess.CalledProcessError:
        raise RuntimeError("fastboot oem device-info failed")

    device_info = {}
    prefix = b"(bootloader) "
    for line in response.splitlines():
        if prefix in line:
            suffix = line.split(prefix, 1)[1]
            suffix_split = suffix.rsplit(b":", 1)
            key = suffix_split[0].strip().decode("utf-8")
            value = suffix_split[1].strip().decode("utf-8")
            device_info[key] = value

    return device_info


def fastboot_device_unlocked(device_info):
    """Return true if device is OEM unlocked"""
    if device_info is None:
        device_info = fastboot_device_info()
    try:
        return device_info["Device unlocked"] == "true"
    except KeyError:
        return False


def fastboot_device_oculus_bootloader():
    """Returns True if the fastboot device is running an Oculus bootloader"""
    oculus_bootloader_version = fastboot_getvar("oculus-ext-version", None)
    return oculus_bootloader_version is not None


def fastboot_device_oculus_bootloader_ver():
    ver = fastboot_getvar("oculus-ext-version", None)
    if ver is None:
        raise FlashAllException("Not running oculus bootloader")

    try:
        int_ver = int(ver)
        if int_ver < 1:
            raise FlashAllException("Unexpected bootloader version: {} ".format(ver))
        return int_ver
    except Exception:
        raise ValueError("Error parsing bootloader version: {}".format(ver))


def fastboot_device_product():
    """Returns the main product name for the device (pacific, monterey, etc.)"""
    if fastboot_device_oculus_bootloader():
        product = fastboot_getvar("product", None)
        if product is not None:
            return product
    return "unknown"


def fastboot_device_model_rev():
    """Returns the main model revision for the device (pacific, monterey, etc.)"""
    if fastboot_device_oculus_bootloader():
        product = fastboot_getvar("model-revision", None)
        if product is not None:
            return product
    return "unknown"


def fastboot_device_critical_unlocked(device_info):
    """Return true if device is critical unlocked (i.e. all commands available)"""
    if device_info is None:
        device_info = fastboot_device_info()
    try:
        return device_info["Device critical unlocked"] == "true"
    except KeyError:
        return False


def fastboot_get_kernel_flavor():
    """Returns the build flavor of the kernel on the device"""
    flavor = None
    try:
        response = fastboot_output(["oem", "get-kernel-flavor"])
    except subprocess.CalledProcessError:
        print("The current bootloader doesn't support get-kernel-flavor command")
        flavor = "unknown"

    if flavor is None:
        prefix = b"(bootloader) "
        flavor = "unknown"
        for line in response.splitlines():
            if prefix in line:
                flavor = line.split(prefix, 1)[1].decode("utf-8")
                break

    return flavor


def fastboot_clear_production_mode():
    """Clear production mode flag and use all available memory"""
    try:
        print("Clearing production mode...")
        fastboot_output(["oem", "set-production-mode", "0"])
    except subprocess.CalledProcessError:
        print("The device doesn't support set-production-mode command, this is ok.")


def fastboot_clear_arb_indexes():
    """Clear anti-rollback indexes"""
    try:
        print("Clearing ARB indexes...")
        fastboot_output(["oem", "reset-rollback-indexes"])
    except subprocess.CalledProcessError:
        print("The device doesn't support resetting anti-rollback indexes, this is ok.")


def wait_for_fastboot_device():
    """Blocks until a fastboot device is detected or a 60s timeout occurs."""

    # wait for device to come back online
    for _ in range(0, 60):
        if fastboot_device_present():
            return
        sleep(1)

    raise OSError("timed out waiting for fastboot device")


def reboot_bootloader():
    """Reboots the fastboot device back into fastboot mode."""

    fastboot(["reboot-bootloader"])
    sleep(1)

    wait_for_fastboot_device()

    # Force reload all variable on the next getvar
    fastboot_vars.clear()


def check_repartition_required(package_metadata):
    """Returns True is if the fastboot device requires a repartition."""

    # Check if repartition is needed
    slot_count = fastboot_getvar("slot-count")
    if slot_count != "2":
        return True

    product = fastboot_device_product()
    device_layout = fastboot_getvar("oculus-partition-ver", None)

    if device_layout is not None:
        package_layout = package_metadata.get("partition-version", "")
        if args.trace:
            print(
                " [repartition] : version check => device={}, package={}".format(
                    device_layout, package_layout
                )
            )
        return device_layout != package_layout

    # Fall back to Android N
    if product == "monterey":
        ovrtz = fastboot_getvar("has-slot:ovrtz")
        return True if ovrtz != "Yes" else False

    raise FlashAllException("Unable to determine if repartion required for " + product)


def repartition():
    """Performs a repartion of the device."""

    # Confirm that the user wants to repartition
    print(
        "You are going to do repartition. "
        "Your persist partition may be lost if something goes wrong.\n"
        "Continue only if you have a backup of the persist partition.\n"
        "Ex. 'adb root; adb shell dd if=/dev/block/bootdevice/by-name/persist of=/data/local/tmp/persist.img && adb pull /data/local/tmp/persist.img'\n"
        "Do you want to continue? (y/N): "
    )
    if args.yes:
        print("y")
        confirm = "y"
    else:
        confirm = input().lower()

    if confirm != "y":
        raise ValueError("Cannot continue without reparitioning.")

    print("REPARTITIONING DEVICE - DO NOT DISCONNECT")

    # Slot a must be active for repartitioning
    active_slot = fastboot_getvar("current-slot")
    if active_slot not in ["_a", "a"]:
        fastboot(["set_active", "a"])

    # Force updating to the new bootloader that is known to support
    # repartitioning and backup/restore of persist
    if args.force:
        fastboot(["flash", "firmware", img_path("firmware.img")])
        reboot_bootloader()

    if not args.nobackup:
        fastboot(["oem", "read-persist"], not args.force)

    partition_meta_image = img_path("ab-repartition.img")
    use_meta_image = True if os.path.exists(partition_meta_image) else False

    try:
        # Use the meta image for partition tables if exists
        # else flash each individual partition table
        if use_meta_image:
            fastboot(["flash", "bootloader", partition_meta_image])
        else:
            for gpt_file in sorted(glob.glob(img_path("gpt_both*.bin"))):
                lun = "partition:%d" % int(os.path.basename(gpt_file)[8])
                fastboot(["flash", lun, gpt_file])
    except Exception as e:
        print("Error: re-partitioning failed!!!")
        print("Try to write persist back.")
        raise e
    finally:
        if not args.nobackup:
            fastboot(["oem", "write-persist"], not args.force)
        print("write persist success.")

    # Erase the misc partition if exists
    if fastboot_getvar("partition-type:misc"):
        fastboot(["erase", "misc"])
    # Flash the new firmware unless we are using the meta image since
    # the new firmware is already included in the partition meta image
    if not use_meta_image:
        fastboot(["flash", "firmware", img_path("firmware.img")])
    reboot_bootloader()


def flash_if_exists(partition, filename):
    """Flash the specified image to the specified partition if the file exists"""
    imagepath = img_path(filename)
    if os.path.exists(imagepath):
        fastboot(["flash", partition, imagepath])
        return True
    return False


def get_fastboot_major_version():
    """Extract the version number of fastboot"""
    try:
        response = fastboot_output(["--version"], no_serial=True)
    except subprocess.CalledProcessError as e:
        print("Unable to get fastboot version")
        raise e
        sys.exit(1)

    major = None
    prefix = b"fastboot version "
    for line in response.splitlines():
        if prefix in line:
            suffix = line.split(prefix, 1)[1]
            suffix_split = suffix.split(b".", 1)
            major = suffix_split[0].strip().decode("utf-8")
            break
    try:
        major_version = int(major)
    except ValueError:
        major_version = 0

    return major_version


def check_fastboot_version():
    """Check and make sure fastboot version is current"""
    if "ANDROID_BUILD_TOP" in os.environ:
        # Don't bother AOSP developers, they know what they are doing ;-)
        return

    major_version = get_fastboot_major_version()
    if major_version < 29:
        print("\n**************************** WARNING ****************************")
        print(
            "Your fastboot version (%d) is unknown or too old, please download"
            % major_version
        )
        print("and install the latest version from the following URL.")
        print("https://developer.android.com/studio/releases/platform-tools\n")


def check_adb_version():
    # Ensure that adb is the right version to help ensure that fastboot is
    # compatible. adb's version is used because fastboot does not use semantic
    # versioning. On most platforms, both will come from the android
    # platform-tools package. For OS engineers, this will come from
    # build output.
    #
    # adb >= 1.0.36 implies fastboot has all the required support
    try:
        adb_version = [
            int(x)
            for x in adb_output(["version"]).splitlines()[0].split()[-1].split(b".")
        ]
        if adb_version[0] < 1 or adb_version[2] < 36:
            raise OSError(
                "adb version 1.0.36 or better required. "
                + "You can get it by installing platform-tools 25.0.3 or better "
                + "from the android SDK manager"
            )
    except Exception as e:
        if args.force:
            pass
        else:
            raise e


def check_product_signing_keys(product, package_metadata, is_secure_boot):
    # List of products that already have production signed firmware bundled
    safe_products = ["monterey", "hollywood", "starlet", "seacliff"]
    if product in safe_products:
        return

    release_build = "release-keys" in package_metadata["fingerprint"]
    if is_secure_boot and not release_build:
        raise OSError(
            "Only user build is supported for flashing provisioned unit, https://fburl.com/o6mgow4z, T65635611."
        )


def check_avb_rollback_index(package_metadata):
    package_arb_indexes = {}
    for key, value in package_metadata.items():
        if not key.startswith("arb_"):
            continue
        location, index = value.split(":")
        package_arb_indexes[int(location)] = int(index)

    fastboot_deviceinfo = fastboot_output(["oem", "device-info"]).decode("ascii")
    device_rollback_infos = re.findall(
        r"[(](\d+)[)] min anti-rollback version: (\d+)", fastboot_deviceinfo
    )
    for device_location, device_index in device_rollback_infos:
        device_location = int(device_location)
        device_index = int(device_index)
        if device_location not in package_arb_indexes:
            # This probably should be an error instead of a warning,
            # but the risk here is blocking flashing of a perfectly
            # fine image which just doesn't have metadata set up
            # properly.
            print(
                "WARNING: Package does not have rollback index provided in location %s, when device expects %s"
                % (device_location, device_index)
            )
            continue
        package_index = package_arb_indexes[device_location]
        if device_index > package_index:
            product = fastboot_device_product()
            # Some builds on monterey v28 has arb min value set to 1596585600.
            # Create this exception for these builds and skip avb check,
            # so that they can flash to lower os version.
            if device_index == 1596585600 and product == "monterey":
                if args.wipe:
                    return
                else:
                    msg = (
                        "Your current build has arb min value set to 1596585600. "
                        + "To make sure device will boot after flashing, "
                        + "please run flash_all.py with -w."
                    )
                    raise RuntimeError(msg)
            msg = (
                "This package is rejected by device anti-rollback. "
                + "In slot %s, package has index %s, which is smaller than %s expected by device. "
                + "Use 'fastboot oem reset-devinfo' to reset anti-rollback indexes."
            ) % (device_location, package_index, device_index)
            if args.force:
                print(msg)
                print("Force used, proceeding anyway.")
            else:
                raise RuntimeError(msg)


def check_dynamic_dependencies(package_metadata):
    dynamic_partitions = package_metadata.get("dynamic-partitions")
    if not dynamic_partitions:
        return
    deps = ["super_empty"] + dynamic_partitions.split()
    for f in deps:
        dep = f + ".img"
        if not os.path.exists(img_path(dep)):
            raise RuntimeError(
                "This package doesn't support flashing to slot B, missing " + dep
            )


def flash_slot_b_dynamic_partitions(package_metadata):
    # Reboot into user space fastboot
    fastboot(["reboot", "fastboot"])

    # Wait for user space fastboot
    for _ in range(5):
        # Reset all the cached variables
        fastboot_vars.clear()
        if fastboot_getvar("is-userspace") == "yes":
            break
        sleep(1)

    # Sanity check if we are in user space fastboot and B slot
    if fastboot_getvar("is-userspace") != "yes":
        raise ValueError("Failed to enter user space fastboot")

    if fastboot_getvar("current-slot") not in ["_b", "b"]:
        raise ValueError("Current slot is not B")

    # Get the list of dynamic partitions for this package
    dynamic_partitions = package_metadata.get("dynamic-partitions")
    if not dynamic_partitions:
        raise ValueError("couldn't find dynamic partition")

    # Flash the empty super partition first then flash the rest of dynamic partitions
    fastboot(["flash", "super", img_path("super_empty.img")])
    deps = dynamic_partitions.split()
    for f in deps:
        dep = f + ".img"
        fastboot(["flash", f, img_path(dep)])


def parse_args():
    parser = argparse.ArgumentParser("Flashes Oculus VROS")
    parser.add_argument(
        "-p", "--repartition", action="store_true", help="Force a repartition"
    )
    parser.add_argument(
        "-k", "--skip_repartition", action="store_true", help="Skip repartition"
    )
    parser.add_argument("-u", "--userdata", action="store_true", help="Flash userdata")
    parser.add_argument("-w", "--wipe", action="store_true", help="Wipe userdata")
    parser.add_argument(
        "-n", "--nowipe", action="store_true", help="Do not wipe userdata"
    )
    parser.add_argument("-s", "--serial", help="device serial number")
    parser.add_argument(
        "-b", "--active_slot_b", action="store_true", help="set slot b as active slot"
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Say yes ('y') to all expected 'are you sure?' type prompts. Useful for automation. "
        "Use with care to avoid loss of user data.",
    )
    parser.add_argument(
        "--clowntown",
        action="store_true",
        dest="force",
        help="Force your way past some serious errors. **Caution** - this could lead "
        "to your device not booting up or going up in smoke. Use with "
        "extreme care.",
    )
    parser.add_argument(
        "-d", "--debugpolicy", action="store_true", help="Flash debug policy"
    )
    parser.add_argument(
        "-x", "--nobackup", action="store_true", help="Skip backup/restore persist"
    )
    parser.add_argument(
        "-r",
        "--rootable",
        action="store_true",
        help="flash boot-debug.img to enable insecure and rootable adb for user builds",
    )
    parser.add_argument(
        "--no-staging",
        action="store_true",
        help="Don't use staging area from AOSP build environment",
    )
    parser.add_argument(
        "--no-reboot", action="store_true", help="Flash only. Do not reboot."
    )
    parser.add_argument(
        "--tools-path",
        help="Android platform tools path. Uses tools in PATH if omitted",
    )
    parser.add_argument(
        "--trace", action="store_true", help="Print debugging information"
    )

    temp_args = parser.parse_args()
    if not temp_args.no_staging:
        init_staging_location()

    if temp_args.tools_path:
        print(" [ANDROID_TOOLSPATH]  : {}".format(temp_args.tools_path))
    return temp_args


BatteryInfo = namedtuple("BatteryInfo", "min_voltage max_voltage scale")


def check_battery_level(product):
    # Check battery voltage requirement
    product_battery_voltages = {
        "eureka865": BatteryInfo(3650, 9999, 1),
        "hollywood": BatteryInfo(3650, 9999, 1),
        "monterey": BatteryInfo(3500, 4315, 1),
        "seabright": BatteryInfo(3650, 9999, 1),
        "seacliff": BatteryInfo(3650, 9999, 1),
        "starlet": BatteryInfo(3650, 9999, 1),
        "unknown": BatteryInfo(0, 9999, 1),
    }

    info = product_battery_voltages.get(product, product_battery_voltages["unknown"])

    batt_voltage = int(fastboot_getvar("battery-voltage"))
    batt_voltage = batt_voltage / info.scale

    if batt_voltage < info.min_voltage:
        raise BatteryLevelException(
            "Battery voltage {}mV insufficient ".format(batt_voltage)
            + "to complete OS download. Please charge device to at least "
            + "{}mV.".format(info.min_voltage)
        )

    if batt_voltage > info.max_voltage:
        raise BatteryLevelException(
            "Battery voltage {}mV exceeds ".format(batt_voltage)
            + "the maximum voltage {}mV. ".format(info.max_voltage)
            + "Please drain to below it!"
        )


def wipe_all():
    fastboot_clear_production_mode()
    fastboot_clear_arb_indexes()
    # Always erasing userdata for f2fs type because some version of the
    # Android platform-tools could leave a device stuck at the boot logo
    if fastboot_getvar("partition-type:userdata") == "f2fs":
        fastboot(["erase", "userdata"])
    elif not fastboot(["format", "userdata"], check_error=False):
        print("WARNING: format userdata failed, trying to erase")
        # Trying to recover in case of corrupted bootloader
        fastboot(["erase", "userdata"])
    # Erase vision partition if exists, ideally we should format instead of
    # erase but older bootloader doesn't have the correct file system type
    if fastboot_getvar("partition-type:vision"):
        fastboot(["erase", "vision"])
    # Erase metadata partition if it exists, this partition stores the
    # userdata encryption keys
    if fastboot_getvar("partition-type:metadata"):
        fastboot(["erase", "metadata"])


def main():
    # Parse the package metadata if it is available
    package_metadata = parse_package_metadata()

    if args.active_slot_b:
        check_dynamic_dependencies(package_metadata)

    # make sure fastboot device exists
    if not fastboot_device_present():
        print("no fastboot device found, trying adb reboot-bootloader")
        if not adb(["reboot-bootloader"]):
            raise OSError("No device found.")

        # block until fastboot device comes up
        wait_for_fastboot_device()

    # Ensure our bootloader is currently running, since the rest of this script
    # depends on some features.
    force_repartition = False
    if not fastboot_device_oculus_bootloader():
        if not args.force:
            raise OSError("device must be running the oculus bootloader or use -f")
        else:
            # Force re-partition to make sure we have the correct partition layout
            force_repartition = True

    device_info = fastboot_device_info()
    oem_unlocked = fastboot_device_unlocked(device_info)
    critical_unlocked = fastboot_device_critical_unlocked(device_info)
    secure_boot = fastboot_getvar("secure") == "yes"

    # Prevent attempting to flash a locked device, secure or insecure,
    # flashing to a locked device via fastboot is not possible.
    if not oem_unlocked:
        print("Can't flash a locked device")
        print("To unlock, follow instructions from https://fburl.com/oemunlock")
        sys.exit(1)

    # Check if debug ramdisk is present in this package
    if args.rootable and not os.path.exists(img_path("boot-debug.img")):
        print("The option --rootable is not supported by this package")
        sys.exit(1)

    # From this point on, there is no need to check for oem_unlocked anymore

    product = fastboot_device_product()
    package_board = package_metadata["board"]
    if package_board != product and not args.force:
        raise OSError(
            "You are trying to install the wrong OS image ("
            + package_board
            + ") for this device ("
            + product
            + ")"
        )

    if product == "seacliff" and not args.force:
        model_rev = fastboot_device_model_rev()
        flavor = package_metadata["flavor"]
        qcseacliff_revision = [
            "Seacliff (Dev0)",
            "Seacliff (P0)",
            "Seacliff (P0 DoubleDouble)",
            "Seacliff (P1.5 DoubleDouble)",
        ]
        p2_seacliff_revision = [
            "Seacliff (P1)",
            "Seacliff (Dev2)",
            "Seacliff (Dev3)",
            "Seacliff (P2)",
            "Seacliff (Dev2.5)",
            "Seacliff (P2 DoubleDouble)",
        ]
        if model_rev == "unknown":
            print(
                "Unknown Seacliff Model Revision detected because the build is too old, the flashing won't proceed.\n"
                + "Please check https://fburl.com/what-seacliff-build-to-use for which build to use\n"
                + "Or you could use '--clowntown' option to do a force flash if the build is correct\n"
                + "Otherwise please do qfil flash following: https://fburl.com/production-qfil-packages\n"
            )
            sys.exit(1)

        elif model_rev in p2_seacliff_revision:
            if flavor[0:11] != "p2_seacliff":
                raise OSError(
                    "You are trying to install the wrong OS image ("
                    + flavor
                    + ") for this device ("
                    + model_rev
                    + ")\n"
                    + "if you are using the maui tool, please check https://fburl.com/update-seacliff-serial-number\n"
                )
        elif model_rev in qcseacliff_revision:
            if flavor[0:11] != "qc_seacliff":
                raise OSError(
                    "You are trying to install the wrong OS image ("
                    + flavor
                    + ") for this device ("
                    + model_rev
                    + ")"
                )
        else:
            if flavor[0:8] != "seacliff":
                raise OSError(
                    "You are trying to install the wrong OS image ("
                    + flavor
                    + ") for this device ("
                    + model_rev
                    + ")\n"
                    + "if you are using the maui tool, please check https://fburl.com/update-seacliff-serial-number\n"
                )

    check_product_signing_keys(product, package_metadata, secure_boot)

    # Save the build variant and grab the target build flavor
    target_build_flavor = package_metadata["flavor"]
    new_build_variant_user = target_build_flavor.split("-")[-1] == "user"
    old_build_variant = fastboot_get_kernel_flavor()
    if old_build_variant != "unknown":
        old_build_variant_user = old_build_variant == "user"
    else:
        old_build_variant_user = fastboot_getvar("build-variant-user", None)
    wipe_required = (old_build_variant_user is not None) and (
        int(old_build_variant_user) != int(new_build_variant_user)
    )
    if wipe_required and not (args.wipe or args.nowipe or args.userdata):
        print(
            "A build flavor change has been detected.\n"
            + "All your data will be lost.\n"
            + "Do you wish to continue? (y/N): "
        )
        if args.yes:
            print("y")
            confirm = "y"
        else:
            confirm = input().lower()

        if confirm != "y":
            sys.exit(1)

    try:
        check_battery_level(product)
    except BatteryLevelException as err:
        if args.force:
            print("WARNING: ** ignoring battery level failure **\n{}".format(err))
        else:
            raise err

    repartition_needed = (
        check_repartition_required(package_metadata) or force_repartition
    ) and not args.skip_repartition
    if repartition_needed:
        print("WARNING: ***** repartition required! *****")

    # Repartition if needed/requested
    do_repartition = args.repartition or repartition_needed
    if do_repartition:
        if critical_unlocked or not secure_boot:
            repartition()
        else:
            raise RuntimeError("Can't repartition without critical unlock")

    # format userdata (repartition doesn't always do this)
    if wipe_required or args.wipe or do_repartition or args.userdata:
        wipe_all()

    # Check anti-rollback indexes now -- we don't want to do that
    # before wiping, as it will raise unnecessary concerns which
    # wiping would solve.
    check_avb_rollback_index(package_metadata)

    # Updating both slots is only available on Go and Quest
    # We don't need to do this anymore for new devices
    product = fastboot_device_product()
    if product == "monterey":
        if fastboot_device_oculus_bootloader_ver() == 1:
            # This command is not available on older bootloader, e.g. DVT2,
            # we can just issue the command and skip checking error
            if not fastboot(["oem", "update-all-slots", "1"], False):
                print("Please ignore the above failure as it is benign and expected")
        else:
            print("oculus-10.0 bootloader detected")

    if args.active_slot_b:
        fastboot(["set_active", "b"])
    else:
        fastboot(["set_active", "a"])

    if args.debugpolicy:
        if not critical_unlocked:
            raise RuntimeError("Flashing debug policy needs critical unlocked")
        fastboot(["flash", "apdp", img_path("apdp.mbn")])
        if fastboot_getvar("partition-type:msadp"):
            fastboot(["flash", "msadp", img_path("msadp.mbn")])

    if critical_unlocked:
        # Skip flashing firmware if the device has a higher required minimum
        # Firmware Anti Rollback version than the version of firmware being currently flashed to prevent
        # bricking the device.Lookup the device-info(fastboot oem device-info) for device's firmware ARB requirements.
        safe_to_flash_firmware = is_firmware_of_sufficient_arb_version()
        if not safe_to_flash_firmware:
            device_info = fastboot_device_info()
            metadata = parse_package_metadata()
            print(
                """WARNING: SKIPPING FLASHING FIRMWARE IMAGES.
                  If YOU FLASH THE FIRMWARE IN THIS PACKAGE (VERSION {})
                  ON THIS DEVICE with build {},IT COULD BRICK THIS DEVICE.
                  BECAUSE FLASHING FIRMWARE IS BEING SKIPPED,
                  PAIRING OS VERSION {} AND FIRMWARE OF {} MAY HAVE INCOMPATABILITIES.""".format(
                    metadata["fingerprint"],
                    device_info["Build number"],
                    metadata["fingerprint"],
                    device_info["Build number"],
                )
            )
            flash_if_exists("frp", "frp.img")
        else:
            # Flash the firmware.img file if exists else flash the old style bootloader/radio pair
            if not flash_if_exists("firmware", "firmware.img"):
                fastboot(["flash", "radio", img_path("radio.img")])
                fastboot(["flash", "bootloader", img_path("bootloader.img")])

            # Reboot into new bootloader before erasing devinfo to ensure devinfo is re-created
            # with the structure of the newly flashed bootloader
            fastboot(["reboot-bootloader"])

            # Wait for 5s in case the platform USB stack cannot handle issuing the command
            # following the reboot in such a narrow time interval
            sleep(5)

            if fastboot_getvar("partition-type:devinfo"):
                fastboot(["erase", "devinfo"])
            if fastboot_getvar("partition-type:misc"):
                fastboot(["erase", "misc"])
            flash_if_exists("frp", "frp.img")
    else:
        print("WARNING: Skip flashing firmware images to a critically locked device")

    boot_img_path = img_path("boot-debug.img" if args.rootable else "boot.img")
    fastboot(["flash", "boot", img_path(boot_img_path)])
    flash_if_exists("dtbo", "dtbo.img")
    flash_if_exists("vbmeta", "vbmeta.img")

    # Flash super.img (system and vendor combined) for dynamic partition
    if fastboot_getvar("partition-type:super"):
        # Skip super.img for slot B since the prebuilt super.img is only for A slot
        if not args.active_slot_b:
            fastboot(["flash", "super", img_path("super.img")])
        flash_if_exists("recovery", "recovery.img")
        flash_if_exists("vbmeta_system", "vbmeta_system.img")
        flash_if_exists("vbmeta_vendor", "vbmeta_vendor.img")
    else:
        fastboot(["flash", "system", img_path("system.img")])
        flash_if_exists("vendor", "vendor.img")

    if args.userdata:
        fastboot(["flash", "userdata", img_path("userdata.img")])

    # Flash dynamic partition to B slot in the last step since it requires reboot
    if args.active_slot_b and fastboot_getvar("partition-type:super"):
        flash_slot_b_dynamic_partitions(package_metadata)

    if not args.no_reboot:
        fastboot(["reboot"])

    # Reminder to erase userdata if switching flavors
    if not (args.wipe or args.userdata or do_repartition or wipe_required):
        color_start = color_end = ""
        if not is_windows():
            color_start = "\033[33m"  # Yellow
            color_end = "\033[0m"
        print(
            (
                """{}REMINDER: YOU MUST FLASH WITH "-w" TO ERASE USERDATA WHEN:{}\n"""
                """  (i) Switching between build flavors (ex. user, userdebug, eng)\n"""
                """ (ii) Flashing a device running an unknown build (ex. from the factory, or second-hand from another user)\n"""
            ).format(color_start, color_end)
        )

    print("Flashing complete")


if __name__ == "__main__":
    args = parse_args()
    init_android_tools(args.tools_path)
    main()
