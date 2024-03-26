import sys
input = sys.stdin.readline

def get_postfix(prefix_target, infix_start, infix_end):
    result = []
    
    infix_target = infix.index(prefix[prefix_target])
    if prefix_target < n - 1 and infix_start < infix_target:
        result += get_postfix(prefix_target + 1, infix_start, infix_target)
    
    next_target = prefix_target + len(result)
    if next_target < n - 1 and infix_target + 1 < infix_end:
        result += get_postfix(next_target + 1, infix_target + 1, infix_end)
    
    return result + [prefix[prefix_target]]


t = int(input())
for _ in range(t):
    n = int(input())
    prefix = list(map(int, input().split()))
    infix = list(map(int, input().split()))
    print(*get_postfix(0, 0, n))