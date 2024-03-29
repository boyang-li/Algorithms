# O(4ˆn * n) time | O(4ˆn * n) space
def phoneNumberMnemonics(phoneNumber):
    currMnemonic = ["0"] * len(phoneNumber)
    mnemonicsFound = []

    phoneNumberMnemonicsHelper(0, phoneNumber, currMnemonic, mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx, phoneNumber, currMnemonic, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currMnemonic, mnemonicsFound)

DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}
