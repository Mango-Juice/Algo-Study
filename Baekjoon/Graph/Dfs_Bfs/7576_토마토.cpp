// https://www.acmicpc.net/problem/7576

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

const int dr[] = { 0, 0, -1, 1 };
const int dc[] = { -1, 1, 0, 0 };
bool visited[1001][1001] = { false };

int main() {
    queue<pair<int, int>> q;
    int i, j, k, tmp, c, r, count = 0;
    FAST_IO;

    cin >> c >> r;

    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            cin >> tmp;
            if (tmp == 1) {
                visited[i][j] = true;
                q.push(make_pair(i, j));
                count++;
            }
            else {
                visited[i][j] = -tmp;
                count += -tmp;
            }
        }
    }

    for (i = 0; i <= 1000000 && !q.empty(); i++) {
        if (count == r * c) {
            cout << i;
            return 0;
        }

        int limit = q.size();
        for (j = 0; j < limit; j++) {
            pair<int, int> rc = q.front();
            q.pop();
            for (k = 0; k < 4; k++) {
                int nr = rc.first + dr[k], nc = rc.second + dc[k];
                if (nr >= 0 && nr < r && nc >= 0 && nc < c && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    count++;
                    q.push(make_pair(nr, nc));
                }
            }
        }
    }

    cout << -1;
    return 0;
}