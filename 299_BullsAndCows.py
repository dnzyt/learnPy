from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 先找到在guess中但是不在secret中的字符个数
        no_overlap = sum((Counter(guess) - Counter(secret)).values())
        bulls = sum(a == b for a, b in zip(secret, guess))
        # 最后从guess总长度里减去bulls的个数以及在guess中但不在secret中的字符个数
        cows = len(guess) - bulls - no_overlap

        return f'{bulls}A{cows}B'


