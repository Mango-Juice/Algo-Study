import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
n, k = map(int, input().split())
levels = [tuple(map(int, input().split())) for _ in range(n)]

#####
dp = [[0] * 3001 for _ in range(n)]

for i in range(n):
    # i번째 문제까지의 경우의 수 계산
    for j in range(levels[i][0], levels[i][1] + 1):
        if i == 0: # 첫 문제 경우의 수는 1
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][min(j + k, 3000)]
            if j - k - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - k - 1]
        
        dp[i][j] %= MOD
        
    # 누적합 계산
    for j in range(1, 3001):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= MOD

print(dp[n - 1][3000])