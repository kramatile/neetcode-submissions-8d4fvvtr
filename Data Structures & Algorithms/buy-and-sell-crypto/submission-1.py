class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right  = left+1
        min_buy = float("inf") 
        max_sell = 0
        for i in range(len(prices)):
            if prices[i] >= min_buy:
                if prices[i] - min_buy > max_sell:
                    max_sell = prices[i] - min_buy
                continue
            min_buy = prices[i]
        return max_sell
