import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c * 2))
    graph[b].append((a, c * 2))

distance = [float('inf')] * (n + 1)
distance[1] = 0

pq = [(0, 1)]
while pq:
    d, u = heapq.heappop(pq)
    if distance[u] < d: continue
    for v, w in graph[u]:
        if distance[v] > d + w:
            distance[v] = d + w
            heapq.heappush(pq, (d + w, v))

wolf_distance = [[float('inf')] * 2 for _ in range(n + 1)]
wolf_distance[1][1] = 0

pq = [(0, 1, True)]
while pq:
    d, u, t = heapq.heappop(pq)
    if wolf_distance[u][t] < d: continue
    for v, w in graph[u]:
        w = w // 2 if t else w * 2
        nt = not t
        if wolf_distance[v][nt] > d + w:
            wolf_distance[v][nt] = d + w
            heapq.heappush(pq, (d + w, v, nt))

answer = 0
for i in range(1, n + 1):
    if distance[i] < min(wolf_distance[i]):
        answer += 1
print(answer)