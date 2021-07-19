#https://www.acmicpc.net/problem/1149

n = int(input())

red = []
green = []
blue = []
rdp = {}
gdp = {}
bdp = {}


def rdfs(idx):
    if idx in rdp:
        return rdp[idx]
    elif idx == n - 1:
        return red[idx]
    v = red[idx] + min(gdfs(idx + 1), bdfs(idx + 1))
    rdp[idx] = v
    return v

def gdfs(idx):
    if idx in gdp:
        return gdp[idx]
    elif idx == n - 1:
        return green[idx]
    v = green[idx] + min(rdfs(idx + 1), bdfs(idx + 1))
    gdp[idx] = v
    return v

def bdfs(idx):
    if idx in bdp:
        return bdp[idx]
    elif idx == n - 1:
        return blue[idx]
    v = blue[idx] + min(rdfs(idx + 1), gdfs(idx + 1))
    bdp[idx] = v
    return v


for _ in range(n):
    nums = input().split()
    red.append(int(nums[0]))
    green.append(int(nums[1]))
    blue.append(int(nums[2]))

print(min(rdfs(0), gdfs(0), bdfs(0)))
