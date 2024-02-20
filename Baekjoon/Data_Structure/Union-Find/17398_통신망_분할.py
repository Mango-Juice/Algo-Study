import sys
input = sys.stdin.readline

def find(a):
    if a == graph[a]: return a
    graph[a] = find(graph[a])
    return graph[a]

def union(a, b):
    a = find(a)
    b = find(b)
    cost = count[a] * count[b] if a != b else 0
    
    if a < b:
        graph[b] = a
        count[a] += count[b]
    if a > b:
        graph[a] = b
        count[b] += count[a]
    return cost

n, m, q = map(int, input().split())
connections = [list(map(int, input().split())) for _ in range(m)]
queries = [int(input()) for _ in range(q)][::-1]

graph = [i for i in range(n + 1)]
count = [1] * (n + 1)

disconnected = [False] * m
for i in queries:
    disconnected[i - 1] = True

for i, (a, b) in enumerate(connections):
    if not disconnected[i]:
        union(a, b)

answer = 0
for i in queries:
    a, b = connections[i - 1]
    answer += union(a, b)

print(answer)