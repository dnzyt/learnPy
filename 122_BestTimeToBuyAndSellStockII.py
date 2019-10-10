class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        total = 0
        for i in range(1, len(prices)):
            total += prices[i] - prices[i - 1]
        return total
