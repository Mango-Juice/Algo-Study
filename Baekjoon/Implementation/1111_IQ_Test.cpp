// https://www.acmicpc.net/problem/1111

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int numbers[51];

int main() {
	int n, a, b, i;
	FAST_IO;

	// 입력
	cin >> n;
	for (i = 0; i < n; i++) cin >> numbers[i];

	// 예외처리
	if (n == 1) cout << 'A';
	else if (n == 2) {
		if (numbers[0] == numbers[1]) cout << numbers[0];
		else cout << 'A';
	}

	// a, b 구하기
	else {
		a = numbers[1] != numbers[0] ? (numbers[2] - numbers[1]) / (numbers[1] - numbers[0]) : 0;
		b = numbers[1] - numbers[0] * a;

		for (i = 2; i < n; i++) {
			if (numbers[i] != numbers[i - 1] * a + b) {
				cout << 'B';
				return 0;
			}
		}

		cout << numbers[n - 1] * a + b;
	}

	return 0;
}