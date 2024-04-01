import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(n):
    students = list(map(int, input().split()))
    for stat in students:
        arr.append((stat, i))

arr.sort()
counter = {arr[0][1]: 1}
l = r = 0
answer = float("inf")

while r < n * m:
    if len(counter) == n:
        answer = min(answer, arr[r][0] - arr[l][0])
        if counter[arr[l][1]] == 1:
            del counter[arr[l][1]]
        else:
            counter[arr[l][1]] -= 1
        l += 1
    else:
        r += 1
        if r < n * m:
            if arr[r][1] in counter:
                counter[arr[r][1]] += 1
            else:
                counter[arr[r][1]] = 1

print(answer)