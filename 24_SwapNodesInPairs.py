class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = first.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = first
        return dummy.next
