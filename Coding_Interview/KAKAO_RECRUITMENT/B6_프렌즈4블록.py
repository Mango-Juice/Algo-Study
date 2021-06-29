#프렌즈4블록
#https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    # ===== 상수 선언 ===== #
    EMPTY = '@'
    
    # ===== 변수 선언 ===== #
    arr = [list(i) for i in board] 
    matched = True
   
    # ===== 실행 ===== #
    while matched: # 지워지는 블록이 없을 때까지 반복
        matched = [] # 리스트 초기화
        
        # ===== 1단계 : 블록 탐지 ===== #
        for i in range(m - 1):
            for j in range(n - 1):
                if arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1] != EMPTY: # 4블록이 있으면
                    matched.append((i, j)) # 지워지는 블록 목록에 추가
        
        # ===== 2단계 : 블록 제거 ===== #
        for i, j in matched:
            arr[i][j] = arr[i][j + 1] = arr[i + 1][j] = arr[i + 1][j + 1] = EMPTY
            
        # ===== 3단계 : 블록 내리기 ===== #
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if arr[i + 1][j] == EMPTY:
                        arr[i + 1][j], arr[i][j] = arr[i][j], EMPTY
                        
    # ===== 출력 ===== #
    return sum(i.count(EMPTY) for i in arr)
