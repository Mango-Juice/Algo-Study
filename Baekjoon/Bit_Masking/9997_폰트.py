# https://www.acmicpc.net/problem/9997

import sys
input = sys.stdin.readline

def choose(now_index, now_bit):
    global answer
    
    new_bit = now_bit | arr[now_index]
    if new_bit == (1 << 26) - 1: answer += 1
    if now_index == N - 1: return

    choose(now_index + 1, now_bit)
    choose(now_index + 1, new_bit)


N = int(input())
arr = []
answer = 0

for _ in range(N):
    bit = 0
    for j in input().rstrip():
        bit |= (1 << ord(j) - 97)
    arr.append(bit)

choose(0, 0)

print(answer)
