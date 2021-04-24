# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def sosu(a, b):
	answer = list(range(int(a**(1/3))+1, int(b**(1/2))+1))
	
	if 1 in answer:
		answer.remove(1)
	if not answer:
		return []
	
	p = 0
	while answer[p] != answer[-1] and answer:
		k = 2
		while answer[p] * k <= answer[-1]:
			if answer[p] * k in answer:
				answer.remove(answer[p]*k)
			k += 1
		p += 1
		
	return answer

def solution(a, b):
	answer = 0
	sosus = sosu(a, b)
	
	for i in sosus:
		if i <= a**(1/2) or i >= b**(1/3):
			answer += 1
		else:
			answer += 2
	return answer


a =  6
b =  30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")
