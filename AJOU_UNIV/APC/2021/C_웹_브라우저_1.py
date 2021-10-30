# C

from collections import deque
import sys
input = sys.stdin.readline

N, Q, C = map(int, input().split())
cache = [0] + list(map(int, input().split()))
back, front, now = deque(), deque(), -1
sumation = 0

for _ in range(Q):
    command = input()
    if command[0] == 'B':
        if back:
            front.append(now)
            now = back.pop()

    elif command[0] == 'F':
        if front:
            back.append(now)
            now = front.pop()

    elif command[0] == 'A':
        while front: sumation -= cache[front.pop()]
        if now != -1: back.append(now)
        now = int(command[2:])
        sumation += cache[now]
        while sumation > C and back: sumation -= cache[back.popleft()]

    else:
        last = -1
        new_back = []
        
        while back:
            t = back.pop()
            if last != t:
                new_back.append(t)
                last = t
            else:
                sumation -= cache[t]
                
        new_back.reverse()
        back = deque(new_back)

    #print(now, front, back, sumation)

print(now)
if not back: print(-1)
else:
    while back:
        print(back.pop(), end = ' ' if back else '')
    print()

if not front: print(-1)
else:
    while front:
        print(front.pop(), end = ' ' if front else '')
