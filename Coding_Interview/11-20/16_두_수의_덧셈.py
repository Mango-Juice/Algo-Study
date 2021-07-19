#두 수의 덧셈
#https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = result = ListNode(val = 0)
        upper: int = 0
        
        while l1 or l2 or upper:
            sum_: int = upper
                
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            upper, sum_ = sum_//10, sum_%10
            result.next = ListNode(sum_)
            result = result.next
        
        return answer.next
