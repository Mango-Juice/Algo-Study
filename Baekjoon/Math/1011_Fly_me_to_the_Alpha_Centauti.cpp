// https://www.acmicpc.net/problem/1011

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;
const int MAX = 46341;
int cnts[MAX + 1];

int main() {
    int t, i;
    int x, y, cnt;
    FAST_IO;

    for (i = 1; i <= MAX; i++) cnts[i] = 2 * i - 1;

    cin >> t;

    for (i = 0; i < t; i++) {
        cin >> x >> y;
        cnt = y - x;

        ll sq = sqrt(cnt);
        ll left = sq * sq;

        if (left == cnt || sq == MAX) { // 숫자가 제곱수일 때
            cout << cnts[sq] << '\n';
            continue;
        }

        ll right = (sq + 1) * (sq + 1);
        if(cnt - left > right - cnt) cout << cnts[sq + 1] << '\n'; // 더 큰 제곱수와 숫자가 가까울 때
        else cout << cnts[sq] + 1 << '\n'; // 더 작은 제곱수와 숫자가 가까울 때
    }

    return 0;
}