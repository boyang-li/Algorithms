# LeetCode 50. Pow(x, n)
# Complexity:
# O(log(n)) time | O(1) space
def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = n * -1

    ans = 1.0
    curProd = x
    print("n=", n, " n % 2=", n % 2, " curProd=", curProd, " ans=", ans)
    while n > 0:
        # if n is odd, we calculate ans = x^i * x^(i-1)
        if n % 2 == 1:
            ans = ans * curProd
        # if n is even, we calculate (x^i)^2 = x^i * x^i = x^2i
        curProd *= curProd
        n = n // 2
        print("n=", n, " n % 2=", n % 2, " curProd=", curProd, " ans=", ans)
    return ans

def main():
    # print(myPow(2, 7))
    print(myPow(2, 8))

if __name__ == "__main__":
    main()