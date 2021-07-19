# https://www.acmicpc.net/problem/1032

import sys

n = int(sys.stdin.readline())
now = []

for _ in range(n):
    if not now:
        now = list(sys.stdin.readline().rstrip())
    else:
        inp = sys.stdin.readline().rstrip()
        
        for i in range(len(now)):
            if now[i] != inp[i]:
                now[i] = "?"

print(''.join(now))
