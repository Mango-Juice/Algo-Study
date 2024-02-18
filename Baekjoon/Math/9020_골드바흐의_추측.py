import sys
input = sys.stdin.readline

is_prime = [True] * 10001

for i in range(2, 101):
    if is_prime[i]:
        for j in range(i * 2, 10001, i):
            is_prime[j] = False

for _ in range(int(input())):
    n = int(input())
    for i in range(n//2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break