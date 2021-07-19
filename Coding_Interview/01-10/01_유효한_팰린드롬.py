#유효한 팰린드롬
#https://leetcode.com/problems/valid-palindrome

import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = collections.deque([]) #리스트보다 빠르게 사용하기 위해 데크(deque) 사용
        
        for i in s:
            if i.isalnum(): #알파벳이거나 숫자라면
                new_s.append(i.lower()) 
                
        while len(new_s) > 1: 
            if new_s.popleft() != new_s.pop(): 
                return False
            
        return True
