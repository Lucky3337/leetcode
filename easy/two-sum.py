from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_dict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in previous_dict:
                return [previous_dict[diff], index]
            previous_dict[number] = index


if __name__ == '__main__':
    s = Solution()
    # 1
    nums = [3, 2, 4]
    target = 6

    # 2
    nums = [3, 2, 3]
    target = 6
    result = s.twoSum(nums, target)
    print(result)