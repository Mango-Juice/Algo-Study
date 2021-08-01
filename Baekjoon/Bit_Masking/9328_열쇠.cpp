// https://www.acmicpc.net/problem/9328

#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

enum type {
	WALL = -3,
	DOCUMENT,
	KEY,
	EMPTY,
	DOOR
};

int arr[100][100] = { 0 };
bool visited[100][100] = { false };
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int i, j, k, t, h, w, target;
	int key = 0, answer = 0;
	char tmp;
	string inp_keys;
	queue<pair<int, int>> q;

	cin >> t; // TextCase 수 입력

	for (i = 0; i < t; i++) {
		key = 0;
		answer = 0;
		q = queue<pair<int, int>>();

		cin >> h >> w; // 높이, 너비 입력

		for (j = 0; j < h; j++) for (k = 0; k < w; k++) visited[j][k] = false;

		// 빌딩 구조 입력
		for (j = 0; j < h; j++) { 
			for (k = 0; k < w; k++) {
				cin >> tmp;
				if (tmp == '.') arr[j][k] = EMPTY;
				else if (tmp == '*') arr[j][k] = WALL;
				else if (tmp == '$') arr[j][k] = DOCUMENT;
				else if (tmp < 'a') arr[j][k] = (1 << ((int)tmp - 'A')) * DOOR;
				else arr[j][k] = (1 << ((int)tmp - 'a')) * KEY - 3;
			}
		}

		// 현재 소지 열쇠 입력
		cin >> inp_keys; 
		for (j = 0; j < inp_keys.length(); j++) {
			if (inp_keys[j] == '0') break;
			target = 1 << ((int)inp_keys[j] - 'a');
			if ((target & key) != target) key += target;
		}

		bool re = true;

		while (re) {
			re = false;
			// 입구부터 찾자!
			for (j = 0; j < h; j++) {
				q.push(pair<int, int>(j, 0));
				q.push(pair<int, int>(j, w - 1));
			}
			for (j = 1; j < w - 1; j++) {
				q.push(pair<int, int>(0, j));
				q.push(pair<int, int>(h - 1, j));
			}

			// BFS
			while (!q.empty()) {
				// 큐에서 하나 뽑기
				bool flag = true;
				pair<int, int> top = q.front();
				q.pop();

				// 좌표 범위 판정 및 방문 판정
				if (top.first < 0 || top.first >= h || top.second < 0 || top.second >= w || visited[top.first][top.second]) continue;

				visited[top.first][top.second] = true; // 방문 기록

				// 이동 가능성 판정
				if (arr[top.first][top.second] == WALL) flag = false;
				else {
					if (arr[top.first][top.second] == DOCUMENT) answer++;
					else if (arr[top.first][top.second] < WALL) {
						target = -1 * (arr[top.first][top.second] + 3);
						if ((target & key) != target) {
							key += target;
							re = true;
							answer = 0;
							for (j = 0; j < h; j++) for (k = 0; k < w; k++) visited[j][k] = false;
							q = queue<pair<int, int>>();
							break;
						}
					}
					else if (arr[top.first][top.second] > EMPTY && (arr[top.first][top.second] & key) != arr[top.first][top.second]) flag = false;
				}

				// 다음으로 이동
				if (flag) for (j = 0; j < 4; j++) q.push(pair<int, int>(top.first + dx[j], top.second + dy[j]));
			}
		}

		std::cout << answer << '\n';
	}
	return 0;
}