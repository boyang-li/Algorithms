# O(nlog(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=True)

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        if fastest:
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
        else:
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[len(blueShirtSpeeds) - 1 - i])
    return totalSpeed
