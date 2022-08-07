# O(n) time | O(n) space - where n is the length of the input string
def shortenPath(path):
    isAbsolutePath = path[0] == "/"
    # combine the split and filter in one line
    tokens = filter(isImportantToken, path.split("/"))
    stack = []
    if isAbsolutePath:
        stack.append("")
    for token in tokens:
        if token == "..":
            # whenever we see a "..", check edge cases to see whether
            # it is meaningful.
            #
            # case 1: the first token is "..", it is meaningful because
            # it is a relative path.
            #
            # case 2: we have back-to-back "..", and it also means
            # a relative path.
            #
            # If a ".." is meaningful, we don't ignore it, instead we
            # push it to the stack.
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                # here ".." is not meaningful, we "go back" to prev dir
                # by removing the top element in the stack
                stack.pop()
        else:
            stack.append(token)
    # if the path is just the root dir
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)

def isImportantToken(token):
    return len(token) > 0 and token != "."
