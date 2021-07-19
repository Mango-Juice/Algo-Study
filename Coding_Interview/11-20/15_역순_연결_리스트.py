#역순 연결 리스트
#https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(now: ListNode, pre: ListNode = None):
            if not now:
                return pre
            tmp, now.next = now.next, pre
            return reverse(tmp, now)
            
        return reverse(now = head)
