"""
Russell Deady
Program I made to use the ceasar cipher encryption method
"""


def main():

    plainText = ""
    cipherText = ""
    sizeOfShift = 0

    print()
    print("Welcome to the caesar cipher encryptor!")
    plainText = input("Enter a message to encrypt (only letters and spaces): ")
    sizeOfShift = input("Enter the amount of letters you want to shift by: ")

    i = 0
    while i <= len(plainText) - 1:
        uniCodeValue = ord(plainText[i])
        if (plainText[i] == " "):
            cipherText = cipherText + " "
            i += 1
            continue
        elif (plainText[i].isalpha() == False):
            cipherText = cipherText + plainText[i]
            i += 1
            continue
        
        if (uniCodeValue < 91):
            uniCodeValue = uniCodeValue + int(sizeOfShift) % 26
            if (uniCodeValue > 90):
                uniCodeValue -= 26
        else: 
            uniCodeValue = uniCodeValue + int(sizeOfShift) % 26
            if (uniCodeValue >= 123):
                uniCodeValue -= 26
        newChar = chr(uniCodeValue)
        cipherText = cipherText + newChar

        i += 1

    print()
    print("Your encrypted message is...")
    print(cipherText)
    print()
    print("Thank you for using the encryptor!")
    print()


main()
