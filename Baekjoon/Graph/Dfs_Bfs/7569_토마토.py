import sys
input = sys.stdin.readline
directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

m, n, h = map(int, input().split())
arr = [[] for _ in range(h)] # arr[h][n][m]
unripe = 0
now = []

for i in range(h):
    for j in range(n):
        inp = list(map(int, input().split()))
        arr[i].append(inp)
        
        for k in range(m):
            if inp[k] == 1:
                now.append((i, j, k))
            elif inp[k] == 0:
                unripe += 1

day = 0
while now and unripe:
    day += 1
    next = []
    
    for i, j, k in now:
        for di, dj, dk in directions:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
                if arr[ni][nj][nk] == 0:
                    arr[ni][nj][nk] = 1
                    unripe -= 1
                    next.append((ni, nj, nk))
    
    now = next[:]
    if unripe == 0:
        break

print(day if unripe == 0 else -1)