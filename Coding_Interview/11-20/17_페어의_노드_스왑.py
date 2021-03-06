#페어의 노드 스왑
#https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = head
        
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
            
        return result
