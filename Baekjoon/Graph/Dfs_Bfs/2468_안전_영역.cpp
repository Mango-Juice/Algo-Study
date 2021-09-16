// https://www.acmicpc.net/problem/2468

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

const int dx[4] = { -1, 1, 0, 0 };
const int dy[4] = { 0, 0, -1, 1 };

int arr[101][101];
int n;

int solution(int height) {
	bool visited[101][101] = { false };
	int i, j, k, result = 0;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (arr[i][j] <= height || visited[i][j]) continue;

			result++;
			visited[i][j] = true;
			queue<pair<int, int>> q;
			q.push(pair<int, int>(i, j));

			while (!q.empty()) {
				pair<int, int> target = q.front();
				q.pop();

				for (k = 0; k < 4; k++) {
					int newx = target.first + dx[k], newy = target.second + dy[k];
					if (newx >= 0 && newx < n && newy >= 0 && newy < n && !visited[newx][newy] && arr[newx][newy] > height) {
						visited[newx][newy] = true;
						q.push(pair<int, int>(newx, newy));
					}
				}
			}
		}
	}

	return result;
}

int main() {
	int i, j, val;
	int answer = 1;
	FAST_IO;

	cin >> n;

	for (i = 0; i < n; i++) for (j = 0; j < n; j++) cin >> arr[i][j];

	for (i = 1; i < 100; i++) {
		val = solution(i);
		if (val == 0) break;
		answer = max(answer, val);
	}

	cout << answer;

	return 0;
}