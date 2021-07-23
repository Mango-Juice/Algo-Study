# https://www.acmicpc.net/problem/3665
# 위상 정렬 활용

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    inp = list(map(int, input().split()))
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    checked = []

    for val in inp:
        for j in checked:
            graph[val][j] = True
            indegree[j] += 1

        checked.append(val)
    
    m = int(input())
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        if(graph[a][b]):
            graph[a][b], graph[b][a] = False, True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b], graph[b][a] = True, False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    unknown = False
    answer = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        if len(q) > 1:
            unknown = True
            break

        target = q.popleft()
        answer.append(target)

        for i in range(1, n + 1):
            if not graph[target][i]:
                continue
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if unknown:
        print('?')
    elif len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(' '.join(list(map(str, answer))[::-1]))
