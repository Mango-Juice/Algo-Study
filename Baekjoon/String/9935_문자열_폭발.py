# https://www.acmicpc.net/problem/9935

target = input()
explode = input()

last = explode[-1]
arr = []
l = len(explode)

for c in target:
    arr.append(c)
    if c == last and ''.join(arr[-l:]) == explode:
        del arr[-l:]

print(''.join(arr) if arr else "FRULA")
