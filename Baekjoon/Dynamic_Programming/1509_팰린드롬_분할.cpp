// https://www.acmicpc.net/problem/1509

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

enum{ NOT_VISITED = -1, FALSE, TRUE };
const int MAX = 2501;

string s;
int palindrome[MAX][MAX];
int dp[MAX];

int minimum(int a, int b) { return a == -1 ? b : min(a, b); }

int isPalindrome(int left, int right) {
	int& value = palindrome[left][right];

	if (value != NOT_VISITED) return value;
	if (left == right) return value = TRUE;
	if (s[left] != s[right]) return value = FALSE;
	if (left + 1 == right) return value = TRUE;

	return value = isPalindrome(left + 1, right - 1);
}

int solution(int idx) {
	int i;
	int& value = dp[idx];

	if (value != NOT_VISITED) return value;
	if (idx == s.length()) return value = 0;

	for (i = idx; i < s.length(); i++) if (isPalindrome(idx, i)) value = minimum(value, 1 + solution(i + 1));

	return value;
}

int main(void) {
	int i, j;

	cin >> s;

	for (i = 0; i < s.length(); i++) {
		dp[i] = NOT_VISITED;
		for (j = 0; j < s.length(); j++) palindrome[i][j] = NOT_VISITED;
	}

	cout << solution(0);

}