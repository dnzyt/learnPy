class Solution:
    def numSquares(self, n):
        q = [(n, 0)]
        visited = [False for i in range(n + 1)]

        while q:
            curr = q.pop(0)
            num = curr[0]
            steps = curr[1]

            i = 1
            while True:
                a = num - i * i
                if a == 0:
                    return steps + 1
                if a < 0:
                    break
                if not visited[a]:
                    q.append((a, steps + 1))
                    visited[a] = True
