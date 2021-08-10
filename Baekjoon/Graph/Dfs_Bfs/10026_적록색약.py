# https://www.acmicpc.net/problem/10026

# ===== 라이브러리 ===== #
import sys
sys.setrecursionlimit(10001)


# ===== 전역 상수/변수 ===== #
input = sys.stdin.readline
c_to_n = {'R': 0, 'G': 1, 'B': 2}
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
arr = []
answer = [0, 0]


# ===== 함수 ===== #
def dfs(a, b):
    visited[a][b] = True
    
    for da, db in directions:
        na, nb = a + da, b + db
        
        if na >= 0 and na < n and nb >= 0 and nb < n and arr[na][nb] == arr[a][b] and not visited[na][nb]:
            dfs(na, nb)
            

# ===== 입력 ===== #
n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr.append(list(map(lambda x : c_to_n[x], input().rstrip())))


# ===== 메인 ===== #
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            answer[0] += 1

for i in range(n):
    for j in range(n):
        visited[i][j] = False
        if arr[i][j] == 0: arr[i][j] = 1

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            answer[1] += 1
            
        
# ===== 출력 ===== #
print(answer[0], answer[1])
