// https://www.acmicpc.net/problem/10844

#include <iostream>

using namespace std;

const int MOD = 1000000000;

int n;
int dp[10][101] = { 0 };

int solution(int num, int length) {
	if (num < 0 || num > 9) return 0;
	if (dp[num][length] == 0) dp[num][length] = (solution(num - 1, length - 1) + solution(num + 1, length - 1)) % MOD;
	return dp[num][length];
}

int main(void) {
	int i;
	int answer = 0;

	cin >> n;

	for (i = 0; i < 10; i++) dp[i][1] = 1;

	for (i = 1; i < 10; i++) {
		answer += solution(i, n);
		answer %= MOD;
	}

	cout << answer << endl;

	return 0;
}