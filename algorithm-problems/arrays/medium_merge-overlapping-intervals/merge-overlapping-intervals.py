# Optimal solution
# note here we are assuming the input param 'intervals'contains
# at least one element.
#  
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

    if currIntervalEnd >= nextIntervalStart:
      currInterval[1] = max(currIntervalEnd, nextIntervalEnd)
    else:
      currInterval = nextInterval
      mergedIntervals.append(currInterval)

  return mergedIntervals