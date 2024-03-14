import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited = [False] * (n + 1)
    ans = val = 0
    
    stack = deque([(start, 0)])
    visited[start] = True
    
    while stack:
        now, now_val = stack.pop()
        
        for next, next_val in graph[now]:
            if not visited[next]:
                stack.append((next, now_val + next_val))
                visited[next] = True
                if now_val + next_val > val:
                    val = now_val + next_val
                    ans = next
    
    return (ans, val)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

index, _ = dfs(1)
_, answer = dfs(index)
print(answer)