// https://www.acmicpc.net/problem/2887

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

struct edge {
	int from, to, weight;
};

int uf[100000] = { 0, };
vector<vector<int>> jwa;
vector<edge> edges;
int cnt = 0;
int answer = 0;

bool cmpe(edge a, edge b) {
	return a.weight < b.weight;
}

bool cmpx(vector<int> a, vector<int> b) {
	return a[1] < b[1];
}

bool cmpy(vector<int> a, vector<int> b) {
	return a[2] < b[2];
}

bool cmpz(vector<int> a, vector<int> b) {
	return a[3] < b[3];
}

int getDistance(vector<int> a, vector<int> b) {
	return min(min(abs(a[1] - b[1]), abs(a[2] - b[2])), abs(a[3] - b[3]));
}

int Find(int target) {
	if (uf[target] != target) uf[target] = Find(uf[target]);
	return uf[target];
}

void Union(edge target){
	int a = Find(target.from);
	int b = Find(target.to);
	if (a != b) {
		uf[a] = b;
		cnt++;
		answer += target.weight;
	}
}

int main(int argc, char** argv) {
	int i, n, a, b, c;
	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		vector<int> tmp;
		scanf("%d %d %d", &a, &b, &c);
		uf[i] = i;
		tmp.push_back(i);
		tmp.push_back(a);
		tmp.push_back(b);
		tmp.push_back(c);
		jwa.push_back(tmp);
	}

	sort(jwa.begin(), jwa.end(), cmpx);
	for (i = 0; i < jwa.size() - 1; i++) {
		edge e;
		e.from = jwa[i][0];
		e.to = jwa[i + 1][0];
		e.weight = getDistance(jwa[i], jwa[i + 1]);
		edges.push_back(e);
	}

	sort(jwa.begin(), jwa.end(), cmpy);
	for (i = 0; i < jwa.size() - 1; i++) {
		edge e;
		e.from = jwa[i][0];
		e.to = jwa[i + 1][0];
		e.weight = getDistance(jwa[i], jwa[i + 1]);
		edges.push_back(e);
	}

	sort(jwa.begin(), jwa.end(), cmpz);
	for (i = 0; i < jwa.size() - 1; i++) {
		edge e;
		e.from = jwa[i][0];
		e.to = jwa[i + 1][0];
		e.weight = getDistance(jwa[i], jwa[i + 1]);
		edges.push_back(e);
	}

	sort(edges.begin(), edges.end(), cmpe);

	for (i = 0; i < edges.size(); i++) {
		Union(edges[i]);
		if (cnt == n) break;
	}
	
	printf("%d", answer);

	return 0;
}