# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newLetters = []
    # get the offset by taking the mode
    newKey = key % 26
    # for each of the old letters, get the offseted letter
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    # build the array of letters into a string
    return "".join(newLetters)

def getNewLetter(letter, key):
    # get the ASCII code for the new letter
    newLetterCode = ord(letter) + key
    # print(letter, ', ', ord(letter))

    # letter-ASCII a-z: 97-122
    # if the code lays in the a-z range, just return the character for that code;
    # otherwise, get the offset by taking the mode
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)
