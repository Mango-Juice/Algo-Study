import sys
from collections import deque
input = sys.stdin.readline

n, d = map(int, input().split())
k = list(map(int, input().split()))

dq = deque([(k[0], 0)])
answer = -float('inf')
for i in range(1, n):
    now = max(dq[0][0] + k[i], k[i])
    while dq and dq[-1][0] <= now: dq.pop()
    dq.append((now, i))
    answer = max(answer, dq[0][0])
    while dq[0][1] <= i - d: dq.popleft()

print(answer)