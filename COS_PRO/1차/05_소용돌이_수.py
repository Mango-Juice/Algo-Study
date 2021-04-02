# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(n):
	answer = 0
	num = 1
	count = 0
	idx = 0

	while num < n*n:
		answer += num
		num += (n-1-idx*2)*2
		if count == 0:
			count = 1
		else:
			count = 0
			idx += 1
	
	if num == n*n:
		answer += num
	
	return answer

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
