import sys
input = sys.stdin.readline

n = int(input())
times = set()
data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))
    times.add(a)
    times.add(b)

times = sorted(times)
index = dict(zip(times, range(len(times))))
value = dict(zip(range(len(times)), times))
data = [(index[i], index[j]) for i, j in data]

line = [0] * len(times)
for i, j in data:
    line[i] += 1
    line[j] -= 1

maximum = -1
f = t = -1
flag = False
for i in range(len(line)):
    line[i] += (line[i - 1] if i > 0 else 0)
    if line[i] == maximum and flag:
        t = i
    elif line[i] > maximum:
        maximum = line[i]
        f = t = i
        flag = True
    else:
        flag = False

print(maximum)
print(value[f], value[t + 1])