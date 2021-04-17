# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(s1, s2):
	length = min(len(s1), len(s2))
	
	while length > 0:
		if s1[len(s1)-length:len(s1)] == s2[0:length]:
			break
		length -= 1
	
	return len(s1) + len(s2) - length


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")
