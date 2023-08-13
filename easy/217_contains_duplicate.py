from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """."""
        map = {}
        for num in nums:
            exists = map.get(num)
            if exists:
                return True
            else:
                map[num] = 1
        return False


def example_three(solution):
    nums = [1, 2, 3, 1]
    expected = True
    actual = solution.containsDuplicate(nums)
    assert actual == expected



if __name__ == '__main__':
    solution = Solution()
    example_three(solution)