class Solution:
    def reverseWords(self, s):
        if s == '':
            return s
        ls = s.split()
        if ls == []:
            return ''

        res = ''
        for i in range(len(ls) - 1):
            res += ls[len(ls) - 1 - i] + ' '
        res += ls[0]
        return res
