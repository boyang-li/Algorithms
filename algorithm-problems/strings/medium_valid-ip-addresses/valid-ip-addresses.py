# Notes:
# For a given string of integers, we need to reurn an array of valid IP
# addresses. We solve this problem by iterating through the integers, and try
# to place dot at appropriate places so that an valid IP address can be formed.
#
# There are three dots we need to place, and there can be multiple combinations
# of the different places we can place the dots.
#
# We will create a helper function to check whether a portion of the potential
# IP address is valid. It should not have leading zeroes and it should between
# 0 and 255.
#
# Each portion of an IP address can have at most three digits, so we construct
# a triple nested loop with a 3-digit iteration in each layer of the inner loops,
# and save all the valid IP addresses out of all possible dot placements.
#
# Complexity:
# Realise the fact that the IP addresses can have at most 12 digits, so it runs
# in constant time and space.
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
    # removes leading 0s by casting string to integer
    stringAsInt = int(string)
    # there is no negative sign so only check it for upper bound
    if stringAsInt > 255:
        return False
    # if there is leading zero then it is invalid
    return len(string) == len(str(stringAsInt))
