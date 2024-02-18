import sys
input = sys.stdin.readline

n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
point.sort()

value = [0, 0]
# 값 구하기 (역행)
last_pos = None
for idx, (pos, val) in enumerate(point[::-1]):
    value[1] += val
    if last_pos != None:
        value[1] += (last_pos - pos) * idx
    last_pos = pos

# 값 구하기 (순행)
last_pos = None
for idx, (pos, val) in enumerate(point):
    value[0] += val
    if last_pos != None:
        value[0] += (pos - last_pos) * idx
    last_pos = pos

answer = float('inf')

# 하나씩 빼보기
for idx, (pos, val) in enumerate(point):
    # 순행 계산
    if idx == n - 1:
        answer = min(answer, value[0] - val - (pos - point[n - 2][0]) * idx)
    else:
        answer = min(answer, value[0] - val - (point[n - 1][0] - pos))
        
    # 역행 계산
    if idx == 0:
        answer = min(answer, value[1] - val - (point[1][0] - pos) * (n - idx - 1))
    else:
        answer = min(answer, value[1] - val - (pos - point[0][0]))

print(answer)