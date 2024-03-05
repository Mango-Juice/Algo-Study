import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
v = list(map(int, input().split()))

v.sort()
rng = n - k - 1

answer = float('inf')
dq = deque()

for i in range(1, n):
    while dq and dq[-1][0] >= v[i] - v[i - 1]: dq.pop()
    dq.append((v[i] - v[i - 1], i))
    while dq and dq[0][1] <= i - rng: dq.popleft()
    
    if i >= rng:
        answer = min(answer, dq[0][0] + v[i] - v[i - rng])

print(answer)