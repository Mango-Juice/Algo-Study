// https://www.acmicpc.net/problem/1697

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <queue>

using namespace std;

bool visited[100001] = { false };

int main() {
	int n, k, answer;
	FAST_IO;

	cin >> n >> k;

	queue<int> q;
	q.push(n);

	for (answer = 0; answer <= 100000; answer++) {
		queue<int> tmpq;
		int flag = false;

		while (!q.empty()) {
			int now = q.front();
			q.pop();

			if (visited[now]) continue;
			visited[now] = true;

			if (now == k) {
				flag = true;
				break;
			}

			if(now < 100000 && !visited[now + 1]) tmpq.push(now + 1);
			if(now > 0 && !visited[now - 1]) tmpq.push(now - 1);
			if(now > 0 && now <= 50000 && !visited[now * 2]) tmpq.push(2 * now);
		}

		if (flag) break;
		q = tmpq;
	}

	cout << answer;
	
	return 0;
}