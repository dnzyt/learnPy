class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, dummy.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return dummy.next
