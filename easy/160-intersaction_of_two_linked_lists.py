# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a  # либо узел пересечения, либо None


if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4]
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2.next = ListNode(3)
    b_root = ListNode(4)

    solution = Solution()
    var_t = solution.getIntersectionNode(node_1, b_root)
    print(var_t)

