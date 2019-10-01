class Solution:
    def lengthOfLastWord(self, s):
        res = 0
        local_count = 0
        for x in s:
            if x == ' ':
                local_count = 0
            else:
                local_count += 1
                res = local_count
        return res
