# https://www.acmicpc.net/problem/1162

import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[] for _ in range(N + 1)]
distance = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(M):
    f, t, w = map(int, input().split())
    arr[f].append((w, t))
    arr[t].append((w, f))

distance[1][0] = 0
heap = [(0, 1, 0)]

while heap:
    w, t, c = heapq.heappop(heap)

    if -1 < distance[t][c] < w:
        continue

    for nw, nt in arr[t]:
        if c < K:
            if not (-1 < distance[nt][c + 1] <= distance[t][c]):
                distance[nt][c + 1] = distance[t][c]
                heapq.heappush(heap, (distance[nt][c + 1], nt, c + 1))

        if not (-1 < distance[nt][c] <= distance[t][c] + nw):
            distance[nt][c] = distance[t][c] + nw
            heapq.heappush(heap, (distance[nt][c], nt, c))

print(min(distance[N]))
