MOD = 10007
n = int(input())

dp = [[0] * 10 for _ in range(n)]
dp[0] = [1] * 10

for i in range(1, n):
    s = 0
    for j in range(10):
        s += dp[i - 1][j]
        dp[i][j] = s

print(sum(dp[n - 1]) % MOD)