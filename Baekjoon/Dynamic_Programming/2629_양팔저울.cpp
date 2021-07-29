// https://www.acmicpc.net/problem/2629

#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

int i, n, m;
int chu[30];
int goo[7];
bool dp[30 + 1][15000 + 1];

void check(int num, int weight) {
	if (num > n) return;
	if (dp[num][weight]) return;
	dp[num][weight] = true;

	check(num + 1, weight + chu[num]);
	check(num + 1, weight);
	check(num + 1, abs(weight - chu[num]));
}

int main(int argc, char** argv) {
	scanf("%d", &n);
	for (i = 0; i < n; i ++) scanf(" %d", chu + i);
	scanf("%d", &m);
	for (i = 0; i < m; i++) scanf(" %d", goo + i);

	memset(dp, false, sizeof(dp));
	check(0, 0);

	for (i = 0; i < m; i++) {
		if (goo[i] > 15000) printf("N ");
		else if (dp[n][goo[i]]) printf("Y ");
		else printf("N ");
	}

	return 0;
}