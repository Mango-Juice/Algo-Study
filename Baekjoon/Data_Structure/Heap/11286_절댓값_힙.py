# https://www.acmicpc.net/problem/11286

import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        print(heapq.heappop(heap)[1] if heap else 0)

    else:
        heapq.heappush(heap, (abs(x), x))
