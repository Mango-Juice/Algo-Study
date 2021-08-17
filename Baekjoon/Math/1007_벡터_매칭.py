# https://www.acmicpc.net/problem/1007

from itertools import combinations
import sys
input = sys.stdin.readline

def get_distance(x, y) -> float:
    return (x ** 2 + y ** 2) ** (1 / 2)

def get_sum(l: list) -> list:
    result = [0, 0]

    for x, y in l:
        result[0] += x
        result[1] += y

    return result

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 300000
    x_sum, y_sum = get_sum(arr)

    for lst in list(combinations(arr, n // 2)):
        newx, newy = get_sum(lst)
        answer = min(answer, get_distance(x_sum - newx * 2, y_sum - newy * 2))

    print(answer)
