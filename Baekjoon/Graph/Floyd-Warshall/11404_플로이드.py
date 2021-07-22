# https://www.acmicpc.net/problem/11404
# 플로이드-와샬 알고리즘

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[0 if i == j else float('inf') for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0
    print(*dist[i][1:], sep = " ")
