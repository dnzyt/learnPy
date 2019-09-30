class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for _ in range(n - 1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        count = 1
        res = ''
        for i in range(len(seq) - 1):
            if seq[i] == seq[i + 1]:
                count += 1
            else:
                res += (str(count) + seq[i])
                count = 1
        res += (str(count) + seq[-1])
        return res
