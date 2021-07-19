# https://www.acmicpc.net/problem/1629

def answer(x, y):
    if y == 1:
        return x % c
    half = answer(x, y // 2)
    if y % 2 == 0:
        return half ** 2 % c
    return half ** 2 * x % c

a, b, c = map(int, input().split())
print(answer(a, b))
