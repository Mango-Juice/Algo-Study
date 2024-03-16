ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

left, right = 0, 100
answer = float("inf")
while right - left >= 1e-7:
    p1 = (left * 2 + right) / 3
    p2 = (left + right * 2) / 3

    minho1 = (ax + (bx - ax) * (p1 / 100), ay + (by - ay) * (p1 / 100))
    minho2 = (ax + (bx - ax) * (p2 / 100), ay + (by - ay) * (p2 / 100))
    
    kangho1 = (cx + (dx - cx) * (p1 / 100), cy + (dy - cy) * (p1 / 100))
    kangho2 = (cx + (dx - cx) * (p2 / 100), cy + (dy - cy) * (p2 / 100))
    
    d1 = ((minho1[0] - kangho1[0]) ** 2 + (minho1[1] - kangho1[1]) ** 2) ** 0.5
    d2 = ((minho2[0] - kangho2[0]) ** 2 + (minho2[1] - kangho2[1]) ** 2) ** 0.5
    answer = min(answer, d1, d2)
    
    if d1 >= d2:
        left = p1
    else:
        right = p2

print(f"{answer:.10f}")