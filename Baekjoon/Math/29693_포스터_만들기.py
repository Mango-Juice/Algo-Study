import sys
import math

input = sys.stdin.readline

y, x = map(int, input().split())
# 1. 테두리는 모두 B다.
# 2. 한쪽이 B면 다른 쪽도 B로 처리한다.
# 3. 노랑을 넣어 나눠지는지 체크.

arr = [list(input().rstrip()) for _ in range(y)]

ridx = 0
while ridx < y:
    if ridx == 0 or ridx == y - 1:
        arr[ridx] = ["B"] * x
        ridx += 1
        continue
    
    cidx = 0
    while cidx < (x / 2):
        if cidx == 0:
            arr[ridx][cidx] = "B"
            cidx += 1
            continue
        
        if arr[ridx][cidx] == "B":
            arr[ridx][x-cidx-1] = "B"
        elif arr[ridx][x-cidx-1] == "B":
            arr[ridx][cidx] = "B"
        cidx += 1
    ridx += 1

cidxl = math.floor((x-1)/2)
cidxr = math.ceil((x-1)/2)
fail = True
ridx = 0
while ridx < y:
    if arr[ridx][cidxl] == "X" and arr[ridx][cidxr] == "X" and arr[ridx][cidxl - 1] == "X" and arr[ridx][cidxr + 1] == "X":
        arr[ridx][cidxl] = "Y"
        arr[ridx][cidxr] = "Y"
        arr[ridx][cidxl - 1] = "W"
        arr[ridx][cidxr + 1] = "W"
        fail = False
        break
    ridx += 1

if fail:
    print("NO")
else:
    print("YES")
    for row in arr:
        print(*map(lambda x : "B" if x == "X" else x,row), sep="")
