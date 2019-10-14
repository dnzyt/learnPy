class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        temp = self.reverse(slow.next)
        slow.next = None
        while temp:
            if temp.val != head.val:
                return False
            temp = temp.next
            head = head.next
        return True

    def reverse(self, head):
        dummy = ListNode(0)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next
