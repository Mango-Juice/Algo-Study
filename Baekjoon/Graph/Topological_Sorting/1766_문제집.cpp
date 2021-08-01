// https://www.acmicpc.net/problem/1766

#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int indegree[32001] = { 0 };
vector<int> parent[32001];
vector<int> answer;
priority_queue<int, vector<int>, greater<int>> heap;

int main() {
	int i, n, m, from, to;

	scanf("%d %d", &n, &m);

	for (i = 0; i < m; i++) {
		scanf("%d %d", &from, &to);
		indegree[to]++;
		parent[from].push_back(to);
	}

	for (i = 1; i <= n; i++) if (indegree[i] == 0) heap.push(i);

	while (!heap.empty()) {
		int target = heap.top();
		heap.pop();
		answer.push_back(target);
		for (i = 0; i < parent[target].size(); i++) {
			indegree[parent[target][i]] --;
			if (indegree[parent[target][i]] == 0) heap.push(parent[target][i]);
		}
	}

	for (i = 0; i < n; i++) printf("%d ", answer[i]);

	return 0;
}