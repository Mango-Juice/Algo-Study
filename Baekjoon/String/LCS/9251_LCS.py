import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
la = len(a)
lb = len(b)

dp = [[0] * (lb + 1) for _ in range(la + 1)]

for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        if ai == bj:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[la][lb])