# https://www.acmicpc.net/problem/1756

#=== Libraries ===#
import sys


#=== Constants and Functions ===#
input = sys.stdin.readline


def bisect(start: int, finish: int, target: int) -> int:
    while start < finish:
        mid = (start + finish) // 2

        if new_width[mid] < target:
            finish = mid
        else:
            start = mid + 1

    return finish


#=== Inputs ===#
D, N = map(int, input().split())
width = list(map(int, input().split()))
pizza = list(map(int, input().split()))


#=== Make New Arr ===#
new_width = []
minimum = float('inf')

for i in width:
    minimum = min(minimum, i)
    new_width.append(minimum)


#=== Put Pizzas ===#
last = D
for i in pizza:
    last = bisect(0, last, i) - 1

    if last < 0:
        break


#=== Print ===#
print(last + 1)
