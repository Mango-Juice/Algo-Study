import sys
from collections import deque
input = sys.stdin.readline


def ccw(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) > 0


def convex_hull(points):
    answer = deque()
    for point3 in points:
        while len(answer) >= 2:
            point1, point2 = answer[0], answer[1]
            if ccw(point1, point2, point3):
                break
            answer.popleft()
        answer.appendleft(point3)
    return len(answer)


n = int(input())
positions = sorted([list(map(int, input().split())) for _ in range(n)])

ans, rev = convex_hull(positions), convex_hull(positions[::-1])
print(ans + rev - 2)