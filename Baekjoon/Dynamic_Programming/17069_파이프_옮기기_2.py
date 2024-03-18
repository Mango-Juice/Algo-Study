import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if arr[i][j] == 1: continue
        if i == 0 and j == 1: continue
        can_rect = (i > 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0)
        
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2] if i > 0 else 0
        dp[i][j][2] = sum(dp[i - 1][j - 1]) if can_rect else 0

print(sum(dp[n - 1][n - 1]))