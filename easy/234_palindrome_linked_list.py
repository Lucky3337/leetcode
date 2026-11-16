# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return True

        values = []
        while head:
            values.append(head.val)
            head = head.next

        right_side = len(values) - 1
        for index, val in enumerate(values):
            if right_side - index > right_side / 2:
                if val != values[right_side - index]:
                    return False
            else:
                break
        return True


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(1)))
    solution = Solution()
    print(solution.isPalindrome(head) == True)