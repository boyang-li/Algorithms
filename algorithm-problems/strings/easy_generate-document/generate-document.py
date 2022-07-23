# O(m + n) time | O(l) space - where n is the length of the characters string, and
# m is the the length of the document string; l is the number of unique characters in
# characters string.
def generateDocument(characters, document):
    chars = {}
    for char in characters:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in document:
        if char not in chars or chars[char] < 1:
            return False
        else:
            chars[char] -= 1

    return True
