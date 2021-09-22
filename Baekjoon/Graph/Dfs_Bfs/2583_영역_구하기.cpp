// https://www.acmicpc.net/problem/2583

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int dx[4] = { 0, 0, 1, -1 };
const int dy[4] = { 1, -1, 0, 0 };
bool visited[101][101] = { false };
vector<int> answer;
int M, N, K;

void dfs(int r, int c) {
    int i, nowx, nowy;

    for (i = 0; i < 4; i++) {
        nowx = r + dx[i];
        nowy = c + dy[i];

        if (nowx >= 0 && nowx < M && nowy >= 0 && nowy < N && !visited[nowx][nowy]) {
            visited[nowx][nowy] = true;
            answer[answer.size() - 1] ++;
            dfs(nowx, nowy);
        }
    }
}

int main() {
    int i, j, k, r1, c1, r2, c2;
    FAST_IO;

    cin >> M >> N >> K;
    for (i = 0; i < K; i++) {
        cin >> c1 >> r1 >> c2 >> r2;
        for (j = r1; j < r2; j++) for (k = c1; k < c2; k++) visited[j][k] = true;
    }
    
    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            if (visited[i][j]) continue;
            visited[i][j] = true;
            answer.push_back(1);
            dfs(i, j);

        }
    }

    sort(answer.begin(), answer.end());
    cout << answer.size() << '\n';
    for (i = 0; i < answer.size(); i++) cout << answer[i] << " ";

    return 0;
}