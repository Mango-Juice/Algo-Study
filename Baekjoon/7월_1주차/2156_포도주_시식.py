#https://www.acmicpc.net/problem/2156

import sys

t = int(sys.stdin.readline())
arr = []
dp1 = [0 for _ in range(t)]
dp2 = [0 for _ in range(t)]

for i in range(t):
    n = int(sys.stdin.readline())
    arr.append(n)

for idx, amount in enumerate(arr):
    target1 = target2 = 0

    if idx > 1:
        target1 = dp2[idx - 1]
        target2 = max(dp1[idx - 2], dp2[idx - 2]) + amount

    dp1[idx] = max(amount, target1, target2)

    if idx > 0:
        dp2[idx] = dp1[idx - 1] + amount

print(max(dp1[-1], dp2[-1]))
