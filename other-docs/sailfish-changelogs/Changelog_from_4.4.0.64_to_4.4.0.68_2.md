============================================================================
SAILFISH OS
Changelog from 4.4.0.64 to 4.4.0.68
2022-07-13
============================================================================
# PACKAGES MODIFIED

### acl
- Updated : 2.2.53-1.6.16.jolla -- 2.2.53-1.7.6.jolla
- [packaging] Fix submodule URL. 
### acpid
- Updated : 2.0.14-1.3.1.jolla -- 2.0.14+git3-1.1.1.jolla
- [packaging] Fix systemd unit install path. 
- [packaging] Drop YAML packaging. 
- [packaging] Use submodule for packaging. 
### aliendalvik-configs
- Updated : 10.0.59-1.4.1.jolla -- 10.0.59.1-1.5.1.jolla
- [appsupport] increase the size of the /dev tmpfs to 2M. 
### aliendalvik-system
- Updated : 10.0.0.62.1.1-1.8.1.jolla -- 10.0.0.62.1.4-1.9.1.jolla
- [appsupport] avoid an issue with the selinux mount. 
- [appsupport] disallow access to /sys/fs/selinux. 
- [appsupport] keep metaState from input as EventHub::mapKey output. Fixes 
- [alien] Fix handling of networks. 
### alsa-utils
- Updated : 1.2.3+git3-1.6.1.jolla -- 1.2.3+git4-1.7.1.jolla
- [git] Move submodule repos to github. 
### attr
- Updated : 2.4.47+git1-1.6.1.jolla -- 2.4.47+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### audit
- Updated : 2.8.4+git7-1.8.12.jolla -- 2.8.4+git8-1.9.2.jolla
- [git] Move submodule repos to github. 
### augeas
- Updated : 1.12.0+git2-1.6.1.jolla -- 1.12.0+git4-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [augeas] Avoid installing tests with -libs. 
### autoconf-archive
- Updated : 2019.01.06+git2-1.5.1.jolla -- 2019.01.06+git3-1.6.1.jolla
- [git] Move more submodule repos to github. 
- [git] Move submodule repos to github. 
### binutils
- Updated : 2.32+git3-1.7.5.jolla -- 2.32+git3.1-1.8.2.jolla
- [packaging] Fix submodule URL. 
### btrfs-progs
- Updated : 3.16+git3-1.6.1.jolla -- 3.16+git4-1.7.1.jolla
- [packaging] Fix submodule URL. 
### cmake
- Updated : 3.19.3+git4-1.10.2.jolla -- 3.19.3+git5-1.11.1.jolla
- [git] Move submodule repos to github. 
### commhistory-daemon
- Updated : 0.8.43-1.11.1.jolla -- 0.8.44-1.12.1.jolla
- [commhistory] Restore notification categories. 
### connman
- Updated : 1.32+git180.2-1.16.1.jolla -- 1.32+git187-1.17.1.jolla
- [blacklist monitor] Plugin to prevent IPv6 default routes on blacklisted ifs. 
- [device] Add wrapper to check if interface is blacklisted for plugins. 
- [inet] Do not add RTF_HOST for IPv6 default route. 
- [inet] Support setting metric value with IPv6 network route. 
- [ipconfig] Add wrapper to conf type getter for plugins. 
- [rtnl] Extend notify and better support IPv6 routes set via RA. 
- [service] Add wrappers for network and index lookup, getter for ipconfig. 
- [unit] Add blacklist monitor unit tests. 
- [connman] Apply upstream rtnl patches, revert debug disable commit. 
- [connman] Follow upstream in setting getter naming. 
- [main] Add path to localtime to config options. 
- [main] Add RegdomFollowsTimezone option for regdom changes. 
- [ofono] Do not change regdom when it follows timezone. 
- [timezone] Change regdom along timezone, use localtime config. 
- [connman] Add configurable run dir, drop legacy /var/run use. Fixes 
- [agent] Add support to check for active pending requests. 
- [service] Check if hidden service has a pending request. 
- [connman] Fix CVE-2022-23096 CVE-2022-23097 CVE-2022-23098. Fixes 
- [service] Implement counting of available services. 
- [wifi] Implement a heurestic for determening a weak WiFi. 
### connman-network-monitor
- Updated : 0.0.0+git1-1.5.1.jolla -- 0.0.0+git2-1.6.1.jolla
- [packaging] Fix submodule URL. 
### crda
- Updated : 4.14+git4-1.6.12.jolla -- 4.14+git5-1.7.2.jolla
- [packaging] Fix submodule URL. 
### createrepo_c
- Updated : 0.12.0-1.2.1.jolla -- 0.12.0+git1-1.3.1.jolla
- [packaging] Fix submodule URL. 
### cross-aarch64-binutils
- Updated : 2.32+git3-1.7.2.jolla -- 2.32+git3.1-1.8.1.jolla
- [packaging] Fix submodule URL. 
### cross-aarch64-gdb
- Updated : 8.2.1+git8-1.5.2.jolla -- 8.2.1+git9-1.6.1.jolla
- [packaging] Fix submodule URL. 
### cross-armv7hl-binutils
- Updated : 2.32+git3-1.7.2.jolla -- 2.32+git3.1-1.8.1.jolla
- [packaging] Fix submodule URL. 
### cross-armv7hl-gdb
- Updated : 8.2.1+git8-1.5.2.jolla -- 8.2.1+git9-1.6.1.jolla
- [packaging] Fix submodule URL. 
### cross-i486-binutils
- Updated : 2.32+git3-1.7.2.jolla -- 2.32+git3.1-1.8.1.jolla
- [packaging] Fix submodule URL. 
### cross-i486-gdb
- Updated : 8.2.1+git8-1.7.2.jolla -- 8.2.1+git9-1.8.1.jolla
- [packaging] Fix submodule URL. 
### cups
- Updated : 2.3.1+git2-1.7.2.jolla -- 2.3.1+git3-1.8.1.jolla
- [git] Move submodule repos to github. 
### cython
- Updated : 0.29.14+git2-1.6.1.jolla -- 0.29.14+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
### dconf
- Updated : 0.40.0+git3-1.8.1.jolla -- 0.40.0+git4-1.9.1.jolla
- [git] Move submodule repos to github. 
### desktop-file-utils
- Updated : 0.26+git3-1.7.1.jolla -- 0.26+git4-1.8.1.jolla
- [packaging] Fix submodule URL. 
### droid-config-xqau51
- Updated : 0.1.24.1-1.6.1.jolla -- 0.1.24.3-1.7.1.jolla
- Binaries removed : droid-config-xqau51-bluez4
- [patterns] Add VoLTE enablers to adaptation pattern. Fixes 
- [configs] Package ofono-binder-plugin. 
- [configs] Remove BlueZ4 bluetoothd configs. 
- [configs] Remove BlueZ4 packaging. Fixes 
- [configs] Remove BlueZ4 PulseAudio related configuration. 
- [lib] Install oneshot scripts under /usr/lib. 
- [patterns] Add configuration to modify installed sailfish patterns. 
- [rpm] Obsolete ofono-configs-binder, we provide our own configs. Fixes 
### droid-config-xqau52
- Updated : 0.1.24.1-1.6.1.jolla -- 0.1.24.3-1.7.1.jolla
- Binaries removed : droid-config-xqau52-bluez4
- [patterns] Add VoLTE enablers to adaptation pattern. Fixes 
- [configs] Package ofono-binder-plugin. 
- [configs] Remove BlueZ4 bluetoothd configs. 
- [configs] Remove BlueZ4 packaging. Fixes 
- [configs] Remove BlueZ4 PulseAudio related configuration. 
- [lib] Install oneshot scripts under /usr/lib. 
- [patterns] Add configuration to modify installed sailfish patterns. 
- [rpm] Obsolete ofono-configs-binder, we provide our own configs. Fixes 
### droid-src-sony-seine
- Updated : 0.1.7-1.4.4.jolla -- 1.12.2-1.5.2.jolla
- [dhs] Immediately fail Android builds on OBS if a command fails. Fixes 
- [droid-src] Add modem configs for Finnish providers Elisa and DNA. 
- [droid-src] Fix path of do not log battery status to kernel log patch. 
- [droid-src] hardware/adreno: Add back vendor->odm symlink for vulkan.qcom.so.
- [hybris] device: sony: common: Do not log battery status to kernel log. 
- [droid-src] hybris: init: improve low memory killer thresholds. Fixes 
- [manifest] temporarily introduce manifest versioning. 
### droid-system-pdx201
- Updated : 0.1.7-1.5.1.jolla -- 0.1.9-1.6.1.jolla
- [dsd] helpers: Add support for product and system_ext.
- [dsd] helpers: Replace all build user instances.
- [dsd] helpers: Return true for setcap post commands.
- [sparse] Add back vendor->odm symlink for vulkan.qcom.so.
- [sparse] Add modem configs for Finnish providers Elisa and DNA. 
- [sparse] Do not log battery status to kernel log. 
- [hybris] init: improve low memory killer thresholds. Fixes 
### droid-system-pdx201-xqau51
- Updated : 0.1.7-1.5.1.jolla -- 0.1.9-1.6.1.jolla
- [dsd] helpers: Add support for product and system_ext.
- [dsd] helpers: Replace all build user instances.
- [dsd] helpers: Return true for setcap post commands.
- [sparse] Add back vendor->odm symlink for vulkan.qcom.so.
- [sparse] Add modem configs for Finnish providers Elisa and DNA. 
- [sparse] Do not log battery status to kernel log. 
- [hybris] init: improve low memory killer thresholds. Fixes 
### droid-system-pdx201-xqau52
- Updated : 0.1.7-1.5.1.jolla -- 0.1.9-1.6.1.jolla
- [dsd] helpers: Add support for product and system_ext.
- [dsd] helpers: Replace all build user instances.
- [dsd] helpers: Return true for setcap post commands.
- [sparse] Add back vendor->odm symlink for vulkan.qcom.so.
- [sparse] Add modem configs for Finnish providers Elisa and DNA. 
- [sparse] Do not log battery status to kernel log. 
- [hybris] init: improve low memory killer thresholds. Fixes 
### dtc
- Updated : 1.4.7-1.2.1.jolla -- 1.4.7+git1-1.3.1.jolla
- [packaging] Fix submodule URL. 
### elfutils
- Updated : 0.177+git1-1.6.1.jolla -- 0.177+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### embedlite-components-search-engines
- Updated : 0.0.3-1.5.1.jolla -- 0.0.5-1.6.1.jolla
- [search-engines] Update google search engine xml. Fixes 
### ffmpeg
- Updated : 4.4.1+git1-1.6.1.jolla -- 4.4.1+git2-1.7.1.jolla
- [ffmpeg] Enable ALAC codec. Fixes 
### flex
- Updated : 2.6.4+git1-1.6.16.jolla -- 2.6.4+git2-1.7.6.jolla
- [git] Move submodule repos to github. 
### fontconfig
- Updated : 2.13.1+git3-1.5.1.jolla -- 2.13.1+git3.1-1.6.1.jolla
- [packaging] Fix submodule URL. 
### fribidi
- Updated : 1.0.10+git1-1.6.1.jolla -- 1.0.10+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### gdb
- Updated : 8.2.1+git8-1.7.4.jolla -- 8.2.1+git9-1.8.2.jolla
- [packaging] Fix submodule URL. 
### git
- Updated : 2.26.2+git1-1.2.2.jolla -- 2.26.2+git2-1.3.1.jolla
- [packaging] Fix submodule URL. 
### gmp-droid
- Updated : 0.5-1.3.1.jolla -- 0.5.1-1.4.1.jolla
- [packaging] Fix submodule URL. 
### gnu-findutils
- Updated : 4.6.0+git2-1.5.1.jolla -- 4.6.0+git3-1.6.1.jolla
- [packaging] Fix submodule URL. 
### gnupg2
- Updated : 2.0.4+git3-1.6.13.jolla -- 2.0.4+git4-1.7.2.jolla
- [packaging] Fix submodule URL. 
### gnutls
- Updated : 2.12.24+git1-1.6.12.jolla -- 2.12.24+git2-1.7.2.jolla
- [git] Move submodule repos to github. 
### gpgme
- Updated : 1.2.0+git6-1.6.1.jolla -- 1.2.0+git7-1.7.1.jolla
- [packaging] Fix submodule URL. 
### grubby
- Updated : 7.0.8-1.5.1.jolla -- 7.0.8+git2-1.1.1.jolla
- [packaging] Drop YAML packaging. 
- [packaging] Use submodule for packaging. 
### gtest
- Updated : 1.11.0+git2-1.6.1.jolla -- 1.11.0+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
### gupnp-av
- Updated : 0.12.10-1.5.1.jolla -- 0.12.10-1.6.1.jolla
- [git] Move submodule repos to github. 
### gupnp-dlna
- Updated : 0.10.5-1.5.1.jolla -- 0.10.5-1.6.1.jolla
- [git] Move submodule repos to github. 
### htop
- Updated : 3.0.2+git1-1.2.1.jolla -- 3.0.2+git2-1.3.1.jolla
- [git] Move submodule repos to github. 
### hunspell
- Updated : 1.6.2+git1-1.6.1.jolla -- 1.6.2+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### iproute
- Updated : 3.7.0+git6-1.6.1.jolla -- 3.7.0+git6.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### iso-codes
- Updated : 3.79+git1-1.6.1.jolla -- 3.79+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### iw
- Updated : 5.0.1+git1-1.6.1.jolla -- 5.0.1+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### jolla-common-configurations
- Updated : 0.11.3-1.5.1.jolla -- 0.11.3.1-1.6.1.jolla
- [connman] Use timed localtime, set regdom to follow timezone. Fixes 
### jolla-keyboard
- Updated : 0.8.28.2-1.6.1.jolla -- 0.8.28.3-1.7.1.jolla
- [keyboard] Decrease spacebar row punctionation keys. 
### jolla-settings-accounts
- Updated : 0.4.57-1.5.1.jolla -- 0.4.57.1-1.6.1.jolla
- [settings-accounts] Add password reset link to the forget password. Fixes 
- [settings-accounts] Show 'Update sign-in credentials' always for Google account. Fixes 
- [settings-accounts] Switch ToS views to use Gecko WebView. 
- [settings-accounts] Use externel browser for Google account. Fixes 
### jolla-settings-networking
- Updated : 1.0.1-1.4.1.jolla -- 1.0.1.1-1.5.1.jolla
- [settings-network] Add VoLTE registration switch for the 'Mobile network'. Fixes 
### jolla-settings-system
- Updated : 1.1.51.1-1.8.4.jolla -- 1.1.51.2-1.9.1.jolla
- [jolla-settings-system] Add rpm linking to the libsystemsettingsplugin.so. Fixes 
- [settings-system] Add packageName and whatProvides properties. 
- [system-settings] Add RPM info class. 
### kernel-cmdline
- Updated : 1.1.0-1.2.42.jolla -- 1.1.1-1.3.8.jolla
- [packaging] Fix submodule URL. 
### kmod
- Updated : 27-1.6.1.jolla -- 27+git1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libaccounts-qt5
- Updated : 1.16+git1-1.6.1.jolla -- 1.16+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [libaccounts-qt5] Add %license file. 
### libatomic_ops
- Updated : 7.4.4+git1-1.6.1.jolla -- 7.4.4+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libcanberra
- Updated : 0.30+git1-1.6.1.jolla -- 0.30+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libcap
- Updated : 2.25+git1-1.6.1.jolla -- 2.25+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libeigen3-devel
- Updated : 3.3.5+git1-1.6.1.jolla -- 3.3.5+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libffi
- Updated : 3.2.1+git1-1.6.1.jolla -- 3.2.1+git1.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libgpg-error
- Updated : 1.27+git3-1.7.1.jolla -- 1.27+git3.1-1.8.1.jolla
- [packaging] Fix submodule URL. 
### libhybris
- Updated : 0.0.5.44-1.3.1.jolla -- 0.0.5.44.1-1.4.1.jolla
- [packaging] Fix submodule URLs. 
### libical
- Updated : 3.0.9+git1-1.5.1.jolla -- 3.0.9+git2-1.6.1.jolla
- [packaging] Fix submodule URL. 
### libksba
- Updated : 1.3.5+git2-1.6.1.jolla -- 1.3.5+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libnl
- Updated : 3.4.0+git3-1.6.1.jolla -- 3.4.0+git3.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libqofono-qt5
- Updated : 0.103-1.5.1.jolla -- 0.112-1.6.1.jolla
- [libqofono] Support for IMS Registration property. 
- [tests] Drop context manipulation parts from connman tests. 
- [tests] Expect failure on context tests on Sailfish. 
- [tests] Fix sim manager tests. 
- [connectionmanager] Add support for reset contexts dbus call
- [libqofono] Added QOfonoConnectionManager::resetContexts. 
- [libqofono] Housekeeping. 
- [libqofono] Run tests with sailfish-radio group. 
- [libqofono] Drop Qt4 legacy.
- [libqofono] Fix phonesim setup in tests. 
- [libqofono] Move tests to /opt/tests. 
- [libqofono] Support for org.ofono.IpMultimediaSystem. 
- [libqofono] Fix systemctl path in tests. 
- [libqofono] Housekeeping. 
- [libqofono] Provide both In and Out annotations for signals
- [libqofono-qt5] Have license file as %license. 
### libsbc
- Updated : 1.3-1.6.1.jolla -- 1.3.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libselinux
- Updated : 3.1+git2-1.5.12.jolla -- 3.1+git3-1.6.2.jolla
- [git] Move submodule repos to github. 
### libsepol
- Updated : 3.1+git2-1.5.1.jolla -- 3.1+git3-1.6.1.jolla
- [git] Move submodule repos to github. 
### libtheora
- Updated : 1.2.0alpha1+git2-1.6.1.jolla -- 1.2.0alpha1+git4-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [libtheora] Declare license file as %license. 
### libusb1
- Updated : 1.0.20-1.6.1.jolla -- 1.0.20.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libutempter
- Updated : 1.1.5+git2-1.6.17.jolla -- 1.1.5+git3-1.7.6.jolla
- [packaging] Fix submodule URL. 
### libvncserver
- Updated : 0.9.10+git1-1.2.1.jolla -- 0.9.10+git2-1.3.1.jolla
- [packaging] Fix submodule URL. 
### libwbxml2
- Updated : 0.11.6+git1-1.6.1.jolla -- 0.11.6+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### libwebp
- Updated : 1.2.0-1.8.2.jolla -- 1.2.0+git1-1.9.1.jolla
- [packaging] Fix submodule URL. 
### libwspcodec
- Updated : 2.2.4-1.5.1.jolla -- 2.2.6-1.6.1.jolla
- [libwspcodec] Allow empty quoted subject. 
- [libwspcodec] Include license as %license. 
- [rpm] Require rpm 4.11 for %license. 
### ltrace
- Updated : 0.8.0+git1-1.2.1.jolla -- 0.8.0+git2-1.3.1.jolla
- [git] Move submodule repos to github. 
### lvm2
- Updated : 2.02.177+git5-1.7.1.jolla -- 2.02.177+git6-1.8.1.jolla
- [packaging] Fix submodule URL. 
### maliit-plugins
- Updated : 0.99.0+git6-1.6.7.jolla -- 0.99.0+git7-1.7.1.jolla
- [packaging] Fix submodule URL. 
### modem_auto_config
- Updated : 1.0.0-1.1.1.jolla -- 1.0.1-1.2.1.jolla
- [modem-auto-config] Fix loading of modem configuration files. 
### nemo-qtmultimedia-plugins-gstvideotexturebackend
- Updated : 0.1.2-1.5.1.jolla -- 0.1.4-1.6.1.jolla
- [videotexturebackend] Fix null pointer derefenence from init. Fixes 
- [nemo-qtmultimedia-plugins] Add license file. 
### ninja
- Updated : 1.10.2+git3-1.5.1.jolla -- 1.10.2+git4-1.6.1.jolla
- [git] Move submodule repos to github. 
### nss-pem
- Updated : 1.0.6+git1-1.5.12.jolla -- 1.0.6+git2-1.6.2.jolla
- [packaging] Fix submodule URL. 
### ofono-binder-plugin
- Updated : 1.1.1-1.2.1.jolla -- 1.1.3-1.3.1.jolla
- [ofono-binder] Use hangupWaitingOrBackground for incoming calls. 
- [ofono-binder] Hook up currentEmergencyNumberList indication. 
- [unit] Added unit_ext_plugin
### ofono-ril-plugin
- Updated : 1.0.2-1.2.2.jolla -- 1.0.2.1-1.3.1.jolla
- [ofono-ril-plugin] Use HANGUP_WAITING_OR_BACKGROUND for incoming calls. 
### ofono-vendor-qti-radio-plugin
- Updated : 1.0.0-1.1.1.jolla -- 1.0.1-1.2.1.jolla
- [qti-radio] Housekeeping
- [qti-radio] Provide ofono-ims-support. 
- [rpm] Bump libglibutil dependency version
### oprofile
- Updated : 1.2.0+git1-1.2.41.jolla -- 1.2.0+git2-1.3.8.jolla
- [packaging] Fix submodule URL. 
### orc
- Updated : 0.4.26+git1-1.6.1.jolla -- 0.4.26+git1.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### parted
- Updated : 3.0+mer5-1.2.1.jolla -- 3.0+mer6-1.3.1.jolla
- [packaging] Fix submodule URL. 
### passwd
- Updated : 0.80+git1-1.6.1.jolla -- 0.80+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### pixman
- Updated : 0.40.0+git1-1.6.1.jolla -- 0.40.0+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [pixman] Include license as %license. 
### polkit
- Updated : 0.105+git8-1.8.6.jolla -- 0.105+git9-1.9.1.jolla
- [packaging] Fix submodule URL. 
### powertop
- Updated : 2.10+git1-1.2.1.jolla -- 2.10+git2-1.3.1.jolla
- [packaging] Fix submodule URL. 
### procps-ng
- Updated : 3.3.16+git1-1.5.1.jolla -- 3.3.16+git2-1.6.1.jolla
- [packaging] Fix submodule URL. 
### pykickstart
- Updated : 3.25+git2-1.2.1.jolla -- 3.25+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python
- Updated : 2.7.17+git7-1.6.1.jolla -- 2.7.17+git8-1.7.1.jolla
- [git] Move submodule repos to github. 
### python3-cairo
- Updated : 1.19.0+git1-1.6.1.jolla -- 1.19.0+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### python3-certifi
- Updated : 2020.04.05.1+git2-1.2.1.jolla -- 2020.04.05.1+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-chardet
- Updated : 3.0.4+git2-1.2.1.jolla -- 3.0.4+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-cheetah
- Updated : 3.2.4+git1-1.3.57.jolla -- 3.2.4+git2-1.4.13.jolla
- [packaging] Fix submodule URL. 
### python3-distro
- Updated : 1.5.0+git2-1.2.1.jolla -- 1.5.0+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-markdown
- Updated : 3.2.1+git2-1.2.1.jolla -- 3.2.1+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-ordered-set
- Updated : 3.1+git2-1.2.1.jolla -- 3.1+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-pycurl
- Updated : 7.43.0.5+git2-1.2.2.jolla -- 7.43.0.5+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-pygments
- Updated : 2.6.1+git2-1.2.11.jolla -- 2.6.1+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### python3-requests
- Updated : 2.23.0+git3-1.2.43.jolla -- 2.23.0+git4-1.3.8.jolla
- [packaging] Fix submodule URL. 
### python3-six
- Updated : 1.14.0+git2-1.5.1.jolla -- 1.14.0+git4-1.6.1.jolla
- [packaging] Fix submodule URL. 
- [python3-six] Have license file as %license. 
### python3-urlgrabber
- Updated : 4.1.0+git3-1.2.44.jolla -- 4.1.0+git4-1.3.9.jolla
- [packaging] Fix submodule URL. 
### python3-urllib3
- Updated : 1.25.9+git2-1.2.1.jolla -- 1.25.9+git3-1.3.1.jolla
- [packaging] Fix submodule URL. 
### qmf-qt5
- Updated : 4.0.4+git135-1.8.1.jolla -- 4.0.4+git136-1.9.1.jolla
- [packaging] Fix submodule URL. 
### qt5-qtdeclarative
- Updated : 5.6.3+git21-1.8.1.jolla -- 5.6.3+git21.1-1.9.1.jolla
- [tests] Remove unused submodule. 
### qt5-qtgraphicaleffects
- Updated : 5.6.2+git3-1.5.1.jolla -- 5.6.2+git4-1.6.1.jolla
- [packaging] Fix submodule URL. 
### qt5-qtimageformats
- Updated : 5.6.3+git2-1.5.1.jolla -- 5.6.3+git4-1.6.1.jolla
- [packaging] Fix submodule URL. 
- [qtimageformats] Add %license file to packages. 
### qt5-qtwebkit
- Updated : 5.6.2+git14-1.6.1.jolla -- 5.6.2+git16-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [qtwebkit] Strip debug symbols from the shared libraries. Fixes 
### qt5-qtxmlpatterns
- Updated : 5.6.3+git3-1.6.1.jolla -- 5.6.3+git4-1.7.1.jolla
- [packaging] Use submodule for packaging. 
### qtmozembed-qt5
- Updated : 1.53.20-1.31.8.jolla -- 1.53.22-1.32.2.jolla
- [qtmozembed] Avoid sending orientation signal on scene changes. Fixes 
- [tests] Split checkDefaultSearch of tst_searchengine to three. 
- [tests] Wait engine to load in initTestCase. 
### qtscenegraph-adaptation
- Updated : 0.7.6-1.3.1.jolla -- 0.7.7-1.4.1.jolla
- [customcontext] Fix copying QImages from hybris textures. 
### quilt
- Updated : 0.64-1.6.1.jolla -- 0.64+git1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### quota
- Updated : 4.05+git1-1.5.1.jolla -- 4.05+git2-1.6.1.jolla
- [git] Move submodule repos to github. 
### re2c
- Updated : 2.0.3+git2-1.5.1.jolla -- 2.0.3+git3-1.6.1.jolla
- [packaging] Fix submodule URL. 
### recode
- Updated : 3.6-1.6.1.jolla -- 3.6-1.7.1.jolla
- [packaging] Drop YAML packaging. 
- [packaging] Fix submodule URL. 
### rfkill
- Updated : 0.5+git1-1.6.1.jolla -- 0.5+git2-1.7.1.jolla
- [packaging] Fix submodule URL. 
### rpm
- Updated : 4.16.1.3+git8-1.10.1.jolla -- 4.16.1.3+git9-1.11.1.jolla
- [packaging] Fix submodule URL. 
### rpm-python
- Updated : 4.16.1.3+git8-1.10.12.jolla -- 4.16.1.3+git9-1.11.2.jolla
- [packaging] Fix submodule URL. 
### rsync
- Updated : 3.1.3+git1-1.5.1.jolla -- 3.1.3+git2-1.6.1.jolla
- [packaging] Fix submodule URL. 
### sailfish-components-webview-qt5
- Updated : 1.5.9-1.19.1.jolla -- 1.5.9.2-1.20.1.jolla
- [webview] Guard programmatic preference change with marker file. Fixes 
- [components-webview] Adjust keyboard margin based on position. 
- [components-webview] Fix keyboard margin calculation. 
- [components-webview] Respect component height. Fixes 
- [webview-docs] Add Jolla copyright to docs footer.
- [webview-docs] Elaborate on using local content with CORS protection. Fixes 
### sailfish-content-browser-default
- Updated : 0.1.4-1.2.1.jolla -- 0.1.6-1.3.1.jolla
- [git] Bump up submodule sha1. Fixes 
- [git] Move submodule repos to github. 
### scons
- Updated : 3.0.5+git2-1.6.13.jolla -- 3.0.5+git3-1.7.2.jolla
- [packaging] Fix submodule URL. 
### screen
- Updated : 4.7.0+git2-1.7.12.jolla -- 4.7.0+git3-1.8.2.jolla
- [packaging] Fix submodule URL. 
### sdk-setup
- Updated : 1.4.55-1.24.1.jolla -- 1.4.58-1.25.1.jolla
- [sdk-manage] Obey also brand when matching SSU releases
- [sdk-manage] Use tarball metadata to look up tooling. 
- [sdk-setup] Automatically load available bash completion. 
- [sdk-setup] Drop outdated bash completion. 
- [sdk-chroot] Utilize profile.d for bash setup. 
### shared-mime-info
- Updated : 1.12-1.6.1.jolla -- 1.12+git1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### signon-qt5
- Updated : 8.60.0+git3-1.8.18.jolla -- 8.60.0+git5-1.9.1.jolla
- [packaging] Fix submodule URL. 
- [libsignon-qt5] Have license file as %license. 
- [libsignon-qt5] Have license file for libsignon-qt5 too. 
- [tests] Cleanup test definitions. Fixes 
### sound-theme-freedesktop
- Updated : 0.8-1.6.1.jolla -- 0.8+git1-1.7.1.jolla
- [packaging] Fix submodule URL. 
- [sound-theme-freedesktop] Package license file. 
### spectacle
- Updated : 0.32-1.2.44.jolla -- 0.33-1.3.8.jolla
- [packaging] Drop YAML packaging. 
### sqlcipher
- Updated : 3.4.1+git2-1.5.1.jolla -- 3.4.1+git2.1-1.6.1.jolla
- [packaging] Fix submodule URL. 
### stress-ng
- Updated : 0.10.17-1.2.1.jolla -- 0.10.17+git1-1.3.1.jolla
- [packaging] Fix submodule URL. 
### systemd
- Updated : 238+git13-1.13.1.jolla -- 238+git13.1-1.14.1.jolla
- [packaging] Fix submodule URL. 
### systemd-bootchart
- Updated : 233+git2-1.7.1.jolla -- 233+git3-1.8.1.jolla
- [git] Move submodule repos to github. 
### systemd-mini
- Updated : 238+git13-1.2.1.jolla -- 238+git13.1-1.3.1.jolla
- [packaging] Fix submodule URL. 
### taglib
- Updated : 1.12+git1-1.5.1.jolla -- 1.12+git2-1.6.1.jolla
- [packaging] Fix submodule URL. 
### tcpdump
- Updated : 4.9.2+git1-1.3.1.jolla -- 4.9.2+git2-1.4.1.jolla
- [packaging] Fix submodule URL. 
### telepathy-qt5
- Updated : 0.9.8+git2-1.9.1.jolla -- 0.9.8+git2.1-1.10.1.jolla
- [packaging] Fix submodule URL. 
### totem-pl-parser
- Updated : 3.26.1+git1-1.6.1.jolla -- 3.26.1+git1.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### usbutils
- Updated : 008-1.6.1.jolla -- 008.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### util-linux
- Updated : 2.33+git3-1.7.15.jolla -- 2.33+git4-1.8.6.jolla
- [packaging] Fix submodule URL. 
### vim
- Updated : 8.2.0000-1.5.10.jolla -- 8.2.0000.1-1.6.2.jolla
- [packaging] Fix submodule URL. 
### volume_key
- Updated : 0.3.9+git2-1.6.1.jolla -- 0.3.9+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 
### wireless-regdb
- Updated : 2020.04.29+git3-1.5.12.jolla -- 2020.04.29+git4-1.6.2.jolla
- [packaging] Fix submodule URL. 
### wpa_supplicant
- Updated : 2.9+git4-1.7.1.jolla -- 2.9+git5-1.8.1.jolla
- [packaging] Fix submodule URL. 
### xdg-dbus-proxy
- Updated : 0.1.2+git3-1.7.1.jolla -- 0.1.2+git4-1.8.1.jolla
- [packaging] Fix submodule URL. 
### xdg-user-dirs
- Updated : 0.16+git2-1.6.1.jolla -- 0.16+git2.1-1.7.1.jolla
- [packaging] Fix submodule URL. 
### xulrunner-qt5
- Updated : 78.15.1+git24.2-1.31.1.jolla -- 78.15.1+git24.3-1.32.1.jolla
- [sailfishos][build] Add support for aarch64 to elfhack. 
- [sailfishos][build] Enable elf-hack. Fixes 
- [sailfishos][embedlite] Add a content controller stack. Fixes 
- [sailfishos][embedlite] Prefer profile directory for search engines. Fixes 
### yasm
- Updated : 1.3.0+git2-1.5.3.jolla -- 1.3.0+git2.1-1.6.1.jolla
- [packaging] Fix submodule URL. 
### zlib
- Updated : 1.2.11+git1-1.6.16.jolla -- 1.2.11+git2-1.7.6.jolla
- [packaging] Fix submodule URL. 
### zxing-cpp
- Updated : 1.1.1+git1-1.6.1.jolla -- 1.1.1+git2-1.7.1.jolla
- [git] Move submodule repos to github. 
### zypper
- Updated : 1.14.38+git2-1.6.1.jolla -- 1.14.38+git3-1.7.1.jolla
- [packaging] Fix submodule URL. 

# PACKAGES ADDED

### ofono-modem-switcher-plugin
- Binaries added : ofono-modem-switcher-plugin - 1.0.2-1.1.1.jolla
- [modemswitcher] Write configuration to rild when it changes. 
- [modemswitcher] Undo configuration on uninstallation. 
- [modemswitcher] Changed package name
- [modemswitcher] Housekeeping
- [modemswitcher] Initial import. 
# PACKAGES REMOVED

### enchant



