# https://www.acmicpc.net/problem/1806

##### 입력 #####
n, s = map(int, input().split())
an = list(map(int, input().split()))

##### 투 포인터 ####
answer = 100001
left, right = 0, 0
total = an[0]

while True:

    if total >= s:
        answer = min(answer, right - left + 1)
        total -= an[left]
        left += 1
        
    elif total < s:
        right += 1
        if right >= n:
            break
        total += an[right]

##### 출력 #####
print(answer if answer != 100001 else 0)
