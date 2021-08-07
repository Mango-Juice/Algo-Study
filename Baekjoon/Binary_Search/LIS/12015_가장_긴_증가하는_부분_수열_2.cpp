// https://www.acmicpc.net/problem/12015

#include <stdio.h>
#include <algorithm>

using namespace std;

int lis[1000005] = { 0 };

int main(void) {
	int i, j, n, tmp;

	scanf("%d", &n);

	for (i = 0, j = 0; i < n; i++) {
		scanf(" %d", &tmp);
		auto lb = lower_bound(lis + 1, lis + j + 1, tmp);
		*lb = tmp;
		if (lb == lis + j + 1) j++;
	}

	printf("%d", j);

	return 0;
}