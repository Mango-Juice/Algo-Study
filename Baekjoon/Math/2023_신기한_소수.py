import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(count, value):
    if count == n:
        print(value)
        return
    
    now = value * 10
    for i in range(10):
        if is_prime(now + i):
            solution(count + 1, now + i)


n = int(input())
solution(0, 0)