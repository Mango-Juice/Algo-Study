// https://www.acmicpc.net/problem/17281

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int result[51][9];
int answer = 0;

int hit(int ru[3], int anta) {
	int new_score = 0;

	new_score += ru[2];
	ru[2] = ru[1];
	ru[1] = ru[0];
	ru[0] = 1;

	for (int i = 1; i < anta; i++) {
		new_score += ru[2];
		ru[2] = ru[1];
		ru[1] = ru[0];
		ru[0] = 0;
	}

	return new_score;
}

void simulation(int order[9]) {
	int score = 0, target = 0, i;

	for (i = 0; i < n; i++) {
		int out = 0;
		int ru[3] = { 0, 0, 0 };

		while (out < 3) {
			if (result[i][order[target]] == 0) out++;
			else score += hit(ru, result[i][order[target]]);

			target = (target + 1) % 9;
		}
	}

	answer = max(answer, score);
}

void solution(int order[9], int used, int count) {
	if (count == 3) {
		order[count] = 0;
		solution(order, used, count + 1);
		return;
	}

	for (int i = 1; i < 9; i++) {
		if (used & (1 << i)) continue;

		int new_order[9];
		copy(order, order + 9, new_order);
		new_order[count] = i;

		if (count == 8) simulation(new_order);
		else solution(new_order, used | (1 << i), count + 1);
	}
}

int main() {
	FAST_IO;

	int i, j;
	int order[9];

	cin >> n;

	for (i = 0; i < n; i++)
		for (j = 0; j < 9; j++) 
			cin >> result[i][j];

	solution(order, 0, 0);
	cout << answer;

	return 0;
}