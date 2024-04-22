import sys
from collections import deque
input  = sys.stdin.readline

n = int(input())
inp = [list(map(int, input().rstrip())) for _ in range(n)]
graph = [[] for _ in range(n)]
visited = [False] * n
answer = 0

for i in range(n):
    for j in range(n):
        if inp[i][j]:
            graph[i].append(j)
            graph[j].append(i)

for i in range(n):
    if visited[i]: continue
    result = [0, 0]
    types = [None] * n
    visited[i] = types[i] = True
    result[types[i]] += 1
    q = deque([i])

    while q:
        now = q.popleft()
        for j in graph[now]:
            if not visited[j]:
                visited[j] = True
                types[j] = not types[now]
                result[types[j]] += 1
                q.append(j)
    
    answer += max(result)

print(answer)