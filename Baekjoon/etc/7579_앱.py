# https://www.acmicpc.net/problem/7579
# 냅색 응용

import sys

N, M = map(int, sys.stdin.readline().split())
An = [0] + list(map(int, sys.stdin.readline().split()))
Cn = [0] + list(map(int, sys.stdin.readline().split()))
hap, answer = sum(Cn), float('inf')
dp = [[0 for _ in range(hap + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, hap + 1):
        if j >= Cn[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - Cn[i]] + An[i])
            if dp[i][j] >= M:
                answer = min(answer, j)
                break
        else:
            dp[i][j] = dp[i - 1][j]

print(answer)
