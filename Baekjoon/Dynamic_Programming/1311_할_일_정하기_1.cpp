// https://www.acmicpc.net/problem/1311

#include <stdio.h>

using namespace std;

int n;
int arr[21][21];
int dp[21][1 << 21] = { 0 };

int min(int a, int b) {
	if (a == 0 && b == 0) return 0;
	else if (a == 0) return b;
	else if (b == 0) return a;
	else return a > b ? b : a;
}

int dfs(int index, int visited) {
	if (visited == (1 << n) - 1) return 0;
	if (dp[index][visited] > 0) return dp[index][visited];

	for (int i = 0; i < n; i++) {
		if (visited & (1 << i)) continue;
		dp[index][visited] = min(dp[index][visited], dfs(index + 1, visited | (1 << i)) + arr[index][i]);
	}

	return dp[index][visited];
}

int main(void) {
	int i, j;
	
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			scanf(" %d", &arr[i][j]);
		}
	}

	printf("%d", dfs(0, 0));

	return 0;
}