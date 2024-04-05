import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    i_graph = [None] * (n + 1)
    o_graph = [[] for _ in range(n + 1)]
    depth = [None] * (n + 1)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        i_graph[b] = a
        o_graph[a].append(b)
    
    for i in range(1, n + 1):
        if i_graph[i] == None:
            root = i
            break

    depth[root] = 1
    stack = deque([root])
    while stack:
        now = stack.pop()
        for target in o_graph[now]:
            if not depth[target]:
                depth[target] = depth[now] + 1
                stack.append(target)

    a, b = map(int, input().split())
    while depth[a] > depth[b]: a = i_graph[a]
    while depth[a] < depth[b]: b = i_graph[b]
    while a != b: a, b = i_graph[a], i_graph[b]
    print(a)