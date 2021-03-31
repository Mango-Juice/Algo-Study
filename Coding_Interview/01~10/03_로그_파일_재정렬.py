#로그 파일 재정렬
#https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs: List[str] = []
        digit_logs: List[str] = []
            
        for i in logs:
            if i.split()[1].isdigit():
                digit_logs.append(i)
            else:
                letter_logs.append(i)
        
        letter_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
