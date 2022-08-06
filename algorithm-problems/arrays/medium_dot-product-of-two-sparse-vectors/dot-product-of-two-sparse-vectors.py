# LeetCode 1570. Dot Product of Two Sparse Vectors

class SparseVector:
    # Approach 1. Dictionary/Hash Set
    #
    # Complexity:
    # O(m+n) time | O(n) space - where m is the length of the input array for
    # which Sparse Vector we are constructing, and n is the length of the
    # Sparse Vector we are calculating dot product with.
    def __init__(self, nums: List[int]):
        # store the two sparse vectors in a hash table:
        # key=index, value=nums[index]
        self.numsDict = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.numsDict[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for idx in self.numsDict.keys():
            if idx in vec.numsDict:
                result += self.numsDict[idx] * vec.numsDict[idx]

        return result

    # Approach 2. Index-Value Pairs
    #
    # Complexity:
    # O(m+n) time | O(n) space - where m is the length of the input array for
    # which Sparse Vector we are constructing, and n is the length of the
    # Sparse Vector we are calculating dot product with.
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
