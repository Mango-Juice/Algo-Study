# https://www.acmicpc.net/problem/9663

# ===== 라이브러리 ===== #
import sys

# ===== 변수/상수 ===== #
input = sys.stdin.readline

# ===== 함수 ===== #
def find(target: int):
    global count

    if target == n:
        count += 1
        return

    for i in range(n):
        flag = True

        for j in range(target):
            if arr[j] == i or abs(target - j) == abs(i - arr[j]):
                flag = False
                break

        if flag:
            arr[target] = i
            find(target + 1)
    
# ===== 입력/초기화 ===== #
n = int(input())
arr = [0] * 15
count = 0

# ===== 출력 ===== #
find(0)
print(count)
