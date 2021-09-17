// https://www.acmicpc.net/problem/5557

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int arr[101];
long long dp[101][21] = { 0 };

int main() {
	int i, j, N, answer;
	FAST_IO;

	cin >> N;
	for (i = 0; i < N - 1; i++) cin >> arr[i];
	cin >> answer;

	dp[0][arr[0]] = 1;
	for (i = 1; i < N ; i++) {
		for (j = 0; j < 21; j++) {
			if (dp[i - 1][j] > 0) { // 전 숫자가 j면
				if (j + arr[i] < 21) dp[i][j + arr[i]] += dp[i - 1][j]; // 덧셈
				if (j >= arr[i]) dp[i][j - arr[i]] += dp[i - 1][j]; // 뺄셈
			}
		}
	}

	cout << dp[N - 2][answer];

	return 0;
}