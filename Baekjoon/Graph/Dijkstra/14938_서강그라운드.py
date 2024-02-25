import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, n + 1):
    value = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            value += t[j]
    answer = max(answer, value)

print(answer)