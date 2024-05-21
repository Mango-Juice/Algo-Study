import sys
input = sys.stdin.readline

NC, W, C = range(3)
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    if arr[r][c] == NC:
        arr[r][c] = C
        answer += 1
        continue
    
    flag = False
    for i in range(4):
        dr, dc = DIR[(d - i + 3) % 4]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == NC:
            r, c = nr, nc
            d = (d - i + 3) % 4
            flag = True
            break
    
    if flag: continue
    dr, dc = DIR[d]
    nr, nc = r - dr, c - dc
    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != W:
        r, c = nr, nc
        continue
    
    break

print(answer)