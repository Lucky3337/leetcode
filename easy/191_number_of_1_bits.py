class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = f"{n:032b}"
        res = 0
        for i in ones:
            if i == "1":
                res += int(i)
        return res


if __name__ == "__main__":
    solution = Solution()

    res = solution.hammingWeight(11)
    res