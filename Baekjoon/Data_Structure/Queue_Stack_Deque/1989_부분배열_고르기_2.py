import sys
from collections import deque
input = sys.stdin.readline

def find_answer(now_index):
    minimum = arr[stack.pop()]
    last_index = stack[-1] + 1 if stack else 0
    hap = sums[now_index] - sums[last_index]
    return (minimum * hap, (last_index + 1, now_index))


n = int(input())
arr = list(map(int, input().split()))
sums = [0]

for i in range(n):
    sums.append(sums[i] + arr[i])

stack = deque()
answer = (-1, None)
for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        result = find_answer(i)
        if result[0] > answer[0]:
            answer = result
    stack.append(i)

while stack:
    result = find_answer(n)
    if result[0] > answer[0]:
        answer = result

print(answer[0])
print(*answer[1])