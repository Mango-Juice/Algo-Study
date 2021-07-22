# https://www.acmicpc.net/problem/1005
# 위상 정

from collections import deque
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N, K = map(int, stdin.readline().split())
    time = [0] + list(map(int, stdin.readline().split()))
    indegree = [0] * (N + 1)
    result = [0] * (N + 1)
    graph = [[] for i in range(N + 1)]
    queue = deque()

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1

    destination = int(stdin.readline())

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i]

    while queue:
        target = queue.popleft()
        
        for i in graph[target]:
            indegree[i] -= 1
            result[i] = max(result[i], result[target] + time[i])
            
            if indegree[i] == 0:
                queue.append(i)

    print(result[destination])
