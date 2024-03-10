import sys, bisect
input = sys.stdin.readline

def getArea(a, b, c):
    return abs(a[0] * b[1] - b[0] * a[1] + b[0] * c[1] - c[0] * b[1] + c[0] * a[1] - a[0] * c[1]) / 2


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

areas = [0]
area = 0

for i in range(2, n):
    area += getArea(points[0], points[i - 1], points[i])
    areas.append(area)

half = area / 2
target = bisect.bisect_left(areas, half)
rate = (areas[target] - half) / (areas[target] - areas[target - 1])

print(areas)
print("YES")
print(f"1 {0:.20f}")
print(f"{target + 1} {rate:.20f}")