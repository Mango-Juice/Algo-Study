# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(arr):
	answer = 0
	last = arr[0]
	now_length = 1
	
	for i in arr[1:]:
		if i > last:
			now_length += 1
		else:
			answer = max(now_length, answer)
			now_length = 1
		last = i
		
	return answer

arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
