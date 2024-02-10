# BFS + 비트마스킹
import sys
from collections import deque
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
keys = list("abcdef")
doors = list("ABCDEF")

n, m = map(int, input().split())
arr = []
q = deque()
visited = [[[False] * (1 << 7 - 1) for _ in range(m)] for _ in range(n)]

for i in range(n):
    inp = list(input().strip())
    arr.append(inp)
    
    if "0" in inp:
        idx = inp.index("0")
        q.append((i, idx, 0, 0))
        visited[i][idx][0] = True


while q:
    r, c, count, key = q.popleft()
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < n and 0 <= nc < m:
            t = arr[nr][nc]
            
            if t == "1":
                print(count + 1)
                exit()
            elif t == "." or t == "0":
                if not visited[nr][nc][key]:
                    q.append((nr, nc, count + 1, key))
                    visited[nr][nc][key] = True
            elif t in keys:
                nkey = key | (1 << keys.index(t))
                if not visited[nr][nc][nkey]:
                    q.append((nr, nc, count + 1, nkey))
                    visited[nr][nc][nkey] = True
            elif t in doors:
                idx = doors.index(t)
                if key & (1 << idx) and not visited[nr][nc][key]:
                    q.append((nr, nc, count + 1, key))
                    visited[nr][nc][key] = True

print(-1)