"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        new = None
        while True:
            if list1 is None:
                if new is not None:
                    new.next = list2
                else:
                    result = list2
                break
            if list2 is None:
                if new is not None:
                    new.next = list1
                else:
                    result = list1
                break

            if list1.val <= list2.val:
                if new is None:
                    new = list1
                    result = new
                else:
                    new.next = list1
                    new = new.next
                list1 = list1.next
            else:
                if new is None:
                    new = list2
                    result = new
                else:
                    new.next = list2
                    new = new.next
                list2 = list2.next
        return result

    def mergeTwoLists2(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists2(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists2(list1, list2.next)
            return list2


if __name__ == '__main__':
    solution = Solution()

    l3 = ListNode(4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    m3 = ListNode(4)
    m2 = ListNode(3, m3)
    m1 = ListNode(1, m2)
    res = solution.mergeTwoLists(l1, m1)
    print(res)
