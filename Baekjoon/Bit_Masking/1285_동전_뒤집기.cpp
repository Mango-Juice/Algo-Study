// https://www.acmicpc.net/problem/1285

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>

using namespace std;

bool coin[21][21] = { false };
int answer = 400;
int n, i, j, k, result, cnt;
bool now;
char c;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			cin >> c;
			if (c == 'H') coin[i][j] = true;
		}
	}

	for (i = 0; i < (1 << n) - 1; i++) {
		result = 0;

		for (j = 0; j < n; j++) {
			cnt = 0;

			for (k = 0; k < n; k++) {
				now = coin[k][j];
				if ((i & (1 << k)) != 0) now ^= true;
				if (now) cnt++;
			}
			
			result += min(cnt, n - cnt);
		}

		answer = min(result, answer);
	}

	cout << answer;
}