import sys
input = sys.stdin.readline

MOD = 1000000007
dp = {}

def fib(n):
    if n in dp: return dp[n]
    
    if n % 2 == 0:
        dp[n] = ((2 * fib(n // 2 - 1) + fib(n // 2)) % MOD) * fib(n // 2) % MOD
    else:
        dp[n] = ((fib(n // 2 + 1) ** 2 % MOD) + (fib(n // 2) ** 2 % MOD)) % MOD
    return dp[n]

dp[0] = 0
dp[1] = 1
print(fib(int(input())))