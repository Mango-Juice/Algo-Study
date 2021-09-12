// https://www.acmicpc.net/problem/1890

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int n;
int arr[101][101];
long long result[101][101] = { 0 };

void solution() {
	int i, j;
	result[0][0] = 1;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n - (int)(i == n - 1); j++) {
			if (result[i][j] == 0) continue;

			int num = arr[i][j];
			if (num + i < n) result[num + i][j] += result[i][j];
			if (num + j < n) result[i][num + j] += result[i][j];
		}
	}
}

int main() {
	int i, j;
	FAST_IO;

	cin >> n;
	for (i = 0; i < n; i++) for (j = 0; j < n; j++) cin >> arr[i][j];

	solution();
	cout << result[n - 1][n - 1];

	return 0;
}