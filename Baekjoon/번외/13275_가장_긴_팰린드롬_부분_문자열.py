#https://www.acmicpc.net/problem/13275
#https://github.com/Mango-Juice/Algo-Study/blob/main/Coding_Interview/01~10/06_가장_긴_팰린드롬_부분_문자열.py 을 해결한 후 조금 더 어려운 유사 문제를 풀어봄.

import sys
input = sys.stdin.readline

def longestPalindrome(s: str) -> int:
    answer: int = 1
    
    def expand(left: int, right: int) -> int:
        to_return: int = 0
        
        if answer > 1:
            cha: int = (answer - (right - left + 1)) // 2
            left -= cha
            right += cha

        while left >= 0 and right <= len(s):
            if s[left:right+1] == s[left:right+1][::-1]:
                to_return = right - left + 1
                left -= 1
                right += 1
            else:
                break
            
        return to_return
                
    if s == s[::-1] or len(s) == 1:
        return len(s)

    for i in range(len(s)-1):
        answer = max(answer, expand(i, i+1), expand(i, i+2))
        if answer == len(s):
            break
        
    return answer

print(longestPalindrome(input().rstrip()))
