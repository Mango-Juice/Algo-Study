# https://www.acmicpc.net/problem/6549

from collections import deque
import sys
input = sys.stdin.readline

while True:
    answer = 0
    stack = deque()
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    
    if n == 0: break

    for i in range(n):
        while stack and arr[i] < arr[stack[0]]:
            height = arr[stack.popleft()]
            length = i
            
            if stack: length = i - stack[0] - 1
            answer = max(answer, length * height)

        stack.appendleft(i)

    while stack:
        height = arr[stack.popleft()]
        length = n

        if stack: length = n - stack[0] - 1
        answer = max(answer, length * height)

    print(answer)
