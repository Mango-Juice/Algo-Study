import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    types = [None] * v
    
    for _ in range(e):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)
    
    no = False
    q = deque()
    
    for i in range(v):
        if types[i] != None: continue
        types[i] = True
        q.append(i)
        while q:
            now = q.popleft()
            for next in graph[now]:
                if types[next] == types[now]:
                    no = True
                    break
                elif types[next] == None:
                    types[next] = not types[now]
                    q.append(next)
            if no: break
        if no: break
    
    print("NO" if no else "YES")