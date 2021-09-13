// https://www.acmicpc.net/problem/2812

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	int i, n, k;
	string s;
	stack<char> stk, answer;
	FAST_IO;

	cin >> n >> k;
	cin >> s;

	for (i = 0; i < n; i++) {
		while (k > 0 && !stk.empty() && stk.top() < s[i]) {
			stk.pop();
			k--;
		}
		stk.push(s[i]);
	}

	while (!stk.empty()) {
		if (k > 0) k--;
		else answer.push(stk.top());
		stk.pop();
	}
	
	while (!answer.empty()) {
		cout << answer.top();
		answer.pop();
	}

	return 0;
}