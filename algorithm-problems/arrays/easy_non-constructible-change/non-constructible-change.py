# Notes:
# Notice that we can have coins with same values, but we CANNOT use a coin
# more than once.
#
# brute-force approach: going through the of the positive integers, and
# eventually hit the one that you cannot create with the given coins. This
# approach is very hard to do and is sub-optimal.
#
# Optimal approach: we sort the input array, and we can solve it in a single
# loop of the sorted array.
#
# assume that we have a set of coins(denoted by U), and the
# upper bound of changes we can make with U(denoted by C). Now, if we add an
# extra coin V to the set U, as long as the value of V is smaller that or
# equal to C + 1, then we can make all of the changes up until C + V.
#
# Realise the fact that if V > C + 1, we CANNOT make the change C + 1 with
# the coins of U plus coin V.
#
# Also, we take the advantage of the sorted array, so that the first V such that
# V > C + 1 gives the minimum non-constructible change, C + 1.
#
# Complexity:
# O(nlog(n)) time | O(1) space - where n is the length of the input array.
def nonConstructibleChange(coins):
    # ask if we can use the built-in sorting function
    coins.sort()

    # this would be C
    currChangeCreated = 0
    for coin in coins:
        # coin would be checking whether V > C + 1
        if coin > currChangeCreated + 1:
            return currChangeCreated + 1

        # update C
        currChangeCreated += coin

    # if we have not found a V such that V > C + 1 after the loop, the minimum
    # non-constructible change is C + 1
    return currChangeCreated + 1
