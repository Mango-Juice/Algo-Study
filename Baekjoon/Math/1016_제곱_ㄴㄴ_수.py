import sys, math
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
pow_number = defaultdict(lambda: True)

for i in range(2, int(math.sqrt(m)) + 1):
    target = i * i
    start = (n // target) * target
    for j in range(start, m + 1, target):
        pow_number[j] = False

count = 0
for i in range(n, m + 1):
    if pow_number[i]:
        count += 1

print(count)