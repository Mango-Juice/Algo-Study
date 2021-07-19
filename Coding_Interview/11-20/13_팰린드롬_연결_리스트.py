#팰린드롬 연결 리스트
#https://leetcode.com/problems/palindrome-linked-list

from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes: Deque = deque()
        
        while head != None:
            nodes.append(head.val)
            head = head.next
            
        while len(nodes) >= 2:
            if nodes.popleft() != nodes.pop():
                return False
            
        return True
