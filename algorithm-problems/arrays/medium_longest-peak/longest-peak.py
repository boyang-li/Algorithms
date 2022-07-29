# Notes:
# We can solve this problem by iterating the array once. First, we locate a
# valid peak of minimum length which is three. Then we try to extend to both
# left and right to get the actual length of the peak. We keep track of the
# longest peak as we loop through the array.
#
# Complexity:
# Realise the fact that we are not going to repeatedly visit the same elements
# in the nested loop which extend the peaks, because the part of a peak is not
# going to be a part of another peak.
# O(n) time | O(1) space - where n is the length of the input array
def longestPeak(array):
  longestPeakLen = 0
  i = 1
  while i < len(array) - 1:
    # a peak is made of values strictly increasing and then strictly decreasing
    # inmediately after the tip.
    isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
    if not isPeak:
      i += 1
      continue

    # we have found the tip, now start to extend in both directions to find
    # how long it is
    leftIdx = i - 2
    while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
      leftIdx -= 1
    rightIdx = i + 2
    while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
      rightIdx += 1

    # recall that the left and right indices are further extended by 1 up front
    # such that left and right are first set to (i - 2) and (i + 2), so when we
    # calculate the actual length of the peak, we need to offset the difference
    # between left and right by -2. Because we calculate the length by two
    # indices such that (right - left + 1), we simply calculate the offseted
    # length by (right - left - 1).
    currPeakLen = rightIdx - leftIdx -1
    longestPeakLen = max(currPeakLen, longestPeakLen)

    # note this is important that we continue the loop from the right pointer
    # because it is the next available element to traverse that is not a part of
    # the last peak.
    i = rightIdx

  return longestPeakLen
