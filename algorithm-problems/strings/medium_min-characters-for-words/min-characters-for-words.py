# O(n * l) time | O(c) space - where n is the number of words,
# l is the length of the longest word, and c is the number of
# unique characters across all words.
def minimumCharactersForWords(words):
    maxCharFreqs = {}

    for word in words:
        charFreqs = countCharFreqs(word)
        updateMaxFreqs(charFreqs, maxCharFreqs)

    return makeArrayFromCharFreqs(maxCharFreqs)

def countCharFreqs(string):
    charFreqs = {}
    for char in string:
        if char not in charFreqs:
            charFreqs[char] = 0

        charFreqs[char] += 1

    return charFreqs

def updateMaxFreqs(freqs, maxFreqs):
    for char in freqs:
        freq = freqs[char]

        if char in maxFreqs:
            maxFreqs[char] = max(freq, maxFreqs[char])
        else:
            maxFreqs[char] = freq

def makeArrayFromCharFreqs(freqs):
    result = []

    for char in freqs:
        freq = freqs[char]

        for _ in range(freq):
            result.append(char)

    return result