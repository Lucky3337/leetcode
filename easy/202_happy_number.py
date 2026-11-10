class Solution:
    def isHappy(self, n: int) -> bool:
        unique_num = set()
        while True:
            summ_num = 0
            for i in str(n):
                summ_num += int(i)**2
            if summ_num == 1:
                return True
            elif summ_num in unique_num:
                return False
            else:
                unique_num.add(summ_num)
                n = summ_num

if __name__ == "__main__":
    solution = Solution()
    res = solution.isHappy(19)
    res

