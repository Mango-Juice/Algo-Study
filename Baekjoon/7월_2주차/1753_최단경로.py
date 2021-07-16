# https://www.acmicpc.net/problem/1753
# 최소 힙을 이용한 다익스트라 알고리즘

import sys, heapq
from collections import defaultdict

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
tree = defaultdict(list)
distance = [-1] * (v + 1)
heap = []

for _ in range(e):
    from_, to_, weight = map(int, sys.stdin.readline().split())
    tree[from_].append((weight, to_))

distance[k] = 0
heapq.heappush(heap, (0, k))

while heap:
    w, t = heapq.heappop(heap)
    
    if -1 < distance[t] < w:
        continue

    for target_weight, target_to_ in tree[t]:
        if distance[target_to_] == -1 or distance[target_to_] > distance[t] + target_weight:
            distance[target_to_] = distance[t] + target_weight
            heapq.heappush(heap, (distance[target_to_], target_to_))

for i in range(1, v + 1):
    print(distance[i] if distance[i] > -1 else "INF")
