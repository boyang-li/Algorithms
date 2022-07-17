# O(n) time | O(n) space - where n is the number of the array
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True

    for num in array:
        # the num is marked False - 'not good to explore'
        if not nums[num]:
            continue
        currentLength = 1
        # explore to left
        left = num - 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        # explore to right
        right = num + 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        # check the new range
        if currentLength > longestLength:
            longestLength = currentLength
            # remeber to shift left and right indices
            # since they were shifted in the end of
            # the while loops for the last iteration.
            bestRange = [left + 1, right - 1]
    return bestRange
