import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [None] * (n + 1)
depth = [None] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth[1] = 1
stack = deque([1])
while stack:
    now = stack.pop()
    for target in graph[now]:
        if not depth[target]:
            depth[target] = depth[now] + 1
            parent[target] = now
            stack.append(target)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    while depth[a] > depth[b]: a = parent[a]
    while depth[a] < depth[b]: b = parent[b]
    while a != b: a, b = parent[a], parent[b]
    print(a)