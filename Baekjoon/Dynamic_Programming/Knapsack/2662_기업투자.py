import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(m + 1)]
last = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(j + 1):
            val = dp[i - 1][j - k] + arr[k][i]
            if val > dp[i][j]:
                dp[i][j] = val
                last[i][j] = k

now = last[m][n]
trace = [now]
for i in range(m - 1, 0, -1):
    target = last[i][n - now]
    trace.append(target)
    now += target
    
print(dp[m][n])
print(*trace[::-1])