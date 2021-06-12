#가장 긴 반복 문자 대체
#https://leetcode.com/problems/longest-repeating-character-replacement

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = right = 0
        
        while right < len(s):
            count[s[right]] += 1
            if max(count.values()) < right - left + 1 - k:
                count[s[left]] -= 1
                left += 1
            right += 1
            
        return right - left
