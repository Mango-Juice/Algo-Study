from collections import deque

n = int(input())
w = list(map(int, input().split()))
answer = 0

dq = deque([(w, 0)])
while dq:
    arr, now = dq.popleft()
    answer = max(answer, now)
    if len(arr) < 3: continue

    for i in range(1, len(arr) - 1):
        energy = now + arr[i - 1] * arr[i + 1]
        target = arr.pop(i)
        dq.append((arr[:], energy))
        arr.insert(i, target)

print(answer)