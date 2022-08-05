# LeetCode 560. Subarray Sum Equals K
#
# Notes:
# The solution to this problem is very similar to the Two Sum problem. We
# iterate through the array to calculate the cumulative sum at each element,
# and use a hash table to quickly check whether we have found a new subarray
# that sum to k.
#
# Note that the full array itself is a subarray of itself. An empty array is a
# subarray of any array.
#
# Complexity:
# O(n) time | O(n) space
def subarraySum(nums: List[int], k: int) -> int:
    # cnt--the counter for the output;
    # sum--cumulative sum up until the ith number.
    cnt, sum = 0, 0

    # use a hash table to store counts for sum as the key
    map = {0: 1}
    for i in range(len(nums)):
        # calculate the cumulative sum
        sum += nums[i]
        # this is ver similiar to the solution to the 'Two Sum' problem--if
        # the key of (sum - k) was added to the hash table, we have just
        # found a subarray that sums to k by exploring the current element.
        if (sum - k) in map:
            # update the counter
            cnt += map[sum - k]
        # always add the new sum to the hash table
        map[sum] = map.get(sum, 0) + 1
    return cnt
