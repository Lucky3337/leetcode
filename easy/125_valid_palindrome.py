import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        match = re.findall(r"[a-z]|[0-9]", s)
        s = "".join(match)
        reversed_s = "".join(list(reversed(s)))
        return reversed_s == s


def example_two(solution):
    s = "0P"
    expected = False
    actual = solution.isPalindrome(s)
    assert actual == expected


def example_three(solution):
    s = "A man, a plan, a canal: Panama"
    expected = True
    actual = solution.isPalindrome(s)
    assert actual == expected


if __name__ == '__main__':
    solution = Solution()
    # example_two(solution)
    example_three(solution)