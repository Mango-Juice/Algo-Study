#추석 트래픽
#https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    # ===== 상수 선언 ===== #
    START = 1
    END = -1
    
    # ===== 변수 선언 ===== #
    acum = 0
    answer = 0
    logs = []
    
    # ===== 문자열 전처리 ===== #
    for i in lines:
        arr = i.split()
        time_arr = tuple(map(float, arr[1].split(':')))
        time = time_arr[0] * 3600 + time_arr[1] * 60 + time_arr[2] #초단위 숫자로 변환
        logs.append((time, END))
        logs.append((time - float(arr[2][:-1]) + 0.001, START)) #시작 시간도 포함해야하므로 0.001초 더함
    
    # ===== 최댓값 계산 ===== #
    logs.sort()
    
    for idx, value1 in enumerate(logs):
        now = acum
        
        for value2 in logs[idx + 1:]: #1초 미만인 쪼꼬미들 처리
            if value2[0] - value1[0] >= 1:
                break
            if value2[1] == START:
                now += 1
        
        answer = max(answer, now)
        acum += value1[1]
        
    # ===== 출력 ===== #
    return answer
