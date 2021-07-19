#정렬된 배열의 이진 탐색 트리 변환
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeTree(left: int, right: int) -> TreeNode:
            center = (left + right) // 2
            node = TreeNode(nums[center])
            
            node.left = makeTree(left, center - 1) if right - left > 1 else None
            node.right = makeTree(center + 1, right) if right - left > 0 else None

            return node
            
        return makeTree(0, len(nums)-1)
