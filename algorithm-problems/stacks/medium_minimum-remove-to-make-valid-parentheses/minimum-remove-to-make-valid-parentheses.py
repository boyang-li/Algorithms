# LeetCode 1249. Minimum Remove to Make Valid Parentheses
#
# Notes:
# The problem can be solved in 2 passes of the string. In the first pass, we
# find the problematic indexes. In the second pass, we build the valid string
# without the values at the problematic indexes.
#
# Note it is very easy to make it O(n^2) to directly remove or insert elements
# from a list, so we will assemble a new array with appropriate letters to make
# sure it runs in O(n).
#
# Complexity:
# O(n) time | O(n) space - where n is the length of the string.
#
# My solution
def minRemoveToMakeValid(self, s: str) -> str:
    strLst = list(s)
    inPosition = [True for _ in strLst]
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                inPosition[i] = False
        else:
            # it is a lowercase letter in a-z, do nothing
            continue

    for item in stack:
        inPosition[item] = False

    for i in reversed(range(len(inPosition))):
        if not inPosition[i]:
            del strLst[i]

    return "".join(strLst)

# LeetCode solution
def minRemoveToMakeValid(self, s: str) -> str:
    # instead of using a list of size n to flag the problematic indexes, use a
    # set to store the problematic indexes.
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()": # it is english letter, do nothing
            continue
        elif c == "(": # add to stack if it is opening paren
            stack.append(i)
        elif not stack:
            # this is the case of ")", but the stack is empty, so this item
            # is problematic and needs to be removed.
            indexes_to_remove.add(i)
        else:
            # cancel the opening paren by popping an item from the stack.
            stack.pop()
    # the final indexes we need to remove is the indexes we have put in the set
    # unions the items left in the stack(the un-closed opening parens).
    indexes_to_remove = indexes_to_remove.union(set(stack))

    # instead of deleting elements from the array, build a new array by only
    # appending the appropriate letters.
    result_array = []
    for i, c in enumerate(s):
        # check whether an item is in a set is O(1)
        if i not in indexes_to_remove:
            result_array.append(c)
    return "".join(result_array)
