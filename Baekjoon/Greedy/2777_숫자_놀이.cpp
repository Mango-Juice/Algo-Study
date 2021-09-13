// https://www.acmicpc.net/problem/2777

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

typedef long long ll;

int solution(ll number, int count) {
	if (number == 1) return count;

	for (ll i = 9; i >= 2; i--) {
		if (number % i == 0) {
			if (number == i) return count;
			return solution(number / i, count + 1);
		}
	}

	return -1;
}

int main() {
	ll n;
	int i, t;
	FAST_IO;

	cin >> t;

	for (i = 0; i < t; i++) {
		cin >> n;
		cout << solution(n, 1) << '\n';
	}

	return 0;
}