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

# The standard solution uses a hash table to store values we have seen.
# O(n) time | O(n) space - where n is the length of the input array.
def firstDuplicateValue(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


# Notes:
# A clever optimal solution leverages the given constrainst that values are
# between 1 and n, and the array is mutable. We can actually use it to map the
# indices of the array, and alter the values we have seen before, so that the
# mutated array serves just like a hash table.
#
# O(n) time | O(1) space - where n is the length of the input array.
def firstDuplicateValue(array):
    for value in array:
        # values are always positive since they are between 1 and n, we still
        # take the absolute value here.
        absValue = abs(value)
        # if we have seen it before, the array would be mutated such that the
        # index of (value - 1) is mapped.
        if array[absValue - 1] < 0:
            return absValue
        # mark the value as seen by flipping its sign to negative
        array[absValue - 1] *= -1

    return -1
