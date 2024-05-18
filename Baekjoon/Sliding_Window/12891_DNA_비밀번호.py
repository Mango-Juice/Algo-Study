import sys
input = sys.stdin.readline

s, p = map(int, input().split())
string = input().rstrip()
a, c, g, t = map(int, input().split())

na = nc = ng = nt = answer = 0

for i in range(p):
    char = string[i]
    if char == "A": na += 1
    elif char == "C": nc += 1
    elif char == "G": ng += 1
    elif char == "T": nt += 1

if na >= a and nc >= c and ng >= g and nt >= t:
    answer += 1

for i in range(p, s):
    ichar = string[i]
    if ichar == "A": na += 1
    elif ichar == "C": nc += 1
    elif ichar == "G": ng += 1
    elif ichar == "T": nt += 1
    
    ochar = string[i - p]
    if ochar == "A": na -= 1
    elif ochar == "C": nc -= 1
    elif ochar == "G": ng -= 1
    elif ochar == "T": nt -= 1
    
    if na >= a and nc >= c and ng >= g and nt >= t:
        answer += 1

print(answer)