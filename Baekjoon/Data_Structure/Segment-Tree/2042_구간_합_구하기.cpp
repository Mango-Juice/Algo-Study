// https://www.acmicpc.net/problem/2042
// 세그먼트 트리

#include <stdio.h>

using namespace std;

typedef long long ll;

ll tree[4000004];
ll arr[1000001];

ll init(int from, int to, int index) {
	if (from == to) tree[index] = arr[from];
	else {
		int mid = (from + to) / 2;
		tree[index] = init(from, mid, index * 2) + init(mid + 1, to, index * 2 + 1);
	}
	return tree[index];
}

ll sum(int from, int to, int index, int left, int right) {
	if (from > right || to < left) return 0;
	if (left <= from && right >= to) return tree[index];
	int mid = (from + to) / 2;
	return sum(from, mid, index * 2, left, right) + sum(mid + 1, to, index * 2 + 1, left, right);
}

void update(int from, int to, int index, int target, ll diff) {
	if (target < from || target > to) return;
	tree[index] += diff;
	if (from == to) return;

	int mid = (from + to) / 2;
	update(from, mid, index * 2, target, diff);
	update(mid + 1, to, index * 2 + 1, target, diff);
}

int main() {
	int i, a, b, n, m, k;
	ll c;

	scanf("%d %d %d", &n, &m, &k);

	for (i = 0; i < n; i++) scanf(" %lld", arr + i);

	init(0, n - 1, 1);

	for (i = 0; i < m + k; i++) {
		scanf("%d %d %lld", &a, &b, &c);
		if (a == 1) {
			ll diff = c - arr[b - 1];
			arr[b - 1] = c;
			update(0, n - 1, 1, b - 1, diff);
		}
		else printf("%lld\n", sum(0, n - 1, 1, b - 1, c - 1));
	}

	return 0;
}