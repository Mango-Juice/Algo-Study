# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


from itertools import permutations

def solution(card, n):
	card.sort()
	if sorted(map(int, str(n))) != card:
		return -1
	
	card_str = list(map(str, card))
	cards = sorted(list(set(map(''.join, permutations(card_str, len(card_str))))))

	return cards.index(str(n))


card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
