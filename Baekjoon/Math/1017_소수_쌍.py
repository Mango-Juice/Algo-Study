import sys, math
input = sys.stdin.readline

N = 2000
is_prime = [True] * (N + 1)
is_prime[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * 2, N + 1, i):
            is_prime[j] = False

####################

def dfs(target):
    for work in matching[target]:
        if visited[work] or removed[work]:
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

####################

n = int(input())
arr = list(map(int, input().split()))

matching = [[] for _ in range(n)]
assign = [-1] * (n + 1)
visited = [False] * (n + 1)
removed = [False] * (n + 1)

for i in range(n - 1):
    for j in range(i + 1, n):
        if is_prime[arr[i] + arr[j]]:
            matching[i].append(j)
            matching[j].append(i)

removed[0] = True
answer = []
for target in matching[0]:
    assign = [-1] * (n + 1)
    removed[target] = True

    result = sum([run(i) for i in range(1, n)])
    if result == n - 2: 
        answer.append(arr[target])
    
    removed[target] = False

answer.sort()
print(*answer if answer else [-1])