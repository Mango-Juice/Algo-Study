# https://www.acmicpc.net/problem/4386

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

n =  int(sys.stdin.readline())
parent = [x for x in range(n)]
rank = [0] * n
stars = []
edges = []
idx = 0
answer = 0

for _ in range(n):
    a, b = map(float, sys.stdin.readline().split())
    for index, star in enumerate(stars):
        edges.append(((a - star[0]) ** 2 + (b - star[1]) ** 2, idx, index))
    stars.append((a, b))
    idx += 1

edges.sort()

for edge in edges:
    weight, st, nd = edge

    if find(st) != find(nd):
        union(st, nd)
        answer += weight ** (1/2)

print(answer)
