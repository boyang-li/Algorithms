# Brute-force
# O(nˆ2) time | O(1) space - where n is the length of the input array
def firstDuplicateValue(array):
  minDupIdx = len(array)
  for i in range(len(array)):
    value = array[i]
    for j in range(i + 1, len(array)):
      valueToAssert = array[j]
      if value == valueToAssert:
        minDupIdx = min(minDupIdx, j)

  if min == len(array):
    return -1

  return array[minDupIdx]

# The optimal solution
# O(n) time | O(n) space - where n is the length of the input array
def firstDuplicateValue(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


# A clever optimal solution leverages the given constrainst that values are 
# between 1..n and the array is mutable. We can actually use them to map the
# indices of the array, alter the values when we first saw them, so that we
# know immediately if we have a duplicate when we see it the second time.
#
# O(n) time | O(1) space - where n is the length of the input array
def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1