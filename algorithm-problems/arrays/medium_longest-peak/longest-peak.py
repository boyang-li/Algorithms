# O(n) time | O(1) space - where n is the length of the input array
def longestPeak(array):
  longestPeakLen = 0
  i = 1
  while i < len(array) - 1:
    # note it is 'strictly' increasing/decreasing
    isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
    if not isPeak:
      i += 1
      continue

    # we are at the peak, so extend to the left and right to find
    # how long it is
    leftIdx = i - 2
    while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
      leftIdx -= 1
    rightIdx = i + 2
    while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
      rightIdx += 1

    # remember to minus 1 since left and right indices are first extended by 1
    # instead of calculate the diff of indices and + 1, we further - 1.
    currPeakLen = rightIdx - leftIdx -1
    longestPeakLen= max(currPeakLen, longestPeakLen)
    i = rightIdx
  return longestPeakLen