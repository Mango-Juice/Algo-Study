import sys
input = sys.stdin.readline

N = int(input())
pos = []
speed = []

def get_l(t):
    minx = miny = float('inf')
    maxx = maxy = -float('inf')
    
    for i in range(N):
        x, y = pos[i][0] + speed[i][0] * t, pos[i][1] + speed[i][1] * t
        minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
    
    return max(maxx - minx, maxy - miny)


for _ in range(N):
    px, py, vx, vy = map(int, input().split())
    pos.append((px, py))
    speed.append((vx, vy))

left, right = 0, 2001
answer = float('inf')
for _ in range(1000):
    p1 = left + (right - left) / 3
    p2 = right - (right - left) / 3
    
    l1 = get_l(p1)
    l2 = get_l(p2)
    answer = min(answer, l1, l2)
    
    if l1 > l2:
        left = p1
    else:
        right = p2

print(answer)