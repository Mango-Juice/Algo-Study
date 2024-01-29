import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1] * (1 << 4) for _ in range(12)] for _ in range(n)]

# 초기화
dp[0][0][0] = 0
for i in range(4):
    dp[0][1][1 << i] = arr[0][i]

# dp
for i in range(1, n):
    for j in range(12):
        for k in range(1 << 4):
            answer = 0
            
            if k & (1 << 0) and j > 0:
                tmp = max(dp[i - 1][j - 1][k], dp[i - 1][j - 1][k - (1 << 0)])
                answer = max(tmp + arr[i][0] if tmp >= 0 else answer, answer)
                
            if k & (1 << 1) and j > 0:
                tmp = max(dp[i - 1][j - 1][k], dp[i - 1][j - 1][k - (1 << 1)])
                answer = max(tmp + arr[i][1] if tmp >= 0 else answer, answer)
                
            if k & (1 << 2) and j > 0:
                tmp = max(dp[i - 1][j - 1][k], dp[i - 1][j - 1][k - (1 << 2)])
                answer = max(tmp + arr[i][2] if tmp >= 0 else answer, answer)
                
            if k & (1 << 3) and j > 0:
                tmp = dp[i - 1][j - 1][k - (1 << 3)]
                answer = max(tmp + arr[i][3] if tmp >= 0 else answer, answer)
            
            dp[i][j][k] = max(answer, dp[i - 1][j][k])


print(dp[n - 1][11][(1 << 4) - 1])
