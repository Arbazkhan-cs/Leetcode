class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price < buyPrice:
                buyPrice = current_price
                continue

            max_profit = max(max_profit, current_price - buyPrice)
        
        return max_profit
