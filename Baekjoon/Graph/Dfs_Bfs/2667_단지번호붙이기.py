# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
answer = []

def dfs(r, c):
    result = 1
    
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N or (not arr[nr][nc]): continue
        arr[nr][nc] = False
        result += dfs(nr, nc)

    return result

for i in range(N):
    for j in range(N):
        if not arr[i][j]: continue
        arr[i][j] = False
        answer.append(dfs(i, j))

print(len(answer))
print(*sorted(answer), sep = '\n')
