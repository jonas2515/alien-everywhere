================================================================
SAILFISH OS
Changelog from 4.3.0.12 to 4.3.0.15
2022-02-07
================================================================
Packages modified 
    polkit
        Updated : 0.105+git5-1.5.3.jolla -- 0.105+git8-1.6.1.jolla
        - [polkit] Fix for CVE-2021-4034 (PwnKit). 
        - [polkit] Drop unneeded Debian patches. 
        - [packaging] Separate Debian patches from the rest
        - [packaging] Use pkgconfig symbols for -devel requires
        - [polkit] Update Debian patches, drop patches already included. 
    ruby
        Updated : 2.7.1+git1 -- 2.7.1+git2
        - [ruby] Fix build with newer bison. 
	sdk-setup
		Updated : 1.4.11-1.5.1.jolla -- 1.4.42-1.6.1.jolla
		- [mb2] Refresh git index before creating a stash. 
		- [mb2] Sync as needed when closing maintenance shell. 
		- [oomadvice] Do not check journal where it is not available. 
		- [sdk-manage] Allow to explicitly operate on snapshots. 
		- [sdk-manage] Fix reseting snapshot forcefully. 
		- [mb2] Do not fail to create git-stash. 
		- [sdk-chroot] Add support for usernames with a dot. 
		- [mb2] Deal with git worktree without commits. 
		- [mb2] Allow to diff build environment changes. 
		- [sdk-assistant] Allow to clone build tools. 
		- [mb2] Cache packages installed as build deps under snapshots. 
		- [sdk-manage] Allow to prune package caches
		- [sdk-manage] Fix checking for package removal in original target. 
		- [sdk-manage] Fix checking for RPM DB changes in original target. 
		- [mb2] Only reset snapshot if pulling build requires. 
		- [sdk-manage] Do not clean package cache when updating. 
		- [sdk-manage] Fix reseting snapshots after SSU changes
		- [mb2] Fix buildroot timestamp check under VBox. 
		- [sdk-setup] Do not rely on ConnMan for proxy configuration. 
		- [sdk-setup] Do not use systemd under Docker. 
		- [mb2] Print progress during zypper based deployment. 
		- [sdk-chroot] Export SAILFISH_SDK. 
		- [sdk-chroot] Rename mer-sdk-chroot to sdk-chroot. 
		- [mb2] Fix false error on talking to SSH agent. 
		- [sdk-init] Support ApplicationName. 
		- [mb2] Allow deployment with password-protected SSH keys. 
		- [mb2] Allow running builds concurently. 
		- [mb2] Do not pollute random CWDs with state files. 
		- [mb2] Do not purge default output dir. 
		- [mb2] Fix applying patches with CRLF on Unix. 
		- [mb2] Fix explicit pull with --no-pull-build-requires
		- [mb2] Fix use with .spec with local includes. 
		- [mb2] Prune older RPMs by default. 
		- [sdk-assistant] Do not leak true command name in messages. 
		- [sdk-vm] Do not automatically refresh RPM repos. 
		- [sdk-make-qmltypes] Allow in-place use without deployment. 
		- [sdk-manage] Do not fail to sync targets with broken symlinks. 
		- [mb2] Do not switch to snapshot for 'run' command
		- [sdk-make-qmltypes] Automatically determine source revision. 
		- [sdk-make-qmltypes] Continue batch after job failure
		- [sdk-make-qmltypes] Use per-user media path. 
		- [mb2] Exit if applying patch fails. 
		- [sdk-manage] Use rpmdb directly. 
		- [sdk-setup] Use correct Short Name for the license. 
		- [sdk-setup] Use correct Short Names for the license. 
		- [sdk-assistant] Be more clear about (not) proceeding with target update
		- [sdk-assistant] Do not always suppress zypper interactivity. 
		- [sdk-assistant] Supplying a password is a confirmation. 
		- [sdk-manage] Do not leak zypper processes when interrupted. 
		- [sdk-manage] Handle more info-level zypper exit codes
		- [sdk-assistant] Make package-search alias of package-list. 
		- [sdk-assistant] Rename package-list to package-search. 
		- [mb2] Allow more control over sb2 invocation. 
		- [packaging] BuildRequire systemd via pkgconfig. 		
		- [sdk-manage] Don't add trailing slash to tooling path. 
		- [mb2] Fix error handling in build and package commands. 
    ssu
        Updated : 1.0.14-1.5.1.jolla -- 1.0.14.1-1.6.1.jolla
        - [ssu] Make sure the ssu cache is up-to-date. 



