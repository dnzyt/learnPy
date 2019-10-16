class Solution:
    def wordPattern(self, pattern, str):
        s = str.split(' ')
        if len(pattern) != len(s):
            return False

        p_map = {}
        s_map = {}

        for i in range(len(pattern)):
            if p_map.get(pattern[i], -1) != s_map.get(s[i], -1):
                return False
            p_map[pattern[i]] = i
            s_map[s[i]] = i
        return True
