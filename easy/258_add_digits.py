class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) <= 1:
            return num

        result = 10

        while result > 9:
            result = 0
            for digit in str(num):
                result += int(digit)
            num = result
        return result


if __name__ == "__main__":
    # 38 --> 3 + 8 --> 11
    # 11 --> 1 + 1 --> 2
    # OUTPUT 2
    s = Solution()
    print(s.addDigits(0))
    print(s.addDigits(38) == 2)
    print(s.addDigits(11) == 2)
