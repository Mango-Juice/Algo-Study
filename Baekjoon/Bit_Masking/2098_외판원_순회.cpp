// https://www.acmicpc.net/problem/2098

#include <stdio.h>
#include <algorithm>

using namespace std;

const int INF = 1e9;
const int MAX = 17;

int n;
int arr[MAX][MAX];
int dp[MAX][1 << MAX];

int dfs(int index, int visited) {
	if (visited == (1 << n) - 1) return arr[index][0] == 0 ? INF : arr[index][0];
	if (dp[index][visited] > 0) return dp[index][visited];
	
	dp[index][visited] = INF;

	for (int i = 0; i < n; i++) {
		if (visited & (1 << i)) continue;
		if (arr[index][i] == 0) continue;
		dp[index][visited] = min(dp[index][visited], dfs(i, visited | (1 << i)) + arr[index][i]);
	}

	return dp[index][visited];
}

int main(void) {
	int i, j, answer = INF;
	
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			scanf(" %d", &arr[i][j]);
		}
	}

	for (i = 0; i < n; i++) {
		answer = min(answer, dfs(i, 1 << i));
		if (answer != INF) break;
	}

	printf("%d", answer);

	return 0;
}