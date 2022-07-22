# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
    result = ""
    if len(string) < 1:
        return result
    elif len(string) == 1:
        return "1" + string[0]

    consecCounter = 1
    char = string[0]
    for i in range(1, len(string)):
        char = string[i]
        if char == string[i - 1] and consecCounter < 9:
            consecCounter += 1
        else:
            result = result + str(consecCounter) + string[i - 1]
            consecCounter = 1
    if consecCounter > 0:
        result = result + str(consecCounter) + char
    return result
