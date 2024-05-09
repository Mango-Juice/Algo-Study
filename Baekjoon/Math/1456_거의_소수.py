import math

a, b = map(int, input().split())
nb = int(b ** 0.5) + 1

era = [True] * nb
era[0] = era[1] = False

for i in range(2, int(nb ** 0.5) + 1):
    if era[i]:
        for j in range(i * 2, nb, i):
            era[j] = False

answer = 0
for i in range(2, nb):
    if era[i]:
        j = max(2, math.ceil(math.log(a, i)))
        while i ** j <= b:
            answer += 1
            j += 1

print(answer)