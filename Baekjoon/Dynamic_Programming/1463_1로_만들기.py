# https://www.acmicpc.net/problem/1463

s = [-1]*1000001

def cal(x):
    #print(x)
    if x == 1:
        return 0
    elif s[x] != -1:
        return s[x]
    else:
        result = 100000
        
        if x % 3 == 0:
            result = min(result, cal(x//3) + 1)
        if x % 2 == 0:
            result = min(result, cal(x//2) + 1)
        result = min(result, cal(x-1) + 1)
            
        s[x] = result
        return result
    
n = int(input())
try:
    print(cal(n))
except:
    for i in range(2,n,500):
        cal(i)
    print(cal(n))
