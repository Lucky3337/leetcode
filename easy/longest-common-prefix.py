from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        current_index = 0

        condition = True
        while condition:
            tmp = ""
            for string_value in strs:
                try:
                    char = string_value[current_index]
                except IndexError:
                    condition = False
                    tmp = ""
                    break
                if tmp == "":
                    tmp = char
                elif tmp != char:
                    condition = False
                    tmp = ""
                    break
            current_index += 1
            result += tmp
        return result





if __name__ == '__main__':
    s = Solution()

    # 1
    strs = ["flower", "flow", "flight"]
    # Output: "fl"

    # 2
    # strs = ["dog", "racecar", "car"]
    # Output: ""
    result = s.longestCommonPrefix(strs)
    print(result)
