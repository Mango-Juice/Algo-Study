// https://www.acmicpc.net/problem/2187

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int r[1001], c[1001], s[1001];

int main() {
    int i, j;
    int N, A, B;
    int answer = 0;
    FAST_IO;

    cin >> N >> A >> B;
    for (i = 0; i < N; i++) {
        cin >> r[i] >> c[i] >> s[i];
        for (j = 0; j < i; j++) if (abs(r[i] - r[j]) < A && abs(c[i] - c[j]) < B) answer = max(answer, abs(s[i] - s[j]));
    }

    cout << answer;

    return 0;
}