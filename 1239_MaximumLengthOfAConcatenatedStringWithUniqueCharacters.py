class Solution:
    def maxLength(self, arr):
        masks = []
        for s in arr:
            m = 0
            for c in s:
                m |= 1 << (ord(c) - ord('a'))
            if bin(m).count('1') == len(s):
                masks.append(m)
        ans = 0

        def dfs(i, mask):
            nonlocal ans
            ans = max(ans, bin(mask).count('1'))
            for j in range(i, len(masks)):
                if masks[j] & mask == 0:
                    dfs(j + 1, mask | masks[j])
        dfs(0, 0)
        return ans
