// https://codeforces.com/contest/1593/problem/A

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int i, t;
    FAST_IO;

    cin >> t;

    for (i = 0; i < t; i++) {
        int a, b, c, maximum;
        cin >> a >> b >> c;
        maximum = max(max(a, b), c);
        a = maximum - a, b = maximum - b, c = maximum - c;
        if (a == 0 && b != 0 && c != 0) a = -1;
        else if (a != 0 && b == 0 && c != 0) b = -1;
        else if (a != 0 && b != 0 && c == 0) c = -1;
        cout << a + 1 << ' ' << b + 1 << ' ' << c + 1 << '\n';
    }

    return 0;
}