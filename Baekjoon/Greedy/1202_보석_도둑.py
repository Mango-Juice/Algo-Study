# https://www.acmicpc.net/problem/1202
# Greedy

import sys, heapq

N, K = map(int, sys.stdin.readline().split())
jewel = []
bag = []
values = []
answer = jewel_idx = 0

for _ in range(N):
    jewel.append(tuple(map(int, sys.stdin.readline().split())))

for _ in range(K):
    bag.append(int(sys.stdin.readline()))

bag.sort()
jewel.sort()

for b in bag:
    while jewel_idx < N and jewel[jewel_idx][0] <= b:
        heapq.heappush(values, -jewel[jewel_idx][1])
        jewel_idx += 1
        
    answer += -heapq.heappop(values) if values else 0

print(answer)
