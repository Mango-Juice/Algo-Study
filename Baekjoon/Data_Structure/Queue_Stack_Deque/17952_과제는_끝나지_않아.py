# https://www.acmicpc.net/problem/17952
# STACK

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = deque()
answer = 0

for _ in range(N):
    inp = input().rstrip()

    if inp != '0':
        inp = tuple(map(int, inp.split()))
        stack.append([inp[2], inp[1]])
    
    if stack:
        stack[-1][0] -= 1
        if stack[-1][0] == 0:
            answer += stack.pop()[1]

print(answer)
