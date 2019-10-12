class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        d_map = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [""]
        for d in digits:
            temp = []
            for ch in d_map[d]:
                for t in res:
                    temp.append(t + ch)
            res = temp
        return res
