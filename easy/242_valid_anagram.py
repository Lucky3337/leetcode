from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = list(t)
        s_list = list(s)
        if len(t_list) != len(s_list):
            return False
        for letter in s_list:
            try:
                t_list.remove(letter)
            except ValueError:
                return False
        if len(t_list) == 0:
            return True
        return False


def example_three(solution):
    s = "anagram"
    t = "nagaram"
    expected = True
    actual = solution.isAnagram(s, t)
    assert actual == expected


if __name__ == '__main__':
    solution = Solution()
    example_three(solution)