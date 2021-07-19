#이진 검색
#https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
            
        return binary_search(0, len(nums) - 1)
