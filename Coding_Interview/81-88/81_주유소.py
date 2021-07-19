#주유소
#https://leetcode.com/problems/gas-station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        answer, tank = 0, 0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]: #연료가 부족하면
                answer = i + 1 #출발지 초기화
                tank = 0
            else: #연료가 충분하면
                tank += gas[i] - cost[i] #넘어가기
        
        return answer
