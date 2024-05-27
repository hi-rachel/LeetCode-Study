class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        max = 0

        for price in prices:
            if price > start:
                max += price - start
            start = price

        return max