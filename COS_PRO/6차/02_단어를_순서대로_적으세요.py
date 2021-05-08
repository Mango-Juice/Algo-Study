# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(K, words):
	if not words:
		return 0
	
	answer = 1
	now = 0
	
	for i in words:
		if now + len(i) <= K:
			now += len(i) + 1
		else:
			now = len(i) + 1
			answer += 1
	
	return answer


K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")
