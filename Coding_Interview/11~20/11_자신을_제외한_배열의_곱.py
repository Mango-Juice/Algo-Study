#자신을 제외한 배열의 곱
#https://leetcode.com/problems/product-of-array-except-self
#조건: 나눗셈 사용 금지, 시간복잡도 O(n) 이하

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left: List[int] = [1]
        answer: List[int] = []
        p: int = 1
            
        for i in range(len(nums)-1):
            p = p * nums[i]
            left.append(p)
        
        p = 1
        
        for i in range(len(nums)-1, -1, -1):
            answer.append(p * left[i])
            p = p * nums[i]
            
        return answer[::-1]
