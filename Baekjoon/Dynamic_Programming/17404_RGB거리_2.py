# https://www.acmicpc.net/problem/17404

import sys

sys.setrecursionlimit(10**8)

def rdfs(idx, exception):
    v = 0
    if idx in rdp[exception]:
        return rdp[exception][idx]
    elif idx == n - 1:
        v = red[idx]
    elif idx == n - 2:
        if exception == B:
            v = red[idx] + gdfs(idx + 1, exception)
        elif exception == G:
            v = red[idx] + bdfs(idx + 1, exception)
        else:
            v = red[idx] + min(gdfs(idx + 1, exception), bdfs(idx + 1, exception))
    else:
        v = red[idx] + min(gdfs(idx + 1, exception), bdfs(idx + 1, exception))
    rdp[exception][idx] = v
    return v

def gdfs(idx, exception):
    v = 0
    if idx in gdp[exception]:
        return gdp[exception][idx]
    elif idx == n - 1:
        v = green[idx]
    elif idx == n - 2:
        if exception == B:
            v = green[idx] + rdfs(idx + 1, exception)
        elif exception == R:
            v = green[idx] + bdfs(idx + 1, exception)
        else:
            v = green[idx] + min(rdfs(idx + 1, exception), bdfs(idx + 1, exception))
    else:
        v = green[idx] + min(rdfs(idx + 1, exception), bdfs(idx + 1, exception))
    gdp[exception][idx] = v
    return v

def bdfs(idx, exception):
    v = 0
    if idx in bdp[exception]:
        return bdp[exception][idx]
    elif idx == n - 1:
        v = blue[idx]
    elif idx == n - 2:
        if exception == R:
            v = blue[idx] + gdfs(idx + 1, exception)
        elif exception == G:
            v = blue[idx] + rdfs(idx + 1, exception)
        else:
            v = blue[idx] + min(gdfs(idx + 1, exception), rdfs(idx + 1, exception))
    else:
        v = blue[idx] + min(gdfs(idx + 1, exception), rdfs(idx + 1, exception))
    bdp[exception][idx] = v
    return v


n = int(sys.stdin.readline())

red = []
green = []
blue = []
rdp = [{}, {}, {}]
gdp = [{}, {}, {}]
bdp = [{}, {}, {}]

R, G, B = 0, 1, 2

for _ in range(n):
    nums = sys.stdin.readline().split()
    red.append(int(nums[0]))
    green.append(int(nums[1]))
    blue.append(int(nums[2]))

print(min(rdfs(0, R), gdfs(0, G), bdfs(0, B)))
