# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    o = 0
    
    for i in input().rstrip():
        o += 1 if i == '(' else -1
        if o < 0: break

    print("YES" if not o else "NO")
