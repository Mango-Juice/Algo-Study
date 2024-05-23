import sys
input = sys.stdin.readline
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
tmp = [[] for _ in range(k + 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            tmp[arr[i][j]].append((i, j))

targets = []
for t in tmp:
    targets.extend(t)

count = 1
while count <= s:
    new_targets = []
    for r, c in targets:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c]
                new_targets.append((nr, nc))
    
    if arr[x - 1][y - 1] or not new_targets: break
    targets = new_targets
    count += 1

print(arr[x - 1][y - 1])