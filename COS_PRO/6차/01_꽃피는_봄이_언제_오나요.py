# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from collections import deque

def solution(n, garden):
	directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
	answer = 0
	Q = deque()
	
	def spread(i, j, count):
		for d in directions:
			new_i = i + d[0]
			new_j = j + d[1]
			if new_i >= 0 and new_i < n and new_j >= 0 and new_j < n  and garden[new_i][new_j] == 0:
				garden[new_i][new_j] = 1
				Q.append((new_i, new_j, count + 1))
	
	for i in range(n):
		for j in range(n):
			if garden[i][j] == 1:
				Q.append((i, j, 0))

	while Q:
		target = Q.popleft()
		spread(target[0], target[1], target[2])
		answer = target[2]

	return answer
