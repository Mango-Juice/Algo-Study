n = int(input())
arr = list(map(int, input().split()))

def solve(d):
    target = [arr[0] + i * d for i in range(n)]
    cha = [abs(arr[i] - target[i]) for i in range(n)]
    return sum(cha)


left, right = 0, arr[-1]
while right - left >= 3:
    p1 = (left * 2 + right) // 3
    p2 = (left + right * 2) // 3

    d1 = solve(p1)
    d2 = solve(p2)

    if d1 >= d2:
        left = p1
    else:
        right = p2

answer = float("inf")
for i in range(left, right + 1):
    answer = min(answer, solve(i))

print(answer)