from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        max_index = m + n - 1
        count_n = 0
        while count_n < n:
            index = max_index - count_n
            nums1[index] = nums2[count_n]
            count_n += 1

        
        # Loop from the second element of the nums1 until
        # the last element
        for i in range(1, len(nums1)):
            # This is the element we want to position in its
            # correct place
            key_item = nums1[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the nums1) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and nums1[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                nums1[j + 1] = nums1[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            nums1[j + 1] = key_item

        return nums1


def example_one(solution):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    solution.merge(
        nums1=nums1,
        m=m,
        nums2=nums2,
        n=n,
    )
    assert nums1 == expected


if __name__ == '__main__':
    solution = Solution()
    example_one(solution)