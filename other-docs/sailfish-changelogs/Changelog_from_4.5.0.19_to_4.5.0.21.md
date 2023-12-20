SAILFISH OS: Changelog from 4.5.0.19 to 4.5.0.21

2023-07-11

## Packages modified (21)

### aliendalvik-configs
        Updated : 11.0.26.2-1.18.1.jolla -- 11.0.26.3-1.19.1.jolla
        - [appsupport] Remove mknod and mknodat syscalls from seccomp blocked list.

### droid-hal-pdx201
        Updated : 0.0.30-1.10.5.jolla -- 0.0.31-1.11.1.jolla
        - [kernel] free task immediately to prevent slab task_struct memory leak.

### droid-hal-pdx213
        Updated : 1.9.6-1.7.1.jolla -- 1.9.7-1.8.1.jolla
        - [kernel] enable CONFIG_SLAB.
        - [kernel] free task immediately to prevent slab task_struct memory leak.

### droidmedia
        Updated : 0.20220929.0-1.6.2.jolla -- 0.20230605.1-1.8.1.jolla
        - [droidmedia] Fix build for droid versions < 7.
        - [droidmedia] Add encoder setting for CBR/VBR.
        - [droidmedia] Fix ALOG usage.
        - [droidmedia] Fix AsyncCodecSource to be asynchronous.

### droidmedia-devel
        Updated : 0.20220929.0-1.4.3.jolla -- 0.20230605.1-1.6.1.jolla
        - [droidmedia] Fix build for droid versions < 7.
        - [droidmedia] Add encoder setting for CBR/VBR.
        - [droidmedia] Fix ALOG usage.
        - [droidmedia] Fix AsyncCodecSource to be asynchronous.
        
### gecko-camera
        Updated : 0.1.6-1.4.1.jolla -- 0.1.7-1.6.1.jolla
        - [gecko-camera] Set up the video encoder to produce CBR stream.
        - [gecko-camera] Use media buffers depending on CPU vendor.

### gecko-camera-droid-plugin
        Updated : 0.1.6-1.4.1.jolla -- 0.1.7-1.6.1.jolla
        - [gecko-camera] Set up the video encoder to produce CBR stream.
        - [gecko-camera] Use media buffers depending on CPU vendor.
        
### gmp-droid
        Updated : 0.7-1.4.1.jolla -- 0.8-1.5.1.jolla
        - [gmp-droid] Set up the video encoder to produce CBR stream.

### hybris-libsensorfw-qt5-binder
        Updated : 0.12.6-1.5.1.jolla -- 0.14.4-1.6.1.jolla
        - [sensorfw] Fix units used for sleep in sysfsadaptor.
        - [sensorfwd] Use ms values for getAvailableIntervals() reply.
        - [hybrisadaptor] Fix build errors from unresolvable id() calls.
        - [hybrisadaptor] Define data and interval ranges earlier.
        - [hybrisadaptor] Silence als/ps initial value warnings.
        - [sensorfwd] Add node id to diagnostic logging messages
        - [clientapitest] Move unit test operator== away from API header
        - [sensorfwd] Use float values for XYZ data.
        - [tapadaptor] Silence unused parameter warnings
        - [declinationfilter] Add unit suffixes to time values
        - [hybrisadaptor] Fix setDelay() return value
        - [nodebase] Remove dead code
        - [nodebase] Use closest supported data rate.
        - [nodebase] Use m_variableName convention for all members
        - [sensorfw] Add setDataRate() D-Bus method.
        - [sensorfw] Drop evaluateIntervalRequests overloading.
        - [sensorfw] Explicitly indicate interval time units.
        - [sensorfw] Handle intervals in microsecond granularity.
        - [sensorfw] Normalize setInterval() parameter order.
        - [hybrisadaptor] Force cancellation of pending POLL transaction.
        - [hybrisadaptor] Read and process capped number of events.
        - [hybrisadaptor] Shuffle cleanup order.
        - [sendorfwd] Skip deadlocking libgbinder cleanup.

