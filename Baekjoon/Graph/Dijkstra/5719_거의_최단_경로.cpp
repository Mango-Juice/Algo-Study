// https://www.acmicpc.net/problem/5719

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

vector<pair<int, int>> tree[500];
vector<int> parents[500];
int dist[500];
bool visited[500][500] = { false };
bool banned[500][500] = { false };

void dfs(pair<int, int> p, int from) {
	if (p.second == from) return;

	for (int i = 0; i < parents[p.second].size(); i++) {
		if (visited[parents[p.second][i]][p.second]) continue;
		visited[parents[p.second][i]][p.second] = true;
		banned[parents[p.second][i]][p.second] = true;
		dfs(pair<int, int>(p.second, parents[p.second][i]), from);
	}
}

int main(void) {
	int i, j, n, m, from, to, u, v, p, result;
	pair<int, int> data, target;

	while (true) {
		// 입력
		scanf(" %d %d", &n, &m);

		if (n == 0 && m == 0) break;

		scanf(" %d %d", &from, &to);

		// 변수 초기화
		memset(banned, false, sizeof(banned[0][0]) * 500 * 500);
		memset(visited, false, sizeof(banned[0][0]) * 500 * 500);
		for (i = 0; i < n; i++) {
			tree[i].clear();
			dist[i] = -1;
		}

		// 간선 등록
		for (i = 0; i < m; i++) {
			scanf(" %d %d %d", &u, &v, &p);
			tree[u].push_back(pair<int, int>(p, v));
		}

		// 순방향 위상 졍렬
		dist[from] = 0;
		priority_queue < pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> q;
		q.push(pair<int, int>(0, from));

		while (!q.empty()) {
			data = q.top();
			q.pop();

			if (dist[data.second] > -1 && dist[data.second] < data.first) continue;

			for (j = 0; j < tree[data.second].size(); j++) {
				target = tree[data.second][j];

				if (dist[target.second] == -1 || dist[target.second] > dist[data.second] + target.first) {
					dist[target.second] = dist[data.second] + target.first;
					q.push(pair<int, int>(dist[target.second], target.second));
					parents[target.second].clear();
					parents[target.second].push_back(data.second);
				} else if(dist[target.second] == dist[data.second] + target.first) parents[target.second].push_back(data.second);
			}
		}

		result = dist[to];

		// 예외 처리
		if (result == -1) {
			printf("-1\n");
			continue;
		}

		// 역추적
		dfs(pair<int, int>(-5, to), from);

		// dist 초기화
		memset(dist, -1, sizeof(dist[0]) * 500);

		// 다시 위상정렬
		dist[from] = 0;
		q.push(pair<int, int>(0, from));

		while (!q.empty()) {
			data = q.top();
			q.pop();

			if (dist[data.second] > -1 && dist[data.second] < data.first) continue;

			for (j = 0; j < tree[data.second].size(); j++) {
				target = tree[data.second][j];

				if (!banned[data.second][target.second] && (dist[target.second] == -1 || dist[target.second] > dist[data.second] + target.first)) {
					dist[target.second] = dist[data.second] + target.first;
					q.push(pair<int, int>(dist[target.second], target.second));
				}
			}
		}

		result = dist[to];

		// 출력
		printf("%d\n", result);
	}
}