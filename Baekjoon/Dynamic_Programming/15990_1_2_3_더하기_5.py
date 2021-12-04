# https://www.acmicpc.net/problem/15990

import sys
input = sys.stdin.readline

# 미리 계산
MAX = 100001
MOD = 1000000009
dp = [[0] * 4 for _ in range(MAX)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, MAX):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

# 입출력
t = int(input())

for _ in range(t):
    print(sum(dp[int(input())]) % MOD)
