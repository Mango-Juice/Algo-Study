// https://www.acmicpc.net/problem/9095

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int dp[12] = { 0 };

int solution(int number) {
	if (dp[number] > 0) return dp[number];
	return dp[number] = solution(number - 1) + solution(number - 2) + solution(number - 3);
}

int main() {
	int i, t, n;
	FAST_IO;

	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;

	cin >> t;

	for (i = 0; i < t; i++) {
		cin >> n;
		cout << solution(n) << '\n';
	}

	return 0;
}