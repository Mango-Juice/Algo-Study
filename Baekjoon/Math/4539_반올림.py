n = int(input())

for _ in range(n):
    x = int(input())
    
    for i in range(9):
        target = 10 ** (i + 1)
        if x <= target:
            break
        
        if (x % target) // (target // 10) >= 5:
            x += target - (x % target)
        else:
            x -= (x % target)
    
    print(x)