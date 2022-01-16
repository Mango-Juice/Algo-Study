import sys
input = sys.stdin.readline

N, R = map(int, input().split())
print(N + 2 * R - 1)
