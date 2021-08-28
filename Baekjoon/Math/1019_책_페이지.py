# https://www.acmicpc.net/problem/1019

def get_answer(n: int, point: int) -> None:
    while n > 0:
        answer[n % 10] += point
        n //= 10

n = int(input())
answer = [0] * 10
start = point = 1

while start <= n:
    while n % 10 != 9 and start <= n:
        get_answer(n, point)
        n -= 1

    if n < start:
        break

    while start % 10 != 0 and start <= n:
        get_answer(start, point)
        start += 1

    start //= 10
    n //= 10

    for i in range(10):
        answer[i] += (n - start + 1) * point

    point *= 10

print(*answer)
