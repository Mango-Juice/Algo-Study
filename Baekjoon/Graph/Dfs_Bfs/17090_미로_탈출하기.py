import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def dfs(r, c):
    if dp[r][c] != None:
        return dp[r][c]
    
    if visited[r][c]:
        dp[r][c] = False
        return dp[r][c]
    
    visited[r][c] = True
    
    dr, dc = directions[arr[r][c]]
    nr, nc = r + dr, c + dc
    
    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        dp[r][c] = True
        return dp[r][c]
    
    dp[r][c] = dfs(nr, nc)
    return dp[r][c]


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dp = [[None] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        answer += dfs(i, j)

print(answer)