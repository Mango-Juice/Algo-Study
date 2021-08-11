# https://www.acmicpc.net/problem/2143

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

# 입력
t = int(input())
n = int(input())
an = list(map(int, input().split()))
m = int(input())
bm = list(map(int, input().split()))

# 누적 합
for i in range(1, n): an[i] += an[i - 1]
for i in range(1, m): bm[i] += bm[i - 1]

# 경우의 수 구하기
arr = an
brr = bm

for i in range(n - 1):
    for j in range(i + 1, n):
        arr.append(an[j] - an[i])
        
for i in range(m - 1):
    for j in range(i + 1, m):
        brr.append(bm[j] - bm[i])

# 이분탐색
answer = 0
arr.sort()
brr.sort()

for i in arr:
    target = t - i
    answer += bisect_right(brr, target) - bisect_left(brr, target)
            
print(answer)
