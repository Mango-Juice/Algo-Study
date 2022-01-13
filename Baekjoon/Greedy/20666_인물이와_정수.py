# https://www.acmicpc.net/problem/20666

import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
C = list(map(int, input().split()))
p = int(input())
arr = [[] for _ in range(N)]
visited = [False] * N

for _ in range(p):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    C[b] += t
    arr[a].append((b, t))

heap = list(zip(C, range(N)))
heapq.heapify(heap)
answer = 0
count = 0

while count < M:
    tv, ti = heapq.heappop(heap)
    if visited[ti]:
        continue
    
    answer = max(answer, tv)
    visited[ti] = True
    count += 1
    
    for idx, val in arr[ti]:
        C[idx] -= val
        heapq.heappush(heap, (C[idx], idx))

print(answer)
