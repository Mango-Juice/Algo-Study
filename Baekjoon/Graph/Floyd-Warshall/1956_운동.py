# https://www.acmicpc.net/problem/1956
# 플로이드-와샬 알고리즘

from collections import deque
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
dist = [[0 if i == j else float('inf') for i in range(v + 1)] for j in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

answer = float('inf')

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j and dist[i][j] != float('inf') and dist[j][i] != float('inf'):
            answer = min(answer, dist[i][j] + dist[j][i])

print(answer if answer < float('inf') else -1)
