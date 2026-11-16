# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        list_values = []
        while head:
            list_values.append(head.val)
            head = head.next

        new_head = None
        prev = None
        for idx, val in enumerate(reversed(list_values)):
            if not new_head:
                new_head = ListNode(val)
                prev = new_head
            else:
                new_node = ListNode(val)
                prev.next = new_node
                prev = new_node

        return new_head




if __name__ == '__main__':
    data = [1, 2, 3]
    head = None
    prev = None
    for idx, val in enumerate(data):
        if not head:
            head = ListNode(val)
            prev = head
        else:
            new_node = ListNode(val)
            prev.next = new_node
            prev = new_node

    solution = Solution()
    res = solution.reverseList(head=head)

    while res:
        print(res.val)
        res = res.next