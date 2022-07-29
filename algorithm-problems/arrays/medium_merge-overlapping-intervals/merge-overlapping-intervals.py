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
      # we want to take the larger end index as the end index of the merged
      # interval
      currInterval[1] = max(currIntervalEnd, nextIntervalEnd)
    else:
      currInterval = nextInterval
      mergedIntervals.append(currInterval)

  return mergedIntervals
