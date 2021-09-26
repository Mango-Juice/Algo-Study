// https://www.acmicpc.net/problem/1600

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

const int dr[4] = { 0, 0, -1, 1 };
const int dc[4] = { -1, 1, 0, 0 };
const int hr[8] = { -2, -1, 1, 2, 2, 1, -1, 2 };
const int hc[8] = { 1, 2, 2, 1, -1, -2, -2, -1 };

int K, W, H;
bool map[201][201][32] = { false };

int main() {
    queue<tuple<int, int, int, int>> q;
    int i, j, k, nowr, nowc, answer = -1;
    bool tmp, flag = false;
    FAST_IO;

    cin >> K;
    cin >> W >> H;

    for (i = 0; i < H; i++) {
        for (j = 0; j < W; j++) {
            cin >> tmp;
            for (k = 0; k <= K; k++) map[i][j][k] = tmp;
        }
    }

    if (W == 1 && H == 1 && map[0][0][0] == 0) {
        cout << 0;
        return 0;
    }

    q.push(tuple<int, int, int, int>(0, 0, K, 0));
    map[0][0][0] = true;

    while (!q.empty()) {
        tuple<int, int, int, int> t = q.front();
        q.pop();

        for (i = 0; i < 4; i++) {
            nowr = get<0>(t) + dr[i], nowc = get<1>(t) + dc[i];
            if (nowr == H - 1 && nowc == W - 1) {
                answer =  get<3>(t) + 1;
                flag = true;
                break;
            }
            if (nowr >= 0 && nowr < H && nowc >= 0 && nowc < W && !map[nowr][nowc][get<2>(t)]) {
                map[nowr][nowc][get<2>(t)] = true;
                q.push(tuple<int, int, int, int>(nowr, nowc, get<2>(t), get<3>(t) + 1));
            }
        }

        if (flag) break;
        if (get<2>(t) <= 0) continue;

        for (i = 0; i < 8; i++) {
            nowr = get<0>(t) + hr[i], nowc = get<1>(t) + hc[i];
            if (nowr == H - 1 && nowc == W - 1) {
                answer = get<3>(t) + 1;
                flag = true;
                break;
            }
            if (nowr >= 0 && nowr < H && nowc >= 0 && nowc < W && !map[nowr][nowc][get<2>(t) - 1]) {
                map[nowr][nowc][get<2>(t) - 1] = true;
                q.push(tuple<int, int, int, int>(nowr, nowc, get<2>(t) - 1, get<3>(t) + 1));
            }
        }

        if (flag) break;
    }

    cout << answer;

    return 0;
}