class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        previous_value = nums[0]
        start = nums[0]
        result = []

        for i in nums[1:]:
            print(f'previous_value: {previous_value}, abs(i - previous_value): {abs(i - previous_value)}, start: {start}')
            print(i)
            if start == "":
                start = str(i)

            if abs(i - previous_value) != 1:
                if start == previous_value:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(previous_value))
                start = i
            previous_value = i

        if start != "":
            if start == previous_value:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(previous_value))
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,5,6,7]
    nums = [0,1,2,4,5,7]
    nums = [0,2,3,4,6,8,9]
    print(solution.summaryRanges(nums))

