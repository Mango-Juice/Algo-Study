#전위, 중위 순회 결과로 이진 트리 구축
#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder and preorder:
            center = preorder.pop(0)

            node = TreeNode(center)
            node.left = self.buildTree(preorder, inorder[0:inorder.index(center)])
            node.right = self.buildTree(preorder, inorder[inorder.index(center) + 1:])

            return node
