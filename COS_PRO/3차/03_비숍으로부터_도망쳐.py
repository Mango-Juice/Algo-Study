# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def getPos(x, y):
	result = set()
	x = ord(x) - 64
	y = int(y)
	cha = x if x < y else y
	x1, y1 = x-cha+1, y-cha+1
	
	while x1 <= 8 and y1 <= 8:
		result.add(10*x1+y1)
		x1 += 1
		y1 += 1
	
	cha = 8 - x if x > y else 8 - y
	x2, y2 = x-cha, y+cha
	
	while x2 <= 8 and y2 >= 0:
		result.add(10*x2+y2)
		x2 += 1
		y2 -= 1
	
	return result


def solution(bishops):
	answer = set()
	for i in bishops:
		answer = answer | getPos(i[0], i[1])
	
	return 64 - len(answer)


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")
