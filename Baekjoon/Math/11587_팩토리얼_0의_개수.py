n = int(input())

def find_zero(x):
    result = 0
    while x >= 5:
        result += x // 5
        x //= 5
    return result


l, r = 1, n * 5
while l <= r:
    mid = (l + r) // 2
    result = find_zero(mid)
    
    if result < n:
        l = mid + 1
    else:
        r = mid - 1
        answer = mid

print(answer if find_zero(answer) == n else -1)