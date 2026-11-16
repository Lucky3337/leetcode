class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Если буква из s уже встречалась, проверяем, совпадает ли пара
            if char_s in s_map:
                if s_map[char_s] != char_t:
                    return False
            # Если буква из s новая, но буква из t уже занята другой буквой
            elif char_t in t_map:
                return False

            # Если всё ок, фиксируем связь в обе стороны
            s_map[char_s] = char_t
            t_map[char_t] = char_s

        return True



if __name__ == '__main__':
    # case 1. s = 'egg', t = 'add' TRUE
    # case 2. s = 'paper', t = 'title' TRUE
    # case 3. s = 'foo', t = 'bar' FALSE

    s = Solution()
    print(s.isIsomorphic('paper', 'title'))