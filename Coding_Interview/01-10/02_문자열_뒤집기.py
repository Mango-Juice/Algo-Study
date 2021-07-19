#문자열 뒤집기
#https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        #OR s[:] = s[::-1]
