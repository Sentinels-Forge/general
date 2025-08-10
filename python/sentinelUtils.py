import subprocess
import sys
import os
from pathlib import Path
import hashlib
import platform
import ensurepip


def installPkg(package):
    '''Takes one arguement: package.\n
    Typically, you pass a list of pkg names for the arguement.'''
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-qqq",
        package])


def getFileHash(filepath, algorithm="sha256"):
    '''Takes one arguement: filepath.\n
    It then returns the hash of the file.'''
    try:
        hashFunc = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hashFunc.update(chunk)
        return hashFunc.hexdigest()
    except Exception as e:
        print(f"Error computing hash for {filepath}: {e}")
        return 1


# Please note that the following two functions are deprecated
# and need to be refactored.

def checkProgRun():
    '''A helper function for quitCusom().'''
    global progRun
    if progRun is False:
        exit()


def quitCustom():
    '''To be paired with a main loop that runs while progRun is True.'''
    input("Press Enter to close the program.\n>")
    global progRun
    progRun = False
    checkProgRun()


def findDuplicates(list):
    '''Prints out duplicates in a list to console.\n
    Takes one arguement: list.'''
    encountered = {}
    duplicates = []

    for index in range(len(list)):
        value = list[index]
        if value in encountered:
            duplicates.append((value, index))
        else:
            encountered[value] = index

    if duplicates:
        print("Duplicates found:")
        for item in duplicates:
            print(f"Value: {item[0]} at index: {item[1]}")
    else:
        print("No duplicates found.")


def letterToBin(letter):
    '''Takes one arguement: letter.\n
    Returns the letters binary equivalent.'''
    decimalLetter = ord(letter)
    binStr = bin(decimalLetter)
    binStr = binStr[2:]
    return binStr


def collectMatchingFiles(source, extensions):
    '''Takes two arguements: source, extensions.\n
    Starting in the source directory, it will grab the paths\n
    of all files with matching extensions.'''
    for root, _, files in os.walk(source):
        for file in files:
            if Path(file).suffix.lower() in extensions:
                absPath = os.path.join(root, file)
                relPath = os.path.relpath(absPath, start=source)
                yield (absPath, relPath)


def findDrive(username):
    '''Takes one arguement: username.\n
    Returns the first external drive found.'''
    system = platform.system()
    drives = []
    if system == "Windows":
        import ctypes
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if bitmask & 1:
                drive = f"{letter}:\\"
                drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
                if drive_type == 2:
                    drives.append(drive)
            bitmask >>= 1
    else:
        mountPoints = [f"/media/{username}",
                       f"/run/media/{username}",
                       f"/Volumes/{username}"]
        for mountPoint in mountPoints:
            if os.path.exists(mountPoint):
                for entry in os.listdir(mountPoint):
                    path = os.path.join(mountPoint, entry)
                    if os.path.ismount(path):
                        drives.append(path)
    if not drives:
        print("[WARN] No external removable drive detected.")
        return None
    return drives[0]


def ensurePip():
    '''Attempts to ensure that pip is installed.\n
    Uses ensurepip.bootstrap() and then get-pip methods.'''
    try:
        import pip  # noqa: F401
    except ImportError:
        try:
            ensurepip.bootstrap()
        except Exception:
            try:
                import urllib.request
                url = "https://bootstrap.pypa.io/get-pip.py"
                with urllib.request.urlopen(url) as response:
                    script = response.read()
                exec(script, {'__name__': '__main__'})
            except Exception as e:
                print(f"Failed to install pip using any method: {e}")
                sys.exit(1)
