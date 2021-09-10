// https://www.acmicpc.net/problem/17610

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <cmath>

using namespace std;

int k, maximum = 0, answer = 0;
int g[14];
bool visited[2600000] = { false };

void solution(int now, int idx) {
	int tmp;

	// 더하기
	tmp = now + g[idx];
	visited[tmp] = true;
	if (idx < k - 1) solution(tmp, idx + 1);

	// 빼기
	tmp = abs(now - g[idx]);
	visited[tmp] = true;
	if (idx < k - 1) solution(tmp, idx + 1);

	// 안씀
	visited[now] = true;
	if(idx < k - 1) solution(now, idx + 1);
}

int main() {
	int i;
	FAST_IO;

	cin >> k;

	for (i = 0; i < k; i++) {
		cin >> g[i];
		maximum += g[i];
	}

	solution(0, 0);
	
	for (i = 1; i < maximum; i++) answer += (int)!visited[i];

	cout << answer;
	return 0;
}