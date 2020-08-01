from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        mid = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        bot = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        res = []
        for word in words:
            w = word.lower()
            s = set(list(w))
            if s.issubset(top):
                res.append(word)
                continue
            elif s.issubset(mid):
                res.append(word)
                continue
            elif s.issubset(bot):
                res.append(word)
        return res
