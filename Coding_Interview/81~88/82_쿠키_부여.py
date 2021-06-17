#쿠키 부여
#https://leetcode.com/problems/assign-cookies

from collections import deque

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gq, sq = deque(sorted(g)), deque(sorted(s))
        gnow, snow = gq.popleft(), sq.popleft() if sq else None
        count = 0
        
        while gnow and snow:
            if gnow <= snow:
                count += 1
                gnow = gq.popleft() if gq else None
            snow = sq.popleft() if sq else None

        return count
