# Notes:
# Anagrams are string made up of exactly the same letters, where order doesn't
# matter. In this problem, we are given an array of words, and we need to return
# a 2-d array which sort the words into groups of anagram for the same set of
# letters.
#
# We first sort each words by the ASCII code for letters, so that the anagrams
# for the same words become identical. Next, we use a hash table to store the
# sorted words, and anagrams's index would be appended to the same key as groups.
# Finaly, we iterate through the hash table values, and construct the 2-d array.
#
# Complexity:
# Sorting would run in O(nlog(n)), and we run sorting for each of the input
# words. Iterating the sorted words runs in O(n) time, and iterating the
# hash table for anagram groups run in O(n) at its worst scenario. Both of them
# can be canceled in big-O notaion.
#
# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word.
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
