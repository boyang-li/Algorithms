# We can take the advantage of the fact that the array is sorted.
#
# The trick is that there could be negative integers. So if we simply return the
# squared array, it could be out of order.
#
# We takle the problem by having two pointers, set up at the two extremeties
# of the array, and loop the array backwards.
#
# As iterating the array, we compare the absolute value of the elements at the
# two pointers. Since the array is sorted, this comparision effectively gives
# us the largest and smallest squared value of the array, and we can put the
# larger squared value in sorted position of the output array as we go.
#
# Complexity:
# The algorithm consists of a single loop of size n, and an auxiliary data
# structure of size n for the output.
# O(n) time | O(n) space - where n is the length of the array
def sortedSquaredArray(array):
	sortedSquares = [0 for _ in array]
	smallerValueIdx = 0
	largerValueIdx = len(array) - 1

	for idx in reversed(range(len(array))):
		smallerValue = array[smallerValueIdx]
		largerValue = array[largerValueIdx]

		if abs(smallerValue) > abs(largerValue):
			sortedSquares[idx] = smallerValue ** 2
			smallerValueIdx += 1
		else:
			sortedSquares[idx] = largerValue ** 2
			largerValueIdx -= 1

	return sortedSquares
