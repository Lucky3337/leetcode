# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        exists_nums = {}
        for num in nums:
            if num in exists_nums:
                del exists_nums[num]
            else:
                exists_nums[num] = 1

        for num, num_count in exists_nums.items():
            if num_count == 1:
                return num
