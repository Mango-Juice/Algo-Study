// https://www.acmicpc.net/problem/2342

#include <stdio.h>
#include <algorithm>

using namespace std;

const int INF = 1e7;
const int cost[5][5] = { {1, 2, 2, 2, 2}, {2, 1, 3, 4, 3}, {2, 3, 1, 3, 4}, {2, 4, 3, 1, 3}, {2, 3, 4, 3, 1} };

int inp[100002] = { 0 };
int dp[100002][5][5] = { 0 };

int solution(int count, int left, int right) {
	if (inp[count] == 0) return 0;
	if (dp[count][left][right] > 0) return dp[count][left][right];

	return dp[count][left][right] = min(solution(count + 1, inp[count], right) + cost[left][inp[count]], solution(count + 1, left, inp[count]) + cost[inp[count]][right]);
}

int main(void) {
	int i = 1;
	for (; i == 1 || inp[i - 1] != 0; i++) scanf("%d", inp + i);
	printf("%d", solution(1, 0, 0));
	return 0;
}