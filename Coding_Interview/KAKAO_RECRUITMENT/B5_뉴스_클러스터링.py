#뉴스 클러스터링
#https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    s1 = []
    s2 = []
    
    for i in range(len(str1) - 1):
        target = str1[i : i + 2]
        if target.isalpha():
            s1.append(target.lower())
    
    for i in range(len(str2) - 1):
        target = str2[i : i + 2]
        if target.isalpha():
            s2.append(target.lower())
    
    gyo = sum((Counter(s1) & Counter(s2)).values())
    hap = sum((Counter(s1) | Counter(s2)).values())
    
    return int(65536 * gyo / hap) if hap > 0 else 65536
