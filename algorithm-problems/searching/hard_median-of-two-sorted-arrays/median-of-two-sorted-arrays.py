# LeetCode 4. Median of Two Sorted Arrays
#
# Notes:
# The naive solution would be first merge the two arrays and then find the
# median in the sorted final array. But, this is not optimal.
#
# Complexity:
# O(m+n) time | O(m+n) space, where m and n are the length of nums1 and nums2.
# this is not optimal.
from typing import List

def findMedianSortedArraysNaive(nums1: List[int], nums2: List[int]) -> float:
    # merge the two arrays to get a new array
    i, j = 0, 0
    nums = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1

    while i < len(nums1):
        nums.append(nums1[i])
        i += 1
    while j < len(nums2):
        nums.append(nums2[j])
        j += 1

    # print(nums)
    isEven = True if len(nums) % 2 == 0 else False


    if isEven:
        mid2 = len(nums) // 2
        mid1 = mid2 - 1
        # print(mid1, ' ', mid2)
        return (nums[mid1] + nums[mid2]) / 2.0
    else:
        mid = len(nums) // 2
        # print(mid)
        return nums[mid]

# Notes:
# The optimal solution involves binary search, but we would need to do it with
# two arrays. We use the partition technique on both arrays to find the left
# half of the merged final array(as if they were merged), and use two sets of
# left and right poniters(for both arrays) to mark the partitions which would
# assemble the final left half.
#
# Complexity:
# O(log(min(m, n))) time | O(1) space, where m and n are the length of nums1
# and nums2.
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # we always start with the shorter array, A
    if len(B) < len(A):
        A, B = B, A

    # at start, the partition includes entire A
    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2 # A
        j = half - i - 2 # B, -2 for off-by-one index errors for both A and B

        # get the values to compare, here Aleft is the max value of the left
        # partition of A, Aright is the minimum value of the right partition of
        # A. Vise-versa for B.
        # Technically, these indices can be out of bounds, so we need to check.
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        # Aleft is to big, we need to reduce it
        # pointer
        elif Aleft > Bright:
            r = i - 1
        # Aleft is to small, we need to increase it
        else:
            l = i + 1
