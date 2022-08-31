# LeetCode 31. Next Permutation

# Notes:
# First, we observe that for any given sequence that is in descending order, no
# next larger permutation is possible. For example, no next permutation is
# possible for the following array: [9, 5, 4, 3, 1]
#
# We need to find the first pair of two successive numbers a[i] and a[i-1], from
# the right, which satisfy a[i] > a[i-1]. Now, no rearrangements to the right of
# a[i-1] can create a larger permutation since that subarray consists of numbers
# in descending order. Thus, we need to rearrange the numbers to the right of
# a[i−1] including itself.
#
# Now, what kind of rearrangement will produce the next larger number? We want
# to create the permutation just larger than the current one. Therefore, we need
# to replace the number a[i−1] with the number which is *just larger* than
# itself among the numbers lying to its right section, say a[j].
#
# Complexity:
# O(n) time | O(1) space - in the worst case, only two scans of the whole array
# are needed. No extra space is used. In place replacements are done.
from typing import List

def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]

    def reverseFrom(array, index):
        i, j = index, len(array) - 1
        while i < j:
            swap(array, i, j)
            i += 1
            j -= 1


    i = len(nums) - 2
    while (i >= 0 and nums[i+1] <= nums[i]):
        i -= 1
    if (i >= 0):
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)

    print(nums)
    print(i)
    reverseFrom(nums, i + 1)

    return nums
