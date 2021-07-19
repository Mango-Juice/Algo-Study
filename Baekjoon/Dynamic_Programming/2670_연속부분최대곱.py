#https://www.acmicpc.net/problem/2670

import sys

t = int(sys.stdin.readline())
dp = []
arr = []

for i in range(t):
    n = float(sys.stdin.readline())
    arr.append(n)

dp.append(arr[0])

for i in arr[1:]:
    dp.append(max(i, dp[-1] * i))

print("{:.3f}".format(round(max(dp), 3)))