### hybris-libsensorfw-qt5-hal
        Updated : 0.12.6-1.5.1.jolla -- 0.14.4-1.6.1.jolla
        - [sensorfw] Fix units used for sleep in sysfsadaptor.
        - [sensorfwd] Use ms values for getAvailableIntervals() reply.
        - [hybrisadaptor] Fix build errors from unresolvable id() calls.
        - [hybrisadaptor] Define data and interval ranges earlier.
        - [hybrisadaptor] Silence als/ps initial value warnings.
        - [sensorfwd] Add node id to diagnostic logging messages
        - [clientapitest] Move unit test operator== away from API header
        - [sensorfwd] Use float values for XYZ data.
        - [tapadaptor] Silence unused parameter warnings
        - [declinationfilter] Add unit suffixes to time values
        - [hybrisadaptor] Fix setDelay() return value
        - [nodebase] Remove dead code
        - [nodebase] Use closest supported data rate.
        - [nodebase] Use m_variableName convention for all members
        - [sensorfw] Add setDataRate() D-Bus method.
        - [sensorfw] Drop evaluateIntervalRequests overloading.
        - [sensorfw] Explicitly indicate interval time units.
        - [sensorfw] Handle intervals in microsecond granularity.
        - [sensorfw] Normalize setInterval() parameter order.
        - [hybrisadaptor] Force cancellation of pending POLL transaction.
        - [hybrisadaptor] Read and process capped number of events.
        - [hybrisadaptor] Shuffle cleanup order.
        - [sendorfwd] Skip deadlocking libgbinder cleanup.

### jolla-email
        Updated : 1.1.37-1.11.1.jolla -- 1.1.38-1.12.1.jolla
        - [email] Fix sharing url or plain text.

### libmce-glib
        Updated : 1.0.13-1.7.1.jolla -- 1.1.0-1.8.1.jolla
        - [debian] Bumped debhelper compat level to 7
        - [libmce-glib] A better way to silence deprecation warnings
        - [libmce-glib] Add an example application
        - [libmce-glib] Add MceInactivity object

### lipstick-jolla-home-qt5
        Updated : 1.25.13.6-1.16.1.jolla -- 1.25.13.7-1.17.1.jolla
        - [lipstick-jolla-home] Fix notification popups getting lost.

### mapplauncherd-booster-browser
        Updated : 0.1.3-1.6.1.jolla -- 0.2.0-1.7.1.jolla
        - [booster-browser] Drop booster-browser.service.

### mkcal-qt5
        Updated : 0.6.12-1.17.1.jolla -- 0.6.12.1-1.18.1.jolla
        - [mkcal] Fix alarm setting for recurring events.
        - [mkcal] Fix recurring event alarms with offset.

### nemo-qml-plugin-dbus-qt5
        Updated : 2.1.30-1.7.2.jolla -- 2.1.32-1.8.1.jolla
        - [nemo-dbus] Support a{sv} typed parameters.
        - [nemo-dbus] Deprecation warning on org.nemomobile.dbus import.

### qt5-plugin-position-geoclue
        Updated : 5.4.2+git2-1.6.1.jolla -- 5.4.2+git3-1.7.1.jolla
        - [qtlocation] Change OSM tileserver URLs to ones which are currently available.

### qt5-qtlocation-source
        Updated : 5.4.2+git2-1.6.1.jolla -- 5.4.2+git3-1.7.1.jolla
        - [qtlocation] Change OSM tileserver URLs to ones which are currently available.

### qt5-qtsensors
        Updated : 5.6.3+git2-1.5.1.jolla -- 5.6.3+git3-1.6.1.jolla
        - [sensorfw] Use setDataRate() for settings data rates.

### sensorfw-qt5
        Updated : 0.12.6-1.8.1.jolla -- 0.14.4-1.9.1.jolla
        - [sensorfw] Fix units used for sleep in sysfsadaptor.
        - [sensorfwd] Use ms values for getAvailableIntervals() reply.
        - [hybrisadaptor] Fix build errors from unresolvable id() calls.
        - [hybrisadaptor] Define data and interval ranges earlier.
        - [hybrisadaptor] Silence als/ps initial value warnings.
        - [sensorfwd] Add node id to diagnostic logging messages
        - [clientapitest] Move unit test operator== away from API header
        - [sensorfwd] Use float values for XYZ data.
        - [tapadaptor] Silence unused parameter warnings
        - [declinationfilter] Add unit suffixes to time values
        - [hybrisadaptor] Fix setDelay() return value
        - [nodebase] Remove dead code
        - [nodebase] Use closest supported data rate.
        - [nodebase] Use m_variableName convention for all members
        - [sensorfw] Add setDataRate() D-Bus method.
        - [sensorfw] Drop evaluateIntervalRequests overloading.
        - [sensorfw] Explicitly indicate interval time units.
        - [sensorfw] Handle intervals in microsecond granularity.
        - [sensorfw] Normalize setInterval() parameter order.
        - [hybrisadaptor] Force cancellation of pending POLL transaction.
        - [hybrisadaptor] Read and process capped number of events.
        - [hybrisadaptor] Shuffle cleanup order.
        - [sendorfwd] Skip deadlocking libgbinder cleanup.

### xulrunner-qt5
        Updated : 78.15.1+git33.1-1.20.1.jolla -- 78.15.1+git33.2-1.21.1.jolla
        - [sailfishos][embedlite] Enable dialog element.

