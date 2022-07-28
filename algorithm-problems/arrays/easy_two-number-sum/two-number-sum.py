# Notes:
# The brute-force approach to solve it would be having a double loop to go
# through every pair of numbers, and check if they sum up to targetSum.
#
# The optimal solution uses a single loop to iterate through the array, and
# uses a hash table to store the numbers we have seen.
#
# For each numbers, we calculat the difference between the number and the
# targetSum, and we check whether the difference is in the hash table. If it is
# in it, it means we have found a valid pair.
#
# Complexity:
# The solution consists of a single loop of size n and an auxiliary data
# structure of size n.
#
# O(n) time | O(n) space - where n is the length of the input array
def twoNumberSum(array, targetSum):
    # use a hash table to store the numbers seen
    seen = {}
    # the result array
    twoSums = []

    for num in array:
        # get the difference between the number and target sum
        difference = targetSum - num
        # if we have seen the difference number before, it means we have found
        # a pair, and we append it to the output array; Otherwise, we update
        # seen to True for the number in the hash table.
        if difference in seen:
            return [num, difference]
        else:
            seen[num] = True

    return twoSums
