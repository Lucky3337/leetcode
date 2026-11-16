class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 0:
            return False

        while n > 1:
            if n % 2 == 1:
                return False
            n = n / 2
        return True





if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(0) == False)
    print(s.isPowerOfTwo(-16) == False)
    print(s.isPowerOfTwo(3) == False)
    print(s.isPowerOfTwo(16) == True)
    print(s.isPowerOfTwo(8) == True)
    print(s.isPowerOfTwo(64) == True)
    print(s.isPowerOfTwo(88) == False)