# https://www.acmicpc.net/problem/1916
# 선형 탐색을 이용한 다익스트라 알고리즘

import sys, heapq
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
tree = defaultdict(list)
distance = [-1] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    from_, to_, weight = map(int, sys.stdin.readline().split())
    tree[from_].append((to_, weight))

start, finish = map(int, sys.stdin.readline().split())
distance[start] = 0

while True:
    min_v, min_i = float('inf'), -1
    
    for i in range(1, n + 1):
        if (not visited[i]) and -1 < distance[i] < min_v:
            min_v, min_i = distance[i], i

    if min_i == -1:
        break
    
    visited[min_i] = True
    for t, w in tree[min_i]:
        if distance[t] < 0 or distance[t] > distance[min_i] + w:
            distance[t] = distance[min_i] + w

print(distance[finish])
