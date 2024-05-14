import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
ans = []

for _ in range(n):
    i = int(input())
    idx = bisect_left(ans, i)
    if idx == len(ans): ans.append(i)
    else: ans[idx] = i

print(n - len(ans))