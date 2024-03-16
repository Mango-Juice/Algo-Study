# https://codeforces.com/contest/1948/problem/A

import sys
input = sys.stdin.readline

alphas = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print("YES")
        answer = ""
        for i in range(n // 2):
            answer += (alphas[i] * 2)
        print(answer)
    else:
        print("NO")