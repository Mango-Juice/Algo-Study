import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(input().strip()) for _ in range(n)]
ctoi = {"W": 0, "B": 1}
answer = float("inf")

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = (i + j + ctoi[arr[i][j]]) % 2
        arr[i][j] += (arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1])

for i in range(8, n + 1):
    for j in range(8, m + 1):
        s = arr[i][j] - arr[i - 8][j] - arr[i][j - 8] + arr[i - 8][j - 8]
        answer = min(answer, s, 64 - s)

print(answer)