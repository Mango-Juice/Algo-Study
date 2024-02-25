import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

answer = 0
now = defaultdict(int)
now[c] = 1

for i in range(n + k):
    now[sushi[i % n]] += 1
    if i >= k:
        now[sushi[i - k]] -= 1
        if now[sushi[i - k]] == 0: del now[sushi[i - k]]
    answer = max(answer, len(now))

print(answer)