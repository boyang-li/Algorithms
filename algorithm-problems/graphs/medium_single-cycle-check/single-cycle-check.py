# Notes:
# Realise the fact that we can tell whether the array forms a "single cycle" by
# the following conditions:
# 1. not returning to the starting index when the current number of traversed
#    elements is within 0 < n < len(array).
# 2. when the number of traversed elements is exactly len(array), we have
#    visited every single elements of the array, and we are back at the starting
#    index.
#
# Note that the value can be greater than the length of the array, we can get
# the appropriate position by using the mod operator. In addition, the values
# of jump can be negative, it simply indicates that we should go backwards.
#
# Complexity:
# O(n) time | O(1) space - where n is the length of the array.
def hasSingleCycle(array):
	numElementsVisited = 0
	currIdx = 0
	while numElementsVisited < len(array):
        # if 0 < n < len(array) and we are back to the starting index, it means
        # this array can't form a single cycle.
		if numElementsVisited > 0 and currIdx == 0:
			return False
		numElementsVisited += 1
		currIdx = getNextIdx(currIdx, array)
	return currIdx == 0

def getNextIdx(currIdx, array):
	jump = array[currIdx]
    # in case that the jump would extend out of bound, we wrap around the array.
	nextIdx = (currIdx + jump) % len(array)
    # check wheter the jump is positive, if not we will get the offset of the
    # backward jump.
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)
