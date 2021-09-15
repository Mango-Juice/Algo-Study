// https://www.acmicpc.net/problem/2110

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int arr[200001];
int n;

int countHouse(int m) {
	int count = 1;
	int last = arr[0];

	for (int i = 1; i < n; i++) {
		int cha = arr[i] - last;
		if (cha >= m) {
			last = arr[i];
			count++;
		}
	}

	return count;
}

int main() {
	int i, c;
	FAST_IO;

	cin >> n >> c;
	for (i = 0; i < n; i++) cin >> arr[i];
	sort(arr, arr + n);

	int left = 1, right = arr[n - 1] - arr[0], answer;

	while (left <= right) {
		int mid = (right - left) / 2 + left;
		int cnt = countHouse(mid);

		if (cnt >= c) {
			answer = mid;
			left = mid + 1;
		}
		else right = mid - 1;
	}

	cout << answer;
	return 0;
}