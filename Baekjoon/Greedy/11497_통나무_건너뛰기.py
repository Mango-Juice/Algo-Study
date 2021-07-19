import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = sorted(map(int, sys.stdin.readline().split()), reverse = True)
    answer = [0 for _ in range(n)]
    cha = arr[0] - arr[1]

    for i in range(2, n):
        cha = max(cha, arr[i - 2] - arr[i])

    print(cha)
