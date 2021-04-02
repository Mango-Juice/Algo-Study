#가장 긴 팰린드롬 부분 문자열
#https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            to_return: str = ''
            
            while left >= 0 and right <= len(s):

                if s[left:right+1] == s[left:right+1][::-1]:
                    to_return = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
                
            return to_return
                
        if s == s[::-1] or len(s) == 1:
            return s
        
        answer: str = s[0]

        for i in range(len(s)-1):
            answer = max(answer, expand(i, i+1), expand(i, i+2), key = len) #홀수 팰린드롬과 짝수 팰린드롬을 둘 다 판별
            
        return answer
