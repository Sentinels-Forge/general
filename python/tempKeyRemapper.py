import keyboard, random

listOfKeys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    "left", "right", "up", "down"
]
keysMapped = []
changedTo = []


for i in listOfKeys:
    currentChoice = i
    if currentChoice not in keysMapped:
        while True:
            changeTo = listOfKeys[random.randint(0, len(listOfKeys) - 1)]
            if changeTo not in changedTo:
                changedTo.append(changeTo)
                break
    keysMapped.append(currentChoice)
    keyboard.remap_hotkey(currentChoice, changeTo)
keyboard.wait()