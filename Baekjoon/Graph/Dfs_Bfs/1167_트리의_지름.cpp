// https://www.acmicpc.net/problem/1167

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;
vector<pair<int, int>> arr[100001];
bool visited[100001] = { false };
int dist[100001];

void dfs(int now, int cost) {
	pair<int, int> target;

	visited[now] = true;
	dist[now] = cost;

	for (int i = 0; i < arr[now].size(); i++) {
		target = arr[now][i];
		if (visited[target.first]) continue;
		dfs(target.first, cost + target.second);
	}
}

int main() {
	int i, v, num, to, weight, maxv = -1, maxi = 0;

	scanf("%d", &v);
	for (i = 0; i < v; i++) {
		scanf(" %d", &num);
		while (true) {
			scanf(" %d", &to);
			if (to == -1) break;
			scanf(" %d", &weight);
			arr[num].push_back(pair<int, int>(to, weight));
		}
	}

	dfs(1, 0);

	for (i = 1; i <= v; i++) {
		if (maxv <= dist[i]) {
			maxv = dist[i];
			maxi = i;
		}
	}

	memset(visited, false, v + 1);

	dfs(maxi, 0);

	for (i = 1; i <= v; i++) if (maxv <= dist[i]) maxv = dist[i];

	printf("%d", maxv);

	return 0;
}