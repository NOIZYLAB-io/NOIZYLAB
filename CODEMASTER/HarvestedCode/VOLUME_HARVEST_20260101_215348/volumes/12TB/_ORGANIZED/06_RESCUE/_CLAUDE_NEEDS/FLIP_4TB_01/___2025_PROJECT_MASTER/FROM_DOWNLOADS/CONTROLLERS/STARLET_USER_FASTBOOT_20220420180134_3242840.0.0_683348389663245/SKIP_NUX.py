#!/usr/bin/env python3

import argparse
import getpass
import io
import re
import subprocess
from timeit import default_timer as timer


def run(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return str(output, "utf-8")


def adb(command, *args, **kwargs):
    return run(" ".join(["adb", command.format(*args, **kwargs)]))


# Tracks progress using logs. When there are no more Skip NUX logs, we're done.
def trackProgress(showLogs):
    print("Please wait...")
    adb("logcat -c")  # clear old logs
    process = subprocess.Popen(["adb", "logcat"], stdout=subprocess.PIPE)
    last_log_time = timer()
    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        log = re.findall(r".*\[Skip NUX\].*", line)
        if log:
            if showLogs:
                print(log[0])
            last_log_time = timer()
        elif (timer() - last_log_time) > 65:  # Auth timeout is 60 seconds
            break
    print("Done")


def skipNux(args):
    command = "shell am startservice -a nux.ota.SKIP_NUX"
    if args.wifi_ssid:
        command += f" -e WIFI_SSID '{args.wifi_ssid}'"
        wifi_pwd = getpass.getpass("Wi-Fi Password (Optional): ")
        if args.wifi_user:
            command += f" -e WIFI_USER '{args.wifi_user}'"
        if wifi_pwd:
            command += f" -e WIFI_PWD '{wifi_pwd}'"
        if args.wifi_auth:
            command += f" -e WIFI_AUTH '{args.wifi_auth}'"
        if args.wifi_hidden:
            command += f" --ez WIFI_HIDDEN '{args.wifi_hidden}'"
    if args.email:
        command += f" -e EMAIL '{args.email}'"
        pwd = getpass.getpass("User Password: ")
        command += f" -e PWD '{pwd}'"
    if args.two_fac_code:
        command += f" -e TWO_FAC_CODE '{args.two_fac_code}'"
    if args.fb:
        command += f" --ez FB '{args.fb}'"
    if args.max_attempts:
        command += f" --ei MAX_ATTEMPTS '{args.max_attempts}'"
    if args.pre_ota_only:
        command += f" --ez PRE_OTA_ONLY '{args.pre_ota_only}'"
    command += " -n com.oculus.nux.ota/.NuxOtaIntentService"

    adb("root")
    adb(command)
    trackProgress(args.show_logs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Skips NUX, including OTA and high-pri app download:"
    )
    parser.add_argument(
        "--wifi-ssid",
        type=str,
        metavar="<string>",
        help="Wi-Fi SSID. Optional, but recommended for most cases, since many services rely on Internet connection.",
    )
    parser.add_argument(
        "--wifi-user",
        type=str,
        metavar="<string>",
        help="Wi-Fi username. Optional, depending on your Wi-Fi configuration.",
    )
    parser.add_argument(
        "--wifi-auth",
        type=str,
        metavar="<string>",
        help="Wi-Fi authentication level. Defaults to WPA.",
    )
    parser.add_argument(
        "--wifi-hidden",
        action="store_true",
        help="Wi-Fi visibility. Optional, depending your Wi-Fi configuration.",
    )
    parser.add_argument(
        "--email",
        type=str,
        metavar="<string>",
        help="User email used for signing in. Optional, but recommended for most cases -- many services rely on user auth.",
    )
    parser.add_argument(
        "--fb",
        action="store_true",
        help="Inidicates that this is an FB account. Optional, but will speed up the process.",
    )
    parser.add_argument(
        "--two-fac-code",
        type=str,
        metavar="<string>",
        help="Six-digit two-fac code, which must be provided for FB accounts with two-fac authentication enabled. Code may be obtained from sources such as FB mobile app, Duo Mobile app, etc.",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        metavar="<integer>",
        help="Number of times a step is retried if failed. Optional. Default is 3.",
    )
    parser.add_argument(
        "--pre-ota-only",
        action="store_true",
        help="Skips only pre-OTA portion of the NUX. Optional.",
    )
    parser.add_argument(
        "--show-logs",
        action="store_true",
        help="Show logs after executing the command.",
    )
    args = parser.parse_args()

    skipNux(args)
