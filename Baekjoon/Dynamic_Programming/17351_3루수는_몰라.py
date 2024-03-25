import sys
input = sys.stdin.readline

atoi = {"M": 1, "O": 2, "L": 3, "A": 4}
n = int(input())
arr = [list(input().strip()) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1 if arr[0][0] == "M" else 0

for i in range(n):
    for j in range(n):
        if i == j == 0: continue
        if i > 0:
            if arr[i][j] in atoi and arr[i-1][j] in atoi and atoi[arr[i][j]] - atoi[arr[i-1][j]] == 1:
                dp[i][j] = dp[i-1][j] + 1
            elif arr[i][j] == "M":
                dp[i][j] = 4 * (dp[i-1][j] // 4) + 1
            else:
                dp[i][j] = 4 * (dp[i-1][j] // 4)
        if j > 0:
            if arr[i][j] in atoi and arr[i][j-1] in atoi and atoi[arr[i][j]] - atoi[arr[i][j-1]] == 1:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + 1)
            elif arr[i][j] == "M":
                dp[i][j] = max(dp[i][j], 4 * (dp[i][j-1] // 4) + 1)
            else:
                dp[i][j] = max(dp[i][j], 4 * (dp[i][j-1] // 4))

print(dp[n-1][n-1] // 4)