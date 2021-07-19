#색 정렬
#https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, j, k = 0, 0, len(nums)
        
        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
