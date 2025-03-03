import platform
import subprocess

if platform.system() is "Windows":
   print(">> python3 windows.py")
   subprocess.call("python3 windows.py", shell=True)
else:
   print(">> python3 unix_mac.py")
   subprocess.call("python3 unix_mac.py", shell=True)

