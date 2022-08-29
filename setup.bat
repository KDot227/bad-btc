@echo off

cd /d %~dp0
color a

python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
pyinstaller -v>NUL
if errorlevel 1 goto errorNoPyInstaller
python -m pip install --upgrade -r requirements.txt
cls
python -m main.py
pause
exit

:errorNoPython
echo Python is not installed on your system or not added to path!!!
pause
exit

:errorNoPip
echo Pip is not installed on your system or not added to path!!!
pause
exit

:errorNoPyInstaller
echo Pyinstaller is not installed on your system or not added to path!!!
pause
exit