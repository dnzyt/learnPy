from typing import List

class Solution:
    # Bottom up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

    # BFS, 寻找0, amount的最短路径
    def coinChange2(self, coins: List[int], amount: int) -> int:
        q = [0]
        visited = [False] * (amount + 1)
        visited[0] = True
        res = 0

        while q:
            res += 1
            temp = []
            for curr in q:
                for coin in coins:
                    newDistance = curr + coin
                    if newDistance == amount:
                        return res
                    if newDistance > amount:
                        continue
                    if not visited[newDistance]:
                        visited[newDistance] = True
                        temp.append(newDistance)
            q, temp = temp, []
        return -1
        
            

