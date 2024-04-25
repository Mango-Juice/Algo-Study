import sys
input = sys.stdin.readline

n, m = map(int, input().split())
types = {}
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    i, t = input().split()
    types[int(i)] = t

for _ in range(m):
    a, b = map(int, input().split())
    if types[a] == "c": graph[a].append(b)
    else: graph[b].append(a)

assign = [-1] * (n + 1)
visited = [False] * (n + 1)

def dfs(target):
    for work in graph[target]:
        if visited[work]:
            continue
        visited[work] = True
        
        if assign[work] < 0 or dfs(assign[work]):
            assign[work] = target
            return 1
    
    return 0

def run(target):
    global visited
    visited = [False] * (n + 1)
    return dfs(target)

print(n - sum([run(i) for i in range(n + 1)]))