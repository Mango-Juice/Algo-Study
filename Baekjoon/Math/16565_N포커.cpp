// https://www.acmicpc.net/problem/16565

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

const int MOD = 10007;
int combinations[53][53] = { 0 };

int getCombi(int n, int k) {
	if (n < 0 || n > 52 || k < 0 || k > 52 || k > n) return 0;
	if (combinations[n][k] > 0) return combinations[n][k];
	if (n == 0 || k == 0 || n == k) return combinations[n][k] = 1;

	combinations[n][k] = (getCombi(n - 1, k) + getCombi(n - 1, k - 1)) % MOD;
	return combinations[n][n - k] = combinations[n][k];
}

int main() {
	int N, answer = 0;
	FAST_IO;

	cin >> N;

	// 포함·배제의 원리 : (합집합의 원소의 개수) = ∑(홀수 개의 교집합의 원소의 갯수) - ∑(짝수 개의 교집합의 원소의 갯수)
	for (int i = 1; i <= N / 4; i ++) {
		// 13개의 조합 중 i개를 고르는 경우의 수 * 남은 카드 중에서 N - 4 * i개를 고르는 경우의 수
		if (i & 1) answer += getCombi(13, i) * getCombi(52 - 4 * i, N - 4 * i);
		else answer -= getCombi(13, i) * getCombi(52 - 4 * i, N - 4 * i);
		answer %= MOD;
	}

	if (answer < 0) answer += MOD;
	cout << answer;

	return 0;
}