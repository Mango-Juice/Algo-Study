# https://www.acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    heapq.heapify(arr)
    answer = 0

    while arr:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        answer += a + b

        if arr:
            heapq.heappush(arr, a + b)

    print(answer)
