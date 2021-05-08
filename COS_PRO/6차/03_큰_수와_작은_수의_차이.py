# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(words, K):
	words.sort()
	answer = 10000
	idx = 0
	
	while idx + K < len(words):
		answer = min(answer, (max(words[idx:idx + K]) - min(words[idx:idx + K])))
		idx += 1
	
	return answer


arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")
