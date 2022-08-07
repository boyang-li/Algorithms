# First solution
#
# O(n^2) time | O(1) space - where n is the length of the buildings array
def largestRectangleUnderSkyline(buildings):
    maxArea = 0
    for pillarIdx in range(len(buildings)):
        currHeight = buildings[pillarIdx]

        # set the furthest left point to the pillar index at the beginning,
        # and then try to extend to the leftmost index we can to form a rectangle.
        furthestLeft = pillarIdx
        while furthestLeft > 0 and buildings[furthestLeft - 1] >= currHeight:
            furthestLeft -= 1

        # set the furthest right point to the pillar index at the beginning,
        # and then try to extend to the rightmost index we can to form a rectangle.
        furthestRight = pillarIdx
        while furthestRight < len(buildings) - 1 and buildings[furthestRight + 1] >= currHeight:
            furthestRight += 1

        areaWithCurrBuilding = (furthestRight - furthestLeft + 1) * currHeight
        maxArea = max(areaWithCurrBuilding, maxArea)

    return maxArea

# Second solution
#
# O(n) time | O(n) space - where n is the length of the buildings array
def largestRectangleUnderSkyline(buildings):
    pillarIndices = []
    maxArea = 0

    for idx, height in enumerate(buildings + [0]):
        while len(pillarIndices) != 0 and buildings[pillarIndices[len(pillarIndices) - 1]] >= height:
            pillarHeight = buildings[pillarIndices.pop()]
            # here we are setting width to current index if our stack is empty,
            # otherwise, we take the difference between the current index and the
            # top index on the stack (which represents the furthest left bulding we
            # can use to form a rectangle)
            width = idx if len(pillarIndices) == 0 else idx - pillarIndices[len(pillarIndices) - 1] - 1
            maxArea = max(width * pillarHeight, maxArea)

        pillarIndices.append(idx)

    return maxArea
