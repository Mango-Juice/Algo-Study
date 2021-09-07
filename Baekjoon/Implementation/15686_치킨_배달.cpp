// https://www.acmicpc.net/problem/15686

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;

vector<pair<int, int>> chickens;
vector<pair<int, int>> houses;
int answer = INT_MAX;
int n, m;

void getAnswer(vector<int> selected) {
	int result = 0;
	int i, j;

	for (i = 0; i < houses.size(); i++) {
		int tmp = INT_MAX;

		for (j = 0; j < selected.size(); j++)
			tmp = min(tmp, abs(houses[i].first - chickens[selected[j]].first) + abs(houses[i].second - chickens[selected[j]].second));

		result += tmp;
	}
	
	answer = min(answer, result);
}

void solution(vector<int> selected, int idx) {
	if (idx < chickens.size() - 1) solution(selected, idx + 1);

	selected.push_back(idx);
	if (selected.size() == m) getAnswer(selected);
	else if (idx < chickens.size() - 1) solution(selected, idx + 1);
}

int main() {
	FAST_IO;
	int i, j, tmp;

	cin >> n >> m;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			cin >> tmp;
			if (tmp == 1) houses.push_back(pair<int, int>(i, j));
			if (tmp == 2) chickens.push_back(pair<int, int>(i, j));
		}
	}

	solution(vector<int>(), 0);
	cout << answer;

	return 0;
}