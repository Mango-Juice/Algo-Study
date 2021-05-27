#가장 큰 수
#https://leetcode.com/problems/largest-number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(nums_str[i] + nums_str[j]) < int(nums_str[j] + nums_str[i]):
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
        return str(int(''.join(nums_str)))
