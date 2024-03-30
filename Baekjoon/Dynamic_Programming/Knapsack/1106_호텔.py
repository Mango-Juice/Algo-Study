import sys
input = sys.stdin.readline

MAX = 100001
c, n = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (MAX + 1)

for i in range(1, n + 1):
    for j in range(1, MAX + 1):
        w, v = arr[i - 1]
        if w <= j: dp[j] = max(dp[j], dp[j - w] + v)

for j in range(1, MAX + 1):
    if dp[j] >= c:
        print(j)
        exit()