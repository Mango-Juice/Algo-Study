# https://www.acmicpc.net/problem/1799

# ===== 라이브러리 ===== #
import sys

# ===== 변수/상수 ===== #
input = sys.stdin.readline

# ===== 함수 ===== #
def can_put(current_arr: list, x: int, y: int) -> bool:
    if current_arr[x][y] == 0: return False
    
    for i in range(1, x + 1):
        if 0 <= x - i:
            if 0 <= y - i and current_arr[x - i][y - i] == 2: return False
            if y + i < n and current_arr[x - i][y + i] == 2: return False

    return True
    
def dfs(current_arr: list, x: int, y: int) -> int:
    nextx, nexty = x, y + 2

    if nexty >= n:
        nextx += 1
        if n % 2 == 0:
            nexty = 1 - (nexty % n)
        else:
            nexty = nexty % n
        
    available = can_put(current_arr, x, y)

    if nextx == n:
        return int(available)
    
    if current_arr[x][y] == 0 or not available:
        return dfs(current_arr, nextx, nexty)

    result = 0
    current_arr[x][y] = 2
    a = dfs(current_arr, nextx, nexty) + 1
    current_arr[x][y] = 1
    b = dfs(current_arr, nextx, nexty)
    
    return max(a, b)
    
# ===== 입력/초기화 ===== #
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# ===== 출력 ===== #
answer = dfs(arr, 0, 0)
if n > 1: answer += dfs(arr, 0, 1)
print(answer)
