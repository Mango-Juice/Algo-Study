import sys, math
from collections import deque
input = sys.stdin.readline

pmtd = ["+","-","*","/"]

n = int(input())
q = input().strip()
nums = [int(input()) for _ in range(n)]

stack = deque()
for c in q:
    if c in pmtd:
        a, b = stack.pop(), stack.pop()
        stack.append(eval(f"{b}{c}{a}"))
    else:
        stack.append(nums[ord(c) - ord('A')])

answer = math.floor(stack.pop() * 100) / 100
print(f"{answer:.2f}")