import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

front = [-1] * (n + 1)
now = n
for i in range(n, -1, -1):
    while arr[now][0] - s >= arr[i][0]:
        front[now] = i
        now -= 1

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[front[i]] + arr[i][1])

print(dp[n])