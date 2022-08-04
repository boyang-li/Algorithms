# Merge Overlapping Intervals(AKA LeetCode 56.Merge Intervals)
#
# Notes:
# For the optimal solution, we first sort the intervals by its starting index.
# From the first interval, we start iterating all the intervals and check
# whether the current interval is overlapping or is back-to-back to the next
# interval.
#
# We merge all the overlapping or connected intervals and add them to the ourput.
#
# We are assuming the input param 'intervals'contains least one element.
#
# Complexity:
# O(nlog(n)) time | O(n) space - where n is the number of intervals

def mergeOverlappingIntervals(intervals):
  # Sorted the intervals by starting value
  sortedIntervals = sorted(intervals, key=lambda x: x[0])

  mergedIntervals = []
  currInterval = sortedIntervals[0]
  mergedIntervals.append(currInterval)

  for nextInterval in sortedIntervals:
    _, currIntervalEnd = currInterval
    nextIntervalStart, nextIntervalEnd = nextInterval

    # compare the end index of the current interval with the start index of the
    # next interval.
    if currIntervalEnd >= nextIntervalStart:
      # This is when to merge, and it is done by updating the currInterval's
      # end value to be the larger end value of the two intervals. We do not
      # need to update the start value since the intervals are sorted.
      # Notice that in Python this would update the nested array--mergedIntervals
      # in place.
      currInterval[1] = max(currIntervalEnd, nextIntervalEnd)
    else:
      currInterval = nextInterval
      mergedIntervals.append(currInterval)

  return mergedIntervals

def main():
  array = [[1, 3], [2, 6], [8, 10], [15, 18]]
  print(mergeOverlappingIntervals(array))
  # note that updating the array value would also update the nested
  # array with the array in place, becasue the nested array uses pointer.
  someArray = [1, 3]
  some2DArray = [someArray]
  print(someArray)
  print(some2DArray)
  someArray[1] = 7
  print(someArray)
  print(some2DArray)

if __name__ == "__main__":
  main()
