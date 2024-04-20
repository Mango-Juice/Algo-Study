import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(target, now_depth, now_dist):
    visited[target] = True
    depth[target] = now_depth
    
    for next_target, next_cost in graph[target]:
        if not visited[next_target]:
            parents[next_target][0] = target
            minimums[next_target][0] = maximums[next_target][0] = next_cost
            dfs(next_target, now_depth + 1, now_dist + next_cost)


def lca(a, b):
    mi, ma = float("inf"), -float("inf")
    
    if depth[a] < depth[b]:
        a, b = b, a
    
    for i in range(MAXIMUM - 1, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            mi = min(mi, minimums[a][i])
            ma = max(ma, maximums[a][i])
            a = parents[a][i]
    
    if a == b:
        return (mi, ma)
    
    for i in range(MAXIMUM - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            mi = min(mi, minimums[a][i], minimums[b][i])
            ma = max(ma, maximums[a][i], maximums[b][i])
            a, b = parents[a][i], parents[b][i]
    
    return (min(mi, minimums[a][i], minimums[b][i]), max(ma, maximums[a][i], maximums[b][i]))


MAXIMUM = 17
n = int(input())

parents = [[0] * MAXIMUM for _ in range(n + 1)]
depth = [0] * (n + 1)
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

minimums = [[float("inf")] * MAXIMUM for _ in range(n + 1)]
maximums = [[-float("inf")] * MAXIMUM for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c= map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dfs(1, 0, 0)
for i in range(1, MAXIMUM):
    for j in range(1, n + 1):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]
        minimums[j][i] = min(minimums[parents[j][i - 1]][i - 1], minimums[j][i - 1])
        maximums[j][i] = max(maximums[parents[j][i - 1]][i - 1], maximums[j][i - 1])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(*lca(a, b))