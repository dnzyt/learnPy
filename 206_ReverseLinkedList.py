class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            temp = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = temp
        return dummy.next

    def reverseList2(self, head):
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
