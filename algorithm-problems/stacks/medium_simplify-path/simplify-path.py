# LeetCode 71. Simplify Path
#
# Notes:
# The main idea of this algorithm is to use a stack. How you decide to process
# the input string is a personal choice.
#
# path = "/home/.././foo//bar/"
# array = path.split("/")
# ["home", "..", ".", "foo", "/bar"]
#
# Complexity:
# O(n) time | O(n) space - where n is the length of the input string.
def simplifyPath(self, path: str) -> str:
    array = path.split("/")
    print(array)
    stack = []
    for i in range(len(array)):
        if array[i] == '' or array[i] == '.':
            continue
        elif array[i] == '..':
            if stack:
                stack.pop()
        else:
            stack.append(array[i])

    result = "/"
    # if the path is just the root dir
    if len(stack) == 0:
        return result
    return result + "/".join(stack)

def main():
  simplifyPath("/home/.././foo//bar/")

if __name__ == "__main__":
  main()
