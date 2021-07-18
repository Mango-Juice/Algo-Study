# https://www.acmicpc.net/problem/1504
# 다익스트라 활용

import sys, heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
tree = defaultdict(list)

for _ in range(m):
    from_, to_, weight = map(int, sys.stdin.readline().split())
    tree[from_].append((to_, weight))
    tree[to_].append((from_, weight))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(fr, to):
    distance = [-1] * (n + 1)
    heap = []
    distance[fr] = 0
    heapq.heappush(heap, (0, fr))

    while heap:
        w, t = heapq.heappop(heap)
        
        for tt, tw in tree[t]:
            if distance[tt] == -1 or distance[tt] > distance[t] + tw:
                distance[tt] = distance[t] + tw
                heapq.heappush(heap, (distance[tt], tt))
    return distance[to]

d1, d2, d3, d4, d5, d6 = dijkstra(1, v1), dijkstra(v1, v2), dijkstra(v2, n), dijkstra(1, v2), dijkstra(v2, v1), dijkstra(v1, n)
t1 = d1 + d2 + d3 if d1 > -1 and d2 > -1 and d3 > -1 else -1
t2 = d4 + d5 + d6 if d4 > -1 and d5 > -1 and d6 > -1 else -1

if t1 == -1:
    print(t2)
elif t2 == -1:
    print(t1)
else:
    print(min(t1, t2))
