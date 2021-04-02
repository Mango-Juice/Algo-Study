#그룹 애너그램
#https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group: Dict[str, List[str]] = {}
            
        for i in strs:
            str_sorted: str = ''.join(sorted(i))
            if str_sorted in group.keys():
                group[str_sorted].append(i)
            else:
                group[str_sorted] = [i]
                
        return group.values()
