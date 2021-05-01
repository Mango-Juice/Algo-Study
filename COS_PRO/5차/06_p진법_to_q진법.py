# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(s1, s2, p, q):
	jin10 = 0
	answer = ""
	
	for idx, i in enumerate(s1[::-1]):
		jin10 += (p ** (idx)) * int(i)
	for idx, i in enumerate(s2[::-1]):
		jin10 += (p ** (idx)) * int(i)
		
	while jin10 > 0:
		answer = str(jin10 % q) + answer
		jin10 //= q
	
	return answer


s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")
