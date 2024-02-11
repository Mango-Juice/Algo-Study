import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
fa = sum(arr, [])
minimum, maximum = min(fa), max(fa)
answer = [float('inf'), 0]

for height in range(minimum, maximum + 1):
    total = 0
    count = b
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] < height:
                total += (height - arr[i][j])
                count -= (height - arr[i][j])
            else:
                total += (arr[i][j] - height) * 2
                count += (arr[i][j] - height)
    
    if count < 0: break
    if total <= answer[0]:
        answer = (total, height)

print(*answer)