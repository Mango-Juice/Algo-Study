#UTF-8 검증
#https://leetcode.com/problems/utf-8-validation

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        start_with_10 =  [False, False, False, False]
        
        def is_start_with_10(size):
            for i in range(idx + 1, idx + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        while idx < len(data):
            num = data[idx]
            if (num >> 3) == 0b11110 and is_start_with_10(3):
                idx += 4
            elif (num >> 4) == 0b1110 and is_start_with_10(2):
                idx += 3
            elif (num >> 5) == 0b110 and is_start_with_10(1):
                idx += 2
            elif (num >> 7) == 0:
                idx += 1
            else:
                return False
        
        return True
