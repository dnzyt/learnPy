class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix2(self, strs):
        res = ''
        i = 0
        while True:
            try:
                sets = set(w[i] for w in strs)
                if len(sets) == 1:
                    res += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                print(e)
                break
        return res

    def longestCommonPrefix3(self, strs):
        if not strs:
            return ''
        minStr = min(strs, key=len)
        left = 0
        right = len(minStr)

        while left < right:
            mid = (left + right) // 2
            if len(strs) == sum(minStr[:mid + 1] == w[:mid + 1] for w in strs):
                left = mid + 1
            else:
                right = mid
        return minStr[:left]
