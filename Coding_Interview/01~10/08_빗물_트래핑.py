#빗물 트래핑
#https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
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
                
        return v
