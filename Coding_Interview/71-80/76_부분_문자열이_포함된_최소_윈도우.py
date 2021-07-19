#부분 문자열이 포함된 최소 윈도우
#https://leetcode.com/problems/minimum-window-substring

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        miss = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            miss -= need[char] > 0
            need[char] -= 1
            
            if miss == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or (right - left <= end - start):
                    start, end = left, right
                    need[s[left]] += 1
                    miss += 1
                    left += 1
                    
        return s[start:end]
