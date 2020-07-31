from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[int]]:
        res = {}
        if len(strs) < 1:
            return strs
        else:
            for s in strs:
                ssorted = ''.join(sorted(s))
                if ssorted in res:
                    res[ssorted].append(s)
                else:
                    res[ssorted] = [s]
        return res.values()
