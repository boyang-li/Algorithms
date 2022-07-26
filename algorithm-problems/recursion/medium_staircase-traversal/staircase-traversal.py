# Optimal solution - the iterative approach with sliding window technique
# O(n) time | O(n) space - where n is the height of the staricase
def staircaseTraversal(height, maxSteps):
    currNumOfWays = 0
    waysToTop = [1]
    for currHeight in range(1, height + 1):
        startOfWindow = currHeight - maxSteps - 1
        endOfWindow = currHeight - 1
        if startOfWindow >= 0:
            currNumOfWays -= waysToTop[startOfWindow]

        currNumOfWays += waysToTop[endOfWindow]
        waysToTop.append(currNumOfWays)

    return waysToTop[height]
