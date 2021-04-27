#상위 K 빈도 요소
#https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
            
        result = sorted(count.items(), key = (lambda x : x[1]), reverse = True)
        return list(zip(*result))[0][:k]
