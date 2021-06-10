#최대 슬라이딩 윈도우
#https://leetcode.com/problems/sliding-window-maximum

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:   
        if k == 0:
            return []
        
        answer = []
        queue = deque()
        left, right = 0, k-1
        
        def add_to_q(i: int) -> None:
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            return
        
        for i in range(k):
            add_to_q(i)
        
        while right < len(nums):
            while True:
                if queue[0] >= left:
                    answer.append(nums[queue[0]])
                    break
                else:
                    queue.popleft()
                    
            left += 1
            right += 1
            
            if right < len(nums):
                add_to_q(right)
            
        return answer
