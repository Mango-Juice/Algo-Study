#https://www.acmicpc.net/problem/1655

import heapq
import sys

n = int(sys.stdin.readline())
maxh = []
minh = []
center = -99999

for _ in range(n):
    num = int(sys.stdin.readline())

    if center == -99999:
        center = num
    elif num > center:
        heapq.heappush(minh, num)
    else:
        heapq.heappush(maxh, -num)

    while not (0 <= len(minh) - len(maxh) <= 1):
        if len(minh) < len(maxh):
            heapq.heappush(minh, center)
            center = -heapq.heappop(maxh)
        else:
            heapq.heappush(maxh, -center)
            center = heapq.heappop(minh)
            
    print(center)
