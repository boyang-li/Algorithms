# O(nlog(n)) time | O(1) space - where n is the number of queries
def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        # the raionale for this formula is that for
        # every quiers left, it has to wait the current
        # duration of time to get executed, so we simply
        # add them up.
        totalWaitingTime += duration * queriesLeft

    return totalWaitingTime
