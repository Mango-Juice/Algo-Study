# https://www.acmicpc.net/problem/1647
# 최소 스패닝 트리 + Union Find

import sys

sys.setrecursionlimit(10 ** 6)

def find(x):
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        tree[x] = y

n, m = map(int, sys.stdin.readline().split())
edges = []
tree = [i for i in range(n + 1)]

for _ in range(m):
    from_, to_, weight = tuple(map(int, sys.stdin.readline().split()))
    edges.append((weight, from_, to_))

edges.sort()

sum_ = 0
count = 0

for edge in edges:
    weight, from_, to_ = edge

    if find(from_) != find(to_):
        sum_ += weight
        union(from_, to_)
        count += 1
        
        if count == n - 2:
            break

print(sum_)
