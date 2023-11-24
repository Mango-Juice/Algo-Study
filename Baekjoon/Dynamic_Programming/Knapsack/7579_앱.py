# https://www.acmicpc.net/problem/7579
# 냅색 응용

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

dp = [[0 for _ in range(10001)] for _ in range(n + 1)]
answer = 10001

for i in range(1, n + 1):
    for j in range(answer):
        if c[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i - 1]] + a[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
            
        if dp[i][j] >= m:
            answer = min(answer, j)
            break

print(answer)
