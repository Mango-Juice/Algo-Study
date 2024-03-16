# https://codeforces.com/contest/1948/problem/D

import sys
input = sys.stdin.readline

def posible(s, l):
    acc = 0
    for i in range(len(s) - l):
        if s[i] == s[i + l] or s[i] == "?" or s[i + l] == "?":
            acc += 1
            if acc == l:
                return True
        else:
            acc = 0
    return False


t = int(input())
for _ in range(t):
    s = input().strip()
    length = len(s)
    
    ans = 0
    l, r = 1, length // 2
    for i in range(length // 2, 0, -1):
        if posible(s, i):
            ans = i * 2
            break
    
    print(ans)