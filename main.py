import platform
import subprocess

# This script runs the appropriate program depending 
# on the current operating system
if platform.system() == "Windows":
   print(">> python3 windows.py")
   subprocess.call("python3 windows.py", shell=True)
else:
   print(">> python3 unix_mac.py")
   subprocess.call("python3 unix_mac.py", shell=True)

