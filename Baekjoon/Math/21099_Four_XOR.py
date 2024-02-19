import sys, math
input = sys.stdin.readline

maximum = math.ceil((1 + math.sqrt(400005))/2)
n = int(input())
numbers = list(map(int, input().split()))

if n > maximum:
    print("Yes")
    exit()

visited = [False] * (2 << 17)
for i in range(n - 1):
    for j in range(i + 1, n):
        xor = numbers[i] ^ numbers[j]
        if visited[xor]:
            print("Yes")
            exit()
        visited[xor] = True

print("No")
