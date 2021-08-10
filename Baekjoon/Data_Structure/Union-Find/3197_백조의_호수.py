# https://www.acmicpc.net/problem/3197

# ===== 라이브러리 ===== #
from collections import deque
import sys

sys.setrecursionlimit(100000)


# ===== 전역 상수/변수 ===== #
input = sys.stdin.readline
DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))
q = deque()
baekjo = []
answer = 0


# ===== 함수 ===== #
def find(target: int) -> int:
    if tree[target] == target:
        return target
    
    tree[target] = find(tree[target])
    return tree[target]


def union_with_around(r: int, c: int) -> None:
    flag = False

    for dr, dc in DIRECTIONS:
        newr, newc = r + dr, c + dc

        if newr >= 0 and newr < R and newc >= 0 and newc < C:
            if arr[newr][newc] == '.':
                u = find(r * C + c)
                v = find(newr * C + newc)

                if u != v:
                    if rank[u] < rank[v]: tree[u] = v
                    else:
                        tree[v] = u
                        if rank[u] == rank[v]: rank[u] += 1
                        
            elif arr[newr][newc] == 'X':
                flag = True

    if flag:
        q.append((r, c))
                    


def check_finished() -> bool:
    return find(baekjo[0]) == find(baekjo[1])


def process() -> None:
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in DIRECTIONS:
            newr, newc = r + dr, c + dc

            if newr >= 0 and newr < R and newc >= 0 and newc < C and arr[newr][newc] == 'X':
                arr[newr][newc] = '.'
                union_with_around(newr, newc)


# ===== 입력 ===== #
R, C = map(int, input().split())
arr = []
tree = [i for i in range(C * R)]
rank = [0 for i in range(C * R)]

for i in range(R):
    arr.append(list(input().rstrip()))


# ===== 메인 ===== #
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            baekjo.append(i * C + j)
            arr[i][j] = '.'
            
        if arr[i][j] == '.':
            union_with_around(i, j)

while q:
    if check_finished(): break
    process()
    answer += 1


# ===== 출력 ===== #
print(answer)
