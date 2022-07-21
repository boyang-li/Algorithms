# O(n) time | O(n) space - where n is the length of the buildings array
def sunsetViews(buildings, direction):
    if len(buildings) < 1:
        return []
    if direction == "EAST":
        currTallestHeight = buildings[len(buildings) - 1]
        results = [len(buildings) - 1]
        for i in reversed(range(len(buildings))):
            buildingHeight = buildings.pop()
            if buildingHeight > currTallestHeight:
                results.insert(0, i)
                currTallestHeight = buildingHeight
    else:
        currTallestHeight = buildings[0]
        results = [0]
        for i in range(len(buildings)):
            buildingHeight = buildings.pop(0)
            if buildingHeight > currTallestHeight:
                results.append(i)
                currTallestHeight = buildingHeight

    return results
