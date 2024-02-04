import sys
input = sys.stdin.readline

n, m = map(int, input().split())
notebooks = [[] for _ in range(n)]
assign = [-1] * n
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    notebooks[a - 1].append(b - 1)

def dfs(target):
    for notebook in notebooks[target]:
        if visited[notebook] :
            continue
        visited[notebook] = True
        
        if assign[notebook] < 0 or dfs(assign[notebook]):
            assign[notebook] = target
            return 1
    
    return 0

def run(target):
    global visited
    visited = [False] * n
    return dfs(target)

print(sum([run(i) for i in range(n)]))