# LeetCode 408. Valid Word Abbreviation
# O(n) time | O(1) space - where n is the length of the 'word' string.
def validWordAbbreviation(word: str, abbr: str) -> bool:
    i, j = 0, 0
    numString = ""

    while i < len(word) and j < len(abbr):
        print("i=", i, " j=", j, " word[i]=", word[i], " abbr[j]=", abbr[j])
        if isAlphabet(abbr[j]):
            if word[i] != abbr[j]:
                return False
            i += 1
        else: # a digit in the abbr string
            # check leading zero
            if numString == "" and abbr[j] == '0':
                return False

            numString += abbr[j]
            if j == len(abbr) - 1 or isAlphabet(abbr[j + 1]):
                i += int(numString)
                numString = ""

        j += 1

    return i == len(word) and j == len(abbr)

def isAlphabet(c):
    return (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122)

def main():
    print(validWordAbbreviation("internationalization", "i12iz4n"))

if __name__ == "__main__":
    main()
