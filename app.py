import os
import platform

system = platform.system()

if system == "Windows" :
    os.system("python script/installer.py")

else :
    os.system("python3 script/installer.py")