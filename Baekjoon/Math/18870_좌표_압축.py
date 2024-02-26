import sys
input = sys.stdin.readline

input()
x = list(map(int, input().split()))
tmp = sorted(set(x))
index = dict(zip(tmp, range(len(tmp))))
print(*[index[i] for i in x])