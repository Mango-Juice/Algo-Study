# https://www.acmicpc.net/problem/17371

import sys

input = sys.stdin.readline


def get_distance(a: tuple[int], b: tuple[int]) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
minimum = float('inf')

for i in range(N):
    maximum = -1

    for j in range(N):
        maximum = max(maximum, get_distance(points[i], points[j]))

    if maximum < minimum:
        nearest = i
        minimum = maximum

print(*points[nearest])
