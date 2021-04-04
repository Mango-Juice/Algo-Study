#두 수의 합
#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum_01(self, nums: List[int], target: int) -> List[int]:
        nums_sorted: List[int] = sorted(nums)
            
        for i in range(len(nums)-1):
            j = 1
            
            while i + j < len(nums) and nums_sorted[i] + nums_sorted[i+j] <= target:
                j += 1
                
            if nums_sorted[i] + nums_sorted[i+j-1] == target:
                first: int = nums.index(nums_sorted[i])
                nums[first] += 1
                return [first, nums.index(nums_sorted[i+j-1])]

    def twoSum_02(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int, int] = {}
        
        for n, i in enumerate(nums):
            if i in num_dict:
                return [num_dict[i], n]
            num_dict[target - i] = n
