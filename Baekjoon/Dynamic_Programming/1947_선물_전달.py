n = int(input())

if n < 2:
    print(0)
    exit()

llast, last = 0, 1

for i in range(2, n):
    llast, last = last, (i * (llast + last)) % 1000000000

print(last)