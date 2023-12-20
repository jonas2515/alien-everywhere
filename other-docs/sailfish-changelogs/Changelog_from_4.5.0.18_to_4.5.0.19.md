# SAILFISH OS: Changelog from 4.5.0.18 to 4.5.0.19

2023-03-15

## Packages modified (8)

### aliendalvik-configs
- Updated : 11.0.26-1.17.1.jolla -- 11.0.26.2-1.18.1.jolla
- [appsupport] Fix startup during SailfishOS boot.
- [appsupport] Fix supplementary service control.
- [appsupport] restart container after new wayland socket.

### connman
- Updated : 1.32+git193-1.18.1.jolla -- 1.32+git194-1.19.1.jolla
- [clat] Add frag hdr and dynamic pool support.
- [clat] Avoid tayga zombies, fix config, improve state changes.
- [clat] Call task stop only once.
- [clat] Delay DNS query to ipv4only.arpa until nameservers are set.
- [clat] Do DAD immediately when CLAT starts, then with timeout.
- [clat] Do restart if interface is lost/invalid.
- [clat] Do task stop when prefix cannot be resolved.
- [clat] Ensure cleanup and stop in error cases.
- [clat] Fix DAD return value use and reply processing.
- [clat] Fix error cases, add leeway + tolerance for resolv errors.
- [clat] Fix memory leaks and mem use error.
- [clat] Fix prefix resolv failure shutdown case.
- [clat] Fix process start and restart cases, handle segfaults.
- [clat] Handle GResolv error cases better, support resolv retry.
- [clat] Implement clat plugin to run tayga for IPv6 cellular.
- [clat] Improve interface error handling and fix if error restart.
- [clat] Improve tethering state monitor, stop if IPv6 goes away.
- [clat] Keep ptr to ipconfig between IPv6 prep and restore.
- [clat] Monitor tethering changes and enable double nat if on.
- [clat] Prepare NAT when interface is up, add MTU 1260 for IPv4 route.
- [clat] Re-add prefix query timeout, fix prefix change check.
- [clat] Repeat prefix query for NO_ANSWER when doing initial one.
- [clat] Stop CLAT if default changes to NULL.
- [clat] Use wakeup timer for DAD and GResolv.
- [connman] Implement CLAT support with tayga.
- [inet] Add functions for creating and removing tun dev.
- [inet] Add support for add/del neighbour proxy.
- [inet] Expose ipv6_do_dad for plugins.
- [inet] Review fix: Add functions for creating and removing tun dev.
- [inet] Set host flag only for a single IPv6 host route.
- [inet] Support adding IPv4 network routes with metric and MTU.
- [ipconfig] Add get/set for ipaddress, accept_ra, ndproxy.
- [nat] Add IPv6 preparation and double NAT support.
- [ofono] Clear IP-address when protocol does not use it.
- [packaging] Depend on tayga.
- [service] Add getter wrapper for ipconfig.
- [tools] Add ipconfig/inet dummies for iptables test.
- [unit] Add CLAT plugin unit tests.
- [unit] Add dummies for ipconfig ref/unref to iptables unit.

### droid-hal-pdx213
- Updated : 1.9.5-1.6.6.jolla -- 1.9.6-1.7.1.jolla
- [Kernel] Enable BNEP options
- [kernel] Fix random restarts while using Android AppSupport or crash reporter
- [kernel] input: sec_ts: Don't use ts->debug_flag to early, fix compile error.
- [kernel] psi: Fix uaf issue when psi trigger is destroyed while being polled.
- [kernel] usb: gadget: ffs: Remove IPC logging support.

### jolla-calendar
- Updated : 1.1.5-1.9.1.jolla -- 1.1.6-1.10.1.jolla
- [calendar] Fix date opened externally.
- [jolla-calendar] Add a gotoDate() function to views.
- [jolla-calendar] Adjust size of view in container.
- [jolla-calendar] Bind view date in TabHeader instance.
- [jolla-calendar] Fix DBus invocation to go to a specific date.
- [jolla-calendar] Replace the gotoToday() signal with gotoDate()
- [jolla-calendar] Use bindings for tab header height.

### jolla-settings-system
- Updated : 1.2.5.3-1.15.1.jolla -- 1.2.5.4-1.16.1.jolla
- [settings-system] Fix landscape lock screen with virtual keyboard.

### lipstick-jolla-home-qt5
- Updated : 1.25.13.3-1.15.1.jolla -- 1.25.13.6-1.16.1.jolla
- [lipstick-jolla-home] Fixup silica requirement.
- [lipstick-jolla-home] Use File.exist to check Weather and Calendar widgets.
- [lipstick-jolla-home] Allow captiveportal raise during Startup Wizard.

### sailfish-homescreen
- Updated : 0.1.7-1.5.1.jolla -- 0.1.7.1-1.6.1.jolla
- [sailfish-homescreen] Trigger captive portal during SUW when requested.

### sailfishsilica-qt5
- Updated : 1.2.103-1.13.2.jolla -- 1.2.103.1-1.14.1.jolla
- [silica] Add internal qmlImportPath.

## Packages added (1)

### tayga
- Binaries added : tayga - 0.9.2+git3-1.1.1.jolla
- [tayga] Remove the ignored patches as well because of OBS.
- [tayga] EAM patches break CLAT, ignore them for now.
- [tayga] Adding packaging data.

