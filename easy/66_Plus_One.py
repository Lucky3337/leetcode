from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_digits = len(digits)
        temp = 0
        for index, num in enumerate(digits[::-1]):
            current_space = len_digits - index - 1
            if num == 9 + temp:
                digits[current_space] = 0
                temp = 1
            else:
                new_num = num + temp
                if new_num <= 9:
                    if temp == 0:
                        new_num += 1
                    digits[current_space] = new_num
                    return digits
                else:
                    digits[current_space] = 0
                    temp = 1
        digits.insert(0, 1)
        return digits


def example_one(solution):
    digits = [1,2,3]
    expected = [1,2,4]
    actual = solution.plusOne(digits)
    assert actual == expected


def example_two(solution):
    digits = [9]
    expected = [1,0]
    actual = solution.plusOne(digits)
    assert actual == expected


def example_tree(solution):
    digits = [9,9]
    expected = [1,0,0]
    actual = solution.plusOne(digits)
    assert actual == expected


def example_four(solution):
    digits = [8, 9, 9, 9]
    expected = [9, 0, 0, 0]
    actual = solution.plusOne(digits)
    assert actual == expected


def example_five(solution):
    digits = [1,2,3]
    expected = [1,2,4]
    actual = solution.plusOne(digits)
    assert actual == expected

if __name__ == '__main__':
    solution = Solution()
    example_one(solution)
    example_two(solution)
    example_tree(solution)
    example_five(solution)