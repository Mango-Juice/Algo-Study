# https://www.acmicpc.net/problem/20149

def ccw(a: tuple, b: tuple, c: tuple) -> int:
    value = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    value -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return 1 if value > 0 else -1 if value < 0 else 0

def print_meeting_point() -> None:
    global x1, y1, x2, y2, x3, y3, x4, y4

    a1 = (y1 - y2) / (x1 - x2) if x1 - x2 != 0 else None
    a2 = (y3 - y4) / (x3 - x4) if x3 - x4 != 0 else None
    flag = True

    if a1 != a2:
        b1 = y1 - a1 * x1 if a1 != None else None
        b2 = y3 - a2 * x3 if a2 != None else None

        if b1 == None:
            ax = x1
            ay = a2 * ax + b2
            
        elif b2 == None:
            ax = x3
            ay = a1 * ax + b1
            
        else:
            ax = -(b1 - b2) / (a1 - a2)
            ay = a1 * ax + b1
        
    else:
        if a > b: x1, x2, y1, y2 = x2, x1, y2, y1
        if c > d: x3, x4, y3, y4 = x4, x3, y4, y3
        
        if a == d and b > c: ax, ay = a
        elif b == c and d > a: ax, ay = b
        else: flag = False

    if flag: print(ax, ay)

answer = 0
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
ab, cd = ccw(a, b, c) * ccw(a, b, d), ccw(c, d, a) * ccw(c, d, b)


if ab == 0 and cd == 0:
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    answer = 1 if c <= b and a <= d else 0
else:
    answer = 1 if ab <= 0 and cd <= 0 else 0

print(answer)

if answer == 1:
    print_meeting_point()
