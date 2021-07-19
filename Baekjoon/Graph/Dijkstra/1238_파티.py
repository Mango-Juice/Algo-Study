# https://www.acmicpc.net/problem/1238
# 다익스트라 알고리즘

from collections import defaultdict
import sys, heapq

N, M, X = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
max_value = 0

for _ in range(M):
    f, t, w = map(int, sys.stdin.readline().split())
    tree[f].append((w, t))

def dijkstra(chulbal, dochak):
    distance = [-1] * (N + 1)
    heap = []
    
    distance[chulbal] = 0
    heapq.heappush(heap, (0, chulbal))

    while heap:
        target_weight, target_idx = heapq.heappop(heap)

        if -1 < distance[target_idx] < target_weight:
            continue

        for next_weight, next_idx in tree[target_idx]:
            if distance[next_idx] == -1 or distance[next_idx] > distance[target_idx] + next_weight:
                distance[next_idx] = distance[target_idx] + next_weight
                heapq.heappush(heap, (distance[next_idx], next_idx))

    return distance[dochak]


for i in range(1, N + 1):
    if i == X:
        continue
    
    value = dijkstra(i, X) + dijkstra(X, i)

    if value > max_value:
        max_value = value

print(max_value)
