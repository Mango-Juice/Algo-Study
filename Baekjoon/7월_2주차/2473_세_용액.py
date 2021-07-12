#https://www.acmicpc.net/problem/2473

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
    
answer = (-1, -1, -1)
min_abs = 3000000000

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        now_sum = arr[i] + arr[left] + arr[right]
        
        if abs(now_sum) < min_abs:
            min_abs = abs(now_sum)
            answer = (arr[i], arr[left], arr[right])

        if now_sum > 0:
            right -= 1
        elif now_sum < 0:
            left += 1
        else:
            break

print(answer[0], answer[1], answer[2])
