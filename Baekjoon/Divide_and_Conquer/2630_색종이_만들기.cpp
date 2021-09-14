// https://www.acmicpc.net/problem/2630

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

bool arr[129][129];
int blue = 0, white = 0;

void solution(int r0, int r1, int c0, int c1) {
	int i, j;
	bool has1 = false, has0 = false;

	for (i = r0; i <= r1; i++) {
		for (j = c0; j <= c1; j++) {
			if (!arr[i][j]) has0 = true;
			else has1 = true;
			if (has1 && has0) break;
		}
	}

	if (!has0) {
		blue++;
		return;
	}
	if (!has1) {
		white++;
		return;
	}

	int rmid = (r0 + r1) / 2;
	int cmid = (c0 + c1) / 2;

	solution(r0, rmid, c0, cmid);
	solution(rmid + 1, r1, c0, cmid);
	solution(r0, rmid, cmid + 1, c1);
	solution(rmid + 1, r1, cmid + 1, c1);
}

int main() {
	int i, j, n;
	FAST_IO;

	cin >> n;

	for (i = 0; i < n; i++) for (j = 0; j < n; j++) cin >> arr[i][j];

	solution(0, n - 1, 0, n - 1);

	cout << white << '\n';
	cout << blue << '\n';
	
	return 0;
}