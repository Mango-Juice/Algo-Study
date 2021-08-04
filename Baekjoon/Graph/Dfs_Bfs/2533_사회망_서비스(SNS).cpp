// https://www.acmicpc.net/problem/2533

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

enum status { NORMAL, EARLY };
vector<int> vec[1000000];
int dp[1000000][2];

void dfs(int target) {
	int i;

	dp[target][NORMAL] = 0;
	dp[target][EARLY] = 1;

	for (i = 0; i < vec[target].size(); i++) {
		if (dp[vec[target][i]][NORMAL] == -1) {
			dfs(vec[target][i]);
			dp[target][NORMAL] += dp[vec[target][i]][EARLY];
			dp[target][EARLY] += min(dp[vec[target][i]][EARLY], dp[vec[target][i]][NORMAL]);
		}
	}
}

int main() {
	int i, n, u, v;

	scanf("%d", &n);

	for (i = 1; i <= n; i++) dp[i][NORMAL] = -1;

	for (i = 1; i < n; i++) {
		scanf("%d %d", &u, &v);
		vec[u].push_back(v);
		vec[v].push_back(u);
	}

	dfs(1);

	printf("%d", min(dp[1][NORMAL], dp[1][EARLY]));

	return 0;
}