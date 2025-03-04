import platform
import subprocess
from pathlib import Path

# This script handles setting up a virtual environment and 
# installing necessary modules, which change depending on 
# the operating system

operating_system = platform.system()

# For Windows
if operating_system == "Windows":

    # Ensure that pip exists
    print(">> python3 -m ensurepip")
    subprocess.call("python3 -m ensurepip", shell=True)

    # if a virtual environment has not been initialized, 
    # initialize one
    if not Path('/Scripts').exists():
        print("\n\n>> python3 -m venv ../FREAKalyze")
        subprocess.call("python3 -m venv ../FREAKalyze", shell=True)

    # Activate the virtual environment
    print("\n\n>> ./Scripts/activate")
    subprocess.run(["powershell", "-Command", "Start-Process ./Scripts/activate"])

    # Install required modules
    print("\n\n>> pip install -r ./windows_requirements.txt")
    subprocess.call("pip install -r ./windows_requirements.txt", shell=True)

# For Mac and Unix
else:

    # Ensure that pip exists
    print(">> python3 -m ensurepip")
    subprocess.call("python3 -m ensurepip", shell=True)

    # if a virtual environment has not been initialized, 
    # initialize one
    if not Path('/bin').exists():
        print("\n\n>> python3 -m venv ../FREAKalyze")
        subprocess.call("python3 -m venv ../FREAKalyze", shell=True)

    # Activate the virtual environment
    print("\n\n>> source ./bin/activate")
    subprocess.call("source ./bin/activate", shell=True)

    # Install required modules
    print("\n\n>> pip install -r ./unix_mac_requirements.txt")
    subprocess.call("pip install -r ./unix_mac_requirements.txt", shell=True)