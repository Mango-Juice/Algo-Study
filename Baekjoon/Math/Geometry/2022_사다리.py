x, y, c = map(float, input().split())
gc = float('inf')

l, r = 0, min(x, y)
while abs(c - gc) > 0.0001:
    mid = (l + r) / 2
    h1, h2 = (x ** 2 - mid ** 2) ** 0.5, (y ** 2 - mid ** 2) ** 0.5
    gc = (h1 * h2) / (h1 + h2)
    
    if gc > c:
        l = mid
    else:
        r = mid

print((l + r) / 2)