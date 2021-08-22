# https://www.acmicpc.net/problem/1062

MUST = (0, 2, 8, 13, 19)

def check_answer(now: int) -> None:
    global answer
    result = 0
    
    for i in arr:
        if now & i == i:
            result += 1

    answer = max(answer, result)

def solution(now: int, target: int, count: int) -> None:
    if count == k:
        check_answer(now)
        return
    
    if 26 - target < k - count: return

    solution(now | (1 << target), target + 1, count + 1)
    if not target in MUST: solution(now, target + 1, count)

n, k = map(int, input().split())
arr = []
answer = 0

for _ in range(n):
    now = 0
    for c in input(): now |= 1 << (ord(c) - 97)
    arr.append(now)

if k < 5: print(0)
elif k == 26: print(n)
else:
    solution(0, 0, 0)
    print(answer)
