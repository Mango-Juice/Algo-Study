# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(commands):
	answer = []
	count = {'U':0, 'D':0, 'L':0, 'R':0}
	
	for i in commands:
		count[i] += 1
	
	answer = [count['R']-count['L'], count['U']-count['D']]
	return answer

commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")
