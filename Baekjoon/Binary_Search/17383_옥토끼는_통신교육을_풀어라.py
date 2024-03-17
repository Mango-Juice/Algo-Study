import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = arr[0], arr[-1]
while l <= r:
    mid = (l + r) // 2
    cover = sum([2 - math.ceil(v / mid) for v in arr])
    
    if cover > 0:
        r = mid - 1
    else:
        l = mid + 1

print(l)