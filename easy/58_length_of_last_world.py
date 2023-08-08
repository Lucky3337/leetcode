class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_count = 0
        flag = 0
        for char in s[::-1]:
            if char != " ":
                max_count += 1
                flag = 1
            else:
                if flag and char == " ":
                    return max_count
        return max_count


def example_one(solution):
    s = "Hello World"
    expected = 5
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


def example_two(solution):
    s = "   fly me   to   the moon  "
    expected = 4
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


def example_tree(solution):
    s = "luffy is still joyboy"
    expected = 6
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


def example_four(solution):
    s = "a"
    expected = 1
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


def example_five(solution):
    s = "a "
    expected = 1
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


def example_six(solution):
    s = "Today is a nice day"
    expected = 3
    actual = solution.lengthOfLastWord(s)
    assert actual == expected


if __name__ == '__main__':
    solution = Solution()
    example_one(solution)
    example_two(solution)
    example_tree(solution)
    example_four(solution)
    example_five(solution)
    example_six(solution)