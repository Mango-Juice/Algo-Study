#k개의 정렬 리스트 병합
#https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        answer = root = ListNode()
        tmp = []
        
        for i in lists:
            while i:
                tmp.append(i.val)
                i = i.next
                
        tmp.sort()
        
        for i in tmp:
            root.next = ListNode(i)
            root = root.next
            
        return answer.next
