import sys
input = sys.stdin.readline

def compress(arr):
    tmp = sorted(set(arr))
    index = dict(zip(tmp, range(len(tmp))))
    return [index[i] for i in arr]


m, n = map(int, input().split())
arr = [compress(list(map(int, input().split()))) for _ in range(m)]
answer = 0

for i in range(m - 1):
    for j in range(i + 1, m):
        if arr[i] == arr[j]:
            answer += 1

print(answer)