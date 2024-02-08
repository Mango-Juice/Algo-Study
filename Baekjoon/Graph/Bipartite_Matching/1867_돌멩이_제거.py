# 쾨닉의 정리
# 최대 매칭 == 최소 정점 커버
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ways = [[] for _ in range(n)]
assign = [-1] * n
visited = [False] * n


def dfs(target):
    for rock in ways[target]:
        if visited[rock]: continue
        visited[rock] = True
        
        if assign[rock] < 0 or dfs(assign[rock]):
            assign[rock] = target
            return 1
    return 0


def run(target):
    global visited
    visited = [False] * n
    return dfs(target)


for _ in range(k):
    r, c = map(int, input().split())
    ways[r - 1].append(c - 1)

print(sum([run(i) for i in range(n)]))