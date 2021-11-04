# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)
answer = 0

l, r = 0, n - 1
while l < r:
    if abs(arr[l]) >= abs(arr[r]):
        hap, gop = arr[l] + arr[l + 1], arr[l] * arr[l + 1]
        if gop > hap:
            answer += gop
            l += 2
        else:
            answer += arr[l]
            l += 1
        
    else:
        hap, gop = arr[r - 1] + arr[r], arr[r - 1] * arr[r]
        if gop > hap:
            answer += gop
            r -= 2
        else:
            answer += arr[r]
            r -= 1

if r == l: answer += arr[r]

print(answer)
