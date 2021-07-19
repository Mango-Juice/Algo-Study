# https://www.acmicpc.net/problem/2467

n = int(input())
arr = list(map(int, input().split()))
min_abs = 10 ** 9 * 2
answer = (-1, -1)

left, right = 0, len(arr) - 1

while left < right:
    cal = arr[left] + arr[right]
    
    if abs(cal) < min_abs:
        min_abs = abs(cal)
        answer = (arr[left], arr[right])
        
        if min_abs == 0:
            break

    if cal > 0:
        right -= 1
    else:
        left += 1

print(answer[0], answer[1])
