def minNumberOfCoinsForChange(n, denoms):
    # initialize the array for coins array(+1 for zero change) with infinity
    numOfCoins = [float("inf") for amount in range(n + 1)]
    # set change for zero money 0
    numOfCoins[0] = 0

    # for each denom, we iterate through each amounts of change, whenever denom is less or
    # equal to that amount, we take the minimum between the num of changes for the amount
    # and the num of changes for the amount minus denom + 1.
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
