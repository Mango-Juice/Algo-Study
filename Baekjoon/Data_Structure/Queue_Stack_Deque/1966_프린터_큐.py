# https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    count = 0

    while q:
        maximum = max(q)
        target = q.popleft()
        m -= 1

        if maximum == target:
            count += 1
            if m < 0:
                print(count)
                break

        else:
            q.append(target)
            if m < 0: m = len(q) - 1
