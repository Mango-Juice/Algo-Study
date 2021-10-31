# https://www.acmicpc.net/problem/2502

f1 = [0, 1, 0, 1, 1] + [0] * 50
f2 = [0, 0, 1, 1, 2] + [0] * 50

for i in range(3, 51):
    f1[i] = f1[i - 1] + f1[i - 2]
    f2[i] = f2[i - 1] + f2[i - 2]

D, K = map(int, input().split())

for a in range(1, 1 + K // f1[D]):
    if (K - f1[D] * a) % f2[D] == 0:
        print(a, (K - f1[D] * a) // f2[D], sep = '\n')
        break
