# LeetCode 215. Kth Largest Element in an Array
#
# Notes:
# kth largest element is the same as (n - k)th smallest element. We can use
# the Quickselect algorithm to find the element in average O(n) time.
#
# Complexity:
# Average case: O(n) time | O(1) space
# Worst case: O(n^2) time | O(1) space
def findKthLargest(nums: List[int], k: int) -> int:
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def select(left, right, k_smallest):
        """
            Returns the k-th smallest element of list within left..right
        """
        if left == right:
            # If the list contains only one element, return that element
            return nums[left]

        # select a random pivot_index between
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]

        elif k_smallest < pivot_index: # go left
            return select(left, pivot_index - 1, k_smallest)
        else: # go right
            return select(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)

# Another approach
def findKthLargest(nums: List[int], k: int) -> int:
    def quickselectHelper(array, startIdx, endIdx, position):
        while True:
            if startIdx > endIdx:
                raise Exception("Invalid pointers")
            pivotIdx = startIdx
            leftIdx = startIdx + 1
            rightIdx = endIdx
            while leftIdx <= rightIdx:
                if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                    swap(array, leftIdx, rightIdx)
                if array[leftIdx] <= array[pivotIdx]:
                    leftIdx += 1
                if array[rightIdx] >= array[pivotIdx]:
                    rightIdx -= 1
            swap(array, rightIdx, pivotIdx)
            if rightIdx == position:
                return array[rightIdx]
            elif rightIdx < position:
                startIdx = rightIdx + 1
            else:
                endIdx = rightIdx - 1

    def swap(array, first, second):
        array[first], array[second] = array[second], array[first]

    # Assume there are 5 elements in the array, n = 5.
    # We want to find the kth largest number where k = 4.
    # Tt is the same thing as finding the (n - k + 1)th smallest number,
    # so (5 - 4 + 1) or 2nd smallest number. The position for the kth smallest
    # number is (n - k) or 1.
    position = len(nums) - k
    return quickselectHelper(nums, 0, len(nums) - 1, position)