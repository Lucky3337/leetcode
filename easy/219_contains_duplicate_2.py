class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            # Если число уже есть в окне размера k, возвращаем True
            if nums[i] in window:
                return True

            window.add(nums[i])

            # Если окно стало больше k, удаляем самый старый элемент
            if len(window) > k:
                window.remove(nums[i - k])

        return False


if __name__ == '__main__':
    # case 1. nums = [1, 2, 3, 1], k=3 TRUE
    # case 2. nums = [1, 0, 1, 1], k = 1 TRUE
    # case 3. nums = [1, 2, 3, 1, 2, 3], k = 2 FALSE
    # case 4. nums = [1, 0, 1, 1], k = 1 TRUE
    s = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))