import keyboard

qwertyToColemakDh = {
    "a": "a",
    "b": "v",
    "c": "c",
    "d": "d",
    "e": "f",
    "f": "g",
    "g": "t",
    "h": "h",
    "i": "u",
    "j": "j",
    "k": "k",
    "l": "y",
    "m": "m",
    "n": "n",
    "o": "o",
    "p": "p",
    "q": "q",
    "r": "r",
    "s": "s",
    "t": "x",
    "u": "i",
    "v": "b",
    "w": "w",
    "x": "z",
    "y": "e",
    "z": "f",
    " ": " "
}

def remap_keys():
    for qwerty_key, colemak_key in qwertyToColemakDh.items():
        keyboard.remap_hotkey(qwerty_key, colemak_key)

remap_keys()
keyboard.wait()
