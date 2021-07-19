# https://www.acmicpc.net/problem/1010

import sys

def C(a, b):
    if b == 0 or a == b:
        return 1
    if dp[a][b] > -1:
        return dp[a][b]
    dp[a][b] = C(a - 1, b - 1) + C(a - 1, b)
    return dp[a][b]

t = int(sys.stdin.readline())
dp = [[-1 for _ in range(31)] for _ in range(31)]

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(C(m, n))
