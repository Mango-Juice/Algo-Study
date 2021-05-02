#조합의 합
#https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(now: List[int]) -> None:
            sum_ = sum(now)
            if sum_ == target:
                now.sort()
                if not now in answer:
                    answer.append(now)
            if sum_ >= target:
                return
            
            for i in candidates:
                tmp = now[:]
                tmp.append(i)
                dfs(tmp)
        
        
        for i in candidates:
            dfs([i])
        
        return answer
