# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10**9)

def find(x: int) -> int:
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    if x != y:
        tree[x] = y


n, m = map(int, sys.stdin.readline().split())
tree = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
