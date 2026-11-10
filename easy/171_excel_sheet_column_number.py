class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result


if __name__ == '__main__':
    # print(ord('Z') - ord('A') + 1)
    # print(ord('Z')-64)
    # print(""[1:])

    solution = Solution()
    print(solution.titleToNumber("AB"))
