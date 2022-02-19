'''A dictionary of all apps to download.

----------INSTRUCTIONS----------
Add a new dict entry by providing the following parameters to cl.App():
- name: app/program name
- download_page: the page where the download link/button would be found in
your browser; usually the site's homepage 
- pattern: a regex pattern, used to get the correct download link (i.e. the
latest stable build for 64-bit Windows) from the download page.
- (optional) download_url: a direct link to the file, if the direct download
link is hard to retrieve through scraping alone
- (optional) base_url: the first part of a download url

Note: Consider providing a download_url parameter anyway if the file is large
(100+MB) and the direct download link leads to the latest version of the
software. This will let you skip all scraping operations and significantly
improve performance.

Instead, consider the base_url parameter if the class can't reconstruct the
absolute url normally (i.e. if the site's relative urls are not clean and
coherent). Github is an example of this issue, but is handled automatically
as a special case in classes.py.

----------ISSUES----------
Currently unable to automatically get the latest update for the following:
- GoldenDict (but hasn't been updated since 2019)
- Logitech SetPoint: dynamic content page, can't scrape download link
- OpenOffice: redirects to v3.3 instead of latest
- Signal: can't find download url through scraping
- Slack: can't find download url through scraping
- Sumatra PDF: can't find download url through scraping
Direct links are provided as 'download_url' parameter for the time being.
'''

import re

import classes as cl

