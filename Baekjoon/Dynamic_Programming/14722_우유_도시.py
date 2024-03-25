import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        dp[i][j] = max(
            dp[i-1][j] + (1 if dp[i-1][j] % 3 == arr[i][j] else 0),
            dp[i][j-1] + (1 if dp[i][j-1] % 3 == arr[i][j] else 0)
        )

print(dp[n-1][n-1])