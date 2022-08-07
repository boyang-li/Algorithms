# O(nˆ2) time | O(n) space - where n is the length of the stack
def sortStack(stack):
    # check for edge case
    if len(stack) == 0:
        return stack

    # always pop the top element off until the stack is empty
    top = stack.pop()
    sortStack(stack)

    # now try to put the top item back in sorted order
    insertInSortedOrder(stack, top)

    return stack

def insertInSortedOrder(stack, value):
    # the case we can just push the value to the stack and it
    # would still be sorted
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return

    # the case we need to place the value deeper into the stack,
    # we start by pooping the stack until we find the appropriate place
    top = stack.pop()

    insertInSortedOrder(stack, value)

    # push the popped top value back to stack
    stack.append(top)
