import sys
from collections import deque
input = sys.stdin.readline


# 상수
OUTER_BLANK = -1
INNER_BLANK = 0
CHEEZE = 1
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


# 변수
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cheezes = []
answer = 0


# 함수
def check_in_four_directions(row, col, condition):
    result = []
    
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
         
        if 0 <= r < n and 0 <= c < m and condition(r, c):
            result.append((r, c))
    
    return result


def outer_blank_to_inner_black(row, col):
    queue = deque([(row, col)])
    arr[row][col] = OUTER_BLANK
        
    while queue:
        tr, tc = queue.popleft()
        
        targets = check_in_four_directions(
            tr, 
            tc, 
            lambda r, c: arr[r][c] == INNER_BLANK,
        )
        
        for target in targets:
            arr[target[0]][target[1]] = OUTER_BLANK
            queue.append(target)
    


# 치즈 분리
for i in range(n):
    for j in range(m):
        if arr[i][j] == CHEEZE:
            cheezes.append((i, j))

# 공기 분리     
outer_blank_to_inner_black(0, 0)

# 치즈 녹이기
while cheezes:
    targets = []
    answer += 1
    
    for row, col in cheezes:
        blanks = check_in_four_directions(
            row, 
            col, 
            lambda r, c: arr[r][c] == OUTER_BLANK,
        )
        
        if len(blanks) >= 2:
            targets.append((row, col))
    
    for row, col in targets:
        cheezes.remove((row, col))
        outer_blank_to_inner_black(row, col)

# 결과 출력
print(answer)