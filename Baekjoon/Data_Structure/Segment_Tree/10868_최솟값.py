# https://www.acmicpc.net/problem/10868

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

arr = []
min_tree = []

def min_init(f, t, i):
    if f == t: min_tree[i] = arr[f]
    else:
        m = (f + t) // 2
        min_tree[i] = min(min_init(f, m, i * 2), min_init(m + 1, t, i * 2 + 1))
    return min_tree[i]

def min_get(f, t, i, l, r):
    if f > r or t < l: return 1000000000
    if l <= f and r >= t: return min_tree[i]
    m = (f + t) // 2
    return min(min_get(f, m, i * 2, l, r), min_get(m + 1, t, i * 2 + 1, l, r))

n, m = map(int, input().split())

for i in range(n): arr.append(int(input()))

min_tree = [0] * n * 4

min_init(0, n - 1, 1)

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(min_get(0, n - 1, 1, a, b))
