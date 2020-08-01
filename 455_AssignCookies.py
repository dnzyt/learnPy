from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        i, j = len(g) - 1, len(s) - 1
        while min(i, j) >= 0:
            if g[i] <= s[j]:
                cnt += 1
                j -= 1
            i -= 1
        return cnt
