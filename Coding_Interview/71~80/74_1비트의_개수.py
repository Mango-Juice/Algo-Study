#1비트의 개수
#https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        
        while n:
            n &= n - 1
            answer += 1
            
        return answer
