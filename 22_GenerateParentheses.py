class Solution:
    def generateParenthesis(self, n):
        self.res = []
        self._gen(0, 0, n, '')
        return self.res

    def _gen(self, left, right, n, current):
        if left == n and right == n:
            self.res.append(current)
            return
        if left < n:
            self._gen(left + 1, right, n, current + "(")
        if left > right and right < n:
            self._gen(left, right + 1, n, current + ')')

    def generateParenthesis2(self, n):
        if n == 1:
            return ['()']
        s = set()
        for res in self.generateParenthesis2(n - 1):
            for i in range(len(res) + 1):
                s.add(res[:i] + '()' + res[i:])
        return s
