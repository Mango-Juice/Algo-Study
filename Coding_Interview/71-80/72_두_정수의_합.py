#두 정수의 합
#https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        
        num1, num2 = bin(a & MASK)[2:].zfill(32), bin(b & MASK)[2:].zfill(32)
        carry = 0
        answer = ""
        
        for idx in range(32):
            A = int(num1[31 - idx])
            B = int(num2[31 - idx])
            
            nand = A & B
            nxor = A ^ B
            ncand = nxor & carry
            S = nxor ^ carry
            carry = ncand | nand
            
            answer += str(S)
        
        if carry == 1:
            answer +=  '1'
        
        result = int(answer[::-1], 2) & MASK
        
        if result > 0x7FFFFFFF: # 음수라면
            result = ~(result ^ MASK)
        
        return result
