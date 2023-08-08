from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 0
        max_len = len(nums)
        while True:
            if i >= max_len:
                break
            is_int = isinstance(nums[i], int)
            if not is_int:
                break
            if i != 0:
                if nums[i - 1] == nums[i]:
                    nums.pop(i)
                    nums.append("_")
                    i -= 1
                else:
                    k += 1
            i += 1
        return k


if __name__ == '__main__':
    solution = Solution()
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = [1,1,2]
    nums = [1,2]
    res = solution.removeDuplicates(nums1)
    print(nums1)
    print(res)