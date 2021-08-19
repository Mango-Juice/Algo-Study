# https://www.acmicpc.net/problem/2437

n = int(input())
arr = sorted(map(int, input().split()))
s = 0

for i in arr:
    # s(현재 - 1까지의 누적합) + 1 < i(현재 값)이면 s + 1 을 못만듦
    if s + 1 < i: break
    s += i

print(s + 1)
