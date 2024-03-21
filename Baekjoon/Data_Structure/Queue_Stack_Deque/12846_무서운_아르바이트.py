import sys
from collections import deque
input = sys.stdin.readline

def find_answer(now_index):
    pay = arr[stack.pop()]
    day = now_index - (stack[-1] + 1 if stack else 0)
    return pay * day


n = int(input())
if n == 0:
    print(0)
    exit()

arr = list(map(int, input().split()))

stack = deque()
answer = 0
for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        answer = max(answer, find_answer(i))
    stack.append(i)

while stack:
    answer = max(answer, find_answer(n))

print(answer)