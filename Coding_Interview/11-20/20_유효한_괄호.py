#유효한 괄호
#https://leetcode.com/problems/valid-parentheses

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        check = deque()
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['}
        
        for c in s:
            if not c in table:
                check.append(c)
            elif not check or table[c] != check.pop():
                return False
        
        return len(check) == 0
