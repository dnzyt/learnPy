class Solution:
    def isValid(self, s):
        lookup = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for paren in s:
            if paren in lookup:
                stack.append(paren)
            elif len(stack) == 0 or lookup[stack.pop()] != paren:
                return False
        return len(stack) == 0
