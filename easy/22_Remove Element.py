from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        max_len = len(nums)
        while True:
            if i >= max_len:
                break
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                i -= 1
                k -= 1
            else:
                k += 1
            i += 1
        return k


if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(result)
    print(nums)