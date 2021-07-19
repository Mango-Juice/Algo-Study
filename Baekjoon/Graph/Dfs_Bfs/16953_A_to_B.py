# https://www.acmicpc.net/problem/16953

from collections import deque

now, target = map(int, input().split())

stack = deque([(now, 1)])
answer = 10 ** 9

while stack:
    num, step = stack.pop()

    if num == target:
        answer = min(answer, step)
        continue

    if num * 2 <= target:
        stack.append((num * 2, step + 1))
    if num * 10 + 1 <= target:
        stack.append((num * 10 + 1, step + 1))

print(-1 if answer == 10 ** 9 else answer)
