import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
n, m = map(int, input().split())
arr = [list(map(lambda x: int(x) if x.isdigit() else -1, input().rstrip())) for _ in range(n)]
dp = [[None for _ in range(m)] for _ in range(n)]

def dfs(r, c):
    if dp[r][c] is not None:
        return dp[r][c]
    
    result = 0
    dp[r][c] = float("inf")
    for dr, dc in directions:
        nr, nc = r + dr * arr[r][c], c + dc * arr[r][c]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] < 0: continue
        if dp[nr][nc] == float("inf"): 
            result = float("inf")
            break
        result = max(result, dfs(nr, nc))
    dp[r][c] = result + 1
    
    return dp[r][c]


res = dfs(0, 0)
print(-1 if res == float("inf") else res)