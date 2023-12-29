# Running Jolla AppSupport/aliendalvik on regular linux distros

This is a small repo documenting the reverse enginieering of Jolla's Android AppSupport (aka Aliendalvik), including steps on how to run it on other linux distros than Sailfish OS.

## Note for everyone attempting this

Aliendalvik is a complex piece of software and requires lots of setup to run. This is a very rough set of steps, it *won't* work on the first try, be prepared to solve problems.

## Steps to run outside of Sailfish OS

1. Get a supported phone with Sailfish OS and Android AppSupport (see https://shop.jolla.com/) and grab the necessary binaries
  - Start the phone, go through setup of Sailfish OS and setup Android AppSupport
  - Get all the necessary files from the phone via SSH, see files.txt

2. Set up dependencies on the target device
  - Install dependencies from the Arch ARM repos: lxc packagekit-qt5 mlite qt5-sensors qt5-location python-pywayland dbus-glib
  - Build necessary libraries that aren't in the Arch ARM repos: libglibutil libgbinder
  - Build custom libraries from forks: [libQtContacts](https://github.com/jonas2515/qtpim/tree/alien-everwhere), [libqtcontacts_folks](https://github.com/jonas2515/qtfolks), [libqtposition_geoclue2](https://github.com/jonas2515/qtpositioning/tree/alien-everwhere), [libqtsensors_iio-sensor-proxy](https://github.com/jonas2515/qtsensors/tree/alien-everywhere)
  - Install shimming services on the target device, see shimming/
  - Build and install patched mobile-mutter and libwayland, see patches/
  - Get the vanilla (not GApps) android system.img and vendor.img from Waydroid

3. Copy all the aliendalvik config, binaries and libraries to the target device, see files.txt

4. Create necessary users, groups, and configure a few more things on the device, see setup-environment.txt

5. Edit the aliendalvik configuration on the device, see configure.txt

6. Do a manual test-run of aliendalvik to check if everything works, see running.txt

7. If you managed to run everything, there's some systemd services and scripts to automate startup of aliendalvik in the automation/ folder
