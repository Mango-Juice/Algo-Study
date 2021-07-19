# https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())
arr = []
answer = 0

for i in range(n):
    w, v = map(int, input().split())
    now = []

    for j in range(k + 1):
        if i == 0:
            now.append(v if j >= w else 0)
        elif w > j:
            now.append(arr[i - 1][j])
        else:
            now.append(max(arr[i - 1][j], v + arr[i - 1][j - w]))

    arr.append(now)

print(arr[-1][-1])
