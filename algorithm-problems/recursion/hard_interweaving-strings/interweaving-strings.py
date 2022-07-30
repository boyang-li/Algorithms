# Notes:
# We use recursion to solve this problem. In each recursion call, we loop at
# the letters at index i of string one and index j of string two, and then
# check whether they can form an interwoven string three if either letters is
# used at index k(k = i + j) of string three.
#
# The vanilla recursive solution would run in O(2^(m + n)) time and a a space
# complexity of O(n + m), but if we use a cache matrix, the complexity would be
# much better, because we would not need not to do the checks anymore.
#
# Complexity:
# O(n * m) time | O(n * m) space - where n, m are the lengths of string one and
# string two, respectively.
def areInterwoven(one, two, three, i, j, cache):
    # if we have cache the result, return it directly
    if cache[i][j] is not None:
        return cache[i][j]

    # we are at the kth index of string three, we are done if we have reached
    # the end of string three
    k = i + j
    if k == len(three):
        return True

    # if we have not finished traversing string one, and the letter at index i
    # of string one still matches the letter in string three at index k, cache
    # the result based on the result of the further recursive call on the next
    # letter in string one.
    if i < len(one) and one[i] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    # this is very similiar to the above loop except this time we are check the
    # letters in string two at index j
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = areInterwoven(one, two, three, i, j + 1, cache)
        if cache[i][j]:
            return True

    # If we have reached this line, it means the recursive calls have not return
    # True in either of the loops above
    cache[i][j] = False
    return False
