# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word
def groupAnagrams(words):
    sortedWords = []
    for i in range(len(words)):
        letterArray = [char for char in words[i]]
        letterArray.sort(key=lambda x : ord(x))
        sortedWords.append("".join(letterArray))

    resultDict = {}
    for idx, ele in enumerate(sortedWords):
        if ele in resultDict:
            resultDict[ele].append(idx)
        else:
            resultDict[ele] = [idx]

    result = []
    for idxGroup in resultDict.values():
        print(idxGroup)
        result.append([words[idx] for idx in idxGroup])
    return result

# Cleaner solution
# O(w * n * log(n)) time | O(wn) space
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())
