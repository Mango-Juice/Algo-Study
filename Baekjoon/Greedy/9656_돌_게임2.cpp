// https://www.acmicpc.net/problem/9656

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int main() {
	int n;
	FAST_IO;

	cin >> n;

	if (n & 1) cout << "CY";
	else cout << "SK";

	return 0;
}