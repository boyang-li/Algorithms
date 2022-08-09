# LeetCode 347. Top K Frequent Elements
from collections import heapq, Counter
import random
from typing import List

class Solution:
    # Approach 2: Quickselect (Hoare's selection algorithm)
    #
    # Notes:
    # The naive solution is to use a hash table to store the frequencies of the
    # numbers, and then construct a Min Heap data structure to store the numbers
    # by frequency. Then we simply pop (n - k) numbers from the heap, and the
    # rest of the heap is the top k frequent numbers.
    #
    # Complexity:
    # O(nlog(k)) time | O(n+k) - where n is the number of nums, and k is the
    # number of most frequent nums we are looking for. Note, k is bound by n,
    # so k <= n, and the time complexity is also bound by O(nlog(n)).
    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            key = nums[i]
            if key not in freq:
                freq[key] = 0
            freq[key] += 1

        pq = []
        for num, freq in freq.items():
            # print(num, freq)
            heapq.heappush(pq, (freq, num))

        result = []
        for item in heapq.nlargest(k, pq):
            result.append(item[1])
        # print(result)

        return result


    # Approach 2: Quickselect (Hoare's selection algorithm)
    #
    # Notes:
    # Quickselect is a textbook algorthm typically used to solve the problems
    # "find kth something": kth smallest, kth largest, kth most frequent, kth
    # less frequent, etc. Like quicksort, quickselect was developed by Tony Hoare,
    # and also known as Hoare's selection algorithm.
    #
    # We use Lomuto's partition scheme for simplicity of implementation, but
    # note that this scheme degrades to O(n^2) when the array is already in order.
    #
    # Complexity:
    # Average case: O(n) time | O(n) space
    # Worst case: O(n^2) time | O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the frequency table
        count = Counter(nums)
        # the list of unique numbers in nums
        unique = list(count.keys())

        def swap(array, i, j):
            array[i], array[j] = array[j], array[i]

        def partitionLomuto(lo, hi, pivot) -> int:
            pivotFreq = count[unique[pivot]]

            # 1. move pivot to the end
            swap(unique, pivot, hi)

            # 2. move all less frequent elements to the left
            storeIdx = lo
            for i in range(lo, hi):
                if count[unique[i]] < pivotFreq:
                    swap(unique, storeIdx, i)
                    storeIdx += 1

            # 3. move pivot to its final sorted position, note that pivot
            # is at the end
            swap(unique, hi, storeIdx)

            return storeIdx

        # kth largest -> n-k smallest
        def quickselect(lo, hi, kSmallest) -> None:
            # sorts a list within lo..hi until kth less frequent element
            # takes its place.
            # base case: the list contains only one element
            if lo == hi:
                return

            # select a random pivot index
            pivot = random.randint(lo, hi)

            # find the pivot position in a sorted list
            pivot = partitionLomuto(lo, hi, pivot)

            if pivot == kSmallest:
                return
            elif kSmallest < pivot:
                quickselect(lo, pivot - 1, kSmallest)
            else:
                quickselect(pivot + 1, hi, kSmallest)

        n = len(unique)

        quickselect(0, n - 1, n - k)
        return unique[n - k:]
