#https://www.acmicpc.net/problem/2960

n, k = list(map(int, input().split()))
numbers: List[int] = [i + 2 for i in range(n - 1)]
now_num: int = 2
now_count: int = 1

while True:
    if len(numbers) == n - k:
        print(now_num * now_count)
        break

    numbers.remove(now_num * now_count)
    while (not now_num * now_count in numbers) and now_num * now_count <= n:
        now_count += 1
    
    if now_num * now_count > n:
        now_count = 1
        now_num = numbers[0]
    
