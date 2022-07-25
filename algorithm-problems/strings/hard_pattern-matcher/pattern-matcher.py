# O(nˆ2+m) time | O(n+m) space- where n is the length of the main string,
# and m is the length of the pattern
def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts)

    if counts["y"] != 0: # case when there are both x's and y's
        # core logic: we try difference lengths of x, then we calculate
        # lenngth of y based on the length of x and numbers of x and y
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]

            # determine if the length of Y is valid
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue

            lenOfY = int(lenOfY)
            # we get the beginning index of the first y-substring in the string
            yIdx = firstYPos * lenOfX
            # we extract the x-substring in the string
            x = string[:lenOfX]
            # we extract the y-substring in the string
            y = string[yIdx : yIdx + lenOfY]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else: # case when it is only consist of x's
        lenOfX = len(string) / counts["x"]
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch):
                return [x, ""] if not didSwitch else ["", x]
    return []

# transform the pattern string into an array of letters in
# such way that character "x" always appear first. BY doing
# this transformation, it makes the algorithm easier to implement.
def getNewPattern(pattern):
    # turn pattern string in to a character array
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        # swap x and y for each letters in the array
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))

# counts the number of x's and y's, then returns the index
# of the first occurrence of y
def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos
