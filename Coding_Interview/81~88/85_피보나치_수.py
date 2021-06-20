#피보나치 수
#https://leetcode.com/problems/fibonacci-number

class Solution:
    dp = { 0 : 0, 1 : 1 }
    
    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        
        result = self.fib(n - 1) + self.fib(n - 2)
        self.dp[n] = result
        return result
