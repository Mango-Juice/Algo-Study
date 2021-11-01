# https://www.acmicpc.net/problem/23295

import sys
input = sys.stdin.readline

MAX = 100001
N, T = map(int, input().split())
times = [0 for _ in range(MAX)]
limit = answer = val = -1

for _ in range(N):
    K = int(input())

    for _ in range(K):
        a, b = map(int, input().split())
        limit = max(limit, b + 1)
        times[a] += 1
        times[b] -= 1

for i in range(1, limit): times[i] += times[i - 1]

for i in range(limit):
    if i > 0: times[i] += times[i - 1]

    if i >= T - 1:
        result = times[i] - (times[i - T] if i >= T else 0)
        if result > val: answer, val = i + 1, result

print(answer - T, answer)
