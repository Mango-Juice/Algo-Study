# https://www.acmicpc.net/problem/17298

import heapq

answer = [ "-1" for _ in range(int(input())) ]
arr = map(int, input().split())
heap = []

for idx, value in enumerate(arr):
    while heap and heap[0][0] < value:
        answer[heapq.heappop(heap)[1]] = str(value)
    heapq.heappush(heap, (value, idx))

print(' '.join(answer))
