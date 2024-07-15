x, y = map(int, input().split())

while True:
    nx, ny = (x + y) / 2, 2 * x * y / (x + y)
    if nx == x and ny == y:
        print(x, y)
        break
    else:
        x, y = nx, ny