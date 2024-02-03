import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
la = len(a)
lb = len(b)
lc = len(c)

dp = [[[0] * (lc + 1) for _ in range(lb + 1)] for _ in range(la + 1)]

for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        for k, ck in enumerate(c):
            if ai == bj == ck:
                dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
            else:
                dp[i + 1][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i + 1][j + 1][k], dp[i + 1][j][k + 1])

print(dp[la][lb][lc])