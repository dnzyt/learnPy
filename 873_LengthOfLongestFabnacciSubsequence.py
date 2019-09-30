class Solution:
    def lenLongestFibSubseq(self, A):
        s = set(A)
        n = len(A)
        result = 0

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                count = 2
                while a + b in s:
                    count += 1
                    a, b = b, a + b
                    result = max(result, count)

        return result if result > 2 else 0
