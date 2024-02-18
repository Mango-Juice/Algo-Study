import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
a, d = map(int, input().split())

dp = [[[-1] * 2 for _ in range(n + 1)] for _ in range(n)]
answer = float('inf')

for i in range(n):
    for j in range(n + 1):
        # 헌혈 안함
        if i == 0 and j == 0: dp[i][j][False] = s[i]
        if i > 0 and dp[i - 1][j][False] > -1: dp[i][j][False] = dp[i - 1][j][False] + s[i]
        if i >= d and dp[i - d][j][True] > -1: dp[i][j][False] = max(dp[i][j][False], dp[i - d][j][True] + s[i])
            
        # 헌혈 함
        if j > 0:
            if i == 0 and j == 1: dp[i][j][True] = a
            if i > 0 and dp[i - 1][j - 1][False] > -1: dp[i][j][True] = dp[i - 1][j - 1][False] + a
            if i >= d and dp[i - d][j - 1][True] > -1: dp[i][j][True] = max(dp[i][j][True], dp[i - d][j - 1][True] + a)
        
        if dp[i][j][True] >= m or dp[i][j][False] >= m:
            answer = min(answer, j)

print(answer if answer != float('inf') else -1)
