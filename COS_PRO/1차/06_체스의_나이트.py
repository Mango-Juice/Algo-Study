# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

able_pos = ((-1, -2), (-2, -1),
						(1, 2), (2, 1),
						(-1, 2), (-2, 1),
						(1, -2), (2, -1))

def solution(pos):
	answer = 0
	real_pos = (ord(pos[0])-64, int(pos[1]))

	for i in able_pos:
		if real_pos[0] + i[0] < 1 or real_pos[0] + i[0] > 8:
			continue
		elif real_pos[1] + i[1] < 1 or real_pos[1] + i[1] > 8:
			continue
		answer += 1
	
	return answer

pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")
