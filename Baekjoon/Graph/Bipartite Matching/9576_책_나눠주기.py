import sys
input = sys.stdin.readline

n, m = 0, 0
books = []
assign = [-1] * (m + 1)
visited = [False] * (m + 1)

def dfs(target):
    for book in books[target]:
        if visited[book] :
            continue
        visited[book] = True
        
        if assign[book] < 0 or dfs(assign[book]):
            assign[book] = target
            return 1
    
    return 0

def run(target):
    global visited
    visited = [False] * (m + 1)
    return dfs(target)


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    books = []
    assign = [-1] * (m + 1)
    visited = [False] * (m + 1)
    
    for _ in range(n):
        a, b = map(int, input().split())
        books.append(range(a, b + 1))
    
    print(sum([run(i) for i in range(n)]))