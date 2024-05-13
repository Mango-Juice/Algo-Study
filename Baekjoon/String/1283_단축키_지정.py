import sys
input = sys.stdin.readline

n = int(input())
keys = set(" ")

for _ in range(n):
    inp = input().rstrip()
    is_first = True
    ans = None
    
    for i, v in enumerate(inp):
        if not v.capitalize() in keys:
            if is_first:
                ans = i
                break
            if ans == None:
                ans = i
        
        is_first = (v == " ")
    
    if ans != None:
        keys.add(inp[ans].capitalize())
        print(f"{inp[:ans] if ans > 0 else ''}[{inp[ans]}]{inp[ans + 1:] if ans < len(inp) - 1 else ''}")
    else:
        print(inp)