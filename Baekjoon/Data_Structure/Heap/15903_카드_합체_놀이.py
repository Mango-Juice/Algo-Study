# https://www.acmicpc.net/problem/15903

import heapq

n, m = map(int, input().split())
an = list(map(int, input().split()))
heapq.heapify(an)

for _ in range(m):
    a = heapq.heappop(an)
    b = heapq.heappop(an)
    heapq.heappush(an, a + b)
    heapq.heappush(an, a + b)

print(sum(an))
