// https://codeforces.com/contest/1593/problem/D1

#define FAST_IO ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0)

#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int arr[41];

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int main() {
    int i, t;
    FAST_IO;

    cin >> t;

    for (i = 0; i < t; i++) {
        int j, n, minimum = 1000001;
        int answer = -1;
        cin >> n;
        for (j = 0; j < n; j++) {
            cin >> arr[j];
            minimum = min(minimum, arr[j]);
        }
        for (j = 0; j < n; j++) {
            int cha = arr[j] - minimum;
            if (cha != 0) answer = (answer == -1 ? cha : gcd(answer, cha));
        }

        cout << answer << '\n';

    }

    return 0;
}