programs = {
    '7zip' : 
        cl.App( '7zip',
                r'https://www.7-zip.org/',
                re.compile(r'7z.+-x64\.exe'),
                base_url=r'https://www.7-zip.org/'),
    'Adobe Reader' :
        cl.App( 'Adobe Reader',
                r'https://get.adobe.com/reader/?promoid=TTGWL47M',
                re.compile(r'readerdc_en_xa_crd_install.exe'),
                download_url=r'https://admdownload.adobe.com/bin/live/readerdc_en_xa_crd_install.exe'),
    'Audacity' :
        cl.App( 'Audacity',
                r'https://github.com/audacity/audacity/releases',
                re.compile(r'audacity-win-\d\.\d{1,2}\.\d{1,2}-64bit.exe')),
    'Authy' :
        cl.App( 'Authy',
                r'https://electron.authy.com/download?channel=stable&arch=x64&platform=win32&version=latest&product=authy',
                re.compile(r'Authy%20Desktop%20Setup%20\d\.\d{1,2}\d.\d{1,2}\d.exe')),
    'Brave' :
        cl.App( 'Brave',
                r'https://laptop-updates.brave.com/latest/winx64',
                re.compile(r'BraveBrowserSetup\.exe')),
    'Brother DCP-L2520DW' :
        cl.App( 'Brother DCP-L2520DW',
                r'https://download.brother.com/welcome/dlf100993/DCP-L2520DW-inst-C1-US.EXE',
                re.compile(r'DCP-L2520DW.+\.EXE'),
                download_url=r'https://download.brother.com/welcome/dlf100993/DCP-L2520DW-inst-C1-US.EXE'),
    'Calibre' :
        cl.App( 'Calibre',
                r'https://calibre-ebook.com/download_windows64',
                re.compile(r'kovidgoyal/.+calibre-64bit-.+\..+\..+\.msi')),
    'DeepL' :
        cl.App( 'DeepL',
                r'https://www.deepl.com/windows/download/full/DeepLSetup.exe',
                re.compile(r'DeepLSetup.exe'),
                download_url='https://www.deepl.com/windows/download/full/DeepLSetup.exe'),
    'Deluge' :
        cl.App( 'Deluge',
                r'https://ftp.osuosl.org/pub/deluge/windows/?C=M;O=D',
                re.compile(r'deluge-\d\.\d{1,2}\.\d{1,2}-win\d\d-py[23]\.\d{1,2}\.exe'),
                base_url='https://ftp.osuosl.org/pub/deluge/windows/'),
    'Discord' :
        cl.App( 'Discord',
                r'https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86',
                re.compile(r'DiscordSetup\.exe')),
    'Everything' :
        cl.App( 'Everything',
                r'https://www.voidtools.com',
                re.compile(r'Everything-.+\.x64-Setup\.exe$'),
                base_url=r'https://www.voidtools.com'),
    'Firefox' :
        cl.App( 'Firefox',
                r'https://mzl.la/3Bp818K',
                re.compile(r'Firefox Installer\.exe')),
    'foobar2000' :
        cl.App( 'foobar2000',
                r'https://www.foobar2000.org/download',
                re.compile(r'foobar2000_v.+\.exe'),
                base_url=r'https://www.foobar2000.org/files/'),
    'Git for Windows' :
        cl.App( 'Git for Windows',
                r'https://github.com/git-for-windows/git/releases',
                re.compile(r'Git-.+-64-bit\.exe')),
    # See http://www.goldendict.org/forum/viewtopic.php?f=4&t=22597
    'GoldenDict 1.5.0 RC2 372 QT 5123 x64' :
        cl.App( 'GoldenDict 1.5.0 RC2 372 QT 5123 x64',
                r'https://sourceforge.net/projects/goldendict/files/early%20access%20builds/Qt5-based/64bit/',
                re.compile(r'GoldenDict-1\.5\.0-RC2-372-.+QT_5123.+64bit.+\.7z'),
                download_url=r'https://netcologne.dl.sourceforge.net/project/goldendict/early%20access%20builds/Qt5-based/64bit/GoldenDict-1.5.0-RC2-372-gc3ff15f_%28QT_5123%29%2864bit%29.7z'),
    'Google Drive (Backup and Sync)' :
        cl.App( 'Google Drive (Backup and Sync)',
                r'https://www.google.com/drive/download/',
                re.compile(r'installbackupandsync.exe$'),
                download_url=r'https://dl.google.com/tag/s/appguid%3D%7B3C122445-AECE-4309-90B7-85A6AEF42AC0%7D%26iid%3D%7B9648D435-67BA-D2A7-54D2-1E0B5656BF03%7D%26ap%3Duploader%26appname%3DBackup%2520and%2520Sync%26needsadmin%3Dtrue/drive/installbackupandsync.exe'),
    'Handbrake' :
        cl.App( 'Handbrake',
                r'https://github.com/HandBrake/HandBrake/releases',
                re.compile(r'HandBrake-\d\.\d{1,2}\.\d{1,2}-x86_64-Win_GUI\.exe')),
    'Google Japanese Input' :
        cl.App( 'Google Japanese Input',
                r'https://tools.google.com/dlpage/japaneseinput/eula.html?platform=win',
                re.compile(r'GoogleJapaneseInputSetup.exe'),
                download_url=r'https://dl.google.com/tag/s/appguid%3D%7BDDCCD2A9-025E-4142-BCEB-F467B88CF830%7D%26iid%3D%7B1675F496-05ED-DDAF-E3DB-35121BF844C5%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Japanese%2520Input%26needsadmin%3Dtrue%26ap%3Dexternal-stable-universal/japanese-ime/GoogleJapaneseInputSetup.exe'),
    'Line' :
        cl.App( 'Line',
                r'https://desktop.line-scdn.net/win/new/LineInst.exe',
                re.compile(r'LineInst\.exe'),
                download_url='https://desktop.line-scdn.net/win/new/LineInst.exe'),
    'Logitech Options' :
        cl.App( 'Logitech Options',
                r'https://download01.logi.com/web/ftp/pub/techsupport/options/options_installer.exe',
                re.compile(r'options_installer\.exe'),
                download_url='https://download01.logi.com/web/ftp/pub/techsupport/options/options_installer.exe'),
    'Logitech SetPoint 6.70.55 x64' :
        cl.App( 'Logitech SetPoint 6.70.55 x64',
                r'https://support.logi.com/hc/en-us/articles/360025141274-SetPoint',
                re.compile(r'SetPoint.+_64\.exe$'),
                download_url=r'https://download01.logi.com/web/ftp/pub/techsupport/mouse/SetPoint6.70.55_64.exe'),
    'Mayflash Wii U Pro W009' :
        cl.App( 'Mayflash Wii U Pro W009',
                r'https://www.mayflash.com/Support/showdownload.php?id=98',
                re.compile(r'W009%20.+Adapter\.exe$')),
    'Malwarebytes' :
        cl.App( 'Malwarebytes',
                r'https://downloads.malwarebytes.com/file/mb-windows',
                re.compile(r'MBSetup\.exe'),
                download_url='https://data-cdn.mbamupdates.com/web/mb4-setup-consumer/MBSetup.exe'),
    'NordVPN' :
        cl.App( 'NordVPN',
                r'https://nordvpn.com/download/',
                re.compile(r'NordVPNSetup\.exe')),
    'OBS Studio' :
        cl.App( 'OBS Studio',
                r'https://obsproject.com/',
                re.compile(r'OBS-Studio-\d\d\.\d{1,2}\.\d{1,2}-Full-Installer-x64.exe')),
    'OpenOffice' :
        cl.App( 'OpenOffice',
                r'https://netcologne.dl.sourceforge.net/project/openofficeorg.mirror/4.1.10/binaries/en-US/Apache_OpenOffice_4.1.10_Win_x86_install_en-US.exe',
                re.compile(r'Apache_OpenOffice_\d\.\d{1,2}\.\d{1,2}_Win_x86_install_en-US\.exe'),
                download_url=r'https://netcologne.dl.sourceforge.net/project/openofficeorg.mirror/4.1.10/binaries/en-US/Apache_OpenOffice_4.1.10_Win_x86_install_en-US.exe'),    
    'Powershell 7' :
        cl.App( 'Powershell 7',
                r'https://github.com/PowerShell/PowerShell/releases/',
                re.compile(r'PowerShell-\d\.\d{1,2}\.\d{1,2}-win-x64\.msi')),
    'Python' :
        cl.App( 'Python',
                r'https://www.python.org/downloads/',
                re.compile(r'python-\d\.\d{1,2}\.\d{1,2}-amd64\.exe')),
    'Signal' :
        cl.App( 'Signal',
                r'https://updates.signal.org/desktop/signal-desktop-win-5.9.0.exe',
                re.compile(r'signal-desktop-win-\d\.\d{1,2}\.\d{1,2}\.exe'),
                download_url=r'https://updates.signal.org/desktop/signal-desktop-win-5.9.0.exe'),
    'Slack' :
        cl.App( 'Slack',
                r'https://downloads.slack-edge.com/releases/windows/4.18.0/prod/x64/SlackSetup.exe',
                re.compile(r'SlackSetup.exe'),
                download_url=r'https://downloads.slack-edge.com/releases/windows/4.18.0/prod/x64/SlackSetup.exe'),
    'Steam' :
        cl.App( 'Steam',
                r'https://store.steampowered.com/about/',
                re.compile(r'SteamSetup.exe')),
    'Sumatra PDF' :
        cl.App( 'Sumatra PDF',
                r'https://kjkpubsf.sfo2.digitaloceanspaces.com/software/sumatrapdf/rel/SumatraPDF-3.3.1-64-install.exe',
                re.compile(r'SumatraPDF-\d{1}\.\d{1,2}\.\d{1,2}-64-install\.exe')),
    'TeraCopy' :
        cl.App( 'TeraCopy',
                r'https://www.codesector.com/downloads',
                re.compile(r'teracopy.exe'),
                base_url = r'https://www.codesector.com'),
    'VLC' :
        cl.App( 'VLC',
                r'https://www.videolan.org/vlc/',
                re.compile(r'vlc-\d\.\d{1,2}\.\d{1,2}-win64\.exe$'),
                base_url=r'https:'),
    'VS Code' :
        cl.App( 'VS Code',
                r'https://code.visualstudio.com/sha/',
                re.compile(r'stable/.+VSCodeUserSetup-x64-.+\.exe$')),                                     
    'Windows Terminal' :
        cl.App( 'Windows Terminal',
                r'https://github.com/microsoft/terminal/releases',
                re.compile(r'Microsoft\.WindowsTerminal_\d\.\d{1,2}\.\d{4}\.\d_8wekyb3d8bbwe\.msixbundle$'))
}