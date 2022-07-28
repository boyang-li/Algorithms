# Notes:
# We can takle this problem by iterating the array once. We set two pointers,
# each at the beginning of the original array and the suquence array.
#
# We continue the loop as long as both pointers have not reach the end. We
# increment the original array index at each iteration, and increment the
# sequence array index when the value at the sequence index value is equal to
# the value in the original array at the iteration.
#
# At the end, we check whether we have finished looping through the sequence
# array, because if we have, it is a valid subsequence of the original array.
#
# Complexity:
# The algorithm consists a single loop of size n, and no auxiliary data
# structure.
# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0

    # So long as none of the indices are in bounds, iterate the original array
	while arrIdx < len(array) and seqIdx < len(sequence):
        # check whether there is a match between the array and the sequence
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1

    # Check whether we have finished iterating the sequence array
	return seqIdx == len(sequence)
