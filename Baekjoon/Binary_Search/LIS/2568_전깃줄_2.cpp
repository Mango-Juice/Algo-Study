// https://www.acmicpc.net/problem/2568

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<pair<int, int>> arr;
int inp[500001] = { 0 };
int lis[500001] = { 0 };
int indexs[500001] = { 0 };
bool answer[500001] = { false };

void getAnswer(int idx, int num) {
	if (idx < 0) return;
	if (indexs[idx] == num) {
		getAnswer(idx - 1, num - 1);
		answer[arr[idx].first] = true;
	}
	else getAnswer(idx - 1, num);
}

int main(void) {
	int i, j, n, a, b;
	int maximum = 0;

	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		scanf(" %d %d", &a, &b);
		inp[a] = b;
		maximum = max(maximum, max(a, b));
	}

	for (i = 1; i <= maximum; i++) {
		if (inp[i] > 0) arr.push_back(pair<int, int>(i, inp[i]));
		else answer[i] = true;
	}

	for (i = 0, j = 0; i < arr.size(); i++) {
		int target = arr[i].second;
		auto lb = upper_bound(lis + 1, lis + j + 1, target);
		*lb = target;
		indexs[i] = distance(lis, lb);
		if (lb == lis + j + 1) j++;
	}

	printf("%d\n", n - j);
	getAnswer(arr.size() - 1, j);

	for (i = 1; i <= maximum; i++) if (!answer[i]) printf("%d\n", i);

	return 0;
}