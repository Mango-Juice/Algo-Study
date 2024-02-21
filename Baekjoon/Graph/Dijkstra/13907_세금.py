import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
s, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distances = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

ps = [int(input()) for _ in range(k)]

pq = [(0, 0, s)]
distances[0][s] = 0

while pq:
    dist, count, node = heapq.heappop(pq)
    if dist > min(distances[node][:count + 1]): continue
    if node == d: continue
    
    for next_node, next_dist in graph[node]:
        if distances[next_node][count + 1] > dist + next_dist:
            distances[next_node][count + 1] = dist + next_dist
            if count < n - 1:
                heapq.heappush(pq, (distances[next_node][count + 1], count + 1, next_node))

print(min(distances[d]))

for p in ps:
    for i in range(1, n + 1):
        distances[d][i] += i * p
    print(min(distances[d]))