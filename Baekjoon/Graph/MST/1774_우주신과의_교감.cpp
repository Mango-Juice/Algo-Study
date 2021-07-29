# https://www.acmicpc.net/problem/1774

#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

// 간선 구조체
struct Edge {
	int from, to;
	double distance;
	bool operator < (Edge E) {
		return distance < E.distance;
	}
};

int arr[1001]; // Union-Find용 배열
pair<int, int> location[1001]; // 좌표 저장 배열
Edge edges[1000001]; // 간선 저장 배열

int find(int a) {
	if (arr[a] != a) arr[a] = find(arr[a]);
	return arr[a];
}

void un(int a, int b) {
	int ar = find(a);
	int br = find(b);
	arr[ar] = br;
}

int main(int argc, char** argv) {
	int n, m, a, b, i, j;
	int now = 0, count = 0;
	double answer = 0;

	scanf("%d %d", &n, &m);

	// 좌표 입력 및 arr 초기화
	for (i = 0; i < n; i++) {
		scanf("%d %d", &location[i].first, &location[i].second);
		arr[i] = i;
	}
	
	// 간선 만들기
	for (i = 0; i < n - 1; i++) {
		for (j = i + 1; j < n; j++) {
			edges[now].from = i;
			edges[now].to = j;
			long long dx =  ((long long) location[i].first - location[j].first) * ((long long) location[i].first - location[j].first);
			long long dy =  ((long long) location[i].second - location[j].second) * ((long long) location[i].second - location[j].second);
			edges[now++].distance = sqrt(dx + dy);
		}
	}

	sort(edges, edges + now);

	// 이미 연결되어 있으면 미리 union
	for (i = 0; i < m; i++) {
		scanf("%d %d", &a, &b);

		if (find(a - 1) != find(b - 1)) {
			un(a - 1, b - 1);
			count++;
		}
	}

	// 이미 다 연결되어 있으면 0.00
	if (count >= n - 1) {
		printf("0.00");
		return 0;
	}

	// 최소 신장 트리
	for (i = 0; i < now; i++) {
		if (find(edges[i].from) != find(edges[i].to)) { // 연결 안되어 있으면
			un(edges[i].from, edges[i].to);
			answer += edges[i].distance;
			if (++count >= n - 1) break;
		}
	}

	printf("%.2lf", round(answer * 100) / 100);

	return 0;
}