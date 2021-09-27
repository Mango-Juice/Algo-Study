// https://www.acmicpc.net/problem/1082

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <vector>

using namespace std;

int P[11];
vector<int> answer;

int main() {
    int cidx = -1, cval = 50;
    int i, N, M;
    FAST_IO;

    cin >> N;
    for (i = 0; i < N; i++) {
        cin >> P[i];
        if (i > 0 && cval >= P[i]) {
            cidx = i;
            cval = P[i];
        }
    }
    cin >> M;

    int money = M;
    answer.push_back(cidx);
    money -= cval;

    if (money < 0) {
        cout << 0;
        return 0;
    }

    if (cval > P[0]) {
        cidx = 0;
        cval = P[0];
    }

    while (money >= cval) {
        answer.push_back(cidx);
        money -= cval;
    }

    int idx = 0;
    while (idx < answer.size() && money > 0) {
        bool flag = false;

        for (i = N - 1; i > cidx; i--) {
            if (money >= P[i] - P[answer[idx]]) {
                money -= P[i] - P[answer[idx]];
                answer[idx] = i;
                flag = true;
                break;
            }
        }

        if (!flag) break;
        idx++;
    }

    for (i = 0; i < answer.size(); i++) cout << answer[i];

    return 0;
}