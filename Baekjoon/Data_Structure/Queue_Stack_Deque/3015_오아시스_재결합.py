# https://www.acmicpc.net/problem/3015

from collections import deque
from sys import stdin
input = stdin.readline

answer = 0
stack = deque()

for _ in range(int(input())):
    target = int(input())

    while stack and stack[0][0] < target: answer += stack.popleft()[1]

    if not stack: stack.appendleft((target, 1))
    
    elif stack[0][0] == target: # 같은 키가 연속으로 나오면
        cv, cc = stack.popleft()
        
        answer += cc # 같은 키끼리 쌍을 이룸
        if stack: answer += 1 # 스택에서 가장 큰 사람과 쌍을 이룸

        stack.appendleft((cv, cc + 1)) # 연속 기록
        
    else:
        stack.appendleft((target, 1))
        answer += 1

print(answer)
