class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        lenofnodes = 0
        curr = head
        while curr:
            curr = curr.next
            lenofnodes += 1
        k = k % lenofnodes
        if k == 0:
            return head
        start, curr = head, head
        for _ in range(k):
            curr = curr.next

        while curr.next:
            start = start.next
            curr = curr.next
        curr.next = head
        head = start.next
        start.next = None
        return head
