# https://www.acmicpc.net/problem/2491
# DP...?

n = int(input())
arr = tuple(map(int, input().split()))
inc = dec = ans = 1
last = arr[0]

for i in range(1, n):
    if arr[i] == last:
        inc += 1
        dec += 1
        ans = max([ans, inc, dec])

    elif arr[i] > last:
        inc += 1
        dec = 1
        ans = max(ans, inc)

    else:
        inc = 1
        dec += 1
        ans = max(ans, dec)

    last = arr[i]

print(ans)
