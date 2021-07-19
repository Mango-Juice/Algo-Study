#가장 긴 동일 값의 경로
#https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.answer = 0
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left, right = dfs(node.left), dfs(node.right)
            left = left + 1 if node.left and node.val == node.left.val else 0
            right = right + 1 if node.right and node.val == node.right.val else 0
            
            self.answer = max(self.answer, left + right)
            return max(left, right)
        
        dfs(root)
        return self.answer
