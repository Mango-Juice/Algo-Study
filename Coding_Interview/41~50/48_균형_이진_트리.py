#균형 이진 트리
#https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.answer = True
        
        def getHeight(tree: TreeNode) -> int:
            if not (tree and self.answer):
                return -1
            
            left_height = getHeight(tree.left)
            right_height = getHeight(tree.right)
            
            if abs(left_height - right_height) >= 2:
                self.answer = False
                return 0
            
            return max(right_height, left_height) + 1
        
        getHeight(root)
        return self.answer
