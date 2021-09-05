// https://www.acmicpc.net/problem/14428

#include <stdio.h>
#include <algorithm>

using namespace std;

int tree[400004], arr[100001];

int getMinIdx(int a, int b) {
	if (a == -1) return b;
	if (b == -1) return a;
	if (arr[a] == arr[b]) return min(a, b);
	return arr[a] > arr[b] ? b : a;
}

int init(int from, int to, int index) {
	if (from == to) tree[index] = from;
	else {
		int mid = (from + to) / 2;
		tree[index] = getMinIdx(init(from, mid, index * 2), init(mid + 1, to, index * 2 + 1));
	}
	return tree[index];
}

int getMin(int from, int to, int index, int left, int right) {
	if (from > right || to < left) return -1;
	if (left <= from && right >= to) return tree[index];

	int mid = (from + to) / 2;
	return getMinIdx(getMin(from, mid, index * 2, left, right), getMin(mid + 1, to, index * 2 + 1, left, right));
}

int update(int from, int to, int index, int target) {
	if (target < from || target > to) return tree[index];
	if (from == to) return tree[index];

	int mid = (from + to) / 2;
	return tree[index] = getMinIdx(update(from, mid, index * 2, target), update(mid + 1, to, index * 2 + 1, target));
}

int main() {
	int i, a, b, c, n, m;

	scanf("%d", &n);

	for (i = 0; i < n; i++) scanf(" %d", arr + i);

	init(0, n - 1, 1);

	scanf("%d", &m);

	for (i = 0; i < m; i++) {
		scanf("%d %d %d", &a, &b, &c);
		if (a == 1) {
			arr[b - 1] = c;
			update(0, n - 1, 1, b - 1);
		}
		else printf("%d\n", getMin(0, n - 1, 1, b - 1, c - 1) + 1);
	}

	return 0;
}