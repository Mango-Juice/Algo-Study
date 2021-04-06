#배열 파티션 1
#https://leetcode.com/problems/array-partition-i

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
