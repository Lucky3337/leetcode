class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


class SolutionTwo:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Создаем фиктивный узел, указывающий на head
        dummy = ListNode(next=head)
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                # Пропускаем узел с целевым значением
                curr.next = curr.next.next
            else:
                # Двигаемся дальше, только если следующий узел валиден
                curr = curr.next

        return dummy.next


if __name__ == '__main__':
    data = [7, 7, 7]
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
    solution_two = SolutionTwo()
    res = solution_two.removeElements(head=head, val=7)

    while res:
        print(res.val)
        res = res.next