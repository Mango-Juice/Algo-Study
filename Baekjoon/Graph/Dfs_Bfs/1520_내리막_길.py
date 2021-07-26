# https://www.acmicpc.net/problem/1520
# DFS

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def dfs(a, b):
    if dp[a][b] > -1:
        return dp[a][b]

    result = 0

    for da, db in DIRECTIONS:
        if m > a + da >= 0 and n > b + db >= 0 and arr[a + da][b + db] < arr[a][b]:
            result += dfs(a + da, b + db)

    dp[a][b] = result
    return result
    

m, n = map(int, input().split())

arr = []
dp = [[-1 for _ in range(n)] for _ in range(m)]
dp[m - 1][n - 1] = 1

for i in range(m):
    arr.append(list(map(int, input().split())))

print(dfs(0, 0))
