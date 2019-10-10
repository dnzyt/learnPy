class Solution:
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        while p1 is not p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p2
