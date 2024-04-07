# https://www.acmicpc.net/problem/16724

# ===== 라이브러리 ===== #
from collections import Counter
import sys

# ===== 변수/상수 ===== #
input = sys.stdin.readline
LEFT, RIGHT, UP, DOWN = 'L', 'R', 'U', 'D'
dx = { 'L' : 0, 'R' : 0, 'U' : -1, 'D' : 1 }
dy = { 'L' : -1, 'R' : 1, 'U' : 0, 'D' : 0 }

# ===== 함수 ===== #
def find(target: int) -> int:
    if tree[target] == target: return target
    tree[target] = find(tree[target])
    return tree[target]

def union(u: int, v: int) -> None:
    u = find(u)
    v = find(v)
    if u != v: tree[u] = v

def xy_to_tree(x: int, y: int) -> int:
    return x * m + y

def union_area(x: int, y: int, c: str) -> None:
    tx, ty = x + dx[c], y + dy[c]
    if 0 <= tx < n and 0 <= ty < m:
        union(xy_to_tree(x, y), xy_to_tree(tx, ty))

# ===== 입력/초기화 ===== #
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
tree = [i for i in range(n * m)]

# ===== 메인 ===== #
for i in range(n):
    for j in range(m):
        union_area(i, j, arr[i][j])

for i in range(n * m):
    tree[i] = find(tree[i])
            
# ===== 출력 ===== #
print(len(Counter(tree)))
