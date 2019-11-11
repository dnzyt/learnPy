class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        indexOfS = 0
        indexOfT = 0
        while indexOfS < len(s) and indexOfT < len(t):
            if s[indexOfS] == t[indexOfT]:
                indexOfS += 1
            indexOfT += 1
        return indexOfS == len(s)
