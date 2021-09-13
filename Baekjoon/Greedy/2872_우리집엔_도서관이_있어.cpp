// https://www.acmicpc.net/problem/2872

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int arr[300001];

int main() {
	int i, n;
	FAST_IO;

	cin >> n;

	for (i = 0; i < n; i++) cin >> arr[i];

	// 움직일 필요가 없는 부분 탐색
	int now = n;
	for (i = n - 1; i >= 0; i--)
		if (arr[i] == now) now--;

	cout << now;

	return 0;
}