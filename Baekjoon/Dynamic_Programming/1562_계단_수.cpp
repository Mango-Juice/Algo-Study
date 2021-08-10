// https://www.acmicpc.net/problem/1562

#include <iostream>
#include <cstring>

using namespace std;

const int MOD = 1000000000;

int n;
int dp[10][101][1 << 10];

int solution(int num, int length, int visited) {
	if (num < 0 || num > 9) return 0;
	if (length == 0) return (int)(visited == (1 << 10) - 1);
	int& v = dp[num][length][visited];
	if(v == -1){
		v = solution(num - 1, length - 1, visited | 1 << (num - 1));
		v += solution(num + 1, length - 1, visited | 1 << (num + 1));
		v %= MOD;
	}
	return v;
}

int main(void) {
	int i;
	int answer = 0;

	cin >> n;

	for (i = 1; i < 10; i++) {
		memset(dp, -1, sizeof(dp));
		answer += solution(i, n - 1, 1 << i);
		answer %= MOD;
	}

	cout << answer << endl;

	return 0;
}