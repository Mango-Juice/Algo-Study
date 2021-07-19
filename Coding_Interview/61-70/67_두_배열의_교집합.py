#두 배열의 교집합
#https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: #투포인터 알고리즘
        answer = []
        n1 = sorted(set(nums1))
        n2 = sorted(set(nums2))
        p1 = p2 = 0
        
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] > n2[p2]:
                p2 += 1
            elif n1[p1] < n2[p2]:
                p1 += 1
            else:
                answer.append(n1[p1])
                p1 += 1
                p2 += 1
                
        return answer
    
    
    def intersection_easy(self, nums1: List[int], nums2: List[int]) -> List[int]: #내장 함수 이용
        return set(nums1) & set(nums2)
