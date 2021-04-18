#중복 문자 제거
#https://leetcode.com/problems/remove-duplicate-letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for i in sorted(set(s)):
            after = s[s.index(i):]
            if set(s) == set(after):
                return i + self.removeDuplicateLetters(after.replace(i, ''))
        return ''
