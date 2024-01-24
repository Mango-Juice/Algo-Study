import sys
input = sys.stdin.readline

n, m, a = map(int, input().split())
s = sorted(list(map(int, input().split())))
nums = range(1, 10 ** 10)

# 초기 실력이 start일 때 가능한 지 판별
def canSuccess(start):
    result = 0
    strength = start
    
    for _ in range(m):
        target = bisect(s, lambda x : x <= strength, 0, n - 1, False)
        
        if target < 0 or target >= n:
            break
        
        result += s[target]
        strength += s[target]
        
    return result >= a


# 이분 탐색
def bisect(data, condition_function, start, end, left = True):
    while start <= end:
        mid = (start + end) // 2
        
        if condition_function(data[mid]) == left:
            end = mid - 1
        else:
            start = mid + 1

    return start if left else end

print(nums[bisect(nums, canSuccess, 0, len(nums) - 1)])