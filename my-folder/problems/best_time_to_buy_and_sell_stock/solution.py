class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_buy = 0, float('inf') 
        for price in prices:
            min_buy = min(min_buy, price)
            profit = max(profit, price - min_buy)
        return profit