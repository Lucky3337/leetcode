class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.convertToTitle(27))