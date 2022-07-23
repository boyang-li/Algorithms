# O(n) time | O (n) space - where n is the length of the input string
def reverseWordsInString(string):
    if len(string) < 1:
        return ""

    reversedArray = []
    start = 0
    end = 0
    while end <= len(string) - 1:
        if not isTimeToSlice(start, end, string):
            if end == len(string) - 1:
                reversedArray.insert(0, string[start:end + 1])
            end += 1
        else:
            reversedArray.insert(0, string[start:end])
            print(reversedArray)
            start = end
    return "".join(reversedArray)

def isTimeToSlice(start, end, string):
    spaceToWord = (string[start] == " " and string[end] != " ")
    wordToSpace = (string[start] != " " and string[end] == " ")
    return spaceToWord or wordToSpace
