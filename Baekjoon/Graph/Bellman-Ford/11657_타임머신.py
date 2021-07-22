# https://www.acmicpc.net/problem/11657
# 벨만-포드 알고리즘

from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
dist = [float('inf')] * (N + 1)
dist[1] = 0

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))

for i in range(N):
    flag = False
    
    for now in range(1, N + 1):
        if dist[now] == float('inf'):
            continue

        for next_, cost in graph[now]:
            if dist[next_] > dist[now] + cost:
                dist[next_] = dist[now] + cost
                flag = True

    if not flag:
        break

if flag:
    print(-1)
else:
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != float('inf') else -1)
