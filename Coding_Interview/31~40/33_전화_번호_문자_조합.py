#전화 번호 문자 조합
#https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        itoa = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        answer = []
        
        def dfs(idx: int, s: str) -> None:
            if idx == len(digits):
                answer.append(s)
                return
            
            for i in itoa[int(digits[idx]) - 2]:
                dfs(idx + 1, s + i)
            
        dfs(0, "")
        return answer
