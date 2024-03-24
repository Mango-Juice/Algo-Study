import sys
import heapq
input = sys.stdin.readline

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

####################
# 입력

n = int(input())
costs = [[1] * (n + 1) for _ in range(n + 1)]

a, b, c, d = map(int, input().split())
start, finish = (a, b), (c, d)

k = int(input())

for _ in range(int(input())):
    inp = list(map(int, input().split()))
    last = (inp[1], inp[2])
    
    for i in range(3, len(inp), 2):
        now = (inp[i], inp[i + 1])
        for r in range(min(last[0], now[0]), max(last[0], now[0]) + 1):
            for c in range(min(last[1], now[1]), max(last[1], now[1]) + 1):
                costs[r][c] = k
        last = now

####################
# 최단거리 계산

distances = [[float('inf')] * (n + 1) for _ in range(n + 1)]
paths = [[None] * (n + 1) for _ in range(n + 1)]
distances[start[0]][start[1]] = costs[start[0]][start[1]]
pq = [(distances[start[0]][start[1]], start)]

while pq:
    dist, node = heapq.heappop(pq)
    if dist > distances[node[0]][node[1]]: continue
    for dr, dc in directions:
        next_node = (node[0] + dr, node[1] + dc)
        if 0 < next_node[0] < n + 1 and 0 < next_node[1] < n + 1:
            if distances[next_node[0]][next_node[1]] > dist + costs[next_node[0]][next_node[1]]:
                distances[next_node[0]][next_node[1]] = dist + costs[next_node[0]][next_node[1]]
                paths[next_node[0]][next_node[1]] = node
                heapq.heappush(pq, (distances[next_node[0]][next_node[1]], next_node))

####################
# 경로 추적
answer = []
last = finish
last_cha = None

while last != start:
    now = paths[last[0]][last[1]]
    now_cha = (last[0] - now[0], last[1] - now[1])
    
    if now_cha != last_cha:
        answer.append(last[1])
        answer.append(last[0])
    
    last = now
    last_cha = now_cha

answer.append(start[1])
answer.append(start[0])

print(distances[finish[0]][finish[1]])
print(len(answer) // 2, *answer[::-1])