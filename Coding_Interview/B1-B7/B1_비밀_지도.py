#비밀지도
#https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('0', ' ').replace('1', '#'))
        
    return answer
