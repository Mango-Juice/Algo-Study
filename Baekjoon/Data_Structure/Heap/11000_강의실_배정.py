# https://www.acmicpc.net/problem/11000

import sys, heapq

n = int(sys.stdin.readline())
heap = []
gang = []

for _ in range(n):
    heapq.heappush(heap, tuple(map(int, sys.stdin.readline().split())))

while heap:
    start, finish = heapq.heappop(heap)
    flag = False

    if gang and gang[0] <= start:
        heapq.heappop(gang)
        
    heapq.heappush(gang, finish)

print(len(gang))
