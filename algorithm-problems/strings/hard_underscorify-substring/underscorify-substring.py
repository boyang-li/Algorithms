# Notes:
# This problem wants us to put underscores around target substrings in place,
# and if multiple target substrings that are 'back-to-back', or overlapping,
# we just put an underscore at each end of the chunk.
#
# A good approach which makes the code much more easier to implement, is to
# break the algorithm down to three sub-operations: 'getLocations', 'collapse',
# and 'underscorify'.
#
# Complexity:
# Average case: O(n + m) | O(n) space - where n is the length
# of the main string and m is the length of the substring.
def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)

# This function uses pointer to find matches of the target substring in the main
# string, and returns the indices of the start and end index pairs of the
# matches. i.e. locations = [[startIdx, endIdx], ...]
def getLocations(string, substring):
    locations = []
    # having a pointer to mark the beginning of the matching substring.
    startIdx = 0
    while startIdx < len(string):
        # get the starting index of the first occurrence of the target substring
        # from the startIdx in the main string, find() returns -1 if not found.
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            # found a match, append the index interval of the substring.
            locations.append([nextIdx, nextIdx + len(substring)])
            # note that next startIdx is the second index of the current
            # matching substring, because substrings can overlap.
            startIdx = nextIdx + 1
        else: break
    return locations

# This function traverse the intervals of the matching substring, and detects
# if any intervals are back-to-back or overlapping, merge them if found.
def collapse(locations):
    if not len(locations):
        return locations
    # create a new array for output with the first element in place.
    newLocations = [locations[0]]
    # compare every two adjacent elements at a time
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        # check whether the intervals are back-to-back or overlapping.
        if current[0] <= previous[1]:
            # collapse a pair of locations by setting the prev's
            # end index to the current's end index.
            # note that prev is alreay in the output array, we are
            # merely modifying its value.
            previous[1] = current[1]
        else:
            # the intervals are separate, add the current interval to the output
            newLocations.append(current)
            # update prev so the loop continues
            previous = current
    return newLocations

# This function actually put underscores around the target matches in place, and
# it is called after the 'collape' operation.
def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    # use a flag to indicate that we are in the position where we have already
    # put the opening undercore, but have not close it yet.
    inBetweenUnderscores = False
    # array of letters for the output string.
    finalChars = []
    i = 0
    # traverse the main string and the locations intervals at the same time,
    # and do stuff.
    while stringIdx < len(string) and locationsIdx < len(locations):
        # whenever we hit an index matching any interval extremities, we have
        # arrived a position to put an underscore.
        if stringIdx == locations[locationsIdx][i]:
            finalChars.append("_")
            # flip the flag for open/closed underscores.
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                # if we have closed an open underscore, it means we can go to
                # the next interval.
                locationsIdx += 1
            # i is the index for intervals, which could either be start(0) or
            # end(1) index.
            i = 0 if i == 1 else 1
        # add the character to the output
        finalChars.append(string[stringIdx])
        # increment the main string index
        stringIdx += 1
    # this is to address the situation when the last character of the main string
    # is part of the target substring, the closing underscore must be added.
    if locationsIdx < len(locations):
        finalChars.append("_")
    # If we have not finish traversing the main string, we need to add the rest
    # of the characters to the output.
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)
