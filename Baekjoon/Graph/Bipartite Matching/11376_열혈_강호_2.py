import sys
input = sys.stdin.readline

n, m = map(int, input().split())
works = [list(map(int, input().split()))[1:] for _ in range(n)] * 2
assign = [-1] * (m + 1)
visited = [False] * (m + 1)

def dfs(target):
    for work in works[target]:
        if visited[work] :
            continue
        visited[work] = True
        
        if assign[work] < 0 or dfs(assign[work]):
            assign[work] = target
            return 1
    
    return 0

def run(target):
    global visited
    visited = [False] * (m + 1)
    return dfs(target)

print(sum([run(i) for i in range(n * 2)]))