// https://www.acmicpc.net/problem/2565

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<pair<int, int>> arr;
int inp[5001] = { 0 };
int lis[5001] = { 0 };

int main(void) {
	int i, j, n, a, b;
	int maximum = 0;

	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		scanf(" %d %d", &a, &b);
		inp[a] = b;
		maximum = max(maximum, max(a, b));
	}

	for (i = 1; i <= maximum; i++) if (inp[i] > 0) arr.push_back(pair<int, int>(i, inp[i]));

	for (i = 0, j = 0; i < arr.size(); i++) {
		int target = arr[i].second;
		auto lb = upper_bound(lis + 1, lis + j + 1, target);
		*lb = target;
		if (lb == lis + j + 1) j++;
	}

	printf("%d", n - j);

	return 0;
}