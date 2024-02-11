import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    answer = [0] * 10000
    q = deque([a])
    answer[a] = ""
    
    while q:
        value = q.popleft()
        
        # D
        d_value = (value * 2) % 10000
        if answer[d_value] == 0:
            answer[d_value] = answer[value] + "D"
            if d_value == b:
                print(answer[d_value])
                break
            q.append(d_value)
        
        # S
        s_value = value - 1
        if answer[s_value] == 0:
            if s_value < 0: s_value = 9999
            answer[s_value] = answer[value] + "S"
            if s_value == b:
                print(answer[s_value])
                break
            q.append(s_value)
        
        # L
        div, mod = value // 1000, value % 1000
        l_value = mod * 10 + div
        if answer[l_value] == 0:
            answer[l_value] = answer[value] + "L"
            if l_value == b:
                print(answer[l_value])
                break
            q.append(l_value)
        
        # R
        div, mod = value // 10, value % 10
        r_value = mod * 1000 + div
        if answer[r_value] == 0:
            answer[r_value] = answer[value] + "R"
            if r_value == b:
                print(answer[r_value])
                break
            q.append(r_value)