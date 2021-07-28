// https://www.acmicpc.net/problem/11049

#include <iostream>
#include <string>
#include <stdio.h>
#include <limits.h>

using namespace std;

int inp[500][2] = {};
int dp[500][500] = {};

int main(int argc, char** argv) {
	int n, i, j, cha;

	scanf("%d", &n);
	for (i = 0; i < n; i++) scanf("%d %d", &inp[i][0], &inp[i][1]);

	if (n == 1) {
		printf("0");
		return 0;
	}

	for (cha = 1; cha < n; cha++) {
		for (i = 0; i + cha < n; i++) {
			int target = i + cha;
			dp[i][target] = INT_MAX;
			for (j = i; j < target; j++) {
				dp[i][target] = min(dp[i][target], dp[i][j] + dp[j + 1][target] + inp[i][0] * inp[j][1] * inp[target][1]);
			}
		}
	}

	printf("%d", dp[0][n - 1]);

	return 0;
}