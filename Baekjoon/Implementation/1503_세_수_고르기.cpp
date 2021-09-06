// https://www.acmicpc.net/problem/1503

#include <iostream>
#include <climits>
#include <algorithm>
#include <stdlib.h>

using namespace std;

const int MAX = 1001;
bool banned[MAX] = { false };

int main() {
	int tmp, i, j, k;
	int n, m;
	int answer = INT_MAX;
	
	cin >> n >> m;

	for (i = 0; i < m; i++) {
		cin >> tmp;
		banned[tmp] = true;
	}

	for (i = 1; i <= MAX; i++) {
		if (banned[i]) continue;

		for (j = i; j <= MAX; j++) {
			if (banned[j]) continue;

			for (k = j; k <= MAX; k++) {
				if (banned[k]) continue;
				answer = min(answer, abs(n - i * j * k));
			}
		}
	}

	cout << answer;
	return 0;
}