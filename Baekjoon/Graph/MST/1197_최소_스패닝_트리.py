# https://www.acmicpc.net/problem/1197

import sys

sys.setrecursionlimit(10**9)

def find(x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x: int, y: int) -> None:
    xr = find(x)
    yr = find(y)

    if xr != yr:
        if rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[xr] = yr
            if rank[xr] == rank[yr]:
                rank[yr] += 1

n, e = map(int, sys.stdin.readline().split())
parent = [x for x in range(n + 1)]
rank = [0] * (n + 1)
edges = []
answer = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    weight, st, nd = edge

    if find(st) != find(nd):
        union(st, nd)
        answer += weight

print(answer)
