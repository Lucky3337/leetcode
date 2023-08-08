"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution:
    mapping = {
        "(": 0,
        ")": 0,
        "{": 0,
        "}": 0,
        "[": 0,
        "]": 0,
    }

    def isValid(self, s: str) -> bool:
        max_len = len(s)
        left = []
        right = []
        for i in range(max_len):
            current = s[i]
            if current in ("(", "[", "{"):
                left.append(current)
            else:
                right.append(current)

        for index, val in enumerate(left, start=1):
            right_index = len(right) - index
            if val != right[right_index]:
                return False
        return True

    def isValid2(self, s: str) -> bool:
        max_len = len(s)
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []
        for i in range(max_len):
            current = s[i]
            if not stack:
                if mapping.get(current) is None:
                    return False
                stack.insert(0, current)
            else:
                if mapping.get(current):
                    stack.insert(0, current)
                elif mapping[stack[0]] == current:
                    stack.pop(0)
                else:
                    return False
        if not stack:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s1 = "()[]{}"
    s3 = "()[]"
    s2 = "([)]"
    s4 = "(])"
    res = solution.isValid2(s1)
    print(res)
