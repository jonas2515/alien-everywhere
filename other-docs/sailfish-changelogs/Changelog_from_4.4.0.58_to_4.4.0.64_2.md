============================================================================
SAILFISH OS
Changelog from 4.4.0.58 to 4.4.0.64
2022-05-11
============================================================================

# PACKAGES MODIFIED

### apkd-l10n
- Updated : 1.145.2-1.6.1.jolla -- 1.145.3-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 38 of 38 strings translated (0 need review).
### commhistory-daemon-l10n
- Updated : 1.90.2-1.6.1.jolla -- 1.90.3-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 43 of 43 strings translated (0 need review).
### droid-config-xqbt52
- Updated : 1.8.2.5-1.10.1.jolla -- 1.8.2.10-1.13.1.jolla
- [dconf] Add key to show reboot dialog when inserting sim cards. 
- [patterns] Add VoLTE enablers to adaptation pattern. 
- [configs] Set default data profile id. 
- [configs] Add workaround for camera service crash. 
- [configs] Add possibility to define specific VOIP sink. 
- [sparse] Add a service for memory reclaim. 
- [sparse] Disable update_verifier for ports starting from Android 10. 
- [sparse] Move sysctl files to /usr/lib. 
### droid-hal-pdx213
- Updated : 1.8.4-1.6.1.jolla -- 1.9.0-1.7.4.jolla
- [kernel] Fix display brightness control. 
- [dhd] Immediately fail Android builds on OBS if a command fails. 
- [helpers] Build pulseaudio-modules-droid-jb2q for Android versions up to 10. 
- [kernel] Fix defconfig symbol wrongfully changed. 
- [kernel] Fix port lowmemorykiller driver from 4.14. 
- [helpers] Refactor utils to use mb2 --package-timeline. Contributes to 
- [kernel] Port lowmemorykiller driver from 4.14 and enable android lmk. 
- [kernel] Replace or remove invalid config symbols in hybris defconfig. 
- [localbuild] Make all build script changes persistent. 
- [localbuild] Pass local repo to zypper ahead of `ssu ar` removal. 
- [localbuild] Remove leftovers manually for now. 
- [localbuild] Switch local repo to flat dir structure. 
- [localbuild] Use mb2 --output-dir instead to deploy RPMs. 
- [localbuild] Use sdk-assistant maintain instead of sb2. 
### droid-src-sony-lena
- Updated : 1.8.4-1.5.3.jolla -- 1.9.1-1.7.1.jolla
- [hybris] mixer_paths: Use handset mic for speaker mode workaround. 
- [camera] QCamera2: mm-interface: Change media entity enumeration logic for k4.19. 
- [droid-src] frameworks: av: Fix browser crash after playing videos. 
- [hybris] device: sony: common: Proper SIM detection fix is now upstream. 
- [sony-common] Revert "init: qcrild.rc : Add vendor prefix to ril-daemon". 
### droid-system-pdx213
- Updated : 1.9.1-1.7.1.jolla -- 1.9.6-1.10.1.jolla
- [system] Enable loudspeaker echo cancellation. 
- [hybris] mixer_paths: Use handset mic for speaker mode workaround. 
- [camera] QCamera2: mm-interface: Change media entity enumeration logic for k4.19. 
- [droid-src] frameworks: av: Fix browser crash after playing videos. 
- [hybris] device: sony: common: Proper SIM detection fix is now upstream. 
- [sony-common] Revert "init: qcrild.rc : Add vendor prefix to ril-daemon". 
- [hybris] device: sony: lena: Disable sensors of tele and uwide lenses for now. 
- [hybris] init: Enable low memory killer. 
### droid-system-pdx213-xqbt52
- Updated : 1.9.1-1.7.1.jolla -- 1.9.6-1.10.1.jolla
- [system] Enable loudspeaker echo cancellation. 
- [hybris] mixer_paths: Use handset mic for speaker mode workaround. 
- [camera] QCamera2: mm-interface: Change media entity enumeration logic for k4.19. 
- [droid-src] frameworks: av: Fix browser crash after playing videos. 
- [hybris] device: sony: common: Proper SIM detection fix is now upstream. 
- [sony-common] Revert "init: qcrild.rc : Add vendor prefix to ril-daemon". 
- [hybris] device: sony: lena: Disable sensors of tele and uwide lenses for now. 
- [hybris] init: Enable low memory killer. 
### jolla-alarm-ui-l10n
- Updated : 1.98.2-1.7.1.jolla -- 1.98.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 31 of 33 strings translated (2 need review).
### jolla-calendar-l10n
- Updated : 1.249.2-1.8.1.jolla -- 1.249.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 139 of 139 strings translated (0 need review).
### jolla-camera
- Updated : 1.2.16.2-1.8.1.jolla -- 1.2.16.3-1.9.1.jolla
- [jolla-camera] Restart camera upon error (xperia 10 III). 
### jolla-camera-l10n
- Updated : 1.218.2-1.8.1.jolla -- 1.218.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 73 of 73 strings translated (0 need review).
### jolla-clock-l10n
- Updated : 1.162.2-1.6.1.jolla -- 1.162.3-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 47 of 48 strings translated (0 need review).
### jolla-contacts-l10n
- Updated : 1.187.2-1.7.1.jolla -- 1.187.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 60 of 60 strings translated (0 need review).
### jolla-devicelock-l10n
- Updated : 1.48.2-1.5.1.jolla -- 1.48.3-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 7 of 7 strings translated (0 need review).
### jolla-email-l10n
- Updated : 1.293.2-1.7.1.jolla -- 1.293.5-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 233 of 233 strings translated (0 need review).
### jolla-gallery-facebook-l10n
- Updated : 1.74.3-1.5.1.jolla -- 1.74.4-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 14 of 14 strings translated (0 need review).
### jolla-gallery-l10n
- Updated : 1.172.2-1.8.1.jolla -- 1.172.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 17 of 17 strings translated (0 need review).
### jolla-messages-l10n
- Updated : 1.199.2-1.8.1.jolla -- 1.199.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 88 of 88 strings translated (0 need review).
### jolla-settings-l10n
- Updated : 1.145.2-1.7.1.jolla -- 1.145.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 22 of 22 strings translated (0 need review).
### jolla-settings-sailfishos-l10n
- Updated : 1.139.2-1.8.1.jolla -- 1.139.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 53 of 53 strings translated (0 need review).
### jolla-settings-system-l10n
- Updated : 1.556.5-1.12.1.jolla -- 1.556.6-1.13.1.jolla
- [l10n] Commit from Jolla localisation: 631 of 631 strings translated (0 need review).
### libgbinder-radio
- Updated : 1.4.8-1.4.1.jolla -- 1.4.10-1.5.1.jolla
- [gbinder-radio] Tweaked completion callback criteria. 
- [gbinder-radio] Added IMS types. 
### libglibutil
- Updated : 1.0.61-1.12.1.jolla -- 1.0.62-1.13.1.jolla
- [glibutil] Added gutil_strlen0()
- [glibutil] Added gutil_strv_find_last() and gutil_strv_remove_dups()
- [glibutil] Fixed a few weird unit test issues
- [glibutil] 
- [license] Freshened up copyright
### lipstick-jolla-home-qt5-l10n
- Updated : 1.428.2-1.8.1.jolla -- 1.428.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 262 of 262 strings translated (0 need review).
### mlsdb-data
- Updated : 0.1.5-1.9.1.jolla -- 0.1.6-1.10.1.jolla
- [mlsdb] Update Mozilla Location DB offline data to 2022-03-22. 
### ofono
- Updated : 1.28+git3.1-1.12.1.jolla -- 1.28+git3.2-1.13.1.jolla
- [ims] D-Bus access control for org.ofono.IpMultimediaSystem. 
- [ims] Disable IMS registration by default
- [ims] Extend org.ofono.IpMultimediaSystem D-Bus API. 
- [ims] Tweak the treatment of the default Registration value
- [watch] Added reg_tech watch. 
### ofono-binder-plugin
- Updated : 1.0.2-1.1.1.jolla -- 1.1.1-1.2.1.jolla
- Binaries added : libofonobinderpluginext - 1.1.1-1.2.1.jolla, libofonobinderpluginext-devel - 1.1.1-1.2.1.jolla
- [ofono-binder] Allow lte value for MaxNonDataMode. 
- [ofono-binder] Fix startup with IRadioConfig 1.2 missing. 
- [ofono-binder] Make data profile ids configurable. 
- [build] Make sure strip is defined
- [ext] Debian packaging for libofonobinderpluginext. 
- [ext] Don't invoke virtual method from a slot finalizer
- [ext] Removed binder_ext_slot_plugin_name
- [ofono-binder] Added IMS state registration tracker object. 
- [ofono-binder] Documented extPlugin config option
- [ofono-binder] Extension for voice calls. 
- [ofono-binder] Fixed conversion of vec<string> to char**
- [ofono-binder] Housekeeping
- [ofono-binder] IMS control extension. 
- [ofono-binder] Prevent infinite recursion
- [ofono-binder] Refactored SMS extension interface. 
- [ofono-binder] Send SMS over IMS when we can. 
- [ofono-binder] Support for plugin extensions. 
- [ofono-binder] Tweaked SMS extension interface. 
- [unit] More unit tests
- [ofono-binder] Added ofono_ims_driver. 
### qmf-eas-plugin-l10n
- Updated : 1.110.2-1.7.1.jolla -- 1.110.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 106 of 106 strings translated (0 need review).
### qt5
- Updated : 5.6.3+git46.1-1.16.2.jolla -- 5.6.3+git46.2-1.17.1.jolla
- [qtbase] Protect QNetworkAccessManager on duplicated state changes. 
### sailfish-browser-l10n
- Updated : 1.262.8-1.15.1.jolla -- 1.262.9-1.16.1.jolla
- [l10n] Commit from Jolla localisation: 162 of 162 strings translated (0 need review).
### sailfish-components-contacts-qt5-l10n
- Updated : 1.198.2-1.7.1.jolla -- 1.198.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 158 of 158 strings translated (0 need review).
### sailfish-components-filemanager-l10n
- Updated : 1.99.4-1.7.1.jolla -- 1.99.5-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 65 of 65 strings translated (0 need review).
### sailfish-components-webview-qt5-l10n
- Updated : 1.83.4-1.11.1.jolla -- 1.83.5-1.12.1.jolla
- [l10n] Commit from Jolla localisation: 123 of 123 strings translated (0 need review).
### sailfish-office-l10n
- Updated : 1.156.2-1.7.1.jolla -- 1.156.3-1.8.1.jolla
- [l10n] Commit from Jolla localisation: 86 of 86 strings translated (0 need review).
### sailfish-utilities
- Updated : 0.1.14-1.5.11.jolla -- 0.1.16-1.6.1.jolla
- [sailfish-utilities] Add a Restart Fingerprint button. 
- [sailfish-utilities] Updated project file for easier development.
- [sailfish-utilities] Include license file as %license. 
### sailfishsilica-qt5-l10n
- Updated : 1.156.3-1.6.1.jolla -- 1.156.6-1.7.1.jolla
- [l10n] Commit from Jolla localisation: 49 of 107 strings translated (0 need review).
### sailjail-permissions
- Updated : 1.0.99-1.30.2.jolla -- 1.1.0-1.31.1.jolla
- [permissions] Allow Location to access sensors to make compass work. 
### simkit-l10n
- Updated : 1.59.3-1.5.1.jolla -- 1.59.4-1.6.1.jolla
- [l10n] Commit from Jolla localisation: 14 of 14 strings translated (0 need review).
### voicecall-ui-jolla
- Updated : 1.14.38-1.5.1.jolla -- 1.14.38.1-1.6.1.jolla
- [voicecall-ui] Combine desktop files.
### voicecall-ui-jolla-l10n
- Updated : 1.301.2-1.8.1.jolla -- 1.301.3-1.9.1.jolla
- [l10n] Commit from Jolla localisation: 250 of 250 strings translated (0 need review).
### xulrunner-qt5
-  Updated : 78.15.1+git24.1-1.30.1.jolla -- 78.15.1+git24.2-1.31.1.jolla
- [sailfishos][embedlite] Drop radio and checkbox max size restriction.

-- the end --
