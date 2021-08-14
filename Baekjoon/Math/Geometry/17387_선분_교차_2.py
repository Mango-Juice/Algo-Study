# https://www.acmicpc.net/problem/17387

def ccw(a: tuple, b: tuple, c: tuple) -> int:
    value = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    value -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return 1 if value > 0 else -1 if value < 0 else 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
ab, cd = ccw(a, b, c) * ccw(a, b, d), ccw(c, d, a) * ccw(c, d, b)

if ab == 0 and cd == 0:
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    print(1 if c <= b and a <= d else 0)
else:
    print(1 if ab <= 0 and cd <= 0 else 0)
