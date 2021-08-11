# https://www.acmicpc.net/problem/13334
# 스위핑

from collections import deque
import sys, heapq
input = sys.stdin.readline

answer = 0
arr = deque()
n = int(input())

for _ in range(n):
    arr.append(sorted(map(int, input().split())))

d = int(input())

arr = deque(sorted(arr, key = lambda x : x[1]))

heap = []

while arr:
    a, b = arr.popleft()
    if b - a > d: continue
    heapq.heappush(heap, (a, b))
    while heap[0][0] < b - d: heapq.heappop(heap)

    answer = max(answer, len(heap))

print(answer)
