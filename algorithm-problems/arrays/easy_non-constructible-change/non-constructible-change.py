# brute-force approach: loop through all of the positive intergers, and
# eventually you hit one that you cannot create.
#
# Clever approach: imagine we have a set of coins, denoted by U, and
# the value we can create by adding up these coins, denoted by C. Now,
# if we are to add an individual coin V to the set U, and V > C + 1
# then we cannot make C + 1 change. Otherwise, if V <= C + 1, we can
# make whatever values up until C + V.
#
# Note that we cannot use a coin more than once.
def nonConstructibleChange(coins):
    coins.sort()

    # this would be V
    currChangeCreated = 0
    for coin in coins:
        if coin > currChangeCreated + 1:
            return currChangeCreated + 1

        currChangeCreated += coin
    return currChangeCreated + 1
