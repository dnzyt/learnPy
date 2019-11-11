class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lookup = dict()
        for x in s:
            if x not in lookup:
                lookup[x] = 1
            else:
                lookup[x] += 1
        for x in t:
            if x not in lookup:
                return x
            if lookup[x] == 0:
                return x
            else:
                lookup[x] -= 1
