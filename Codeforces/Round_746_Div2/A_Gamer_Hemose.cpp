// https://codeforces.com/contest/1592/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>

using namespace std;

int main() {
    int i, j, tmp, t;
    FAST_IO;

    cin >> t;
    for (i = 0; i < t; i++) {
        int n, H;
        int w1 = 0, w2 = 0;
        bool flag = true;
        cin >> n >> H;

        for (j = 0; j < n; j++) {
            cin >> tmp;
            if (tmp >= w1) {
                w2 = w1;
                w1 = tmp;
            }
            else if (tmp > w2) w2 = tmp;
        }

        int cycle = (H / (w1 + w2)) * 2;
        int mod = H % (w1 + w2);
        if (mod > 0) cycle += (mod <= w1 ? 1 : 2);

        cout << cycle << '\n';
    }

    return 0;
}