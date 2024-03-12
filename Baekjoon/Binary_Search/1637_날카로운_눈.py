import sys
input = sys.stdin.readline

def get_count(number):
    result = 0
    
    for a, c, b in ops:
        if a <= number:
            result += (min(c, number) - a) // b + 1
    
    return result


n = int(input())
ops = [tuple(map(int, input().split())) for _ in range(n)]

l, r = 1, 2147483647
answer = None
while r >= l:
    mid = (l + r) // 2
    val = get_count(mid)
    
    if val % 2 == 0:
        l = mid + 1
    else:
        answer = mid
        r = mid - 1

if not answer:
    print("NOTHING")
else:
    print(answer)
    print(get_count(answer) - get_count(answer - 1))