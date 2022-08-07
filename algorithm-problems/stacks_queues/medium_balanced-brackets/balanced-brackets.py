# O(n) time | O(n) space - where n is the length of the input string
def balancedBrackets(string):
    if len(string) == 0:
        return True

    stack = []
    for char in string:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            lastChar = stack.pop()
            if lastChar != '(':
                return False
        elif char == ']':
            if len(stack) == 0:
                return False
            lastChar = stack.pop()
            if lastChar != '[':
                return False
        elif char == '}':
            if len(stack) == 0:
                return False
            lastChar = stack.pop()
            if lastChar != '{':
                return False
    return True if len(stack) == 0 else False
