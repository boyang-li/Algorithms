# LeetCode 1304. Find N Unique Integers Sum up to Zero
#
# Notes:
# Return an array where the values are symmetric. (+x , -x).
# If n is odd, append value 0 in your returned array.
#
# Complexity:
# The algorithm consists of a single loop of size n/2
# O(n) time | O(n) space - where n is the length of the result array
def sumZero(n: int) -> List[int]:
    m = n // 2

    result = [] if n % 2 == 0 else [0]

    for i in range(m):
        result.append(i + 1)
        result.append(-i - 1)

    return result
