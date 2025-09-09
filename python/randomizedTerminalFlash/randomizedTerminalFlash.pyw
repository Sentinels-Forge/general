# .pyw file so no terminal. To end, go to Task Manager and kill Python
import subprocess, os, random
from time import sleep

# Get the user so we can get the path
user = os.getlogin()

# The file we want to open
file = "popup.py"

# NOTE This is the path where the two files will be. If you change it, make sure this points to the correct directory.
folder = os.path.join(
    "C:\\Users", # \\ is a literal backslash
    user,
    "Downloads",
    "randomizedTerminalFlash",)

# Infinite loop
while True:
    # Create 1 - 3 quick popups
    for i in range(random.randint(1,3)):
        # This opens a Python program in another terminal
        popup = subprocess.Popen(f'start cmd /c python {file}', shell=True, cwd=folder)
    # Delays the next one between 30 and 250 seconds
    sleep(random.randint(30, 250))
