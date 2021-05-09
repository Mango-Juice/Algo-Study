#이진 트리의 직경
#https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.answer = 0
        
        def dfs(tree: TreeNode) -> int:
            if not tree:
                return 0
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            self.answer = max(self.answer, left + right)
            
            return max(left, right) + 1
                
        dfs(root)
        
        return self.answer
