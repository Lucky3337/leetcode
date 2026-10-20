class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

    # return int(f"{a:032b}"[::-1], 2)


if __name__ == "__main__":
    n = 4
    result = 0
    print((result << 1) | (n & 1))
    result = (result << 1) | (n & 1)  # (1) и (2)
    solution = Solution()
    res = solution.reverseBits(4)
