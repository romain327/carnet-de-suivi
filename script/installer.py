import platform
import os

system = platform.system()

if os.path.isfile("script/start.py") :
    if system == "Windows" :
        os.system("python script/start.py")
    else :
        os.system("python3 script/start.py")
    exit(0)

else :
    with open("script/start.py", "w") as file :
        file.write("import os\n")
        file.write("import platform\n")
        file.write("system = platform.system()\n")
        file.write("if system == \"Windows\" :\n")
        file.write("    os.system(\"python script/suivi.py\")\n")
        file.write("else :\n")
        file.write("    os.system(\"python3 script/suivi3.py\")\n")
    file.close()

print("installation des librairies...")

if system == "Windows" :
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install tk")
    print("installation terminée")
    os.system("python script/start.py")

elif system == "Linux" :
    os.system("sudo apt install texlive")
    os.system("sudo apt install python3-pip")
    os.system("python3 -m pip install --upgrade --break-system-packages pip")
    os.system("python3 -m pip install --break-system-packages tk")
    print("installation terminée")
    os.system("python3 script/start.py")

else :
    os.system("sudo brew install texlive")
    os.system("sudo brew install python3-pip")
    os.system("python3 -m pip install --upgrade --break-system-packages pip")
    os.system("python3 -m pip install --break-system-packages tk")
    print("installation terminée")
    os.system("python3 script/start.py")

