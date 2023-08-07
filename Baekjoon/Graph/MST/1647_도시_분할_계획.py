# https://www.acmicpc.net/problem/1647
# 최소 스패닝 트리 + Union Find

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

roads = []
parents = [i for i in range(n + 1)]
answer = 0
last = 0

def find(a):
    if parents[a] != a:
        return find(parents[a])
    return a

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))

roads.sort()

for c, a, b in roads:
    if find(a) != find(b):
        union(a, b)
        answer += c
        last = c

print(answer - last)
