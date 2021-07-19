# https://www.acmicpc.net/problem/20040

import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def find(x: int) -> int:
    if tree[x] == -1:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    if x != y:
        tree[x] = y

n, m = map(int, sys.stdin.readline().split())
tree = [-1] * n
flag = False

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if find(a) == find(b):
        print(i + 1)
        flag = True
        break
    else:
        union(a, b)

if not flag:
    print(0)
