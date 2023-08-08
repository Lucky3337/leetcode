from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num == target:
                return index
            elif num > target:
                return index
        return len(nums)


def example_one(solution):
    nums = [1, 3, 5, 6]
    target = 5
    expected = 2
    actual = solution.searchInsert(nums, target)
    assert actual == expected


def example_two(solution):
    nums = [1, 3, 5, 6]
    target = 2
    expected = 1
    actual = solution.searchInsert(nums, target)
    assert actual == expected


def example_tree(solution):
    nums = [1,3,5,6]
    target = 7
    expected = 4
    actual = solution.searchInsert(nums, target)
    assert actual == expected


if __name__ == '__main__':
    solution = Solution()
    example_one(solution)
    example_two(solution)
    example_tree(solution)