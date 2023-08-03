from collections import deque

n = int(input())
dq = deque(enumerate(map(int, input().split())))
ans = []

while dq:
    target = dq.popleft()
    ans.append(target[0] + 1)
    
    if dq:
        if target[1] > 0:
            for _ in range(target[1] - 1):
                dq.append(dq.popleft())
        else:
            for _ in range(-target[1]):
                dq.appendleft(dq.pop())
print(*ans)
