#주식을 사고팔기 가장 좋은 시점
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer: int = 0
        low: int = 10000
        
        for price in prices:
            answer = max(price-low, answer)
            low = min(low, price)
        
        return answer
