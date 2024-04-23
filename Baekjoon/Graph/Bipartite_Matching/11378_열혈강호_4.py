import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
works = [list(map(int, input().split()))[1:] for _ in range(n)]
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

answer = sum([run(i) for i in range(n)])
flag = True

while flag and k:
    flag = False
    
    for i in range(n):
        result = run(i)
        if result:
            answer += 1
            k -= 1
            flag = True
        if k == 0:
            break

print(answer)