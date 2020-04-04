class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, le, ri, item, result):
        if le > ri:
            return
        if le == 0 and ri == 0:
            result.append(item)
        if le > 0:
            self.helper(le - 1, ri, item + '(', result)
        if ri > 0:
            self.helper(le, ri - 1, item + ')', result)

    def generateParenthesis2(self, n):
        if n == 1:
            return ['()']
        s = set()
        for res in self.generateParenthesis2(n - 1):
            for i in range(len(res) + 1):
                s.add(res[:i] + '()' + res[i:])
        return s
