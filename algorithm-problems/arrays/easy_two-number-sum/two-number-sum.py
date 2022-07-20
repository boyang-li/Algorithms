# O(n) time | O(n) space - where n is the length of the input array
def twoNumberSum(array, targetSum):
    seen = {}
    twoSums = []
    for num in array:
        # calculate the difference between target sum and current number
        difference = targetSum - num
        # if we have seen the difference number before, it means we have found
        # a pair, and we append it to the output array; Otherwise, we mark the
        # number as seen by saving it as a key to the hash table with value True.
        if difference in seen:
            return [num, difference]
        else:
            seen[num] = True
    return twoSums
