import sys

def encryptionFormula(character,key=3):

    Alphabets ={
                 0 : 'a',  1: 'b',   2: 'c',  3: 'd',  4: 'e',
                 5 : 'f',  6: 'g',   7: 'h',  8: 'i',  9: 'j',
                 10: 'k', 11: 'l',  12: 'm', 13: 'n', 14: 'o',
                 15: 'p', 16: 'q',  17: 'r', 18: 's', 19: 't',
                 20: 'u', 21: 'v',  22: 'w', 23: 'x', 24: 'y',
                 25: 'z', 26: ' ',  27: '.',
                 }
    
    characterKey = next((key for key, value in Alphabets.items() if value == character), None)
    if characterKey == None:
        print(f"Character = {character} not found!!!")
        sys.exit()

    Cipher = (characterKey+key)%len(Alphabets)
    return Alphabets[Cipher]


def encryption(textToEncrypt):
    
    encryptedText = ""
    for character in textToEncrypt:
        encryptedText+=encryptionFormula(character.lower())
    return encryptedText


if "__main__" == __name__:
    textToEncrypt = "network security and cryptography."
    print(f"textToEncrypt : {textToEncrypt}")
    encryptedText = encryption(textToEncrypt) 
    print(f"encryptedText : {encryptedText}")
    