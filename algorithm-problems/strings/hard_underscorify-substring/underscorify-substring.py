# we break the algorithm into three functions:
# getLocations(), collapse(), and underscorify()
# this way, the code is much more easier to write and readable.
#
# Average case: O(n + m) | O(n) space - where n is the length
# of the main string and m is the length of the substring
def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)

# given the input string and the substring, find all the
# index pairs of the substring instances in the input string.
# i.e. locations = [[startIdx, endIdx], ...]
def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        # get the starting index of the first occurrence of the
        # substring, find() returns -1 if not found
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            # note that next start index is 1 index further,
            # because substrings can overlap each other
            startIdx = nextIdx + 1
        else: break
    return locations

# collapse detects if any pair of the substring intervals in the
# locations array are back-to-back or overlapping each other,
# merge them if found.
def collapse(locations):
    if not len(locations):
        return locations
    # create a new array for output
    newLocations = [locations[0]]
    # compare the two adjacent elements at a time
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        # check if the two locations are back-to-back or
        # overlapping each other.
        if current[0] <= previous[1]:
            # collapse a pair of locations by setting the prev's
            # end index to the current's end index.
            # note that prev is alreay in the output array, we are
            # merely modifying its value.
            previous[1] = current[1]
        else:
            # the locations are apart, and we just add the current
            # location to the output array.
            newLocations.append(current)
            previous = current
    return newLocations

# given the collapsed locations array, we can now safely wrap
# each of the elements with underscores.
def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    # we are in a position where we have added the opening
    # undercore, but still have not added the closing one.
    inBetweenUnderscores = False
    finalChars = []
    i = 0
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]:
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1
            i = 0 if i == 1 else 1
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)
