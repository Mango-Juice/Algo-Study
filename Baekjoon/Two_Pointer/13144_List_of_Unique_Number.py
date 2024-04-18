import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


l = r = 0
counts = set([arr[0]])
answer = 1

while r < n - 1:
    if arr[r + 1] in counts:
        counts.remove(arr[l])
        l += 1
    else:
        r += 1
        counts.add(arr[r])
        answer += len(counts)

print(answer)