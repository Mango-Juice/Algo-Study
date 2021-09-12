// https://www.acmicpc.net/problem/1339

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct alphabet {
	int idx;
	int score;

	bool operator < (const alphabet& b) {
		return score > b.score;
	}
};

struct alphabet alphas[26];
string strs[10];
int result[26];
int n;

void printAnswer() {
	int answer = 0, index = 0, i, j, weight;

	while (alphas[index].score > 0) {
		result[alphas[index].idx - 'A'] = 9 - index;
		index++;
	}

	for (i = 0; i < n; i++) {
		weight = 1;

		for (j = strs[i].length() - 1; j >= 0; j--) {
			answer += result[strs[i][j] - 'A'] * weight;
			weight *= 10;
		}
	}

	cout << answer;
	
}

int main() {
	int i, j, weight;
	FAST_IO;

	for (i = 'A'; i <= 'Z'; i++) {
		alphas[i - 'A'].idx = i;
		alphas[i - 'A'].score = 0;
	}

	cin >> n;
	for (i = 0; i < n; i++) {
		weight = 1;
		cin >> strs[i];

		for (j = strs[i].length() - 1; j >= 0; j--) {
			alphas[strs[i][j] - 'A'].score += weight;
			weight *= 10;
		}
	}
	
	sort(alphas, alphas + 26);
	printAnswer();
	return 0;
}