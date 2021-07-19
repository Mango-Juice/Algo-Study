#부분 집합
#https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def dfs(idx: int, now: List[int]) -> None:
            answer.append(now)
            for i in range(idx, len(nums)):
                dfs(i + 1, now + [nums[i]])
        
        dfs(0, [])
        return answer
