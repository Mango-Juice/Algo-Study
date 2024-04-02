import sys
input = sys.stdin.readline

START, FINISH = 0, 1
n = int(input())
arr = []

for _ in range(n):
    x, y, w, h = map(lambda x: int(float(x) * 10) , input().split())
    arr.append((x, y, y + h, START))
    arr.append((x + w, y, y + h, FINISH))

arr.sort()

answer = 0
ys = [(arr[0][1], arr[0][2])]
last_x = arr[0][0]

for i in range(1, n * 2):
    x, y_low, y_high, lt = arr[i]
    
    y = 0
    if ys:
        ys.sort()
        low, high = ys[0]
        for j in range(1, len(ys)):
            l, h = ys[j]
            if l <= high: high = max(high, h)
            else:
                y += high - low
                low, high = l, h
        y += high - low
    
    answer += (x - last_x) * y
    
    if lt == START:
        ys.append((y_low, y_high))
    else:
        ys.remove((y_low, y_high))
    
    last_x = x

if answer % 100 == 0:
    print(answer // 100)
else:
    print(f'{answer / 100:.2f}')