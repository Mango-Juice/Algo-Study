from collections import deque

inp = input()
stack = deque()

calcs = {"*": 1, "/": 1, "+": 0, "-": 0}
answer = ""

for c in inp:
    if c == "(":
        stack.append(c)
    elif c == ")":
        while stack and stack[-1]!= "(":
            answer += stack.pop()
        stack.pop()
    elif c in calcs:
        while stack and stack[-1] in calcs and calcs[stack[-1]] >= calcs[c]:
            answer += stack.pop()
        stack.append(c)
    else:
        answer += c

while stack:
    answer += stack.pop()

print(answer)