=======================================
SAILFISH OS
Changelog from 4.4.0.68 to 4.4.0.72
2022-09-30
=======================================
# PACKAGES MODIFIED

### buteo-sync-plugins-sailfisheas
- Updated : 0.1.2-1.5.1.jolla -- 0.1.3-1.6.2.jolla
- [common] Derive sync service name from provider.
### jolla-settings-accounts
- Updated : 0.4.57.1-1.6.1.jolla -- 0.4.57.2-1.7.1.jolla
- [settings-accounts] Support 3-legged OAuth 1.0a flow with external browser.
### libjollasignonuiservice-qt5
- Updated : 0.4.14-1.3.1.jolla -- 0.4.17-1.4.1.jolla
- [libjollasignonservice] Get state query item from OAuth plugin.
- [signonuiservice] Support external browser with 3-legged OAuth.
- [signonuiservice] Switch OAuth to gecko WebView.
### libsailfishkeyprovider-data-jolla
- Updated : 0.0.18-1.2.1.jolla -- 0.1.0-1.3.2.jolla
- [keyprovider-data] Add sailfisheas data.
### mic
- Updated : 1.0.9-1.3.57.jolla -- 1.0.11-1.4.13.jolla
- [mic] Automatically create missing /var/lock.
- [mic] Run scripts verbosely when mic is verbose
- [mic] Run scripts with errexit when --erroronfail is used.
- [packaging] Require kmod.
### ofono-binder-plugin
- Updated : 1.1.3-1.3.1.jolla -- 1.1.5-1.4.2.jolla
- [debian] Bumped debhelper compat level to 7
- [ofono-binder] Fix call forwarding query.
- [debian] Updated changelog version
- [ofono-binder] Fetch IMS registration state from one place.
### patterns-sailfish
- Updated : 1.1.6+git1-1.7.1.jolla -- 1.1.6+git2-1.8.1.jolla
- [patterns] Require 'android-tools' from image-creation-tools.
- [patterns] Require 'atruncate' from image-creation-tools.
### pj-oss-project-config
- Updated : 0.0.20-1.8.1.jolla -- 0.0.22-1.9.2.jolla
- [prjconf] Ensure diffutils are available for build-compare.
- [prjconf] Set source_date_epoch_from_changelog.
### qmf-eas-plugin
- Updated : 0.3.40-1.3.5.jolla -- 0.4.1-1.5.1.jolla
- [qmf-eas-plugin] Fix checking credentials again after failure.
- [qmf-eas-plugin] Use outlook.office.com domain in scopes.
- [qmf-eas-plugin] Add account update page.
- [qmf-eas-plugin] Add support for logging in with OAuth.
- [qmf-eas] Remove declarations without implementation.
### qtmozembed-qt5
- Updated : 1.53.22-1.32.2.jolla -- 1.53.23-1.33.1.jolla
- [qtmozembed] Use physicalDotsPerInch for EmbedLiteView dpi.
### rpmlint
- Updated : 2.0.0+git2-1.6.14.jolla -- 2.0.0+git2.1-1.7.3.jolla
- [rpmlint] Ignore dynamic parts of version/release number.
### sailfish-browser
- Updated : 2.2.38.4-1.25.1.jolla -- 2.2.54.1-1.26.1.jolla
- [browser] Ignore SIGPIPE. 
- [browser] Quick copy url to clipboard by press-and-hold url from toolbar. 
- [ua] Add linux for facebook user-agent. 
- [user-agent] Update preprocessed user agent overrides
- [ua] Add linux for facebook user-agent. 
- [user-agent] Update user-agent overrides for 78.0. 
- [user-agent] Update preprocessed user agent overrides
- [ua] Adjust linkedin.com user-agent. 
- [user-agent] Update user-agent overrides for 78.8. 
- [user-agent] Update preprocessed user agent overrides
- [browser] Remove browser application name from google domain overrides. 
- [browser] Do not raise overlay when starting with requested url. 
- [browser] Webview test crash fix. 
- [tests] Stabilize declarativehistorymodel test case. 
- [browser] Fix icon for add to app grid. 
- [browser] Bump up package version
- [browser] Cleanup general.useragent.override from preferences. 
- [browser] Fix popup input region. 
- [browser] Fix tab closing in app exit. 
- [browser] Explicitly state Camera permission. 
- [browser] Make it possible to configure max live tab count via setting. 
- [tests] Stop embedding after views&window destoyed (tst_webview). 
- [tests] Do not spy urlChanged signals on forwardBackwardNavigation case. 
- [tests] Mark tst_webview restart test as skipped. 
- [tests] Mark webcontainer of tst_webview as C++ owned. 
- [tests] Sleep 10ms whilst waiting for signals. 
- [tests] Add running property to the test object. 
- [tests] Cleanup tst_logins. 
- [browser] Add missing method for webpage mock
- [tests] Improve test case comments. 
- [tests] The most recently used tab is activated when an active tab is closed. 
- [tests] Wait that created tabs are loaded. 
- [browser] After closing the active shift new active tab index. 
- [browser] Support touch events when selection active. 
- [user-agent] Update preprocessed user agent overrides for m.vk.com
- [browser] Decreate overlay animation duration to 250ms. 
- [browser] Add invisible footer for favorite grid and history list. 
- [browser] Follow drag direction when opening / closing overlay. 
### sailfish-eas
- Updated : 0.5.18.1-1.5.1.jolla -- 0.5.18.3-1.6.1.jolla
- [sailfish-eas] Allow alternative provider and service name.
- [sailfish-eas] Add OAuth to login flow and protocol commands.
- [sailfish-eas] Ask to update credentials on failure.
- [sailfish-eas] Implement token refresh on authentication error.
### sailfish-mdm
- Updated : 0.4.14-1.4.32.jolla -- 0.4.15-1.5.1.jolla
- [docs] Fix links to User Manager docs.
### sailfish-qdoc-template
- Updated : 0.1.0-1.2.2.jolla -- 0.3-1.3.2.jolla
- [sailfish-qdoc-template] Package documentation in HTML format.
- [sailfish-qdoc-template] Allow linking between projects.
- [sailfish-qdoc-template] Export BASE_URL to qdoc.
### sailjail-permissions
- Updated : 1.1.0-1.31.2.jolla -- 1.1.1-1.32.4.jolla
- [docs] Advice on data migration.
### sdk-setup
- Updated : 1.4.58-1.25.1.jolla -- 1.4.61-1.26.1.jolla
- [mb2] Fix passing arguments to make with %make_build.
- [git-change-log] Allow for changes in tag naming conventions.
- [git-change-log] Only consider tags reachable through first parent
- [mb2] Prefer .changes.run file over .changes.
### signon-plugin-oauth2-qt5
- Updated : 0.21.7+git1-1.5.1.jolla -- 0.25+git1-1.6.1.jolla
- [git] Move submodule repos to github.
- [signon-plugin-oauth2] Update to version 0.25.
### signon-qt5
- Updated : 8.60.0+git5-1.9.1.jolla -- 8.60.0+git6-1.10.2.jolla
- [libsignon] Increase maximum token storage size.
### user-managerd
- Updated : 0.8.5-1.7.2.jolla -- 0.8.7-1.8.2.jolla
- [docs] Fix index file generation.
- [user-managerd] Include license file as %license.

-- the end --