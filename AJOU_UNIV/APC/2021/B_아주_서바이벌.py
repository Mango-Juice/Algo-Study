# B

import sys
input = sys.stdin.readline

T, N = map(int, input().split())
loc = [1 for _ in range(N + 2)]
item = [[] for _ in range(N + 2)]

boojung = []
banned = set()

for _ in range(T):
    inp = input().split()
    no, player, code, target = int(inp[0]), int(inp[1]), inp[2], int(inp[3])
    
    if inp[2] == 'M':loc[player] = target

    elif inp[2] == 'F':
        item[player].append(target)
        
        if target != loc[player]:
            boojung.append(no)

    elif inp[2] == 'C':
        flag = 0
        target2 = int(inp[4])
        
        if target in item[player]:
            item[player].remove(target)
            flag += 1
        
        if target2 in item[player]:
            item[player].remove(target2)
            flag += 1

        if flag < 2:
            boojung.append(no)
            
    elif loc[player] != loc[target]:
        boojung.append(no)
        banned.add(player)


print(len(boojung))
if boojung:
    boojung.sort()
    print(*boojung)

print(len(banned))
if banned:
    print(*sorted(banned))
