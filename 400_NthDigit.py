class Solution:
    def findNthDigit(self, n: int) -> int:
        lenofnum = 1
        cnt = 9
        start = 1
        while n > lenofnum * cnt:
            n -= lenofnum * cnt
            cnt *= 10
            lenofnum += 1
            start *= 10
        start += (n - 1) / lenofnum
        return int(str(start)[(n - 1) % lenofnum])
