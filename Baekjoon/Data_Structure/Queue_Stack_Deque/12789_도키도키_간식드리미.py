import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = map(int, input().split())

goal = 1
wait = deque()
for i in arr:
    wait.append(i)
    while wait and goal == wait[-1]:
        goal += 1
        wait.pop()

print("Nice" if goal == n + 1 else "Sad")