from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
ai = tuple(map(int, input().split()))
dq = deque()

for i, a in enumerate(ai):
    if dq and dq[0][0] + l == i:
        dq.popleft()
        
    while dq and dq[-1][1] > a:
        dq.pop()
    
    dq.append((i, a))
    print(dq[0][1], end=' ')