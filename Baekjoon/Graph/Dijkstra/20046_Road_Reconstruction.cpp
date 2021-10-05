// https://www.acmicpc.net/problem/20046

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

const int dr[4] = { -1, 1, 0, 0 };
const int dc[4] = { 0, 0, -1, 1 };
const int MAX = 2000001;
const int BLOCK = -1;

int map[1001][1001];
int answer[1001][1001];

int main() {
    int i, j, n, m;
    FAST_IO;

    cin >> n >> m;

    for (i = 0; i < n; i++) for (j = 0; j < m; j++) cin >> map[i][j];

    if (map[0][0] == BLOCK || map[n - 1][m - 1] == BLOCK) { // 시작, 끝 점이 막혀있을 때
        cout << -1;
        return 0;
    }

    for (i = 0; i < n; i++) fill_n(answer[i], m, MAX);

    // 다익스트라
    priority_queue < tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q;
    q.push(tuple<int, int, int>(map[0][0], 0, 0));

    while (!q.empty()) {
        int r = get<1>(q.top()), c = get<2>(q.top()), v = get<0>(q.top());
        q.pop();

        if (answer[r][c] <= v) continue;
        answer[r][c] = v;
        if (r == n - 1 && c == m - 1) break;

        for (i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                int nv = v + map[nr][nc];
                if (nv < answer[nr][nc] && map[nr][nc] != BLOCK) q.push(tuple<int, int, int>(nv, nr, nc)); // 갱신 가능하고, 도로 설치가 가능할 때만 push
            }
        }
    }

    cout << (answer[n - 1][m - 1] < MAX ? answer[n - 1][m - 1] : -1);

    return 0;
}