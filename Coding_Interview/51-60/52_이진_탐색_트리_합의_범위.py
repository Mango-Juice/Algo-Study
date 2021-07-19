#이진 탐색 트리 합의 범위
#https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return node.val + dfs(node.left) + dfs(node.right)
            
        return dfs(root)
