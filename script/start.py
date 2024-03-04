import os
import platform
system = platform.system()
if system == "Windows" :
    os.system("python script/suivi.py")
else :
    os.system("python3 script/suivi.py")
