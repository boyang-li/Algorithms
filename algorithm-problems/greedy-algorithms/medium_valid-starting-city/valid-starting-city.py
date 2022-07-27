# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    numOfCities = len(distances)
    milesRemaining = 0

    idxOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1, numOfCities):
        distanceFromPrevCity = distances[cityIdx - 1]
        fuelFromPrevCity = fuel[cityIdx - 1]
        milesRemaining += fuelFromPrevCity * mpg - distanceFromPrevCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            idxOfStartingCityCandidate = cityIdx

    return idxOfStartingCityCandidate
