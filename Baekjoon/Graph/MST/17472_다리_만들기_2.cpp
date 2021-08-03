// https://www.acmicpc.net/problem/17472

#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int dx[4] = { -1, 1, 0, 0 };
const int dy[4] = { 0, 0, -1, 1 };

struct edge {
	int node1, node2, weight;

	edge(int a, int b, int c) : node1(a), node2(b), weight(c) {}

	bool operator < (const edge& cmp) const {
		return weight < cmp.weight;
	}
};

int uf[7] = { 0 };
int arr[10][10] = { 0 };
int inp[10][10] = { 0 };
bool visited[10][10] = { false };
int island_count = 0;
int n, m;
vector<pair<int, int>> islands[7];
vector<edge> bridges;

int FIND(int a) {
	if (uf[a] == 0) return a;
	return uf[a] = FIND(uf[a]);
}

void UNION(int a, int b) {
	a = FIND(a);
	b = FIND(b);
	uf[a] = b;
}

bool allConnected() {
	for (int i = 2; i <= island_count; i++) if (FIND(i) != FIND(1)) return false;
	return true;
}

void makeMap(int x, int y, int cnt) {
	int i;

	if (x < 0 || x >= n || y < 0 || y >= m) return;
	if (inp[x][y] == 0 || visited[x][y]) return;

	visited[x][y] = true;
	arr[x][y] = cnt;
	islands[cnt].push_back(pair<int, int>(x, y));

	for (i = 0; i < 4; i++) makeMap(x + dx[i], y + dy[i], cnt);
}

int getDistance(int is1, int is2) {
	int i, j, x, y;
	int res = 10;

	 for (i = 0; i < islands[is1].size(); i++) {
		x = islands[is1][i].first; y = islands[is1][i].second;

		for (j = 0; j < 4; j++) {
			int newx = x + dx[j], newy = y + dy[j], d = 0;

			while (true) {
				if (newx < 0 || newx >= n || newy < 0 || newy >= m) break;
				if (arr[newx][newy] == is1) break;

				if (arr[newx][newy] == 0) {
					d++;
					newx += dx[j];
					newy += dy[j];
				}
				else {
					if (arr[newx][newy] == is2 && d > 1) res = min(res, d);
					break;
				}
			}
		}
	}

	return res;
}

int main() {
	int tmp, i, j;
	int answer = 0;
	scanf("%d %d", &n, &m);

	for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf(" %d", &inp[i][j]);

	for (i = 0; i < n; i++) for (j = 0; j < m; j++) if(!visited[i][j] && inp[i][j] == 1) makeMap(i, j, ++island_count);

	for (i = 1; i < island_count; i++) {
		for (j = i + 1; j <= island_count; j++) {
			tmp = getDistance(i, j);
			if(tmp < 10) bridges.push_back(edge(i, j, tmp));
		}
	}
	sort(bridges.begin(), bridges.end());

	for (i = 0; i < bridges.size(); i++) {
		edge bridge = bridges[i];

		if (FIND(bridge.node1) != FIND(bridge.node2)) {
			UNION(bridge.node1, bridge.node2);
			answer += bridge.weight;
		}

		if (allConnected()) break;
	}

	printf("%d", allConnected() ? answer : -1);
	return 0;
}