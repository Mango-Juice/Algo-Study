import sys
input = sys.stdin.readline

uses = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [float('inf')] * 101

dp[0] = 0
for i in range(101):
    for j in range(10):
        if uses[j] <= i:
            last = dp[i - uses[j]]
            if not (last == j == 0 or last == float('inf')):
                dp[i] = min(dp[i], last * 10 + j)

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n], "1" * (n // 2) if n % 2 == 0 else "7" + "1" * (n // 2 - 1))