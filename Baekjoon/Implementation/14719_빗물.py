# https://www.acmicpc.net/problem/14719

input()
height = list(map(int, input().split()))

v = 0
left, right = 0, len(height)-1
lmax, rmax = 0, 0
        
while left < right:
    lmax = max(lmax, height[left])
    rmax = max(rmax, height[right])
            
    if lmax <= rmax:
        v += lmax - height[left]
        left += 1
    else:
        v += rmax - height[right]
        right -= 1
                
print(v)
