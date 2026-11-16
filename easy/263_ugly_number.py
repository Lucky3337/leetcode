class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in (2, 3, 5):
            while n % factor == 0:
                n /= factor

        return n == 1



if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6) == True)
    print(6 // 2)
    # n = 6 -> 2 * 3 | True
    # n = 1 True
    # n = 14 False -> 2 * 7
    # 2,3,5