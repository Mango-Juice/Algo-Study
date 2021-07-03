#https://www.acmicpc.net/problem/12852

from collections import defaultdict, deque

x = int(input())

dp = {}
count = {}
count[x] = 0

for i in range(x, 1, -1):
    if i % 3 == 0 and (not i // 3 in count or count[i // 3] > count[i] + 1):
        dp[i // 3] = i
        count[i // 3] = count[i] + 1
    if i % 2 == 0 and (not i // 2 in count or count[i // 2] > count[i] + 1):
        dp[i // 2] = i
        count[i // 2] = count[i] + 1
    if i > 1 and (not i - 1 in count or count[i - 1] > count[i] + 1):
        dp[i - 1] = i
        count[i - 1] = count[i] + 1

answer = []
idx = 1

while idx <= x:
    answer.append(idx)
    idx = dp[idx] if idx in dp else x + 1

print(len(answer) - 1)
print(' '.join(map(str, answer[::-1])))
