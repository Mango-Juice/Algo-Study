// https://www.acmicpc.net/problem/17626

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;
int dp[50001] = { 0 };

int getAnswer(int value, int count) {
	if (value == 0) return 0;
	if (count > 4) return INT_MAX - 1;
	if (dp[value] > 0) return dp[value];

	int result = INT_MAX - 1;
	int limit = sqrt(value);

	for (int i = 1; i <= limit; i++)
		result = min(result, getAnswer(value - i * i, count + 1) + 1);
	
	return dp[value] = result;
}

int main() {
	int n;
	FAST_IO;

	cin >> n;
	cout << getAnswer(n, 1);

	return 0;
}