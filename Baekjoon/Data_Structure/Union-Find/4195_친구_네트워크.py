#https://www.acmicpc.net/problem/4195

import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def find(x: int) -> int:
    if tree[x] == '':
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x: int, y: int) -> None:
    xr = find(x)
    yr = find(y)
    if xr != yr:
        tree[xr] = yr
        count[xr], count[yr] = 0, count[xr] + count[yr] + 1

t = int(input())

for _ in range(t):
    f = int(sys.stdin.readline())
    tree = defaultdict(str)
    count = defaultdict(int)

    for _ in range(f):
        a, b = sys.stdin.readline().split()
        union(a, b)
        print(count[find(a)] + 1)
