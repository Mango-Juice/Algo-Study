#회전 정렬된 배열 검색
#https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 최솟값 인덱스 탐색
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # 원래 형태 구하기
        sorted_nums = nums[left:] + nums[:left]
        rotated = left
        
        # target 인덱스 탐색
        answer = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if sorted_nums[mid] < target:
                left = mid + 1
            elif sorted_nums[mid] > target:
                right = mid - 1
            else:
                answer = mid
                break
        
        #결과 리턴
        return (answer + rotated) % len(nums) if answer != -1 else -1
