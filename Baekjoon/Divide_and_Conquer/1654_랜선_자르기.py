# https://www.acmicpc.net/problem/1654

inp = input().split()
k = int(inp[0])
n = int(inp[1])
lan = []

for i in range(k):
    lan.append(int(input()))

###############################
    
min_ = 1
max_ = max(lan)
target = 0
result = 0

###############################

while max_>=min_:        
    count = 0

    target = (min_ + max_) // 2
    for i in lan:
        count += i // target
        
    if count >= n:
        result = target;
        min_ = target + 1
    else:
        max_ = target - 1

###############################
        
print(result)
