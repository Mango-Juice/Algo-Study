#다트 게임
#https://programmers.co.kr/learn/courses/30/lessons/17682

NONE, NUM, BONUS, OPTION = range(4)

def solution(dartResult):
    arr = []
    last = NONE
    
    for i in dartResult:
        #점수
        if i.isdigit():
            if last == NUM:
                arr[-1] += 9
            else:
                arr.append(int(i))
                last = NUM
        
        #보너스
        elif i == 'S':
            last = BONUS
        elif i == 'D':
            arr[-1] **= 2
            last = BONUS
        elif i == 'T':
            arr[-1] **= 3
            last = BONUS
        
        #옵션
        elif i == '#':
            arr[-1] *= -1
            last = OPTION
        elif i == '*':
            arr[-1] *= 2
            if len(arr) >= 2:
                arr[-2] *= 2
            last = OPTION

    return sum(arr)
