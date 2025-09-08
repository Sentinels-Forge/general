# Functions
def binToText(string):
    # Split the string by spaces and convert each binary chunk to text
    binaries = string.split()
    message = ""
    for binary in binaries:
        # Converts the binary chunk from a base two value to base 10
        dec = int(binary, 2)
        # gets the ASCII value from the decimal number
        full = chr(dec)
        message = message + full
    print(f"Your message says: {message}")

def textToBin(message):
    binaryString = ""
    for letter in message:
        # Gets the unicode number for each letter
        dec = ord(letter)
        # Gets the binary value, and strips the 0b from the start of it
        binary = bin(dec)[2:].zfill(8)
        binaryString = binaryString + binary + " "
    print(f"Your encoded string is: {binaryString}")

# Code
while True:
    choice = input("Would you like to encode [press 1], decode [press 2], or end the program [press 3]: ")
    if choice == "1":
        textToBin(input("Please enter a message: "))
    elif choice == "2":
        binToText(input("Please enter your binary: "))
    elif choice == "3":
        break

