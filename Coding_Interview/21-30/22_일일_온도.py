#일일 온도
#https://leetcode.com/problems/daily-temperatures

from collections import deque

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        before = Deque()
        
        for idx, temp in enumerate(T):
            while before and T[before[-1]] < temp:
                last = before.pop()
                answer[last] = idx - last
            before.append(idx)
            
        return answer
