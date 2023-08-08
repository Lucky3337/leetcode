class Solution:

    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        max_len = len(s)
        total_sum = 0
        i = 0
        while i < max_len:
            rom_number_current = s[i]
            number_current = self.mapping[rom_number_current]
            number = number_current
            try:
                rom_number_next = s[i + 1]
                number_next = self.mapping[rom_number_next]
            except IndexError:
                pass
            else:
                if number_current < number_next:
                    number = number_next - number_current
                    i += 1
            total_sum += number
            i += 1
        return total_sum



if __name__ == '__main__':
    # Symbol       Value
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    """
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    
    """

    solution = Solution()

    # 1
    s = "LVIII"
    result = solution.romanToInt(s)
    print(result)