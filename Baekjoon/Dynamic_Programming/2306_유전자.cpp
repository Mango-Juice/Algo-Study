// https://www.acmicpc.net/problem/2306

#include <iostream>
#include <string>

using namespace std;

string str;
int dp[501][501] = { 0 };

bool isKOI(int from, int to) {
	return ((str[from] == 'a' && str[to] == 't') || (str[from] == 'g' && str[to] == 'c'));
}

int main(int argc, char** argv) {
	int answer = 0, len = 0;

	cin >> str;
	len = str.length();

	for (int cha = 1; cha < len; cha++) {
		for (int i = 0; i + cha < len; i++) {
			int j = i + cha;
			if (isKOI(i, j)) dp[i][j] = dp[i + 1][j - 1] + 2; // 1, 2단계 판별 (a-t, g-c)

			for (int k = i; k < j; k++) { // 현재 유전자를 반으로 쪼개서
				dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j]); // 양쪽 다 KOI 유전자면 이어 붙이기
			}
		}
	}

	cout << dp[0][len - 1];
	return 0;
}