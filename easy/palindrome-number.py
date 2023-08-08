"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        result_value = 0
        while n != 0:
            digit = n % 10
            result_value = result_value * 10 + digit
            n = int(n / 10)
        if x == result_value:
            return True
        else:
            return False




if __name__ == '__main__':
    s = Solution()
    x = 1221
    result = s.isPalindrome(x)
    print(result)