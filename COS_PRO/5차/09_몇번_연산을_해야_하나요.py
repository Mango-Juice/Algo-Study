# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(number, target):
	if number > target:
		return number - target
	
	answer = 0
	while abs(target - (number * 2)) < abs(target - number):
		answer += 1
		number *= 2

	return answer + abs(target - number)


number1 = 5
target1 = 9
ret1 = solution(number1, target1)

print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

print("solution 함수의 반환 값은", ret2, "입니다.")
