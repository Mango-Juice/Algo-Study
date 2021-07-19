# https://www.acmicpc.net/problem/11399

n = int(input())
arr = sorted(list(map(int, input().split())))
now_time = answer = 0

for i in range(n):
    now_time += arr[i]
    answer += now_time

print(answer)
