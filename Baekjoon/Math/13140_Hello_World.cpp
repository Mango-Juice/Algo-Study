// https://www.acmicpc.net/problem/13140

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>

using namespace std;

int n;

void checkAnswer(vector<int> &v) {
	int num1 = v[0] * 10000 + v[1] * 1000 + v[2] * 100 + v[2] * 10 + v[3];
	int num2 = v[4] * 10000 + v[3] * 1000 + v[5] * 100 + v[2] * 10 + v[6];

	if (num1 + num2 == n && v[0] > 0 && v[4] > 0) {
		cout << "  " << num1 << '\n';
		cout << "+ " << num2 << '\n';
		cout << "-------" << '\n';
		cout << (n >= 100000 ? " " : "  ") << n;
		exit(0);
	}
}

void solution(vector<int> &v, int used) {
	for (int i = 0; i < 10; i++) {
		if (used & (1 << i)) continue;

		vector<int> newv;
		newv.resize(v.size());
		copy(v.begin(), v.end(), newv.begin());

		newv.push_back(i);
		if (newv.size() >= 7) checkAnswer(newv);
		else solution(newv, used | (1 << i));

	}
}

int main() {
	FAST_IO;
	vector<int> v;

	cin >> n;

	if (n >= 200000) cout << "No Answer";
	else {
		solution(v, 0);
		cout << "No Answer";
	}

	return 0;
}