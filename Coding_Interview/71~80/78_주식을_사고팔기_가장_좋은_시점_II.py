#주식을 사고팔기 가장 좋은 시점 II
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum( max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1) )
