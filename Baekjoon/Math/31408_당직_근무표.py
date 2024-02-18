import sys, math
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
print("NO" if Counter(a).most_common(1)[0][1] > math.ceil(n / 2) else "YES")