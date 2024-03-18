import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, a, b = map(int, input().split())
    hap = a + b if a + b >= 0 else -float('inf')
    graph[u].append((hap, v))
    graph[v].append((hap, u))

T = int(input())

heap = [(0, 1)]
distance = [float('inf')] * (N + 1)
distance[1] = 0

while heap:
    w, t = heapq.heappop(heap)
    if distance[t] < w: continue
    for nw, nt in graph[t]:
        if distance[nt] > distance[t] + nw:
            distance[nt] = distance[t] + nw
            heapq.heappush(heap, (distance[nt], nt))

answer = []
for i in range(2, N + 1):
    if distance[i] <= T * 2:
        answer.append(i)

print(len(answer))
if answer: print(*answer)