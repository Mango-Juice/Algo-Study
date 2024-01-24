import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
dp = [ float('inf') ] * n

# 1~3 처리
dp[0] = 1

if n >= 2:
    dp[1] = 1

if n >= 3:
    dp[2] = 1 if int(s[0:3]) <= 641 else 2

# 이후 DP
for i in range(3, n):
    if s[i] != '0':
        dp[i] = min(dp[i], dp[i - 1] + 1)
    
    if s[i-1] != '0':
        dp[i] = min(dp[i], dp[i - 2] + 1)
    
    if int(s[i-2:i+1]) <= 641 and s[i-2] != '0':
        dp[i] = min(dp[i], dp[i - 3] + 1)
    
print(dp[n - 1])