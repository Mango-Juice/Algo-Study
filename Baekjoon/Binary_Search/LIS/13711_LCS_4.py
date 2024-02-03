import sys
from bisect import bisect_left
input = sys.stdin.readline

l = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_b = [a.index(x) for x in b]
lis = []

for x in new_b:
    idx = bisect_left(lis, x)
    
    if idx >= len(lis):
        lis.append(x)
    else:
        lis[idx] = x

print(len(lis))
