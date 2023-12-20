============================================
SAILFISH OS
Changelog from 4.3.0.15 to 4.4.0.58
2022-03-15
============================================

# PACKAGES REMOVED

### kcalcore-qt5
- kcalcore-qt5-devel - 4.10.2+9git28-1.4.1.jolla, kcalcore-qt5 - 4.10.2+9git28-1.4.1.jolla
### tohd
- tohd - 1.2.6-1.2.1.jolla, tohd-tools - 1.2.6-1.2.1.jolla

# PACKAGES MODIFIED

### SDL2
- Updated : 2.0.16+git1-1.7.1.jolla -- 2.0.18+git1-1.8.1.jolla
- [sdl] Update to version 2.0.18. 
### alien-system-tests
- Updated : 1.0.9-1.5.1.jolla -- 1.0.11-1.4.1.jolla
- [aas] Add write permission for screen capture data. 
- [aas] Fix permissions for screen capture data. 
### alienaudioservice
- Updated : 0.16.4-1.6.1.jolla -- 0.18.0-1.4.2.jolla
- [hook] Add hook for service manager connection state. 
- [service] Invoke hook when service is (dis)connected to service manager. 
- [audio] Add state for stream stopped by request-stop. 
### alienaudioservice-plugin-sailfish
- Updated : 0.5.0-1.4.1.jolla -- 0.6.0-1.3.1.jolla
- [sailfish] Report system_server application id to policy. 
- [sailfish] Update changed hook name. 
### aliendalvik
- Updated : 1.1.0-1.4.1.jolla -- 1.2.0-1.3.1.jolla
- [aliendalvik] Require binder-utils. 
### aliendalvik-configs
- Updated : 10.0.57-1.5.1.jolla -- 10.0.59-1.4.1.jolla
- [alien] Add some missing properties from android 11. 
- [alien] use swiftshader if vgem is enabled. 
### aliendalvik-system
- Updated : 10.0.0.58.2.1-1.7.2.jolla -- 10.0.0.62.1.1-1.8.1.jolla
- [alien] Update patches for android-security-10.0.0_r62. 
- [alien] Set interface name for wifi LinkProperties. 
- [alien] Update patches for android-security-10.0.0_r60. 
- [alien] Further file and URL association fixes. 
- [alien] Correct level for system call filter. 
- [alien] Disable wifi and bluetooth battery stats. 
- [alien] Don't complain about missing memtrack. 
- [alien] Don't print Bad file descriptor errors. 
- [alien] Remove error logging for non-error message. 
- [init] Disable access to bpf stats. 
- [alien] cherry pick missing android 11 dependency. 
- [alien] add listener iface to app closed events from wl_manager. 
- [alien] add some missing manifest entries. 
- [alien] Add some missing symbols and cherry-picks from android 11. 
- [alien] allow starting c2 vendor service if needed. 
- [alien] allow starting graphics allocator vendor service if needed. 
- [alien] reintroduce graphics patches, but prefer system graphics libraries over vendor implementations. 
- [alien] Enable i915 minigbm driver by default, 
- [alien] Disable SimSelectNotification. 
- [alien] Add some missing libraries. 
- [alien] use display sizes and dpi information from wayland. 
- [alien] File and sharing optimizations. 
- [alien] Make android.hardware.wifi feature common. 
- [alien] Implement propagating cover URI & Bitmap to host from android. 
- [alien] make sure Wi-Fi state is in sync with host/apkd. 
### alsa-utils
- Updated : 1.2.3+git2-1.4.1.jolla -- 1.2.3+git3-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### amber-web-authorization-l10n
- Updated : 1.5.1-1.4.1.jolla -- 1.7.2-1.6.1.jolla
- Binaries added : amber-web-authorization-l10n-lv - 1.7.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 1 of 1 strings translated (0 need review).
### ambienced
- Updated : 0.29.26-1.5.1.jolla -- 0.29.29-1.6.2.jolla
- [ambienced] Order ambiences by favorite changes and editing timestamp. 
- [ambienced] Remove TohMonitor. 
- [packaging] BuildRequire systemd via pkgconfig. 
### android-tools-hadk
- Updated : 5.1.1+git7-1.3.1.jolla -- 5.1.1+git8-1.4.1.jolla
- [ubu-chroot] Add missing -h option to getopts
- [ubu-chroot] Disable pam account management for sudo. 
- [ubu-chroot] Remove non-standard and deprecated use of fgrep
- [ubu-chroot] Use grep -q instead of redirecting to /dev/null
### apkd-l10n
- Updated : 1.143.1-1.4.1.jolla -- 1.145.2-1.6.1.jolla
- Binaries added : apkd-l10n-lv - 1.145.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
### apkd8
- Updated : 10.0.0.39.1-1.8.1.jolla -- 10.0.0.47.1-1.8.1.jolla
- [alien] Special handling for text share maps. 
- [apkd] Use new sharing plugin format. 
- [apkd] Setup binder device nodes for devices with binderfs. 
- [packaging] Include binderfs-setup.sh script.
- [alien] Check if launchers have shareTypes when comparing. 
- [apkd] listen/propagate appclosed events via binder/dbus. 
- [apkd] reset SupplicantService staIface callback after disabling wifi in Android. 
- [alien] Add getAndroidVersionData DBus call. 
- [alien] Include apk version in launcher yaml. 
- [alien] Report service status and improve service control. 
- [alien] Secret Android Settings app launch. 
- [apkd] Implement setting coverArt in MPRIS metadata. 
- [alien] set env file and user/group on bridge services. 
### apkd8-l10n
- Updated : 1.54.1-1.6.1.jolla -- 1.59-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 23 of 60 strings translated (0 need review).
- [tpl] translation templates update for 10.0.0.47
- [l10n] Commit from Jolla localisation: 60 of 60 strings translated (0 need review).
- [tpl] translation templates update for 10.0.0.42
- [l10n] Commit from Jolla localisation: 23 of 50 strings translated (0 need review).
### audiosystem-passthrough
- Updated : 1.1.2-1.2.1.jolla -- 1.3.0-1.6.1.jolla
- [af] Wait for binder device node if not present. 
- [helper] Add argument for binder device node location.
- [hw2_0] Omit 'Conflicts=bluebinder.service' declaration. 
- [hw2_0] Move dummy-hw2_0 to system session. 
- [qti] Add support for alternative interface name.
- [packaging] BuildRequire systemd via pkgconfig. 
### bluetooth-rfkill-event
- Updated : 1.0.9-1.2.1.jolla -- 1.1.0-1.3.1.jolla
- [bluetooth-rfkill-event] Workaround for busybox killall. 
- [packaging] Add killall helper script and bump version.
### bluetooth-rfkill-event-hciattach
- Updated : 1.0.9-1.2.1.jolla -- 1.1.0-1.3.1.jolla
- [bluetooth-rfkill-event] Workaround for busybox killall. 
- [packaging] Add killall helper script and bump version.
### bluez5
- Updated : 5.58+git3-1.6.3.jolla -- 5.58+git4-1.7.12.jolla
- [sailfish] Fix build by creating directory for ell/useful.h 
### btrfs-balancer
- Updated : 1.2.7-1.5.1.jolla -- 1.2.8-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### busybox
- Updated : 1.31.0+git18-1.4.3.jolla -- 1.33.1+git3-1.7.12.jolla
- [busybox] Obsolete old version of busybox-symlinks-cpio. 
- [packaging] BuildRequire systemd via pkgconfig. 
- [busybox] Update to 1.33.1. 
### buteo-mtp-qt5
- Updated : 0.9.1-1.7.1.jolla -- 0.9.3-1.8.1.jolla
- Binaries removed : buteo-mtp-qt5-sync-plugin
- [buteo-mtp] Execute astyle on the code. 
- [buteo-mtp] Drop "mtp as buteo sync fw plugin" feature. 
### buteo-sync-plugin-caldav
- Updated : 0.2.5-1.9.1.jolla -- 0.2.8-1.10.1.jolla
- [buteo-sync-plugin-caldav] Call Incidence::update() before updated().
- [buteo-sync-plugin-caldav] Correct NotebookSyncAgent tests.
- [buteo-sync-plugin-caldav] Don't modify the lastModified stamp when creating RDates for parent.
- [buteo-sync-plugin-caldav] Don't report failure on item issues.
- [buteo-sync-plugin-caldav] Don't report failure on item issues. 
- [buteo-sync-plugin-caldav] Fix build issue. 
- [buteo-sync-plugin-caldav] Report error when etag fetching fails.
- [buteo-sync-plugin-caldav] Store error data per item logs.
- [buteo-sync-plugin-caldav] Store error data per item logs. 
### buteo-sync-plugins-sailfisheas
- Updated : 0.1.1-1.4.1.jolla -- 0.1.2-1.5.1.jolla
- [buteo-sync-plugin-sailfisheas] Install to /usr/lib64 for aarch64 builds. 
### buteo-sync-plugins-social-l10n
- Updated : 1.7.1-1.6.1.jolla -- 1.7.3-1.7.1.jolla
- Binaries added : buteo-sync-plugins-social-l10n-lv - 1.7.3-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 11 of 11 strings translated (0 need review).
### buteo-syncfw-qt5
- Updated : 0.10.10-1.17.6.jolla -- 0.10.13-1.17.17.jolla
- Binaries added : buteo-syncfw-qt5-qml-plugin - 0.10.13-1.17.17.jolla
- [buteo-syncfw] Add a list model for SyncResults from various sources. 
- [buteo-syncfw] Make SyncResults and lower Q_GADGET and creates a QML plugin.
- [packaging] BuildRequire systemd via pkgconfig. 
- [buteo-syncfw] Add a new minor code for completed syncs with some ite?
- [buteo-syncfw] Add a new minor code for completed syncs with some items in error.
- [buteo-syncfw] Adjust sync result codes. 
### ca-certificates
- Updated : 2020.2.41-1.4.1.jolla -- 2021.2.50-1.6.1.jolla
- Update to latest upstream ca-certificates. 
### calligra
- Updated : 3.2.1+git2-1.9.1.jolla -- 3.2.1+git3-1.11.1.jolla
- [calligra] Correct Fontconfig variable name.
- [calligra] Fix build with newer extra-cmake-modules. 
### commhistory-daemon
- Updated : 0.8.40-1.9.1.jolla -- 0.8.43-1.11.1.jolla
- [commhistory] Use feedback events instead of notification categories. 
- [commhistory-daemon] Reset voicemail notification on number change.
- [commhistory-daemon] Use direct number to dial on voicemail notification.
- [commhistoryd] Update notification on voicemail number change signal. 
- [packaging] BuildRequire systemd via pkgconfig. 
### commhistory-daemon-l10n
- Updated : 1.89.1-1.5.1.jolla -- 1.90.2-1.6.1.jolla
- Binaries added : commhistory-daemon-l10n-lv - 1.90.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 43 of 43 strings translated (0 need review).
### connectionagent-qt5
- Updated : 0.11.41-1.5.1.jolla -- 0.11.42-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### connman
- Updated : 1.32+git173.1-1.14.1.jolla -- 1.32+git180.2-1.16.1.jolla
- [agent] Add support to check for active pending requests. 
- [service] Check if hidden service has a pending request. 
- [connman] Fix CVE-2022-23096 CVE-2022-23097 CVE-2022-23098. 
- [ofono] Support 3GPP TS 24.301 dual network mode. 
- [ipconfig] Do not enable/disable ipv6 for all ifs. 
- [service] Support hot-plug of techs by updating ipconfig index. 
- [openvpn] Handle script context in notify and check signature. 
- [openvpn] Improve config data processing. 
- [openvpn-script] Pass script context to notify, set as required. 
- [vpn-provider] Add ECONNRESET to connect_cb(). 
- [vpn-provider] Support checking if provider setting key exists. 
- [vpn] Use VPN_STATE_UNKNOWN as error for invalid notify msg. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
- [storage] Do not process ENOENT in path validation when loading. 
- [storage] Move user change post() call after user dir creation. 
- [technology] Create settings file in user change post command. 
- [storage] Prevent symlinks and references in paths. 
- [unit] Add storage path validation error tests using symlinks. 
### connman-qt5
- Updated : 1.2.38-1.4.1.jolla -- 1.2.39-1.6.1.jolla
- [libconnman-qt] Add support for ethernet tech and services. 
### contactsd
- Updated : 1.4.9-1.12.1.jolla -- 1.4.10-1.14.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
- [packaging] Require buteo-syncw with pkgconfig
### contactsd-l10n
- Updated : 1.54.1-1.5.1.jolla -- 1.54.3-1.6.1.jolla
- Binaries added : contactsd-l10n-lv - 1.54.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 2 of 2 strings translated (0 need review).
### crash-reporter
- Updated : 1.15.11-1.5.7.jolla -- 1.15.13-1.7.9.jolla
- [crash-reporter] Add dependencies for endurance-collect script. 
- [packaging] BuildRequire systemd via pkgconfig. 
### cross-glibc-devel-inject
- Updated : 2.30+git8-1.5.1.jolla -- 2.30+git11-1.6.1.jolla
No new changelog entries!
### cross-glibc-headers-inject
- Updated : 2.30+git8-1.5.1.jolla -- 2.30+git11-1.6.1.jolla
No new changelog entries!
### cross-glibc-inject
- Updated : 2.30+git8-1.5.1.jolla -- 2.30+git11-1.6.1.jolla
No new changelog entries!
### csd
- Updated : 0.16.28-1.3.10.jolla -- 0.16.29-1.4.22.jolla
- [csd] Remove QtSystemInfo dependency. 
### csd-l10n
- Updated : 1.93.1-1.4.1.jolla -- 1.94.1-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 483 of 483 strings translated (0 need review).
- [tpl] translation templates update for 0.16.29
### cups
- Updated : 2.3.1+git1-1.5.1.jolla -- 2.3.1+git2-1.7.2.jolla
- [packaging] Only BuildRequire systemd via pkgconfig. 
### curl
- Updated : 7.78.0+git1-1.6.1.jolla -- 7.81.0+git1-1.8.1.jolla
- [curl] Fix CVE-2021-22946: Protocol downgrade required TLS bypassed
- [curl] Fix CVE-2021-22947: STARTTLS protocol injection via MITM
- [curl] Update to new upstream 7.81.0. 
### dconf
- Updated : 0.40.0+git2-1.7.1.jolla -- 0.40.0+git3-1.8.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### declarative-transferengine-qt5
- Updated : 0.4.6-1.4.1.jolla -- 1.0.3-1.8.2.jolla
- Binaries added : declarative-transferengine-qt5-doc - 1.0.3-1.8.2.jolla
- [declarative-transferengine] Add plugins.qmltypes for Sailfish.Share. 
- [transferengine] Migrate org.nemomobile.thumbnailer import to Nemo.Thumbnailer. 
- [declarative-transferengine] Migrate to sailfish-qdoc-template. 
- [declarative] Load sharing methods directly. 
- [sailfish-share] Add loading indicator. 
- [declarative-transferengine] Install plugin translations in plugin repo instead of declarative_plugin.cpp. 
- [declarative-transferengine] Add docs packaging. 
### declarative-transferengine-qt5-l10n
- Updated : 1.125.1-1.5.1.jolla -- 1.128.2-1.8.1.jolla
- Binaries added : declarative-transferengine-qt5-l10n-lv - 1.128.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 32 of 32 strings translated (0 need review).
- [tpl] translation templates update for 1.0.0
- [l10n] Commit from Jolla localisation: 32 of 32 strings translated (0 need review).
### deltarpm
- Updated : 3.6.2+git1-1.5.3.jolla -- 3.6.3+git1-1.7.10.jolla
- [deltarpm] Upgrade deltarpm and enable zstd support. 
### droid-config-f5121
- Updated : 1.3.24.1-1.5.1.jolla -- 1.3.27-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse.
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
- [flashing] Fix windows flash script guidance URL. 
- [patterns] Pull in legacy ofono RIL plugin. 
### droid-config-f5122
- Updated : 1.3.24.1-1.5.1.jolla -- 1.3.27-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse.
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
- [flashing] Fix windows flash script guidance URL. 
- [patterns] Pull in legacy ofono RIL plugin. 
### droid-config-geminipda
- Updated : 0.2.38-1.6.1.jolla -- 0.2.41-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse.
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Pull in legacy ofono RIL plugin. 
- [configs] Update ohm signals for application id. 
### droid-config-h3113
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-h3213
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-h3413
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-h4113
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-h4213
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-h4413
- Updated : 0.2.79-1.5.1.jolla -- 0.2.82-1.5.1.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [patterns] Use libsensorfw binder instead of old hal implementation. 
- [configs] Update ohm signals for application id. 
### droid-config-i3113
- Updated : 0.0.67-1.5.1.jolla -- 0.0.69-1.5.2.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
### droid-config-i3213
- Updated : 0.0.67-1.5.1.jolla -- 0.0.69-1.5.2.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
### droid-config-i4113
- Updated : 0.0.67-1.5.1.jolla -- 0.0.69-1.5.2.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
### droid-config-i4213
- Updated : 0.0.67-1.5.1.jolla -- 0.0.69-1.5.2.jolla
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
### droid-config-l500d
- Updated : 0.14.32-1.5.1.jolla -- 0.14.36-1.5.1.jolla
- [configs] Disable color filters on L500D. 
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse.
- [configs] move vendor-specific sparse to separate submodule.
- [udev] Add missing path to firmware loader script.
- [configs] Update ohm signals for application id. 
- [patterns] Pull in legacy ofono RIL plugin. 
### droid-config-tbj
- Updated : 0.9.26-1.4.1.jolla -- 0.9.29-1.6.1.jolla
- [camera] Disable color filters. 
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse.
- [configs] move vendor-specific sparse to separate submodule.
- [configs] Update ohm signals for application id. 
- [udev] Add missing path to firmware loader script.
- [configs] Add /oem -> /vendor/oem symlink for all Android 10 based Sony devices. 
- [configs] Restart hwcomposer when lipstick exists. 
- [flashing] A bit more robust getvar handling. 
- [flashing] Add dry run option for testing.
- [flashing] Disable autosuspend while flashing. 
- [flashing] Remove kickstart workaround. 
- [patterns] Use libngf-qt5-qtfeedback plugin. 
### droid-config-xqau51
- Updated : 0.1.21.1-1.6.1.jolla -- 0.1.24.1-1.6.1.jolla
- [configs] Fix single sim configs. 
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule. 
- [udev] Add missing path to firmware loader script. 
- [configs] Update ohm signals for application id. 
### droid-config-xqau52
- Updated : 0.1.21.1-1.6.1.jolla -- 0.1.24.1-1.6.1.jolla
- [configs] Fix single sim configs. 
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule. 
- [udev] Add missing path to firmware loader script. 
- [configs] Update ohm signals for application id. 
### droid-hal-discovery
- Updated : 0.1.27-1.2.3.jolla -- 0.1.28-1.3.5.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
- [libhybris] Update to latest version.
### droid-hal-f5121
- Updated : 0.5.13-1.3.2.jolla -- 0.5.14-1.3.5.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
### droid-hal-geminipda
- Updated : 0.0.16-1.1.1.jolla -- 0.0.17-1.2.1.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
### droid-hal-kirin
- Updated : 0.0.48-1.2.3.jolla -- 0.0.49-1.3.5.jolla
- [android-10] Do not fail if apex folder already exists.
- [audioflingerglue] Fix afglue build on aarch64 target
- [dhd] Add Android 11 support.
- [dhd] BuildRequire systemd via pkgconfig. 
- [dhd] Don't terminate build if files are missing build ids.
- [dhd] Fix detection of header location in local builds
- [dhd] lib{c,dl,m}.so may be in alternate locations.
- [dhd] Move droid headers to /usr/include
- [dhd] remove note about aarch64 since there is an aarch64 target now.
- [helpers] Add quotes to find parameters.
- [helpers] build handy dummy_netd and yamuisplash.
- [helpers] build sailfish-connman-plugin-suspend.
- [helpers] Remove unnecessary packages from build_packages.sh.
- [helpers] support self-hosted repositories.
- [helpers] Use github for middleware packages.
- [libhybris] Add OpenGL ES 3 support.
- [libhybris] Add support for Android 11.
- [libhybris] add support for stdio_ext functions.
- [libhybris] camera_compat_layer: Fix nullptr access in android_camera_enumerate_supported_flash_modes
- [libhybris] camera_service: Conditionalize WANT_UBUNTU_CAMERA_HEADERS from Halium-side
- [libhybris] Cleanup libhybris code
- [libhybris] compat: fix compilation on Android 5 or lower
- [libhybris] Conditionalize Ubuntu Camera Headers
- [libhybris] configure: Check android headers also when pkgconfig is used.
- [libhybris] eglplatform: Fix handling max buffer count.
- [libhybris] eglplatform: increase eglextensionsbuf
- [libhybris] eglplatform_wayland: load libEGL add runtime
- [libhybris] egl: Set buffer dimensions on window resize.
- [libhybris] egl: tests: Add libhardware to ld flags
- [libhybris] egl: wayland: Remove additional space before EGL_EXT
- [libhybris] enable arm tracing also for aarch64
- [libhybris] extract-headers.sh: Fix warnings about double quotes
- [libhybris] extract-headers.sh: Use version from Mer (Adds Android 8 & 9 support)
- [libhybris] Fallback to own property implementation if libc is not present
- [libhybris] Fix pkg-config file when using --with-android-headers
- [libhybris] hooks: Improve adreno quirks.
- [libhybris] hooks: remove __attribute__((packed)) from struct bionic_file.
- [libhybris] hooks: Reset reference count of condition variable before pthread_cond_destroy.
- [libhybris] hybris: Add tracing support for jb linker.
- [libhybris] hybris: common: o: improve android pie support
- [libhybris] hybris: common: prioritize library path set by environment variable
- [libhybris] hybris: common: q: Fix building q linker without HYBRIS_TRACE_(*)HOOKED support.
- [libhybris] hybris: common: q: prioritize library path set by environment variable.
- [libhybris] hybris: egl: Update EGL headers to version 1.5.
- [libhybris] hybris: fix crash when gralloc1 not supported on the device
- [libhybris] hybris: fix wrappers for aarch64.
- [libhybris] hybris: hook close.
- [libhybris] hybris: hook __cxa_thread_atexit
- [libhybris] hybris: hwc2: avoid crash in hwc2_compat_display_present
- [libhybris] hybris: introduce ARM64 support for HYBRIS_TRACE_(DYNHOOKED/UNHOOKED/HOOKED)
- [libhybris] hybris: Move android-config include before gralloc.h include to fix crashes on devices with QCOM_BSP.
- [libhybris] hybris: Remove automatically generated INSTALL file.
- [libhybris] hybris: support HYBRIS_TRACE_(*)HOOKED in q linker.
- [libhybris] hybris: use internal counter for __cxa_thread_exit
- [libhybris] libhybris: Fix various warnings about wrong argument types
- [libhybris] media_format_layer_priv.cpp: Drop orphaned #endif
- [libhybris] Prevent race condition on ws init
- [libhybris] scripts: Fix double quote issues. Python fix minor errors
- [libhybris] support Android 10.
- [libhybris] Unlock mutex even when already initialized
- [libhybris] update submodule after the latest upstream changes.
- [libhybris] Use default platform if env variable is empty
- [packaging] Cleanup spec and silence some rpmlint warnings.
- [packaging] Cleanup spec. Fix conflict with mesa.
- [packaging] Fix for the 64bit architecture.
- [patterns] remove yaml leftovers.
### droid-hal-l500d
- Updated : 0.0.98-1.3.6.jolla -- 0.0.99-1.4.9.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
### droid-hal-mermaid
- Updated : 0.0.48-1.2.3.jolla -- 0.0.49-1.3.5.jolla
- [android-10] Do not fail if apex folder already exists.
- [audioflingerglue] Fix afglue build on aarch64 target
- [dhd] Add Android 11 support.
- [dhd] BuildRequire systemd via pkgconfig. 
- [dhd] Don't terminate build if files are missing build ids.
- [dhd] Fix detection of header location in local builds
- [dhd] lib{c,dl,m}.so may be in alternate locations.
- [dhd] Move droid headers to /usr/include
- [dhd] remove note about aarch64 since there is an aarch64 target now.
- [helpers] Add quotes to find parameters.
- [helpers] build handy dummy_netd and yamuisplash.
- [helpers] build sailfish-connman-plugin-suspend.
- [helpers] Remove unnecessary packages from build_packages.sh.
- [helpers] support self-hosted repositories.
- [helpers] Use github for middleware packages.
- [libhybris] Add OpenGL ES 3 support.
- [libhybris] Add support for Android 11.
- [libhybris] add support for stdio_ext functions.
- [libhybris] camera_compat_layer: Fix nullptr access in android_camera_enumerate_supported_flash_modes
- [libhybris] camera_service: Conditionalize WANT_UBUNTU_CAMERA_HEADERS from Halium-side
- [libhybris] Cleanup libhybris code
- [libhybris] compat: fix compilation on Android 5 or lower
- [libhybris] Conditionalize Ubuntu Camera Headers
- [libhybris] configure: Check android headers also when pkgconfig is used.
- [libhybris] eglplatform: Fix handling max buffer count.
- [libhybris] eglplatform: increase eglextensionsbuf
- [libhybris] eglplatform_wayland: load libEGL add runtime
- [libhybris] egl: Set buffer dimensions on window resize.
- [libhybris] egl: tests: Add libhardware to ld flags
- [libhybris] egl: wayland: Remove additional space before EGL_EXT
- [libhybris] enable arm tracing also for aarch64
- [libhybris] extract-headers.sh: Fix warnings about double quotes
- [libhybris] extract-headers.sh: Use version from Mer (Adds Android 8 & 9 support)
- [libhybris] Fallback to own property implementation if libc is not present
- [libhybris] Fix pkg-config file when using --with-android-headers
- [libhybris] hooks: Improve adreno quirks.
- [libhybris] hooks: remove __attribute__((packed)) from struct bionic_file.
- [libhybris] hooks: Reset reference count of condition variable before pthread_cond_destroy.
- [libhybris] hybris: Add tracing support for jb linker.
- [libhybris] hybris: common: o: improve android pie support
- [libhybris] hybris: common: prioritize library path set by environment variable
- [libhybris] hybris: common: q: Fix building q linker without HYBRIS_TRACE_(*)HOOKED support.
- [libhybris] hybris: common: q: prioritize library path set by environment variable.
- [libhybris] hybris: egl: Update EGL headers to version 1.5.
- [libhybris] hybris: fix crash when gralloc1 not supported on the device
- [libhybris] hybris: fix wrappers for aarch64.
- [libhybris] hybris: hook close.
- [libhybris] hybris: hook __cxa_thread_atexit
- [libhybris] hybris: hwc2: avoid crash in hwc2_compat_display_present
- [libhybris] hybris: introduce ARM64 support for HYBRIS_TRACE_(DYNHOOKED/UNHOOKED/HOOKED)
- [libhybris] hybris: Move android-config include before gralloc.h include to fix crashes on devices with QCOM_BSP.
- [libhybris] hybris: Remove automatically generated INSTALL file.
- [libhybris] hybris: support HYBRIS_TRACE_(*)HOOKED in q linker.
- [libhybris] hybris: use internal counter for __cxa_thread_exit
- [libhybris] libhybris: Fix various warnings about wrong argument types
- [libhybris] media_format_layer_priv.cpp: Drop orphaned #endif
- [libhybris] Prevent race condition on ws init
- [libhybris] scripts: Fix double quote issues. Python fix minor errors
- [libhybris] support Android 10.
- [libhybris] Unlock mutex even when already initialized
- [libhybris] update submodule after the latest upstream changes.
- [libhybris] Use default platform if env variable is empty
- [packaging] Cleanup spec and silence some rpmlint warnings.
- [packaging] Cleanup spec. Fix conflict with mesa.
- [packaging] Fix for the 64bit architecture.
- [patterns] remove yaml leftovers.
### droid-hal-pdx201
- Updated : 0.0.13-1.3.7.jolla -- 0.0.20-1.6.1.jolla
- [kernel] lowmemorykiller: consider swap free size. 
- [dhd] helpers: Build pulseaudio-modules-droid-jb2q for Android versions up to 10. 
- [helpers] Refactor utils to use mb2 --package-timeline. 
- [kernel] proc: update perms of node reclaim. 
- [localbuild] Make all build script changes persistent. 
- [localbuild] Pass local repo to zypper ahead of `ssu ar` removal. 
- [localbuild] Remove leftovers manually for now. 
- [localbuild] Switch local repo to flat dir structure. 
- [localbuild] Use mb2 --output-dir instead to deploy RPMs. 
- [localbuild] Use sdk-assistant maintain instead of sb2. 
- [kernel] Lessen touchpad driver kmsg spam. 
- [kernel] Enable USB_RTL8152 driver. 
- [kernel] Update to version 4.14.254.
- [kernel] Update to version 4.14.253. 
- [dhd] Add Android 11 support.
- [dhd] BuildRequire systemd via pkgconfig. 
- [dhd] Don't terminate build if files are missing build ids.
- [dhd] lib{c,dl,m}.so may be in alternate locations.
- [dhd] remove note about aarch64 since there is an aarch64 target now.
- [helpers] Add quotes to find parameters.
- [helpers] Remove unnecessary packages from build_packages.sh.
- [helpers] Use github for middleware packages.
- [libhybris] Add support for Android 11.
- [libhybris] enable arm tracing also for aarch64
- [libhybris] hooks: Reset reference count of condition variable before pthread_cond_destroy.
- [libhybris] hybris: Add tracing support for jb linker.
- [libhybris] hybris: common: q: Fix building q linker without HYBRIS_TRACE_(*)HOOKED support.
- [libhybris] hybris: common: q: prioritize library path set by environment variable.
- [libhybris] hybris: fix wrappers for aarch64.
- [libhybris] hybris: hook close.
- [libhybris] hybris: Move android-config include before gralloc.h include to fix crashes on devices with QCOM_BSP.
- [libhybris] hybris: support HYBRIS_TRACE_(*)HOOKED in q linker.
- [droid-hal] Disable unneeded mount points. 
- [kernel] Update to latest 4.14.240. 
### droid-hal-pioneer
- Updated : 0.1.27-1.2.3.jolla -- 0.1.28-1.3.5.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
- [libhybris] Update to latest version.
### droid-hal-tbj
- Updated : 0.0.53-1.3.6.jolla -- 0.0.54-1.4.7.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
### droid-hal-tbj-img-boot
- Updated : 3.10.20.20200204.1-1.2.5.jolla -- 3.10.20.20211112.1-1.3.6.jolla
- [tbj] Add missing expat build requirement. 
### droid-hal-voyager
- Updated : 0.1.27-1.2.3.jolla -- 0.1.28-1.3.5.jolla
- [dhd] BuildRequire systemd via pkgconfig. 
- [libhybris] Update to latest version.
### droid-src-sony-seine
- Updated : 0.1.6-1.3.2.jolla -- 0.1.7-1.4.4.jolla
- [droid-src] Update manifest from sony upstream. 
### droid-system-pdx201
- Updated : 0.1.6-1.4.1.jolla -- 0.1.7-1.5.1.jolla
- [sparse] Update from upstream to fix vulkan support. 
### droid-system-pdx201-xqau51
- Updated : 0.1.6-1.4.1.jolla -- 0.1.7-1.5.1.jolla
- [sparse] Update from upstream to fix vulkan support. 
### droid-system-pdx201-xqau52
- Updated : 0.1.6-1.4.1.jolla -- 0.1.7-1.5.1.jolla
- [sparse] Update from upstream to fix vulkan support. 
### droidmedia
- Updated : 0.20210818.0-1.4.1.jolla -- 0.20211101.0-1.5.1.jolla
- [droidmedia] Set the depth of the decoder input queue. 
- [droidmedia] Add support for Android 11 base.
- [droidmedia] Use recorder callback for Android 8. 
- [droidmedia] Change function prototypes according to AOSP Android 10. 
- [droidmedia] Make service_10_0_0.h include all necessary headers. 
### droidmedia-devel
- Updated : 0.20210818.0-1.2.4.jolla -- 0.20211101.0-1.3.14.jolla
- [droidmedia] Set the depth of the decoder input queue. 
- [droidmedia] Add support for Android 11 base.
- [droidmedia] Use recorder callback for Android 8. 
- [droidmedia] Change function prototypes according to AOSP Android 10. 
- [droidmedia] Make service_10_0_0.h include all necessary headers. 
### dsme
- Updated : 0.83.1-1.5.1.jolla -- 0.84.0-1.7.1.jolla
- [DSME] Use wheel group as priveleged
- [tests] Use correct DSME D-Bus object path. 
### embedlite-components-qt5
- Updated : 1.23.11-1.20.1.jolla -- 1.24.33-1.35.1.jolla
- [embedlite-components] Report back default search engine change. 
- [embedlite-components] Fixed password save dialog showing incorrect host. 
- [embedlite-components] Fixed password save dialog showing incorrect (stripped to TLD) hostname
- [embedlite-components] removed extra newline
- [embedlite-components] Removed _getShortDisplayHost function because we use login.displayOrigin which doesn't need to be altered.
- [embedlite-components] Populate the technical details of the certificate page. 
- [embedlite-components] Pass double taps to javascript handlers. 
- [embedlite-components] Touch the recipeParentPromise lazy getter. 
- [embedlite-components] Fix Form ownerDocument is undefined error. 
- [embedlite-components] Update default locale release date. 
- [embedlite-components] Update en-US locale for ESR78
- [embedlite-components] Update fi locale for ESR78
- [embedlite-components] Update ru locale for ESR78
- [embedlite-components] Initialize the certificate viewer handler. 
- [embedlite-components] Enable password autocomplete. 
- [embedlite-components] Fix username keybaord autofill bar entries
- [embedlite-components] Update legacyHistory index. 
- [embedlite-components] Fix SelectionPrototype characterMove error. 
- [embedlite-components] Provide autocomplete and autocapitalize attributes values. 
- [embedlite-components] Catch possible selection listener errors. 
- [embedlite-components] Fix credentials saving error in LoginManagerPrompter. 
- [embedlite-components] Fix EmbedLiteConsoleListener. 
- [embedlite-components] Don't add user-agent header when in CORS mode. 
- [embedlite-components] Send visual viewport offset for context menu and text selection. 
- [embedlite-components] Add ability of calculating cache and site data size. 
- [embedlite-components] Replace clearing of "cookie" with "cookies-and-site-data". 
- [embedlite-components] Use a new API for clearing cookie and cache. 
- [embedlite-components] Broadcast media types used for WebRTC. 
- [embedlite-components] Fix TLS certificate error page. 
- [embedlite-components] Update to new nsITypeAheadFind interface. 
- [embedlite-components] Reinstate search in text selection toolbar. 
- [embedlite-components] Fix javascript console logging output. 
- [embedlite-components] Remove reference to nsIDOMNode as it no longer exists. 
- [embedlite-components] Pass private browsing status when requesting permissions. 
- [embedlite-components] Rename nsLoginManagerPrompter.js to LoginManagerPrompter.js. 
- [embedlite-components] Update LoginManagerPrompter.js with code from upstream. 
- [embedlite-components] Update to new nsILoginManagerPrompter interface. 
- [embedlite-components] Cleanup unused xpcom-shutdown. 
- [embedlite-components] Replace uses of URI only permissions API. 
- [embedlite-components] Fix WebRTC camera permissions. 
- [embedlite-components] Use both element.form and element.formAction to figure out origin. 
- [embedlite-components] Fix for dropped nsIDOMNSEditableElement for esr78. 
- [embedlite-components] Adapt ContentPermissionManager to esr78. 
- [embedlite-components] Adapt 'embedui:addhistory' code to API changes. 
- [embedlite-components] Adapt HelperAppDialog aka file saving to work. 
- [embedlite-components] Adapt LoginManagerParent listener registrations. 
- [embedlite-components] Adapt PromptService. 
- [embedlite-components] Adapt Services.locale.setAvailableLocales to new API. 
- [embedlite-components] Adapt window.QueryInterface calls (part 1). 
- [embedlite-components] Adapt window.queryInterface usage (part 2). 
- [embedlite-components] Add fallback attaching for ActorManagerChild. 
- [embedlite-components] Add missing argument to the speculative connect. 
- [embedlite-components] Add UserAgentUpdates handle. 
- [embedlite-components] Cleanup sendAsyncMessage wrapper. 
- [embedlite-components] Comment out LoginManagerContent call. 
- [embedlite-components] Distribute a default favicon. 
- [embedlite-components] Do not ignore root scroll frame on send mouse event. 
- [embedlite-components] Do not redeclare XPCOMUtils for FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from ContextMenu. 
- [embedlite-components] Fix addEventListener reference errors from embedhelper subscript loading. 
- [embedlite-components] Fix addEventListener reference errors from FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from SelectAsyncHelper. 
- [embedlite-components] Fix addEventListener reference errors from SelectionHandler. 
- [embedlite-components] Fix authentication prompt window id. 
- [embedlite-components] Fix Ci.nsIDOMMouseEvent references. 
- [embedlite-components] Fix default user-agent returning. 
- [embedlite-components] Fix for FilePicker.js error. 
- [embedlite-components] Fix fullscreen mode. 
- [embedlite-components] Fix isFirstPaint check. 
- [embedlite-components] Fix Node.Element reference errors. 
- [embedlite-components] Fix null message manager from SelectionHandler.js. 
- [embedlite-components] Fix OrientationChangeHandler loading. 
- [embedlite-components] Fix per frame initialization of lecacy window actors. 
- [embedlite-components] Fix PrivateBrowsingUtils reference errors. 
- [embedlite-components] Fix quering windowUtils from contextmenu handlers. 
- [embedlite-components] Fix "QueryInterface is not a function" error. 
- [embedlite-components] Fix references errors from text selection. 
- [embedlite-components] Fix WebRTC permission prompts. 
- [embedlite-components] For time being hack sendAsyncMessage. 
- [embedlite-components] Import resources with ChromeUtils. 
- [embedlite-components] Instead of using Ci.nsIDOMNode.ELEMENT_NODE use Node.ELEMENT_NODE. 
- [embedlite-components] Move UserAgentOverrides.jsm to embedlite-components. 
- [embedlite-components] Pass nodePrincipal to the speculative connect. 
- [embedlite-components] Remove nsIDOMDocument usage. 
- [embedlite-components] Remove redeclared XPCOMUtils from InputMethodHandlers. 
- [embedlite-components] Remove unneeded search engine setting that throws an error. 
- [embedlite-components] Remove video control overrides. 
- [embedlite-components] Rename LoginManagerContent to LoginManagerChild. 
- [embedlite-components] Replace calls to XPCOMUtils.generateQI. 
- [embedlite-components] Replace Ci.nsIDOMNode.ELEMENT_NODE with Node.ELEMENT_NODE. 
- [embedlite-components] Replace XPCOMUtils.generateQI with ChromeUtils.generateQI. 
- [embedlite-components] Return default user-agent if there is no override for loading principal uri. 
- [embedlite-components-search-engines] Search engine init fix for esr78. 
- [embedlite-components] Setup ActorManagerParent. 
- [embedlite-components] Use PurgeHistory from legacy history. 
- [embedlite-components] Add fallback attaching for ActorManagerChild. 
- [embedlite-components] Remove redeclared XPCOMUtils from InputMethodHandlers. 
- [embedlite-components] Replace XPCOMUtils.generateQI with ChromeUtils.generateQI. 
- [embedlite-components] Return default user-agent if there is no override for loading principal uri. 
- [embedlite-components] Adapt 'embedui:addhistory' code to API changes. 
- [embedlite-components] Adapt HelperAppDialog aka file saving to work. 
- [embedlite-components] Adapt LoginManagerParent listener registrations. 
- [embedlite-components] Adapt PromptService. 
- [embedlite-components] Adapt Services.locale.setAvailableLocales to new API. 
- [embedlite-components] Adapt window.QueryInterface calls (part 1). 
- [embedlite-components] Adapt window.queryInterface usage (part 2). 
- [embedlite-components] Add missing argument to the speculative connect. 
- [embedlite-components] Add UserAgentUpdates handle. 
- [embedlite-components] Cleanup sendAsyncMessage wrapper. 
- [embedlite-components] Comment out LoginManagerContent call. 
- [embedlite-components] Do not ignore root scroll frame on send mouse event. 
- [embedlite-components] Do not redeclare XPCOMUtils for FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from ContextMenu. 
- [embedlite-components] Fix addEventListener reference errors from embedhelper subscript loading. 
- [embedlite-components] Fix addEventListener reference errors from FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from SelectAsyncHelper. 
- [embedlite-components] Fix addEventListener reference errors from SelectionHandler. 
- [embedlite-components] Fix authentication prompt window id. 
- [embedlite-components] Fix Ci.nsIDOMMouseEvent references. 
- [embedlite-components] Fix default user-agent returning. 
- [embedlite-components] Fix for FilePicker.js error. 
- [embedlite-components] Fix fullscreen mode. 
- [embedlite-components] Fix isFirstPaint check. 
- [embedlite-components] Fix Node.Element reference errors. 
- [embedlite-components] Fix null message manager from SelectionHandler.js. 
- [embedlite-components] Fix OrientationChangeHandler loading. 
- [embedlite-components] Fix per frame initialization of lecacy window actors. 
- [embedlite-components] Fix PrivateBrowsingUtils reference errors. 
- [embedlite-components] Fix quering windowUtils from contextmenu handlers. 
- [embedlite-components] Fix "QueryInterface is not a function" error. 
- [embedlite-components] Fix references errors from text selection. 
- [embedlite-components] Fix WebRTC permission prompts. 
- [embedlite-components] For time being hack sendAsyncMessage. 
- [embedlite-components] Import resources with ChromeUtils. 
- [embedlite-components] Instead of using Ci.nsIDOMNode.ELEMENT_NODE use Node.ELEMENT_NODE. 
- [embedlite-components] Move UserAgentOverrides.jsm to embedlite-components. 
- [embedlite-components] Pass nodePrincipal to the speculative connect. 
- [embedlite-components] Remove nsIDOMDocument usage. 
- [embedlite-components] Remove unneeded search engine setting that throws an error. 
- [embedlite-components] Remove video control overrides. 
- [embedlite-components] Rename LoginManagerContent to LoginManagerChild. 
- [embedlite-components] Replace calls to XPCOMUtils.generateQI. 
- [embedlite-components] Replace Ci.nsIDOMNode.ELEMENT_NODE with Node.ELEMENT_NODE. 
- [embedlite-components-search-engines] Search engine init fix for esr78. 
- [embedlite-components] Setup ActorManagerParent. 
- [embedlite-components] Use PurgeHistory from legacy history. 
- [embedlite-components] Adapt 'embedui:addhistory' code to API changes. 
- [embedlite-components] Adapt HelperAppDialog aka file saving to work. 
- [embedlite-components] Adapt LoginManagerParent listener registrations. 
- [embedlite-components] Adapt PromptService. 
- [embedlite-components] Adapt Services.locale.setAvailableLocales to new API. 
- [embedlite-components] Adapt window.QueryInterface calls (part 1). 
- [embedlite-components] Adapt window.queryInterface usage (part 2). 
- [embedlite-components] Add missing argument to the speculative connect. 
- [embedlite-components] Add UserAgentUpdates handle. 
- [embedlite-components] Cleanup sendAsyncMessage wrapper. 
- [embedlite-components] Comment out LoginManagerContent call. 
- [embedlite-components] Do not ignore root scroll frame on send mouse event. 
- [embedlite-components] Do not redeclare XPCOMUtils for FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from ContextMenu. 
- [embedlite-components] Fix addEventListener reference errors from embedhelper subscript loading. 
- [embedlite-components] Fix addEventListener reference errors from FormAssistant. 
- [embedlite-components] Fix addEventListener reference errors from SelectAsyncHelper. 
- [embedlite-components] Fix addEventListener reference errors from SelectionHandler. 
- [embedlite-components] Fix authentication prompt window id. 
- [embedlite-components] Fix Ci.nsIDOMMouseEvent references. 
- [embedlite-components] Fix default user-agent returning. 
- [embedlite-components] Fix for FilePicker.js error. 
- [embedlite-components] Fix isFirstPaint check. 
- [embedlite-components] Fix Node.Element reference errors. 
- [embedlite-components] Fix null message manager from SelectionHandler.js. 
- [embedlite-components] Fix OrientationChangeHandler loading. 
- [embedlite-components] Fix per frame initialization of lecacy window actors. 
- [embedlite-components] Fix PrivateBrowsingUtils reference errors. 
- [embedlite-components] Fix quering windowUtils from contextmenu handlers. 
- [embedlite-components] Fix "QueryInterface is not a function" error. 
- [embedlite-components] Fix references errors from text selection. 
- [embedlite-components] For time being hack sendAsyncMessage. 
- [embedlite-components] Import resources with ChromeUtils. 
- [embedlite-components] Instead of using Ci.nsIDOMNode.ELEMENT_NODE use Node.ELEMENT_NODE. 
- [embedlite-components] Move UserAgentOverrides.jsm to embedlite-components. 
- [embedlite-components] Pass nodePrincipal to the speculative connect. 
- [embedlite-components] Remove nsIDOMDocument usage. 
- [embedlite-components] Remove unneeded search engine setting that throws an error. 
- [embedlite-components] Remove video control overrides. 
- [embedlite-components] Rename LoginManagerContent to LoginManagerChild. 
- [embedlite-components] Replace calls to XPCOMUtils.generateQI. 
- [embedlite-components] Replace Ci.nsIDOMNode.ELEMENT_NODE with Node.ELEMENT_NODE. 
- [embedlite-components-search-engines] Search engine init fix for esr78. 
- [embedlite-components] Setup ActorManagerParent. 
- [embedlite-components] Use PurgeHistory from legacy history. 
- [embedlite-components] Cleanup desktop user-agent of the UserAgentOverrideHelper. 
- [embedlite-components] Block click event only when "href" attribute is defined. 
- [embedlite-components] Provide input context info for predictive text input. 
- [embedlite-components] Cleanup EmbedLiteConsoleListener. 
- [embedlite-components] Update gecko error page design. 
### eventsview-extensions-l10n
- Updated : 1.34.1-1.5.1.jolla -- 1.36.2-1.7.1.jolla
- Binaries added : eventsview-extensions-l10n-lv - 1.36.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 21 of 21 strings translated (0 need review).
### extra-cmake-modules
- Updated : 5.75.0+git1-1.4.1.jolla -- 5.85.0+git1-1.6.1.jolla
- [extra-cmake-modules] Update to 5.85.0. 
- [extra-cmake-modules] Update to upstream 5.85.0.
### ffmpeg
- Updated : 4.3.1+git1-1.4.1.jolla -- 4.4.1+git1-1.6.1.jolla
- [ffmpeg] Update to version 4.4.1. 
### filesystem
- Updated : 3.1+git5-1.7.1.jolla -- 3.16+git1-1.9.1.jolla
- Binaries added : filesystem-content - 3.16+git1-1.9.1.jolla
- Sync with Fedora 3.16 version. 
### fingerterm-l10n
- Updated : 1.26.1-1.11.1.jolla -- 1.28.2-1.13.1.jolla
- Binaries added : fingerterm-l10n-lv - 1.28.2-1.13.1.jolla
- [l10n] Commit from Jolla localisation: 37 of 37 strings translated (0 need review).
### firejail
- Updated : 0.9.66+git1-1.6.1.jolla -- 0.9.66+git2-1.7.1.jolla
- [firejail] Retain symlink chains. 
### gecko-camera
- Updated : 0.1.0-1.2.3.jolla -- 0.1.4-1.4.4.jolla
- [gecko-camera] Add dummy camera plugin.
- [gecko-camera] Change camera API for convenience on Gecko side
- [gecko-camera] Create plugin manager
- [gecko-camera] Define codec API. 
- [gecko-camera] Eliminate the possible race condition and rename class members.
- [gecko-camera] Fix timestamps for camera frames
- [gecko-camera] Implement codec API in the droid plugin. 
- [gecko-camera] Move the droid plugin to a subdirectory. 
- [gecko-camera] Recommend gecko-camera-droid-plugin when installing gecko-camera. 
- [droid] Stop capturing when opening another camera. 
- [droid] Disconnect camera on stopCapture(). 
- [droid] Do not unlock the camera before disconnecting. 
- [example] Add ability to select a camera to test
### gecko-camera-droid-plugin
- Updated : 0.1.0-1.2.1.jolla -- 0.1.4-1.4.1.jolla
- [gecko-camera] Add dummy camera plugin.
- [gecko-camera] Change camera API for convenience on Gecko side
- [gecko-camera] Create plugin manager
- [gecko-camera] Define codec API. 
- [gecko-camera] Eliminate the possible race condition and rename class members.
- [gecko-camera] Fix timestamps for camera frames
- [gecko-camera] Implement codec API in the droid plugin. 
- [gecko-camera] Move the droid plugin to a subdirectory. 
- [gecko-camera] Recommend gecko-camera-droid-plugin when installing gecko-camera. 
- [droid] Stop capturing when opening another camera. 
- [droid] Disconnect camera on stopCapture(). 
- [droid] Do not unlock the camera before disconnecting. 
- [example] Add ability to select a camera to test
### geoclue-provider-hybris-binder
- Updated : 0.2.32-1.3.1.jolla -- 0.2.35-1.5.1.jolla
- [geoclue-providers-hybris] Fix setting accuracy properly. 
- [geoclue-providers-hybris] Have license file as %license. 
- [packaging] BuildRequire systemd via pkgconfig. 
### geoclue-provider-hybris-hal
- Updated : 0.2.32-1.3.1.jolla -- 0.2.35-1.5.1.jolla
- [geoclue-providers-hybris] Fix setting accuracy properly. 
- [geoclue-providers-hybris] Have license file as %license. 
- [packaging] BuildRequire systemd via pkgconfig. 
### giflib
- Updated : 4.2.3+git2-1.5.1.jolla -- 5.2.1+git1-1.7.1.jolla
- Binaries removed : giflib-doc
- [giflib] Update to 5.2.1. 
### glibc
- Updated : 2.30+git8-1.9.1.jolla -- 2.30+git11-1.10.1.jolla
- Add fix for CVE-2022-23218. 
- Add fix for CVE-2022-23219. 
- Remove broken Obsoletes for x86_64. 
- Disable crypt. 
### gmp-droid
- Updated : 0.4-1.2.1.jolla -- 0.5-1.3.1.jolla
- [gmp] Fix encoder crash when stopped. 
- [gmp] Fix several stablilty issues. 
- [gmp] Rework locking in decoder. 
### grilo-qt5
- Updated : 0.3.1-1.6.1.jolla -- 0.3.2-1.8.1.jolla
- [qtgrilo] Update plugins.qmltypes. 
### gstreamer1.0
- Updated : 1.18.4+git1-1.5.3.jolla -- 1.18.5+git1-1.7.11.jolla
- [gstreamer] Update to 1.18.5. 
### gstreamer1.0-droid
- Updated : 0.20210820.0-1.2.1.jolla -- 0.20211101.0-1.3.1.jolla
- [gst-droid] Fix deadlocking during stop preview. 
- [droidcamsrc] Add missing null checks for buffer pool. 
### gstreamer1.0-libav
- Updated : 1.18.4+git1-1.5.1.jolla -- 1.18.5+git1-1.7.1.jolla
- [gst-libav] Update to 1.18.5. 
### gstreamer1.0-plugins-bad
- Updated : 1.18.4+git1-1.5.1.jolla -- 1.18.5+git1-1.7.1.jolla
- [gst-plugins-bad] Update to 1.18.5. 
### gstreamer1.0-plugins-base
- Updated : 1.18.4+git2-1.6.1.jolla -- 1.18.5+git2-1.7.3.jolla
- [gst-plugins-base] Remove old conflicting patch. 
- [gst-plugins-base] Update to 1.18.5. 
### gstreamer1.0-plugins-good
- Updated : 1.18.4+git1-1.5.1.jolla -- 1.18.5+git2-1.7.1.jolla
- [spec] Properly buildrequires on nasm. 
- [spec] Properly buildrequires on nasm for x86_64. 
- [gst-plugins-good] Update to 1.18.5. 
### hybris-libsensorfw-qt5-binder
- Updated : 0.12.4-1.3.1.jolla -- 0.12.6-1.5.1.jolla
- [sensorfw] Add support for sensor binder API 2. 
- [sensorfw] Fix build on 32-bit kernels with 64-bit time_t. 
### hybris-libsensorfw-qt5-hal
- Updated : 0.12.4-1.3.1.jolla -- 0.12.6-1.5.1.jolla
- [sensorfw] Add support for sensor binder API 2. 
- [sensorfw] Fix build on 32-bit kernels with 64-bit time_t. 
### iptables
- Updated : 1.8.2+git3-1.5.1.jolla -- 1.8.7+git1-1.7.1.jolla
- [upstream] Update to iptables 1.8.7. 
### jolla-alarm-ui
- Updated : 0.2.15-1.3.1.jolla -- 0.2.16-1.4.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### jolla-alarm-ui-l10n
- Updated : 1.96.1-1.5.1.jolla -- 1.98.2-1.7.1.jolla
- Binaries added : jolla-alarm-ui-l10n-lv - 1.98.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 33 of 33 strings translated (0 need review).
### jolla-ca
- Updated : 0.10-1.3.1.jolla -- 0.11-1.4.1.jolla
- [ca] Add new root CA certificate 
### jolla-calculator
- Updated : 1.0.7-1.3.1.jolla -- 1.0.8-1.4.1.jolla
- [calculator] Include app summary and description in translations. 
- [calculator] Remove absolute path for qmltestrunner. 
### jolla-calculator-l10n
- Updated : 1.75.2-1.4.1.jolla -- 1.80.3-1.7.1.jolla
- Binaries added : jolla-calculator-l10n-lv - 1.80.3-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 6 of 6 strings translated (0 need review).
- [tpl] translation templates update for 1.0.8
### jolla-calendar
- Updated : 1.0.31-1.4.1.jolla -- 1.0.36-1.6.1.jolla
- [calendar] Add communication history to permissions. 
- [jolla-calendar] Propose to overwrite existing events on import.
- [jolla-calendar] Remove unneeded Sharing permission. 
- [calendar] Show attendee email as fallback to name. 
- [jolla-calendar] Move EventListDelegate to the components. 
### jolla-calendar-l10n
- Updated : 1.244.1-1.5.1.jolla -- 1.249.2-1.8.1.jolla
- Binaries added : jolla-calendar-l10n-lv - 1.249.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 139 of 139 strings translated (0 need review).
- [tpl] translation templates update for 1.0.35
- [l10n] Commit from Jolla localisation: 137 of 137 strings translated (0 need review).
- [tpl] translation templates update for 1.0.33
### jolla-camera
- Updated : 1.2.11.2-1.6.1.jolla -- 1.2.16.2-1.8.1.jolla
- [jolla-camera] Disable video torch on camera switch if not supported. 
- [jolla-camera] Disable exposure modes on 4.4 release. 
- [jolla-camera] Enable few color filters. 
- [camera] Use vertical flick down to access camera settings again. 
- [camera] Remove ambience grid and make setting global. 
- [camera] Remove absolute path for qmltestrunner. 
- [camera] Update supported configs when the capture mode is changes between image and video. 
- [jolla-camera] Remove unneeded Sharing permission. 
### jolla-camera-l10n
- Updated : 1.212.1-1.5.1.jolla -- 1.218.2-1.8.1.jolla
- Binaries added : jolla-camera-l10n-lv - 1.218.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 73 of 73 strings translated (0 need review).
- [tpl] translation templates update for 1.2.16.1
- [l10n] Commit from Jolla localisation: 73 of 73 strings translated (0 need review).
- [tpl] translation templates update for 1.2.14
- [tpl] translation templates update for 1.2.15
- [tpl] translation templates update for 1.2.16
- [l10n] Commit from Jolla localisation: 63 of 63 strings translated (0 need review).
### jolla-clock
- Updated : 1.1.18-1.3.1.jolla -- 1.1.19-1.4.1.jolla
- [jolla-clock] Remove absolute path for qmltestrunner. 
### jolla-clock-l10n
- Updated : 1.161.1-1.5.1.jolla -- 1.162.2-1.6.1.jolla
- Binaries added : jolla-clock-l10n-lv - 1.162.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 47 of 48 strings translated (0 need review).
### jolla-common-configurations
- Updated : 0.11.1.1-1.5.1.jolla -- 0.11.3-1.5.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
- [config] Enable sandboxing of all apps. 
### jolla-contacts
- Updated : 0.6.33-1.4.1.jolla -- 0.6.36-1.6.1.jolla
- [contacts] Add permission to access contact history. 
- [contacts] Remove unnecessary qtopengl build requirement. 
- [jolla-contacts] Remove unneeded Sharing permission. 
### jolla-contacts-l10n
- Updated : 1.185.1-1.5.1.jolla -- 1.187.2-1.7.1.jolla
- Binaries added : jolla-contacts-l10n-lv - 1.187.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 60 of 60 strings translated (0 need review).
### jolla-devicelock
- Updated : 0.2.46-1.2.4.jolla -- 0.2.47-1.3.21.jolla
- [packaging] Only BuildRequire systemd via pkgconfig. 
### jolla-devicelock-l10n
- Updated : 1.47.4-1.3.1.jolla -- 1.48.2-1.5.1.jolla
- Binaries added : jolla-devicelock-l10n-lv - 1.48.2-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 7 of 7 strings translated (0 need review).
### jolla-email
- Updated : 1.1.24-1.4.1.jolla -- 1.1.29-1.8.1.jolla
- [email] Refactor crypto availability to singleton. 
- [email] Change org.nemomobile.thumbnailer import to Nemo.Thumbnailer. 
- [jolla-email] Use WebView.footerMargin instead of resizing the view. 
- [email] Add communication history permission. 
- [jolla-email] Fix ClickEventBlocker loading for esr78. 
- [jolla-email] Remove unneeded Sharing permission. 
### jolla-email-l10n
- Updated : 1.291.1-1.5.1.jolla -- 1.293.2-1.7.1.jolla
- Binaries added : jolla-email-l10n-lv - 1.293.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 233 of 233 strings translated (0 need review).
- [l10n 
- [tpl] translation templates update for 1.1.29
- [l10n] Commit from Jolla localisation: 233 of 233 strings translated (0 need review).
### jolla-gallery
- Updated : 1.0.38.1-1.5.1.jolla -- 1.1.0-1.6.5.jolla
- [gallery] Use GridItem in Gallery. 
- [gallery] Fix video controls on externally opened files. 
- [gallery] Remove absolute path for qmltestrunner. 
- [gallery] Remove unnecessary qtopengl build requirement. 
- [jolla-gallery] Remove unneeded Sharing permission. 
### jolla-gallery-ambience-l10n
- Updated : 1.133.1-1.5.1.jolla -- 1.134.2-1.7.1.jolla
- Binaries added : jolla-gallery-ambience-l10n-lv - 1.134.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
- [l10n 
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
### jolla-gallery-extensions-l10n
- Updated : 1.43.1-1.4.1.jolla -- 1.43.3-1.5.1.jolla
- Binaries added : jolla-gallery-extensions-l10n-lv - 1.43.3-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 13 of 13 strings translated (0 need review).
### jolla-gallery-facebook
- Updated : 0.1.12-1.3.1.jolla -- 0.1.13-1.4.1.jolla
- [jolla-gallery-facebook] Remove absolute path for qmltestrunner. 
### jolla-gallery-facebook-l10n
- Updated : 1.74.1-1.4.1.jolla -- 1.74.3-1.5.1.jolla
- Binaries added : jolla-gallery-facebook-l10n-lv - 1.74.3-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 14 of 14 strings translated (0 need review).
### jolla-gallery-l10n
- Updated : 1.170.1-1.5.1.jolla -- 1.172.2-1.8.1.jolla
- Binaries added : jolla-gallery-l10n-lv - 1.172.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 17 of 17 strings translated (0 need review).
- [tpl] translation templates update for 1.0.41
- [tpl] translation templates update for 1.1.0
- [l10n] Commit from Jolla localisation: 17 of 17 strings translated (0 need review).
### jolla-keyboard
- Updated : 0.8.28-1.4.1.jolla -- 0.8.28.2-1.6.1.jolla
- [keyboard] Add Latvian layout. 
- [keyboard] Fix number layout getting stuck. 
### jolla-keyboard-l10n
- Updated : 1.100.1-1.5.1.jolla -- 1.101.2-1.6.1.jolla
- Binaries added : jolla-keyboard-l10n-lv - 1.101.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 21 of 21 strings translated (0 need review).
### jolla-mediaplayer
- Updated : 1.3.0-1.4.1.jolla -- 1.3.1.1-1.6.1.jolla
- [mediaplayer] Adapt to adjusted mpris loop enum naming. 
- [mediaplayer] Port to new MPRIS API. 
### jolla-mediaplayer-l10n
- Updated : 1.141.1-1.5.1.jolla -- 1.143.2-1.7.1.jolla
- Binaries added : jolla-mediaplayer-l10n-lv - 1.143.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 65 of 65 strings translated (0 need review).
- [tpl] translation templates update for 1.3.1
- [l10n] Commit from Jolla localisation: 65 of 65 strings translated (0 need review).
### jolla-mediaplayer-radio
- Updated : 0.3.2-1.4.1.jolla -- 0.3.4-1.6.1.jolla
- [mediaplayer-radio] Adapt to adjusted mpris loop enum naming. 
- [mediaplayer-radio] Port to new MPRIS API. 
### jolla-mediaplayer-radio-l10n
- Updated : 1.66.1-1.5.1.jolla -- 1.67.2-1.6.1.jolla
- Binaries added : jolla-mediaplayer-radio-l10n-lv - 1.67.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 11 of 11 strings translated (0 need review).
- [tpl] translation templates update for 0.3.3
### jolla-messages
- Updated : 1.1.55-1.4.1.jolla -- 1.1.60-1.6.1.jolla
- [messages] Add Pictures permission to allow saving MMSes. 
- [messages] Add transition back to new message page opening. 
- [messages] Allow empty recipients in dbus openUrl() call. 
- [messages] Allow sharing of links to Messages app. 
- [jolla-messages] Remove unneeded Sharing permission. 
### jolla-messages-l10n
- Updated : 1.196.1-1.5.1.jolla -- 1.199.2-1.8.1.jolla
- Binaries added : jolla-messages-l10n-lv - 1.199.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 88 of 88 strings translated (0 need review).
- [tpl] translation templates update for 1.1.58
- [l10n] Commit from Jolla localisation: 88 of 88 strings translated (0 need review).
- [tpl] translation templates update for 1.1.57
### jolla-notes
- Updated : 1.0.18-1.4.1.jolla -- 1.0.20-1.5.1.jolla
- [jolla-notes] Remove absolute path for qmltestrunner. 
- [jolla-notes] Remove unneeded Sharing permission. 
### jolla-notes-l10n
- Updated : 1.119.1-1.5.1.jolla -- 1.121.2-1.7.1.jolla
- Binaries added : jolla-notes-l10n-lv - 1.121.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 22 of 22 strings translated (0 need review).
### jolla-sessions-qt5
- Updated : 1.4.20-1.2.1.jolla -- 1.4.21-1.3.1.jolla
- [packaging] Only BuildRequire systemd via pkgconfig. 
### jolla-settings
- Updated : 1.1.15-1.4.1.jolla -- 1.1.15.1-1.5.1.jolla
- [jolla-settings] Get application sandboxing status from sailjail. 
- [settings] Hide Compatibility permission. 
### jolla-settings-accounts
- Updated : 0.4.56-1.4.1.jolla -- 0.4.57-1.5.1.jolla
- [settings-accounts] Remove absolute path for qmltestrunner. 
### jolla-settings-accounts-l10n
- Updated : 1.315.1-1.5.1.jolla -- 1.317.2-1.7.1.jolla
- Binaries added : jolla-settings-accounts-l10n-lv - 1.317.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 382 of 382 strings translated (0 need review).
### jolla-settings-bluetooth
- Updated : 0.2.14-1.2.1.jolla -- 0.2.15-1.3.1.jolla
- [settings-bluetooth] Remove absolute path for qmltestrunner. 
### jolla-settings-bluetooth-l10n
- Updated : 1.122.2-1.4.1.jolla -- 1.123.2-1.5.1.jolla
- Binaries added : jolla-settings-bluetooth-l10n-lv - 1.123.2-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 16 of 16 strings translated (0 need review).
### jolla-settings-l10n
- Updated : 1.144.1-1.5.1.jolla -- 1.145.2-1.7.1.jolla
- Binaries added : jolla-settings-l10n-lv - 1.145.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 22 of 22 strings translated (0 need review).
### jolla-settings-networking-l10n
- Updated : 1.385.1-1.5.1.jolla -- 1.387.2-1.7.1.jolla
- Binaries added : jolla-settings-networking-l10n-lv - 1.387.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 549 of 549 strings translated (0 need review).
### jolla-settings-sailfishos-l10n
- Updated : 1.138.1-1.6.1.jolla -- 1.139.2-1.8.1.jolla
- Binaries added : jolla-settings-sailfishos-l10n-lv - 1.139.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 53 of 53 strings translated (0 need review).
### jolla-settings-sync-l10n
- Updated : 1.65.3-1.3.1.jolla -- 1.65.5-1.4.1.jolla
- Binaries added : jolla-settings-sync-l10n-lv - 1.65.5-1.4.1.jolla
- [l10n] Commit from Jolla localisation: 23 of 23 strings translated (0 need review).
### jolla-settings-system
- Updated : 1.1.48-1.5.8.jolla -- 1.1.51.1-1.8.1.jolla
- Binaries added : jolla-settings-system-packages - 1.1.51.1-1.8.1.jolla
- [system-settings] Add Latvian language. 
- [settings-system] Add Bluetooth Secure Simple Pairing setting to NFC settings. 
- [settings-system] Add 'Install apps' system settings. 
- [settings-system] Remove absolute path for qmltestrunner. 
### jolla-settings-system-l10n
- Updated : 1.551.1-1.6.1.jolla -- 1.556.5-1.12.1.jolla
- Binaries added : jolla-settings-system-l10n-lv - 1.556.5-1.12.1.jolla
- [l10n] Commit from Jolla localisation: 631 of 631 strings translated (0 need review).
- [tpl] translation templates update for 1.1.50
### jolla-signon-ui-l10n
- Updated : 1.59.1-1.5.1.jolla -- 1.59.3-1.6.1.jolla
- Binaries added : jolla-signon-ui-l10n-lv - 1.59.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 3 of 3 strings translated (0 need review).
- [l10n 
### jolla-startupwizard
- Updated : 0.4.39-1.2.1.jolla -- 0.4.40-1.3.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### jolla-startupwizard-l10n
- Updated : 1.217.1-1.5.1.jolla -- 1.217.4-1.7.1.jolla
- Binaries added : jolla-startupwizard-l10n-lv - 1.217.4-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 47 of 47 strings translated (0 need review).
### jolla-vault-l10n
- Updated : 1.179.1-1.5.1.jolla -- 1.182.2-1.7.1.jolla
- Binaries added : jolla-vault-l10n-lv - 1.182.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 84 of 84 strings translated (0 need review).
### kf5-calendarcore
- Updated : 5.83+git2-1.8.1.jolla -- 5.86+git3-1.9.1.jolla
- [kf5-kcalendarcore] Update from upstream, fix exception creating time?
- [kf5-kcalendarcore] Update from upstream, fix exception creating time. 
- [kf5-calendarcore] Fix pkgconfig qtgui dependency. 
- [kf5-kcalendarcore] Fix the missing Qt5Gui dependency in pkgconfig.
- [kf5-calendarcore] Update to 5.86. 
- [kf5-calendarcore] Update to upstream 5.86.
### libblockdev
- Updated : 2.19+git2-1.4.1.jolla -- 2.26+git1-1.6.1.jolla
- [libblockdev] Upgrade to 2.26. 
### libcommhistory-qt5
- Updated : 1.11.11-1.11.1.jolla -- 1.11.11.1-1.12.1.jolla
- [libcommhistory] Fix race when sending a temporary file with MMS. 
### libcontacts-qt5-l10n
- Updated : 1.31.4-1.5.1.jolla -- 1.31.6-1.6.1.jolla
- Binaries added : libcontacts-qt5-l10n-lv - 1.31.6-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 3 of 3 strings translated (0 need review).
### libcontentaction-qt5
- Updated : 0.4.4-1.7.1.jolla -- 0.4.5-1.8.1.jolla
- [libcontentaction] Remove unused qt5systeminfo usage. 
### libgbinder
- Updated : 1.1.10-1.2.1.jolla -- 1.1.18-1.5.1.jolla
- [gbinder] Disassociate auto-created proxies. 
- [gbinder] Expose gbinder_ipc_name as an internal function
- [gbinder] Logging improvements
- [gbinder] Don't release remote proxy handle too early. 
- [gbinder] Make sure stale object pointers don't hang around. 
- [gbinder] Print transaction code in debug build. 
- [gbinder] Properly shut down remote object inside the proxy. 
- [gbinder] Read ref_count from GObject atomically. 
- [license] Freshened up copyright
- [unit] Improved gbinder_ipc_find_local_object coverage
- [gbinder] Added readers for int8 and int16. 
- [gbinder] Added writers for int8 and int16. 
- [gbinder] Housekeeping
- [gbinder] Updated README
- [gbinder] Added "aidl3" variant of RPC protocol. 
- [gbinder] Added "aidl3" variant of service manager. 
- [gbinder] Added gbinder_client_rpc_header(). 
- [gbinder] Added gbinder_reader_get_data(). 
- [gbinder] Added gbinder_servicemanager_device(). 
- [gbinder] Added gbinder_writer_get_data(). 
- [gbinder] Add FMQ unit tests. 
- [gbinder] Add preset gbinder config to support Android API version 30. 
- [gbinder] Add support for FMQ (Fast Message Queue). 
- [gbinder] Don't compile fmq code if __NR_memfd_create is undefined
- [gbinder] Housekeeping. 
- [gbinder] Replace use of stdatomic.h and linux/memfd.h.
- [gbinder] Support writing file descriptor via local reply
- [gbinder] Tolerate NULL const GBinderReader pointers.
- [rpm] Install license file. 
- [unit] Added test for gbinder_local_reply_append_fd()
- [unit] Assert that dummy type functions don't get invoked. 
- [gbinder] Added gbinder_writer_strdup(). 
- [gbinder] Add gbinder_writer_append_hidl_string_copy(). 
- [gbinder] Drop pkgconfig requirement for devel package. 
- [gbinder] Simplify writer a bit. 
- [test] Added ashmem-test. 
- [test] Add binder-call. 
- [test] Add binder-call to debian build. 
- [debian] Bump libglibutil requirement
- [gbinder] Fix occasional crashes in pthread_setname_np(). 
- [gbinder] Fix potential deadlock in gbinder_ipc_looper_free(). 
- [unit] Allow side-by-side linking with libglibutil
- [unit] Make unit tests comptible with glib < 2.36
- [unit] Pull in definition of _IOC_SIZE. 
- [unit] Serialize execution of /ipc/transact_2way
### libgbinder-radio
- Updated : 1.4.1-1.2.1.jolla -- 1.4.8-1.4.1.jolla
- [gbinder-radio] Fixed retries of blocking requests. 
- [gbinder-radio] More logging in radio_request_default_retry()
- [unit] Added test for retry of a blocking request. 
- [gbinder-radio] Added internal DEBUG_ASSERT macro
- [gbinder-radio] Fixed owner queue logic. 
- [gbinder-radio] Houskeeping
- [gbinder-radio] Added RadioConfig API. 
- [gbinder-radio] Fixed compilation issues
- [gbinder-radio] Fixed compilation warning
- [gbinder-radio] Moved reusable code to RadioBase class. 
- [license] Freshened up copyright
- [gbinder-radio] Added radio_req_resp2(). 
- [gbinder-radio] Added IRadio@1.2 IndicationFilter bits. 
- [gbinder-radio] Add RadioClient and related APIs. 
- [rpm] Install license file. 
- [unit] Small fix
- [gbinder-radio] Added unit tests. 
- [gbinder-radio] Don't assume that GBinderServiceManager is a GObject
- [gbinder-radio] Housekeeping
### libgcrypt
- Updated : 1.8.6+git1-1.4.1.jolla -- 1.8.6+git2-1.6.1.jolla
- [packaging] Fix name of gpg-error pkgconfig. 
### libglibutil
- Updated : 1.0.55-1.8.1.jolla -- 1.0.61-1.12.1.jolla
- [glibutil] Added gutil_strv_remove()
- [glibutil] 
- [rpm] Require rpm 4.11 for %license. 
- [libglibutil] Have license file as %license. 
- [glibutil] Don't check upper bound when setting log level from env
- [glibutil] 
- [test] Fixed test_misc for older 32-bit systems
- [glibutil] Added utilities for parsing 64-bit integers
- [glibutil] Dropped pkgconfig requirement
- [glibutil] Housekeeping
- [glibutil] MER#1437
- [unit] Enable parallel build for unit tests
### libgpg-error
- Updated : 1.27+git2-1.5.1.jolla -- 1.27+git3-1.7.1.jolla
- [packaging] Match pkgconfig file with upstream. 
### libgrilio
- Updated : 1.0.40-1.4.1.jolla -- 1.0.41-1.6.1.jolla
- [build] Added dependency of pkgconfig on build dir
- [rpm] Cleaned up the spec
- [test] Increased unit test timeout to 30 sec. 
### libhybris
- Updated : 0.0.5.42.1-1.3.1.jolla -- 0.0.5.44-1.3.1.jolla
- [libhybris] hybris: common: o: Fix incorrect variable name. 
- [libhybris] Add support for Android 11. 
- [libhybris] hooks: Reset reference count of condition variable before pthread_cond_destroy. 
### libiodata-qt5
- Updated : 0.19.11+git1-1.5.1.jolla -- 0.19.11+git2-1.7.1.jolla
- [libiodata-qt5] Explicitly depend on pkgconfig(libcrypt). 
### libjollasignonuiservice-qt5-l10n
- Updated : 1.46.1-1.4.1.jolla -- 1.47.2-1.6.1.jolla
- Binaries added : libjollasignonuiservice-qt5-l10n-lv - 1.47.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 10 of 10 strings translated (0 need review).
### libkeepalive
- Updated : 1.8.4-1.4.1.jolla -- 1.8.7-1.7.2.jolla
- [nemo-keepalive] Fix preventBlankingChanged signal. 
- [nemo-keepalive] Include license file as %license. 
- [nemo-keepalive] Migrate to sailfish-qdoc-template. 
### libmce-glib
- Updated : 1.0.11-1.4.1.jolla -- 1.0.12-1.6.1.jolla
- [libmce-glib] Housekeeping. 
- [libmce-glib] Update license. 
### libnciplugin
- Updated : 1.1.1-1.3.1.jolla -- 1.1.2-1.4.1.jolla
- [nciplugin] Dropped pkgconfig requirement for dev package
- [nciplugin] Fixed adapter mode updates. 
### libngf-qt5
- Updated : 0.8.1-1.7.1.jolla -- 0.8.2-1.9.1.jolla
- [libngf-qt] Update plugins.qmltypes. 
### libphonenumber
- Updated : 8.12.12+git2-1.5.4.jolla -- 8.12.33+git1-1.7.12.jolla
- [libphonenumber] Update libphonenumber to 8.12.33. 
### libresource
- Updated : 0.24.1-1.4.1.jolla -- 0.25.1-1.6.1.jolla
- [libresource] Add missing include. 
- [libresource] Introduce app_id for identifying clients. 
### libresourceqt-qt5
- Updated : 1.30.6-1.7.1.jolla -- 1.31.0-1.9.1.jolla
- [libresourceqt] Use application id with audio. 
### libsailfishapp
- Updated : 1.2.12-1.6.1.jolla -- 1.2.13-1.7.2.jolla
- [libsailfishapp] Added license file. 
- [libsailfishapp] Port to sailfish-qdoc-template. 
### libseccomp
- Updated : 2.4.2+git3-1.4.1.jolla -- 2.5.2+git1-1.6.1.jolla
- [libseccomp] Update to 2.5.2. 
### libsocialcache-l10n
- Updated : 1.12.3-1.5.1.jolla -- 1.12.5-1.6.1.jolla
- Binaries added : libsocialcache-l10n-lv - 1.12.5-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 8 of 8 strings translated (0 need review).
### libsolv
- Updated : 0.7.17+git1-1.5.3.jolla -- 0.7.20+git1-1.6.3.jolla
- [libsolv] Update to 0.7.20. 
### libuser
- Updated : 0.62+git4-1.5.1.jolla -- 0.62+git5-1.7.1.jolla
- [libuser] Explicitly depend on pkgconfig(libcrypt). 
### libxkbcommon
- Updated : 0.5.0+git1-1.5.1.jolla -- 1.3.1+git1-1.7.1.jolla
- [libxkbcommon] Update to 1.3.1. 
### libxslt
- Updated : 1.1.33+git1-1.5.1.jolla -- 1.1.34+git1-1.7.1.jolla
- [libxslt] Update to 1.1.34. 
### lipstick-jolla-home-qt5
- Updated : 1.24.10-1.4.12.jolla -- 1.24.16.3-1.9.5.jolla
- [storage] Reset storage dialog state when shown. 
- [lipstick-jolla-home] Close the parent storage device dialog after the notification is closed. 
- [oom] Align with Android OOM killer scores. 
- [lipstick-jolla] Fix silent ringtone detection. 
- [lipstick-jolla-home] Add support for basic mouse cursor. 
- [lipstick-jolla-home] Add support for basic mouse pointer. 
- [windowprompt] Unregister service first. 
- [tests] Remove absolute path for qmltestrunner. 
- [lipstick-jolla-home] Require explicit action to permanently hide sticky app grid hint. 
- [windowprompt] Implement queueing of windowprompts. 
### lipstick-jolla-home-qt5-l10n
- Updated : 1.423.2-1.6.1.jolla -- 1.428.2-1.8.1.jolla
- Binaries added : lipstick-jolla-home-qt5-l10n-lv - 1.428.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 262 of 262 strings translated (0 need review).
- [tpl] translation templates update for 1.24.16.2
- [tpl] translation templates update for 1.24.16.3
- [l10n] Commit from Jolla localisation: 262 of 262 strings translated (0 need review).
- [tpl] translation templates update for 1.24.12
- [l10n] Commit from Jolla localisation: 262 of 262 strings translated (0 need review).
- [tpl] translation templates update for 1.24.11
### lipstick-qt5
- Updated : 0.35.4-1.11.7.jolla -- 0.36.3.2-1.15.5.jolla
- [lipstick] Delete removed methods from AboutSettings stub. 
- [notificationmanager] Identify xdg-dbus-proxy clients. 
- [lipstick] Force reloading hidden launcher when file changes. 
- [touchscreen] Also mouse events terminate waiting for touch. 
- [lipstick] Map the right mouse key to the back-step action. 
- [lipstick] Emit application id for topmost window. 
### lipstick-qt5-l10n
- Updated : 1.103.1-1.5.1.jolla -- 1.103.3-1.6.1.jolla
- Binaries added : lipstick-qt5-l10n-lv - 1.103.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 16 of 16 strings translated (0 need review).
- [tpl] translation templates update for 0.36.3.1
- [l10n] Commit from Jolla localisation: 16 of 16 strings translated (0 need review).
### lipstick2vnc
- Updated : 0.9.12-1.2.1.jolla -- 0.9.14-1.4.82.jolla
- [lipstick2vnc] Move lipstick2vnc to user session. 
- [packaging] BuildRequire systemd via pkgconfig. 
- [vnc] Autostart service after installation package
- [vnc] Do not fail on post scripts.
### lua
- Updated : 5.3.5-1.5.1.jolla -- 5.3.5-1.7.1.jolla
- [lua] Fix loading of dynamic libraries. 
### lvm2
- Updated : 2.02.177+git4-1.5.1.jolla -- 2.02.177+git5-1.7.1.jolla
- [packaging] Use pkgconfig to require systemd-devel. 
### lxc
- Updated : 3.0.1+git4-1.4.3.jolla -- 4.0.10+git3-1.6.11.jolla
- Binaries removed : lxc-doc
- [packaging] BuildRequire systemd via pkgconfig. 
- [packaging] Remove mentions of init sysv and convert to bconds. 
- [lxc] Fix dependency on lxc-libs to match version. 
- [lxc] Update lxc to 4.0.10. 
### maliit-framework-wayland
- Updated : 0.99.1+git10-1.8.1.jolla -- 0.99.1+git11-1.9.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### mapplauncherd
- Updated : 4.2.9-1.9.3.jolla -- 4.2.11-1.10.12.jolla
- [mapplauncherd] Make connection handler less noisy. 
- [mapplauncherd] Sync exec validation from sailjail. 
### mapplauncherd-booster-browser
- Updated : 0.1.1-1.4.10.jolla -- 0.1.3-1.6.10.jolla
- [booster-browser] Cleanup Silica references. 
- [booster-browser] Update copyright years. 
- [packaging] Mark license with %license macro. 
- [rpm] Update repository url. 
- [booster-browser] Use correct Short Name for the license. 
### mapplauncherd-booster-firejail
- Updated : 0.0.4-1.5.6.jolla -- 0.0.5-1.6.14.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### mapplauncherd-qt5
- Updated : 1.1.20-1.7.6.jolla -- 1.1.21-1.8.15.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### mce
- Updated : 1.108.0-1.7.1.jolla -- 1.109.1-1.9.1.jolla
- [mce-dbus] Identify clients behind xdg-dbus-proxy
- [mce-dbus] Identify clients behind xdg-dbus-proxy. Fixes: 
- [build] Cleanup 64-bit compilation warnings
- [config] Do not hide sw keyboard when YubiKey is attached. 
- [dbus] Mouse availability signaling. 
- [event-input] Improvements to input device type configuration
- [packaging] Drop systemd BuildRequires. 
### mce-headers
- Updated : 1.28.3-1.4.1.jolla -- 1.29.0-1.6.1.jolla
- [mce] Add mouse availability state D-Bus constants. 
### meego-rpm-config
- Updated : 0.18-1.6.1.jolla -- 0.18-1.7.1.jolla
- [meego-rpm-config] Use correct Short Names for the license. 
- [macros] Refactor to use upstream macros. 
- [macros] Remove redundant %configure macro. 
### meson
- Updated : 0.59.0+git1-1.5.1.jolla -- 0.59.1+git1-1.6.2.jolla
- [meson] Update to version 0.59.1. 
### mkcal-qt5
- Updated : 0.5.47-1.12.1.jolla -- 0.5.50-1.13.1.jolla
- [mkcal] Remove version table. 
- [mkcal] Ensure that insertion pattern from ICalFormat::fromRawString() is working. 
- [mkcal] Rename sqlite api wrapper with its own names. 
### mlsdb-data-l10n
- Updated : 1.11.1-1.4.1.jolla -- 1.12.2-1.6.1.jolla
- Binaries added : mlsdb-data-l10n-lv - 1.12.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 12 of 12 strings translated (0 need review).
### mms-engine
- Updated : 1.0.77-1.4.1.jolla -- 1.0.78-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### mobile-broadband-provider-info
- Updated : 20131125+git76-1.4.1.jolla -- 20131125+git78-1.6.1.jolla
- [mbpi] Fix git submodule url.
- [mbpi] Remove Polish mobile network Cyfrowy Polsat
- [mbpi] Remove stale Polish mobile network. 
- [mbpi] Update Polish network Play
- [mbpi] Update Polish provider Play. 
### mpc
- Updated : 1.1.0+git1-1.5.1.jolla -- 1.1.0+git2-1.13.1.jolla
- [mpc] Fix git submodule url. 
### mpg123
- Updated : 1.25.11-1.5.1.jolla -- 1.25.11+git1-1.7.1.jolla
- [mpg123] Update CPU optimizations per architecture. 
- [packaging] Cleanup spec file
### ncurses
- Updated : 6.1+git2-1.5.1.jolla -- 6.1+git3-1.7.1.jolla
- [ncurses] Enable ABI6 and move ABI5 libs to a separte package. 
### nemo-password-manager
- Updated : 0.1.4-1.4.1.jolla -- 0.1.5-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### nemo-qml-plugin-calendar-qt5
- Updated : 0.6.21-1.8.6.jolla -- 0.6.26-1.10.17.jolla
- [nemo-qml-plugin-calendar] Update plugins.qmltypes. 
- [nemo-qml-plugin-calendar] Don't change the default notebook on import.
- [nemo-qml-plugin-calendar] Override existing events on import. 
- [nemo-qml-plugin-calendar] Simplify importation to memory code.
- [nemo-qml-plugin-calendar] Store in an occurrence if its correspondin?
- [nemo-qml-plugin-calendar] Store in an occurrence if its corresponding event is all day. 
- [nemo-qml-plugin-calendar] Add a list model for a set of given events. 
- [nemo-qml-plugin-calendar] Use instanceIdentifier to delegate EventQueries to the worker.
- [nemo-qml-plugin-calendar] Save the event when accepting the invitati?
- [nemo-qml-plugin-calendar] Save the event when accepting the invitation. 
### nemo-qml-plugin-configuration-qt5
- Updated : 0.2.3-1.5.1.jolla -- 0.2.5-1.7.2.jolla
- [nemo-qml-plugin-configuration] Migrate to sailfish-qdoc-template. 
- [nemo-qml-plugin-configuration] Remove absolute path for qmltestrunne?
- [nemo-qml-plugin-configuration] Remove absolute path for qmltestrunner. 
### nemo-qml-plugin-connectivity
- Updated : 0.2.8-1.5.1.jolla -- 0.2.10-1.6.1.jolla
- [connectivity] Do not connect to poweredChanged signal due to race. 
- [connectivity] Add support for ConnMan tech powered state update. 
### nemo-qml-plugin-contacts-qt5
- Updated : 0.3.20-1.10.1.jolla -- 0.3.21-1.12.1.jolla
- [nemo-qml-plugin-contacts] Update plugins.qmltypes. 
### nemo-qml-plugin-dbus-qt5
- Updated : 2.1.26-1.5.1.jolla -- 2.1.28-1.6.2.jolla
- [nemo-qml-plugin-dbus] Port to sailfish-qdoc-template. 
- [nemo-qml-plugin-dbus] Remove absolute path for qmltestrunner. 
### nemo-qml-plugin-devicelock
- Updated : 0.3.6-1.5.1.jolla -- 0.3.7-1.7.1.jolla
- [nemo-qml-plugin-devicelock] Provide an authentication service on the system bus. 
### nemo-qml-plugin-email-qt5
- Updated : 0.6.20-1.8.1.jolla -- 0.6.23-1.10.1.jolla
- [nemo-qml-plugin-email] Don't set URL in attachment list model if the file does not exist.
- [nemo-qml-plugin-email] Add license files and fix .spec license declarations. 
- [nemo-qml-plugin-email] Update plugins.qmltypes. 
### nemo-qml-plugin-email-qt5-offline
- Updated : 0.6.20-1.6.1.jolla -- 0.6.21-1.8.1.jolla
- [nemo-qml-plugin-email] Update plugins.qmltypes. 
### nemo-qml-plugin-filemanager
- Updated : 0.1.35-1.8.1.jolla -- 0.1.37-1.11.1.jolla
- [nemo-filemanager] Update plugins.qmltypes. 
- [nemo-qml-plugin-filemanager] Remove absolute path for qmltestrunner.
### nemo-qml-plugin-models-qt5
- Updated : 0.2.2-1.6.1.jolla -- 0.2.3-1.7.1.jolla
- [models] Remove absolute path for qmltestrunner. 
### nemo-qml-plugin-notifications-qt5
- Updated : 1.2.14-1.6.1.jolla -- 1.2.16-1.8.2.jolla
- [nemo-qml-plugin-notifications] Migrate to sailfish-qdoc-template. 
- [nemo-qml-plugin-notifications-qt5] Action inputs. 
### nemo-qml-plugin-systemsettings
- Updated : 0.5.77.2-1.9.2.jolla -- 0.5.90-1.10.7.jolla
- [external-storage] Add all valid block devices to map. 
- [external-storage] Mark block device as locked after 'encrypted-lock' is done. 
- [external-storage] Update partitions when a block is destroyed. 
- [partionmanager] Keep hintAuto state when morphing objects
- [partionmanager] Refactor after changes in Udisks2Monitor. 
- [partionmanager] Remove redundant checks for blocks being external. 
- [partionmanager] Replace isExternal with hintAuto
- [rpm] Bump up package version. 
- [sdcard] Clear formatting flag when new FileSystem interface is added. 
- [sdcard] Expose block devices only after each Block instance has completed. 
- [sdcard] Lookup created blocks when creating a new block. 
- [nemo-qml-plugin-systemsettings] Add license file. 
- [nemo-qml-plugin-systemsettings] Remove storage info api from AboutSettings. 
- [nemo-qml-plugin-systemsettings] Get application permissions from sailjail. 
- [nemo-qml-plugin-systemsettings] Fix partition model not getting memory card entry. 
- [nemo-qml-plugin-systemsettings] Require nemodbus from pc & devel package. 
- [nemo-qml-plugin-systemsettings] Cleanup unimplemented Finished slots from user model. 
- [nemo-qml-plugin-systemsettings] Use NemoDBus::Interface rather than QDBusInterface. 
- [nemo-qml-plugin-systemsettings] Move the tests under /opt/tests/. 
- [nemo-qml-plugin-systemsettings] Migrate location.conf from old path. 
- [nemo-qml-plugin-systemsettings] Move location config to /var. 
- [nemo-systemsettings] Add preferred language support. 
- [nemo-qml-plugin-systemsettings] Abort mount/unmount operations when device is busy. 
- [nemo-qml-plugin-systemsettings] Abort mount/unmount operation when device is busy. 
### nemo-qml-plugin-systemsettings-l10n
- Updated : 1.16.2-1.8.1.jolla -- 1.17.2-1.10.1.jolla
- Binaries added : nemo-qml-plugin-systemsettings-l10n-lv - 1.17.2-1.10.1.jolla
- [l10n] Commit from Jolla localisation: 3 of 3 strings translated (0 need review).
- [tpl] translation templates update for 0.5.90
- [l10n] Commit from Jolla localisation: 3 of 3 strings translated (0 need review).
- [tpl] translation templates update for 0.5.79
### nemo-qml-plugin-thumbnailer-qt5
- Updated : 1.0.4-1.4.1.jolla -- 1.0.5-1.6.2.jolla
- [nemo-thumbnailer] Migrate to sailfish-qdoc-template. 
### nemo-transferengine-qt5
- Updated : 1.0.13-1.8.1.jolla -- 2.0.0-1.10.2.jolla
- [transferengine] Split transfer and sharing plugins. 
- [packaging] BuildRequire systemd via pkgconfig. 
- [transfer-engine] fix example qml
### nemo-transferengine-qt5-l10n
- Updated : 1.63.1-1.5.1.jolla -- 1.66.2-1.8.1.jolla
- Binaries added : nemo-transferengine-qt5-l10n-lv - 1.66.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 10 of 10 strings translated (0 need review).
- [tpl] translation templates update for 2.0.0
- [l10n] Commit from Jolla localisation: 10 of 10 strings translated (0 need review).
### nfcd
- Updated : 1.1.6-1.7.1.jolla -- 1.1.7-1.8.1.jolla
- [core] Print plugin directory to debug log. 
- [dbus] Added glib annotation for DatagramReceived. 
- [dbus] Handle graceful rejection of LLC connection. 
### ngfd
- Updated : 1.3.0-1.5.1.jolla -- 1.3.1-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### ngfd-plugin-droid-vibrator
- Updated : 1.2.2-1.2.1.jolla -- 1.3.0-1.3.1.jolla
- [droid-vibrator] Add haptic.duration support. 
- [droid-vibrator] Add values for QtFeedback effects
### nss
- Updated : 3.58+git1-1.6.3.jolla -- 3.73.1+git1-1.8.8.jolla
- [git] Move submodule repos to github. 
- [nss] Update to 3.73.1. 
### ofono
- Updated : 1.23+git35-1.10.1.jolla -- 1.28+git3.1-1.12.1.jolla
- [dbus-access] Added access control entry for SendDataMessage. 
- [ofono] Added API for querying IMEI from the modem. 
- [sms] Add support for sending SMS data messages. 
- [sms] Support setting endianess for SMS data messages. 
- [voicecall] Allow filtering for emergency calls. 
- [ims] Expose ext_info bits to the plugins. 
- [ofono] Add ofono_ussd_decode and ofono_ussd_decode_free API. 
- [ofono] Updated baseline to 1.28. 
- [ofono] Housekeeping
- [voicecall] Added ofono_voicecall_is_emergency_number() API. 
- [ofono] Fixed re-evaluation of data slot after SIM change. 
- [unit] Added one more slot-manager test case
- [ofono] Update baseline to 1.27. 
- [include] Updated enum ofono_gprs_auth_method. 
- [ofono] Fixed a few compilation warnings
- [ofono] Handle OFONO_GPRS_AUTH_METHOD_ANY. 
- [ofono] Updated baseline to 1.26
- [packaging] Detect rpm version at build time. 
- [unit] Avoid using g_key_file_save_to_file
- [plugins] Add ofono_cell_info based NetMon driver. 
- [plugins] Add generic phonebook plugin. 
- [include] Added ofono_slot_remove_all_handlers macro. 
- [include] Defined enum ofono_call_mode. 
- [include] Define struct modem in types.h
- [ofono] Pulled in a bug fix from upstream. 
- [ofono] Bump libglibutil requirement
- [packaging] BuildRequire systemd via pkgconfig. 
- [radio-settings] Removed unreachable code
- [ofono] Expose modem watch API to plugins. 
- [ofono] Update baseline to 1.25. 
- [plugin] Disabled OFONO_API_SUBJECT_TO_CHANGE check in plugin.h
- [ofono] Do not require non-critical packages. 
- [ofono] Added debug trace
- [ofono] Fixed a problem with D-Bus signal not being emitted. 
- [unit] Added back test-conf
- [unit] Fixed coverage script
- [unit] Test DefaultDataModemChanged signal. 
- [ofono] Replace built-in ril plugin with the external one. 
- [ril] Fix double-free. 
- [ofono] Make more APIs available to external plugins. 
- [ofono] Update baseline to 1.24. 
### ofono-alien-binder-plugin
- Updated : 0.1.5-1.2.3.jolla -- 0.1.5.1-1.3.2.jolla
- [ofono-alien] Always register alien services with hwpuddlejumper. 
### ofono-ril-binder-plugin
- Updated : 1.2.5-1.3.1.jolla -- 1.2.6-1.4.2.jolla
- [rilbinder] Require ofono-ril-plugin. 
ofono-ril-plugin
Reverted : 1.23+git35-1.10.1.jolla -- 1.0.2-1.2.2.jolla
- Binaries added : ofono-ril-plugin - 1.0.2-1.2.2.jolla
- [build] Fixed a problem with STRIP not being defined. 
- [ofono-ril] Package sample ril_subscription.conf. 
- [ofono-ril] Legacy RIL plugin. 
### ohm-plugins-misc
- Updated : 1.7.1-1.7.1.jolla -- 1.8.0-1.8.1.jolla
- [media] Adapt to using application id. 
- [notification] Adapt to using application id. 
- [resource] Adapt to using application id. 
- [telephony] Adapt to using application id. 
### oneshot
- Updated : 0.6.9-1.5.1.jolla -- 0.6.11-1.6.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
- [oneshot] Provide SessionBus address for user scripts. 
### openfortivpn
- Updated : 1.17.0+git1-1.7.1.jolla -- 1.17.1+git1-1.8.1.jolla
- [openfortivpn] Upgrade to version 1.17.1. 
### openssh
- Updated : 8.0p1+git12-1.6.3.jolla -- 8.8p1+git1-1.9.3.jolla
- [git] Move submodule repos to github. 
- [openssh] Update to 8.8p1. 
- [packaging] BuildRequire systemd via pkgconfig. 
### openvpn
- Updated : 2.5.2+git2-1.8.3.jolla -- 2.5.2+git3-1.9.9.jolla
- [openvpn] Update upstream submodule path. 
### p11-kit
- Updated : 0.23.20+git2-1.5.1.jolla -- 0.23.22+git1-1.7.1.jolla
- [git] Move submodule repos to github. 
- [p11-kit] Fix CVE-2020-29361. 
- [p11-kit] Fix CVE-2020-29362. 
- [p11-kit] Fix CVE-2020-29363. 
- [p11-kit] Upgrade to 0.23.22. 
### p7zip
- Updated : 16.02+git1-1.3.1.jolla -- 16.02+git3-1.4.1.jolla
- [p7zip] Remove + from License tag. 
- [p7zip] Use correct Short Name for the license. 
### pam
- Updated : 1.3.1+git1-1.5.1.jolla -- 1.3.1+git2-1.7.1.jolla
- [pam] Explicitly depend on pkgconfig(libcrypt). 
### partnerspace-launcher
- Updated : 0.1.4-1.2.1.jolla -- 0.1.5-1.3.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### patterns-sailfish
- Updated : 1.1.1-1.4.1.jolla -- 1.1.6+git1-1.7.1.jolla
- [patterns] Add sailfish-aml to cellular apps section. 
- [patterns] Recommend gnu-cpio. 
- [patterns-non-oss] Replace mer-qdoc-template with sailfish variant. 
- [patterns] Clean up qa-tools pattern. 
- [patterns] Move some more rarely needed content from qt5-devel-basic to qt5-devel-full. 
- [patterns] Remove qtpublishsubscribe and serviceframework from basic patterns. 
### perl
- Updated : 0.76-1.6.5.jolla -- 0.76-1.7.16.jolla
- [perl] Require pkgconfig(libcrypt) in -devel package. 
- Add missing patch file.
- [perl] fix build failure with recent glibc or libxcrypt. 
- [perl] Fix typo. 
- [perl] Explicitly depend on pkgconfig(libcrypt). 
### pj-oss-project-config
- Updated : 0.0.14-1.5.1.jolla -- 0.0.20-1.8.1.jolla
- [prjconf] Make pulling in cross compilers for rust less heavy for all other i586 builds. 
- [prjconf] Preinstall libzstd as it is required by rpm now. 
- [prjconf] Preinstall libxcrypt by default. 
- [prjconf] Replace busybox-symlinks-which with which and prefer. 
- [prjconf] Enable systemd-mini and document. 
- [prjconf] Document libxcrypt transition. 
- [prjconf] Preinstall libxcrypt-compat. 
- [prjconf] Allow for Ncurses ABI5 -> ABI6 transition. 
- [prjconf] Preinstall ncurses-libs5 to allow for rebuild. 
### policy-settings-common
- Updated : 0.11.2-1.6.3.jolla -- 0.12.1-1.8.12.jolla
- [common] Fix volume control when appsupport is not in use. 
- [common] Use application id for media state. 
### polkit-qt-1
- Updated : 0.99.1+git1-1.4.1.jolla -- 0.99.1+git2-1.6.1.jolla
- [packaging] Fix license tag. 
- [packaging] Remove unsused RPM Groups
- [polkit-qt-1] Dont require removed polkit-qt-gui in pkgconf. 
### ppp
- Updated : 2.4.9+git1-1.6.1.jolla -- 2.4.9+git2-1.7.1.jolla
- [ppp] Explicitly depend on pkgconfig(libcrypt). 
### protobuf
- Updated : 3.14.0+git1-1.5.1.jolla -- 3.18.0+git1-1.7.1.jolla
- [protobuf] Update protobuf to 3.18.0. 
### provisioning-service
- Updated : 0.1.6-1.5.1.jolla -- 0.1.7-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### pulseaudio
- Updated : 14.2+git4-1.7.1.jolla -- 14.2+git6-1.8.1.jolla
- [sailfish] BuildRequire systemd via pkgconfig. 
- [sailfish] Add policy application id for all clients. 
### pulseaudio-modules-droid
- Updated : 14.2.92-1.3.1.jolla -- 14.2.97-1.3.1.jolla
- [common] Enable audio_cal_wait properly. 
- [pulseaudio-modules-droid] Update implementation for Android 11. 
- [common] Handle profiles with no supported channels
- [common] New API for calling HAL functions. 
- [common] Use more generic stream property for audio source. 
- [common] Add generic converter for fancy audio sources.
- [common] Allow custom audio source based on property. 
- [common] Fix segfault with adaptations which assume empty adress is not NULL. 
- [source] Use source-output proplist when reconfiguring input stream. 
### pulseaudio-modules-droid-hidl
- Updated : 1.3.1-1.2.1.jolla -- 1.4.0-1.3.1.jolla
- [module] Use new API from pulsecore shared. 
- [packaging] Drop build requirement for libdroid-util.
### pulseaudio-policy-enforcement
- Updated : 14.2.44-1.4.1.jolla -- 14.2.45-1.6.1.jolla
- [policy-enforcement] Use application id to identify streams. 
### python
- Updated : 2.7.17+git6-1.4.2.jolla -- 2.7.17+git7-1.6.1.jolla
- [python] Explicitly depend on pkgconfig(libcrypt). 
### python3-base
- Updated : 3.8.11+git2-1.6.6.jolla -- 3.8.11+git3-1.7.15.jolla
- [python3] Explicitly depend on pkgconfig(libcrypt). 
### python3-extra
- Updated : 3.8.11+git2-1.6.1.jolla -- 3.8.11+git3-1.7.1.jolla
- [python3] Explicitly depend on pkgconfig(libcrypt). 
### python3-imaging
- Updated : 8.0.1+git1-1.4.1.jolla -- 9.0.0+git1-1.5.1.jolla
- [python3-imaging] Update to version 9.0.0. 
### python3-lxml
- Updated : 4.6.3+git1-1.6.1.jolla -- 4.6.5+git1-1.8.1.jolla
- [git] Move submodule repos to github. 
- [python3-lxml] Update submodule to 4.6.5. 
### qmf-eas-plugin-l10n
- Updated : 1.109.1-1.5.1.jolla -- 1.110.2-1.7.1.jolla
- Binaries added : qmf-eas-plugin-l10n-lv - 1.110.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 106 of 106 strings translated (0 need review).
### qmf-notifications-plugin-l10n
- Updated : 1.58.1-1.8.1.jolla -- 1.59.2-1.10.1.jolla
- Binaries added : qmf-notifications-plugin-l10n-lv - 1.59.2-1.10.1.jolla
- [l10n] Commit from Jolla localisation: 8 of 8 strings translated (0 need review).
### qmf-qt5
- Updated : 4.0.4+git134-1.8.1.jolla -- 4.0.4+git135-1.8.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### qt5
- Updated : 5.6.3+git45-1.13.1.jolla -- 5.6.3+git46.1-1.16.2.jolla
- [qtbase] Enable libproxy support. 
- [qtbase] Support VPN connection reset case in state change. 
### qt5-plugin-generic-vboxtouch
- Updated : 1.1.10-1.2.1.jolla -- 1.1.12-1.4.1.jolla
- [lipstick] Fix user switching. 
- [qt5-plugin-vboxtouch] Use correct Short Name for the license. 
### qt5-qpa-hwcomposer-plugin
- Updated : 5.6.2.18-1.2.1.jolla -- 5.6.2.20-1.3.1.jolla
- [hwcomposer] Fix loading hwcomposer on devices with hwc2 headers but no hwc2 support. 
- [hwcomposer] Do not load hardware module on hwc2 devices. 
- [hwcomposer] Silence some build warnings and cleanup formatting.
### qt5-qtconnectivity
- Updated : 5.6.2+git2-1.4.1.jolla -- 5.6.2+git3-1.6.1.jolla
- [qtbluetooth] Use correct Short Names for the license. 
### qt5-qtdeclarative
- Updated : 5.6.3+git19-1.5.1.jolla -- 5.6.3+git21-1.8.1.jolla
- [qtdeclarative] Don't assume DST is +1 hour
- [qtdeclarative] Fix timezone handling for e.g. Ireland. 
- [qtdeclarative] Bump version. 
### qt5-qtmultimedia
- Updated : 5.6.2+git29-1.11.1.jolla -- 5.6.2+git31-1.12.1.jolla
- [camera] Fix checking for supported color filters. Fix memory leaks. 
- [camera] Fix checking for supported color filters. 
- [camera] Apply audio source property to PulseAudio sources. 
### qtmozembed-qt5
- Updated : 1.52.27-1.17.9.jolla -- 1.53.20-1.31.5.jolla
- [qtmozembed] Use logging category for QMozSecurity. 
- [qtmozembed] Cleanup wrong initialization order. 
- [qtmozembed] Fix some valgrind reports.
- [qtmozembed] Fix some valgrind reports. 
- [qtmozembed] Fix text input with xt9. 
- [qtmozembed] Include license file. 
- [qtmozembed] Bring back previous setPreference and overload it. 
- [qtmozembed] httpUserAgent test fix. 
- [qtmozembed] Add preference type to the setPreference. 
- [qtmozembed] Add common TestWindow for unit tests. 
- [qtmozembed] Add wait for test case cleanup. 
- [qtmozembed] Automated tests fix. 
- [qtmozembed] Destroy all created view in tst_newviewrequest. 
- [qtmozembed] Increase length of basic scroll test. 
- [qtmozembed] Take parentBrowsingContext into use for tst_newwindowrequest. 
- [qtmozembed] Add setter for parent browsing context. 
- [qtmozembed] Pass parent browsing context through from view creator. 
- [qtmozembed] Mark load start to 15%. 
- [qtmozembed] Reload requested url if stop requested before url resolved. 
- [qtmozemebed] Make none resolved url visible. 
- [qtmozembed] Add change signal for the resolution property. 
- [qtmozembed] Cleanup unit tests a bit. 
- [qtmozembed] Default to an empty json response in RecvSyncMessage. 
- [qtmozembed] Drop rootScrollFrame argument. 
- [qtmozembed] Handle "off" values of autocomplete and autocapitalize attributes. 
- [qtmozembed] Take screen primary orientation into account when rotating mozilla window. 
- [qtmozembed] Change resetPainted as generic reset. 
- [qtmozembed] Mark dynamic toolbar height dirty on reset. 
- [qtmozembed] Move goBack, goForward, stop, and reload to private class. 
- [qtmozembed] Reset domContentLoaded during reset. 
- [qtmozembed] Send screen properties. 
- [qtmozembed] Add domContentLoaded property and signal. 
- [qtmozembed] Clear dirty dynamic toolbar after 'DOMContentLoaded'. 
- [qtmozembed] Avoid stretching the QuickMozView content when the item and texture size differ. 
- [qtmozembed] Implement QuickMozView::dynamicToolbarHeight. 
- [qtmozembed] Fix corruption of requested oversized thumbnails. 
- [qtmozembed] Cleanup drawUnderlay. 
- [qtmozembed] Drop rendering guards until engine statuses are reported correctly. 
- [qtmozembed] Emit drawOverlay from CompositingFinished. 
- [qtmozembed] Ignore spurious location changes to about:blank. 
- [qtmozembed] Remove unnecessary header includes. 
- [qtmozembed] Replace nsISSLStatus usage with nsITransportSecurityInfo. 
- [qtmozembed] Update TLS_VERSION enum. 
- [qtmozembed] Use appropriate state values from nsIWebProgressListener. 
- [qtmozembed] Cleanup drawUnderlay. 
- [qtmozembed] Drop rendering guards until engine statuses are reported correctly. 
- [qtmozembed] Emit drawOverlay from CompositingFinished. 
- [qtmozembed] Ignore spurious location changes to about:blank. 
- [qtmozembed] Remove unnecessary header includes. 
- [qtmozembed] Replace nsISSLStatus usage with nsITransportSecurityInfo. 
- [qtmozembed] Update TLS_VERSION enum. 
- [qtmozembed] Use appropriate state values from nsIWebProgressListener. 
- [qtmozembed] Provide a separate method for setting toolbar height. 
- [qtmozembed] Remove sending the overlapped by keyboard area height. 
- [qtmozembed] Add doNotTrack global setting property to WebEngineSettings. 
- [qtmozembed] Introduce predictive text input support. 
- [qtmozembed] Pass replacement start and length to embedlite text event handler. 
- [qtmozembed] Provide ImSurroundingText, ImCursorPosition and ImAnchorPosition values for predictive text input. 
- [qtmozembed] Asynchronous destruction of QMozWindow. 
- [qtmozembed] Move EmbedLiteApp::CreateWindow call to a separate method. 
- [qtmozembed] Provide an ability to recreate EmbedLiteApp window. 
- [qtmozembed] Provide an interface for getting the number of embedlite views and windows. 
- [qtmozembed] Always pass charCode with keyevent. 
### rpm
- Updated : 4.16.1.3+git4-1.8.1.jolla -- 4.16.1.3+git8-1.10.1.jolla
- [rpm] Add zstd support. 
- [rpm] Drop support for so.8 libraries. 
- [rpm-python] Add missing patch to spec. 
- [rpm] Pass the target platform to configure again. 
### rpm-python
- Updated : 4.16.1.3+git4-1.8.4.jolla -- 4.16.1.3+git8-1.10.11.jolla
- [rpm] Add zstd support. 
- [rpm] Drop support for so.8 libraries. 
- [rpm-python] Add missing patch to spec. 
- [rpm] Pass the target platform to configure again. 
### rpmlint
- Updated : 2.0.0+git1-1.5.3.jolla -- 2.0.0+git2-1.6.11.jolla
- [rpmlint] Require gnu-cpio. 
### rust
- Updated : 1.52.1+git1-1.7.1.jolla -- 1.52.1+git1-1.7.2.jolla
- Add wrapper for host-gcc used as a host-compatible linker by rustc. 
- Provide default std-static from correct package. 
- Cross package binaries built by rust. 
### sailfish-access-control
- Updated : 0.0.5-1.5.1.jolla -- 0.0.6-1.7.1.jolla
- [sailfish-access-control] Add plugins.qmltypes. 
### sailfish-access-control-qt5
- Updated : 0.0.5-1.5.1.jolla -- 0.0.6-1.7.1.jolla
- [sailfish-access-control] Add plugins.qmltypes. 
### sailfish-account-nextcloud
- Updated : 0.2.5-1.4.1.jolla -- 1.0.0-1.5.1.jolla
- [transferengine-plugins] Split sharing and transfer plugins. 
### sailfish-account-nextcloud-l10n
- Updated : 1.21.1-1.5.1.jolla -- 1.22.2-1.7.1.jolla
- Binaries added : sailfish-account-nextcloud-l10n-lv - 1.22.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 5 of 5 strings translated (0 need review).
### sailfish-archive-l10n
- Updated : 1.18.3-1.3.1.jolla -- 1.18.5-1.4.1.jolla
- Binaries added : sailfish-archive-l10n-lv - 1.18.5-1.4.1.jolla
- [l10n] Commit from Jolla localisation: 7 of 7 strings translated (0 need review).
### sailfish-audiorecorder
- Updated : 0.1.7-1.3.1.jolla -- 0.1.8-1.4.1.jolla
- [audiorecorder] Remove unneeded Sharing permission. 
### sailfish-audiorecorder-l10n
- Updated : 1.20.1-1.5.1.jolla -- 1.21.2-1.6.1.jolla
- Binaries added : sailfish-audiorecorder-l10n-lv - 1.21.2-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 30 of 30 strings translated (0 need review).
### sailfish-browser
- Updated : 2.1.44.1-1.5.1.jolla -- 2.2.38.4-1.25.1.jolla
- [browser] Cleanup general.useragent.override from preferences. 
- [browser] Fix popup input region. 
- [browser] After closing the active shift new active tab index. 
- [browser] Explicitly state Camera permission. 
- [browser] Make it possible to configure max live tab count via setting. 
- [browser] Support touch events when selection active. 
- [browser] Add anchor element test case for context menu with text. 
- [browser] Add memory leak test pages. 
- [browser] RFC: Bring back the close button in the toolbar. 
- [browser] Activate previously used tab when closing the active tab. 
- [browser] Activate recently used tab when closing the active tab. 
- [browser] Add svg rendering test case. 
- [browser] Show back button to close a child tab. 
- [browser] Take new icon-m-back-tab into use for back button. 
- [browser] Check unique id from WebPageEntry instead of live page. 
- [browser] Cleanup obsoleted parentTabId in favour of findTabId. 
- [browser] Use findTabId to find parent tab. 
- [browser] Clean tabs in reboot fix. 
- [browser] Clean tabs in reboot. 
- [browser] Lookup parentId when mapping parentId to tabId. 
- [browser] Fix painting of pages loaded with pushState. 
- [browser] Switch license file to .txt, and include in rpm. 
- [browser] Add ability of using cutout API. 
- [browser] Add double tap handler and tap-to-zoom test case. 
- [browser] Add test case for opening tel uri into a new tab. 
- [browser] Pass preference type argument when setting a pref. 
- [browser] Let QGuiApplication to synthesize touch for unhandled mouse events. 
- [browser] Pass back browsing context when web content requested new window. 
- [browser] Request new tab (page) before adding to the model. 
- [browser] Add test case for target="_blank" download triggering. 
- [sailfish-browser] Fix error reading tab thumbnails from cache. 
- [browser] Create new requested tab immediately. 
- [browser] Fix tst_persistenttabmodel unit tests. 
- [browser] Fix tst_webview unit tests. 
- [browser] Handle external urls immediately when seen. 
- [browser] Make tst_dbmanager unit tests to pass. 
- [browser] Remove opaqueBackground property. 
- [browser] Remove waitingForNewTab property. 
- [browser] Render page upon activation if already loaded. 
- [browser] Request url update test case for tst_dbmanager. 
- [browser] Test requested external url against previous requested and resolved url. 
- [sailfish-browser] Emulate touch events when mouse events come to the browser window. 
- [sailfish-browser] Improve text input test. 
- [sailfish-browser] Move primary orientation handling to qmozwindow. 
- [sailfish-browser] Fix CertificateInfo warning about undefined url. 
- [sailfish-browser] Add confirm dialog of clearing browser data. 
- [sailfish-browser] Follow screen primary orientation when rotating the web window. 
- [sailfish-browser] Take primary screen orientation into account in the overlay input mask. 
- [ua] Cleanup obsoloted user-agent overrides. 
- [ua] Cleanup user-agent overrides that matches to default. 
- [ua] Drop ask.com user-agent override. 
- [ua] Drop hymy.fi and alibi.fi user-agent overrides. 
- [ua] Drop thomann.de user-agent override. 
- [ua] Drop verkkokauppa.com user-agent override. 
- [user-agent] Update preprocessed user agent overrides
- [sailfish-browser] Add ability of calculating cache and site data size. 
- [sailfish-browser] Replace clearing of "cookie" with "cookie and site data" in PrivacySettingsPage. 
- [sailfish-browser] Replace clearing of "cookie" with "cookie and site data". 
- [browser] Be a bit more aggresive on lowering toolbar. 
- [sailfish-browser] Keep the device awake during WebRTC calls. 
- [browser] Update browser cover on tab changes. 
- [browser] Remove SettingManager initialisation. 
- [tests] Add test page for javascript log output. 
- [tests] ServiceWorkers test. 
- [browser] Cleanup domContentLoaded property and signal. 
- [browser] Add history erasing within periods. 
- [sailfish-browser] Fix corrupted tab view icons. 
- [tests] Add fixed bottom toolbar to testmarginbottom.html. 
- [tests] Raise arrow on testmarginbottom higher on z-index. 
- [sailfish-browser] Fix invalid thumbnail sizes for tabs being requested. 
- [browser] Fix active tab flickering. 
- [sailfish-browser] Add manual test for storage. 
- [browser] Cleanup drawUnderlay. 
- [browser] Update update-agent override url for newer engine. 
- [sailfish-browser] Fix ClickEventBlocker loading for esr78. 
- [ua] Adapt to 78.0 user-agent. 
- [ua] Add 78.0 overrides. 
- [ua] elpais.com.co loads mobile fine without additional ua changes. 
- [ua] facebook.com loads good mobile page without ua override. 
- [ua] Update 78.0 user-agent overrides.
- [user-agent] Update preprocessed user agent overrides
- [browser] Cleanup drawUnderlay. 
- [browser] Update update-agent override url for newer engine. 
- [ua] Adapt to 78.0 user-agent. 
- [ua] Add 78.0 overrides. 
- [ua] elpais.com.co loads mobile fine without additional ua changes. 
- [ua] facebook.com loads good mobile page without ua override. 
- [ua] Update 78.0 user-agent overrides.
- [user-agent] Update preprocessed user agent overrides
- [browser] Cleanup drawUnderlay. 
- [browser] Update update-agent override url for newer engine. 
- [ua] Adapt to 78.0 user-agent. 
- [ua] Add 78.0 overrides. 
- [ua] elpais.com.co loads mobile fine without additional ua changes. 
- [ua] facebook.com loads good mobile page without ua override. 
- [user-agent] Update preprocessed user agent overrides
- [user-agent] Update user agent override for zoom.us. 
- [user-agent] User agent override for trueconf.com. 
- [sailfish-browser] Improve bottom margin test page. 
- [sailfish-browser] Use setDynamicToolbarHeight to set the toolbar height. 
- [sailfish-browser] Fix browser termination when all downloads are completed. Fixes to 
- [ua] Update esr60 user-agent overrides. 
- [ua] Add 78.0 overrides. 
- [user-agent] User agent override for mosreg.ru. 
- [ua] Add 78.0 overrides. 
- [browser] Add remove all permissions to PrivacySettingsPage. 
- [browser] Make SettingsManager refactoring. 
- [sailfish-browser] Fix adding link to bookmarks if opening history page via popup menu. 
- [browser] Fix active tab display when opening tabs. 
- [browser] Use combobox also for save destination. 
- [user-agent] User agent override for omp.ru. 
- [saifish-browser] Use connectivity to establish online status. 
- [user-agent] User agent override for mail.ru. 
- [sailfish-browser] Asynchronous destruction of QMozWindow. 
- [sailfish-browser] Create embedlite window after all QMozWindow signals are connected. 
- [sailfish-browser] Move CloseEventFilter to DeclarativeWebContainer. 
- [sailfish-browser] Post clearWindowSurfaceTask on QMozWindow::compositorCreated event. 
- [sailfish-browser] Prevent browser from being stuck if engine doesn't call lastWindowDestroyed. 
- [sailfish-browser] Recreate browser window from existing process on browser launch. 
- [sailfish-browser] Add text input test page. 
- [browser] Fix accessing the security code prompt from within a sandbox. 
- [sailfish-browser] Remove unneeded Sharing permission. 
- [browser] Rename home page dialog's web site address to web page address. 
- [browser] Do not reset model upon a tab close. 
### sailfish-browser-l10n
- Updated : 1.253.2-1.7.1.jolla -- 1.262.8-1.15.1.jolla
- Binaries added : sailfish-browser-l10n-lv - 1.262.8-1.15.1.jolla
- [l10n] Commit from Jolla localisation: 162 of 162 strings translated (0 need review).
- [tpl] translation templates update for 2.2.38.1
- [l10n] Commit from Jolla localisation: 162 of 162 strings translated (0 need review).
- [tpl] translation templates update for 2.2.35
- [tpl] translation templates update for 2.2.36
- [l10n] Commit from Jolla localisation: 161 of 161 strings translated (0 need review).
- [tpl] translation templates update for 2.2.21
- [tpl] translation templates update for 2.2.25
- [tpl] translation templates update for 2.2.26
- [l10n] Commit from Jolla localisation: 160 of 160 strings translated (0 need review).
- [tpl] translation templates update for 2.2.17
- [l10n] Commit from Jolla localisation: 148 of 148 strings translated (0 need review).
- [tpl] translation templates update for 2.2.14
- [l10n] Commit from Jolla localisation: 148 of 148 strings translated (0 need review).
- [tpl] translation templates update for 2.2.11
- [l10n] Commit from Jolla localisation: 148 of 148 strings translated (0 need review).
- [tpl] translation templates update for 2.2.6
- [tpl] translation templates update for 2.2.7
- [l10n] Commit from Jolla localisation: 143 of 143 strings translated (0 need review).
- [tpl] translation templates update for 2.1.55
- [tpl] translation templates update for 2.1.54
- [l10n] Commit from Jolla localisation: 142 of 142 strings translated (0 need review).
- [tpl] translation templates update for 2.1.48
- [tpl] translation templates update for 2.1.53
- [l10n] Commit from Jolla localisation: 142 of 142 strings translated (0 need review).
- [tpl] translation templates update for 2.1.46
### sailfish-btrfs-balancer-l10n
- Updated : 1.24.4-1.3.1.jolla -- 1.24.6-1.4.1.jolla
- Binaries added : sailfish-btrfs-balancer-l10n-lv - 1.24.6-1.4.1.jolla
- [l10n] Commit from Jolla localisation: 5 of 5 strings translated (0 need review).
### sailfish-ca
- Updated : 0.1.1-1.2.1.jolla -- 0.2-1.3.1.jolla
- [sailfish-ca] Add new CA certificates 
### sailfish-components-accounts-qt5
- Updated : 0.2.54-1.4.1.jolla -- 0.2.55-1.5.2.jolla
- [components-accounts] Remove unnecessary qtopengl dependency. 
### sailfish-components-accounts-qt5-l10n
- Updated : 1.121.1-1.5.1.jolla -- 1.122.2-1.7.1.jolla
- Binaries added : sailfish-components-accounts-qt5-l10n-lv - 1.122.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 55 of 55 strings translated (0 need review).
### sailfish-components-bluetooth-qt5
- Updated : 0.2.18-1.3.1.jolla -- 0.2.19-1.4.1.jolla
- [bluetooth] Remove absolute path for qmltestrunner. 
### sailfish-components-bluetooth-qt5-l10n
- Updated : 1.92.1-1.5.1.jolla -- 1.92.3-1.6.1.jolla
- Binaries added : sailfish-components-bluetooth-qt5-l10n-lv - 1.92.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 39 of 39 strings translated (0 need review).
### sailfish-components-contacts-qt5
- Updated : 0.4.36-1.4.1.jolla -- 0.4.37-1.5.1.jolla
- [components-contacts] Remove unnecessary qtopengl build requirement. 
### sailfish-components-contacts-qt5-l10n
- Updated : 1.196.1-1.5.1.jolla -- 1.198.2-1.7.1.jolla
- Binaries added : sailfish-components-contacts-qt5-l10n-lv - 1.198.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 159 of 159 strings translated (0 need review).
### sailfish-components-filemanager-l10n
- Updated : 1.99.1-1.5.1.jolla -- 1.99.4-1.7.1.jolla
- Binaries added : sailfish-components-filemanager-l10n-lv - 1.99.4-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 65 of 65 strings translated (0 need review).
### sailfish-components-gallery-qt5
- Updated : 1.2.0-1.4.1.jolla -- 1.2.3-1.7.1.jolla
- [components-gallery] Fix sharing local but not public files. 
- [gallery] Introduce draggable scrollbar. 
- [gallery] Use GridItem in Gallery. 
- [components-gallery] Remove unnecessary opengl dependency. 
### sailfish-components-gallery-qt5-l10n
- Updated : 1.157.1-1.5.1.jolla -- 1.158.2-1.7.1.jolla
- Binaries added : sailfish-components-gallery-qt5-l10n-lv - 1.158.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 54 of 54 strings translated (0 need review).
- [tpl] translation templates update for 1.2.2
### sailfish-components-pickers-qt5
- Updated : 1.0.17-1.4.1.jolla -- 1.0.21-1.6.2.jolla
- [components-pickers] Adapt to Sailfish.Gallery refactorings. 
- [components-pickers] Migrate to sailfish-qdoc-template. 
- [components-pickers] Remove unnecessary qtopengl build requirement. 
- [components-pickers] Remove absolute path for qmltestrunner. 
### sailfish-components-pickers-qt5-l10n
- Updated : 1.101.1-1.5.1.jolla -- 1.103.2-1.8.1.jolla
- Binaries added : sailfish-components-pickers-qt5-l10n-lv - 1.103.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
- [tpl] translation templates update for 1.0.21
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
### sailfish-components-telephony-qt5-l10n
- Updated : 1.37.2-1.4.1.jolla -- 1.37.4-1.5.1.jolla
- Binaries added : sailfish-components-telephony-qt5-l10n-lv - 1.37.4-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 14 of 14 strings translated (0 need review).
### sailfish-components-timezone-qt5
- Updated : 0.2.0-1.2.8.jolla -- 0.2.1-1.3.19.jolla
- [sailfish-components-timezone] Remove absolute path for qmltestrunner. 
### sailfish-components-timezone-qt5-l10n
- Updated : 1.95.1-1.6.1.jolla -- 1.99.3-1.10.1.jolla
- Binaries added : sailfish-components-timezone-qt5-l10n-lv - 1.99.3-1.10.1.jolla
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.1
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.1
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.1
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.1
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.1
- [l10n] Commit from Jolla localisation: 693 of 693 strings translated (0 need review).
- [tpl] translation templates update for 0.2.0
- [tpl] translation templates update for 0.2.1
### sailfish-components-weather-qt5-l10n
- Updated : 1.64.1-1.4.1.jolla -- 1.64.3-1.5.1.jolla
- Binaries added : sailfish-components-weather-qt5-l10n-lv - 1.64.3-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 72 of 72 strings translated (0 need review).
### sailfish-components-webview-qt5
- Updated : 1.3.13-1.8.1.jolla -- 1.5.9-1.19.1.jolla
- Binaries removed : sailfish-components-webview-qt5-pickers-ts-devel, sailfish-components-webview-qt5-popups-ts-devel
- [components-webview] Fix click handling after selection. 
- [webview-popups] Allow copying link text to clipboard. 
- [components-webview] Add license file. 
- [webview-doc] Fix typo in setPreference method. 
- [webview-docs] Add documentation how to bypass CORS checking. 
- [sailfish-webview] Add logging categories. 
- [sailfish-webview] Disable wasm_baselinejit on lower memory devices. 
- [webview-doc] Document overloaded setPreference C++ method. 
- [webview-doc] Refer to CookieBehavior and PreferenceType via WebEngineSettings. 
- [sailfish-webview] Document preference type of setPreference. 
- [webview] Align to ViewCreator API changes. 
- [sailfish-components-webview] Only populate permissions model with known permissions. 
- [sailfish-webview] Always enable image download in context menu. 
- [webview-examples] Make it possible to show viewport infos. 
- [sailfish-webview] Adjust text selection handles by visual viewport offset. 
- [sailfish-webview] Add wrap mode of label to SingleSelectPage. 
- [sailfish-webview] Introduce webview test application. 
- [sailfish-webview] Ensure geo permissions can be saved in normal browsing. 
- [components-webview] Migrate to sailfish-qdoc-template. 
- [sailfish-webview] Act on private browsing when requesting permissions. 
- [sailfish-components-webview] Add a footer margin property. 
- [spec] Drop separate `popups-ts-devel` and `pickers-ts-devel` sub-packages.
- [spec] Drop separate `popups-ts-devel` and `pickers-ts-devel` sub-packages. 
- [spec] Minor spec refactoring.
- [sailfish-webview] Adjust text selection markers by scrollable offset. 
- [sailfish-webview] Integrate esr78. 
### sailfish-components-webview-qt5-l10n
- Updated : 1.78.1-1.6.1.jolla -- 1.83.4-1.11.1.jolla
- Binaries added : sailfish-components-webview-qt5-l10n-lv - 1.83.4-1.11.1.jolla
- [l10n] Commit from Jolla localisation: 123 of 123 strings translated (0 need review).
- [tpl] translation templates update for 1.5.9
- [l10n] Commit from Jolla localisation: 123 of 123 strings translated (0 need review).
- [tpl] translation templates update for 1.5.8
- [l10n] Commit from Jolla localisation: 122 of 122 strings translated (0 need review).
- [tpl] translation templates update for 1.4.9
- [l10n] Commit from Jolla localisation: 122 of 122 strings translated (0 need review).
- [tpl] translation templates update for 1.4.4
- [l10n] Commit from Jolla localisation: 121 of 121 strings translated (0 need review).
### sailfish-content-ambiences-default-l10n
- Updated : 1.62.2-1.4.1.jolla -- 1.62.4-1.5.1.jolla
- Binaries added : sailfish-content-ambiences-default-l10n-lv - 1.62.4-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 29 of 29 strings translated (0 need review).
### sailfish-content-graphics-default
- Updated : 1.2.1-1.3.1.jolla -- 1.3.0.1-1.6.1.jolla
- [theme] Add new icon-m-back-tab. 
- [theme-jolla-ambient] Restructure and migrate to sailfish-qdoc-template. 
- [theme] Add an icon for mouse pointer. 
- [camera] Add color filter icons. 
### sailfish-device-encryption
- Updated : 0.10.2-1.3.1.jolla -- 0.10.3.1-1.5.3.jolla
- [sailfish-device-encryption] Fix libresource aborting on uninitialized data. 
- [qa-encrypt-device] Stop target units first. 
### sailfish-device-encryption-l10n
- Updated : 1.63.1-1.5.1.jolla -- 1.64.2-1.7.1.jolla
- Binaries added : sailfish-device-encryption-l10n-lv - 1.64.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 47 of 47 strings translated (0 need review).
### sailfish-eas
- Updated : 0.5.18-1.4.1.jolla -- 0.5.18.1-1.5.1.jolla
- [MS-ASCAL] 2.2.2.1 AllDayEvent
- [sailfish-eas] Adjust end date for all day events. 
- [sailfish-eas] Cascade all day status to exceptions. 
- [sailfish-eas] Correctly interpret single part attachment downloads. 
- [sailfish-eas] Handle all day exceptions better. 
- [sailfish-eas] Make timezone conversion more robust. 
- [sailfish-eas] Reset sync key when Calendar is disabled. 
### sailfish-filemanager-l10n
- Updated : 1.23.2-1.4.1.jolla -- 1.23.4-1.5.1.jolla
- Binaries added : sailfish-filemanager-l10n-lv - 1.23.4-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 5 of 5 strings translated (0 need review).
### sailfish-fpd
- Updated : 1.4.9-1.3.1.jolla -- 1.5.0-1.4.1.jolla
- [slave] Remove dependency on android hardware headers for binder slave. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
### sailfish-fpd-slave-binder
- Updated : 1.4.9-1.3.1.jolla -- 1.5.0-1.2.2.jolla
- [slave] Remove dependency on android hardware headers for binder slave. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
### sailfish-fpd-slave-f5121
- Updated : 1.4.9-1.3.1.jolla -- 1.5.0-1.4.1.jolla
- [slave] Remove dependency on android hardware headers for binder slave. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
### sailfish-homescreen
- Updated : 0.1.5-1.3.4.jolla -- 0.1.6-1.4.10.jolla
- [homescreen-services] Do not replace https captiveportal urls with fallback. 
### sailfish-homescreen-l10n
- Updated : 1.9.1-1.5.1.jolla -- 1.9.4-1.7.1.jolla
- Binaries added : sailfish-homescreen-l10n-lv - 1.9.4-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 2 of 2 strings translated (0 need review).
### sailfish-installationhandler-l10n
- Updated : 1.12.1-1.5.1.jolla -- 1.12.3-1.6.1.jolla
- Binaries added : sailfish-installationhandler-l10n-lv - 1.12.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 7 of 7 strings translated (0 need review).
### sailfish-maps-l10n
- Updated : 1.113.1-1.5.1.jolla -- 1.114.2-1.7.1.jolla
- Binaries added : sailfish-maps-l10n-lv - 1.114.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 89 of 89 strings translated (0 need review).
### sailfish-mdm
- Updated : 0.4.12-1.3.11.jolla -- 0.4.14-1.4.28.jolla
- [sailfish-mdm] Migrate to sailfish-qdoc-template. 
- [sailfish-policy] Use /var/lib to store policies. 
### sailfish-mdm-l10n
- Updated : 1.33.2-1.4.1.jolla -- 1.33.4-1.5.1.jolla
- Binaries added : sailfish-mdm-l10n-lv - 1.33.4-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 4 of 4 strings translated (0 need review).
### sailfish-minui
- Updated : 0.0.32-1.3.1.jolla -- 0.0.32.1-1.4.1.jolla
- [mindbus] Fix nullptr unref. 
### sailfish-minui-l10n
- Updated : 1.36.3-1.3.1.jolla -- 1.36.5-1.4.1.jolla
- Binaries added : sailfish-minui-l10n-lv - 1.36.5-1.4.1.jolla
- [l10n] Commit from Jolla localisation: 15 of 15 strings translated (0 need review).
### sailfish-office
- Updated : 1.6.0-1.4.1.jolla -- 1.6.1-1.5.1.jolla
- [sailfish-office] Remove unneeded Sharing permission. 
### sailfish-office-l10n
- Updated : 1.155.1-1.5.1.jolla -- 1.156.2-1.7.1.jolla
- Binaries added : sailfish-office-l10n-lv - 1.156.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 86 of 86 strings translated (0 need review).
### sailfish-policy
- Updated : 0.4.12-1.3.3.jolla -- 0.4.14-1.4.12.jolla
- [sailfish-mdm] Migrate to sailfish-qdoc-template. 
- [sailfish-policy] Use /var/lib to store policies. 
### sailfish-polkit-agent
- Updated : 1.0.4-1.4.1.jolla -- 1.0.5-1.5.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### sailfish-secrets
- Updated : 0.2.21-1.5.1.jolla -- 0.2.31-1.11.2.jolla
- [sailfish-secrets] Create the socket directory in the plugin also.
- [sailfish-secrets] Create the socket directory in the plugin also. 
- [sailfish-secrets] Bump version. 
- [sailfish-secrets] Correct p2p socket name for the password agent. 
- [sailfish-secrets] Have license file as %license. 
- [sailfish-secrets] Put the P2P DBus socket in a sub-directory of /run.
- [sailfish-secrets] Put the P2P DBus socket in a sub-directory of /run. 
- [sailfish-secrets] Remove mentions of the Mailing list. Change references pointing to together.jolla.com to forum.sailfishos.org and rename all mentions of Together Jolla to Sailfish OS Forum. Contributes to: 
- [SecretsCrypto] Update notification configuration. 
- [secrets] Adapt to sailfish-qdoc-template. 
- [packaging] BuildRequire systemd via pkgconfig. 
- [sailfish-secrets] Fix libgpg-error pkgconfig symbol name
- [sailfish-secrets] Fix libgpg-error pkgconfig symbol name. 
### sailfish-secrets-l10n
- Updated : 1.45.1-1.10.1.jolla -- 1.48.2-1.14.1.jolla
- Binaries added : sailfish-secrets-l10n-lv - 1.48.2-1.14.1.jolla
- [l10n] Commit from Jolla localisation: 50 of 50 strings translated (0 need review).
- [tpl] translation templates update for 0.2.25
- [l10n] Commit from Jolla localisation: 49 of 49 strings translated (0 need review).
### sailfish-secrets-ui
- Updated : 0.1.8-1.3.1.jolla -- 0.1.9-1.4.1.jolla
- [share] Update sharing plugin to new interface. 
### sailfish-secrets-ui-l10n
- Updated : 1.45.1-1.5.1.jolla -- 1.47.2-1.7.1.jolla
- Binaries added : sailfish-secrets-ui-l10n-lv - 1.47.2-1.7.1.jolla
- [tpl] translation templates update for 0.1.9
- [l10n] Commit from Jolla localisation: 54 of 54 strings translated (0 need review).
### sailfish-tutorial-l10n
- Updated : 1.105.1-1.6.1.jolla -- 1.107.2-1.8.1.jolla
- Binaries added : sailfish-tutorial-l10n-lv - 1.107.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 61 of 61 strings translated (0 need review).
### sailfish-upgrade-ui-l10n
- Updated : 1.28.3-1.3.1.jolla -- 1.29.2-1.5.1.jolla
- Binaries added : sailfish-upgrade-ui-l10n-lv - 1.29.2-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 3 of 3 strings translated (0 need review).
### sailfish-utilities
- Updated : 0.1.13-1.4.4.jolla -- 0.1.14-1.5.11.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### sailfish-utilities-l10n
- Updated : 1.74.1-1.5.1.jolla -- 1.74.3-1.6.1.jolla
- Binaries added : sailfish-utilities-l10n-lv - 1.74.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 16 of 16 strings translated (0 need review).
### sailfish-version
- Updated : 4.3.0-1.4.15.jolla -- 4.4.0-1.5.58.jolla
- [version] Change name for 4.4.0 (Vanha Rauma). 
### sailfish-weather-l10n
- Updated : 1.59.1-1.5.1.jolla -- 1.60.2-1.7.1.jolla
- Binaries added : sailfish-weather-l10n-lv - 1.60.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 25 of 25 strings translated (0 need review).
### sailfishsilica-qt5
- Updated : 1.2.71.1-1.6.1.jolla -- 1.2.79.1-1.8.1.jolla
- [silica] Regenerate qmltypes without dependencies between modules. 
- [silica] Drop Qt Multimedia dependency. 
- [silica] Introduce draggable scrollbar. 
- [silica] Fix broken autoscroll on dialer. 
- [silica] Use sailfish-qdoc-template. 
- [coveraction] Use random id on bus names. 
- [silica] Remove absolute path for qmltestrunner. 
- [silica] Remove extra make docs. 
- [silica] Add Theme cheat sheet to scalability documentation. 
### sailfishsilica-qt5-l10n
- Updated : 1.156.1-1.5.1.jolla -- 1.156.3-1.6.1.jolla
- Binaries added : sailfishsilica-qt5-l10n-lv - 1.156.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 49 of 107 strings translated (0 need review).
### sailjail
- Updated : 1.1.12.1-1.15.1.jolla -- 1.1.18.2-1.18.3.jolla
- [sailjail] Obsolete sailjail-homescreen-plugin. 
- [dbus] Allow identification of clients behind xdg-dbus-proxy. 
- [sailjail] Filter out Compatiblity.permission. 
- [sailjail] Validate ExecDBus correctly. 
- [prompter] Close dialog if client disconnects. 
- [daemon] Exclude apkd-launcher from default sandboxing. 
- [client] Add --debug-mode option. 
- [client] Add --dry-run option. 
- [client] Add missing prototypes
- [prompter] Make only locally used function static
- [daemon] Allow canceling windowprompt. 
### sailjail-permissions
- Updated : 1.0.81.4-1.28.1.jolla -- 1.0.99-1.30.2.jolla
- [permissions] Allow apps to receive dsme dbus signals. 
- [permissions] Remove folder required by WebView from blacklist.
- [permissions] Supplement broadcast permissions for UDisksListen.
- [permissions] Drop voicecall-ui-prestart.profile symlink. 
- [voicecall-ui] Allow checking lock state and starting csd. 
- [permissions] Be more verbose about avoiding Compatibility permission
- [permissions] Add /etc/media_codec.xml to base permissions. 
- [permissions] Add Compatibility permission. 
- [permissions] Add contextkit dir to base permissions. 
- [sailjail-permissions] Add a permission to talk over secrets daemon DBus.
- [permissions] Add access to policies 
- [permissions] Add location.conf file directory to whitelist. 
- [permissions] Use Harbour-compatible Exec line in example. 
- [permissions] Add MmsHandler to Messages.permission. 
- [permissions] Give sailfish-browser access to the device lock Authenticator interface. 
- [permissions] Allow Sharing by default. 
- [permissions] Fix libsignond bus permission. 
- [media] Give access to /etc/gst-droid for media and camera applications. 
### sailjail-permissions-l10n
- Updated : 1.47.2-1.22.1.jolla -- 1.55.2-1.24.1.jolla
- Binaries added : sailjail-permissions-l10n-lv - 1.55.2-1.24.1.jolla
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.93
- [tpl] translation templates update for 1.0.99
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.92
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.91
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.85
- [tpl] translation templates update for 1.0.86
- [tpl] translation templates update for 1.0.87
- [tpl] translation templates update for 1.0.88
- [tpl] translation templates update for 1.0.89
- [tpl] translation templates update for 1.0.90
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.85
- [tpl] translation templates update for 1.0.86
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.85
- [l10n] Commit from Jolla localisation: 62 of 62 strings translated (0 need review).
- [tpl] translation templates update for 1.0.59
- [tpl] translation templates update for 1.0.84
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.83
- [l10n] Commit from Jolla localisation: 66 of 66 strings translated (0 need review).
- [tpl] translation templates update for 1.0.59
- [tpl] translation templates update for 1.0.82
### sb2-tools-aarch64-inject
- Updated : 1.0+git25-1.6.2.jolla -- 1.0+git29-1.8.8.jolla
- Add zstd and libzstd now used by rpm. 
- Replace busybox-symlinks-which with which. 
- Add libxcrypt. 
- Add lua-posix. 
### sb2-tools-armv7hl-inject
- Updated : 1.0+git25-1.6.2.jolla -- 1.0+git29-1.8.8.jolla
- Add zstd and libzstd now used by rpm. 
- Replace busybox-symlinks-which with which. 
- Add libxcrypt. 
- Add lua-posix. 
### sb2-tools-i486-inject
- Updated : 1.0+git25-1.6.1.jolla -- 1.0+git29-1.8.8.jolla
- Add zstd and libzstd now used by rpm. 
- Replace busybox-symlinks-which with which. 
- Add libxcrypt. 
- Add lua-posix. 
### sb2-tools-qt5-aarch64
- Updated : 5.0-1.6.2.jolla -- 5.0-1.8.3.jolla
- [packages] systemd-libs -> systemd-mini-libs. 
- [packaging] Remove libselinux not needed by systemd-mini. 
### sb2-tools-qt5-armv7hl
- Updated : 5.0-1.6.2.jolla -- 5.0-1.8.3.jolla
- [packages] systemd-libs -> systemd-mini-libs. 
- [packaging] Remove libselinux not needed by systemd-mini. 
### scratchbox2
- Updated : 2.3.90+git45-1.9.1.jolla -- 2.3.90+git51-1.13.1.jolla
- [sb2] Fix exec policy for executables under SDK workspace. 
- [sb2] Fix mapping error with /sdkroot. 
- [sb2] Allow to access arbitrary paths under SDK root. 
- [sb2] Accelerate zstd. 
- [lua_scripts] Handle wrappers in argvenvp_misc directly. 
- [lua_scripts] Not only map argvmods to /usr/bin.
- [lua_scripts] Refactor processing of argvenvp rules
- [lua_scripts] Restore docs argvmods
- [packaging] Fix rpm license tag. 
- [packaging] Remove unused fakeroot dependency. 
- [packaging] Use %configure, %make in spec file
- [sb2] Don't use relative paths for include path and makefiles
- [sb2] Remove redudant /sb2 paths from PATH. 
- [sb2] Do not use git-subtree for packaging. 
### screen
- Updated : 4.7.0+git1-1.5.3.jolla -- 4.7.0+git2-1.7.11.jolla
- [screen] Explicitly depend on pkgconfig(libcrypt). 
### sdk-client
- Updated : 0.11-1.2.1.jolla -- 0.12-1.3.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### sdk-harbour-rpmvalidator
- Updated : 1.70-1.6.1.jolla -- 1.80-1.10.25.jolla
- [harbour-validator] Disallow OpenSSL 1.0 libraries. 
- [harbour-validator] Deprecate QtWebKit. 
- [rpmvalidator] Fix mapplauncherd url to current location. 
- [harbour-validator] Ignore comment lines on X-Sailjail section. 
- [harbour-validator] Print warning for Compatibility permission. 
- [harbour-validator] Generate list of allowed permissions. 
- [harbour-validator] Clean up comments in conf files. 
- [harbour-validator] Generate Markdown lists. 
- [harbour-validator] Allow Compatibility permission. 
- [harbour-validator] Add missing linefeed. 
- [harbour-validator] Allow Amber.Mpris 1.0. 
- [harbour-validator] Only allow specified Amber imports. 
### sdk-setup
- Updated : 1.4.42-1.6.1.jolla -- 1.4.55-1.24.1.jolla
- [sdk-manage] Silently process unsigned packages in cache. 
- [mb2] Expand on basic build tasks in built-in help. 
- [mb2] Allow to diff/reset build requires without spec. 
- [sdk-manage] Use sdk-register from /usr/libexec if possible. 
- [sdk-chroot] Accept y/n when creating target directories. 
- [mb2] Fix package version also for build-requires commands
- [mb2] Fix spec Version tags also inside included files. 
- [mb2] Run rpmlint by default after build. 
- [sdk-setup] Allow to run scripts directly from host. 
- [mb2] Do not remove latest RPMs with volatile EVR. 
- [mb2] Do not discard exit code of maintenance shell. 
- [sdk-manage] Do not sync after failed maintenance command
- [sdk-manage] Fix zypper under snapshots with custom SDK prefix. 
- [sdk-setup] Fix compatibility with newer sudo. 
- [sdk-manage] Do not fail to sync trees with file type change. 
- [sdk-manage] Fix purging snapshot files that are gone in original
### sensorfw-qt5
- Updated : 0.12.4-1.6.1.jolla -- 0.12.6-1.8.1.jolla
- [sensorfw] Add support for sensor binder API 2. 
- [sensorfw] Fix build on 32-bit kernels with 64-bit time_t. 
### setup
- Updated : 2.13.6+git4-1.8.3.jolla -- 2.13.6+git5-1.10.9.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### shadow-utils
- Updated : 4.8.1+git1-1.5.3.jolla -- 4.8.1+git2-1.7.11.jolla
- [shadow] Explicitly depend on pkgconfig(libcrypt). 
### simkit
- Updated : 0.4.29-1.3.3.jolla -- 0.4.30-1.4.11.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### simkit-l10n
- Updated : 1.59.1-1.4.1.jolla -- 1.59.3-1.5.1.jolla
- Binaries added : simkit-l10n-lv - 1.59.3-1.5.1.jolla
- [l10n] Commit from Jolla localisation: 14 of 14 strings translated (0 need review).
### sp-rich-core
- Updated : 1.74.25-1.6.1.jolla -- 1.74.26-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### sp-stress
- Updated : 0.2.1-1.2.19.jolla -- 0.2.2-1.3.38.jolla
- [sp-stress] Clean up old packaging.
- [sp-stress] Clean up spec file. 
### sqlite
- Updated : 3.33.0+git1-1.4.1.jolla -- 3.37.2+git1-1.7.1.jolla
- [rpm] Cleanup unnecessary Obsoletes and Conflicts. 
- [sqlite] Update to version 3.37.2. 
- [sqlite] Update to version 3.36.0. 
### ssu
- Updated : 1.0.14.1-1.6.1.jolla -- 1.0.19-1.8.1.jolla
- [tests] Install test repo data correctly to repos.d for ut_repomanager. 
- [tests] Install test repo data correctly to repos.d for ut_ssu. 
- [tests] Install test repo data correctly to repos.d for ut_ssuurlresolver. 
- [tests] Install test repo data correctly to repos.d for ut_urlresolver. 
- [tests] Reorganize SSU test set. 
- [ssu] Output global variables in ssu status. 
- [ssu] Make sure the ssu cache is up-to-date. 
### ssu-repos
- Updated : 0.129-1.12.1.jolla -- 0.131-1.13.1.jolla
- [ssu-repos] Expect ssu to touch the config files. 
- [ssu-repos] Remove old expired GPG keys after stop release. 
- [ssu-repos] Remove ancient gconf reference. 
### store-client
- Updated : 1.3.4-1.5.1.jolla -- 1.3.4.1-1.6.1.jolla
- [store-client] Release cover image for 4.4.0. 
### store-client-l10n
- Updated : 1.206.1-1.5.1.jolla -- 1.207.2-1.7.1.jolla
- Binaries added : store-client-l10n-lv - 1.207.2-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 145 of 145 strings translated (0 need review).
### systemd
- Updated : 238+git7-1.12.1.jolla -- 238+git13-1.13.1.jolla
- [systemd] Add workaround for OBS dependency problem for building systemd. 
- [packaging] Fix typo
- [packaging] Add missing files to sources
- [systemd] Add bootstrap build condition. 
- [systemd] Add libstdc++-devel needed to build. 
- [systemd] Add script to generate bootstrap variant spec. 
- [systemd-mini] Generate spec file. 
- [systemd] Explicitly depend on pkgconfig(libcrypt). 
### systemd-bootchart
- Updated : 233+git1-1.5.1.jolla -- 233+git2-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### systemd-user-session-targets
- Updated : 0.0.2-1.5.1.jolla -- 0.0.2-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### telepathy-mission-control
- Updated : 5.16.6+git3-1.5.1.jolla -- 5.16.6+git6-1.7.1.jolla
- [git] Move submodule repos to github. 
- [telepathy-mission-control] Don't let OOM killer kill. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
- [packaging] BuildRequire systemd via pkgconfig. 
### telepathy-ring
- Updated : 2.5.10-1.4.1.jolla -- 2.5.12-1.7.4.jolla
- [tp-ring] Don't let OOM killer kill telepathy-ring. 
- [packaging] BuildRequire systemd via pkgconfig. 
### testrunner-lite
- Updated : 1.9.0-1.4.24.jolla -- 1.9.1-1.5.44.jolla
- [testrunner-lite] Add config.sub to fix autoreconf problem. 
- [testrunner-lite] Disable doxygen and html docs. 
- [testrunner-lite] Fix unit tests for newer check version. 
- [testrunner-lite] Workaround gcc 10.3.0 problems. 
### thumbnaild
- Updated : 0.0.9-1.5.1.jolla -- 0.0.10-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### tracker
- Updated : 3.1.2+git4-1.5.1.jolla -- 3.2.1+git1-1.6.1.jolla
- [tracker] Update to 3.2.1. 
- [tracker] Update to 3.2.0. 
### tracker-miners
- Updated : 3.1.2+git2-1.5.1.jolla -- 3.2.1+git1-1.6.2.jolla
- [tracker-miners] Update to 3.2.1. 
- [tracker-miners] Update to 3.2.0. 
- [tracker-miners] Fix nfo:fileName and nfo:fileLastModified updates. 
### transferengine-plugins
- Updated : 0.2.22-1.4.1.jolla -- 0.3.0-1.6.1.jolla
- [declarative] Separate sharing plugins from transfer plugins. 
- [transferengine-plugins] Add lib and plugin for translations. 
- [transferengine-plugins] Add SMS sharing plugin. 
### transferengine-plugins-l10n
- Updated : 1.129.1-1.6.1.jolla -- 1.133.2-1.9.1.jolla
- Binaries added : transferengine-plugins-l10n-lv - 1.133.2-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 17 of 17 strings translated (0 need review).
- [tpl] translation templates update for 0.3.0
- [l10n] Commit from Jolla localisation: 20 of 20 strings translated (0 need review).
- [tpl] translation templates update for 0.2.23
### udisks2
- Updated : 2.8.1+git11-1.6.2.jolla -- 2.9.4+git2-1.10.1.jolla
- [udisks2] Add workaround for mount if mmcblk1 is internal. 
- [packaging] Remove copying from -devel package. 
- [udisks2] Update to version 2.9.4. 
- [packaging] Only BuildRequire systemd via pkgconfig. 
### usb-moded
- Updated : 0.86.0+mer55-1.6.2.jolla -- 0.86.0+mer56-1.8.4.jolla
- [packaging] Only BuildRequire systemd via pkgconfig. 
### user-managerd
- Updated : 0.8.3-1.6.1.jolla -- 0.8.5-1.7.2.jolla
- [user-managerd] Migrate to sailfish-qdoc-template. 
- [user-managerd] Add script execution on user pre-switch. 
### util-linux
- Updated : 2.33+git2-1.5.5.jolla -- 2.33+git3-1.7.14.jolla
- [util-linux] Explicitly depend on pkgconfig(libcrypt). 
### valgrind
- Updated : 3.15.0+git2-1.2.1.jolla -- 3.18.1+git1-1.3.1.jolla
- [valgrind] Update to version 3.18.1. 
### virtualbox
- Updated : 5.2.30+git3-1.2.2.jolla -- 5.2.30+git4-1.3.3.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
### voicecall-qt5
- Updated : 0.7.11-1.5.1.jolla -- 0.7.13-1.7.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 
- [voicecall] Remove unimplemented methods. 
### voicecall-ui-jolla
- Updated : 1.14.37-1.4.1.jolla -- 1.14.38-1.5.1.jolla
- [voicecall-ui] Remove unneeded Sharing permission. 
### voicecall-ui-jolla-l10n
- Updated : 1.299.1-1.6.1.jolla -- 1.301.2-1.8.1.jolla
- Binaries added : voicecall-ui-jolla-l10n-lv - 1.301.2-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 250 of 250 strings translated (0 need review).
### wpa_supplicant
- Updated : 2.9+git2-1.5.2.jolla -- 2.9+git4-1.7.1.jolla
- [wpa_supplicant] Patch CVE-2021-0326 and CVE-2021-27803. 
- [packaging] BuildRequire systemd via pkgconfig. 
### xdg-dbus-proxy
- Updated : 0.1.2+git2-1.6.1.jolla -- 0.1.2+git3-1.7.1.jolla
- [xdb-dbus-proxy] Add D-Bus interface for querying client process details. 
### xulrunner-qt5
- Updated : 60.9.1+git61-1.11.7.jolla -- 78.15.1+git24.1-1.30.1.jolla
- [sailfishos][gecko] Initialise SVGGeometryProperty::ResolveAll parameters. 
- [sailfishos][gecko] Add a video decoder based on gecko-camera. 
- [sailfishos][gecko-dev] Adapt to gecko-camera API change. 
- [sailfishos][embedlite] Disable system extension dirs. 
- [sailfishos][gecko] Fix memory reporting of wasm memory. 
- [sailfishos][gecko] Revert "Bug 1611386 - Drop support for --enable-system-sqlite". 
- [sailfishos][gecko][rpm] Use system sqlite. 
- [sailfishos][rpm] Use system sqlite. 
- [sailfishos][gecko-dev] Add preference to bypass CORS on nsContentSecurityManager. 
- [sailfishos][embedlite] Pass double taps to embedhelper.js. 
- [sailfishos][embedlite] Load external uris directory via nsIExternalProtocolService. 
- [sailfishos][gecko] Ensure zooming is always allowed if desktop mode is active. 
- [sailfishos][embedlite] Fix user agent notify. 
- [sailfishos][gecko-dev] Ensure clipboard service can be accessed. 
- [sailfishos][gecko-dev] Fix video hardware accelaration not being used on first playback. 
- [sailfishos][embedlite] Pass parent browsing context down to CreateNewWindowRequested. 
- [sailfishos][rpm] Drop python2 dependency from xulrunner build. 
- [sailfishos][embedlite][egl] Fix egl patch to prevent crashing. 
- [sailfishos][embedlite][egl] Fix mesa egl display and buffer initialisation. 
- [sailfishos][embedlite] Make EmbedFrame an EventListener. 
- [sailfishos][rpm] Re-enable startup cache for all arch except x86. 
- [sailfishos][embedlite] Drop root frame argument from the PEmbedLiteView.ipdl and EmbedLiteViewListener::HandleScrollEvent. 
- [sailfishos][embedlite] Read scrollable rect from frame metrics of root layer. 
- [sailfishos][embedlite] Http max-connections to 40. 
- [sailfishos][gecko] Fix audio underruns for the fullduplex mode. 
- [sailfishos][gecko] Restart the camera when changing the resolution. 
- [sailfishos][embedlite] Add task reference to FIXME. 
- [sailfishos][embedlite] Cleanup already fixed FIXME
- [sailfishos][embedlite] Guard against null pointer dereference when calling OnDynamicToolbarHeightChanged. 
- [sailfishos][embedlite] Prevent invalid manifest location from being added. 
- [sailfishos][embedlite] Drop embedlite specific History listener. 
- [sailfishos][rpm] Fix patch numbering. 
- [sailfishos][rpm] Format patches with --zero-commit. 
- [sailfishos][rpm] Revert 'Remove static registration of Remove static registration of the 'mozilla/places/History.h' module'. 
- [sailfishos][embedlite] Enable the pointer event API. 
- [sailfishos][embedlite] Enable VisualViewport API. 
- [sailfishos][gecko-dev] Enable the pointer event API. 
- [sailfishos][gecko] Enable the pointer event API. 
- [sailfishos][gecko] Fix default font size. 
- [sailfishos][embedlite] Implement nsIWidget methods in nsWindow.cpp. 
- [sailfishos][gecko] Remove nsWidget.h/cpp and mozqwidget.h/cpp from widget/qt. 
- [sailfishos][gecko] Fix download starting when multiple tabs are closed. 
- [sailfishos][embedlite] Set ScreenManager's screen properties. 
- [sailfishos][gecko] Bump up to latest 78.15.1 sha1. 
- [sailfishos][docshell] Create CanonicalBrowsingContext. 
- [sailfishos][embedlite] Create Secure Browser UI. 
- [sailfishos][embedlite] Fix crash in EmbedLiteSecurity. 
- [sailfishos][gecko] Allow LoginManagerPrompter to find its window. 
- [sailfishos][embedlite] Remove unused variable. 
- [sailfishos][gecko] Enable support for WebRTC. 
- [sailfishos][embedlite] Fix EmbedLiteSecurity compiler warnings. 
- [sailfishos][embedlite] Remove unused ContentListener class. 
- [sailfishos][gecko] Fix media elements being suspended on the active tab. 
- [sailfishos][gecko-dev] Fix timeouts when querying location. 
- [sailfishos][browserchild] Add parentIsActive attribute to the nsIBrowserChild. 
- [sailfishos][embedlite] Enable serviceworkers. 
- [sailfishos][embedlite] Guard access to EmbedLiteViewChildIface in BrowserChildHelper. 
- [sailfishos][embedlite] Set valid webnavigation for the BrowserChildHelper. 
- [sailfishos][gecko] Fix nsIBrowserChild activity status receiving in nsFocusManager. 
- [sailfishos][embedlite] Enable touch event legacy apis. 
- [sailfishos][embedlite] Update dynamic toolbar offset. 
- [sailfishos][gecko] Adapt safemode patch. 
- [sailfishos][gecko] Patching not needed for reCAPTCHA in esr78. 
- [sailfishos][rpm] Adapt safemode patch. 
- [sailfishos][gecko] Reformat patch to allow git am to work
- [sailfishos][sidebar] Load sidebar for embedlite as well. 
- [sailfishos][embedlite] Add a separate method to set the height of the area overlapped by the toolbar. 
- [sailfishos][embedlite] Add scrolling of focused text input field to the visible area when changing view margins. 
- [sailfishos][embedlite] Remove unused EmbedLiteViewBaseChild::RecvSetVirtualKeyboardHeight. 
- [sailfishos][embedlite] Remove unused EmbedLiteViewBaseChild::ScrollInputFieldIntoView. 
- [sailfishos][embedlite] Setting view margins by changing nsBaseWidget::mBounds. 
- [sailfishos][embedlite] Use OS agnostic user-agent. 
- [sailfishos][ua] Do not replace platform name. 
- [sailfishos][rpm] Move old patches out of rpm directory. 
- [sailfishos][embedlite] Cleanup DrawWindowUnderlay and DrawUnderlay. 
- [sailfishos][embedlite] Use StaticXREAppData to read application.ini. 
- [sailfishos][gecko] Use only embedlite clipboard. 
- [sailfishos][gfx] Use scroll frame background color as clear color. 
- [sailfishos][audio] Bring back "pulse" cubeb backend. 
- [sailfishos][components] Cleanup app-info from xre/components.conf. 
- [sailfishos][components] Cleanup static components definitions. 
- [sailfishos][embedlite] Add string formatted component CID in comments
- [sailfishos][embedlite] Define EmbedLiteXulAppInfo as static component. 
- [sailfishos][configure] Update submodule to new gecko-dev mirror. 
- [sailfishos][embedlite] Add methods to get current number of EmbedLiteApp views and windows. 
- [sailfishos][embedlite] Add support for text replacing in text event handler. 
- [sailfishos][embedlite] Allow current window id to be retrieved. 
- [sailfishos][embedlite] Allow EmbedLiteApp window re-creation. 
- [sailfishos][embedlite] Cherry-pick EmbedLiteAppChild changes from master. 
- [sailfishos][embedlite] Cleanup DrawWindowOverlay. 
- [sailfishos][embedlite] Define extensions.systemAddon.update.enabled as false. 
- [sailfishos][embedlite] Do not destroy uninitialized PEmbedLiteView. 
- [sailfishos][embedlite] Do not destroy uninitialized PEmbedLiteWindow. 
- [sailfishos][embedlite] Fix child actor services not receiving events. 
- [sailfishos][embedlite] Fix flickering on animated web page in a web view. 
- [sailfishos][embedlite] Introduce back DestroyBrowserWindow method implementation. 
- [sailfishos][embedlite] Pass EmbedLiteWindowListener pointer to PEmbedLiteWindowConstructor. 
- [sailfishos][embedlite] Pass parent browsing context to the view. 
- [sailfishos][embedlite] Prevent null pointer dereference in PuppetWidgetBase::Invalidate. 
- [sailfishos][embedlite] Provide KeyNameIndex and CodeNameIndex for WidgetKeyboardEvent. 
- [sailfishos][embedlite] Reset toolbar height after vkb closes. 
- [sailfishos][embedlite] Set BrowsingContext to private mode before attaching it. 
- [sailfishos][embedlite] Switch LOGNI() for LOGT() in places
- [sailfishos][embedlite] Synchronize puppet widget margins change. 
- [sailfishos][embedlite] Use dynamic toolbar height API to set bottom margin. 
- [sailfishos][embedlite] Use std::map::find to get view pointer in EmbedLiteAppChild::GetViewByID. 
- [sailfishos][gecko] Add ESR68 WebRTC patches into old_patches. 
- [sailfishos][gecko] Apply unchanged patches. 
- [sailfishos][gecko] Reapply patch: "Configure application as mobile/sailfishos". 
- [sailfishos][gecko] Reapply patch: "Delete startupCache if it's stale". 
- [sailfishos][gecko] Reapply patch: "Disable loading heavier extensions". 
- [sailfishos][gecko] Reapply patch: "Do not flip scissor rects when...". 
- [sailfishos][gecko] Reapply patch: "Embedlite doesn't have prompter implementation". 
- [sailfishos][gecko] Reapply patch: "Ensure audio continues when screen is locked". 
- [sailfishos][gecko] Reapply patch: "Fix content action integration to work". 
- [sailfishos][gecko] Reapply patch: "Fix flipped FBO textures when rendering to an offscreen target". 
- [sailfishos][gecko] Reapply patch: "Get 12/24h timeformat setting from dconf". 
- [sailfishos][gecko] Reapply patch: "Handle temporary directory similarly as in MacOSX". 
- [sailfishos][gecko] Reapply patch: "Hardcode loopback address for profile lock filename". 
- [sailfishos][gecko] Reapply patch: "Hide accessible carets also with touch select all event". 
- [sailfishos][gecko] Reapply patch: "Make fullscreen enabling work...". 
- [sailfishos][gecko] Reapply patch: "Prioritize loading of extension versions...". 
- [sailfishos][gecko] Reapply patch: "Skip invalid WatchId in geolocation.clearWatch()". 
- [sailfishos][gecko] Reapply patch: "Start using user-agent builder". 
- [sailfishos][gecko] Reapply patch: "Suppress LoginManagerContent.jsm ownerDocument errors". 
- [sailfishos][gecko] Reapply patch: "Use libcontentaction for custom scheme uri handling". 
- [sailfishos][gecko] Remove redundant patches. 
- [sailfishos][gecko] Remove redundant patch. 
- [sailfishos][gecko] Revert "Bug 1494175 - Remove unimplementet nsIWebBrowserChrome methods. r=qdot". 
- [sailfishos][gecko] Tidy up patch. 
- [sailfishos][media] Ensure audio continues when screen is locked.
- [sailfishos][packaging] Workaround for .git directory in submodule 
- [sailfishos][contentcontrollre] Use MessageLoop to forward events. 
- [sailfishos][egl] Drop swap_buffers_with_damage extension support. 
- [sailfishos][embedlite] Adapt EmbedLiteViewChild::RecvHandleSingleTap to APZEventState::ProcessSingleTap. 
- [sailfishos][embedlite] Adapt package-manifest.in from Android FF. 
- [sailfishos][embedlite] Add dummy preprocessor directive. Fixex 
- [sailfishos][embedlite] Adjust embed scroll style. Fixex 
- [sailfishos][embedlite] Call ViewportUtils::GetVisualToLayoutTransform to touch point position. 
- [sailfishos][embedlite] Fix a crash when trying to a acquire a wake lock. 
- [sailfishos][embedlite] Fix MessageManagerCallback overrides. 
- [sailfishos][embedlite] Fix search plugin directories. 
- [sailfishos][embedlite] Use GetTopLevelPresShell for ApplyPointTransform. 
- [sailfishos][gecko] Adapt GMP patches from ESR60. 
- [sailfishos][gecko] Fix delivery of MozAfterPaint events. 
- [sailfishos][packaging] Avoid stripping debug symbols during final link step on arm. 
- [sailfishos][packaging] Disable startupCache for all architectures. 
- [sailfishos][compositor] Adapt EmbedLiteCompositorBridgeParent to CompositorBridgeParent. 
- [sailfishos][compositor] Adapt patch "Allow compositor specializations to override the composite (part 2)". 
- [sailfishos][compositor] Backport "Create EmbedLiteCompositorBridgeParent in CompositorManagerParent" 
- [sailfishos][configure] Align cross-linker to work with sb2
- [sailfishos][configure] Configure build environment
- [sailfishos][configure] Disable LTO for rust 1.52.1 with ESR78. 
- [sailfishos][configure] Expose elf32-i386 libclang.so.10 to arm target. 
- [sailfishos][configure] Expose sb2 target to build process
- [sailfishos][configure] Expose std headers in separate folder. 
- [sailfishos][configure] Get the target and host from the environment
- [sailfishos][configure] Patch glslopt to build on arm. 
- [sailfishos][configure] Patch libloading to build on arm.
- [sailfishos][configure] Reduce libxul.so link step memory. 
- [sailfishos][configure] Skip min_libclang_version test during configuration. 
- [sailfishos][contentcontroller] Dispatch to ui thread only if not already there. 
- [sailfishos][docshell] Get ContentFrameMessageManager via nsIDocShellTreeOwner. 
- [sailfishos][egl] Backport display fixes. 
- [sailfishos][egl] Fix mesa egl display initialisation
- [sailfishos][embedlite] Adapt BrowserChildHelper to nsIBrowserChild. 
- [sailfishos][embedlite] Adapt code from EmbedLiteViewBaseChild/Parent to EmbedLiteViewChild/Parent. 
- [sailfishos][embedlite] Adapt EmbedContentController to GeckoContentController. 
- [sailfishos][embedlite] Adapt EmbedHistoryListener to IHistory. 
- [sailfishos][embedlite] Adapt EmbedLiteAppBaseChild to PEmbedLiteAppChild. 
- [sailfishos][embedlite] Adapt EmbedLiteCompositorProcessParent to CompositorBridgeParent. 
- [sailfishos][embedlite] Adapt embedlite/installer/Makefile.in for esr78. 
- [sailfishos][embedlite] Adapt EmbedLiteJSON. 
- [sailfishos][embedlite] Adapt embedlite nsEmbedClipboard. 
- [sailfishos][embedlite] Adapt embedlite utils for esr78. 
- [sailfishos][embedlite] Adapt EmbedLiteViewBaseChild to PEmbedLiteViewChild. 
- [sailfishos][embedlite] Adapt EmbedLiteViewBaseParent to PEmbedLiteViewParent. 
- [sailfishos][embedlite] Adapt EmbedLiteViewParent to IAPZCTreeManager. 
- [sailfishos][embedlite] Adapt EmbedLiteWindowBaseChild to PEmbedLiteWindowChild. 
- [sailfishos][embedlite] Adapt EmbedLiteWindowBaseParent to PEmbedLiteWindowParent. 
- [sailfishos][embedlite] Adapt EmbedLiteXulAppInfo to nsIXULAppInfo and nsIXULRuntime. 
- [sailfishos][embedlite] Adapt embed modules for esr78
- [sailfishos][embedlite] Adapt embed process for esr78
- [sailfishos][embedlite] Adapt embed shared for esr78
- [sailfishos][embedlite] Adapt nsEmbedClipboard to nsTransferable. 
- [sailfishos][embedlite] Adapt nsIDOMWindowUtils getter calls. 
- [sailfishos][embedlite] Adapt nsWindow to nsBaseWidget. 
- [sailfishos][embedlite] Adapt TabChildHelper for gecko esr78. 
- [sailfishos][embedlite] Add an API to load desktop version of the site. 
- [sailfishos][embedlite] Add DispatchMessageManagerMessage implementation to BrowserChildHelper. 
- [sailfishos][embedlite] Add '--enable-default-toolkit=cairo-qt' option back to the mozconfig.merqtxulrunner. 
- [sailfishos][embedlite] Add including of PrefsTypes to PEmbedLiteApp.ipdl. 
- [sailfishos][embedlite] Add input field scrolling to visible area when keyboard appears. 
- [sailfishos][embedlite] Add passing of vsync rate when constructing LayerTransactionParent. 
- [sailfishos][embedlite] Add 'using namespace mozilla::dom;' to WebBrowserChrome.cpp. 
- [sailfishos][embedlite] Add 'using namespace mozilla;' to EmbedLog.cpp. 
- [sailfishos][embedlite] Add WebBrowserChrome::OnContentBlockingEvent implementation. 
- [sailfishos][embedlite] Cleanup embedding/embedlite/Makefile.in DEFINES. 
- [sailfishos][embedlite] Comment out nsPIDOMWindowInner::Freeze and nsPIDOMWindowInner::Thaw usage. 
- [sailfishos][embedlite] Comment out Preferences::GetPreferences usage. 
- [sailfishos][embedlite] Configure as mobile/sailfishos. 
- [sailfishos][embedlite] Configure embedlite without tests and marionette. 
- [sailfishos][embedlite] Construct WidgetTouchEvent object in-place. 
- [sailfishos][embedlite] Convert nsEmbedHistoryModule to static registration. 
- [sailfishos][embedlite] Convert nsEmbedWidgetFactoryModule to static registration. 
- [sailfishos][embedlite] Create BrowserChildHelper early enough. 
- [sailfishos][embedlite] Create web browser object trough nsWebBrowser::Create. 
- [sailfishos][embedlite] Define with-app-name=xulrunner-qt5 in mozconfig.merqtxulrunner. 
- [sailfishos][embedlite] Disable embedLiteCoreInitTest and embedLiteViewInitTest. 
- [sailfishos][embedlite] Disable layers.progressive-paint. 
- [sailfishos][embedlite] Disable WebRTC support for now. 
- [sailfishos][embedlite] Do not call NS_LogTerm upon InitEmbedding. 
- [sailfishos][embedlite] Don't use MessageLoop threads with APZ. 
- [sailfishos][embedlite] Enable CCS touch action handling to EmbedLiteViewChild. 
- [sailfishos][embedlite] Explicitly include unistd.h for getpid(). 
- [sailfishos][embedlite] Export mozsqlite3 library to base package. 
- [sailfishos][embedlite] Fix crash coming RecvSetIsActive calling RecvScheduleUpdate. 
- [sailfishos][embedlite] Fix crash from EmbedLiteAppService::GetIDByWindow. 
- [sailfishos][embedlite] Fix crash from EmbedLiteViewChild::RecvSetIsActive. 
- [sailfishos][embedlite] Fix CreateExposableURI call in WebBrowserChrome::OnLocationChange. 
- [sailfishos][embedlite] Fix EmbedLiteViewChild::RecvSuspendTimeouts and EmbedLiteViewChild::RecvResumeTimeouts. 
- [sailfishos][embedlite] Fix EmbedWidgetFactoryRegister init. 
- [sailfishos][embedlite] Fix empty nspr version requirement in libxul.pc. 
- [sailfishos][embedlite] Fix flipped FBO textures when rendering to an offscreen window. 
- [sailfishos][embedlite] Fix for progress listener. 
- [sailfishos][embedlite] Fix getting pointer to nsPresContext trough nsIDocShell in BrowserChildHelper. 
- [sailfishos][embedlite] Fix including of EmbedLiteView.h in EmbedLiteViewIface.idl. 
- [sailfishos][embedlite] Fix InitializeUserPrefs call in GeckoLoader::InitEmbedding. 
- [sailfishos][embedlite] Fix JS_ReadStructuredClone calls in BrowserChildHelper. 
- [sailfishos][embedlite] Fix LayerManager::BeginTransaction override in EmbedLiteAppProcessParentManager. 
- [sailfishos][embedlite] Fix LogModule initialization in EmbedLiteApp. 
- [sailfishos][embedlite] Fix mesa egl display initialisation
- [sailfishos][embedlite] Fix nsFrameMessageManager usage in BrowserChildHelper. 
- [sailfishos][embedlite] Fix nsMessageManagerScriptExecutor::LoadScriptInternal usage in BrowserChildHelper. 
- [sailfishos][embedlite] Fix overriding of nsIWidget::SetFocus in PuppetWidgetBase. 
- [sailfishos][embedlite] Fix path to packager.mk. 
- [sailfishos][embedlite] Get rid of nsIDOMScrollAreaEvent. 
- [sailfishos][embedlite] Get rid of nsIWindowCreator2. 
- [sailfishos][embedlite] Group the results of APZInputBridge::ReceiveInputEvent into a struct. 
- [sailfishos][embedlite] Implement BrowserChildHelperMessageManager for BrowserChildHelper. 
- [sailfishos][embedlite] Include embedlite directory in the project through the symlink '/mobile/sailfishos'. 
- [sailfishos][embedlite] Initialize profiler properly. 
- [sailfishos][embedlite] Introduce EmbedLiteAppParent interface. 
- [sailfishos][embedlite] Move ContentFrameMessageManager usage in EmbedFrame under mozilla::dom namespace. 
- [sailfishos][embedlite] Pass aTargets to NewRunnableMethod in RecvSetTargetAPZC by rvalue reference. 
- [sailfishos][embedlite] Pass LayersId object to SendPLayerTransactionConstructor. 
- [sailfishos][embedlite] Pass LayersId to SendSetTargetAPZCNotification instead of ScrollableLayerGuid. 
- [sailfishos][embedlite] Pass nsTArray to aServerCert->GetRawDER call in EmbedLiteSecurity::importState. 
- [sailfishos][embedlite] Provide BrowsingContext for nsWebBrowser::Create. 
- [sailfishos][embedlite] Reduce usage of mozilla::layers::FrameMetrics in embedlite. 
- [sailfishos][embedlite] Reenable layers.progressive-paint. 
- [sailfishos][embedlite] Remove APZCCallbackHelper::ApplyCallbackTransform usage. 
- [sailfishos][embedlite] Remove deprecated configuration options. 
- [sailfishos][embedlite] Remove `#include "nsAutoPtr.h"` from embedlite. 
- [sailfishos][embedlite] Remove `#include "nsIDOMDocument.h"` from embedlite. 
- [sailfishos][embedlite] Remove include of signing.mk from installer makefile. 
- [sailfishos][embedlite] Remove inheritence from TabChildBase. 
- [sailfishos][embedlite] Remove JS request API usage in BrowserChildHelper. 
- [sailfishos][embedlite] Remove now unused gfxPrefs. 
- [sailfishos][embedlite] Remove redundant uses of do_QueryInterface. 
- [sailfishos][embedlite] Remove unused #include from qmessagepump.h. 
- [sailfishos][embedlite] Remove unused ScrollableLayerGuid parameter. 
- [sailfishos][embedlite] Remove usage of nsISSLStatus and nsISSLStatusProvider. 
- [sailfishos][embedlite] Rename KeyboardEventBinding to KeyboardEvent_Binding. 
- [sailfishos][embedlite] Rename NS_STRINGIFY to MOZ_STRINGIFY. 
- [sailfishos][embedlite] Rename TabChildHelper to BrowserChildHelper to match naming in gecko. 
- [sailfishos][embedlite] Replace CompositorBridgeParent::SetEGLSurfaceSize usage with CompositorBridgeParent::SetEGLSurfaceRect. 
- [sailfishos][embedlite] Replace CompositorThreadHolder usage with CompositorThread. 
- [sailfishos][embedlite] Replace FrameMetrics usage with RepaintRequest in EmbedContentController::RequestContentRepaint. 
- [sailfishos][embedlite] Replace GetFocusedContent usage with GetFocusedElement. 
- [sailfishos][embedlite] Replace InfallibleTArray usage with nsTArray. 
- [sailfishos][embedlite] Replace Link::SetLinkState(eLinkState_Visited) with Link::VisitedQueryFinished. 
- [sailfishos][embedlite] Replace MOZ_FALLTHROUGH usage with [[fallthrough]]. 
- [sailfishos][embedlite] Replace mozilla::dom::ScreenOrientationInternal with hal::ScreenOrientation. 
- [sailfishos][embedlite] Replace mozilla::Move usage with std::move. 
- [sailfishos][embedlite] Replace nsIContentFrameMessageManager with ContentFrameMessageManager. 
- [sailfishos][embedlite] Replace nsIDocShellTreeItem::GetRootTreeItem usage with GetInProcessRootTreeItem. 
- [sailfishos][embedlite] Replace nsIDocument::GetDefaultView() usage with GetWindow(). 
- [sailfishos][embedlite] Replace nsIDocument usage with Document. 
- [sailfishos][embedlite] Replace nsIDOMEventTarget with EventTarget. 
- [sailfishos][embedlite] Replace nsIDOMEvent usage with Event. 
- [sailfishos][embedlite] Replace nsIDOMMouseEvent::MOZ_SOURCE_TOUCH usage with MouseEvent_Binding::MOZ_SOURCE_TOUCH. 
- [sailfishos][embedlite] Replace nsIMessageBroadcaster usage with ChromeMessageBroadcaster. 
- [sailfishos][embedlite] Replace nsIPresShell usage with PresShell. 
- [sailfishos][embedlite] Replace nsITabChild usage with nsIBrowserChild. 
- [sailfishos][embedlite] Replace nsIWebBrowserChrome2 usage with nsIWebBrowserChrome. 
- [sailfishos][embedlite] Replace nsIWebBrowser usage with nsWebBrowser. 
- [sailfishos][embedlite] Replace nsPIDOMWindowOuter::GetTop usage with GetInProcessTop. 
- [sailfishos][embedlite] Replace SameProcessDifferentThread with SameProcess in BrowserChildHelper. 
- [sailfishos][embedlite] Set '--disable-nodejs' configuration option. 
- [sailfishos][embedlite] Support custom http user agent string management. 
- [sailfishos][embedlite] Switch to use nsIDocShell::isActive attribute instead of nsIWebBrowser::isActive. 
- [sailfishos][embedlite] Synchronize GeckoChildProcessHost destruction with launching. 
- [sailfishos][embedlite] Use layers::LayersId type for layer IDs in embedlite. 
- [sailfishos][embedlite] Use LoadURIOptions object to pass options to LoadURI. 
- [sailfishos][embedlite] Use move semantic in work with IPC::Channel. 
- [sailfishos][embedlite] Use move semantic to assign mPrefs in EmbedLiteAppProcessParent::RecvPrefsArrayInitialized. 
- [sailfishos][embedlite] Use MOZ_APP_VERSION instead of FIREFOX_VERSION. 
- [sailfishos][embedlite] Use nsTArray type for aFlavorList parameter of nsEmbedClipboard::HasDataMatchingFlavors. 
- [sailfishos][embedlite] Use nsWebBrowser to focus active window. 
- [sailfishos][fonts] Load and set FTLibrary for the Factory. 
- [sailfishos][gecko] Adapt patch "Backport Embed MessageLoop contructor back". 
- [sailfishos][gecko] Adapt patch "Bring back Qt layer". 
- [sailfishos][gecko] Adapt patch "Enable Pango for the build". 
- [sailfishos][gecko] Adapt patch "Fix embedlite building". 
- [sailfishos][gecko] Adapt patch "Fix GLContextProvider defines". 
- [sailfishos][gecko] Adapt patch "Hackish fix for preferences usage in Parent process". 
- [sailfishos][gecko] Adapt patch "Make it possible to extend CompositorBridgeParent". 
- [sailfishos][gecko] Add including of nsRefPtrHashtable.h to GamepadEventChannelChild.h. 
- [sailfishos][gecko] Add missing GetTotalScreenPixels for screen manager. 
- [sailfishos][gecko] Add missing #include for nsIObserver and startupObserver. 
- [sailfishos][gecko] Add symlink to embedlite. 
- [sailfishos][gecko] Backport: "building with --disable-marionette fails with compile error" fix. 
- [sailfishos][gecko] Bring back: 'Avoid incorrect compiler optimisation' patch. 
- [sailfishos][gecko] Bring SDK back. 
- [sailfishos][gecko] Bump up to latest esr78 version. 
- [sailfishos][gecko] Comment out Preferences::GetPreferences usage. 
- [sailfishos][gecko] Disable Gecko Rust Feature cubeb-remoting. 
- [sailfishos][gecko] Disable MOC code generation for message_pump_qt. 
- [sailfishos][gecko] Disable unaligned FP access emulation on ARM for WebAssembly. 
- [sailfishos][gecko] Drop patch "Respect - gfxPrefs::ClearCompoisitorContext for clearing". 
- [sailfishos][gecko] Drop static casting from BrowserChild. 
- [sailfishos][gecko][embedlite] Bring SDK back in esr78 build. 
- [sailfishos][gecko] Enable compile-environment as that guards use of system libs. 
- [sailfishos][gecko] Fix for esr78 i486 configure, 
- [sailfishos][gecko] Fix GeckoChildProcessHost build errors. 
- [sailfishos][gecko] Fix gfxPlatform::AsyncPanZoomEnabled for embedlite. 
- [sailfishos][gecko] Force MOZ_BUILD_DATE env var in order to have more reproducible builds 
- [sailfishos][gecko] Force to build mozglue and xpcomglue static libraries. 
- [sailfishos][gecko] Only set --without-thumb for arm32. 
- [sailfishos][gecko] Only use rust SB vars for arm and aarch64. 
- [sailfishos][gecko] Remove static registration of the 'mozilla/places/History.h' module. 
- [sailfishos][gecko] Remove x11 dependency declaration for gfx-backend-vulkan. 
- [sailfishos][gecko] Use system library for libwebp 
- [sailfishos][gecko] Use updated nasm. 
- [sailfishos][ipc] Whitelist sync messages of EmbedLite. 
- [sailfishos][mozglue] Adapt patch "Introduce EmbedInitGlue to the mozglue". 
- [sailfishos][packaging] Add explicit nss dependencies to the devel package. 
- [sailfishos][packaging] Fix SDK build regression introduced with MOZ_BUILD_DATE commit 
- [sailfishos][packaging] Remove duplicated SB2 env vars. 
- [sailfishos][packaging] Update submodule url. 
- [sailfishos][qt] Adapt "Bring back Qt layer" patch for esr78, part 1. 
- [sailfishos][qt] Adapt "Bring back Qt layer" patch for esr78, part 2. 
- [sailfishos][qt] Adapt "Bring back Qt layer" patch for esr78, part 3. 
- [sailfishos][qt] Adapt GfxInfo to nsIGfxInfo and GfxInfoBase. 
- [sailfishos][qt] Adapt gfxQtPlatform to base class gfxPlatform. 
- [sailfishos][qt] Adapt nsClipboard to nsTransferable. 
- [sailfishos][qt] Adapt nsLookAndFeel to LookAndFeel and nsXPLookAndFeel. 
- [sailfishos][qt] Adapt nsWindow to nsIWidget. 
- [sailfishos][qt] Adapt patch "Provide checkbox/radio renderer for Sailfish OS". 
- [sailfishos][qt] Add missing #include for do_CreateInstance. 
- [sailfishos][qt] Add nsIWidget::CreateBidiKeyboardInner implementation to nsBidiKeyboard. 
- [sailfishos][qt] Add Qt headers to system headers. 
- [sailfishos][qt] Allow Cairo as content/canvas backend for MOZ_WIDGET_QT
- [sailfishos][qt] Convert nsWidgetQtModule to static registration. 
- [sailfishos][qt] Drop nsQtNetworkLinkService in favor of linux common nsNetworkLinkService. 
- [sailfishos][qt] Fix nsPrimitiveHelpers::CreateDataFromPrimitive call in nsClipboard. 
- [sailfishos][qt] Include LinuxProcessLauncher::DoSetup implementation for MOZ_WIDGET_QT. 
- [sailfishos][qt] Introduce MediaKeysEventSourceFactory. 
- [sailfishos][qt] Introduce ProcInfo. 
- [sailfishos][qt] Move `#include <qclipboard.h>` from nsClipboard.h to nsClipboard.cpp. 
- [sailfishos][qt] Move NullPrincipal under mozilla namespace. 
- [sailfishos][qt] Remove nsIWebBrowserPrint usage from nsPrintDialogQt. 
- [sailfishos][qt] Replace non-asserting NS_PRECONDITIONs with MOZ_ASSERTs. 
- [sailfishos][qt] Replace nsCOMPtr<nsIArray> with nsTArray<nsCString> in GetNativeClipboardData. 
- [sailfishos][qt] Replace nsCOMPtr<nsIArray> with nsTArray<nsCString> in SetNativeClipboardData. 
- [sailfishos][qt] Replace nsGeolocation usage with Geolocation and nsGeoPosition with GeolocationPosition. 
- [sailfishos][qt] Replace nsIDOMWheelEvent usage with WheelEvent_Binding. 
- [sailfishos][qt] Replace NullPrincipal::Create usage with NullPrincipal::CreateWithoutOriginAttributes. 
- [sailfishos][qt] Revert and adapt "Remove unneeded QT-related rules and configure bits". 
- [sailfishos][qt] Sort the #include statements in nsQAppInstance.cpp. 
- [sailfishos][qt] Switch aFlavorList parameter of the nsClipboard::HasDataMatchingFlavors to type nsTArray<nsCString>. 
- [sailfishos][qt] Use gfxPlatform::GetBackendPrefs to pass prefs in InitBackendPrefs. 
- [sailfishos][qt] Use Span in constructing a byte input stream in nsClipboard. 
- [sailfishos][rpm] Add clang-devel to build requirements. 
- [sailfishos][rpm] Add libatomic to build requirements. 
- [sailfishos][rpm] Add libicu to build requirements. 
- [sailfishos][rpm] Add python3-sqlite to build requirements. 
- [sailfishos][rpm] Bump up the required nspr version to 4.25.0. 
- [sailfishos][rpm] Bump up the required nss version to 3.53.1. 
- [sailfishos][rpm] Define CARGO_HOME under build dir. 
- [sailfishos][rpm] Fix obj-build-dir path. 
- [sailfishos][rpm] Move none adapted esr60 patches under old-patches. 
- [sailfishos][rpm] Set minimum required libpng version to 1.6.35. 
- [sailfishos][rpm] Update esr78 build requirements. 
- [sailfishos][rpm] Update packaging for 78.8.0. 
### yamuisplash
- Updated : 1.0.1-1.3.1.jolla -- 1.0.2-1.4.1.jolla
- [packaging] BuildRequire systemd via pkgconfig. 

# PACKAGES ADDED

### amber-mpris
- Binaries added : amber-qml-plugin-mpris - 1.1.1.3-1.5.2.jolla, amber-qml-plugin-mpris-doc - 1.1.1.3-1.5.2.jolla, amber-mpris - 1.1.1.3-1.5.2.jolla, amber-mpris-devel - 1.1.1.3-1.5.2.jolla
- [amber-mpris] Remove the deprecated loop enums. 
- [amber-mpris] Rename loop enums with more context. 
- [mpris] Properly clean up when playing client quits. 
- [mpris] Update plugins.qmltypes. 
- [mpris] Document the QML API. 
- [mpris] Rewrite from mprisqt. 
- [mpris] Remove qml dependency from c++ lib. 
- [mpris] Add build option to use system dbus. 
- [qtmpris] Switch to integrated build of qtdbusextended. 
- [qt] Replace Qt keywords with macros. 
- [license] Package license file, fix license shortname. 
- [qtmpris] Update plugins.qmltypes. 
- [qtmpris] Fixed pkgconfig version, 
- [qtmpris] Add plugins.qmltypes. 
- [qtmpris] Fix DBus registration order. 
- [qtmpris] Avoid creating unnecessary warnings when instantiating MPrisPlayer. 
- [license] Unify open source licenses. 
- [player] Unregister from DBus upon destruction. Fixes MER#1350
- [release] Bumped version to 0.0.5
- [mpris] Missing bits for Mpris singleton in the examples. Fixes MER#1156
- [rpm] Released 0.0.4
- [mpris] Made the Mpris void class a singleton. Fixes MER#1090
- [examples] Added initial examples
- [interface] Added async and GetAll methods
- [interface] Function pointer syntax in dis/connect for better performance
- [rpm] Released 0.0.2
- [adaptor] Added the adaptor
- [interface] Added the interface
- [rpm] Packaging and released 0.0.1
- [xml] MPRIS DBus specification
### binder-utils
- Binaries added : binder-utils - 1.0.0-1.2.1.jolla
- [utils] Add binder-add. 
### droid-config-xqbt52
- Binaries added : droid-config-xqbt52-sailfish - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-pulseaudio-settings - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-bluez5 - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52 - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-kickstart-configuration - 1.8.2.5-1.10.1.jolla, patterns-sailfish-device-configuration-common-xqbt52 - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-policy-settings - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-flashing - 1.8.2.5-1.10.1.jolla, patterns-sailfish-device-configuration-xqbt52 - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-ssu-kickstarts - 1.8.2.5-1.10.1.jolla, patterns-sailfish-device-adaptation-pdx213 - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-out-of-image-files - 1.8.2.5-1.10.1.jolla, droid-config-xqbt52-preinit-plugin - 1.8.2.5-1.10.1.jolla
- [configs] Fix SIM detection on boot by updating 4.4.0 to new telephony. 
- [configs] Package ofono-binder-plugin. 
- [configs] Add memnotify configuration. 
- [configs] Disable lid sensor (Hall sensor). 
- [configs] Add PulseAudio configs. 
- [configs] Add workaround for VOIP sink. 
- [configs] Add xpolicy.conf from 1.9.0.
- [configs] Modify voice call volume levels. 
- [flash] Update Sony binary version requirement. 
- [camera] Fix labels of 0.6 and 2.0 cameras. 
- [flash-on-windows] bump SW binaries version to v8a. 
- [boot] bump SW binaries version to v8a. 
- [lib] Install oneshot scripts under /usr/lib. 
- [patterns] Add configuration to modify installed sailfish patterns.
- [configs] Enable mouse input for lipstick homescreen. 
- [configs] move lipstick env file to general sparse. 
- [configs] move vendor-specific sparse to separate submodule. 
- [udev] Add missing path to firmware loader script. 
- [lena] Initial content for Xperia 10 III. 
### droid-hal-pdx213
- Binaries added : droid-hal-pdx213 - 1.8.4-1.6.1.jolla, droid-hal-pdx213-tools - 1.8.4-1.6.1.jolla, droid-hal-pdx213-kernel-modules - 1.8.4-1.6.1.jolla, droid-hal-pdx213-kernel-dtbo - 1.8.4-1.6.1.jolla, droid-hal-pdx213-detritus - 1.8.4-1.6.1.jolla, droid-hal-pdx213-users - 1.8.4-1.6.1.jolla, droid-hal-pdx213-devel - 1.8.4-1.6.1.jolla, droid-hal-pdx213-kernel - 1.8.4-1.6.1.jolla
- [kernel] Update from upstream. 
- [kernel] Update submodules. 
- [hybris-patches] common-kernel patch is now upstream. 
- [helpers] fix local build of pulseaudio-modules-droid-hidl. 
- [kernel] Add video hardware codec module, upstream updates. 
- [kernel] Fix SIM-card detection of 2nd SIM slot, upstream updates. 
- [dhd] BuildRequire systemd via pkgconfig. 
- [dhd] dhd: Fix typo in default skip %{makefstab_skip_entries}. 
- [helpers] fix internal localbuilds. 
- [helpers] take droidmedia-devel from hw common repo. 
- [helpers] take gmp-droid from hw common repo. 
- [helpers] take gst-droid from hw common repo. 
- [kernel] update from Sony to 4.19.188. 
- [libhybris] hybris: common: o: Fix incorrect variable name.
- [kernel] fix random restarts on boot. 
- [droid-hal] Add initial support for lena (Xperia 10 III). 
### droid-hal-pdx213-img-boot
- Binaries added : droid-hal-pdx213-img-recovery - 1.1.0-1.3.18.jolla, droid-hal-pdx213-img-boot - 1.1.0-1.3.18.jolla
- [img-boot] Remove msm_drm.blhack_dsi_display0 from cmdline. 
- [img-boot] Initial content for Xperia 10 III. 
### droid-hal-prjconf-sony-lena
- Binaries added : droid-hal-prjconf-sony-lena - 1.0.0-1.2.1.jolla
- [prjconf] Initial content for Xperia 10 III. 
### droid-hal-version-xqbt52
- Binaries added : droid-hal-version-xqbt52 - 1.0.0-1.2.114.jolla, droid-hal-version-xqbt52-doc - 1.0.0-1.2.114.jolla
- [version] Initial content for Xperia 10 III. 
### droid-src-sony-lena
- Binaries added : droid-src-sony-lena-build - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-clang-tools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-r8 - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-jdk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-dhs-rootdir - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-build-tools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-external - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-rust-linux-x86 - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-ndk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-bootable - 1.8.4-1.5.3.jolla, droid-src-sony-lena-development - 1.8.4-1.5.3.jolla, droid-src-sony-lena-vendor - 1.8.4-1.5.3.jolla, droid-src-sony-lena-developers - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-abi-dumps - 1.8.4-1.5.3.jolla, droid-src-sony-lena-sdk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-ktlint - 1.8.4-1.5.3.jolla, droid-src-sony-lena-system - 1.8.4-1.5.3.jolla, droid-src-sony-lena-packages - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-gcc - 1.8.4-1.5.3.jolla, droid-src-sony-lena-device - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-tools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-sdk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-toolchain - 1.8.4-1.5.3.jolla, droid-src-sony-lena-hardware - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-bundletool - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-checkstyle - 1.8.4-1.5.3.jolla, droid-src-sony-lena-cts - 1.8.4-1.5.3.jolla, droid-src-sony-lena-platform_testing - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-misc - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-go - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-asuite - 1.8.4-1.5.3.jolla, droid-src-sony-lena-test - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-fuchsia_sdk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-checkcolor - 1.8.4-1.5.3.jolla, droid-src-sony-lena-frameworks - 1.8.4-1.5.3.jolla, droid-src-sony-lena-kernel - 1.8.4-1.5.3.jolla, droid-src-sony-lena-bionic - 1.8.4-1.5.3.jolla, droid-src-sony-lena-tools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-vndk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-python - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-manifest-merger - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-devtools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-dhs-full - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-cmdline-tools - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-clang - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-maven_repo - 1.8.4-1.5.3.jolla, droid-src-sony-lena-dalvik - 1.8.4-1.5.3.jolla, droid-src-sony-lena-dhs-utils - 1.8.4-1.5.3.jolla, droid-src-sony-lena-pdk - 1.8.4-1.5.3.jolla, droid-src-sony-lena-libnativehelper - 1.8.4-1.5.3.jolla, droid-src-sony-lena-dhs-makefile - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-gdb - 1.8.4-1.5.3.jolla, droid-src-sony-lena-libcore - 1.8.4-1.5.3.jolla, droid-src-sony-lena-art - 1.8.4-1.5.3.jolla, droid-src-sony-lena-prebuilts-gradle-plugin - 1.8.4-1.5.3.jolla
- [manifest] Add missing ODM Camera features. 
- [manifest] Update build kernel script. 
- [manifest] Sync, pull in configs for media hal to use hardware codecs. 
- [manifest] fix device not booting after 7 reboots. 
- [manifest] temporarily introduce manifest versioning. 
- [manifest] manifest: Fix packages/apps/ExtendedSetting branch. 
- [manifest] manifest: Fix vendor/qcom/opensource/usb source repo. 
- [manifest] simplify local build. 
- [manifest] Sync Sony repos with Sony. 
- [manifest] update from Sony. 
- [manifest] Update repository with broken submodule failing cloning. 
- [manifest] Update to latest Android 11 release. 
- [droid-src] Initial content for Android 11. 
### droid-system-pdx213
- Binaries added : droid-system-pdx213 - 1.9.1-1.7.1.jolla
- [hybris] device: sony: common: Workaround when sensor hal starts too early. 
- [hybris] device: sony: common: Workaround when qcrild starts too early. 
- [sparse] update against Sony's 11.0.0_r46 on 20220204. 
- [sparse] fix device not booting after 7 reboots. 
- [sparse] Split vendor/odm/etc/build.prop into a separate file. 
- [sparse] update against Sony's 11.0.0_r46 on 20211209. 
- [lena] add system, system_ext and vendor binaries. 
### droid-system-pdx213-xqbt52
- Binaries added : droid-system-pdx213-xqbt52 - 1.9.1-1.7.1.jolla
- [hybris] device: sony: common: Workaround when sensor hal starts too early. 
- [hybris] device: sony: common: Workaround when qcrild starts too early. 
- [sparse] update against Sony's 11.0.0_r46 on 20220204. 
- [sparse] fix device not booting after 7 reboots. 
- [sparse] Split vendor/odm/etc/build.prop into a separate file. 
- [sparse] update against Sony's 11.0.0_r46 on 20211209. 
- [lena] add system, system_ext and vendor binaries. 
### gnu-which
- Binaries added : gnu-which - 2.21+git2-1.2.1.jolla
- [which] Provide which. 
- [which] Initial packaging. 
### libxcrypt
- Binaries added : libxcrypt-devel - 4.4.23+git1-1.2.1.jolla, libxcrypt - 4.4.23+git1-1.2.1.jolla, libxcrypt-compat - 4.4.23+git1-1.2.1.jolla
- [libxcrypt] Initial packaging based on Fedora. 
### lua-posix
- Binaries added : lua-posix - 35.0.1+git2-1.2.1.jolla
- [packaging] Pull in libcrypt for crypt function. 
- [lua-posix] Initial packaging. 
### ofono-binder-plugin
- Binaries added : ofono-configs-binder - 1.0.2-1.1.1.jolla, ofono-binder-plugin - 1.0.2-1.1.1.jolla
- [ofono-binder] Wait for IRadioConfig service at startup. 
- [ofono-binder] Handle various config corner cases. 
- [ofono-binder] Initial implementation. 
### sailfish-aml
- Binaries added : sailfish-aml - 1.0.2+git1-1.1.1.jolla, sailfish-aml-data - 1.0.2+git1-1.1.1.jolla
- [aml] Set 4.4.0 version requirements for Ofono and libmce. 
- [aml] Change default SMS data port to 48000. 
- [aml] Support setting endianess with GSMEndianess. 
- [aml] Version 1.0.2, require Ofono 1.28+git5. 
- [data] Add European country DB according to EENA.org. 
- [process] Use DATA_DIR set at buildtime. 
- [unit] Update unit test to use GSMEndianess. 
- [aml] Use libkeepalive to ensure wakeups every 1 second. 
- [aml] Fix AML message format. 
- [aml] GSM 7-bit packing implementation. 
- [aml] Implement first version of AML process
- [aml] Move D-Bus related common code to aml_dbus.{c,h}. 
- [aml] Set license to proprietary. 
- [aml] Stage 1 with data, core, battery monitor and basic Geoclue location. 
- [aml] Use new battery monitor, unify aml start process. 
- [battery monitor] Implement battery monitoring with libmce-glib. 
- [dbus] Add helper to send D-Bus sync message. 
- [dbus] Drop call id from D-Bus params, use GetCalls to get vc path. 
- [dbus] Use little endian for SMS data message. 
- [packaging] Fix build requires and versions. 
- [plugin] Add retrieval of IMEI, MCC, MNC and call id from Ofono. 
- [plugin] Allow to use phone number overrides for testing. 
- [plugin] Drop call id use. 
- [position] Implement basic position support with Geoclue 
- [process] Add finish option to process stop and fix position use. 
- [process] Fix battery resume cases to set correct interval. 
- [unit] Adapt process tests to position changes and cleanup. 
- [unit] Adapt to process changes, move main makefile to common. 
- [unit] Add basic unit tests for aml_process.c. 
- [unit] Add battery monitor tests. 
- [unit] Add process resume tests. 
- [unit] Add simple util tests. 
- [unit] Create position tests and simulate Geoclue, add libs to makefiles. 
- [util] Fix broken 7bit GSM encoding. 
### sailfish-qdoc-template
- Binaries added : sailfish-qdoc-template-doc - 0.1.0-1.2.2.jolla, sailfish-qdoc-template - 0.1.0-1.2.2.jolla
- [mer-qdoc-template] Add common Qt defines and similar. 
- [mer-qdoc-template] Add packaging. Contributes to MER#1194
- [mer-qdoc-template] Adjust template for use with QTextBrowser. 
- [mer-qdoc-template] Do not hide overflowed pre content
- [mer-qdoc-template] Ensure link to index page is always available. Contribute to 
- [mer-qdoc-template] Fix qdoc getting confused on new Qt macros. 
- [mer-qdoc-template] Hide next-previous page links
- [mer-qdoc-template] Increase space around headings
- [mer-qdoc-template] Install to /usr/share/mer-qdoc-template. 
- [mer-qdoc-template] Let qdoc ignore Q_DECLARE_LOGGING_CATEGORY. 
- [mer-qdoc-template] Stick QML name and description together
- [mer-qdoc-template] Sync common configs with QtBase 5.6. 
- [sailfish-qdoc-template] Rename from mer version. 
### systemd-mini
- Binaries added : systemd-mini-config-mer - 238+git13-1.2.1.jolla, systemd-mini-libs - 238+git13-1.2.1.jolla, systemd-mini-devel - 238+git13-1.2.1.jolla, systemd-mini - 238+git13-1.2.1.jolla, systemd-mini-analyze - 238+git13-1.2.1.jolla
- [systemd] Add workaround for OBS dependency problem for building systemd. 
- [packaging] Fix typo
- [packaging] Fix typo. 
- [packaging] Add missing files to sources
- [systemd] Add bootstrap build condition. 
- [systemd] Add libstdc++-devel needed to build. 
- [systemd] Add script to generate bootstrap variant spec. 
- [systemd-mini] Generate spec file. 
- [systemd] Explicitly depend on pkgconfig(libcrypt). 
- [systemd] Fix build with meson 0.57.2. 
- [systemd] journald: Retry if posix_fallocate returned -1 (EINTR). 
- [systemd] Return back pam_limits.so to systemd-user. 
- [systemd] Fix CVE-2020-1712. 
- [systemd] Fix firmware events handling by udev. 
- [systemd] Backport adding new system-update-pre.target. 
- [systemd] Backport removing support for API bus "started outside our own logic". 
- [systemd] Removing support for API bus "started outside our own logic".
- [systemd] Upgrade systemd to v238. 
- [systemd] Add gperf 3.1 compatibility patch. 
- [systemd] Fix system units in posttrans. 
- [systemd] Fix system units which still point to /lib inside /etc/systemd/system. 
- [systemd] Cleanup /lib/systemd symlink workaround. 
- [systemd] Fix systemctl-user script. 
- [systemd] Fix /sbin/init symlink. 
- [aarch64] Make sure that files end up in the same place regardless of bits. 
- [systemd] Fix sd_seat_get_sessions. 
- [systemd] Fix systemd pam library install location. 
- [systemd] Systemd-analyze doesn't use python anymore. 
- [packaging] Update config as per policy.
- [systemd] Enable audit support. 
- [systemd] Enable selinux support. 
- [systemd] Fix CVE-2019-3842. 
- [systemd] Fix for CVE-2013-4391. Decrease DATA_SIZE_MAX. 
- [systemd] Fix for CVE-2016-7795. 
- [systemd] Fix for CVE-2018-16865 in systemd-journal. 
- [systemd] Fix for CVE-2018-16866. fix syslog_parse_identifier(). 
- [systemd] Require which. 
- [systemd] Fix timestamps in udev. 
- [systemd] Skip extra BindsTo in systemd-cryptsetup-generator. 
- [systemd] Ghost own the /etc/crypttab. 
- [systemd] Fix build with glibc-2.28. Fixes MER#2034
- [systemd] Create and own /etc/crypttab. 
- [systemd] Enable cryptsetup. 
- [packaging] Rename systemd-docs to system-doc. 
- [systemd] Fix for CVE-2018-15688 in DHCP6 client. 
- [systemd] Disable lto for now. Contributes MER#1985
- [systemd] backported some serialization security fixes. 
- [systemd] Install an empty machine-id. Contribute to 
- [PATCH] core: downgrade "Time has been changed" to debug
- [PATCH] shutup 'Time has been changed messages' in journal info
- [systemd] Integrate systemd patch to reduce logging. 
- [systemd] Avoid occassional boot hangups. 
- [pam_systemd] Add timeout=<seconds> argument. 
- [systemd] Add explicit disables for things that were disabled on clean builds.
- [systemd] Drop: machined and importd. 
- [systemd] Drop: nss-myhostname, sysv init compat, hibernate. 
- [systemd] Drop: quotacheck, firstboot, backlight. 
- [systemd] Drop: timedated, localed, networkd. 
- [systemd] Drop: zsh completions. 
- [systemd] Disable rfkill. 
- [systemd] Disable timesyncd and resolved. 
- [security] Addresses CVE-2015-8842
- [update] Upgrade systemd to v225. Fixes MER#608
- [packaging] Drop unneeded usbutils build dep. 
- [systemd] Add ./.libs to library linking path. Fixes MER#1612
- [spec] Add psmisc dependecy because of used pidof tool. 
- [bootchart] Add upstream patch to fix bootchart crash. 
- [packaging] Fix wrong months in systemd.changes. 
- [packaging] Add libtool to BuildRequires in .spec. 
- [PATCH] [packaging] Add libtool to BuildRequires in .spec. 
- [patch] Add patch from upstream: Don't wait for new data from the sensor
- [systemd] Fix potential boot delay and cause for boot failures. Fixes MER#1088
- [patch] Remove unused systemd-187-reintroduce-support-for-deprecated-oom.patchpatch
- [patch] Support additional argument in reboot

- [patch] Add do-not-pull-4-megs-from-stack-for-journal-send-test patch
- [patch] Added systemd-208-count-only-restarts.patch
- [new-patch] Added systemd-208-fix-restart.patch to fix restart logic

- [tests] Update tests.xml to match systemd version 208 tests
- [new-patch] Added support to configurable timemouts and startlimits
- [packaging] bootchart.conf moved to systemd-config-mer package
- [rpm macros] support old rpm macro location
- [update] Update to systemd version 208.
- Updated to version 187
- Require filesystem >= 3 as /run was moved to that package.
- Require util-linux >= 2.21.2 because of fsck.
- Added systemd-187-reintroduce-support-for-deprecated-oom.patch to
readd support for older kernels.
- Require network.target with multi-user.target.
- Prep for user sessions:
- make sure video owns tty and input devices, for xorg startup
- don't start tty1 automatically
- exclude /usr/lib/systemd/user/default.target - vendors provide that
- Fix tty1 autostart by excluding the file in /etc/systemd/system/getty.target.wants/
- Added file /lib/systemd/system/systemd-stop-user-sessions.service
Fixes NEMO#502: Shutdown is not working properly when systemd user session is used
- Disable collecting core dumps in journal
- Add systemd-187-make-readahead-depend-on-sysinit.patch by Thilo Fromm to sort out readahead
- Renamed -tools package to -analyze.
- Fixes MER#82: Change pycairo to python-cairo dependency in -analyze.
- Added support for EnvironmentDir in .service files.
systemd-187-support-env-dirs.patch
Fixes MER#640 : systemd .service files should support EnvironmentDir option
- EnvironmentDir support is replaced with globbing support in EnvironmentFile
deleted systemd-187-support-env-dirs.patch
added systemd-187-support-glob-EnvironmentFile.patch
Fixes MER#640 : systemd .service files should support EnvironmentDir option
- Add test package for upstream tests with tests.xml
- Added helper script systemctl-user
It can be used to run \"systemctl --user\" commands when logged in as root
- Systemd config files separated to new package called systemd-config-mer
Vendors can replace this package with their own configuration by
having a package that \"Provides: systemd-config\"
- default.target is also moved into this config package
- Removed link /etc/systemd/system/multi-user.target.wants/remote-fs.target
- Removed need for display-manager.service in graphical.target
- Add traditional droid paths to firmware searches
- configure.ac: fix FTBFS with new glibc
- Fixes MER#364: Upgrade to 185, now includes udev
- Fixes MER#114: Update systemd to newer version
- New upstream version 37
- ExecStart patch accepted upstream
- kbd-model-map packaged
- Moved consoles from sysinit.target.wants to getty.target.wants
- Restore /run directory
- Add ttyAMA0 system console ability
- Update to version 35
- Removed hwclock-load.service link creation as destination does not exist anymore.
- Moved %fdupes under %install to fix BMC#22706
- Added systemd-35-execstart-line-rescue-service.patch to
fix multiple ExecStart lines in rescue.service.
- updated to version 30, and udpate patch set in MeeGo.
- Cosmetic cleanups
- Disabling internal logger as it's nonfunctional - we'll fall
back to dmesg logging only for now.
- With systemd-loginctl we no longer need to pre-activate tty2
- Vala isn't needed to build because we disable building the gtk UI app.
- Fix several rpmlint warnings (perms, %config out of place).
- Fix rpm group names.
- Rename -analyze subpackage to -tools. There will likely be more dev tools coming.
- Enable ACL dependency, we really want to use it going forward.
- Run %fdupes.
- Disable tcp_wrappers dependency as we don't use it in MeeGo.
- Remove libnotify dependancy, drags in gtk+ and other
things.
- updated to 29
- removed provides and obsolete of removed packages as they are not needed
- BMC#18652 - Separate packages for hardware adaptation serials
- added install alias to serial-getty unit file
- udpate to 28
- split out the systemd-analyze tool into a separate subpackage, as it
requires python/pycairo to run
- split out the systemd man pages into separate subpackages
- Update to -25
- sysvinit hack until sysvinit get removed
- Update to 26
- add a syslog daemon inside systemd
- Updated to -20
- Initial automated packaging
### zstd
- Binaries added : libzstd - 1.5.0+git1-1.1.14.jolla, libzstd-static - 1.5.0+git1-1.1.14.jolla, libzstd-devel - 1.5.0+git1-1.1.14.jolla, zstd - 1.5.0+git1-1.1.14.jolla
- [zstd] Initial packaging for zstd. 
-- the end --