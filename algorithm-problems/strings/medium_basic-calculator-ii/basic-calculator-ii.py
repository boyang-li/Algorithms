# LeetCode 227. Basic Calculator II
#
# My solution
# O(n) time | O(1) space
def calculateInt(s: str) -> int:
    topOps = {"*", "/"}
    subOps = {"+", "-"}
    tuple = [None, None]
    currNumStr = ""
    opOne, opTwo = None, None

    for i in range(len(s)):
        print("curr=", s[i])

        # ASCII code for [0-9] is [48-57]
        # [A-Z] is [65-90], [a-z] is [97-122]
        if 48 <= ord(s[i]) <= 57:
            currNumStr += (s[i])

        isOperant = (s[i] in topOps or s[i] in subOps)
        isLastCharacter = (i == len(s) - 1)

        if isOperant or isLastCharacter:
            # cast the number string to integer
            currNum = int(currNumStr) if currNumStr else 0
            # clear the number string
            currNumStr = ""

            # the first number is explored, fill the first position with it
            # and update operant one
            if currNum != 0:
                if tuple[0] == None:
                    tuple[0] = currNum
                    if isOperant:
                        opOne = s[i]
                # the second number is discovered,  we check the operant
                elif tuple[1] == None: # second number is empty, we
                    if opOne in topOps:
                        # after we evaluate the operation, simply update the first position
                        # with the result.
                        tuple[0] = tuple[0] * currNum if opOne == "*" else tuple[0] // currNum
                        if isOperant:
                            opOne = s[i]
                    else:
                        # fill the sedond position and update operant two
                        tuple[1] = currNum
                        if isOperant:
                            opTwo = s[i]
                # the third number is explored. there can be two cases:
                # 1. last operant is a top-op, we evaluate it with the second and the third
                #    number, and update the second position with the result;
                # 2. last operant is a sub-op, we evaluate the prev-op with the first and the
                #    second number, and update the first position with the result, and finaly,
                #    update the second position with the third number.
                else:
                    if opTwo in topOps:
                        # after we evaluate the operation, simply update the second position
                        # with the result.
                        tuple[1] = tuple[1] * currNum if opTwo == "*" else tuple[1] // currNum

                    else:
                        # evaluate the prev-op with the first and the second number
                        tuple[0] = tuple[0] + tuple[1] if opOne == "+" else tuple[0] - tuple[1]
                        tuple[1] = currNum
                        opOne = opTwo

                    if isOperant:
                        opTwo = s[i]
                print(tuple, "opOne=", opOne, "opTwo=", opTwo)

    if tuple[0] is not None and tuple[1] is None:
        return tuple[0]
    elif tuple[0] is not None and tuple[1] is not None and opOne is not None:
        return tuple[0] + tuple[1] if opOne == "+" else tuple[0] - tuple[1]
    else:
        return 0

def calculate(s: str) -> int:
    if not s or len(s) == 0:
        return 0
    currentNum, lastNum, result = 0, 0, 0
    operation = '+'
    currNumStr = ""
    for i in range(len(s)):
        isDigit = (48 <= ord(s[i]) <= 57)
        print("s[i] = ", s[i], "ord(s[i]) = ", ord(s[i]), " isDigit = ", isDigit)

        if isDigit:
            currNumStr += (s[i])

        if not isDigit and s[i] != ' ' or i == len(s) - 1:
            currentNum = int(currNumStr)

            if operation == '+' or operation == '-':
                result += lastNum
                lastNum = currentNum if operation == '+' else currentNum * -1
            elif operation == '*':
                lastNum = lastNum * currentNum
            elif operation == '/':
                lastNum = int(lastNum / currentNum)

            print("s[i] = ", s[i], " result=", result, " lastNum = ", lastNum, " currentNum = ", currentNum, " operation = ", operation)

            operation = s[i]
            currentNum = 0
            currNumStr = ""

    result += lastNum
    return result

def main():
#   print(calculate("3+2*2*2   - 7 * 5"))

  print(calculate("14-3/2"))

if __name__ == "__main__":
  main()