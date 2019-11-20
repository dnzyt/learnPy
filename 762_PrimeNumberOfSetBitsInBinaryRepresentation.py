class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        s = set([2, 3, 5, 7, 11, 13, 17, 19])
        ans = 0
        for i in range(L, R + 1):
            if bin(i).count("1") in s:
                ans += 1
        return ans
