@echo off
setlocal

REM Define the URL for the TeX Live installer
set INSTALLER_URL=http://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe

REM Define the path where the installer will be downloaded
set DOWNLOAD_PATH=%TEMP%\install-tl-windows.exe

REM Download the TeX Live installer
echo Downloading TeX Live installer...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%INSTALLER_URL%', '%DOWNLOAD_PATH%')"

REM Check if the download was successful
if not exist "%DOWNLOAD_PATH%" (
    echo Failed to download the TeX Live installer.
    exit /b 1
)

REM Start the TeX Live installation process
echo Starting TeX Live installation...
start "" "%DOWNLOAD_PATH%"

python -m pip install requirements.txt

REM Create a shortcut to the application (optional)
echo Creating shortcut...
set SHORTCUT_NAME=Carnet de suivi
set SHORTCUT_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs
set SHORTCUT_TARGET=%~dp0suivi.py
set SHORTCUT_ICON=%~dp0icon.ico
set SHORTCUT_DESCRIPTION=Ouvre le carnet de suivi

powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%SHORTCUT_PATH%\%SHORTCUT_NAME%.lnk'); $Shortcut.TargetPath = '%SHORTCUT_TARGET%'; $Shortcut.IconLocation = '%SHORTCUT_ICON%'; $Shortcut.Description = '%SHORTCUT_DESCRIPTION%'; $Shortcut.Save()"
if errorlevel 1 (
    echo Failed to create the shortcut.
    exit /b 1
)

endlocal
exit /b 0