# https://www.acmicpc.net/problem/5430

from collections import deque

t = int(input())

for _ in range(t):
    command = input()
    n = int(input())
    
    if n:
        dq = deque(map(int, input()[1:-1].split(',')))
    else:
        dq = []
        input()
        
    reverse = False
    error = False

    for i in command:
        if i == 'R':
            reverse ^= True
        elif len(dq) == 0:
            error = True
            break
        elif reverse:
            dq.pop()
        else:
            dq.popleft()

    if error:
        print("error")
    elif reverse:
        print(str(list(dq)[::-1]).replace(' ', ''))
    else:
        print(str(list(dq)).replace(' ', ''))
