import sys
input = sys.stdin.readline

N, X = map(int, input().split())
p = list(map(int, input().split()))

print(int(sum(p) % X == 0))