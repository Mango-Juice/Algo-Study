# https://www.acmicpc.net/problem/2166

import sys

n = int(sys.stdin.readline())
xs = []
ys = []
answer = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)

for i in range(n):
    answer += xs[i] * (ys[i + 1] - ys[i - 1]) if i + 1 < n else xs[i] * (ys[0] - ys[i - 1])

print("{0:.1f}".format(abs(answer) / 2))
