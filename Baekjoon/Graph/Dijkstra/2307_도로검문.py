# https://www.acmicpc.net/problem/2307
# 다익스트라 알고리즘 활용

import sys, heapq
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
blocked_from = blocked_to = -1

for _ in range(M):
    from_, to, weight = map(int, sys.stdin.readline().split())
    tree[from_].append((weight, to))
    tree[to].append((weight, from_))

def dijkstra():
    distance = [[-1, []] for _ in range(N + 1)]
    heap = []

    distance[1][0] = 0
    distance[1][1] = [1]
    heapq.heappush(heap, (0, 1))

    while heap:
        w, t = heapq.heappop(heap)
        
        if -1 < distance[t][0] < w:
            continue

        for target_weight, target_to in tree[t]:
            if blocked_from == t and blocked_to == target_to:
                continue
            
            if (distance[target_to][0] == -1 or distance[target_to][0] > distance[t][0] + target_weight):
                distance[target_to][0] = distance[t][0] + target_weight
                distance[target_to][1] = distance[t][1] + [target_to]
                heapq.heappush(heap, (distance[target_to][0], target_to))

    return distance[N]

thief = dijkstra()
answer = 0

for i in range(len(thief[1]) - 1):
    if answer == -1:
        break

    blocked_from, blocked_to = thief[1][i], thief[1][i + 1]
    new_thief = dijkstra()
    answer = max(answer, new_thief[0] - thief[0]) if new_thief[0] > -1 else -1

print(answer)
