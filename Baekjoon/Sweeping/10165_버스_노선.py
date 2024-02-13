# 라인 스위핑 + 환형 처리
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []
answer = set()

for i in range(m):
    a, b = map(int, input().split())
    
    if a > b:
        arr.append((a, b + n, i + 1))
        arr.append((a - n, b, i + 1))
    else:
        arr.append((a, b, i + 1))

arr.sort(key=lambda x: (x[0], -x[1]))
right = arr[0][1]
answer.add(arr[0][2])

for i in range(1, len(arr)):
    a, b, j = arr[i]
    
    if right < b:
        answer.add(j)
        right = b

print(*sorted(answer))