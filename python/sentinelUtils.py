import subprocess
import sys
import hashlib


def installPkg(package):
    '''Takes one arguement, package.\n
    Typically, you pass a list of pkg names for the arguement.'''
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-qqq",
        package])


def getFileHash(filepath, algorithm="sha256"):
    '''Takes one arguement, filepath.\n
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
