# https://www.acmicpc.net/problem/2075

import sys
import heapq
input = sys.stdin.readline

n = int(input())
table=[]

for i in range(n):
    table.append(list(map(int, input().split())))
    
heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap, table[i][j])
        if len(heap)>n:
            heapq.heappop(heap)
            
print(heap[0])
