# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(hour, minute):
	answer = 0
	md = minute * (180/30)
	hd = hour * 30 + minute * (30/60)
	answer = abs(md - hd)
	if answer > 180:
		answer -= 180
	return "{:.1f}".format(answer)


hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")
