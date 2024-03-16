# https://codeforces.com/contest/1948/problem/B

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    last = -float("inf")
    posible = True
    for i in range(n):
        if a[i] < 10:
            if a[i] < last:
                posible = False
                break
            last = a[i]
        else:
            front, back = divmod(a[i], 10)
            if front <= back and front >= last:
                last = back
            else:
                if a[i] < last:
                    posible = False
                    break
                last = a[i]
    
    print("YES" if posible else "NO")