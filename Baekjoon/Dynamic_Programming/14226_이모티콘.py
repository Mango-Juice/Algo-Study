# https://www.acmicpc.net/problem/14226

from collections import deque

MAX = 10000
S = int(input())
arr = [[MAX for _ in range(S + 1)] for _ in range(S + 1)]
arr[1][0] = 0
answer = -1

q = deque()
q.append((1,0))

while q:
    now, clip = q.popleft()
    
    if arr[now][now] == MAX: # 복사
        arr[now][now] = arr[now][clip] + 1
        q.append((now, now))

    if now + clip <= S and arr[now + clip][clip] == MAX: # 붙여넣기
        arr[now + clip][clip] = arr[now][clip] + 1
        q.append((now + clip, clip))

    if now > 0 and arr[now - 1][clip] == MAX: # 삭제
        arr[now - 1][clip] = arr[now][clip] + 1
        q.append((now - 1, clip))

print(min(arr[S]))
