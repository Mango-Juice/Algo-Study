import sys
input = sys.stdin.readline

n = int(input())
inp = list(map(int, input().split()))
half = sum(inp) // 2
arr = []

for i, v in enumerate(inp):
    arr.append((i + 1, v))

arr.sort(key = lambda x: -x[1])
dp = [[] for _ in range(100001)]
answer = 0

for i, v in arr:
    for last in range(half, -1, -1):
        value = last + v
        if (dp[last] or last == 0) and not dp[value]:
            answer = max(answer, value)
            dp[value] = dp[last] + [i]

print(len(dp[answer]))
print(*dp[answer])