import sys
from collections import deque
input = sys.stdin.readline

char_to_int = {".": 0, "R": 1, "G": 2, "B": 3, "P": 4, "Y": 5}
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
arr = [[0] * 12 for _ in range(6)]

for j in range(12):
    inp = list(map(lambda x: char_to_int[x], input().strip()))
    for i in range(6):
        arr[i][11 - j] = inp[i]

count = 0
while True:
    visited = [[False] * 12 for _ in range(6)]
    flag = False

    for i in range(6):
        for j in range(12):
            if arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                targets = [(i, j)]
                q = deque([(i, j)])
                
                while q:
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= 6 or nc < 0 or nc >= 12: continue
                        if arr[nr][nc] == arr[r][c] and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            targets.append((nr, nc))
                
                if len(targets) >= 4:
                    flag = True
                    for r, c in targets:
                        arr[r][c] = 0
    
    if not flag: break
    count += 1
    
    for i in range(6):
        new_arr = [0] * 12
        idx = 0
        for j in range(12):
            if arr[i][j] != 0:
                new_arr[idx] = arr[i][j]
                idx += 1
        arr[i] = new_arr

print(count)