import sys
from collections import deque
input = sys.stdin.readline
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(start_row, start_col, n, m, arr):
    res = [[float('inf')] * (m + 2) for _ in range(n + 2)]
    dq = deque([(start_row, start_col)])
    res[start_row][start_col] = 0
    
    while dq:
        r, c = dq.popleft()
        
        for dr, dx in directions:
            nr, nc = r + dr, c + dx
            if nr < 0 or nr >= n + 2 or nc < 0 or nc >= m + 2: continue
            if arr[nr][nc] == "." and res[nr][nc] > res[r][c]:
                dq.appendleft((nr, nc))
                res[nr][nc] = res[r][c]
            elif arr[nr][nc] == "#" and res[nr][nc] > res[r][c] + 1:
                dq.append((nr, nc))
                res[nr][nc] = res[r][c] + 1

    return res


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [["."] * (m + 2)]
    s = []
    
    for i in range(n):
        inp = list(input().strip())
        for j in range(m):
            if inp[j] == "$":
                inp[j] = "."
                s.append((i + 1, j + 1))
        arr.append(["."] + inp + ["."])
    arr.append(["."] * (m + 2))
    
    res1 = bfs(0, 0, n, m, arr)
    res2 = bfs(s[0][0], s[0][1], n, m, arr)
    res3 = bfs(s[1][0], s[1][1], n, m, arr)
    
    answer = float("inf")
    for i in range(n + 2):
        for j in range(m + 2):
            res = res1[i][j] + res2[i][j] + res3[i][j] - (2 if arr[i][j] == "#" else 0)
            answer = min(answer, res)
    
    print(answer)