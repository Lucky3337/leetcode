class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        quantity_data = {}
        for i in nums:
            quantity_data[i] = quantity_data.get(i, 0) + 1

        return max(quantity_data, key=quantity_data.get)