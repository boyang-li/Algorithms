# O(n) time | O(n) space - where n is the length of the array
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for i in range(2 * len(array)):
        circularIdx = i % len(array)

        while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circularIdx]:
            top = stack.pop()
            result[top] = array[circularIdx]

        stack.append(circularIdx)

    return result
