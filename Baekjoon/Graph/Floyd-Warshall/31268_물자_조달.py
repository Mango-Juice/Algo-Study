# 플로이드 와샬 응용 + 오프라인 쿼리

import sys
input = sys.stdin.readline

# 입력
n, m, q = map(int, input().split())
t = [0] + list(map(int, input().split()))
road = [[float('inf')] * (n + 1) for _ in range(n + 1)]
queries = []
answers = []

for _ in range(m):
    u, v, w = map(int, input().split())
    road[u][v] = road[v][u] = w
    
for _ in range(q):
    inp = list(map(int, input().split()))
    queries.append(inp)
    
    if inp[0] == 1:
        t[inp[1]] += inp[2]
        
# 플로이드 와샬
def find_way(target):
    if target < 0:
        for k in range(1, n + 1):
            find_way(k)
    else:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                road[i][j] = min(road[i][j], road[i][target] + road[target][j] + t[target])

# 오프라인 쿼리
find_way(-1)
target = -1

for command, a, b in queries[::-1]:
    if command == 1:
        if target != a:
            if target > 0:
                find_way(target)
            target = a
        t[a] -= b
        
    else:
        cost = road[a][b]
        if target > 0:
            cost = min(cost, road[a][target] + road[target][b] + t[target])
        answers.append(-1 if cost == float('inf') else cost)

# 출력
print(*answers[::-1], sep = '\n')
