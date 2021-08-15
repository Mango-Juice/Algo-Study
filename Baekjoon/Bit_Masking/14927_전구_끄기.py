# https://www.acmicpc.net/problem/14927

import sys
input = sys.stdin.readline

def push(x: int, y: int, arr: list) -> None:
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)):
        if 0 <= x + dx < n and 0 <= y + dy < n:
            arr[x + dx] ^= 1 << (y + dy)
    
def find_answer(row: int, arr: list, result: int) -> None:
    global answer

    if row == n:
        flag = True
        
        for y in range(n):
            if arr[row - 1] & 1 << y == 1 << y:
                flag = False
                break

        if flag: answer = min(answer, result)
        return

    cnt = 0
    
    for y in range(n):
        if arr[row - 1] & 1 << y == 1 << y:
            cnt += 1
            push(row, y, arr)

    find_answer(row + 1, arr, result + cnt)

def solution(count: int, arr: list, result: int) -> None:
    if count == n:
        find_answer(1, arr.copy(), result)
        return
    
    solution(count + 1, arr, result)
    new_arr = arr.copy()
    push(0, count, new_arr)
    solution(count + 1, new_arr, result + 1)
    

answer = 400
n = int(input())
inp = [int(input().replace(' ', '')[::-1], 2) for _ in range(n)]

solution(0, inp, 0)
print(answer if answer < 400 else -1)
