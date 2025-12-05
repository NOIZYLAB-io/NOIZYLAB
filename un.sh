mount -r -w -o remount /system;
/data/local/tmp/busybox mount -orw,remount /system;
rm /system/xbin/cdaemonsu;
rm /system/xbin/daemonsu;
rm /system/etc/install-recovery.sh;
rm /system/bin/su8;
rm /system/xbin/su8;

mount -r -w -o remount /system;
/data/local/tmp/busybox mount -orw,remount /system;
rm /system/xbin/daemonsu;
rm /system/etc/install-recovery.sh;
rm /system/app/Superuser.apk;
rm /system/app/SuperSU.apk;
rm /system/bin/su;
rm /system/xbin/su;
pm uninstall eu.chainfire.supersu;