import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
is_prime = [True] * (m + 1)
is_prime[1] = False

for i in range(2, int(math.sqrt(m)) + 1):
    if is_prime[i]:
        for j in range(i * 2, m + 1, i):
            is_prime[j] = False

print(*[i for i in range(n, m + 1) if is_prime[i]], sep="\n")