class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(len(prices)):
            profit = 0
            for j in range(i, len(prices)):
                profit = max(prices[j] - prices[i], profit)

            max_profit = max(profit, max_profit)

        return max_profit
