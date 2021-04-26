#중복 문자 없는 가장 긴 부분 문자열
#https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        
        result = 1
        left = 0
        right = 1
        
        while right < len(s):
            if len(set(s[left:right+1])) == right - left + 1:
                result = max(result, right - left + 1)
            else:
                left += 1
            right += 1
                
        return result
