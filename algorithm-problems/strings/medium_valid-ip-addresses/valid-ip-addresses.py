# O(1) time | O(1) space
def validIPAddresses(string):
    ipAddressesFound = []

    for i in range(1 , min(len(string), 4)):
        currentIPAddressParts = ["", "", "", ""]

        # place the first dot
        currentIPAddressParts[0] = string[:i]
        if not isValidPart(currentIPAddressParts[0]):
            continue

        # place the second dot
        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i:j]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            # place the third dot
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append(".".join(currentIPAddressParts))
    return ipAddressesFound

def isValidPart(string):
    stringAsInt = int(string) # removes leading 0s
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt)) # check for leading 0s
