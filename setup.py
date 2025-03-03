import platform
import subprocess
from pathlib import Path

operating_system = platform.system()

if operating_system == "Windows":
    print(">> python3 -m ensurepip")
    subprocess.call("python3 -m ensurepip", shell=True)
    if not Path('/Scripts').exists():
        print("\n\n>> python3 -m venv ../FREAKalyze")
        subprocess.call("python3 -m venv ../FREAKalyze", shell=True)
    print("\n\n>> ./Scripts/activate")
    subprocess.run(["powershell", "-Command", "Start-Process ./Scripts/activate"])
    print("\n\n>> pip install -r ./windows_requirements.txt")
    subprocess.call("pip install -r ./windows_requirements.txt", shell=True)
else:
    print(">> python3 -m ensurepip")
    subprocess.call("python3 -m ensurepip", shell=True)
    if not Path('/bin').exists():
        print("\n\n>> python3 -m venv ../FREAKalyze")
        subprocess.call("python3 -m venv ../FREAKalyze", shell=True)
    print("\n\n>> source ./bin/activate")
    subprocess.call("source ./bin/activate", shell=True)
    print("\n\n>> pip install -r ./unix_mac_requirements.txt")
    subprocess.call("pip install -r ./unix_mac_requirements.txt", shell=True)