from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        needle_list = list(needle)
        stack = []
        index = 0
        for char_index in len(haystack):
            stack.append(haystack[char_index])
            if len(stack) <= needle_len:
                for i, st in enumerate(stack):
                    if needle_list[i] != st:
                        stack = []
                        continue
                if len(stack) == needle_len:
                    return index - needle_len + 1
            index += 1
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        index = 0
        stack = []
        if len(haystack.split(needle)) == 1:
            return -1
        while True:
            stack.append(haystack[index])
            print(index)
            if len(stack) <= len(needle):
                for i, st in enumerate(stack):
                    if needle[i] != st:
                        index = index - len(stack) + 1
                        stack = []
                        break
                if stack == list(needle):
                    return index - len(needle) + 1

            index += 1


if __name__ == '__main__':
    solution = Solution()
    haystack = "mississippi"
    needle = "issip"
    res = solution.strStr2(haystack, needle)
    print(res)
