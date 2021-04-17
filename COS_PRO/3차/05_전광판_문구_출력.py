# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(phrases, second):
	second = second % 28
	
	if second == 14:
		return phrases
	elif second < 14:
		tmp = '_' * (14 - second)
		tmp += phrases[0:second]
		return tmp
	else:
		tmp = phrases[second-14:]
		tmp += '_' * (second - 14)
	return tmp


phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")
