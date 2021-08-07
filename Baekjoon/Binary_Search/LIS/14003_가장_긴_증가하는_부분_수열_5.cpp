// https://www.acmicpc.net/problem/14003

#include <stdio.h>
#include <algorithm>

using namespace std;

int arr[1000001] = { 0 };
int lis[1000001] = { 0 };
int indexs[1000001] = { 0 };

void getAnswer(int idx, int num) {
	if (idx == 0) return;
	if (indexs[idx] == num) {
		getAnswer(idx - 1, num - 1);
		printf("%d ", arr[idx]);
	}
	else getAnswer(idx - 1, num);
}

int main(void) {
	int i, j, n;

	scanf("%d", &n);

	for (i = 1, j = 0; i <= n; i++) {
		scanf(" %d", arr + i);
		auto lb = lower_bound(lis + 1, lis + j + 1, arr[i]);
		*lb = arr[i];
		indexs[i] = distance(lis, lb);
		if (lb == lis + j + 1) j++;
	}

	printf("%d\n", j);
	getAnswer(n, j);

	return 0;
}