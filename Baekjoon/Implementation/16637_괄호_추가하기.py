import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()

if n == 1:
    print(arr[0])
    exit()

answer = -float('inf')
q = deque([(1, arr[0])])
while q:
    nowi, nowv = q.popleft()
    
    if nowi == n:
        answer = max(answer, nowv)
        continue
    if nowi <= n - 2:
        q.append((nowi + 2, eval(f"{nowv}{arr[nowi]}{arr[nowi+1]}")))
    if nowi <= n - 4:
        q.append((nowi + 4, eval(f"{nowv}{arr[nowi]}({arr[nowi+1:nowi+4]})")))

print(answer)