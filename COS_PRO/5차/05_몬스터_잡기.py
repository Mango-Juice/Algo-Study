# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(enemies, armies):
	answer = 0
	
	for i in sorted(enemies):
		for j in sorted(armies):
			if i <= j:
				answer += 1
				break
	
	return answer


enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

print("solution 함수의 반환 값은", ret2, "입니다.")
