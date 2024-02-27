import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

q = deque([(float('inf'), 0)])
answer = []
for i in range(n):
    while q[-1][0] < arr[i]:
        q.pop()
    answer.append(q[-1][1])
    q.append((arr[i], i + 1))

print(*answer)