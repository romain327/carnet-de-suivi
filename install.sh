#!/bin/bash
sudo apt update
sudo apt install -y texlive python3-tk

echo "Would you like to create a desktop shortcut? (y/n)"
read shortcut

if [ $shortcut == "y" ]; then
    echo "Creating desktop shortcut..."
    echo "[Desktop Entry]
    Name=Suivi
    Exec=python3 $PWD/suivi.py
    Icon=$PWD/icon.png
    Terminal=false
    Type=Application
    Categories=Office;" > Carnet\ de\ suivi.desktop
    sudo mv Carnet\ de\ suivi.desktop ~/.local/share/applications/
    chmod +x ~/.local/share/applications/Carnet\ de\ suivi.desktop
fi

echo "installation complete"
exit 0