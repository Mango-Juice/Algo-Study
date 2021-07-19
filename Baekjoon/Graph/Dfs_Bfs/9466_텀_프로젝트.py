#https://www.acmicpc.net/problem/9466

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100001)

def dfs(x):
    global answer
    visited[x] = True
    number = numbers[x]
    
    cycle.append(x)
    
    if visited[number]:
        if number in cycle:
            answer += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False for _ in range(n)]
    answer = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
            
    print(n - len(answer))
