// https://www.acmicpc.net/problem/11578

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int people[12] = { 0 };
int N, M, answer = -1;

void solution(int idx, int status, int count) {
    if (status == (1 << N + 1) - 2) {
        answer = answer > -1 ? min(answer, count) : count;
        return;
    }
    if (idx > M) return;

    solution(idx + 1, status, count);
    solution(idx + 1, status | people[idx], count + 1);
}

int main() {
    int i, j, tmp, O;
    FAST_IO;

    cin >> N >> M;

    for (i = 1; i <= M; i++){
        cin >> O;

        for (j = 1; j <= O; j++) {
            cin >> tmp;
            people[i] |= (1 << tmp);
        }
    }

    solution(1, 0, 0);

    cout << answer;

    return 0;
}