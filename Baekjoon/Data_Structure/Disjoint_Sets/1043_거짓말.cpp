// https://www.acmicpc.net/problem/1043

#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int arr[51];
vector<int> truth;
vector<vector<int>> party;

int find(int a) {
	if (arr[a] != a) arr[a] = find(arr[a]);
	return arr[a];
}

void un(int a, int b) {
	int ar = find(a);
	int br = find(b);
	if (ar != br) arr[ar] = br;
}

int main(int argc, char** argv) {
	int i, j, n, m, know, people, tmp, last;
	bool flag;
	int answer = 0;

	scanf("%d %d", &n, &m);	

	for (i = 1; i <= n; i++) arr[i] = i;

	scanf("%d", &know);

	for (i = 0; i < know; i++) {
		scanf(" %d", &tmp);
		truth.push_back(tmp);
	}

	for (i = 0; i < m; i++) {
		vector<int> now;
		last = -1;

		scanf("%d", &people);

		for (j = 0; j < people; j++) {
			scanf(" %d", &tmp);
			if (last > -1) un(last, tmp);
			now.push_back(tmp);
			last = tmp;
		}
		party.push_back(now);
	}
	
	while (!party.empty()) {
		vector<int> now = party.back();
		flag = true;
		party.pop_back();

		for (i = 0; i < now.size(); i++) {
			for (j = 0; j < truth.size(); j++) {
				if (find(now[i]) == find(truth[j])) {
					flag = false;
					break;
				}
			}
			if (!flag) break;
		}
		if (flag) answer++;
	}

	printf("%d", answer);
	return 0;
}