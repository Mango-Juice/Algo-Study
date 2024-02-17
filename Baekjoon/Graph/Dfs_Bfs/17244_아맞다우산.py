import sys
from collections import deque
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

m, n = map(int, input().split())
arr = []
q = deque()
x = 0

for i in range(n):
    inp = list(input().strip())
    
    for j in range(m):
        if inp[j] == "S":
            q.append((i, j, 0, 0))
        
        if inp[j] == "X":
            inp[j] = x
            x += 1
    
    arr.append(inp)

visited = [[[False] * (1 << x) for _ in range(m)] for _ in range(n)]

while q:
    row, col, time, key = q.popleft()
    visited[row][col][key] = True
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        
        if 0 <= nr < n and 0 <= nc < m:
            target = arr[nr][nc]
            
            if type(target) == int:
                next_key = key | (1 << target)
                if not visited[nr][nc][next_key]:
                    visited[nr][nc][next_key] = True
                    q.append((nr, nc, time + 1, next_key))
                    
            elif (target == "." or target == "S") and not visited[nr][nc][key]:
                visited[nr][nc][key] = True
                q.append((nr, nc, time + 1, key))
                
            elif target == "E" and key == (1 << x) - 1:
                print(time + 1)
                exit()