# https://www.acmicpc.net/problem/15823

import math, sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
cards = tuple(map(int, sys.stdin.readline().split()))

left, right = 0, n // m
answer = 0

while left <= right:
    mid = left + (right - left) // 2
    q_left = q_right = pack_count = 0
    visited = defaultdict(bool)
    
    for i in range(n):
        if visited[cards[i]]:
            while cards[q_left] != cards[i]:
                visited[cards[q_left]] = False
                q_left += 1
            q_left += 1

        q_right += 1
        visited[cards[i]] = True

        if q_right - q_left >= mid:
            pack_count += 1
            q_left = q_right
            visited = defaultdict(bool)
    
    if pack_count >= m:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)
