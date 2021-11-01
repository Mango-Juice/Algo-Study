# https://www.acmicpc.net/problem/23300

from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
back, front, now = deque(), deque(), -1

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
        front = deque()
        if now != -1: back.append(now)
        now = int(command[2:])

    else:
        last = -1
        new_back = []
        
        while back:
            t = back.pop()
            if last != t:
                new_back.append(t)
                last = t
                
        new_back.reverse()
        back = deque(new_back)


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
