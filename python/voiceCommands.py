import speech_recognition as sr
import ctypes
import os
import pygetwindow as gw
import psutil
from sentinelUtils import installPkg
import subprocess

pkgs = {"pygetwindow", "psutil", "pyaudio"}
for pkg in pkgs:
    try:
        installPkg(pkg)
    except Exception as e:
        print(f"Could not install {pkg}: {e}")

r = sr.Recognizer()

commands = {"schlafen",
            "herunterfahren",
            "schleuse",
            "schließen",
            "offen"
            }

while True:
    with sr.Microphone() as source:
        audioData = r.record(source, duration=5)
        text = r.recognize_google(audioData, language="de-DE")

        recognizedCommand = None
        for command in commands:
            if command in text.lower():
                recognizedCommand = command
                break
        if recognizedCommand == "schalfen":
            WTS_SLEEP = 0x00000004
            ctypes.windll.kernel32.SetSystemPowerState(
                WTS_SLEEP,
                False)
        elif recognizedCommand == "herunterfahren":
            os.system("shutdown /s /f /t 0")
        elif recognizedCommand == "schleuse":
            ctypes.windll.user32.LockWorkStation()
        elif recognizedCommand == "schließen":
            focused_window = gw.getWindowsWithTitle(
                gw.getActiveWindowTitle())[0]
            pid = focused_window._hWnd

            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['pid'] == pid:
                    proc.terminate()
                    print(f"Closed application: {proc.info['name']}")
        elif recognizedCommand == "offen":
            subprocess.Popen(["code"])
