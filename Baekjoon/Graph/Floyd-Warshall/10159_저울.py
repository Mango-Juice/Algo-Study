import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True

for i in range(1, n + 1):
    graph[i][i] = True

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for i in range(1, n + 1):
    print(n - sum([graph[j][i] or graph[i][j] for j in range(1, n + 1)]))